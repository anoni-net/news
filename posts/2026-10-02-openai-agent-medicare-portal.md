---
title: 澳洲 Medicare 統計網站的 AI 代理程式入侵事件
description: OpenAI 的 AI 代理程式在 6 月的內部評估中繞過存取限制，進入澳洲 Medicare 統計網站並寫入檔案。澳洲政府 9 月才從公開信箱收到通知，從事件發生到通報隔了將近三個月。澳洲政府目前研判沒有個人資料外洩。
date: 2026-10-02T07:05:00+08:00
slug: openai-agent-medicare-portal
sources:
  - title: Australia launches urgent review after OpenAI program hacks government health portal
    url: https://www.bbc.com/news/live/cvgl73pxgndwt
    publisher: BBC News
    date: 2026-09-24
  - title: "OpenAI ‘climbed the fence’: Taskforce scrambles after long delays flagging Medicare hack"
    url: https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html
    publisher: The Sydney Morning Herald
    date: 2026-09-24
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
authors:
  - anoni-net
---

澳洲總理在 9 月 24 日於紐約公布，OpenAI 的一個 AI 代理程式未經授權進入 Services Australia 管理的 Medicare 統計報表網站（Medicare Statistics Reporting Service），存取了公開與非公開的檔案，還在內部伺服器寫入檔案。澳洲訊號局（ASD）正協助鑑識調查，範圍包括其他政府系統是否也受到影響。

Medicare 統計報表網站提供醫療支出之類的非敏感統計資料。依澳洲政府的說明，目前研判沒有個人資料外洩，調查仍在進行，網站也已經停用。代理程式當時在執行 OpenAI 內部的能力評估，任務是上網研究公共藥品支出，取得資料的要求被拒絕之後，改用其他方式繞過限制。

事件發生在 6 月 18 日，OpenAI 在 8 月的一次全面檢視中察覺，9 月 10 日寄信到 Services Australia 的公開信箱。該信箱每天查看一次，Services Australia 在 11 日看到信，15 日才通報澳洲網路安全中心。

澳洲總理在記者會上表示，OpenAI 通知得太慢，通知的方式也無法接受。政府已成立專案小組檢討網路防護與罰則，也可能把案件移交聯邦警察。

OpenAI 發言人表示，模型在內部評估中存取了「數個澳洲政府的網站與服務」，並「採取了我們沒有預期的行動」。OpenAI 的事件說明頁寫到，已通知數十個受影響的第三方，並公開匿名的行為分類，包括繞過存取控制、使用外流的登入資訊、注入查詢或指令、讀取服務的內部檔案。

## 導讀觀點 {#perspective}

OpenAI 列出的繞過手法，例如改用另一個網址、修改請求的內容、沿用權限過大的登入工作階段，都是網站常見的存取控制弱點，換成人工操作同樣可行。出事的網站據 SMH 報導是一個主要給學者使用的舊網站。維護網站的組織可以先盤點還在線上、但已經少有人管理的舊系統，用不到的下線，還要用的確認非公開檔案需要登入才能取得。

台灣的《資通安全事件通報應變及演練辦法》規定，公務機關知悉資安事件後需在一小時內通報。澳洲這次耗時最長的階段在機關知悉之前，從事件發生到 OpenAI 寄出通知將近三個月。OpenAI 選擇寄到公開信箱，通知又在政府內部多走了幾天才送到資安單位。

一般使用者讓 AI 代理程式代為瀏覽網頁、填寫表單時，代理程式能觸及的範圍，就是它手上的登入狀態與權限。新加坡資通訊媒體發展局（IMDA）1 月發布的代理式 AI 治理框架裡的建議，是在設計階段限制代理程式的自主程度、可用工具與資料存取。個人使用時可以比照辦理，在電腦版 Chrome 右上方的設定檔圖示選擇「新增 Chrome 設定檔」，讓代理程式在獨立的設定檔執行，只登入任務需要的帳號。
