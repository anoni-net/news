---
title: Signal 免電話號碼註冊的 Android 測試版
description: Signal 的 Android 測試版可以不用電話號碼註冊，付一次費用換一個不綁門號的帳號，代價是帳號遺失後沒有任何復原管道。iPhone 版還在開發。
date: 2026-09-26T01:23:00+08:00
slug: signal-numberless-registration
pin: true
sources:
  - title: Phone Numberless Registration for Android
    url: https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android
    publisher: Signal Support
  - title: Beta feedback for the upcoming Android 8.28 release
    url: https://community.signalusers.org/t/beta-feedback-for-the-upcoming-android-8-28-release/76457
    publisher: Signal Community
    date: 2026-09-16
  - title: Beta feedback for the upcoming Android 8.29 release
    url: https://community.signalusers.org/t/beta-feedback-for-the-upcoming-android-8-29-release/76509
    publisher: Signal Community
    date: 2026-09-23
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
  - title: Signal Beta
    url: https://support.signal.org/hc/en-us/articles/360007318471-Signal-Beta
    publisher: Signal Support
watch:
  - date: 2026-10-07
    note: Signal Login 是否離開測試版進入正式版，iPhone 版與既有帳號改用的進度
authors:
  - anoni-net
---

Signal 在 Android 8.28 測試版加入不用電話號碼的註冊方式，名為 Signal Login。9 月 23 日的 8.29 測試版公告寫明，這項功能會再留在測試版一週。到 9 月 26 日為止，iPhone 版還在開發，已經用電話號碼註冊的帳號也還不能移除號碼。

註冊時選擇不使用電話號碼，要透過 Google Play 付一次 2.99 美元的費用，各國價格可能不同。沒有安裝 Google Play 服務的裝置，暫時無法用這個方式註冊。

Signal 在社群論壇的公告寫明，付款使用跟捐款系統相同的零知識證明，付款紀錄與帳號之間沒有連結。收費的原因也寫在公告裡，免費的話，垃圾訊息業者可以大量申請帳號。

註冊完成後會取得一組 Account ID 與 Recovery Key，作用相當於帳號與密碼。帳號沒有 PIN，也沒有其他復原管道，其中任一項遺失，帳號就無法找回。

使用者名稱可以另外設定，沒有設定的話，別人無法搜尋到這個帳號，只能參與自己發起的對話。註冊後可以在設定裡加上兩步驗證，到 9 月 26 日為止支援 TOTP 驗證器，passkey 與硬體金鑰會在之後加入。

## 導讀觀點 {#perspective}

門號在許多地方都要實名登記，用門號註冊的通訊帳號等於間接連回真實身分。Signal 的端對端加密保護訊息內容，帳號本身過去卻一直綁著一支門號。改成付費加上零知識證明之後，帳號跟門號、付款都脫鉤，想把工作與私人身分分開的人，不必另外申辦門號。Signal 的 Android 版以 AGPL-3.0 授權公開原始碼，介面有正體中文。

沒有門號之後，別人只能透過使用者名稱找到這個帳號。Freedom of the Press Foundation 的文章寫到，公開分享過的使用者名稱要一直保留，否則別人可以取得同一個名稱來冒充。用使用者名稱接受消息來源聯繫的人，被冒充的後果更嚴重。

另一篇討論 passkey 的觀點文章寫到，一個帳號的安全程度取決於最弱的那一種復原方式。Signal 的免門號帳號沒有任何復原方式，攻擊者少了一個較弱的入口，遺失的風險則全部落在使用者身上。

想試用的人，要先在 Google Play 訂閱 Signal 的測試版，再透過 Google Play 付 2.99 美元的一次性費用，沒有 Google Play 服務的手機無法用這個方式註冊。註冊後把 Account ID 與 Recovery Key 存進密碼管理器並保留離線備份，設定 TOTP 時也要準備不只一個第二因素。
