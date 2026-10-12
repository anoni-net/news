---
title: Firefox iOS 版的內建廣告封鎖與 Android 的系統層做法
description: iPhone 與 iPad 上的 Firefox 內建廣告封鎖，9 月中的 156 版版本說明首次列出。功能預設關閉，要自己到設定開啟。Android 版 Firefox 本來就能裝擴充套件。一篇個人部落格整理的 Android 系統層做法多半要信任提供服務的業者或 App。
date: 2026-10-13T00:05:00+08:00
slug: firefox-ios-ad-blocker
categories:
  - mobile
sources:
  - title: "Introducing Ad Blocker for Firefox on iOS: More control, fewer distractions"
    url: https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/
    publisher: Mozilla
    date: 2026-09-01
  - title: 156.0 Firefox for iOS Release
    url: https://www.firefox.com/en-US/firefox/ios/156.0/releasenotes/
    publisher: Mozilla
    date: 2026-09-15
  - title: System-level ad-blocking in Android in 2026
    url: https://kevinboone.me/adblock.html
    publisher: Kevin Boone
    date: 2026-10-01
  - title: 在 Android 手機上管理進階網路設定
    url: https://support.google.com/android/answer/9654714?hl=zh-Hant
    publisher: Google
  - title: Mozilla adds ad blocking to Firefox for iOS
    url: https://www.theregister.com/software/2026/08/17/mozilla-adds-ad-blocking-to-firefox-for-ios/5288585
    publisher: The Register
    date: 2026-08-17
  - title: Firefox 快速隱私瀏覽器
    url: https://apps.apple.com/tw/app/firefox-private-safe-browser/id989804926
    publisher: App Store
  - title: App Review Guidelines
    url: https://developer.apple.com/app-store/review/guidelines/
    publisher: Apple
    date: 2026-06-08
authors:
  - anoni-net
---

Mozilla 9 月 1 日公告，iPhone 與 iPad 上的 Firefox 內建廣告封鎖，預設關閉。使用者要自己到設定的瀏覽（Browsing）區開啟，原始碼裡的正體中文介面字串寫作「廣告封鎖」。版本說明在 9 月 15 日發布的 156 版首次列出這項功能。依外電轉述的 Mozilla 說法，功能是逐步開放的，到 10 月 12 日 App Store 上的最新版是 158.0。

公告寫明，廣告封鎖用 Apple 的 WebKit 內容封鎖技術與 EasyList 過濾清單，在許多第三方廣告與廣告相關的追蹤器載入之前擋掉。Mozilla 的說法是，iOS 上的擴充套件運作方式跟其他平台不同，所以直接把功能做進瀏覽器。公告也寫明廣告支撐許多網站，所以功能設計成可選用。網站自己直接放的廣告、搜尋結果裡的廣告與 Firefox 新分頁上的贊助捷徑，都不受這項功能影響。

電腦版與 Android 版的 Firefox 本來就能安裝廣告封鎖的擴充套件，這次的變更只影響 iOS 版。想在 Android 整支手機擋廣告的人，有另一套做法。10 月 1 日一篇個人部落格的作者整理了 2026 年在 Android 系統層封鎖廣告的四種做法，分別是封鎖型的 DNS（把網域名稱轉成 IP 位址的服務）服務、附廣告封鎖的 VPN 服務、不需要 root 的本機 VPN App，以及需要 root（取得手機系統的最高權限）改寫系統 hosts 檔的做法。就作者所知，這幾種都是改寫 DNS 的行為，把已知廣告商的主機名稱對應到假的 IP 位址。

## 導讀觀點 {#perspective}

兩邊都是在連線之前擋掉已知的廣告網址，差在作用的範圍。iOS 版的廣告封鎖只作用在 Firefox 開啟的網頁，用的是 WebKit 的內容封鎖技術，Apple 的審核指南也規定瀏覽網頁的 App 要使用 WebKit（歐盟與日本另有申請例外的辦法）。Android 的系統層做法作用在所有 App。依作者的說明，廣告內建在 App 裡、或 App 直接用 IP 位址連線（作者寫明目前還少見）時，改寫 DNS 就擋不住。

依本文的推論，前三種做法要信任提供服務的那一方，因為所有 App 查詢的網域都會經過它。作者提醒，惡意的 DNS 或 VPN 業者甚至可能把網路銀行的連線導到自己的代理伺服器，在意隱私的人可以挑不留紀錄、支援加密 DNS 的服務。本機 VPN App 會讓所有流量經過同一個 App，作者建議只用開源的。需要 root 的做法不必信任外部業者，作者寫的取捨是要自行檢查寫進 hosts 檔的內容。

用 iPhone 或 iPad 的讀者把 Firefox 更新到最新版，設定的瀏覽區應該就有廣告封鎖的開關，App Store 標示需要 iOS 15.0 以上。正體中文介面的說明寫明，使用後網站出現異常時，可以試著關閉。開啟之後，網站自己放的廣告、搜尋結果的廣告與新分頁的贊助內容仍會出現。

主要在意網頁廣告的 Android 使用者，作者認為最簡單的做法可能是改用支援廣告封鎖的瀏覽器，不必動到系統設定。想連 App 裡的廣告一起擋，可以在設定的「網路與網際網路」裡找到「私人 DNS」（不同廠牌的選單位置可能不同），填入封鎖型 DNS 服務的主機名稱。作者寫明這類服務價格不一，多數有免費試用。填了之後，所有 App 的網域查詢都會交給那家業者處理，要先確認它的紀錄保存政策。
