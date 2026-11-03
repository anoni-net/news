---
title: 检查 Microsoft 365 与 Google Workspace 设置的 CISA 免费工具
description: 美国 CISA 10 月 22 日发布 ScubaGear v2.0.0 与 ScubaGoggles v1.1.0，免费比对组织的 Microsoft 365 与 Google Workspace 设置跟 CISA 的安全基线，生成报告。用得到的是组织的管理员，ScubaGear 只能在 Windows 运行，ScubaGoggles 要用超级管理员账号。
date: 2026-11-06T00:00:00+08:00
slug: cisa-scuba-config-tools
categories:
  - security
regions:
  - US
sources:
  - title: Release v2.0.0 · cisagov/ScubaGear
    url: https://github.com/cisagov/ScubaGear/releases/tag/v2.0.0
    publisher: GitHub
    date: 2026-10-22
  - title: Release v1.1.0 · cisagov/ScubaGoggles
    url: https://github.com/cisagov/ScubaGoggles/releases/tag/v1.1.0
    publisher: GitHub
    date: 2026-10-22
  - title: Secure Cloud Business Applications (SCuBA) Project
    url: https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project
    publisher: CISA
  - title: "BOD 25-01: Implementing Secure Practices for Cloud Services"
    url: https://www.cisa.gov/news-events/directives/bod-25-01-implementing-secure-practices-cloud-services
    publisher: CISA
    date: 2024-12-17
  - title: ScubaGear/README.md
    url: https://github.com/cisagov/ScubaGear/blob/main/README.md
    publisher: GitHub
  - title: ScubaGoggles/README.md
    url: https://github.com/cisagov/ScubaGoggles/blob/main/README.md
    publisher: GitHub
  - title: Interactive Permissions
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/prerequisites/interactive.md
    publisher: GitHub
  - title: Dependencies
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/prerequisites/dependencies.md
    publisher: GitHub
  - title: Network Access
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/prerequisites/networkaccess.md
    publisher: GitHub
  - title: Assumptions
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/misc/assumptions.md
    publisher: GitHub
  - title: Reports
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/execution/reports.md
    publisher: GitHub
  - title: Prerequisites
    url: https://github.com/cisagov/ScubaGoggles/blob/main/docs/prerequisites/Prerequisites.md
    publisher: GitHub
  - title: Limitations
    url: https://github.com/cisagov/ScubaGoggles/blob/main/docs/usage/Limitations.md
    publisher: GitHub
  - title: Getting started
    url: https://github.com/cisagov/ScubaGoggles/blob/main/docs/installation/DownloadAndInstall.md
    publisher: GitHub
  - title: CISA提供兩款免費工具，協助檢測M365與Google Workspace的安全設定錯誤
    url: https://www.ithome.com.tw/news/180058
    publisher: iThome
    date: 2026-10-29
  - title: Launch of Cloud Security Companion Guides for Organisations
    url: https://www.csa.gov.sg/news-events/press-releases/launch-of-cloud-security-companion-guides-for-organisations/
    publisher: CSA
    date: 2023-10-17
  - title: Cloud Security for Organisations
    url: https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cloud-security-for-organisations/
    publisher: CSA
  - title: Information and Cyber Security Within the Government
    url: https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/information_cyber_security/government/
    publisher: Digital Policy Office
  - title: 云计算服务安全评估办法
    url: https://www.cac.gov.cn/2019-07/22/c_1124781475.htm
    publisher: 国家互联网信息办公室
    date: 2019-07-22
authors:
  - anoni-net
---

美国网络安全暨基础设施安全局（CISA）10 月 22 日在 GitHub 发布 ScubaGear v2.0.0 与 ScubaGoggles v1.1.0。两款都是免费的评估工具，把组织的 Microsoft 365 或 Google Workspace 设置跟 CISA 的安全设置基线逐条比对，再生成报告。用得到的是管理组织租户（tenant，组织在云服务里的整套账号与设置）的管理员，没有组织管理后台的个人账号不在范围内。美国联邦民事机关另有部署这类工具的义务，其他地方的组织可以自行选用。

依 CISA 的约束性指令 BOD 25-01，联邦民事机关须替已有 CISA 定稿基线的云服务部署 SCuBA 的评估工具。指令发布时只有 Microsoft 365 有定稿基线，页面没有提到 Google Workspace。

iThome 10 月 29 日报道了这两次更新。依 CISA 的项目页，SCuBA（安全云商务应用）项目 2022 年成立，2023 年推出这两款工具。两个 repo 除另有注明的部分外，以 CC0（放弃著作权、任何人都能自由使用的许可）公开，基线文档也放在同一处。

依 ScubaGear 的 README，工具用 PowerShell 向 Microsoft 365 的 API 查询设置，再交给 OPA（Open Policy Agent，依规则文件比对数据的策略引擎）比对。比对用的规则照基线文档写成，结果输出成 HTML、JSON 与 CSV。基线涵盖 Entra ID、Exchange Online、Teams、SharePoint 与 OneDrive、Power BI、Power Platform，以及高级威胁防护的 Security Suite。依 ScubaGear 的报告说明，报告存在运行那台电脑的文件夹里，其中只列未通过强制项目的 `ActionPlan.csv` 可以填写原因与改善时程。

