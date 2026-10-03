"""產生導讀與導讀歷史日期頁的社群預覽卡片，上傳到圖片主機，寫進 og_cards.toml。規則見 SPEC.md「預覽卡片」。

    uv run tools/make_cards.py --dry-run [posts/<檔名>.md | history/MM-DD.md ...]
    NEWS_ASSETS_RSYNC=<rsync 目標> uv run tools/make_cards.py [posts/<檔名>.md | history/MM-DD.md ...]

沒給檔名時處理所有還沒有卡片、或內容改過讓卡片過期的頁面，排程中的也算。三個語系各一張，
用 tools/card.html 填入標題、分類（導讀歷史是「導讀歷史 · 年份」）與日期，再用 Chrome 截成
1200×630 的 PNG。導讀歷史的日期頁用那一天最新的一則快照。

--dry-run 只產圖，放在 .cache/cards/，另外產生一頁 .cache/cards/preview.html 把卡片排在一起看。
拿掉 --dry-run 之後上傳到 $NEWS_ASSETS_RSYNC/og/，確認 https://assets.anoni.net/news/og/ 底下
回 200，才寫進 og_cards.toml。卡片不進 repo，repo 裡只有登記表。

需要 Chrome 與 Noto Serif CJK、Noto Sans CJK 的 TC 與 SC 字型。
"""
from __future__ import annotations

import argparse
import io
import json
import os
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

CACHE = ROOT / ".cache" / "cards"
CHROME = os.environ.get("CHROME", "google-chrome")
MAX_BYTES = 150_000


def render(data: dict, out: Path) -> None:
    """填好模板，用 Chrome 截圖，再轉成調色盤 PNG 縮小檔案，不留 metadata。"""
    html_text = build.CARD_TEMPLATE.read_text(encoding="utf-8")
    html_text = html_text.replace("LOGO_URL", (ROOT / "static" / "logo-wordmark-white.svg").as_uri())
    html_text = html_text.replace("CARD_DATA", json.dumps(data, ensure_ascii=False))
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "card.html"
        page.write_text(html_text, encoding="utf-8")
        shot = Path(tmp) / "shot.png"
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--password-store=basic", "--window-size=1200,630", f"--screenshot={shot}",
                        page.as_uri()], check=True, capture_output=True, timeout=60)
        image = Image.open(shot).convert("RGB")
    if image.size != (1200, 630):
        raise SystemExit(f"{out.name}：卡片尺寸是 {image.size}，應該是 1200×630")
    out.parent.mkdir(parents=True, exist_ok=True)
    buffer = io.BytesIO()
    image.quantize(colors=128, method=Image.Quantize.MEDIANCUT).save(buffer, "PNG", optimize=True)
    if buffer.tell() > MAX_BYTES:
        raise SystemExit(f"{out.name}：卡片 {buffer.tell()} bytes，超過 {MAX_BYTES}")
    out.write_bytes(buffer.getvalue())


def pending(paths: list[str]) -> list[tuple[str, str, tuple[str, str, dict]]]:
    """要產生的卡片：(顯示用的檔名, 語系, card)。指定的檔案全部重做，沒指定時只做缺的與過期的。"""
    authors = build.load_authors(ROOT / "authors.yml")
    cards = build.load_cards()
    wanted = {str(Path(p).with_suffix("")).removeprefix("posts/") for p in paths}
    items = []
    for post in build.load_site(ROOT / "posts", authors):
        for version in post.translations.values() or [post]:
            if not version.image:  # 指定了 image 的文章用那張圖
                items.append((post.path.stem, version.where, version.lang, build.post_card(version)))
    days, _ = build.load_history(ROOT / "history", authors)
    for day in days:
        for version in day.translations.values() or [day]:
            if version.snapshots:
                items.append((f"history/{day.mmdd}", version.where, version.lang, build.history_card(version, version.snapshots[-1])))
    if wanted:
        return [(where, lang.code, card) for name, where, lang, card in items if name in wanted]
    return [(where, lang.code, card) for _, where, lang, card in items if build.card_url(card, lang, cards) is None]


def write_registry(cards: dict[str, dict[str, str]]) -> None:
    lines = ["# 每篇導讀的社群預覽卡片，由 tools/make_cards.py 寫入，不要手改。見 SPEC.md「預覽卡片」。",
             "# 鍵是文章的檔名（不含 .md）或 history/MM-DD，值是三個語系的卡片在 https://assets.anoni.net/news/ 底下的路徑。",
             "", "[cards]"]
    for stem in sorted(cards):
        values = ", ".join(f'"{code}" = "{rel}"' for code, rel in sorted(cards[stem].items()))
        lines.append(f'"{stem}" = {{ {values} }}')
    build.CARDS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def preview(made: list[tuple[str, Path]]) -> Path:
    rows = "\n".join(f'<figure><img src="{path.relative_to(CACHE)}" width="600" height="315" alt="">'
                     f"<figcaption>{where}</figcaption></figure>" for where, path in made)
    page = CACHE / "preview.html"
    page.write_text(f"""<!DOCTYPE html><meta charset="utf-8"><title>預覽卡片</title>
<style>body{{font-family:sans-serif;display:flex;flex-wrap:wrap;gap:24px;padding:24px;background:#eee}}
figure{{margin:0}}img{{display:block;box-shadow:0 1px 4px #0004}}figcaption{{font-size:13px;margin-top:6px}}</style>
{rows}
""", encoding="utf-8")
    return page


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("posts", nargs="*", help="只處理這幾篇（posts/ 底下的檔名），沒給就處理缺的與過期的")
    parser.add_argument("--dry-run", action="store_true", help="只產圖與預覽頁，不上傳也不改登記表")
    args = parser.parse_args()

    todo = pending(args.posts)
    if not todo:
        print("每篇導讀都有最新的卡片")
        return 0
    made = []
    for where, _, (_, rel, data) in todo:
        out = CACHE / rel
        render(data, out)
        made.append((where, out))
        print(f"{where} → {rel}（{out.stat().st_size // 1024} KB）")
    print(f"預覽：{preview(made)}")
    if args.dry_run:
        return 0

    target = os.environ.get("NEWS_ASSETS_RSYNC")
    if not target:
        print("沒有設定 NEWS_ASSETS_RSYNC（rsync 的目標，例如 host:/path/news），卡片沒有上傳，登記表沒有改動")
        return 1
    # --relative 搭配 /./ 保留 og/YYYY/MM/ 這一段路徑
    files = [f"{CACHE}/./{rel}" for _, _, (_, rel, _) in todo]
    subprocess.run(["rsync", "-a", "--relative", "--mkpath", *files, target.rstrip("/") + "/"], check=True)
    cards = build.load_cards()
    for _, code, (key, rel, _) in todo:
        url = build.ASSETS_PREFIX + rel
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "anoni-news-cards"})
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise SystemExit(f"{url} 回 {response.status}，登記表沒有改動")
        cards.setdefault(key, {})[code] = rel
    write_registry(cards)
    print(f"已上傳 {len(made)} 張，寫進 {build.CARDS_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
