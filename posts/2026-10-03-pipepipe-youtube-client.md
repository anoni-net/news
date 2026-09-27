---
title: 開源 YouTube 用戶端 PipePipe 5.4.0
description: PipePipe 是從 NewPipe 分支出來的 Android 開源用戶端，不需要帳號就能觀看 YouTube、NicoNico 與 BiliBili。9 月 24 日發布的 5.4.0 改善了電視操作，也修正多項播放問題。
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
authors:
  - anoni-net
---

PipePipe 在 9 月 24 日發布 5.4.0 版，是一款可以瀏覽 YouTube、NicoNico 與 BiliBili 的 Android 開源用戶端，以 GPL-3.0 授權。開發者在 2022 年初從 NewPipe 分支出來獨立開發，之後兩個專案不再互相同步更新。

官網列出的特色包括不需要帳號、沒有廣告與追蹤器、不蒐集資料，並整合 SponsorBlock 跳過業配片段，可以依關鍵字或頻道過濾內容、隱藏 Shorts，支援背景播放與下載整個播放清單。5.4.0 改善了電視的操作，直播可以選擇畫質，也修正了全螢幕時字幕消失等十多個問題。

安裝管道有 F-Droid 與 IzzyOnDroid，兩邊都標示 NonFreeNet 反功能，意思是 App 依賴非自由的網路服務。撰稿時 IzzyOnDroid 已經更新到 5.4.0，F-Droid 還是 9 月 12 日加入的 5.3.1。

也可以從 GitHub 的發布頁直接下載 APK，依發布說明，多數手機選 arm64-v8a 版本即可。F-Droid 標示需要 Android 6.0 以上，頁面也寫到直接下載 APK 安裝不會收到更新通知。

## 導讀觀點 {#perspective}

第三方用戶端的好處是不必登入 Google 帳號，訂閱分組與離線播放清單都在 App 內管理。影片請求仍然直接送往 YouTube，YouTube 限制匿名請求時會出現「Sign in to confirm you're not a bot」，專案文件的建議是換一個網路或 VPN 出口再試。PipePipe 也支援登入，說明寫到登入 cookie 只在取得播放串流時使用，但登入之後這些請求就與帳號連在一起。

YouTube 逐步改用 SABR 協定傳送影音，開發者為了跟上，讓 PipePipe 從 GitHub 的公開 repo 下載一份經 Ed25519 簽章的播放策略程式碼。App 驗證簽章、有效期間與版本號之後才執行，失敗時退回內建的實作。開發者因此不必發新版就能調整播放邏輯，原始碼也公開可供審閱，代價是 App 會執行從網路下載的程式碼。

用 DNS 過濾廣告的人要留意，專案文件寫明 PipePipe 需要連到 googleapis.com 與 google.com 的子網域，被擋下時所有 YouTube 影片都會播放失敗。介面有正體與簡體中文，專案的翻譯說明寫到這兩種語言由 AI 輔助翻譯，用詞不順的地方可以直接送 PR 修正。

回報問題時也有隱私上的細節要注意。專案文件寫到，公開的 issue 不要附上 cookie、token、帳號 Email 或登入過程的錄影，也不要公開 IP 位址，寫明有沒有登入與看到的錯誤訊息就足以開始排查。
