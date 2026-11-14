---
title: eMudhra 证书事件的事故报告、macOS 修复版与 G1 根的期限
description: 印度证书颁发机构 eMudhra 的弱私钥事件在 11 月有三项进展。Apple 11 月 9 日推出 macOS 27.2.1、26.7.3 与 15.8.3，修复内置的 git、curl 等命令行工具。在 Mac 上用这些工具的人要更新系统，其他人不必另外设置。eMudhra 11 月 10 日提交事故报告，交代 11 月 7 日另外吊销的八张 RSA 中间证书。依 11 月 14 日读到的源代码，Chrome 与 Mozilla 不再信任 UTC 11 月 16 日之后签发、以 emSign Root CA - G1 为根的证书，Microsoft 排定同一天移除 Edge 与 WebView2 对 G1 的信任。
date: 2026-11-17T00:00:00+08:00
slug: emudhra-incident-closeout
categories:
  - security
follows:
  - 2026-11-03-emudhra-key-compromise-followup
sources:
  - title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c82
    publisher: Mozilla Bugzilla
    date: 2026-11-10
  - title: About the compromised eMudhra intermediate CAs
    url: https://support.apple.com/en-us/149555
    publisher: Apple
    date: 2026-11-09
  - title: Apple security releases
    url: https://support.apple.com/en-us/100100
    publisher: Apple
  - title: "MC1529467 - Microsoft Windows: Updates to address compromised eMudhra certificate authority keys"
    url: https://mc.merill.net/message/MC1529467
    publisher: Microsoft 365 Message Center Archive
    date: 2026-11-11
  - title: "Moving Forward Together: InCommon Certificate Service Update"
    url: https://incommon.org/about/news/incommon-certificate-service-update
    publisher: InCommon
    date: 2026-11-10
  - title: eMudhra Statement on Recent Certificate Security Incident
    url: https://emudhra.com/en/post/certificate-security-incident
    publisher: eMudhra
    date: 2026-11-05
  - title: root_store.textproto
    url: https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.textproto
    publisher: Chromium
  - title: certdata.txt
    url: https://github.com/mozilla-firefox/firefox/blob/main/security/nss/lib/ckfw/builtins/certdata.txt
    publisher: Mozilla
  - title: eMudhra憑證事故擴大，再有8張RSA中繼CA憑證遭撤銷
    url: https://www.ithome.com.tw/news/180445
    publisher: iThome
    date: 2026-11-13
  - title: eMudhra Intermediate CA Compromise
    url: https://emudhra.we-have-a-problem.com/
    publisher: emudhra.we-have-a-problem.com
authors:
  - anoni-net
---

印度证书颁发机构 eMudhra（证书品牌 emSign）有八张中间证书的私钥可以直接算出，事件 10 月中公开之后，11 月有三项进展。Apple 11 月 9 日推出 macOS 27.2.1、26.7.3 与 15.8.3，修复内置的命令行工具，也更新了根证书列表文件 `/etc/ssl/cert.pem`。eMudhra 11 月 10 日在 Mozilla 的 Bugzilla 事故单 2083449 提交完整事故报告。Chrome 与 Mozilla 对 eMudhra 的另一张根证书 emSign Root CA - G1 设下日期限制，Microsoft 则排定移除 Edge 与 WebView2（Windows App 内嵌网页用的组件）对它的信任。

在 Mac 上用内置的 git、curl、python3 等工具连 `https://` 网址的人，要把系统更新到上述其中一个版本，其他人不必另外设置。依 Apple 的支持文档，Safari、Mail 与使用 Apple 网络和安全框架的 App 早已自动封锁受影响的证书，不必安装更新。依 Microsoft 的公告，Edge 与 WebView2 的相关更新通过组件推送。

依 Apple 11 月 9 日改版的支持文档，从 macOS 27.2.1 起，macOS 与 Xcode Command Line Tools 附带的命令行工具也会拦下受影响的 12 份中间证书。10 月吊销的八张 ECDSA 中间证书里有六张是 TLS 用的中间证书，每张各有两份证书，合计 12 份。两份分别连到 eMudhra 的根 emSign ECC Root CA - G3，以及经 Sectigo 交叉签名连到 AAA Certificate Services。更新同时从 `/etc/ssl/cert.pem` 移除五张根证书，包括这两张根与 emSign Root CA - G1，macOS 26 与 macOS 15 对应的修复版是 26.7.3 与 15.8.3。

依事故报告，eMudhra 在 11 月 7 日吊销八张 RSA-4096 的中间证书（G2B 与 G2C 系列）。加上 10 月 18 日吊销的八张 ECDSA 中间证书，受影响的中间证书共 16 张。11 月 7 日填的吊销理由是停止营运（`cessationOfOperation`），前一批 ECDSA 中间证书填的是 CA 私钥泄露（`caCompromise`）。

依报告，八把 RSA 私钥没有弱私钥的问题，签名都对得上证书里的公钥。16 把密钥在 2025 年 4 月 30 日的同一场密钥生成仪式建立，导入时私钥材料经过主机上一支 Python 程序的内存，离开了硬件安全模块（HSM，专门生成与保管私钥的硬件）。eMudhra 因此无法证明这批私钥的处理符合自家证书实践声明（CPS，证书颁发机构公开承诺的作业规范）对私钥转移的规定。报告写 RSA 的问题是在 11 月初、根证书计划讨论这条规定之后确认，没有写是哪一家计划，也没有写吊销是否出于对方要求。

