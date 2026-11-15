---
title: NIST 写给一人事业的网络安全指南 CSWP 50
description: NIST 11 月 2 日发布 CSWP 50，写给没有雇员的一人事业，用不预设网络安全知识的写法整理多因素验证、备份、更新与钓鱼识别等行动。指南免费下载，到 11 月 15 日只查到英文版。内容以美国读者为对象，其他地方的接案者与个人工作者可以参考其中的做法。
date: 2026-11-22T00:00:00+08:00
slug: nist-solopreneur-guide
categories: [civil-society]
regions: [US]
sources:
  - title: "Self-Employed? Solopreneur? NIST Has a Cybersecurity Guide Just for You"
    url: https://www.nist.gov/news-events/news/2026/11/self-employed-solopreneur-nist-has-cybersecurity-guide-just-you
    publisher: NIST
    date: 2026-11-02
  - title: "CSWP 50, Small Business Cybersecurity: Non-Employer Firms"
    url: https://csrc.nist.gov/pubs/cswp/50/small-business-cybersecurity-non-employer-firms/final
    publisher: NIST
    date: 2026-11-02
  - title: 中小企業基本資安防護指引
    url: https://www-api.moda.gov.tw/File/Get/acs/zh-tw/1rpP5Mb1iyZwZUF
    publisher: 数字发展部资通安全署
  - title: Seven Habits of Cyber Security for SMEs
    url: https://www.hkcert.org/security-guideline/seven-habits-of-cyber-security-for-smes
    publisher: HKCERT
    date: 2018-09-11
  - title: Incident Response Guideline for SMEs
    url: https://www.hkcert.org/security-guideline/incident-response-guideline-for-smes
    publisher: HKCERT
    date: 2022-07-29
  - title: Toolkits for enterprise leaders and SME owners
    url: https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cybersecurity-toolkits/enterprise-leaders-and-sme-owners
    publisher: Cyber Security Agency of Singapore
authors:
  - anoni-net
---

美国国家标准暨技术研究院（NIST）11 月 2 日发布 CSWP 50《Small Business Cybersecurity: Non-Employer Firms》，写给没有雇员、业主就是唯一有薪工作者的一人事业。依新闻稿，指南用普通人读得懂的语言写成，不预设读者具备网络安全知识。指南已经定稿，可以免费下载，到 11 月 15 日只查到英文版。

指南以美国读者为对象，也写到许多小企业有跨国的业务与合作，内容可以调整后用在这些情境。美国以外的接案者与个人工作者可以参考其中的做法。本文的推论是，指南提到的美国法规与辅导方案在其他地方不适用，要换成当地的对应资源。

依新闻稿，美国有超过 2,800 万家小企业属于一人事业。指南的摘要写到，对象是美国小型企业管理局定义的 non-employer firms，也就是业主以外没有员工的事业。员工很少或 IT 设备很少的事业也可能适用。对象一节列出独资业主、自由工作者、单一成员的有限责任公司、独立承包商与零工经济的工作者，也把小企业依赖的顾问列为主要读者之一。

依新闻稿，旧版指南 NISTIR 7621 写给各种规模的小企业，更新后的 CSWP 50 集中在保护数字系统不受恶意攻击。指南以 NIST 网络安全框架 2.0 版（CSF 2.0，NIST 用来整理组织网络安全工作的架构）为基础，内容比 CSF 给小企业的快速入门指南详细许多。新闻稿介绍的中段列出一人事业可以执行的行动，每项写出理由、如何起步，以及事业成长之后的选项。最后是盘点资产的工作表、追踪已完成行动的表格，以及律师、手工艺者与商业顾问三个假设案例，案例放在另外的附录文件。

指南的导论列出九项可以大幅降低风险的行动。第一项是启用防钓鱼的多因素验证（MFA，登录时除了密码还要再提供一种验证），对象是有提供 MFA 的账号，尤其是电子邮件、银行、密码管理器与重要的云服务。密码依 NIST 的建议至少 15 个字符，可以考虑用密码管理器，可行时改用通行密钥（passkey，用设备上的指纹、面部或 PIN 解锁的登录凭证，不必输入账号密码）。

