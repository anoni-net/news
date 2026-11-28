---
title: Signal 對作業系統 AI 助理的截圖封鎖與限制
description: Signal 在 iOS 與 Android 版限制作業系統內建的 AI 助理擷取對話，Mac 版沒有這項保護，Mac 使用者要自行在 Siri 設定排除 Signal。到 11 月 29 日，Siri AI 不支援中文，Gemini 自動讀取畫面的螢幕情境限用英文。對話另一端的人開了這些功能時，自己的訊息一樣可能被讀取。
date: 2026-11-30T00:00:00+08:00
slug: signal-ai-agent-screenshots
categories:
  - encryption
follows:
  - 2026-11-03-siri-ai-exclude-apps
watch:
  - date: 2026-12-30
    note: Signal 是否在支援中心說明 Block Siri AI 與 Android 自動開啟 Screen security，Apple 與 Google 是否提供開發者讓 App 退出 AI 讀取的方式，macOS 是否有可以擋截圖的 API，Gemini 的螢幕情境能否依 App 關閉，Siri AI 是否加入中文
sources:
  - title: Signal is Serious About Protecting Your Privacy
    url: https://signal.org/blog/protecting-your-privacy/
    publisher: Signal
    date: 2026-11-20
  - title: By Default, Signal Doesn't Recall
    url: https://signal.org/blog/signal-doesnt-recall/
    publisher: Signal
    date: 2025-05-21
  - title: "Add 'Block Siri AI' setting to Settings > Privacy"
    url: https://github.com/signalapp/Signal-iOS/commit/9256c9583
    publisher: Signal-iOS（GitHub）
    date: 2026-11-02
  - title: AssistantScreenSecurityObserver.kt
    url: https://github.com/signalapp/Signal-Android/blob/main/app/src/main/java/org/thoughtcrime/securesms/components/AssistantScreenSecurityObserver.kt
    publisher: Signal-Android（GitHub）
  - title: Signal Moves to Block AI Agents
    url: https://www.eff.org/deeplinks/2026/11/signal-now-blocks-ai-agents
    publisher: EFF
    date: 2026-11-24
  - title: "Victory! You Can Now Exclude Apps from Siri AI"
    url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
    publisher: EFF
    date: 2026-10-28
  - title: About iOS 27 Updates
    url: https://support.apple.com/en-us/149076
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-11-12
  - title: Use screen actions to chat with the Gemini mobile app
    url: https://support.google.com/gemini/answer/15850607?hl=en
    publisher: Google
  - title: Signal blocks screenshots by Apple, Google operating systems to protect data from AI agents
    url: https://therecord.media/signal-no-screenshots-by-apple-google-operating-systems
    publisher: The Record
    date: 2026-11-23
authors:
  - anoni-net
---

Signal 宣布在 iPhone 與 Android 版限制作業系統內建的 AI 代理（能替使用者讀取畫面、操作 App 的 AI 助理）擷取對話，Mac 版沒有這項保護。到 11 月 29 日，Apple 的 Siri AI（iOS 27 推出的新版 Siri）不支援中文，Google 的 Gemini 自動讀取畫面的螢幕情境也限用英文。以中文使用手機的人多半還沒開這些功能。依 Signal 的部落格，資料被擷取之後受影響的是對話裡的所有人，包含另一端開了這些功能的人。

作業系統的 AI 代理靠掃描螢幕取得資訊，Signal 11 月 20 日的部落格提到 Google 與 Apple 把 Gemini 與 Siri AI 這類代理功能深度整合進作業系統，Signal 的對話因此被擷取。依 Signal 的說法，擷取的內容會存進代理當下使用的本機資料庫或遠端伺服器，之後就不在 Signal 的控制範圍內。Signal 在 2025 年 5 月處理過類似的問題，當時在 Windows 11 預設開啟 Screen security（讓 Signal 畫面無法被截圖的設定），擋下 Microsoft Recall。

