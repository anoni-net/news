---
title: Signal 对操作系统 AI 助理的截图封锁与限制
description: Signal 在 iOS 与 Android 版限制操作系统内置的 AI 助理获取对话，Mac 版没有这项保护，Mac 用户要自行在系统设置里把 Signal 排除在 Siri 之外。到 11 月 29 日，Siri AI 不支持中文，Gemini 自动读取屏幕的屏幕情境限用英文。对话另一端的人开了这些功能时，自己的消息一样可能被读取。
date: 2026-11-30T00:00:00+08:00
slug: signal-ai-agent-screenshots
categories:
  - encryption
follows:
  - 2026-11-03-siri-ai-exclude-apps
sources:
  - title: Signal is Serious About Protecting Your Privacy
    url: https://signal.org/blog/protecting-your-privacy/
    publisher: Signal
    date: 2026-11-20
  - title: By Default, Signal Doesn't Recall
    url: https://signal.org/blog/signal-doesnt-recall/
    publisher: Signal
    date: 2025-05-21
  - title: "Add 'Block Siri AI' setting to Settings > Privacy"
    url: https://github.com/signalapp/Signal-iOS/commit/9256c9583
    publisher: Signal-iOS（GitHub）
    date: 2026-11-02
  - title: AssistantScreenSecurityObserver.kt
    url: https://github.com/signalapp/Signal-Android/blob/main/app/src/main/java/org/thoughtcrime/securesms/components/AssistantScreenSecurityObserver.kt
    publisher: Signal-Android（GitHub）
  - title: Signal Moves to Block AI Agents
    url: https://www.eff.org/deeplinks/2026/11/signal-now-blocks-ai-agents
    publisher: EFF
    date: 2026-11-24
  - title: "Victory! You Can Now Exclude Apps from Siri AI"
    url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
    publisher: EFF
    date: 2026-10-28
  - title: About iOS 27 Updates
    url: https://support.apple.com/en-us/149076
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-11-12
  - title: Use screen actions to chat with the Gemini mobile app
    url: https://support.google.com/gemini/answer/15850607?hl=en
    publisher: Google
  - title: Signal blocks screenshots by Apple, Google operating systems to protect data from AI agents
    url: https://therecord.media/signal-no-screenshots-by-apple-google-operating-systems
    publisher: The Record
    date: 2026-11-23
  - title: Siri AI, a profoundly more capable and personal assistant, is here
    url: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/
    publisher: Apple Newsroom
    date: 2026-09-14
  - title: Where you can use the Gemini web app
    url: https://support.google.com/gemini/answer/13575153?hl=en
    publisher: Google
  - title: Gemini mobile app availability
    url: https://support.google.com/gemini/answer/14579026?hl=en
    publisher: Google
authors:
  - anoni-net
---

Signal 宣布在 iPhone 与 Android 版限制操作系统内置的 AI 代理（能替用户读取屏幕、操作 App 的 AI 助理）获取对话，Mac 版没有这项保护。到 11 月 29 日，Apple 的 Siri AI（iOS 27 推出的新版 Siri）不支持中文，Google 的 Gemini 自动读取屏幕的屏幕情境也限用英文。依 Signal 的博客，数据被获取之后受影响的是对话里的所有人，包含另一端开了这些功能的人。

操作系统的 AI 代理靠扫描屏幕获取信息，Signal 11 月 20 日的博客提到 Google 与 Apple 把 Gemini 与 Siri AI 这类代理功能深度整合进操作系统，Signal 的对话因此被获取。依 Signal 的说法，获取的内容会存进代理当下使用的本地数据库或远程服务器，之后就不在 Signal 的控制范围内。Signal 在 2025 年 5 月处理过类似的问题，当时在 Windows 11 默认开启 Screen security（让 Signal 画面无法被截图的设置），挡下 Microsoft Recall。

iPhone 上的 Signal 在 iOS 27 直接挡下截图，App 内与 App Switcher（切换 App 时显示的缩略图画面）都包括在内。设置叫 Block Siri AI（封锁 Siri AI），位在 Signal 的隐私设置里，名称出自 Signal-iOS 的源代码。想截图的人可以关掉这项设置，电子前哨基金会（EFF）11 月 24 日的文章写明它默认开启。

