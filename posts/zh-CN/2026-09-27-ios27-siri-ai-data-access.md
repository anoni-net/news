---
title: iOS 27 Siri AI 的数据访问设置
description: iOS 27 的新版 Siri 默认可以读取备忘录、信息与邮件，请求可能发到 Apple 的服务器处理。EFF 整理了限制读取范围的设置。Siri 语言设为中文的用户暂时用不到。
date: 2026-09-27T03:21:00+08:00
slug: ios27-siri-ai-data-access
sources:
  - title: How to Limit What Apple's New Siri AI Can Access in iOS 27
    url: https://www.eff.org/deeplinks/2026/09/how-limit-what-apples-new-siri-ai-can-access-ios-27
    publisher: EFF
    date: 2026-09-18
  - title: Turn off and restrict access to Apple Intelligence features on Mac
    url: https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-09-22
  - title: How to get the next generation of Apple Intelligence
    url: https://support.apple.com/en-us/121115
    publisher: Apple
    date: 2026-09-14
authors:
  - anoni-net
---

Apple 在 iOS 27 推出新版 Siri（Siri AI），跟 Spotlight 合并成同一个界面，在主屏幕往下滑打开搜索时，调出的也是 Siri。只有 iPhone 15 Pro、15 Pro Max 与 iPhone 16 之后的机型能使用。到 9 月 27 日为止，Siri AI 还是只支持英文的测试版，也还没有在所有地区开放。Siri 语言设为中文的用户暂时无法使用。

Siri AI 默认可以读取备忘录、信息与邮件等 Apple 自家 App 的内容，第三方 App 需要开发者加入支持才会纳入。请求可能在手机上处理，也可能发到 Apple 的 Private Cloud Compute 服务器，屏幕上不会显示是哪一种。EFF 的文章特别写给开启高级数据保护的用户，他们的 iCloud 数据以端到端加密保存，一旦发出设备交给云端处理，风险评估就跟着改变。

屏幕感知（on-screen awareness）让用户随时调出 Siri，请它解释屏幕上的内容。EFF 举的例子是请 Siri 总结正在看的 Signal 加密群聊，此时屏幕上的数据可能发到 Private Cloud Compute。到 9 月 27 日为止，用户与 App 开发者都无法屏蔽屏幕感知。

要限制 Siri AI 读取某个 App，EFF 建议在「设置」的 App 列表点进该 App，在 Search 关闭 Show Content in Search。要改回旧版 Siri，可以在「屏幕使用时间」开启「内容与隐私访问限制」，再把 Siri 的 Allowed Siri Version 设为 Siri Classic。Siri AI 默认不会用交互记录训练模型，设置过程中如果点了同意，可以到「隐私与安全性」的 Analytics & Improvements 关闭 Improve Siri & Dictation 撤回。以上选项名称照原文的英文界面，中文界面的名称可能不同。

Mac 的做法写在 Apple 的说明页。macOS 27 在「系统设置」关闭 Siri 之后可以改用 Siri Classic，信息、邮件与通知的摘要功能也各有开关。

## 导读观点 {#perspective}

Apple 的支持页写明，Apple 账户地区在中国大陆时，Siri AI 目前无法使用。在中国大陆购买的设备，Apple Intelligence 的功能也都无法使用。Apple Intelligence 本身支持简体中文，Siri AI 则只有英文，所以这篇的设置主要跟 Apple 账户地区不在中国大陆、设备与 Siri 语言都设为英文的人有关。

EFF 在原文写明，Private Cloud Compute 的「Private」代表系统的设计让 Apple 无法看到、也不保存数据，但不保证数据经过加密或留在设备上。使用 Private Cloud Compute 要信任 Apple 的服务器按设计运作，端到端加密则只需要密钥留在用户自己的设备上。

屏幕感知无法屏蔽，加密对话能不能留在设备上，取决于对话里的每一个人。群聊中只要有人对着对话调出 Siri，内容就可能从那个人的手机发出，端到端加密无法保护这一段。在群聊里讨论敏感事务的人，可以跟成员约定不对对话使用屏幕感知，自己也可以考虑改回 Siri Classic。

用户无从得知哪一次请求离开了手机，想继续使用 Siri AI，就只能从源头限制它能读取哪些 App。Apple 账户地区不在中国大陆、使用 iPhone 15 Pro 以后的机型且 Siri 语言设为英文的人，可以对备忘录、邮件这类存有工作资料或个人记录的 App 关闭 Show Content in Search，开启了高级数据保护的人尤其需要。关闭之后，Siri AI 回答一般问题时不会调用该 App 的数据，但屏幕上正在显示的内容仍可能通过屏幕感知发到 Private Cloud Compute。
