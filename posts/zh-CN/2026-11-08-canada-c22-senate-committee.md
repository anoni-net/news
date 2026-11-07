---
title: 加拿大 C-22 法案的参议院委员会审查与加密弱点的争论
description: 加拿大的 C-22 合法访问法案 10 月 22 日在参议院二读通过，交付国家安全、国防与退伍军人事务委员会审查，到 11 月 7 日为止还没有三读。Citizen Lab 的研究员主张 6 月以来 AI 带动的网络威胁出现重大变化，通信系统不该再留下弱点。政府 5 月的备询材料则主张法案不要求建立后门，服务商可以拒绝会引入系统性漏洞的要求。加拿大以外的读者现在不需要调整设置。
date: 2026-11-08T00:05:00+08:00
slug: canada-c22-senate-committee
categories: [encryption]
follows:
  - 2026-10-20-canada-c22-senate-debate
sources:
  - title: C-22 (45-1) - LEGISinfo - Parliament of Canada
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: "Built-In Weakness: Lawful Access and Encryption in the Age of AI-Powered Cyber Threats"
    url: https://citizenlab.ca/built-in-weakness-lawful-access-and-encryption-in-the-age-of-ai-powered-cyber-threats/
    publisher: Citizen Lab
    date: 2026-10-23
  - title: We Shouldn’t Have to Give Up Our Safety Online to Be Safe
    url: https://www.internetsociety.org/blog/2026/10/we-shouldnt-have-to-give-up-our-safety-online-to-be-safe/
    publisher: Internet Society
    date: 2026-10-21
  - title: The Lawful Access Act threatens to blow a hole in Canada’s national security
    url: https://www.theglobeandmail.com/opinion/article-the-lawful-access-act-threatens-to-blow-a-hole-in-canadas-national/
    publisher: The Globe and Mail
    date: 2026-10-09
  - title: Messaging service Signal says minister’s changes to lawful access bill will not persuade it to stay in Canada
    url: https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-06
  - title: Analysis of Proposed Surveillance Law Expansion under Bill C-22
    url: https://citizenlab.ca/research/analysis-of-proposed-surveillance-law-expansion-under-bill-c-22/
    publisher: Citizen Lab
    date: 2026-06-02
  - title: "Parliamentary Committee Notes: appearance before the Standing Committee on Public Safety and National Security (SECU)"
    url: https://publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20260828-1/index-en.aspx
    publisher: Public Safety Canada
    date: 2026-05-05
  - title: Investigatory Powers Act 2016, section 253
    url: https://www.legislation.gov.uk/ukpga/2016/25/section/253
    publisher: legislation.gov.uk
  - title: Cryptography Law of the People's Republic of China (China Law Translate 英译本)
    url: https://www.chinalawtranslate.com/en/cryptography-law/
    publisher: China Law Translate
  - title: 中华人民共和国反恐怖主义法
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: 中国人大网
    date: 2018-06-12
  - title: Implementation Rules for Article 43 of the Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region gazetted
    url: https://www.info.gov.hk/gia/general/202007/06/P2020070600784.htm
    publisher: Hong Kong Government
    date: 2020-07-06
  - title: 2026 年〈中华人民共和国香港特别行政区维护国家安全法第四十三条实施细则〉(修订)实施细则
    url: https://www.doj.gov.hk/tc/legco/pdf/ajls20260324c1.pdf
    publisher: 香港律政司
    date: 2026-03-24
  - title: 署理律政司司长与保安局局长出席立法会司法及法律事务委员会及保安事务委员会联席会议后会见传媒开场发言
    url: https://www.doj.gov.hk/tc/community_engagement/press/pdf/pr20260324c2.pdf
    publisher: 香港律政司
    date: 2026-03-24
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法访问法》（Bill C-22）10 月 22 日在参议院完成二读，同一天交付参议院国家安全、国防与退伍军人事务常设委员会审查。加拿大国会的法案数据库 LEGISinfo 列出委员会 11 月 2 日的一次会议，到 11 月 7 日为止委员会还没有提出报告。法案 6 月已在众议院三读通过，参议院 10 月辩论期间，通信与审查规避工具的服务商都公开提出反对的理由。法案还没有成为法律，加拿大以外的读者现在不需要调整设置。

法案让政府能要求通信与网络服务商建立协助执法的技术能力，也能以法规要求服务商保存元数据（通信内容以外的记录）。参议院到 11 月 7 日没有通过任何修正，委员会提出报告之后，法案才会进入三读。

Citizen Lab 是多伦多大学的研究室，10 月 23 日在网站上贴出一场座谈的视频。依主办方之一 Internet Society（在世界各地设有分会、推动开放与安全互联网的国际组织）的帖子，座谈在 10 月初为国会议员举行，主题是合法访问在 AI 带动网络威胁的时代代表什么。页面只有一段文字，写到 Citizen Lab 的资深研究员在座谈上谈法案的法律疑虑。研究员强调应该修补与预防漏洞，不要在日常的通信系统上“钻更多洞”。

同一位研究员 10 月 9 日在《环球邮报》（The Globe and Mail）发表评论，主张 6 月以来 AI 带动的网络威胁出现重大变化。作者在评论里举的例子包括 7 月 OpenAI 的 AI agent 逃出沙箱、攻击软件公司 Hugging Face，以及外界对 Anthropic 未公开发布的模型 Claude Mythos 的担忧。评论没有附这些事件的来源，本文也没有核对相关公司的原始公告。依评论的结论，政府官员假设科技公司能找到“安全的方式”削弱信息安全防护，误判了当前的威胁环境。

