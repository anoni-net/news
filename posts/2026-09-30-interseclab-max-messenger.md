---
title: 俄羅斯國家通訊 App Max 的技術分析
description: InterSecLab 分析俄羅斯規定預裝的通訊 App Max，發現沒有端對端加密，VPN 偵測、網路探測與語音轉文字都能從伺服器針對個別帳號開啟，介面上看不出來。
date: 2026-09-30T07:05:00+08:00
slug: interseclab-max-messenger
sources:
  - title: "The Max Messenger: An Analysis of Russia’s State-Mandated Messaging Application"
    url: https://interseclab.org/research/max/
    publisher: InterSecLab
    date: 2026-09-24
  - title: О включении цифровой платформы Max в список программ для предварительной установки
    url: http://government.ru/docs/55977/
    publisher: Правительство России
    date: 2025-08-21
  - title: Russia says it has blocked WhatsApp amid wider clampdown on social media
    url: https://www.cnn.com/2026/02/12/tech/russia-whatsapp-social-media-clampdown-intl
    publisher: CNN
    date: 2026-02-12
  - title: "Should We Chat? Privacy in the WeChat Ecosystem"
    url: https://citizenlab.ca/2023/06/privacy-in-the-wechat-ecosystem-full-report/
    publisher: Citizen Lab
    date: 2023-06-28
authors:
  - anoni-net
---

研究監控與審查科技的 InterSecLab 在 9 月 24 日發表報告，分析俄羅斯政府規定預裝的通訊 App Max。報告寫明 Max 沒有端對端加密，營運方 VK 的伺服器可以讀取每則訊息，也沒有任何模式能讓內容不被營運方讀取。研究者分析的是 2026 年 3 到 5 月的 Android 版。預裝的規定只在俄羅斯實施。

報告列為最重要的發現，是網路探測、VPN 偵測、語音轉文字、加強記錄等功能都由 VK 的伺服器針對一個或一批帳號開啟。開啟時不需要更新 App，介面上也看不出來。網路探測開啟時，App 每次打開或切到背景，都會查詢裝置的公開 IP、檢查有沒有開 VPN、讀取電信業者，並測試一串網路服務能否連上。結果全部回報給 VK。

Max 偵測到裝置上有 VPN 就會停止運作，研究者回覆訊息時，畫面上只有關閉 VPN 的提示，沒有其他選項。Max 也會把整份通訊錄以明文上傳給 VK，語音訊息則在 VK 的伺服器上轉成文字。

俄羅斯政府 2025 年 8 月宣布，Max 從 9 月 1 日起列入電子裝置必須預裝的軟體。CNN 報導，俄羅斯在 2026 年 2 月證實封鎖 WhatsApp，並引導民眾改用 Max。

報告寫明，研究結果不代表 VK 或俄羅斯的政府機關已經對特定的人使用這些功能。研究者在 9 月 25 日更正報告網頁，撤回 PDF 裡關於「祕密聊天」的說法，因為 Max 沒有這項功能，沒有端對端加密的結論不受影響。

## 導讀觀點 {#perspective}

端對端加密的意義，在於連營運方都無法讀取內容。Max 沒有這一層，每則訊息 VK 都能讀取。Max 的功能還能由伺服器針對帳號開關，同一個 App 對不同的人可能做不同的事。使用者從介面上無從察覺，外界也只能靠逆向分析發現。

亞洲也有類似的架構，Citizen Lab 2023 年對微信的研究結論是，微信沒有端對端加密，騰訊能存取平台上所有訊息。中國大陸帳號的訊息還會被依關鍵字自動審查，Max 則多了一層政府規定的預裝。

不得不在俄羅斯使用 Max 的人，報告的建議是把 VPN 設在路由器上、把 Max 放在獨立的 Android 工作設定檔，或用另一支手機專門安裝政府要求的 App。報告也寫明，這些做法都無法保護訊息內容，因為 VK 以未加密的方式儲存訊息。

俄羅斯以外的讀者不需要做任何設定。面對任何被要求安裝的通訊 App，可以先問三件事：有沒有端對端加密、功能能不能從伺服器遠端開關、有沒有獨立的研究者檢驗過。敏感的對話，仍然要留給有端對端加密的工具。
