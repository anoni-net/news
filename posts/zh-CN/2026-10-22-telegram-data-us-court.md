---
title: Telegram 交给美国执法部门的用户数据
description: 美国联邦法院新归档的文件里，有一封 Telegram 依法院命令提供用户电话号码、用户 ID 与 IP 地址的信。Telegram 的隐私政策 2024 年 9 月起，把可以提供 IP 地址与电话号码的范围从恐怖活动嫌疑人扩大到违反服务条款的犯罪案件，条文没有限定适用地区。到 10 月 20 日为止，没有看到 Telegram 对这批文件的公开回应。
date: 2026-10-22T00:05:00+08:00
slug: telegram-data-us-court
categories:
  - encryption
sources:
  - title: Telegram Privacy Policy
    url: https://telegram.org/privacy
    publisher: Telegram
  - title: Telegram FAQ
    url: https://telegram.org/faq
    publisher: Telegram
  - title: Telegram Privacy Policy
    url: https://web.archive.org/web/20240901002603/https://telegram.org/privacy
    publisher: Internet Archive
  - title: Scheduled Messages, Reminders, Custom Cloud Themes and More Privacy
    url: https://telegram.org/blog/scheduled-reminders-themes
    publisher: Telegram
    date: 2019-09-05
  - title: Here’s What Telegram Giving Data to the U.S. Government Looks Like
    url: https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/
    publisher: 404 Media
    date: 2026-10-16
  - title: Court filing reveals the user data Telegram is handing over to US authorities
    url: https://cyberinsider.com/telegram-sharing-user-data-with-us-authorities/
    publisher: CyberInsider
    date: 2026-10-17
  - title: Telegram Hands U.S. Authorities Data on Thousands of Users
    url: https://www.404media.co/telegram-hands-u-s-authorities-data-on-thousands-of-users/
    publisher: 404 Media
    date: 2025-01-06
  - title: Crowdsourcing Telegram ‘transparency reports’ to map the network’s claimed compliance with governments around the world
    url: https://meduza.io/en/feature/2024/10/23/crowdsourcing-telegram-transparency-reports-to-map-the-network-s-claimed-compliance-with-governments-around-the-world
    publisher: Meduza
    date: 2024-10-23
  - title: telegram-transparency
    url: https://github.com/Te-k/telegram-transparency
    publisher: GitHub
  - title: Translations
    url: https://translations.telegram.org/zh-hant/
    publisher: Telegram
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
  - title: Real-name Registration Programme for Subscriber Identification Module (SIM) Cards
    url: https://www.ofca.gov.hk/en/consumer_focus/guide/hot_topics/sim_registration/index.html
    publisher: 通讯事务管理局办公室
  - title: Is https://telegram.org blocked in mainland China?
    url: https://en.greatfire.org/https/telegram.org
    publisher: GreatFire
  - title: "OONI API aggregation: telegram, CN"
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=telegram&since=2026-07-18&until=2026-10-18
    publisher: OONI
regions:
  - US
authors:
  - anoni-net
---

404 Media 10 月 16 日报道，美国联邦法院新归档的文件里有一封 Telegram 写给美国当局的信，依法院命令提供了一位用户的电话号码、用户 ID 与 IP 地址。依 CyberInsider 的报道，信件日期是 9 月 4 日，10 月 15 日在路易斯安那州西区联邦地区法院的一件刑事案件中归档。Telegram 隐私政策里提供 IP 地址与电话号码的条文没有限定地区，美国以外的用户也适用同一套规则。到 10 月 20 日为止，没有看到 Telegram 对这批文件的公开回应。

404 Media 的报道有付费墙，写稿时只读得到开头，到 10 月 20 日为止法院文件本身也查不到。信件的细节因此依 CyberInsider 的报道。信中的 IP 地址附有协调世界时（UTC）的时间戳，代表账号最后一次登录的时间。Telegram 在信中把这次提供描述为自愿，并表示提供数据不代表接受美国的管辖。

依 CyberInsider，这份附件只有账号与连接信息、没有消息内容，但不代表调查人员没有从其他渠道取得别的数据。同一篇也提到，Telegram 通常需要电话号码才能查到账号的非公开数据。账号先前因内容管理被处置过，或 Telegram 收到正式请求后启用了额外记录时，有时凭用户名或数字 ID 也可以。信中没有说这个账号有没有启用额外记录。

