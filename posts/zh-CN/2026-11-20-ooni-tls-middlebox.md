---
title: OONI Probe 的 TLS Middlebox 实验与数据收集问卷
description: OONI 11 月 10 日公告 Probe 新增定位审查设备的 TLS Middlebox 实验，公告发布时 App 只支持默认模式。可能推估出用户所在城市的高级模式只在命令行版本提供，需自行选择加入。OONI 同时开放问卷到 12 月 10 日，询问用户能否接受收集更多地理与网络数据。没有运行 Probe、也不用 OONI 数据的读者不受影响。
date: 2026-11-20T00:00:00+08:00
slug: ooni-tls-middlebox
categories:
  - censorship
sources:
  - title: New OONI Probe TLS Middlebox Experiment
    url: https://ooni.org/post/2026-ooni-probe-tls-middlebox-experiment/
    publisher: OONI
    date: 2026-11-10
  - title: "Survey: Collecting Additional Geographic and Network-Level Data with OONI Probe"
    url: https://ooni.org/post/2026-tls-middlebox-survey/
    publisher: OONI
    date: 2026-11-10
  - title: OONI Data Policy
    url: https://ooni.org/about/data-policy/
    publisher: OONI
    date: 2026-10-22
  - title: "Risks: Things you should know before running OONI Probe"
    url: https://ooni.org/about/risks/
    publisher: OONI
  - title: TLS middlebox
    url: https://github.com/ooni/spec/blob/master/nettests/ts-037-tlsmiddlebox.md
    publisher: OONI
    date: 2026-10-22
  - title: Frequently Asked Questions (FAQ)
    url: https://ooni.org/support/faq/
    publisher: OONI
  - title: Investigating TLS blocking in India
    url: https://ooni.org/post/2020-tls-blocking-india/
    publisher: OONI、Centre for Internet & Society
    date: 2020-07-08
authors:
  - anoni-net
---

OONI 11 月 10 日在博客公告，OONI Probe 新增一项 TLS Middlebox 实验，用来找出拦截加密连接（TLS）的审查设备位在网络路径上的哪个位置。OONI Probe 是测量网站封锁的软件，任何人都可以在自己的网络上运行，测量结果公开成开放数据。实验已放进命令行版本（在终端输入指令操作的版本）v3.31.0，以及手机与桌面 App 的 v6.3.0。公告发布时 App 只支持默认模式，收集较多数据的高级模式只有命令行版本提供，而且只开放用户选择加入。

OONI 同一天发布一份问卷，询问用户能否接受 OONI 收集更多地理与网络层级的数据，以及这些数据对自己有多少用处。实验公告提到，OONI 想在把高级模式加进 App 之前先收集社区的意见，App 是全球多数 Probe 用户使用的版本。问卷开放到 12 月 10 日，问卷公告也欢迎读者转给其他 Probe 用户，以及在工作中使用 OONI 测量数据的人。没有运行 Probe、也不用 OONI 数据的读者不必做任何事。

中间设备（middlebox）是位在用户与网站之间、会检查或干扰流量的网络设备。OONI 的测试规格写到，实验检测的是依 SNI（建立 TLS 加密连接时以明文发送的网站名称）拦截连接的设备。根据实验公告的介绍，实验出自一项研究过境审查的计划。过境审查指流量的起点与终点都不在某个网络，经过那个网络时却被拦下。

公告描述的步骤是先用 traceroute（列出数据包沿途经过哪些路由器的工具）画出 Probe 到目标服务器的路径。接着向同一台服务器分别发出对照用域名与被审查域名的请求，让请求在路径上的不同位置失效。OONI 借此判断审查从哪一点开始，找出审查设备的网络位置。这些数据也可以帮助判断审查设备部署在靠近用户的地方，还是在其他网络、甚至其他国家。

默认模式对路径上的每个路由器记录三项，分别是 IP 地址对应的国家、所属的 AS（自治系统，互联网上由同一个运营商或机构管理的一组网络）与 AS 的组织名称。公告的评估是，默认模式没有带来其他 Probe 测试与 OONI 风险说明以外的新风险，第三方只凭路由器的国家与 AS 无法做出识别用户的分析。代价是用处有限，审查设备要位在某个国家或网络的深处，才能确认它在那里。

高级模式另外记录每个路由器的 IP 地址，以及数据包往返每个路由器所需的时间（RTT）。公告写到用户因此承担比现有 Probe 测试更高的风险。第三方可能用路由器的时间与位置三角定位出运行 Probe 的城市，也可能从路径反推用户所在的 /24 网段（前三组数字相同、共 256 个地址的 IP 区段）。最坏的情况是运行当下那个网段只有一个使用中的 IP 地址，用户的 IP 地址也就可能被找出来。

公告也描述了较实际的情境，第三方可以推估出用户所在的城市与网络，但很难认出特定的人。OONI 的理由是同一网络有许多使用中的 IP 地址，同一城市也有许多人运行这项测试。基于这些风险，高级模式只开放选择加入。换来的好处是审查设备落在两个国家或两个网络的交界时也能定位，还能以城市为单位测量审查，公告提到城市层级的数据是 OONI 社区长期的要求。

## 导读观点 {#perspective}

OONI 的数据政策写到，OONI 不以收集用户的 IP 地址为目标，也会采取措施从测量数据库移除。高级模式公开的路由器 IP 地址与往返时间，是 OONI 想取得的研究数据，也是第三方用来反推用户所在地的数据。本文的判断是，研究价值与暴露程度无法分开调整。

数据政策的另一条原则是送到服务器的测量都会公开，除非用户安全有疑虑，OONI 原则上不删除测量。本文的推论是，选择加入高级模式的测量会长期留在任何人都能下载的数据里，日后仍可以用来推估城市与网段。

数据政策同样列出，送出的每条测量都会附上用户的国家代码与网络的 ASN（AS 的编号），这两项无法单独退出。运行 Probe 本身也有风险，OONI 的常见问题写到 Probe 不是隐私工具，监控网络活动的人（例如政府、网络运营商、雇主）可能看到你在运行它。风险说明页则写到，运行 Probe 的潜在风险取决于用户的威胁模型（自己可能面对谁、对方有什么能力）与所在国家的法规。

OONI 与印度的 Centre for Internet & Society 在 2020 年 7 月 8 日发布的报告，测了印度三家互联网服务商（ACT Fibernet、Bharti Airtel 与 Reliance Jio）的 TLS 封锁。报告记录到 Bharti Airtel 与 Reliance Jio 有依 SNI 的封锁，Reliance Jio 还会依 TLS 握手所连的服务器判断是否封锁。这是 2020 年的数据，不代表现况。报告显示依 SNI 的封锁在这项实验之前就已有记录。

依 11 月 10 日的公告，App 还没有高级模式，用 App 运行 Probe 的人不必为它做任何设置。对 OONI 收集更多数据有意见的 Probe 用户，以及工作中会用到 OONI 数据的人，可以在 12 月 10 日前填写问卷。问卷架在 Google 表单上，链接在原文清单的问卷公告里，公告请读者花几分钟填写。

在运行 Probe 本身就可能引起注意的环境，可以照风险说明页在 App 里选择要运行哪些测试。数据政策也提到，App 的设置里可以选择不送出测量。不送出测量可以让结果不公开，但本文依常见问题推论，这两种做法都改变不了监控网络的人看得到有人在运行 Probe。命令行版本的用户考虑开启高级模式时，代价是所在城市与网段可能被推估出来，而且测量公开后原则上不会删除。
