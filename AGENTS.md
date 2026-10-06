# AGENTS.md

本文件寫給在 anoni-net/news 工作的 AI 協作工具與使用它們的貢獻者，不限定哪一家的服務。Claude Code 從 `CLAUDE.md` 引入本文件。

## 專案概述

`anoni.net/news` 是匿名網路社群 anoni.net 的新聞導讀，整理國際上隱私、匿名網路與網路審查的新聞，從科技與開源生態的角度介紹可用的專案與技術，一則寫成一篇。選題標準與跟文件站（`anoni-net/docs`，網址 `anoni.net/docs`）的分工寫在 [`README.md`](./README.md)。

目前在籌備階段。網站由本 repo 的 `build.py` 產生，規格在 [`SPEC.md`](./SPEC.md)，要改行為先改規格。

## 寫作指南的索引

寫稿與審稿的規則分成幾份檔案，本檔只放索引、開發指令與共通的步驟。各份不會自動載入，著手前讀對應的那份，只需要其中一節時讀那一節就好。

| 要做的事 | 先讀 |
|---|---|
| 寫導讀 | `guides/posts.md`，用 AI 協作工具時加讀 `guides/ai-workflow.md` |
| 寫每週短訊 | `guides/brief.md` |
| 寫導讀歷史 | `guides/history.md` |
| 用 AI 協作工具查資料、派審稿 | `guides/ai-workflow.md` |
| 寫區域段落 | `notes/` 裡對應主題的筆記，格式見 `notes/README.md` |
| 改網站的行為或格式 | `SPEC.md` |

## 開發指令

```bash
uv sync
uv run build.py                    # 產生 public/clearnet 與 public/onion
uv run build.py --check            # 產生之後執行 SPEC.md「驗證與 CI」的九項檢查
uv run build.py --update-contract  # 新增網址之後，把它們收進 url_contract.txt
uv run build.py --watch            # 列出快到期、還沒有後續稿的追蹤事件，貼進每週候選票
uv run build.py --history          # 導讀歷史：列出 7 天內要上線、現況要重新查證的快照，以及 30 天內還沒寫的日期
uv run tools/front_matter_text.py /tmp/fm  # 把 front matter 的標題、description 與「同一天還有」抽成 Markdown，給 linter 掃
uv run tools/prose_check.py posts/<檔名>.md posts/zh-CN/<檔名>.md posts/en/<檔名>.md  # 送審前自查長句與長段落，見 `guides/history.md`「交稿前」
uv run pytest -q
./tools/make_og.sh                 # 改了 tools/og.html 或標語之後，重新產生三個語系的預覽圖
uv run tools/ingest_images.py --dry-run posts/<檔名>.md  # 維護者：試跑搬圖
uv run tools/fetch_favicons.py --dry-run posts/<檔名>.md  # 維護者：試抓原文網站的圖示
uv run tools/bluesky_post.py --dry-run  # 列出這一輪會發到 Bluesky 的貼文，見 SPEC.md「Bluesky」
uv run tools/make_cards.py --dry-run    # 維護者：產生還沒有或已過期的預覽卡片，見 SPEC.md「預覽卡片」
```

`--check` 會從 GitHub 下載文件站的網址合約，離線時用 `--docs-contract <檔案>` 指定本機的一份。建置時會把 `assets.anoni.net` 的圖片抓進產物，快取在 `.cache/assets/`。版面檢查需要 Chrome，找不到時略過並提示，截圖存在 `.cache/screenshots/`，送出 PR 前要實際看過。

## 寫一篇

1. 在 `posts/` 新增 `YYYY-MM-DD-<slug>.md`，front matter 與內文格式見 `SPEC.md`「一篇的格式」。`posts/zh-CN/` 與 `posts/en/` 放同檔名的另外兩個版本，寫法見 `guides/posts.md`「三個語系」
2. `date` 填預定的發布時間，固定在台北時間午夜 0 點（`YYYY-MM-DDT00:00:00+08:00`），同一天的第二篇排 00:05，三個語系相同，檔名的日期跟著改。最多排到 7 天後，時間到了才上線，見 `SPEC.md`「排程發布」。排不下時取捨題目，不放寬天數，被排掉的稿等進到 7 天內再開 PR。導讀歷史的提早寫稿另有規定，見 `guides/history.md`。要當天馬上上線的，填合併的時間
3. `categories` 填一個分類，例如 `categories: [encryption]`，三個語系相同。可用的分類與各自收什麼見 `SPEC.md`「分類」
4. `uv run build.py --check`，錯誤訊息會列出檔名與行號
5. `uv run build.py --update-contract`，把新文章的網址收進合約，跟文章放在同一個 PR

維護者要把這篇放進首頁的焦點時，三個語系的 front matter 都寫 `pin: YYYY-MM-DD`，填焦點的最後一天，過了就自動離開，規則見 `SPEC.md`「一篇的格式」。

有圖片時，投稿者用 Markdown 的圖片語法標出位置就好，網址可以是任何地方。維護者合併前設好 `NEWS_ASSETS_RSYNC`，執行 `uv run tools/ingest_images.py posts/<檔名>.md` 把圖片搬到 `assets.anoni.net`，再依工具列出的原始網址審核授權與來源，補上替代文字與圖說。規則見 `SPEC.md`「圖片」。

維護者合併前設好 `NEWS_ASSETS_RSYNC`，執行 `uv run tools/make_cards.py` 產生這篇三個語系的社群預覽卡片，工具會上傳卡片並寫進 `og_cards.toml`。導讀歷史的快照也一樣，標題改過就要重新產生。規則見 `SPEC.md`「預覽卡片」。

原文的網站還沒有登記圖示時，建置會列出是哪個主機。維護者先執行 `uv run tools/fetch_favicons.py --dry-run posts/<檔名>.md`，看過 `.cache/favicons/preview.html` 的預覽，再設好 `NEWS_ASSETS_RSYNC` 拿掉 `--dry-run` 執行一次，工具會上傳圖示並寫進 `favicons.toml`。抓不到或不適合的，用 `--from` 指定來源或用 `--none` 登記成通用圖示。規則見 `SPEC.md`「原文的網站圖示」。

## 寫作規則

寫作與協作的規則以[貢獻者百科](https://anoni.net/docs/community/contributor-handbook/)為準，英文版照[英文的貢獻者百科](https://anoni.net/docs/en/community/contributor-handbook/)，要調整規則時改百科，不要在這裡另存一份。檢查工具沿用文件站的 `tools/docs_style_lint.py`。

導讀另有三條界線：

- 只寫摘要與評註，不整篇翻譯。引用原文時照錄原始標題，引述盡量短
- 不把內容跟特定基金會或具名的個人綁在一起，原文提到的人名與組織只在理解新聞必要時保留
- 不描述特定地區、特定族群使用哪些工具。地區、族群與產品名稱同時出現，就足以構成偵查線索
