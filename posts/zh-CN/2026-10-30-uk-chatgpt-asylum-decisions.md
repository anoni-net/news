---
title: 英国内政部用生成式 AI 摘要庇护面谈的争议
description: 英国数字权利团体 Open Rights Group 10 月发表调查，内政部在庇护案件使用两个生成式 AI 工具，其中一个摘要面谈记录。内政部的业务专家抽查 203 份摘要，第一轮判定 22% 不能使用。现任负责的部长在信中写到，申请人没有被特别告知 AI 参与了处理。内政部表示工具只是辅助，不会取代审查人员的决定。
date: 2026-10-30T00:00:00+08:00
slug: uk-chatgpt-asylum-decisions
categories:
  - tracking
regions:
  - GB
sources:
  - title: ORG Investigation into use of ChatGPT in asylum decisions highlights errors, inaccuracies and Home Office incompetence
    url: https://www.openrightsgroup.org/press-releases/org-investigation-into-use-of-chatgpt-in-asylum-decisions-highlights-errors-inaccuracies-and-home-office-incompetence/
    publisher: Open Rights Group
    date: 2026-10-12
  - title: The Use of ChatGPT in Asylum Decisions
    url: https://www.openrightsgroup.org/publications/the-use-of-chatgpt-in-asylum-decisions/
    publisher: Open Rights Group
    date: 2026-10-12
  - title: Evaluation of AI trials in the asylum decision making process
    url: https://www.gov.uk/government/publications/evaluation-of-ai-trials-in-the-asylum-decision-making-process/evaluation-of-ai-trials-in-the-asylum-decision-making-process
    publisher: Home Office
    date: 2025-04-29
  - title: Letter from the Minister for Border Security and Asylum (22 June 2026)
    url: https://www.openrightsgroup.org/app/uploads/2026/10/Letter-to-Bell-Ribeiro-Addy-MP-from-Alex-Norris.pdf
    publisher: Home Office（经 Open Rights Group 公布）
    date: 2026-06-22
  - title: Letter from the Minister for Border Security and Asylum (7 August 2026)
    url: https://www.openrightsgroup.org/app/uploads/2026/10/Letter-to-Bell-Rebeiro-Addy-from-Anna-Turley.pdf
    publisher: Home Office（经 Open Rights Group 公布）
    date: 2026-08-07
  - title: An inspection of asylum casework (June – December 2025)
    url: https://www.gov.uk/government/publications/an-inspection-of-asylum-casework-june-december-2025
    publisher: Independent Chief Inspector of Borders and Immigration
    date: 2026-06-25
  - title: UK Home Office May Face Investigation Over Use of OpenAI Tech
    url: https://www.wired.com/story/uk-home-office-may-face-investigation-over-use-of-openai-tools/
    publisher: WIRED
    date: 2026-10-27
  - title: Home Office asylum AI flunks one in five accuracy checks
    url: https://www.theregister.com/public-sector/2026/10/13/home-office-asylum-ai-flunks-one-in-five-accuracy-checks/5302649
    publisher: The Register
    date: 2026-10-13
  - title: "Automating the Hostile Environment: AI in the asylum decision-making process"
    url: https://www.openrightsgroup.org/app/uploads/2026/01/Automating-the-Hostile-Environment-AI-tools-in-Asylum-Policy-Paper.pdf
    publisher: Open Rights Group
  - title: "Borders, immigration and citizenship: privacy information notice"
    url: https://www.gov.uk/government/publications/personal-information-use-in-borders-immigration-and-citizenship/borders-immigration-and-citizenship-privacy-information-notice--2
    publisher: Home Office
  - title: "The use of artificial intelligence tools by government: a case study of the Home Office's asylum practice: joint legal opinion for the Open Rights Group"
    url: https://www.openrightsgroup.org/app/uploads/2026/03/Legal-Opinion-on-AI-tools-in-the-asylum-process.pdf
    publisher: Open Rights Group
  - title: Data, privacy, and security for Foundry Models sold by Azure in Microsoft Foundry
    url: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy
    publisher: Microsoft Learn
  - title: Algorithmic Transparency Records
    url: https://www.gov.uk/algorithmic-transparency-records
    publisher: GOV.UK
  - title: 【資安宣導】行政院於112年10月3日函頒「行政院及所屬機關（構）使用生成式 AI 參考指引」，敬請參考
    url: https://www.sme.gov.tw/article-tw-2391-11626
    publisher: 經濟部中小及新創企業署
  - title: 人工智慧基本法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0160093
    publisher: 全國法規資料庫
  - title: 政务领域人工智能大模型部署应用指引
    url: https://www.cac.gov.cn/2025-10/10/c_1761819469929310.htm
    publisher: 中国网信网
    date: 2025-10-10
  - title: 中央网信办、国家发展改革委印发《政务领域人工智能大模型部署应用指引》
    url: https://www.cac.gov.cn/2025-10/10/c_1761819469876932.htm
    publisher: 中国网信网
    date: 2025-10-10
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 中国人大网
    date: 2021-08-20
