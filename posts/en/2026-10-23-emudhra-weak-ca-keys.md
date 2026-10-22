---
title: Weak private keys in eight eMudhra intermediate certificates
description: Eight intermediate certificates from the Indian certificate authority eMudhra had private keys smaller than 256, which anyone could compute at once and use to issue HTTPS certificates for other people's websites. After a researcher reported it on 17 October, Chrome and Firefox blocked them automatically within hours, with nothing for ordinary browser users to set up. Programs that do not go through a browser carry their own trust lists, and Node.js, Python's certifi, Go, Java and Linux distributions have been shipping updates since 19 October (not all complete as of 22 October), so people who write their own code or run servers need to update each one.
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

The Indian certificate authority eMudhra (certificate brand emSign) had eight intermediate certificates whose private keys were simple enough to calculate directly. Intermediate certificates sit below the root and are the layer actually used to sign website certificates. A researcher reported the problem to Apple, Chrome, Microsoft, Mozilla and eMudhra at 18:05 UTC on 17 October (02:05 on 18 October Taipei time), attaching proofs signed with each of the eight keys. According to Mozilla's 20 October post on the dev-security-policy mailing list, anyone holding the keys could issue HTTPS certificates for websites they do not own.

Chrome and Firefox blocked the six TLS intermediates within hours of the report through automatically pushed blocklists, so most users did not need to update or restart their browsers. The bigger exposure is in programs that do not go through a browser, such as tools and servers written in Node.js, Python, Go or Java, which each keep trusting the certificates until they are updated. Mozilla added on the incident ticket on 20 October that several people had independently computed the keys, and that some of them had made this public.

According to the preliminary analysis by Mozilla engineers on the Bugzilla incident ticket, all eight are P-384 elliptic-curve keys, each of which should be a randomly chosen 384-bit integer. The actual values were all below 256, so trying 256 numbers in turn is enough to find them. Six of the eight sign TLS certificates for websites and are trusted by Chrome, Mozilla, Microsoft and Apple, while the other two sign code and are trusted by Microsoft.

eMudhra's statement says the eight intermediates were created at a key generation ceremony on 30 April 2025, and the problem went unnoticed for about 18 months and through two independent audits. In eMudhra's preliminary explanation on the incident ticket, the software used in the ceremony was flawed and generated a set of weak keys alongside the intended ones. The two sets had similar labels, and the weak keys were mistakenly used to request the certificates. eMudhra's statement, updated on 21 October, also says the exact root cause is still under investigation.

According to the same statement, seven of the eight were never used in production, and the one in use had issued no certificates. eMudhra also says it knows of no evidence that anyone computed the weak keys before disclosure. Google's 20 October blog post says that before the block, Certificate Transparency (CT, the public logs that record every certificate) held no website certificates signed by the six intermediates. Because Chrome by default accepts only certificates logged in CT, Google concluded that forged certificates could not fool Chrome, nor Android apps that target the latest SDK or have opted in to CT checks.

An explainer page that a Mozilla engineer set up for the incident adds that many programs outside the browser do not check CT. The page also says the keys could have been abused ever since the certificates were created in April 2025, and that it is not known whether attackers used the weak keys against such programs.

## Perspective {#perspective}

A browser trusts an HTTPS site because the site's certificate is signed layer by layer by a chain of certificate authorities, with the root certificate at the top preinstalled in the trust list of the browser or operating system. The private key of an intermediate certificate can sign a certificate for any domain. FreeBSD's 21 October security advisory says an attacker able to intercept network traffic could use the computed keys to impersonate any TLS server and read or modify the connection without being detected.

Chrome's CRLSet and Firefox's OneCRL are blocklists that the browsers download automatically in the background, and they can block a specific intermediate certificate on its own. Together with the CT requirement, Chrome and Firefox had two layers of protection on the day of the report. According to Mozilla's release notes and the incident ticket, Firefox installations with automatic list downloads (Remote Settings) disabled need to update to 158.0.1. Some Firefox for Android profiles did not apply the list at startup and need 158.0.2.

