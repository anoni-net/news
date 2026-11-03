---
title: Free CISA tools for checking Microsoft 365 and Google Workspace settings
description: On 22 October the US Cybersecurity and Infrastructure Security Agency (CISA) released ScubaGear v2.0.0 and ScubaGoggles v1.1.0, free tools that compare an organisation's Microsoft 365 and Google Workspace settings against CISA's security baselines and produce a report. They are meant for an organisation's administrators. ScubaGear runs only on Windows, and ScubaGoggles needs a super admin account.
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
    publisher: Cyber Security Agency of Singapore
    date: 2023-10-17
  - title: Cloud Security for Organisations
    url: https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cloud-security-for-organisations/
    publisher: Cyber Security Agency of Singapore
  - title: Allen & Gledhill on Singapore's planned Cybersecurity Code of Practice for Cloud Services
    url: https://www.allenandgledhill.com/sg/publication/articles/33410/
    publisher: Allen & Gledhill
  - title: Information and Cyber Security Within the Government
    url: https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/information_cyber_security/government/
    publisher: Digital Policy Office, Hong Kong
  - title: 云计算服务安全评估办法
    url: https://www.cac.gov.cn/2019-07/22/c_1124781475.htm
    publisher: Cyberspace Administration of China
    date: 2019-07-22
authors:
  - anoni-net
---

On 22 October the US Cybersecurity and Infrastructure Security Agency (CISA) published ScubaGear v2.0.0 and ScubaGoggles v1.1.0 on GitHub. Both are free assessment tools that check an organisation's Microsoft 365 or Google Workspace settings, item by item, against CISA's secure configuration baselines and then produce a report. They are for the administrators who manage an organisation's tenant (the full set of accounts and settings an organisation has inside a cloud service), so personal accounts without an organisational admin console are out of scope. US federal civilian agencies are separately required to deploy tools of this kind, and organisations elsewhere can choose to use them.

Under CISA's Binding Operational Directive BOD 25-01, federal civilian agencies must deploy the SCuBA assessment tools for every cloud service that has a finalised CISA baseline. When the directive was issued only Microsoft 365 had a finalised baseline, and the directive's page does not mention Google Workspace.

iThome reported on the two releases on 29 October. According to CISA's project page, the SCuBA (Secure Cloud Business Applications) project began in 2022 and the two tools came out in 2023. Except where noted otherwise, both repositories are released under CC0 (a waiver of copyright that lets anyone use the work freely), and the baseline documents sit in the same place.

According to ScubaGear's README, the tool uses PowerShell to query Microsoft 365 APIs for settings and hands them to OPA (Open Policy Agent, a policy engine that checks data against rule files). The rules it checks against are written from the baseline documents, and the results come out as HTML, JSON and CSV. The baselines cover Entra ID, Exchange Online, Teams, SharePoint and OneDrive, Power BI, Power Platform, and Security Suite for advanced threat protection. According to ScubaGear's notes on reports, the report is saved to a folder on the computer that ran it, and one file, `ActionPlan.csv`, lists only the mandatory items that failed and has fields for a reason and a remediation timeline.

ScubaGoggles works in a similar way, exporting settings and admin logs mainly through the Google Admin SDK and producing HTML and JSON reports. Its baselines cover Gmail, Drive and Docs, Meet, Calendar, Chat, Classroom, Sites, Groups and Gemini, among other services. ScubaGear's README says its controls have been mapped to NIST SP 800-53 (the catalogue of security controls for US federal information systems) and MITRE ATT&CK (a knowledge base that classifies attack techniques), and the ScubaGoggles README also lists mappings.

According to the release notes, ScubaGear 2.0.0 adds checks for Power BI, a policy that blocks high-risk Entra AI agents, and a feature for comparing the results of two runs. ScubaGoggles 1.1.0 adds a Meet policy and a first version of the comparison feature, and moves the Gemini baseline from Alpha to Beta. This ScubaGoggles release adds, removes or changes none of the configurations required under BOD 25-01.

## Perspective {#perspective}

