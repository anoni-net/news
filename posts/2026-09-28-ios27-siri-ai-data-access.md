---
title: iOS 27 Siri AI 的資料存取設定
description: iOS 27 的新版 Siri 預設可以讀取備忘錄、訊息與郵件，請求可能送到 Apple 的伺服器處理。EFF 整理了限制它能讀到哪些資料的設定。
date: 2026-09-28
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

Apple 在 iOS 27 推出新版 Siri（Siri AI），跟 Spotlight 合併成同一個介面，往下滑搜尋 App 時也等於在呼叫 Siri。支援的機型是 iPhone 15 Pro、15 Pro Max 與 iPhone 16 之後的機型。Siri AI 目前是測試版，只支援英文，也還沒有在所有地區開放，Siri 語言設成中文的使用者現在還用不到。

預設情況下，Siri AI 可以讀取備忘錄、訊息與郵件等 Apple 自家 App 的內容，第三方 App 要等開發者開放才會納入。請求可能在手機上處理，也可能送到 Apple 的 Private Cloud Compute 伺服器，畫面上沒有提示告訴使用者是哪一種。EFF 特別點名開啟進階資料保護的使用者，這些資料原本在 iCloud 上以端對端加密保存，送出裝置交給雲端處理，會改變原本的風險評估。

螢幕感知（on-screen awareness）功能會讀取畫面上正在顯示的內容，EFF 舉的例子是 Signal 的加密群組對話也能被摘要。這個功能目前使用者與 App 開發者都沒有辦法封鎖。

要限制 Siri AI 讀取某個 App，EFF 的步驟是在「設定」的 App 清單點進該 App，進入 Search，關閉 Show Content in Search。想完全回到舊版 Siri，在「螢幕使用時間」開啟「內容與隱私權限制」後，把 Siri 的 Allowed Siri Version 設成 Siri Classic。「隱私權與安全性」的 Analytics & Improvements 裡，可以關閉 Improve Siri & Dictation。原文以英文介面寫成，中文介面的選項名稱可能不同。

Apple 的說明頁列出 macOS 27 的做法，在「系統設定」關閉 Siri 後，可以改用 Siri Classic，訊息、郵件與通知的摘要也各自有開關。

## 技術觀點 {#technical-view}

EFF 在原文寫明，Private Cloud Compute 的 Private 是系統設計上讓 Apple 看不到也不保存資料，不代表資料有加密、不會離開裝置。它的保護來自伺服器端的工程設計，端對端加密則是只有使用者的裝置能解密，兩者的信任基礎不同。

使用者看不出哪一次請求離開了手機，想繼續使用 Siri AI 的話，逐一關閉 App 的搜尋權限是目前能掌握的控制方式。備忘錄、郵件這類放著工作資料或個人紀錄的 App，可以優先關閉。

螢幕感知無法封鎖，代表在 iPhone 上閱讀加密通訊時，端對端加密保護的範圍只到畫面為止。需要在手機上處理敏感對話的人，可以考慮切回 Siri Classic。

螢幕使用時間與各 App 的搜尋開關已經存在，可以趁 Siri AI 支援中文之前先檢查一遍。
