import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import ready_check  # noqa: E402


def test_siblings_only_existing(tmp_path):
    zh_tw = tmp_path / "posts" / "a.md"
    (tmp_path / "posts" / "en").mkdir(parents=True)
    zh_tw.write_text("x", encoding="utf-8")
    (tmp_path / "posts" / "en" / "a.md").write_text("x", encoding="utf-8")
    assert [lang for lang, _ in ready_check.siblings(zh_tw)] == ["zh-TW", "en"]


def test_usage_errors(capsys):
    assert ready_check.main([]) == 2
    assert ready_check.main(["--fast", "posts/a.md"]) == 2
    assert ready_check.main(["posts/no-such-file.md"]) == 2
