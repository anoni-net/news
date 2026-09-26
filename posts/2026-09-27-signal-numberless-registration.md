---
title: Signal 免電話號碼註冊的 Android 測試版
description: Signal 的 Android 測試版可以不用電話號碼註冊，付一次費用換一個不綁門號的帳號，代價是帳號遺失後沒有任何復原管道。
date:
  created: 2026-09-27
  updated: 2026-09-28
slug: signal-numberless-registration
pin: true
sources:
  - title: Beta feedback for the upcoming Android 8.28 release
    url: https://community.signalusers.org/t/beta-feedback-for-the-upcoming-android-8-28-release/76457
    publisher: Signal Community
    date: 2026-09-16
  - title: Signal tests account registration without phone number on Android
    url: https://cyberinsider.com/signal-tests-account-registration-without-phone-number-on-android/
    publisher: CyberInsider
    date: 2026-09-18
  - title: "Signal Will Let You Sign Up Without a Phone Number — For $3"
    url: https://itsfoss.com/news/signal-numberless-registration/
    publisher: It's FOSS
    date: 2026-09-22
  - title: Signal introduces registration without a phone number
    url: https://freedom.press/digisec/blog/signal-introduces-registration-without-a-phone-number/
    publisher: Freedom of the Press Foundation
    date: 2026-09-23
  - title: I don't like passkeys
    url: https://hawksley.dev/blog/i-dont-like-passkeys
    date: 2026-09-18
authors:
  - anoni-net
---

Signal 在 Android 8.28 測試版加入不用電話號碼的註冊方式。目前只有 Android 測試版可以使用，iPhone 版還在開發，已經用電話號碼註冊的帳號也還不能移除號碼。

註冊時選擇不使用電話號碼，要透過 Play 商店的應用程式內購買付一次費用，費用是 3 美元，各國價格可能不同。Signal 在社群論壇的公告寫明，付款使用跟捐款系統相同的零知識證明，付款紀錄與帳號之間沒有連結。公告也說明了收費的原因，免費的話，垃圾訊息業者可以大量申請帳號。

註冊完成後會取得一組 Account Id 與 Account Key，作用相當於帳號與密碼。帳號沒有 PIN，也沒有其他復原管道，其中任一項遺失，帳號就找不回來。使用者名稱可以另外設定，不設定的話別人找不到這個帳號，只能參與自己發起的對話。Freedom of the Press Foundation 提醒，公開分享過的使用者名稱要一直保留，放掉之後，別人可以取得同一個名稱來冒充原本的使用者。

註冊後可以在設定裡加上兩步驗證，目前支援 TOTP 驗證器，passkey 與硬體金鑰會在之後加入。

## 技術觀點 {#technical-view}

門號在許多地方都要實名登記，用門號註冊的通訊帳號，等於間接連回真實身分。Signal 的端對端加密保護的是訊息內容，帳號本身過去一直綁著一支門號。改成付費加上零知識證明之後，帳號跟門號、付款都脫鉤，想把工作與私人身分分開的人，不必為此另外申辦門號。

取捨在於帳號的安全完全落在 Account Key 的保管上，遺失之後沒有簡訊驗證碼或任何其他管道可以找回帳號。Account Id 與 Account Key 要存進密碼管理器，另外保留一份離線備份。設定 TOTP 時也要準備不只一個第二因素，第二因素全部遺失同樣會永久鎖住帳號。

另一篇討論 passkey 的觀點文章可以對照著讀。作者認為對個人使用者來說，帳號遺失的風險比被釣魚更高，而一個帳號的安全程度取決於最弱的那一種復原方式。Signal 的免門號帳號沒有任何復原方式，攻擊者少了一個較弱的入口，遺失的風險則全部落在使用者身上。

付款目前只走 Play 商店，需要 Google Play 服務，沒有安裝 Play 服務的裝置暫時無法用這個方式註冊。Signal 的 Android 版以 AGPL-3.0 授權公開原始碼，介面有正體中文。
