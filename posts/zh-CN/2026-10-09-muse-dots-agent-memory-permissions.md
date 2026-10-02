---
title: Meta Muse 与 OpenAI Dots 的记忆与权限设计
description: Meta 的 Muse 与 OpenAI 的 Dots 都在 9 月推出，在云端常驻、读取连接的应用数据并整理成记忆。截至 10 月 2 日，OpenAI 的支持清单不含中国大陆，Muse 在中国大陆的 App Store 没有上架，在海外使用 ChatGPT 或 Mac 的人可以先检查记忆与权限设置。
date: 2026-10-09T00:05:00+08:00
slug: muse-dots-agent-memory-permissions
sources:
  - title: "Introducing Muse: The World’s First Personal AI Agent Built for Everyone"
    url: https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
    publisher: Meta
    date: 2026-09-08
  - title: How to manage your Muse data
    url: https://www.meta.com/help/artificial-intelligence/2225571704857152/
    publisher: Meta
  - title: Introducing dots
    url: https://openai.com/index/introducing-dots/
    publisher: OpenAI
    date: 2026-09-29
  - title: Dots privacy, security, and safety FAQs
    url: https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
    publisher: OpenAI
  - title: Getting started with your dot
    url: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
    publisher: OpenAI
  - title: Meta’s Muse AI surprises users — but not in a good way
    url: https://freedom.press/digisec/blog/metas-muse-ai-surprises-users-but-not-in-a-good-way/
    publisher: Freedom of the Press Foundation
    date: 2026-09-30
  - title: Muse, Meta's extraordinarily privileged AI assistant, has a serious 0-day
    url: https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/
    publisher: Ars Technica
    date: 2026-09-21
  - title: I asked Meta’s Muse for its filesystem and it sent me 6.8 GB
    url: https://mouse.dev/blog/muse-runtime-export/
    publisher: mouse.dev
    date: 2026-09-22
  - title: Yeah, don't give Meta's Muse app access to your Mac
    url: https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/
    publisher: 9to5Mac
    date: 2026-09-28
  - title: Meta's Muse AI Agent Read a User's Private iMessages. Then It Lied About How
    url: https://decrypt.co/379122/metas-muse-ai-agent-user-private-imessages-lied-how
    publisher: Decrypt
    date: 2026-09-23
  - title: ChatGPT can now send texts for you with new Apple Messages plug-in
    url: https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/
    publisher: TechCrunch
    date: 2026-08-20
  - title: ChatGPT gets all up in your iMessages
    url: https://freedom.press/digisec/blog/chatgpt-gets-all-up-in-your-imessages/
    publisher: Freedom of the Press Foundation
    date: 2026-08-26
  - title: Memory in ChatGPT
    url: https://help.openai.com/en/articles/8590148-memory-faq
    publisher: OpenAI
  - title: Data controls in ChatGPT
    url: https://help.openai.com/en/articles/7730893-data-controls-faq
    publisher: OpenAI
  - title: 在 Mac 上更改「隱私權與安全性」設定
    url: https://support.apple.com/zh-tw/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: Premium seats are coming to ChatGPT Business
    url: https://openai.com/index/premium-seats-chatgpt-business/
    publisher: OpenAI
  - title: 允許輔助使用 App 取用 Mac
    url: https://support.apple.com/zh-tw/guide/mac-help/mh43185/mac
    publisher: Apple
  - title: 允许无障碍 App 访问你的 Mac
    url: https://support.apple.com/zh-cn/guide/mac-help/mh43185/mac
    publisher: Apple
  - title: Muse from Meta App
    url: https://apps.apple.com/us/app/muse-from-meta/id6760173601
    publisher: App Store
  - title: Warning sources against using AI chatbots
    url: https://securedrop.org/news/updated-landing-page-guidance/
    publisher: SecureDrop
    date: 2026-09-24
  - title: 在 Mac 上更改隐私与安全设置
    url: https://support.apple.com/zh-cn/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: "OONI Explorer: chatgpt.com, China"
    url: https://explorer.ooni.org/chart/mat?probe_cc=CN&test_name=web_connectivity&domain=chatgpt.com&since=2026-09-01&until=2026-10-01&axis_x=measurement_start_day
    publisher: OONI
authors:
  - anoni-net
---

Meta 在 9 月 8 日推出 Muse，OpenAI 在 9 月 29 日推出 Dots。两者都是 AI 智能体，也就是能自行替用户执行一连串工作的 AI 助手。它们在云端持续运行，读取用户连接的应用与服务、整理成记忆，再主动处理事情。Meta 的公告写明 Muse 先在美国推出，Dots 截至 10 月 2 日只开放给 ChatGPT 的 Pro 与 Business Premium 方案。

Muse 有 iPhone、Android 与网页版，Meta 的公告写到大部分功能免费，另有付费方案，美国 App Store 页面列出的界面语言包含简体与繁体中文。新闻自由组织 Freedom of the Press Foundation（FPF）的电子报转述一位用户的说法，Muse 替用户在 Facebook Marketplace 卖键盘时接受了用户不满意的价格，把住址给了买家，买家上门时也没有通知用户。截至 10 月 2 日，我们没有看到 Meta 对这个案例的回应。FPF 也提醒，Muse 默认会用用户的互动记录训练 Meta 的模型。

