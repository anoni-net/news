---
title: eMudhra 弱私钥事件的后续处置与 macOS 命令行工具
description: 印度证书颁发机构 eMudhra 八张中间证书的私钥被算出之后，Apple、Microsoft 与 Chrome 都已封锁或移除相关证书，一般用户的浏览器、手机与电脑不必另外设置。macOS 内置的 git、curl 等命令行工具仍可能接受这些证书，到 11 月 2 日还没有查到 Apple 的修复。eMudhra 宣布退出公开 TLS 证书业务，到 11 月 1 日还没在事故单提交正式事故报告。
date: 2026-11-03T00:05:00+08:00
slug: emudhra-key-compromise-followup
categories:
  - security
follows:
  - 2026-10-23-emudhra-weak-ca-keys
sources:
  - title: About the compromised eMudhra intermediate CAs
    url: https://support.apple.com/en-us/149555
    publisher: Apple
    date: 2026-10-29
  - title: "MC1529467 - Microsoft Windows: Updates to address compromised eMudhra certificate authority keys"
    url: https://mc.merill.net/message/MC1529467
    publisher: Microsoft 365 Message Center Archive
    date: 2026-10-28
  - title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
    publisher: Mozilla Bugzilla
    date: 2026-10-18
  - title: eMudhra Statement on Recent Certificate Security Incident
    url: https://emudhra.com/en/post/certificate-security-incident
    publisher: eMudhra
    date: 2026-10-20
  - title: Protecting Chrome and Android Users from Compromised eMudhra Intermediate CA Certificates
    url: https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/
    publisher: Google
    date: 2026-10-20
  - title: root_store.textproto
    url: https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.textproto
    publisher: Chromium
  - title: Apple's git still trusts the compromised eMudhra certificates
    url: https://emudhra.we-have-a-problem.com/apple.html
    publisher: emudhra.we-have-a-problem.com
    date: 2026-10-28
  - title: eMudhra Intermediate CA Compromise
    url: https://emudhra.we-have-a-problem.com/
    publisher: emudhra.we-have-a-problem.com
    date: 2026-10-20
  - title: Microsoft releases out-of-band Windows fixes with certificate updates
    url: https://www.theregister.com/a/5305637
    publisher: The Register
    date: 2026-10-27
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
    date: 2026-11-01
authors:
  - anoni-net
---

印度证书颁发机构 eMudhra（证书品牌 emSign）有八张中间证书的私钥小到可以直接算出，取得私钥的人能替不属于自己的网站签发 HTTPS 证书。10 月中事件公开之后，Apple 与 Microsoft 陆续公布了各自的处置，Chrome 的信任列表也拿掉了相关的根证书。一般用户的浏览器、手机与电脑不必另外设置。依 Apple 10 月 29 日的支持文档，macOS 内置的 git、curl 等命令行工具在之后的软件更新之前，仍可能接受这些证书。

依 Apple 的支持文档，Apple 从 10 月 19 日起封锁六张签发 TLS 证书的中间证书。每张中间证书各有两份证书，一份连到 eMudhra 的根证书 emSign ECC Root CA - G3，另一份经 Sectigo 交叉签名（另一家证书颁发机构的根再签一份，让同一张中间证书多一条信任路径）连到 Sectigo 的根 AAA Certificate Services。Apple 封锁的是这 12 份证书，10 月 23 日起也封锁了 G3 根。封锁通过证书配置数据自动送到设备，不必安装软件更新，Safari、Mail 与使用 Apple 网络和安全框架的 App 都会拦下。

同一份文档也提到，macOS 与 Xcode Command Line Tools 附带的 curl、git、python3、ruby、perl 与 openssl，会拿 `/etc/ssl/cert.pem` 这个文件验证证书。证书连到文件里的根时，这些工具不检查 Apple 的封锁，也不检查证书有没有被吊销。Apple 写这个文件会在之后的 macOS 更新里更新，没有写是哪个版本、什么时候推出。

