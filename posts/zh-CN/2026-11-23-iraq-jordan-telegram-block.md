---
title: 伊拉克与约旦的 Telegram 封锁与 OONI 测量
description: 伊拉克与约旦 11 月 16 日宣布封锁 Telegram。依 OONI Probe 的测量，两国的 Telegram 测试在 11 月 15 日到 16 日之间（UTC）转为异常，到 11 月 20 日仍然全部异常。两国的命令只适用于各自境内的网络，其他地方的读者不受这次封锁影响。
date: 2026-11-23T00:05:00+08:00
slug: iraq-jordan-telegram-block
categories:
  - censorship
sources:
  - title: "Iraq and Jordan block Telegram (16 Nov 2026): OONI measurements"
    url: https://github.com/net4people/bbs/issues/686
    publisher: net4people
    date: 2026-11-19
  - title: Iraq
    url: https://explorer.ooni.org/chart/mat?probe_cc=IQ&since=2026-11-01&until=2026-11-21&time_grain=day&axis_x=measurement_start_day&test_name=telegram
    publisher: OONI Explorer
  - title: Jordan
    url: https://explorer.ooni.org/chart/mat?probe_cc=JO&since=2026-11-01&until=2026-11-21&time_grain=day&axis_x=measurement_start_day&test_name=telegram
    publisher: OONI Explorer
  - title: Telegram test
    url: https://ooni.org/nettest/telegram/
    publisher: OONI
  - title: Frequently Asked Questions (FAQ)
    url: https://ooni.org/support/faq/
    publisher: OONI
  - title: "Risks: Things you should know before running OONI Probe"
    url: https://ooni.org/about/risks/
    publisher: OONI
  - title: ooni/probe
    url: https://github.com/ooni/probe
    publisher: GitHub
  - title: Iraqi Government Orders Telegram Ban Over Regulatory Violations
    url: https://www.kurdistan24.net/en/story/953424/iraqi-government-orders-telegram-ban-over-regulatory-violations
    publisher: Kurdistan24
    date: 2026-11-16
  - title: Jordan and Iraq block Telegram app over national security concerns
    url: https://www.al-monitor.com/originals/2026/11/jordan-and-iraq-block-telegram-app-over-national-security-concerns
    publisher: Al-Monitor（转载路透）
    date: 2026-11-17
  - title: Jordan and Iraq block Telegram over national security concerns
    url: https://www.aljazeera.com/news/2026/11/16/jordan-bans-telegram-messing-app-over-national-security-concerns
    publisher: Al Jazeera
    date: 2026-11-16
  - title: Is https://telegram.org blocked in mainland China?
    url: https://en.greatfire.org/https/telegram.org
    publisher: GreatFire
  - title: "OONI API aggregation: telegram, CN"
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=telegram&since=2026-08-22&until=2026-11-21
    publisher: OONI
regions:
  - IQ
  - JO
authors:
  - anoni-net
---

政府宣布封锁时，公告不一定交代何时生效、涵盖哪些网络，外界可以从当地网络上的测量确认。伊拉克通信与媒体委员会 11 月 16 日依总理的指令，宣布在全国封锁 Telegram，约旦的公共安全局同一天也宣布封锁。依 OONI Probe（测量网络封锁的开源软件）的测量，两国的 Telegram 测试在 11 月 15 日到 16 日之间（UTC）转为异常，到 20 日仍然全部异常。两国的命令只适用于各自境内的网络，其他地方的读者不受这次封锁影响。

伊拉克的委员会指 Telegram 没有处理平台上的违法内容、没有履行伊拉克法律规定的义务，给运营公司 30 天补正法律地位。Kurdistan24 报道的声明没有指出决定依据的是哪些频道或帖子，也没有说明期限内要完成哪些步骤、期限过后会如何处理。依 Al Jazeera 的报道，约旦的公共安全局以遏止违法内容与极端主义的内容为由宣布封锁。路透的报道写 Telegram 否认伊拉克的指控，Telegram 给路透的声明提到它打击恐怖主义的做法超出法律的要求。

OONI Probe 由用户在自己的网络上运行，测量结果公开，日期以协调世界时（UTC）计。伊拉克在封锁前每天有 67 到 80 笔 Telegram 测试，几乎没有异常。16 日的 72 笔有 33 笔异常，17 日起全部异常。讨论网络审查的公开论坛 net4people 上，一则 11 月 19 日整理两国测量的帖子提到，同一周伊拉克的 WhatsApp 与 Signal 测试维持平常的水平。

约旦的测量少得多，封锁前每天只有 1 到 8 笔，都没有异常。15 日的 13 笔有 7 笔异常，16 日起全部异常。OONI 以 UTC 计日，约旦当地时间比 UTC 快 3 小时。UTC 15 日的最后 3 小时在约旦已经是 16 日，从这些数字分不出异常是否早于公告。

## 导读观点 {#perspective}

OONI 的 Telegram 测试在用户的网络上试着连上 Telegram App 使用的服务器，也试着打开网页版 `web.telegram.org`。依 OONI 的测试说明，App 的服务器全部无法连接或网页版无法正常打开时，Telegram 可能遭到封锁。测量标为异常，代表结果符合其中一种情况，连接失败的原因要另外判断。

伊拉克 11 月 17 日以后有测量的 12 个 AS（互联网上由同一个运营商或机构管理的一组网络），以及约旦 16 日以后的 4 个 AS，每一笔测量都是异常。从这些数字看不出封锁用什么技术、在网络的哪一处拦下。一般而言，拦截的方式会影响其他服务是否一并受波及。

能看出两国的转折，是因为封锁前已经有每天正常的测量可以对照。测量只涵盖有人运行测试的网络，像约旦这样每天只有个位数测试的网络，很难判断转折发生在哪个时刻。想看数字的人不必安装，在 OONI 公开测量结果的网站 OONI Explorer 选择国家与 Telegram 测试就能查询。

在自己的网络上运行 Probe 也有代价。OONI 的常见问题写到 Probe 不是隐私工具，监控网络活动的人（例如政府、网络运营商、雇主）可能看到你在运行它。风险说明页则写到，运行 Probe 的潜在风险取决于用户的威胁模型（自己可能面对谁、对方有什么能力）与所在国家的法规。本站 11 月 20 日[OONI Probe 的 TLS Middlebox 实验与数据收集问卷](https://anoni.net/news/zh-cn/2026/11/ooni-tls-middlebox/)那篇写了 App 里可以选择运行哪些测试、不发送测量，以及做了这些设置，有人在运行 Probe 仍可能被看到。

依 OONI 公开的测量汇总，2026 年 8 月 22 日到 11 月 21 日中国大陆的 Telegram 测试共 2,324 笔，约 96% 标为异常。异常代表测试结果显示可能受到干扰，单凭这个标记还不能断定是封锁。GreatFire 对网址的测试显示，`telegram.org` 在中国大陆到 2026 年 10 月 18 日的最后一次测试为止 100% 无法连上，自 2015 年 7 月起就有干扰记录。这两组数据量的是测试与网址的连通情况，不能直接当成 App 里消息连接的状况。

伊拉克与约旦以外的读者不必为这次封锁做任何设置。依路透的报道，伊拉克 2023 年也封锁过 Telegram，一周后在政府表示公司已回应安全部门的要求之后恢复服务。两国宣布解除之后，Telegram 测试有没有回到正常，同样可以在 OONI Explorer 对照。
