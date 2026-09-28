"""build.py 的測試。每一項檢查都放一個故意寫壞的例子，確認它真的會報錯。

檢查全部通過不代表內容沒問題，也可能是檢查本身失效。版面檢查就發生過：拿
scrollWidth 跟 window.innerWidth 比，手機模式下兩者一起被撐寬，永遠通過。
"""

from __future__ import annotations

import re
import shutil
import sys
import textwrap
from datetime import datetime
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
ONION_HOST = build.load_config(ROOT / "site.toml")[0]["onion_host"]
AUTHORS = build.load_authors(FIXTURES / "authors.yml")

GOOD = """\
---
title: 測試文章
description: 一句話的描述。
date: 2026-09-18
slug: test-post
sources:
  - title: Source
    url: https://example.org/
authors:
  - anoni-net
---

內文，延伸閱讀：[威脅模型](https://anoni.net/docs/basics/threat-model/)
"""


def write_post(tmp_path: Path, text: str, name: str = "2026-09-18-test-post.md") -> Path:
    path = tmp_path / name
    path.write_text(textwrap.dedent(text), encoding="utf-8")
    return path


def problems_of(tmp_path: Path, text: str, name: str = "2026-09-18-test-post.md") -> list[str]:
    try:
        build.load_post(write_post(tmp_path, text, name), AUTHORS)
    except build.BuildError as error:
        return error.problems
    return []


# ---------------------------------------------------------------- front matter

def test_good_post_loads(tmp_path):
    post = build.load_post(write_post(tmp_path, GOOD), AUTHORS)
    assert post.rel == "2026/09/test-post/"
    assert post.guid == "anoni-news:2026/09/test-post"


def test_draft_is_skipped(tmp_path):
    text = GOOD.replace("authors:", "draft: true\nauthors:")
    assert build.load_post(write_post(tmp_path, text), AUTHORS) is None


@pytest.mark.parametrize("old, new, expected", [
    ("title: 測試文章\n", "", "缺少必填欄位"),
    ("slug: test-post\n", "slug: test-post\nsubtitle: x\n", "不認得的欄位"),
    ("slug: test-post", "slug: Test_Post", "slug"),
    ("date: 2026-09-18", "date: 2026-09-19", "檔名的日期跟 date 不同"),
    ("  - anoni-net", "  - nobody", "不在 authors.yml"),
    ("sources:\n  - title: Source\n    url: https://example.org/\n", "sources: []\n", "sources 至少要有一筆"),
    ("    url: https://example.org/", "    url: example.org", "完整網址"),
    ("    url: https://example.org/", "    url: https://example.org/\n    lang: en", "不認得的欄位"),
])
def test_front_matter_problems(tmp_path, old, new, expected):
    problems = problems_of(tmp_path, GOOD.replace(old, new))
    assert any(expected in p for p in problems), problems


def test_filename_slug_must_match(tmp_path):
    problems = problems_of(tmp_path, GOOD, "2026-09-18-other-slug.md")
    assert any("檔名的 slug" in p for p in problems)


def test_date_mapping(tmp_path):
    text = GOOD.replace("date: 2026-09-18", "date:\n  created: 2026-09-18\n  updated: 2026-09-20")
    post = build.load_post(write_post(tmp_path, text), AUTHORS)
    assert post.updated == datetime(2026, 9, 20, tzinfo=build.TZ)


# ---------------------------------------------------------------- 內文

@pytest.mark.parametrize("body, expected", [
    ("## 沒有錨點\n", "要用 {#id} 寫明錨點"),
    ("# 一級標題 {#h1}\n", "不能用一級標題"),
    ("## 大寫 {#Bad_Id}\n", "只能用小寫英文"),
    ("## 甲 {#same}\n\n## 乙 {#same}\n", "重複"),
])
def test_heading_problems(tmp_path, body, expected):
    problems = problems_of(tmp_path, GOOD + "\n" + body)
    assert any(expected in p for p in problems), problems


def test_heading_inside_fence_is_ignored(tmp_path):
    text = GOOD + "\n```\n# 這是程式碼\n```\n"
    assert problems_of(tmp_path, text) == []


def test_docs_link_is_optional(tmp_path):
    # 延伸閱讀是文件站有合適的頁面才放，沒有連到文件站也能建置
    posts = tmp_path / "posts"
    posts.mkdir()
    write_post(posts, GOOD.replace("內文，延伸閱讀：[威脅模型](https://anoni.net/docs/basics/threat-model/)", "內文。"))
    assert len(build.load_posts(posts, AUTHORS)) == 1


def test_slug_unique_within_month(tmp_path):
    posts = tmp_path / "posts"
    posts.mkdir()
    write_post(posts, GOOD)
    write_post(posts, GOOD.replace("2026-09-18", "2026-09-20"), "2026-09-20-test-post.md")
    with pytest.raises(build.BuildError, match="網址相同"):
        build.load_posts(posts, AUTHORS)


# ---------------------------------------------------------------- 文件站的網址合約

DOCS_CONTRACT = """\
# comment
/
/basics/threat-model/
\t#三個基本問題
/old/ -> /basics/threat-model/
/tools/rss/
/zh-cn/tools/rss/
/en/tools/rss/
"""


@pytest.mark.parametrize("href, problem, notice", [
    ("https://anoni.net/docs/basics/threat-model/", False, False),
    ("https://anoni.net/docs/basics/threat-model/#%E4%B8%89%E5%80%8B%E5%9F%BA%E6%9C%AC%E5%95%8F%E9%A1%8C", False, False),
    ("https://anoni.net/docs/basics/threat-model/#不存在", True, False),
    ("https://anoni.net/docs/basics/no-such-page/", True, False),
    ("https://anoni.net/docs/old/", False, True),
])
def test_docs_links(tmp_path, href, problem, notice):
    post = build.load_post(write_post(tmp_path, GOOD), AUTHORS)
    post.html = f'<a href="{href}">x</a>'
    problems, notices = build.check_docs_links([post], build.parse_docs_contract(DOCS_CONTRACT))
    assert bool(problems) is problem
    assert bool(notices) is notice


