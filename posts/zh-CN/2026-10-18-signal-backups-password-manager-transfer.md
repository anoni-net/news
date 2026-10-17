---
title: Signal 的跨平台加密备份与 Android 的密码管理器迁移
description: Signal 9 月 28 日发布 iOS 8.30，加密备份 Signal Secure Backups 可以在 Android 与 iPhone 之间恢复，换手机时能把聊天记录带到另一个平台。Google 9 月在 Android 推出密码管理器之间的迁移流程，不必导出文件，公告列出四款支持的密码管理器。
date: 2026-10-18T12:00:00+08:00
slug: signal-backups-password-manager-transfer
categories:
  - mobile
sources:
  - title: "Back to Backups: A Year in Review"
    url: https://signal.org/blog/backup-improvements/
    publisher: Signal
    date: 2026-09-28
  - title: Signal Secure Backups
    url: https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backups
    publisher: Signal
  - title: Signal 安全備份
    url: https://support.signal.org/hc/zh-tw/articles/9708267671322
    publisher: Signal
  - title: Backups and Device Transfers on Signal
    url: https://support.signal.org/hc/en-us/articles/10074659364122-Backups-and-Device-Transfers-on-Signal
    publisher: Signal
  - title: Troubleshooting Signal Secure Backups
    url: https://support.signal.org/hc/en-us/articles/10075139325850-Troubleshooting-Signal-Secure-Backups
    publisher: Signal
  - title: iOS to iOS Device Transfer
    url: https://support.signal.org/hc/en-us/articles/10045771316762-iOS-to-iOS-Device-Transfer
    publisher: Signal
  - title: Switching password managers is easy and safe on Android
    url: https://blog.google/products-and-platforms/platforms/android/switch-password-managers/
    publisher: Google
    date: 2026-09-10
  - title: Credential transfer
    url: https://developer.android.com/identity/sign-in/credential-transfer
    publisher: Android Developers
  - title: Import or export passwords and passkeys with Chrome
    url: https://support.google.com/chrome/answer/13068232?co=GENIE.Platform%3DAndroid
    publisher: Google
  - title: Android offers password manager switching tool
    url: https://freedom.press/digisec/blog/android-offers-password-manager-switching-tool/
    publisher: Freedom of the Press Foundation
    date: 2026-09-16
  - title: "Password managers on Android: Switch without manual export"
    url: https://www.heise.de/en/news/Password-managers-on-Android-Switch-without-manual-export-11450892.html
    publisher: heise online
    date: 2026-09-11
  - title: Credential Exchange Format
    url: https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html
    publisher: FIDO Alliance
    date: 2025-08-14
  - title: ASCredentialExportManager
    url: https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager
    publisher: Apple
  - title: What’s new in passkeys
    url: https://developer.apple.com/videos/play/wwdc2025/279/
    publisher: Apple
    date: 2025-06-09
  - title: Export passwords to another password manager on iPhone
    url: https://support.apple.com/guide/iphone/export-passwords-iphf28f2e93e/ios
    publisher: Apple
  - title: Is https://signal.org blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/signal.org
    publisher: GreatFire
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
authors:
  - anoni-net
---

Signal 9 月 28 日发布 iOS 8.30，博客写明从这一版起，加密备份可以在 Android、iOS 与桌面版之间创建与恢复。支持中心写明 Signal Secure Backups 能在 Android 与 iPhone 之间恢复，换手机时可以把聊天记录带到另一个平台。Google 9 月 10 日也在 Android 推出密码管理器之间的迁移流程，密码与通行密钥（passkey，取代密码的登录方式）可以直接迁移到另一款 App，不必先下载成文件。公告写明 Android 8 以上可用，列出 Google 密码管理工具、1Password、Bitwarden 与 Dashlane 四款，之后还会增加。

Signal Secure Backups 由 Signal 托管，开启时会生成一组 64 个字符的恢复密钥（recovery key），支持中心写明这组密钥不会交给 Signal 的服务。密钥丢失就再也无法恢复备份，Signal 也无法协助找回。到 10 月 18 日为止，免费方案备份全部文字消息与最近 45 天的媒体文件，每月 1.99 美元的付费方案可以存到 100 GB 的媒体。只能查看一次的消息，以及 24 小时内就会消失的消息，都不会备份。

博客写明托管的备份每 24 小时生成一份新的，前一份自动删除。支持中心写明，备份只能在第一次设置 Signal 时恢复，而且要用同一个电话号码注册。

