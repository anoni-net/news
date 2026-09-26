---
title: iOS 27 Siri AI 的資料存取設定
description: iOS 27 的新版 Siri 預設可以讀取備忘錄、訊息與郵件，請求可能送到 Apple 的伺服器處理。EFF 整理了限制讀取範圍的設定。
date: 2026-09-27T03:21:00+08:00
slug: ios27-siri-ai-data-access
sources:
  - title: How to Limit What Apple's New Siri AI Can Access in iOS 27
    url: https://www.eff.org/deeplinks/2026/09/how-limit-what-apples-new-siri-ai-can-access-ios-27
    publisher: EFF
    date: 2026-09-18
  - title: Turn off and restrict access to Apple Intelligence features on Mac
    url: https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac
    publisher: Apple
authors:
  - anoni-net
---

Apple 在 iOS 27 推出新版 Siri（Siri AI），跟 Spotlight 合併成同一個介面，在主畫面往下滑開啟搜尋時，叫出的也是 Siri。只有 iPhone 15 Pro、15 Pro Max 與 iPhone 16 之後的機型能使用。Siri AI 目前是測試版，只支援英文，也還沒有在所有地區開放，Siri 語言設為中文的使用者暫時無法使用。

Siri AI 預設可以讀取備忘錄、訊息與郵件等 Apple 自家 App 的內容，第三方 App 需要開發者加入支援才會納入。請求可能在手機上處理，也可能送到 Apple 的 Private Cloud Compute 伺服器，畫面上不會顯示是哪一種。EFF 特別提醒開啟進階資料保護的使用者，他們的 iCloud 資料以端對端加密保存，一旦送出裝置交給雲端處理，風險評估就跟著改變。

螢幕感知（on-screen awareness）讓使用者隨時叫出 Siri，請它解釋畫面上的內容。EFF 舉的例子是請 Siri 摘要正在看的 Signal 加密群組對話，此時畫面上的資料可能送到 Private Cloud Compute。使用者與 App 開發者目前都無法封鎖螢幕感知。

要限制 Siri AI 讀取某個 App，EFF 建議在「設定」的 App 清單點進該 App，於 Search 關閉 Show Content in Search。要改回舊版 Siri，可以在「螢幕使用時間」開啟「內容與隱私權限制」，再把 Siri 的 Allowed Siri Version 設為 Siri Classic。Siri AI 預設不會用互動紀錄訓練模型，設定過程中如果點了同意，可以到「隱私權與安全性」的 Analytics & Improvements 關閉 Improve Siri & Dictation 撤回。以上選項名稱照原文的英文介面，中文介面的名稱可能不同。

Mac 的做法寫在 Apple 的說明頁。macOS 27 在「系統設定」關閉 Siri 之後可以改用 Siri Classic，訊息、郵件與通知的摘要功能也各有開關。

## 導讀觀點 {#perspective}

EFF 在原文寫明，Private Cloud Compute 的「Private」代表系統的設計讓 Apple 無法看到、也不保存資料，但不保證資料經過加密或留在裝置上。使用 Private Cloud Compute 要信任 Apple 的伺服器照設計運作，端對端加密則只需要金鑰留在使用者自己的裝置上。

使用者無從得知哪一次請求離開了手機，想繼續使用 Siri AI，就只能從源頭限制它能讀取哪些 App。開啟了進階資料保護的人，可以優先關閉存有工作資料或個人紀錄的 App，例如備忘錄與郵件。各 App 的搜尋設定現在就能調整，不必等 Siri AI 支援中文。

螢幕感知無法封鎖，加密對話能不能留在裝置上，取決於對話裡的每一個人。群組中只要有人對著對話叫出 Siri，內容就可能從那個人的手機送出，端對端加密無法保護這一段。在群組裡討論敏感事務的人，可以跟成員約定不對對話使用螢幕感知，自己也可以考慮改回 Siri Classic。
