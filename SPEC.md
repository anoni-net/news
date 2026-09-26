# 建置規格

`anoni.net/news` 由本 repo 的 `build.py` 產生，不採用現成的靜態網站產生器。本文件定義第一版要做到的事、網址與內容格式的承諾，以及明確不做的功能。實作與審查都以這份為準，要改規格先改這份。

## 自行開發的理由

新聞導讀的需求是每期一頁、一個列表、一份 RSS。這個範圍用幾百行 Python 就能涵蓋，換來四件現成工具給不了的事：

- 不依賴 JavaScript、不對外請求、clearnet 與 onion 各一份產物，這三條由程式本身保證，不靠設定關掉工具的預設行為
- 網址與輸出格式由本 repo 決定，不會因為上游停止維護而被迫搬家
- 建置程式讀得完，產物裡有什麼說得清楚
- 外觀跟官網首頁同一家族

代價是維護落在社群身上，所以功能範圍刻意收小（見「第一版不做的事」），內容格式也跟 Material for MkDocs 的 blog 相容，保留改用 Zensical 或 mkdocs-ng 的退路。

## 原則

| 原則 | 怎麼驗證 |
|---|---|
| 不依賴 JavaScript | 產物裡沒有任何 `<script>` 元素 |
| 不對外請求 | 產物的 `src`、`<link href>`、CSS 的 `url()` 只能指向站內路徑 |
| clearnet 與 onion 分開產出 | onion 產物裡沒有任何 `https://anoni.net` 開頭的連結 |
| 網址一經公開就不改 | 網址合約，移除或改名會讓 CI 失敗 |

## 目錄結構

```
issues/                  # 每期一個 Markdown，檔名是發刊日
  2026-09-18.md
templates/               # Jinja2 模板
  _layout.html.j2
  issue.html.j2
  index.html.j2
  404.html.j2
  feed.xml.j2
  sitemap.xml.j2
static/                  # 兩份產物共用的檔案
  css/news.css
  favicon.svg
  logo.svg
site.toml                # 兩個輸出目標的差異
build.py
tests/
url_contract.txt         # 網址合約，由 build.py --update-contract 產生
```

產物寫到 `public/clearnet/` 與 `public/onion/`，不進 `main`，由 CI 推到 `build` 分支（見「部署」）。

## 一期的格式

一期是 `issues/` 底下的一個 Markdown 檔，檔名是發刊日 `YYYY-MM-DD.md`。同一天只能有一期。

### front matter

欄位名稱與寫法沿用 Material for MkDocs 的 blog，換工具時不必改寫文章。

```yaml
---
title: 年齡驗證的零知識證明迷思與西班牙封鎖的附帶傷害
description: 本期五則，EFF 談零知識證明用在年齡驗證的限制，OONI 量測西班牙 IP 封鎖波及的網站。
date: 2026-09-18
slug: 2026-09-18
authors:
  - anoni
---
```

| 欄位 | 必填 | 說明 |
|---|---|---|
| `title` | 是 | 這一期的標題，用名詞片語，套貢獻者百科的標題句構 |
| `description` | 是 | 一兩句話，用在列表頁、RSS 與 `<meta name="description">` |
| `date` | 是 | 發刊日，必須跟檔名相同。有更正時寫成 `date: {created: 2026-09-18, updated: 2026-09-20}` |
| `slug` | 是 | 必須跟檔名相同。Material 的 blog 預設從標題產生 slug，寫明才能確保換工具後網址不變 |
| `authors` | 否 | 對應 `authors.yml` 的鍵。第一版只顯示，不產生作者頁 |
| `draft` | 否 | `true` 時不產出，也不進列表與 RSS |

多出來的欄位建置時報錯，避免打錯字的欄位被靜默忽略。

### 內文

每一則新聞是一個 `##` 小標題，小標題必須用 `{#id}` 寫明錨點：

```markdown
## 零知識證明用在年齡驗證的限制 {#zkp-age-verification}

來源：[Zero-Knowledge Proofs Aren't Age Verification Silver Bullets](https://www.eff.org/deeplinks/2026/08/zkps-arent-age-verification-silver-bullets) · EFF · 2026-08-18

摘要段落……

跟正體中文使用者的關係……

延伸閱讀：[威脅模型](https://anoni.net/docs/basics/threat-model/)
```

建置時檢查：

- 每個 `##` 都有 `{#id}`，id 只用小寫英文、數字與連字號，同一期裡不重複。中文標題自動產生的錨點會隨著改字而變，寫明 id 才能讓單則分享的網址長期有效
- 每則的第一段以「來源：」開頭，而且含一條外部連結
- 每則至少有一條連到 `https://anoni.net/docs/` 的連結
- 連到文件站的網址必須存在於文件站的網址合約（`anoni-net/docs` 的 `tools/data/url_contract.txt`），錨點也一樣

站內與文件站的連結一律寫 clearnet 的完整網址，onion 產物由建置程式改寫（見「clearnet 與 onion」）。

## 網址

