"""產生 anoni.net/news 的 clearnet 與 onion 兩份靜態產物。

    uv run build.py                    # 產生 public/clearnet 與 public/onion
    uv run build.py --check            # 產生之後執行 SPEC.md「驗證與 CI」的九項檢查
    uv run build.py --update-contract  # 認可目前的網址，寫回 url_contract.txt

規格見 SPEC.md，要改行為先改規格。
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import html
import json
import re
import shutil
import sys
import tempfile
import tomllib
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path

import markdown
import yaml
from PIL import Image
from jinja2 import Environment, FileSystemLoader, StrictUndefined, pass_context
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
TZ = timezone(timedelta(hours=8))
DOCS_PREFIX = "https://anoni.net/docs/"
NEWS_PREFIX = "https://anoni.net/news/"
DOCS_CONTRACT_URL = "https://raw.githubusercontent.com/anoni-net/docs/main/tools/data/url_contract.txt"
DOCS_CONTRACT_CACHE = ROOT / ".cache" / "docs_url_contract.txt"

FRONT_MATTER_KEYS = {"title", "description", "date", "slug", "sources", "authors", "categories", "draft", "image", "pin",
                     "follows", "watch"}
REQUIRED_KEYS = {"title", "description", "date", "slug", "sources", "authors"}
SOURCE_KEYS = {"title", "url", "publisher", "date"}
AUTHOR_KEYS = {"name", "names", "description", "url"}
WATCH_KEYS = {"date", "note"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ANCHOR_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
HEADING_ID_RE = re.compile(r"\{\s*#([^\s}]+)\s*\}$")
HREF_RE = re.compile(r'(href)="([^"]*)"')

# 圖片規則見 SPEC.md「圖片」
ASSETS_PREFIX = "https://assets.anoni.net/news/"
ASSETS_CACHE = ROOT / ".cache" / "assets"
IMAGE_EXTS = {".webp", ".png", ".jpg", ".jpeg"}
IMAGE_FORMATS = {"WEBP", "PNG", "JPEG"}
MAX_IMAGE_BYTES = 300_000
MAX_IMAGE_EDGE = 2000
IMG_RE = re.compile(r"<img\b[^>]*>")
STANDALONE_IMG_RE = re.compile(r"<p>\s*(<img\b[^>]*>)\s*</p>")
INGEST_HINT = "維護者合併前執行 uv run tools/ingest_images.py 把圖片搬到 assets.anoni.net"

# 原文的網站圖示，規則見 SPEC.md「原文的網站圖示」
FAVICONS_PATH = ROOT / "favicons.toml"
FAVICON_DIR = "favicons/"
FAVICON_SIZE = 64
MAX_FAVICON_BYTES = 8_000
FAVICON_KEYS = {"icon", "from", "same_as", "none"}
FAVICON_NAME_RE = re.compile(r"^[a-z0-9.-]+-[0-9a-f]{8}\.png$")
FAVICON_HINT = "維護者執行 uv run tools/fetch_favicons.py 抓取並登記"


# 語系規則見 SPEC.md「多語系」
@dataclass(frozen=True)
class Lang:
    code: str       # strings.toml 的區段名
    dir: str        # posts/ 底下的子目錄，zh-TW 放在 posts/ 這一層
    path: str       # 網址前綴，接在站台前綴之後
    html: str       # <html lang> 與 hreflang
    og_locale: str
    og_image: str   # 全站共用的預覽圖，放在 static/


LANGS = [
    Lang("zh-TW", "", "", "zh-Hant", "zh_TW", "og.png"),
    Lang("zh-CN", "zh-CN", "zh-cn/", "zh-Hans", "zh_CN", "og-zh-cn.png"),
    Lang("en", "en", "en/", "en", "en_US", "og-en.png"),
]
DEFAULT_LANG = LANGS[0]
# 三個版本必須相同的欄位。date 另外比 created，updated 可以不同
SHARED_KEYS = ("slug", "authors", "pin", "draft", "image", "categories", "follows")
STRINGS_PATH = ROOT / "strings.toml"
# 文章以外的固定頁面，每個語系一份 Markdown，網址是 /news/<名稱>/。見 SPEC.md「關於頁」
PAGES_DIR = ROOT / "pages"
SITE_PAGES = ("about", "subscribe")
# 固定頁面裡代入該語系 feed 的完整網址，clearnet 與 onion 各自換成自己的網址
FEED_URL_PLACEHOLDER = "%FEED_URL%"
PAGE_KEYS = {"title", "description"}
# 排程發布：date 晚於現在的文章先不產出，最多只能排到幾天後。見 SPEC.md「排程發布」
MAX_SCHEDULE_DAYS = 7
# 追蹤中的事件：回頭查的日期在幾天內就列出來，跟排程的窗口相同，趕得上排進下一批稿。見 SPEC.md「追蹤中的事件」
WATCH_AHEAD_DAYS = MAX_SCHEDULE_DAYS


def load_strings(path: Path = STRINGS_PATH) -> dict[str, dict]:
    """介面文字。三個語系都要有，鍵也要一致，少一個就建置失敗。"""
    with open(path, "rb") as f:
        data = tomllib.load(f)
    problems = []
    for lang in LANGS:
        if lang.code not in data:
            problems.append(f"{path.name}：缺少 [{lang.code}]")
    keys = set(data.get(DEFAULT_LANG.code, {}))
    for lang in LANGS[1:]:
        other = set(data.get(lang.code, {}))
        for key in sorted(keys - other):
            problems.append(f"{path.name}：[{lang.code}] 缺少 {key}")
        for key in sorted(other - keys):
            problems.append(f"{path.name}：[{lang.code}] 多了 {key}，[{DEFAULT_LANG.code}] 沒有")
    if problems:
        raise BuildError(problems)
    return data


_strings: dict[str, dict] | None = None


def strings() -> dict[str, dict]:
    global _strings
    if _strings is None:
        _strings = load_strings()
    return _strings


def format_date(s: dict, key: str, d: date) -> str:
    return s[key].format(year=d.year, month=s["months"][d.month - 1], day=d.day, weekday=s["weekdays"][d.weekday()])


class BuildError(Exception):
    """內容或設定不符合規格。訊息逐條列出，一次看到全部的問題。"""

    def __init__(self, problems: list[str]):
        super().__init__("\n".join(problems))
        self.problems = problems


# ---------------------------------------------------------------- 內容

@dataclass
class Source:
    title: str
    url: str
    publisher: str | None = None
    date: date | None = None
    # 網站圖示在產物 assets/ 底下的路徑。登記成 none 或還沒解析時是 None，頁面改用通用圖示
    icon: str | None = None

    @property
    def host(self) -> str:
        return source_host(self.url)


def source_host(url: str) -> str:
    """favicons.toml 的鍵：網址的主機名稱，去掉開頭的 www.。"""
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


@dataclass
class Watch:
    """文章裡記下的一件之後要回頭查的事。due 是回頭查的日期，note 是要查什麼。"""
    due: date
    note: str


@dataclass
class Post:
    path: Path
    title: str
    description: str
    created: datetime
    updated: datetime | None
    slug: str
    sources: list[Source]
    authors: list[dict]
    categories: list[str]
    body: str
    html: str = ""
    anchors: list[str] = field(default_factory=list)
    image: str | None = None
    pin: bool = False
    # 接續的舊文章，寫檔名（不含 .md）。見 SPEC.md「前情與後續」
    follows: list[str] = field(default_factory=list)
    # 之後要回頭查的事，只寫在 zh-TW 版本。見 SPEC.md「追蹤中的事件」
    watch: list[Watch] = field(default_factory=list)
    lang: Lang = DEFAULT_LANG
    # date 晚於建置當下，排程中，這次不產出
    scheduled: bool = False
    # 同一篇的三個版本，鍵是語系代碼，包含自己。由 load_site 填入
    translations: dict[str, "Post"] = field(default_factory=dict)

    @property
    def image_rel(self) -> str | None:
        """front matter 的 image 在產物 assets/ 底下的相對路徑。"""
        return self.image[len(ASSETS_PREFIX):] if self.image else None

    @property
    def rel(self) -> str:
        """文章在網站裡的相對路徑，例如 2026/09/zkp-age-verification/。"""
        return f"{self.lang.path}{self.created:%Y}/{self.created:%m}/{self.slug}/"

    @property
    def guid(self) -> str:
        return f"anoni-news:{self.rel.rstrip('/')}"

    @property
    def where(self) -> str:
        return f"{self.lang.dir}/{self.path.name}" if self.lang.dir else self.path.name


def current_time() -> datetime:
    """台北時間的現在。測試會替換這個函式，檢查未來日期時不必真的等時間過去。"""
    return datetime.now(TZ)


def to_datetime(value, where: str, problems: list[str]) -> datetime | None:
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=TZ)
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day, tzinfo=TZ)
    problems.append(f"{where}：日期要寫成 YYYY-MM-DD，讀到的是 {value!r}")
    return None


def load_authors(path: Path) -> dict[str, dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    problems = []
    for key, info in data.items():
        if not SLUG_RE.match(str(key)):
            problems.append(f"authors.yml：鍵 {key!r} 只能用小寫英文、數字與連字號")
        if not isinstance(info, dict) or "name" not in info:
            problems.append(f"authors.yml：{key} 缺少 name")
            continue
        extra = set(info) - AUTHOR_KEYS
        if extra:
            problems.append(f"authors.yml：{key} 有不認得的欄位 {sorted(extra)}，只收 name、names、description、url")
        names = info.get("names", {})
        codes = {lang.code for lang in LANGS[1:]}
        if not isinstance(names, dict) or set(names) - codes:
            problems.append(f"authors.yml：{key} 的 names 是其他語系的名稱，鍵只能是 {sorted(codes)}")
        url = info.get("url")
        if url and not str(url).startswith("https://"):
            problems.append(f"authors.yml：{key} 的 url 要用 https://")
    if problems:
        raise BuildError(problems)
    return {key: {"key": key, "description": None, "url": None, "names": {}, **info} for key, info in data.items()}


def split_front_matter(text: str, where: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise BuildError([f"{where}：開頭要是 front matter（---）"])
    end = text.find("\n---\n", 4)
    if end == -1:
        raise BuildError([f"{where}：front matter 沒有結尾的 ---"])
    meta = yaml.safe_load(text[4:end]) or {}
    if not isinstance(meta, dict):
        raise BuildError([f"{where}：front matter 要是 key: value 的格式"])
    return meta, text[end + 5:]


def check_headings(body: str, where: str, problems: list[str]) -> list[str]:
    """內文的小標題一律寫明 {#id}，不能用一級標題。回傳錨點清單。"""
    anchors, in_fence = [], False
    for number, line in enumerate(body.splitlines(), 1):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        match = None if in_fence else HEADING_RE.match(line)
        if not match:
            continue
        if len(match.group(1)) == 1:
            problems.append(f"{where}:{number}：內文不能用一級標題，文章標題由模板產生，從 ## 開始")
        found = HEADING_ID_RE.search(match.group(2))
        if not found:
            problems.append(f"{where}:{number}：小標題要用 {{#id}} 寫明錨點")
            continue
        anchor = found.group(1)
        if not ANCHOR_RE.match(anchor):
            problems.append(f"{where}:{number}：錨點 {anchor!r} 只能用小寫英文、數字與連字號")
        if anchor in anchors:
            problems.append(f"{where}:{number}：錨點 {anchor!r} 在同一篇裡重複")
        anchors.append(anchor)
    return anchors


def is_post_name(name: str) -> bool:
    """文章的檔名去掉 .md，也就是 follows 的寫法，例如 2026-09-18-zkp-age-verification。"""
    match = FILENAME_RE.match(name + ".md")
    return bool(match and SLUG_RE.match(match.group(2)))


def load_post(path: Path, authors: dict[str, dict], lang: Lang = DEFAULT_LANG) -> Post | None:
    """讀一篇文章。草稿回傳 None，不符合規格就丟 BuildError。"""
    where = f"{lang.dir}/{path.name}" if lang.dir else path.name
    meta, body = split_front_matter(path.read_text(encoding="utf-8"), where)
    if meta.get("draft") is True:
        return None

    problems = []
    missing = REQUIRED_KEYS - set(meta)
    if missing:
        problems.append(f"{where}：缺少必填欄位 {sorted(missing)}")
    extra = set(meta) - FRONT_MATTER_KEYS
    if extra:
        problems.append(f"{where}：有不認得的欄位 {sorted(extra)}")
    if problems:
        raise BuildError(problems)

    for key in ("title", "description"):
        if not isinstance(meta[key], str) or not meta[key].strip():
            problems.append(f"{where}：{key} 要是非空的文字")

    raw_date = meta["date"]
    updated = None
    if isinstance(raw_date, dict):
        if set(raw_date) - {"created", "updated"} or "created" not in raw_date:
            problems.append(f"{where}：date 寫成對照表時只能有 created 與 updated，而且要有 created")
            created = None
        else:
            created = to_datetime(raw_date["created"], where, problems)
            if "updated" in raw_date:
                updated = to_datetime(raw_date["updated"], where, problems)
    else:
        created = to_datetime(raw_date, where, problems)

    # date 是預定的發布時間，晚於現在就是排程中，這次建置先不產出。更正日期是實際改稿的時間，不能在未來
    now = current_time()
    if created and created > now + timedelta(days=MAX_SCHEDULE_DAYS):
        problems.append(f"{where}：date 是 {created:%Y-%m-%d %H:%M}，排程最多只能排到 {MAX_SCHEDULE_DAYS} 天後"
                        f"（台北時間 {now + timedelta(days=MAX_SCHEDULE_DAYS):%Y-%m-%d %H:%M} 以前）")
    if updated and updated > now:
        problems.append(f"{where}：date.updated 是 {updated:%Y-%m-%d %H:%M}，晚於現在（台北時間 {now:%Y-%m-%d %H:%M}），"
                        "填實際更正的時間")

    slug = str(meta["slug"])
    if not SLUG_RE.match(slug) or not 3 <= len(slug) <= 60:
        problems.append(f"{where}：slug {slug!r} 只能用小寫英文、數字與連字號，3 到 60 個字元")

    name = FILENAME_RE.match(path.name)
    if not name:
        problems.append(f"{where}：檔名要是 YYYY-MM-DD-<slug>.md")
    else:
        if created and name.group(1) != f"{created:%Y-%m-%d}":
            problems.append(f"{where}：檔名的日期跟 date 不同")
        if name.group(2) != slug:
            problems.append(f"{where}：檔名的 slug 跟 front matter 的 slug 不同")

    sources = []
    raw_sources = meta["sources"]
    if not isinstance(raw_sources, list) or not raw_sources:
        problems.append(f"{where}：sources 至少要有一筆")
        raw_sources = []
    for index, item in enumerate(raw_sources, 1):
        if not isinstance(item, dict) or not item.get("title") or not item.get("url"):
            problems.append(f"{where}：sources 第 {index} 筆要有 title 與 url")
            continue
        extra = set(item) - SOURCE_KEYS
        if extra:
            problems.append(f"{where}：sources 第 {index} 筆有不認得的欄位 {sorted(extra)}")
        if not str(item["url"]).startswith(("https://", "http://")):
            problems.append(f"{where}：sources 第 {index} 筆的 url 要是完整網址")
        source_date = item.get("date")
        if source_date is not None and not isinstance(source_date, date):
            problems.append(f"{where}：sources 第 {index} 筆的 date 要寫成 YYYY-MM-DD")
            source_date = None
        sources.append(Source(str(item["title"]), str(item["url"]), item.get("publisher"), source_date))

    post_authors = []
    raw_authors = meta["authors"]
    if not isinstance(raw_authors, list) or not raw_authors:
        problems.append(f"{where}：authors 至少要有一個，不想署名就寫 anoni-net")
        raw_authors = []
    for key in raw_authors:
        if key not in authors:
            problems.append(f"{where}：authors 的 {key!r} 不在 authors.yml 裡")
        else:
            post_authors.append(authors[key])

    image = meta.get("image")
    if image is not None and (not isinstance(image, str) or not image.startswith(ASSETS_PREFIX)):
        problems.append(f"{where}：image 要是 {ASSETS_PREFIX} 開頭的網址，{INGEST_HINT}")
        image = None

    pin = meta.get("pin", False)
    if not isinstance(pin, bool):
        problems.append(f"{where}：pin 只能寫 true 或 false")
        pin = False

    categories = meta.get("categories") or []
    if not isinstance(categories, list):
        problems.append(f"{where}：categories 要是清單")
        categories = []

    follows = meta.get("follows") or []
    if not isinstance(follows, list) or not all(isinstance(ref, str) and is_post_name(ref) for ref in follows):
        problems.append(f"{where}：follows 要是清單，每一項寫接續的舊文章檔名、不含 .md，例如 2026-09-18-zkp-age-verification")
        follows = []

    watch = []
    raw_watch = meta.get("watch") or []
    if raw_watch and lang != DEFAULT_LANG:
        problems.append(f"{where}：watch 只寫在 zh-TW 版本，這是編輯用的追蹤筆記，不翻譯")
    elif not isinstance(raw_watch, list):
        problems.append(f"{where}：watch 要是清單，每一筆有 date 與 note")
    else:
        for index, item in enumerate(raw_watch, 1):
            if (not isinstance(item, dict) or set(item) != WATCH_KEYS
                    or not isinstance(item["date"], date) or isinstance(item["date"], datetime)
                    or not isinstance(item["note"], str) or not item["note"].strip()):
                problems.append(f"{where}：watch 第 {index} 筆要有 date（YYYY-MM-DD，回頭查的日期）與 note（要查什麼）")
            elif created and item["date"] <= created.date():
                problems.append(f"{where}：watch 第 {index} 筆的 date 是 {item['date']}，要晚於發布日")
            else:
                watch.append(Watch(item["date"], item["note"].strip()))

    anchors = check_headings(body, where, problems)
    if problems:
        raise BuildError(problems)

    return Post(
        path=path,
        title=meta["title"].strip(),
        description=meta["description"].strip(),
        created=created,
        updated=updated,
        slug=slug,
        sources=sources,
        authors=post_authors,
        categories=[str(c) for c in categories],
        image=image,
        pin=pin,
        follows=list(follows),
        watch=watch,
        body=body,
        anchors=anchors,
        lang=lang,
        scheduled=created > now,
    )


def render_markdown(body: str) -> str:
    md = markdown.Markdown(extensions=["attr_list", "tables", "fenced_code"])
    return md.convert(body)


@dataclass
class Asset:
    rel: str       # 在產物 assets/ 底下的路徑，例如 2026/09/slug/figure-1.webp
    path: Path     # 本機的檔案
    width: int
    height: int


class AssetStore:
    """把 assets.anoni.net/news/ 的圖片抓到本機並檢查。local_dir 有值時改讀本機目錄，測試用。"""

    def __init__(self, local_dir: Path | None = None):
        self.local_dir = local_dir
        self.assets: dict[str, Asset] = {}

    def get(self, url: str, where: str, problems: list[str]) -> Asset | None:
        rel = url[len(ASSETS_PREFIX):]
        if rel in self.assets:
            return self.assets[rel]
        if Path(rel).suffix.lower() not in IMAGE_EXTS:
            problems.append(f"{where}：{url} 只收 WebP、PNG、JPEG")
            return None
        path = (self.local_dir or ASSETS_CACHE) / rel
        if not path.exists():
            if self.local_dir:
                problems.append(f"{where}：找不到圖片 {path}")
                return None
            try:
                request = urllib.request.Request(url, headers={"User-Agent": "anoni-net-news-build"})
                with urllib.request.urlopen(request, timeout=30) as response:
                    data = response.read()
            except OSError as error:
                problems.append(f"{where}：抓不到 {url}（{error}），圖片要先上傳到 assets.anoni.net 才能建置")
                return None
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        size = check_image(path, f"{where}：{url}", problems)
        if not size:
            return None
        self.assets[rel] = Asset(rel, path, *size)
        return self.assets[rel]


def check_image(path: Path, where: str, problems: list[str]) -> tuple[int, int] | None:
    """格式、metadata、大小。回傳 (寬, 高)，不合格回傳 None。"""
    before = len(problems)
    if path.stat().st_size > MAX_IMAGE_BYTES:
        problems.append(f"{where} 有 {path.stat().st_size // 1000}KB，單張不能超過 {MAX_IMAGE_BYTES // 1000}KB")
    try:
        with Image.open(path) as image:
            fmt, (width, height) = image.format, image.size
            metadata = []
            if image.getexif() or "exif" in image.info:
                metadata.append("EXIF")
            if any(key in image.info for key in ("xmp", "XML:com.adobe.xmp")):
                metadata.append("XMP")
            if getattr(image, "text", None):
                metadata.append("PNG 文字區塊")
            if "comment" in image.info:
                metadata.append("註解")
    except OSError:
        problems.append(f"{where} 不是可以讀取的圖片")
        return None
    if fmt not in IMAGE_FORMATS:
        problems.append(f"{where} 的格式是 {fmt}，只收 WebP、PNG、JPEG")
    if max(width, height) > MAX_IMAGE_EDGE:
        problems.append(f"{where} 是 {width}×{height}，長邊不能超過 {MAX_IMAGE_EDGE}px")
    if metadata:
        problems.append(f"{where} 帶著 {'、'.join(metadata)}，可能洩漏拍攝地點、時間或裝置，{INGEST_HINT}")
    return None if len(problems) > before else (width, height)


def process_images(post: Post, store: AssetStore, problems: list[str]) -> None:
    """檢查內文圖片，獨立成段的圖轉成 figure，補上寬高。src 維持 assets 網址，產出時再換成站內副本。"""
    where = post.where
    if post.image:
        store.get(post.image, f"{where} 的 image", problems)

    reported: set[str] = set()

    def to_figure(match: re.Match) -> str:
        attrs = dict(ATTR_RE.findall(match.group(1)))
        src = html.unescape(attrs.get("src", ""))
        reported.add(src)
        if not src.startswith(ASSETS_PREFIX):
            problems.append(f"{where}：圖片 {src} 不在 assets.anoni.net，{INGEST_HINT}")
            return match.group(0)
        ok = True
        if not attrs.get("alt", "").strip():
            problems.append(f"{where}：圖片 {src} 缺少替代文字")
            ok = False
        if not attrs.get("title", "").strip():
            problems.append(f"{where}：圖片 {src} 缺少圖說，寫在 title，例如 \"圖：EFF，CC-BY 4.0\"")
            ok = False
        asset = store.get(src, where, problems)
        if not ok or not asset:
            return match.group(0)
        return (f'<figure><img src="{html.escape(src)}" alt="{attrs["alt"]}" width="{asset.width}" '
                f'height="{asset.height}" loading="lazy" decoding="async">'
                f'<figcaption>{attrs["title"]}</figcaption></figure>')

    post.html = STANDALONE_IMG_RE.sub(to_figure, post.html)
    outside_figures = re.sub(r"<figure>.*?</figure>", "", post.html, flags=re.S)
    for tag in IMG_RE.findall(outside_figures):
        src = html.unescape(dict(ATTR_RE.findall(tag)).get("src", ""))
        if src not in reported:
            problems.append(f"{where}：圖片 {src} 要獨立成一段，不能跟文字寫在同一段")


def load_favicons(path: Path) -> dict[str, dict]:
    """讀 favicons.toml，每個主機只能是 icon、same_as、none 其中一種。"""
    with open(path, "rb") as f:
        hosts = tomllib.load(f).get("hosts", {})
    problems = []
    for host, entry in hosts.items():
        where = f"{path.name} 的 {host}"
        if not isinstance(entry, dict):
            problems.append(f"{where} 要寫成表格")
            continue
        extra = set(entry) - FAVICON_KEYS
        if extra:
            problems.append(f"{where} 有不認得的欄位 {sorted(extra)}")
        kinds = [key for key in ("icon", "same_as", "none") if key in entry]
        if len(kinds) != 1:
            problems.append(f"{where} 要寫 icon、same_as、none 其中一個")
            continue
        if "from" in entry and "icon" not in entry:
            problems.append(f"{where}：from 只跟 icon 一起寫")
        if "icon" in entry and not FAVICON_NAME_RE.match(str(entry["icon"])):
            problems.append(f"{where}：icon {entry['icon']!r} 要是 <主機>-<8 碼雜湊>.png")
        if "none" in entry and (not isinstance(entry["none"], str) or not entry["none"].strip()):
            problems.append(f"{where}：none 要寫理由")
        if "same_as" in entry:
            target = hosts.get(entry["same_as"])
            if not isinstance(target, dict):
                problems.append(f"{where}：same_as 指向的 {entry['same_as']} 不在登記表裡")
            elif "same_as" in target:
                problems.append(f"{where}：same_as 指向的 {entry['same_as']} 本身也是 same_as，要直接指到有 icon 或 none 的主機")
    if problems:
        raise BuildError(problems)
    return hosts


def resolve_favicons(posts: list[Post], hosts: dict[str, dict], store: AssetStore, problems: list[str]) -> None:
    """替每一筆原文找到網站圖示，抓進產物並檢查。沒登記的主機只報一次。"""
    reported: set[str] = set()
    checked: set[str] = set()
    for post in posts:
        for source in post.sources:
            host = source.host
            entry = hosts.get(host)
            if entry is None:
                if host not in reported:
                    problems.append(f"{post.where}：原文 {source.url} 的網站 {host} 不在 favicons.toml，{FAVICON_HINT}")
                    reported.add(host)
                continue
            if "same_as" in entry:
                entry = hosts[entry["same_as"]]
            if "icon" not in entry:
                continue
            where = f"favicons.toml 的 {host}"
            asset = store.get(ASSETS_PREFIX + FAVICON_DIR + entry["icon"], where, problems)
            if not asset:
                continue
            if asset.rel not in checked:
                checked.add(asset.rel)
                with Image.open(asset.path) as image:
                    fmt = image.format
                if fmt != "PNG" or (asset.width, asset.height) != (FAVICON_SIZE, FAVICON_SIZE):
                    problems.append(f"{where}：圖示要是 {FAVICON_SIZE}×{FAVICON_SIZE} 的 PNG，"
                                    f"現在是 {asset.width}×{asset.height} 的 {fmt}")
                if asset.path.stat().st_size > MAX_FAVICON_BYTES:
                    problems.append(f"{where}：圖示有 {asset.path.stat().st_size // 1000}KB，"
                                    f"不能超過 {MAX_FAVICON_BYTES // 1000}KB")
            source.icon = asset.rel


def localize_assets(text: str, target: "Target", absolute: bool = False) -> str:
    """把 assets.anoni.net 的圖片網址換成產物裡的副本。"""
    base = target.abs_url("assets/") if absolute else target.url("assets/")
    return text.replace(f'src="{ASSETS_PREFIX}', f'src="{base}')


def load_posts(posts_dir: Path, authors: dict[str, dict], store: AssetStore | None = None,
               lang: Lang = DEFAULT_LANG) -> list[Post]:
    """讀一個語系的文章，posts_dir 是該語系的目錄。"""
    problems, posts = [], []
    for path in sorted(posts_dir.glob("*.md")):
        try:
            post = load_post(path, authors, lang)
        except BuildError as error:
            problems += error.problems
            continue
        if post:
            post.html = render_markdown(post.body)
            process_images(post, store or AssetStore(), problems)
            posts.append(post)

    pinned = [post.where for post in posts if post.pin]
    if len(pinned) > 1:
        problems.append(f"首頁的頭條只能有一篇，現在有 {len(pinned)} 篇設了 pin：{'、'.join(pinned)}。換頭條時先拿掉舊的那篇")

    seen: dict[str, Post] = {}
    for post in posts:
        if post.rel in seen:
            problems.append(f"{post.where}：跟 {seen[post.rel].where} 的網址相同，slug 在同一個年月內不能重複")
        seen[post.rel] = post
    if problems:
        raise BuildError(problems)
    # 新的在前。同一個時間發的，依 slug 排，讓順序固定
    return sorted(posts, key=lambda p: (-p.created.timestamp(), p.slug))


def lang_dir(posts_dir: Path, lang: Lang) -> Path:
    return posts_dir / lang.dir if lang.dir else posts_dir


def load_site_pages(pages_dir: Path) -> dict[str, dict[str, dict]]:
    """關於頁這類固定頁面。三個語系都要有，錨點集合要相同，跟文章的規則一致。"""
    problems: list[str] = []
    result: dict[str, dict[str, dict]] = {}
    for name in SITE_PAGES:
        versions: dict[str, dict] = {}
        for lang in LANGS:
            path = lang_dir(pages_dir, lang) / f"{name}.md"
            where = str(path.relative_to(pages_dir.parent)) if path.is_relative_to(pages_dir.parent) else str(path)
            if not path.exists():
                problems.append(f"{where}：缺少 {lang.code} 版本")
                continue
            meta, body = split_front_matter(path.read_text(encoding="utf-8"), where)
            for key in sorted(PAGE_KEYS - set(meta)):
                problems.append(f"{where}：front matter 缺少 {key}")
            for key in sorted(set(meta) - PAGE_KEYS):
                problems.append(f"{where}：front matter 多了不認得的欄位 {key}")
            anchors = check_headings(body, where, problems)
            versions[lang.code] = {"title": str(meta.get("title", "")), "description": str(meta.get("description", "")),
                                   "html": render_markdown(body), "anchors": anchors, "where": where}
        default = versions.get(DEFAULT_LANG.code)
        for code, version in versions.items():
            if default and code != DEFAULT_LANG.code and set(version["anchors"]) != set(default["anchors"]):
                problems.append(f"{version['where']}：錨點跟 {DEFAULT_LANG.code} 版本不同")
        result[name] = versions
    if problems:
        raise BuildError(problems)
    return result


def created_of(meta: dict):
    raw = meta.get("date")
    return raw.get("created") if isinstance(raw, dict) else raw


def check_translations(posts_dir: Path) -> list[str]:
    """三個版本都在，共用欄位相同，sources 包含 zh-TW 的每一筆網址。草稿也一起比，三個版本要同時發布。"""
    problems = []
    files = {lang.code: {p.name: p for p in lang_dir(posts_dir, lang).glob("*.md")} for lang in LANGS}
    base = files[DEFAULT_LANG.code]
    for lang in LANGS[1:]:
        other = files[lang.code]
        for name in sorted(set(base) - set(other)):
            problems.append(f"{name}：缺少 {lang.code} 版本 posts/{lang.dir}/{name}，三個語系要一起送出")
        for name in sorted(set(other) - set(base)):
            problems.append(f"{lang.dir}/{name}：找不到對應的 zh-TW 版本 posts/{name}")
        for name in sorted(set(base) & set(other)):
            where = f"{lang.dir}/{name}"
            try:
                meta_tw, _ = split_front_matter(base[name].read_text(encoding="utf-8"), name)
                meta, _ = split_front_matter(other[name].read_text(encoding="utf-8"), where)
            except BuildError:
                continue  # 格式錯誤由 load_post 報
            if created_of(meta) != created_of(meta_tw):
                problems.append(f"{where}：date 的發布日跟 zh-TW 不同")
            for key in SHARED_KEYS:
                if meta.get(key) != meta_tw.get(key):
                    problems.append(f"{where}：{key} 跟 zh-TW 不同，三個版本要一致")

            def urls(m: dict) -> list[str]:
                items = m.get("sources") if isinstance(m.get("sources"), list) else []
                return [str(i.get("url")) for i in items if isinstance(i, dict)]

            for url in urls(meta_tw):
                if url not in urls(meta):
                    problems.append(f"{where}：sources 少了 zh-TW 有的 {url}")
    return problems


def check_follows(posts: list[Post]) -> list[str]:
    """follows 指到的文章要存在，而且比這篇早發布。三個語系的 follows 相同，只查 zh-TW。
    排程中的文章也算，兩篇都還在排程裡的時候一樣能接續。"""
    by_stem = {post.path.stem: post for post in posts}
    problems = []
    for post in posts:
        for ref in post.follows:
            earlier = by_stem.get(ref)
            if earlier is None:
                problems.append(f"{post.where}：follows 的 {ref} 找不到，寫舊文章的檔名、不含 .md。草稿不能被接續")
            elif earlier.created >= post.created:
                problems.append(f"{post.where}：follows 的 {ref} 沒有比這篇早發布，只能接續較早的文章")
    return problems


def story_threads(posts: list[Post]) -> dict[str, list[Post]]:
    """用 follows 把同一事件的文章串成一條事件線，回傳每篇的檔名對應到整條線，由舊到新排。
    posts 只放這次要產出的文章。後續還在排程中時不在裡面，舊文章就不會提早露出它的標題，
    到了發布時間重建才連上。只有自己一篇的不列。"""
    by_stem = {post.path.stem: post for post in posts}
    parent = {stem: stem for stem in by_stem}

    def root(stem: str) -> str:
        while parent[stem] != stem:
            stem = parent[stem]
        return stem

    for post in posts:
        for ref in post.follows:
            if ref in by_stem:
                parent[root(post.path.stem)] = root(ref)
    groups: dict[str, list[Post]] = {}
    for stem, post in by_stem.items():
        groups.setdefault(root(stem), []).append(post)
    threads = {}
    for group in groups.values():
        if len(group) > 1:
            ordered = sorted(group, key=lambda p: (p.created.timestamp(), p.slug))
            for post in group:
                threads[post.path.stem] = ordered
    return threads


def due_watches(posts: list[Post], today: date,
                ahead: int = WATCH_AHEAD_DAYS) -> tuple[list[tuple[Watch, Post]], list[tuple[Watch, Post]]]:
    """追蹤中的事件，分成到期（回頭查的日期在 ahead 天內或已經過了）與還沒到期兩組，各自依日期排。
    已經有後續稿的文章不列，後續稿還在排程中也算有了。posts 要包含排程中的文章。"""
    followed = {ref for post in posts for ref in post.follows}
    due, later = [], []
    for post in posts:
        if post.path.stem in followed:
            continue
        for item in post.watch:
            (due if item.due <= today + timedelta(days=ahead) else later).append((item, post))

    def key(pair: tuple[Watch, Post]):
        return pair[0].due, pair[1].created

    return sorted(due, key=key), sorted(later, key=key)


def watch_report(posts: list[Post], today: date) -> str:
    """--watch 的輸出。到期的每筆一行 checkbox，可以直接貼進每週候選票的「追蹤中的事件」。"""
    due, later = due_watches(posts, today)
    lines = [f"追蹤中的事件：{len(due)} 筆已到期或 {WATCH_AHEAD_DAYS} 天內到期（今天 {today}，台北時間）"]
    for item, post in due:
        late = (today - item.due).days
        suffix = f"（已過 {late} 天）" if late > 0 else ""
        lines.append(f"- [ ] {item.due} {post.title}：{item.note} {NEWS_PREFIX}{post.rel}{suffix}")
    if later:
        lines.append(f"另有 {len(later)} 筆還沒到期，最早是 {later[0][0].due}")
    lines.append("寫了後續稿（follows 接上這篇）就不再列出。事件沒有新進展時，刪掉那一筆 watch")
    return "\n".join(lines)


def load_site(posts_dir: Path, authors: dict[str, dict], store: AssetStore | None = None,
              favicons: dict[str, dict] | None = None) -> list[Post]:
    """讀三個語系，檢查對應之後回傳 zh-TW 的文章，其他版本放在 translations。
    favicons 是 favicons.toml 的內容，沒給就不解析網站圖示，原文一律用通用圖示。"""
    problems: list[str] = []
    by_lang: dict[str, list[Post]] = {}
    for lang in LANGS:
        try:
            by_lang[lang.code] = load_posts(lang_dir(posts_dir, lang), authors, store, lang)
        except BuildError as error:
            problems += error.problems
            by_lang[lang.code] = []
    problems += check_translations(posts_dir)
    if favicons is not None:
        resolve_favicons([post for posts in by_lang.values() for post in posts], favicons, store or AssetStore(), problems)
    if problems:
        raise BuildError(problems)

    index = {code: {post.path.name: post for post in posts} for code, posts in by_lang.items()}
    for post in by_lang[DEFAULT_LANG.code]:
        group = {code: index[code][post.path.name] for code in index}
        for code, version in group.items():
            version.translations = group
            if code != DEFAULT_LANG.code and sorted(version.anchors) != sorted(post.anchors):
                problems.append(f"{version.where}：小標題的錨點 {sorted(version.anchors)} 跟 zh-TW 的 "
                                f"{sorted(post.anchors)} 不同，分享出去的段落連結換了語系會失效")
    problems += check_follows(by_lang[DEFAULT_LANG.code])
    if problems:
        raise BuildError(problems)
    return by_lang[DEFAULT_LANG.code]


def all_versions(posts: list[Post]) -> list[Post]:
    """三個語系的全部文章。還沒經過 load_site 的文章只有自己。"""
    return [version for post in posts for version in (post.translations.values() or [post])]


def hrefs(text: str) -> list[str]:
    return [html.unescape(m.group(2)) for m in HREF_RE.finditer(text)]


# ---------------------------------------------------------------- 產生

@dataclass
class Target:
    name: str
    out: Path
    base_url: str
    prefix: str
    clearnet: bool
    rewrites: list[tuple[str, str]]
    # 流量統計的設定（src、website_id、domains），沒有就不載入，onion 一律沒有
    analytics: dict | None = None

    def url(self, rel: str = "") -> str:
        return self.prefix + rel

    def abs_url(self, rel: str = "") -> str:
        return self.base_url + rel

    def rewrite(self, url: str) -> str:
        for old, new in self.rewrites:
            if url.startswith(old):
                return new + url[len(old):]
        return url

    def rewrite_html(self, text: str) -> str:
        if not self.rewrites:
            return text
        return HREF_RE.sub(lambda m: f'{m.group(1)}="{html.escape(self.rewrite(html.unescape(m.group(2))))}"', text)


def load_config(path: Path) -> tuple[dict, dict[str, Target]]:
    with open(path, "rb") as f:
        config = tomllib.load(f)
    targets = {}
    for name, t in config["targets"].items():
        targets[name] = Target(
            name=name,
            out=ROOT / t["out"],
            base_url=t["base_url"],
            prefix=t["prefix"],
            clearnet=t["clearnet"],
            rewrites=[tuple(pair) for pair in t["rewrites"]],
            analytics=t.get("analytics"),
        )
    return config, targets


@dataclass
class Page:
    """一個產出的 HTML 頁面，檢查與網址合約都從這份清單讀。"""
    rel: str            # 相對於網站根目錄的網址，例如 2026/09/，首頁是空字串
    file: str           # 相對於產物根目錄的檔名
    noindex: bool
    anchors: list[str] = field(default_factory=list)


def chunk(items: list, size: int) -> list[list]:
    return [items[i:i + size] for i in range(0, len(items), size)] or [[]]


def jsonld(post: Post, target: Target, config: dict) -> str:
    homepage = target.rewrite(config["homepage"])
    organization = {"@type": "Organization", "name": "anoni.net", "url": homepage}
    authors = []
    for author in post.authors:
        if author["key"] == "anoni-net":
            authors.append(organization)
        else:
            person = {"@type": "Person", "name": author["name"]}
            if author.get("url"):
                person["url"] = author["url"]
            authors.append(person)
    data = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": post.title,
        "description": post.description,
        "datePublished": post.created.isoformat(),
        "url": target.abs_url(post.rel),
        "mainEntityOfPage": target.abs_url(post.rel),
        "image": target.abs_url("assets/" + post.image_rel) if post.image else target.abs_url(post.lang.og_image),
        "inLanguage": post.lang.html,
        "author": authors,
        "publisher": organization,
        "citation": [{"@type": "CreativeWork", "name": s.title, "url": s.url} for s in post.sources],
    }
    if post.updated:
        data["dateModified"] = post.updated.isoformat()
    # </script> 出現在字串裡會提早結束 script 元素，跳脫掉
    return json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")


