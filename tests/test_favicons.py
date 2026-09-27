"""tools/fetch_favicons.py 的轉檔、候選網址與登記表。抓取與上傳要連網，不在這裡測。"""

from __future__ import annotations

import io
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import build  # noqa: E402
import fetch_favicons  # noqa: E402
from PIL import Image  # noqa: E402


def encode(image: Image.Image, fmt: str, **kwargs) -> bytes:
    out = io.BytesIO()
    image.save(out, fmt, **kwargs)
    return out.getvalue()


def test_ico_uses_largest_frame():
    frames = Image.new("RGBA", (128, 128), (200, 30, 45, 255))
    data = encode(frames, "ICO", sizes=[(16, 16), (32, 32), (128, 128)])
    with Image.open(io.BytesIO(fetch_favicons.convert(data))) as image:
        assert image.format == "PNG" and image.size == (64, 64)
        # 取到 128 那張縮下來，中心是實心的紅色
        assert image.convert("RGBA").getpixel((32, 32))[:3] == (200, 30, 45)


def test_non_square_is_padded_not_stretched():
    data = encode(Image.new("RGBA", (200, 100), (0, 62, 87, 255)), "PNG")
    with Image.open(io.BytesIO(fetch_favicons.convert(data))) as image:
        rgba = image.convert("RGBA")
        assert rgba.getpixel((32, 2))[3] == 0      # 上方補的是透明邊
        assert rgba.getpixel((32, 32))[3] == 255


def test_output_has_no_metadata_and_fits():
    from PIL import PngImagePlugin
    info = PngImagePlugin.PngInfo()
    info.add_text("Comment", "tracking")
    exif = Image.Exif()
    exif[0x010F] = "Example Camera"
    data = encode(Image.new("RGB", (180, 180), "#ffffff"), "PNG", pnginfo=info, exif=exif)
    out = fetch_favicons.convert(data)
    assert len(out) <= build.MAX_FAVICON_BYTES
    with Image.open(io.BytesIO(out)) as image:
        assert not image.getexif() and not getattr(image, "text", None)


def test_noisy_icon_is_quantized_under_limit():
    import os
    noise = Image.frombytes("RGBA", (256, 256), os.urandom(256 * 256 * 4))
    assert len(fetch_favicons.convert(encode(noise, "PNG"))) <= build.MAX_FAVICON_BYTES


@pytest.mark.parametrize("data, expected", [
    (b'<svg xmlns="http://www.w3.org/2000/svg"></svg>', "SVG"),
    (b"<!DOCTYPE html><html></html>", "SVG 或網頁"),
])
def test_svg_and_html_are_rejected(data, expected):
    with pytest.raises(ValueError, match=expected):
        fetch_favicons.convert(data)


def test_tiny_icon_is_rejected():
    with pytest.raises(ValueError, match="太小"):
        fetch_favicons.convert(encode(Image.new("RGBA", (8, 8)), "PNG"))


def test_candidates_prefer_large_and_skip_svg():
    page = """
    <link rel="icon" href="/favicon-16.png" sizes="16x16">
    <link rel="icon" type="image/svg+xml" href="/icon.svg">
    <link rel="mask-icon" href="/mask.png">
    <link rel='apple-touch-icon' href='/touch.png'>
    <link rel="icon" href="https://cdn.example.org/icon-512.png" sizes="512x512">
    <link rel="stylesheet" href="/style.css">
    """
    assert fetch_favicons.candidates("https://example.org/", page) == [
        "https://cdn.example.org/icon-512.png",
        "https://example.org/touch.png",
        "https://example.org/favicon-16.png",
        "https://example.org/apple-touch-icon.png",
        "https://example.org/favicon.ico",
    ]


def test_candidates_fall_back_to_conventions():
    assert fetch_favicons.candidates("https://example.org/", "") == [
        "https://example.org/apple-touch-icon.png", "https://example.org/favicon.ico"]


@pytest.mark.parametrize("host, parent", [
    ("support.signal.org", "signal.org"),
    ("signal.org", None),
])
def test_parent_host(host, parent):
    assert fetch_favicons.parent_host(host) == parent


def test_registry_round_trip_passes_build(tmp_path):
    hosts = {
        "signal.org": {"icon": "signal.org-0123abcd.png", "from": "https://signal.org/a.png"},
        "support.signal.org": {"same_as": "signal.org"},
        "openai.com": {"none": "抓取被擋下，理由裡有 \"引號\""},
    }
    path = tmp_path / "favicons.toml"
    path.write_text(fetch_favicons.dump_registry(hosts), encoding="utf-8")
    assert build.load_favicons(path) == hosts
    # 依主機名稱排序，diff 才看得出改了哪幾筆
    text = path.read_text(encoding="utf-8")
    assert text.index('"openai.com"') < text.index('"signal.org"') < text.index('"support.signal.org"')


def test_fetched_name_follows_content():
    a = fetch_favicons.Fetched("eff.org", b"one", "x")
    b = fetch_favicons.Fetched("eff.org", b"two", "x")
    assert a.name != b.name and build.FAVICON_NAME_RE.match(a.name)


def test_project_registry_is_valid():
    build.load_favicons(build.FAVICONS_PATH)


def test_archive_fallback_when_site_blocks(monkeypatch):
    """原站整個擋下時，改從 Internet Archive 取同一個網站的首頁與圖示。"""
    icon = encode(Image.new("RGBA", (180, 180), (0, 0, 0, 255)), "PNG")
    page = b'<link rel="apple-touch-icon" href="/apple-icon.png">'

    def fake_fetch(url: str) -> bytes:
        if not url.startswith("https://web.archive.org/"):
            raise OSError("HTTP Error 403: Forbidden")
        return page if url.endswith("openai.com/") else icon

    monkeypatch.setattr(fetch_favicons, "fetch", fake_fetch)
    item, tried = fetch_favicons.fetch_icon("openai.com", "openai.com")
    assert item and item.source == fetch_favicons.archived("https://openai.com/apple-icon.png")
    assert any("403" in reason for reason in tried)


def test_fetch_decompresses_archive_gzip(monkeypatch):
    import gzip

    class Response(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    monkeypatch.setattr(fetch_favicons.urllib.request, "urlopen",
                        lambda *args, **kwargs: Response(gzip.compress(b"\x00\x00\x01\x00icon")))
    assert fetch_favicons.fetch("https://web.archive.org/web/20260927id_/https://example.org/favicon.ico") == b"\x00\x00\x01\x00icon"
