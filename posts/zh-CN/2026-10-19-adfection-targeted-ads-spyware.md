---
title: 定向广告投放的零点击间谍软件
description: Citizen Lab 10 月 15 日发表报告，以高信心把半岛电视台至少 45 台设备在 2024 到 2025 年遭到的攻击，关联到以色列广告公司 Discover-Tech 的定向广告与 Candiru 的间谍软件。报告确认的锁定对象只有半岛电视台，也没有说明被利用的漏洞。给一般读者的建议是屏蔽广告与限制广告标识符，报告也提到这些做法只能降低部分风险。
date: 2026-10-19T00:00:00+08:00
slug: adfection-targeted-ads-spyware
categories:
  - surveillance
sources:
  - title: "Exposing AdFection: How Discover-Tech Turned Targeted Ads Into a Pipeline for Zero-Click Mercenary Spyware"
    url: https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/
    publisher: Citizen Lab
    date: 2026-10-15
  - title: Exposing AdFection Executive Summary
    url: https://citizenlab.ca/research/exposing-adfection-executive-summary/
    publisher: Citizen Lab
    date: 2026-10-15
  - title: "Re: Citizen Lab Right to Reply"
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Citizen-Lab-Right-to-Reply-IAB.pdf
    publisher: IAB Europe
    date: 2026-10-15
  - title: "Re: Citizen Lab Report Right to Reply"
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Adtimizer-Response-to-Request-for-Comment.pdf
    publisher: Adtimizer
    date: 2026-10-11
  - title: Citizen Lab Right of Reply
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Volasim-Response-to-Request-for-Comment.pdf
    publisher: Volasim
    date: 2026-10-12
  - title: Israeli ad-tech firm helped place spyware on Al Jazeera devices
    url: https://www.aljazeera.com/news/2026/10/15/israeli-ad-tech-firm-helped-spy-on-al-jazeera-devices
    publisher: Al Jazeera
    date: 2026-10-15
  - title: Targeted ads delivered 0-click exploits to install mercenary malware
    url: https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/
    publisher: Ars Technica
    date: 2026-10-15
  - title: Online ads weaponised to deliver ‘zero-click’ spyware, researchers say
    url: https://www.theguardian.com/technology/2026/oct/15/israeli-firm-digital-ads-enabling-installation-of-zero-click-spyware-researchers-say
    publisher: The Guardian
    date: 2026-10-15
  - title: First Zero-Click Mercenary Spyware Delivered Via Targeted Ads Uncovered by CitizenLab
    url: https://www.privacyguides.org/news/2026/10/16/first-mercenary-spyware-delivered-via-targeted-ads-uncovered-by-citizenlab/
    publisher: Privacy Guides
    date: 2026-10-16
  - title: 以色列廣告業者利用定向廣告發動零點擊攻擊，半島電視臺裝置遭間諜軟體入侵
    url: https://www.ithome.com.tw/news/179747
    publisher: iThome
    date: 2026-10-16
  - title: 如果 App 要求追蹤你的活動
    url: https://support.apple.com/zh-tw/102420
    publisher: Apple
  - title: 廣告 ID
    url: https://support.google.com/googleplay/android-developer/answer/6048248?hl=zh-Hant
    publisher: Play 管理中心說明
  - title: 如果 App 请求跟踪你的活动
    url: https://support.apple.com/zh-cn/102420
    publisher: Apple
  - title: 广告 ID
    url: https://support.google.com/googleplay/android-developer/answer/6048248?hl=zh-Hans
    publisher: Play 管理中心帮助
  - title: Is https://citizenlab.ca blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/citizenlab.ca
    publisher: GreatFire
authors:
  - anoni-net
---

依 Citizen Lab 10 月 15 日发表的 AdFection 报告，以色列广告公司 Discover-Tech 的在线广告被用来投放雇佣兵间谍软件（卖给政府客户的商业间谍软件），广告显示在屏幕上就能触发。报告以高信心把半岛电视台（Al Jazeera）在 2024 到 2025 年遭到的攻击关联到以色列厂商 Candiru 的间谍软件，至少 45 台设备遭到锁定。报告确认的锁定对象只有半岛电视台，Discover-Tech 的广告则出现在近 20 万个网站与 App，广告曝光本身不代表遭到锁定。报告没有说明被利用的漏洞与受影响的版本，研究者取得的样本是从一台受害设备分离出来的 Windows 程序文件，报告没有确认手机遭到感染。