def build_target(target: Target, posts: list[Post], config: dict, env: Environment,
                 store: AssetStore | None = None, site_pages: dict[str, dict[str, dict]] | None = None) -> list[Page]:
    """posts 是 zh-TW 的文章，其他語系從 translations 取。"""
    if target.out.exists():
        shutil.rmtree(target.out)
    shutil.copytree(ROOT / "static", target.out)
    for asset in (store.assets.values() if store else []):
        dest = target.out / "assets" / asset.rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(asset.path, dest)
    pages: list[Page] = []
    texts = strings()

    def onion_url(rel: str) -> str | None:
        if not target.clearnet:
            return None
        return f"http://news.{config['onion_host']}/{rel}"

    def alternates(rel_by_code: dict[str, str] | None, current: Lang) -> list[dict]:
        """頁首的語系切換與 hreflang。沒有對應頁面（404）時回傳空清單。"""
        if not rel_by_code:
            return []
        return [{"code": lang.code, "html": lang.html, "name": texts[lang.code]["lang_name"],
                 "href": target.url(rel_by_code[lang.code]), "abs": target.abs_url(rel_by_code[lang.code]),
                 "current": lang == current} for lang in LANGS]

    def write(page: Page, template: str, lang: Lang, rels: dict[str, str] | None, **context) -> None:
        html_text = env.get_template(template).render(
            target=target,
            config=config,
            url=target.url,
            # static/ 的檔案帶版本號，見 static_version
            asset=lambda rel: f"{target.url(rel)}?v={static_version(rel)}",
            abs_asset=lambda rel: f"{target.abs_url(rel)}?v={static_version(rel)}",
            lang=lang,
            s=texts[lang.code],
            home=lang.path,
            alternates=alternates(rels, lang),
            page_url=target.abs_url(page.rel),
            onion_url=onion_url(page.rel),
            noindex=page.noindex,
            **{"og_image": None, **context},
        )
        dest = target.out / page.file
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(target.rewrite_html(html_text), encoding="utf-8")
        pages.append(page)

    def same_page(suffix: str) -> dict[str, str]:
        return {lang.code: lang.path + suffix for lang in LANGS}

    threads = story_threads(posts)
    sitemap_homes: list[tuple[str, str | None, list[dict]]] = []
    sitemap_urls: list[tuple[str, str | None, list[dict]]] = []
    for lang in LANGS:
        s = texts[lang.code]
        lposts = [post.translations.get(lang.code, post) for post in posts] if lang != DEFAULT_LANG else posts
        if lang != DEFAULT_LANG and any(post.lang != lang for post in lposts):
            continue  # 沒有經過 load_site 的文章只產 zh-TW，測試用
        base = lang.path

        for i, post in enumerate(lposts):
            # 文章已經由新到舊排好，同一天的順序跟首頁時間軸相同，前後篇直接取相鄰的兩篇
            newer = lposts[i - 1] if i > 0 else None
            older = lposts[i + 1] if i + 1 < len(lposts) else None
            rels = {code: version.rel for code, version in post.translations.items()} or None
            # 同一事件的導讀，由舊到新。這篇不是最新的一篇時，標題區提示最新的後續
            thread = [item.translations.get(lang.code, item) for item in threads.get(post.path.stem, [])]
            followup = thread[-1] if thread and thread[-1].rel != post.rel else None
            # #sources 是模板產生的原文清單錨點，頂端那行出處連到這裡，跟內文的錨點一起收進合約
            write(Page(post.rel, post.rel + "index.html", False, post.anchors + ["sources"]), "post.html.j2",
                  lang, rels, post=post, newer=newer, older=older, thread=thread, followup=followup,
                  content=target.rewrite_html(localize_assets(post.html, target)),
                  jsonld=jsonld(post, target, config),
                  og_image=target.abs_url("assets/" + post.image_rel) if post.image else None)
            sitemap_urls.append((target.abs_url(post.rel), (post.updated or post.created).date().isoformat(),
                                 alternates(rels, lang)))

        featured = next((post for post in lposts if post.pin), None)
        featured_image = None
        if featured and featured.image and store and featured.image_rel in store.assets:
            asset = store.assets[featured.image_rel]
            featured_image = {"src": target.url("assets/" + asset.rel), "width": asset.width, "height": asset.height}

        per_page = config["per_page"]
        groups = chunk(lposts, per_page)
        for number, group in enumerate(groups, 1):
            suffix = "" if number == 1 else f"page/{number}/"
            write(Page(base + suffix, base + suffix + "index.html", number > 1), "list.html.j2", lang, same_page(suffix),
                  kind="index", heading=s["site_name"], posts=group, number=number, total=len(groups),
                  latest=lposts[0] if lposts else None,
                  featured=featured if number == 1 else None, featured_image=featured_image,
                  prev_rel=(base if number == 2 else f"{base}page/{number - 1}/") if number > 1 else None,
                  next_rel=f"{base}page/{number + 1}/" if number < len(groups) else None)
        sitemap_homes.append((target.abs_url(base), None, alternates(same_page(""), lang)))

        years: dict[int, list[Post]] = {}
        months: dict[tuple[int, int], list[Post]] = {}
        for post in lposts:
            years.setdefault(post.created.year, []).append(post)
            months.setdefault((post.created.year, post.created.month), []).append(post)
        for year, group in years.items():
            suffix = f"{year}/"
            write(Page(base + suffix, base + suffix + "index.html", True), "list.html.j2", lang, same_page(suffix),
                  kind="archive", heading=s["year_heading"].format(year=year), posts=group, number=1, total=1,
                  latest=None, prev_rel=None, next_rel=None, featured=None, featured_image=None)
        for (year, month), group in months.items():
            suffix = f"{year}/{month:02d}/"
            write(Page(base + suffix, base + suffix + "index.html", True), "list.html.j2", lang, same_page(suffix),
                  kind="archive", heading=s["month_heading"].format(year=year, month=s["months"][month - 1]),
                  posts=group, number=1, total=1, latest=None,
                  prev_rel=None, next_rel=None, featured=None, featured_image=None)

        for name, versions in (site_pages or {}).items():
            suffix = f"{name}/"
            version = versions[lang.code]
            content = version["html"].replace(FEED_URL_PLACEHOLDER, target.abs_url(base + "feed.xml"))
            write(Page(base + suffix, base + suffix + "index.html", False, version["anchors"]), "page.html.j2",
                  lang, same_page(suffix), site_page=version, content=content)
            sitemap_urls.append((target.abs_url(base + suffix), None, alternates(same_page(suffix), lang)))

        feed_posts = lposts[:config["feed_items"]]
        feed = env.get_template("feed.xml.j2").render(
            target=target, config=config, lang=lang, s=s, home=base,
            items=[{
                "post": post,
                "link": target.abs_url(post.rel),
                "pub_date": format_datetime(post.created),
                "content": target.rewrite_html(localize_assets(env.get_template("_post_body.html.j2").render(
                    post=post, content=post.html, url=target.url, s=s), target, absolute=True)),
            } for post in feed_posts],
            build_date=format_datetime(feed_posts[0].created) if feed_posts else None,
        )
        (target.out / base).mkdir(parents=True, exist_ok=True)
        (target.out / base / "feed.xml").write_text(feed, encoding="utf-8")

    # 404 只有一頁，三種語言各寫一段。伺服器依路徑回同一個檔案
    write(Page("404.html", "404.html", True), "404.html.j2", DEFAULT_LANG, None,
          versions=[{"lang": lang, "s": texts[lang.code]} for lang in LANGS])

    sitemap = env.get_template("sitemap.xml.j2").render(urls=sitemap_homes + sitemap_urls)
    (target.out / "sitemap.xml").write_text(sitemap, encoding="utf-8")

    if not target.clearnet:
        robots = env.get_template("robots.txt.j2").render(sitemap=target.abs_url("sitemap.xml"))
        (target.out / "robots.txt").write_text(robots, encoding="utf-8")
    return pages


