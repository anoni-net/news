---
title: 澳大利亚 Medicare 统计网站的 AI 智能体入侵事件
description: OpenAI 的 AI 智能体在 6 月的内部评估中绕过访问限制，进入澳大利亚 Medicare 统计网站并写入文件。澳大利亚政府 9 月才从公共邮箱收到通知，从事件发生到通报相隔近三个月。澳大利亚政府目前研判没有个人信息泄露。
date: 2026-10-02T07:05:00+08:00
slug: openai-agent-medicare-portal
sources:
  - title: Australia launches urgent review after OpenAI program hacks government health portal
    url: https://www.bbc.com/news/live/cvgl73pxgndwt
    publisher: BBC News
    date: 2026-09-24
  - title: "OpenAI ‘climbed the fence’: Taskforce scrambles after long delays flagging Medicare hack"
    url: https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html
    publisher: The Sydney Morning Herald
    date: 2026-09-24
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
  - title: 通过多份个人资料使用 Chrome
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hans
    publisher: Google Chrome 帮助
authors:
  - anoni-net
---

澳大利亚总理于 9 月 24 日在纽约公布，OpenAI 的一个 AI 智能体未经授权进入 Services Australia 管理的 Medicare 统计报表网站（Medicare Statistics Reporting Service），访问了公开与非公开的文件，还在内部服务器上写入文件。澳大利亚信号局（ASD）正协助取证调查，范围包括其他政府系统是否也受到影响。

Medicare 统计报表网站提供医疗支出之类的非敏感统计数据。据澳大利亚政府 9 月 24 日的说明，研判没有个人信息泄露，调查仍在进行，网站也已停用。智能体当时在执行 OpenAI 内部的能力评估，任务是上网研究公共药品支出，获取数据的请求被拒绝之后，改用其他方式绕过限制。

事件发生在 6 月 18 日，OpenAI 在 8 月的一次全面审查中察觉，9 月 10 日发信到 Services Australia 的公共邮箱。该邮箱每天查看一次，Services Australia 在 11 日看到邮件，15 日才通报澳大利亚网络安全中心。

澳大利亚总理在记者会上表示，OpenAI 通知得太慢，通知方式也无法接受。政府已成立专责小组审视网络防护与罚则，也可能把案件移交联邦警察。

OpenAI 发言人表示，模型在内部评估中访问了“数个澳大利亚政府的网站与服务”，并“采取了我们没有预期的行动”。OpenAI 的事件说明页写到，已通知数十个受影响的第三方，并公开匿名的行为分类，包括绕过访问控制、使用外泄的登录凭据、注入查询或命令、读取服务的内部文件。

## 导读观点 {#perspective}

OpenAI 列出的绕过手法，例如换一个网址、修改请求内容、沿用权限过大的登录会话，都是网站常见的访问控制弱点，换成人工操作同样可行。据《悉尼先驱晨报》报道，出事的网站是一个主要供学者使用的旧网站。维护网站的机构可以先盘点仍在线、但已少有人管理的旧系统，用不到的下线，还要用的确认非公开文件需要登录才能获取。

中国大陆的《国家网络安全事件报告管理办法》要求网络运营者发现较大以上的网络安全事件后报告，关键信息基础设施最迟 1 小时，其他运营者最迟 4 小时。办法也鼓励社会组织和个人报告，网信部门设有 12387 热线统一接收。澳大利亚这次的延误主要发生在机关知悉之前。

普通用户让 AI 智能体代为浏览网页、填写表单时，智能体能触及的范围，就是它手上的登录状态与权限。新加坡资讯通信媒体发展局（IMDA）1 月发布的智能体 AI 治理框架里的建议，是在设计阶段限制智能体的自主程度、可用工具与数据访问。个人使用时可以参照，在电脑版 Chrome 右上角的个人资料图标选择「添加 Chrome 个人资料」，让智能体在独立的个人资料中运行，只登录任务需要的账号。
