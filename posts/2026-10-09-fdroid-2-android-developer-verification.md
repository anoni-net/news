---
title: F-Droid 2.0 與 Google 的 Android 開發者驗證
description: 開源 App 商店 F-Droid 9 月 24 日推出全面改寫的 2.0，最低需要 Android 7。Google 9 月 30 日起在巴西、印尼、新加坡、泰國要求七家商店的 App 由驗證身分的開發者註冊，2027 年擴大到全球的認證 Android 裝置。到 10 月 2 日為止，台灣讀者從 F-Droid 安裝 App 不受影響。
date: 2026-10-09T00:00:00+08:00
slug: fdroid-2-android-developer-verification
sources:
  - title: "F-Droid 2.0: A New Chapter for Android Freedom"
    url: https://f-droid.org/en/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html
    publisher: F-Droid
    date: 2026-09-24
  - title: Android developer verification
    url: https://developer.android.com/developer-verification/guides
    publisher: Google
    date: 2026-08-18
  - title: Frequently asked questions | Android developer verification
    url: https://developer.android.com/developer-verification/guides/faq
    publisher: Google
    date: 2026-09-30
  - title: Learn about Android developer verification
    url: https://support.google.com/android/answer/17065026
    publisher: Google
  - title: Register your app on open source platforms
    url: https://developer.android.com/developer-verification/guides/open-source-app-registration
    publisher: Google
    date: 2026-09-30
  - title: "Android developer verification: Building a safer ecosystem together"
    url: https://android-developers.googleblog.com/2026/06/android-developer-verification.html
    publisher: Google
    date: 2026-06-18
  - title: A new layer of security for certified Android devices
    url: https://android-developers.googleblog.com/2025/08/elevating-android-security.html
    publisher: Google
    date: 2025-08-25
  - title: "Breaking Up with Google Play: Why Conversations Is Now Free"
    url: https://gultsch.de/posts/breaking-up-with-google-play/
    publisher: Conversations
    date: 2026-09-24
  - title: F-Droid and Google's Developer Registration Decree
    url: https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html
    publisher: F-Droid
    date: 2025-09-29
  - title: An Open Letter Opposing Android Developer Verification
    url: https://f-droid.org/en/2026/02/24/open-letter-opposing-developer-verification.html
    publisher: F-Droid
    date: 2026-02-24
  - title: What We Talk About When We Talk About Malware
    url: https://f-droid.org/en/2026/07/01/adv-malware.html
    publisher: F-Droid
    date: 2026-07-01
  - title: Keep Android Open
    url: https://keepandroidopen.org/
    publisher: Keep Android Open
  - title: F-Droid
    url: https://f-droid.org/en/packages/org.fdroid.fdroid/
    publisher: F-Droid
  - title: Use Google Play Protect to help keep your apps safe & your data private
    url: https://support.google.com/googleplay/answer/2812853
    publisher: Google
watch:
  - date: 2026-11-09
    note: F-Droid 2.0 的安全審查報告是否公開，套件頁是否把 2.0 改為建議版本
  - date: 2026-12-15
    note: Google 是否公布 2027 年全球適用的月份與國別時程，F-Droid 用戶端與開源 App 的註冊情況
authors:
  - anoni-net
---

開源的 Android App 商店 F-Droid 在 9 月 24 日推出 2.0，用戶端整個改寫，最低需要 Android 7。9 月 30 日起，Google 在巴西、印尼、新加坡、泰國要求 Google Play 與六家手機廠商商店上架的 App 由驗證過身分的開發者註冊，預計 2027 年擴大到全球的認證 Android 裝置。到 10 月 2 日為止，各地的讀者從 F-Droid 或網站直接下載安裝 App 都不受影響。

F-Droid 只收錄開源 App，依 F-Droid 的說明，團隊會審查公開的原始碼、確認沒有廣告與追蹤器，再自行建置發布。2.0 改用 Kotlin 與 Jetpack Compose 寫成，介面縮減為探索、搜尋與我的 App 三個分頁。App 更新改為預設自動下載安裝，已經調整過的偏好設定會保留。F-Droid 的 2.0 公告也寫到搜尋改善了中文、日文、韓文的支援。

2.0 經過獨立的安全審查，公告寫明完整報告確認可以發表後才會公開。原本的「使用 Tor」改成一般的 Proxy 設定，公告建議改用 Tor VPN。緊急刪除 App 的功能暫時移除了，公告建議依賴這項功能的人延後更新。到 10 月 2 日為止，F-Droid 首頁提供下載的是 2.0.1，套件頁則仍把 2.0 標為測試版，建議版本是 1.23.2。

