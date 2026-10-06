---
title: iPhone Automatic Restart and a forensic vendor's bypass claim
description: Since iOS 18.1, an iPhone that stays locked for a long time restarts itself, putting its data back into a harder-to-extract state. In a forensic vendor's video, apparently made in early 2025, an employee says seized phones keep their once-unlocked state even after a restart. As of 7 October it is unclear whether this works on the latest iOS, and neither Apple nor Magnet responded to 404 Media.
date: 2026-10-08T00:10:00+08:00
slug: iphone-inactivity-reboot-bypass
categories:
  - mobile
sources:
  - title: Protecting user data in the face of attack
    url: https://support.apple.com/guide/security/protecting-user-data-in-the-face-of-attack-secf5549a4f5/web
    publisher: Apple
    date: 2026-01-28
  - title: 遭遇攻擊時保護使用者資料
    url: https://support.apple.com/zh-tw/guide/security/secf5549a4f5/web
    publisher: Apple
    date: 2026-01-28
  - title: Cops Can Bypass iPhone’s Automatic Reboot to Get Into Locked Phones, Leaked Video Claims
    url: https://www.404media.co/cops-can-bypass-iphone-automatic-inactivity-reboot-graykey/
    publisher: 404 Media
    date: 2026-10-01
  - title: Leaked Video Shows That Police Can Bypass iPhones' Automatic Reboot Feature
    url: https://www.privacyguides.org/news/2026/10/01/leaked-video-shows-that-police-can-bypass-iphones-automatic-reboot-feature/
    publisher: Privacy Guides
    date: 2026-10-01
  - title: GrayKey maker can reportedly bypass the iPhone’s ‘Inactivity Reboot’ security feature
    url: https://9to5mac.com/2026/10/01/graykey-maker-can-reportedly-bypass-the-iphones-inactivity-reboot-security-feature/
    publisher: 9to5Mac
    date: 2026-10-01
  - title: A forensic tool claims it can stop seized iPhones from locking down after 72 hours
    url: https://www.techspot.com/news/114070-new-graykey-feature-police-stop-seized-iphones-becoming.html
    publisher: TechSpot
    date: 2026-10-02
  - title: Access the critical iOS and Android evidence you need
    url: https://www.magnetforensics.com/products/magnet-graykey/
    publisher: Magnet Forensics
  - title: New Apple security feature reboots iPhones after 3 days, researchers confirm
    url: https://techcrunch.com/2024/11/14/new-apple-security-feature-reboots-iphones-after-3-days-researchers-confirm
    publisher: TechCrunch
    date: 2024-11-14
  - title: Reverse Engineering iOS 18 Inactivity Reboot
    url: https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html
    publisher: naehrdine
    date: 2024-11-17
  - title: 密碼
    url: https://support.apple.com/zh-tw/guide/security/sec20230a10d/web
    publisher: Apple
    date: 2024-12-19
  - title: 在 iPhone 上設定密碼
    url: https://support.apple.com/zh-tw/guide/iphone/iph14a867ae/ios
    publisher: Apple
  - title: Apple 安全性發布
    url: https://support.apple.com/zh-tw/100100
    publisher: Apple
  - title: Passcodes and passwords
    url: https://support.apple.com/guide/security/passcodes-and-passwords-sec20230a10d/web
    publisher: Apple
    date: 2024-12-19
  - title: Set a passcode on iPhone
    url: https://support.apple.com/guide/iphone/set-a-passcode-iph14a867ae/ios
    publisher: Apple
  - title: Apple security releases
    url: https://support.apple.com/en-us/100100
    publisher: Apple
  - title: 2026 Implementation Rules for Amending the Implementation Rules for Article 43 of the Law of the People’s Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region
    url: https://www.doj.gov.hk/en/legco/pdf/ajls20260324e1.pdf
    publisher: Department of Justice, HKSAR
    date: 2026-03-24
  - title: 署理律政司司長與保安局局長出席立法會司法及法律事務委員會及保安事務委員會聯席會議後會見傳媒開場發言（只有中文）
    url: https://www.doj.gov.hk/tc/community_engagement/press/pdf/pr20260324c2.pdf
    publisher: Department of Justice, HKSAR
    date: 2026-03-24
  - title: Criminal Procedure Code 2010
    url: https://sso.agc.gov.sg/Act/CPC2010?ProvIds=pr40-
    publisher: Singapore Statutes Online
  - title: 最高人民法院 最高人民检察院 公安部关于办理刑事案件收集提取和审查判断电子数据若干问题的规定
    url: https://www.court.gov.cn/fabu/xiangqing/26431.html
    publisher: 最高人民法院
    date: 2016-09-20
  - title: 公安机关办理刑事案件电子数据取证规则
    url: https://www.chinalawtranslate.com/公安机关办理刑事案件电子数据取证规则/
    publisher: China Law Translate
    date: 2019-01-03
  - title: 公安部拟明确刑事案件电子数据取证中获取密码等特殊程序
    url: https://www.news.cn/20260522/8b1b030da10b422aa634e1324e5a1f10/c.html
    publisher: Xinhua
    date: 2026-05-22
authors:
  - anoni-net
---

404 Media reported on 1 October that it had obtained a video made by Magnet Forensics, the maker of Graykey, a tool sold to law enforcement for unlocking phones and extracting their data. In the video, a Magnet employee says the Graykey Preserve device and Graykey's Evidence Preservation Mode keep a seized iPhone in a state that is easier to extract data from, even if the phone reboots "for any number of reasons" or loses power. 404 Media's report describes the technology as a way around what it calls inactivity reboot, the iOS 18.1 feature that Apple's Platform Security guide calls Automatic Restart. According to 9to5Mac, citing 404 Media, it is a training video made for law enforcement and appears to date from early 2025.

