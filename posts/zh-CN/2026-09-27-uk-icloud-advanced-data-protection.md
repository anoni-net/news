---
title: 英国 iCloud 高级数据保护的分级现状
description: Apple 从 2025 年 2 月起不再让英国的新用户开启高级数据保护，在那之前开启的人仍受保护，英国的 iCloud 因此分成两种加密程度。英国以外的用户仍可开启。
date: 2026-09-27T07:28:00+08:00
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
  - title: Apple Launches New Legal Challenge Against UK Backdoor Demand
    url: https://www.macrumors.com/2026/08/03/apple-legal-challenge-against-uk-demand/
    publisher: MacRumors
    date: 2026-08-03
  - title: 如何開啟 iCloud 進階資料保護
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
  - title: 如何打开 iCloud 高级数据保护
    url: https://support.apple.com/zh-cn/108756
    publisher: Apple
authors:
  - anoni-net
---

Apple 从 2025 年 2 月起不再让英国的新用户开启 iCloud 的高级数据保护（Advanced Data Protection，简称 ADP），在那之前已经开启的人仍受保护。一位英国作者在 9 月 21 日的文章写到，同样住在英国、用同一款 iPhone 的两个人，iCloud 的加密程度因此不同。英国以外的地方仍可以开启 ADP。

起因是《华盛顿邮报》2025 年 2 月的报道，英国政府依据《调查权力法》发出技术能力通知，要求 Apple 建立访问加密 iCloud 数据的能力，范围涵盖全球用户。Apple 在 2 月 21 日宣布英国的新用户不能再开启 ADP，说明页写明 Apple 从未、也不会在产品中建置后门或万能钥匙。

Apple 的说明页列出影响范围。默认就端到端加密的 15 类数据不受影响，例如 iCloud 钥匙串与健康数据，iMessage 与 FaceTime 也维持端到端加密。没有开启 ADP 的英国用户，iCloud 云备份、iCloud 云盘、照片、备忘录等 10 类数据改用标准数据保护，密钥存放在 Apple 的数据中心。

已经开启 ADP 的英国用户，Apple 无法自动替他们关闭，这个设置只能从用户信任的设备更改。Apple 的公告写到会给这些用户一段时间自行关闭，原文写到 9 月 21 日为止还没有公布期限。

EFF 在 2025 年 10 月的文章写到，据报道英国改发了一份只针对英国用户的通知。Apple 在 2026 年 7 月向调查权力法庭提出新的申诉，争议还没有结果。

## 导读观点 {#perspective}

所有 iCloud 数据都有加密，差别在密钥放在哪里。标准数据保护的密钥在服务方手上，收到合法的调取要求时可以解密交出。ADP 让密钥只留在用户信任的设备上，Apple 没有钥匙，要取得内容就只能改变系统设计，英国的通知与 Apple 就僵持在这一点。

在中国大陆，iCloud 由 GCBD（AIPO Cloud (Guizhou) Technology Co. Ltd）运营，存放的照片、文件与备份受 GCBD 的条款约束。Apple 的说明页也写明，不是居住在中国大陆的中国公民，可以把 Apple 账户的国家或地区改成目前所在的地方，继续按 Apple 的条款使用 iCloud。

没有开启 ADP 时，Apple 的说明写明，同时开着 iCloud 云备份与「iCloud 中的信息」，备份里会附上信息的密钥。关闭 iCloud 云备份之后，设备会生成新的密钥，之后的信息维持端到端加密。改用电脑做加密的本地备份，备份就留在自己手上，这个选项默认没有开启，要在 Finder 或 Apple 设备 App 里勾选。

ADP 的代价是 Apple 无法协助恢复端到端加密的数据，丢失所有恢复方式就找不回来。开启之后 iCloud.com 的网页访问也会关闭，需要时要从信任的设备批准。

要开启 ADP，在 iPhone 的「设置」点自己的名字，进入 iCloud 打开「高级数据保护」，Apple 的支持页面有简体中文的步骤。Apple 账户需要先打开双重认证，并设置恢复联系人或恢复密钥，登录同一账户的所有设备也要更新到 iOS 16.2、macOS 13.1 以上的对应版本。管理式 Apple 账户与儿童账户不能开启。
