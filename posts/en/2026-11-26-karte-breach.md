---
title: The breach of Japanese marketing platform KARTE and member data from hundreds of companies
description: KARTE, a marketing platform run by the Japanese company PLAID, Inc., was broken into by an outside attacker on 13 November. PLAID's investigation findings of 20 November list member data imported by hundreds of companies, and records of visitors' behaviour on those companies' websites, as leaked or possibly leaked, including data from companies whose contracts had ended and whose data should already have been deleted. Ordinary visitors may not know that a website uses KARTE. Customers and members of these companies, and users of their websites and apps, can watch for notices from the companies.
date: 2026-11-26T00:05:00+08:00
slug: karte-breach
categories: [security]
regions: [JP]
sources:
  - title: 「KARTE」への不正アクセスに関する当社調査結果と、サービス再開の見通し等のお知らせ
    url: https://plaid.co.jp/news/20261120/
    publisher: PLAID
    date: 2026-11-20
  - title: 不正アクセスによる個人情報を含む可能性のある情報等の漏えいに関するお詫びとお知らせ
    url: https://plaid.co.jp/news/20261116/
    publisher: PLAID
    date: 2026-11-16
  - title: 当社サービスへの不正アクセスについて（KARTEをご利用いただいている企業のお客様向けのご案内）
    url: https://plaid.co.jp/notice/202611-faq/
    publisher: PLAID
  - title: 当行委託先が提供するサービスへの不正アクセスについて
    url: https://www.bk.mufg.jp/news/news2026/pdf/news1118.pdf
    publisher: MUFG Bank
    date: 2026-11-18
  - title: 外部サービス「KARTE」への不正アクセスに伴うお客様情報漏えいに関するお詫びとお知らせ
    url: https://dhc-corporate.co.jp/cms_dH8vjpRq/wp-content/uploads/2026/11/2d7a589cb5008fbc262624582782444f.pdf
    publisher: DHC
    date: 2026-11-18
  - title: プレイドのCXプラットフォーム「KARTE」への不正アクセスについてまとめてみた
    url: https://piyolog.hatenadiary.jp/entry/2026/11/18/010752
    publisher: piyolog
    date: 2026-11-18
  - title: JS SDK（計測タグ）について
    url: https://developers.karte.io/reference/js-sdk
    publisher: KARTE Developers
  - title: EasyPrivacy
    url: https://easylist.to/easylist/easyprivacy.txt
    publisher: EasyList
    date: 2026-11-21
  - title: 個人情報の保護に関する法律
    url: https://laws.e-gov.go.jp/law/415AC0000000057
    publisher: e-Gov法令検索
  - title: JINS、三菱UFJ銀行等數十家日本企業陸續發布資安事件公告，皆因第三方行銷科技業者PLAID旗下KARTE平臺遭駭
    url: https://www.ithome.com.tw/news/180640
    publisher: iThome
    date: 2026-11-19
  - title: 個人資料保護法（民國 112 年 05 月 31 日版）
    url: https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=I0050021
    publisher: 全國法規資料庫
  - title: 金融監督管理委員會指定非公務機關個人資料檔案安全維護辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0380233
    publisher: 全國法規資料庫
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 中国人大网
    date: 2021-08-20
authors:
  - anoni-net
---

People who have signed up as members on a Japanese shopping site or banking app may have their data stored at a marketing company they have never dealt with directly. KARTE is a marketing platform from the Japanese company PLAID, Inc. that is embedded in companies' websites and apps to record what visitors view and click, and companies also import their own member data into KARTE to use alongside those records. PLAID detected an outside attacker on 13 November and shut down the entire KARTE service the same day, and its investigation findings published on 20 November list data entrusted by hundreds of companies as leaked or possibly leaked. Only customers and members of companies that have used KARTE, and people who have used those companies' websites or apps, can fall within the scope of this breach.

According to PLAID's announcement of 16 November, the attacker exploited a vulnerability in PLAID's servers in the early hours of the 13th to steal the credentials used to connect to its databases, and read data out of them. The attacker then used the same credentials to take over accounts and log in to KARTE's admin console, and PLAID detected the intrusion that morning and shut down its servers in the afternoon.

The 20 November announcement sorts the data that companies entrusted to KARTE into four categories, and because some companies fall into more than one, the per-category counts cannot be added up; the announcement gives no overall total. The two categories that concern website users directly are customer data the companies imported, such as member data (570 companies), and records of visitors' page views and clicks (487 companies), and in each case it is part of that data that leaked or may have leaked. The other two are cached data that KARTE held temporarily, which includes visitor identifiers, and credentials for connecting to services such as email delivery, the equivalent of keys or passwords. The credentials contain no personal data, but if they are not revoked they could be used to access those services.

