# 建置規格

`anoni.net/news` 由本 repo 的 `build.py` 產生，不採用現成的靜態網站產生器。本文件定義第一版要做到的事、網址與內容格式的承諾，以及明確不做的功能。實作與審查都以這份為準，要改規格先改這份。

## 自行開發的理由

新聞導讀的需求是一篇一頁、列表與封存頁、一份 RSS。這個範圍用幾百行 Python 就能涵蓋，換來四件現成工具給不了的事：

- 不依賴 JavaScript、不對外請求、clearnet 與 onion 各一份產物，這三條由程式本身保證，不靠設定關掉工具的預設行為
- 網址與輸出格式由本 repo 決定，不會因為上游停止維護而被迫搬家
- 建置程式讀得完，產物裡有什麼說得清楚
- 外觀跟官網首頁同一家族

代價是維護落在社群身上，所以功能範圍刻意收小（見「第一版不做的事」），內容格式也跟 Material for MkDocs 的 blog 相容，保留改用 Zensical 或 mkdocs-ng 的退路。

## 原則

| 原則 | 怎麼驗證 |
|---|---|
| 不依賴 JavaScript | 閱讀與導覽都不需要 JavaScript。產物裡可執行的 `<script>` 只有 clearnet 的流量統計（見「流量統計」），onion 一支都沒有。`type="application/ld+json"` 的結構化資料不會被執行，不算在內 |
| 不對外請求 | 產物的 `src`、`<link href>`、CSS 的 `url()` 只能指向站內路徑。例外同上，clearnet 的流量統計從 anoni.net 底下的子網域載入 |
| clearnet 與 onion 分開產出 | onion 產物裡沒有任何 `https://anoni.net` 開頭的連結 |
| 網址一經公開就不改 | 網址合約，移除或改名會讓 CI 失敗 |

## 目錄結構

```
posts/                   # 一篇一個 Markdown，檔名是發布日加 slug，這一層是 zh-TW
  2026-09-18-zkp-age-verification.md
  zh-CN/                 # 同檔名的簡體中文版
    2026-09-18-zkp-age-verification.md
  en/                    # 同檔名的英文版
    2026-09-18-zkp-age-verification.md
pages/                   # 文章以外的固定頁面：關於頁與訂閱頁，語系目錄的排法同 posts/
  about.md
  subscribe.md
  zh-CN/about.md、zh-CN/subscribe.md
  en/about.md、en/subscribe.md
strings.toml             # 介面文字，三個語系各一組
templates/               # Jinja2 模板
  _layout.html.j2
  post.html.j2
  page.html.j2           # 關於頁這類固定頁面
  list.html.j2           # 列表頁與年、月封存頁共用
  404.html.j2
  feed.xml.j2
  sitemap.xml.j2
  robots.txt.j2          # 只輸出到 onion，clearnet 的 robots.txt 在官網 repo
static/                  # 兩份產物共用的檔案
  css/news.css
  favicon.svg            # 文件站的 logo-tonal.svg
  logo-wordmark-white.svg  # 文件站的 mono white wordmark，放在頁首
  og.png                 # 全站共用的社群分享預覽圖，1200×630，zh-TW
  og-zh-cn.png           # zh-CN 的預覽圖
  og-en.png              # en 的預覽圖
tools/
  og.html                # 三張預覽圖的原始檔，用 ?lang= 切換語系
  make_og.sh             # 用 Chrome 從 og.html 產生三張預覽圖
  ingest_images.py       # 維護者合併前把稿件裡的圖片搬到 assets.anoni.net
authors.yml              # 署名清單，front matter 的 authors 對應這裡的鍵
site.toml                # 兩個輸出目標的差異
build.py
layout_check.py          # 驗證第 8 項，用 headless Chrome 量版面
tests/
  test_build.py
  fixtures/              # 測試用的文章與署名，--check 的版面檢查也用這一批
url_contract.txt         # 網址合約，由 build.py --update-contract 產生
```

產物寫到 `public/clearnet/` 與 `public/onion/`，不進 `main`，由 CI 推到 `build` 分支（見「部署」）。

## 一篇的格式

一則新聞寫成一篇，是 `posts/` 底下的一個 Markdown 檔。檔名是 `YYYY-MM-DD-<slug>.md`，日期與 slug 都要跟 front matter 相同。檔名帶日期只是為了讓目錄依時間排序，網址由 front matter 決定。

### front matter

欄位名稱與寫法沿用 Material for MkDocs 的 blog，換工具時不必改寫文章。`sources` 是本站自己加的欄位，Material 與 Zensical 會忽略不認得的欄位，不影響相容。

```yaml
---
title: 零知識證明用在年齡驗證的限制
description: EFF 指出零知識證明用在年齡驗證時，仍會留下單點失效與 metadata 軌跡。
date: 2026-09-18
slug: zkp-age-verification
sources:
  - title: "Zero-Knowledge Proofs Aren't Age Verification Silver Bullets"
    url: https://www.eff.org/deeplinks/2026/08/zkps-arent-age-verification-silver-bullets
    publisher: EFF
    date: 2026-08-18
authors:
  - anoni-net
---
```

| 欄位 | 必填 | 說明 |
|---|---|---|
| `title` | 是 | 用名詞片語，套貢獻者百科的標題句構。照錄原文標題時不在此限 |
| `description` | 是 | 一兩句話，用在列表頁、RSS 與 `<meta name="description">` |
| `date` | 是 | 發布的時間，決定網址裡的年月，發布之後不能改。晚於現在（台北時間）就是排程中，見「排程發布」。可以帶時間，例如 `2026-09-28T07:00:00+08:00`，同一天發布多篇時由時間決定排序，頁面上只顯示日期。有更正時寫成 `date: {created: 2026-09-18, updated: 2026-09-20}`，`updated` 是實際改稿的時間，不能晚於現在 |
| `slug` | 是 | 小寫英文、數字與連字號，3 到 60 個字元，同一個年月內不重複。Material 的 blog 預設從標題產生 slug，寫明才能確保換工具後網址不變 |
| `sources` | 是 | 原文，至少一筆。每筆的 `title` 與 `url` 必填，`publisher` 與 `date` 選填。一篇可以列多筆，用在同一事件的多篇報導，也用在把好幾篇原文整理成一篇觀點 |
| `authors` | 是 | 對應 `authors.yml` 的鍵，見「發佈身分」。不想署名就寫 `anoni-net` |
| `categories` | 否 | 第一版只存不產頁 |
| `image` | 否 | 這篇在社群平台分享時的預覽圖，網址規則同內文圖片（見「圖片」），建議 1200×630。沒填就用全站共用的 `og.png` |
| `draft` | 否 | `true` 時不產出，也不進列表、封存頁與 RSS |
| `pin` | 否 | `true` 時放在首頁最上方的「焦點」。同一時間只能有一篇，換焦點時先拿掉舊的那篇，否則建置失敗。欄位名稱沿用 Material blog 的置頂 |
| `follows` | 否 | 這篇接續的舊文章，寫檔名、不含 `.md`，例如 `2026-09-18-zkp-age-verification`。用清單，一篇可以接續兩件事。見「前情與後續」 |
| `watch` | 否 | 之後要回頭查的事，只寫在 zh-TW 版本。每一筆有 `date`（回頭查的日期）與 `note`（要查什麼）。見「追蹤中的事件」 |

