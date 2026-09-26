"""產生 anoni.net/news 的 clearnet 與 onion 兩份靜態產物。

    uv run build.py                    # 產生 public/clearnet 與 public/onion
    uv run build.py --check            # 產生之後執行 SPEC.md「驗證與 CI」的九項檢查
    uv run build.py --update-contract  # 認可目前的網址，寫回 url_contract.txt

規格見 SPEC.md，要改行為先改規格。
"""

from __future__ import annotations

import argparse
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
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent
TZ = timezone(timedelta(hours=8))
DOCS_PREFIX = "https://anoni.net/docs/"
NEWS_PREFIX = "https://anoni.net/news/"
DOCS_CONTRACT_URL = "https://raw.githubusercontent.com/anoni-net/docs/main/tools/data/url_contract.txt"
DOCS_CONTRACT_CACHE = ROOT / ".cache" / "docs_url_contract.txt"

FRONT_MATTER_KEYS = {"title", "description", "date", "slug", "sources", "authors", "categories", "draft", "image"}
REQUIRED_KEYS = {"title", "description", "date", "slug", "sources", "authors"}
SOURCE_KEYS = {"title", "url", "publisher", "date"}
AUTHOR_KEYS = {"name", "description", "url"}
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

    @property
    def image_rel(self) -> str | None:
        """front matter 的 image 在產物 assets/ 底下的相對路徑。"""
        return self.image[len(ASSETS_PREFIX):] if self.image else None

    @property
    def rel(self) -> str:
        """文章在網站裡的相對路徑，例如 2026/09/zkp-age-verification/。"""
        return f"{self.created:%Y}/{self.created:%m}/{self.slug}/"

    @property
    def guid(self) -> str:
        return f"anoni-news:{self.created:%Y}/{self.created:%m}/{self.slug}"


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
            problems.append(f"authors.yml：{key} 有不認得的欄位 {sorted(extra)}，只收 name、description、url")
        url = info.get("url")
        if url and not str(url).startswith("https://"):
            problems.append(f"authors.yml：{key} 的 url 要用 https://")
    if problems:
        raise BuildError(problems)
    return {key: {"key": key, "description": None, "url": None, **info} for key, info in data.items()}


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


def load_post(path: Path, authors: dict[str, dict]) -> Post | None:
    """讀一篇文章。草稿回傳 None，不符合規格就丟 BuildError。"""
    where = path.name
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

    categories = meta.get("categories") or []
    if not isinstance(categories, list):
        problems.append(f"{where}：categories 要是清單")
        categories = []

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
        body=body,
        anchors=anchors,
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
    where = post.path.name
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


def localize_assets(text: str, target: "Target", absolute: bool = False) -> str:
    """把 assets.anoni.net 的圖片網址換成產物裡的副本。"""
    base = target.abs_url("assets/") if absolute else target.url("assets/")
    return text.replace(f'src="{ASSETS_PREFIX}', f'src="{base}')


def load_posts(posts_dir: Path, authors: dict[str, dict], store: AssetStore | None = None) -> list[Post]:
    problems, posts = [], []
    for path in sorted(posts_dir.glob("*.md")):
        try:
            post = load_post(path, authors)
        except BuildError as error:
            problems += error.problems
            continue
        if post:
            post.html = render_markdown(post.body)
            process_images(post, store or AssetStore(), problems)
            posts.append(post)

    seen: dict[str, Post] = {}
    for post in posts:
        if post.rel in seen:
            problems.append(f"{post.path.name}：跟 {seen[post.rel].path.name} 的網址相同，slug 在同一個年月內不能重複")
        seen[post.rel] = post
        if not any(href.startswith(DOCS_PREFIX) for href in hrefs(post.html)):
            problems.append(f"{post.path.name}：至少要有一條連到 {DOCS_PREFIX} 的連結")
    if problems:
        raise BuildError(problems)
    # 新的在前。同一個時間發的，依 slug 排，讓順序固定
    return sorted(posts, key=lambda p: (-p.created.timestamp(), p.slug))


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
        "image": target.abs_url("assets/" + post.image_rel) if post.image else target.abs_url("og.png"),
        "inLanguage": "zh-Hant-TW",
        "author": authors,
        "publisher": organization,
        "citation": [{"@type": "CreativeWork", "name": s.title, "url": s.url} for s in post.sources],
    }
    if post.updated:
        data["dateModified"] = post.updated.isoformat()
    # </script> 出現在字串裡會提早結束 script 元素，跳脫掉
    return json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")


