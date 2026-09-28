---
title: 开源 YouTube 客户端 PipePipe 5.4.0
description: PipePipe 是从 NewPipe 分支出来的 Android 开源客户端，不需要账号与 Google Play 就能观看 YouTube、NicoNico 与 BiliBili。5.4.0 改进了在电视上的操作，也修复了 12 个问题。中国大陆境内的网络无法直接连上 YouTube。
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
  - title: Is http://youtube.com blocked in mainland China?
    url: https://en.greatfire.org/youtube.com
    publisher: GreatFire
    date: 2026-09-21
  - title: Is http://google.com blocked in mainland China?
    url: https://en.greatfire.org/google.com
    publisher: GreatFire
    date: 2026-09-27
  - title: Is http://googleapis.com blocked in mainland China?
    url: https://en.greatfire.org/googleapis.com
    publisher: GreatFire
    date: 2026-08-16
authors:
  - anoni-net
---

采用 GPL-3.0 许可证的 Android 开源客户端 PipePipe 于 9 月 24 日（UTC）发布 5.4.0 版，可以浏览 YouTube、日本的视频平台 NicoNico 与中国的 BiliBili，不需要 Google Play 就能安装。新版改进了在电视上的操作，直播可以选择画质，也修复了进入全屏时字幕消失等 12 个问题。

开发者在 2022 年初从另一款开源 YouTube 客户端 NewPipe 分支出来，之后两个项目不再互相同步更新。官网列出的特点是不需要账号、没有广告与跟踪器、不收集数据。App 整合了 SponsorBlock（用户标记、自动跳过推广片段的服务），可以按关键词或频道过滤内容、隐藏 Shorts，也支持后台播放与下载整个播放列表。

安装渠道有 F-Droid（只收录开源 App 的 Android 仓库）与 IzzyOnDroid（兼容 F-Droid 客户端的第三方仓库），两边都标注了 NonFreeNet 反功能（Anti-Features），意思是 App 依赖非自由的网络服务。截至 9 月 29 日，IzzyOnDroid 已更新到 5.4.0，F-Droid 仍是 9 月 12 日加入的 5.3.1。GitHub 的发布页也提供 APK，按发布说明，多数设备选 `arm64-v8a` 即可。

## 导读观点 {#perspective}

开发者在 GitHub 问题反馈区（issue）置顶的 `#2757` 写明，PipePipe 需要连到 `googleapis.com`、`google.com` 与两者的子域名。GreatFire（监测中国网络审查的网站）记录中，`youtube.com` 最近三次有结论的测试都无法连上（9 月 21 日），`google.com` 最近 23 次有 87% 失败（9 月 27 日），`googleapis.com` 最近三次都受到干扰。由此推断，在中国大陆境内的网络下，PipePipe 很可能无法直接播放 YouTube。

在海外用第三方客户端不必登录 Google 账号，但视频请求仍然直接发往 YouTube，匿名请求受限时 App 会显示“Sign in to confirm you're not a bot”。社区维护的 PipePipe Wiki 写的做法是先重试，再换网络或 VPN 出口。用 DNS 过滤广告的人拦下上述域名时，播放同样会失败，Wiki 的解法是加入允许列表。

PipePipe 也支持登录，README 写明 YouTube 的登录 cookie 只在获取播放流时使用，这些请求也就能对应到账号。Wiki 写明登录最好留给 IP 被封、年龄限制与频道会员内容，登录后不能只下载音频，直播也不能回看。

Wiki 的开发者指南写到，YouTube 越来越多地使用 SABR（客户端与服务器保持连接、分小段传送音视频的流媒体协议）。PipePipe 会从 GitHub 的公开仓库下载播放策略，验证 Ed25519 签名（确认出自开发者、未被篡改）、有效期与版本号之后才执行，失败就退回内置实现。从设计上看，开发者不发布新版本也能调整播放方式，代价是 App 会执行从网络下载的代码。

反馈问题时，Wiki 写明公开的 issue 不要附上 cookie、token 等登录凭证、账号邮箱或登录过程的录屏，也不要公开 IP 地址。第一次反馈写明是否登录与显示的错误信息即可。

海外读者试用需要一部 Android 6.0 以上的手机（根据 F-Droid 的标注），无需 Google 账号。从 GitHub 发布页下载 `arm64-v8a` 的 APK 最直接，想要自动更新，就在 F-Droid 客户端添加 IzzyOnDroid 仓库后安装（官方客户端要手动添加）。界面有简体与正体中文，翻译说明写明两者由 AI 辅助翻译，Wiki 与 issue 则以英文为主。
