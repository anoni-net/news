---
title: Brave 的電子郵件別名
description: Brave 桌面版從 1.94 起提供電子郵件別名，註冊網站時用轉寄信箱取代真實信箱。每人免費 5 個，要先建立 Brave 帳號。到 10 月 12 日為止手機版還沒有，別名能否回信官方沒有寫。
date: 2026-10-14T00:05:00+08:00
slug: brave-email-aliases
categories:
  - tracking
sources:
  - title: Brave launches Email Aliases to keep your personal email address private from websites
    url: https://brave.com/privacy-updates/39-email-aliases/
    publisher: Brave
    date: 2026-08-27
  - title: "Brave Accounts: your password never leaves your device, ever."
    url: https://brave.com/blog/brave-accounts/
    publisher: Brave
    date: 2026-08-27
  - title: What is a Brave Email Alias?
    url: https://support.brave.app/hc/en-us/articles/45530506862349-What-is-a-Brave-Email-Alias
    publisher: Brave
    date: 2026-08-28
  - title: Brave Browser Privacy Policy
    url: https://brave.com/privacy/browser/
    publisher: Brave
    date: 2026-09-23
  - title: "[Email Aliases] Bubble UI for mobiles"
    url: https://github.com/brave/brave-browser/issues/50818
    publisher: GitHub
    date: 2025-11-13
  - title: Brave Release Notes
    url: https://brave.com/latest/
    publisher: Brave
  - title: brave_components_resources_zh-TW.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-TW.xtb
    publisher: GitHub
  - title: Block bravealias.com disposable email domain
    url: https://github.com/disposable/disposable/issues/288
    publisher: GitHub
    date: 2026-08-29
  - title: 如何在 iPhone 或 iPad 上使用 iCloud+ 的「隱藏電子郵件地址」
    url: https://support.apple.com/zh-tw/102548
    publisher: Apple
    date: 2025-09-30
  - title: Firefox Relay
    url: https://relay.firefox.com/
    publisher: Mozilla
  - title: SimpleLogin Pricing
    url: https://simplelogin.io/pricing/
    publisher: SimpleLogin
watch:
  - date: 2026-12-15
    note: Brave 電子郵件別名是否推出 Android 與 iOS 版、免費額度是否提高、Premium 版的價格
authors:
  - anoni-net
---

Brave 8 月 27 日推出電子郵件別名（Email Aliases），桌面版從 1.94 起可以在註冊網站時改用轉寄信箱，不交出真實信箱。每人免費 5 個，要先建立 Brave 帳號，這個帳號跟訂閱 Brave VPN 等服務的 Premium 帳號分開。到 10 月 12 日為止，Android 與 iOS 版的版本紀錄都還沒有這項功能，說明頁只有英文與日文。

在網站的信箱欄位會出現建立別名的提示，沒出現時可以在欄位上按右鍵選「New Email Alias」，寄到別名的信會轉寄到 Brave 帳號登記的信箱。依 Brave 的發布頁與隱私政策，Brave 不讀信件內容，只做一般的垃圾信與病毒過濾。轉寄成功後信件數秒內從伺服器刪除，主信箱暫時收不到時最多重試 24 小時，轉寄服務用的是 Amazon Web Services。發布頁也提醒，初期部分轉寄信可能會被分到垃圾信匣。

同一天推出的 Brave 帳號用 OPAQUE 協定登入，這種協定讓伺服器不必持有密碼也能驗證使用者，2025 年 7 月發布為 RFC 9807。Brave 帳號的部落格文章提到密碼本身不會送到 Brave 的伺服器。同一篇文章也提醒，OPAQUE 本身擋不了釣魚網站，也不會讓弱密碼變強。

## 導讀觀點 {#perspective}

Brave 的發布頁把信箱稱為長期且通用的識別碼，並以 Meta、Google、LinkedIn 的廣告功能為例，廣告主可以上傳客戶的信箱來比對使用者。這種比對在伺服器之間進行，瀏覽器擋追蹤器擋不到。每個網站用不同的別名，網站之間就無法用信箱比對出同一個人。

依發布頁，Brave 會加密保存帳號信箱與產生的每個別名，別名與真實信箱的對應存在 Brave 的伺服器上。說明頁列出為了除錯會記錄收信時間與部分信件標頭，但不記錄信件內容與寄件人資訊，隱私政策寫這些紀錄最長 14 天內刪除。在隱私政策裡，除非有效的法律要求使 Brave 有義務揭露，否則不會揭露帳號關聯的信箱與別名。官方頁面沒有寫能不能從別名回信，也沒有寫別名用哪個網域。

一份網站用來擋拋棄式信箱的開源名單，9 月在回報議題裡把 `bravealias.com` 當成 Brave 別名的網域，列入較嚴格的分級。維護者提到這是轉寄服務、不是拋棄式信箱，跟 Firefox Relay、SimpleLogin 屬於同一類。所以只列入較嚴格的分級，採用這一級的網站才會擋。

Apple 的「隱藏電子郵件地址」包含在 iCloud+ 付費方案，可以直接回覆。Firefox Relay 免費提供 5 個，匿名回信列在付費方案，付費方案的供應地區名單沒有台灣與香港。SimpleLogin 是開源專案，免費方案有 10 個別名並可從別名回信。

用 Brave 桌面版的讀者更新到 1.94 以上，在網址列輸入 `brave://settings/email-aliases` 建立帳號，就能產生別名。原始碼裡的正體中文介面字串寫作「電子郵件別名」。別名保護的只是信箱這個識別碼，用手機號碼、真實姓名或付款資料註冊時，網站仍然可以用這些資料比對出同一個人。