def test_rss_links_point_to_the_subscribe_page(fixture_site):
    """頁面上的 RSS 連結指向同語系的訂閱頁，閱讀器用的自動探索仍然指向 feed。"""
    targets, _, _ = fixture_site
    for lang in ("", "zh-cn/", "en/"):
        page = (targets["clearnet"].out / lang / "index.html").read_text(encoding="utf-8")
        assert page.count(f'href="/news/{lang}subscribe/"') == 2  # 刊頭與頁尾
        assert f'type="application/rss+xml" title=' in page and f'href="https://anoni.net/news/{lang}feed.xml"' in page
    post = (targets["clearnet"].out / "2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
    assert post.count('href="/news/subscribe/"') == 2  # 文章末與頁尾


def test_subscribe_page_shows_the_feed_of_each_target(fixture_site):
    """訂閱頁代入的 feed 網址跟著語系與輸出目標，onion 版顯示 onion 的網址。"""
    targets, _, _ = fixture_site
    for lang in ("", "zh-cn/", "en/"):
        clearnet = (targets["clearnet"].out / lang / "subscribe" / "index.html").read_text(encoding="utf-8")
        onion = (targets["onion"].out / lang / "subscribe" / "index.html").read_text(encoding="utf-8")
        assert f"https://anoni.net/news/{lang}feed.xml" in clearnet and build.FEED_URL_PLACEHOLDER not in clearnet
        assert f"http://news.{ONION_HOST}/{lang}feed.xml" in onion and "https://anoni.net/news/" not in onion


def test_site_page_docs_links_are_checked(tmp_path):
    contract = build.parse_docs_contract(DOCS_CONTRACT.replace("/en/tools/rss/\n", ""))
    pages = {"subscribe": {"en": {"html": '<a href="https://anoni.net/docs/en/tools/rss/">x</a>', "where": "pages/en/subscribe.md"}}}
    problems, _ = build.check_docs_links([], contract, pages)
    assert problems == ["pages/en/subscribe.md：https://anoni.net/docs/en/tools/rss/ 不在文件站的網址合約裡"]


# ---------------------------------------------------------------- onion 改寫

def onion_target():
    _, targets = build.load_config(ROOT / "site.toml")
    return targets["onion"]


@pytest.mark.parametrize("url, expected_host", [
    ("https://anoni.net/news/2026/09/x/", "http://news."),
    ("https://anoni.net/docs/tools/", "http://docs."),
    ("https://form.anoni.net/s/abc", "http://form."),
    ("https://anoni.net/", "http://anoninet"),
    ("https://example.org/", "https://example.org/"),
])
def test_onion_rewrite(url, expected_host):
    assert onion_target().rewrite(url).startswith(expected_host)


def test_rewrite_only_touches_href():
    text = '<a href="https://anoni.net/docs/">x</a><code>https://anoni.net/docs/</code>'
    out = onion_target().rewrite_html(text)
    assert 'href="http://docs.' in out
    assert "<code>https://anoni.net/docs/</code>" in out


# ---------------------------------------------------------------- 產物檢查

@pytest.fixture(scope="module")
def fixture_site(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    targets, pages, posts = build.build(FIXTURES / "posts", out)
    return targets, pages, posts


def test_fixture_site_is_clean(fixture_site):
    targets, pages, _ = fixture_site
    for name, target in targets.items():
        assert build.check_output(target, pages[name]) == []


def test_fixture_pages_and_order(fixture_site):
    _, pages, posts = fixture_site
    assert [p.slug for p in posts] == ["layout-stress-test", "zkp-age-verification", "age-verification-roundup", "onion-link-rewrite"]
    rels = {p.rel for p in pages["clearnet"]}
    assert {"", "2026/", "2026/09/", "2026/08/", "404.html", "2026/09/zkp-age-verification/"} <= rels


def tamper(target, page_file, old, new):
    path = target.out / page_file
    path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")


@pytest.mark.parametrize("old, new, expected", [
    ("</head>", "<script>alert(1)</script></head>", "可執行的 <script>"),
    ("</head>", '<script type="application/ld+json">{bad json</script></head>', "無法解析"),
    ("</head>", '<link rel="stylesheet" href="https://fonts.example.org/a.css"></head>', "站外資源"),
    ("</head>", '<img src="//cdn.example.org/x.png"></head>', "站外資源"),
    ('<meta property="og:image"', '<meta property="og:imagex"', "缺少 og:image"),
])
def test_output_check_catches(tmp_path, old, new, expected):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["clearnet"])
    target = targets["clearnet"]
    tamper(target, "index.html", old, new)
    problems = build.check_output(target, pages["clearnet"])
    assert any(expected in p for p in problems), problems


def test_analytics_only_on_clearnet(fixture_site):
    targets, _, _ = fixture_site
    clearnet = (targets["clearnet"].out / "index.html").read_text(encoding="utf-8")
    onion = (targets["onion"].out / "index.html").read_text(encoding="utf-8")
    assert 'src="https://aa.anoni.net/script.js"' in clearnet
    assert 'data-domains="anoni.net"' in clearnet
    assert "Umami" in clearnet
    assert "aa.anoni.net" not in onion
    assert "anoniBeforeSend" not in onion
    assert "Umami" not in onion


@pytest.mark.parametrize("old, new", [
    # 換掉 Umami 的來源、網站 ID，或拿掉 domains 限制，都不再是允許的那一支
    ('src="https://aa.anoni.net/script.js"', 'src="https://evil.example.org/script.js"'),
    ('data-website-id="', 'data-website-id="x'),
    ('data-domains="anoni.net"', 'data-domains=""'),
    # 其他內嵌 script 不能借用過濾那一支的例外
    ("</body>", "<script>alert(1)</script></body>"),
])
def test_analytics_exception_is_narrow(tmp_path, old, new):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["clearnet"])
    target = targets["clearnet"]
    tamper(target, "index.html", old, new)
    problems = build.check_output(target, pages["clearnet"])
    assert any("可執行的 <script>" in p for p in problems), problems


def test_onion_rejects_analytics_script(tmp_path):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["onion"])
    target = targets["onion"]
    tamper(target, "index.html", "</head>",
           '<script defer src="https://aa.anoni.net/script.js" data-website-id="3790f14b-870c-4c29-83eb-dbb2977c65a9" '
           'data-domains="anoni.net" data-before-send="anoniBeforeSend"></script></head>')
    problems = build.check_output(target, pages["onion"])
    assert any("可執行的 <script>" in p for p in problems), problems
    assert any("clearnet 的連結" in p for p in problems), problems


def test_onion_check_catches_clearnet_link(tmp_path):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["onion"])
    target = targets["onion"]
    tamper(target, "index.html", "</main>", '<a href="https://anoni.net/docs/">x</a></main>')
    problems = build.check_output(target, pages["onion"])
    assert any("clearnet 的連結" in p for p in problems), problems


def test_onion_feed_link_is_caught(tmp_path):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["onion"])
    target = targets["onion"]
    feed = target.out / "feed.xml"
    feed.write_text(feed.read_text(encoding="utf-8").replace("</channel>", "<item><link>https://anoni.net/news/x/</link></item></channel>"))
    assert any("feed.xml" in p for p in build.check_output(target, pages["onion"]))


def test_story_pager_links_neighbours(fixture_site):
    targets, _, posts = fixture_site
    out = targets["clearnet"].out
    order = [p.slug for p in posts]  # 由新到舊，跟首頁時間軸相同

    def pager(slug):
        post = next(p for p in posts if p.slug == slug)
        text = (out / post.rel / "index.html").read_text(encoding="utf-8")
        nav = text[text.index('class="pager pager--story"'):]
        nav = nav[:nav.index("</nav>")]
        return nav

    newest, middle, oldest = order[0], order[1], order[-1]
    assert "較新的一篇" not in pager(newest) and "較舊的一篇" in pager(newest)
    assert "較新的一篇" not in pager(newest)
    assert "較新的一篇" in pager(oldest) and "較舊的一篇" not in pager(oldest)
    nav = pager(middle)
    assert f"/news/{posts[0].rel}" in nav and f"/news/{posts[2].rel}" in nav
    assert posts[0].title in nav and posts[2].title in nav
    for slug in order:
        assert "所有文章" in pager(slug)


def test_icon_is_inline_and_hidden_from_screen_readers():
    svg = build.icon("rss")
    assert svg.startswith('<svg class="icon" viewBox="0 0 24 24"')
    assert 'aria-hidden="true"' in svg and 'focusable="false"' in svg
    assert 'fill="currentColor"' in svg
    # 來源檔的 title、id、xmlns 不帶進頁面
    assert "<title>" not in build.icon("torproject")
    assert "id=" not in svg and "xmlns" not in svg


def test_every_icon_file_is_recorded_with_its_license():
    readme = (build.ICON_DIR / "README.md").read_text(encoding="utf-8")
    for svg in build.ICON_DIR.glob("*.svg"):
        assert f"`{svg.name}`" in readme, svg.name


def test_icons_render_on_both_targets(fixture_site):
    targets, _, _ = fixture_site
    for name in ("clearnet", "onion"):
        index = (targets[name].out / "index.html").read_text(encoding="utf-8")
        assert index.count('<svg class="icon"') >= 4  # 刊頭兩個、頁尾至少兩個
    # onion 版本的連結只在 clearnet 出現，Tor 圖示也一樣
    tor = str(build.icon("torproject"))
    assert tor in (targets["clearnet"].out / "index.html").read_text(encoding="utf-8")
    assert tor not in (targets["onion"].out / "index.html").read_text(encoding="utf-8")