新旧两部手机都在手边、又是同一个平台时，也可以用设备间迁移。聊天记录会从旧手机移到新手机，旧手机不保留。博客写明 iOS 8.30 改用 Wi-Fi Aware 在两部 iPhone 之间建立端到端加密的本地连接，速度与稳定性都有提高。

另一种是存在自己设备上的备份文件，博客写 Android、iOS 与桌面版都能创建，格式跨平台。到 10 月 18 日为止，支持中心各页的写法跟博客不同，彼此也不一致。10 月 11 日更新的备份与迁移说明页写三个平台都有、但只能在同一个平台恢复，10 月 3 日更新的故障排除页则写只限 Android 之间。备份与迁移说明页和桌面版备份页都写明，Android 或桌面版的备份文件不能在 iPhone 恢复。

Google 的公告写明，Android 的密码迁移从新的密码管理器开始，在新 App 选择从其他服务导入。Android 会列出手机上可以导出的密码管理器，用户接着在旧的那款里选择要迁移的项目并授权。Google 的开发者文档写明，迁移在同一部手机的两个 App 之间进行，原始凭据不会暴露给 Android 系统或未经验证的 App。文档也写明采用 FIDO 联盟（制定通行密钥等登录标准的产业组织）的凭据交换格式（Credential Exchange Format，CXF），密码、通行密钥、地址与自定义字段都能迁移。

Apple 在 iOS 26 与 macOS 26 为密码管理器的开发者提供同类的导出与导入 API，开发者文档写明由操作系统居中确认双方 App 的身份，过程不写入任何文件。WWDC25 的开发者讲座写明，数据格式是跟 FIDO 联盟的成员合作制定。Apple 支持网站的 iPhone 使用手册里，密码导出与导入的两页到 10 月 18 日为止都只写 CSV 文件的做法，导出页并警告导出的密码没有加密。

## 导读观点 {#perspective}

Signal 的备份由用户手上的恢复密钥加密，支持中心写明没有这组密钥，包括 Signal 在内都无法读取或恢复备份。iCloud 备份也带不走 Signal 的聊天记录，支持中心写明 iCloud 备份跟 Signal 不兼容。

Signal Secure Backups 另外加了一把每天更换的辅助密钥，存放在 Signal 托管服务那一端的可信执行环境（TEE，处理器里隔离出来的安全区）。博客写明这把密钥没有恢复密钥就解不开备份，唯一的用途是提供前向保密（forward secrecy，日后密钥泄露时，过去的数据仍无法被解开）。存在自己设备上的备份，博客写明无法用同一套 TEE 提供前向保密。博客也写明，TEE 是目前保护这把密钥最好的方式，之后可能随研究进展而改变。

Google 的公告写明，以前迁移密码要先下载成没有加密的文本文件，通行密钥则完全无法迁移。Apple 的开发者文档写明，新的迁移过程不写入文件系统。Android 的开发者文档写明，两个 App 之间用受保护的内容 URI（Content URI）传递，背后是临时的缓存文件。文档写的理由是整个密码库可能超过 Android 进程间单次传输 1MB 的上限。

密码能不能整个迁移过去，heise 的报道写明要看新旧两个 App 是否都实现了这套标准。Google 的帮助页写明，导入到 Google 密码管理工具时要登录另一款密码管理器，导入通行密钥时可能还要输入恢复密钥。帮助页也提醒，导入前要确认信任对方的密码管理器。

在中国大陆，第三方测量项目 GreatFire 到 10 月 11 日的测试显示，`signal.org` 与 `play.google.com` 两个网站都被完全封锁。GreatFire 测的是网址能否连上，不是 Signal App 的消息连接。Android 的开发者文档写明，这套迁移流程对调用方的检查以 Google Play 服务的系统组件为准，文档没有写没有 Google Play 服务的手机能否使用。

打算换手机的 Signal 用户，可以在旧手机的 Signal 设置里开启备份，把恢复密钥保存好再换机。密钥可以存进密码管理器或手动保存，存进密码管理器的人，换机时要能在新手机或其他设备打开密码管理器（本文依设置流程推论）。Signal Secure Backups 保护的是手机丢失或换平台时的聊天记录，换电话号码时无法恢复，博客也提醒恢复密钥不要交给任何人。

想在 Android 换一款密码管理器的人，打开新的 App 找导入的选项，新旧两款都要支持这套流程。Google 9 月 10 日的公告列出的是 Google 密码管理工具、1Password、Bitwarden 与 Dashlane。导入到 Google 密码管理工具时，Google 的帮助页写明要用手机的屏幕锁定验证身份。iPhone 用户用 CSV 文件迁移时，Apple 的使用手册警告导出的文件没有加密，任何取得文件的人都能读到内容。
