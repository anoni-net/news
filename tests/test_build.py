"""build.py 的測試。每一項檢查都放一個故意寫壞的例子，確認它真的會報錯。

檢查全部通過不代表內容沒問題，也可能是檢查本身失效。版面檢查就發生過：拿
scrollWidth 跟 window.innerWidth 比，手機模式下兩者一起被撐寬，永遠通過。
"""

from __future__ import annotations

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


def test_post_needs_docs_link(tmp_path):
    posts = tmp_path / "posts"
    posts.mkdir()
    write_post(posts, GOOD.replace("https://anoni.net/docs/basics/threat-model/", "https://example.org/"))
    with pytest.raises(build.BuildError, match="至少要有一條連到"):
        build.load_posts(posts, AUTHORS)


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
    assert '<a href="#sources">整理 5 篇原文，來自 EFF、Access Now、OONI</a>' in page
    assert page.index('class="story__body content"') < page.index('id="sources"')
    assert page.count('class="source-slip__item"') == 5
    assert "整理 5 篇原文，來自 EFF、Access Now、OONI" in (out / "index.html").read_text(encoding="utf-8")
    import json
    post = next(p for p in posts if p.slug == "age-verification-roundup")
    data = json.loads(build.jsonld(post, targets["clearnet"], {"homepage": "https://anoni.net/"}))
    assert len(data["citation"]) == 5
