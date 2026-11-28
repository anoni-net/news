---
title: GrapheneOS 支援 Pixel 11 的條件
description: 隱私強化手機系統 GrapheneOS 8 月底以 Pixel 11 缺少記憶體標記擴充（MTE）為由，建議不要購買。GrapheneOS 11 月的貼文提到 Android 17 QPR2 已替 Pixel 11 補上 MTE 的韌體支援，GrapheneOS 要等 QPR2 進入 Android 開源專案並完成移植才能支援。到 11 月 14 日官方支援清單還沒有 Pixel 11，建議購買的機型仍是 Pixel 8 到 Pixel 10a。
date: 2026-11-16T00:00:00+08:00
slug: grapheneos-pixel-11
categories:
  - mobile
related:
  - title: GrapheneOS，高度隱私的行動作業系統
    url: https://anoni.net/docs/tools/grapheneos/
sources:
  - title: Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped
    publisher: GrapheneOS Discussion Forum
    date: 2026-08-29
  - title: 'GrapheneOS: "Our port to the Pixel 11 series was nearly comple…" - GrapheneOS Mastodon'
    url: https://grapheneos.social/@GrapheneOS/117596333575500952
    publisher: GrapheneOS
    date: 2026-11-11
  - title: 'GrapheneOS: "Our port to Android 17 QPR2 is nearly complete. P…" - GrapheneOS Mastodon'
    url: https://grapheneos.social/@GrapheneOS/117596341370458465
    publisher: GrapheneOS
    date: 2026-11-11
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3mzztj5fbk226
    publisher: GrapheneOS
    date: 2026-11-11
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3n277527yrk2u
    publisher: GrapheneOS
    date: 2026-11-13
  - title: 'GrapheneOS: "Motorola Signature 27 meets all of our official s…" - GrapheneOS Mastodon'
    url: https://grapheneos.social/@GrapheneOS/117570889454162312
    publisher: GrapheneOS
    date: 2026-11-06
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3mzogzkzr622p
    publisher: GrapheneOS
    date: 2026-11-06
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3mzqmjgfuxs2o
    publisher: GrapheneOS
    date: 2026-11-07
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#recommended-devices
    publisher: GrapheneOS
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases
    publisher: GrapheneOS
  - title: GrapheneOS translate to other languages - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/5030-grapheneos-translate-to-other-languages
    publisher: GrapheneOS Discussion Forum
  - title: Google introduces Pixel 11, Pixel 11 Pro and Pixel 11 Pro XL
    url: https://blog.google/products-and-platforms/devices/pixel/google-pixel-11-pro-xl/
    publisher: Google
    date: 2026-08-12
  - title: Learn when you'll get software updates on Google Pixel phones - Nexus Help
    url: https://support.google.com/nexus/answer/4457705?hl=en
    publisher: Google
  - title: Release notes | Android Developers
    url: https://developer.android.com/about/versions/17/qpr2/release-notes
    publisher: Android Developers
  - title: GrapheneOS Announces Pixel 11 Support Can Be Completed Now
    url: https://www.privacyguides.org/news/2026/11/12/grapheneos-announces-pixel-11-support-can-be-completed-now/
    publisher: Privacy Guides
    date: 2026-11-12
watch:
  - date: 2026-11-21
    note: Android 17 QPR2 是否已推送到 AOSP，GrapheneOS 的 FAQ 支援清單與版本紀錄是否列入 Pixel 11
authors:
  - anoni-net
---

