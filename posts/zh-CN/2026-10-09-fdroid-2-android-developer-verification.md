---
title: F-Droid 2.0 与 Google 的 Android 开发者验证
description: 开源应用商店 F-Droid 9 月 24 日推出全面重写的 2.0，最低需要 Android 7。Google 9 月 30 日起在巴西、印度尼西亚、新加坡、泰国要求七家商店的应用由验证身份的开发者注册，2027 年扩大到全球的认证 Android 设备。截至 10 月 2 日，各地从 F-Droid 安装应用都不受影响。
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
  - title: 利用 Google Play 保护机制保障应用的安全性和数据的私密性
    url: https://support.google.com/googleplay/answer/2812853?hl=zh-Hans
    publisher: Google
  - title: "OONI Explorer: f-droid.org, China"
    url: https://explorer.ooni.org/chart/mat?probe_cc=CN&test_name=web_connectivity&domain=f-droid.org&since=2026-06-01&until=2026-10-02&axis_x=measurement_start_day
    publisher: OONI
  - title: F-Droid 镜像使用帮助
    url: https://mirrors.tuna.tsinghua.edu.cn/help/fdroid/
    publisher: 清华大学 TUNA 协会
  - title: F-Droid 2.0：Android 自由的新篇章
    url: https://f-droid.org/zh_Hans/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html
    publisher: F-Droid
    date: 2026-09-24
  - title: Google Play 中应用和数字内容的推出国家/地区
    url: https://support.google.com/googleplay/answer/2843119?hl=zh-Hans
    publisher: Google
authors:
  - anoni-net
---

开源的 Android 应用商店 F-Droid 在 9 月 24 日推出 2.0，客户端整个重写，最低需要 Android 7。9 月 30 日起，Google 在巴西、印度尼西亚、新加坡、泰国要求 Google Play 与六家手机厂商商店上架的应用由验证过身份的开发者注册，预计 2027 年扩大到全球的认证 Android 设备。截至 10 月 2 日，各地的读者从 F-Droid 或网站直接下载安装应用都不受影响。

F-Droid 只收录开源应用，依 F-Droid 的说明，团队会审查公开的源代码、确认没有广告与追踪器，再自行构建发布。2.0 改用 Kotlin 与 Jetpack Compose 编写，界面缩减为发现、搜索与我的应用三个标签页。应用更新改为默认自动下载安装，已经调整过的偏好设置会保留。F-Droid 的 2.0 公告也写到搜索改善了中文、日文、韩文的支持。

2.0 经过独立的安全审查，公告写明完整报告确认可以发表后才会公开。原本的“使用 Tor”改成一般的代理设置，公告建议改用 Tor VPN。紧急删除应用的功能暂时移除了，公告建议依赖这项功能的人推迟更新。截至 10 月 2 日，F-Droid 首页提供下载的是 2.0.1，软件包页面则仍把 2.0 标为测试版，建议版本是 1.23.2。

开源即时通信应用 Conversations 的开发者 9 月 24 日在博客写到 Google Play 一再退回应用的更新、应用也被下架过两次，文章发表时还有一个更新已经等了 14 天审核。开发者认为 Google 不区分功能更新与安全更新，安全更新延迟数日是危险的。关于 Google Play 的审核，截至 10 月 2 日只看到开发者一方的说法。

Conversations 开发者的文章也写明 F-Droid 已成为主要的分发渠道，F-Droid 上的版本改为可重现构建（任何人都能从源代码构建出相同的文件），由开发者自己的密钥签名。原本收费的 Google Play 版本截至 10 月 2 日已改为免费。

Google 的开发者验证要求开发者证明身份，并以私钥签名的安装包（APK）登记包名，Google 借此把应用对应到开发者账号。截至 10 月 2 日，Google 的常见问题写明第一阶段只限七家参与的商店，其他商店与侧载（不经商店直接安装）不受影响。2027 年扩大后，认证设备上没有注册的应用只能用开发者工具 ADB 安装，或通过 Google 称为 advanced flow 的流程开放安装。Google 的帮助中心另外写明 AOSP（Android 开源项目）的设备、未经认证的设备，以及 Google 移动服务不支持的地区都不适用这项要求。

