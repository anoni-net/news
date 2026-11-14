---
title: The netiCRM provider's server breach and a client's copied donation database
description: NETivism, the Taiwanese provider of netiCRM, a donation and membership management system for non-profits, had an internal management server broken into on 9 November. The provider confirmed that data such as client organisations' contact names and email addresses was stolen. According to an iThome update on 13 November, one client organisation was also notified that its donation database had been copied. For other clients' donor data, iThome wrote that the investigation was still ongoing (as of 14 November). People who donated, joined or registered for events through an organisation using netiCRM can watch for notices from that organisation and for impersonation scams.
date: 2026-11-19T00:05:00+08:00
slug: neticrm-breach
categories:
  - civil-society
regions:
  - TW
sources:
  - title: netiCRM服務商內部管理主機遭駭，暫未發現捐款人資料外洩，已將500家客戶主機納入檢查及重建範圍
    url: https://www.ithome.com.tw/news/180438
    publisher: iThome
    date: 2026-11-12
  - title: netiCRM服務商遭駭，超過30個非營利組織接連示警（標題略去組織名稱）
    url: https://www.ithome.com.tw/news/180384
    publisher: iThome
    date: 2026-11-10
  - title: netiCRM
    url: https://github.com/NETivism/netiCRM
    publisher: GitHub
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021
    publisher: 全國法規資料庫
  - title: 個人資料保護法修法問答集
    url: https://ws.pdpc.gov.tw/FS01/FilePath/3/relfile/30/1072/a842b3f2-3399-4742-96ae-3f6648bd071a.pdf
    publisher: 個人資料保護委員會籌備處
    date: 2025-12-26
  - title: Data Breach Notification
    url: https://www.pcpd.org.hk/english/enforcement/data_breach_notification/dbn.html
    publisher: PCPD
  - title: Guidance on Data Breach Handling and Data Breach Notifications
    url: https://www.pcpd.org.hk/english/resources_centre/publications/files/guidance_note_dbn_e.pdf
    publisher: PCPD
    date: 2023-06-30
  - title: Prevention of personal data breaches and financial crimes
    url: https://www.info.gov.hk/gia/general/202501/22/P2025012200305.htm
    publisher: Hong Kong Government
    date: 2025-01-22
  - title: 有關維護資訊保安的工作
    url: https://www.legco.gov.hk/yr2026/chinese/panels/itb/papers/itb20260713cb2-1000-3-c.pdf
    publisher: 香港立法會
    date: 2026-07-13
  - title: Personal Data Protection Act 2012, Part 6A
    url: https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-
    publisher: Singapore Statutes Online
  - title: Personal Data Protection (Notification of Data Breaches) Regulations 2021
    url: https://sso.agc.gov.sg/SL/PDPA2012-S64-2021
    publisher: Singapore Statutes Online
  - title: Advisory Guidelines on Key Concepts in the Personal Data Protection Act
    url: https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/ag-on-key-concepts/advisory-guidelines-on-key-concepts-in-the-pdpa-17-may-2022.pdf
    publisher: PDPC
    date: 2026-04-29
authors:
  - anoni-net
---

An attacker broke into the internal management server of NETivism, the Taiwanese company behind netiCRM, a donation and membership management system for non-profit organisations, in the early hours of 9 November. According to an iThome update on 13 November, one client organisation announced on 12 November that the provider had notified it that its donation database had been copied. The organisation's notice lists donors' names, email addresses, phone numbers, postal addresses and donation records as possibly exposed. As for whether other client organisations and the people who donate to them are affected, iThome wrote that donor data was still under investigation (as of 14 November).

iThome's report of 12 November ran under a headline saying no leak of donor data had been found so far, based on the provider's statement of 11 November. As iThome relayed it, the provider had by then confirmed the theft of client data it held itself, including organisation contacts' names and email addresses, service plans, billing data and customer support records. For donor and supporter data on the non-profits' websites, the investigation had not yet found signs of theft, and the report did not say which records the investigation examined. The news that a donation database had been copied appears further down the same page, relayed through two layers, the client organisation's notice and iThome.

The account of the intrusion comes from the provider's statement in iThome's report of 10 November. The attacker obtained a username and password for the provider's internal code management system, then exploited a system vulnerability to gain administrator access to a server, breaking in at 01:55 on 9 November (Taipei time). The provider cut off all of the attacker's connections to that server at about 03:30 and sent clients a security incident notice the same day. According to the client notice that iThome quoted on 12 November, the provider reported the incident to the Ministry of Digital Affairs on the afternoon of 10 November and filed a report with the Taipei City Police Department.

In its statement of 10 November, the provider treated the admin accounts of client websites and the email account settings used for sending mail as possibly exposed, and said admin passwords were stored hashed (a one-way transformation that cannot be turned back into the password directly). According to what a client organisation relayed on the evening of 10 November, the breached machine was the provider's internal technical management server, not the server holding donation records. By 11 November, the provider's statement was that this server had administrative access to other servers, so every client server was being checked and rebuilt. Client websites and the netiCRM service might be temporarily unavailable during the rebuild.