def by_day(posts: list[Post]) -> list[dict]:
    """列表頁的時間軸：依發布日分組，保持原本新的在前的順序。"""
    groups: list[dict] = []
    for post in posts:
        day = post.created.date()
        if not groups or groups[-1]["date"] != day:
            groups.append({"date": day, "posts": []})
        groups[-1]["posts"].append(post)
    return groups


def source_line(post: Post, s: dict | None = None) -> str:
    """列表與頭條上的出處行。一篇原文寫出處，多篇原文寫篇數與出處，出處太多只列前三個。"""
    s = s or strings()[post.lang.code]
    publishers: list[str] = []
    for source in post.sources:
        if source.publisher and source.publisher not in publishers:
            publishers.append(source.publisher)
    count = len(post.sources)
    if count == 1:
        return s["source_one"].format(publishers=publishers[0]) if publishers else ""
    if not publishers:
        return s["source_count"].format(count=count)
    if len(publishers) <= 3:
        return s["source_some"].format(count=count, publishers=s["list_sep"].join(publishers))
    return s["source_many"].format(count=count, publishers=s["list_sep"].join(publishers[:3]), total=len(publishers))


def source_icons(post: Post) -> list[str | None]:
    """署名旁出處行的網站圖示，對應出處行列出的網站，最多三個。值是產物 assets/ 底下的路徑，
    None 是登記成 none 的網站。都沒填 publisher 時出處行只寫篇數，回傳空清單，維持文件圖示。"""
    icons, publishers = [], []
    for source in post.sources:
        if source.publisher and source.publisher not in publishers:
            publishers.append(source.publisher)
            icons.append(source.icon)
    return icons[:3]