開源即時通訊 App Conversations 的開發者 9 月 24 日在部落格寫到 Google Play 一再退回 App 的更新、App 也被下架過兩次，文章發表時還有一個更新已經等了 14 天審核。開發者認為 Google 不區分功能更新與安全更新，安全更新延遲數日是危險的。關於 Google Play 的審核，到 10 月 2 日為止只看到開發者一方的說法。

Conversations 開發者的文章也寫明 F-Droid 已成為主要的散布管道，F-Droid 上的版本改為可重現建置（任何人都能從原始碼建出相同的檔案），由開發者自己的金鑰簽章。原本收費的 Google Play 版本到 10 月 2 日已改為免費。

Google 的開發者驗證要求開發者證明身分，並以私鑰簽章的安裝檔（APK）登記套件名稱，Google 藉此把 App 對應到開發者帳號。到 10 月 2 日為止，Google 的 FAQ 寫明第一階段只限七家參與的商店，其他商店與側載（不經商店直接安裝）不受影響。2027 年擴大後，認證裝置上沒有註冊的 App 只能用開發者工具 ADB 安裝，或透過 Google 稱為 advanced flow 的程序開放安裝。Google 的說明中心另外寫明 AOSP（Android 開源專案）的裝置、未經認證的裝置，以及 Google 行動服務不支援的地區都不適用這項要求。

advanced flow 要先在系統設定開啟開發者模式，並確認自己沒有被人在旁指導操作，接著重新開機並重新驗證身分。之後有一次性的一天等待期。期滿後用指紋、臉部辨識或 PIN 確認，就能選擇開放 7 天或無限期安裝未驗證開發者的 App。

## 導讀觀點 {#perspective}

兩種做法對「這個 App 能不能信任」有不同的答案。Google 要求開發者證明身分，F-Droid 的信任則來自公開的原始碼，App 由 F-Droid 的金鑰簽章，可重現建置的 App 則改用原開發者的金鑰。依 Google 的規則，套件名稱要由開發者本人註冊。F-Droid 在 2025 年 9 月的公告表示無法要求開發者向 Google 註冊，也不能替開源 App 接管套件名稱。

Google 在 2025 年 8 月的公告寫到，依 Google 自己的分析，網路側載來源的惡意程式是 Google Play 上的 50 倍以上。公告也寫明第一階段選在受詐騙 App 影響的國家，並引述印尼、泰國主管機關的正面評價。F-Droid 在 2026 年 7 月的文章則指出，Android 開發者主控台的條款寫明散布惡意程式可以終止帳號，但沒有定義什麼是惡意程式。

多個自由軟體與數位權利組織參與的 Keep Android Open 列出 advanced flow 的九個步驟，並指出這個程序由 Google Play 服務提供、不在 Android 系統本身，因此 Google 可以隨時更改。Google 的 FAQ 寫明一天的等待期是為了打斷詐騙者在電話上催促受害者立刻更改安全設定。FAQ 也寫明開啟 advanced flow 之後不必保持開發者模式，用 ADB 安裝也不受等待期限制。

F-Droid 在 2026 年 2 月發表公開信，建議開發者現在與將來都不要註冊。F-Droid 在 2025 年的公告也表示，這項規定會終結 F-Droid 與其他開源散布管道現在的運作方式。Google 則為開源平台寫了註冊指南。依指南，開發者以自己的帳號登記套件名稱，會重新簽章的平台另外提供平台金鑰的指紋，使用者就能維持現在的安裝方式。

到 10 月 2 日為止，台灣的 Android 使用者不必調整任何設定。想體驗 F-Droid 的人，可以從官網首頁下載約 12.5 MB 的安裝檔，在系統設定允許瀏覽器安裝不明應用程式。F-Droid 的網站與 App 有正體中文，但到 10 月 2 日為止，2.0 新的分類名稱只翻譯了約四成，部分會顯示英文。依賴緊急刪除 App 功能的人，可以先使用套件頁建議的 1.23.2。

想知道 2027 年之後會不會受影響，可以打開 Google Play 商店，點右上方的個人資料圖示，在「設定」的「關於」查看裝置是否通過 Play 安全防護認證。到 10 月 2 日為止，Google 的公告只寫 2027 年擴大到全球，月份與各地的先後順序都沒有公布。依 Google 的計畫，屆時在認證裝置上安裝未註冊開發者的 App，要提前一天開啟 advanced flow，關閉 advanced flow 之後，這些 App 會無法更新。