ScubaGoggles 的做法相近，主要通过 Google Admin SDK 导出设置与管理日志，再输出 HTML 与 JSON 的报告。基线涵盖 Gmail、云端硬盘与文档、Meet、日历、Chat、Classroom、协作平台、群组与 Gemini 等服务。ScubaGear 的 README 写到控制项已对应 NIST SP 800-53（美国联邦信息系统的安全控制目录）与 MITRE ATT&CK（攻击手法的分类知识库），ScubaGoggles 的 README 也列有对照表。

依版本说明，ScubaGear 2.0.0 新增 Power BI 的检查、一条封锁高风险 Entra AI 代理程序的策略，以及比较两次运行结果的功能。ScubaGoggles 1.1.0 新增一条 Meet 的策略与比较功能的初版，Gemini 的基线从 Alpha 改为 Beta。BOD 25-01 要求的设置在 ScubaGoggles 这一版没有新增、移除或修改。

## 导读观点 {#perspective}

云办公服务的设置分散在好几个管理后台，两款工具把它们读出来，集中跟一份公开的规则对照。依 ScubaGear 的网络需求说明，工具通过 HTTPS 连到 Microsoft 的服务读取租户设置，报告写在本机。本文查过的 README 与几份说明文档里，没有写到把结果自动上传给 CISA 的机制，代码则没有检查。依 BOD 25-01 的页面，机关可以自行把工具的结果接到 CISA 的持续监控方案自动回报，或每季以 CISA 核可的机器可读格式提交用最新版评估工具生成的结果。

依 ScubaGear 的权限说明，以交互方式登录时，多数产品最低要全局读取者（Global Reader）角色。角色门槛的例外是 2.0.0 新增检查的 Power BI 要 Fabric 管理员或全局管理员，Power Platform 则要 Power Platform 管理员。工具向 Microsoft Graph 申请的权限都是读取类。ScubaGoggles 的前置说明则要求运行者是超级管理员，同意画面上的范围多数带 `readonly`，只有 `apps.licensing` 与 `apps.groups.settings` 两项没有。

同一份说明提到 Groups Settings API 本身不提供只读范围，所以改用群组读取者（Groups Reader）角色搭配委派管理服务账户（DASA）限缩权限。两款工具的说明都只写评估，但 ScubaGoggles 运行时登录的仍是超级管理员，ScubaGear 检查 Power BI 与 Power Platform 时也要用管理员角色。依本文的推论，运行工具的电脑与保存的登录凭据，安全程度要比照管理后台。

依 ScubaGoggles 的限制说明，部分检查要从管理日志推断设置，从未改过默认值的设置因此无从判断。管理日志也只保留 6 个月，文档提醒这类结果可能漏报，要保留怀疑。ScubaGear 的 README 则提醒，没有设好 YAML 配置文件时，工具采用的默认值未必符合组织实际的策略。配置文件也可以把组织接受的风险记成排除或注记。

ScubaGear 的假设说明列出，测试用的租户是 E3、G3 或 E5、G5 的许可证组合，部分检查依赖 Entra ID P2 或 Defender for Office 365。依本文的推论，用较低阶方案的小型组织看到未通过的项目时，要先分辨原因出在设置或方案本来就没有那项功能。

管理组织 Microsoft 365 的人要先准备一台 Windows 电脑，ScubaGear 依赖只有 Windows 版的 PowerShell 5，安装之后还要下载 OPA 等组件。管理 Google Workspace 的人运行 ScubaGoggles，需要 64 位系统与 Python 3.11 以上，并在 Google Cloud 项目启用 Admin SDK 等四个 API。安装与登录的步骤见两个 repo 的说明文档。

截至 11 月 2 日，新加坡、香港与中国大陆的官方文件里，本文没有查到同时提供 Microsoft 365 或 Google Workspace 租户设置基线与自动检查工具的项目（检索结果的归纳，查不到不等于不存在，两项服务在各地的供应状况也没有查）。新加坡网络安全局（CSA）2023 年 10 月 17 日与 Cloud Security Alliance 合作发布云安全配套指南，对应 Cyber Essentials（面向订阅 SaaS 的中小企业）与 Cyber Trust（面向较大或数字化程度较高的组织）两套认证，新闻稿没有提到自动化评估工具。CSA 的页面另列 2022 年与 Microsoft、Google 合作的 Cyber Essentials 配套指南，页面没有提到设置检查清单。香港数字政策办公室列有供政府部门采用云计算的 Practice Guide for Cloud Computing Security（ISPG-SM04），同样没有查到对应工具。

中国大陆有 2019 年 9 月 1 日施行的《云计算服务安全评估办法》（国家网信办等四部门发布），对象是党政机关与关键信息基础设施运营者采购的云计算服务。评估的是云服务商的资信、人员背景、供应链、安全管理与数据迁移等，结果有效期 3 年，不检查客户自己租户的设置。

ScubaGear 的 README 提到，不带配置文件的第一次运行只会生成现状的报告、不会修改设置，README 也没有描述自动修改设置的功能。要不要改、先改哪几项，由管理员依组织的处境判断。依本文的推论，报告只涵盖基线列出的设置，账号是否已被入侵、文件是否已经外泄都不在比对的范围内。