ICON_DIR = ROOT / "templates" / "icons"
SVG_VIEWBOX_RE = re.compile(r'viewBox="([^"]+)"')
SVG_BODY_RE = re.compile(r"<svg\b[^>]*>(.*)</svg>", re.S)


@functools.cache
def static_version(rel: str) -> str:
    """static/ 底下檔案內容的雜湊，接在網址後面當版本號。內容改了網址就跟著變，
    瀏覽器與 Cloudflare 會當成新檔案去抓，不必等快取過期或手動清除。"""
    return hashlib.sha256((ROOT / "static" / rel).read_bytes()).hexdigest()[:10]


def icon(name: str) -> Markup:
    """內嵌 templates/icons/ 裡的 SVG。大小跟字級、顏色跟文字，讀屏軟體略過，旁邊的文字才是名稱。"""
    raw = (ICON_DIR / f"{name}.svg").read_text(encoding="utf-8")
    view_box = SVG_VIEWBOX_RE.search(raw).group(1)
    body = re.sub(r"<title>.*?</title>", "", SVG_BODY_RE.search(raw).group(1), flags=re.S).strip()
    return Markup(f'<svg class="icon" viewBox="{view_box}" width="1em" height="1em" fill="currentColor" '
                  f'aria-hidden="true" focusable="false">{body}</svg>')


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        undefined=StrictUndefined,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    # 日期與出處行依頁面的語系，從模板的 s（該語系的 strings.toml 區段）取格式
    for name, key in (("ymd", "date"), ("md", "date_short"), ("full_date", "date_full"), ("day_meta", "day_meta")):
        env.filters[name] = pass_context(lambda ctx, d, key=key: format_date(ctx["s"], key, d))
    # 署名在其他語系另有寫法時用 authors.yml 的 names，筆名與人名通常不翻
    env.filters["author_name"] = pass_context(lambda ctx, author: author["names"].get(ctx["lang"].code, author["name"]))
    env.filters["by_day"] = by_day
    env.filters["source_line"] = pass_context(lambda ctx, post: source_line(post, ctx["s"]))
    env.filters["source_icons"] = source_icons
    # 原文標題是英文時標上 lang="en"，瀏覽器才會用英文的斷字與字型
    env.tests["cjk"] = lambda text: re.search(r"[\u3400-\u9fff]", str(text)) is not None
    env.filters["iso"] = lambda d: d.isoformat()
    env.globals["icon"] = icon
    return env


