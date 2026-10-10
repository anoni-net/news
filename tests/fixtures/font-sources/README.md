# 測試用的標題字型

`build.py` 在測試用的文章目錄旁邊找到 `font-sources/` 時，用這裡的字型代替正式的原始檔，測試不必下載約 40 MB 的檔案。

這幾個檔案是 `build.py` 的 `FONT_SOURCES` 那四個原始檔（思源宋體 Noto Serif CJK，Serif2.003 的 SubsetOTF）的子集，目錄結構相同，只留 `tests/fixtures/` 網站用到的明體字與 ASCII 可見字元。授權是 SIL Open Font License 1.1，全文在 `LICENSE`。

fixture 的標題或小標題加了新字，字型裡沒有的字只會出現建置時的提示，`tests/test_fonts.py` 會因為子集少了那些字而失敗。這時照下面的做法重新產生：先用正式字型建置一次 fixture 網站，收集明體用到的字，再從原始檔切出子集。

```python
import sys, tempfile
from pathlib import Path
sys.path.insert(0, ".")
import build
from fontTools import subset
from fontTools.ttLib import TTFont

dest = build.ROOT / "tests/fixtures/font-sources"
backup = dest.rename(dest.with_name("font-sources.old"))  # 先移開，建置才會用正式的原始檔
with tempfile.TemporaryDirectory() as tmp:
    targets, pages, _ = build.build(build.ROOT / "tests/fixtures/posts", Path(tmp), ["clearnet"])
    out = targets["clearnet"].out
    needed = build.serif_chars([(out / p.file).read_text() for p in pages["clearnet"]])
backup.rename(dest)
for s in build.FONT_SOURCES:
    chars = needed.get((s.script, s.weight), set()) | {chr(c) for c in range(0x21, 0x7f)}
    font = TTFont(build.FONT_CACHE / s.file, recalcTimestamp=False)
    options = subset.Options()
    options.name_IDs, options.notdef_outline, options.hinting, options.desubroutinize = ["*"], True, False, True
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=[ord(c) for c in chars])
    subsetter.subset(font)
    font.save(dest / s.file)
```
