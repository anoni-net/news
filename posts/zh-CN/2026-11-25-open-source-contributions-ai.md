---
title: AI 时代开源项目收紧的外部贡献入口
description: curl 停掉漏洞奖金，GitHub 让维护者限制谁能开 PR 与 issue，开源项目在 2026 年收紧外部贡献的入口。作者认为收紧处理的是大量低质量投稿的数量问题，信任的问题仍在。xz 后门与 Shai-Hulud 蠕虫的恶意版本都由已经受信任的开发者账号发布，缺的是审查人力与权限管理。
date: 2026-11-25T00:15:00+08:00
slug: open-source-contributions-ai
categories: [column]
authors: [toomore]
sources:
  - title: The end of the curl bug-bounty
    url: https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
    publisher: curl 作者的博客
    date: 2026-01-26
  - title: Contributing to the curl project
    url: https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md
    publisher: curl
  - title: Welcome to the Eternal September of open source. Here's what we plan to do for maintainers.
    url: https://github.blog/open-source/maintainers/welcome-to-the-eternal-september-of-open-source-heres-what-we-plan-to-do-for-maintainers/
    publisher: GitHub
    date: 2026-02-12
  - title: Limit open pull requests for users without write access
    url: https://github.blog/changelog/2026-06-17-limit-open-pull-requests-for-users-without-write-access/
    publisher: GitHub
    date: 2026-06-17
  - title: Restrict issue creation to collaborators only
    url: https://github.blog/changelog/2026-06-29-restrict-issue-creation-to-collaborators-only/
    publisher: GitHub
    date: 2026-06-29
  - title: "Pull request limits: Exempt contributors by age or history"
    url: https://github.blog/changelog/2026-10-28-pull-request-limits-exempt-contributors-by-age-or-history
    publisher: GitHub
    date: 2026-10-28
  - title: All projects
    url: https://osssaysno.com/all
    publisher: Open Source Says No
  - title: About
    url: https://osssaysno.com/about
    publisher: Open Source Says No
  - title: Kernel Guidelines for Tool-Generated Content
    url: https://github.com/torvalds/linux/blob/master/Documentation/process/generated-content.rst
    publisher: Linux 内核
  - title: Open source was not ready for AI-speed contributions
    url: https://frenck.dev/open-source-was-not-ready-for-ai-speed-contributions/
    publisher: Home Assistant 维护者的博客
    date: 2026-05-31
  - title: XZ Utils backdoor
    url: https://tukaani.org/xz-backdoor/
    publisher: Tukaani
  - title: backdoor in upstream xz/liblzma leading to ssh server compromise
    url: https://www.openwall.com/lists/oss-security/2024/03/29/4
    publisher: oss-security
    date: 2024-03-29
  - title: Timeline of the xz open source attack
    url: https://research.swtch.com/xz-timeline
    publisher: xz 攻击时间线
  - title: AI cuts coding time, but it's also filling open source's inbox with crap
    url: https://www.theregister.com/ai-and-ml/2026/10/21/ai-cuts-coding-time-but-its-also-filling-open-sources-inbox-with-crap/5304389
    publisher: The Register
    date: 2026-10-21
  - title: Sunsetting Jazzband
    url: https://jazzband.co/news/2026/03/14/sunsetting-jazzband
    publisher: Jazzband
  - title: Widespread Supply Chain Compromise Impacting npm Ecosystem
    url: https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
    publisher: CISA
    date: 2025-09-23
  - title: "Open Source Stewardship Communities: \"We need you, but not your pull request\""
    url: https://arxiv.org/abs/2609.12236
    publisher: arXiv
    date: 2026-09-10
  - title: What Will Replace Pull Requests? Rethinking Software Collaboration for AI Agents
    url: https://arxiv.org/abs/2610.34933
    publisher: arXiv
    date: 2026-10-26
---

开源项目的源代码仍然公开，外人能送进项目的东西却越来越受限制。我把外人向项目提交代码修改、报告问题或通报漏洞的渠道，称为外部贡献的入口。2026 年有项目停掉漏洞奖金，也有平台让维护者只开放协作者发起修改，背后的理由都跟 AI 带来的大量投稿有关。我想厘清收紧入口能保护到什么，以及开源项目要为此付出什么。

我的看法是，关掉外部的 PR（pull request，向项目提出的代码修改）能挡下 AI 送进来的大量低质量贡献，收紧入口的项目提出的理由也多半是保护维护者的时间。收紧处理的是数量的问题，我担心的是它被当成安全措施。我认为供应链攻击多半从已经受信任的账号或人进来，信任的问题仍在，开源项目真正缺的是审查人力与权限管理。