报告没有写有人取得 RSA 私钥的证据，对整起事件的说法是没有已知的滥用案例。报告提交当天有人在事故单上留言，问既然无法证明私钥的处理合规，吊销理由为何不用私钥泄露（`keyCompromise`）。到 11 月 14 日，事故单上没有 eMudhra 对这则提问的回复。

依报告的附录，八张里有六张是 TLS 用的中间证书（颁发者 emSign Root TLS CA - G1），另外两张是代码签名用的中间证书（颁发者 emSign Root CS CA - G2）。两种中间证书各有 G2B 与 G2C 版本，G2B 的四张没有签发过终端证书。G2C 的四张 5 月起在美国投入使用，签发过网站证书与代码签名证书。G2C 最后一次签发在 11 月 3 日，报告写终端证书已经迁移或换发。

依 eMudhra 10 月 28 日的更新，约 3 万 800 张 G3 证书所属的美国客户生态系统，已改由 eMudhra 的 G1 RSA 根签发。事故报告把 G1 层级的主要服务对象写成北美的一个大学联盟。本文对照 10 月 28 日的更新与事故报告推论，那条 G1 RSA 通道包含这次吊销的 G2C 中间证书，两份文档都没有直接写出。报告列的 TLS 中间证书颁发者是 emSign Root TLS CA - G1，它与 emSign Root CA - G1 的关系，本文没有查到第一手资料。

InCommon（美国大学与研究机构的证书服务）11 月 10 日的公告写，自家目前经 G1 签发的证书颁发机构已无法再取得公开信任（"Our current G1 issuing Certificate Authority (CA) is no longer viable for public trust"）。同一页之后的更新写签发已从 emSign 改到 SSL.com，并请各机构在 11 月 16 日当天结束前换掉受影响的证书。InCommon 是否就是报告里的大学联盟，报告没有写名称，本文依两者的描述推论是同一个客户。

eMudhra 的报告写 G1 层级的所有签发在 11 月 16 日前停止，报告 11 月 10 日提交时，这一项列为进行中。本文 11 月 14 日读到的 Chromium 与 Firefox 源代码，都对 emSign Root CA - G1 设了日期限制。UTC 11 月 16 日 23:59:59（台北时间 11 月 17 日 07:59:59）之后签发的证书不再信任，之前签发的仍信任。本文没有查到 Chrome 与 Mozilla 针对 G1 的公告，源代码也没有写正式版何时带上这项设置。

Microsoft 11 月 11 日更新的公告写，11 月 16 日推出组件更新，Edge 与 WebView2 收到后移除 G1 在内四张 eMudhra 根的默认信任。到 11 月 14 日，本文没有查到这项更新推出的结果。

## 导读观点 {#perspective}

照 11 月 14 日的源代码设置，Chrome 的限制看证书记进证书透明度日志（CT log，公开记录每一张证书的日志）的时间，Mozilla 的列表也设了同一天的期限。设置生效后，已经发出的证书可以用到过期，期限之后的新证书不被接受。Microsoft 为 Edge 与 WebView2 预定的更新则直接拿掉 G1，macOS 命令行工具更新后也一样，连到 G1 的网站证书不论何时签发都可能无法通过验证。本文据此推论，还没换掉 G1 证书的网站可能在 Chrome 正常打开，在 Edge 或 Mac 的 curl 里验证失败。

依 eMudhra 11 月 5 日更新的事件声明，Apple 预定在 11 月 30 日移除并不再信任 G1 根，G1 底下任何时间签发的证书都不再被 Apple 的平台信任。InCommon 11 月 10 日的公告也转述了这个日期。到 11 月 14 日，Apple 11 月 9 日改版的支持文档没有写这个日期，只写了 `/etc/ssl/cert.pem` 移除 G1。

前篇提到，不想等更新的人可以依 Apple 的步骤，从 `/etc/ssl/cert.pem` 手动移除 G3 与 AAA Certificate Services。依同一份支持文档，更新到 27.2.1、26.7.3 或 15.8.3 之后就不必再重做这些步骤。照 Apple 步骤操作时留下的备份文件 `/etc/ssl/cert.pem.orig` 可以用 `sudo rm` 删掉，也不要还原更新前做的备份。更新后的文件少了五张根，Apple 提醒只读这份文件的工具，可能无法验证部分证书连到这些根的网站。

研究者维护的说明页（不是华为或 Google 的公告）11 月 14 日的清单，仍把 OpenHarmony 与 HarmonyOS NEXT 列为尚未修复，写这类设备不允许用户停用系统根证书。同一页的 Android 段落写，没收到更新后封锁列表的设备也许能在受信任凭据里停用相关根证书，但步骤只列 emSign ECC Root CA - G3 与 AAA Certificate Services 而没有 G1。上述清单对应 G3 与 ECDSA 中间证书，页面没有提到 RSA 中间证书与 G1。中国与香港的系统和浏览器如何处理 RSA 吊销，本文没有查到。

需要更新的命令行工具包括内置的 git、curl、python3、ruby、perl 与 openssl。无法更新到上述版本的 Mac，可以照 Apple 支持文档的步骤从 `/etc/ssl/cert.pem` 手动移除根证书，需要管理员账号。自带根证书列表的 App 与工具不读 `/etc/ssl/cert.pem`，也不套用 Apple 的封锁。系统更新保护不到这些工具，要向开发者确认。

只用 Safari、Mail 与使用 Apple 框架的 App 的人不需要做任何事。接下来可以留意 eMudhra 预定 12 月 4 日完成的 KPMG 独立审查、Apple 是否在 11 月 30 日对 G1 有所处置，以及到 11 月 14 日只设了日期限制的 Chrome 与 Mozilla，之后会不会把 G1 整个移出信任列表。
