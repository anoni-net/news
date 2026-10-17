---
title: Let's Encrypt 默认证书的 64 天有效期
description: Let's Encrypt 公告 2027 年 2 月 10 日起，默认签发的证书有效期从 90 天缩短为 64 天。用它搭建网站或自建服务的人，要确认自动续期不是写死在固定天数，公告没有针对一般访问者的说明。
date: 2026-10-15T00:05:00+08:00
slug: letsencrypt-64-day-certs
categories:
  - encryption
sources:
  - title: 64-Day Certificate Lifetimes Coming Feb 2027
    url: https://letsencrypt.org/2026/10/07/64-day-certs.html
    publisher: Let's Encrypt
    date: 2026-10-07
  - title: Decreasing Certificate Lifetimes to 45 Days
    url: https://letsencrypt.org/2025/12/02/from-90-to-45.html
    publisher: Let's Encrypt
    date: 2025-12-02
  - title: Shorter Certificate Lifetimes and Rate Limits
    url: https://letsencrypt.org/2026/02/24/rate-limits-45-day-certs.html
    publisher: Let's Encrypt
    date: 2026-02-24
  - title: ACME Renewal Information (ARI) Published as RFC 9773
    url: https://letsencrypt.org/2025/09/16/ari-rfc.html
    publisher: Let's Encrypt
    date: 2025-09-16
  - title: "Ballot SC081v3: Introduce Schedule of Reducing Validity and Data Reuse Periods"
    url: https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/
    publisher: CA/Browser Forum
    date: 2025-04-11
  - title: Let's Encrypt cuts certificate lifetimes to 64 days starting February 2027
    url: https://arstechnica.com/gadgets/2026/10/lets-encrypt-cuts-certificate-lifetimes-to-64-days-starting-february-2027/
    publisher: Ars Technica
    date: 2026-10-08
  - title: Why ninety-day lifetimes for certificates?
    url: https://letsencrypt.org/2015/11/09/why-90-days.html
    publisher: Let's Encrypt
    date: 2015-11-09
  - title: ACME Client Implementations
    url: https://letsencrypt.org/docs/client-options/
    publisher: Let's Encrypt
  - title: Profiles
    url: https://letsencrypt.org/docs/profiles/
    publisher: Let's Encrypt
  - title: certbot/CHANGELOG.md
    url: https://github.com/certbot/certbot/blob/main/certbot/CHANGELOG.md
    publisher: GitHub
  - title: 重要通知─配合國際規範 TWCA SSL / TLS 憑證調整重要通知
    url: https://www.twca.com.tw/news_detail/04f741de-2258-431d-be3a-992268cd5d72
    publisher: TWCA
    date: 2025-12-02
  - title: Is https://acme-v02.api.letsencrypt.org blocked in mainland China?
    url: https://en.greatfire.org/https/acme-v02.api.letsencrypt.org
    publisher: GreatFire
  - title: 电子认证服务管理办法
    url: https://www.gov.cn/zhengce/2022-08/23/content_5722726.htm
    publisher: 中国政府网
authors:
  - anoni-net
---

Let's Encrypt 10 月 7 日公告，2027 年 2 月 10 日起签发与续期的证书，默认有效期从 90 天缩短为 64 天。最后一张 90 天证书预计 2027 年 5 月 11 日到期，现有的有效证书不会被吊销。公告只对搭建网站与自建服务的人提出要求，没有针对一般访问者的说明。

测试环境（staging）10 月 14 日先改发 64 天证书，Let's Encrypt 建议正式生效前先在这里测试。依 2025 年 12 月的公告，2028 年 2 月 16 日默认有效期会再缩短为 45 天。想提早改用的人，现在就可以选 45 天或 6 天的证书类型（profile，申请时指定的一组证书规格）。

依 Let's Encrypt 的说明，缩短有效期是为了降低密钥泄露与证书误签发的风险。CA/Browser Forum（证书机构与浏览器厂商共同制定证书规范的组织）2025 年 4 月通过的决议，把证书有效期上限从 398 天逐步缩短，2026 年 3 月 15 日起 200 天、2027 年 3 月 15 日起 100 天、2029 年 3 月 15 日起 47 天。64 天比 2027 年的上限更短，本文依两份公告的时间表推论，这是 Let's Encrypt 在 2029 年 47 天上限之前自定的中间阶段。

## 导读观点 {#perspective}

证书用来证明「这个网站就是它声称的那一个」，密钥泄露或被误签发的证书，在到期之前都可能被拿来冒充网站。有效期越短，出事之后能被冒用的时间就越短（依 Let's Encrypt 2015 年的说明，这也是当初选择 90 天的理由之一）。代价是续期变得更频繁，Let's Encrypt 2 月的说明预期有效期缩到 45 天时每天的续期请求会翻倍。2025 年 12 月的公告提到不建议手动续期，10 月的公告也提到速率限制不受影响。

负责申请与续期证书的程序称为 ACME 客户端，例如 Certbot。已经自动续期、而且客户端支持 ARI（ACME Renewal Information，让证书机构告诉客户端何时该续期的机制，2025 年成为 RFC 9773）的人，依公告不必做任何改动，Certbot 从 2025 年 6 月的 4.1.0 版起默认会检查 ARI。把续期时间写死在固定天数的人，Let's Encrypt 建议改成在有效期约三分之二时续期。不确定有没有写死的，可以在定时任务、脚本与运维手册里找 83、80、60 这类数字。

第三方监测网站 GreatFire 的页面（10 月 12 日查阅，最近一次测试在 9 月中旬，9 月几次连接被拒绝已不再算作封锁的证据）显示，letsencrypt.org 与签发证书用的 ACME 接口在中国大陆都可以连接。2015 年修订的《电子认证服务管理办法》规范电子签名认证，条文没有写是否适用网站的 TLS 证书。截至 10 月 12 日，本文也没有找到针对境外机构签发 TLS 证书的明文规定。中国大陆的证书机构 iTrusChina、SHECA、TrustAsia 在 CA/Browser Forum 那次投票中都投了赞成票。

用 Let's Encrypt 搭建网站的读者现在可以先确认客户端是否支持 ARI，10 月 14 日之后用测试环境执行一次续期，并照公告的建议加上续期失败的通知。只能通过网页界面手动上传证书的设备，公告没有专门的说明。依本文推算，每张证书用满 64 天一年也要换 6 次，照公告建议在约三分之二时更换约要 9 次。Let's Encrypt 的客户端列表页说明不列浏览器内的 ACME 客户端，理由是它们鼓励手动续期，会增加漏掉续期的风险。