根据 10 月 20 日查阅的 Telegram 隐私政策第 8.3 条，收到有效的司法命令时 Telegram 会先做法律分析，可能向相关机关提供 IP 地址与电话号码。命令要确认用户是违反服务条款的犯罪案件嫌疑人，提供之后会写进每季度的透明度报告。网页存档的旧版本显示，2024 年 9 月 23 日修改以前这一条只限恐怖活动嫌疑人，还写到「So far, this has never happened」（到目前为止从未发生）。

透明度报告要用 Telegram 账号向官方机器人查询，依 Meduza 2024 年 10 月的说明，机器人只返回查询者账号注册所在国的数据。404 Media 2025 年 1 月引述机器人的回复，2024 年 1 到 9 月 Telegram 完成美国调取 IP 地址或电话号码的请求 14 次、涉及 108 位用户，全年则是 900 次、2,253 位。另有一份由用户贴上机器人回复、在 GitHub 汇整的众包数据集，2025 年美国是 1,706 次、4,807 位。Telegram 没有在网页上公开这些数字。

## 导读观点 {#perspective}

依 10 月 20 日查阅的 Telegram FAQ 与隐私政策，一般对话（云端对话，包括一对一对话与群组）在客户端与服务器之间加密，消息存在 Telegram 的服务器上。私密对话（Secret Chats）是端到端加密（只有对话双方的设备能解开），不存在服务器上，只留在双方各自开启这段对话的那台设备。FAQ 的数据请求一节写到，云端对话的解密密钥分散在不同司法管辖区，「To this day, we have disclosed 0 bytes of user messages to third parties, including governments」（至今没有向包括政府在内的第三方披露任何用户消息）。这一节只涉及消息内容，IP 地址与电话号码的提供条件写在隐私政策第 8.3 条。

Telegram 在这封信提供的是电话号码、用户 ID 与 IP 地址这类账号数据。隐私政策第 5.2 条提到，为了账号安全与防止垃圾消息和滥用，Telegram 可能收集 IP 地址、使用过的设备与 App、用户名的变更记录。有收集的话，这些记录最多保存 12 个月。注册账号也需要电话号码。

香港的《电讯（登记电话智能卡）规例》2021 年 9 月 1 日生效，2022 年 3 月 1 日起所有月费计划与储值卡都要先实名登记才能启用。个人要登记中英文姓名、出生日期与香港身份证号码及副本。从 Telegram 隐私政策第 8.3 条与这项规定可以推出，用香港号码注册的账号一旦号码被交出，号码在运营商那里对应的是登记过的实名信息。

第三方监测网站 GreatFire 10 月 18 日的最后一次测试显示，`https://telegram.org` 在中国大陆 100% 被封锁（2015 年 7 月 10 日起就有干扰记录），`https://t.me` 也列为封锁。GreatFire 测试网址能否连接，不包括 App 的消息连接。在 OONI（网络干扰观测项目）公开 API 的汇总里，7 月 18 日到 10 月 18 日在中国的 Telegram 测试共 2,877 笔，其中 2,819 笔标为异常（anomaly）、0 笔确认封锁（异常不等于确认封锁）。前面提到的众包数据集里，中国大陆与香港只有 2024 年 1 到 9 月的数据（Telegram 完成的请求都是 0 次），没有更晚的数字。

根据 FAQ，电话号码默认只有你存进通讯录的联系人看得到，路径是 Settings > Privacy and Security > Phone Number（中文界面的用词以 App 为准）。官方博客 2019 年的说明提到，把谁能看到号码设成 Nobody 之后，还可以把谁能用号码找到你设成只限联系人（现行界面的名称以 App 为准）。依同一篇说明，把你的号码加进联系人的陌生人就对应不到你的个人资料（FAQ 提醒已经存了你号码的人仍然看得到）。用户名一律公开，FAQ 也建议不想被搜索找到的人不要设置。

对于需要处理敏感对话的人，FAQ 建议只在官方或可验证的开源 App 里使用私密对话并搭配自毁计时器，也建议开启两步验证与密码锁。私密对话要在对方的个人页点选「…」再选 Start Secret Chat，退出登录后私密对话会消失。Telegram 的翻译平台上有简体中文语言包，FAQ 与隐私政策则没有中文版。依隐私政策第 5.2 条与注册需要电话号码推论，这些做法不会让 Telegram 手上没有账号号码，IP 地址有没有被收集则依第 5.2 条的情况而定。
