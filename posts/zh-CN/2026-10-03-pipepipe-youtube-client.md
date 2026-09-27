---
title: 开源 YouTube 客户端 PipePipe 5.4.0
description: PipePipe 是从 NewPipe 分支出来的 Android 开源客户端，不需要账号就能观看 YouTube、NicoNico 与 BiliBili。9 月 24 日发布的 5.4.0 改进了电视操作，也修复了多项播放问题。
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
  - title: Is http://youtube.com blocked in mainland China?
    url: https://en.greatfire.org/youtube.com
    publisher: GreatFire
    date: 2026-09-21
authors:
  - anoni-net
---

PipePipe 于 9 月 24 日发布 5.4.0 版，是一款可以浏览 YouTube、NicoNico 与 BiliBili 的 Android 开源客户端，采用 GPL-3.0 许可证。开发者在 2022 年初从 NewPipe 分支出来独立开发，之后两个项目不再互相同步更新。

官网列出的特点包括不需要账号、没有广告与跟踪器、不收集数据，并整合 SponsorBlock 跳过推广片段，可以按关键词或频道过滤内容、隐藏 Shorts，支持后台播放与下载整个播放列表。5.4.0 改进了电视的操作，直播可以选择画质，也修复了全屏时字幕消失等十多个问题。

安装渠道有 F-Droid 与 IzzyOnDroid，两边都标注了 NonFreeNet 反功能，意思是 App 依赖非自由的网络服务。撰稿时 IzzyOnDroid 已更新到 5.4.0，F-Droid 仍是 9 月 12 日加入的 5.3.1。也可以从 GitHub 的发布页直接下载 APK，发布说明建议多数手机选择 arm64-v8a 版本，F-Droid 标注需要 Android 6.0 以上。

## 导读观点 {#perspective}

在中国大陆，GreatFire 9 月 21 日的测试显示 youtube.com 处于完全封锁状态。项目文档写明 PipePipe 需要连到 googleapis.com 与 google.com 的子域名，所在网络连不上这些域名时，所有 YouTube 视频都会播放失败。在海外使用 DNS 广告过滤的人，也要把这两组域名加入允许清单。

第三方客户端的好处是不必登录 Google 账号，订阅分组与离线播放列表都在 App 内管理。视频请求仍然直接发往 YouTube，YouTube 限制匿名请求时会出现“Sign in to confirm you're not a bot”，项目文档建议换一个网络或 VPN 出口再试。PipePipe 也支持登录，说明写到登录 cookie 只在获取播放流时使用，但登录之后这些请求就与账号关联在一起。

YouTube 逐步改用 SABR 协议传送音视频，PipePipe 为了跟上，会从 GitHub 的公开仓库下载一份经 Ed25519 签名的播放策略代码，验证签名、有效期与版本号之后才执行，失败时退回内置实现。开发者因此不必发新版就能调整播放逻辑，源代码也公开可供审阅，代价是 App 会执行从网络下载的代码。界面有简体与繁体中文，项目的翻译说明写到这两种语言由 AI 辅助翻译，用词不顺的地方可以直接提交 PR 修改。

反馈问题时也有隐私上的细节要注意。项目文档提醒，公开的 issue 不要附上 cookie、token、账号邮箱或登录过程的录屏，也不要公开 IP 地址，写明是否登录与看到的错误信息就足以开始排查。
