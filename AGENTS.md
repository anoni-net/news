# AGENTS.md

本文件寫給在 anoni-net/news 工作的 AI 協作工具與使用它們的貢獻者，不限定哪一家的服務。Claude Code 從 `CLAUDE.md` 引入本文件。

## 專案概述

`anoni.net/news` 是匿名網路社群 anoni.net 的新聞導讀，介紹讓公民團體、記者與調查記者把工作做得更快、更安全的開源專案與科技工具，一則寫成一篇。選題標準與跟文件站（`anoni-net/docs`，網址 `anoni.net/docs`）的分工寫在 [`README.md`](./README.md)。

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

## 寫作規則

寫作與協作的規則以[貢獻者百科](https://anoni.net/docs/community/contributor-handbook/)為準，要調整規則時改百科，不要在這裡另存一份。檢查工具沿用文件站的 `tools/docs_style_lint.py`。

導讀另有三條界線：

- 只寫摘要與評註，不整篇翻譯。引用原文時照錄原始標題，引述盡量短
- 不把內容跟特定基金會或具名的個人綁在一起，原文提到的人名與組織只在理解新聞必要時保留
- 不描述特定地區、特定族群使用哪些工具。地區、族群與產品名稱同時出現，就足以構成偵查線索