AI 工具让生成代码变得又快又容易之后，我认为开源项目看待贡献的方式也要跟着调整。开源项目收到一份修改时，维护者要先读懂代码、确认没有错误或安全问题才会合并，这个步骤称为审查（review）。审查别人的修改、写出能重现问题的测试、把问题描述清楚，本来就是维护项目的重要工作，以往多半由维护者自己承担。现在送来的代码变多，我认为这些工作更需要外部贡献者一起分担，也应该被当成贡献看待。

## 外部贡献入口的收紧 {#tightening}

curl 是一套常用的网络传输工具，作者 1 月 26 日在博客宣布结束漏洞奖金，1 月 31 日正式停止。根据同一篇文章，这个奖金计划从 2019 年 4 月开始总共确认了 87 个漏洞，发给报告者的奖金合计超过 10 万美元。作者写明停掉奖金的目的，是不再让人有动机捏造报告来领奖金。之后要报告漏洞的人，改用 GitHub 的私下报告功能，或发邮件到项目的安全邮箱。

依 GitHub 2 月 12 日的博客文章，维护者已经可以只让协作者（collaborator，被项目加入、有权限直接修改代码的成员）发起 PR，也可以整个关闭 PR。依 GitHub 的更新说明，6 月 17 日起维护者可以设定其他用户最多能同时打开几个 PR。到了上限，要等旧的被关闭或合并才能再开新的。

草稿状态的 PR 不算在上限里，维护者也可以把信任的贡献者加进例外名单（bypass list）。10 月 28 日 GitHub 再加上自动豁免的规则，让账号注册满一定天数或已经在该项目合并过一定数量 PR 的人超过上限。

6 月 29 日，GitHub 把同样的限制延伸到 issue（报告问题或提出需求的讨论串），项目可以设定只有协作者能开 issue。依更新说明，开启这个设定之后，其他人从项目页面上的任何地方都无法创建 issue。**我比较在意这一项，因为我认为 issue 是不写代码的人报告问题的主要渠道**。

追踪 AI 贡献政策的网站 Open Source Says No 到 11 月 20 日收录 221 个项目，收录门槛是 GitHub 上至少 5,000 颗星，或属于发行版、编程语言运行时、主要库这类广泛使用的基础设施。其中 24 个禁止 AI 生成的贡献。其余大多数接受 AI 辅助的贡献，但附带条件，例如要披露用了 AI、要经过人工审查。网站在说明页写明只整理信息，不判断这些政策对不对。

## 生成成本与审查成本的落差 {#review-cost}

依 GitHub 2 月那篇博客，PR 现在几秒钟就能生成，生成式 AI 让人大量产出代码、issue 与安全报告。文中的说法是生成的成本降了，审查的成本没有降。同一篇也提到维护者一直都在处理噪音，低质量的投稿早就存在。Linux 内核的贡献规则也有相近的说法：工具可能让贡献的数量增加，但审查者与维护者的时间有限。

依 curl 作者的文章，漏洞奖金计划前几年有超过 15% 的报告确认是漏洞，2025 年起降到 5% 以下。作者把原因归到 AI 生成的劣质报告（原文 AI slop）暴增，连不明显属于劣质内容的报告，质量也在下降。情况从 2024 年下半年开始，2025 年急剧恶化。同一篇也提到 PR 在 curl 没有造成问题，因为在一份 PR 通过全部 200 项 CI 任务（持续集成，每次修改都会自动运行的测试）之前，项目不必花任何人力看它。

Home Assistant（开源的智能家居平台）的一位维护者 5 月 31 日在个人网站提到，贡献者借助 AI 能提交更多修改，但每一份仍要由维护者验证。依这位维护者的描述，以前贡献者要先读懂代码、写出修改、运行测试、说明结果才能提交一份修改，这些步骤本身就是一道门槛。这位维护者提出的判断标准是，提交修改的人是否理解自己的修改、验证过、愿意负责，有没有用到 AI 则不在标准里。

## 收紧入口能防范与无法防范的风险 {#what-it-stops}

我在前面引用的几份文件里，读到的收紧理由都是投稿的数量与维护者的时间，没有读到防范供应链攻击。我把两件事放在一起看，是因为 Python 包的共同维护组织 Jazzband 在结束运营的公告里，把开放加入的模式跟能否安全运营连在一起。同一份公告也举了 xz 后门作为独自维护的人倦怠之后的例子。

