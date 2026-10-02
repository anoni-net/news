"""導讀歷史的測試。規則見 SPEC.md「導讀歷史」。每一項檢查都放一個故意寫壞的例子。"""

from __future__ import annotations

import sys
import textwrap
from datetime import date, datetime
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

AUTHORS = build.load_authors(ROOT / "tests" / "fixtures" / "authors.yml")
NOW = datetime(2026, 10, 1, 12, 0, tzinfo=build.TZ)


def snapshot_yaml(date_value: str = "2026-09-29T00:10:00+08:00", event: str = "2023-09-29", extra: str = "") -> str:
    return f"""\
  - date: {date_value}
    title: 測試事件
    description: 一句話。
    event: {event}
    sources:
      - title: Source
        url: https://example.org/
    authors:
      - anoni-net
{extra}"""


def write_day(tmp_path: Path, snapshots: str, body: str, name: str = "09-29.md") -> Path:
    path = tmp_path / name
    path.write_text(f"---\nsnapshots:\n{snapshots}---\n\n{textwrap.dedent(body)}", encoding="utf-8")
    return path


def load(tmp_path: Path, snapshots: str, body: str, name: str = "09-29.md"):
    return build.load_history_day(write_day(tmp_path, snapshots, body, name), AUTHORS, build.DEFAULT_LANG, NOW)


def problems_of(tmp_path: Path, snapshots: str, body: str, name: str = "09-29.md") -> list[str]:
    try:
        load(tmp_path, snapshots, body, name)
    except build.BuildError as error:
        return error.problems
    return []


GOOD_BODY = "## 2026 {#y2026}\n\n一段回看。\n"


def test_good_day_loads(tmp_path):
    day = load(tmp_path, snapshot_yaml(), GOOD_BODY)
    assert day.rel == "history/09-29/"
    assert [snap.year for snap in day.snapshots] == [2026]
    assert day.snapshots[0].anchor == "y2026"


def test_years_are_appended_in_order(tmp_path):
    snapshots = snapshot_yaml() + snapshot_yaml("2027-09-29T00:10:00+08:00")
    body = GOOD_BODY + "\n## 2027 {#y2027}\n\n隔年增補的一段。\n"
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(build, "HISTORY_MAX_SCHEDULE_DAYS", 400)
        day = build.load_history_day(write_day(tmp_path, snapshots, body), AUTHORS, build.DEFAULT_LANG, NOW)
    assert [snap.year for snap in day.snapshots] == [2026, 2027]


@pytest.mark.parametrize("body, expected", [
    ("## 二〇二六 {#y2026}\n\n一段。\n", "小標題只能寫年份"),
    ("前言\n\n## 2026 {#y2026}\n\n一段。\n", "第一個年份小標題之前不能有內文"),
    ("## 2026 {#y2026}\n\n第一段。\n\n第二段。\n", "每個年份底下寫一段"),
    ("## 2026 {#y2026}\n\n- 清單\n", "每個年份底下寫一段"),
    ("## 2025 {#y2025}\n\n一段。\n", "跟小標題的 2025 不同"),
])
def test_body_rules(tmp_path, body, expected):
    assert any(expected in p for p in problems_of(tmp_path, snapshot_yaml(), body))


def test_heading_count_matches_snapshots(tmp_path):
    body = GOOD_BODY + "\n## 2027 {#y2027}\n\n多出來的一段。\n"
    assert any("要一個年份對一筆" in p for p in problems_of(tmp_path, snapshot_yaml(), body))


@pytest.mark.parametrize("name, event, expected", [
    ("02-30.md", "2023-02-28", "不是存在的日期"),
    ("09-29.md", "2023-09-28", "event 的月日跟檔名"),
    ("09-29.md", "2026-09-29", "event 要早於"),
])
def test_dates_follow_the_file_name(tmp_path, name, event, expected):
    assert any(expected in p for p in problems_of(tmp_path, snapshot_yaml(event=event), GOOD_BODY, name))


def test_date_must_fall_on_the_file_day(tmp_path):
    problems = problems_of(tmp_path, snapshot_yaml("2026-09-30T00:10:00+08:00"), GOOD_BODY)
    assert any("date 的月日跟檔名" in p for p in problems)