The affected companies also include ones whose contracts with PLAID had fully or partly ended, a correction the 20 November announcement made to what PLAID said on 16 November. Under the terms of service this data should have been deleted when the contracts ended, but it remained because of lapses in staff operations and management, and PLAID plans to delete it and send notifications once the verification it will carry out for resuming the service is complete.

Company notices began appearing on 17 November, and by 21 November the Japanese security blog piyolog had listed 108 organisations that had published one. What leaked varies widely from company to company, and the two examples below are ones whose original notices we checked. MUFG Bank's notice covers about 6.5 million records containing only customers' gender, age and area of residence, with no names or contact details. DHC's covers about 19.11 million records, including names, email addresses, dates of birth and member IDs, but not login passwords or credit card data.

## Perspective {#perspective}

KARTE's tracking tag is a piece of code that a company issues from the admin console and places on its web pages, and according to the developer documentation, once a visitor's browser loads it, the tag sends browsing events to KARTE. Companies separately import their own member data, so both kinds of data sit on the same platform, and data from hundreds of companies is concentrated with a single provider. The [netiCRM incident](https://anoni.net/news/en/2026/11/neticrm-breach/) we covered on 19 November was also a break-in at a service provider's server, after which one client organisation announced it had been notified that its donation database had been copied.

Visitors never sign up for KARTE themselves, and their data is handled by PLAID on behalf of the companies. PLAID's FAQ for ordinary visitors says it cannot answer whether a particular website uses KARTE or whether a given person's data is within the scope of the leak, and its announcements offer no way to look this up. To find out whether you are affected, you have to wait for a company's notice or ask the companies you deal with, and whether and when to notify is up to each company. Since data from companies whose contracts had ended was still on PLAID's systems, our reading is that data may also stay with the provider after a company stops using KARTE, and a request to delete it likewise goes to the company.

Content-blocking extensions can reduce the behavioural data that third-party tools collect in the browser, and filter lists such as EasyPrivacy can be applied to decide which addresses to block. The 21 November version of EasyPrivacy has blocking rules for only some KARTE addresses and also makes exceptions for 3 websites, so installing an extension does not guarantee that every request to KARTE is blocked. Extensions work only inside the browser and have no effect on collection inside apps. Member data is data a company already holds and imports into KARTE itself, so blocking KARTE's code in the browser does not stop the company from sending data it already has.

People who receive a notice from a company can check in it which items leaked, and the notices from MUFG Bank and DHC both say the companies will contact affected customers individually. DHC's notice asks customers who receive suspicious emails claiming to be from DHC not to open links or attachments, and not to enter personal data or passwords. Following these reminders lowers the chance of being tricked into handing over data by impersonation emails, but data that has already leaked cannot be taken back.

Japan's national data protection regulator is the Personal Information Protection Commission (PPC). Under Article 26(1) of the Act on the Protection of Personal Information, as in force on 9 October 2026, a business that handles personal data on another business's behalf need not report a breach to the PPC itself if it has notified the business that entrusted it with the data in the manner the PPC's rules set. Article 26(2) also excludes a business that has given such notice from the duty to notify the people affected, so in our reading, where PLAID has notified its clients in this way, telling customers falls to each client company.

JINS Japan is among the companies that issued notices, and according to iThome, JINS in Taiwan announced on 18 November that the leak was limited to systems in Japan and that Taiwanese members' data is managed separately and was not affected. In Taiwan, Article 12 of the Personal Data Protection Act as in force on 9 October 2026 requires an organisation that violates the Act, resulting in personal data being stolen or leaked, to notify the people concerned by appropriate means once the facts are established, but sets no deadline and no duty to report to a regulator, and amendments promulgated in November 2025 that add a reporting duty had no effective date as of that day. Reporting comes instead from sector rules, such as those of the Financial Supervisory Commission (FSC), which require banks and other financial institutions to report serious incidents within 72 hours. In mainland China, Article 57 of the Personal Information Protection Law requires a personal information handler, when personal information has been or may have been leaked, to take remedial measures immediately and notify the responsible authorities and the individuals concerned, with no set number of days, though individuals need not be notified if the measures can effectively prevent harm, unless the authorities consider harm possible and require notification.

PLAID has set mid-January 2027 as its target for resuming KARTE in stages, will also bring in a third-party organisation for verification, and plans to hand detailed data to each company in turn from 24 November. As of 22 November, the PPC had not posted anything about the incident on its website, while PLAID's announcement says it is in the process of reporting to the commission. Things to watch are whether companies update the number of records and the items in their notices once they have the detailed data, and how the commission handles the case.