def build(posts_dir: Path = ROOT / "posts", out_root: Path | None = None,
          only: list[str] | None = None,
          include_scheduled: bool = False) -> tuple[dict[str, Target], dict[str, list[Page]], list[Post]]:
    """產生產物，回傳的文章包含排程中的。產物只放已經到發布時間的，include_scheduled 時全部放，
    網址合約用這種產物，排程中的文章還沒上線也不算網址消失。"""
    config, targets = load_config(ROOT / "site.toml")
    if out_root is not None:
        for target in targets.values():
            target.out = out_root / target.out.relative_to(ROOT)
    # 測試用的文章目錄旁邊可以放自己的 authors.yml，測得到筆名與具名的署名
    authors_path = posts_dir.parent / "authors.yml"
    authors = load_authors(authors_path if authors_path.exists() else ROOT / "authors.yml")
    # 測試用的圖片放在文章目錄旁邊的 assets/，不必連網
    assets_dir = posts_dir.parent / "assets"
    store = AssetStore(assets_dir if assets_dir.exists() else None)
    favicons_path = posts_dir.parent / "favicons.toml"
    favicons = load_favicons(favicons_path if favicons_path.exists() else FAVICONS_PATH)
    strings()  # 介面文字有缺漏時在這裡就失敗
    posts = load_site(posts_dir, authors, store, favicons)
    # 測試用的文章目錄旁邊有 pages/ 時用那一份，沒有就用正式的
    pages_dir = posts_dir.parent / "pages"
    site_pages = load_site_pages(pages_dir if pages_dir.exists() else PAGES_DIR)
    published = posts if include_scheduled else [post for post in posts if not post.scheduled]
    env = make_env()
    pages = {}
    for name, target in targets.items():
        if only and name not in only:
            continue
        pages[name] = build_target(target, published, config, env, store, site_pages)
    return targets, pages, posts


