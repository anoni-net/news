---
title: GrapheneOS 支持 Pixel 11 的条件
description: 隐私强化手机系统 GrapheneOS 8 月底以 Pixel 11 缺少内存标记扩展（MTE）为由，建议不要购买。GrapheneOS 11 月的帖文提到 Android 17 QPR2 已为 Pixel 11 补上 MTE 的固件支持，GrapheneOS 要等 QPR2 进入 Android 开源项目并完成移植才能支持。到 11 月 14 日官方支持列表还没有 Pixel 11，建议购买的机型仍是 Pixel 8 到 Pixel 10a。
date: 2026-11-16T00:00:00+08:00
slug: grapheneos-pixel-11
categories:
  - mobile
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
  - title: Learn about devices & services available in your region - Google Store Help
    url: https://support.google.com/store/answer/2462844?hl=en
    publisher: Google
  - title: Is https://releases.grapheneos.org blocked in mainland China?
    url: https://en.greatfire.org/https/releases.grapheneos.org
    publisher: GreatFire
  - title: GrapheneOS/platform_packages_apps_Settings
    url: https://github.com/GrapheneOS/platform_packages_apps_Settings/tree/2026102100/res
    publisher: GitHub
authors:
  - anoni-net
---

GrapheneOS 是以 Android 开源代码为基础的隐私强化手机系统（本站写过它的[剪贴板读取开关](https://anoni.net/news/2026/10/grapheneos-clipboard-toggle/)），到 11 月 14 日，官方的支持列表与版本记录都还没有 Google 8 月推出的 Pixel 11 系列。依 GrapheneOS 11 月在 Bluesky 的帖文，Android 17 QPR2 已为 Pixel 11 补上内存标记扩展（MTE，在硬件层面检测并拦下利用内存错误发动攻击的功能）的固件支持。GrapheneOS 要等 QPR2 的源代码发布到 Android 开源项目（AOSP）并完成移植，才能加入 Pixel 11。受影响的是打算买新机安装 GrapheneOS 的人，以及已经有 Pixel 11、想改装 GrapheneOS 的人。

依 GrapheneOS 8 月 29 日在官方论坛的公告，Pixel 11 系列 8 月 20 日上架后，团队花了约一周完成部分移植。公告提到软件与固件缺少 MTE 的支持，硬件也可能没有，移植因此无法完成。公告推测 Google 为了节省成本拿掉了这项安全功能，公告提到的不符项目只有 MTE。公告强烈建议不要购买 Pixel 11，也写到可能跳过整个系列，把重心移到即将推出的 Motorola 机型。

同一篇公告也列出 Pixel 11 的安全改进，包括改用能抵抗量子计算机破解的验证启动签名（ML-DSA），以及新的 Titan M3 安全芯片。根据公告的说明，Titan M3 应该能让开机后、第一次解锁前的手机更难被取出数据，对没有设置高强度密码的人有帮助。少了 MTE，手机解锁过之后的安全性则会大幅下降。公告另外写到 Pixel 10 比较便宜，硬件相近也有 MTE。

依 Privacy Guides 转引的 GrapheneOS 9 月 1 日 Bluesky 帖文，Pixel 11 的硬件仍有最低限度的 MTE 支持。GrapheneOS 在那则帖文推测 Google 为了省钱拿掉了 CPU 缓存大部分的硬件加速，MTE 的性能因此太差，最后在固件里完全关闭。帖文也写到 MTE 可能仍然可以使用。

GrapheneOS 11 月 11 日的帖文写到，Android 17 QPR2 为 Pixel 11 加入了 MTE 支持，GrapheneOS 已用自己的 QPR2 移植确认可以运作。同一天的另一则帖文提到开启 MTE 的性能可以接受，跟前几代 Pixel 相近。GrapheneOS 在同一则帖文写到，外泄消息提到的移除出现在 Google 最后没有采用的设计上。

GrapheneOS 11 月 13 日的帖文提到，Pixel 11 要等 Android 17 QPR2 推送到 AOSP、GrapheneOS 对 QPR2 的移植完成之后才能支持。GrapheneOS 等的是 QPR2 的源代码进入 AOSP，Google 推送 QPR2 给 Pixel 手机的更新不算在内（本文依帖文的说法推论）。到 11 月 14 日，本文没有查到 QPR2 已经进入 AOSP 的记录。

GrapheneOS 11 月 11 日谈 QPR2 移植进度的帖文提到，移植接近完成，先为已支持的机型推出之后再加入 Pixel 11。帖文也写到 QPR2 之后的主要优先是完成 Motorola 新机 Signature 27 的支持，Pixel 11 的支持早已大致完成，同样可以在 QPR2 之后推出。到 11 月 14 日，GrapheneOS 没有公布 Pixel 11 加入的时间表。Privacy Guides 报道这件事的标题是“GrapheneOS Announces Pixel 11 Support Can Be Completed Now”，GrapheneOS 自己的帖文写的仍是 QPR2 进入 AOSP、移植完成之后。

到 11 月 14 日，Pixel 11 与 MTE 的说法只有 GrapheneOS 一方。Google 8 月 12 日的 Pixel 11 发布文没有提到 MTE，Android Developers 的 QPR2 版本说明也没有 MTE 的条目，本文没有查到 Google 对 Pixel 11 MTE 的说明。

## 导读观点 {#perspective}

依 Privacy Guides 的说明，ARM 芯片的硬件功能 MTE 会为一段内存加上标签，访问它的指针也带同一个标签。两者不符时程序不会继续运行，利用内存安全错误（例如读写到不该访问的内存位置）的攻击因此被挡下。GrapheneOS 的论坛公告写到，MTE 大幅提升了对几乎所有远程攻击与许多本地攻击的防护。

依同一篇公告，Pixel 8 在 2023 年 10 月推出时开始有硬件 MTE。GrapheneOS 当月开始使用，到公告发布时已在整个基础系统启用，包括内核与每个标准的系统进程（少数设备专用的进程暂时关闭）。Android 与 Pixel 原厂系统没有默认启用，Android 16 的高级保护模式只为少数进程开启（高级保护的开启方式见[旧版 iOS 与 Android 被利用的已知漏洞](https://anoni.net/news/2026/11/ios-android-exploits-lockdown/)）。公告也提到 iPhone 17 的 Memory Integrity Enforcement（MIE）一直开启，是用最新标准扩展实现的 MTE。

GrapheneOS 的 FAQ 把硬件内存标记列为未来支持机型的需求，跟至少 5 年的更新、每月完整的 Android 安全公告修补放在同一份清单。GrapheneOS 11 月 7 日在 Bluesky 的帖文提到，要达到跟 iPhone 相比的业界标准漏洞防护就需要 MTE，自从硬件推出就把它当成必要条件。

根据 Google 的更新说明页，Pixel 8 以后的手机从在美国 Google Store 开卖起提供 7 年的系统与安全更新，列表包括 Pixel 11 系列。照 GrapheneOS FAQ 用上市日起算 7 年的方式，本文推算 Pixel 11 约到 2033 年 8 月，Google 的页面没有写结束的月份。留在原厂系统的 Pixel 11 用户照常收到这些更新。依 GrapheneOS 11 月 7 日的帖文，到那天 Google 仍只在 Android 的高级保护模式里为少数进程启用 MTE。

GrapheneOS 在 11 月 6 日的帖文写到，Motorola Signature 27 符合它所有的安全需求，搭载 Qualcomm 的 MTE 实现。帖文也写到 GrapheneOS 将可以为这款手机提供上市起 7 年的更新。同一天的另一则帖文提到，Pixel 11 加入之后，符合全部安全需求的当代机型会有两个系列。

打算买手机安装 GrapheneOS 的人，到 11 月 14 日 FAQ 强烈建议购买的是 Pixel 8、8 Pro、8a、Pixel 9 系列、9a、Pixel 10 系列与 10a。FAQ 的支持年限表里这几款都有上市后 7 年的原厂最低支持，最早结束的 Pixel 8 与 8 Pro 到 2030 年 10 月，最晚的 Pixel 10a 到 2033 年 3 月。FAQ 也提醒，GrapheneOS 只能在原厂持续发布更新时提供完整的安全更新。

依 Google Store 帮助页的列表（2026 年 11 月 14 日重新查看），Pixel 11 系列在亚洲只列了印度、日本、新加坡与台湾，中国大陆、香港、澳门与韩国都不在列表里。这一页只涵盖 Google Store 本身，不代表其他零售渠道没有销售，而 Pixel 11 目前也不在 GrapheneOS 的支持列表上（本文依此推论，亚洲各地都还不能用 Pixel 11 安装 GrapheneOS）。GrapheneOS 的系统更新程序从 `releases.grapheneos.org` 下载更新，GreatFire 对防火长城的测量显示该域名在中国大陆受到干扰（10 月 2 日的最后一次测试是 100% 受干扰，过去 90 天只有 1 次有结果的测试）。依 GrapheneOS 论坛管理者的回复，到 10 月 23 日查证时 GrapheneOS 自己新增的设置与 App 只有英文，设置程序的代码库里沿用 AOSP 的部分则有简体中文的字符串。

已经有 Pixel 11 的人不必做任何设置，原厂系统照常更新。想改装 GrapheneOS 的人，可以留意 Android 17 QPR2 何时推送到 AOSP，以及 GrapheneOS 的 FAQ 与版本记录何时列出 Pixel 11。依 8 月论坛公告的比较，Pixel 10 价格较低、硬件相近也有 MTE，是 GrapheneOS 已经支持的机型。原厂支持结束的时间比 Pixel 11 的推算早一年左右（FAQ 的表上 Pixel 10 到 2032 年 8 月）。
