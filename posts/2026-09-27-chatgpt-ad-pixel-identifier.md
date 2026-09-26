---
title: ChatGPT 廣告像素的跨站識別碼
description: 一份流量分析發現，ChatGPT 的廣告系統會設定一個跟帳號連動的 cookie，買廣告的網站再透過 OpenAI 的像素把它連同瀏覽資料送回去。
date: 2026-09-27
slug: chatgpt-ad-pixel-identifier
sources:
  - title: ChatGPT now knows what you do on other websites via ad collector
    url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
    publisher: Buchodi's Threat Intel
    date: 2026-09-20
authors:
  - anoni-net
---

一位資安研究者分析 ChatGPT 的廣告流量，發現使用 ChatGPT 時，OpenAI 的廣告收集器 `bzr.openai.com` 會設定一個名為 `__obi` 的 cookie。它跟 ChatGPT 帳號連動，有效期一年，而且允許在其他網站的請求中送出。目前只在 Android 版 Chrome 觀察到，iOS 上的瀏覽器都擋掉了。ChatGPT 的廣告在台灣有沒有上線，原文沒有提到。

在 ChatGPT 買廣告的業者，會在自己的網站裝上 OpenAI 的像素。使用者之後造訪這些網站時，像素會把 `__obi` 連同頁面資料送回 OpenAI，包括網址路徑、表單欄位與網頁上的文字。電子郵件、電話與姓名經過 SHA-256 雜湊，國家、地區、城市與郵遞區號則是明碼。研究者觀察到的網址都去掉了查詢字串，但路徑本身有時就透露了病症這類敏感資訊。

這組識別碼在登出時也會設定。研究者檢視的每一個同步權杖，同意類別都是「分析」，只允許分析、拒絕行銷的使用者照樣會被設定。

研究者在自己的手機上重現，用兩種方式擷取流量，另外分析了 936 個廣告主像素、超過一千個網域。原文也寫明了幾項限制：約五分之一的 ChatGPT 工作階段產生同步權杖，桌機版 Chrome 沒有測試，而 OpenAI 在伺服器端把識別碼對應回帳號，是從設計推論，研究者沒有直接觀察到。研究者 9 月 14 日去信詢問，OpenAI 的客服收到後沒有回答提問。

## 技術觀點 {#technical-view}

廣告主網站上的像素把造訪紀錄送回廣告平台，Meta 與 Google 的轉換追蹤用的都是同一套做法。差別在於 ChatGPT 帳號裡還有使用者跟 AI 的對話，許多人會在對話裡提到健康、工作與個人問題，這些資料跟其他網站的瀏覽紀錄，現在有機會連到同一個帳號。

`__obi` 能在其他網站送出，靠的是第三方 cookie。Safari 預設阻擋跨站追蹤，iOS 上的瀏覽器又都使用 Safari 的 WebKit 引擎，所以研究者在 iOS 上都沒有觀察到。Android 與桌機可以在瀏覽器設定裡封鎖第三方 cookie，Firefox 預設就把第三方 cookie 依網站隔離，Brave 預設封鎖。平常不需要登入狀態跨網站延續的人，封鎖第三方 cookie 的代價很小。

同意橫幅上的「分析」與「行銷」只是業者自訂的分類，選項名稱不代表實際行為。只允許分析，並不能擋下跟廣告連動的識別碼。

這份分析出自單一研究者的流量觀察，OpenAI 沒有回應，伺服器端的對應也沒有直接證據。它的價值在於把機制拆得夠細，其他研究者可以照著驗證。