取消漏洞奖金、限制 PR 的数量、只让协作者开 issue，我把这三项措施都看成针对大量投稿的做法，也认为能减轻数量的问题。curl 的作者也提醒他们的判断有可能错，错了会再采取进一步的做法。依 The Register 10 月 21 日的报道，curl 当周宣布把低与中度严重性的漏洞移到公开处理，报道写的理由是 curl 的安全团队几乎被 AI 辅助生成的报告压垮。从这则报道看，停掉奖金之后报告的压力仍在，收紧入口能减轻多少要看之后的数字。

xz 是 Linux 系统常见的压缩工具。从入口的角度看 2024 年 3 月曝光的 xz 后门，会得到跟我不同的观察，因为植入后门的账号一开始就是外部贡献者。依 xz 项目网站的说明，5.6.0 与 5.6.1 两个版本的发布压缩包（tarball）含有后门，这两个压缩包就是由那个账号制作并签名的。

依一份逐日引用 xz-devel 邮件列表的公开时间线，那个账号 2021 年 10 月发出第一个无害的补丁，到了 2022 年底已经可以直接把修改合并进项目。2024 年 2 月，该账号把后门藏进测试用的二进制文件，接着发布 5.6.0。

从这个角度看，如果项目完全不收外部的补丁，这个账号连第一步都踏不进来。依时间线的日期计算，从第一个补丁到发布含后门的版本，中间隔了两年四个月。**我的看法是，收紧入口只能延后这类花长时间取得信任的攻击，有耐心的攻击者仍然可以用时间换取信任**。

依开源安全邮件列表 oss-security 上公开警告后门的那封信，后门有一部分只存在发布的压缩包里，是 git 上的源代码没有的一行构建脚本。我的理解是，发行版与用户常下载维护者另外打包并加上数字签名的压缩包，内容不一定跟 git 上公开的源代码相同。所以我推论，就算仔细审查每一个 PR 也看不到那行脚本，关键在于谁有权限制作并签名发布文件。

原维护者 2022 年在邮件列表提到自己能投入的精力有限（依同一份时间线转录）。**我认为 xz 事件暴露的弱点，是维护者太少，以及发布权限交给谁的管理问题。关掉入口，也不会让项目多出一位能分担审查与发布的人**。

Jazzband 开放任何人加入，成员共用 push 权限（直接把修改推进项目的权限），3 月宣布逐步结束运营、关闭新注册。依公告，Jazzband 十年间累积 3,135 名成员、维护过 84 个项目。公告列出的原因是 AI 生成的大量垃圾 PR 与 issue，让开放加入、共用 push 权限的做法撑不下去。负责人也表示，不能再一边把 push 权限交给每个加入的人，一边还要安全地运营。

公告也列出另一个问题：每一次项目转移、PyPI（Python 的包发布平台）权限变更与基础设施的决定，都要经过负责人一个人。负责人在同一篇公告把 xz 描述成独自维护的人倦怠之后、由恶意的人补上空缺的例子。

公告写的直接原因是 AI 投稿，我则把它看成权限管理的问题。在 Jazzband，任何人加入就能取得 push 权限，可以直接把修改推进组织里的项目。垃圾投稿变多之后，我认为负责人难以判断每个加入的人是否可信，也没有其他人能分担把关。加入就给权限的做法，因此撑不下去。

依美国网络安全与基础设施安全局（CISA）2025 年 9 月 23 日的警示，名为 Shai-Hulud 的自我复制蠕虫入侵了 500 多个 npm（JavaScript 的包注册表）包。警示没有写攻击者一开始如何入侵，只写到恶意程序会搜索环境里存放的凭据，锁定 GitHub 的令牌（让程序代替密码登录账号的密钥）与云服务的密钥。蠕虫接着以被入侵的开发者身份登录 npm，把恶意代码加进其他包，再发布新版本。CISA 的警示建议更换所有开发者的凭据，并在 GitHub 与 npm 账号强制使用防钓鱼的多因素认证（登录时除了密码，另外要求一道验证）。

CISA 的警示列出的建议里，没有一项是限制外部 PR。我认为 xz 的攻击者用时间换取信任，Shai-Hulud 则扫描并窃取开发者的凭据、以被入侵的开发者身份发布，两者造成伤害时都利用了已经受信任的账号。

## 新维护者的来源 {#new-maintainers}

GitHub 2 月那篇博客也提到，这些限制可能对第一次参与、出于善意的贡献者影响特别大，所以 GitHub 把它们做成可选、可以调整的设置。我的推论是，不符合自动豁免条件的新人要等维护者手动加进例外名单，才能超过同时打开 PR 的数量上限。

