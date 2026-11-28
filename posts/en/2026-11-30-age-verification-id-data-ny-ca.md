---
title: Age assurance rules and data handling for social media platforms in New York and California
short_title: New York and California age assurance rules
description: From January 2027, New York and California require social media platforms to confirm users' ages, and accounts that are unconfirmed, or belong to minors without parental consent, get no algorithmic feeds or late-night notifications. New York's rules limit what data can be collected and kept during age checks, and platforms that accept government ID must also offer a way that does not require it. The rules cover users located in the two states.
meta_description: From January 2027, New York and California require social platforms to confirm adulthood before showing algorithmic feeds or late-night notifications.
date: 2026-11-30T00:05:00+08:00
slug: age-verification-id-data-ny-ca
categories: [censorship]
sources:
  - title: Attorney General James and Governor Hochul Release Final SAFE for Kids Act Rules to Protect Children Online
    url: https://ag.ny.gov/press-release/2026/attorney-general-james-and-governor-hochul-release-final-safe-kids-act-rules
    publisher: New York State Attorney General
    date: 2026-07-28
  - title: SAFE for Kids Act Rule Text
    url: https://ag.ny.gov/sites/default/files/2026-07/safe_for_kids_act_rule_text.pdf
    publisher: New York State Attorney General
    date: 2026-07-28
  - title: Governor Newsom signs the strongest child safety chatbot and social media laws in the nation
    url: https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/
    publisher: Office of the Governor of California
    date: 2026-09-10
  - title: New York and California Age Gating Rules Go Into Effect in the New Year
    url: https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year
    publisher: EFF
    date: 2026-11-24
  - title: Lawmakers warn ID verification companies to bolster security after September hack
    url: https://therecord.media/idscan-data-breach-warning-congressional-letter
    publisher: The Record
    date: 2026-11-24
  - title: FBI Probes Service Selling 153M+ Drivers Licenses
    url: https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/
    publisher: KrebsOnSecurity
    date: 2026-09-01
  - title: "Now open source: our Zero-Knowledge Proof (ZKP) libraries for age assurance"
    url: https://blog.google/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/
    publisher: Google
    date: 2025-07-03
  - title: longfellow-zk
    url: https://github.com/longfellow-zk/longfellow-zk
    publisher: GitHub
  - title: Code of Practice for Online Safety – App Distribution Services
    url: https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/regulations/codes-of-practice/code-of-practice-app-distribution-services/code-of-practice-for-online-safety-app-distribution-services.pdf
    publisher: Infocomm Media Development Authority
  - title: Factsheet on Age Assurance under the ADS Code
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2025/01/ads-code/factsheet-on-age-assurance.pdf
    publisher: Infocomm Media Development Authority
    date: 2025-01-15
  - title: Keeping Young Users Safe Online
    url: https://www.imda.gov.sg/how-we-can-help/age-assurance
    publisher: Infocomm Media Development Authority
    date: 2026-04-22
  - title: 坚决防止未成年人沉迷网络游戏——国家新闻出版署有关负责人就《关于进一步严格管理 切实防止未成年人沉迷网络游戏的通知》答记者问
    url: https://www.gov.cn/zhengce/2021-08/30/content_5634208.htm
    publisher: 中国政府网
    date: 2021-08-30
regions:
  - US
authors:
  - anoni-net
---

From January 2027, social media platforms in New York and California must confirm that a user is an adult before showing them an algorithmic feed (the home feed a platform curates and keeps pushing as you scroll) or sending notifications late at night. In the New York Attorney General's press release, these two features are tied to depression, anxiety, and eating and sleep disorders among children, and in the California Governor's press release, the ban on offering addictive features to under-16s is listed as a child protection measure. California's law takes effect on 1 January, and New York's rules under the SAFE for Kids Act take effect on 25 January. Readers outside the two states are not covered.