多出來的欄位建置時報錯，避免打錯字的欄位被靜默忽略。

### 內文

原文由模板依 `sources` 產生（見「版面」的原文區塊），內文不再重寫一次。內文依序寫摘要、導讀觀點。摘要的第一段寫出誰受影響，新聞發生在特定國家或只影響特定平台時，也寫明其他地方、其他平台的讀者受不受影響。導讀觀點從科技與開源的角度評註這則新聞，有相關的專案或技術時，交代它能解決什麼問題，以及授權、維護狀態、使用門檻、有沒有正體中文介面，讀者看完就能判斷要不要試。導讀觀點的最後一段寫讀者現在能做的第一步，連同要付出的門檻。2026-09 用模擬讀者檢視第一批稿件時，不寫程式的讀者多半讀完仍不知道自己該做什麼，才加上這兩條。導讀觀點用 `## 導讀觀點 {#perspective}` 當小標題，篇幅與語氣見 `AGENTS.md`「導讀的寫法」。小標題原本叫「技術觀點」，2026-09 第一批上線後改名。「技術」兩字會讓不寫程式的讀者以為內容是寫給工程師看的，實際寫的卻是讀者現在能做什麼：

```markdown
摘要段落……

## 導讀觀點 {#perspective}

導讀觀點……
```

連到文件站的延伸閱讀目前不放。2026-09 第一批上線時決定維持導讀的輕量，等文章累積到一定數量再評估。建置程式對文件站連結的檢查保留著，之後恢復時不必改程式。

建置時檢查：

- 內文如果有小標題，一律用 `{#id}` 寫明錨點，id 只用小寫英文、數字與連字號，同一篇裡不重複。中文標題自動產生的錨點會隨著改字而變，寫明 id 才能讓分享出去的段落連結長期有效
- 有連到文件站時，網址必須存在於文件站的網址合約（`anoni-net/docs` 的 `tools/data/url_contract.txt`），錨點也一樣。文件站改了網址，這裡會先發現

站內與文件站的連結一律寫 clearnet 的完整網址，onion 產物由建置程式改寫（見「clearnet 與 onion」）。

## 前情與後續 {#follow-ups}

隱私與審查的新聞常拖上好幾個月，一條法案從提案、修正到表決，每一段都可能寫成一篇導讀。讀者通常只從其中一篇進來，從搜尋或舊的社群連結點進舊文章時，要能馬上知道事情已經有新的進展。

寫新文章時在 front matter 用 `follows` 指出接續的舊文章，舊文章不用改。建置時把用 `follows` 相連的文章串成一條事件線，依發布時間由舊到新排，同一條線上的每一篇都會在頁面上出現兩個東西：

- 標題區的最後一行提示最新的一篇（「後續發展：〈標題〉（日期）」），只在這篇不是最新的一篇時出現。已發布的文章因此多了後續的連結，但內容沒有更動，不算更正，`date.updated` 不動
- 內文與原文清單之後、訂閱行之前，列出整條事件線（「同一事件的導讀」），目前這一篇標上「本篇」、不加連結

後續的文章還在排程中時，舊文章不會出現它的標題與網址，到了發布時間重建才連上，跟排程中的文章不進列表與 RSS 的道理相同。

事件線放在 `<article>` 外面，標上 `role="navigation"`，閱讀模式與朗讀抽正文時不會念進去。標題區那行提示留在正文裡，用聽的讀者一樣需要知道有後續。RSS 只放正文，不列事件線，前情由新文章的第一段交代。

`follows` 只用在同一件事的新進展，例如同一條法案、同一個產品變更、同一起事件。主題相近但事件不同的文章不串在一起。

建置時檢查：

- `follows` 的每一項是一篇存在的文章的檔名，草稿不能被接續
- 被接續的文章要比新文章早發布，接續自己與循環也因此會被擋下。兩篇都在排程中也可以
- 三個語系的 `follows` 相同

## 追蹤中的事件 {#watch}

寫稿時常會遇到之後才有結果的事，例如 12 月才釋出的原始碼、年底前要上線的 App、還在測試版的功能。在 front matter 用 `watch` 記下回頭查的日期與要查什麼，之後選題時掃這一類就好，不必靠人記得：

```yaml
watch:
  - date: 2026-12-10
    note: Android 17 QPR2 是否把 QPR1 的 API 與修補釋出到 AOSP
```

- 只寫在 zh-TW 版本，這是編輯用的筆記，不翻譯。zh-CN 與 en 寫了會報錯
- 不出現在頁面、RSS 與 sitemap。對讀者寫「會持續追蹤」等於一個承諾，事件停擺時反而難交代。repo 是公開的，`note` 只寫要查什麼
- `date` 要晚於發布日。日期依原文寫的時間推估，原文沒有寫時間的，抓一個月後再看一次
- 後續稿用 `follows` 接上之後，舊文章的 `watch` 全部視為完成，不必回頭改。後續稿還在排程中也算
- 事件沒有新進展、不打算再寫時，刪掉那一筆。只動 front matter、內容沒變，不算更正，`date.updated` 不動

`uv run build.py --watch` 列出回頭查的日期在 7 天內或已經過了、還沒有後續稿的項目，每筆一行 checkbox，可以直接貼進每週候選票的「追蹤中的事件」。7 天跟排程的上限相同，列出來的題目趕得上排進下一批稿。過期只提醒，不讓 `--check` 失敗。

## 多語系

每篇導讀都有正體中文（zh-TW）、簡體中文（zh-CN）與英文（en）三個版本，同時發布。zh-TW 是第一版，選題與事實查核在這一版完成，另外兩個版本以它為準。三個版本的事實相同，導讀觀點依各自的讀者重寫，寫法見 `AGENTS.md`「三個語系」。

| 語系 | 檔案 | 網址 | `<html lang>` | hreflang |
|---|---|---|---|---|
| zh-TW | `posts/<檔名>.md` | `/news/…` | `zh-Hant` | `zh-Hant`，另標 `x-default` |
| zh-CN | `posts/zh-CN/<檔名>.md` | `/news/zh-cn/…` | `zh-Hans` | `zh-Hans` |
| en | `posts/en/<檔名>.md` | `/news/en/…` | `en` | `en` |

目錄與網址的大小寫跟文件站相同，目錄是 `zh-CN`，網址是小寫的 `zh-cn`。文件站的 `docs_style_lint.py` 依路徑裡的 `/zh-CN/` 與 `/en/` 選規則集，目錄寫成小寫的話，簡體版會被套上兩岸用詞的規則，英文版會被套上中文標點的規則。

### 三個版本的對應

同檔名的三個檔案就是同一篇。建置時檢查：

