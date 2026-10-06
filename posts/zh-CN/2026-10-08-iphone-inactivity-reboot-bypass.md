---
title: iPhone 自动重启与取证工具的绕过说法
description: iOS 18.1 起，iPhone 长时间没有解锁会自动重启，让数据回到较难提取的状态。一段约在 2025 年初制作的取证厂商视频里，员工说扣押的手机即使重启也能保留解锁过一次的状态。这项手法对最新版 iOS 是否有效，到 10 月 7 日为止并不清楚。Apple 没有回复报道的询问，担心手机被扣押取证的人可以留意后续。
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
  - title: 在用户数据受到攻击时提供保护
    url: https://support.apple.com/zh-cn/guide/security/secf5549a4f5/web
    publisher: Apple
    date: 2026-01-28
  - title: 密码
    url: https://support.apple.com/zh-cn/guide/security/sec20230a10d/web
    publisher: Apple
    date: 2024-12-19
  - title: 在 iPhone 上设定密码
    url: https://support.apple.com/zh-cn/guide/iphone/iph14a867ae/ios
    publisher: Apple
  - title: Apple 安全性发布
    url: https://support.apple.com/zh-cn/100100
    publisher: Apple
  - title: 最高人民法院 最高人民检察院 公安部关于办理刑事案件收集提取和审查判断电子数据若干问题的规定
    url: https://www.court.gov.cn/fabu/xiangqing/26431.html
    publisher: 最高人民法院
    date: 2016-09-20
  - title: 公安机关办理刑事案件电子数据取证规则
    url: https://www.chinalawtranslate.com/公安机关办理刑事案件电子数据取证规则/
    publisher: China Law Translate
    date: 2019-01-03
  - title: 公安机关电子数据取证规则（征求意见稿）及起草说明
    url: https://www.elawcn.com/rule/2026/0827/1902.html
    publisher: 中国互联网法务网
    date: 2026-08-27
  - title: 公安部拟明确刑事案件电子数据取证中获取密码等特殊程序
    url: https://www.news.cn/20260522/8b1b030da10b422aa634e1324e5a1f10/c.html
    publisher: 新华社
    date: 2026-05-22
  - title: 公安机关电子数据取证规则（征求意见稿）
    url: https://www.chinalawtranslate.com/en/22621-2/
    publisher: China Law Translate
    date: 2026-06-01
authors:
  - anoni-net
---

404 Media 在 10 月 1 日的报道写到，他们取得了一段 Magnet Forensics 的视频，该公司的 Graykey 是卖给执法部门、用来解锁手机并提取数据的工具。视频里的 Magnet 员工说，Graykey Preserve 设备与 Graykey 的 Evidence Preservation Mode 能让扣押的 iPhone 停留在较容易提取数据的状态，即使手机因各种原因重启或断电也一样。404 Media 的报道把这项技术写成用来绕过 iOS 18.1 起的“自动重启”（英文报道多称 Inactivity Reboot）。据 9to5Mac 引述 404 Media 的内容，这是专给执法人员的培训视频，看起来在 2025 年初制作。

TechSpot 在 10 月 2 日的报道写明，这一说法尚未经过独立验证。9to5Mac 也写到，这项技术提供给执法部门多久、是否用在实际案件，以及对最新版的 iOS 是否有效都不清楚。据 9to5Mac 与 Privacy Guides 的转述，404 Media 向 Apple 与 Magnet 询问，两家都没有回复。到 10 月 7 日为止，本文查到的来源里没有 Apple 对这一说法的回应。

TechCrunch 2024 年 11 月的报道写到两种状态的差别。手机开机之后还没输入过密码的状态称为“首次解锁前”（BFU）。据 TechCrunch 的说法，这时用户数据完全加密，不知道密码几乎无法提取。输入过一次密码之后是“首次解锁后”（AFU），即使手机锁着也有部分数据没有加密，某些取证工具可能比较容易提取。

Apple 的安全性指南写明，iOS 18.1 与 iPadOS 18.1 起的“自动重启”由“安全隔区”（芯片里专门处理密钥的独立子系统）监控设备的解锁事件，设备长时间处于锁定状态就会自动重启。重启会让设备从 AFU 转为 BFU，并从内存清除敏感的安全密钥和瞬态数据。iOS 18.4 起，管理员可以打开或关闭这项机制，受监督设备（公司或学校通过设备管理统一设置的 iPhone）默认关闭。Apple 的文件没有写出要锁定多久，研究者 2024 年 11 月的实测是 72 小时，TechCrunch 当时的报道也写到 Magnet 确认了这个数字。

