"""標題字型的測試：分片的歸屬、子集的內容、onion 不放。規則見 SPEC.md「標題字型」。

測試用的字型放在 tests/fixtures/font-sources/，是正式原始檔只留 fixture 用到的字的子集，
產生方式見同一個目錄的 README.md。
"""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import pytest
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
FONT_FACE_RE = re.compile(r"@font-face \{(.*?)\}", re.S)


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    out = tmp_path_factory.mktemp("fonts-site")
    return build.build(FIXTURES / "posts", out, ["clearnet", "onion"])


def faces(css: str) -> list[dict]:
    """fonts.css 的每條 @font-face：字型、字重、檔案與收的字。"""
    result = []
    for body in FONT_FACE_RE.findall(css):
        ranges = re.search(r"unicode-range: ([^;]+);", body).group(1)
        chars = set()
        for part in ranges.split(", "):
            low, _, high = part[2:].partition("-")
            chars |= {chr(code) for code in range(int(low, 16), int(high or low, 16) + 1)}
        result.append({
            "family": re.search(r'font-family: "([^"]+)"', body).group(1),
            "weight": int(re.search(r"font-weight: (\d+)", body).group(1)),
            "file": re.search(r'url\("[^"]*/(fonts/[^"?]+)\?v=', body).group(1),
            "chars": chars,
        })
    return result


def all_css(out: Path) -> str:
    return "".join((out / build.FONTS_CSS.format(script=script)).read_text(encoding="utf-8")
                   for script in build.FONT_FAMILIES)


def post(lang: str, created: str, title: str, body: str = "") -> SimpleNamespace:
    return SimpleNamespace(lang=SimpleNamespace(html=lang), created=datetime.fromisoformat(created),
                           title=title, html=body)


def test_serif_weights_match_news_css():
    css = (ROOT / "static" / "css" / "news.css").read_text(encoding="utf-8")
    found = {}
    for selector, body in re.findall(r"^([^\s@/}][^{]*)\{([^}]*)\}", css, re.M):
        if "var(--font-serif)" in body:
            weight = re.search(r"font-weight:\s*(\d+)", body)
            found[selector.strip()] = int(weight.group(1)) if weight else None
    expected = {f".{name}": weight for name, weight in build.SERIF_WEIGHTS.items()}
    expected[".content h2"] = build.CONTENT_H2_WEIGHT
    assert set(found) == set(expected)
    for selector, weight in found.items():
        # 沒寫字重的都是 h1 到 h3，瀏覽器預設的粗體
        assert (weight or 700) == expected[selector], selector


def test_font_families_lead_the_serif_stacks():
    css = (ROOT / "static" / "css" / "news.css").read_text(encoding="utf-8")
    stacks = re.findall(r"--font-serif:\s*([^;]+);", css)
    for family in build.FONT_FAMILIES.values():
        assert any(stack.startswith(f'"{family}"') for stack in stacks), family


def test_owners_follow_the_first_month():
    owners = build.font_owners([
        post("zh-Hant", "2026-09-26T00:00:00+08:00", "隱私工具", "<h2 id=\"a\">審查<a href=\"#a\">量測</a></h2>"),
        post("zh-Hant", "2026-10-02T00:00:00+08:00", "隱私新聞"),
        post("zh-Hans", "2026-10-02T00:00:00+08:00", "隐私新闻"),
        post("en", "2026-10-02T00:00:00+08:00", "Privacy"),
    ])
    tc = owners["tc"]
    assert {tc[c] for c in "隱私工具審查量測"} == {"2026-09"}
    assert {tc[c] for c in "新聞"} == {"2026-10"}
    assert owners["sc"]["隐"] == "2026-10"
    assert "P" not in tc


def test_new_posts_leave_past_buckets_alone():
    needed = {("tc", 700): set("隱私工具新聞關於")}
    before = build.font_buckets(needed, build.font_owners([
        post("zh-Hant", "2026-09-26T00:00:00+08:00", "隱私工具"),
        post("zh-Hant", "2026-10-02T00:00:00+08:00", "隱私新聞"),
    ]))
    assert before[("tc", 700, "2026-09")] == set("隱私工具")
    assert before[("tc", 700, "2026-10")] == set("新聞")
    # 固定頁面才有的字放在 site
    assert before[("tc", 700, "site")] == set("關於")

    needed[("tc", 700)] |= set("更新")
    after = build.font_buckets(needed, build.font_owners([
        post("zh-Hant", "2026-09-26T00:00:00+08:00", "隱私工具"),
        post("zh-Hant", "2026-10-02T00:00:00+08:00", "隱私新聞"),
        post("zh-Hant", "2026-11-01T00:00:00+08:00", "工具更新"),
    ]))
    assert after[("tc", 700, "2026-09")] == before[("tc", 700, "2026-09")]
    assert after[("tc", 700, "2026-10")] == before[("tc", 700, "2026-10")]
    # 「新」十月就用過了，十一月只多了「更」
    assert after[("tc", 700, "2026-11")] == set("更")


def test_masthead_weight_stays_in_one_bucket():
    """刊頭的 900 字重只有介面文字，就算導讀的標題用過同樣的字，也只放一個分片。"""
    owners = build.font_owners([post("zh-Hant", "2026-09-26T00:00:00+08:00", "新聞")])
    buckets = build.font_buckets({("tc", 900): set("新聞導讀"), ("tc", 700): set("新聞導讀")}, owners)
    assert buckets[("tc", 900, "site")] == set("新聞導讀")
    assert buckets[("tc", 700, "2026-09")] == set("新聞")