- 每一篇 zh-TW 都要有 zh-CN 與 en，缺一個就建置失敗。三個版本在同一個 PR 送出，同時上線
- `date.created`、`slug`、`authors`、`pin`、`draft`、`image` 與 `categories` 三個版本相同。`date.updated` 可以不同，只改了其中一個版本時只更新那一個
- `sources` 要包含 zh-TW 的每一筆網址，可以再加。導讀觀點為了比較各地狀況而查證的資料，來源加在該版本的 `sources`。原文標題照錄，三個版本都不翻譯
- 內文的錨點集合三個版本相同，`{#perspective}` 這類分享出去的段落連結換了語系照樣有效
- 圖片共用同一個網址，替代文字與圖說各版本用自己的語言寫

### 介面

- 介面文字寫在 `strings.toml`，三個語系的鍵必須一致，少一個就建置失敗。出處行、日期格式、頁尾、404 與 `<title>` 的站名都從這裡取
- 日期格式：zh-TW 與 zh-CN 維持現在的「2026 年 9 月 27 日 星期日」，en 寫成「Sunday, 27 September 2026」
- 站名：zh-TW「anoni.net 新聞導讀」、zh-CN「anoni.net 新闻导读」、en「anoni.net News」
- 其他語系的連結只列目前語系以外的兩個，例如 zh-TW 頁寫「其他語言：简体中文、English」。每一頁放在頁尾，文章頁另外放在署名的下一行，連到另外兩個版本的同一篇。列表頁與封存頁連到另外兩個語系的同一種頁面。頁首不放，避免跟「新聞導讀」擠在同一列。這一行用 `<nav role="navigation">`，閱讀模式與朗讀才不會把它當成正文（見「閱讀模式與朗讀」）
- 小標題的明體與內文的黑體依 `:lang()` 各給一組字型。zh-CN 先找簡體字型（思源宋體 SC、宋体、PingFang SC、微软雅黑），避免用正體字型的字形顯示簡體字
- 訂閱電子報的表單依語系不同，zh-TW 與 zh-CN 用中文的表單，en 用英文的表單，網址寫在 `strings.toml` 的 `newsletter_url`
- 標語改了之後，`tools/og.html` 裡的文字要一起改，再用 `tools/make_og.sh` 重新產生三張預覽圖
- 授權連結指向 CC-BY 4.0 各自語言的頁面
- 404 只有一頁，三種語言各寫一段，連到三個首頁。伺服器依路徑回同一個 `/news/404.html`，不必依語系分流

### 產物

- 每個語系有自己的列表頁、分頁、年月封存頁與 RSS（`/news/feed.xml`、`/news/zh-cn/feed.xml`、`/news/en/feed.xml`）
- sitemap 只有一份，每一篇用 `xhtml:link` 列出三個版本
- 文章頁的 `<head>` 用 `<link rel="alternate" hreflang>` 列出三個版本與 `x-default`，JSON-LD 加上 `inLanguage`
- 社群預覽圖各語系一張，文章指定 `image` 時三個版本共用

## 圖片

圖片放在社群的圖片主機 `assets.anoni.net` 的 `/news/` 底下，跟文件站 blog 用同一台主機。上傳與審核由維護者負責，投稿者只需要標出圖片的位置。

### 上稿流程

1. 投稿者在稿件裡用 Markdown 的圖片語法標出位置，網址可以是任何地方，例如原文網站上的圖，或自己放在圖床的截圖。替代文字與圖說可以先寫草稿
2. 維護者合併前執行 `uv run tools/ingest_images.py posts/<檔名>.md`。工具把每一張不在 `assets.anoni.net` 的圖下載下來，清掉 metadata、轉成 WebP、長邊縮到 1600px 以內，上傳到圖片主機，再把文章裡的網址換成 `https://assets.anoni.net/news/YYYY/MM/<slug>/figure-N.webp`。最後列出每張圖的原始網址，供維護者審核
3. 維護者審核每張圖的授權與來源，補上替代文字與圖說。圖說寫在圖片語法的 title 欄位，寫出處與授權：`![替代文字](網址 "圖：EFF，CC-BY 4.0")`
4. 合併