一位 Mozilla 工程师为事件搭建了说明页，10 月 28 日另外写了一页谈 Apple 的工具。依该页，10 月 26 日推出的 macOS 27.2 没有修复问题，还让用户手动移除根证书的处理失效。位于连接路径上的攻击者可以让 git 从 `https://` 远程取得攻击者挑的代码，也能拦截 GitHub token 这类登录信息。到 11 月 2 日，本文没有查到 macOS 27.2 之后的修复版本。

Microsoft 10 月 28 日在 Microsoft 365 消息中心的公告提到，Windows 的不信任证书列表（Disallowed Certificate Trust List）已经封锁受影响的证书颁发机构。Edge 与 WebView2（Windows App 内嵌网页用的组件）另外通过组件更新收到 CRLSet，也就是在后台下载的封锁列表，不必安装新版浏览器。公告也写到 Microsoft 已发布 Windows 与 Edge 的更新，从信任列表移除这些证书层级的相关证书，没有写 Edge 的日期。

依 Microsoft 消息中心的公告与 The Register 引述的 Microsoft 安全响应中心（MSRC）博客，Microsoft 10 月 26 日发布 Windows 的带外更新（out-of-band，例行更新以外的更新），从 Windows 的信任列表移除七张跟受影响证书层级相关的证书。这份更新给无法连到 Microsoft 证书更新服务、或停用自动更新信任列表的设备，也带着 10 月 13 日更新的已知问题。证书列表通常经由更新服务送达，很多设备不需要这份更新。

Google 10 月 20 日的博客预告，Chrome Root Store 会在太平洋时间 10 月 27 日上午移除 emSign ECC Root CA - G3。本文查不到 Chrome 宣告完成的公告，11 月 2 日读到的 Chromium 源代码里，Chrome Root Store 的列表已经没有这张根。eMudhra 的另一张根 emSign Root CA - G1 仍在列表上，Mozilla 10 月 20 日也在事故单上写当时不移除对 G1 的信任。Google 10 月 20 日的博客写正在评估 eMudhra 其他证书是否继续信任，到 11 月 2 日本文没有查到结果。

Chrome 根证书计划（Chrome Root Program）10 月 27 日在事故单上回复社区的提问，把 CRLSet 的封锁与事故单结案称为紧急遏制，之后还有后续的工作。依这则留言，Chrome 在通报后一小时内用 Google 的 `paranoid_crypto` 检查了 Chrome 信任的所有 CA 证书，没有找到其他已知类型的弱密钥。业界常用的检查工具在事件之前，没有检查椭圆曲线私钥过小的情况。Chrome 已在 CCADB（各家浏览器共用的证书颁发机构数据库）的工具项目提出议题，要让 CA 披露证书之前先通过弱密钥检查。

eMudhra 10 月 25 日在事故单上宣布退出公开 TLS 证书业务，10 月 30 日任命 KPMG 为独立的外部审查者。依 eMudhra 的事件声明页，领导层 10 月 26 日的说明写问题出在自家的脚本错误，并承诺通过 CCADB 的程序公布完整的根本原因分析。10 月 28 日的更新写到，G3 底下约 3 万 800 张证书属于美国的单一客户生态系统，这个生态系统已改用 eMudhra 的 G1 RSA 根签发新证书。eMudhra 也请各家根证书计划给时间让这批客户迁移，迁移完成后就停止从 G1 签发 TLS 证书。

Mozilla 根证书计划 10 月 20 日向 eMudhra 寄出问题清单，要求 24 小时内初步回复，到 10 月 23 日还没收到。eMudhra 10 月 23 日把延迟归因于社交媒体与投资人、客户的密集关注，Chrome 根证书计划回复这不是可以接受的理由。eMudhra 10 月 25 日的留言主张，CCADB 的事故通报规定给 CA 14 天提交完整报告，自己仍在期限内。

