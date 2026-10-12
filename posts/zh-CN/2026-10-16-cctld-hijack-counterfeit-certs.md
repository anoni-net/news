---
title: 国家代码顶级域名劫持事件与未经授权的 HTTPS 证书
description: Google 10 月 6 日公告，加纳、塞拉利昂与美属萨摩亚的国家代码顶级域名遭到劫持，攻击者取得 Google 与其他组织域名的 HTTPS 证书。Chrome 已拦截找到的证书，自己管理域名的人可以监控证书透明度日志。
date: 2026-10-16T00:05:00+08:00
slug: cctld-hijack-counterfeit-certs
categories:
  - security
regions:
  - GH
  - SL
  - AS
sources:
  - title: Chrome's Response to Recent ccTLD Registry Hijacks
    url: https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/
    publisher: Google
    date: 2026-10-06
  - title: Chrome's Response to Recent ccTLD Registry Hijacks
    url: https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941
    publisher: Let's Encrypt 社区论坛
    date: 2026-10-07
  - title: Hackers obtain counterfeit TLS certificates for Google and other large services
    url: https://arstechnica.com/security/2026/10/hackers-obtain-counterfeit-tls-certificates-for-google-and-other-large-services/
    publisher: Ars Technica
    date: 2026-10-06
  - title: Hackers Impersonate Google and Other Large Services With Counterfeit TLS Certificates
    url: https://www.privacyguides.org/news/2026/10/08/hackers-impersonate-google-and-other-large-services-with-counterfeit-tls-certificates/
    publisher: Privacy Guides
    date: 2026-10-08
  - title: 3個國碼頂級網域遭劫持，攻擊者取得Google等組織HTTPS憑證
    url: https://www.ithome.com.tw/news/179500
    publisher: iThome
    date: 2026-10-09
  - title: Attackers hijack ccTLDs to fake certs for Google
    url: https://www.itnews.com.au/news/attackers-hijack-cctlds-to-fake-certs-for-google-629504
    publisher: iTnews
    date: 2026-10-08
  - title: DNS Hijacks Across Three ccTLDs Linked to 32 Unauthorized HTTPS Certificates
    url: https://circleid.com/posts/dns-hijacks-across-three-cctlds-linked-to-32-unauthorized-https-certificates
    publisher: CircleID
    date: 2026-10-08
  - title: CRLSets
    url: https://www.chromium.org/Home/chromium-security/crlsets/
    publisher: The Chromium Projects
  - title: Certificate Transparency Monitoring
    url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/
    publisher: Cloudflare
  - title: Cert Spotter - Certificate Transparency Monitor - Detect Security and Availability Problems
    url: https://sslmate.com/certspotter/
    publisher: SSLMate
  - title: Certification Authority Authorization (CAA)
    url: https://letsencrypt.org/docs/caa/
    publisher: Let's Encrypt
  - title: 服务简介
    url: https://www.cnnic.net.cn/n4/2022/0901/c56-10201.html
    publisher: 中国互联网络信息中心
    date: 2026-04-09
authors:
  - anoni-net
---

Google 10 月 6 日公告，.gh（加纳）、.sl（塞拉利昂）与 .as（美属萨摩亚）三个国家代码顶级域名遭到劫持，攻击者借此取得多个 Google 域名与其他组织域名的 HTTPS 证书。国家代码顶级域名（ccTLD）是代表国家或地区的顶级域名，例如中国大陆的 .cn、台湾的 .tw。公告写明有风险的是以这三个代码结尾的域名，Google 自家的系统没有遭到入侵。Chrome 已拦截找到的证书，公告写明 Chrome 用户不必采取任何行动。

依 Google 的公告，攻击者入侵的是由第三方运营的这三个顶级域名，改动了权威 DNS 记录（决定一个域名该解析到哪里的那一份记录）。公告没有写攻击者从哪个环节入侵（例如运营机构的系统或注册商账号）、劫持从何时开始，到 10 月 12 日为止也查不到三个运营机构的说明。Ars Technica 的报道写明攻击者控制 DNS 记录之后通过了证书颁发机构的域名控制验证（DCV，确认申请者确实掌控域名的程序），iThome 写的是可能借此通过。Google 的公告写明没有理由认为签发证书的证书颁发机构做错了什么。

