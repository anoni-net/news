---
title: iOS 27.2 的 Siri AI 排除 App 设置
description: iOS 27.2 在“设置”的 Siri 加入 Excluded Apps，可以选定不让 Siri、搜索与建议读取的 App。依 EFF 的文章，被排除的 App 连屏幕感知也不运作。iPhone 与 iPad 版的 Siri AI 在欧盟与中国大陆没有提供，到 11 月 2 日支持的语言也不含中文，设备与 Siri 语言设为中文的人暂时用不到 Siri AI。
date: 2026-11-03T00:00:00+08:00
slug: siri-ai-exclude-apps
categories:
  - tracking
follows:
  - 2026-09-27-ios27-siri-ai-data-access
sources:
  - title: About iOS 27 Updates
    url: https://support.apple.com/en-us/149076
    publisher: Apple
    date: 2026-10-26
  - title: "Victory! You Can Now Exclude Apps from Siri AI"
    url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
    publisher: EFF
    date: 2026-10-28
  - title: About iPadOS 27 Updates
    url: https://support.apple.com/en-us/149075
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-10-22
  - title: Siri AI, a profoundly more capable and personal assistant, is here
    url: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/
    publisher: Apple
    date: 2026-09-14
  - title: iOS 和 iPadOS 27 - 功能的供應狀況 - Apple (香港)
    url: https://www.apple.com/hk/ios/feature-availability/
    publisher: Apple
  - title: iOS 和 iPadOS 27 - 功能特色適用範圍 - Apple (台灣)
    url: https://www.apple.com/tw/ios/feature-availability/
    publisher: Apple
  - title: iOS and iPadOS 27 - Feature Availability - Apple (SG)
    url: https://www.apple.com/sg/ios/feature-availability/
    publisher: Apple
authors:
  - anoni-net
---

依 Apple 10 月 26 日发布的版本说明，iOS 27.2 加入 Excluded Apps，用户可以在“设置”的 Siri 里选择 Siri、搜索与建议能读取哪些 App。Siri AI 是 iOS 27 推出的新版 Siri，可以读取 App 的内容回答问题，适用 iPhone 15 Pro、15 Pro Max 与 iPhone 16 之后的机型。Excluded Apps 列在版本说明的 Siri AI 小节，iPadOS 27.2 的版本说明也列了同一项。iPhone 与 iPad 版的 Siri AI 在欧盟与中国大陆没有提供，支持的语言到 11 月 2 日也不含中文，设备与 Siri 语言设为中文的人暂时无法使用 Siri AI。

同一份版本说明写到，Siri AI 在 27.2 增加法文、日文、韩文、葡萄牙文与西班牙文，加上原本的英文共六种。Apple 10 月 22 日发布的“How to get Siri AI”说明页，到 11 月 2 日仍写目前只支持英文，本文以较晚发布的版本说明为准。依 Apple 9 月的新闻稿，Apple Intelligence 的其他功能支持繁体与简体中文，Siri AI 另有自己的语言清单。

EFF 10 月 28 日的文章写到，Excluded Apps 回应了 EFF 在 2026 年稍早“Encrypt It Already”倡议提出的一项要求。文章提到的顾虑是许多 AI 功能需要云端处理，即使系统设计了隐私保护，加密通信 App 的内容仍可能在用户不知情时离开设备。EFF 当初要求让用户能指定操作系统的 AI 不读取某个 App，即使因此少掉一些功能，设置也要简单易懂。

依 EFF 的说明，更新到 27.2 之后在“设置”的 Siri 点进 Excluded Apps，再点 Add Apps 选择要排除的 App。排除之后 Siri AI 无法读取该 App 的内容，也可能少掉部分功能。EFF 举的例子是排除信息 App 之后，就不能请 Siri AI 朗读或回复信息。屏幕感知（叫出 Siri 询问眼前画面内容的功能）对排除的 App 也不再运作，排除 Signal 之后，无法请 Siri 识别 Signal 画面上的任何信息。