Privacy Guides 转述视频的说法，Evidence Preservation Mode 会在 AFU 状态“捕捉”iPhone，重启之后 AFU 状态也不会消失。据 TechSpot 的转述，视频里的员工说，Graykey 在取得初步访问、进入保存状态之后会关闭手机的无线电（Wi-Fi、蓝牙与移动网络）。员工也说 Graykey Preserve 能保留缓存的位置数据、最近删除的照片与 iMessage，这些数据原本会在一段时间后清除。据 Privacy Guides 的转述，视频没有说明技术细节。

Magnet 官网的 Graykey 产品页到 10 月 7 日为止写到，Graykey 能保护数据提取不受自动重启计时器影响。同一页对 Graykey Preserve 的说明只提到 iOS。

## 导读观点 {#perspective}

2024 年的逆向分析写到，窃贼没有资源在三天内取得最新的破解手法，自动重启很可能让他们完全取不到数据。同一篇也写到，执法部门因此多了时间压力。Magnet 的说法如果属实，取得初步访问并开始保存的手机，72 小时到期时 AFU 状态也不会消失。

本文引用的来源都没有写到普通用户能做什么来挡下 Magnet 的手法。据 iPhone 使用手册，开机或重启之后一律要输入密码。本文从 BFU 的定义推论，关机之后再开机的手机会处于 BFU，担心手机被扣押取证的人因此可以在手机可能离开自己身边之前关机。视频没有说明 Magnet 的手法能不能用在已经是 BFU 的手机。

据视频的说法，保存开始之后即使断电，AFU 状态也不会消失。关机的代价是期间收不到电话与消息，手机在使用中被拿走时也来不及关机。

中国大陆办理刑事案件时，手机扣押之后的封存方式有明文规定。最高人民法院、最高人民检察院与公安部 2016 年的规定，以及公安部 2019 年施行的《公安机关办理刑事案件电子数据取证规则》，都把信号屏蔽、信号阻断或者切断电源列为封存措施。两份规定都没有提到 iPhone，切断电源只是并列的措施之一。

公安部 2026 年 5 月公开征求意见的《公安机关电子数据取证规则（征求意见稿）》修订的是 2019 年施行的规则，封存手机的措施列出信号屏蔽、信号阻断等，没有列出切断电源。起草说明列出的修订背景没有提到封存措施的改动，到 10 月 7 日为止本文也没有查到定稿。

据新华社的报道，征求意见稿明确了确需输入与案件相关的智能终端等账号密码、持有人又不提供时的程序。此时公安机关采取措施获取账号密码，需经县级以上公安机关负责人批准，并明确告知持有人或者有见证人见证。持有人不提供账号密码，又不立即提取数据可能造成灭失等严重后果时，征求意见稿允许先行采取措施获取账号密码。先行采取措施之后，须在 24 小时内补办批准手续。

Apple 的“密码”说明写到，攻击者即使取得设备，在没有密码的情况下也无法访问某些特定保护类的数据。同一份说明也写到密码越长强度越高，更容易阻止暴力破解攻击。与较短的字母数字密码相比，较长的数字密码可能更容易输入，而且可以提供类似的安全性。这份说明没有谈到密码长度对 Magnet 手法的影响。

在“设置”的“面容 ID 与密码”（或“触控 ID 与密码”）轻点“更改密码”，再轻点“密码选项”就能更换。iPhone 使用手册把“自定义字母数字密码”与“自定义数字密码”列为最安全的选项。长密码的代价是开机或重启之后，以及超过 48 小时没有解锁时，都要输入较长的字符串。

Magnet 所说的手法跟执法部门扣押手机之后的取证有关，没有手机被扣押顾虑的人不必改变设置。据 Apple 的安全性指南，受监督的 iPhone 默认不启用自动重启，使用这类手机的人不能假设有 72 小时的保护。

Apple 的“Apple 安全性发布”页面写明，在进行调查并全面推出修补程序或发行版之前，Apple 不会透露、讨论或确认安全性问题。到 10 月 7 日为止，Magnet 的手法对最新版 iOS 是否有效并不清楚。11 月可以回头看 iOS 的更新说明有没有相关修补，以及有没有研究者独立验证。