之后 eMudhra 在 10 月 27 日的留言写已经直接回复 Mozilla 的问题，10 月 29 日在事故单附上给 Google 的回复文档。到 11 月 1 日事故单的最后一则留言为止，eMudhra 还没有在这张单上提交正式事故报告，事故单的状态仍是处理中。

## 导读观点 {#perspective}

Chrome 的 CRLSet、Apple 的证书配置数据与 Windows 的不信任证书列表都在后台自动更新，可以单独拦下特定的中间证书。macOS 内置的命令行工具只读 `/etc/ssl/cert.pem` 一个文件，文件里还有 G3 根与 Sectigo 的 AAA Certificate Services，连到这两张根的证书就会通过验证。Apple 的文档写这些工具不检查吊销，所以 eMudhra 在 UTC 10 月 18 日吊销八张中间证书，对它们没有作用。

依一位研究者 10 月 25 日在事故单上的统计（本文没有另外核对），UTC 10 月 20 日到 21 日之间有 107,107 张用其中六把密钥签出的证书，被记进一家厂商的证书透明度日志（CT log，公开记录每一张证书的日志）。其中 106,050 张是只写 google.com 的概念验证证书，106,058 张经由 Sectigo 的 AAA 交叉签名连到根。这位研究者列出的例子里有一张内嵌了三家日志的收录证明（SCT），三家都是 Chrome 列为可用的日志，本文据此推论只要求 CT 收录证明拦不下这类证书。这些证书几乎都没有吊销信息的指针，只检查网站证书本身吊销状态的程序也拦不下，只有逐层检查 CA 证书吊销、收到推送的封锁列表或已移除相关根证书的程序会拒绝。

依 Apple 的文档，不用终端的人不需要做任何事，在 Mac 上用内置的 git、curl 或 python3 连 `https://` 网址的人可以等 Apple 的更新。不想等的人可以依同一份文档，用管理员权限从 `/etc/ssl/cert.pem` 移除 emSign ECC Root CA - G3。只移除 G3 拦不下 Sectigo 交叉签名的那六份，需一起移除 AAA Certificate Services。依同一份文档，代价是经由这张根、跟事件无关的部分网站，也可能在这些工具里验证失败。

Apple 的文档另外提醒，macOS 更新可能换回原本的文件。安装到含修复的版本之前，每次更新后都要重新检查。自带根证书列表的 App 与工具不读这个文件，也不套用 Apple 的封锁，要向开发者确认。在 Mac 上手动移除根证书，保护到的只有读这个文件的工具。

研究者说明页的「谁已修复」清单把 OpenHarmony 与 HarmonyOS NEXT 列为尚未修复（这份清单由研究者维护，不是华为发布的，本文没有查到华为的公告）。页面写这类设备不允许用户停用系统根证书，修复版本发布之前用户端没有变通办法。HarmonyOS 4.3 及更早版本，页面写可以像其他基于 Android 的系统一样停用系统内置的根证书。我们没有查到中国的政府或企业网站使用过受影响的 eMudhra 证书。

Google 的封锁经由 Google Play 服务的更新渠道送到许多 Android 设备，说明页提醒部分设备不允许用户停用系统根证书。GreatFire 的量测显示 `https://play.google.com` 在中国大陆到 2026 年 11 月 1 日的最后一次测试是 100% 被封锁。这项量测只看网址能否连线，不能确定设备是否收得到更新，本文据此推论在中国大陆没有 Google Play 服务的 Android 设备可能收不到这一份封锁。说明页给了手动停用两张根证书的步骤，部分设备不允许停用时无法手动处理。

接下来可以留意 Apple 修复 `/etc/ssl/cert.pem` 的 macOS 更新、eMudhra 依 CCADB 程序提交的正式事故报告，以及各家根证书计划对 G1 根的决定。约 3 万 800 张证书所属的客户生态系统已经改用 G1 签发。本文推论，G1 是否继续被信任，会影响这批网站多久之后要再换一次证书。