def contract_pages(posts_dir: Path = ROOT / "posts") -> list[Page]:
    """網址合約的頁面，排程中的文章也算在內。另外建一份放進暫存目錄，不動正式的產物。"""
    with tempfile.TemporaryDirectory() as tmp:
        _, pages, _ = build(posts_dir, Path(tmp), ["clearnet"], include_scheduled=True)
    return pages["clearnet"]


# ---------------------------------------------------------------- 網址合約

def contract_lines(pages: list[Page]) -> list[str]:
    """clearnet 的網址與錨點。onion 的網址由固定的對應推得，不另外記。"""
    lines = []
    for page in sorted(pages, key=lambda p: p.rel):
        lines.append("/" + page.rel)
        lines += [f"\t#{anchor}" for anchor in sorted(page.anchors)]
    lines += [f"/{lang.path}feed.xml" for lang in LANGS] + ["/sitemap.xml"]
    return lines


CONTRACT_HEADER = """\
# anoni.net/news 的網址合約，由 build.py --update-contract 產生，不要手改。
#
# 每一行是 https://anoni.net/news 底下的一個路徑，縮排的 # 開頭是上一行那一頁的錨點。
# 移除任何一行都是對讀者的破壞性變更，新增則隨時可以。判準見 SPEC.md「網址合約」。
"""


