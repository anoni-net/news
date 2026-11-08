---
title: 生成式 AI 用于跨国镇压的案例与 AI 厂商的应对
description: Anthropic 9 月的威胁情报报告列出国家相关行为者用 Claude 进行监控的案例，其中几件以居住在国外的异见人士为对象。Citizen Lab 研究者 10 月在 Just Security 的评论分析这份报告，建议 AI 厂商在披露与通知、检测与拒绝、保存证据三方面着手。报告与评论都没有给普通用户的设置建议。
date: 2026-11-12T00:05:00+08:00
slug: genai-transnational-repression
categories:
  - civil-society
sources:
  - title: "Detecting and countering misuse of AI: September 2026"
    url: https://www.anthropic.com/threat-intelligence-report-september-2026
    publisher: Anthropic
    date: 2026-09-10
  - title: How Generative AI is Scaling Transnational Repression
    url: https://www.justsecurity.org/159245/how-generative-ai-scaling-transnational-repression/
    publisher: Just Security
    date: 2026-10-12
  - title: How Generative AI is Scaling Transnational Repression
    url: https://citizenlab.ca/how-generative-ai-is-scaling-transnational-repression/
    publisher: Citizen Lab
    date: 2026-10-22
  - title: Supported Regions Policy
    url: https://www.anthropic.com/supported-countries
    publisher: Anthropic
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: 互联网信息服务深度合成管理规定
    url: https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm
    publisher: 中国网信网
    date: 2022-12-11
  - title: 关于印发《人工智能生成合成内容标识办法》的通知
    url: https://www.gov.cn/zhengce/zhengceku/202503/content_7014286.htm
    publisher: 中国政府网
    date: 2025-03-07
authors:
  - anoni-net
---

Anthropic 的威胁情报团队 9 月 10 日发布〈Detecting and countering misuse of AI: September 2026〉，监控一章列出 2026 年 1 到 7 月间发现并中断的一系列行动。依报告，国家相关的组织、替国家工作的承包商与商业间谍软件厂商用 Claude 搭建、运行监控。其中部分案例被报告归为跨国镇压，对象是居住在国外的异见人士与海外社区。

Citizen Lab 的三位研究者 10 月 12 日在 Just Security 发表评论分析这份报告，Citizen Lab 网站 10 月 22 日转载了摘要。评论分析的案例都出自 Anthropic 的报告。报告与评论的对象都是攻击者如何使用 AI 服务，都没有给普通用户的设置建议。

研究者引用 Freedom House 的定义，数字跨国镇压指政府用数字技术恐吓、压制流亡在外与海外社区里的异见人士。依研究者先前访谈受影响者的研究，这类威胁造成恐惧与孤立，也让人自我审查、退出倡导活动。

研究者把报告的案例归纳成四项变化。第一项是成本，数字镇压原本依赖语言能力、受过训练的情报分析师与软件工程师，研究者认为案例显示 AI 可以取代其中一部分。第二项是公开数据的整理，海外社区在社交平台、即时通信软件、公开数据库与组织网站留下大量数据。AI 助手可以把零散的数据整理成情报报告，用来重建人际关系、推断政治倾向与找出所在位置，甚至标出弱点。

第三项是把模型接进固定的流程，少数人员就能监督重复运行、部分自动化的监控报告，其中一案每天自动审阅 15 到 30 篇以上的外国媒体报道。第四项，监控的产出可以支持实体跟踪、胁迫、发展线人与干扰公民团体的活动。研究者也写到报告没有证明这些侦察导致了实体攻击。

依报告的案例，模型参与的环节还包括翻译与用方言撰写消息、为假的网络人设生成多语帖子，以及编写代码搭建浏览器扩展这类监控工具。其中一案还在试行阶段，另外备有超过 255 个合成的社交账号，报告认为这显示是先备好账号、之后再投入使用。对照先前一份新闻调查描述的后续监控环节，报告在封禁账号之前没有发现它们用在真实对象上。另一案计划对流亡媒体的记者发动集体举报与机器人账号放大，报告的写法是计划，没有写已经执行。

依报告，在计划对流亡媒体记者集体举报的同一个行动里，Claude 拒绝了几项秘密审讯与大规模生成假人设的请求。在评论归为国内监控的一件案例里，Claude 先拒绝生成监控报告。对方换个说法重新提问之后，模型仍生成了点名 10 位平民的指引。评论提到的另一件国内案例做出的监控系统完全在本地模型上运行，Anthropic 封禁了账号，却无法停用已经部署的系统。

