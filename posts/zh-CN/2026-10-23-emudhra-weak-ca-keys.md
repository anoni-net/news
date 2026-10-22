---
title: eMudhra 八张中间证书的弱私钥事件
description: 印度证书机构 eMudhra 有八张中间证书的私钥小于 256，任何人都能立刻算出来，再用来替别人的网站签发 HTTPS 证书。研究者 10 月 17 日通报后，Chrome 与 Firefox 在几个小时内自动封锁，一般用户的浏览器不必另外设置。不经过浏览器的程序各自带着信任列表，Node.js、Python 的 certifi、Go、Java 与 Linux 发行版从 10 月 19 日起陆续推出更新（到 10 月 22 日还没全部完成），自行写程序或维护服务器的人要逐一更新。
date: 2026-10-23T00:00:00+08:00
slug: emudhra-weak-ca-keys
categories:
  - security
sources:
  - title: Compromised eMudhra Intermediate Certificates
    url: https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE
    publisher: Mozilla dev-security-policy
    date: 2026-10-20
  - title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
    publisher: Mozilla Bugzilla
    date: 2026-10-18
  - title: Protecting Chrome and Android Users from Compromised eMudhra Intermediate CA Certificates
    url: https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/
    publisher: Google
    date: 2026-10-20
  - title: eMudhra Statement on Recent Certificate Security Incident
    url: https://emudhra.com/en/post/certificate-security-incident
    publisher: eMudhra
    date: 2026-10-20
  - title: eMudhra Statement on distrust of select Global TLS Intermediate and one Root CA
    url: https://emudhra.com/en/press-release/emudhra-statement-distrust-global-tls-intermediate-root-ca
    publisher: eMudhra
    date: 2026-10-21
  - title: Wednesday, October 21, 2026 Security Releases
    url: https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
    publisher: Node.js
    date: 2026-10-21
  - title: "crypto/x509: mitigation for security concerns with a specific Certificate Authority"
    url: https://github.com/golang/go/issues/82345
    publisher: Go
    date: 2026-10-19
  - title: "OpenJDK Vulnerability Advisory: 2026/10/21"
    url: https://openjdk.org/groups/vulnerability/advisories/2026-10-21
    publisher: OpenJDK
    date: 2026-10-21
  - title: Bug #2171507 “ca-certificates update tracking bug” : Bugs : ca-certificates package : Ubuntu
    url: https://bugs.launchpad.net/ubuntu/+source/ca-certificates/+bug/2171507
    publisher: Launchpad
    date: 2026-10-20
  - title: 2556376 – Update to mitigate current issues with eMudhra
    url: https://bugzilla.redhat.com/show_bug.cgi?id=2556376
    publisher: Red Hat Bugzilla
    date: 2026-10-20
  - title: FreeBSD-SA-26:73.caroot
    url: https://www.freebsd.org/security/advisories/FreeBSD-SA-26:73.caroot.asc
    publisher: FreeBSD
    date: 2026-10-21
  - title: eMudhra Intermediate CA Compromise
    url: https://emudhra.we-have-a-problem.com/
    publisher: emudhra.we-have-a-problem.com
    date: 2026-10-20
  - title: 8 eMudhra certificates are compromised. Here's what you need to know
    url: https://blog.cloudflare.com/emudhra-certificate-compromise/
    publisher: Cloudflare
    date: 2026-10-20
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
authors:
  - anoni-net
---

印度的证书机构 eMudhra（证书品牌 emSign）有八张中间证书的私钥简单到可以直接算出来。中间证书位于根证书之下，是实际用来签发网站证书的那一层。一位研究者在 UTC 10 月 17 日 18:05（北京时间 10 月 18 日 02:05）通报 Apple、Chrome、Microsoft、Mozilla 与 eMudhra，附上用八把私钥各自签出的证明。依 Mozilla 10 月 20 日在 dev-security-policy 邮件列表的帖子，取得私钥的人可以替自己不拥有的网站签发 HTTPS 证书。

Chrome 与 Firefox 在通报后几个小时内就用自动推送的封锁列表挡下六张 TLS 中间证书，多数用户不必更新或重启浏览器。受影响比较大的是不经过浏览器的程序，例如用 Node.js、Python、Go 或 Java 写成的工具与服务器，各自要等更新才会停止信任。Mozilla 10 月 20 日在事故单上补充，已经有好几个人各自算出私钥，其中有些人公开了这件事。

依 Mozilla 工程师在 Bugzilla 事故单的初步分析，八把都是 P-384 椭圆曲线的私钥，本来应该是一个随机挑选、长达 384 位的整数。实际的值却都小于 256，依次试过 256 个数字就能找出来。八张里有六张用来签发网站的 TLS 证书，受 Chrome、Mozilla、Microsoft 与 Apple 信任。另外两张用来签署代码，受 Microsoft 信任。

eMudhra 的声明写到，八张中间证书在 2025 年 4 月 30 日的密钥生成仪式上创建，问题经过约 18 个月、两次独立审计都没有被发现。依 eMudhra 在事故单上的初步说明，仪式使用的程序有缺陷，在原本的密钥之外多生成了一组弱密钥。两组密钥的标签相近，弱密钥被误用来申请证书。eMudhra 10 月 21 日更新的声明也提到，确切的根本原因还在调查。

依同一份声明，八张中有七张从没用在生产环境，正在使用的那一张没有签发过任何证书。eMudhra 也不知道有人在公开之前算出弱密钥的证据。依 Google 10 月 20 日的博客，封锁之前证书透明度（Certificate Transparency，CT，公开记录每一张证书的日志）里没有六张中间证书签出的网站证书。Chrome 默认只接受记入 CT 的证书，所以 Google 判断伪造证书骗不过 Chrome，也骗不过目标为最新 SDK 或自行启用 CT 检查的 Android App。