def read_contract(path: Path) -> set[tuple[str, str]]:
    """讀成 (頁面, 錨點) 的集合，頁面本身的錨點是空字串。"""
    entries, current = set(), None
    if not path.exists():
        return entries
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or (line.startswith("#")):
            continue
        if line.startswith("\t#"):
            entries.add((current, line[2:]))
        else:
            current = line.strip()
            entries.add((current, ""))
    return entries


def parse_contract_lines(lines: list[str]) -> set[tuple[str, str]]:
    entries, current = set(), None
    for line in lines:
        if line.startswith("\t#"):
            entries.add((current, line[2:]))
        else:
            current = line
            entries.add((current, ""))
    return entries


# ---------------------------------------------------------------- 文件站的網址合約

@dataclass
class DocsContract:
    pages: dict[str, set[str]]
    redirects: dict[str, str]


def parse_docs_contract(text: str) -> DocsContract:
    pages: dict[str, set[str]] = {}
    redirects: dict[str, str] = {}
    current = None
    for line in text.splitlines():
        if not line or line.startswith("#"):
            continue
        if line.startswith("\t#"):
            if current is not None:
                pages[current].add(line[2:])
            continue
        if " -> " in line:
            source, dest = line.split(" -> ", 1)
            redirects[source.strip()] = dest.strip()
            current = None
            continue
        current = line.strip()
        pages.setdefault(current, set())
    return DocsContract(pages, redirects)


def load_docs_contract(path: Path | None) -> DocsContract:
    if path is None:
        try:
            with urllib.request.urlopen(DOCS_CONTRACT_URL, timeout=20) as response:
                text = response.read().decode("utf-8")
            DOCS_CONTRACT_CACHE.parent.mkdir(parents=True, exist_ok=True)
            DOCS_CONTRACT_CACHE.write_text(text, encoding="utf-8")
        except OSError as error:
            if not DOCS_CONTRACT_CACHE.exists():
                raise BuildError([f"抓不到文件站的網址合約（{error}），可以用 --docs-contract 指定本機的檔案"])
            print(f"注意：抓不到文件站的網址合約，改用快取 {DOCS_CONTRACT_CACHE}", file=sys.stderr)
            text = DOCS_CONTRACT_CACHE.read_text(encoding="utf-8")
    else:
        text = path.read_text(encoding="utf-8")
    return parse_docs_contract(text)


def check_docs_link(href: str, where: str, contract: DocsContract, problems: list[str], notices: list[str]) -> None:
    parsed = urllib.parse.urlsplit(href)
    path = "/" + urllib.parse.unquote(parsed.path)[len("/docs/"):]
    anchor = urllib.parse.unquote(parsed.fragment)
    if path in contract.redirects:
        notices.append(f"{where}：{href} 是轉址頁，建議直接連到 {contract.redirects[path]}")
    elif path not in contract.pages:
        problems.append(f"{where}：{href} 不在文件站的網址合約裡")
    elif anchor and anchor not in contract.pages[path]:
        problems.append(f"{where}：{href} 的錨點 #{anchor} 不在文件站的網址合約裡")


def check_docs_links(posts: list[Post], contract: DocsContract,
                     site_pages: dict[str, dict[str, dict]] | None = None) -> tuple[list[str], list[str]]:
    """文章、固定頁面與介面文字裡連到文件站的網址。訂閱頁連到文件站的 RSS 訂閱入門。"""
    problems, notices = [], []
    documents = [(post.html, post.where) for post in posts]
    documents += [(version["html"], version["where"]) for versions in (site_pages or {}).values()
                  for version in versions.values()]
    for text, where in documents:
        for href in hrefs(text):
            if href.startswith(DOCS_PREFIX):
                check_docs_link(href, where, contract, problems, notices)
    for code, s in strings().items():
        for key, value in s.items():
            if isinstance(value, str) and value.startswith(DOCS_PREFIX):
                check_docs_link(value, f"strings.toml 的 {code}.{key}", contract, problems, notices)
    return problems, notices


# ---------------------------------------------------------------- 產物檢查

SCRIPT_RE = re.compile(r"<script\b([^>]*)>(.*?)</script>", re.S | re.I)
RESOURCE_TAG_RE = re.compile(r"<(img|iframe|source|video|audio|embed|object|link)\b([^>]*)>", re.I)
ATTR_RE = re.compile(r'([a-zA-Z:-]+)="([^"]*)"')
RESOURCE_RELS = {"stylesheet", "icon", "preload", "prefetch", "modulepreload", "manifest", "apple-touch-icon"}
CLEARNET_HOST_RE = re.compile(r"https?://(?:[a-z0-9-]+\.)*anoni\.net\b", re.I)
CSS_URL_RE = re.compile(r"url\(\s*['\"]?([^'\")]+)")


def is_external(url: str) -> bool:
    """會讓瀏覽器連到別的主機的網址。data: 是內嵌資料，不算。"""
    return url.startswith(("http://", "https://", "//"))


def is_analytics_script(attrs: dict[str, str], analytics: dict | None) -> bool:
    """流量統計的兩支 script：送出前的過濾（內嵌）與 Umami 本體。其他 script 一律不准。"""
    if not analytics:
        return False
    if "src" not in attrs:
        return attrs.get("data-anoni") == "before-send"
    return (attrs.get("src") == analytics["src"]
            and attrs.get("data-website-id") == analytics["website_id"]
            and attrs.get("data-domains") == analytics["domains"]
            and attrs.get("data-before-send") == "anoniBeforeSend")