EFF 提到 Siri AI 刚推出时，要封锁它读取某个 App 需要切换好几个选项，不然就只能整个关掉 Siri AI。本站 9 月 27 日的导读依 EFF 当时的文章，写到用户与 App 开发者都无法封锁屏幕感知，限制读取的做法是逐一在各 App 关闭 Show Content in Search。27.2 的排除列表集中在一处，也涵盖屏幕感知，EFF 认为少掉功能正好代表设置生效。

文章也检查了 Android 的现状。依 EFF 的说明，在 Gemini App 点用户照片后进入 Settings > Personal Intelligence > Connected Apps，可以撤销不想让 Gemini 读取的 App。EFF 肯定这份列表采用选择加入（opt-in），但认为流程不够直观。Signal 完全不支持 Gemini 的 App 访问功能，所以不在列表上，Gemini 也无法直接读取 Signal 的内容。

不过 EFF 也写到，开启 Connected Apps 里的 Device Assistance 之后，Gemini 可以读取通知。设置计时器等基本功能也需要 Device Assistance，EFF 推测多数人都已经开启。

屏幕情境（screen context）在 Gemini 设置里的选项是 Use screen and app data，位置在 Device controls > Screen context，关闭之后才会停用。Use screen and app data 无法按 App 单独设置。依 EFF 的说明，用户选择使用读取通知与屏幕情境时，两者都可能读取 Signal 的内容或通知。EFF 希望 Google 让用户可以按 App 关闭这两项功能。

## 导读观点 {#perspective}

本站 9 月的导读提到，Siri AI 的请求可能在手机上处理，也可能送到 Private Cloud Compute（Apple 自己运营、处理 AI 请求的云端服务器）。界面上不会显示是哪一种，9 月的导读因此推论，想继续使用 Siri AI 的人只能从源头限制它读取哪些 App。依 EFF 的说明，Siri AI 无法读取被排除的 App 内容，本文据此推论这些内容也不会随请求送出设备。EFF 认为 Apple 应该再进一步，提供只用设备端 AI 功能的选项，类似 Samsung 在 Galaxy AI 提供的做法。

iOS 27.2 的版本说明也列出 Siri AI 可以取用更多来源，包括信息里附的照片、日历活动的参加者、语音留言、Safari 的浏览记录与阅读列表，Siri AI 也能记得过去的对话。依版本说明，已经在用 Siri AI 的人更新之后，Siri AI 能取用的来源比更新前多。

Apple 的版本说明没有写排除之后 Siri 还能做什么，只写这项设置管的是 Siri、搜索与建议。依这句推想，被排除的 App 内容可能也不会出现在搜索与建议里，这是本文的推论。

Android 这一端，EFF 的文章把 Gemini 的 App 列表与 iOS 的排除列表放在一起比较，认为 Android 的流程不如 Apple 的新设置直接。依 EFF 的说明，用 Android 手机与 Gemini 的人可以检查 Connected Apps 里的 Device Assistance 与 Use screen and app data 两处，两者都只能整项关闭。关闭 Device Assistance 也会一并少掉计时器这类基本功能。

设备与 Siri 语言设为中文的人暂时用不到 Siri AI。没有开启 Siri AI 的人在“设置”里是否看得到 Excluded Apps、设置之后会不会影响搜索与建议，到 11 月 2 日 Apple 的说明页都没有写。

Apple 9 月的新闻稿写到，Siri AI 与其他新的 Apple Intelligence 功能在 Apple 处理监管要求期间不会在中国提供。10 月 22 日的“How to get Siri AI”说明页写明，账户地区在中国大陆时 Siri AI 目前无法运作，两处都没有写时间表。Apple 香港、台湾、新加坡的功能可用性页到 11 月 2 日仍写支持英文，并注明不适用于中国大陆与欧盟。这几页的内容可能还没有随 27.2 更新，这是本文的推测。

已经开启 Siri AI 的人更新到 iOS 27.2 之后，可以到“设置”的 Siri 点 Excluded Apps 加入要排除的 App（选项名称照 EFF 文章的英文界面）。依 EFF 的说明，偏好旧版的人目前仍可以关闭 Siri AI、改回 Siri Classic。排除列表只管自己的手机，本文推论群组里其他成员没有排除同一个 App、又对同一段对话叫出 Siri AI 时，内容仍可能从对方的手机送出。