authors:
  - anoni-net
---

英国数字权利团体 Open Rights Group（ORG）10 月 12 日发表报告，整理半年来对内政部两个生成式 AI 工具的调查。庇护案件摘要工具（ACS）把庇护面谈的逐字记录整理成摘要给审查人员，庇护政策搜索工具（APS）让审查人员以对话方式查询各国的政策信息。据 ORG 的报告，两者建在 OpenAI 的 GPT-4o 上、通过 Microsoft 的 Azure 提供。ORG 1 月的文件与 WIRED 则写 GPT-4，内政部自己的公开文件没有写出模型名称。

ACS 在 2026 年 4 月全面上线。据 ORG 通过议会质询与信息公开申请取得的资料，内政部的业务专家此后抽查了 203 份摘要。第一轮判定 45 份不能使用（22%），另有 19 份标记后送第二轮复查。第二轮的 56 份里有 30 份不能使用，报告以 203 份为分母算成 15%（30÷203 约 14.8%，这是我们的换算），也没有说明 19 份跟 56 份为何对不上。

ORG 拿这两个数字跟内政部 2025 年试行评估的 9% 比较，那是试行时技术专员逐份审查后、因不准确或缺漏而剔除的摘要比例，跟上线后的抽查方法不同。The Register 的报道写到内政部没有回复该媒体的提问，我们也没有查到内政部对这些数字的公开回应。

ORG 依数据保护影响评估（处理高风险个人信息前要做的评估）的月平均推算，4 到 7 月约处理 7 万个案件，只有 0.3% 经过专家抽查。受影响的是在英国申请庇护的人，现任负责庇护的部长 8 月给议员的信写到，他们没有被特别告知 AI 参与了案件的处理。内政部的隐私声明写到部分处理可能涉及自动化，复杂或不利的决定一定由受过训练的人员作出，声明里没有提到这两个工具。ORG 委托三位律师在 2 月出具的法律意见（委托方取得的意见，未经法院判断）认为，没有告知申请人「很可能违法」，我们没有查到内政部对这份意见的公开回应。

## 导读观点 {#perspective}

据 WIRED 转述的内政部回应，庇护决定由受过训练的审查人员作出，工具不能单独使用、也不会对申请作出决定。前任部长 6 月的信也写到，摘要只是审查人员决定前要读的文件之一，审查人员仍要读完案件的所有文件。内政部也承诺公布更新的评估。

2025 年的试行评估写到，使用 ACS 的组别读完一份逐字记录比对照组快 23 分钟（约省下 32%）。评估自己也写明这是小规模试行，全面上线前需要进一步评估。ORG 认为，审查人员若仍要读完所有文件，就不可能省下这些时间。

ORG 以信息公开申请取得的数字指出，2026 年 4 月起每月的初次实质决定比前一年同期少约 42%，从面谈到决定的平均时间增加 29%。The Register 的报道写到，这些数字不能证明是 AI 造成的，也看不出部长承诺的效率提升。ORG 主张在庇护申请全面禁用 AI，报告的建议是先暂停两个工具、委托独立的审计。

两边对工具做了什么有不同的描述。部长 8 月的信写到，这些工具摘要申请人提供的信息，不会产生新内容。ORG 的报告则写到两个工具都会产生新的文字，可能筛掉、改写或遗漏跟决定有关的事实。

据 ORG 报告的描述，大语言模型的摘要是重新生成的句子，部长 8 月的信没有说明「新内容」指的范围。试行评估写到 ACS 的摘要刻意没有标示原文出处，以降低试行的技术复杂度，之后可以重新考虑。没有出处编号时，审查人员不容易对照逐字记录的原句（本文的推论），部长的信则写到之后要加上出处的编号。

前任部长 6 月的信写到专家每周抽查 ACS 的产出，内政部也对 WIRED 表示会定期监控工具的表现。据 ORG 的报告，抽查表里「是否遗漏最相关的事实」这一项有评分，但不列为不合格的条件。ORG 据此认为遗漏重要事实的摘要只要剩下的内容正确，仍可能通过，内政部对评分标准的说明我们没有看到。

申请人能不能看到摘要，是另一个问题。据 ORG 的报告，申请人看不到、也无法更正自己面谈的 AI 摘要。部长 8 月的信提到申请人在面谈后的约定期间可以修改面谈记录，ACS 是在修改期过后让审查人员重新熟悉案件，信里没有提到申请人能否看到或更正摘要。

