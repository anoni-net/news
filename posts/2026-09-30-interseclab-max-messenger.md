---
title: 俄羅斯國家通訊 App Max 的技術分析
description: InterSecLab 分析俄羅斯規定預裝的通訊 App Max，發現它沒有端對端加密。VPN 偵測、網路探測與語音轉文字都能從伺服器針對個別帳號切換，介面上沒有任何提示。預裝規定只在俄羅斯實施。
date: 2026-09-30T07:05:00+08:00
slug: interseclab-max-messenger
sources:
  - title: "The Max Messenger: An Analysis of Russia’s State-Mandated Messaging Application"
    url: https://interseclab.org/research/max/
    publisher: InterSecLab
    date: 2026-09-24
  - title: Правительство включит новые цифровые продукты в перечень программ для обязательной предустановки
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
watch:
  - date: 2026-10-30
    note: InterSecLab 報告頁是否已放上俄文譯本
  - date: 2026-10-30
    note: 報告是否發布 1.1 之後的新版，修正伺服器端設定何時生效的描述，內文要不要跟著更正
regions:
  - RU
authors:
  - anoni-net
---

數位安全實驗室 InterSecLab 在 9 月 24 日發表報告，分析俄羅斯政府規定預裝的通訊 App Max。報告寫明 Max 沒有端對端加密，開發 Max 的俄羅斯網路公司 VK 可以在伺服器上讀取每則訊息。研究者在 2026 年 3 到 5 月間分析 Android 版 `26.12.0`，結果只代表這一個版本。預裝規定只適用於在俄羅斯販售的手機與平板，俄羅斯以外的讀者不受影響。

俄羅斯政府 2025 年 8 月宣布，Max 從 2025 年 9 月 1 日起列入電子裝置必須預裝的軟體。CNN 報導，俄羅斯在 2026 年 2 月證實封鎖 WhatsApp，並引導民眾改用 Max。報告也寫明，使用政府服務愈來愈常需要 Max。

報告最重要的發現是，VK 的伺服器可以針對一個或一批帳號，切換網路探測、VPN 偵測、語音轉文字等功能。切換時不需要更新 App，介面上也沒有提示。網路探測開啟後，App 每次啟動或切換到背景都會查詢裝置的公開 IP、檢查是否啟用 VPN、讀取電信業者，再回報給 VK。

Max 偵測到 VPN 就停止運作。研究者嘗試回覆訊息時，畫面只剩關閉 VPN 的指示。偵測只檢查裝置本身，路由器上的 VPN 不會被發現。

Max 也會把整份通訊錄以明文上傳給 VK。語音訊息則在 VK 的伺服器上轉成文字，不在手機上處理。

研究者 9 月 25 日在報告網頁刊出更正，Max 的介面上沒有「祕密聊天」這項功能，1.1 版 PDF 已在 9 月 28 日改寫相關段落。沒有端對端加密的結論不受影響，依據是在 App 內攔截到的明文訊息。

## 導讀觀點 {#perspective}

端對端加密讓營運方也無法讀取訊息內容，Max 沒有這項保護。Max 的功能又能由伺服器針對帳號切換，同一版 App 在不同帳號上的行為可能不同。研究者只能看到測試帳號收到的設定，也沒有蒐集到 VK 或任何俄羅斯國家機關對特定的人使用這些功能的證據。

多倫多大學的研究室 Citizen Lab 在 2023 年的微信報告寫明，微信的聊天訊息沒有端對端加密，騰訊能看到所有訊息。中國大陸帳號的訊息會被依關鍵字自動審查。根據同一份報告引述的研究，中國大陸以外帳號的訊息也被用來訓練審查演算法。Max 除了架構相近，還有政府規定的預裝。

報告的建議是不要用 Max 傳送敏感內容，裝了 Max 的人應假設內容都能被 VK 讀取。報告也列出不得不使用 Max 時的三種做法，把 VPN 設在路由器上、把 Max 放在獨立的 Android 設定檔，或用另一支手機安裝政府要求的 App。三種做法能讓規避封鎖的工具繼續運作，但 VK 儲存的訊息未經加密，內容仍無保護。

俄羅斯以外的讀者不需要做任何設定。可以留意的後續有報告的俄文譯本，以及下一版報告對伺服器端設定何時生效的修正。
