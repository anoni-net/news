---
title: iOS 27.2 的 Siri AI 排除 App 設定
description: iOS 27.2 在「設定」的 Siri 加入 Excluded Apps，可以選定不讓 Siri、搜尋與建議讀取的 App。依 EFF 的文章，被排除的 App 連螢幕感知也不運作。iPhone 與 iPad 版的 Siri AI 在歐盟與中國大陸沒有提供，到 11 月 2 日支援的語言也不含中文，裝置與 Siri 語言設為中文的人暫時用不到 Siri AI。
date: 2026-11-03T00:00:00+08:00
slug: siri-ai-exclude-apps
categories:
  - tracking
follows:
  - 2026-09-27-ios27-siri-ai-data-access
watch:
  - date: 2026-12-03
    note: Siri AI 是否加入中文，How to get Siri AI 說明頁與各地功能可用性頁的語言是否跟上 27.2 的版本說明，Google 是否讓 Gemini 的螢幕情境可以依 App 關閉
sources:
  - title: About iOS 27 Updates
    url: https://support.apple.com/en-us/149076
    publisher: Apple
    date: 2026-10-26
  - title: "Victory! You Can Now Exclude Apps from Siri AI"
    url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
    publisher: EFF
    date: 2026-10-28
  - title: About iPadOS 27 Updates
    url: https://support.apple.com/en-us/149075
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-10-22
  - title: Siri AI, a profoundly more capable and personal assistant, is here
    url: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/
    publisher: Apple
    date: 2026-09-14
authors:
  - anoni-net
---

依 Apple 10 月 26 日發布的版本說明，iOS 27.2 加入 Excluded Apps，使用者可以在「設定」的 Siri 裡選擇 Siri、搜尋與建議能讀取哪些 App。Siri AI 是 iOS 27 推出的新版 Siri，可以讀取 App 的內容回答問題，適用 iPhone 15 Pro、15 Pro Max 與 iPhone 16 之後的機型。Excluded Apps 列在版本說明的 Siri AI 小節，iPadOS 27.2 的版本說明也列了同一項。iPhone 與 iPad 版的 Siri AI 在歐盟與中國大陸沒有提供，支援的語言到 11 月 2 日也不含中文，裝置與 Siri 語言設為中文的人暫時無法使用 Siri AI。

同一份版本說明寫到，Siri AI 在 27.2 增加法文、日文、韓文、葡萄牙文與西班牙文，加上原本的英文共六種。Apple 10 月 22 日發布的「How to get Siri AI」說明頁，到 11 月 2 日仍寫目前只支援英文，本文以較晚發布的版本說明為準。依 Apple 9 月的新聞稿，Apple Intelligence 的其他功能支援正體與簡體中文，Siri AI 另有自己的語言清單。

EFF 10 月 28 日的文章寫到，Excluded Apps 回應了 EFF 在 2026 年稍早「Encrypt It Already」倡議提出的一項要求。文章提到的顧慮是許多 AI 功能需要雲端處理，即使系統設計了隱私保護，加密通訊 App 的內容仍可能在使用者不知情時離開裝置。EFF 當初要求讓使用者能指定作業系統的 AI 不讀取某個 App，即使因此少掉一些功能，設定也要簡單易懂。

依 EFF 的說明，更新到 27.2 之後在「設定」的 Siri 點進 Excluded Apps，再點 Add Apps 選擇要排除的 App。排除之後 Siri AI 無法讀取該 App 的內容，也可能少掉部分功能。EFF 舉的例子是排除訊息 App 之後，就不能請 Siri AI 朗讀或回覆訊息。螢幕感知（叫出 Siri 詢問眼前畫面內容的功能）對排除的 App 也不再運作，排除 Signal 之後，無法請 Siri 辨識 Signal 畫面上的任何資訊。