In New York, users who are under 18 or have not confirmed their age will see only content from accounts they follow or select, in a set sequence such as chronological order, and will get no notifications between midnight and 6 a.m., according to the Attorney General's press release. Parental consent lifts these limits, and users without it are not cut off from the platform. California's SB 976 likewise requires parental consent for under-18s, while AB 1709 does not allow these features for under-16s even with consent. [AB 1043](https://anoni.net/news/en/2026/10/california-ab1856-open-source-exemption/) is a separate mechanism, under which the operating system passes the age range entered by the account holder to apps.

New York's rules apply to platforms where users spend at least 20 percent of their time on algorithmic feeds. Companies can pick any age assurance method that meets the rules' accuracy standards and protects users' data, and examples in the press release include uploading an image or video, or verifying an email address or phone number and cross-checking it against other information. A company that lists government ID as a method must also offer at least one method that does not require it. Companies that offer zero-knowledge proofs (a cryptographic method that proves a user is an adult without revealing anything else), and companies already required by other laws to collect ID, are exempt from offering that alternative.

New York's rules also limit what companies can keep after checking someone's age. They may collect only the minimum data needed, may not use it for any other purpose, and must delete it immediately after use, or de-identify it and use it only in that state. What must be kept for five years is a record tied to the account, such as the date, the method used and whether the result was adult or minor, and under the rules, no other personally identifying data beyond this record is required to be kept. When a platform hires an outside verification company, that company is bound by the same rules.

IDScan, an ID scanning company in Louisiana that scans IDs at in-person counters for clients such as car rental companies and cannabis dispensaries, was reported in September to have had client data stolen from its cloud platform. A seller on the dark web claimed to hold more than 153 million driver's licences from the United States and Canada, and after interviewing people whose IDs were being sold, KrebsOnSecurity concluded that the data appears to come from IDScan. The breach and age checks on social media are separate matters, and the link between them comes from KrebsOnSecurity's observations and a privacy researcher it interviewed.

## Perspective {#perspective}

Once you hand over an ID or a photo, a copy may stay with the verification company. The Record quotes KrebsOnSecurity's author as saying that in the couple of months after the IDScan incident he found more than twenty identity verification companies that often keep ID scans by default, and that the companies hiring them often have to pay extra to stop it. The privacy researcher KrebsOnSecurity interviewed believes that online identity schemes requiring a driver's licence in the name of child protection are sending sensitive data to more and more third-party companies, with oversight falling behind. On 23 November, members of Congress from both parties also wrote to several identity verification companies asking them to minimise the personal data they collect, share and keep.

Zero-knowledge proofs let a company receive only the result that a user is an adult, without getting the ID itself. The EU's age verification scheme takes this approach, and in September we looked at [its privacy design and disputes](https://anoni.net/news/en/2026/09/eu-age-verification-blueprint/). In July 2025, Google open-sourced longfellow-zk, its zero-knowledge proof library, under the Apache-2.0 licence, and it can work with existing digital credential standards. New York's rules do not require platforms to offer zero-knowledge proofs, and whether platforms adopt them will only be known after the rules take effect.

Reviewing the same rules, the Electronic Frontier Foundation (EFF), a digital rights group, is concerned that de-identified data could be used to train AI models or re-identified after a breach, and also counts the five-year record as a risk of misuse and breach. The rules require platforms to take reasonable steps to detect users concealing or misrepresenting their location, which EFF believes will expand location tracking and may affect VPN users.

Adults can also be wrongly classified as minors, and they can appeal. New York's rules require companies to respond or ask for more information within 10 business days, and an appeal must accept at least one kind of supporting information other than government ID. The rules set no ceiling on how often adults are misclassified, and only require the misclassification rate for users aged 18 to 30 to be reported in each annual certification.

Users in New York who are asked to confirm their age can read the platform's explanation before choosing a method, since the rules require platforms to state which methods they offer, what the data is used for, and when and how it is deleted. Alternatives such as photos, videos and phone numbers also hand data to a company. Per the press release, people who do not want to confirm their age can still use the platform, seeing content only from accounts they follow or select, in a set sequence. California's rules were still a draft as of 24 November, so users in California will not know which methods platforms will offer until they are final.

Singapore puts the duty on app stores, and since 1 April 2026 the five stores designated by the Infocomm Media Development Authority (IMDA), including Apple's App Store and Google Play, have had to establish whether a user is under 18. As in New York, each store chooses its own method, and IMDA's list, updated in April 2026, ranges from a check against Singpass or an identity document to AI estimation from a face or voice. The code also calls for data minimisation under Singapore's Personal Data Protection Act.

In mainland China, every online game account must be registered with real identity information, and games may not serve unregistered users in any form, including guest modes, according to an August 2021 Q&A from the National Press and Publication Administration on its notice on online gaming by minors. The notice limited minors to one hour of play, between 8 and 9 in the evening on Fridays, weekends and public holidays.

When comparing rules elsewhere, on privacy, look at whether there is a way to avoid showing ID, what data companies may keep and for how long, and whether hired verification companies are bound by the same rules. On child protection, look at how people who are misclassified can appeal, and whether the rules actually stop minors from using these features.
