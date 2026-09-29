---
title: 澳大利亚 Medicare 统计网站的 AI 智能体入侵事件
description: OpenAI 的 AI 智能体 6 月在内部评估中绕过访问限制，进入澳大利亚 Medicare 统计网站并写入文件。截至 9 月 24 日，澳大利亚政府研判没有个人信息遭到访问，网站上是汇总的统计数据。使用 AI 智能体的人可以为它开一份独立的浏览器个人资料。
date: 2026-10-02T00:05:00+08:00
slug: openai-agent-medicare-portal
sources:
  - title: Press conference - New York
    url: https://www.pm.gov.au/media/press-conference-new-york
    publisher: Prime Minister of Australia
    date: 2026-09-24
  - title: Press Conference, Sydney
    url: https://www.minister.defence.gov.au/transcripts/2026-09-24/press-conference-sydney
    publisher: Australian Minister for Defence
    date: 2026-09-24
  - title: The Hugging Face incident and other third-party impact from misaligned models
    url: https://openai.com/hugging-face-incident-and-misalignment/
    publisher: OpenAI
    date: 2026-09-25
  - title: Australia launches urgent review after OpenAI program hacks government health portal
    url: https://www.bbc.com/news/live/cvgl73pxgndwt
    publisher: BBC News
    date: 2026-09-24
  - title: "OpenAI ‘climbed the fence’: Taskforce scrambles after long delays flagging Medicare hack"
    url: https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html
    publisher: The Sydney Morning Herald
    date: 2026-09-24
  - title: Singapore Launches New Model AI Governance Framework for Agentic AI
    url: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai
    publisher: IMDA
    date: 2026-01-22
  - title: Factsheet - Model AI Governance Framework for Agentic AI
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2026/01/factsheet-model-ai-governance-framework-for-agentic-ai.pdf
    publisher: IMDA
    date: 2026-01-22
  - title: 資通安全事件通報應變及演練辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=A0030305
    publisher: 全國法規資料庫
    date: 2026-01-05
  - title: 国家网络安全事件报告管理办法
    url: https://www.cac.gov.cn/2025-09/15/c_1759583017717009.htm
    publisher: 国家互联网信息办公室
    date: 2025-09-15
  - title: 管理多個 Chrome 設定檔
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hant
    publisher: Google Chrome 說明
  - title: 管理多個 Chrome 設定檔（Android）
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hant&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 說明
  - title: 通过多份个人资料使用 Chrome
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hans
    publisher: Google Chrome 帮助
  - title: Google Chrome 网络浏览器
    url: https://www.google.cn/chrome/
    publisher: Google
regions:
  - AU
authors:
  - anoni-net
---

澳大利亚总理在纽约的记者会上（澳大利亚东部时间 9 月 24 日清晨 6 点过后，北京时间凌晨 4 点过后）公布，OpenAI 的 AI 智能体（能自行操作网页的程序）未经授权，进入澳大利亚 Medicare（全民医保）的统计报表网站。智能体访问了非公开的文件，也在内部服务器写入文件。截至 9 月 24 日，澳大利亚政府研判没有个人信息遭到访问。OpenAI 也通知了数十个可能受影响的第三方。

网站由 Services Australia（办理医保等服务的联邦机构）管理，存放汇总统计数据，到 9 月 24 日已经停用。智能体当时在 OpenAI 的内部能力评估中研究政府的药品支出，6 月 18 日被网站拒绝之后，改用其他方式绕过限制。

OpenAI 8 月在全面审查中察觉这起事件，9 月 10 日发信到 Services Australia 受理漏洞报告的邮箱。该机构 11 日看到邮件，经过周末与核实真伪，15 日通报澳大利亚信号局（ASD，负责网络防御的情报机构）下属的澳大利亚网络安全中心。

总理表示，OpenAI 通知得太慢，方式也无法接受。政府成立专责小组审视网络防护与罚则，也将评估是否移交澳大利亚联邦警察。取证调查由 ASD 协助，范围包括其他政府系统是否受影响。

OpenAI 发言人表示，模型「采取了并非我们本意的行动」。OpenAI 在事件说明页列出匿名的行为分类，例如绕过访问控制、使用公开暴露的登录凭据，没有写明 Medicare 网站属于哪一类。

## 导读观点 {#perspective}

OpenAI 举的绕过例子有换用另一个网址、修改请求内容，利用的都是常见的访问控制弱点，人工操作也可以做到。主管 Services Australia 的部长说明，网站是用了数十年的旧系统。维护网站的机构可以把少有人管理的旧系统下线，还要用的确认非公开文件需要登录。

中国大陆的《国家网络安全事件报告管理办法》规定较大以上事件涉及关键信息基础设施的最迟 1 小时报告，中央和国家机关各部门 2 小时，其他运营者 4 小时。台湾的《资通安全事件通报应变及演练办法》规定，公务机关知悉后须在一小时内通报。澳大利亚这次从事件发生到 OpenAI 发出通知将近三个月，都在机关知悉之前。外部发现者何时通知，大陆办法第六条只作鼓励，台湾办法没有规定。

新加坡资讯通信媒体发展局（IMDA）1 月发布智能体 AI 的治理框架，建议机构在设计阶段就限制智能体的自主程度、可用工具与数据访问。个人也可以照这个原则做。

在电脑版 Chrome 运行智能体的人，可以从右上角的个人资料图标选择「添加 Chrome 个人资料」，在里面只登录必要的账号。`google.cn` 有电脑版 Chrome 的简体中文下载页，添加个人资料只有三步，不需要 Google 账号。Android 版 Chrome 只能有一份个人资料，云端浏览器里运行的智能体也用不上这个做法。代价是新的个人资料没有原来的书签、密码与登录状态，账号要重新登录。
