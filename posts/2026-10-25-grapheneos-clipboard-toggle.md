---
title: GrapheneOS 的剪貼簿讀取開關
description: 官方只支援 Pixel 的隱私強化手機系統 GrapheneOS，9 月 18 日公告的版本加入 Secure Paste，可以逐一設定哪些 App 不能讀取其他 App 複製的內容。到 10 月 23 日功能預設沒有開啟，要自己到設定調整，GrapheneOS 自己新增的設定也只有英文。一般 Android 手機在 App 讀取剪貼簿之後才通知，iPhone 則在 App 用程式讀取前請使用者同意。複製密碼之後讓密碼管理器自動清除剪貼簿，是兩邊都能做的一步。
date: 2026-10-25T00:05:00+08:00
slug: grapheneos-clipboard-toggle
categories:
  - mobile
sources:
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases#2026091700
    publisher: GrapheneOS
  - title: GrapheneOS version 2026091700 released
    url: https://discuss.grapheneos.org/d/42090-grapheneos-version-2026091700-released
    publisher: GrapheneOS Discussion Forum
    date: 2026-09-18
  - title: Features overview | GrapheneOS
    url: https://grapheneos.org/features#secure-paste
    publisher: GrapheneOS
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#supported-devices
    publisher: GrapheneOS
  - title: Web installer | Install | GrapheneOS
    url: https://grapheneos.org/install/web
    publisher: GrapheneOS
  - title: "GrapheneOS: \"It's an opt-in feature wit…\" - GrapheneOS Mastodon"
    url: https://grapheneos.social/@GrapheneOS/117292361749585692
    publisher: GrapheneOS
    date: 2026-09-18
  - title: platform_packages_apps_Settings/res/values/strings_ext.xml
    url: https://github.com/GrapheneOS/platform_packages_apps_Settings/blob/2026102100/res/values/strings_ext.xml
    publisher: GitHub
  - title: platform_frameworks_base/core/res/res/values/config_ext.xml
    url: https://github.com/GrapheneOS/platform_frameworks_base/blob/2026102100/core/res/res/values/config_ext.xml
    publisher: GitHub
  - title: GrapheneOS translate to other languages - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/5030-grapheneos-translate-to-other-languages
    publisher: GrapheneOS Discussion Forum
  - title: Privacy changes in Android 10
    url: https://developer.android.com/about/versions/10/privacy/changes
    publisher: Android Developers
  - title: "Behavior changes: all apps"
    url: https://developer.android.com/about/versions/12/behavior-changes-all
    publisher: Android Developers
  - title: Features and APIs Overview
    url: https://developer.android.com/about/versions/13/features
    publisher: Android Developers
  - title: UIPasteControl
    url: https://developer.apple.com/documentation/uikit/uipastecontrol
    publisher: Apple Developer Documentation
  - title: iOS 16.1 Introduces New Copy-and-Paste Permission Settings on Per-App Basis
    url: https://www.macrumors.com/2022/10/17/ios-16-1-paste-from-other-apps-settings/
    publisher: MacRumors
    date: 2022-10-17
  - title: Protecting Android clipboard content from unintended exposure
    url: https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/
    publisher: Microsoft Security Blog
    date: 2023-03-06
  - title: Copy and fill passwords into apps that don't work with 1Password
    url: https://support.1password.com/copy-passwords/
    publisher: 1Password Support
    date: 2026-08-17
watch:
  - date: 2026-12-15
    note: GrapheneOS 是否調整 Secure Paste 的預設值、是否把設定畫面翻譯成其他語言，Android 或 iOS 是否推出類似的逐 App 控制
authors:
  - anoni-net
---

GrapheneOS 是以 Android 開源程式碼為基礎的隱私強化手機系統，到 10 月 23 日官方支援的機型是 Pixel 6 到 Pixel 10a。9 月 18 日官方論壇公告的 2026091700 版，加入名為 Secure Paste 的剪貼簿控制。依發布紀錄，使用者可以逐一關閉 App 讀取剪貼簿的權限，也可以用全域開關把所有第三方 App 預設為關閉。關閉之後，使用者仍可以透過系統的選取工具列、鍵盤、鍵盤快捷鍵或無障礙服務，把內容貼進這些 App。

依 GrapheneOS 的功能介紹頁，Android 只允許目前取得焦點、正在操作的 App 與鍵盤讀取剪貼簿。App 讀到其他 App 複製的內容時 Android 會顯示通知，但通知出現時內容已經被讀走了。開啟 Secure Paste 之後，App 讀不到其他 App 複製的內容，仍可讀取自己複製的內容。

