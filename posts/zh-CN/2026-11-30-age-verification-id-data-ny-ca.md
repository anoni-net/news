---
title: 纽约与加州的社交平台年龄确认规则与数据保管
description: 美国纽约与加州 2027 年 1 月起要求社交平台确认用户的年龄，没有确认年龄、或未成年且没有家长同意的账号，不提供依算法推荐的动态与深夜的通知。纽约的规则限制确认年龄时能收集与保存的数据，并要求以政府证件确认年龄的平台另外提供不必出示证件的方式。规则以位在两州的用户为对象。
date: 2026-11-30T00:05:00+08:00
slug: age-verification-id-data-ny-ca
categories: [censorship]
sources:
  - title: Attorney General James and Governor Hochul Release Final SAFE for Kids Act Rules to Protect Children Online
    url: https://ag.ny.gov/press-release/2026/attorney-general-james-and-governor-hochul-release-final-safe-kids-act-rules
    publisher: New York State Attorney General
    date: 2026-07-28
  - title: SAFE for Kids Act Rule Text
    url: https://ag.ny.gov/sites/default/files/2026-07/safe_for_kids_act_rule_text.pdf
    publisher: New York State Attorney General
    date: 2026-07-28
  - title: Governor Newsom signs the strongest child safety chatbot and social media laws in the nation
    url: https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/
    publisher: Office of the Governor of California
    date: 2026-09-10
  - title: New York and California Age Gating Rules Go Into Effect in the New Year
    url: https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year
    publisher: EFF
    date: 2026-11-24
  - title: Lawmakers warn ID verification companies to bolster security after September hack
    url: https://therecord.media/idscan-data-breach-warning-congressional-letter
    publisher: The Record
    date: 2026-11-24
  - title: FBI Probes Service Selling 153M+ Drivers Licenses
    url: https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/
    publisher: KrebsOnSecurity
    date: 2026-09-01
  - title: "Now open source: our Zero-Knowledge Proof (ZKP) libraries for age assurance"
    url: https://blog.google/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/
    publisher: Google
    date: 2025-07-03
  - title: longfellow-zk
    url: https://github.com/longfellow-zk/longfellow-zk
    publisher: GitHub
  - title: 坚决防止未成年人沉迷网络游戏——国家新闻出版署有关负责人就《关于进一步严格管理 切实防止未成年人沉迷网络游戏的通知》答记者问
    url: https://www.gov.cn/zhengce/2021-08/30/content_5634208.htm
    publisher: 中国政府网
    date: 2021-08-30
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

美国纽约与加州从 2027 年 1 月起，社交平台要先确认用户已成年，才能提供依算法推荐的动态（平台替用户挑选内容、不断往下推送的首页）与深夜的通知。纽约州总检察长的新闻稿写到，这两项功能与未成年人的抑郁、焦虑、饮食与睡眠障碍有关，加州州长的新闻稿也把禁止对未满 16 岁的人提供成瘾功能列为保护未成年人的措施。加州的法律 1 月 1 日生效，纽约为 SAFE for Kids Act 制定的规则 1 月 25 日生效，两州以外的读者不在规则的范围内。