Android 版在检测到 AI 助理要求读取屏幕时才自动打开 Screen security，之后 Signal 里的画面都不能截图，直到用户关掉。Signal 的博客提到，在 Pixel 以外许多厂商的 Android 上，Signal 停用截图之后就无法可靠地得知用户试过截图。直接停用截图会让截图无声失效、让用户困惑，所以 Signal 改成检测 AI 助理。自动打开时会弹出提示让用户再关闭，Signal-Android 的源代码写明关闭之后 90 天内不会再提示。

Signal 在博客要求操作系统厂商提供开发者简单、有文档的方式，让 App 退出 AI 的读取与处理。The Record 的报道写到，Apple 没有立即回应，Microsoft 与 Google 拒绝评论。

## 导读观点 {#perspective}

端到端加密保护的是消息在传输途中与服务器上的内容，只有对话双方的设备能解开。消息显示在屏幕上时已经解密，操作系统能获取的画面内容跟用户看到的相同，所以内置的 AI 读取屏幕不需要破解任何加密。Signal 的博客把这件事写成操作系统的 AI 功能削弱了 Signal 独立保证隐私的能力。

挡下截图无法涵盖其他可能的途径，例如 AI 代理可能通过文件系统读取设备上已有的内容，Signal 在博客里也称这次补救不完整。依 Signal 的说明，Mac 版没有封锁 Siri AI 是因为找不到可靠挡下截图的 API（应用程序接口）。多数代理正是用截图读取 App 的数据，macOS 却只对持续的屏幕录制有防护。Signal 给 Mac 用户的建议因此改从系统设置着手。

群组里有成员关掉保护、使用 Mac，或用的是无法检测到 AI 助理的 Android 机型时，对话内容仍可能从那个人的设备被 AI 读取。Signal 的博客提到，关掉保护可能让自己与联系人的 Signal 内容都暴露给 AI 代理。

操作系统的设置只跟开了 Siri AI 或 Gemini 屏幕情境的人有关，Signal 的设置则每个用 Signal 的人都该看一次。更新 App 之后，iPhone 用户可以到 Signal 的隐私设置确认 Block Siri AI 是否开启，Android 用户看到提示时可以选择保留 Screen security。Signal-Android 的源代码显示检测到助理时打开的就是同一个 Screen security，所以不必等提示就能自行打开，代价是 Signal 里无法截图。

到 11 月 29 日，Apple 账户地区在中国大陆时 Siri AI 无法运作，Apple 9 月的新闻稿写明处理监管要求期间 Siri AI 不会在中国提供。使用 Siri AI 的前提是设备语言与 Siri 语言设为同一种支持的语言，说明页列出的六种语言不含中文。到 10 月 20 日，Gemini 手机 App 的支持地区清单里没有中国大陆，网页版在中国大陆只限 Workspace 账号。

Apple 这一侧已有用户能调整的设置，iOS 27.2 在“设置”的 Siri 加入 Excluded Apps（排除的 App 列表），可以选定不让 Siri、搜索与建议读取的 App。macOS 27 的“系统设置”也有同一项，Signal 给 Mac 用户的唯一建议就是把 Signal 加入列表，防止 Siri AI 主动读取消息内容。依 EFF 10 月的文章，排除 Signal 之后，连呼叫 Siri 询问 Signal 屏幕上的内容也无法取得回答。Signal 的 Block Siri AI 是让 Signal 里无法截图，属于另一种机制，iPhone 用户可以两项都开。

Android 上用 Gemini 的人可以关闭自动读取屏幕的屏幕情境，位置在 Gemini 设置的 Screen context，分成 Use text from screen（使用屏幕上的文字）与 Use screenshot（使用截图）两项。Google 的说明页没有按 App 单独设置的选项，EFF 10 月的文章也写明没有，到 11 月 29 日只能对所有 App 一起关闭。手动点“Ask about…”询问屏幕内容的功能不受这两项影响。
