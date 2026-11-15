"""tools/publish_assets.py 的測試：任一語系的稿件路徑都換成同一篇，路徑不對時停下來。"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import publish_assets  # noqa: E402


def a_post() -> str:
    """repo 裡任一篇有三個語系的導讀，回傳檔名。"""
    for path in sorted((ROOT / "posts").glob("*.md")):
        if (ROOT / "posts/zh-CN" / path.name).exists() and (ROOT / "posts/en" / path.name).exists():
            return path.name
    pytest.skip("repo 裡沒有三個語系齊全的導讀")


def test_any_language_maps_to_zh_tw():
    name = a_post()
    for rel in (f"posts/{name}", f"posts/zh-CN/{name}", f"posts/en/{name}"):
        assert publish_assets.canonical(str(ROOT / rel)) == ("posts", f"posts/{name}")
    assert publish_assets.all_versions(f"posts/{name}") == [f"posts/{name}", f"posts/zh-CN/{name}", f"posts/en/{name}"]


def test_history_path():
    day = sorted((ROOT / "history").glob("[0-9][0-9]-[0-9][0-9].md"))[0].name
    assert publish_assets.canonical(str(ROOT / "history/en" / day)) == ("history", f"history/{day}")


@pytest.mark.parametrize("rel", ["README.md", "guides/posts.md", "posts/2099-01-01-not-there.md"])
def test_rejects_non_posts(rel):
    with pytest.raises(SystemExit):
        publish_assets.canonical(str(ROOT / rel))


def test_rejects_other_worktree(tmp_path):
    other = tmp_path / "posts" / "2026-01-01-x.md"
    other.parent.mkdir()
    other.write_text("x", encoding="utf-8")
    with pytest.raises(SystemExit):
        publish_assets.canonical(str(other))