EFF 提到 Siri AI 剛推出時，要封鎖它讀取某個 App 需要切換好幾個選項，不然就只能整個關掉 Siri AI。本站 9 月 27 日的導讀依 EFF 當時的文章，寫到使用者與 App 開發者都無法封鎖螢幕感知，限制讀取的做法是逐一在各 App 關閉 Show Content in Search。27.2 的排除清單集中在一處，也涵蓋螢幕感知，EFF 認為少掉功能正好代表設定生效。

文章也檢查了 Android 的現況。依 EFF 的說明，在 Gemini App 點使用者照片後進入 Settings > Personal Intelligence > Connected Apps，可以撤銷不想讓 Gemini 讀取的 App。EFF 肯定這份清單採選擇加入（opt-in），但認為流程不夠直覺。Signal 完全不支援 Gemini 的 App 存取功能，所以不在清單上，Gemini 也無法直接讀取 Signal 的內容。

不過 EFF 也寫到，開啟 Connected Apps 裡的 Device Assistance 之後，Gemini 可以讀取通知。設定計時器等基本功能也需要 Device Assistance，EFF 推測多數人都已經開啟。

螢幕情境（screen context）在 Gemini 設定裡的選項是 Use screen and app data，位置在 Device controls > Screen context，關閉之後才會停用。Use screen and app data 無法依 App 個別設定。依 EFF 的說明，使用者選擇使用讀取通知與螢幕情境時，兩者都可能讀取 Signal 的內容或通知。EFF 希望 Google 讓使用者可以依 App 關閉這兩項功能。

## 導讀觀點 {#perspective}

本站 9 月的導讀提到，Siri AI 的請求可能在手機上處理，也可能送到 Private Cloud Compute（Apple 自己營運、處理 AI 請求的雲端伺服器）。畫面上不會顯示是哪一種，9 月的導讀因此推論，想繼續使用 Siri AI 的人只能從源頭限制它讀取哪些 App。依 EFF 的說明，Siri AI 無法讀取被排除的 App 內容，本文據此推論這些內容也不會隨請求送出裝置。EFF 認為 Apple 應該再進一步，提供只用裝置端 AI 功能的選項，類似 Samsung 在 Galaxy AI 提供的做法。

iOS 27.2 的版本說明也列出 Siri AI 可以取用更多來源，包括訊息裡附的相片、行事曆活動的參加者、語音留言、Safari 的瀏覽紀錄與閱讀列表，Siri AI 也能記得過去的對話。依版本說明，已經在用 Siri AI 的人更新之後，Siri AI 能取用的來源比更新前多。

Apple 的版本說明沒有寫排除之後 Siri 還能做什麼，只寫這項設定管的是 Siri、搜尋與建議。依這句推想，被排除的 App 內容可能也不會出現在搜尋與建議裡，這是本文的推論。

Android 這一端，EFF 的文章把 Gemini 的 App 清單與 iOS 的排除清單放在一起比較，認為 Android 的流程不如 Apple 的新設定直接。依 EFF 的說明，用 Android 手機與 Gemini 的人可以檢查 Connected Apps 裡的 Device Assistance 與 Use screen and app data 兩處，兩者都只能整項關閉。關閉 Device Assistance 也會一併少掉計時器這類基本功能。

裝置與 Siri 語言設為中文的人暫時用不到 Siri AI。沒有開啟 Siri AI 的人在「設定」裡是否看得到 Excluded Apps、設定之後會不會影響搜尋與建議，到 11 月 2 日 Apple 的說明頁都沒有寫。

已經開啟 Siri AI 的人更新到 iOS 27.2 之後，可以到「設定」的 Siri 點 Excluded Apps 加入要排除的 App（選項名稱照 EFF 文章的英文介面）。依 EFF 的說明，偏好舊版的人目前仍可以關閉 Siri AI、改回 Siri Classic。排除清單只管自己的手機，本文推論群組裡其他成員沒有排除同一個 App、又對同一段對話叫出 Siri AI 時，內容仍可能從對方的手機送出。