def test_text_stays_separated_without_css(fixture_site):
    """閱讀器模式、複製文字與 RSS 閱讀器看不到 CSS，圖示與前後篇的標籤都要靠真正的空格跟文字分開。"""
    targets, _, posts = fixture_site
    page = (targets["clearnet"].out / posts[1].rel / "index.html").read_text(encoding="utf-8")
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", re.sub(r"<svg.*?</svg>", "", page, flags=re.S)))
    assert f"較新的一篇 {posts[0].title}" in text
    assert f"較舊的一篇 {posts[2].title}" in text
    assert re.search(r"</svg>[^ <]", page) is None, "圖示後面要接空格"


def test_noindex_expectations(fixture_site):
    targets, _, _ = fixture_site
    out = targets["clearnet"].out
    assert 'content="noindex' not in (out / "index.html").read_text(encoding="utf-8")
    assert 'content="noindex' in (out / "2026" / "index.html").read_text(encoding="utf-8")
    assert 'content="noindex' in (out / "404.html").read_text(encoding="utf-8")


def test_css_url_must_stay_local(tmp_path):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["clearnet"])
    target = targets["clearnet"]
    css = target.out / "css" / "news.css"
    css.write_text(css.read_text(encoding="utf-8") + "\nbody{background:url(https://example.org/x.png)}\n")
    assert any("url() 指向站外" in p for p in build.check_output(target, pages["clearnet"]))


# ---------------------------------------------------------------- RSS 與 JSON-LD

def test_feed(fixture_site):
    targets, _, _ = fixture_site
    feed = (targets["onion"].out / "feed.xml").read_text(encoding="utf-8")
    assert "<pubDate>Fri, 18 Sep 2026 00:00:00 +0800</pubDate>" in feed
    assert "<guid isPermaLink=\"false\">anoni-news:2026/09/zkp-age-verification</guid>" in feed
    assert "<dc:creator>夜梟</dc:creator>" in feed
    assert "@" not in feed.split("<item>")[1].split("</dc:creator>")[0]
    assert "anoni.net/news" not in feed


def test_jsonld_author_types(fixture_site):
    targets, _, posts = fixture_site
    post = next(p for p in posts if p.slug == "layout-stress-test")
    import json
    data = json.loads(build.jsonld(post, targets["clearnet"], {"homepage": "https://anoni.net/"}))
    assert [a["@type"] for a in data["author"]] == ["Person", "Person"]
    assert "url" not in data["author"][0]
    assert data["dateModified"].startswith("2026-09-20")


# ---------------------------------------------------------------- 網址合約

def test_contract_detects_removal(fixture_site):
    _, pages, _ = fixture_site
    current = build.parse_contract_lines(build.contract_lines(pages["clearnet"]))
    committed = current | {("/2026/09/removed/", "")}
    assert committed - current == {("/2026/09/removed/", "")}


def test_contract_includes_anchors(fixture_site):
    _, pages, _ = fixture_site
    lines = build.contract_lines(pages["clearnet"])
    assert "/2026/09/layout-stress-test/" in lines
    assert "\t#results" in lines


# ---------------------------------------------------------------- 對比度

def test_contrast_values():
    assert round(build.contrast("#006d99", "#ffffff"), 2) == 5.76
    assert round(build.contrast("#0089bf", "#ffffff"), 2) == 3.94


def test_contrast_check_passes_and_catches(tmp_path):
    css = ROOT / "static" / "css" / "news.css"
    assert build.check_contrast(css) == []
    bad = tmp_path / "bad.css"
    bad.write_text(css.read_text(encoding="utf-8").replace("--c-link: var(--brand-cyan-800);", "--c-link: var(--brand-cyan-500);"))
    assert any("--c-link" in p for p in build.check_contrast(bad))


# ---------------------------------------------------------------- 多篇原文

def source_post(tmp_path, sources_yaml: str):
    text = GOOD.replace("sources:\n  - title: Source\n    url: https://example.org/\n", sources_yaml)
    return build.load_post(write_post(tmp_path, text), AUTHORS)


@pytest.mark.parametrize("sources_yaml, expected", [
    ("sources:\n  - title: A\n    url: https://a.example/\n    publisher: EFF\n", "原文來自 EFF"),
    ("sources:\n  - title: A\n    url: https://a.example/\n", ""),
    ("sources:\n  - title: A\n    url: https://a.example/\n  - title: B\n    url: https://b.example/\n", "整理 2 篇原文"),
    ("sources:\n  - title: A\n    url: https://a.example/\n    publisher: EFF\n"
     "  - title: B\n    url: https://b.example/\n    publisher: EFF\n"
     "  - title: C\n    url: https://c.example/\n    publisher: OONI\n", "整理 3 篇原文，來自 EFF、OONI"),
    ("sources:\n" + "".join(f"  - title: {n}\n    url: https://{n}.example/\n    publisher: P{n}\n" for n in "abcd"),
     "整理 4 篇原文，來自 Pa、Pb、Pc 等 4 個出處"),
])
def test_source_line(tmp_path, sources_yaml, expected):
    assert build.source_line(source_post(tmp_path, sources_yaml)) == expected


def test_multi_source_post_renders(fixture_site):
    targets, _, posts = fixture_site
    out = targets["clearnet"].out
    page = (out / "2026" / "09" / "age-verification-roundup" / "index.html").read_text(encoding="utf-8")
    assert "原文（5 篇）" in page
    # 頂端一行出處連到文末的原文清單，清單排在內文之後
    # 行首是出處行列出的三個網站的圖示：EFF 有圖示，Access Now 與 OONI 在 example.org，登記成通用圖示
    stack = page[page.index('<a href="#sources"><span class="favicon-stack">'):page.index('整理 5 篇原文')]
    assert stack.count("<img ") == 1 and stack.count('<svg class="icon"') == 2, stack
    assert '</span> <span>整理 5 篇原文，來自 EFF、Access Now、OONI</span></a>' in page
    assert page.index('class="story__body content"') < page.index('id="sources"')
    assert page.count('class="source-slip__item"') == 5
    assert "整理 5 篇原文，來自 EFF、Access Now、OONI" in (out / "index.html").read_text(encoding="utf-8")
    import json
    post = next(p for p in posts if p.slug == "age-verification-roundup")
    data = json.loads(build.jsonld(post, targets["clearnet"], {"homepage": "https://anoni.net/"}))
    assert len(data["citation"]) == 5


# ---------------------------------------------------------------- 圖片

ASSET = "https://assets.anoni.net/news/2026/09/test-post/"


def make_image(path: Path, size=(400, 300), fmt="WEBP", exif: bool = False, noise: bool = False):
    from PIL import Image
    path.parent.mkdir(parents=True, exist_ok=True)
    if noise:
        import os
        image = Image.frombytes("RGB", size, os.urandom(size[0] * size[1] * 3))
    else:
        image = Image.new("RGB", size, "#003e57")
    kwargs = {}
    if exif:
        data = Image.Exif()
        data[0x010F] = "Example Camera"  # Make
        kwargs["exif"] = data
    image.save(path, fmt, **kwargs)


def image_problems(tmp_path, body: str, files: dict | None = None, front: str = "") -> list[str]:
    posts, assets = tmp_path / "posts", tmp_path / "assets"
    posts.mkdir()
    for rel, options in (files or {"2026/09/test-post/a.webp": {}}).items():
        make_image(assets / rel, **options)
    write_post(posts, GOOD.replace("authors:", front + "authors:") + "\n" + body)
    try:
        build.load_posts(posts, AUTHORS, build.AssetStore(assets))
    except build.BuildError as error:
        return error.problems
    return []


def test_good_image_passes(tmp_path):
    assert image_problems(tmp_path, f'![替代文字]({ASSET}a.webp "圖：anoni.net 社群")\n') == []


