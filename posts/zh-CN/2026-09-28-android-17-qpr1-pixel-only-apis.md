---
title: Android 17 QPR1 的 Pixel 独占 API
description: Android 17 QPR1 新增了给 App 开发者的 API，源代码却没有发布到 AOSP，非 Pixel 的手机与 GrapheneOS 这类系统要等到 12 月的 QPR2。
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
  - title: Create Wear OS apps for China
    url: https://developer.android.com/training/wearables/creating-app-china
    publisher: Android Developers
  - title: "Huawei Mate 70 launch: HarmonyOS Next details, specs, price"
    url: https://www.cnbc.com/2024/11/26/huawei-mate-70-launch-harmonyos-next-details-specs-price-.html
    publisher: CNBC
    date: 2024-11-26
  - title: Web install
    url: https://grapheneos.org/install/web
    publisher: GrapheneOS
authors:
  - anoni-net
---

Google 在 9 月 15 日推送给 Pixel 6 以后机型的 Android 17 QPR1，新增了给 App 开发者的 API，版本号是 API level 37.1，例如新的 `android.hardware.hid` 包。这些 API 的源代码没有发布到 Android 开源项目（AOSP）。GrapheneOS 的公告写到，Android 3.x 以来还没有过新 API 不经过 AOSP 就推出的情况。非 Pixel 的手机与基于 AOSP 的系统，要等到 12 月的 Android 17 QPR2 才能取得。

这跟 Google 的发布方式有关。Google 在 2025 年 3 月向 Android Authority 证实，Android 的开发会全部改在内部进行，内部分支只开放给签了 Google 移动服务（GMS）授权的公司。AOSP 网站也写明，从 2026 年起只在第二季度与第四季度发布源代码。Android 16 的 QPR1 晚了几周才进 AOSP，到 9 月 27 日为止，AOSP 上 Android 17 只有正式版的分支，没有 QPR1。

GrapheneOS 的公告写到，他们在 QPR1 推出前就把自家的代码移植好了，但到 9 月 27 日为止还没有取得发布的许可，因此改成把 Pixel 的固件、内核驱动与硬件抽象层从 QPR1 移回 Android 17。9 月 17 日的版本先移植了 QPR1 的移动网络调制解调器固件，19 日再补上对应的运营商设置。

GrapheneOS 另外写到，9 月的 Pixel 更新公告里有几项通用 Android 组件的补丁，没有出现在同月的 Android 安全公告，其他厂商要等 12 月的 QPR2。GrapheneOS 也写到，9 月 1 日向 Google 索取的 GPL 源代码，隔了两周多才取得。

## 导读观点 {#perspective}

Android 的开放建立在 AOSP 上，没有 GMS 授权的厂商与 GrapheneOS 等项目，都从同一份源代码构建系统。源代码改成半年发布一次之后，Pixel 先取得新 API 与部分安全补丁，其他设备的用户要多等几个月。

在中国大陆，Google 的开发者文档写到，为中国开发 App 要考虑没有预装 Google Play 服务的手机。华为的 HarmonyOS NEXT 据 CNBC 报道已不再使用 Android 的开源代码，AOSP 的发布时程对它没有直接影响。

GrapheneOS 以 OSI 认可的开源授权发布，只支持 Pixel，9 月仍陆续推出新版本。GrapheneOS 写到，可以用逆向工程的方式提前补上 Pixel 公告里的补丁，也预期支持即将推出的 Motorola 新机会比支持 Pixel 容易，因为会取得官方提供的固件与驱动程序。

想刷 GrapheneOS 保护隐私的人，在 Motorola 新机推出之前只能选 Pixel，官方支持的机型列在 GrapheneOS 的 FAQ。官方的网页安装程序需要一台至少有 2GB 可用内存与 32GB 可用空间的电脑和一根 USB 线，浏览器要用 Chrome、Edge 这类官方支持的浏览器，安装说明是英文。可能由运营商锁定销售的机型，要先联网让原厂系统确认手机没有被锁定，才能解锁 bootloader。解锁 bootloader 与安装系统都会清除手机上的所有数据，而且换成 GrapheneOS 之后，要等到 QPR2 才有原厂系统已经提供的 QPR1 新 API。

用其他品牌手机的人不必做任何设置，QPR1 新增的 API 与部分补丁要等手机厂商推送 QPR2 之后才会收到。12 月可以留意 Google 发布 QPR2 时有没有把 QPR1 的 API 与补丁一起放进 AOSP，以及 GrapheneOS 与其他厂商何时取得。
