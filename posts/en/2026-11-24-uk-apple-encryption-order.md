---
title: UK secrecy over the Apple technical capability notice and the Investigatory Powers Tribunal ruling
description: The Investigatory Powers Tribunal ruled on 19 November that the UK government had not shown that publicly confirming it gave Apple a technical capability notice would damage national security. Whether the notice is lawful has not been heard and its content has not been published. The parties indicate they are likely to agree arrangements aimed at a substantive hearing in the first half of 2027, and according to Apple's support page, users outside the UK could still turn on iCloud Advanced Data Protection as of 21 November.
date: 2026-11-24T00:05:00+08:00
slug: uk-apple-encryption-order
categories:
  - encryption
follows:
  - 2026-09-27-uk-icloud-advanced-data-protection
sources:
  - title: OPEN Judgment Apple Inc. and Privacy Int. Ors
    url: https://www.judiciary.uk/wp-content/uploads/2026/11/OPEN-Judgment-Apple-Inc.-and-Privacy-Int.-Ors.pdf
    publisher: Investigatory Powers Tribunal
    date: 2026-11-19
  - title: UK court confirms British government served Apple with secret encryption notice
    url: https://therecord.media/apple-uk-encryption-notice
    publisher: The Record
    date: 2026-11-19
  - title: "Win! Tribunal orders UK Government to come clean about secret order to Apple"
    url: https://privacyinternational.org/news-analysis/5896/win-tribunal-orders-uk-government-come-clean-about-secret-order-apple
    publisher: Privacy International
    date: 2026-11-19
  - title: UK Loses Secrecy Fight Over Apple 'Backdoor' Order
    url: https://www.macrumors.com/2026/11/19/uk-loses-secrecy-fight-over-apple-backdoor-order/
    publisher: MacRumors
    date: 2026-11-19
  - title: UK Government Forced to Admit It Issued Apple a Secret Encryption Order
    url: https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/
    publisher: MacAnorak
    date: 2026-11-19
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: iCloud data security overview
    url: https://support.apple.com/en-us/102651
    publisher: Apple
    date: 2026-01-05
  - title: 如何開啟「iCloud 進階資料保護」
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
    date: 2026-04-24
  - title: How to turn on Advanced Data Protection for iCloud
    url: https://support.apple.com/en-us/108756
    publisher: Apple
    date: 2026-04-17
  - title: 如何開啟「iCloud 進階資料保護」 (How to turn on Advanced Data Protection for iCloud, Apple Support Hong Kong)
    url: https://support.apple.com/zh-hk/108756
    publisher: Apple
    date: 2026-04-24
  - title: Learn more about iCloud in China mainland
    url: https://support.apple.com/en-us/111754
    publisher: Apple
    date: 2025-04-15
  - title: 适用于中国客户的 Apple 和云上贵州数据隐私声明 (Apple and GCBD data privacy statement for customers in China)
    url: https://support.apple.com/zh-cn/121767
    publisher: Apple
    date: 2024-12-10
regions:
  - GB
authors:
  - anoni-net
---

The Investigatory Powers Tribunal, a UK court that hears certain national security cases, published a judgment on 19 November finding that the government had not shown that publicly confirming it had given Apple a "technical capability notice" would damage national security. A technical capability notice is a government order requiring a company to maintain the ability to help with investigations, and the tribunal confirmed in the judgment that the government had given Apple one. The tribunal did not decide whether the notice is lawful, and it did not publish the notice's content.

On its support page about the UK, Apple writes that Advanced Data Protection (ADP, which lets only the user's own devices decrypt data such as iCloud backups and photos) "continues to be available everywhere else in the world." As of 21 November, new users in the UK still cannot turn ADP on, and those who already have it will need to turn it off themselves to keep using their iCloud account. Apple wrote that it would give them a period of time to do so, but MacRumors reported on 19 November that no deadline had yet been set, and we have not found a public statement from Apple on the ruling.

Since February 2025, media have reported that the UK government used the Investigatory Powers Act 2016 to require Apple to keep the ability to access user data in decrypted form. According to a timeline compiled by the advocacy group Privacy International, the UK reportedly withdrew one notice, and a second notice later reported by the Financial Times was believed to apply only to the UK. Apple and advocacy groups including Privacy International each challenged the notice, and the tribunal dealt with both challenges together.

The UK government follows a "neither confirm nor deny" policy on such notices, and argued before the tribunal that even confirming the notice existed would damage national security. The tribunal inferred that reports in The Times and the Financial Times citing government sources were based on briefings the government had authorised, and therefore found that official confirmation would not add materially to what malign actors already know. It agreed that making the notice's content and all of both sides' evidence public would damage national security, and left the question of which details can be disclosed until the parties have exchanged evidence. For the substantive hearing on whether the notice itself is lawful, the parties indicated that they are likely to agree arrangements aimed at the first half of 2027.

## Perspective {#perspective}

In a statement after the ruling, quoted by The Record, a government spokesperson said Apple had been helping the police and intelligence agencies pursue criminals for several years, in accordance with the law, and that "This Technical Capability Notice simply requires that they maintain the ability to do so." Under iCloud's default standard data protection, data is encrypted but the keys are held in Apple's data centres. With ADP turned on, the keys for most data stay only on the user's trusted devices. Our reading of the government's statement is that maintaining that ability for accounts with ADP would require Apple to get hold of those keys again, while Apple wrote on its UK support page in September 2025 that "we have never built a backdoor or master key to any of our products or services and we never will."

In its challenge, Apple questions whether the powers in the Investigatory Powers Act can be used to regulate the security or privacy services a company offers, and whether the notice's interference with rights protected by the European Convention on Human Rights goes further than its aim requires. The spokesperson also said that the right to privacy is crucial but "should not come at the expense of the safety of the British public," and that decisions affecting the public's safety "must be made by democratically elected governments and independent judges, not in the boardrooms of technology companies."

The ruling does not change the current restriction for UK users; where ADP is offered, Apple's steps for iPhone and iPad go through Settings, your name and iCloud to Advanced Data Protection, where an account that has not enabled it will see Turn on Advanced Data Protection. Before turning it on you set up a recovery contact or recovery key. Once it is on, Apple does not have the keys needed to help with recovery, so if you lose access to your account you recover your data with one of those methods or your device passcode. With ADP on, iCloud Backup, iCloud Drive, Photos, Notes and other data move to end-to-end encryption, while Apple still holds the keys for iCloud Mail, Contacts and Calendars.

Apple's Traditional Chinese support pages for Taiwan and Hong Kong carry the same steps as the English page, consistent with the UK page's statement that ADP remains available everywhere else. In mainland China, iCloud is operated by GCBD (AIPO Cloud (Guizhou) Technology Co. Ltd), and according to Apple's privacy statement for customers in China, personal information on that service, including photos, documents and other iCloud data, is stored inside China. Whether accounts on GCBD-operated iCloud can turn on ADP is not stated on Apple's ADP support pages.

One of the questions for the substantive hearing is whether the powers in the Investigatory Powers Act can be used to regulate the security or privacy services a company offers its customers. In our reading, if they can, what follows is whether a company operating in the UK could still offer a design in which the keys stay only on users' devices, and whether the investigative effect the government wants could be achieved under such a design. The tribunal will also have to decide how much of the hearing can be held in public, weighing the British public's need to understand the scope of this power against the national security risks the government says disclosure would bring.
