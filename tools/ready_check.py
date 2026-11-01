"""開 PR 前的檢查一次執行完，只印出沒有通過的項目。

用 AI 協作工具寫稿時，prose_check、寫作風格的 linter、front matter 與 build.py --check 分開執行，
主對話要多花十幾個回合，每個回合都重讀整段上下文（見 guides/ai-workflow.md「主對話」）。
這支把四項併成一次，通過的項目只印一行。

用法：uv run tools/ready_check.py [--no-build] posts/<檔名>.md [history/<檔名>.md ...]

給 zh-TW 的路徑就好，zh-CN 與 en 同名的檔案存在時一起檢查。
- prose_check：tools/prose_check.py 列出的長句與長段落。要逐處判斷，照錄的原文標題可以留著
- 寫作風格：文件站的 docs_style_lint.py，下載到 .cache/ 並每 12 小時更新一次，跟 CI 用同一份
- front matter：只抽這幾個檔案的標題、description 與「同一天還有」再交給 linter，舊稿的警告不會混進來
- build：build.py --check，只印最後 30 行。--no-build 略過

有沒通過的項目時結束代碼為 1，參數錯誤為 2。
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from front_matter_text import lines_for  # noqa: E402

USAGE = "用法：uv run tools/ready_check.py [--no-build] posts/<檔名>.md [history/<檔名>.md ...]"
LINTER_URL = "https://raw.githubusercontent.com/anoni-net/docs/main/tools/docs_style_lint.py"
LINTER = ROOT / ".cache" / "docs_style_lint.py"
LANGS = (("zh-TW", ""), ("zh-CN", "zh-CN"), ("en", "en"))
TAIL = 30
CLEAN = "0 error、0 warn"


def siblings(path: Path) -> list[tuple[str, Path]]:
    """zh-TW 的路徑展開成三個語系裡存在的檔案。"""
    out = []
    for lang, sub in LANGS:
        candidate = path.parent / sub / path.name if sub else path
        if candidate.exists():
            out.append((lang, candidate))
    return out


def linter() -> Path:
    if not LINTER.exists() or time.time() - LINTER.stat().st_mtime > 12 * 3600:
        LINTER.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(LINTER_URL, timeout=30) as resp:
            LINTER.write_bytes(resp.read())
    return LINTER


def run(cmd: list[str]) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def report(name: str, ok: bool, output: str) -> bool:
    if ok:
        print(f"通過　{name}")
    else:
        lines = output.splitlines()
        print(f"未通過　{name}")
        for line in lines[-TAIL:]:
            print(f"  {line}")
    return ok


def main(argv: list[str]) -> int:
    build = "--no-build" not in argv
    args = [a for a in argv if a != "--no-build"]
    if not args or any(a.startswith("-") for a in args):
        print(USAGE, file=sys.stderr)
        return 2
    files: list[tuple[str, Path]] = []
    for arg in args:
        path = (ROOT / arg).resolve() if not Path(arg).is_absolute() else Path(arg)
        if not path.exists():
            print(f"找不到檔案：{arg}", file=sys.stderr)
            return 2
        files += siblings(path)

    results = []
    code, out = run(["uv", "run", "tools/prose_check.py", *[str(p) for _, p in files]])
    results.append(report("prose_check", code == 0, out))

    lint = str(linter())
    code, out = run([sys.executable, lint, *[str(p) for _, p in files]])
    results.append(report("寫作風格", code == 0 and CLEAN in out, out))

    with tempfile.TemporaryDirectory() as tmp:
        targets = []
        for lang, _ in LANGS:
            lines = [line for code_, path in files if code_ == lang for line in lines_for(path)]
            if lines:
                target = Path(tmp) / lang / "front-matter.md"
                target.parent.mkdir(parents=True)
                target.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
                targets.append(str(target))
        code, out = run([sys.executable, lint, *targets])
        results.append(report("front matter", code == 0 and CLEAN in out, out))

    if build:
        code, out = run(["uv", "run", "build.py", "--check"])
        results.append(report("build.py --check", code == 0, out))

    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