def test_collector_follows_css_scopes():
    page = """<html lang="zh-Hant"><body>
    <a class="site-header__product">新聞導讀</a>
    <h1 class="masthead__title">新聞導讀</h1>
    <p>內文不用明體</p>
    <div class="content"><h2>小標<br>題</h2><h3>三級</h3></div>
    <h2>不在內文裡</h2>
    <section class="not-found" lang="zh-Hans"><a class="site-header__product">简体</a></section>
    </body></html>"""
    chars = build.serif_chars([page])
    assert chars[("tc", 700)] == set("新聞導讀小標題")
    assert chars[("tc", 900)] == set("新聞導讀")
    assert chars[("sc", 700)] == set("简体")
    assert build.serif_chars(['<html lang="en"><h1 class="story__title">Title</h1></html>']) == {}


def test_unicode_ranges():
    assert build.unicode_ranges(set("ABCE")) == "U+41-43, U+45"


def test_fonts_only_on_clearnet(site):
    targets, pages, _ = site
    onion = targets["onion"].out
    assert not list(onion.glob(build.FONTS_CSS.format(script="*")))
    assert not list(onion.rglob("*.woff2"))
    for page in pages["onion"]:
        assert "css/fonts-" not in (onion / page.file).read_text(encoding="utf-8")
    for name, target in targets.items():
        assert build.check_output(target, pages[name]) == []


def test_pages_link_their_own_fonts_css(site):
    """正體頁只載入正體那一份，簡體頁只載入簡體那一份，en 頁面一份都不載入。"""
    targets, pages, _ = site
    target = targets["clearnet"]
    links = {}
    for script in build.FONT_FAMILIES:
        rel = build.FONTS_CSS.format(script=script)
        version = build.hashlib.sha256((target.out / rel).read_bytes()).hexdigest()[:10]
        links[script] = f'href="/news/{rel}?v={version}"'
    seen = set()
    for page in pages["clearnet"]:
        text = (target.out / page.file).read_text(encoding="utf-8")
        lang = re.search(r'<html lang="([^"]+)"', text).group(1)
        script = build.FONT_SCRIPTS.get(lang)
        assert text.count("css/fonts-") == (1 if script else 0), page.file
        if script:
            assert links[script] in text, page.file
            seen.add(script)
    assert seen == set(build.FONT_FAMILIES)


def test_every_serif_char_is_in_a_subset(site):
    targets, pages, _ = site
    target = targets["clearnet"]
    needed = build.serif_chars([(target.out / page.file).read_text(encoding="utf-8") for page in pages["clearnet"]])
    css = all_css(target.out)
    covered: dict[tuple[str, int], set[str]] = {}
    families = {family: script for script, family in build.FONT_FAMILIES.items()}
    for face in faces(css):
        covered.setdefault((families[face["family"]], face["weight"]), set()).update(face["chars"])
    assert covered == needed
    # 兩個月份的導讀各有自己的分片
    months = {re.search(r"-(\d{4}-\d{2}|site)\.woff2$", face["file"]).group(1) for face in faces(css)}
    assert {"2026-08", "2026-09"} <= months


def test_subsets_hold_only_their_chars_under_a_new_name(site):
    targets, _, _ = site
    target = targets["clearnet"]
    for face in faces(all_css(target.out)):
        font = TTFont(target.out / face["file"])
        assert {chr(code) for code in font.getBestCmap()} == face["chars"], face["file"]
        for name_id in (1, 4, 6, 16):
            value = font["name"].getDebugName(name_id)
            assert value and "Noto" not in value and "Source" not in value, (face["file"], name_id, value)
    assert (target.out / build.FONTS_DIR / "OFL.txt").exists()


def test_fonts_are_reproducible(tmp_path, monkeypatch):
    """同樣的內容每次產生同樣的檔案，build 分支才不會在每小時的建置裡白白變動。
    兩次用不同的快取目錄，第二次也是重新子集化。"""
    outputs = []
    for run in ("a", "b"):
        monkeypatch.setattr(build, "FONT_CACHE", tmp_path / f"cache-{run}")
        targets, _, _ = build.build(FIXTURES / "posts", tmp_path / run, ["clearnet"])
        out = targets["clearnet"].out
        files = sorted(out.joinpath(build.FONTS_DIR).iterdir()) + sorted(out.glob(build.FONTS_CSS.format(script="*")))
        outputs.append({path.relative_to(out): path.read_bytes() for path in files})
    assert outputs[0] == outputs[1]


def test_missing_chars_are_reported(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "FONT_CACHE", tmp_path)
    source = FIXTURES / "font-sources" / build.FONT_SOURCES[0].file
    data, missing = build.subset_font(source, set("新𪚥"), "anoni news serif TC", "Bold")
    assert missing == {"𪚥"}
    assert data


def test_check_rejects_fonts_on_onion(tmp_path):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["onion"])
    target = targets["onion"]
    (target.out / "fonts").mkdir()
    (target.out / "fonts" / "x.woff2").write_bytes(b"wOF2")
    problems = build.check_output(target, pages["onion"])
    assert any("字型檔" in p for p in problems), problems


def test_check_catches_unreplaced_version(tmp_path):
    targets, pages, _ = build.build(FIXTURES / "posts", tmp_path, ["clearnet"])
    target = targets["clearnet"]
    path = target.out / "index.html"
    path.write_text(re.sub(r"(fonts-tc\.css\?v=)\w+", r"\g<1>" + build.FONTS_VERSION_PLACEHOLDER,
                           path.read_text(encoding="utf-8")), encoding="utf-8")
    problems = build.check_output(target, pages["clearnet"])
    assert any("版本號沒有換上" in p for p in problems), problems