According to the provider's statement of 11 November as relayed by iThome, its clients are more than 500 non-profit organisations. The provider had isolated the affected systems, identified the point of entry and replaced all leaked keys, and had also scanned and updated every client's mail server. Rebuilding the official website `neticrm.tw`, an investigation with outside experts and monitoring each server for anomalies were still under way at the time of the report, and the provider said the outside security firm it contacted had no staff available to help for now. When we, a community based in Taiwan, fetched `neticrm.tw` with a script on 14 November, we received only a verification page, so every statement from the provider in this article is relayed through iThome or client organisations.

## Perspective {#perspective}

According to its official GitHub page, netiCRM is a fork of CiviCRM (a relationship management system for non-profits developed since 2005), and its source code is public. The provider has offered it since 2011 as SaaS (software as a service, where the provider hosts and runs the servers and the system). Organisations do not have to run their own servers, and in turn the security of donor data depends on how well the provider protects its internal accounts and management servers (our inference).

According to the provider's statement of 11 November as relayed by iThome, the breached management server held the management system's code, parameters and data. The attacker could use the stolen code and data to go on to attack client websites and vulnerable servers, and at the time the provider was working on fixing the stolen code. Changing passwords and keys only blocks connections that use the old credentials; once the management system's code is out, flaws in the code itself also need patching (our inference).

According to iThome, the client organisation whose donation database was copied urged supporters to stay alert to phishing emails, unknown callers and impersonation scams. The claim that credit card data was unaffected comes only from that organisation's notice. iThome reported on 10 November that more than 30 organisations had issued warnings, telling donors to watch for suspicious calls and scam messages. To find out whether an organisation you donated to, joined or registered for an event with has been affected, check that organisation's own notices.

The fields that organisation listed as possibly exposed include phone numbers, addresses and donation records, so an impersonator might be able to tell a donor which organisation they gave to and how much (our inference). If a call or email from someone claiming to be from the organisation asks you to transfer money, give a credit card number or change a direct debit, you can hold off and call back on the number listed on the organisation's official website. Calling back is our suggestion, not something the sources say. It stops impersonated requests, but it cannot stop data that may already have leaked from being reused.

The provider gave organisations using netiCRM advice on two occasions. In iThome's report of 10 November, it advised changing the passwords of every admin account as soon as possible, reminding donors to watch for scam calls and messages, and notifying internal stakeholders. On 11 November it advised first telling donors and members on the official website or social media that online donations and event registration might be temporarily unavailable, and posting an anti-scam reminder at the same time. The provider also said some of the attack sources pointed to IP addresses at client offices and that it had notified those clients, without giving details.

According to the provider, whether to report to the regulator is up to each organisation, based on the applicable laws, its internal rules and its arrangements with the regulator. Those who are unsure can ask the regulator or a legal adviser.

Article 12 of Taiwan's current Personal Data Protection Act requires a government or non-government agency that violates the Act, resulting in personal data being stolen or leaked, to notify the people concerned by appropriate means after the facts are established. The article contains no duty to report to a regulator and no deadline. Amendments promulgated in November 2025 add a duty to report to the regulator when an incident falls within a defined reporting scope, with the effective date to be set by the Executive Yuan (Taiwan's cabinet), and as of 14 November the Laws & Regulations Database still listed that date as undetermined. A Q&A from Taiwan's Personal Data Protection Commission Preparatory Office says the current Act continues to apply until the amendments take effect.

As of 9 October 2026, if a similar incident happened in Hong Kong, the organisation holding the data would have no statutory duty to report it to the Office of the Privacy Commissioner for Personal Data (PCPD), which treats notification as recommended practice. The PCPD's June 2023 guidance advises notifying the office and the affected people as soon as practicable, particularly where the breach is likely to cause a real risk of harm. Amendment proposals that would make breach notification mandatory and regulate data processors directly were still under government study at that date, with no bill published.

As of 9 October 2026, if a similar incident happened in Singapore, the Personal Data Protection Act 2012 would make a breach notifiable if it results or is likely to result in significant harm to an affected person, or affects or is likely to affect 500 or more people. A data intermediary, which processes personal data on behalf of another organisation, must notify that organisation without undue delay. That organisation then assesses whether the breach is notifiable, which Singapore's Personal Data Protection Commission (PDPC) generally expects within 30 calendar days, and if it is, must notify the PDPC within three calendar days of the assessment. Affected people must be notified only where significant harm is likely.

People who have not donated, joined or registered for events through an organisation using netiCRM do not need to do anything. For organisations that use netiCRM, the provider has confirmed that contacts' names and email addresses were stolen, so staff may also receive impersonation emails (our inference). As of 14 November, iThome had reported only one client organisation being notified that its donation database had been copied, and did not say whether other clients were in the same situation. Next to watch are the provider's full investigation findings and the outside experts' investigation, and whether other client organisations receive the same notice.