advanced flow 要先在系统设置开启开发者模式，并确认自己没有被人在旁指导操作，接着重启手机并重新验证身份。之后有一次性的一天等待期。期满后用指纹、人脸识别或 PIN 确认，就能选择开放 7 天或无限期安装未验证开发者的应用。

## 导读观点 {#perspective}

两种做法对“这个应用能不能信任”有不同的答案。Google 要求开发者证明身份，F-Droid 的信任则来自公开的源代码，应用由 F-Droid 的密钥签名，可重现构建的应用则改用原开发者的密钥。依 Google 的规则，包名要由开发者本人注册。F-Droid 在 2025 年 9 月的公告表示无法要求开发者向 Google 注册，也不能替开源应用接管包名。

Google 在 2025 年 8 月的公告写到，依 Google 自己的分析，网络侧载来源的恶意软件是 Google Play 上的 50 倍以上。公告也写明第一阶段选在受诈骗应用影响的国家，并引述印度尼西亚、泰国主管机关的正面评价。F-Droid 在 2026 年 7 月的文章则指出，Android 开发者控制台的条款写明分发恶意软件可以终止账号，但没有定义什么是恶意软件。

多个自由软件与数字权利组织参与的 Keep Android Open 列出 advanced flow 的九个步骤，并指出这个流程由 Google Play 服务提供、不在 Android 系统本身，因此 Google 可以随时更改。Google 的常见问题写明一天的等待期是为了打断诈骗者在电话上催促受害者立刻更改安全设置。常见问题也写明开启 advanced flow 之后不必保持开发者模式，用 ADB 安装也不受等待期限制。

F-Droid 在 2026 年 2 月发表公开信，建议开发者现在与将来都不要注册。F-Droid 在 2025 年的公告也表示，这项规定会终结 F-Droid 与其他开源分发渠道现在的运作方式。Google 则为开源平台写了注册指南。依指南，开发者以自己的账号登记包名，会重新签名的平台另外提供平台密钥的指纹，用户就能维持现在的安装方式。

截至 10 月 2 日，Google Play 不在中国大陆提供服务，Google 的帮助中心也没有逐一列出哪些地区属于 Google 移动服务不支持的范围，没有写明中国大陆是否适用这项要求。F-Droid 本身在中国大陆能否连上是另一个问题。网络审查观测项目 OONI 在 2026 年 6 月 1 日到 10 月 2 日之间，从中国大陆对 `f-droid.org` 做了 1506 次连接测试，其中 1179 次出现异常，288 次测量失败，37 次正常，另有 2 次被 OONI 确认遭到封锁。

清华大学 TUNA 协会提供 F-Droid 的镜像，截至 10 月 1 日与官方仓库保持同步，帮助页面说明可以在客户端里添加这个镜像。TUNA 的帮助页面也引述了 F-Droid 的提醒：第一次安装时 `f-droid.org` 是官方下载地址，从其他来源下载要提防伪造的客户端。

截至 10 月 2 日，F-Droid 2.0 的界面与分类名称都有完整的简体中文，依赖紧急删除应用功能的人可以先使用软件包页面建议的 1.23.2。在中国大陆第一次安装的人如果连不上官方地址，可以改用 TUNA 帮助页面列出、由 F-Droid 团队提供的替代下载来源，包括 GitLab 与 GitHub 上的发布页面。

在海外使用 Google Play 的读者，可以在 Google Play 商店点右上方的个人资料图标，在“设置”的“关于”查看设备是否通过 Play 保护机制认证。依 Google 的计划，2027 年之后在认证设备上安装未注册开发者的应用，要提前一天开启 advanced flow，关闭 advanced flow 之后，这些应用会无法更新。截至 10 月 2 日，Google 只写了 2027 年扩大到全球，月份与各地的先后顺序都没有公布。