Citizen Lab 6 月提交给众议院委员会的意见书早于研究员 10 月的评论，内容是逐部分检视条文的法律与政策分析。意见书的核心建议是整个撤回法案第二部分，也就是规范服务商技术能力的新法。理由之一是政府可以对任何电子服务商施加任何义务，包括改变服务的运作方式或在服务里嵌入监控工具。意见书只有一句提到 AI，内容是随着 AI 监控技术增加，法案的侵入性也会跟着提高。

## 导读观点 {#perspective}

依 Citizen Lab 的意见书，为了配合监控义务而修改的技术设计很难保护，范围比加拿大更窄的美国与新西兰制度也多次被外国情报机关秘密入侵。意见书引用美国国家安全局（NSA）的测试，NSA 测试的符合美国监听能力法 CALEA 的交换机每一台都有安全漏洞，也引用与中国政府有关的黑客组织 Salt Typhoon 入侵美国监听能力系统的事件。依本站 11 月 7 日整理的 [EFF 文章](https://anoni.net/news/2026/11/eff-security-worse/)，前沿 AI 模型让找漏洞变得便宜。10 月 10 日那篇则整理了 [Anthropic 测试开放权重模型写出攻击浏览器程序的报告](https://anoni.net/news/2026/10/glm-5-3-cyber-capabilities/)。

依公共安全部长 5 月 5 日到众议院委员会备询的材料，政府不支持、法案也不要求建立后门，政府只订定对服务商的要求、不指定技术做法。服务商评估某项要求无法在不引入系统性漏洞（影响整类产品或大量用户、不只针对单一目标的漏洞）的情况下遵守时，就不必遵守。系统性漏洞已经在条文里定义，部长命令也要事先经情报专员（审查情报授权的独立官员）批准。Citizen Lab 的意见书则把法案的保障评为弹性大、定义不清，适用范围也没有设限。

Citizen Lab 研究员的评论把 AI 当成 6 月之后的新情况，主张政府期待服务商兼顾监控义务与信息安全的前提，已经跟不上威胁的变化。公共安全部的备询材料早于这波论点，材料转述通信安全局（CSE，加拿大负责信号情报与网络安全的机关）的意见，认为恶意网络活动的威胁本来就存在。依备询材料转述的 CSE 评估，法案让合法访问从临时、自愿的做法改成标准化的管理，能改善信息安全。公共安全部长办公室的发言人 10 月初向《环球邮报》表示，法案不允许或强迫服务商引入系统性漏洞或后门。

依备询材料，加拿大的警察与情报人员对付懂技术的犯罪者与国家行为者时，用的是数十年前的工具。政府把法案定位成补上这个落差的做法。Internet Society 首席执行官在同一场座谈的开场演讲中，提出的替代做法是加强数字取证能力、改善跨境合作、相称地使用元数据，以及跟服务商建立合作关系。演讲的前提是弱点一旦存在，任何找到它的人都能利用。

法案到 11 月 7 日仍在参议院委员会审查，依本文的判断，在加拿大的读者现在也不需要调整设置。前面提到的 EFF 文章给每个人的建议是更新浏览器与 App、改用密码管理器并提防钓鱼，这些做法跟法案的结果无关。接下来可以留意委员会的报告有没有修正第二部分，以及参议院三读的时间。

英国的《调查权力法》（Investigatory Powers Act 2016）第 253 条同样让政府对服务商发出技术能力通知，通知要经司法专员批准，可以规定的义务包括移除服务商自己施加的电子保护。依本站 9 月的整理，Apple 收到通知之后，从 2025 年 2 月起不再让英国的新用户开启 [iCloud 高级数据保护](https://anoni.net/news/2026/09/uk-icloud-advanced-data-protection/)。依政府 5 月的备询材料，加拿大的部长命令由情报专员事先批准。法案也另设例外，服务商评估会引入系统性漏洞时可以不遵守。

依 China Law Translate 的非官方英译本，中国大陆《密码法》（2020 年 1 月 1 日施行）第三十一条第二款规定，密码管理部门和有关部门及其工作人员不得要求商用密码从业单位和商用密码检测认证机构披露源代码等密码相关专有信息。译本里读过的第二十六条到第三十二条，没有要求服务商替执法机关解密的条文。协助义务写在别的法律，[本站此前的导读](https://anoni.net/news/zh-cn/2026/10/canada-c22-senate-debate/)提到的《反恐怖主义法》第十八条，要求电信业务经营者、互联网服务提供者为公安机关、国家安全机关依法进行防范、调查恐怖活动提供技术接口和解密等技术支持和协助。依本文的归纳，两部法律管的对象不同，《密码法》这一款限制的是主管部门索取源代码。

依政府 2020 年 7 月的英文公布，香港《维护国家安全法》第四十三条实施细则让警方在特定情况下向裁判官申请手令，要求服务供应者提供识别记录（identification record，中文名称是本文依英文译出）或解密协助。2026 年 3 月 23 日刊宪的修订细则让警方调查危害国家安全罪行时，可以要求个人（“指明人士”，包括嫌疑人与警方合理相信知道密码的人）提供电子设备的密码，对象不是服务商。无合理辩解而不遵从的，最高罚款 10 万港元及监禁 1 年。依保安局局长 3 月 24 日向媒体的说法，警方要先以誓章向法院申请搜查令，本文对中国大陆与香港都没有查服务商能不能公开收到的要求。

比较各地做法时，可以问命令由谁批准、服务商能不能拒绝或公开命令，以及系统性漏洞最后由谁认定。也可以问威胁环境改变之后，谁负责重新评估已经建立的访问能力。另外要问政策想达成的调查目的，能不能用数字取证、跨境合作这类不削弱加密的方法做到。也可以从政府的标准问，标准化的访问能力能不能补上备询材料提到的调查工具落差，又能不能改善 CSE 提到的临时、自愿做法的信息安全问题。
