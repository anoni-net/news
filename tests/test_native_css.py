"""列印、高對比模式、引用段落的標示與長列表的樣式。規則見 SPEC.md「列印」、「高對比模式」、
「引用段落的連結」與「版面」。

這幾項都是純 CSS，用 headless Chrome 模擬列印與高對比模式，讀計算後的樣式確認規則真的生效。
找不到 Chrome 時略過，跟版面檢查相同。
"""

from __future__ import annotations

import asyncio
import functools
import sys
import tempfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

import build  # noqa: E402
import layout_check  # noqa: E402
from test_read_aloud import Browser  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
POST = "2026/09/layout-stress-test/"


def style(selector, prop, pseudo=None):
    pseudo = f", '{pseudo}'" if pseudo else ""
    return f"getComputedStyle(document.querySelector('{selector}'){pseudo}).getPropertyValue('{prop}')"


async def scenarios(ws_url, base):
    import websockets

    async with websockets.connect(ws_url, max_size=None) as ws:
        b = Browser(ws, base)
        await b.call("Page.enable")
        results = {}

        # 列印：桌機寬度、系統是深色模式時打開，再切到列印
        await b.call("Emulation.setDeviceMetricsOverride", width=1280, height=900, deviceScaleFactor=1, mobile=False)
        await b.call("Emulation.setEmulatedMedia", media="print",
                     features=[{"name": "prefers-color-scheme", "value": "dark"}])
        await b.open(POST, "real")
        results["列印隱藏"] = await b.eval(
            "['.site-header', '.site-footer', '.story__langs', '.pager', '.subscribe']"
            ".map(s => document.querySelector(s) ? getComputedStyle(document.querySelector(s)).display : 'none')")
        results["列印原文區塊"] = await b.eval(
            f"[{style('.source-slip', 'position')}, {style('.source-slip', 'overflow-y')}, {style('.source-slip', 'max-height')}]")
        results["列印原文網址"] = await b.eval(style('.source-slip a[href^="http"]', "content", "::after"))
        results["列印本頁網址"] = await b.eval(style(".story", "content", "::after"))
        results["列印的字色與底色"] = await b.eval(f"[{style('body', 'color')}, {style('body', 'background-color')}]")

        # 高對比模式
        await b.call("Emulation.setDeviceMetricsOverride", width=390, height=900, deviceScaleFactor=1, mobile=True)
        await b.call("Emulation.setEmulatedMedia", features=[{"name": "forced-colors", "value": "active"}])
        await b.open(POST, "real")
        results["高對比頁首"] = await b.eval(f"[{style('.site-header', 'forced-color-adjust')}, {style('.site-header', 'background-color')}]")
        results["高對比色塊"] = await b.eval(style(".cat", "background-color", "::before"))
        results["高對比字色"] = await b.eval(style("body", "color"))

        # 增加對比：只改顏色，版面不變。比對同一頁在一般與增加對比時，每個元素的位置與大小
        await b.call("Emulation.setDeviceMetricsOverride", width=390, height=900, deviceScaleFactor=1, mobile=True)
        rects = "[...document.querySelectorAll('body *')].map(e => { const r = e.getBoundingClientRect(); return [r.x, r.y, r.width, r.height].map(Math.round).join(','); }).join(';')"
        colors = (f"[{style('body', 'color')}, {style('.story__byline', 'color')}, {style('.source-slip__item + .source-slip__item', 'border-top-color')},"
                  f" {style('.story__body a, .story__byline a', 'color')}, {style('body', 'background-color')}]")
        for scheme in ("light", "dark"):
            await b.call("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": scheme}])
            await b.open(POST, "real")
            normal = (await b.eval(rects), await b.eval(colors))
            await b.call("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": scheme},
                                                                  {"name": "prefers-contrast", "value": "more"}])
            await b.open(POST, "real")
            more = (await b.eval(rects), await b.eval(colors))
            results[f"增加對比-{scheme}"] = {"版面相同": normal[0] == more[0], "一般": normal[1], "增加對比": more[1],
                                          "底線": await b.eval(style(".story__body a", "text-decoration-thickness"))}

        # 一般畫面：長列表與引用段落的標示色
        await b.call("Emulation.setEmulatedMedia", features=[])
        await b.open("", "real")
        results["長列表"] = await b.eval(f"[{style('.day', 'content-visibility')}, {style('.day', 'contain-intrinsic-height')}]")
        results["日期標題"] = await b.eval(style(".day__date", "position"))
        await b.open(POST, "real")
        results["引用標示"] = await b.eval(
            "[...document.styleSheets].flatMap(s => [...s.cssRules]).some(r => r.selectorText === '::target-text')")
        return results


