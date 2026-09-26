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
| 不依賴 JavaScript | 產物裡沒有可執行的 `<script>`。唯一的例外是 `type="application/ld+json"` 的結構化資料，瀏覽器不會執行它 |
| 不對外請求 | 產物的 `src`、`<link href>`、CSS 的 `url()` 只能指向站內路徑 |
| clearnet 與 onion 分開產出 | onion 產物裡沒有任何 `https://anoni.net` 開頭的連結 |
| 網址一經公開就不改 | 網址合約，移除或改名會讓 CI 失敗 |

## 目錄結構

```
posts/                   # 一篇一個 Markdown，檔名是發布日加 slug
  2026-09-18-zkp-age-verification.md
templates/               # Jinja2 模板
  _layout.html.j2
  post.html.j2
  list.html.j2           # 列表頁與年、月封存頁共用
  404.html.j2
  feed.xml.j2
  sitemap.xml.j2
  robots.txt.j2          # 只輸出到 onion，clearnet 的 robots.txt 在官網 repo
static/                  # 兩份產物共用的檔案
  css/news.css
  favicon.svg            # 文件站的 logo-tonal.svg
  logo-wordmark-white.svg  # 文件站的 mono white wordmark，放在頁首
  og.png                 # 全站共用的社群分享預覽圖，1200×630
tools/
  og.html                # og.png 的原始檔
  make_og.sh             # 用 Chrome 從 og.html 產生 og.png
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
| `date` | 是 | 第一次發布的日期，決定網址裡的年月，發布之後不能改。有更正時寫成 `date: {created: 2026-09-18, updated: 2026-09-20}` |
| `slug` | 是 | 小寫英文、數字與連字號，3 到 60 個字元，同一個年月內不重複。Material 的 blog 預設從標題產生 slug，寫明才能確保換工具後網址不變 |
| `sources` | 是 | 原文，至少一筆。每筆的 `title` 與 `url` 必填，`publisher` 與 `date` 選填。一篇可以列多筆，用在同一事件的多篇報導，也用在把好幾篇原文整理成一篇觀點 |
| `authors` | 是 | 對應 `authors.yml` 的鍵，見「發佈身分」。不想署名就寫 `anoni-net` |
| `categories` | 否 | 第一版只存不產頁 |
| `draft` | 否 | `true` 時不產出，也不進列表、封存頁與 RSS |

多出來的欄位建置時報錯，避免打錯字的欄位被靜默忽略。

### 內文

來源由模板依 `sources` 顯示在標題下方，內文不再重寫一次。內文依序寫摘要、跟正體中文使用者的關係，最後是延伸閱讀：

```markdown
摘要段落……

跟正體中文使用者的關係……