def build_target(target: Target, posts: list[Post], config: dict, env: Environment,
                 store: AssetStore | None = None) -> list[Page]:
    if target.out.exists():
        shutil.rmtree(target.out)
    shutil.copytree(ROOT / "static", target.out)
    for asset in (store.assets.values() if store else []):
        dest = target.out / "assets" / asset.rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(asset.path, dest)
    pages: list[Page] = []

    def onion_url(rel: str) -> str | None:
        if not target.clearnet:
            return None
        return f"http://news.{config['onion_host']}/{rel}"

    def write(page: Page, template: str, **context) -> None:
        html_text = env.get_template(template).render(
            target=target,
            config=config,
            url=target.url,
            page_url=target.abs_url(page.rel),
            onion_url=onion_url(page.rel),
            noindex=page.noindex,
            latest=posts[0] if posts else None,
            **{"og_image": None, **context},
        )
        dest = target.out / page.file
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(target.rewrite_html(html_text), encoding="utf-8")
        pages.append(page)

    for post in posts:
        # #sources 是模板產生的原文清單錨點，頂端那行出處連到這裡，跟內文的錨點一起收進合約
        write(Page(post.rel, post.rel + "index.html", False, post.anchors + ["sources"]), "post.html.j2",
              post=post, content=target.rewrite_html(localize_assets(post.html, target)),
              jsonld=jsonld(post, target, config),
              og_image=target.abs_url("assets/" + post.image_rel) if post.image else None)

    per_page = config["per_page"]
    groups = chunk(posts, per_page)
    for number, group in enumerate(groups, 1):
        rel = "" if number == 1 else f"page/{number}/"
        write(Page(rel, rel + "index.html", number > 1), "list.html.j2",
              kind="index", heading="anoni.net 新聞導讀", posts=group, number=number, total=len(groups),
              prev_rel=("" if number == 2 else f"page/{number - 1}/") if number > 1 else None,
              next_rel=f"page/{number + 1}/" if number < len(groups) else None)

    years: dict[int, list[Post]] = {}
    months: dict[tuple[int, int], list[Post]] = {}
    for post in posts:
        years.setdefault(post.created.year, []).append(post)
        months.setdefault((post.created.year, post.created.month), []).append(post)
    for year, group in years.items():
        write(Page(f"{year}/", f"{year}/index.html", True), "list.html.j2",
              kind="archive", heading=f"{year} 年的文章", posts=group, number=1, total=1, prev_rel=None, next_rel=None)
    for (year, month), group in months.items():
        write(Page(f"{year}/{month:02d}/", f"{year}/{month:02d}/index.html", True), "list.html.j2",
              kind="archive", heading=f"{year} 年 {month} 月的文章", posts=group, number=1, total=1,
              prev_rel=None, next_rel=None)

    write(Page("404.html", "404.html", True), "404.html.j2")

    feed_posts = posts[:config["feed_items"]]
    feed = env.get_template("feed.xml.j2").render(
        target=target, config=config,
        items=[{
            "post": post,
            "link": target.abs_url(post.rel),
            "pub_date": format_datetime(post.created),
            "content": target.rewrite_html(localize_assets(env.get_template("_post_body.html.j2").render(
                post=post, content=post.html, url=target.url), target, absolute=True)),
        } for post in feed_posts],
        build_date=format_datetime(feed_posts[0].created) if feed_posts else None,
    )
    (target.out / "feed.xml").write_text(feed, encoding="utf-8")

    sitemap = env.get_template("sitemap.xml.j2").render(
        urls=[(target.abs_url(""), None)] + [
            (target.abs_url(p.rel), (p.updated or p.created).date().isoformat()) for p in posts
        ],
    )
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


def source_line(post: Post) -> str:
    """列表與頭條上的出處行。一篇原文寫出處，多篇原文寫篇數與出處，出處太多只列前三個。"""
    publishers: list[str] = []
    for source in post.sources:
        if source.publisher and source.publisher not in publishers:
            publishers.append(source.publisher)
    count = len(post.sources)
    if count == 1:
        return f"原文來自 {publishers[0]}" if publishers else ""
    if not publishers:
        return f"整理 {count} 篇原文"
    if len(publishers) <= 3:
        return f"整理 {count} 篇原文，來自 {'、'.join(publishers)}"
    return f"整理 {count} 篇原文，來自 {'、'.join(publishers[:3])} 等 {len(publishers)} 個出處"


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        undefined=StrictUndefined,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["ymd"] = lambda d: f"{d.year} 年 {d.month} 月 {d.day} 日"
    env.filters["md"] = lambda d: f"{d.month} 月 {d.day} 日"
    env.filters["weekday"] = lambda d: "星期" + "一二三四五六日"[d.weekday()]
    env.filters["by_day"] = by_day
    env.filters["source_line"] = source_line
    # 原文標題是英文時標上 lang="en"，瀏覽器才會用英文的斷字與字型
    env.tests["cjk"] = lambda text: re.search(r"[\u3400-\u9fff]", str(text)) is not None
    env.filters["iso"] = lambda d: d.isoformat()
    return env