iPhone 上的 Signal 在 iOS 27 直接擋下截圖，App 內與 App Switcher（切換 App 時顯示的縮圖畫面）都包括在內。設定叫 Block Siri AI（封鎖 Siri AI），位在 Signal 的隱私設定裡，名稱出自 Signal-iOS 的原始碼。想截圖的人可以關掉這項設定，EFF 11 月 24 日的文章寫明它預設開啟。

Android 版在偵測到 AI 助理要求讀取畫面時才自動打開 Screen security，之後 Signal 裡的畫面都不能截圖，直到使用者關掉。Signal 的部落格提到，在 Pixel 以外許多廠商的 Android 上，Signal 停用截圖之後就無法可靠地得知使用者試過截圖。直接停用截圖會讓截圖無聲失效、讓使用者困惑，所以 Signal 改成偵測 AI 助理。自動打開時會跳出提示讓使用者再關閉，Signal-Android 的原始碼寫明關閉之後 90 天內不會再提示。

Signal 在部落格要求作業系統廠商提供開發者簡單、有文件的方式，讓 App 退出 AI 的讀取與處理。The Record 的報導寫到，Apple 沒有立即回應，Microsoft 與 Google 拒絕評論。

## 導讀觀點 {#perspective}

端對端加密保護的是訊息在傳輸途中與伺服器上的內容，只有對話雙方的裝置能解開。訊息顯示在螢幕上時已經解密，作業系統能取得的畫面內容跟使用者看到的相同，所以內建的 AI 讀取畫面不需要破解任何加密。Signal 的部落格把這件事寫成作業系統的 AI 功能削弱了 Signal 獨立保證隱私的能力。

擋下截圖無法涵蓋其他可能的途徑，例如 AI 代理可能透過檔案系統讀取裝置上已有的內容，Signal 在部落格裡也稱這次補救不完整。依 Signal 的說明，Mac 版沒有封鎖 Siri AI 是因為找不到可靠擋下截圖的 API（應用程式介面）。多數代理正是用截圖讀取 App 的資料，macOS 卻只對持續的螢幕錄製有防護。Signal 給 Mac 使用者的建議因此改從系統設定著手。

群組裡有成員關掉保護、使用 Mac，或用的是無法偵測到 AI 助理的 Android 機型時，對話內容仍可能從那個人的裝置被 AI 讀取。Signal 的部落格提到，關掉保護可能讓自己與聯絡人的 Signal 內容都暴露給 AI 代理。

作業系統的設定只跟開了 Siri AI 或 Gemini 螢幕情境的人有關，Signal 的設定則每個用 Signal 的人都該看一次。更新 App 之後，iPhone 使用者可以到 Signal 的隱私設定確認 Block Siri AI 是否開啟，Android 使用者看到提示時可以選擇保留 Screen security。Signal-Android 的原始碼顯示偵測到助理時打開的就是同一個 Screen security，所以不必等提示就能自行打開，代價是 Signal 裡無法截圖。

Apple 這一側已有使用者能調整的設定，iOS 27.2 在「設定」的 Siri 加入 Excluded Apps（排除的 App 清單），可以選定不讓 Siri、搜尋與建議讀取的 App。macOS 27 的「系統設定」也有同一項，Signal 給 Mac 使用者的唯一建議就是把 Signal 加入清單，防止 Siri AI 主動讀取訊息內容。依 EFF 10 月的文章，排除 Signal 之後，連呼叫 Siri 詢問 Signal 畫面上的內容也得不到回答。Signal 的 Block Siri AI 是讓 Signal 裡無法截圖，屬於另一種機制，iPhone 使用者可以兩項都開。

Android 上用 Gemini 的人可以關閉自動讀取畫面的螢幕情境，位置在 Gemini 設定的 Screen context，分成 Use text from screen（使用畫面上的文字）與 Use screenshot（使用截圖）兩項。Google 的說明頁沒有依 App 個別設定的選項，EFF 10 月的文章也寫明沒有，到 11 月 29 日只能對所有 App 一起關閉。手動點「Ask about…」詢問畫面內容的功能不受這兩項影響。