在线广告大多通过实时竞价（RTB，每次显示广告前即时进行的拍卖）决定，广告主出价争取把某则广告显示给特定用户，广告里也可以带着在 App 或浏览器里运行的代码。依报告，Discover-Tech 的许多广告带有一段标签，显示时会连回它的服务器并发送用户的广告标识符或 cookie 标识符。服务器只对选定的目标返回代码，Discover-Tech 平台的客户（报告认为包括 Candiru 这类间谍软件厂商）可以用手机的广告标识符、浏览器的 cookie 标识符或 IP 地址挑选目标，其他人收到的是空白响应。依报告，这个设计让 Discover-Tech 不必把恶意代码、甚至指向它的链接交给替它投放广告的平台。

研究者在 Discover-Tech 的网站找到两个公开可读的数据库，2026 年 3 到 6 月的竞价记录约 37.7 亿笔，看起来中标约 4.4 亿笔。其中至少 7.2 亿笔竞价的广告从名称判断带有连回这类服务器的标签，七成以上的竞价发生在 App 里。报告列出曾有广告曝光的网络，包括北约、联合国、欧洲议会与二十多个国家的政府网络。报告评估这些曝光至少让 Discover-Tech 能剖析设备，部分情况可能让其他厂商的代码在设备上运行，但曝光不等于确认遭到锁定或感染。

依报告附的各家回复，Google 终止了 Discover-Tech 在广告交易平台的出价与投放，并用安全浏览（Safe Browsing）对已知的域名显示警告。Beeswax、Vungle（Liftoff）与 Eskimi 也停止或暂停了合作。依 IAB Europe 的回信，Discover-Tech 从 10 月 8 日起在供应商名录（GVL，参与其透明度与同意框架的厂商清单）遭到暂停（报告正文写的是移除），原因是审核发现违反框架政策。Discover-Tech 与 Candiru 没有在报告给的期限内回复，到 10 月 18 日也查不到两家的公开声明。

报告另外点名 Adtimizer 与 Volasim 两家公司。Adtimizer 的回信表示只把一些子域名分配给一般广告用途，那些子域名只在 Discover-Tech 的基础设施里使用。Volasim 的回信表示 Discover-Tech 是它委托推广产品的外部广告商之一，并愿意在保密协议下提供源代码供独立审查。报告认为两家与 Discover-Tech 有关联，但也提到没有确切证据显示两家知情参与。

## 导读观点 {#perspective}

监控产业把利用广告数据识别与追踪特定人的平台称为广告情报（ADINT）。依报告，能取得竞价数据的公司可以从同一个标识符的出价请求看出一个人在不同地点与网络之间的移动，AdFection 则把这套识别接上了攻击程序（本文的理解）。报告的评价是这些广告业名录看起来大多靠厂商自我声明。IAB Europe 的回信则表示，列入名录不代表 IAB Europe 认证该公司的所有活动都符合 GDPR，该组织也没有能力与职权做取证或刑事调查。

Citizen Lab 给一般用户的建议是在浏览器安装可信的广告拦截扩展、改用会拦截追踪的浏览器、定期重置手机的广告标识符并关闭广告追踪，也可以在家中的路由器或可信的 VPN 服务屏蔽广告。给组织安全人员的建议，报告判断目前最可行的防护是在组织网络的出口（网关）屏蔽定向广告，直到业界证明能可靠拦下这类手法。报告没有写出被利用的漏洞，无法判断更新到哪个版本能修补，Ars Technica 另外提醒及时安装更新。

在中国大陆，第三方测量项目 GreatFire 到 10 月 16 日的最后一次测试显示 `citizenlab.ca` 被完全封锁（依据最近 2 次有结论的测试），从 2017 年 7 月 20 日起就有干扰记录。报告按 IP 地理位置统计带有这类标签的竞价，中国约 3,007 万笔、排第六（报告提醒 IP 地理位置可能不准确，竞价也不等于锁定或感染）。Discover-Tech 也通过中国的广告科技公司 Sunteng 投放广告，占它竞价平台出价的 0.03%，Sunteng 没有在报告给的期限内回复。

因工作或身份而面临较高风险的人，报告建议寻求专家协助。一般读者可以先限制广告标识符。iPhone 到「设置」的「隐私与安全性」、「跟踪」，关闭「允许 App 请求跟踪」（iOS 14.5 及以上）。Android 依 Google 的说明到「设置」的「隐私」、「广告」选「删除广告 ID」（需要 Google Play 服务，中国大陆销售的各款手机是否预装，本文没有查证），两家的说明页都有简体中文版（10 月 18 日查证）。

依报告，这些做法降低的是部分风险。报告在给组织安全人员的建议里提到，屏蔽广告标识符能挡下 Discover-Tech 目前的做法，但研究者推测这类攻击的范围更大。依本文的理解，重置手机的广告标识符挡不到用 cookie 标识符或 IP 地址挑选的目标。漏洞没有公开，更新到哪个版本能修补也无从判断。