@pytest.fixture(scope="module")
def results(tmp_path_factory):
    chrome = layout_check.find_chrome()
    if not chrome:
        pytest.skip("沒有找到 Chrome")
    out = tmp_path_factory.mktemp("site")
    targets, _, _ = build.build(FIXTURES / "posts", out, ["clearnet"])
    serve = tmp_path_factory.mktemp("serve")
    (serve / "news").symlink_to(targets["clearnet"].out.resolve())
    server = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(layout_check.QuietHandler, directory=serve))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    process, ws_url = layout_check.launch(chrome, Path(tempfile.mkdtemp()))
    try:
        if not ws_url:
            pytest.skip("Chrome 沒有開出偵錯連接埠")
        return asyncio.run(scenarios(ws_url, f"http://127.0.0.1:{server.server_address[1]}/news/"))
    finally:
        process.terminate()
        process.wait(timeout=10)
        server.shutdown()


def test_print_hides_navigation(results):
    assert results["列印隱藏"] == ["none"] * 5


def test_print_shows_whole_source_list(results):
    # 桌機的原文區塊停在頂端、在區塊內捲動，列印時要整塊印出來
    assert results["列印原文區塊"] == ["static", "visible", "none"]


def test_print_shows_addresses(results):
    assert "attr(href)" not in results["列印原文網址"] and "https://" in results["列印原文網址"]
    assert "https://anoni.net/news/2026/09/layout-stress-test/" in results["列印本頁網址"]


def test_print_is_black_on_white_even_in_dark_mode(results):
    assert results["列印的字色與底色"] == ["rgb(0, 0, 0)", "rgb(255, 255, 255)"]


def test_forced_colors_keeps_header_and_category_marks(results):
    adjust, header_bg = results["高對比頁首"]
    assert adjust == "none" and header_bg == "rgb(0, 62, 87)"
    # 分類色塊改用文字色，跟字色相同，不會變成透明或背景色
    assert results["高對比色塊"] == results["高對比字色"]


def test_long_lists_skip_offscreen_layout(results):
    assert results["長列表"] == ["auto", "auto 960px"]
    # 日期標題照樣停在頂端
    assert results["日期標題"] == "sticky"


def test_target_text_has_brand_highlight(results):
    assert results["引用標示"] is True


def test_mark_colors_are_checked_for_contrast():
    assert ("--c-mark-text", "--c-mark-bg") in build.CONTRAST_PAIRS
    assert build.check_contrast(ROOT / "static" / "css" / "news.css") == []


def rgb_hex(value):
    r, g, b = (int(x) for x in value[value.index("(") + 1:value.index(")")].split(",")[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


@pytest.mark.parametrize("scheme", ["light", "dark"])
def test_more_contrast_changes_colors_only(results, scheme):
    r = results[f"增加對比-{scheme}"]
    # 間距與尺寸都不動，每個元素的位置與大小跟平常相同
    assert r["版面相同"] is True
    text, muted, border, link, bg = (rgb_hex(v) for v in r["增加對比"])
    # 次要文字跟內文同色
    assert muted == text
    assert rgb_hex(r["一般"][1]) != text
    # 邊框至少 3:1（非文字元件的標準），連結至少 7:1
    assert build.contrast(border, bg) >= 3 > build.contrast(rgb_hex(r["一般"][2]), bg)
    assert build.contrast(link, bg) >= 7
    assert r["底線"] == "2px"
