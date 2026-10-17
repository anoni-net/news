---
title: Apple 对 Mac「完全磁盘访问权限」的授权预告
description: Apple 10 月 2 日预告之后会让 Mac 用户只能通过非常明确的操作授予「完全磁盘访问权限」。理由包括部分开发者的用法可能让用户数据暴露，以及 AI 智能体会让风险增加。Apple 没有写版本与上线时间，到 10 月 12 日为止版本说明都没有写到这项控制。
date: 2026-10-15T00:00:00+08:00
slug: apple-full-disk-access
categories:
  - tracking
follows:
  - 2026-10-09-muse-dots-agent-memory-permissions
sources:
  - title: Updates to Full Disk Access in macOS
    url: https://developer.apple.com/news/?id=p6zjojqw
    publisher: Apple
    date: 2026-10-02
  - title: 在 Mac 上更改「隱私權與安全性」設定
    url: https://support.apple.com/zh-tw/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: macOS 27 Golden Gate Release Notes
    url: https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes
    publisher: Apple
  - title: macOS 27.2 Golden Gate Beta 3 Release Notes
    url: https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes
    publisher: Apple
  - title: Meta disputes claim that Muse read a user's private messages without permission
    url: https://techcrunch.com/2026/09/30/meta-disputes-claim-that-muse-read-a-users-private-messages-without-permission/
    publisher: TechCrunch
    date: 2026-09-30
  - title: Meta Pushes Back on Claim That Muse AI Read a User's Messages Without Consent
    url: https://decrypt.co/379868/meta-muse-ai-agent-read-messages-without-permission
    publisher: Decrypt
    date: 2026-10-01
  - title: Apple says it's tightening macOS 'Full Disk Access' controls due to new risks from AI agents
    url: https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/
    publisher: TechCrunch
    date: 2026-10-02
  - title: Apple changes full-disk access permissions to curb abuse from AI agents
    url: https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/
    publisher: Ars Technica
    date: 2026-10-02
  - title: 蘋果將增加macOS完全磁碟存取的開關控制
    url: https://www.ithome.com.tw/news/179400
    publisher: iThome
    date: 2026-10-05
  - title: Apple Tightens "Full Disk Access" Permission on macOS in Light of AI Agent Security Concerns
    url: https://www.privacyguides.org/news/2026/10/06/apple-tightens-full-disk-access-permission-on-macos-in-light-of-ai-agent-security-concerns/
    publisher: Privacy Guides
    date: 2026-10-06
  - title: Meta VP of Communications on X
    url: https://x.com/andymstone/status/2105107596734849423
    publisher: X
    date: 2026-09-30
  - title: "Microsoft Execution Containers: Policy-driven containment for AI agents"
    url: https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/
    publisher: Microsoft
    date: 2026-10-07
  - title: Microsoft eXecution Container (MXC)
    url: https://github.com/microsoft/mxc
    publisher: GitHub
  - title: 在 Mac 上更改隐私与安全设置
    url: https://support.apple.com/zh-cn/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: ChatGPT Supported Countries
    url: https://web.archive.org/web/20261011164107/https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: 生成式人工智能服务管理暂行办法
    url: https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
    publisher: 国家互联网信息办公室
    date: 2023-07-13
  - title: Muse from Meta App - App Store
    url: https://apps.apple.com/us/app/muse-from-meta/id6760173601
    publisher: App Store
authors:
  - anoni-net
---

Apple 10 月 2 日在开发者新闻预告，之后会为 macOS 的「完全磁盘访问权限」加入额外的控制，让真的想授予这项权限的用户只能通过非常明确的操作完成。Apple 没有写是哪个版本、何时上线、界面是什么样子，也没有写已经授权的 App 要不要重新确认。到 10 月 12 日为止，macOS 27 与 27.2 第三个测试版的版本说明都没有写到这项新控制。