英国政府有一套让机关公开算法工具的透明度记录（Algorithmic Transparency Records），我们 10 月 29 日查询时共 154 条，内政部的 2 条都不是这两个工具。部长的信写到，两个工具的开发早于这套记录成为强制规定，现在正在补做。ORG 申请公开工具使用的提示词被拒，理由之一是网络安全风险，部长说要在 8 月公布的平等影响评估（评估政策对不同群体影响的文件）到 10 月 12 日也还没有公布。

监督内政部边境与移民业务的独立监察官 6 月公布 2025 年 6 到 12 月的庇护案件检查报告，写到 APS 的成效与可靠性不一。报告也写到有证据显示 AI 工具曾被不当用在决定书与面谈，包括内政部规定不得用于庇护面谈与决定的 Microsoft AI 助手 Copilot，以及 ChatGPT。庇护决定单位的主管表示这些情况已经处理。据 WIRED 的报道，监察官请 ORG 提供更多资料供拟定明年的检查题目，但表示在公布前无法确认会检查哪些题目。

面谈记录送进 Azure 处理，申请人的陈述可能被谁读到，要看服务的条件（本文的推论）。Microsoft 的说明文档写到，客户的提示（送进模型的文字）与输出不提供给 OpenAI、也不用来改进模型。服务仍有检测违规使用的滥用监控，被系统标记的提示与输出可能由经授权的 Microsoft 员工人工审查，经核准修改滥用监控的客户则不做这种存储与人工审查。

文档也把部署分成几种，数据处理的地区各不相同，其中 Global 类型的提示与响应可能在任何部署了该模型的地区处理。到 10 月 29 日为止，内政部采用哪一种部署、有没有修改滥用监控，我们查不到内政部自己的说明。

中国大陆的《政务领域人工智能大模型部署应用指引》由中央网信办与国家发展改革委联合印发，中国网信网 2025 年 10 月 10 日刊登。指引开头写明，本指引为各级政务部门提供工作导向和基本参照。正文要求落实大模型的「辅助型」定位，参考场景包括辅助执法监管与项目的智能辅助评审。应用界面要在显著位置设置风险提示、告知服务的局限性并标识输出内容，提示的对象是使用界面的人，指引没有写到受决定影响的当事人。

面向公众和企业的智能问答、辅助办理等应用要执行内容审核，合理采用人工审核等措施。指引没有写不得以大模型的产出作为决定的唯一依据，我们也没有查到中国大陆针对庇护或移民审查使用生成式 AI 的专门规定。

中国大陆的《个人信息保护法》第三十三条规定，国家机关处理个人信息适用本法。依第二十四条，以自动化决策方式作出对个人权益有重大影响的决定时，个人有权要求说明并拒绝仅以自动化决策方式作出决定。第三十五条的告知义务在告知将妨碍履行法定职责等情形下除外，第三十六条要求国家机关处理的个人信息在境内存储。条文写的是自动化决策、没有提到生成式 AI，本文没有查证国家机关在实践中如何适用这些条文。

在中国境内的读者，遇到对自己权益有重大影响、可能以自动化决策方式作出的决定时，可以依第二十四条要求说明（本文的建议）。在海外跟当地政府机关往来的读者，可以询问承办机关是否使用生成式 AI 处理自己的案件（本文的建议）。以英国为例，部长的信写明不特别告知申请人，询问不保证能得到完整的答案。

台湾的行政院 2023 年订定《行政院及所属机关（构）使用生成式AI参考指引》，适用于行政院及所属机关，性质是参考指引。第五点写到不得以未经确认的产出直接作成行政行为或作为决策的唯一依据，方向跟英国内政部所说的工具不能单独使用相近。第六点要求机关使用生成式 AI 作为辅助工具时适当揭露，但没有写揭露的对象，英国的部长信则写不特别告知申请人。

2026 年 1 月公布的《人工智慧基本法》第 19 条另规定，政府使用人工智能执行业务应进行风险评估。我们没有查到台湾针对移民或庇护程序使用 AI 的专门规定。

在台湾跟行政院所属机关往来的读者，同样可以询问承办机关是否使用生成式 AI 处理自己的案件（本文的建议）。指引第六点没有写向谁揭露、揭露到什么程度，询问不保证能得到完整的答案。除此之外，读者不需要因为这件事调整使用习惯。

比较各地政府用 AI 处理个人案件的做法，可以看当事人会不会被告知、能不能看到并更正 AI 的产出，以及抽查的比例与标准有没有公开、遗漏事实算不算错误。政策想达成的效果也要一起看，省下的时间能不能抵过错误的代价，评估由谁来做、结果有没有公布。
