"""tools/bluesky_post.py 的測試。只測不連網的部分：哪些文章要發、貼文的內容、怎麼判斷發過了。"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import build  # noqa: E402
import bluesky_post  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"
BASE = "https://anoni.net/news/"


@pytest.fixture
def posts(monkeypatch):
    # 固定現在的時間，fixtures 的文章都算已發布
    monkeypatch.setattr(build, "current_time", lambda: datetime(2026, 9, 30, 12, 0, tzinfo=build.TZ))
    return build.load_site(FIXTURES / "posts", build.load_authors(FIXTURES / "authors.yml"),
                           build.AssetStore(FIXTURES / "assets"))


def at(text: str) -> datetime:
    return datetime.fromisoformat(text)


def test_only_posts_from_the_last_24_hours(posts):
    """9/18 發布的兩篇在 9/18 12:00 要發，zh-TW 與 en 各一則，zh-CN 不發。一天之後就不再列出。"""
    items = bluesky_post.plan(posts, BASE, at("2026-09-18T12:00:00+08:00"))
    assert sorted((i.post.slug, i.tag) for i in items) == [
        ("layout-stress-test", "en"), ("layout-stress-test", "zh"),
        ("zkp-age-verification", "en"), ("zkp-age-verification", "zh")]
    assert not any("/zh-cn/" in i.url for i in items)
    assert bluesky_post.plan(posts, BASE, at("2026-09-19T00:00:01+08:00")) == []


def test_scheduled_posts_are_not_posted(posts):
    """發布時間還沒到的文章不發。9/17 23:00 時 9/18 的兩篇還在排程中，只剩 9/17 之前一天內的文章。"""
    items = bluesky_post.plan(posts, BASE, at("2026-09-17T23:00:00+08:00"))
    assert items == []


def test_item_content(posts):
    items = {(i.post.slug, i.tag): i for i in bluesky_post.plan(posts, BASE, at("2026-09-18T12:00:00+08:00"))}
    zh = items[("zkp-age-verification", "zh")]
    assert zh.url == "https://anoni.net/news/2026/09/zkp-age-verification/"
    assert zh.link == zh.url + "?utm_source=bluesky&utm_medium=social"
    assert zh.text == f"{zh.post.title}\n\n{zh.post.description}"
    # 文章自己的預覽圖優先，沒有時用該語系的共用預覽圖
    assert zh.thumb == zh.post.image
    assert items[("layout-stress-test", "en")].thumb == "og-en.png"
    # 後續稿引用同語系前一篇的貼文
    assert zh.quote_url == "https://anoni.net/news/2026/09/age-verification-roundup/"
    assert items[("zkp-age-verification", "en")].quote_url == "https://anoni.net/news/en/2026/09/age-verification-roundup/"
    assert items[("layout-stress-test", "zh")].quote_url is None


def test_items_are_ordered_oldest_first(posts):
    """由舊到新排，同一篇 zh-TW 在前。前一篇先發，同一輪裡的後續稿才找得到它的貼文。"""
    items = bluesky_post.plan(posts, BASE, at("2026-09-18T12:00:00+08:00"))
    assert [(i.post.slug, i.tag) for i in items] == [
        ("layout-stress-test", "zh"), ("layout-stress-test", "en"),
        ("zkp-age-verification", "zh"), ("zkp-age-verification", "en")]


def test_long_text_falls_back_to_the_title():
    assert bluesky_post.post_text("標題", "短的描述。") == "標題\n\n短的描述。"
    long = "字" * 400
    assert bluesky_post.post_text("標題", long) == "標題"


def test_posted_links_reads_both_embed_types():
    records = [
        {"uri": "at://a/1", "cid": "c1", "value": {"embed": {
            "$type": "app.bsky.embed.external",
            "external": {"uri": "https://anoni.net/news/2026/09/a/?utm_source=bluesky&utm_medium=social"}}}},
        {"uri": "at://a/2", "cid": "c2", "value": {"embed": {
            "$type": "app.bsky.embed.recordWithMedia",
            "media": {"$type": "app.bsky.embed.external", "external": {"uri": "https://anoni.net/news/en/2026/09/b/"}}}}},
        {"uri": "at://a/3", "cid": "c3", "value": {"text": "沒有連結卡片"}},
    ]
    assert bluesky_post.posted_links(records) == {
        "https://anoni.net/news/2026/09/a/": {"uri": "at://a/1", "cid": "c1"},
        "https://anoni.net/news/en/2026/09/b/": {"uri": "at://a/2", "cid": "c2"},
    }


def test_make_record(posts):
    items = {(i.post.slug, i.tag): i for i in bluesky_post.plan(posts, BASE, at("2026-09-18T12:00:00+08:00"))}
    item = items[("zkp-age-verification", "en")]
    blob = {"$type": "blob", "ref": {"$link": "bafy"}, "mimeType": "image/webp", "size": 1}
    now = at("2026-09-18T12:00:00+08:00")

    plain = bluesky_post.make_record(item, blob, None, now)
    assert plain["langs"] == ["en"]
    assert plain["createdAt"] == "2026-09-18T04:00:00.000Z"
    assert plain["embed"]["$type"] == "app.bsky.embed.external"
    assert plain["embed"]["external"] == {"uri": item.link, "title": item.post.title,
                                          "description": item.post.description, "thumb": blob}

    quote = {"uri": "at://did/app.bsky.feed.post/1", "cid": "bafyq"}
    quoted = bluesky_post.make_record(item, blob, quote, now)
    assert quoted["embed"]["$type"] == "app.bsky.embed.recordWithMedia"
    assert quoted["embed"]["record"] == {"$type": "app.bsky.embed.record", "record": quote}
    assert quoted["embed"]["media"] == plain["embed"]
