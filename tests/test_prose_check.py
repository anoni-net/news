import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import prose_check  # noqa: E402

FRONT = "---\ntitle: 標題\ndescription: 甲，乙，丙，丁。\n---\n\n"


def write(tmp_path: Path, rel: str, body: str, front: str = FRONT) -> Path:
    path = tmp_path / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front + body, encoding="utf-8")
    return path


def body_items(path: Path) -> list[str]:
    return [item for item in prose_check.check(path) if "front matter" not in item]


def test_long_zh_sentence_and_description(tmp_path):
    path = write(tmp_path, "posts/zh-CN/a.md", "一，二，三，四。短句。\n")
    found = prose_check.check(path)
    assert any("front matter：4 個逗號分句" in item for item in found)
    assert f"{path}:6：4 個逗號分句：一，二，三，四。" in found


def test_quotes_links_and_code_do_not_count_or_split(tmp_path):
    body = (
        "設定成「甲，乙。丙，丁」之後（例如，這樣），依[標題，副標，第三](https://example.com)的說明，"
        "`a，b，c` 的值變了。原文寫「甲。」乙。三。四。\n"
    )
    assert body_items(write(tmp_path, "posts/a.md", body)) == []


def test_paragraph_length_limits(tmp_path):
    body = "一。二。三。四。五。\n\n## 小標題\n\n一。二。\n"
    path = write(tmp_path, "posts/a.md", body)
    assert body_items(path) == [f"{path}:6：這一段有 5 句，超過 4 句"]
    assert body_items(write(tmp_path, "history/a.md", body)) == []


def test_fences_lists_and_admonitions_are_skipped(tmp_path):
    body = (
        "~~~\n一，二，三，四。\n~~~\n\n```\n一，二，三，四。\n```\n\n"
        "- 一，二，三，四。\n1. 一，二，三，四。\n!!! tip\n    一，二，三，四。\n"
    )
    assert body_items(write(tmp_path, "posts/a.md", body)) == []


def test_history_snapshot_texts_are_checked(tmp_path):
    front = (
        "---\nsnapshots:\n  - date: 2020-10-05\n    description: 甲，乙，丙，丁。\n"
        "    also:\n      - text: 一，二，三，四。\n---\n\n"
    )
    found = prose_check.check(write(tmp_path, "history/10-05.md", "短句。\n", front))
    assert len([item for item in found if "front matter" in item]) == 2


def test_english_checks_paragraph_length_only(tmp_path):
    body = "One, two, three, four, five. The U.S. Senate passed it. Three. Four.\n\nOne. Two. Three. Four. Five.\n"
    path = write(tmp_path, "posts/en/a.md", body)
    assert body_items(path) == [f"{path}:8：這一段有 5 句，超過 4 句"]


def test_file_without_front_matter_and_missing_file(tmp_path, capsys):
    path = write(tmp_path, "posts/a.md", "一，二，三，四。\n", front="")
    assert prose_check.check(path) == [f"{path}:1：4 個逗號分句：一，二，三，四。"]
    assert prose_check.main([str(tmp_path / "nope.md")]) == 2
    assert "找不到檔案" in capsys.readouterr().out


def test_english_quotes_lowercase_and_abbreviations(tmp_path):
    body = 'He said "stop." Then he left. iOS 27 ships soon. Sen. Smith of Washington, D.C. agreed. Inc. filings. Five.\n'
    path = write(tmp_path, "posts/en/a.md", body)
    # 6 句：引號後、小寫開頭都會切，Sen.、D.C.、Inc. 不切
    assert body_items(path) == [f"{path}:6：這一段有 6 句，超過 4 句"]


def test_main_exit_codes_and_broken_front_matter(tmp_path, capsys):
    assert prose_check.main([]) == 2
    assert "用法" in capsys.readouterr().out
    clean = write(tmp_path, "posts/clean.md", "短句。\n", front="---\ndescription: 短句。\n---\n\n")
    assert prose_check.main([str(clean)]) == 0
    broken = write(tmp_path, "posts/broken.md", "短句。\n", front="---\ndescription: x: y\n---\n\n")
    assert prose_check.main([str(broken)]) == 2
    assert "front matter 無法解析" in capsys.readouterr().out


def test_parent_folders_outside_the_site_are_ignored(tmp_path):
    path = write(tmp_path / "en" / "history", "posts/a.md", "一。二。三。四。五。\n")
    assert body_items(path) == [f"{path}:6：這一段有 5 句，超過 4 句"]


def test_english_abbreviations_before_lowercase_do_not_split(tmp_path):
    body = "Smith et al. found it, etc. and more. See Fig. 3 for approx. 5 percent... maybe. Four. Five.\n"
    path = write(tmp_path, "posts/en/a.md", body)
    assert body_items(path) == []