一位 Mozilla 工程师为事件架设的说明页另外提到，很多浏览器以外的程序不检查 CT。说明页也写到，从 2025 年 4 月证书创建起就有被滥用的可能，目前不知道攻击者有没有利用弱密钥攻击这些程序。

## 导读观点 {#perspective}

浏览器信任一个 HTTPS 网站，是因为网站的证书由一串证书机构逐层签署，最上层的根证书预先放在浏览器或操作系统的信任列表里。中间证书的私钥可以签出任何域名的证书。依 FreeBSD 10 月 21 日的安全公告，能拦截网络流量的攻击者可以用被算出的私钥冒充任何 TLS 服务器，读取或修改连接内容而不被发现。

Chrome 的 CRLSet 与 Firefox 的 OneCRL 都是浏览器在后台自动下载的封锁列表，可以单独挡下特定的中间证书。再加上 CT 的要求，Chrome 与 Firefox 这一端在通报当天就有两层保护。依 Mozilla 的发行说明与事故单，停用了自动下载列表（Remote Settings）的 Firefox 要更新到 158.0.1。部分 Android 版 Firefox 的配置文件没有在启动时应用列表，要更新到 158.0.2。

依 Bugzilla 事故单，eMudhra 在 UTC 10 月 18 日把八张中间证书标为吊销。依 Mozilla 在事故单上的说法，有些程序不读取吊销信息，或没有机制单独撤回特定的中间证书。NSS 是 Mozilla 维护的加密库，许多程序与发行版沿用它的根证书列表。为了保护前述的程序，Mozilla 在 10 月 20 日的 NSS 3.131.1 移除六张 TLS 中间证书往上连到的根证书 emSign ECC Root CA - G3。

Node.js 10 月 21 日的 22.23.4、24.22.1、26.12.1 换上了新列表，Go 也发布了 1.27.3 与 1.26.10。依说明页的修补列表，Python 的 certifi 2026.10.19 与 curl 的 CA bundle 也已更新。依 Ubuntu 的跟踪单，到 10 月 22 日为止 22.04、24.04、26.04 与 26.10 已发布 ca-certificates 的更新，20.04 以前的版本还没有。Fedora 已提交更新，依 Red Hat Bugzilla 的 bug 单，到 10 月 22 日为止这批更新仍信任签发两张代码签名中间证书的根证书。

依说明页的建议，一般用户尽快把浏览器与操作系统更新到最新版。依 Google 的博客，Android 设备在 UTC 10 月 19 日 22:00 前后（北京时间 10 月 20 日 06:00）通过 Google Play 服务收到同样的封锁。Google 写大多数 Android 设备已经收到，还没收到的重启就能马上应用。没有 Google Play 服务的 Android 设备不在 Google 这段说明的范围内，本文没有查到 Android 系统本身的更新。

依 GreatFire 的记录（本文 10 月 18 日查证），这个第三方测量项目在 10 月 11 日的最后一次测试显示 `play.google.com` 在中国大陆被完全封锁，2012 年 3 月 10 日起就有干扰记录。GreatFire 只测网址能否连上，没有测设备上的 Google Play 服务能否收到更新。依本文的推论，没有或连不上 Google Play 服务的 Android 设备不在 Google 那段说明的范围内，浏览器自行下载的 CRLSet 与 OneCRL 则不经过 Google Play 服务。说明页对一般用户的建议是把浏览器与系统更新到最新版，来源没有说更新对上述设备是否足够，本文也没有查证两份列表在中国大陆能否顺利下载。

自行写程序、维护服务器或在电脑上运行命令行工具的人，要更新的是各自的运行环境。Go 的修补在标准库的 `crypto/x509` 包，Go 程序编译时会把标准库打包进可执行文件，所以要用新版重新编译。Python 的 certifi 是单独安装的包，每个虚拟环境与容器各有一份，要分别更新。依说明页，macOS 内置的 curl、python3 等命令读取 `/etc/ssl/cert.pem` 时不检查吊销，到 10 月 22 日这个文件还没更新。

依 OpenJDK 10 月 21 日的公告，操作系统软件包提供的 Java 多半使用系统的证书，更新系统就够。自行安装的 Java，以及 FreeBSD 与 Homebrew 的软件包，要直接更新。

Cloudflare 的博客提醒，更新之后如果出现证书错误，不要用关闭证书验证的方式解决。说明页准备了用受影响的中间证书签发的测试网址，用 curl 连接出现证书错误，代表 curl 已经不信任这些证书。Cloudflare 的博客也写到，这类测试只代表测到的那个程序，使用其他验证方式的程序要分别确认。

移除根证书可以保护不读取吊销信息的程序，代价是部分正当网站的证书也跟着失效。eMudhra 在事故单上估计约 3 万张证书需要更换，声明写影响范围限于美国的单一客户生态系统。Chrome 在事故单上依到 10 月 21 日的 CT 数据统计，这个根证书下约 3 万 800 条还没过期的证书记录，有 99.9% 由 Internet2 与 InCommon 的两张从属中间证书签发。依 Google 的博客，Chrome 预计在太平洋时间 10 月 27 日上午从 Chrome Root Store 移除同一个根证书，也在评估 eMudhra 其他证书是否继续信任。

说明页写 Apple 设备从 10 月 19 日起封锁，Microsoft 平台从 10 月 20 日起封锁。到 10 月 22 日为止，本文没有找到两家自己的公告。依 Bugzilla 事故单，到 UTC 10 月 21 日深夜为止，eMudhra 还没有提交正式的事故报告。正式报告、eMudhra 对 Chrome 在事故单上所提问题的回复，以及 Chrome 对 eMudhra 其他证书的决定，是接下来可以留意的地方。
