---
title: 加州 AB 1856 的开源操作系统豁免
description: 美国加州 9 月签署的 AB 1856，修改了要求操作系统在账号设置时询问用户年龄的州法。修改后，发行操作系统或 App 时用的许可若允许复制、再分发与修改，发行的人或组织就不算受规范的操作系统提供者。规定 2027 年起适用，条文以加州的账号持有人为对象。
date: 2026-10-11T00:00:00+08:00
slug: california-ab1856-open-source-exemption
categories:
  - censorship
sources:
  - title: "AB-1856 Age verification signals: software applications."
    url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1856
    publisher: California Legislative Information
    date: 2026-09-11
  - title: "AB 1856: Age verification signals: software applications."
    url: https://calmatters.digitaldemocracy.org/bills/ca_202520260ab1856
    publisher: CalMatters Digital Democracy
    date: 2026-09-10
  - title: "AB-1043 Age verification signals: software applications and online services."
    url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1043
    publisher: California Legislative Information
    date: 2025-10-14
  - title: "Press release: child safety chatbot and social media laws signed"
    url: https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/
    publisher: Office of the Governor of California
    date: 2026-09-10
  - title: CONCERNING AGE ATTESTATION FOR USERS OF COMPUTING DEVICES.
    url: https://leg.colorado.gov/laws/session-laws/SB26-051/343/download
    publisher: Colorado General Assembly
    date: 2026-06-03
  - title: California Steps Back From Dangerous Expansion of Its Age-Gating Law
    url: https://www.eff.org/deeplinks/2026/07/california-steps-back-dangerous-expansion-its-age-gating-law
    publisher: EFF
    date: 2026-07-15
  - title: A.B. 1043's Internet Age Gates Hurt Everyone
    url: https://www.eff.org/deeplinks/2026/03/ab-1043s-internet-age-gates-hurt-everyone
    publisher: EFF
    date: 2026-03-12
  - title: System76 on Age Verification Laws
    url: https://system76.com/blog/post/system76-on-age-verification
    publisher: System76
    date: 2026-03-05
  - title: Bits from the DPL
    url: https://lists.debian.org/debian-devel-announce/2026/04/msg00001.html
    publisher: Debian
    date: 2026-04-04
  - title: Ubuntu's response to California's Digital Age Assurance Act (AB 1043)
    url: https://discourse.ubuntu.com/t/ubuntus-response-to-californias-digital-age-assurance-act-ab-1043/77948
    publisher: Ubuntu Discourse
    date: 2026-03-04
  - title: "userdb: add birthDate field to JSON user records"
    url: https://github.com/systemd/systemd/pull/40954
    publisher: GitHub
    date: 2026-03-05
  - title: 未成年人网络保护条例
    url: https://www.gov.cn/zhengce/content/202310/content_6911288.htm
    publisher: 中华人民共和国国务院
    date: 2023-10-24
  - title: 移动互联网未成年人模式建设指南
    url: https://www.cac.gov.cn/2024-11/15/c_1733364304749288.htm
    publisher: 国家互联网信息办公室
    date: 2024-11-15
  - title: 关于《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》公开征求意见的通知
    url: https://www.cac.gov.cn/2026-09/18/c_1791482017777471.htm
    publisher: 国家互联网信息办公室
    date: 2026-09-18
regions:
  - US
authors:
  - anoni-net
---

美国加州州长 9 月 10 日签署 AB 1856，修改 2025 年通过的 Digital Age Assurance Act（AB 1043，数字年龄保证法）。原法要求操作系统提供者在账号设置时，让账号持有人（成年用户本人，或未成年用户的家长）填写用户的年龄，再把年龄范围以信号（signal）的形式提供给 App。AB 1856 另外规定，发行操作系统或 App 时用的许可若允许复制、再分发与修改，发行的人或组织就不算操作系统提供者。规定 2027 年 1 月 1 日起适用，条文以加州的账号持有人为对象，到 10 月 7 日为止加州以外的读者不需要调整设置。

依 AB 1043 的条文，年龄信号分成未满 13 岁、13 到未满 16 岁、16 到未满 18 岁与 18 岁以上四级。App 下载并启动时要向操作系统提供者或应用商店要求年龄信号，收到信号的开发者就视为知道用户的年龄范围。违反规定时由加州检察总长提起民事诉讼，过失违规时每名受影响的儿童最高罚 2,500 美元，故意违规最高 7,500 美元。

AB 1856 把操作系统提供者的义务限定在有账号设置功能的操作系统，也要求应用商店向操作系统要求年龄信号、再提供给开发者。法律没有要求的人，不得向操作系统提供者或应用商店索取年龄信号。法案曾经把浏览器与网站纳入，参议院 7 月的修正案删掉了这部分。

