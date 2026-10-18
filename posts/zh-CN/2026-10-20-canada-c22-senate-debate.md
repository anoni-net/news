---
title: 加拿大 C-22 法案的参议院二读与服务商的表态
description: 加拿大的 C-22 合法访问法案 10 月 8 日在参议院进行二读辩论，到 10 月 18 日为止还没有二读通过。Signal 的副总裁在座谈会上表示，若被命令收集更多元数据就只能撤出加拿大，公共安全部长办公室则表示法案不要求解密端到端加密的信息。加拿大以外的读者现在不需要调整设置。
date: 2026-10-20T00:05:00+08:00
slug: canada-c22-senate-debate
categories:
  - encryption
follows:
  - 2026-10-05-canada-c22-lawful-access
sources:
  - title: C-22 (45-1) - LEGISinfo - Parliament of Canada
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: Debates, Issue 92 (October 8, 2026)
    url: https://sencanada.ca/en/content/sen/chamber/451/debates/092db_2026-10-08-e
    publisher: Senate of Canada
    date: 2026-10-08
  - title: "Parliamentary Committee Notes: appearance before the Standing Committee on Public Safety and National Security (SECU)"
    url: https://publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20260828-1/index-en.aspx
    publisher: Public Safety Canada
    date: 2026-05-05
  - title: Messaging service Signal says minister’s changes to lawful access bill will not persuade it to stay in Canada
    url: https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-06
  - title: Toronto-based VPN provider plans to quit Canada over lawful-access bill
    url: https://www.theglobeandmail.com/politics/article-psiphon-vpn-provider-plans-to-quit-canada-over-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-04
  - title: The Lawful Access Act threatens to blow a hole in Canada’s national security
    url: https://www.theglobeandmail.com/opinion/article-the-lawful-access-act-threatens-to-blow-a-hole-in-canadas-national/
    publisher: The Globe and Mail
    date: 2026-10-09
  - title: The Lawful Access Act’s threats to Canada’s national security
    url: https://citizenlab.ca/the-lawful-access-acts-threats-to-canadas-national-security/
    publisher: Citizen Lab
    date: 2026-10-16
  - title: Telecommunications and Other Legislation Amendment (Assistance and Access) Act 2018
    url: https://www.legislation.gov.au/C2018A00148/latest/text
    publisher: Federal Register of Legislation
  - title: 中华人民共和国反恐怖主义法
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: 中国人大网
    date: 2018-06-12
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法访问法》（Bill C-22）6 月在众议院三读通过，参议院 10 月 8 日进行二读辩论后休会，下次开会是 10 月 20 日。据加拿大国会的法案数据库 LEGISinfo，到 10 月 18 日为止法案还没有二读通过，也没有交付委员会或御准（总督签署成为法律）的记录。10 月 4 日到 16 日之间，Signal、审查规避工具 Psiphon 与多伦多大学的研究机构 Citizen Lab 都公开提出反对的理由，代表政府在参议院推动法案的参议员（提案人）则在二读演说中说明法案的保障。法案尚未通过、服务商的撤出也都附有条件，依本文的判断，加拿大以外的读者现在不需要调整设置。

Signal 的策略与全球事务副总裁 10 月 5 日在互联网协会加拿大分会的座谈会上发言，《环球邮报》（The Globe and Mail）隔天报道。据报道，这位副总裁主张法律对加密的保护要涵盖用密钥解密以外的情况，被要求大幅改动软件同样会抵消加密的目的。Signal 只保存用户的电话号码、加入日期与最后登录信息，若被命令收集更多元数据（通信内容以外的记录）并保存最长六个月，就只能撤出加拿大。到 10 月 18 日为止，Signal 的博客与 Bluesky 账号没有发表关于 C-22 的书面声明。

Psiphon 10 月 2 日向《环球邮报》表示已开始拟定把运营搬出加拿大的计划，条件是法案按现状通过。公司的副总裁在书面回复中写到，开源代码的每一行都公开，法案若要求建立访问能力就会被全世界看到（包括用户想躲避的威权政府）。Citizen Lab 一位资深研究员 10 月 9 日在同一份报纸发表评论，主张不存在只让执法单位进得去、其他攻击者却没有机会利用的设计，Citizen Lab 10 月 16 日在网站上转载了摘要。

据提案人 10 月 8 日的二读演说，法案第二部分规范服务商技术能力的新法，本身不会给执法单位或加拿大安全情报局（CSIS）新的获取信息的权力。部长命令要经情报专员（审查情报授权的独立官员）批准、接受独立审查，有效期最长两年。元数据保存限于指定的类别、最长六个月，不包含通信内容与浏览记录。公共安全部长办公室的发言人向《环球邮报》表示，法案明文不要求解密端到端加密的信息，也不允许或强迫服务商引入系统性漏洞或后门。

## 导读观点 {#perspective}

据公共安全部 5 月的委员会备询材料，服务商评估某项要求无法在不引入系统性漏洞（影响整类产品或大量用户、不只针对单一目标的漏洞）的情况下遵守时就不必遵守，政府用这个词划出服务商不必遵守的范围。提案人在演说中也提到，委员会要听取技术证据，了解一项能力被描述成针对特定目标、却可能影响整个产品或更新系统时这个词如何运作。Psiphon 被一位参议员引用的意见则是开源软件里任何法定的访问机制都会公开，无法只限于加拿大机关或单一调查。

监督方式是另一个争议点。一位参议员在辩论中批评部长命令被排除在《法定文书法》（规定法规送交国会审查的法律）之外，另一位参议员引用 Citizen Lab 与一个公民自由团体的联合意见书，意见书写到法案的义务可以在没有司法授权的情况下施加。提案人在演说中则提到，命令与佐证材料要送交国家安全与情报审查机构（NSIRA，审查情报与安全机关的独立机构），并引用警察团体代表对法案的支持。

公共安全部的备询材料提到澳大利亚有类似的保障。澳大利亚 2018 年的《协助与访问法》同样规定，技术能力通知（要求服务商建立特定能力的书面命令）不得要求服务商建立系统性弱点或系统性漏洞。澳大利亚的法律把系统性弱点定义为影响整类技术的弱点，不包括只针对特定人刻意引入的弱点（若会危及他人的信息安全仍算）。Citizen Lab 研究员的评论则引用澳大利亚的经验，写到一家公司表示信任流失造成约 10 亿澳元的经济损失。

比较各地做法时，可以问命令由谁批准、需不需要法院，以及服务商能不能公开命令的存在。系统性漏洞由谁判断、元数据保存的范围与期限，也是可以对照的地方。另外可以问政策想达成的调查目的，能不能在不削弱加密的情况下做到。

依公共安全部的说法，加拿大的法案以系统性漏洞划出服务商不必遵守的范围。类似的协助义务在中国大陆也写在《反恐怖主义法》第十八条，电信业务经营者、互联网服务提供者「应当为公安机关、国家安全机关依法进行防范、调查恐怖活动提供技术接口和解密等技术支持和协助」。本文只核对了第十八条，条文本身没有写到协助要经谁批准、需不需要法院，也没有类似系统性漏洞的除外规定。服务商能否公开收到的要求，第十八条同样没有写到。

Signal 与 Psiphon 的撤出都附有条件，到 10 月 18 日为止两家都没有宣布撤出的日期。参议院 10 月 20 日复会后的二读表决，以及法案交付哪个委员会，是接下来可以观察的进度。在加拿大的读者会受什么影响，要看法案最后的条文与服务商的决定。
