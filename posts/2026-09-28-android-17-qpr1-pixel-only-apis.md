---
title: Android 17 QPR1 的 Pixel 獨占 API
description: Android 17 QPR1 新增了給 App 開發者的 API，原始碼卻沒有釋出到 AOSP，非 Pixel 的手機與 GrapheneOS 這類系統要等到 12 月的 QPR2。
date: 2026-09-28T07:05:00+08:00
slug: android-17-qpr1-pixel-only-apis
sources:
  - title: Android Open Source Project
    url: https://source.android.com/
    publisher: Google
  - title: Android 17 QPR1 is the first release since Android Honeycomb (3.x) adding new APIs for app developers without a release to the Android Open Source Project
    url: https://grapheneos.social/@GrapheneOS/117282080803799576
    publisher: GrapheneOS
    date: 2026-09-16
  - title: Android API Differences Report
    url: https://developer.android.com/sdk/api_diff/37.1/changes/changes-summary
    publisher: Android Developers
  - title: Google rolling out Android 17 QPR1 for Pixel
    url: https://9to5google.com/2026/09/15/android-17-qpr1-pixel/
    publisher: 9to5Google
    date: 2026-09-15
  - title: Android 16 QPR1's source code is now available on AOSP
    url: https://www.androidauthority.com/android-16-qpr1-source-code-available-3614853/
    publisher: Android Authority
    date: 2025-11-11
  - title: "Exclusive: Google will develop the Android OS fully in private, here's why"
    url: https://www.androidauthority.com/google-android-development-aosp-3538503/
    publisher: Android Authority
    date: 2025-03-26
  - title: Frequently Asked Questions
    url: https://grapheneos.org/faq
    publisher: GrapheneOS
  - title: GrapheneOS changelog
    url: https://grapheneos.org/releases
    publisher: GrapheneOS
  - title: Web install
    url: https://grapheneos.org/install/web
    publisher: GrapheneOS
authors:
  - anoni-net
---

Google 在 9 月 15 日推送給 Pixel 6 以後機型的 Android 17 QPR1，新增了給 App 開發者的 API，版本號是 API level 37.1，例如新的 `android.hardware.hid` 套件。這些 API 的原始碼沒有釋出到 Android 開源專案（AOSP）。GrapheneOS 的公告寫到，Android 3.x 以來還沒有過新 API 不經過 AOSP 就推出的情況。非 Pixel 的手機與以 AOSP 為基礎的系統，要等到 12 月的 Android 17 QPR2 才能取得。

這跟 Google 的釋出方式有關。Google 在 2025 年 3 月向 Android Authority 證實，Android 的開發會全部改在內部進行，內部分支只開放給簽了 Google 行動服務（GMS）授權的公司。AOSP 網站也寫明，從 2026 年起只在第二季與第四季釋出原始碼。Android 16 的 QPR1 晚了幾週才進 AOSP，到 9 月 27 日為止，AOSP 上 Android 17 只有正式版的分支，沒有 QPR1。

GrapheneOS 的公告寫到，他們在 QPR1 推出前就把自家的程式移植好了，但還沒有取得釋出的許可，目前改成把 Pixel 的韌體、核心驅動與硬體抽象層從 QPR1 移回 Android 17。9 月 17 日的版本先移植了 QPR1 的行動網路數據機韌體，19 日再補上對應的電信業者設定。

GrapheneOS 另外寫到，9 月的 Pixel 更新公告裡有幾項一般 Android 元件的修補，沒有出現在同月的 Android 安全公告，其他廠商要等 12 月的 QPR2。GrapheneOS 也寫到，9 月 1 日向 Google 索取的 GPL 原始碼，隔了兩週多才取得。

## 導讀觀點 {#perspective}

Android 的開放建立在 AOSP 上，其他手機廠商與 GrapheneOS 等專案都從同一份原始碼建構系統。原始碼改成半年釋出一次之後，Pixel 先取得新 API 與部分安全修補，其他裝置的使用者要多等幾個月。非 Google 的廠商想及時推送修補，需先取得 Google 的安全預覽權限，GrapheneOS 寫到他們是透過另一家廠商取得。

GrapheneOS 以 OSI 核可的開源授權釋出，目前只支援 Pixel，9 月到現在仍陸續推出新版本。GrapheneOS 寫到，可以用反向工程的方式提早補上 Pixel 公告裡的修補，使用者在 QPR2 之前仍能收到更新。

GrapheneOS 也寫到，Pixel 現在比許多裝置更難支援，過去的優勢反而成了負擔。他們預期支援即將推出的 Motorola 新機會比支援 Pixel 容易，因為會取得官方提供的韌體與驅動程式。

用其他品牌手機的人，QPR1 新增的 API 與部分修補要等到 12 月的 QPR2，實際收到的時間還要看手機廠商何時推送。想刷 GrapheneOS 保護隱私的人，現在仍然只能選 Pixel，官方支援的機型列在 GrapheneOS 的 FAQ。官方的網頁安裝程式需要一台至少有 2GB 可用記憶體與 32GB 可用空間的電腦和一條 USB 線，瀏覽器要用 Chrome、Edge 這類官方支援的瀏覽器，安裝說明是英文。可能由電信業者鎖定販售的機型，解鎖前要連網，讓原廠系統確認手機沒有被鎖定。