开源豁免在 5 月 18 日的众议院修正版加入，条文只有一个条件，发行时用的许可要允许接收者复制、再分发与修改。条文没有出现 open source 或 Linux，没有要求非商业，也没有指定哪一种许可。豁免只写在操作系统提供者的定义，应用商店与开发者的定义没有同样的句子。

科罗拉多州 6 月签署的 SB26-051 有类似的豁免，条件同样是许可允许复制、再分发与修改。另外多一个条件，发行者不得用技术或合同限制用户安装修改过的版本。科罗拉多的规定 2028 年 7 月 1 日起适用。

## 导读观点 {#perspective}

年龄信号的做法是由操作系统在账号设置时询问年龄，App 再通过操作系统提供的接口查询，条文要求提供的是年龄范围而非生日。条文没有要求验证填写的年龄是否正确，也没有指定接口的格式与数据存放的位置。许多 Linux 发行版用来管理系统与用户账号的组件 systemd 在 3 月合并了一项修改，在用户记录里加上只有管理者能修改的生日字段，提交说明写到加州、科罗拉多州与巴西的法律。各发行版是否采用，本文没有查到。

支持的一方在乎家长能不能让孩子的年龄跟着设备走。委员会的法案分析引述提案的州众议员，AB 1043 提供一条以隐私优先的年龄确认途径，不会干涉 App 既有的账号功能与家长控制。加州州长 2025 年签署 AB 1043 时写到，让孩子当主要用户的家长，可以设置设备把孩子的年龄告诉 App 开发者。儿童保护团体 Common Sense Media 针对还包含浏览器与网站的版本写信支持，信中写到年龄信号跟着孩子走，平台就不能因为孩子换了使用途径而不套用保护措施。

Debian 与 Canonical 在豁免加入之前的公开说明，都还没有定论。Debian 项目负责人 4 月写到，还不清楚这类规定如何适用于不卖软件、以高度分散方式提供软件的志愿者项目。Ubuntu 的开发公司 Canonical 3 月在 Ubuntu 论坛的公告写明，正在请律师审查 AB 1043，还没有具体计划。

数字权利组织 EFF 3 月的文章写到，AB 1043 的负担特别落在开源软件这类没有大公司资源的开发者身上。EFF 7 月的文章写到，浏览器与网站的扩大已经放弃，豁免也降低了对开源社区的威胁。EFF 因此撤回对 AB 1856 的反对，但仍认为 AB 1043 违宪。

条文规定操作系统只能送出必要的最少信息，洛杉矶的公立学区洛杉矶联合学区在支持信里也把数据最少化列为 AB 1856 的内容。Linux 电脑制造商 System76 的文章写到，填写年龄的人可以说谎，孩子也可以在虚拟机（在电脑里模拟另一台电脑的软件）里创建成年账号。System76 也写到，如果这种做法成为标准，App 与网站在没有收到信号时会把用户当成最低的年龄范围。条文没有规定没有信号时 App 要如何处理。

在中国大陆，《未成年人网络保护条例》（2024 年 1 月 1 日施行）第十九条要求智能终端产品制造者在产品出厂前安装未成年人网络保护软件，或者以显著方式告知用户安装渠道和方法。国家互联网信息办公室（国家网信办）2024 年 11 月发布的《移动互联网未成年人模式建设指南》要求移动智能终端、应用程序与应用程序分发平台联动。用户首次进入未成年人模式（在终端上限制使用时段与时长、退出要家长验证的模式）时，终端要提供设置生日、选择年龄或年龄区间的方式。《指南》是指引，没有写施行日期与罚则。

国家网信办 2026 年 9 月 18 日公开征求意见的《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》，拟要求智能终端产品制造者设置未成年人模式联动、防绕过等功能。征求意见稿也拟规定，应用程序分发平台对不符合适用年龄的应用程序要限制下载与安装，意见反馈截止日是 10 月 17 日。条例与征求意见稿把义务放在智能终端产品制造者，应用程序分发平台的要求出现在《指南》与征求意见稿，征求意见稿全文没有出现“操作系统”一词。

本文依条文推论，加州的用户 2027 年起在许可不允许复制、再分发与修改的操作系统创建账号时，可能会被要求填写用户的年龄。同样依条文推论，符合豁免条件的 Linux 发行版不受这项义务约束，但条文没有逐一认定哪些发行版符合。到 10 月 7 日为止，本文查不到 Apple、Google、Microsoft，以及 Debian 与 Canonical 在 AB 1856 通过后公布的做法。

之后读到要求操作系统或应用商店处理年龄的法律时，可以比较几件事。年龄由谁填写、有没有验证，离开设备的是生日还是年龄范围。开源与志愿者维护的系统在不在范围内，豁免的条件是许可方式，还是另外要求不得限制用户修改。年龄信号的做法能不能让家长在孩子的设备上，用比上传证件更少的数据达成保护。
