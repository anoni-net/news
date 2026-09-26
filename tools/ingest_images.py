"""維護者合併前，把稿件裡的圖片搬到 assets.anoni.net。規則見 SPEC.md「圖片」。

    uv run tools/ingest_images.py --dry-run posts/2026-09-18-slug.md   # 只下載與轉檔，列出計畫
    NEWS_ASSETS_RSYNC=<rsync 目標> uv run tools/ingest_images.py posts/2026-09-18-slug.md

每一張不在 assets.anoni.net 的圖：下載、依 EXIF 轉正方向、清掉 metadata、轉成 WebP、
長邊縮到 1600px 以內，上傳到 $NEWS_ASSETS_RSYNC/YYYY/MM/<slug>/，確認
https://assets.anoni.net/news/YYYY/MM/<slug>/figure-N.webp 回 200 之後，才改寫文章裡的網址。

授權與來源要人審核，工具只把每張圖的原始網址、替代文字與圖說列出來。
"""

from __future__ import annotations

import argparse
import io
import os
import re
import subprocess
import sys
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

MAX_EDGE = 1600
START_QUALITY = 82
IMAGE_MD_RE = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<url>[^)\s]+)(?:\s+"(?P<title>[^"]*)")?\)')
FIGURE_NAME_RE = re.compile(r"figure-(\d+)\.webp$")


@dataclass
class Found:
    url: str
    alt: str
    title: str


def find_images(text: str) -> list[Found]:
    """內文的圖片語法與 front matter 的 image，略過程式碼區塊。"""
    found, in_fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("image:"):
            found.append(Found(line.split(":", 1)[1].strip(), "（front matter 的 image）", "（預覽圖不需要圖說）"))
        for match in IMAGE_MD_RE.finditer(line):
            found.append(Found(match["url"], match["alt"], match["title"] or ""))
    return found


def convert(data: bytes) -> bytes:
    """轉正方向、清掉 metadata、縮圖、轉成 WebP，壓到規格的大小上限以內。"""
    with Image.open(io.BytesIO(data)) as source:
        image = ImageOps.exif_transpose(source)
        image = image.convert("RGBA" if image.mode in ("RGBA", "LA", "P") else "RGB")
        image.thumbnail((MAX_EDGE, MAX_EDGE))
    quality = START_QUALITY
    while True:
        out = io.BytesIO()
        # 不傳 exif、xmp、icc_profile，另存時不會帶任何 metadata
        image.save(out, "WEBP", quality=quality, method=6)
        if out.tell() <= build.MAX_IMAGE_BYTES or quality <= 40:
            return out.getvalue()
        quality -= 8


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "anoni-net-news-ingest"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def is_live(url: str) -> bool:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "anoni-net-news-ingest"})
    for _ in range(5):
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status == 200:
                    return True
        except OSError:
            pass
        time.sleep(2)
    return False


def rewrite(text: str, mapping: dict[str, str]) -> str:
    """只換圖片語法與 front matter image 裡的網址，內文其他地方出現同一個網址不動。"""
    def replace_md(match: re.Match) -> str:
        url = match["url"]
        return match.group(0).replace(url, mapping[url], 1) if url in mapping else match.group(0)

    lines, in_fence = [], False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        elif not in_fence:
            if line.startswith("image:"):
                url = line.split(":", 1)[1].strip()
                if url in mapping:
                    line = f"image: {mapping[url]}\n"
            line = IMAGE_MD_RE.sub(replace_md, line)
        lines.append(line)
    return "".join(lines)


def ingest(post_path: Path, dry_run: bool) -> int:
    text = post_path.read_text(encoding="utf-8")
    meta, _ = build.split_front_matter(text, post_path.name)
    created = meta["date"]["created"] if isinstance(meta["date"], dict) else meta["date"]
    folder = f"{created:%Y}/{created:%m}/{meta['slug']}"
    base_url = f"{build.ASSETS_PREFIX}{folder}/"

    images = find_images(text)
    external = []
    for image in images:
        if not image.url.startswith(build.ASSETS_PREFIX) and image.url not in [e.url for e in external]:
            external.append(image)
    if not external:
        print(f"{post_path.name}：沒有需要搬的圖片")
        return 0

    used = [int(m.group(1)) for i in images if (m := FIGURE_NAME_RE.search(i.url)) and i.url.startswith(base_url)]
    number = max(used, default=0)
    staging = ROOT / ".cache" / "ingest" / folder
    staging.mkdir(parents=True, exist_ok=True)

    mapping, problems = {}, []
    for image in external:
        number += 1
        name = f"figure-{number}.webp"
        try:
            data = convert(download(image.url))
        except (OSError, ValueError) as error:
            problems.append(f"{image.url}：下載或轉檔失敗（{error}）")
            continue
        (staging / name).write_bytes(data)
        build.check_image(staging / name, name, problems)
        mapping[image.url] = base_url + name
    if problems:
        print("處理失敗，文章沒有改動：")
        print("\n".join(f"  {p}" for p in problems))
        return 1

    if not dry_run:
        target = os.environ.get("NEWS_ASSETS_RSYNC")
        if not target:
            print("沒有設定 NEWS_ASSETS_RSYNC（rsync 的目標，例如 host:/path/news），圖片沒有上傳")
            return 1
        subprocess.run(["rsync", "-a", "--mkpath", f"{staging}/", f"{target.rstrip('/')}/{folder}/"], check=True)
        missing = [url for url in mapping.values() if not is_live(url)]
        if missing:
            print("上傳之後這些網址沒有回 200，文章沒有改動：")
            print("\n".join(f"  {url}" for url in missing))
            return 1
        post_path.write_text(rewrite(text, mapping), encoding="utf-8")

    print(f"{post_path.name}：{'（試跑，沒有上傳也沒有改文章）' if dry_run else '已上傳並改寫網址'}")
    print("請逐張審核授權與來源，並確認替代文字與圖說：")
    for image in external:
        print(f"\n  {mapping[image.url]}")
        print(f"    原始網址：{image.url}")
        print(f"    替代文字：{image.alt or '（缺，要補）'}")
        print(f"    圖說：{image.title or '（缺，要補出處與授權，例如 圖：EFF，CC-BY 4.0）'}")
    print(f"\n轉好的檔案在 {staging.relative_to(ROOT)}/")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("posts", nargs="+", type=Path, help="要處理的文章")
    parser.add_argument("--dry-run", action="store_true", help="只下載與轉檔，不上傳也不改文章")
    args = parser.parse_args()
    status = 0
    for post in args.posts:
        status |= ingest(post, args.dry_run)
    return status


if __name__ == "__main__":
    sys.exit(main())
