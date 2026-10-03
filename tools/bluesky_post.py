"""新文章上線時，在 Bluesky 的 @news.anoni.net 發一則貼文。規則見 SPEC.md「Bluesky」。

    uv run tools/bluesky_post.py --dry-run                              # 列出這一輪會發的貼文，不登入也不發文
    uv run tools/bluesky_post.py --dry-run --now 2026-10-05T07:10:00+08:00  # 預覽某個時間點會發什麼
    BLUESKY_APP_PASSWORD=<app password> uv run tools/bluesky_post.py    # 實際發文，deploy workflow 用

只處理已經發布、發布時間在 24 小時內的文章，zh-TW 與 en 各一則。帳號上已經有同一篇文章的貼文就略過，
帳號自己的貼文紀錄就是狀態，repo 裡不另存。發文前確認 clearnet 的文章網址回應 200，還沒上線就跳過，
下一輪重建時再試。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

# 發文的語系與貼文的 langs。zh-CN 不發，bsky.app 在中國大陸被封鎖
LANG_TAGS = {"zh-TW": "zh", "en": "en"}
# 只發這段時間內發布的文章，剛開始自動發文時不會把過去的文章一次補發
WINDOW = timedelta(hours=24)
# Bluesky 一則貼文的上限是 300 個字元（grapheme）。中文一個字就是一個，用字元數算不會超過
MAX_TEXT = 300
UTM = "utm_source=bluesky&utm_medium=social"
# 等文章上線：m6 每 5 分鐘拉一次，Cloudflare 快取 5 分鐘
LIVE_WAIT = timedelta(minutes=15)
LIVE_INTERVAL = 30
USER_AGENT = "anoni-net-news-bluesky/1 (+https://anoni.net/news/)"
IMAGE_TYPES = {".png": "image/png", ".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


@dataclass
class Item:
    """這一輪要發（或已經發過）的一則貼文。"""
    post: build.Post
    tag: str
    url: str          # 文章的 clearnet 網址，不帶 query，用來比對是否發過
    text: str
    thumb: str        # 預覽圖：static/ 底下的檔名，或 assets.anoni.net 的網址
    quote_url: str | None  # follows 的前一篇在同語系的網址，找得到它的貼文就引用轉貼

    @property
    def link(self) -> str:
        return f"{self.url}?{UTM}"


def post_text(title: str, description: str) -> str:
    """標題，空一行接 description。放不下時只放標題。"""
    text = f"{title}\n\n{description}"
    return text if len(text) <= MAX_TEXT else title[:MAX_TEXT]


def plan(posts: list[build.Post], base_url: str, now: datetime) -> list[Item]:
    """這一輪該發的貼文，由舊到新排，前一篇先發，後續稿才找得到它的貼文。posts 是 zh-TW 的文章。"""
    items = []
    cards = build.load_cards()
    by_stem = {post.path.stem: post for post in posts}
    for post in sorted(posts, key=lambda p: (p.created, p.slug)):
        if post.created > now or now - post.created > WINDOW:
            continue
        for code, tag in LANG_TAGS.items():
            version = post.translations.get(code, post)
            earlier = by_stem.get(post.follows[0]) if post.follows else None
            quote_url = base_url + earlier.translations.get(code, earlier).rel if earlier else None
            items.append(Item(
                post=version,
                tag=tag,
                url=base_url + version.rel,
                text=post_text(version.title, version.description),
                # 預覽圖跟頁面的 og:image 相同：指定的 image、這篇的預覽卡片，都沒有時用全站的預覽圖
                thumb=version.image or build.card_url(build.post_card(version), version.lang, cards) or version.lang.og_image,
                quote_url=quote_url,
            ))
    return items


def strip_query(url: str) -> str:
    return url.split("?", 1)[0].split("#", 1)[0]


def posted_links(records: list[dict]) -> dict[str, dict]:
    """帳號上每則貼文的連結卡片網址（不含 query）對應到貼文的 uri 與 cid。"""
    links = {}
    for record in records:
        embed = record.get("value", {}).get("embed") or {}
        external = embed.get("external") or (embed.get("media") or {}).get("external") or {}
        if external.get("uri"):
            links[strip_query(external["uri"])] = {"uri": record["uri"], "cid": record["cid"]}
    return links


def make_record(item: Item, thumb_blob: dict | None, quote: dict | None, now: datetime) -> dict:
    external = {
        "$type": "app.bsky.embed.external",
        "external": {"uri": item.link, "title": item.post.title, "description": item.post.description},
    }
    if thumb_blob:
        external["external"]["thumb"] = thumb_blob
    embed = external
    if quote:
        embed = {
            "$type": "app.bsky.embed.recordWithMedia",
            "record": {"$type": "app.bsky.embed.record", "record": quote},
            "media": external,
        }
    return {
        "$type": "app.bsky.feed.post",
        "text": item.text,
        "langs": [item.tag],
        "embed": embed,
        "createdAt": now.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    }


# ---------------------------------------------------------------- 網路

def request(url: str, data: bytes | dict | None = None, token: str | None = None,
            content_type: str = "application/json") -> dict:
    headers = {"User-Agent": USER_AGENT}
    if isinstance(data, dict):
        data = json.dumps(data).encode()
    if data is not None:
        headers["Content-Type"] = content_type
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def resolve_pds(handle: str) -> tuple[str, str]:
    """帳號名稱 → (DID, PDS 網址)。"""
    did = request("https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?"
                  + urllib.parse.urlencode({"handle": handle}))["did"]
    doc = request(f"https://plc.directory/{did}")
    pds = next(s["serviceEndpoint"] for s in doc["service"] if s["id"] == "#atproto_pds")
    return did, pds


def list_posts(pds: str, did: str) -> list[dict]:
    records, cursor = [], None
    while True:
        query = {"repo": did, "collection": "app.bsky.feed.post", "limit": 100}
        if cursor:
            query["cursor"] = cursor
        page = request(f"{pds}/xrpc/com.atproto.repo.listRecords?" + urllib.parse.urlencode(query))
        records += page.get("records", [])
        cursor = page.get("cursor")
        if not cursor or not page.get("records"):
            return records


def is_live(url: str) -> bool:
    """文章網址在 clearnet 回應 200。加上 query 避開 Cloudflare 快取的舊結果。"""
    try:
        req = urllib.request.Request(f"{url}?bsky-live={int(time.time())}", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status == 200
    except urllib.error.URLError:
        return False


def wait_live(url: str) -> bool:
    deadline = time.monotonic() + LIVE_WAIT.total_seconds()
    while True:
        if is_live(url):
            return True
        if time.monotonic() > deadline:
            return False
        time.sleep(LIVE_INTERVAL)


def thumb_bytes(thumb: str) -> tuple[bytes, str]:
    suffix = Path(urllib.parse.urlparse(thumb).path).suffix.lower()
    if thumb.startswith("https://"):
        req = urllib.request.Request(thumb, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read(), IMAGE_TYPES[suffix]
    return (ROOT / "static" / thumb).read_bytes(), IMAGE_TYPES[suffix]


# ---------------------------------------------------------------- 主程式

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="列出這一輪會發的貼文，不登入也不發文")
    parser.add_argument("--now", help="當下的時間（ISO 8601，例如 2026-10-05T07:10:00+08:00），預設是現在")
    parser.add_argument("--offline", action="store_true", help="跟 --dry-run 一起用，不讀帳號上的貼文紀錄")
    args = parser.parse_args()

    config, targets = build.load_config(ROOT / "site.toml")
    handle = config["bluesky"]["handle"]
    now = datetime.fromisoformat(args.now) if args.now else build.current_time()
    build.current_time = lambda: now  # 排程中的判斷跟著 --now
    posts = build.load_site(ROOT / "posts", build.load_authors(ROOT / "authors.yml"))
    items = plan(posts, targets["clearnet"].base_url, now)

    if args.offline and not args.dry_run:
        parser.error("--offline 只能跟 --dry-run 一起用")
    password = os.environ.get("BLUESKY_APP_PASSWORD")
    if not args.dry_run and not password:
        print("沒有設定 BLUESKY_APP_PASSWORD，略過發文")
        return 0

    posted: dict[str, dict] = {}
    if not args.offline:
        did, pds = resolve_pds(handle)
        posted = posted_links(list_posts(pds, did))
    todo = [item for item in items if item.url not in posted]
    print(f"@{handle}：{now:%Y-%m-%d %H:%M} 前 24 小時發布的貼文 {len(items)} 則，已發過 {len(items) - len(todo)} 則，"
          f"這一輪要發 {len(todo)} 則")

    if args.dry_run:
        for item in items:
            state = "已發過" if item.url in posted else "要發"
            quote = item.quote_url and (f"引用 {item.quote_url}" + ("" if item.quote_url in posted or args.offline
                                                                     else "（找不到它的貼文，改發一般貼文）"))
            print(f"\n[{state}] {item.post.where}（langs={item.tag}，{len(item.text)} 字元）")
            print("  " + item.text.replace("\n", "\n  "))
            print(f"  連結：{item.link}")
            print(f"  預覽圖：{item.thumb}")
            if quote:
                print(f"  {quote}")
        return 0

    session = request(f"{pds}/xrpc/com.atproto.server.createSession", {"identifier": handle, "password": password})
    token = session["accessJwt"]
    failed = 0
    for item in todo:
        if not wait_live(item.url):
            print(f"略過 {item.url}：還沒上線，下一輪再試")
            continue
        try:
            data, mime = thumb_bytes(item.thumb)
            blob = request(f"{pds}/xrpc/com.atproto.repo.uploadBlob", data, token, mime)["blob"]
            quote = posted.get(item.quote_url) if item.quote_url else None
            record = make_record(item, blob, quote, datetime.now(timezone.utc))
            result = request(f"{pds}/xrpc/com.atproto.repo.createRecord",
                             {"repo": did, "collection": "app.bsky.feed.post", "record": record}, token)
        except (urllib.error.URLError, KeyError, OSError) as error:
            print(f"發文失敗 {item.url}：{error}")
            failed += 1
            continue
        # 同一輪裡的後續稿要引用這一則
        posted[item.url] = {"uri": result["uri"], "cid": result["cid"]}
        print(f"已發文 {item.url} → {result['uri']}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