Secure Paste 預設不阻擋讀取，GrapheneOS 在 Mastodon 的回覆說明這是要自己開啟的功能，設定程式碼的預設值也是允許讀取。依設定程式碼，開關在「Settings > Security & privacy > Privacy controls > Clipboard access」，官方的使用說明沒有寫路徑。全域預設的選項是「Allow」與「Blocked」，每個 App 另外可以選「Allow」、「Paste only」，或用「Follow system clipboard access setting」跟著全域預設。設定程式碼的說明文字也提醒，改成 Paste only 可能讓某些 App 無法正常運作。

之後的 2026091900 版把擋下讀取時的通知間隔從 1 分鐘縮短為 6 秒，這則通知可以逐 App 關閉。2026092500 版改善了設定畫面，到 10 月 21 日的 2026102100 版，發布紀錄沒有再列出剪貼簿相關的條目。

依設定程式碼的說明文字，全域開關不套用到系統 App。目前使用的鍵盤以及部分 App 與系統功能，一律可以讀取剪貼簿。

App 仍可看到剪貼簿有沒有內容、內容類型與複製時間，能檢視並操作畫面內容的無障礙服務也可以觸發貼上，並可能取得貼上的內容。依功能介紹頁，設成 Paste only 之後，要貼到自行實作選取工具列的 App（例如用 Flutter 這套跨平台開發框架寫的 App）需改用鍵盤上的貼上按鈕。依官方論壇的回覆，GrapheneOS 在預設鍵盤加了這個按鈕，Gboard 原本就有。使用其他鍵盤的人要先確認有沒有貼上功能。

## 導讀觀點 {#perspective}

依 Microsoft 2023 年的資安部落格，手機使用者常用剪貼簿複製密碼、付款資訊這類敏感內容。Android 的 App 讀寫剪貼簿不需要使用者同意，也不需要特定權限。

Microsoft 在同一篇文章公布調查結果，一款購物 App 的舊版本會定期讀取剪貼簿，內容符合特定格式就傳回伺服器。文中也提到並未得知特定的惡意意圖，該行為在 2022 年 5 月已移除。Android 10 起背景 App 不能讀剪貼簿，但這項限制擋不住前景的 App。

依 Android 開發者文件，Android 12 起 App 第一次讀取其他 App 複製的內容時，系統會顯示通知。Android 13 另外在複製時顯示預覽，用來確認複製成功。依 Apple 的開發者文件，iOS 16 起 App 用程式讀取剪貼簿時，系統會先請使用者同意。MacRumors 2022 年的報導提到，iOS 16.1 起要求過貼上的 App 在設定裡多了「Paste from Other Apps」選項，本文沒有在現行 iOS 核對。

本文建議用 GrapheneOS 的讀者先挑幾個 App 改成 Paste only，再視情況把全域預設改成 Blocked，貼上時改用工具列或鍵盤（先確認自己的鍵盤有貼上鍵）。設定程式碼的提醒與官方列出的限制都顯示，一次全部擋下比較容易遇到無法正常運作的 App。改了之後某個 App 無法正常運作，可以把那個 App 改回 Allow。

依 GrapheneOS 的功能介紹頁，Secure Paste 取代了桌機與手機系統的標準做法，一般 Android 手機沒有逐 App 的開關。iPhone 則是 App 用程式讀取時會先詢問，兩邊都可以先調整密碼管理器，1Password 的說明頁寫各平台複製出去的密碼預設 90 秒後自動清除。本文建議用其他密碼管理器的人，在設定裡找清除剪貼簿的選項。定時清除只縮短內容留在剪貼簿的時間，清除之前取得焦點的 App 仍可讀取。

想安裝 GrapheneOS 的人要先有一支支援的 Pixel，官方 FAQ 提醒電信業者鎖定的機型無法安裝，主要發生在美國的電信業者。依官方網頁安裝器的說明，執行安裝器的裝置要有至少 2GB 可用記憶體與 32GB 可用空間，電腦或 Android 手機、平板都可以。依 10 月 23 日查到的設定程式碼目錄推斷，GrapheneOS 自己新增的設定與 App 只有英文，系統其他部分沿用 Android 的正體中文。

已經在用 GrapheneOS 的人改成 Paste only 之後，擋下的是 App 自行讀取，擋不到已開啟的無障礙服務與目前使用的鍵盤。代價是部分 App 要改用鍵盤的貼上鍵。
