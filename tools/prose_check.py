"""送審前的自查：列出句子太長與段落太長的地方，寫稿的人逐處判斷，該拆的拆完再交給審稿。

docs_style_lint.py 只抓詞表上的句型。寫作規則的「一句話接了四個以上的逗號分句時拆成兩句」與
guides/ 規定的段落句數要靠逐句讀，2026-10 一篇導讀的第一輪審稿列了 25 條，多數是這兩類。這兩類可以
機械地找出來，先處理掉，審稿的人就能專心看指涉、擬人化與事實。

- 中文：一句有 4 個以上的分句（3 個以上的「，」）就列出。「」、（）、連結文字與 inline code 裡的逗號不算
- 段落句數：導讀與短訊超過 4 句、導讀歷史超過 5 句就列出。英文的句數是近似值，常見縮寫不切句
- 小標題、清單、引言、表格、程式碼區塊與 admonition（`!!!`、`???` 與四格縮排）整行不檢查
- 英文只檢查段落句數，不數逗號，英文的長句要靠審稿逐句讀
- front matter 的 description，以及導讀歷史快照的 description 與「同一天還有」只檢查逗號

列出的是要人判斷的位置，照錄的原文標題這類不該改的可以留著。有列出項目時結束代碼為 1，
參數錯誤、找不到檔案或 front matter 無法解析時為 2。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

USAGE = "用法：uv run tools/prose_check.py posts/<檔名>.md posts/zh-CN/<檔名>.md posts/en/<檔名>.md"
MAX_COMMAS = 2
MAX_SENTENCES = {"history": 5}
DEFAULT_MAX_SENTENCES = 4
# 引號、括號、連結文字與 inline code 裡的內容，切句與數逗號時都當成一個字
QUOTED = re.compile(r"「[^「」]*」|『[^『』]*』|（[^（）]*）|\[[^\]]*\]\([^)]*\)|`[^`]*`")
ZH_END = re.compile(r"(?<=[。！？])")
EN_ABBREVIATIONS = ("U.S.", "U.K.", "D.C.", "e.g.", "i.e.", "No.", "Mr.", "Ms.", "Dr.", "St.", "vs.", "Sen.", "Rep.", "Inc.", "Corp.", "Ltd.", "Co.", "Prof.", "Mt.", "Fig.",
    "et al.", "etc.", "approx.", "Jan.", "Feb.", "Mar.", "Apr.", "Aug.", "Sept.", "Sep.", "Oct.", "Nov.", "Dec.",
)
# 句號後面可能先接引號或括號，下一句也可能是小寫開頭的產品名（iOS、npm）
EN_END = re.compile(r"(?:(?<=[.!?])|(?<=[.!?][\"”’)])|(?<=[.!?][\"”’)]{2}))\s+(?=[A-Za-z0-9\"“(`\x00])")
SKIP_PREFIXES = ("#", "- ", "* ", "+ ", "|", ">", "!!!", "???")
FENCES = ("```", "~~~")


def site_parts(path: Path) -> tuple[str, ...]:
    """posts/ 或 history/ 之後的路徑段落，絕對路徑上層的資料夾名稱不影響判斷。"""
    parts = path.parts
    for index in range(len(parts) - 1, -1, -1):
        if parts[index] in ("posts", "history", "pages"):
            return parts[index:]
    return parts[-2:]


def is_english(path: Path) -> bool:
    return "en" in site_parts(path)[:-1]


def max_sentences(path: Path) -> int:
    return next((limit for part, limit in MAX_SENTENCES.items() if part in site_parts(path)[:1]), DEFAULT_MAX_SENTENCES)


def mask(text: str) -> tuple[str, list[str]]:
    """把引號、括號、連結與程式碼換成佔位字，回傳換過的文字與原本的片段。"""
    pieces: list[str] = []

    def keep(match: re.Match) -> str:
        pieces.append(match.group(0))
        return f"\x00{len(pieces) - 1}\x00"

    return QUOTED.sub(keep, text), pieces


def unmask(text: str, pieces: list[str]) -> str:
    return re.sub(r"\x00(\d+)\x00", lambda match: pieces[int(match.group(1))], text)


def split_sentences(text: str, english: bool) -> list[str]:
    """回傳換過佔位字的句子。佔位字裡的句號不會切句，逗號也不會被數到。"""
    masked, _ = mask(text)
    if english:
        masked = masked.replace("...", "\x01\x01\x01")
        for abbreviation in EN_ABBREVIATIONS:
            masked = masked.replace(abbreviation, abbreviation.replace(".", "\x01"))
        parts = [part.replace("\x01", ".") for part in EN_END.split(masked)]
    else:
        parts = ZH_END.split(masked)
    return [part.strip() for part in parts if part.strip()]


class FrontMatterError(ValueError):
    pass


def front_matter_texts(meta) -> list[str]:
    if not isinstance(meta, dict):
        raise FrontMatterError("front matter 不是鍵值對")
    texts = [meta.get("description")]
    for snap in meta.get("snapshots") or []:
        if isinstance(snap, dict):
            texts.append(snap.get("description"))
            texts += [item.get("text") for item in snap.get("also") or [] if isinstance(item, dict)]
    return [text for text in texts if isinstance(text, str)]


def paragraphs(path: Path) -> tuple[list[tuple[int, str]], list[str]]:
    """回傳 (起始行號, 段落文字) 的清單，以及 front matter 裡要檢查的句子。"""
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    meta_texts: list[str] = []
    offset = 0
    if text.startswith("---\n") and text.count("---\n") >= 2:
        _, meta, body = text.split("---\n", 2)
        try:
            meta_texts = front_matter_texts(yaml.safe_load(meta) or {})
        except yaml.YAMLError as error:
            raise FrontMatterError(f"front matter 無法解析：{error}") from error
        offset = meta.count("\n") + 2
        text = body
    found: list[tuple[int, str]] = []
    block: list[str] = []
    start = 0
    fenced = False
    for number, line in enumerate(text.split("\n"), offset + 1):
        stripped = line.strip()
        if stripped.startswith(FENCES):
            fenced = not fenced
            continue
        skip = fenced or stripped.startswith(SKIP_PREFIXES) or re.match(r"\d+\. ", stripped) or line.startswith(("    ", "\t"))
        if not stripped or skip:
            if block:
                found.append((start, " ".join(block)))
                block = []
            continue
        if not block:
            start = number
        block.append(stripped)
    if block:
        found.append((start, " ".join(block)))
    return found, meta_texts


def long_sentences(text: str, where: str) -> list[str]:
    found = []
    for sentence in split_sentences(text, english=False):
        count = sentence.count("，")
        if count > MAX_COMMAS:
            _, pieces = mask(text)
            shown = unmask(sentence, pieces)
            shown = shown if len(shown) <= 40 else shown[:40] + "…"
            found.append(f"{where}：{count + 1} 個逗號分句：{shown}")
    return found


def check(path: Path) -> list[str]:
    english = is_english(path)
    limit = max_sentences(path)
    blocks, meta_texts = paragraphs(path)
    found = []
    if not english:
        for text in meta_texts:
            found += long_sentences(text, f"{path}:front matter")
    for line, text in blocks:
        where = f"{path}:{line}"
        count = len(split_sentences(text, english))
        if count > limit:
            found.append(f"{where}：這一段有 {count} 句，超過 {limit} 句")
        if not english:
            found += long_sentences(text, where)
    return found


def main(argv: list[str]) -> int:
    if not argv:
        print(USAGE)
        return 2
    missing = [name for name in argv if not Path(name).is_file()]
    if missing:
        print("找不到檔案：" + "、".join(missing))
        return 2
    found = []
    for name in argv:
        try:
            found += check(Path(name))
        except FrontMatterError as error:
            print(f"{name}：{error}")
            return 2
    for item in found:
        print(item)
    print(f"共 {len(found)} 處，掃描 {len(argv)} 個檔案")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
