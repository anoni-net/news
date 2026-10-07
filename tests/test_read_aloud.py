"""朗讀按鈕（static/js/read-aloud.js）在瀏覽器裡的行為。規則見 SPEC.md「朗讀按鈕」。

headless Chrome 的語音清單是空的，測不到真正的朗讀。這裡在頁面載入前換掉 speechSynthesis，
語音清單由測試指定，每一段要不要念完也由測試推進，不靠計時，CI 上不會因為機器快慢而不穩。
找不到 Chrome 時略過，跟版面檢查相同。
"""

from __future__ import annotations

import asyncio
import functools
import json
import sys
import tempfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402
import layout_check  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
POST = "2026/09/layout-stress-test/"

# 假的 speechSynthesis：speak() 排進佇列，__advance() 念完目前這一段，cancel() 清空佇列。
# voices 是 null 時整個 API 拿掉，模擬不支援的瀏覽器
FAKE = r"""
(() => {
  const voices = __VOICES__;
  if (voices === null) {
    Object.defineProperty(window, "speechSynthesis", { value: undefined, configurable: true });
    return;
  }
  window.SpeechSynthesisUtterance = function (text) { this.text = text; this.voice = null; this.lang = ""; };
  window.__spoken = [];
  const queue = [];
  let cur = null;
  function next() {
    if (cur || !queue.length) return;
    cur = queue.shift();
    window.__spoken.push({ text: cur.text, voice: cur.voice && cur.voice.name, lang: cur.lang });
    if (cur.onstart) cur.onstart({});
  }
  window.__advance = function () {
    const u = cur;
    cur = null;
    if (u && u.onend) u.onend({});
    next();
  };
  window.__queued = function () { return queue.length + (cur ? 1 : 0); };
  Object.defineProperty(window, "speechSynthesis", { configurable: true, value: {
    getVoices() { return voices; },
    speak(u) { queue.push(u); next(); },
    cancel() {
      queue.length = 0;
      const u = cur;
      cur = null;
      if (u && u.onerror) u.onerror({ error: "interrupted" });
    },
    addEventListener() {},
  }});
})();
"""

TW_REMOTE = {"name": "Google 國語（臺灣）", "lang": "zh-TW", "localService": False, "default": True}
TW_LOCAL = {"name": "Meijia", "lang": "zh-TW", "localService": True, "default": False}
CN_LOCAL = {"name": "Tingting", "lang": "zh_CN", "localService": True, "default": False}
HK_LOCAL = {"name": "Sinji", "lang": "zh-HK", "localService": True, "default": False}
EN_LOCAL = {"name": "Samantha", "lang": "en-US", "localService": True, "default": False}

VISIBLE = "!document.querySelector('[data-read-aloud]').hidden"
STATE = """({
  state: document.querySelector('.listen__button').dataset.state,
  label: document.querySelector('[data-label]').textContent,
  reading: (document.querySelector('.is-reading') || {}).textContent || null,
  tracked: document.querySelector('.listen__button').hasAttribute('data-anoni-event'),
})"""
CLICK = "document.querySelector('.listen__button').click()"


class Browser:
    def __init__(self, ws, base):
        self.ws, self.base, self.counter, self.script = ws, base, 0, None

    async def call(self, method, **params):
        self.counter += 1
        message_id = self.counter
        await self.ws.send(json.dumps({"id": message_id, "method": method, "params": params}))
        while True:
            reply = json.loads(await self.ws.recv())
            if reply.get("id") == message_id:
                if "error" in reply:
                    raise RuntimeError(f"{method}: {reply['error']}")
                return reply.get("result", {})

    async def eval(self, expression):
        result = await self.call("Runtime.evaluate", expression=expression, returnByValue=True, awaitPromise=True)
        return result["result"].get("value")

    async def open(self, rel, voices="real"):
        """voices 是語音清單、None（沒有語音 API），或 "real"（不替換，用 headless Chrome 自己的）。"""
        if self.script:
            await self.call("Page.removeScriptToEvaluateOnNewDocument", identifier=self.script)
            self.script = None
        if voices != "real":
            source = FAKE.replace("__VOICES__", json.dumps(voices))
            self.script = (await self.call("Page.addScriptToEvaluateOnNewDocument", source=source))["identifier"]
        await self.call("Page.navigate", url=self.base + rel)
        for _ in range(50):
            if await self.eval("document.readyState") == "complete":
                break
            await asyncio.sleep(0.1)
        # 腳本是 defer，load 之後才一定執行過。等到兩個畫格之後再看按鈕
        await self.eval("new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")