其余几项是学会识别钓鱼与勒索软件、日常工作用标准用户账号、盘点重要的资产与依赖的服务、建立并测试备份，以及让所有设备与 App 保持更新。最后两项是列出事件发生时要通报的内外部联系人，并留一份纸质，以及列出跟网络安全有关的法律、法规与合同要求。指南在勒索软件一节建议隔离保护重要数据的备份，第 3 章的备份项目另外建议考虑至少留一份在外接硬盘或云端这类不连着设备的介质上。

指南建议尽量不要混用个人与业务的资产，让个人设备与业务设备分开。设备必须跟家人共用时，每个人要有自己的账号，家人的账号也不能访问敏感的业务数据。指南还提醒在家、咖啡店与共享办公空间各有不同的实体威胁，设备要开启定位追踪与远程清除。

遇到更改汇款账号、修改发票、紧急付款或购买礼品卡这类要求时，指南建议用已知或公开的联系方式确认，不通过收到的消息本身回复。指南的钓鱼一节也提到，AI 产品与服务现在可以用来制作更有说服力的钓鱼消息，指南把它们称为「Super Intelligence」（SI）。

依指南的脚注，SI 是 9 月 29 日美国行政命令要求的改称，命令要求行政机关把用语从「artificial intelligence」改成「super intelligence」。指南也为 AI 工具另立一节，建议盘点正在使用的 AI 工具与软件内置的 AI 功能。输入敏感信息前先看过数据保留、是否用于训练与访问权限的设置，AI 生成的内容在使用前也要先审阅。

## 导读观点 {#perspective}

指南的 MFA 说明写到，在所有提供 MFA 的账号上启用，是保护事业最重要的步骤之一。说明也提到有些 MFA 的形式容易被钓鱼，防钓鱼的例子是通行密钥。依一般的钓鱼手法，短信或验证 App 的一次性密码可能被假网站骗走后转发出去。通行密钥跟注册时的网站绑在一起，假网站难以获得可用的凭证。

新闻稿引述作者之一的说法，许多行动只需有限的技术知识或很少的花费就能自行完成。指南只零星提到密码管理器是相对便宜的做法，没有逐项估算费用。自行处理之外也可以交给顾问或外包厂商，指南提醒外包之后，保护系统与数据的责任不会跟着转移出去。

需要中文资料的读者可以参考台湾数字发展部资通安全署的《中小企業基本資安防護指引》，封面日期是 2026 年 3 月，PDF 共 11 页。内容从账号管理、设备和数据管理、网络安全意识培育三个方面着手，附一份自检表。对象是中小企业，没有针对一人事业另外写。本文对照两份文件，自检表的密码至少 15 位、更改联网设备的默认密码、备份、自动更新与资产清单，都跟 NIST 指南的建议重叠。

在海外的读者也可以参考 HKCERT 与香港生产力促进局 2018 年 9 月 11 日发布的《Seven Habits of Cyber Security for SMEs》，涵盖安全政策与管理、终端、网络、系统、监控、事件处理与用户意识七个方面，附自我评估检查表。HKCERT 另有 2022 年 7 月 29 日发布、面向中小企业与非技术读者的《Incident Response Guideline for SMEs》，含情景题与应急响应程序模板。新加坡网络安全局（CSA）的中小企业工具包页面以可能没有专职 IT 人员的中小企业为对象，列出五个主题，页面只有英文 PDF。本文到 11 月 15 日的检索，没有找到中国大陆针对小微企业或个人工作者的专门官方指引。

没有雇员、自己处理所有账号与设备的人，可以先用导论的九项行动逐一对照自己的状况。指南可以从 NIST 官网免费下载，是 33 页的英文 PDF，盘点用的工作表与三个案例另外放在 .xlsx 文件。新闻稿也引述作者的说法，指南没有涵盖每位一人事业的所有需求。依指南第 3 章的说明，表格列出的行动不是检查清单或合规标准，隐私的保护也大多不在范围内（只列了几个基本步骤）。
