---
title: Country-code top-level domain hijacks and unauthorized HTTPS certificates
description: Google announced on 6 October that the .gh, .sl and .as country-code top-level domains were hijacked and attackers obtained HTTPS certificates for Google and other organizations. Chrome has blocked the certificates it found; domain owners can monitor Certificate Transparency logs.
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
    publisher: Let's Encrypt Community Forum
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
  - title: 將您的域名「鎖」上——Registry Lock
    url: https://twnic.tw/blog/contents.php?id=25&lang=zh-tw
    publisher: TWNIC
    date: 2025-09-12
  - title: .tw 域名安全鎖服務 Registry Lock Service
    url: https://registrylock.tw/
    publisher: TWNIC
  - title: レジストリロックサービス
    url: https://jprs.jp/about/dom-rule/registry-lock/
    publisher: JPRS
  - title: HKIRC Launches .hk LOCK
    url: https://www.hkdnr.hk/en/hkirc-launches-hk-lock/
    publisher: HKDNR
    date: 2014-01-15
authors:
  - anoni-net
---

Google announced on 6 October that the .gh (Ghana), .sl (Sierra Leone) and .as (American Samoa) country-code top-level domains (ccTLDs) had been hijacked, and that attackers used this to obtain HTTPS certificates for several Google domains and for domains of other organizations. The announcement says the domains at risk are those ending in these three codes, and that Google's own systems were not compromised. Chrome has blocked the certificates Google found, and the announcement says Chrome users do not need to take any action.

According to Google, the attackers compromised these three third-party-operated ccTLDs and modified authoritative DNS records, the records that say where a domain points. The announcement does not say where the attackers got in, for example the operator's systems or a registrar account, or when the hijacks began, and as of 12 October we, a community based in Taiwan, could not find any statement from the three operators. Ars Technica reports that control of the DNS records let the attackers pass certificate authorities' domain control validation (DCV), the check that an applicant really controls a domain, while iThome writes that they may have passed it this way. Google writes that it has no reason to believe the issuing certificate authorities did anything wrong.

Google first blocked the certificates for its own domains through CRLSets, Chrome's emergency certificate blocklist, and asked the issuing CAs to revoke them. Certificate Transparency (CT) logs, public logs that record every issued certificate, then revealed other organizations believed to be affected by the same attacks, including leading global brands and widely used online services, and Chrome blocked those certificates as well. A Let's Encrypt staff member confirmed on its forum that it had issued certificates for Google and YouTube and that they have been revoked. iTnews compared CT logs against Chrome's blocklist and found 32 certificates issued to the attackers between 22 and 27 September, a count CircleID notes has not been independently reproduced.

## Perspective {#perspective}

An HTTPS certificate vouches that a site is the one it claims to be. Before issuing one, a certificate authority checks that the applicant controls the domain, and one way is to ask the applicant to publish a specific DNS record. DNS is delegated downward from the top-level domain, so we infer that when the layer above is hijacked, an attacker can pass validation even though the owner of the domain below did nothing wrong. Google's announcement notes that CAs may reuse earlier validation results, and lists shorter certificate lifetimes and shorter validation reuse periods among its long-term improvements.

The other possibly affected organizations were found by Google in Certificate Transparency logs. Chrome and Safari require publicly trusted certificates to be recorded in public logs that anyone can search. The certificates Google found were all found in those logs. Our reading is that CT lets such certificates be discovered after issuance and does not stop them at the moment of issuance.

Google also writes that Chrome's blocking does not reliably protect users of other browsers, and that it cannot guarantee it identified every affected domain. The announcement says the certificates for Google domains were revoked with the CAs' help, but for other organizations it only says Chrome blocked them, while iTnews reports that the CAs have revoked the bogus certificates it found. Privacy Guides writes that Firefox handles them with CRLite, its revocation checking mechanism, and as of 12 October we found nothing from Safari or Edge. CircleID notes that, as of 8 October, how much traffic may have been intercepted had not been established publicly.

Google recommends that domain owners continuously monitor CT logs for all of their domains, including parked and regional ccTLD domains, and that anyone with a .gh, .sl or .as domain review recent entries for unexpected certificates. Services such as Cloudflare and Cert Spotter send alerts when a new certificate is issued. Cloudflare's alerts are switched on from its Edge Certificates page and are off by default, and Cert Spotter's site lists a 30-day free trial. Google also recommends CAA records, which name the CAs allowed to issue for a domain, ideally bound to specific ACME accounts (ACME being the protocol Let's Encrypt and others use for automated issuance).

Google writes that CAA cannot prevent issuance during an active DNS hijack. Its value comes after DNS control is restored, when it stops an attacker from using earlier validation results to obtain new certificates. CT monitoring likewise helps owners find out sooner after the fact, and Google's recommendations include nothing a domain owner can do to block this kind of upstream hijack in advance.

Several registries in Asia offer registry-level locks, which add update, transfer and delete prohibitions to a domain. In Taiwan, TWNIC's Registry Lock lists NT$6,000 per domain per year, with a NT$4,800 first-year price for new applications until 31 December 2026, as of 12 October. Japan's JPRS offers its registry lock only through designated registrars, whose offerings vary. Hong Kong's HKIRC announced .hk LOCK in 2014, with each change verified by human contact, and we could not confirm its current terms.

These locks guard against unauthorized changes to registration data, and TWNIC writes that its lock still protects a domain even if the registrar is compromised. We found no official description of a registry lock from South Korea's KRNIC. We found no official statement on whether a lock helps when the registry operator itself is breached, and Google's recommendations do not mention locks.

As of 12 October, we found no disclosure from the three operators, the issuing CAs or the Asian registries above about how the attackers got in, and no full list of the certificates. It is worth checking again in mid-November for any incident report that explains the point of entry.