在纽约，未满 18 岁或没有确认年龄的用户只会看到自己关注或选择的账号、依固定顺序（例如时间排序）排列的内容，午夜到早上 6 点也不会收到通知。有家长同意时例外，没有同意的人也不会因此被挡在平台之外。加州的 SB 976 同样要求未满 18 岁的人取得家长同意，AB 1709 对未满 16 岁的人则是有家长同意也不提供。[AB 1043](https://anoni.net/news/zh-cn/2026/10/california-ab1856-open-source-exemption/) 是另一套机制，让操作系统把账号持有人填写的年龄范围提供给 App。

纽约的规则适用于用户至少两成时间花在算法动态上的平台。企业可以自选准确度达到规则标准、能保护用户数据的确认方式，总检察长的新闻稿举的例子有上传照片或视频，以及验证电子邮件或电话号码再比对其他信息。把政府证件列为确认方式的企业，要另外提供至少一种不必出示证件的方式。提供零知识证明（只证明已成年、不透露其他数据的密码学方法）的企业，以及依其他法律本来就要收集证件的企业，可以不另外提供这种方式。

企业确认年龄时能留下什么，纽约的规则也有限制。用来确认的数据只能收集最少量、不得挪作他用，用完要立即删除，或者去标识化之后才能继续使用。要保存五年的是跟账号连在一起的记录，内容有确认的日期、方式与结果，规则写明除此之外不要求保存其他可以识别个人的数据。平台委托外部的验证服务商时，受托的服务商同样受这些规定约束。

路易斯安那州的证件扫描服务商 IDScan 替租车公司、大麻药房这类实体柜台扫描证件，9 月传出云平台上的客户数据被窃。暗网上的销售者声称握有美国与加拿大超过 1.53 亿张驾照，KrebsOnSecurity 采访证件被卖的人之后，判断数据看来来自 IDScan。这起泄露跟社交平台的年龄确认是两件事，把两者连在一起的是 KrebsOnSecurity 的观察与它采访的隐私研究者。

## 导读观点 {#perspective}

交出证件或照片之后，副本可能留在验证服务商手上。The Record 引述 KrebsOnSecurity 的作者，他在 IDScan 事件之后的两个月里找到二十几家常默认保存证件扫描件的身份验证服务商，委托验证的公司常要多付费才能停止。KrebsOnSecurity 采访的隐私研究者认为，以保护未成年人为由要求出示驾照的线上身份机制让敏感数据流向越来越多第三方服务商，监督却跟不上。两党的国会议员 11 月 23 日也写信给数家身份验证服务商，要求尽量少收集、分享与保存个人数据。

零知识证明让企业只收到已成年这个结果，不获取证件本身。欧盟的年龄验证方案采用这种做法，本站 9 月整理过[它的隐私设计与争议](https://anoni.net/news/zh-cn/2026/09/eu-age-verification-blueprint/)。Google 在 2025 年 7 月以 Apache-2.0 许可证开源零知识证明的库 longfellow-zk，可以搭配现有的数字证件标准。纽约的规则没有要求平台提供零知识证明，平台会不会采用要等规则生效后才知道。

对同一套规则，电子前哨基金会（EFF，数字权利组织）担心去标识化的数据被用来训练 AI 模型、泄露之后被重新识别，也把五年的记录列为滥用与泄露的风险。规则要求平台采取合理措施检测用户隐藏或谎报所在地，EFF 认为这会扩大位置追踪，可能波及 VPN 用户。

成年人也可能被误判为未成年人，这时可以申诉。纽约的规则要求企业在 10 个工作日内答复或要求补件，申诉时至少要能用一种政府证件以外的资料佐证。成年人被误判的比率，规则没有定上限，只要求每年认证时列出 18 到 30 岁的误判率。

位在纽约的用户被要求确认年龄时，可以先读平台的说明再选择方式，规则要求平台写出提供哪些方式、数据的用途与删除的时间和方式。照片、视频与电话号码这些替代方式同样会把数据交给企业。不想确认年龄的人依新闻稿仍可使用平台，看到的是依固定顺序排列、只来自关注或选择账号的内容。加州的规则到 11 月 24 日还是草案，加州的用户要等定稿才知道平台会提供哪些方式。

在中国大陆，2021 年起网络游戏用户必须用真实有效的身份信息注册和登录，企业不得以游客体验模式等任何形式向未实名的用户提供服务。对未成年人，企业只能在周五、周六、周日和法定节假日每日 20 时至 21 时提供 1 小时服务。智能终端首次进入未成年人模式时要提供设置生日或选择年龄的方式，退出需家长验证同意，依据是国家互联网信息办公室（国家网信办）2024 年发布的指引。国家网信办 2026 年 9 月 18 日公开征求意见的规定草案（征求意见稿）第十条，拟要求终端制造者设置未成年人模式的联动与退出核验。

比较其他地方的规定时，隐私方面可以看有没有不出示证件的方式、企业能保存哪些数据与保存多久、委托的验证服务商是否同样受约束。未成年人保护方面可以看被误判的人如何申诉，以及规则能不能实际阻止未成年人使用这些功能。
