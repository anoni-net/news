---
title: Tor Project 与 Mullvad 合作关系的决定与争议
description: VPN 服务商 Mullvad 一位联合创始人的政治捐款引发争议后，Tor Project 10 月 9 日说明不终止合作，但暂停联合品牌宣传并修改 Mullvad Browser 的描述。两款浏览器没有停止维护的公告，声明下的留言看法分歧。
date: 2026-10-14T00:00:00+08:00
slug: tor-mullvad-relationship
categories:
  - civil-society
sources:
  - title: A statement on the Tor Project's relationship with Mullvad
    url: https://blog.torproject.org/on-tor-relationship-with-mullvad/
    publisher: Tor Project
    date: 2026-10-09
  - title: A statement on the Tor Project's relationship with Mullvad
    url: https://forum.torproject.org/t/a-statement-on-the-tor-projects-relationship-with-mullvad/22247
    publisher: Tor Project Forum
    date: 2026-10-09
  - title: Donation controversy
    url: https://mullvad.net/en/blog/donation-controversy
    publisher: Mullvad
    date: 2026-07-20
  - title: Techprofil ger miljoner till Örebropartiet
    url: https://www.flamman.se/techprofil-ger-miljoner-till-orebropartiet/
    publisher: Flamman
    date: 2026-06-26
  - title: We've Teamed Up With Mullvad VPN to Launch the Mullvad Browser
    url: https://blog.torproject.org/releasing-mullvad-browser/
    publisher: Tor Project
    date: 2023-04-03
  - title: MULLVAD VPN AND THE TOR PROJECT TEAM UP TO RELEASE THE MULLVAD BROWSER.
    url: https://mullvad.net/en/blog/mullvad-vpn-and-the-tor-project-team-up-to-release-the-mullvad-browser
    publisher: Mullvad
    date: 2023-04-03
  - title: What is Mullvad Browser?
    url: https://support.torproject.org/mullvad-browser/faqs/what-is-mullvad-browser/
    publisher: Tor Project
  - title: Releases · mullvad/mullvad-browser
    url: https://github.com/mullvad/mullvad-browser/releases
    publisher: GitHub
  - title: 2023-7-1 thru 2024-6-30 IRS Form 990
    url: https://www.torproject.org/static/findoc/2023-2024-TheTorProject-PublicDisclosureForm990.pdf
    publisher: Tor Project
  - title: Snowflake Daily Operations 2026 July update, and a statement about Mullvad donations
    url: https://forum.torproject.org/t/snowflake-daily-operations-2026-july-update-and-a-statement-about-mullvad-donations/21954
    publisher: Tor Project Forum
    date: 2026-08-05
  - title: A statement on the Tor Project's relationship with Mullvad
    url: https://news.ycombinator.com/item?id=50022266
    publisher: Hacker News
    date: 2026-10-09
  - title: Is https://mullvad.net blocked in mainland China?
    url: https://en.greatfire.org/https/mullvad.net
    publisher: GreatFire
  - title: Is https://www.torproject.org blocked in mainland China?
    url: https://en.greatfire.org/https/www.torproject.org
    publisher: GreatFire
authors:
  - anoni-net
---

VPN 服务商 Mullvad 一位联合创始人的政治捐款引发争议之后，Tor Project 10 月 9 日发布声明，决定不终止与 Mullvad 的关系。声明提到要设下清楚的界线，技术合作按双方范围很窄的协议继续，主动的联合品牌宣传暂停。Tor 自己的渠道也修改了 Mullvad Browser 的描述。到 10 月 12 日为止，Tor Browser 与 Mullvad Browser 最近的稳定版都是 9 月底发布的 15.0.24，没有停止维护的公告。

争议源自瑞典媒体 Flamman 6 月 26 日的报道，一位联合创始人 2025 年以个人名义捐出 500 万瑞典克朗给瑞典的政党 Örebropartiet，占该党 2025 年收入的 72%。Flamman 称该党为民粹政党，并形容它主张大规模遣返移民。Mullvad 7 月 20 日在博客写这是个人捐款、公司没有参与，对捐款「不认可也不谴责」，也写这很可能是个坏主意。

根据 Tor 的声明，这项合作改善了 Tor Browser 代码的结构、可维护性与可审计性，也让更多人多一个免费的开源隐私工具。依 Tor 公开的 2023 年 7 月到 2024 年 6 月美国国税局（IRS）990 表，Mullvad 提供约 140 万美元，是企业来源中最大的一笔。声明本身没有写金额，到 10 月 12 日为止，Tor 财务报告页最新只到 2024 年 6 月的会计年度。