@pytest.mark.parametrize("date_value, ok", [
    ("2026-10-29T00:10:00+08:00", True),    # 28 天後，在導讀歷史的範圍內
    ("2026-11-10T00:10:00+08:00", False),   # 40 天後，超過 30 天
])
def test_history_can_be_scheduled_further_than_posts(tmp_path, date_value, ok):
    name = date_value[5:10] + ".md"
    event = "2020" + date_value[4:10]
    problems = problems_of(tmp_path, snapshot_yaml(date_value, event), "## 2026 {#y2026}\n\n一段。\n", name)
    assert (not any("排程最多" in p for p in problems)) == ok


@pytest.mark.parametrize("checked, expected", [
    ("2026-10-02", "晚於今天"),
    ("not-a-date", "checked 要寫成 YYYY-MM-DD"),
])
def test_checked_is_a_past_date(tmp_path, checked, expected):
    snapshots = snapshot_yaml("2026-10-20T00:10:00+08:00", "2020-10-20", f"    checked: {checked}\n")
    assert any(expected in p for p in problems_of(tmp_path, snapshots, GOOD_BODY, "10-20.md"))


def test_report_lists_snapshots_that_need_a_recheck(tmp_path):
    # 9 月 10 日就寫好、10 月 5 日上線，現況查證早於上線前 7 天，要列出來
    stale = snapshot_yaml("2026-10-05T00:10:00+08:00", "2020-10-05", "    checked: 2026-09-10\n")
    fresh = snapshot_yaml("2026-10-06T00:10:00+08:00", "2020-10-06", "    checked: 2026-09-30\n")
    days = [load(tmp_path, stale, GOOD_BODY, "10-05.md"), load(tmp_path, fresh, GOOD_BODY, "10-06.md")]
    report = build.history_report(days, NOW.date())
    assert "10-05 history/10-05.md" in report
    assert "10-06 history/10-06.md" not in report
    assert "- [ ] 10-02（history/10-02.md 的 2026）" in report
    assert "10-05（history/10-05.md" not in report


def test_snapshot_without_checked_counts_as_checked_on_its_date(tmp_path):
    day = load(tmp_path, snapshot_yaml("2026-10-05T00:10:00+08:00", "2020-10-05"), GOOD_BODY, "10-05.md")
    assert not day.snapshots[0].needs_recheck


def test_draft_snapshot_is_left_out(tmp_path):
    day = load(tmp_path, snapshot_yaml(extra="    draft: true\n"), GOOD_BODY)
    assert day.snapshots == []


def test_timeline_puts_history_after_the_posts_of_the_day(tmp_path):
    day = load(tmp_path, snapshot_yaml(), GOOD_BODY)
    days = build.timeline([], day.snapshots)
    assert days == [{"date": date(2026, 9, 29), "posts": [], "history": day.snapshots[0]}]


def test_reader_mode_skips_sources_and_language_links(tmp_path):
    """日期頁的正文太短，閱讀模式會放寬條件重抓，role="navigation" 擋不住。原文、署名與語系連結
    包在 aside 裡，Readability 一律移除。索引頁的日曆格子也一樣，閱讀模式裡只留日期加標題的清單。"""
    import re

    targets, _, _ = build.build(ROOT / "posts", tmp_path, only=["clearnet"])
    out = targets["clearnet"].out
    day = next((out / "history").glob("[0-9][0-9]-[0-9][0-9]/index.html")).read_text(encoding="utf-8")
    assert '<meta name="author" content="anoni.net 社群">' in day
    without_asides = re.sub(r"<aside\b.*?</aside>", "", day, flags=re.S)
    article = without_asides[without_asides.index("<article"):without_asides.index("</article>")]
    for leftover in ("story__langs", "snapshot__sources", "snapshot__byline"):
        assert leftover not in article, leftover
    assert "snapshot__body" in article
    index = (out / "history" / "index.html").read_text(encoding="utf-8")
    index_text = re.sub(r"<aside\b.*?</aside>", "", index, flags=re.S)
    assert "history-month__grid" not in index_text and "story__langs" not in index_text
    assert "history-month__list" in index_text