Google 先用 CRLSets（Chrome 紧急拦截特定证书用的清单）拦截 Google 域名的证书，并请签发的证书颁发机构吊销。之后从证书透明度（CT，公开记录每一张已签发证书的日志）找到可能受同一波攻击影响的其他组织，包括几个全球大型品牌与广泛使用的在线服务，也在 Chrome 拦截了这些证书。

Let's Encrypt 的工作人员在论坛确认，该机构签发过 Google 与 YouTube 的证书，已经吊销。澳大利亚媒体 iTnews 自行比对 CT 日志与 Chrome 的拦截清单，找到 9 月 22 日到 27 日之间发给攻击者的 32 张证书。CircleID 注明这个数字还没有经过其他人独立复现。

## 导读观点 {#perspective}

HTTPS 证书用来证明「这个网站就是它声称的那一个」，证书颁发机构签发之前确认的是申请者能不能掌控域名，其中一种做法是请申请者在 DNS 加上一条指定的记录。DNS 从顶级域名一路往下委派，依这个机制推论，上层被劫持时攻击者一样能让验证通过。下层域名的持有者即使没有犯任何错，也挡不住这种情况。Google 公告写明，证书颁发机构可以复用先前完成的验证结果，缩短证书有效期与验证结果的复用期限是 Google 列出的长期改进方向。

其他可能受影响的组织，是 Google 从证书透明度的日志找到的。Chrome 与 Safari 都要求公开信任的证书登记在公开的日志里，任何人都能查询。Google 找到的证书都是从日志查到的。依本文的理解，CT 让这类证书在签发之后被发现，签发当下并不会挡下。

Google 也写明，Chrome 的拦截无法可靠地保护其他浏览器的用户，Google 也不能保证已经找出每一个受影响的域名。公告写明 Google 域名的证书已请证书颁发机构吊销，其他组织的证书只写了在 Chrome 拦截，iTnews 的报道则写它找到的伪造证书已由证书颁发机构吊销。Privacy Guides 的报道写 Firefox 用 CRLite（Firefox 检查证书是否已吊销的机制）处理，Safari 与 Edge 到 10 月 12 日查不到相关说明。被拦截的连接有多少，CircleID 写明到 10 月 8 日都还没有公开的资料。

Google 建议自己管理域名的人持续监控手上所有域名的 CT 日志，包括停放中或各地区的国家代码域名，使用 .gh、.sl 或 .as 域名的人要回头检查近期有没有非预期的证书。Cloudflare 与 Cert Spotter 等服务会在有新证书签发时发出通知。Cloudflare 的通知要在它的 Edge Certificates 页面开启，默认是关闭的，Cert Spotter 的网站列的是 30 天免费试用。Google 也建议设置 CAA 记录（DNS 里指定哪些证书颁发机构可以签发的记录），最好绑定特定的 ACME（Let's Encrypt 等机构自动签发证书用的协议）账号。

Google 写明 CAA 挡不住劫持进行中的签发，它的作用在 DNS 控制权恢复之后，可以防止攻击者拿先前通过的验证结果继续申请新证书。CT 监控同样是让人在事后早一点发现，Google 的建议里没有域名持有者能事先挡下这类上层劫持的做法。

依中国互联网络信息中心（CNNIC）官网 2026 年 4 月 9 日的页面，CNNIC 为 .cn 与 .中国 域名提供「国家域名保护锁服务」，在注册管理机构层面设置禁止删除、禁止修改、禁止转移三个状态。解锁要通过 CNNIC 的核验流程。Google 的建议没有提到这类锁定，注册管理机构自己的系统被入侵时能不能挡下，也查不到官方说明。到 10 月 12 日，查不到 CNNIC 针对这次事件的说明。

到 10 月 12 日，查不到三个运营机构或签发的证书颁发机构公布入侵的环节与完整的证书清单。11 月中可以再查一次，看看有没有事故报告说明攻击者从哪里入侵。