def build(posts_dir: Path = ROOT / "posts", out_root: Path | None = None,
          only: list[str] | None = None) -> tuple[dict[str, Target], dict[str, list[Page]], list[Post]]:
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
    posts = load_posts(posts_dir, authors, store)
    env = make_env()
    pages = {}
    for name, target in targets.items():
        if only and name not in only:
            continue
        pages[name] = build_target(target, posts, config, env, store)
    return targets, pages, posts


# ---------------------------------------------------------------- 網址合約

def contract_lines(pages: list[Page]) -> list[str]:
    """clearnet 的網址與錨點。onion 的網址由固定的對應推得，不另外記。"""
    lines = []
    for page in sorted(pages, key=lambda p: p.rel):
        lines.append("/" + page.rel)
        lines += [f"\t#{anchor}" for anchor in sorted(page.anchors)]
    lines += ["/feed.xml", "/sitemap.xml"]
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


def check_docs_links(posts: list[Post], contract: DocsContract) -> tuple[list[str], list[str]]:
    problems, notices = [], []
    for post in posts:
        for href in hrefs(post.html):
            if not href.startswith(DOCS_PREFIX):
                continue
            parsed = urllib.parse.urlsplit(href)
            path = "/" + urllib.parse.unquote(parsed.path)[len("/docs/"):]
            anchor = urllib.parse.unquote(parsed.fragment)
            if path in contract.redirects:
                notices.append(f"{post.path.name}：{href} 是轉址頁，建議直接連到 {contract.redirects[path]}")
                continue
            if path not in contract.pages:
                problems.append(f"{post.path.name}：{href} 不在文件站的網址合約裡")
            elif anchor and anchor not in contract.pages[path]:
                problems.append(f"{post.path.name}：{href} 的錨點 #{anchor} 不在文件站的網址合約裡")
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


def check_output(target: Target, pages: list[Page]) -> list[str]:
    """第 4、5、7 項：script、對外資源、onion 的 clearnet 連結、SEO 欄位與 noindex。"""
    problems = []
    for page in pages:
        where = f"{target.name}:{page.file}"
        text = (target.out / page.file).read_text(encoding="utf-8")

        for match in SCRIPT_RE.finditer(text):
            attrs = dict(ATTR_RE.findall(match.group(1)))
            if attrs.get("type") != "application/ld+json" or "src" in attrs:
                problems.append(f"{where}：有可執行的 <script>")
                continue
            try:
                json.loads(match.group(2))
            except ValueError:
                problems.append(f"{where}：JSON-LD 無法解析成 JSON")

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

def run_check(args, targets, pages, posts) -> int:
    problems, notices = [], []

    docs_problems, docs_notices = check_docs_links(posts, load_docs_contract(args.docs_contract))
    problems += docs_problems
    notices += docs_notices

    for name, target in targets.items():
        problems += check_output(target, pages[name])

    current = parse_contract_lines(contract_lines(pages["clearnet"]))
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
        fixture_docs, _ = check_docs_links(fixture_posts, load_docs_contract(args.docs_contract))
        problems += [f"fixtures：{p}" for p in fixture_docs]
        for name, target in fixture_targets.items():
            problems += [f"fixtures：{p}" for p in check_output(target, fixture_pages[name])]
        layout_problems, layout_notice = layout_check.run(
            fixture_targets["clearnet"].out, ["", fixture_posts[0].rel if fixture_posts else "", "404.html"],
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
    print(f"檢查通過：{len(posts)} 篇文章，clearnet 與 onion 各 {len(pages['clearnet'])} 頁")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="產生之後執行 SPEC.md 的九項檢查")
    parser.add_argument("--update-contract", action="store_true", help="把目前的網址寫回 url_contract.txt")
    parser.add_argument("--docs-contract", type=Path, help="文件站網址合約的本機檔案，預設從 GitHub 下載")
    args = parser.parse_args()

    try:
        targets, pages, posts = build()
        if args.update_contract:
            (ROOT / "url_contract.txt").write_text(
                CONTRACT_HEADER + "\n".join(contract_lines(pages["clearnet"])) + "\n", encoding="utf-8")
            print("已寫回 url_contract.txt，記得把 diff 一起送審")
        if args.check:
            return run_check(args, targets, pages, posts)
    except BuildError as error:
        print(f"建置失敗，共 {len(error.problems)} 項：")
        print("\n".join(f"  {p}" for p in error.problems))
        return 1
    for name, target in targets.items():
        print(f"產生 {target.out.relative_to(ROOT)}/：{len(pages[name])} 頁")
    return 0


if __name__ == "__main__":
    sys.exit(main())