async def scenarios(ws_url, base):
    import websockets

    async with websockets.connect(ws_url, max_size=None) as ws:
        b = Browser(ws, base)
        await b.call("Page.enable")
        results = {}

        for name, rel, voices in [
            ("headless 的語音清單", POST, "real"),
            ("沒有語音 API", POST, None),
            ("只有線上語音", POST, [TW_REMOTE]),
            ("英文頁只有中文語音", "en/" + POST, [TW_LOCAL, CN_LOCAL]),
        ]:
            await b.open(rel, voices)
            results[name] = await b.eval(VISIBLE)

        for name, rel, voices in [
            ("正體頁", POST, [TW_REMOTE, HK_LOCAL, CN_LOCAL, TW_LOCAL]),
            ("正體頁沒有台灣語音", POST, [HK_LOCAL, CN_LOCAL, TW_REMOTE]),
            ("簡體頁", "zh-cn/" + POST, [TW_LOCAL, HK_LOCAL, CN_LOCAL]),
            ("英文頁", "en/" + POST, [TW_LOCAL, EN_LOCAL]),
        ]:
            await b.open(rel, voices)
            await b.eval(CLICK)
            results[name] = await b.eval("__spoken[0].voice")

        # 一篇完整念過：開始、念兩段、暫停、繼續、念完
        await b.open(POST, [TW_REMOTE, TW_LOCAL])
        results["開始前"] = await b.eval(STATE)
        await b.eval(CLICK)
        results["開始"] = await b.eval(STATE)
        results["title"] = await b.eval("document.querySelector('.story__title').textContent.trim()")
        await b.eval("__advance(); __advance()")
        results["第三段"] = await b.eval(STATE)
        await b.eval(CLICK)
        results["暫停"] = await b.eval(STATE)
        results["暫停後的佇列"] = await b.eval("__queued()")
        await b.eval(CLICK)
        results["繼續"] = await b.eval(STATE)
        results["繼續的第一段"] = await b.eval("__spoken[__spoken.length - 1].text")
        await b.eval("for (let i = 0; i < 200 && __queued(); i++) __advance()")
        results["念完"] = await b.eval(STATE)
        results["念過的段落"] = await b.eval("__spoken.map(s => s.text)")
        results["語音"] = await b.eval("[...new Set(__spoken.map(s => s.voice + '|' + s.lang))]")
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


@pytest.mark.parametrize("case", ["headless 的語音清單", "沒有語音 API", "只有線上語音", "英文頁只有中文語音"])
def test_button_hidden_without_local_voice(results, case):
    assert results[case] is False


@pytest.mark.parametrize("case, voice", [
    ("正體頁", "Meijia"),
    # 沒有台灣的語音時用中國的普通話，粵語排最後
    ("正體頁沒有台灣語音", "Tingting"),
    ("簡體頁", "Tingting"),
    ("英文頁", "Samantha"),
])
def test_picks_local_voice_for_page_language(results, case, voice):
    assert results[case] == voice


def test_never_uses_online_voice(results):
    assert results["語音"] == ["Meijia|zh-TW"]


def test_play_pause_resume_finish(results):
    s = build.strings()["zh-TW"]
    assert results["開始前"] == {"state": "idle", "label": s["listen"], "reading": None, "tracked": True}
    # 第一次點擊之後拿掉統計事件，暫停與繼續不再計算
    assert results["開始"]["state"] == "playing" and results["開始"]["label"] == s["listen_pause"]
    assert results["開始"]["tracked"] is False
    assert results["開始"]["reading"].strip() == results["title"]
    third = results["第三段"]["reading"]
    assert results["暫停"]["state"] == "paused" and results["暫停"]["label"] == s["listen_resume"]
    assert results["暫停"]["reading"] == third
    assert results["暫停後的佇列"] == 0
    # 從暫停的那一段重新念
    assert results["繼續"]["state"] == "playing"
    assert results["繼續的第一段"] == " ".join(third.split())
    assert results["念完"]["state"] == "idle" and results["念完"]["reading"] is None


def test_reads_title_body_and_tables_but_not_code(results):
    spoken = results["念過的段落"]
    assert spoken[0] == results["title"]
    assert not any("ooniprobe run" in text for text in spoken)
    assert any(text.startswith("Spain，1,234，554,500，5.8%") for text in spoken)
    # 原文清單、語系連結與訂閱行不在朗讀範圍
    assert not any(text.startswith(("其他語言", "想收到新的導讀")) for text in spoken)
