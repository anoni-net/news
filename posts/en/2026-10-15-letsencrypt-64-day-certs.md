---
title: Let's Encrypt's 64-day default certificate lifetime
description: Let's Encrypt will cut its default certificate lifetime from 90 to 64 days from 10 February 2027. Anyone running a site or self-hosted service on its certificates should check that automatic renewal is not tied to a fixed number of days. The announcement says nothing to ordinary visitors.
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
  - title: サーバー証明書の最長有効期間短縮に伴うサービス改定について
    url: https://jprs.jp/pubcert/info/notice/20251127-certificate-shortened-validity-period.html
    publisher: JPRS
    date: 2025-11-27
  - title: "[공지] SSL/TLS 인증서 유효기간 단축 안내"
    url: https://www.kicassl.com/cstmrsuprt/ntc/searchNtcDetail.sg?ntcSeq=1461
    publisher: KICA
    date: 2025-04-17
authors:
  - anoni-net
---

Let's Encrypt announced on 7 October that certificates issued or renewed from 10 February 2027 will have a default lifetime of 64 days instead of 90. The last 90-day certificates are expected to expire on 11 May 2027, and valid certificates will not be revoked. The announcement only asks things of people running sites and self-hosted services, and says nothing to ordinary visitors.

The staging environment switches to 64-day certificates on 14 October, and Let's Encrypt recommends testing there first. Under its December 2025 announcement, the default drops again to 45 days on 16 February 2028, and anyone who wants to move early can already choose a 45-day or 6-day profile (a named set of certificate settings requested at issuance).

Let's Encrypt says shorter lifetimes reduce the risk of key compromise and mis-issuance. A ballot passed in April 2025 by the CA/Browser Forum, where certificate authorities and browser makers set the rules for certificates, cuts the maximum lifetime from 398 days in steps: 200 days from 15 March 2026, 100 days from 15 March 2027 and 47 days from 15 March 2029. Since 64 days is shorter than the 2027 cap, our reading of the two announcements is that it is an intermediate step Let's Encrypt chose before the 47-day limit arrives.

## Perspective {#perspective}

A certificate proves that a site is who it claims to be, and a leaked key or mis-issued certificate can be used to impersonate the site until it expires. Shorter lifetimes shrink that window, which, according to Let's Encrypt's 2015 explanation, was one of its reasons for choosing 90 days. The cost is more frequent renewal: a February post expects daily renewal requests to double once lifetimes reach 45 days. The December 2025 announcement advises against manual renewal, and rate limits are not affected.

The software that requests and renews certificates is called an ACME client, such as Certbot. If renewal is automated and the client supports ARI (ACME Renewal Information, which lets the certificate authority tell the client when to renew, published as RFC 9773 in 2025), the announcement says no change is needed, and Certbot has checked ARI by default since version 4.1.0 in June 2025. Let's Encrypt recommends that anyone who hard-coded renewal at a fixed number of days switch to renewing at about two-thirds of the lifetime, and suggests searching cron jobs, scripts and runbooks for numbers such as 83, 80 or 60 if unsure.

Certificate authorities in Asia have announced their own changes for the CA/Browser Forum caps, and the three announcements we read do not mention Let's Encrypt's 64 days. Taiwan Certificate Authority (TWCA) set a 198-day lifetime from 9 March 2026, meaning two applications a year, and Japan Registry Services (JPRS) cut its server certificates from one year to five months from 18 February 2026 while leaving its ACME-based service unchanged. In South Korea, Korea Information Certificate Authority (KICA), which sells Sectigo certificates, published the CA/Browser Forum schedule in April 2025. TWCA and JPRS were among the five certificate issuers that abstained in the 2025 ballot.

Site operators using Let's Encrypt can check now whether their client supports ARI, run a renewal against staging after 14 October and, as the announcement suggests, add alerts for failed renewals. The announcement says nothing specific about devices that only accept certificates uploaded through a web interface. By our count, using each certificate for the full 64 days still means six replacements a year, or about nine if renewed at two-thirds as recommended, and Let's Encrypt's client list explains that it leaves out in-browser ACME clients because they encourage manual renewal, which increases the risk of missed renewals.