TechSpot's report of 2 October says the claim has not been independently verified. 9to5Mac's report adds that it is unclear how long the technique has been available, whether it has been used in real cases, and whether it still works on the latest iOS. According to 9to5Mac and Privacy Guides, neither Apple nor Magnet responded to 404 Media's request for comment.

According to Privacy Guides, which relays 404 Media's report, the video gives no technical details of how this works. As of 7 October, Magnet's own Graykey product page says it can "protect your extractions from automatic reboot timers".

## Perspective {#perspective}

The protection rests on two states described in a TechCrunch report from November 2024. Before First Unlock (BFU) is a phone that has been switched on but not yet unlocked with its passcode, and according to that report its data is fully encrypted and near-impossible to access without the passcode. After First Unlock (AFU) is a phone that has been unlocked at least once since starting up, and some of its data is unencrypted, which some forensic tools may extract more easily even while the phone is locked.

Apple's Platform Security guide says Automatic Restart in iOS 18.1 and iPadOS 18.1 or later uses the Secure Enclave, a dedicated subsystem on the chip that handles keys, to watch unlock events. A device left locked for a prolonged period restarts on its own, moving from AFU to BFU and purging sensitive keys and transient data from memory. From iOS 18.4, device management administrators can turn Automatic Restart on or off, and it is off by default on supervised devices (iPhones set up centrally by an organisation such as an employer or school). Apple's guide does not give the interval, but a researcher measured 72 hours in November 2024, and TechCrunch reported at the time that Magnet also confirmed the figure.

The researcher who measured the 72 hours wrote that thieves lack the means to get current exploits within three days, so the restart likely locks them out entirely, while law enforcement comes under more time pressure. Privacy Guides' news brief relays the video's claim that Evidence Preservation Mode "captures" the iPhone in AFU, so the AFU state survives a restart. If that is true, a phone that has already been accessed and preserved keeps its AFU state when the 72 hours run out. In our view, how much that time pressure matters depends on whether investigators can demand the passcode, and the rules differ from place to place, as Hong Kong, Singapore and mainland China show.

In Hong Kong, amended rules under Article 43 of the National Security Law took effect on 23 March 2026 for investigations of offences endangering national security. Police may require a suspect, or anyone they reasonably believe owns, uses or knows the password to a device, to provide the password or other decryption method, and failing to comply without reasonable excuse carries up to a year in prison and a HK$100,000 fine. The Secretary for Security told reporters on 24 March that police must first apply to a court for a warrant on affidavit. The Department of Justice's paper notes that the earlier rules already let police search electronic equipment where obtaining a warrant was not reasonably practicable, but does not say whether that route also applies to the new password requirement.

Singapore's Criminal Procedure Code, section 40, lets police authorised by the Public Prosecutor require access to decryption information when investigating an arrestable offence. Failing to comply can bring a fine of up to S$10,000, up to three years in prison, or both, with heavier penalties of up to S$50,000 or ten years where the data holds evidence of certain serious offences.

In mainland China, a 2016 regulation from the Supreme People's Court, the Supreme People's Procuratorate and the Ministry of Public Security, and the Ministry's rules on electronic evidence in criminal cases, in force since February 2019, both say seized phones should be sealed with signal shielding, signal blocking or cutting the power. Xinhua reported in May 2026 that the Ministry of Public Security had published a draft revision of those rules for public comment. When the holder refuses to provide an account password, the draft lets police obtain it by other means with approval from a public security chief at county level or above, after informing the holder or in front of a witness. We found no final version as of 7 October.

Our reading is that where a passcode can be compelled, a phone in BFU guards against thieves more than against a legal demand for the passcode. Where it cannot, keeping a seized phone in AFU is worth more to investigators. None of the sources says what an ordinary user can do to stop Magnet's technique.

Apple's iPhone User Guide says the passcode is always required after the phone is turned on or restarted. People worried that their phone could be seized can switch it off before it may leave their hands, so it starts up in BFU. This is our inference from the definition of BFU, and the video does not say whether Magnet's technique works on a phone already in BFU.

According to the video, once preservation starts even a loss of power does not lose the AFU state. In our reading, switching off only helps before the phone is taken. Switching off also means missing calls and messages in the meantime.

Apple's "Passcodes and passwords" page says an attacker holding a device cannot get at data in specific protection classes without the passcode, and that longer passcodes are stronger against brute-force attacks. The same page adds that a longer numeric passcode may be easier to enter than a shorter alphanumeric one while giving similar security. It does not discuss how passcode length affects Magnet's technique.

To change the passcode, go to Settings, then Face ID & Passcode (or Touch ID & Passcode), tap Change Passcode, then Passcode Options. The iPhone User Guide lists Custom Alphanumeric Code and Custom Numeric Code as the most secure options. The cost is typing a longer passcode after every restart and whenever the phone has not been unlocked for more than 48 hours.

People with no reason to expect their phone to be seized do not need to change anything for this story. People using a supervised iPhone cannot assume the 72-hour restart applies.

Apple's security releases page says Apple does not disclose, discuss or confirm security issues until an investigation has occurred and patches or releases are generally available. As of 7 October it is unclear whether Magnet's technique works on the latest iOS, and in November it is worth checking iOS release notes for a related fix and whether any researcher has verified the claim.
