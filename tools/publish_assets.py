"""維護者的機器上一次完成網站圖示與預覽卡片，給 news-publish-assets 指令呼叫。

    news-publish-assets --dry-run <稿件路徑> ...
    news-publish-assets [--from 主機=網址或檔案] [--none 主機=理由] [--same-as 主機=另一個主機] <稿件路徑> ...

稿件路徑可以是任一個語系的檔案，也可以是絕對路徑，例如
/home/.../worktrees/<分支>/posts/2026-11-20-slug.md 或 history/en/11-20.md。同一篇的三個語系會一起處理。

依序執行 tools/fetch_favicons.py、tools/make_cards.py 與 build.py --check。網址合約不在這裡更新，
稿件的 PR 不收新網址，由每週短訊的 PR 一次收進去，見 SPEC.md「網址合約」。
--dry-run 只執行前者與卡片的試跑，產生 .cache/favicons/preview.html 與 .cache/cards/preview.html，
不上傳也不改登記表。上傳的目的地讀 ~/.config/anoni-news/assets-rsync，不寫進 repo。
開始上傳之前先確認連得到圖片主機，連不到就停下來說明原因，不嘗試上傳。

要讓 AI 協作工具在 auto mode 下穩定執行，用 tools/install_publish_assets.sh 安裝指令與允許規則。
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path.home() / ".config" / "anoni-news" / "assets-rsync"
LANGS = ("", "zh-CN/", "en/")


def destination() -> str:
    """上傳的目的地。設定檔優先，其次是環境變數 NEWS_ASSETS_RSYNC。"""
    if CONFIG.exists():
        value = CONFIG.read_text(encoding="utf-8").strip()
        if value:
            return value
    value = os.environ.get("NEWS_ASSETS_RSYNC", "").strip()
    if value:
        return value
    raise SystemExit(f"沒有上傳的目的地：請在 {CONFIG} 寫一行 rsync 目標，例如 <主機>:<路徑>")


def reachable(dest: str) -> None:
    """用 ssh 確認連得到圖片主機，連不到就停下來，不讓工具在上傳途中失敗。"""
    host = dest.split(":", 1)[0]
    result = subprocess.run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10", host, "true"],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"連不到圖片主機 {host}，這台機器不能上傳。請在 PR 內文列出要上傳的項目，"
                         f"交給能連線的機器處理。\n{result.stderr.strip()}")


def canonical(path: str) -> tuple[str, str]:
    """把任一語系的稿件路徑換成 (種類, repo 裡的 zh-TW 路徑)，種類是 posts 或 history。"""
    p = Path(path).resolve()
    try:
        rel = p.relative_to(ROOT)
    except ValueError:
        raise SystemExit(f"{path} 不在這個 worktree（{ROOT}）裡")
    parts = rel.parts
    if len(parts) < 2 or parts[0] not in ("posts", "history") or p.suffix != ".md":
        raise SystemExit(f"{path} 不是 posts/ 或 history/ 底下的稿件")
    kind, name = parts[0], parts[-1]
    zh_tw = f"{kind}/{name}"
    if not (ROOT / zh_tw).exists():
        raise SystemExit(f"找不到 {zh_tw}")
    return kind, zh_tw


def all_versions(zh_tw: str) -> list[str]:
    kind, name = zh_tw.split("/", 1)
    return [f"{kind}/{lang}{name}" for lang in LANGS if (ROOT / f"{kind}/{lang}{name}").exists()]


def run(args: list[str], env: dict[str, str]) -> None:
    print("→", " ".join(args), flush=True)
    result = subprocess.run(args, cwd=ROOT, env=env)
    if result.returncode != 0:
        raise SystemExit(f"{args[2] if len(args) > 2 else args[0]} 失敗（結束碼 {result.returncode}），後面的步驟沒有執行")


def main() -> None:
    parser = argparse.ArgumentParser(description="上傳稿件的網站圖示與預覽卡片，並更新網址合約")
    parser.add_argument("paths", nargs="+", help="稿件路徑，任一語系皆可")
    parser.add_argument("--dry-run", action="store_true", help="只試抓圖示、試產卡片，不上傳也不改登記表")
    parser.add_argument("--from", dest="overrides", action="append", default=[], metavar="主機=網址或檔案")
    parser.add_argument("--none", dest="nones", action="append", default=[], metavar="主機=理由")
    parser.add_argument("--same-as", dest="aliases", action="append", default=[], metavar="主機=另一個主機")
    args = parser.parse_args()

    targets = sorted({canonical(p)[1] for p in args.paths})
    files = [v for t in targets for v in all_versions(t)]
    favicon_opts = ([f"--from={o}" for o in args.overrides] + [f"--none={n}" for n in args.nones]
                    + [f"--same-as={a}" for a in args.aliases])
    env = dict(os.environ)

    if args.dry_run:
        run(["uv", "run", "tools/fetch_favicons.py", "--dry-run", *favicon_opts, *files], env)
        run(["uv", "run", "tools/make_cards.py", "--dry-run", *targets], env)
        print("試跑完成，看過 .cache/favicons/preview.html 與 .cache/cards/preview.html 再拿掉 --dry-run")
        return

    dest = destination()
    reachable(dest)
    env["NEWS_ASSETS_RSYNC"] = dest
    run(["uv", "run", "tools/fetch_favicons.py", *favicon_opts, *files], env)
    run(["uv", "run", "tools/make_cards.py", *targets], env)
    run(["uv", "run", "build.py", "--check"], env)
    print("完成：網站圖示與預覽卡片都已更新，請 commit favicons/ 與 og_cards/ 底下新增或改動的檔案")


if __name__ == "__main__":
    main()
