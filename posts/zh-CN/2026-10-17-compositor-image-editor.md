---
title: 开源图像编辑软件 Compositor 与 AI 生成代码的维护和审计
description: 一位设计师 9 月发布 Mac 上的开源图像编辑软件 Compositor，免费、不用账号，作者自述代码全由 AI 写成。本文读到的批评集中在「我做的」这个说法，以及 AI 写的代码由谁检查、谁维护。到 10 月 12 日只支持 Apple 芯片、macOS 26 以上的 Mac。
date: 2026-10-17T00:00:00+08:00
slug: compositor-image-editor
categories:
  - tracking
sources:
  - title: Compositor – The Photoshop alternative for Mac
    url: https://robbietilton.com/compositor
    publisher: Compositor
  - title: Compositor/README.md
    url: https://github.com/robbietilton/Compositor/blob/main/README.md
    publisher: GitHub
  - title: Compositor launch post on X
    url: https://x.com/i/status/2100946395972976843
    publisher: X
    date: 2026-09-18
  - title: Compositor developer's reply on X
    url: https://x.com/i/status/2101334715513106496
    publisher: X
    date: 2026-09-19
  - title: Quote post by a concept artist on X
    url: https://x.com/i/status/2101093572720148574
    publisher: X
    date: 2026-09-18
  - title: Thread by a creative tools developer on X
    url: https://x.com/i/status/2103514110843551887
    publisher: X
    date: 2026-09-25
  - title: Thread by a creative tools developer on X (continued)
    url: https://x.com/i/status/2103514716962501046
    publisher: X
    date: 2026-09-25
  - title: Thread by a creative tools developer on X (follow-up)
    url: https://x.com/i/status/2103523639685738691
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's post on ports on X
    url: https://x.com/i/status/2103520923697733898
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's reply on maintenance on X
    url: https://x.com/i/status/2103519019282358348
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's reply on tracking on X
    url: https://x.com/i/status/2108977298905133319
    publisher: X
    date: 2026-10-10
  - title: Compositor releases
    url: https://github.com/robbietilton/Compositor/releases
    publisher: GitHub
  - title: Add Generative Fill, Remove and Expand (optional, with the user's own Gemini key)
    url: https://github.com/robbietilton/Compositor/pull/58
    publisher: GitHub
    date: 2026-09-21
  - title: Add Enlarger, AI upscaling with Real-ESRGAN
    url: https://github.com/robbietilton/Compositor/pull/73
    publisher: GitHub
    date: 2026-09-22
  - title: Fix unsafe formatting of persisted rotation and hue angles
    url: https://github.com/robbietilton/Compositor/pull/10
    publisher: GitHub
    date: 2026-09-19
  - title: "Feature request: Windows version of Compositor"
    url: https://github.com/robbietilton/Compositor/issues/23
    publisher: GitHub
    date: 2026-09-19
  - title: "FYI: Simplified Chinese localization fork (compositor-cn)"
    url: https://github.com/robbietilton/Compositor/issues/222
    publisher: GitHub
    date: 2026-10-07
  - title: Is https://github.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
  - title: Is https://raw.githubusercontent.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/raw.githubusercontent.com
    publisher: GreatFire
authors:
  - anoni-net
---

一位设计师 9 月 16 日（UTC）在 GitHub 发布 Mac 上的图像编辑软件 Compositor，9 月 18 日在 X 公开介绍。软件以 MIT 许可证开源、免费下载，不需要账号，作者的发布帖子写起初是为了摆脱 Adobe 的订阅而做给自己用。到 10 月 12 日为止，最新版是 10 月 11 日（UTC）发布的 1.4.10，只支持搭载 Apple 芯片、macOS 26 以上的 Mac。界面只有英文，作者也暂时不接受翻译。

发布帖子到 10 月 12 日累计约 240 万次浏览，帖子下面的回复本文没有取得，以下只根据 X 上少数公开帖子。一位影视概念设计师引用发布帖子，批评把 AI 写成的软件说成「I built」（我做的），认为这类作品都是 vibe coding（用自然语言指示 AI 写代码）。作者回复这则帖子时写「AI wrote every line of this」，也写「Code was always the painful part, never the important part.」依本文 10 月 12 日统计 GitHub 的 commit（代码的每一次修改记录），451 个有 282 个带 AI 编程工具的共同作者署名。

另一位开发创作工具的开发者在 X 借这个项目探讨 AI 如何改变创作工具的生态，写这个项目的代码「decidedly not for human consumption」，并问作者接下来半年、两年维护它的动力在哪里。作者回复会继续维护，因为自己每天都在用。作者只维护 Mac 版，在 X 写其他人做的 Windows 与 Linux 移植他都没有测试。

## 导读观点 {#perspective}

作者在 GitHub 写 Compositor 是「a local, single-user editor with no network path」。发布说明另外提到会检查更新，打开时每天最多一次，更新要用户自行确认才安装。本文读配置文件确认，检查的对象是 GitHub 上的更新清单。作者也在 X 写「no login, no account, no tracking」。

外部贡献者曾提交 PR（向项目提出的代码修改）加入生成式填充，默认关闭，用户要自备 Google 的 Gemini AI 服务密钥、按下生成才会把图片发送出去。PR 正文自己写这是第一个让用户内容离开电脑的功能。作者留言要再想想长期如何在 Compositor 加入 AI，这个 PR 之后关闭、没有合并。另一个在本地运行的 AI 放大功能，作者留言宁可整体重新规划 AI 功能（可能在 v2），不要一项一项加。

开源让这些主张可以被检查，不必只听作者的说法。本文 10 月 12 日用关键词搜索过主分支的源代码，除了更新检查之外没有找到网络请求或统计分析的代码，这不是完整的审计。依本文计算，Swift 代码约 3.7 万行，从 commit 署名推论大多由 AI 生成。前述开发者对这些代码的说法是「decidedly not for human consumption」。

9 月 19 日有外部开发者依一份安全扫描提出八个修补 PR，其中一个提到特制的项目文件数值超出范围时，会让程序的属性面板或调整编辑器停止运行。作者把这批 PR 一起关闭，留言写软件在本地单人使用、没有不受信任的输入，这些属于程序稳定性的范围（「robustness questions rather than security ones」）。作者的留言没有说明，打开别人传来的项目文件算不算不受信任的输入。

作者的关闭留言也写，导入、缩放与导出都已统一限制在 1 亿像素、单边 3 万像素，新加的限制可能拒绝正常的文件。留言另外写到，这批 PR 让作者发现自动测试已经有一段时间无法运行，修好之后有 362 个测试。作者请提交者在实际复现崩溃时，附上文件与步骤另开 issue（项目的问题反馈）。

作者的说法是自用的工具会持续维护，需要其他平台的人可以依 MIT 许可证自行移植，已有其他开发者做出 Windows 等平台的移植版。前述开发者怀疑作者是否会持续维护用户要求、作者自己不用的功能，也写面向一般用户的软件似乎没有开源项目常见的咨询收入（为企业提供服务、支撑开发的收入）。另有开发者做了简体中文的分支（另外复制一份、自行修改的版本），在原项目的 issue 写分支移除了自动更新。理由是避免用户被更新回英文版，也不连接原项目的更新清单。

用搭载 Apple 芯片、macOS 26 以上的 Mac 处理图片的人，可以从 GitHub 或 Homebrew 下载试用。下载不必注册，反馈问题要有 GitHub 账号。依作者的说法与本文的关键词搜索，编辑图片时除了更新检查不会联网，更新检查默认开启、装不装由用户决定。本文没有完整审计代码，作者也没有说明打开别人传来的项目文件是否有风险。

Compositor 官方的安装文件与更新清单都放在 GitHub。到 10 月 11 日的最后一次测试，GreatFire 对 github.com 最近 90 天内 56 次有结论的测试中 64% 受到干扰。存放更新清单的 raw.githubusercontent.com，到 10 月 8 日最近 4 次测试全部受到干扰，样本只有 4 次。这是第三方对主机名的量测，没有测具体的下载路径。

比较这类工具时，可以从几个方面问。作者重视的是软件在本地运行、不用登录、可以自行修改，这些主张能不能从源代码与实际的网络连接确认。批评的一方在意的是维护，维护者只有一人时，自己需要的功能停止更新要怎么办。AI 写成的代码有没有人读过，外部报告的问题又如何处理，也可以从项目的 issue 与 PR 看出来。
