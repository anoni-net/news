"""tools/ingest_images.py 的轉檔與改寫。上傳與線上確認要連到圖片主機，不在這裡測。"""

from __future__ import annotations

import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import ingest_images  # noqa: E402
from PIL import Image  # noqa: E402


def jpeg_with_exif(size=(3000, 2000)) -> bytes:
    exif = Image.Exif()
    exif[0x010F] = "Example Camera"   # Make
    exif[0x0112] = 6                  # Orientation：需要轉 90 度
    out = io.BytesIO()
    Image.new("RGB", size, "#003e57").save(out, "JPEG", exif=exif)
    return out.getvalue()


def test_convert_strips_metadata_and_resizes():
    data = ingest_images.convert(jpeg_with_exif())
    with Image.open(io.BytesIO(data)) as image:
        assert image.format == "WEBP"
        assert not image.getexif()
        assert "exif" not in image.info and "xmp" not in image.info
        # Orientation 6 轉正之後變成直的，長邊縮到 1600
        assert image.size == (1067, 1600)
    assert len(data) <= 300_000


def test_find_and_rewrite_skip_code_blocks():
    text = (
        "---\nimage: https://example.org/og.png\n---\n\n"
        '![圖](https://example.org/a.png "圖：x")\n\n'
        "```\n![圖](https://example.org/a.png)\n```\n\n"
        "網址文字 https://example.org/a.png 不動\n"
    )
    found = ingest_images.find_images(text)
    assert [f.url for f in found] == ["https://example.org/og.png", "https://example.org/a.png"]
    mapping = {"https://example.org/a.png": "https://assets.anoni.net/news/x/figure-1.webp",
               "https://example.org/og.png": "https://assets.anoni.net/news/x/figure-2.webp"}
    out = ingest_images.rewrite(text, mapping)
    assert '![圖](https://assets.anoni.net/news/x/figure-1.webp "圖：x")' in out
    assert "image: https://assets.anoni.net/news/x/figure-2.webp" in out
    assert "```\n![圖](https://example.org/a.png)\n```" in out
    assert "網址文字 https://example.org/a.png 不動" in out
