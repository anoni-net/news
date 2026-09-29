---
title: 澳洲 Medicare 統計網站的 AI 代理程式入侵事件
description: OpenAI 的 AI 代理程式 6 月在內部評估中繞過存取限制，進入澳洲 Medicare 統計網站並寫入檔案。到 9 月 24 日為止，澳洲政府研判沒有個人資料遭到存取，網站上是彙總的統計資料。使用 AI 代理程式的人可以替它開一個獨立的瀏覽器設定檔。
date: 2026-10-02T07:05:00+08:00
slug: openai-agent-medicare-portal
sources:
  - title: Press conference - New York
    url: https://www.pm.gov.au/media/press-conference-new-york
    publisher: Prime Minister of Australia
    date: 2026-09-24
  - title: Press Conference, Sydney
    url: https://www.minister.defence.gov.au/transcripts/2026-09-24/press-conference-sydney
    publisher: Australian Minister for Defence
    date: 2026-09-24
  - title: The Hugging Face incident and other third-party impact from misaligned models
    url: https://openai.com/hugging-face-incident-and-misalignment/
    publisher: OpenAI
    date: 2026-09-25
  - title: Australia launches urgent review after OpenAI program hacks government health portal
    url: https://www.bbc.com/news/live/cvgl73pxgndwt
    publisher: BBC News
    date: 2026-09-24
  - title: "OpenAI ‘climbed the fence’: Taskforce scrambles after long delays flagging Medicare hack"
    url: https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html
    publisher: The Sydney Morning Herald
    date: 2026-09-24
  - title: Singapore Launches New Model AI Governance Framework for Agentic AI
    url: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai
    publisher: IMDA
    date: 2026-01-22
  - title: Factsheet - Model AI Governance Framework for Agentic AI
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2026/01/factsheet-model-ai-governance-framework-for-agentic-ai.pdf
    publisher: IMDA
    date: 2026-01-22
  - title: 資通安全事件通報應變及演練辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=A0030305
    publisher: 全國法規資料庫
    date: 2026-01-05
  - title: 管理多個 Chrome 設定檔
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hant
    publisher: Google Chrome 說明
  - title: 管理多個 Chrome 設定檔（Android）
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hant&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 說明
watch:
  - date: 2026-11-02
    note: 澳洲專案小組的檢討結果、ASD 鑑識調查與是否移交澳洲聯邦警察，OpenAI 事件說明頁是否補上 Medicare 的分類
regions:
  - AU
authors:
  - anoni-net
---

澳洲總理在紐約的記者會上（澳洲東部時間 9 月 24 日 6 點過後，台北時間 4 點過後）公布，OpenAI 的 AI 代理程式（能自行操作網頁的程式）未經授權，進入澳洲 Medicare（全民健保）的統計報表網站。代理程式存取了非公開的檔案，也在內部伺服器寫入檔案。到 9 月 24 日為止，澳洲政府研判沒有個人資料遭到存取。OpenAI 另外通知了數十個可能受影響的第三方。

網站由 Services Australia（辦理健保等服務的聯邦機關）管理，放的是彙總的統計資料，9 月 24 日已經停用。代理程式當時在 OpenAI 的內部能力評估中研究政府的藥品支出，6 月 18 日被網站拒絕之後，改用其他方式繞過限制。

OpenAI 8 月在全面檢視中察覺，9 月 10 日寄信到 Services Australia 受理漏洞通報的信箱。該機關 11 日看到信，經過週末與查核真偽，15 日通報澳洲訊號局（ASD，負責網路防禦的情報機關）轄下的澳洲網路安全中心。

總理表示，OpenAI 通知得太慢，方式也無法接受。政府成立專案小組檢討網路防護與罰則，也將評估是否移交澳洲聯邦警察。ASD 協助鑑識調查，也在查其他政府系統是否受影響。

OpenAI 發言人表示，模型「採取了並非我們本意的行動」。OpenAI 在事件說明頁列出匿名的行為分類，例如繞過存取控制、使用公開外露的登入資訊，沒有寫明 Medicare 網站屬於哪一類。

## 導讀觀點 {#perspective}

OpenAI 舉的繞過例子有改用另一個網址、修改請求的內容，都是常見的存取控制弱點，人工操作一樣可以做到。主管部長說明，網站是用了數十年的舊系統。維護網站的組織可以盤點少有人管理的舊系統，用不到的下線，還要用的確認非公開檔案需要登入。

台灣的《資通安全事件通報應變及演練辦法》規定，公務機關知悉資安事件後需在一小時內通報。澳洲這次從事件發生到 OpenAI 寄出通知將近三個月。外部發現問題的人何時要通知，辦法沒有規定。

新加坡資訊通信媒體發展局（IMDA）1 月發布代理式 AI 的治理框架，建議組織在設計階段就限制代理程式的自主程度、可用工具與資料存取。個人也適用同一個原則，代理程式能觸及的範圍就是它手上的登入狀態與權限。

在電腦版 Chrome 執行代理程式的人，可以從右上方的設定檔圖示選擇「新增 Chrome 設定檔」，替它開一個只登入必要帳號的設定檔。步驟只有三步，不需要 Google 帳號，說明頁有正體中文。Android 版 Chrome 只能有一個設定檔，在雲端瀏覽器執行的代理程式也用不上這個做法。代價是新設定檔沒有原本的書籤、密碼與登入狀態，帳號要再登入一次。
