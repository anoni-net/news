"""維護者抓取原文網站的圖示，上傳到 assets.anoni.net 並登記在 favicons.toml。規則見 SPEC.md「原文的網站圖示」。

    uv run tools/fetch_favicons.py --dry-run                     # 全部文章，只抓取與轉檔，產生預覽
    uv run tools/fetch_favicons.py --dry-run posts/2026-09-18-slug.md
    NEWS_ASSETS_RSYNC=<rsync 目標> uv run tools/fetch_favicons.py posts/2026-09-18-slug.md
    uv run tools/fetch_favicons.py --from openai.com=~/Downloads/openai.png --none ooni.org=網站沒有提供圖示
    uv run tools/fetch_favicons.py --refetch openai.com                  # 已登記的主機重新抓取

只處理 favicons.toml 還沒登記的主機。每個主機依序試網站首頁 <link> 宣告的 apple-touch-icon、
標了尺寸的 PNG 或 ICO，最後才試 /favicon.ico，取最大的一張縮成 64×64 的 PNG。原站擋下自動抓取時，
改從 Internet Archive 取同一個網站最近的存檔。上傳到
$NEWS_ASSETS_RSYNC/favicons/，確認 https://assets.anoni.net/news/favicons/ 底下回 200 之後才寫進登記表。

抓到的圖對不對要人看，--dry-run 會產生 .cache/favicons/preview.html，把每個圖示放在淺色與深色背景上。
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import io
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import build  # noqa: E402
import ingest_images  # noqa: E402

STAGING = ROOT / ".cache" / "favicons"
MIN_EDGE = 16
ARCHIVE_RETRY_WAITS = (10, 30, 60)
# 有些網站擋掉不像瀏覽器的請求，抓圖示時用一般瀏覽器的 User-Agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
LINK_RE = re.compile(r"<link\b[^>]*>", re.I)
ATTR_RE = re.compile(r'([a-zA-Z-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))')
HEADER = """\
# 原文網站的圖示登記表，格式與流程見 SPEC.md「原文的網站圖示」。
# 鍵是 sources 網址的主機名稱，去掉開頭的 www.。由 tools/fetch_favicons.py 寫入，手改之前先讀規格。
"""


@dataclass
class Fetched:
    host: str
    png: bytes
    source: str    # 抓取的原始網址，或手動指定的檔案

    @property
    def name(self) -> str:
        return f"{self.host}-{hashlib.sha256(self.png).hexdigest()[:8]}.png"


# ---------------------------------------------------------------- 轉檔

def convert(data: bytes) -> bytes:
    """任何 Pillow 讀得了的點陣圖（PNG、ICO、JPEG、WebP、GIF）轉成 64×64 的 PNG，不帶 metadata。
    ICO 取最大的一張，非正方形的置中補透明邊。SVG 不收。"""
    head = data[:512].lstrip().lower()
    if head.startswith((b"<svg", b"<?xml", b"<!doctype", b"<html")):
        raise ValueError("是 SVG 或網頁，不是點陣圖")
    with Image.open(io.BytesIO(data)) as source:
        if source.format == "ICO":
            source.size = max(source.info.get("sizes") or {source.size})
        source.load()
        image = source.convert("RGBA")
    if min(image.size) < MIN_EDGE:
        raise ValueError(f"只有 {image.size[0]}×{image.size[1]}，太小")
    edge = max(image.size)
    square = Image.new("RGBA", (edge, edge), (0, 0, 0, 0))
    square.paste(image, ((edge - image.width) // 2, (edge - image.height) // 2))
    square = square.resize((build.FAVICON_SIZE, build.FAVICON_SIZE), Image.Resampling.LANCZOS)
    for candidate in (square, square.quantize(256, method=Image.Quantize.FASTOCTREE)):
        out = io.BytesIO()
        # 不傳 pnginfo、exif、icc_profile，另存時不會帶任何 metadata
        candidate.save(out, "PNG", optimize=True)
        if out.tell() <= build.MAX_FAVICON_BYTES:
            return out.getvalue()
    raise ValueError(f"壓到 256 色仍超過 {build.MAX_FAVICON_BYTES // 1000}KB")


# ---------------------------------------------------------------- 抓取

# 照常驗證憑證鏈，只拿掉 Python 3.13 起預設的嚴格模式。台灣政府網站的 GRCA 憑證缺少
# Subject Key Identifier，嚴格模式會擋下，curl 與瀏覽器都接受
TLS = ssl.create_default_context()
TLS.verify_flags &= ~ssl.VERIFY_X509_STRICT


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    # Internet Archive 短時間內請求太多會直接拒絕連線，等一下再試就會通
    waits = ARCHIVE_RETRY_WAITS if url.startswith("https://web.archive.org/") else ()
    for wait in (*waits, None):
        try:
            with urllib.request.urlopen(request, timeout=30, context=TLS) as response:
                data = response.read()
            break
        except urllib.error.HTTPError:
            raise
        except OSError:
            if wait is None:
                raise
            time.sleep(wait)
    # Internet Archive 的原始檔照原站的壓縮格式回傳，urllib 不會自己解開
    return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data


def archived(url: str) -> str:
    """Internet Archive 裡最接近今天的那一份原始檔。原站擋下自動抓取時，改從這裡取同一個網址。"""
    return f"https://web.archive.org/web/{date.today():%Y%m%d}id_/{url}"


def candidates(page_url: str, page: str) -> list[str]:
    """首頁宣告的圖示，由大到小，SVG 與 mask-icon 略過，最後補上慣例的位置。"""
    found: list[tuple[int, int, str]] = []
    for order, tag in enumerate(LINK_RE.findall(page)):
        attrs = {m.group(1).lower(): html.unescape(m.group(2) or m.group(3) or m.group(4) or "")
                 for m in ATTR_RE.finditer(tag)}
        rel = attrs.get("rel", "").lower().split()
        href = attrs.get("href", "").strip()
        if not href or "mask-icon" in rel:
            continue
        if attrs.get("type", "").lower() == "image/svg+xml" or urllib.parse.urlsplit(href).path.lower().endswith(".svg"):
            continue
        if any(r.startswith("apple-touch-icon") for r in rel):
            default = 180
        elif "icon" in rel:
            default = 32
        else:
            continue
        sizes = [int(w) for w, _ in re.findall(r"(\d+)x(\d+)", attrs.get("sizes", ""))]
        found.append((max(sizes, default=default), -order, urllib.parse.urljoin(page_url, href)))
    urls = [url for _, _, url in sorted(found, reverse=True)]
    for fallback in ("/apple-touch-icon.png", "/favicon.ico"):
        url = urllib.parse.urljoin(page_url, fallback)
        if url not in urls:
            urls.append(url)
    return urls


def fetch_icon(host: str, origin: str) -> tuple[Fetched | None, list[str]]:
    """回傳抓到的圖示，以及每個試過的網址失敗的原因。

    首頁先讀原站，讀不到再讀 Internet Archive 最近的存檔，拿到網站宣告的圖示清單。每個圖示同樣先試原站、
    再試存檔。Cloudflare 這類防護常把首頁與圖示一起擋下，存檔裡的是原站自己的檔案。慣例位置排在宣告的
    圖示之後：首頁讀不到就直接抓 /favicon.ico，拿到的可能是網站系統的預設圖示，eSafety 就是這樣。"""
    tried: list[str] = []
    page_url = f"https://{origin}/"
    page = ""
    for url in (page_url, archived(page_url)):
        try:
            page = fetch(url).decode("utf-8", "replace")
            break
        except (OSError, ValueError) as error:
            tried.append(f"{url}：{error}")
    for url in candidates(page_url, page):
        for attempt in (url, archived(url)):
            try:
                return Fetched(host, convert(fetch(attempt)), attempt), tried
            except (OSError, ValueError, Image.DecompressionBombError) as error:
                tried.append(f"{attempt}：{error}")
    return None, tried


def parent_host(host: str) -> str | None:
    """三段以上的主機往上一層，例如 support.signal.org 的上一層是 signal.org。"""
    parts = host.split(".")
    return ".".join(parts[1:]) if len(parts) >= 3 else None


def from_override(host: str, value: str) -> Fetched:
    """--from 指定的網址或本機檔案。"""
    if value.startswith(("https://", "http://")):
        return Fetched(host, convert(fetch(value)), value)
    path = Path(value).expanduser()
    return Fetched(host, convert(path.read_bytes()), f"手動提供的檔案 {path.name}")


# ---------------------------------------------------------------- 登記表

def load_registry(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    with open(path, "rb") as f:
        return tomllib.load(f).get("hosts", {})


def dump_registry(hosts: dict[str, dict]) -> str:
    """依主機名稱排序寫回，欄位順序固定，diff 才看得出改了哪幾筆。"""
    blocks = [HEADER]
    for host in sorted(hosts):
        lines = [f"[hosts.{json.dumps(host)}]"]
        for key in ("icon", "from", "same_as", "none"):
            if key in hosts[host]:
                lines.append(f"{key} = {json.dumps(hosts[host][key], ensure_ascii=False)}")
        blocks.append("\n".join(lines) + "\n")
    return "\n".join(blocks)


def source_hosts(paths: list[Path]) -> dict[str, str]:
    """文章 sources 的主機，值是第一次出現時的原始主機（可能帶 www.），抓首頁用。
    導讀歷史的來源寫在每一年的 snapshots 底下，一起收進來。"""
    hosts: dict[str, str] = {}
    for path in paths:
        meta, _ = build.split_front_matter(path.read_text(encoding="utf-8"), path.name)
        items = list(meta.get("sources") or [])
        for snapshot in meta.get("snapshots") or []:
            if isinstance(snapshot, dict):
                items += snapshot.get("sources") or []
        for item in items:
            url = str(item.get("url", "")) if isinstance(item, dict) else ""
            origin = urllib.parse.urlsplit(url).hostname
            if origin:
                hosts.setdefault(build.source_host(url), origin.lower())
    return hosts


def all_posts() -> list[Path]:
    """三個語系的全部文章，加上導讀歷史的日期檔（前言 index.md 沒有來源，不算）。"""
    posts = [p for lang in build.LANGS for p in build.lang_dir(ROOT / "posts", lang).glob("*.md")]
    history = [p for lang in build.LANGS for p in build.lang_dir(build.HISTORY_DIR, lang).glob("*.md")
               if p.name != build.HISTORY_INDEX]
    return sorted(posts + history)


def write_preview(fetched: list[Fetched], failed: dict[str, list[str]]) -> Path:
    rows = []
    for item in fetched:
        tiles = "".join(f'<td style="background:{bg}"><img src="{item.name}" width="16" height="16" '
                        f'style="background:#fff;padding:1px;border-radius:3px;vertical-align:middle"> '
                        f'<img src="{item.name}" width="64" height="64" style="vertical-align:middle"></td>'
                        for bg in ("#ffffff", "#132a34"))
        rows.append(f"<tr><th>{html.escape(item.host)}</th>{tiles}<td>{html.escape(item.source)}</td></tr>")
    for host, reasons in failed.items():
        rows.append(f"<tr><th>{html.escape(host)}</th><td colspan=3>抓不到：{html.escape('；'.join(reasons[-3:]))}</td></tr>")
    path = STAGING / "preview.html"
    path.write_text('<!doctype html><meta charset="utf-8"><title>網站圖示預覽</title>'
                    '<table border=1 cellpadding=8 style="border-collapse:collapse;font:14px sans-serif">'
                    "<tr><th>主機</th><th>淺色</th><th>深色</th><th>來源</th></tr>" + "".join(rows) + "</table>",
                    encoding="utf-8")
    return path


# ---------------------------------------------------------------- 主流程

def pairs(values: list[str], flag: str) -> dict[str, str]:
    result = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"{flag} 要寫成 <主機>=<值>，收到 {value!r}")
        host, rest = value.split("=", 1)
        result[build.source_host(f"https://{host.strip()}/")] = rest.strip()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("posts", nargs="*", type=Path, help="要處理的文章，不給就是三個語系的全部文章與導讀歷史")
    parser.add_argument("--dry-run", action="store_true", help="只抓取與轉檔、產生預覽，不上傳也不改登記表")
    parser.add_argument("--from", dest="overrides", action="append", default=[], metavar="主機=網址或檔案",
                        help="指定圖示的來源，抓不到或抓到的圖不適合時用")
    parser.add_argument("--none", dest="nones", action="append", default=[], metavar="主機=理由",
                        help="登記成通用的地球圖示")
    parser.add_argument("--same-as", dest="aliases", action="append", default=[], metavar="主機=另一個主機",
                        help="沿用另一個主機的圖示")
    parser.add_argument("--refetch", action="append", default=[], metavar="主機",
                        help="已經登記的主機也重新抓取，例如之前登記成 none 的")
    args = parser.parse_args()

    registry = load_registry(build.FAVICONS_PATH)
    overrides, nones, aliases = pairs(args.overrides, "--from"), pairs(args.nones, "--none"), pairs(args.aliases, "--same-as")
    wanted = source_hosts(args.posts or all_posts())
    refetch = {build.source_host(f"https://{host.strip()}/") for host in args.refetch}
    for host in [*overrides, *nones, *aliases, *refetch]:
        wanted.setdefault(host, host)
    todo = {host: origin for host, origin in wanted.items()
            if host not in registry or host in overrides or host in nones or host in aliases or host in refetch}
    if not todo:
        print("每個主機都已經登記，沒有要處理的")
        return 0

    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    entries: dict[str, dict] = {}
    fetched: list[Fetched] = []
    failed: dict[str, list[str]] = {}

    def keep(item: Fetched) -> None:
        (STAGING / item.name).write_bytes(item.png)
        fetched.append(item)
        entries[item.host] = {"icon": item.name, "from": item.source}

    for host, origin in todo.items():
        if host in nones:
            entries[host] = {"none": nones[host]}
        elif host in aliases:
            entries[host] = {"same_as": aliases[host]}
        elif host in overrides:
            try:
                keep(from_override(host, overrides[host]))
            except (OSError, ValueError) as error:
                failed[host] = [f"{overrides[host]}：{error}"]
        else:
            item, tried = fetch_icon(host, origin)
            if item:
                keep(item)
                continue
            parent = parent_host(host)
            if parent and parent in registry and "same_as" not in registry[parent]:
                entries[host] = {"same_as": parent}
                continue
            if parent and parent not in todo:
                item, more = fetch_icon(parent, parent)
                if item:
                    keep(item)
                    entries[host] = {"same_as": parent}
                    continue
                tried += more
            failed[host] = tried

    # 子網域排在上一層前面處理時，上一層那時還沒抓，這裡補登記成 same_as
    for host in list(failed):
        parent = parent_host(host)
        if parent and "icon" in entries.get(parent, {}):
            entries[host] = {"same_as": parent}
            del failed[host]

    preview = write_preview(fetched, failed)
    for host, entry in entries.items():
        detail = entry.get("from") or entry.get("none") or f"沿用 {entry.get('same_as')}"
        print(f"  {host}：{entry.get('icon', '')} {detail}".rstrip())
    if failed:
        print("\n抓不到，用 --from <主機>=<網址或檔案> 指定來源，或 --none <主機>=<理由> 登記成通用圖示：")
        for host, reasons in failed.items():
            print(f"  {host}")
            for reason in reasons[-3:]:
                print(f"    {reason}")
    print(f"\n預覽：{preview}")

    if args.dry_run:
        print("（試跑，沒有上傳也沒有改登記表）")
        return 1 if failed else 0

    if fetched:
        target = os.environ.get("NEWS_ASSETS_RSYNC")
        if not target:
            print("沒有設定 NEWS_ASSETS_RSYNC（rsync 的目標，例如 host:/path/news），圖示沒有上傳，登記表沒有改動")
            return 1
        files = [str(STAGING / item.name) for item in fetched]
        subprocess.run(["rsync", "-a", "--mkpath", *files, f"{target.rstrip('/')}/{build.FAVICON_DIR}"], check=True)
        missing = [item.name for item in fetched
                   if not ingest_images.is_live(build.ASSETS_PREFIX + build.FAVICON_DIR + item.name)]
        if missing:
            print("上傳之後這些圖示沒有回 200，登記表沒有改動：")
            print("\n".join(f"  {name}" for name in missing))
            return 1

    registry.update(entries)
    build.FAVICONS_PATH.write_text(dump_registry(registry), encoding="utf-8")
    build.load_favicons(build.FAVICONS_PATH)  # 寫回去的格式不對時在這裡就失敗
    print(f"已寫入 {build.FAVICONS_PATH.name}，共 {len(entries)} 個主機")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
