---
title: 開源 YouTube 用戶端 PipePipe 5.4.0
description: PipePipe 是從 NewPipe 分支出來的 Android 開源用戶端，不需要帳號與 Google Play 就能觀看 YouTube、NicoNico 與 BiliBili。5.4.0 改善了在電視上的操作，也修正了 12 個問題。
date: 2026-10-03T07:05:00+08:00
slug: pipepipe-youtube-client
sources:
  - title: PipePipe v5.4.0
    url: https://github.com/InfinityLoop1308/PipePipe/releases/tag/v5.4.0
    publisher: PipePipe
    date: 2026-09-24
  - title: PipePipe
    url: https://pipepipe.dev
    publisher: PipePipe
  - title: InfinityLoop1308/PipePipe
    url: https://github.com/InfinityLoop1308/PipePipe
    publisher: GitHub
  - title: PipePipe
    url: https://f-droid.org/packages/InfinityLoop1309.NewPipeEnhanced/
    publisher: F-Droid
  - title: PipePipe
    url: https://apt.izzysoft.de/fdroid/index/apk/InfinityLoop1309.NewPipeEnhanced
    publisher: IzzyOnDroid
  - title: PipePipe SABR policies
    url: https://github.com/InfinityLoop1308/PipePipeSabrPolicies
    publisher: GitHub
  - title: YouTube playback, network, and sign-in
    url: https://priveetee.github.io/Docs-PipePipe/issues/youtube-playback.html
    publisher: PipePipe Wiki
  - title: TRANSLATION.md
    url: https://github.com/InfinityLoop1308/PipePipe/blob/main/TRANSLATION.md
    publisher: GitHub
  - title: "[Important] YouTube playback will fail if your DNS blocks googleapis.com or google.com"
    url: https://github.com/InfinityLoop1308/PipePipe/issues/2757
    publisher: GitHub
    date: 2026-07-24
  - title: SABR
    url: https://priveetee.github.io/Docs-PipePipe/developer-guide/introduction.html
    publisher: PipePipe Wiki
authors:
  - anoni-net
watch:
  - date: 2026-10-17
    note: F-Droid 是否更新到 5.4.0
---

Android 開源用戶端 PipePipe 在 9 月 24 日（UTC）發布 5.4.0 版，可以瀏覽 YouTube、日本的影音平台 NicoNico 與中國的 BiliBili。PipePipe 以 GPL-3.0 授權，不需要 Google Play 就能安裝。新版改善了在電視上的操作，直播可以選擇畫質，也修正了進入全螢幕時字幕消失等 12 個問題。

開發者在 2022 年初從另一款開源 YouTube 用戶端 NewPipe 分支出來，此後兩個專案互不同步更新。官網列出的特色是不需要帳號、沒有廣告與追蹤器、不蒐集資料。App 整合了 SponsorBlock（由使用者標記並自動跳過業配片段的服務），可以依關鍵字或頻道過濾內容、隱藏 Shorts，也支援背景播放與下載整個播放清單。

安裝管道有 F-Droid（只收錄開源 App 的 Android 軟體庫）與 IzzyOnDroid（另一個與 F-Droid 客戶端相容的第三方軟體庫），兩邊都標示 NonFreeNet 反功能（Anti-Features），意思是 App 依賴非自由的網路服務。到 9 月 29 日為止，IzzyOnDroid 已更新到 5.4.0，F-Droid 仍是 9 月 12 日加入的 5.3.1。PipePipe 在 GitHub 的發布頁也提供 APK，發布說明寫明多數裝置選 `arm64-v8a` 版本即可。

## 導讀觀點 {#perspective}

用第三方用戶端不必登入 Google 帳號，但影片請求仍然直接送往 YouTube。YouTube 限制匿名請求時，App 會顯示「Sign in to confirm you're not a bot」。官網與 README 連到的 PipePipe Wiki 由社群維護，疑難排解頁寫的做法是先重試，再換網路或 VPN 出口。

PipePipe 也支援登入，README 寫明 YouTube 的登入 cookie 只在取得播放串流時使用。登入之後，帶著 cookie 的播放請求就能對應到帳號。Wiki 寫明登入最好留給 IP 遭封鎖、年齡限制與頻道會員內容，代價是不能只下載音訊，進行中的直播也不能倒轉。

開發者在 GitHub 問題回報區（issue）置頂的 `#2757` 寫明，PipePipe 需要連到 `googleapis.com`、`google.com` 與兩者的子網域。用 DNS 過濾廣告的人擋下這些網域時，YouTube 播放會失敗。Wiki 寫的解法是把它們加入允許清單，不要整個關掉過濾。

Wiki 的開發者指南寫到，YouTube 越來越常用 SABR（用戶端與伺服器保持連線、分小段傳送影音的串流協定）。PipePipe 會從 GitHub 的公開儲存庫下載播放策略，驗證 Ed25519 簽章（確認出自開發者、未遭竄改）、有效期間與版本號之後才執行，失敗就退回內建的實作。從設計上看，開發者不發布新版也能調整播放方式，策略原始碼則公開可供審閱。代價是 App 會執行從網路下載的程式碼。

回報問題時，Wiki 寫明公開的 issue 不要附上 cookie、token 等登入憑證、帳號電子郵件地址或登入過程的螢幕錄影，也不要公開 IP 位址。第一次回報只要寫明有沒有登入與看到的錯誤訊息。

試用需要一支 Android 6.0 以上的手機（依 F-Droid 的標示），不需要 Google 帳號。從 GitHub 發布頁下載 `arm64-v8a` 的 APK 最直接。用 F-Droid 客戶端安裝也會收到更新通知，官方軟體庫還沒有 5.4.0，想先用新版可以加入 IzzyOnDroid 軟體庫（官方客戶端要手動加入）。介面有正體與簡體中文，專案的翻譯說明寫明兩者由 AI 輔助翻譯，Wiki 與 issue 則以英文為主。
