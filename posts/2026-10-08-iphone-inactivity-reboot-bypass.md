---
title: iPhone 自動重新啟動與鑑識工具的繞過宣稱
description: iOS 18.1 起，iPhone 長時間沒有解鎖會自動重新啟動，讓資料回到較難取出的狀態。一支約在 2025 年初製作的鑑識廠商影片裡，員工說扣押的手機即使重新啟動也能保留解鎖過一次的狀態。這項手法對最新版 iOS 是否有效，到 10 月 7 日為止並不清楚。Apple 沒有回覆報導的詢問，擔心手機被扣押取證的人可以留意後續。
date: 2026-10-08T00:10:00+08:00
slug: iphone-inactivity-reboot-bypass
categories:
  - mobile
sources:
  - title: Protecting user data in the face of attack
    url: https://support.apple.com/guide/security/protecting-user-data-in-the-face-of-attack-secf5549a4f5/web
    publisher: Apple
    date: 2026-01-28
  - title: 遭遇攻擊時保護使用者資料
    url: https://support.apple.com/zh-tw/guide/security/secf5549a4f5/web
    publisher: Apple
    date: 2026-01-28
  - title: Cops Can Bypass iPhone’s Automatic Reboot to Get Into Locked Phones, Leaked Video Claims
    url: https://www.404media.co/cops-can-bypass-iphone-automatic-inactivity-reboot-graykey/
    publisher: 404 Media
    date: 2026-10-01
  - title: Leaked Video Shows That Police Can Bypass iPhones' Automatic Reboot Feature
    url: https://www.privacyguides.org/news/2026/10/01/leaked-video-shows-that-police-can-bypass-iphones-automatic-reboot-feature/
    publisher: Privacy Guides
    date: 2026-10-01
  - title: GrayKey maker can reportedly bypass the iPhone’s ‘Inactivity Reboot’ security feature
    url: https://9to5mac.com/2026/10/01/graykey-maker-can-reportedly-bypass-the-iphones-inactivity-reboot-security-feature/
    publisher: 9to5Mac
    date: 2026-10-01
  - title: A forensic tool claims it can stop seized iPhones from locking down after 72 hours
    url: https://www.techspot.com/news/114070-new-graykey-feature-police-stop-seized-iphones-becoming.html
    publisher: TechSpot
    date: 2026-10-02
  - title: Access the critical iOS and Android evidence you need
    url: https://www.magnetforensics.com/products/magnet-graykey/
    publisher: Magnet Forensics
  - title: New Apple security feature reboots iPhones after 3 days, researchers confirm
    url: https://techcrunch.com/2024/11/14/new-apple-security-feature-reboots-iphones-after-3-days-researchers-confirm
    publisher: TechCrunch
    date: 2024-11-14
  - title: Reverse Engineering iOS 18 Inactivity Reboot
    url: https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html
    publisher: naehrdine
    date: 2024-11-17
  - title: 密碼
    url: https://support.apple.com/zh-tw/guide/security/sec20230a10d/web
    publisher: Apple
    date: 2024-12-19
  - title: 在 iPhone 上設定密碼
    url: https://support.apple.com/zh-tw/guide/iphone/iph14a867ae/ios
    publisher: Apple
  - title: Apple 安全性發布
    url: https://support.apple.com/zh-tw/100100
    publisher: Apple
authors:
  - anoni-net
watch:
  - date: 2026-11-08
    note: Apple 是否回應或在 iOS 更新說明修補，Magnet 的手法適用哪些 iOS 版本是否有獨立驗證
---

404 Media 在 10 月 1 日的報導寫到，他們取得了一支 Magnet Forensics 的影片，該公司的 Graykey 是賣給執法單位、用來解鎖手機並取出資料的工具。影片裡的 Magnet 員工說，Graykey Preserve 裝置與 Graykey 的 Evidence Preservation Mode 能讓扣押的 iPhone 停留在較容易取出資料的狀態，即使手機因各種原因重新啟動或斷電也一樣。404 Media 的報導把這項技術寫成用來繞過 iOS 18.1 起的「自動重新啟動」（英文報導多稱 Inactivity Reboot）。依 9to5Mac 引述 404 Media 的內容，這是專給執法人員的教學影片，看起來在 2025 年初製作。

TechSpot 在 10 月 2 日的報導寫明，這項宣稱尚未經過獨立驗證。9to5Mac 也寫到，這項技術提供給執法單位多久、是否用在實際案件，以及對最新版的 iOS 是否有效都不清楚。依 9to5Mac 與 Privacy Guides 的轉述，404 Media 向 Apple 與 Magnet 詢問，兩家都沒有回覆。到 10 月 7 日為止，本文查到的來源裡沒有 Apple 對這項宣稱的回應。

