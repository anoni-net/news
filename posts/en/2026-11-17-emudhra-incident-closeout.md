---
title: The eMudhra incident report, macOS fixes and the deadline for the G1 root
description: The weak private key incident at the Indian certificate authority eMudhra had three developments in November. On 9 November Apple released macOS 27.2.1, 26.7.3 and 15.8.3, fixing git, curl and other built-in command-line tools. People who use these tools on a Mac should update, and everyone else needs no extra setup. On 10 November eMudhra filed an incident report covering the eight RSA intermediate certificates it separately revoked on 7 November. According to the source code we read on 14 November, Chrome and Mozilla no longer trust certificates chaining to emSign Root CA - G1 that are issued after 16 November UTC, and Microsoft has scheduled the removal of trust in G1 from Edge and WebView2 on the same day.
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
  - title: Transcript of the Earnings Call held on Thursday, November 05, 2026
    url: https://nsearchives.nseindia.com/corporate/EMUDHRA2008_09112026195622_Conferencecall_Transcript__1_.pdf
    publisher: eMudhra
    date: 2026-11-09
  - title: Business Responsibility and Sustainability Report for the financial year ended on March 31, 2025
    url: https://nsearchives.nseindia.com/corporate/EMUDHRA2008_28052025174638_BRSR.pdf
    publisher: eMudhra
    date: 2025-05-28
  - title: eMudhra Intermediate CA Compromise
    url: https://emudhra.we-have-a-problem.com/
    publisher: emudhra.we-have-a-problem.com
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
    date: 2026-11-01
authors:
  - anoni-net
---

The Indian certificate authority eMudhra (certificate brand emSign) had eight intermediate certificates whose private keys could be computed directly, and since the incident became public in mid-October there have been three developments in November. On 9 November Apple released macOS 27.2.1, 26.7.3 and 15.8.3, which fix the built-in command-line tools and update the root certificate file `/etc/ssl/cert.pem`. On 10 November eMudhra filed a full incident report on Mozilla's Bugzilla incident ticket `2083449`. Chrome and Mozilla have put a date limit on another eMudhra root certificate, emSign Root CA - G1, and Microsoft has scheduled the removal of trust in it from Edge and WebView2 (the component Windows apps use to embed web pages).

People who use the built-in git, curl, python3 or similar tools on a Mac to reach `https://` URLs should update to one of these versions, and everyone else needs no extra setup. According to Apple's support document, Safari, Mail and apps that use Apple's networking and security frameworks were already blocking the affected certificates automatically, with no update to install. According to Microsoft's notice, the related updates for Edge and WebView2 arrive through component updates.

Apple's support document, revised on 9 November, says that from macOS 27.2.1 the command-line tools that ship with macOS and the Xcode Command Line Tools also block the 12 affected intermediate certificates. Six of the eight ECDSA intermediates revoked in October are TLS intermediates, and each exists as two certificates, 12 in all: one chains to eMudhra's root emSign ECC Root CA - G3, and the other is cross-signed by Sectigo and chains to AAA Certificate Services. The update also removes five root certificates from `/etc/ssl/cert.pem`, including those two roots and emSign Root CA - G1, and the corresponding fixes for macOS 26 and macOS 15 are 26.7.3 and 15.8.3.

According to the incident report, eMudhra revoked eight RSA-4096 intermediate certificates (the G2B and G2C series) on 7 November. Together with the eight ECDSA intermediates revoked on 18 October, that makes 16 affected intermediates. The revocation reason given on 7 November was cessation of operation (`cessationOfOperation`), while the earlier ECDSA batch was revoked for CA key compromise (`caCompromise`).

The report says the eight RSA private keys are not weak, and their signatures all match the public keys in the certificates. All 16 keys were created at the same key generation ceremony on 30 April 2025, and when they were imported, the private key material passed through the memory of a Python program on a host machine, outside the hardware security module (HSM, hardware built to generate and hold private keys). As a result, eMudhra cannot show that its handling of these keys met the private key transfer rules in its own Certification Practice Statement (CPS, the operating rules a certificate authority publicly commits to). The report says the RSA problem was confirmed in early November after root programs discussed this rule, without saying which program raised it or whether the revocation was made at its request.

The report gives no evidence that anyone obtained the RSA private keys, and for the incident as a whole it says there are no known cases of misuse. On the day the report was filed, a commenter on the ticket asked why, if eMudhra cannot show the keys were handled in compliance, the revocation reason was not key compromise (`keyCompromise`). As of 14 November, eMudhra had not replied to this question on the ticket.

According to the report's appendix, six of the eight are TLS intermediates (issuer emSign Root TLS CA - G1) and two are code-signing intermediates (issuer emSign Root CS CA - G2). Each kind has G2B and G2C versions, and the four G2B intermediates never issued end-entity certificates. The four G2C intermediates went into use in the United States from May and issued both website certificates and code-signing certificates. The G2C intermediates last issued a certificate on 3 November, and the report says the end-entity certificates have been migrated or reissued.

According to eMudhra's 28 October update, the US customer ecosystem holding about 30,800 G3 certificates has moved to issuing from eMudhra's G1 RSA root. The incident report describes the main customer of the G1 hierarchy as a university federation in North America. Comparing the 28 October update with the incident report, we infer that this G1 RSA pathway includes the G2C intermediates revoked this time, though neither document says so directly. The report lists the issuer of the TLS intermediates as emSign Root TLS CA - G1, and we found no primary source on how it relates to emSign Root CA - G1.