GrapheneOS 是以 Android 開源程式碼為基礎的隱私強化手機系統（本站寫過它的[剪貼簿讀取開關](https://anoni.net/news/2026/10/grapheneos-clipboard-toggle/)），到 11 月 14 日，官方的支援清單與版本紀錄都還沒有 Google 8 月推出的 Pixel 11 系列。依 GrapheneOS 11 月在 Bluesky 的貼文，Android 17 QPR2 已替 Pixel 11 補上記憶體標記擴充（MTE，在硬體層級偵測並攔下利用記憶體錯誤發動攻擊的功能）的韌體支援。GrapheneOS 要等 QPR2 的原始碼釋出到 Android 開源專案（AOSP）並完成移植，才能加入 Pixel 11。受影響的是打算買新機安裝 GrapheneOS 的人，以及已經有 Pixel 11、想改裝 GrapheneOS 的人。

依 GrapheneOS 8 月 29 日在官方論壇的公告，Pixel 11 系列 8 月 20 日上架後，團隊花了約一週完成部分移植。公告提到軟體與韌體缺少 MTE 的支援，硬體也可能沒有，移植因此無法完成。公告推測 Google 為了節省成本拿掉了這項安全功能，公告提到的不符項目只有 MTE。公告強烈建議不要購買 Pixel 11，也寫到可能跳過整個系列，把重心移到即將推出的 Motorola 機型。

同一篇公告也列出 Pixel 11 的安全改進，包括改用能抵抗量子電腦破解的驗證開機簽章（ML-DSA），以及新的 Titan M3 安全晶片。根據公告的說明，Titan M3 應該能讓開機後、第一次解鎖前的手機更難被取出資料，對沒有設定高強度密碼的人有幫助。少了 MTE，手機解鎖過之後的安全性則會大幅下降。公告另外寫到 Pixel 10 比較便宜，硬體相近也有 MTE。

依 Privacy Guides 轉引的 GrapheneOS 9 月 1 日 Bluesky 貼文，Pixel 11 的硬體仍有最低限度的 MTE 支援。GrapheneOS 在那則貼文推測 Google 為了省錢拿掉了 CPU 快取大部分的硬體加速，MTE 的效能因此太差，最後在韌體裡完全關閉。貼文也寫到 MTE 可能仍然可以使用。

GrapheneOS 11 月 11 日的貼文寫到，Android 17 QPR2 替 Pixel 11 加入了 MTE 支援，GrapheneOS 已用自己的 QPR2 移植確認可以運作。同一天的另一則貼文提到開啟 MTE 的效能可以接受，跟前幾代 Pixel 相近。GrapheneOS 在同一則貼文寫到，外流消息提到的移除出現在 Google 最後沒有採用的設計上。

GrapheneOS 11 月 13 日的貼文提到，Pixel 11 要等 Android 17 QPR2 推送到 AOSP、GrapheneOS 對 QPR2 的移植完成之後才能支援。GrapheneOS 等的是 QPR2 的原始碼進入 AOSP，Google 推送 QPR2 給 Pixel 手機的更新不算在內（本文依貼文的說法推論）。到 11 月 14 日，本文沒有查到 QPR2 已經進入 AOSP 的紀錄。

GrapheneOS 11 月 11 日談 QPR2 移植進度的貼文提到，移植接近完成，先替已支援的機型推出之後再加入 Pixel 11。貼文也寫到 QPR2 之後的主要優先是完成 Motorola 新機 Signature 27 的支援，Pixel 11 的支援早已大致完成，同樣可以在 QPR2 之後推出。到 11 月 14 日，GrapheneOS 沒有公布 Pixel 11 加入的時程。Privacy Guides 報導這件事的標題是「GrapheneOS Announces Pixel 11 Support Can Be Completed Now」，GrapheneOS 自己的貼文寫的仍是 QPR2 進入 AOSP、移植完成之後。

到 11 月 14 日，Pixel 11 與 MTE 的說法只有 GrapheneOS 一方。Google 8 月 12 日的 Pixel 11 發表文沒有提到 MTE，Android Developers 的 QPR2 版本說明也沒有 MTE 的條目，本文沒有查到 Google 對 Pixel 11 MTE 的說明。

## 導讀觀點 {#perspective}

依 Privacy Guides 的說明，ARM 晶片的硬體功能 MTE 會替一段記憶體加上標籤，存取它的指標也帶同一個標籤。兩者不符時程式不會繼續執行，利用記憶體安全錯誤（例如讀寫到不該存取的記憶體位置）的攻擊因此被擋下。GrapheneOS 的論壇公告寫到，MTE 大幅提升了對幾乎所有遠端攻擊與許多本機攻擊的防護。

依同一篇公告，Pixel 8 在 2023 年 10 月推出時開始有硬體 MTE。GrapheneOS 當月開始使用，到公告發布時已在整個基礎系統啟用，包括核心與每個標準的系統程序（少數裝置專用的程序暫時關閉）。Android 與 Pixel 原廠系統沒有預設啟用，Android 16 的進階保護模式只替少數程序開啟（進階保護的開啟方式見[舊版 iOS 與 Android 被利用的已知漏洞](https://anoni.net/news/2026/11/ios-android-exploits-lockdown/)）。公告也提到 iPhone 17 的 Memory Integrity Enforcement（MIE）一直開啟，是用最新標準擴充實作的 MTE。

GrapheneOS 的 FAQ 把硬體記憶體標記列為未來支援機型的需求，跟至少 5 年的更新、每月完整的 Android 安全公告修補放在同一份清單。GrapheneOS 11 月 7 日在 Bluesky 的貼文提到，要達到跟 iPhone 相比的業界標準漏洞防護就需要 MTE，自從硬體推出就把它當成必要條件。

根據 Google 的更新說明頁，Pixel 8 以後的手機從在美國 Google Store 開賣起提供 7 年的系統與安全更新，清單包括 Pixel 11 系列。照 GrapheneOS FAQ 用上市日起算 7 年的方式，本文推算 Pixel 11 約到 2033 年 8 月，Google 的頁面沒有寫結束的月份。留在原廠系統的 Pixel 11 使用者照常收到這些更新。依 GrapheneOS 11 月 7 日的貼文，到那天 Google 仍只在 Android 的進階保護模式裡替少數程序啟用 MTE。

GrapheneOS 在 11 月 6 日的貼文寫到，Motorola Signature 27 符合它所有的安全需求，搭載 Qualcomm 的 MTE 實作。貼文也寫到 GrapheneOS 將可以替這款手機提供上市起 7 年的更新。同一天的另一則貼文提到，Pixel 11 加入之後，符合全部安全需求的當代機型會有兩個系列。

打算買手機安裝 GrapheneOS 的人，到 11 月 14 日 FAQ 強烈建議購買的是 Pixel 8、8 Pro、8a、Pixel 9 系列、9a、Pixel 10 系列與 10a。FAQ 的支援年限表裡這幾款都有上市後 7 年的原廠最低支援，最早結束的 Pixel 8 與 8 Pro 到 2030 年 10 月，最晚的 Pixel 10a 到 2033 年 3 月。FAQ 也提醒，GrapheneOS 只能在原廠持續發布更新時提供完整的安全更新。GrapheneOS 論壇管理者的回覆寫到，到 10 月 23 日查證時，GrapheneOS 自己新增的設定與 App 只有英文。

已經有 Pixel 11 的人不必做任何設定，原廠系統照常更新。想改裝 GrapheneOS 的人，可以留意 Android 17 QPR2 何時推送到 AOSP，以及 GrapheneOS 的 FAQ 與版本紀錄何時列出 Pixel 11。依 8 月論壇公告的比較，Pixel 10 價格較低、硬體相近也有 MTE，是 GrapheneOS 已經支援的機型。原廠支援結束的時間比 Pixel 11 的推算早一年左右（FAQ 的表上 Pixel 10 到 2032 年 8 月）。