| 網址 | 內容 |
|---|---|
| `/news/` | 列表頁，新的在前，每頁 20 期 |
| `/news/page/2/` | 第二頁起，超過 20 期才產生 |
| `/news/2026-09-18/` | 一期 |
| `/news/2026-09-18/#zkp-age-verification` | 一期裡的一則 |
| `/news/feed.xml` | RSS 2.0 |
| `/news/sitemap.xml` | sitemap |
| `/news/404.html` | 找不到頁面 |

頁面一律輸出成目錄加 `index.html`，網址結尾是斜線。站內連結從根目錄起算（`/news/...`），不寫網域。

### 網址合約

`build.py --update-contract` 把所有頁面網址與每一期的錨點寫進 `url_contract.txt`。CI 比對產物與合約，新增只印提醒，移除或改名讓建置失敗。判準與文件站的 `tools/check_url_contract.py` 相同：拿走讀者已經收藏或分享出去的網址，才算破壞性變更。

## RSS

- RSS 2.0，放最新 20 期，一期一個 `<item>`
- `<description>` 放該期的 `description`，`<content:encoded>` 放整期的 HTML，讀者在閱讀器裡就能讀完
- `<guid isPermaLink="false">` 用 `anoni-news:2026-09-18`，clearnet 與 onion 兩份 feed 用同一個值
- 日期用 RFC 822 格式，時區固定 `+0800`
- feed 裡的網址必須是完整網址，這是兩份產物一定不同的地方

## clearnet 與 onion

兩份產物用同一批模板，差異只寫在 `site.toml`：

| 項目 | clearnet | onion |
|---|---|---|
| 完整網址的前綴（RSS、sitemap、canonical） | `https://anoni.net` | `http://<onion 位址>` |
| 文件站連結 `https://anoni.net/docs/…` | 原樣 | 改寫成 `http://docs.<onion 位址>/…` |
| 官網連結 `https://anoni.net/…` | 原樣 | 改寫成 `http://<onion 位址>/…` |
| `<link rel="canonical">` | 有 | 無 |
| `<meta http-equiv="onion-location">` | 有 | 無 |
| 流量統計 | 待定（見「待決定的事」） | 無 |

改寫在 Markdown 轉成 HTML 之後，對 `href` 屬性做，不對內文做字串取代，避免改到程式碼區塊或照錄的網址文字。

`onion-location` 標頭另外由 Cloudflare 的 Transform Rules 發送。現有的 `onion-anoni.net` 規則只排除 `/docs`，`/news/…` 會對應到 `http://<onion 位址>/news/…`，正是 onion 產物所在的位置，上線時要實測確認。

## 頁面

- 樣式自己寫，只用系統字型，不載入 Bulma 與 Font Awesome。品牌色沿用官網 `self.css` 的 `--brand-*` 變數
- 支援 `prefers-color-scheme: dark`
- 頁首：anoni.net 標誌連回官網首頁、「新聞導讀」、連到文件站
- 頁尾：RSS、授權（CC-BY 4.0）、onion 位址（clearnet 才顯示）、訂閱電子報
- 一期的頁面在標題下列出該期各則的小標題，當成目次

## 驗證與 CI

`uv run build.py` 產出兩份產物，`uv run build.py --check` 在產出後執行下列檢查，任何一項不過就 exit 1：

1. front matter 的欄位、日期、slug 與檔名
2. 內文的錨點、「來源：」段落、文件站連結
3. 文件站連結對得上文件站的網址合約
4. 產物沒有 `<script>`，也沒有指向站外的資源
5. onion 產物沒有 clearnet 的 anoni.net 連結
6. 本站的網址合約

GitHub Actions 在 PR 上執行 `--check`、`pytest`，並用文件站的 `docs_style_lint.py` 掃 `issues/*.md` 與 `README.md`。

## 部署

1. `main` 有新的 commit 時，CI 建置兩份產物，推到 `build` 分支，目錄是 `clearnet/` 與 `onion/`
2. 伺服器上 clone `build` 分支，nginx 在 clearnet 與 onion 的 server block 各加一條 `location /news/`，分別指向兩個目錄
3. 第一版手動 `git pull` 上線，自動部署等官網首頁的部署方式定案後一起處理

## 相依

- Python 3.12，用 uv 管理
- `jinja2`、`markdown`（Python-Markdown，開 `attr_list`、`tables`、`toc`）、`pyyaml`

選 Python-Markdown 是因為 MkDocs 家族用的就是它，同一份 Markdown 換到 Zensical 或 mkdocs-ng 時的轉換結果最接近。

## 第一版不做的事

以下功能不在第一版，要做之前先修改本文件：

- 站內搜尋。中文要斷詞，而且需要 JavaScript
- 多語系，只出正體中文
- 分類、標籤與作者頁，`categories` 與 `authors` 只存不產頁
- 圖片。有圖就要處理授權、替代文字與體積，第一版全文字
- 社群分享用的預覽卡片圖
- 留言與任何需要伺服器端的功能
- 自動寄送電子報

## 待決定的事

- 發刊頻率：每週或雙週
- clearnet 是否放流量統計，官網首頁與文件站都有 Umami
- 內部篩選過的新聞改寫成對外版本時，由誰改寫、誰審稿
- 第一期的內容：整理 2026 年 6 月到 9 月累積的新聞，或從下一次篩選開始