Apple 的预告提到，为了让备份 App 在 Mac 上正常运行，完全磁盘访问权限大致绕过了保护用户数据的其他控制。Apple 也写到，有些开发者使用这项权限的方式，可能让用户在不完全知情下暴露文件、邮件、消息甚至浏览记录。预告也提到，AI 智能体（能代替用户操作电脑、读取文件与 App 的 AI 程序）越来越能自主行动，这类权限的风险会大幅增加。TechCrunch 的报道发出后补了更正，把原本写的「限制权限」改成增加知情同意的步骤，并注明这不是新的限制。

预告发出前几天，依 TechCrunch 与 Decrypt 的转述，一位专栏作者声称 Meta 的 AI 智能体 Muse 的 Mac 版在完全磁盘访问权限关闭时读到他的私人消息（10 月 9 日的导读写过这件事）。依 Decrypt 的转述，作者设置时拒绝给消息权限，之后发现 Muse 已同步了 Mac 本机的「信息」App 数据库。Meta 传播副总裁 9 月 30 日在 X 表示，要同时开启完全磁盘访问权限与 Muse 内的 Messages 连接器，Muse 才能读取消息。Apple 的预告没有点名任何 App 或开发者，把两者写成互相反驳的，是 Ars Technica 与 iThome 的解读。

## 导读观点 {#perspective}

完全磁盘访问权限是操作系统层级的权限，Apple 的帮助页介绍它让 App 访问电脑上所有文件，包括「邮件」、「信息」等其他 App 的数据与时间机器备份。Ars Technica 引述的一位 macOS 安全专家表示，取得这项权限的程序读得到浏览记录、浏览器 cookie 与聊天内容等文件。Meta 一位主管则表示，读取消息要经过 App 内的权限设置与 macOS 系统层级的保护，即使 App 有错误也无法绕过（TechCrunch 的转述）。Apple 的帮助页与安全专家描述的是取得权限后 App 读得到什么，Meta 的说法描述的是 Muse 要经过哪些授权步骤。

Microsoft 10 月 7 日发布的 Microsoft Execution Containers（MXC）是另一种做法。依 Microsoft 的博客，开发者或 IT 管理员用策略定义 AI 智能体能读写哪些文件、连到哪些网络，策略放在智能体能控制的范围之外。MXC 以 MIT 许可证开源，在 macOS 上使用 Seatbelt 沙盒（限制程序能访问哪些资源的机制）。README 的描述是嵌进 App 的套件，Microsoft 列出已支持的工具有 GitHub Copilot、OpenAI Codex 等（名单里没有 Muse 或 ChatGPT），本文推论一般用户不会直接配置它。

Microsoft 与 Apple 的文件都没有提到对方，本文把两者并列，差别在由谁把关。Apple 预告的做法是在授权那一刻让用户更清楚自己给出了什么，MXC 则是由开发者事先限定智能体能碰的范围。Apple 的预告没有写到新控制会不会改变完全磁盘访问权限能读到的范围。之后可以留意 macOS 的版本说明何时出现这项控制，以及已授权的 App 要不要重新确认。

Muse 的 App Store 页面只有美国区，中国大陆区的同一网址打不开，Meta 的公告也只写 Muse 在美国推出。ChatGPT 的支持国家与地区名单（OpenAI 说明页 10 月 11 日的存档）没有中国大陆、香港与澳门。国家网信办等七部门的《生成式人工智能服务管理暂行办法》2023 年 8 月 15 日施行，规范向境内公众提供的生成式 AI 服务，第二十条规定境外服务不符合规定时应采取技术措施予以处置。本文没有查这些服务未在中国大陆提供的原因，也没有查是否有服务依此条被处置。

用 Mac 的读者现在就可以打开「系统设置」的「隐私与安全」，在「完全磁盘访问权限」查看哪些 App 取得了这项权限。看到不认识的 App，可以先查清楚它为什么需要这项权限，备份类的 App 正是 Apple 预告提到的用途。Apple 的帮助页只写了添加 App 的步骤，Meta 则表示 Muse 的授权可以随时撤销。授权之前可以先想清楚，这项权限让 App 读得到别人发给你的消息与浏览记录，这部分的判断 Apple 的新控制上线之后仍然要由用户自己做。