According to the Bugzilla incident ticket, eMudhra marked the eight intermediates as revoked on 18 October UTC. Mozilla wrote on the ticket that some programs do not read revocation information, or have no mechanism for distrusting a particular intermediate on its own. NSS is the cryptographic library maintained by Mozilla, and many programs and distributions reuse its root certificate list. To protect those programs, Mozilla removed emSign ECC Root CA - G3, the root that the six TLS intermediates chain up to, in NSS 3.131.1 on 20 October.

Node.js shipped the new list in 22.23.4, 24.22.1 and 26.12.1 on 21 October, and Go released 1.27.3 and 1.26.10. The explainer page's list of fixes shows that Python's certifi 2026.10.19 and curl's CA bundle have been updated as well. Ubuntu's tracking bug shows ca-certificates updates released for 22.04, 24.04, 26.04 and 26.10 as of 22 October, with nothing yet for 20.04 and earlier. Fedora has submitted updates, but according to the Red Hat Bugzilla bug, as of 22 October they still trust the root that issued the two code-signing intermediates.

The explainer page advises ordinary users to update their browsers and operating systems to the latest version as soon as possible. According to Google's blog, Android devices received the same block through Google Play services around 22:00 UTC on 19 October (06:00 on 20 October Taipei time). Google says most Android devices have already received it, and those that have not can apply it immediately by restarting. Android devices without Google Play services fall outside what Google describes there, and we found no update to the Android system itself.

When we checked on 18 October, the third-party monitor GreatFire's last test (on 11 October) found `play.google.com` fully blocked in mainland China, with interference recorded since 10 March 2012. GreatFire measures whether websites can be reached, not whether Google Play services on a device can receive updates. We, a community based in Taiwan, infer from Google's description that Android devices without Google Play services, or whose Google Play services cannot connect, are not covered by the block it describes, while the CRLSet and OneCRL lists that browsers download themselves do not go through Google Play services. The explanation page's advice to ordinary users is to update the browser and system to the latest version, but none of the sources says whether that is enough for such devices, and we did not check whether the two lists download reliably in mainland China.

People who write their own code, run servers or use command-line tools on their computers need to update each runtime they use. Go's fix is in the standard library's `crypto/x509` package, and because Go compiles the standard library into the executable, programs have to be rebuilt with the new version. Python's certifi is a separately installed package with its own copy in every virtual environment and container, so each copy needs updating. According to the explainer page, the curl, python3 and other commands built into macOS do not check revocation when reading `/etc/ssl/cert.pem`, and the file had not been updated as of 22 October.

OpenJDK's 21 October advisory says Java provided by operating system packages mostly uses the system certificates, so updating the system is enough. Java installed separately, along with the FreeBSD and Homebrew packages, needs to be updated directly.

Cloudflare's blog warns against switching off certificate validation to get rid of certificate errors that appear after updating. The explainer page provides test URLs signed by the affected intermediates, and a certificate error when connecting with curl means curl no longer trusts those certificates. Cloudflare's blog also notes that such a test speaks only for the program tested, and programs that validate certificates in other ways need to be checked separately.

Removing the root protects programs that do not read revocation information, at the cost of invalidating some legitimate sites' certificates as well. eMudhra estimated on the incident ticket that about 30,000 certificates need replacing, and its statement says the impact is limited to a single customer ecosystem in the United States. From CT data up to 21 October, Chrome counted on the ticket about 30,800 unexpired certificate entries under this root, 99.9% of them issued by two subordinate intermediates of Internet2 and InCommon. According to Google's blog, Chrome plans to remove the same root from the Chrome Root Store on the morning of 27 October Pacific Time, and is assessing whether to keep trusting eMudhra's other certificates.

The explainer page says Apple devices have blocked the certificates since 19 October and Microsoft platforms since 20 October. As of 22 October, we had not found announcements from either company. According to the Bugzilla incident ticket, eMudhra had not filed a formal incident report as of late on 21 October UTC. The formal report, eMudhra's answers to Chrome's questions on the ticket, and Chrome's decision on eMudhra's other certificates are the things to watch next.