InCommon (a certificate service for US universities and research institutions) wrote in its 10 November announcement that "Our current G1 issuing Certificate Authority (CA) is no longer viable for public trust". A later update on the same page says issuance has moved from emSign to SSL.com and asks institutions to replace the affected certificates by the end of 16 November. The report does not name the university federation, and from the two descriptions we infer that InCommon is the same customer.

eMudhra's report says all issuance under the G1 hierarchy will stop before 16 November, and when the report was filed on 10 November this item was listed as in progress. The Chromium and Firefox source code we read on 14 November both put a date limit on emSign Root CA - G1. Certificates issued after 23:59:59 UTC on 16 November (07:59:59 on 17 November, UTC+8) are no longer trusted, while those issued earlier still are. We found no announcement from Chrome or Mozilla about G1, and the source code does not say when stable releases will carry the setting.

Microsoft's notice, updated on 11 November, says a component update ships on 16 November, after which Edge and WebView2 remove default trust in four eMudhra roots, G1 among them. As of 14 November, we had found nothing on the outcome of this update.

## Perspective {#perspective}

Under the source code settings as of 14 November, Chrome's limit goes by the time a certificate was recorded in a Certificate Transparency log (CT log, a public log that records every certificate), and Mozilla's list sets a deadline on the same day. Once the settings take effect, certificates already issued can be used until they expire, and new ones issued after the deadline are rejected. Microsoft's planned update for Edge and WebView2 removes G1 outright, as does the macOS command-line tools update, so website certificates chaining to G1 may fail verification no matter when they were issued. From this we infer that a website that has not yet replaced its G1 certificate may open normally in Chrome but fail verification in Edge or in curl on a Mac.

eMudhra's incident statement, updated on 5 November, says Apple plans to remove and distrust the G1 root on 30 November, after which no certificate under G1, whenever issued, will be trusted on Apple's platforms. InCommon's 10 November announcement repeats this date. As of 14 November, Apple's support document revised on 9 November did not give this date, and said only that G1 had been removed from `/etc/ssl/cert.pem`.

Our previous article noted that people who did not want to wait for an update could follow Apple's steps to remove G3 and AAA Certificate Services from `/etc/ssl/cert.pem` by hand. According to the same support document, after updating to 27.2.1, 26.7.3 or 15.8.3 there is no need to repeat those steps. The backup file `/etc/ssl/cert.pem.orig` left by Apple's steps can be deleted with `sudo rm`, and a backup made before the update should not be restored either. The updated file has five fewer roots, and Apple warns that tools that read only this file may be unable to verify some websites whose certificates chain to these roots.

The command-line tools that need the update include the built-in git, curl, python3, ruby, perl and openssl. On a Mac that cannot update to one of these versions, you can remove the root certificates from `/etc/ssl/cert.pem` by hand following the steps in Apple's support document, which requires an administrator account. Apps and tools that bring their own root certificate list do not read `/etc/ssl/cert.pem` and do not apply Apple's block either. System updates do not protect these tools, and you need to ask their developers.

In its earnings call on 5 November, whose transcript it filed with India's stock exchanges on 9 November, eMudhra said it had added significant clients in Indonesia, the Philippines, Germany, Qatar and Abu Dhabi, and that its trust services pipeline in the UAE was still awaiting a licence. On the same call the company put its publicly trusted TLS business at about 1% of revenue, said its digital signatures, eSign and five enterprise platforms were not affected, and described a university federation in the US as the only customer directly affected. Its business responsibility and sustainability report for the year ended 31 March 2025 lists "Middle East & Africa" and "Far East & Indonesia" among its operating regions, along with wholly owned subsidiaries including eMudhra DMCC and eMudhra Pte Ltd. As of 14 November we had found no public TLS customers or business of eMudhra in mainland China, Hong Kong or Taiwan, nor anything linking the RSA revocation to websites there.

The explainer page's list of who has shipped fixes for the G3 and ECDSA intermediates, maintained by a researcher rather than by the vendors, still marked OpenHarmony/HarmonyOS NEXT as pending when we read it on 14 November, and as of 2 November we had found no statement from Huawei. The same page says many Android devices received Google's block through the Google Play services update channel, and that on devices without the updated blocklist users may be able to disable the affected roots in Settings, though its steps name only emSign ECC Root CA - G3 and AAA Certificate Services, not G1. GreatFire's last test on 1 November found `play.google.com` fully blocked in mainland China, a measure of whether the site can be reached rather than whether devices receive updates. The page does not mention G1 or the RSA intermediates, we did not check how HarmonyOS or Android handle G1, and as of 14 November we had found no statement from systems or browsers in mainland China, Hong Kong or Singapore on the RSA revocation.

People who use only Safari, Mail and apps built on Apple's frameworks need to do nothing. Things to watch next are the independent KPMG review that eMudhra expects to complete on 4 December, whether Apple acts on G1 on 30 November, and whether Chrome and Mozilla, which as of 14 November had only set a date limit, go on to remove G1 from their trust lists entirely.
