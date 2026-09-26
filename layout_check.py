"""SPEC.md 驗證第 8 項：用 headless Chrome 以三種寬度開頁面，整頁不能出現橫向捲軸。

由 build.py --check 呼叫。找不到 Chrome 時略過並回傳提示，不讓沒有 Chrome 的機器卡住。
截圖存到指定目錄，只證明頁面撐得住，排版好不好看要有人實際看過。
"""

from __future__ import annotations

import asyncio
import base64
import functools
import json
import os
import shutil
import socket
import subprocess
import tempfile
import threading
import time
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

WIDTHS = (320, 390, 1280)
CHROME_CANDIDATES = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")


def find_chrome() -> str | None:
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for name in CHROME_CANDIDATES:
        if path := shutil.which(name):
            return path
    return None


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


async def measure(ws_url: str, base: str, pages: list[str], shots: Path) -> list[str]:
    import websockets

    problems = []
    async with websockets.connect(ws_url, max_size=None) as ws:
        counter = 0

        async def call(method: str, **params):
            nonlocal counter
            counter += 1
            message_id = counter
            await ws.send(json.dumps({"id": message_id, "method": method, "params": params}))
            while True:
                reply = json.loads(await ws.recv())
                if reply.get("id") == message_id:
                    if "error" in reply:
                        raise RuntimeError(f"{method}: {reply['error']}")
                    return reply.get("result", {})

        await call("Page.enable")
        for width in WIDTHS:
            await call("Emulation.setDeviceMetricsOverride", width=width, height=900,
                       deviceScaleFactor=1, mobile=width < 800)
            for rel in pages:
                await call("Page.navigate", url=base + rel)
                for _ in range(50):
                    state = await call("Runtime.evaluate", expression="document.readyState", returnByValue=True)
                    if state["result"]["value"] == "complete":
                        break
                    await asyncio.sleep(0.1)
                # 跟設定的螢幕寬度比，不能跟 window.innerWidth 比。手機模式下頁面被撐寬時，
                # Chrome 會自動縮小畫面去容納內容，innerWidth 跟著變大，兩邊永遠一樣寬。
                result = await call(
                    "Runtime.evaluate", returnByValue=True,
                    expression="Math.max(document.documentElement.scrollWidth, document.body.scrollWidth)")
                scroll_width = result["result"]["value"]
                if scroll_width > width:
                    problems.append(f"版面：{width}px 寬開 /{rel} 出現橫向捲軸，內容寬 {scroll_width}px")
                shot = await call("Page.captureScreenshot", format="png", captureBeyondViewport=True)
                name = (rel.strip("/").replace("/", "_") or "index").replace(".html", "")
                (shots / f"{width}-{name}.png").write_bytes(base64.b64decode(shot["data"]))
    return problems


def run(site: Path, pages: list[str], shots: Path, prefix: str = "news") -> tuple[list[str], str | None]:
    """site 是 clearnet 產物的根目錄，架在 /<prefix>/ 底下開。回傳 (問題, 提示)。"""
    chrome = find_chrome()
    if not chrome:
        return [], "沒有找到 Chrome，略過版面檢查（第 8 項），可以用 CHROME 環境變數指定"

    shots.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / prefix).symlink_to(site.resolve())
        handler = functools.partial(QuietHandler, directory=tmp)
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{server.server_address[1]}/{prefix}/"

        port = free_port()
        profile = Path(tmp) / "profile"
        process = subprocess.Popen(
            [chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--password-store=basic", f"--user-data-dir={profile}", f"--remote-debugging-port={port}",
             "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            ws_url = None
            for _ in range(100):
                try:
                    with urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=1) as response:
                        tabs = json.load(response)
                    ws_url = next(t["webSocketDebuggerUrl"] for t in tabs if t["type"] == "page")
                    break
                except (OSError, StopIteration, ValueError):
                    time.sleep(0.1)
            if not ws_url:
                return ["版面：Chrome 沒有開出偵錯連接埠"], None
            problems = asyncio.run(measure(ws_url, base, pages, shots))
        finally:
            process.terminate()
            process.wait(timeout=10)
            server.shutdown()
    return problems, f"版面截圖存在 {shots}，送出 PR 前請實際看過"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