TechCrunch 2024 年 11 月的報導寫到兩種狀態的差別。手機開機之後還沒輸入過密碼的狀態稱為「首次解鎖前」（BFU）。依 TechCrunch 的說法，這時使用者資料完全加密，不知道密碼幾乎無法取出。輸入過一次密碼之後是「首次解鎖後」（AFU），即使手機鎖著也有部分資料沒有加密，某些鑑識工具可能比較容易取出。

Apple 的安全性指南寫明，iOS 18.1 與 iPadOS 18.1 起的「自動重新啟動」由「安全隔離區」（晶片裡專門處理密鑰的獨立子系統）監控裝置的解鎖事件，裝置長時間維持鎖定就會自動重新啟動。重新啟動會讓裝置從 AFU 轉為 BFU，並從記憶體清除敏感的密鑰與暫存資料。iOS 18.4 起，裝置管理者可以開關這項機制，受監管的裝置（公司或學校透過裝置管理統一設定的 iPhone）預設關閉。Apple 的文件沒有寫出要鎖定多久，研究者 2024 年 11 月的實測是 72 小時，TechCrunch 當時的報導也寫到 Magnet 確認了這個數字。

Privacy Guides 轉述影片的說法，Evidence Preservation Mode 會在 AFU 狀態「捕捉」iPhone，重新啟動之後 AFU 狀態也不會消失。依 TechSpot 的轉述，影片裡的員工說，Graykey 在取得初步存取、進入保存狀態之後會關閉手機的無線電（Wi-Fi、藍牙與行動網路）。員工也說 Graykey Preserve 能保留快取的位置資料、最近刪除的照片與 iMessage，這些資料原本會在一段時間後清除。依 Privacy Guides 的轉述，影片沒有說明技術細節。

Magnet 官網的 Graykey 產品頁到 10 月 7 日為止寫到，Graykey 能保護資料擷取不受自動重新啟動計時器影響。同一頁對 Graykey Preserve 的說明只提到 iOS。

## 導讀觀點 {#perspective}

2024 年的逆向分析寫到，竊賊沒有資源在三天內取得最新的破解手法，自動重新啟動很可能讓他們完全取不到資料。同一篇也寫到，執法單位因此多了時間壓力。Magnet 的說法如果屬實，取得初步存取並開始保存的手機，72 小時到期時 AFU 狀態也不會消失。

本文引用的來源都沒有寫到一般使用者能做什麼來擋下 Magnet 的手法。依 iPhone 使用手冊，開機或重新開機之後一律要輸入密碼。本文從 BFU 的定義推論，關機之後再開機的手機會處於 BFU，擔心手機被扣押取證的人因此可以在手機可能離開自己身邊之前關機。影片沒有說明 Magnet 的手法能不能用在已經是 BFU 的手機。

依影片的說法，保存開始之後即使斷電，AFU 狀態也不會消失。關機的代價是期間收不到電話與訊息，手機在使用中被拿走時也來不及關機。

Apple 的「密碼」說明寫到，攻擊者即使取得裝置，沒有密碼也無法存取特定保護類別的資料。同一份說明也寫到密碼越長越能抵擋暴力破解，較長的數字密碼與較短的英數密碼相比更便於輸入，也可提供類似的安全性。這份說明沒有談到密碼長度對 Magnet 手法的影響。

在「設定」的「Face ID 與密碼」（或「Touch ID 與密碼」）點「更改密碼」，再點「密碼選項」就能更換。iPhone 使用手冊把「自訂英數密碼」與「自訂數字密碼」列為最安全的選項。長密碼的代價是開機或重新開機之後，以及超過 48 小時沒有解鎖時，都要輸入較長的字串。

Magnet 宣稱的手法跟執法單位扣押手機之後的取證有關，沒有手機被扣押疑慮的人不必改變設定。依 Apple 的安全性指南，受監管的 iPhone 預設不啟用自動重新啟動，使用這類手機的人不能假設有 72 小時的保護。

Apple 的「Apple 安全性發布」頁面寫明，在調查並公開提供修補程式或版本之前，不會揭露、討論或確認安全性問題。到 10 月 7 日為止，Magnet 的手法對最新版 iOS 是否有效並不清楚。11 月可以回頭看 iOS 的更新說明有沒有相關修補，以及有沒有研究者獨立驗證。