两位软件工程研究者 9 月在 arXiv（学术论文的预印本平台）发布一篇论文。依摘要，AI 让写出一份修改的成本降低，审查别人的贡献却仍然很费力。因此有些项目限制谁可以提交代码，同时欢迎其他形式的参与。论文认为，这些项目限制的原因是那些代码已经不值得花力气审查，跟代码是不是 AI 写的无关。

研究者把这种形态称为管家型社区（stewardship community）。在这种社区里，只有一小群核心成员能把代码写进项目，其他人不写代码也仍然能影响软件。依论文的定义，在这种社区里想写代码越来越需要先经过批准，不能自己主动提交。摘要也提醒，AI 可能取代原本由外部贡献者提供的写代码人力，同时削弱开源社区自我更新（培养新成员接手）的方式。

另一篇 10 月在 arXiv 发布的论文，研究者整理了 31 个组织或个人的 50 份灰色文献（博客、公告这类没有经过学术出版的文件）。依摘要，大多数做法仍然保留 PR 再加上工具或限制，其中最常被采用的是加上限制。

Jazzband 宣布结束运营之后，原本由它维护的项目要另外找人接手。公告建议 Django 相关的项目转到 Django Commons，部分项目已经转过去，公告当时 Django Commons 有 5 位管理员与 15 个活跃的项目。pip-tools、tablib 这些不属于 Django 的项目，负责人表示不知道有对等的去处。

我预期入口收紧之后，项目更难从外部贡献者里培养新的维护者，维护者不足的问题就会一直存在。我认为这个代价跟 xz 的弱点是同一件事，维护者太少，攻击者才有空缺可以补。

## 贡献的转向与读者可以留意的信号 {#what-readers-can-do}

我不反对项目收紧入口，面对大量投稿，维护者需要先保护自己的时间。我希望省下来的时间投进审查与权限管理，例如谁能合并、谁能发布、令牌如何保管，前面提到的 CISA 建议可以当作检查的起点。

我认为值得算作贡献的，是**降低维护者验证成本的工作**。xz 后门被发现的起点，是一位开发者在 Debian 的开发版（sid）上注意到 ssh 登录异常占用 CPU，以及 valgrind（检查内存错误的工具）报告的错误。这位开发者追查之后在 oss-security 公开警告，我把那封信看成一份问题描述，价值不下于一份补丁。

想参与的人可以先读项目的贡献政策。依 Open Source Says No 收录的政策，Linux 内核要求贡献者理解自己提交的所有内容，并且能为它辩护。依 curl 的贡献文档，项目接受 AI 辅助写成的代码，前提是符合代码风格、文档与测试等一般要求。用 AI 工具找问题的报告者，也要在报告里披露。

不写代码的人也能参与，报告问题时写清楚版本、操作步骤与能否重现，就能省下维护者验证的时间。项目把 issue 限制在协作者时，先看贡献文档有没有写其他报告渠道。

使用隐私工具的人，我建议看项目有几位活跃的维护者、贡献政策有没有写清楚 AI 与权限的规则，以及漏洞从报告到修复花了多久（贡献文档、版本记录与安全公告多半可以找到）。到 11 月 20 日，Open Source Says No 没有收录 Tor、Tails、Signal 等工具，有没有相关规定要到各项目的贡献文档确认。xz 的 README 在 2022 年底列了两位维护者（依前面那份时间线），其中一位就是后来植入后门的账号。因此这些信号只能当作参考，不能保证安全。

你常用的隐私工具，贡献文档有没有写到 AI 与权限的规则？如果项目不再接受外部的 PR，你会用什么方式参与？

## 延伸阅读 {#further-reading}

- [AI 加速找漏洞之后的个人防护与开源维护](https://anoni.net/news/zh-cn/2026/11/eff-security-worse/)：PHP 的安全团队一边修复真漏洞，一边处理一百多份无效或无法重现的报告，处境跟 curl 相近
- [AI 编程工具的扩展后门与恶意指引文件](https://anoni.net/news/zh-cn/2026/11/ai-devtools-supply-chain/)：被篡改的扩展以已验证的账号出现在市场上，另一起经由受信任的发布渠道进来的事件
- [开源图像编辑软件 Compositor 与 AI 生成代码的维护和审计](https://anoni.net/news/zh-cn/2026/10/compositor-image-editor/)：作者自述代码全由 AI 写成，外部开发者送来的八个补丁 PR 被一起关闭，从作者这一端看 AI 代码的审查