延伸閱讀：[威脅模型](https://anoni.net/docs/basics/threat-model/)
```

建置時檢查：

- 內文如果有小標題，一律用 `{#id}` 寫明錨點，id 只用小寫英文、數字與連字號，同一篇裡不重複。中文標題自動產生的錨點會隨著改字而變，寫明 id 才能讓分享出去的段落連結長期有效
- 至少有一條連到 `https://anoni.net/docs/` 的連結
- 連到文件站的網址必須存在於文件站的網址合約（`anoni-net/docs` 的 `tools/data/url_contract.txt`），錨點也一樣

站內與文件站的連結一律寫 clearnet 的完整網址，onion 產物由建置程式改寫（見「clearnet 與 onion」）。

## 發佈身分

news 開放多人發布，署名可以是本名、固定的筆名，或不具名。身分會從兩個地方洩漏：網站上顯示的署名，以及公開 repo 留下的 git 紀錄與 PR。只處理前者，匿名就只是表面上的。

### 署名

`authors.yml` 列出所有署名，每篇的 `authors` 對應其中的鍵：

```yaml
anoni-net:
  name: anoni.net 社群
night-owl:
  name: 夜梟
  description: 關注網路封鎖的量測
```

| 欄位 | 必填 | 說明 |
|---|---|---|
| `name` | 是 | 顯示在文章頁、列表頁與 RSS 的名稱 |
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
| `/news/404.html` | 找不到頁面 |

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
- `<guid isPermaLink="false">` 用 `anoni-news:2026/09/zkp-age-verification`，clearnet 與 onion 兩份 feed 用同一個值
- 日期用 RFC 822 格式，時區固定 `+0800`
- feed 裡的網址必須是完整網址，這是兩份產物一定不同的地方

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

## 頁面

- 樣式自己寫，只用系統字型，不載入 Bulma 與 Font Awesome。配色見下方「品牌與配色」
- 支援 `prefers-color-scheme: dark`
- 頁首：anoni.net 標誌連回官網首頁、「新聞導讀」、連到文件站
- 頁尾：RSS、授權（CC-BY 4.0）、onion 位址（clearnet 才顯示）、訂閱電子報

### 版面

排版要讓人一眼看出是新聞，跟文件站的說明文件分開。版面從導讀這種內容的兩個特徵出發：每則新聞都有日期，每篇都是一份外文原文加上一段中文解讀。

- 標題用明體，依序找系統裡的思源宋體、宋體、新細明體，都沒有時退回黑體。內文維持黑體，螢幕上比較好讀
- 標題的字色用品牌墨色 `cyan-900`，深色模式用 `cyan-100`
- 首頁：頁首底下接一塊同色的刊頭，放大的「新聞導讀」、一句介紹與最後更新日期。刊頭之後是最新一篇的頭條，再來是時間軸
- 時間軸：其餘文章依發布日分組，日期標題用 `position: sticky` 在捲動時停在頂端，讀者隨時知道讀到哪一天。桌機時日期在左欄。第二頁起的列表與年月封存頁用同一種時間軸，沒有刊頭與頭條
- 每篇在列表上顯示標題、`description` 與出處行。一篇原文寫「原文來自 EFF」，多篇寫「整理 4 篇原文，來自 EFF、OONI、Access Now」，出處超過三個只列前三個再加「等 N 個出處」，都沒填 `publisher` 時只寫篇數
- 文章頁：發布日期與星期、標題、以 `description` 當副標、署名與更正日期。原文的標題、出處與日期放在獨立的「原文」區塊，多篇時標題寫成「原文（4 篇）」。手機時放在文末，讀者先讀到導讀。桌機寬度（64em 以上）時移到右欄，跟導讀並排，比畫面高時在區塊內捲動。署名旁另有一行出處（跟列表上的相同），連到原文區塊的 `#sources`，讓讀者一開始就知道這篇在整理外電
- 手機上的表格不換行，讀者左右滑動看。畫面外的欄位如果照樣換行，會把每一列撐高

### 品牌與配色

沿用文件站[品牌素材](https://anoni.net/docs/community/brand-assets/)的 logo 與色票，不新增色相。news 的產品色是品牌色盤裡最深的 `cyan-900`（`#003e57`），跟文件站頁首的亮藍 `cyan-500` 一眼分得出來，墨色的調性也接近新聞。品牌素材頁把 cyan-900 底列為 mono white 版 logo 的建議背景，頁首與預覽圖直接照用。

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
- 可以點的東西觸控範圍至少 2.75rem 見方，相鄰的連結之間要有間距，避免手指點到隔壁
- 頁首在窄螢幕上不固定在畫面頂端，把高度留給內文。連結太多時換行，不收進需要 JavaScript 才打得開的選單

## 搜尋引擎與社群分享

### 標題與描述

`<title>` 固定寫成「文章標題 | anoni.net 新聞導讀」，列表頁是「anoni.net 新聞導讀」。`<meta name="description">` 用 front matter 的 `description`。每頁只有一個 `<h1>`，文章頁放文章標題。

### 社群分享的預覽

每一頁都帶 Open Graph 與 Twitter card 的欄位。新文章會發到社群平台，連結預覽是讀者看到的第一個畫面。

| 欄位 | 文章頁 | 列表頁與封存頁 |
|---|---|---|
| `og:type` | `article` | `website` |
| `og:title`、`og:description`、`og:url` | 標題、`description`、本頁網址 | 同左 |
| `og:image` | 全站共用的 `og.png` | 同左 |
| `article:published_time` | `date.created` | 無 |
| `article:modified_time` | 有更正時放 `date.updated` | 無 |
| `twitter:card` | `summary_large_image` | 同左 |

預覽圖只有一張，放在 `static/`，不為每篇另外產圖。圖是站內的靜態檔，讀者端不會因此對外請求。

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

只摘要別人的新聞，搜尋引擎可能判定為內容單薄或轉貼。能拉開差距的是每篇都有的「跟正體中文使用者的關係」與連到文件站的延伸閱讀。建置程式只查得到有沒有連到文件站，寫得夠不夠深入要靠審稿。

## 驗證與 CI

`uv run build.py` 產出兩份產物，`uv run build.py --check` 在產出後執行下列檢查，任何一項不過就 exit 1：

1. front matter 的欄位、日期、slug 與檔名，slug 在同一個年月內不重複，`authors` 的每個鍵都在 `authors.yml` 裡
2. 內文的錨點與文件站連結
3. 文件站連結對得上文件站的網址合約
4. 產物沒有可執行的 `<script>`（`application/ld+json` 除外，而且內容要能解析成 JSON），也沒有指向站外的資源
5. onion 產物沒有 clearnet 的 anoni.net 連結
6. 本站的網址合約
7. 每頁都有 `<title>`、`description` 與 Open Graph 欄位，封存頁、第二頁起的列表頁與 404 頁帶 `noindex`
8. 版面：用 headless Chrome 以 320、390、1280 三種寬度開啟列表頁、一篇文章與 404 頁，每頁的 `scrollWidth` 不得超過設定的寬度，並存下截圖。要跟設定的寬度比，不能跟 `window.innerWidth` 比：手機模式下頁面被撐寬時，Chrome 會自動縮小畫面去容納內容，`innerWidth` 跟著變大，兩邊永遠一樣寬
9. 對比度：`news.css` 裡文字色與背景色的組合，淺色與深色模式都要達到 4.5:1

測試用的文章放在 `tests/fixtures/`，刻意放進最長的英文標題、長網址、表格與程式碼區塊，版面出問題時在這裡先發生。第 8 項需要 Chrome，GitHub Actions 的 runner 上有，本機沒有 Chrome 時略過並提示。截圖只證明頁面撐得住，排版好不好看，送出 PR 前還是要有人實際看過截圖。

GitHub Actions 在 PR 上執行 `--check`、`pytest`，並用文件站的 `docs_style_lint.py` 掃 `posts/*.md` 與 `README.md`。

## 部署

1. `main` 有新的 commit 時，CI 執行 `--check` 後建置兩份產物，推到 `build` 分支，目錄是 `clearnet/` 與 `onion/`。`build` 分支保留歷史，出問題時可以退回上一個 commit
2. 伺服器上 clone `build` 分支。nginx 在 clearnet 的 `anoni.net` server block 加一條 `location /news/` 指向 `clearnet/`，onion 那一側新增一個 `news.<onion 位址>` 的 server block，根目錄指向 `onion/`。子網域共用同一個 onion service，由 nginx 依主機名稱分流，跟 `docs.<onion 位址>` 相同，Tor 的設定不用改
3. 官網 repo 的 `robots.txt` 模板補上 `/news/sitemap.xml`，跟 news 上線同一天合併
4. 第一版手動 `git pull` 上線，自動部署等官網首頁的部署方式定案後一起處理

## 相依

- Python 3.12，用 uv 管理
- `jinja2`、`markdown`（Python-Markdown，開 `attr_list`、`tables`、`fenced_code`）、`pyyaml`
- `websockets`，版面檢查用來跟 Chrome 溝通
- 開發用 `pytest`

選 Python-Markdown 是因為 MkDocs 家族用的就是它，同一份 Markdown 換到 Zensical 或 mkdocs-ng 時的轉換結果最接近。不開 `toc`，它會替沒寫 `{#id}` 的小標題自動產生錨點，漏寫的錨點就檢查不到了。

## 第一版不做的事

以下功能不在第一版，要做之前先修改本文件：

- 站內搜尋。中文要斷詞，而且需要 JavaScript，加入前要先處理「路徑與子網域」一節提到的同源問題
- 多語系，只出正體中文
- 分類與標籤頁，`categories` 只存不產頁
- 作者頁。筆名的作者頁會把同一個人的文章集中成一頁，要做之前先想清楚匿名的代價
- 內文圖片。有圖就要處理授權、替代文字與體積，第一版全文字。全站共用的 `og.png` 不在此限
- 每篇各自產生的預覽卡片圖，第一版全站共用一張
- 留言與任何需要伺服器端的功能
- 自動寄送電子報
- 投稿平台。維護者代發的稿件，之後會需要一個讓投稿者送稿、跟維護者往返修改的平台，第一版先用「發布管道」一節列的 Matrix、email 與 Send
- 每週彙整頁（例如 `/news/weekly/2026-09-18/`），把一週的文章整理成一頁給電子報與不常來的讀者，第一版上線後再評估

## 待決定的事

- 發布節奏：寫好就發，或固定在每週某幾天發
- clearnet 是否放流量統計，官網首頁與文件站都有 Umami
- 內部篩選過的新聞改寫成對外版本時，由誰改寫、誰審稿
- 維護者代發時用維護者本人的身分，或另設一個共用的發布身分（例如 `news@anoni.net`，要另外準備簽章金鑰）
- 上線時的第一批文章：整理 2026 年 6 月到 9 月累積的新聞，或從下一次篩選開始