別人新聞裡的照片與圖表，著作權屬於原作者。能放的是社群自己做的圖、自己截的畫面，或授權明確允許轉載的圖，審核時照這個標準判斷。截圖裡出現的帳號、人臉與個人資料，用文件站的[截圖遮蔽工具](https://anoni.net/docs/utils/redact/)處理過再上傳。

上傳的目的地由環境變數 `NEWS_ASSETS_RSYNC` 指定（rsync 的目標路徑），不寫在 repo 裡。上傳後工具會用 HTTP 確認每張圖在 `assets.anoni.net` 上回 200，才改寫文章。

### 建置時的處理

- 內文與 `image` 只接受 `https://assets.anoni.net/news/` 開頭的圖片，其他網址讓建置失敗，並提示執行搬圖工具。投稿的 PR 在圖片搬好之前會是紅燈，代表還有圖片待處理
- 建置時把圖片抓進產物的 `assets/` 底下，頁面引用站內的副本，讀者不會連到 `assets.anoni.net`，onion 產物也不必改寫。做法跟文件站的 privacy 外掛相同。抓下來的檔案快取在 `.cache/assets/`
- deploy workflow 用 `actions/cache` 保留 `.cache/assets/`，m6 暫時連不上時，已經抓過的檔案照樣建置得出來，每小時的排程發布不會因此停擺。檔名不會重複使用，內文圖片依序編號、網站圖示帶內容雜湊，快取不必過期。PR 的 check 不用快取，每次從 `assets.anoni.net` 重新抓，確認檔案真的在圖片主機上
- 抓下來的檔案再檢查一次：只收 WebP、PNG、JPEG，不能有 EXIF、XMP 或 PNG 文字區塊這類 metadata，單張不超過 300KB，長邊不超過 2000px。圖片主機上的檔案被換掉，這一步也擋得住
- 圖片要獨立成一段，替代文字與圖說都必填。圖說轉成 `<figure>` 與 `<figcaption>`
- 自動補上 `width`、`height`、`loading="lazy"` 與 `decoding="async"`，載入時版面不會跳動
- RSS 裡的圖片用完整網址，指向產物裡的副本
- 不收 SVG，SVG 裡可以夾帶程式碼與對外請求

### 原文的網站圖示

原文區塊的每一筆標題前面放來源網站的圖示（favicon），讀者掃過就知道這篇整理了哪幾家的報導。圖示跟內文圖片放在同一台主機，由維護者抓取、審核、上傳，建置時抓進產物，讀者不會連到來源網站。

登記表是 repo 根目錄的 `favicons.toml`，鍵是 `sources` 網址的主機名稱，去掉開頭的 `www.`。每個主機寫成下面三種之一：

| 欄位 | 說明 |
|---|---|
| `icon` | 圖示的檔名，放在 `https://assets.anoni.net/news/favicons/`。檔名帶內容雜湊，例如 `eff.org-1a2b3c4d.png`，換圖示就換檔名，不必處理快取。同一筆的 `from` 記抓取的原始網址，供審核 |
| `same_as` | 沿用另一個主機的圖示，例如 `support.signal.org` 沿用 `signal.org`。指向的主機要直接寫 `icon` 或 `none` |
| `none` | 不放網站的圖示，改用通用的地球圖示。值寫理由，例如網站沒有提供、抓取被擋、圖示不適合放 |

- `sources` 的主機不在登記表時建置失敗，投稿的 PR 在圖示登記好之前是紅燈，跟圖片相同
- 圖示一律是 64×64 的 PNG，不超過 8KB，不能帶 metadata。頁面上以 16px 顯示，高解析度螢幕照樣清楚
- 圖示底下墊一塊白色的圓角底，透明底的深色圖示在深色模式也看得見
- `alt` 留空，網站名稱已經寫在旁邊的標題或出處欄。圖示放在連結裡面，點圖示同樣連到原文
- 放在文章頁的原文區塊與署名旁的出處行。出處行不在句子裡插圖示，改成行首並排的一串圖示，對應出處行列出的網站，最多三個，都沒填 `publisher` 時維持文件圖示
- RSS 不放，不少閱讀器會忽略 `width` 與 `height`，64px 的原圖會整個撐開。時間軸與焦點的出處行維持文字，一頁 20 則的畫面保持讓讀者靠標題掃過去
- 圖示是各網站的商標，只用來標示連結的出處。對方要求移除時改成 `none`

上稿流程：

1. 維護者執行 `uv run tools/fetch_favicons.py --dry-run posts/<檔名>.md`。工具列出還沒登記的主機，下載並轉好圖示，另外產生一頁預覽 `.cache/favicons/preview.html`，把每個圖示放在淺色與深色背景上
2. 看過預覽，設好 `NEWS_ASSETS_RSYNC` 之後拿掉 `--dry-run` 再執行一次。工具把圖示上傳到 `favicons/`，確認每個網址回 200 之後才寫進 `favicons.toml`
3. 抓不到或抓到的圖不適合時，用 `--from <主機>=<網址或檔案>` 指定來源，或用 `--none <主機>=<理由>` 登記成通用圖示

工具依序試網站首頁 `<link>` 宣告的 apple-touch-icon、標了尺寸的 PNG 或 ICO 圖示，最後才試 `/favicon.ico`，取最大的一張縮成 64×64，非正方形的補透明邊。SVG 不收，理由同內文圖片。原站擋下自動抓取時（例如 Cloudflare 回 403），改從 Internet Archive 取同一個網站最近的存檔，用的仍是原站自己的圖示，`from` 記存檔的網址。三段以上的主機還是抓不到時改抓上一層，例如 `support.signal.org` 改抓 `signal.org`，成功的話登記成 `same_as`。已經登記的主機要重新抓取時用 `--refetch <主機>`。

## 發佈身分

news 開放多人發布，署名可以是本名、固定的筆名，或不具名。身分會從兩個地方洩漏：網站上顯示的署名，以及公開 repo 留下的 git 紀錄與 PR。只處理前者，匿名就只是表面上的。

### 署名

`authors.yml` 列出所有署名，每篇的 `authors` 對應其中的鍵：

```yaml
anoni-net:
  name: anoni.net 社群
  names:
    zh-CN: anoni.net 社区
    en: anoni.net community
night-owl:
  name: 夜梟
  description: 關注網路封鎖的量測
```

| 欄位 | 必填 | 說明 |
|---|---|---|
| `name` | 是 | 顯示在文章頁、列表頁與 RSS 的名稱 |
| `names` | 否 | 其他語系的寫法，鍵是 `zh-CN` 或 `en`，沒寫的語系沿用 `name`。筆名與人名通常不翻 |
| `description` | 否 | 一句話介紹 |
| `url` | 否 | 個人網站或公開帳號，只有願意公開身分的人才填 |

不收頭像，頭像是圖片，也是跨站比對身分的線索。

三種署名的差別在於文章彼此串不串得起來：

| 署名 | 例 | 同一人的文章串得起來嗎 | 適合 |
|---|---|---|---|
| 社群 | `anoni-net`，顯示「anoni.net 社群」 | 串不起來，所有不署名的文章共用同一個署名 | 預設。不想留下任何個人痕跡 |
| 筆名 | 自選的名字，固定使用 | 串得起來 | 想累積寫作紀錄，又不想公開本名 |
| 具名 | 本名或公開帳號，可以附連結 | 串得起來 | 願意公開身分 |

建議要匿名的人用社群署名。筆名會把同一個人寫的文章集中起來，寫得越多，從題目、時間與文風推回本人越容易。

### 建置程式的保證

- 頁面、RSS 與 sitemap 只讀 front matter，不讀 git 紀錄。不顯示「最後編輯者」，日期也不從 commit 時間推算
- RSS 用 `<dc:creator>` 放署名的 `name`，不放 email
- 第一版不產生作者頁，避免把同一個筆名的文章自動集中成一頁

### 發布管道

| 管道 | repo 留下的痕跡 | 適合 |
|---|---|---|
| 自己開 PR | 開 PR 的 GitHub 帳號、commit 的作者、email 與時區、PR 裡的討論 | 具名，或已經有一個跟本人無關的 GitHub 帳號 |
| 維護者代發 | 只有維護者的身分，投稿者不出現在任何紀錄裡 | 不想在 repo 留下任何痕跡 |

自己開 PR 又不想暴露身分時，GitHub 帳號與本人的其他帳號不要有任何關聯，email 用 GitHub 提供的 noreply 位址，commit 時用 `TZ=UTC git commit` 把時區換掉，否則每個 commit 都帶著 `+0800`。

維護者代發時，稿件透過 Matrix 私訊、寄到 `whisper@anoni.net`（建議 PGP 加密），或照文件站的[上傳機敏資訊流程](https://anoni.net/docs/community/upload-sensitive/)傳遞。維護者以自己的身分 commit，commit 訊息與 PR 內文都不提投稿者，也不加 `Co-authored-by`。

兩種管道都遮不掉文風。寫作習慣、用詞與關注的題目本身就能辨識身分，需要高度匿名的人要把這一點算進去。

### 發布權限

能合併 PR 的人就能發布。`main` 設分支保護，每個 PR 至少要有一位作者以外的維護者核可才能合併，跟貢獻者百科「請求至少一位非作者 review」的規則一致。審稿者的身分不顯示在網站上。

## 網址

clearnet 掛在 `anoni.net` 的路徑 `/news/` 底下，onion 則照文件站的做法切成獨立的子網域 `news.<onion 位址>`，網站放在子網域的根目錄。下表列的是 clearnet 的網址，onion 那一側去掉 `/news` 前綴，例如 `/news/2026/09/zkp-age-verification/` 對應到 `http://news.<onion 位址>/2026/09/zkp-age-verification/`。

| 網址 | 內容 |
|---|---|
| `/news/` | 列表頁，新的在前，每頁 20 篇 |
| `/news/page/2/` | 第二頁起，超過 20 篇才產生 |
| `/news/2026/` | 年封存頁，列出該年全部文章 |
| `/news/2026/09/` | 月封存頁，列出該月全部文章 |
| `/news/2026/09/zkp-age-verification/` | 一篇 |
| `/news/feed.xml` | RSS 2.0 |
| `/news/sitemap.xml` | sitemap |
| `/news/about/` | 關於頁，見「關於頁」 |
| `/news/subscribe/` | 用 RSS 訂閱的三個步驟，見「RSS」 |
| `/news/404.html` | 找不到頁面，三個語系共用 |
| `/news/zh-cn/…`、`/news/en/…` | zh-CN 與 en，底下的結構與上面各列相同 |

語系代碼 `zh-cn` 與 `en` 保留給語系用，不會跟年份撞在一起。

年齡驗證、VPN 禁令、年度報告這類題目每隔一段時間就會再寫一次，文章網址帶年月之後，slug 只需要在同一個月內不重複。新聞寫的是某個時間點的事，讀者從網址也看得出新舊。年月取第一次發布的日期，之後更正也不變。

網址裡有年月，讀者就可能把網址往上刪一層，所以年與月各有一種封存頁，不會落在 404。封存頁不分頁。

Material 的 blog 設定 `post_url_format: "{date}/{slug}"` 加 `post_url_date_format: yyyy/MM` 可以產出相同的文章網址，跟文件站 blog 的格式一致。封存頁的網址格式不同，換工具時要另外設定或補轉址。

頁面一律輸出成目錄加 `index.html`，網址結尾是斜線。站內連結從根目錄起算、不寫網域，前綴依輸出目標而不同，clearnet 是 `/news/`，onion 是 `/`，由建置程式依 `site.toml` 產生，模板裡不寫死。

### 路徑與子網域

clearnet 用路徑，跟文件站的 `anoni.net/docs` 同一個模式，官網首頁的產品卡片也照這個寫法列出。onion 用子網域，讓每個服務在 onion 那一側各自獨立，跟 `docs.<onion 位址>` 一致。

用路徑的代價是 news 跟官網首頁、文件站共用同一個 origin，瀏覽器的 localStorage 與 IndexedDB 彼此讀得到。文件站有幾支工具把資料存在瀏覽器裡，news 不放任何 JavaScript，同源也讀不到那些資料。日後 news 要加入 JavaScript 時，先重新評估這一點，必要時改成子網域。

### 網址合約

`build.py --update-contract` 把所有頁面網址與每一篇的錨點寫進 `url_contract.txt`。CI 比對產物與合約，新增只印提醒，移除或改名讓建置失敗。判準與文件站的 `tools/check_url_contract.py` 相同：拿走讀者已經收藏或分享出去的網址，才算破壞性變更。

合約只記 clearnet 的路徑。onion 的網址由「去掉 `/news` 前綴、接上 `news.<onion 位址>`」這條固定的對應推得，不另外記一份。

## RSS

- RSS 2.0，放最新 20 篇，一篇一個 `<item>`
- `<description>` 放該篇的 `description`，`<content:encoded>` 放整篇的 HTML，連同來源清單，讀者在閱讀器裡就能讀完
- 三個語系各一份 feed，只放該語系的文章
- `<guid isPermaLink="false">` 用 `anoni-news:2026/09/zkp-age-verification`，clearnet 與 onion 兩份 feed 用同一個值。zh-CN 與 en 在前面加上語系，寫成 `anoni-news:zh-cn/2026/09/zkp-age-verification`
- 日期用 RFC 822 格式，時區固定 `+0800`
- feed 裡的網址必須是完整網址，這是兩份產物一定不同的地方
- 頁面上的 RSS 連結（頁尾、刊頭、文章末的訂閱行、還沒有文章時的提示）指向同語系的訂閱頁 `subscribe/`。直接連到 `feed.xml` 的話，沒用過 RSS 的讀者點下去只會看到一整頁 XML
- 訂閱頁只寫完成訂閱需要的三個步驟：安裝閱讀器、複製 feed 網址、在閱讀器裡新增訂閱。閱讀器照文件站[RSS 訂閱入門](https://anoni.net/docs/tools/rss/)查證過的清單，隱私取捨、經由 Tor 讀取與團隊聊天工具只留一個連到那一頁的連結。2026-09 之前 RSS 連結直接指向文件站的 RSS 訂閱入門。該頁涵蓋文件站、更新日誌與新聞導讀所有的 feed，只想訂閱新聞導讀的讀者要讀完整頁，才能找到自己要的網址
- 訂閱頁的內文寫 `%FEED_URL%`，建置時代入該語系 feed 的完整網址，clearnet 與 onion 各自換成自己的網址
- `<head>` 的 `<link rel="alternate" type="application/rss+xml">` 維持指向 feed，已經在用閱讀器的讀者貼上 news 首頁的網址，閱讀器就會自己找到 feed

## clearnet 與 onion

兩份產物用同一批模板，差異只寫在 `site.toml`：

| 項目 | clearnet | onion |
|---|---|---|
| 網站位置 | `https://anoni.net/news/` | `http://news.<onion 位址>/` |
| 站內連結的前綴 | `/news/` | `/` |
| 本站連結 `https://anoni.net/news/…` | 原樣 | 改寫成 `http://news.<onion 位址>/…` |
| 文件站連結 `https://anoni.net/docs/…` | 原樣 | 改寫成 `http://docs.<onion 位址>/…` |
| 電子報表單 `https://form.anoni.net/…` | 原樣 | 改寫成 `http://form.<onion 位址>/…` |
| 官網連結 `https://anoni.net/…` | 原樣 | 改寫成 `http://<onion 位址>/…` |
| `<link rel="canonical">` | 指向 clearnet 的網址 | 指向 onion 的網址 |
| `robots.txt` | 由官網 repo 產生，列出 `/news/sitemap.xml` | 本站產生，列出 onion 版的 sitemap |
| `<meta http-equiv="onion-location">` | 有 | 無 |
| 流量統計 | 待定（見「待決定的事」） | 無 |

改寫在 Markdown 轉成 HTML 之後，對 `href` 屬性做，不對內文做字串取代，避免改到程式碼區塊或照錄的網址文字。改寫規則寫在 `site.toml` 的 `rewrites`，由上往下比對，第一條比對到的就套用，所以 `/news/`、`/docs/` 與 `form.` 排在官網那條前面。

`onion-location` 標頭另外由 Cloudflare 的 Transform Rules 發送，上線前要改兩條規則：

- 現有的 `onion-anoni.net` 規則目前只排除 `/docs` 與 `/docs/*`，要再排除 `/news` 與 `/news/*`，否則 `/news/…` 會指到官網 onion 根目錄底下不存在的 `/news/…`
- 新增一條 `onion-news` 規則，比照 `onion-docs.anoni.net`，砍掉 `/news` 前綴之後接上 `news.<onion 位址>`

上線後用 `curl -I` 確認標頭指向的網址在 onion 那一側回 200。

## 流量統計

clearnet 以自架的 Umami（`aa.anoni.net`）計算閱讀量，用來判斷哪些題目有人讀、讀者從哪個社群平台進來。onion 不載入，理由跟文件站相同，onion 讀者的請求不能送到 clearnet 的端點。 <!-- docs-style-lint: disable-line -->

- 設定寫在 `site.toml` 的 `[targets.clearnet.analytics]`，網站是 Umami 上的 `anoni-net-news`，跟文件站分開，兩邊的報告不會混在一起
- `data-domains` 限定 `anoni.net`，本機預覽與 CI 的版面檢查不會送出資料
- 送出前經過 `templates/_analytics.html.j2` 的過濾。只送頁面瀏覽，不送自訂事件與效能資料。網址只留 `utm_source`、`utm_medium`、`utm_campaign`、`utm_content`，其餘 query 與 `#` 之後的片段拿掉。螢幕尺寸捨去到百位。瀏覽器開啟「請勿追蹤」或 Global Privacy Control 時整筆不送
- 頁尾寫明本站用 Umami 計算閱讀量、不使用 cookie、onion 版本不載入

`build.py --check` 對 script 的檢查只放行兩支：帶 `data-anoni="before-send"` 的內嵌過濾，以及來源、網站 ID、`data-domains` 與 `data-before-send` 都跟 `site.toml` 相符的 Umami。onion 產物照舊不能有任何可執行的 script，也不能出現 `aa.anoni.net`。 <!-- docs-style-lint: disable-line -->

## 頁面

- 樣式自己寫，只用系統字型，不載入 Bulma 與 Font Awesome。配色見下方「品牌與配色」
- 支援 `prefers-color-scheme: dark`
- 頁首：anoni.net 標誌加「新聞導讀」，兩者是同一個連結，回到該語系的 news 首頁。讀者在 news 裡點左上角，預期回到正在看的網站首頁，官網首頁的入口放在頁尾。頁首、刊頭與頁尾這些頁面框架不放文件站的入口，避免讀者分不清兩個產品，文件站只出現在文章內文與訂閱頁（延伸閱讀目前不放，見「內文」）
- 頁尾：RSS、訂閱電子報、關於頁、回報錯誤、官網首頁、onion 位址（clearnet 才顯示）、授權（CC-BY 4.0）。回報錯誤連到 GitHub 的 issue 表單，三個語系相同

### 閱讀模式與朗讀

想用聽的讀者，靠瀏覽器與作業系統內建的功能，例如 Safari 的閱讀器、Chrome 與 Edge 的朗讀、螢幕閱讀器。news 不自己放朗讀按鈕，那需要 JavaScript，而 Chrome 桌機版預設的中文語音是線上語音，全文會送到 Google 的伺服器。

這些功能多半先把正文抽出來再念，文章頁的標記要讓它們抽得乾淨：

- 正文從日期、副標、出處行與署名開始，接著是內文與導讀觀點。有後續的文章，標題區多一行後續提示，也算正文（見「前情與後續」）
- 原文清單、其他語系的連結、同一事件的導讀、訂閱行與前後篇導覽不在正文裡。語系連結放在 `<article>` 裡面，所以另外標上 `role="navigation"`，Firefox 閱讀模式用的 Readability 只認這個屬性，不看 `<nav>` 標籤本身
- 改動文章頁的結構時，用 Readability（`@mozilla/readability`）解析三個語系各一篇，確認抽出來的文字符合上面兩點

iPhone Safari 的「聆聽網頁」會依頁面與裝置的語言決定是否出現。2026-09-28 在介面設成中文的 iPhone 上實測，正體中文的文章頁有這個選項，同一篇的英文版沒有。英文版在 Readability 的判定下比中文版更容易抽出正文，所以判斷是 Safari 依語言決定，跟本站的標記無關。關於頁的「朗讀」一節因此另外寫了不受語言限制的「朗讀螢幕」，設定路徑照 Apple 支援頁各語系的用字：「輔助使用 > 閱讀與朗讀」、「无障碍 > 阅读与朗读」、「Accessibility > Read & Speak」。

### 關於頁

寫給第一次來的讀者，也寫給考慮引用的記者與研究者：選題方式、查核方式、更正方式、三個語系為什麼不完全相同、社群署名、回報錯誤的管道、閱讀量統計與授權。2026-09 用模擬讀者檢視時，研究者與記者都把「查得到編輯流程與更正方式」列為引用的前提。

- 內容寫在 `pages/about.md`、`pages/zh-CN/about.md`、`pages/en/about.md`，front matter 只有 `title` 與 `description`，多出來的欄位建置時報錯
- 網址是各語系首頁底下的 `about/`，例如 `/news/about/`、`/news/zh-cn/about/`。收進 sitemap 與網址合約，不帶 noindex
- 小標題的規則跟文章相同，一律寫明 `{#id}`，三個語系的錨點集合相同，缺一個語系就建置失敗
- 更正的寫法跟實際做法一致。已經發布的文章修正時，三個語系一起改，修改紀錄留在公開 repo

### 版面

排版要讓人一眼看出是新聞，跟文件站的說明文件分開。版面從導讀這種內容的兩個特徵出發：每則新聞都有日期，每篇都是一份外文原文加上一段中文解讀。

- 標題用明體，依序找系統裡的思源宋體、宋體、新細明體，都沒有時退回黑體。內文維持黑體，螢幕上比較好讀
- 標題的字色用品牌墨色 `cyan-900`，深色模式用 `cyan-100`
- 首頁：頁首底下接一塊同色的刊頭，放大的「新聞導讀」、一句介紹，最底下一列左邊是最後更新日期，右邊是 RSS 與訂閱電子報的連結。有文章設了 `pin` 時，刊頭之後放「焦點」區塊，再來是時間軸。沒有設就直接接時間軸
- 焦點：標上「焦點」兩個字，讀者才知道這一篇為什麼長得不一樣。文章有 `image` 時把圖放進焦點區塊，手機在標題上方，桌機在右側約三分之一寬。同一篇照樣出現在時間軸自己的日期底下，日期分組不會被拆開
- 時間軸：所有文章依發布日分組，日期標題用 `position: sticky` 在捲動時停在頂端，讀者隨時知道讀到哪一天。桌機時日期在左欄。第二頁起的列表與年月封存頁用同一種時間軸，沒有刊頭與焦點
- 每篇在時間軸上顯示標題、`description` 與出處行，不放縮圖。一篇原文寫「原文來自 EFF」，多篇寫「整理 4 篇原文，來自 EFF、OONI、Access Now」，出處超過三個只列前三個再加「等 N 個出處」，都沒填 `publisher` 時只寫篇數
- 文章頁：發布日期與星期、標題、以 `description` 當副標、署名與更正日期。原文的標題、出處與日期放在獨立的「原文」區塊，多篇時標題寫成「原文（4 篇）」，每筆標題前面放來源網站的圖示（見「原文的網站圖示」）。手機時放在文末，讀者先讀到導讀。桌機寬度（64em 以上）時移到右欄，跟導讀並排，比畫面高時在區塊內捲動。署名旁另有一行出處（跟列表上的相同），行首是出處網站的圖示，連到原文區塊的 `#sources`，讓讀者一開始就知道這篇在整理外電。文章最後、導覽之前放一行 RSS 與訂閱電子報，從社群平台點進來的讀者看不到首頁的刊頭，讀完一篇時在這裡給訂閱的入口。導覽放「較新的一篇」、「較舊的一篇」與「所有文章」，前後篇帶標題，順序跟首頁時間軸相同。從社群平台點進來的讀者讀完一篇，可以直接接著讀相鄰的文章，不必先回首頁。手機上下排，桌機較新在左、較舊在右
- 手機上的表格不換行，讀者左右滑動看。畫面外的欄位如果照樣換行，會把每一列撐高

### 品牌與配色

沿用文件站[品牌素材](https://anoni.net/docs/community/brand-assets/)的 logo 與色票，不新增色相。news 的產品色是品牌色盤裡最深的 `cyan-900`（`#003e57`），跟文件站頁首的亮藍 `cyan-500` 一眼分得出來，墨色的調性也接近新聞。品牌素材頁把 cyan-900 底列為 mono white 版 logo 的建議背景，頁首與預覽圖直接照用。

圖示跟文件站用同一套，一般圖示用 Material Design Icons，Tor 這類品牌圖示用 Simple Icons。只放用到的 SVG 在 `templates/icons/`，由 `build.py` 的 `icon()` 內嵌進 HTML，不載入字型或外部檔案，onion 版本一樣可用。圖示只放在有辨識用途的連結前面：RSS、訂閱電子報、官網首頁、onion 版本、原文，以及前後篇的方向。來源與授權記在 `templates/icons/README.md`。

| 位置 | 用色 |
|---|---|
| 頁首 | `cyan-900` 底，mono white 版 logo 加「新聞導讀」 |
| 內文連結 | `cyan-800`（`#006d99`） |
| 社群預覽圖 `og.png` | `cyan-900` 底、mono white 版 logo 加「新聞導讀」 |
| 標題 | `cyan-900`，深色模式 `cyan-100` |
| 裝飾用的線條與焦點框 | `cyan-500`，不拿來寫字 |

色票變數沿用文件站 `extra.css` 的名稱（`--brand-cyan-*`），數值從那裡照抄，不自己調。

其他色相在文件站已經有固定意義：橘色是行動與活動，也是匿名支付的主題色，紅色是緊急求救，綠色是個人隱私，紫色是 Tor Relay 校園。news 要加顏色之前，先確認沒有跟這些語意撞在一起。

小字的對比度至少 4.5:1。放在白底上，`cyan-700` 只有 3.94、`cyan-500` 只有 2.47，都不能拿來寫內文或連結，`cyan-800` 是 5.76，`cyan-900` 是 11.5。

### 小螢幕

樣式從手機寬度開始寫，桌機再放寬。讀者多半從社群平台的連結點進來，第一個畫面通常就是手機。

- 每頁帶 `<meta name="viewport" content="width=device-width, initial-scale=1">`
- 320px 寬的螢幕也不能出現橫向捲軸，整頁的 `scrollWidth` 不得超過視窗寬度
- 內文欄寬在桌機上限約 40 個中文字（`max-width: 40em`），手機上就是螢幕寬度扣掉左右留白
- 內文字級至少 16px，行高 1.7 以上，中文字多，行距太密會難讀
- 原文標題與網址常是一長串英文，來源清單與內文連結加 `overflow-wrap: anywhere`，讓它們在任何位置斷行
- 表格與程式碼區塊在自己的範圍內橫向捲動（`overflow-x: auto`），不把整頁撐寬
- 行內的程式碼（cookie 名稱、主機名稱這類識別碼）加上底色與細框，跟前後的文字分得開。長的主機名稱可以在任何位置斷行，斷行後每一行保留自己的底色
- 可以點的東西觸控範圍至少 2.75rem 見方，相鄰的連結之間要有間距，避免手指點到隔壁
- 頁首在窄螢幕上不固定在畫面頂端，把高度留給內文。連結太多時換行，不收進需要 JavaScript 才打得開的選單

## 搜尋引擎與社群分享

### 標題與描述

`<title>` 固定寫成「文章標題 | 站名」，列表頁只寫站名，站名依語系而不同（見「多語系」）。`<meta name="description">` 用 front matter 的 `description`。每頁只有一個 `<h1>`，文章頁放文章標題。

### 社群分享的預覽

每一頁都帶 Open Graph 與 Twitter card 的欄位。新文章會發到社群平台，連結預覽是讀者看到的第一個畫面。

| 欄位 | 文章頁 | 列表頁與封存頁 |
|---|---|---|
| `og:type` | `article` | `website` |
| `og:title`、`og:description`、`og:url` | 標題、`description`、本頁網址 | 同左 |
| `og:image` | front matter 的 `image`，沒填時用全站共用的 `og.png` | 全站共用的 `og.png` |
| `article:published_time` | `date.created` | 無 |
| `article:modified_time` | 有更正時放 `date.updated` | 無 |
| `twitter:card` | `summary_large_image` | 同左 |

全站共用的預覽圖放在 `static/`。文章指定的 `image` 跟內文圖片一樣在建置時抓進產物，兩種都是站內的靜態檔，讀者端不會因此對外請求。

### 結構化資料

文章頁放一段 JSON-LD 的 `NewsArticle`，包含標題、`description`、發布與更正日期、網址與署名，`citation` 列出每一筆原文。署名依「發佈身分」的類型對應：

| 署名 | JSON-LD |
|---|---|
| 社群 `anoni-net` | `Organization`，名稱 anoni.net，網址是官網首頁 |
| 筆名、具名 | `Person`，只放 `name`。`authors.yml` 有 `url` 才放 `url` |

`publisher` 一律是 anoni.net 的 `Organization`。網址依輸出目標產生，onion 產物裡的 JSON-LD 用 onion 的網址。

### 索引範圍

- `/news/` 與每一篇文章允許索引
- 年、月封存頁與 `/news/page/2/` 之後的列表頁加 `<meta name="robots" content="noindex, follow">`。內容跟文章重複，搜尋引擎順著連結找到文章就好，不必把列表當成搜尋結果
- 404 頁加 `noindex`
- onion 的 `robots.txt` 允許爬取並列出 onion 版的 sitemap，跟文件站的 onion 版相同，onion 的搜尋引擎可以收錄

上線後在 Search Console 的 `anoni.net` 網域資源提交 `/news/sitemap.xml`，之後定期看 404 報表。文件站的轉址有一批就是從那份報表補的。

### 內容品質

只摘要別人的新聞，搜尋引擎可能判定為內容單薄或轉貼。能拉開差距的是每篇都有的導讀觀點。寫得夠不夠深入，建置程式查不到，要靠審稿。

## 驗證與 CI

`uv run build.py` 產出兩份產物，`uv run build.py --check` 在產出後執行下列檢查，任何一項不過就 exit 1：

1. front matter 的欄位、日期、slug 與檔名，slug 在同一個年月內不重複，`authors` 的每個鍵都在 `authors.yml` 裡。三個語系的對應（見「多語系」）。圖片的來源、格式、metadata、大小、替代文字與圖說（見「圖片」）。`sources` 的每個主機都在 `favicons.toml` 裡，圖示的格式與尺寸符合規定（見「原文的網站圖示」）
2. 內文的錨點
3. 文章、固定頁面與 `strings.toml` 有連到文件站時，網址對得上文件站的網址合約。訂閱頁連到的 RSS 訂閱入門搬家或改名，這一項會擋下來
4. 產物沒有可執行的 `<script>`（`application/ld+json` 除外，而且內容要能解析成 JSON），也沒有指向站外的資源
5. onion 產物沒有 clearnet 的 anoni.net 連結
6. 本站的網址合約
7. 每頁都有 `<title>`、`description` 與 Open Graph 欄位，封存頁、第二頁起的列表頁與 404 頁帶 `noindex`
8. 版面：用 headless Chrome 以 320、390、1280 三種寬度開啟三個語系的列表頁與一篇文章，以及 404 頁，每頁的 `scrollWidth` 不得超過設定的寬度，並存下截圖。要跟設定的寬度比，不能跟 `window.innerWidth` 比：手機模式下頁面被撐寬時，Chrome 會自動縮小畫面去容納內容，`innerWidth` 跟著變大，兩邊永遠一樣寬
9. 對比度：`news.css` 裡文字色與背景色的組合，淺色與深色模式都要達到 4.5:1

測試用的文章放在 `tests/fixtures/`，刻意放進最長的英文標題、長網址、表格與程式碼區塊，版面出問題時在這裡先發生。第 8 項需要 Chrome，GitHub Actions 的 runner 上有，本機沒有 Chrome 時略過並提示。截圖只證明頁面撐得住，排版好不好看，送出 PR 前還是要有人實際看過截圖。

`main` 設了分支保護：`check` 必須通過才能合併，PR 的分支落後 `main` 時要先更新（PR 頁面的「Update branch」，或 `gh pr update-branch`）再執行一次 CI，管理員也一樣。規則改嚴的 PR 合併之後，其他開著的 PR 要照新規則重新執行 CI，不會帶著舊的綠燈合併進來。2026-09-27 就發生過，原文網站圖示的檢查合併之後，三篇在那之前通過 CI 的文章接著合併，`main` 的部署失敗了約半小時。

GitHub Actions 在 PR 上執行 `--check`、`pytest`，並用文件站的 `docs_style_lint.py` 掃 `posts/` 底下全部的 Markdown 與 `README.md`。檔案一律傳完整路徑，linter 才能從 `/zh-CN/` 與 `/en/` 認出語系。

## 部署

1. `main` 有新的 commit 時，CI 執行 `--check` 後建置兩份產物，推到 `build` 分支，目錄是 `clearnet/` 與 `onion/`。`build` 分支保留歷史，出問題時可以退回上一個 commit
2. 伺服器上 clone `build` 分支。nginx 在 clearnet 的 `anoni.net` server block 加一條 `location /news/` 指向 `clearnet/`，onion 那一側新增一個 `news.<onion 位址>` 的 server block，根目錄指向 `onion/`。子網域共用同一個 onion service，由 nginx 依主機名稱分流，跟 `docs.<onion 位址>` 相同，Tor 的設定不用改
3. 官網 repo 的 `robots.txt` 模板補上 `/news/sitemap.xml`，跟 news 上線同一天合併。2026-09-26 上線時漏了這一步，隔天由 toomore/anoni-net#7 補上，clearnet 與 onion 兩份都列
4. `static/` 的檔案（樣式、favicon、頁首 logo、預覽圖）在網址後面帶內容雜湊，例如 `css/news.css?v=3f9a1c2b7e`。HTML 不讓瀏覽器快取，內容改了網址就跟著變，瀏覽器與 Cloudflare 會當成新檔案去抓，部署之後不必清這些檔案的快取
5. m6 由 `ubuntu` 的 crontab 每 5 分鐘執行 `/home/ubuntu/news-pull.sh`，拉 `build` 分支上線，原始檔是本 repo 的 `tools/m6-pull.sh`。只接受 fast-forward，`build` 分支的歷史被改寫時停下來寫進 `/home/ubuntu/news-pull.log`，不強制覆蓋
6. 從合併到上線最慢約 15 分鐘：CI 建置約 3 分鐘，m6 最多等 5 分鐘，Cloudflare 上的頁面最多快取 5 分鐘。急著看的話清頁面的快取

## 排程發布

稿子可以先審、先合併，到了 `date` 寫的時間才上線，不必每天在固定時間按合併。

- `date` 晚於建置當下（台北時間）的文章是排程中，建置照樣檢查它的格式、三個語系的對應與圖片，但不產生頁面，也不進首頁、封存頁、RSS 與 sitemap，前後篇的連結當它不存在
- 固定在台北時間早上 7 點發布，`date` 寫成 `YYYY-MM-DDT07:00:00+08:00`
- 最多排到 7 天後，超過就建置失敗。寫稿當下查核的事實放久了可能又變了，排程不宜太遠
- deploy workflow 每小時第 2 分鐘重建一次（`cron: "2 * * * *"`），時間到的文章就出現在產物裡。GitHub 的排程在尖峰時會延遲，版面檢查也偶爾失敗，每小時一輪讓最壞情況是晚一小時上線。產物沒變時不推 `build` 分支
- 網址合約收進排程中的文章，`--check` 比對的是「已發布加上排程中」的網址，排程中的文章還沒上線不算網址消失
- `anoni-net/news` 是公開 repo，排程中的稿子合併之後，發布前就讀得到。需要等特定時間才能公開的稿子，到時間再合併
- 排程中的稿子要改，就再開一個 PR。已經上線的照更正處理
- GitHub 會停掉 60 天沒有任何 commit 的公開 repo 的排程。照目前的發稿節奏不會遇到，長期停更之前要記得這件事

## 相依

- Python 3.12，用 uv 管理
- `jinja2`、`markdown`（Python-Markdown，開 `attr_list`、`tables`、`fenced_code`）、`pyyaml`
- `websockets`，版面檢查用來跟 Chrome 溝通
- `pillow`，讀圖片的尺寸與 metadata，搬圖工具與圖示工具也用它轉檔
- 開發用 `pytest`

選 Python-Markdown 是因為 MkDocs 家族用的就是它，同一份 Markdown 換到 Zensical 或 mkdocs-ng 時的轉換結果最接近。不開 `toc`，它會替沒寫 `{#id}` 的小標題自動產生錨點，漏寫的錨點就檢查不到了。

## 第一版不做的事

以下功能不在第一版，要做之前先修改本文件：

- 站內搜尋。中文要斷詞，而且需要 JavaScript，加入前要先處理「路徑與子網域」一節提到的同源問題
- 分類與標籤頁，`categories` 只存不產頁
- 作者頁。筆名的作者頁會把同一個人的文章集中成一頁，要做之前先想清楚匿名的代價
- 每篇自動產生的預覽卡片圖。需要專屬預覽圖時，用 front matter 的 `image` 手動指定
- 留言與任何需要伺服器端的功能
- 自動寄送電子報
- 投稿平台。維護者代發的稿件，之後會需要一個讓投稿者送稿、跟維護者往返修改的平台，第一版先用「發布管道」一節列的 Matrix、email 與 Send
- 時間軸的縮圖。多數文章預期沒有圖，有圖與沒圖混在一起版面參差，一頁 20 張圖也增加 onion 與手機讀者的負擔。上線一段時間後，大多數文章都有 `image` 再評估
- 每週彙整頁（例如 `/news/weekly/2026-09-18/`），把一週的文章整理成一頁給電子報與不常來的讀者，第一版上線後再評估

## 待決定的事

- 發布節奏：寫好就發，或固定在每週某幾天發
- 內部篩選過的新聞改寫成對外版本時，由誰改寫、誰審稿
- 維護者代發時用維護者本人的身分，或另設一個共用的發布身分（例如 `news@anoni.net`，要另外準備簽章金鑰）
