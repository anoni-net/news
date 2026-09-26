---
title: Two tiers of iCloud Advanced Data Protection in the UK
description: Since February 2025 new UK users cannot turn on Advanced Data Protection, while those who enabled it earlier keep it, leaving two levels of iCloud encryption in the same country.
date: 2026-09-29
slug: uk-icloud-advanced-data-protection
sources:
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: iCloud data security overview
    url: https://support.apple.com/en-us/102651
    publisher: Apple
    date: 2026-01-05
  - title: How to turn on Advanced Data Protection for iCloud
    url: https://support.apple.com/en-us/108756
    publisher: Apple
    date: 2026-04-17
  - title: About encrypted backups on your iPhone, iPad, or iPod touch
    url: https://support.apple.com/en-us/108353
    publisher: Apple
    date: 2026-09-21
  - title: Two-Tier Encryption in the UK
    url: https://macanorak.com/two-tier-encryption-in-the-uk/
    publisher: MacAnorak
    date: 2026-09-21
  - title: The UK Is Still Trying to Backdoor Encryption for Apple Users
    url: https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users
    publisher: EFF
    date: 2025-10-01
  - title: iCloud in China mainland
    url: https://support.apple.com/en-us/111754
    publisher: Apple
    date: 2025-04-15
  - title: "Assistance and Access: A new industry assistance framework"
    url: https://www.homeaffairs.gov.au/about-us/our-portfolios/national-security/lawful-access-telecommunications/assistance-and-access-industry-assistance-framework
    publisher: Australian Department of Home Affairs
    date: 2026-09-22
  - title: Apple Launches New Legal Challenge Against UK Backdoor Demand
    url: https://www.macrumors.com/2026/08/03/apple-legal-challenge-against-uk-demand/
    publisher: MacRumors
    date: 2026-08-03
authors:
  - anoni-net
---

Since February 2025, Apple has not let new UK users turn on Advanced Data Protection (ADP) for iCloud, while people who turned it on earlier keep it. A UK writer pointed out on 21 September that two people in the UK with the same iPhone can therefore have different levels of iCloud encryption. ADP remains available everywhere else.

The Washington Post reported in February 2025 that the UK had issued a technical capability notice under the Investigatory Powers Act, requiring Apple to be able to access encrypted iCloud data worldwide. On 21 February Apple withdrew ADP for new UK users, and its support page states that it has never built a backdoor or master key and never will.

The 15 categories end-to-end encrypted by default, such as iCloud Keychain and Health data, are unaffected, as are iMessage and FaceTime. For UK users without ADP, 10 categories including iCloud Backup, iCloud Drive, Photos and Notes fall back to standard data protection, with keys held in Apple's data centres. Apple cannot switch ADP off for existing UK users, because only their trusted devices can change the setting, and as of 21 September it had published no deadline for them to do it themselves.

EFF wrote in October 2025 that the UK had reportedly narrowed the notice to UK users. Apple filed a new complaint with the Investigatory Powers Tribunal in July 2026, and the dispute is unresolved.

## Perspective {#perspective}

All iCloud data is encrypted. What differs is who holds the keys. Under standard data protection Apple holds them and can decrypt data in response to a lawful demand. With ADP the keys stay on the user's trusted devices, so the only way to reach the content would be to change the system's design, and that is the point on which the UK notice and Apple are stuck.

The same legal instrument exists elsewhere in the region with a different limit. Australia's Assistance and Access Act 2018 also created technical capability notices, issued jointly by the Attorney-General and the Minister for Communications. The Department of Home Affairs states that such a notice is expressly prohibited from requiring a provider to build a capability to decrypt information or remove electronic protection. The UK notice, as reported, asks for the kind of capability that the Australian version rules out.

In mainland China, iCloud is operated by GCBD (AIPO Cloud (Guizhou) Technology Co. Ltd), and data stored there is subject to GCBD's terms. Apple's page adds that people who are not Chinese citizens living in mainland China can change their Apple Account country or region to where they are now and keep using iCloud under Apple's terms.

In Hong Kong, Taiwan, Japan, Singapore and the rest of Asia, ADP is available but optional, so it protects only people who switch it on. When the UK moved, the only people who stayed covered were those who had already done so.

To turn it on, open Settings, tap your name, then iCloud. You will be asked to set up a recovery contact or recovery key first, and every device on the account needs iOS 16.2 or the equivalent version. Without ADP, Apple notes that if iCloud Backup and Messages in iCloud are both on, the backup includes the Messages key. Turning off iCloud Backup makes the device generate a new key that keeps future messages end-to-end encrypted. An encrypted local backup on a computer, off by default and enabled in Finder or the Apple Devices app, keeps backups in your own hands.

The cost of ADP is that Apple cannot help you recover end-to-end encrypted data if you lose every recovery method. Web access at iCloud.com is also turned off until you approve it from a trusted device.
