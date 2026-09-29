---
title: Doxxing prevention and incident response
description: "EFF published a two-part doxxing safety guide in late August: audit your own footprint, then log incidents, harden accounts and lock your phone number. It is written for US readers, but the footprint audit and account hardening work anywhere."
date: 2026-10-03T07:00:00+08:00
slug: eff-doxxing-safety
sources:
  - title: "Doxxing Safety Pt I: Prevention and Footprint Management"
    url: https://www.eff.org/deeplinks/2026/08/doxxing-safety-pt-i-prevention-and-footprint-management
    publisher: Electronic Frontier Foundation
    date: 2026-08-31
  - title: "Doxxing Safety Part II: Incident Response"
    url: https://www.eff.org/deeplinks/2026/08/doxxing-safety-part-ii-incident-response
    publisher: Electronic Frontier Foundation
    date: 2026-08-31
  - title: The Personal Data (Privacy) (Amendment) Ordinance 2021
    url: https://www.pcpd.org.hk/english/data_privacy_law/amendments_2021/amendment_2021.html
    publisher: Office of the Privacy Commissioner for Personal Data, Hong Kong
    date: 2021-10-08
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=I0050021
    publisher: 全國法規資料庫
    date: 2023-05-31
  - title: 最高人民法院 最高人民检察院 公安部印发《关于依法惩治网络暴力违法犯罪的指导意见》的通知
    url: http://gongbao.court.gov.cn/Details/12dfb372281fcfc26a1489d012108b.html
    publisher: 最高人民法院公报
    date: 2023-09-20
  - title: "Have I Been Pwned: Check if your email address has been exposed in a data breach"
    url: https://haveibeenpwned.com/
    publisher: Have I Been Pwned
  - title: FAQs - Have I Been Pwned
    url: https://haveibeenpwned.com/FAQs
    publisher: Have I Been Pwned
  - title: DROP for data brokers
    url: https://privacy.ca.gov/data-brokers
    publisher: California Privacy Protection Agency
  - title: Connecting to Tor from censored regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: Is http://www.torproject.org blocked in mainland China?
    url: https://en.greatfire.org/www.torproject.org
    publisher: GreatFire
  - title: Is https://haveibeenpwned.com blocked in mainland China?
    url: https://en.greatfire.org/https/haveibeenpwned.com
    publisher: GreatFire
authors:
  - anoni-net
---

On 31 August the Electronic Frontier Foundation (EFF), a US digital rights group, published a two-part guide to doxxing, which it defines as "the deliberate disclosure of personal information" to bully, harass or intimidate someone. Part I is about prevention, Part II about responding once an attack is under way. The guide is written for readers in the US, but auditing your footprint and hardening your accounts work anywhere.

Prevention starts with auditing yourself: check breach databases, list the sites where your usernames are registered (EFF notes such search tools may not be entirely accurate) and set social media accounts to private. EFF names data brokers as a frequent source for doxxers and cites a study finding DIY removal requests more effective than paid services, which may still suit people who would rather hand the work off.

Once an incident starts, keep a log of times, places, people and what you saw. To check forums where harassers gather, EFF recommends Tor Browser (a browser that hides where you connect from) and no engagement. Turn on two-factor authentication, consider shutting down targeted accounts and, where providers offer them, add PINs to phone and bank accounts to block SIM swapping (an attacker taking over your number by impersonating you). Friends can share the monitoring, and Part II suggests a PACE plan (primary, alternate, contingency, escape/emergency).

## Perspective {#perspective}

Doxxers piece together scraps of information from breach databases, data brokers and public records into a dossier. Some remedies exist only in the US: address confidentiality programmes in some states, which substitute a proxy address in public records, and California's DROP, which lets residents send one deletion request to all registered data brokers. In mainland China, GreatFire's tests show torproject.org blocked (checked 29 September), and the Tor Project's support page advises users there to get Tor Browser through GetTor and connect with bridges (unlisted entry points to the Tor network).

Hong Kong made doxxing a specific offence in October 2021, with a first tier punishable by up to HK$100,000 and two years in prison and a second tier, where specified harm is caused, by up to HK$1,000,000 and five years. The Privacy Commissioner for Personal Data, head of the city's privacy regulator, can also serve cessation notices to have doxxing content removed, including posts on online platforms.

In mainland China, under 2023 guidelines on cyber violence from the Supreme People's Court, the Supreme People's Procuratorate and the Ministry of Public Security, organising a "human flesh search" to illegally collect citizens' personal information and publish it to the public at large is punished as the crime of infringing citizens' personal information when the circumstances are serious. Victims who can show an infringement is under way or imminent can also seek an injunction under Article 997 of the Civil Code.

In Taiwan, unlawfully collecting or using personal data in a way liable to cause damage can bring up to five years in prison under Article 41 of the Personal Data Protection Act, to which a fine of up to NT$1 million may be added. The offence requires intent to obtain an unlawful gain for oneself or a third party, or to damage another person's interests.

Whichever system applies, a complaint needs evidence, so start the incident log with the first message and keep screenshots and links alongside it. Going to the police is a judgement call: EFF writes that "for many, talking to law enforcement will only make things worse."

The first step you can take today is to enter your email address at Have I Been Pwned, a site that indexes known data breaches. As of 29 September the search is free, needs no account and the site is English-only; GreatFire's last test, on 9 February, found it reachable from mainland China. If your address appears, EFF lists changing the exposed email address or phone number as an option, while noting that doing so is "extremely inconvenient".