@pytest.mark.parametrize("body, expected", [
    ('![替代文字](https://example.org/a.png "圖：x")\n', "不在 assets.anoni.net"),
    (f'![]({ASSET}a.webp "圖：x")\n', "缺少替代文字"),
    (f'![替代文字]({ASSET}a.webp)\n', "缺少圖說"),
    (f'文字 ![替代文字]({ASSET}a.webp "圖：x") 文字\n', "要獨立成一段"),
    (f'![替代文字]({ASSET}a.svg "圖：x")\n', "只收 WebP、PNG、JPEG"),
    (f'![替代文字]({ASSET}missing.webp "圖：x")\n', "找不到圖片"),
])
def test_image_problems(tmp_path, body, expected):
    problems = image_problems(tmp_path, body)
    assert any(expected in p for p in problems), problems


def test_missing_caption_is_not_reported_twice(tmp_path):
    problems = image_problems(tmp_path, f'![替代文字]({ASSET}a.webp)\n')
    assert not any("要獨立成一段" in p for p in problems), problems


@pytest.mark.parametrize("options, expected", [
    ({"fmt": "JPEG", "exif": True}, "EXIF"),
    ({"size": (2400, 300)}, "長邊不能超過"),
    ({"size": (1000, 1000), "fmt": "PNG", "noise": True}, "單張不能超過"),
])
def test_image_file_checks(tmp_path, options, expected):
    name = "a.jpg" if options.get("fmt") == "JPEG" else ("a.png" if options.get("fmt") == "PNG" else "a.webp")
    problems = image_problems(tmp_path, f'![替代文字]({ASSET}{name} "圖：x")\n',
                              {f"2026/09/test-post/{name}": options})
    assert any(expected in p for p in problems), problems


def test_front_matter_image_must_be_on_assets(tmp_path):
    problems = image_problems(tmp_path, "", front="image: https://example.org/og.png\n")
    assert any("image 要是" in p for p in problems), problems


def test_figure_is_localized_per_target(fixture_site):
    targets, _, _ = fixture_site
    rel = "2026/09/layout-stress-test/figure-1.webp"
    clearnet = (targets["clearnet"].out / "2026/09/layout-stress-test/index.html").read_text(encoding="utf-8")
    assert f'<figure><img src="/news/assets/{rel}"' in clearnet
    assert 'width="1600" height="900" loading="lazy" decoding="async"' in clearnet
    assert "<figcaption>圖：anoni.net 社群" in clearnet
    onion = (targets["onion"].out / "2026/09/layout-stress-test/index.html").read_text(encoding="utf-8")
    assert f'<img src="/assets/{rel}"' in onion
    assert (targets["onion"].out / "assets" / rel).exists()
    feed = (targets["clearnet"].out / "feed.xml").read_text(encoding="utf-8")
    assert f"src=&#34;https://anoni.net/news/assets/{rel}&#34;" in feed