The settings for a cloud office suite are spread across several admin consoles, and the two tools read them out and check them in one place against a published set of rules. According to ScubaGear's network access notes, the tool connects to Microsoft's services over HTTPS to read tenant settings and writes the report locally. In the READMEs and the handful of documentation pages we read, we found no mechanism for uploading results to CISA automatically, though we did not review the code. According to the BOD 25-01 page, agencies can feed the tools' results into CISA's continuous monitoring programme for automatic reporting, or submit results from the latest version of the assessment tool each quarter in a machine-readable format CISA has approved.

According to ScubaGear's permissions notes, an interactive login needs at least the Global Reader role for most products. The exceptions are Power BI, newly checked in 2.0.0, which needs a Fabric administrator or Global Administrator, and Power Platform, which needs a Power Platform administrator. The Microsoft Graph permissions the tool requests are all read permissions. ScubaGoggles' prerequisites, by contrast, require the person running it to be a super admin, and most of the scopes on the consent screen carry `readonly`, with only `apps.licensing` and `apps.groups.settings` lacking it.

The same prerequisites explain that the Groups Settings API offers no read-only scope of its own, so the tool narrows its access with the Groups Reader role and Delegated Admin Service Account (DASA) authorisation. Both tools are documented only as assessment tools, but ScubaGoggles still runs under a super admin login, and ScubaGear needs admin roles to check Power BI and Power Platform. Our inference is that the computer running the tools, and any login credentials stored on it, deserve the same protection as the admin consoles themselves.

According to ScubaGoggles' limitations page, some checks infer a setting from admin log events, so a setting that has never been changed from its default cannot be determined. Admin logs are kept for only six months, and the page advises treating such results with scepticism because results may be missing and false negatives are possible. ScubaGear's README warns that without a properly set up YAML configuration file, the tool assumes defaults that may not match the organisation's actual policies. The configuration file can also record risks the organisation accepts, as exclusions or annotations.

ScubaGear's assumptions page says it was tested against tenants with E3 or G3 and E5 or G5 licence bundles, and some checks depend on Entra ID P2 or Defender for Office 365. Our inference is that a small organisation on a lower-tier plan that sees failed items should first work out whether the cause is a setting or a feature its plan never included.

As of 2 November we had found no official counterpart in Singapore, Hong Kong or mainland China, meaning a published configuration baseline for Microsoft 365 or Google Workspace tenants paired with a tool that checks it automatically, though not finding one does not mean none exists. In October 2023 Singapore's Cyber Security Agency (CSA) launched Cloud Security Companion Guides with the Cloud Security Alliance, mapped to its Cyber Essentials mark for smaller organisations subscribing to SaaS and its Cyber Trust mark for larger or more digitalised ones, and CSA's cloud security page lists companion guides for Cyber Essentials written jointly with Microsoft and with Google for Google Workspace in 2022. The press release does not mention an automated assessment tool, and the page does not mention a configuration checklist.

According to an article by the law firm Allen & Gledhill, CSA announced in July 2026 a Cybersecurity Code of Practice for Cloud Services covering critical information infrastructure (CII) hosted on the cloud, to be published in the second half of 2026 alongside provider-specific guides on configuration. We could not find CSA's own announcement, and as of 2 November we had not found the code published. Hong Kong's Digital Policy Office lists a Practice Guide for Cloud Computing Security (ISPG-SM04) as guidance for the secure adoption of cloud computing in government, a management guide for departments, and we found no matching tool for checking either suite. In mainland China, the Measures for Security Assessment of Cloud Computing Services, issued by the Cyberspace Administration of China (CAC) and three other departments and in force since 1 September 2019, assess the cloud providers that serve Party and government bodies and critical information infrastructure operators, not the settings inside a customer's tenant, and an assessment result is valid for three years.

Anyone managing an organisation's Microsoft 365 will first need a Windows computer, because ScubaGear depends on PowerShell 5, which exists only on Windows, and after installation it still has to download OPA and other components. Anyone managing Google Workspace who runs ScubaGoggles needs a 64-bit system, Python 3.11 or later, and four APIs, including the Admin SDK, enabled in a Google Cloud project. The installation and login steps are in each repository's documentation.

ScubaGear's README says the first run without a configuration file only produces a report of the current state and changes no settings, and the README describes no feature for changing settings automatically. Whether to change anything, and which items to fix first, is for administrators to decide in light of their organisation's circumstances. Our inference is that the report covers only the settings listed in the baselines, and whether an account has already been compromised or files have already leaked is outside what it checks.
