---
title: ChatGPT 廣告像素的跨站識別碼
description: 一份流量分析發現，ChatGPT 的廣告系統會設定一個跟帳號連動的 cookie，買廣告的網站再透過 OpenAI 的像素，把它連同瀏覽資料送回 OpenAI。目前只在 Android 版 Chrome 觀察到。
date: 2026-09-26T01:24:00+08:00
slug: chatgpt-ad-pixel-identifier
sources:
  - title: ChatGPT now knows what you do on other websites via ad collector
    url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
    publisher: Buchodi's Threat Intel
    date: 2026-09-20
  - title: ChatGPT Ads expands to Southeast Asia and Taiwan
    url: https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
    publisher: OpenAI
    date: 2026-09-23
  - title: 在 Chrome 中刪除、允許使用與管理 Cookie
    url: https://support.google.com/chrome/answer/95647?hl=zh-Hant&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 說明
authors:
  - anoni-net
---

一位資安研究者分析 ChatGPT 的廣告流量，發現使用 ChatGPT 時，OpenAI 的廣告收集器 `bzr.openai.com` 會設定一個名為 `__obi` 的 cookie。它跟 ChatGPT 帳號連動，有效期一年，而且允許在其他網站的請求中送出。研究者只在 Android 版 Chrome 觀察到這個機制，iOS 上的瀏覽器都會阻擋。OpenAI 在 9 月 23 日宣布 ChatGPT 廣告開始在台灣等七個亞洲市場推出，廣告只顯示給 Free 與 Go 方案的使用者。

在 ChatGPT 買廣告的業者，會在自己的網站裝上 OpenAI 的像素。使用者之後造訪廣告主的網站時，像素會把 `__obi` 連同頁面資料送回 OpenAI，包括網址路徑、表單欄位與網頁上的文字。電子郵件、電話與姓名經過 SHA-256 雜湊，國家、地區、城市與郵遞區號則是明碼。研究者觀察到的網址都去掉了查詢字串，但路徑本身有時就透露了病症等敏感資訊。

使用者在登出狀態下同樣會被設定 `__obi`。研究者檢視的每一個同步權杖，同意類別都標為「分析」。使用者只要允許分析，即使拒絕行銷也會收到 `__obi`。

研究者在自己的手機上重現，用兩種方式擷取流量，另外分析了 936 個廣告主像素、超過一千個網域。原文也寫明了幾項限制：約五分之一的 ChatGPT 工作階段產生同步權杖，桌機版 Chrome 沒有測試。OpenAI 在伺服器端把識別碼對應回帳號，是研究者從設計推論，沒有直接觀察到。研究者 9 月 14 日去信詢問，OpenAI 的客服收到後沒有回答提問。

## 導讀觀點 {#perspective}

廣告主網站上的像素把造訪紀錄送回廣告平台，研究者在原文把它比作零售業者早已安裝的 Meta 與 Google 追蹤程式碼。差別在於 ChatGPT 帳號裡還有使用者跟 AI 的對話，許多人會在對話裡提到健康、工作與個人問題，對話內容與其他網站的瀏覽紀錄可能因此連到同一個帳號。

`__obi` 透過第三方 cookie 在其他網站送出。Safari 預設阻擋跨站追蹤，iOS 上的瀏覽器又都使用 Safari 的 WebKit 引擎，所以研究者在 iOS 上都沒有觀察到。Android 與桌機可以在瀏覽器設定裡封鎖第三方 cookie，Firefox 預設把第三方 cookie 依網站隔離，Brave 預設封鎖。

同意橫幅的分類由業者自行定義，在這次的案例裡，「分析」這個選項也涵蓋了廣告用途的識別碼同步。只拒絕「行銷」不足以避開廣告追蹤。

研究者觀察到的情境是在 Android 手機上用 Chrome 登入 ChatGPT，用 iPhone 的人不必另外設定。符合的人可以在 Chrome 的「設定」依序點「網站設定」、「第三方 Cookie」，選擇「封鎖第三方 Cookie」，Google 的說明頁有正體中文的步驟。封鎖之後部分網站可能無法正常運作，可以把需要的網站加進例外清單。不想更動 Chrome 設定的人，也可以改在另一個瀏覽器使用 ChatGPT，跟平常瀏覽其他網站的瀏覽器分開。
