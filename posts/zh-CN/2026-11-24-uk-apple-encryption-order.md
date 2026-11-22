---
title: 英国政府对 Apple 技术能力通知的保密主张与调查权力法庭判决
description: 英国调查权力法庭 11 月 19 日的判决认定政府没有证明公开确认曾对 Apple 发出技术能力通知会损害国家安全，通知是否合法还没有审理，内容也没有公布。双方表示可望以 2027 年上半年为目标安排实质听证，依 Apple 的说明页，到 11 月 21 日英国以外的用户仍可开启 iCloud 高级数据保护。
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
  - title: 如何打开 iCloud 高级数据保护
    url: https://support.apple.com/zh-cn/108756
    publisher: Apple
    date: 2026-04-24
  - title: 进一步了解 iCloud（中国大陆）
    url: https://support.apple.com/zh-cn/111754
    publisher: Apple
    date: 2025-04-22
  - title: 适用于中国客户的 Apple 和云上贵州数据隐私声明
    url: https://support.apple.com/zh-cn/121767
    publisher: Apple
    date: 2024-12-10
  - title: iCloud 数据安全概览
    url: https://support.apple.com/zh-cn/102651
    publisher: Apple
    date: 2026-01-08
regions:
  - GB
authors:
  - anoni-net
---

英国调查权力法庭（审理部分国家安全案件的法庭）11 月 19 日公布判决，认定政府没有证明公开确认「曾对 Apple 发出技术能力通知」会损害国家安全。技术能力通知是政府要求运营商保有协助调查能力的命令，判决写明政府确实对 Apple 发出了通知。法庭没有判断通知是否合法，也没有公布通知的内容。

判决处理的是英国政府对 Apple 的要求，Apple 的英国说明页写明高级数据保护（ADP，让 iCloud 备份、照片等数据只有用户设备能解密）在英国以外的地方继续提供。到 11 月 21 日英国的新用户仍不能开启 ADP，已经开启的人之后要自行关闭才能继续使用 iCloud 账号。Apple 写会给这些人一段期间，MacRumors 11 月 19 日的报道写期限仍没有公布，我们也没有查到 Apple 对判决的公开声明。

媒体从 2025 年 2 月起报道，英国政府依《2016 年调查权力法》要求 Apple 维持以解密形式访问用户数据的能力。依倡议组织 Privacy International 整理的时间线，英国据报撤回一份通知，《金融时报》之后报道的第二份通知范围据信只限英国。Apple 与 Privacy International 等倡议组织都对通知提出申诉，法庭这次把两边的申诉一起处理。

英国政府对这类通知采取「不证实也不否认」的政策，在法庭上主张连确认通知存在都会损害国安。法庭推断，《泰晤士报》与《金融时报》引述政府消息来源的报道是经政府授权的说明，因此认定官方确认不会让恶意者多掌握实质的信息。法庭同意把通知内容与双方的证据全部公开会损害国安，哪些细节可以公开要等双方交换证据之后再决定。之后要审理通知本身是否合法的实质听证，双方表示可望以 2027 年上半年为目标安排。

## 导读观点 {#perspective}

英国政府在判决后的声明由 The Record 引述，声明提到 Apple 多年来依法协助警方与情报机关追查罪犯，「这份技术能力通知只是要求他们维持这样的能力」。iCloud 默认的标准数据保护会加密数据，密钥则存放在 Apple 的数据中心，开启 ADP 后大部分数据的密钥只留在用户信任的设备上。我们依政府声明的说法推论，要对开启 ADP 的账号维持这种能力，Apple 就需要重新取得密钥。Apple 则在 2025 年 9 月的英国说明页写到，从未在任何产品或服务中植入后门或万能钥匙，将来也不会。

Apple 在申诉中质疑《调查权力法》的权力能否用来规范公司提供的安全或隐私服务，也质疑通知对欧洲人权公约保障的权利所做的限制，是否超出达成目的所需的程度。政府的声明则写到隐私虽然重要也不该以英国民众的安全为代价，影响民众安全的决定应由民选政府与独立的法官做出，不在科技公司的董事会里决定。

判决没有改变英国用户目前的限制。在提供 ADP 的地区，iPhone 与 iPad 用户依 Apple 简体中文说明页的步骤在「设置」App 依次轻点你的姓名、「iCloud」与「高级数据保护」，还没开启的账户会看到「打开高级数据保护」。打开前要先设置恢复联系人或恢复密钥，打开后 Apple 没有协助恢复所需的密钥，无法访问账户时要靠这些方式或设备密码恢复数据。打开之后 iCloud 云备份、iCloud 云盘、照片、备忘录等数据改用端对端加密，iCloud 邮件、通讯录与日历仍由 Apple 保管密钥。

iCloud 在中国大陆由云上贵州（云上艾珀（贵州）技术有限公司）运营，Apple 的说明页写明用户的照片、文件和其他 iCloud 数据会储存在中国境内。Apple 简体中文的 ADP 说明页与 iCloud 数据安全概览都没有提到中国大陆的限制。到 11 月 21 日，我们没有找到 Apple 对 ADP 在中国大陆账号是否可用的说明，判决也没有写到由云上贵州运营的 iCloud。

之后的实质听证要处理的问题之一，是《调查权力法》的权力能否用来规范公司提供给客户的安全或隐私服务。如果可以，在英国提供服务的公司还能不能提供密钥只留在用户设备上的设计？政府想达成的调查效果在这种设计下能否做到？法庭也要在英国民众了解这项权力范围的需要，与政府主张公开细节会带来的国安风险之间，决定审理能公开到什么程度。
