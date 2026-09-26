# AGENTS.md

本文件寫給在 anoni-net/news 工作的 AI 協作工具與使用它們的貢獻者，不限定哪一家的服務。Claude Code 從 `CLAUDE.md` 引入本文件。

## 專案概述

`anoni.net/news` 是匿名網路社群 anoni.net 的新聞導讀，整理國際上隱私、匿名網路與網路審查的新聞，從科技與開源生態的角度介紹可用的專案與技術，一則寫成一篇。選題標準與跟文件站（`anoni-net/docs`，網址 `anoni.net/docs`）的分工寫在 [`README.md`](./README.md)。

目前在籌備階段。網站由本 repo 的 `build.py` 產生，規格在 [`SPEC.md`](./SPEC.md)，要改行為先改規格。

## 開發指令

```bash
uv sync
uv run build.py                    # 產生 public/clearnet 與 public/onion
uv run build.py --check            # 產生之後執行 SPEC.md「驗證與 CI」的九項檢查
uv run build.py --update-contract  # 新增網址之後，把它們收進 url_contract.txt
uv run pytest -q
./tools/make_og.sh                 # 改了 tools/og.html 之後重新產生 static/og.png
uv run tools/ingest_images.py --dry-run posts/<檔名>.md  # 維護者：試跑搬圖
```

`--check` 會從 GitHub 下載文件站的網址合約，離線時用 `--docs-contract <檔案>` 指定本機的一份。建置時會把 `assets.anoni.net` 的圖片抓進產物，快取在 `.cache/assets/`。版面檢查需要 Chrome，找不到時略過並提示，截圖存在 `.cache/screenshots/`，送出 PR 前要實際看過。

## 寫一篇

1. 在 `posts/` 新增 `YYYY-MM-DD-<slug>.md`，front matter 與內文格式見 `SPEC.md`「一篇的格式」
2. `uv run build.py --check`，錯誤訊息會列出檔名與行號
3. `uv run build.py --update-contract`，把新文章的網址收進合約，跟文章放在同一個 PR

有圖片時，投稿者用 Markdown 的圖片語法標出位置就好，網址可以是任何地方。維護者合併前設好 `NEWS_ASSETS_RSYNC`，執行 `uv run tools/ingest_images.py posts/<檔名>.md` 把圖片搬到 `assets.anoni.net`，再依工具列出的原始網址審核授權與來源，補上替代文字與圖說。規則見 `SPEC.md`「圖片」。

## 導讀的寫法

導讀的文字重量要輕，讀者從社群連結點進來，幾分鐘讀完就知道發生什麼事、跟自己有沒有關係、現在能做什麼。2026-09 上線的第一批（`posts/2026-09-27-*.md`）是範本，寫之前先讀一遍。

### 篇幅

- 全文約 600 到 800 個漢字，摘要與技術觀點大約各半
- 八到十段，每段兩到四句，一段只處理一件事
- 不用條列，全部寫成完整的段落。步驟真的很多時，寫出最關鍵的一兩步，其餘指向原文

### 結構

1. 第一段寫發生什麼事、現在誰用得到。版本號、測試版、只在某個平台或地區才有，這些限制放在第一段，讀者不必讀到最後才發現跟自己無關
2. 接著兩三段寫原文的機制與數字，只寫原文有的內容
3. `## 技術觀點 {#technical-view}` 小標題之後寫三件事：背後的技術原理、讀者現在能做什麼、這項技術的代價或取捨

第一段的寫法跟貢獻者百科「敘事結構」的「前言不堆日期、版本號，先交代為什麼重要」不同。那條是為文件站的長文設計的，新聞導讀用新聞的寫法，先交代發生什麼事與影響範圍。百科的其他規則照常適用。

### 事實與不確定

- 原文自己寫明的限制一定寫進去，例如「只在 Android 版 Chrome 觀察到」、「伺服器端的對應是推論」，導讀不能比原文更肯定
- 沒有查證的事直接寫出來，例如「台灣的 Play 商店能不能完成付款，我們還沒有實測」
- 能從原文推出結論的就直接寫結論，不寫「原文沒有提到」。例如原文寫只支援英文，就寫「Siri 語言設成中文的使用者現在還用不到」，不寫「台灣能不能使用，原文沒有提到」
- 官方來源與報導分開，能找到官方公告就列為第一個 `sources`，名詞照官方的寫法
- 來源的發布日期看頁面上的 `datePublished` 或 `<time>`，不照抄轉述者寫的日期

### 用字

- 組織的說法寫成「Signal 在社群論壇的公告寫明」，不寫「Signal 說」。原文作者寫「研究者」、「作者」，不寫名字
- cookie 名稱、主機名稱這類識別碼用 inline code
- 段落末尾不加總結句或評語，例如「保管就是全部」、「它的價值在於……」，寫完事實就收尾
- 延伸閱讀目前不放，見 `SPEC.md`「內文」

## 寫作規則

寫作與協作的規則以[貢獻者百科](https://anoni.net/docs/community/contributor-handbook/)為準，要調整規則時改百科，不要在這裡另存一份。檢查工具沿用文件站的 `tools/docs_style_lint.py`。

導讀另有三條界線：

- 只寫摘要與評註，不整篇翻譯。引用原文時照錄原始標題，引述盡量短
- 不把內容跟特定基金會或具名的個人綁在一起，原文提到的人名與組織只在理解新聞必要時保留
- 不描述特定地區、特定族群使用哪些工具。地區、族群與產品名稱同時出現，就足以構成偵查線索
