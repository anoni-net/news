"""把 front matter 裡寫給讀者看的文字抽成 Markdown，讓 docs_style_lint.py 也掃得到。

linter 會跳過 front matter，導讀的 title、description，以及導讀歷史快照的 title、description
與「同一天還有」的句子都掃不到。2026-10 有一則「同一天還有」寫了破折號，CI 沒有擋下來。

用法：uv run tools/front_matter_text.py <輸出目錄>
輸出 <輸出目錄>/zh-TW/front-matter.md、zh-CN/、en/ 三份，每行標明來源檔與欄位。目錄名稱
帶語系，linter 才會套對規則。
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LANG_DIRS = (("zh-TW", ""), ("zh-CN", "zh-CN"), ("en", "en"))


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    return yaml.safe_load(text.split("---\n", 2)[1]) or {}


def lines_for(path: Path) -> list[str]:
    meta = front_matter(path)
    rel = path.relative_to(ROOT)
    out = []
    for key in ("title", "description"):
        if isinstance(meta.get(key), str):
            out.append(f"{rel} {key}：{meta[key]}")
    for snap in meta.get("snapshots") or []:
        year = str(snap.get("date", ""))[:4]
        for key in ("title", "description"):
            if isinstance(snap.get(key), str):
                out.append(f"{rel} {year} {key}：{snap[key]}")
        for index, item in enumerate(snap.get("also") or [], 1):
            out.append(f"{rel} {year} also {index}：{item.get('text', '')}")
    return out


def main(target: Path) -> None:
    for lang, sub in LANG_DIRS:
        lines = []
        for folder in ("posts", "history"):
            base = ROOT / folder / sub if sub else ROOT / folder
            for path in sorted(base.glob("*.md")):
                lines += lines_for(path)
        out = target / lang
        out.mkdir(parents=True, exist_ok=True)
        # 每行之間空一行，各自成為一個段落
        (out / "front-matter.md").write_text("\n\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