9to5Mac 与 Decrypt 报道了一位科技专栏作者在 Mac 上测试 Muse 的经过。作者在设置时拒绝了「信息」权限，之后 Muse 的建议却用到作者与节目搭档的对话。Decrypt 写到读取 Mac 的「信息」数据库需要完全磁盘访问权限。Meta 一位主管在 Threads 回应「信息」访问是需要用户自行开启的功能，作者则表示拒绝之后 Muse 的设置里仍显示该访问为开启。

研究者也找到 Muse 的其他问题。Ars Technica 9 月 21 日报道一个让其他应用与终端命令可以控制 Muse 的漏洞，并写到 Meta 在报道刊出约 12 小时后发布修复。另一位研究者取得了 Muse 所在的整个云端运行环境，解压后有 6.8 GB。这位研究者通过 Meta 的漏洞奖励计划提交发现，Meta 标为不适用，回复列出几种可能的理由，但没有指明适用哪一种。

Dots 的每个 dot 是一个独立的助手，有自己的云端电脑，通过插件连接其他应用。依 OpenAI 的帮助页面，用户没有交办工作时，dot 会读取已连接的数据并写进自己的笔记，这个阶段不能发消息、修改内容或操作浏览器。截至 10 月 2 日，帮助页面写明单条记忆无法查看、删除或直接修改，要删只能删掉整个 dot。删掉 dot 时，它创建的文件与对话另外存放，不会一起删除。

帮助页面也谈到提示注入，也就是网页、电子邮件或文件里藏着要 dot 执行用户没交办动作的指令，OpenAI 写的是防护能降低风险，但无法消除。OpenAI 也写明在支持的登录流程里，密码经由独立的表单送进浏览器环境、不经过模型，在聊天、文件或插件里提供的密码则不在保护范围。Dots 只能在电脑上创建，未满 18 岁不能使用。截至 10 月 2 日，Dots 的说明只见于 OpenAI 自己的文件，还没有独立的检验报告。

## 导读观点 {#perspective}

两个产品都替用户在云端开一台常驻的电脑，连接的数据在后台被读取、整理成记忆，之后的回答与行动都以这份记忆为基础。截至 10 月 2 日，Dots 的记忆只能连同整个 dot 一起删除。Muse 的记忆存在一个可以直接查看与编辑的文件里，但 Meta 的帮助页面写明，删除之后 Muse 仍可能记得从中学到的内容。

两者的训练设置也不同。Muse 的「Help improve our AI models」在第一次使用时默认开启，Meta 写明关闭之后也适用于过去的互动。OpenAI 的公告写明，个人方案可以控制 dot 的对话与工作是否用于改进模型。ChatGPT 一般对话的训练设置是「Improve the model for everyone」，OpenAI 的帮助页面写明关闭之后只对新对话生效，但没有写这个设置在个人方案的默认值。

截至 10 月 2 日，OpenAI 的支持国家与地区清单里没有中国大陆、香港与澳门，Muse 在中国大陆的 App Store 也没有上架，网页版是否可用我们没有查证。测量网络审查的项目 OONI 在 9 月从中国大陆对 `chatgpt.com` 做了 57 次连接测试，44 次出现异常，12 次测量失败，1 次正常。异常代表有受到干扰的迹象，不等于确认被封锁，测量失败则是测试本身没有完成。境内读者不需要为这两个产品调整设置。

OpenAI 8 月推出的 ChatGPT「信息」插件，能读取、摘要、草拟与发送 Mac「信息」应用里的消息，设置时要开启完全磁盘访问权限。TechCrunch 转述 OpenAI 的说明，消息内容存在用户的电脑上、不存到服务器，FPF 则提醒使用 ChatGPT 时 OpenAI 仍会处理对话内容。Apple 的帮助页面写明，完全磁盘访问权限让应用读取电脑上的所有文件，包括「信息」等其他应用的数据。

依 OpenAI 的帮助页面，断开应用只停止 dot 之后的访问，已经整理进 dot 的数据要删掉整个 dot 才清得掉。关闭 ChatGPT 的记忆也只停止之后与 dot 的共享，dot 已经收到的信息不会删除。「信息」数据库里也有别人发来的消息，依 Meta 与 OpenAI 的说明推论，收消息的人开启这类权限时，发消息给他的人无法控制这些消息被 AI 读取。

在海外使用 ChatGPT 的人，可以在设置的「Personalization」查看记忆。OpenAI 写明只删掉对话，不一定会删掉由该对话产生的记忆，要另外删除。训练设置在「Data controls」，关闭之后只对新对话生效，OpenAI 的帮助页面以英文界面写出这两个位置。

用 Mac 且授权过 AI 应用的人，可以在「系统设置」的「隐私与安全性」，查看「完全磁盘访问权限」与「辅助功能」有哪些应用取得权限。Apple 的帮助页面写明，取得辅助功能权限的应用也能访问联系人、日历等数据。

想试用 Muse 或 Dots 的人，FPF 建议等技术更成熟，或用一台只放必要数据的设备，代价是要另外准备设备。截至 10 月 2 日，Dots 需要付费方案，其中 Business Premium 每人每月 125 美元。SecureDrop 在 9 月 24 日的公告建议，准备联系媒体披露信息的人不要在登录状态下使用 AI 聊天服务，提示词的记录可能被用来识别身份。