Anthropic 的使用政策禁止用 Claude 进行未经同意的监控与侧写，也禁止用来侵害个人的公民自由与人权。依报告，每个案例都封禁了相关账号，也改进检测同类手法的能力。行动影响到平台以外时，Anthropic 视情况把识别信息与情报分享给行业伙伴与主管机关。报告另外提到部分行为者用 VPN 绕过 Anthropic 的服务地区限制。

研究者写明这份报告只反映一家公司在短期内看得到、检测得到的范围，部分归因的信心也有限。以报告本身为例，其中一案只以低信心判断行为者是替国家安全机关工作的承包商，而不是机关本身。

## 导读观点 {#perspective}

研究者提到过去对 AI 用于跨国镇压的警告多半从技术能力推想，少有具体的案例，并认为 Anthropic 的报告提供了少见的操作细节。研究者建议检测不要只抓容易识别的镇压字眼，改为标出社交监控、地理定位、弱点侧写与政治倾向推断同时出现的组合，这些能力合起来可以指向一套跨国镇压的工作流程。

研究者的建议以联合国《工商业与人权指导原则》（UNGPs）为依据，指导原则要求企业处理自身涉入的人权负面影响。评论主张 AI 厂商把跨国镇压列为独立的威胁类别，跟国内监控、影响力行动分开，并在三个方向上着手。到 11 月 8 日，查不到 Anthropic、OpenAI、DeepMind 与 xAI 对评论的公开回应。厂商这一方目前只看得到 Anthropic 9 月的报告，它早于评论发表，不是对建议的回应。

在第一个方向披露与通知上，Anthropic 的报告本身就是一份公开披露，处置的部分写的是视情况把信息分享给行业伙伴与主管机关。研究者肯定报告的细节，也认为 OpenAI、DeepMind 与 xAI 可能遇到类似的行动，只是没有标准化的报告可以评估。研究者也建议通知受影响的社区，Google 与 Apple 已经有通知国家支持攻击对象的流程。这类通知发给的是遭锁定的自家用户，AI 厂商面对的被锁定者却不一定是自家的用户，研究者因此建议用对方读得懂的格式与语言做社区层面的通知。

在第二个方向检测与拒绝上，研究者肯定 Anthropic 多次在行动大规模部署之前就发现并阻止，也指出部分案例换个说法重新提问就绕过了拒绝。Anthropic 的报告写的做法是在每个案例改进检测同类手法的能力，并把调查的结果并入防护措施。

在第三个方向保存证据上，研究者提到已有民事诉讼与刑事调查来自数字跨国镇压演变成实体伤害的案件。研究者因此主张厂商保存包含归因数据的详细事件记录，供日后调查使用。研究者也写明该保存什么取决于各地法律，目前仍有争议。

评论与 Citizen Lab 的页面都没有给被锁定者的操作建议。Google 与 Apple 各有通知国家支持行动锁定对象的流程，评论把它们当作 AI 厂商建立通知机制时的参考。

Anthropic 的 Supported Regions Policy 页面标示 2026 年 11 月 12 日生效，11 月 2 日查证的清单含日本、新加坡、韩国、台湾，没有中国大陆、香港与澳门（页面写明不在清单内的国家与地区不受支持）。10 月 20 日查证的 OpenAI ChatGPT 支持国家清单同样没有这三个地区（在清单以外使用可能导致账号被封锁或停权）。中国大陆境内提供的生成合成服务适用《互联网信息服务深度合成管理规定》（2023 年 1 月 10 日施行）与《人工智能生成合成内容标识办法》（2025 年 9 月 1 日施行）。前者要求提供者处理利用服务制作的虚假信息（第十一条），后者规定生成合成内容的标识义务。

之后读到其他 AI 厂商的威胁报告时，可以比较几件事：有没有把跨国镇压独立分类、处置包含哪些步骤（封禁账号、改进检测、分享情报）、有没有通知被锁定的社区、保存了哪些记录。另一组问题是效果，研究者指出部分案例换个说法就绕过了拒绝。系统部署在本地模型上时，封禁账号也停不了，检测要早到哪个阶段才有用也值得比较。研究者提到行业没有标准化的报告，各家之间能不能比较，也取决于会不会建立共同的格式。