def check_output(target: Target, pages: list[Page]) -> list[str]:
    """第 4、5、7 項：script、對外資源、onion 的 clearnet 連結、SEO 欄位與 noindex。"""
    problems = []
    for page in pages:
        where = f"{target.name}:{page.file}"
        text = (target.out / page.file).read_text(encoding="utf-8")

        for match in SCRIPT_RE.finditer(text):
            attrs = dict(ATTR_RE.findall(match.group(1)))
            if attrs.get("type") == "application/ld+json" and "src" not in attrs:
                try:
                    json.loads(match.group(2))
                except ValueError:
                    problems.append(f"{where}：JSON-LD 無法解析成 JSON")
                continue
            if not is_analytics_script(attrs, target.analytics):
                problems.append(f"{where}：有可執行的 <script>")

        for tag, raw in RESOURCE_TAG_RE.findall(text):
            attrs = dict(ATTR_RE.findall(raw))
            if tag.lower() == "link" and not (set(attrs.get("rel", "").split()) & RESOURCE_RELS):
                continue
            for key in ("src", "href", "srcset", "data"):
                value = attrs.get(key)
                if value and is_external(html.unescape(value)):
                    problems.append(f"{where}：<{tag}> 載入站外資源 {value}")

        if not target.clearnet:
            attr_values = [html.unescape(v) for _, v in ATTR_RE.findall(text)]
            scripts = [m.group(2) for m in SCRIPT_RE.finditer(text)]
            for value in attr_values + scripts:
                for found in CLEARNET_HOST_RE.findall(value):
                    problems.append(f"{where}：onion 產物裡有 clearnet 的連結 {found}")

        for needle, label in [("<title>", "<title>"), ('name="description"', "description"),
                              ('property="og:title"', "og:title"), ('property="og:description"', "og:description"),
                              ('property="og:url"', "og:url"), ('property="og:image"', "og:image"),
                              ('property="og:type"', "og:type")]:
            if needle not in text:
                problems.append(f"{where}：缺少 {label}")
        has_noindex = re.search(r'<meta name="robots" content="noindex', text) is not None
        if page.noindex and not has_noindex:
            problems.append(f"{where}：應該帶 noindex")
        if not page.noindex and has_noindex:
            problems.append(f"{where}：不應該帶 noindex")

    if not target.clearnet:
        # 只看連結所在的位置。RSS 全文裡照錄的網址文字（例如程式碼區塊）不是連結，不算
        for name in ("feed.xml", "sitemap.xml", "robots.txt"):
            path = target.out / name
            if not path.exists():
                continue
            text = html.unescape(path.read_text(encoding="utf-8"))
            links = hrefs(text) + re.findall(r"<(?:link|loc)>([^<]*)<", text) + re.findall(r"^Sitemap:\s*(\S+)", text, re.M)
            for link in links:
                for found in CLEARNET_HOST_RE.findall(link):
                    problems.append(f"{target.name}:{name}：onion 產物裡有 clearnet 的連結 {found}")

    for css in target.out.rglob("*.css"):
        for value in CSS_URL_RE.findall(css.read_text(encoding="utf-8")):
            if is_external(value.strip()):
                problems.append(f"{target.name}:{css.relative_to(target.out)}：url() 指向站外 {value}")
    return problems


# ---------------------------------------------------------------- 對比度

# news.css 裡要檢查的文字與背景組合，淺色與深色模式各檢查一次
CONTRAST_PAIRS = [
    ("--c-text", "--c-bg"), ("--c-muted", "--c-bg"), ("--c-link", "--c-bg"),
    ("--c-text", "--c-surface"), ("--c-muted", "--c-surface"), ("--c-link", "--c-surface"),
    ("--c-headline", "--c-bg"), ("--c-headline", "--c-surface"),
    ("--c-header-text", "--c-header-bg"), ("--c-header-link", "--c-header-bg"),
]


def css_variables(css: str) -> tuple[dict[str, str], dict[str, str]]:
    """讀 :root 與深色模式 :root 裡的變數，var() 只解一層以上的參照。"""
    def block(text: str) -> dict[str, str]:
        return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", text))

    dark_match = re.search(r"@media\s*\(prefers-color-scheme:\s*dark\)\s*\{\s*:root\s*\{(.*?)\}", css, re.S)
    light_match = re.search(r"^:root\s*\{(.*?)\}", css, re.S | re.M)
    light = block(light_match.group(1)) if light_match else {}
    dark = {**light, **block(dark_match.group(1))} if dark_match else dict(light)

    def resolve(values: dict[str, str]) -> dict[str, str]:
        out = {}
        for key, value in values.items():
            seen = 0
            while (ref := re.fullmatch(r"var\((--[\w-]+)\)", value.strip())) and seen < 10:
                value, seen = values[ref.group(1)], seen + 1
            out[key] = value.strip()
        return out

    return resolve(light), resolve(dark)


def contrast(foreground: str, background: str) -> float:
    def luminance(hex_color: str) -> float:
        h = hex_color.lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    high, low = sorted([luminance(foreground), luminance(background)], reverse=True)
    return (high + 0.05) / (low + 0.05)


def check_contrast(css_path: Path) -> list[str]:
    light, dark = css_variables(css_path.read_text(encoding="utf-8"))
    problems = []
    for mode, values in (("淺色", light), ("深色", dark)):
        for fg, bg in CONTRAST_PAIRS:
            if fg not in values or bg not in values:
                problems.append(f"news.css：{mode}模式缺少 {fg} 或 {bg}")
                continue
            ratio = contrast(values[fg], values[bg])
            if ratio < 4.5:
                problems.append(f"news.css：{mode}模式 {fg} 在 {bg} 上的對比度只有 {ratio:.2f}，要到 4.5")
    return problems


# ---------------------------------------------------------------- 主程式

def run_check(args, targets, pages, posts, contract: list[Page]) -> int:
    problems, notices = [], []

    docs_problems, docs_notices = check_docs_links(all_versions(posts), load_docs_contract(args.docs_contract),
                                                   load_site_pages(PAGES_DIR))
    problems += docs_problems
    notices += docs_notices

    for name, target in targets.items():
        problems += check_output(target, pages[name])

    current = parse_contract_lines(contract_lines(contract))
    committed = read_contract(ROOT / "url_contract.txt")
    removed = committed - current
    added = current - committed
    for page, anchor in sorted(removed):
        problems.append(f"網址合約：{page}{'#' + anchor if anchor else ''} 不見了")
    if added:
        notices.append(f"網址合約：新增 {len(added)} 項，執行 --update-contract 收進合約")

    problems += check_contrast(ROOT / "static" / "css" / "news.css")

    import layout_check
    with tempfile.TemporaryDirectory() as tmp:
        fixture_targets, fixture_pages, fixture_posts = build(ROOT / "tests" / "fixtures" / "posts", Path(tmp))
        fixture_docs, _ = check_docs_links(all_versions(fixture_posts), load_docs_contract(args.docs_contract))
        problems += [f"fixtures：{p}" for p in fixture_docs]
        for name, target in fixture_targets.items():
            problems += [f"fixtures：{p}" for p in check_output(target, fixture_pages[name])]
        # 三個語系的列表頁、關於頁、最新一篇與有後續的一篇（標題區的後續提示與事件線），加上共用的 404
        layout_pages = [lang.path for lang in LANGS] + [lang.path + name + "/" for lang in LANGS for name in SITE_PAGES]
        followed = {ref for post in fixture_posts for ref in post.follows}
        newest = next((post for post in fixture_posts if not post.scheduled), None)
        earlier = next((post for post in fixture_posts if not post.scheduled and post.path.stem in followed), None)
        for post in (newest, earlier):
            if post:
                layout_pages += [post.translations.get(lang.code, post).rel for lang in LANGS]
        layout_problems, layout_notice = layout_check.run(
            fixture_targets["clearnet"].out, list(dict.fromkeys(layout_pages)) + ["404.html"],
            ROOT / ".cache" / "screenshots")
        problems += layout_problems
        if layout_notice:
            notices.append(layout_notice)

    for notice in notices:
        print(f"注意：{notice}")
    if problems:
        print(f"檢查沒過，共 {len(problems)} 項：")
        print("\n".join(f"  {p}" for p in problems))
        return 1
    scheduled = [post for post in posts if post.scheduled]
    note = f"，另有 {len(scheduled)} 篇排程中：" + "、".join(
        f"{post.slug}（{post.created:%m-%d %H:%M}）" for post in scheduled) if scheduled else ""
    print(f"檢查通過：{len(posts) - len(scheduled)} 篇文章各 {len(LANGS)} 個語系，"
          f"clearnet 與 onion 各 {len(pages['clearnet'])} 頁{note}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="產生之後執行 SPEC.md 的九項檢查")
    parser.add_argument("--update-contract", action="store_true", help="把目前的網址寫回 url_contract.txt")
    parser.add_argument("--docs-contract", type=Path, help="文件站網址合約的本機檔案，預設從 GitHub 下載")
    parser.add_argument("--watch", action="store_true", help="列出追蹤中、快要到期的事件，不產生網站")
    args = parser.parse_args()

    try:
        if args.watch:
            print(watch_report(load_site(ROOT / "posts", load_authors(ROOT / "authors.yml")), current_time().date()))
            return 0
        targets, pages, posts = build()
        contract = contract_pages() if args.update_contract or args.check else []
        if args.update_contract:
            (ROOT / "url_contract.txt").write_text(
                CONTRACT_HEADER + "\n".join(contract_lines(contract)) + "\n", encoding="utf-8")
            print("已寫回 url_contract.txt，排程中的文章也收進去了，記得把 diff 一起送審")
        if args.check:
            return run_check(args, targets, pages, posts, contract)
    except BuildError as error:
        print(f"建置失敗，共 {len(error.problems)} 項：")
        print("\n".join(f"  {p}" for p in error.problems))
        return 1
    for name, target in targets.items():
        print(f"產生 {target.out.relative_to(ROOT)}/：{len(pages[name])} 頁")
    return 0


if __name__ == "__main__":
    sys.exit(main())