def test_og_image_from_front_matter(fixture_site):
    targets, _, _ = fixture_site
    page = (targets["onion"].out / "2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
    assert "og:image\" content=\"http://news." in page and "/assets/2026/09/zkp-age-verification/og.webp" in page
    other = (targets["onion"].out / "2026/08/onion-link-rewrite/index.html").read_text(encoding="utf-8")
    assert "/og.png" in other


# ---------------------------------------------------------------- 焦點（pin）

def test_pin_must_be_bool(tmp_path):
    problems = problems_of(tmp_path, GOOD.replace("authors:", "pin: yes please\nauthors:"))
    assert any("pin 只能寫 true 或 false" in p for p in problems), problems


def test_only_one_pin(tmp_path):
    posts = tmp_path / "posts"
    posts.mkdir()
    write_post(posts, GOOD.replace("authors:", "pin: true\nauthors:"))
    write_post(posts, GOOD.replace("authors:", "pin: true\nauthors:").replace("2026-09-18", "2026-09-20"),
               "2026-09-20-test-post.md")
    with pytest.raises(build.BuildError, match="頭條只能有一篇"):
        build.load_posts(posts, AUTHORS)


def test_featured_on_front_page_and_still_in_timeline(fixture_site):
    targets, _, _ = fixture_site
    out = targets["clearnet"].out
    index = (out / "index.html").read_text(encoding="utf-8")
    featured = index.split('<section class="featured')[1].split("</section>")[0]
    assert "焦點" in featured and "零知識證明用在年齡驗證的限制" in featured
    assert '<img class="featured__image" src="/news/assets/2026/09/zkp-age-verification/og.webp"' in featured
    timeline = index.split("</section>", 1)[1]
    assert "/news/2026/09/zkp-age-verification/" in timeline
    # 焦點只在首頁，封存頁沒有
    assert 'class="featured' not in (out / "2026" / "09" / "index.html").read_text(encoding="utf-8")


def write_versions(posts: Path, text: str, name: str = "2026-09-18-test-post.md",
                   overrides: dict[str, tuple[str, str]] | None = None) -> None:
    """同一篇寫成三個語系。overrides 依語系代碼替換某一段文字，用來做出不一致的版本。"""
    for lang in build.LANGS:
        directory = posts / lang.dir if lang.dir else posts
        directory.mkdir(parents=True, exist_ok=True)
        version = text
        if overrides and lang.code in overrides:
            old, new = overrides[lang.code]
            assert old in version
            version = version.replace(old, new)
        write_post(directory, version, name)


def test_no_pin_no_featured(tmp_path):
    posts = tmp_path / "posts"
    write_versions(posts, GOOD)
    shutil.copy(FIXTURES / "authors.yml", tmp_path / "authors.yml")
    shutil.copy(FIXTURES / "favicons.toml", tmp_path / "favicons.toml")
    targets, _, _ = build.build(posts, tmp_path / "out", ["clearnet"])
    assert 'class="featured' not in (targets["clearnet"].out / "index.html").read_text(encoding="utf-8")


# ---------------------------------------------------------------- 多語系

def site_problems(tmp_path, overrides=None, text=GOOD) -> list[str]:
    posts = tmp_path / "posts"
    write_versions(posts, text, overrides=overrides)
    try:
        build.load_site(posts, AUTHORS)
    except build.BuildError as error:
        return error.problems
    return []


def test_three_versions_load_together(tmp_path):
    assert site_problems(tmp_path) == []
    posts = build.load_site(tmp_path / "posts", AUTHORS)
    versions = posts[0].translations
    assert [versions[code].rel for code in ("zh-TW", "zh-CN", "en")] == [
        "2026/09/test-post/", "zh-cn/2026/09/test-post/", "en/2026/09/test-post/"]
    assert versions["en"].guid == "anoni-news:en/2026/09/test-post"
    assert versions["zh-TW"].guid == "anoni-news:2026/09/test-post"


def test_missing_and_orphan_versions(tmp_path):
    posts = tmp_path / "posts"
    posts.mkdir()
    write_post(posts, GOOD)
    (posts / "en").mkdir()
    write_post(posts / "en", GOOD, "2026-09-18-other.md")
    problems = build.check_translations(posts)
    assert any("缺少 zh-CN 版本" in p for p in problems), problems
    assert any("缺少 en 版本" in p for p in problems), problems
    assert any("en/2026-09-18-other.md：找不到對應的 zh-TW 版本" in p for p in problems), problems


@pytest.mark.parametrize("override, expected", [
    (("  - anoni-net", "  - night-owl"), "authors 跟 zh-TW 不同"),
    (("authors:", "pin: true\nauthors:"), "pin 跟 zh-TW 不同"),
    (("authors:", "draft: true\nauthors:"), "draft 跟 zh-TW 不同"),
    (("date: 2026-09-18", "date:\n  created: 2026-09-18\n  updated: 2026-09-19"), None),
    (("    url: https://example.org/", "    url: https://example.org/other"), "sources 少了 zh-TW 有的 https://example.org/"),
    (("內文，", "## Perspective {#perspective}\n\n內文，"), "錨點"),
])
def test_versions_must_agree(tmp_path, override, expected):
    problems = site_problems(tmp_path, {"en": override})
    if expected is None:
        assert problems == []  # 只有 updated 不同是允許的
    else:
        assert any(expected in p for p in problems), problems


FOLLOW_UP = GOOD.replace("date: 2026-09-18", "date: 2026-09-20").replace("slug: test-post", "slug: follow-up") \
    .replace("authors:", "follows:\n  - 2026-09-18-test-post\nauthors:")


@pytest.mark.parametrize("follows", ["follows: 2026-09-18-test-post", "follows:\n  - test-post", "follows:\n  - 2026-09-18-test-post.md"])
def test_follows_is_a_list_of_file_names(tmp_path, follows):
    text = GOOD.replace("authors:", follows + "\nauthors:")
    assert any("follows 要是清單" in p for p in problems_of(tmp_path, text)), problems_of(tmp_path, text)


@pytest.mark.parametrize("old, new, expected", [
    (None, None, None),
    ("  - 2026-09-18-test-post", "  - 2026-09-18-no-such-post", "找不到"),
    ("  - 2026-09-18-test-post", "  - 2026-09-20-follow-up", "沒有比這篇早發布"),
])
def test_follows_points_to_an_earlier_post(tmp_path, old, new, expected):
    """follows 指到的文章要存在、比較早發布。接續自己也算沒有比較早。"""
    posts = tmp_path / "posts"
    write_versions(posts, GOOD)
    write_versions(posts, FOLLOW_UP.replace(old, new) if old else FOLLOW_UP, "2026-09-20-follow-up.md")
    try:
        build.load_site(posts, AUTHORS)
        problems = []
    except build.BuildError as error:
        problems = error.problems
    if expected is None:
        assert problems == []
    else:
        assert any(expected in p for p in problems), problems


def test_follows_must_agree(tmp_path):
    override = ("authors:", "follows:\n  - 2026-09-18-test-post\nauthors:")
    assert any("follows 跟 zh-TW 不同" in p for p in site_problems(tmp_path, {"en": override}))


@pytest.mark.parametrize("watch, expected", [
    ("watch:\n  - date: 2026-10-01\n    note: 正式版是否推出", None),
    ("watch: 2026-10-01", "watch 要是清單"),
    ("watch:\n  - date: 2026-10-01", "watch 第 1 筆要有 date"),
    ("watch:\n  - date: 2026-10-01\n    note: ''", "watch 第 1 筆要有 date"),
    ("watch:\n  - date: 2026-10-01T07:00:00+08:00\n    note: x", "watch 第 1 筆要有 date"),
    ("watch:\n  - date: 2026-10-01\n    note: x\n    who: y", "watch 第 1 筆要有 date"),
    ("watch:\n  - date: 2026-09-18\n    note: x", "要晚於發布日"),
])
def test_watch_needs_a_date_and_a_note(tmp_path, watch, expected):
    text = GOOD.replace("authors:", watch + "\nauthors:")
    problems = problems_of(tmp_path, text)
    if expected is None:
        assert problems == []
        post = build.load_post(write_post(tmp_path, text), AUTHORS)
        assert [(w.due.isoformat(), w.note) for w in post.watch] == [("2026-10-01", "正式版是否推出")]
    else:
        assert any(expected in p for p in problems), problems


def test_watch_only_in_the_zh_tw_version(tmp_path):
    """watch 是編輯用的追蹤筆記，不翻譯，其他語系寫了就報錯。只有 zh-TW 寫是正常的寫法。"""
    watch = ("authors:", "watch:\n  - date: 2026-10-01\n    note: x\nauthors:")
    assert site_problems(tmp_path / "a", {"zh-TW": watch}) == []
    assert any("watch 只寫在 zh-TW" in p for p in site_problems(tmp_path / "b", {"en": watch}))


def test_due_watches(tmp_path):
    """快到期與過期的列出來，還沒到期的只算數量，已經有後續稿（包含排程中的）就不列。"""
    posts = tmp_path / "posts"
    watched = GOOD.replace("authors:", "watch:\n  - date: 2026-09-30\n    note: 過期的\n"
                                       "  - date: 2026-10-08\n    note: 七天內的\n"
                                       "  - date: 2026-10-20\n    note: 還沒到的\nauthors:")
    for lang in build.LANGS:
        directory = posts / lang.dir if lang.dir else posts
        directory.mkdir(parents=True, exist_ok=True)
        write_post(directory, watched if lang == build.DEFAULT_LANG else GOOD)
    other = GOOD.replace("date: 2026-09-18", "date: 2026-09-19").replace("slug: test-post", "slug: other-post") \
        .replace("authors:", "watch:\n  - date: 2026-10-02\n    note: 會被後續結案\nauthors:")
    for lang in build.LANGS:
        directory = posts / lang.dir if lang.dir else posts
        write_post(directory, other if lang == build.DEFAULT_LANG else other.replace("watch:\n  - date: 2026-10-02\n    note: 會被後續結案\n", ""),
                   "2026-09-19-other-post.md")
    loaded = build.load_site(posts, AUTHORS)
    today = datetime(2026, 10, 2).date()
    due, later = build.due_watches(loaded, today)
    assert [w.note for w, _ in due] == ["過期的", "會被後續結案", "七天內的"]
    assert [w.note for w, _ in later] == ["還沒到的"]

    follow_up = FOLLOW_UP.replace("2026-09-18-test-post", "2026-09-19-other-post")
    write_versions(posts, follow_up, "2026-09-20-follow-up.md")
    loaded = build.load_site(posts, AUTHORS)
    due, _ = build.due_watches(loaded, today)
    assert [w.note for w, _ in due] == ["過期的", "七天內的"]

    report = build.watch_report(loaded, today)
    assert "- [ ] 2026-09-30 測試文章：過期的 https://anoni.net/news/2026/09/test-post/（已過 2 天）" in report
    assert "- [ ] 2026-10-08 測試文章：七天內的 https://anoni.net/news/2026/09/test-post/\n" in report
    assert "另有 1 筆還沒到期，最早是 2026-10-20" in report


def test_extra_sources_are_allowed(tmp_path):
    extra = ("authors:", "  - title: Regional source\n    url: https://example.org/region\nauthors:")
    assert site_problems(tmp_path, {"zh-CN": extra}) == []


def test_strings_must_have_same_keys(tmp_path):
    bad = tmp_path / "strings.toml"
    bad.write_text(build.STRINGS_PATH.read_text(encoding="utf-8").replace('other_langs = "Also in "\n', ""))
    with pytest.raises(build.BuildError, match=r"\[en\] 缺少 other_langs"):
        build.load_strings(bad)


def test_every_language_gets_its_pages(fixture_site):
    targets, pages, _ = fixture_site
    rels = {p.rel for p in pages["clearnet"]}
    for base in ("", "zh-cn/", "en/"):
        assert {base, base + "2026/", base + "2026/09/", base + "2026/09/zkp-age-verification/"} <= rels
    out = targets["clearnet"].out
    assert '<html lang="en">' in (out / "en" / "index.html").read_text(encoding="utf-8")
    assert '<html lang="zh-Hans">' in (out / "zh-cn" / "index.html").read_text(encoding="utf-8")
    assert '<html lang="zh-Hant">' in (out / "index.html").read_text(encoding="utf-8")
    assert "404.html" in rels and not any(r.endswith("/404.html") for r in rels)


def test_story_thread_links_earlier_and_later_coverage(fixture_site):
    """zkp-age-verification 接續 age-verification-roundup。兩篇都列出整條事件線，較舊的那篇在標題區提示後續。"""
    targets, _, _ = fixture_site
    out = targets["clearnet"].out
    old = (out / "2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    new = (out / "2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")

    notice = old[old.index('<p class="story__followup">'):]
    notice = notice[:notice.index("</p>")]
    assert '後續發展：<a href="/news/2026/09/zkp-age-verification/">零知識證明用在年齡驗證的限制</a>（2026 年 9 月 18 日）' in notice
    assert old.index('class="story__langs"') < old.index('class="story__followup"') < old.index('class="story__body')
    assert "story__followup" not in new

    for page, current in ((old, "各國年齡驗證立法的共同問題"), (new, "零知識證明用在年齡驗證的限制")):
        # 放在 <article> 外面並標上 role，閱讀模式不會當成正文
        assert page.index("</article>") < page.index('<nav class="thread" role="navigation"') < page.index('class="subscribe"')
        thread = page[page.index('<nav class="thread"'):]
        thread = thread[:thread.index("</nav>")]
        assert thread.index("各國年齡驗證立法的共同問題") < thread.index("零知識證明用在年齡驗證的限制")
        assert f'<span class="thread__title">{current}</span> <span class="thread__here">本篇</span>' in thread
        assert f'">{current}</a>' not in thread
        assert thread.count("<li") == 2

    en = (out / "en/2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    assert 'Follow-up: <a href="/news/en/2026/09/zkp-age-verification/">' in en
    assert "Coverage of this story" in en and "This story" in en
    onion = (targets["onion"].out / "zh-cn/2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
    assert '<a class="thread__title" href="/zh-cn/2026/09/age-verification-roundup/">' in onion

    alone = (out / "2026/09/layout-stress-test/index.html").read_text(encoding="utf-8")
    assert 'class="thread"' not in alone and "story__followup" not in alone
    # 事件線不進 RSS，前情由第一段交代
    assert "thread__" not in (out / "feed.xml").read_text(encoding="utf-8")


def test_watch_is_not_published(fixture_site):
    """watch 是編輯用的筆記，頁面、RSS 與 sitemap 都不出現。"""
    targets, _, _ = fixture_site
    for target in targets.values():
        for path in target.out.rglob("*"):
            if path.suffix in {".html", ".xml", ".json"}:
                assert "追蹤筆記" not in path.read_text(encoding="utf-8"), path


def test_alternates_and_language_switch(fixture_site):
    targets, _, _ = fixture_site
    page = (targets["clearnet"].out / "en/2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
    for hreflang, url in (("zh-Hant", "2026"), ("zh-Hans", "zh-cn/2026"), ("en", "en/2026"), ("x-default", "2026")):
        assert f'<link rel="alternate" hreflang="{hreflang}" href="https://anoni.net/news/{url}/09/zkp-age-verification/">' in page
    # 頁首不放語系切換，文章頁在署名下方、每頁在頁尾列出另外兩個語系，不列目前的語系
    assert "site-header__langs" not in page
    for cls in ("story__langs", "site-footer__langs"):
        # role 跟 nav 重複，閱讀模式（Readability）只看 role 屬性，少了它朗讀會把這一行當成正文
        line = page[page.index(f'<nav class="{cls}" role="navigation"'):]
        line = line[:line.index("</nav>")]
        assert 'Also in <a href="/news/2026/09/zkp-age-verification/" hreflang="zh-Hant" lang="zh-Hant">正體中文</a>, ' \
            '<a href="/news/zh-cn/2026/09/zkp-age-verification/" hreflang="zh-Hans" lang="zh-Hans">简体中文</a>' in line
        assert "English" not in line
    assert page.index('class="story__byline"') < page.index('class="story__langs"') < page.index('class="story__body')
    zh = (targets["clearnet"].out / "2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
    assert '其他語言：<a href="/news/zh-cn/2026/09/zkp-age-verification/"' in zh and ">正體中文</a>" not in zh
    onion = (targets["onion"].out / "en/2026/09/index.html").read_text(encoding="utf-8")
    assert '<a href="/zh-cn/2026/09/" hreflang="zh-Hans"' in onion
    assert 'hreflang="en" href="http://news.' in onion


def test_interface_text_follows_language(fixture_site):
    targets, _, _ = fixture_site
    out = targets["clearnet"].out
    en = (out / "en/2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    assert "Thursday, 10 September 2026" in en
    assert "Based on 5 sources from EFF, Access Now, OONI" in en
    assert "Sources (5)" in en and "Older story" in en and "All stories" in en
    assert "/news/og-en.png" in en and '"inLanguage": "en"' in en
    # 文章內容與頁尾列出的語言名稱之外，英文頁不能留中文
    chrome = re.sub(r'<(article|script)\b.*?</\1>|<nav class="site-footer__langs".*?</nav>', "", en, flags=re.S)
    assert not re.search(r"[\u4e00-\u9fff]", chrome), "英文頁的介面文字還有中文"
    cn = (out / "zh-cn/2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    assert "整理 5 篇原文，来自 EFF、Access Now、OONI" in cn and "较旧的一篇" in cn
    assert (out / "zh-cn" / "index.html").read_text(encoding="utf-8").count("新闻导读") >= 2


def test_feed_per_language(fixture_site):
    targets, _, _ = fixture_site
    out = targets["onion"].out
    en = (out / "en" / "feed.xml").read_text(encoding="utf-8")
    assert "<language>en</language>" in en and "<title>anoni.net News</title>" in en
    assert '<guid isPermaLink="false">anoni-news:en/2026/09/zkp-age-verification</guid>' in en
    assert "Limits of zero-knowledge proofs" in en and "零知識證明" not in en.split("<item>")[0]
    assert "<language>zh-CN</language>" in (out / "zh-cn" / "feed.xml").read_text(encoding="utf-8")


def test_sitemap_lists_every_version(fixture_site):
    targets, _, _ = fixture_site
    sitemap = (targets["clearnet"].out / "sitemap.xml").read_text(encoding="utf-8")
    assert "<loc>https://anoni.net/news/en/2026/09/zkp-age-verification/</loc>" in sitemap
    assert '<xhtml:link rel="alternate" hreflang="zh-Hans" href="https://anoni.net/news/zh-cn/2026/09/zkp-age-verification/"/>' in sitemap
    assert sitemap.index("<loc>https://anoni.net/news/</loc>") < sitemap.index("<loc>https://anoni.net/news/en/</loc>")


def test_not_found_page_has_three_languages(fixture_site):
    targets, _, _ = fixture_site
    page = (targets["clearnet"].out / "404.html").read_text(encoding="utf-8")
    assert page.count("<h1>") == 1
    for lang, home in (("zh-Hant", "/news/"), ("zh-Hans", "/news/zh-cn/"), ("en", "/news/en/")):
        assert f'<section class="not-found" lang="{lang}">' in page
        assert f'href="{home}"' in page
    assert "hreflang" not in page


def test_about_page_per_language(fixture_site):
    targets, pages, _ = fixture_site
    rels = {page.rel for page in pages["clearnet"]}
    assert {"about/", "zh-cn/about/", "en/about/"} <= rels
    about = next(page for page in pages["clearnet"] if page.rel == "about/")
    assert not about.noindex and "report" in about.anchors
    sitemap = (targets["clearnet"].out / "sitemap.xml").read_text(encoding="utf-8")
    assert "https://anoni.net/news/en/about/" in sitemap
    # 頁尾連到同語系的關於頁與回報錯誤的 issue 表單
    for rel, home in (("", "/news/"), ("en/", "/news/en/")):
        page = (targets["clearnet"].out / rel / "index.html").read_text(encoding="utf-8")
        assert f'href="{home}about/"' in page
        assert 'href="https://github.com/anoni-net/news/issues/new"' in page


def test_site_page_problems(tmp_path):
    for lang in build.LANGS:
        d = build.lang_dir(tmp_path, lang)
        d.mkdir(parents=True, exist_ok=True)
        anchor = "report" if lang != build.LANGS[2] else "other"
        (d / "about.md").write_text(f"---\ntitle: t\ndescription: d\nextra: x\n---\n\n## 回報 {{#{anchor}}}\n", encoding="utf-8")
    (build.lang_dir(tmp_path, build.LANGS[1]) / "about.md").unlink()
    with pytest.raises(build.BuildError) as error:
        build.load_site_pages(tmp_path)
    text = "\n".join(error.value.problems)
    assert "缺少 zh-CN 版本" in text
    assert "多了不認得的欄位 extra" in text
    assert "錨點跟 zh-TW 版本不同" in text


def test_contract_includes_feeds_per_language(fixture_site):
    _, pages, _ = fixture_site
    lines = build.contract_lines(pages["clearnet"])
    assert {"/feed.xml", "/zh-cn/feed.xml", "/en/feed.xml", "/en/2026/09/layout-stress-test/"} <= set(lines)


def test_author_names_per_language(fixture_site):
    targets, _, _ = fixture_site
    out = targets["clearnet"].out
    assert "By anoni.net community" in (out / "en/2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    assert "导读：anoni.net 社区" in (out / "zh-cn/2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    # 筆名沒有寫 names，各語系都沿用 name
    assert "<dc:creator>夜梟</dc:creator>" in (out / "en" / "feed.xml").read_text(encoding="utf-8")


def test_author_names_keys_are_checked(tmp_path):
    path = tmp_path / "authors.yml"
    path.write_text("anoni-net:\n  name: x\n  names:\n    fr: y\n", encoding="utf-8")
    with pytest.raises(build.BuildError, match="names"):
        build.load_authors(path)


def test_traditional_chinese_is_called_zheng_ti(fixture_site):
    """社群用「正體中文」，見文件站的 community/zh-hant-naming。產物裡任何一頁都不該出現「繁體中文」。"""
    targets, _, _ = fixture_site
    for page in targets["clearnet"].out.rglob("*.html"):
        assert "繁體中文" not in page.read_text(encoding="utf-8"), page


def test_header_links_to_news_home(fixture_site):
    """左上角的標誌與「新聞導讀」回到該語系的 news 首頁，官網首頁的入口在頁尾。"""
    targets, _, _ = fixture_site
    for rel, home in (("2026/09/zkp-age-verification/", "/news/"), ("en/2026/", "/news/en/"),
                      ("zh-cn/2026/09/zkp-age-verification/", "/news/zh-cn/")):
        page = (targets["clearnet"].out / rel / "index.html").read_text(encoding="utf-8")
        header = page[page.index('<header class="site-header">'):page.index("</header>")]
        assert re.findall(r'href="([^"]+)"', header) == [home], header
        footer = page[page.index('<footer'):]
        assert 'href="https://anoni.net/"' in footer
    onion = (targets["onion"].out / "en" / "index.html").read_text(encoding="utf-8")
    assert '<a class="site-header__home" href="/en/">' in onion


def test_static_files_carry_content_version(fixture_site):
    """樣式、圖示與預覽圖的網址帶內容雜湊，改了內容網址就變，讀者不必等快取過期。"""
    import hashlib
    targets, _, _ = fixture_site
    for name, prefix in (("clearnet", "/news/"), ("onion", "/")):
        out = targets[name].out
        page = (out / "en" / "index.html").read_text(encoding="utf-8")
        for rel in ("css/news.css", "favicon.svg", "logo-wordmark-white.svg"):
            digest = hashlib.sha256((out / rel).read_bytes()).hexdigest()[:10]
            assert f'"{prefix}{rel}?v={digest}"' in page, rel
        og = hashlib.sha256((out / "og-en.png").read_bytes()).hexdigest()[:10]
        assert f'og-en.png?v={og}"' in page


def test_newsletter_form_follows_language(fixture_site):
    """訂閱表單中文與英文各一份，onion 版本改寫成 form.<onion>。"""
    targets, _, _ = fixture_site
    zh_form = "https://form.anoni.net/s/cmc9ceju1000dlj017fiathzq"
    en_form = "https://form.anoni.net/s/w21855zpca072rvgp0s2govj"
    out = targets["clearnet"].out
    for rel, form, other in (("", zh_form, en_form), ("zh-cn/", zh_form, en_form), ("en/", en_form, zh_form)):
        page = (out / rel / "index.html").read_text(encoding="utf-8")
        assert page.count(f'href="{form}"') == 2 and other not in page  # 刊頭與頁尾
    post = (out / "en/2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
    assert post.count(f'href="{en_form}"') == 2 and "in Chinese" not in post  # 文末與頁尾
    onion = (targets["onion"].out / "en" / "index.html").read_text(encoding="utf-8")
    assert "http://form.anoninetru5tflukgfaehun7q6khowgmymcff3gtk5oyesqazhmfxtyd.onion/s/w21855zpca072rvgp0s2govj" in onion


NOW = datetime(2026, 9, 18, 12, 0, tzinfo=build.TZ)


@pytest.mark.parametrize("date_yaml, name, scheduled, problem", [
    ("date: 2026-09-18", "2026-09-18-test-post.md", False, None),
    ("date: 2026-09-18T10:00:00+08:00", "2026-09-18-test-post.md", False, None),
    ("date: 2026-09-18T12:30:00+08:00", "2026-09-18-test-post.md", True, None),
    ("date: 2026-09-25T07:00:00+08:00", "2026-09-25-test-post.md", True, None),
    ("date: 2026-09-25T12:30:00+08:00", "2026-09-25-test-post.md", None, "最多只能排到 7 天後"),
    ("date:\n  created: 2026-09-18\n  updated: 2026-09-20", "2026-09-18-test-post.md", None, "date.updated"),
])
def test_future_date_is_scheduled_up_to_seven_days(tmp_path, monkeypatch, date_yaml, name, scheduled, problem):
    """date 晚於現在就是排程中，最多排到 7 天後。更正日期不能在未來。現在固定成 2026-09-18 12:00（台北時間）。"""
    monkeypatch.setattr(build, "current_time", lambda: NOW)
    text = GOOD.replace("date: 2026-09-18", date_yaml)
    if problem:
        assert any(problem in p for p in problems_of(tmp_path, text, name)), problems_of(tmp_path, text, name)
    else:
        assert build.load_post(write_post(tmp_path, text, name), AUTHORS).scheduled is scheduled


def test_scheduled_post_is_left_out_until_its_time(tmp_path, monkeypatch):
    """排程中的文章不產出頁面，也不進首頁、RSS 與 sitemap，網址合約先收進去。到了時間重建就出現。"""
    posts = tmp_path / "posts"
    write_versions(posts, GOOD)
    # 排程中的後續接續已發布的文章，舊文章在後續上線以前不能露出它的標題與網址
    later = GOOD.replace("date: 2026-09-18", "date: 2026-09-19T07:00:00+08:00").replace("slug: test-post", "slug: next-post") \
        .replace("authors:", "follows:\n  - 2026-09-18-test-post\nauthors:")
    write_versions(posts, later, "2026-09-19-next-post.md")
    shutil.copy(FIXTURES / "authors.yml", tmp_path / "authors.yml")
    shutil.copy(FIXTURES / "favicons.toml", tmp_path / "favicons.toml")

    monkeypatch.setattr(build, "current_time", lambda: NOW)
    targets, pages, all_posts = build.build(posts, tmp_path / "out", ["clearnet"])
    out = targets["clearnet"].out
    assert [p.slug for p in all_posts if p.scheduled] == ["next-post"]
    assert not (out / "2026/09/next-post").exists() and not (out / "en/2026/09/next-post").exists()
    for rel in ("index.html", "feed.xml", "sitemap.xml", "en/index.html", "2026/09/test-post/index.html"):
        assert "next-post" not in (out / rel).read_text(encoding="utf-8"), rel
    assert 'class="thread"' not in (out / "2026/09/test-post/index.html").read_text(encoding="utf-8")
    contract = build.contract_lines(build.contract_pages(posts))
    assert "/2026/09/next-post/" in contract and "/en/2026/09/next-post/" in contract

    monkeypatch.setattr(build, "current_time", lambda: datetime(2026, 9, 19, 7, 5, tzinfo=build.TZ))
    targets, _, _ = build.build(posts, tmp_path / "out", ["clearnet"])
    out = targets["clearnet"].out
    assert (out / "2026/09/next-post/index.html").exists()
    assert "next-post" in (out / "feed.xml").read_text(encoding="utf-8")
    earlier = (out / "2026/09/test-post/index.html").read_text(encoding="utf-8")
    assert '<p class="story__followup">後續發展：<a href="/news/2026/09/next-post/">' in earlier
    assert 'class="thread"' in earlier


def test_time_of_day_orders_posts_on_the_same_day(tmp_path):
    posts = tmp_path / "posts"
    posts.mkdir()
    write_post(posts, GOOD.replace("date: 2026-09-18", "date: 2026-09-18T09:00:00+08:00"))
    write_post(posts, GOOD.replace("date: 2026-09-18", "date: 2026-09-18T15:00:00+08:00").replace("slug: test-post", "slug: another-post"),
               "2026-09-18-another-post.md")
    assert [p.slug for p in build.load_posts(posts, AUTHORS)] == ["another-post", "test-post"]


# ---------------------------------------------------------------- 原文的網站圖示

FAVICON = "eff.org-512902b2.png"


def favicon_problems(tmp_path, hosts: dict, files: dict | None = None) -> list[str]:
    """GOOD 的原文在 example.org，hosts 是 favicons.toml 的內容，files 是圖示主機上的檔案。"""
    posts, assets = tmp_path / "posts", tmp_path / "assets"
    write_versions(posts, GOOD)
    for name, options in (files or {}).items():
        make_image(assets / "favicons" / name, **{"size": (64, 64), "fmt": "PNG", **options})
    try:
        build.load_site(posts, AUTHORS, build.AssetStore(assets), hosts)
    except build.BuildError as error:
        return error.problems
    return []


def test_source_slip_shows_favicons(fixture_site):
    targets, _, _ = fixture_site
    for name, src in (("clearnet", f"/news/assets/favicons/{FAVICON}"), ("onion", f"/assets/favicons/{FAVICON}")):
        out = targets[name].out
        page = (out / "2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
        assert f'<img class="source-slip__icon" src="{src}" width="16" height="16" alt=""' in page
        assert (out / "assets/favicons" / FAVICON).exists()
    # 登記成 none 的 example.org 用通用的地球圖示，不是空白
    page = (targets["clearnet"].out / "2026/09/age-verification-roundup/index.html").read_text(encoding="utf-8")
    slip = page[page.index('id="sources"'):]
    assert '<a href="https://example.org/' in slip and '<svg class="icon"' in slip


def test_feed_has_no_favicons(fixture_site):
    targets, _, _ = fixture_site
    for target in targets.values():
        for feed in target.out.rglob("feed.xml"):
            assert "favicons/" not in feed.read_text(encoding="utf-8"), feed


def test_unregistered_host_fails(tmp_path):
    problems = favicon_problems(tmp_path, {"eff.org": {"none": "x"}})
    assert len([p for p in problems if "example.org 不在 favicons.toml" in p]) == 1, problems


def test_same_as_and_none_resolve(tmp_path):
    assert favicon_problems(tmp_path, {"example.org": {"same_as": "eff.org"}, "eff.org": {"icon": FAVICON}},
                            {FAVICON: {}}) == []
    assert favicon_problems(tmp_path / "none", {"example.org": {"none": "網站沒有提供"}}) == []


@pytest.mark.parametrize("entry, expected", [
    ({}, "icon、same_as、none 其中一個"),
    ({"icon": FAVICON, "none": "x"}, "icon、same_as、none 其中一個"),
    ({"icon": "eff.png"}, "<主機>-<8 碼雜湊>.png"),
    ({"none": ""}, "none 要寫理由"),
    ({"none": "x", "from": "https://example.org/favicon.ico"}, "from 只跟 icon 一起寫"),
    ({"icon": FAVICON, "size": 64}, "不認得的欄位"),
    ({"same_as": "missing.org"}, "不在登記表裡"),
])
def test_favicon_registry_problems(tmp_path, entry, expected):
    path = tmp_path / "favicons.toml"
    lines = [f'{key} = {value!r}' if isinstance(value, int) else f'{key} = "{value}"' for key, value in entry.items()]
    path.write_text('[hosts."example.org"]\n' + "\n".join(lines) + "\n", encoding="utf-8")
    with pytest.raises(build.BuildError) as error:
        build.load_favicons(path)
    assert any(expected in p for p in error.value.problems), error.value.problems


def test_same_as_cannot_chain(tmp_path):
    path = tmp_path / "favicons.toml"
    path.write_text('[hosts."a.org"]\nsame_as = "b.org"\n[hosts."b.org"]\nsame_as = "c.org"\n'
                    '[hosts."c.org"]\nnone = "x"\n', encoding="utf-8")
    with pytest.raises(build.BuildError) as error:
        build.load_favicons(path)
    assert any("本身也是 same_as" in p for p in error.value.problems), error.value.problems


@pytest.mark.parametrize("options, expected", [
    ({"size": (32, 32)}, "64×64 的 PNG"),
    ({"fmt": "WEBP"}, "64×64 的 PNG"),
    ({"noise": True}, "不能超過 8KB"),
])
def test_favicon_file_checks(tmp_path, options, expected):
    problems = favicon_problems(tmp_path, {"example.org": {"icon": FAVICON}}, {FAVICON: options})
    assert any(expected in p for p in problems), problems


def test_favicon_missing_on_assets(tmp_path):
    (tmp_path / "assets").mkdir()
    problems = favicon_problems(tmp_path, {"example.org": {"icon": FAVICON}})
    assert any("找不到圖片" in p for p in problems), problems


@pytest.mark.parametrize("url, host", [
    ("https://www.eff.org/deeplinks/x", "eff.org"),
    ("https://Support.Apple.com/en-us/1", "support.apple.com"),
    ("http://wwwexample.org/", "wwwexample.org"),
])
def test_source_host(url, host):
    assert build.source_host(url) == host


def test_byline_icons_follow_source_line(tmp_path):
    """署名旁的圖示對應出處行列出的網站，最多三個，同一個出處只算一次。都沒填 publisher 時沒有圖示。"""
    def icons_of(sources: str) -> list:
        post = build.load_post(write_post(tmp_path, GOOD.replace(
            "sources:\n  - title: Source\n    url: https://example.org/\n", "sources:\n" + sources)), AUTHORS)
        for source in post.sources:
            source.icon = f"favicons/{source.host}-00000000.png"
        return build.source_icons(post)

    item = "  - title: T\n    url: https://{host}/\n    publisher: {publisher}\n"
    many = "".join(item.format(host=f"s{i}.org", publisher=f"P{i}") for i in range(5))
    assert icons_of(many) == [f"favicons/s{i}.org-00000000.png" for i in range(3)]
    same = item.format(host="a.org", publisher="A") + item.format(host="b.org", publisher="A")
    assert icons_of(same) == ["favicons/a.org-00000000.png"]
    assert icons_of("  - title: T\n    url: https://a.org/\n") == []


def test_byline_icons_on_both_targets(fixture_site):
    targets, _, _ = fixture_site
    for name, src in (("clearnet", f"/news/assets/favicons/{FAVICON}"), ("onion", f"/assets/favicons/{FAVICON}")):
        page = (targets[name].out / "2026/09/zkp-age-verification/index.html").read_text(encoding="utf-8")
        assert f'<a href="#sources"><span class="favicon-stack"><img src="{src}" width="16" height="16" alt=""' in page