## 导读观点 {#perspective}

Mullvad Browser 是 2023 年 4 月推出的浏览器，由 Mullvad 发布，Tor 的说法是「不走 Tor 网络的 Tor Browser」。两者的版本号与发布日期同步，Mullvad Browser 也由 Tor Browser 的开发者签名，本文的推论是两者大部分代码共用。差别在连接方式，Tor Browser 走 Tor 网络、可以连 onion 服务并内置规避审查的功能，Mullvad Browser 则搭配用户自己信任的 VPN 或直接连接。

依 Tor 的声明，它捍卫言论自由，但强烈反对威胁其他人权与自由的言论。声明也提到，隐私工作的资源严重不足，有时需要做困难的妥协。Mullvad 的博客则写公司主张言论自由、信息自由与隐私权，并把创始人个人的看法与公司的使命分开。运营一座 Snowflake 网桥（让网络受封锁的人连上 Tor 的入口之一）的志愿者小组（自称不属于 Tor Project）8 月 5 日宣布拒收 Mullvad 的捐款，理由是捐款对象是他们所称「危险的民粹政党」，即使所需年度开销因此只剩约四分之一有着落。

Tor 博客这篇声明底下的论坛留言，到 10 月 12 日共 8 则，支持维持合作与批评或谴责的各 3 则（留言是自愿发言的少数，不代表社区整体）。支持的留言写到 Mullvad 的使命与 Tor 一致，失去 Mullvad Browser 会伤害用户。

批评的一方有留言直接表示谴责。一则自称前 Tor Browser 开发者的留言写，Mullvad 没有开发者参与、只提供资金，「技术合作」的说法有误导之嫌。Tor 的支持页写这款浏览器由 Tor Project 与 Mullvad 合作开发，Mullvad 的公告写由 Tor 的工程师开发，两边都没有写 Mullvad 是否派人参与。

Tor 的声明提到，决定之前做过社区、员工与董事会的讨论、员工调查与财务分析，但没有公开调查结果与财务数字。论坛有一则留言要求公开 Mullvad 占预算的比例，也问是否所有捐款都经过同样的审查。到 10 月 12 日为止，Tor Project 人员没有在留言中回应，Mullvad 的博客也没有针对这份声明的新文章。

Hacker News 上同一篇声明的讨论串到 10 月 12 日有 353 则留言，看得到内容的顶层留言有 22 则（另有 11 则被标记而看不到内容），这些留言同样不代表社区整体。表示理解或支持维持合作的顶层留言有 4 则，其中两则的理由是这类工具的资金难得，断绝关系不见得更有利于使命。有 5 则反对声明划出的言论界线，例如主张言论自由本质上是绝对的，回复里的反驳则认为 Tor 只是不想与这些言论连在一起。另有 3 则批评声明没有交代捐款与政党的细节或语气像公关稿，也有顶层留言担心 Tor 依赖 Mullvad 的资金之后，独立性会受影响。

第三方监测网站 GreatFire 10 月 12 日的记录显示，mullvad.net 在中国大陆最近 16 次有效测试全部失败，www.torproject.org 的 2 次有效测试也都失败（最近一次约在两个月前）。本文的推论是，在中国大陆获取这两款浏览器要先绕过封锁，Tor 的决定不改变这一点。

使用 Tor Browser 或 Mullvad Browser 的读者，到 10 月 12 日为止不必做任何设置。这次的争议在资金与组织的立场，两款浏览器的隐私保护机制没有因此改变，这是本文依声明「技术合作按协议继续」的推论。介意资金来源的读者可以留意，两款浏览器都由 Tor Project 的工程师维护，改用另一款不会改变 Tor 与 Mullvad 之间的资金关系。之后可以留意联合品牌宣传的暂停是否有期限、Tor 是否公开 Mullvad 近年的资金比例，以及下一份财务报告。

比较这件事时可以问，隐私工具的开发组织接受企业资金时用什么标准审查捐款者、标准是否一视同仁，公司与创始人个人的政治捐款又能否分开看待。暂停宣传与修改描述，是否足以让用户分辨合作的范围与组织的立场。断绝合作之后，一款仍在维护的开源浏览器能否找到其他资金继续发布。
