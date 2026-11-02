---
title: Aftermath of the eMudhra weak private keys, and macOS command-line tools
description: After the private keys of eight intermediate certificates from the Indian certificate authority eMudhra were computed, Apple, Microsoft and Chrome have all blocked or removed the related certificates, and ordinary users' browsers, phones and computers need no extra setup. The git, curl and other command-line tools built into macOS may still accept these certificates, and as of 2 November we had found no fix from Apple. eMudhra has announced it is leaving the public TLS certificate business, and as of 1 November had not filed a formal incident report on the incident ticket.
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

The Indian certificate authority eMudhra (certificate brand emSign) had eight intermediate certificates whose private keys were small enough to compute directly, letting anyone holding them issue HTTPS certificates for websites they do not own. Since the incident became public in mid-October, Apple and Microsoft have published how they are handling it, and Chrome's trust list has dropped the related root certificate. Ordinary users' browsers, phones and computers need no extra setup. According to Apple's 29 October support document, though, the git, curl and other command-line tools built into macOS may keep accepting these certificates until a future software update.

Apple's support document says that since 19 October Apple has blocked the six intermediates that issue TLS certificates. Each of them exists as two certificates, one chaining to eMudhra's root emSign ECC Root CA - G3 and one cross-signed by Sectigo (another certificate authority's root signs a second copy, giving the same intermediate an extra path to trust) that chains to Sectigo's root AAA Certificate Services. Apple blocks all 12 of these certificates, and has also blocked the G3 root since 23 October. The block reaches devices automatically through certificate configuration data, with no software update to install, and Safari, Mail and apps that use Apple's networking and security frameworks all reject the certificates.

The same document says the curl, git, python3, ruby, perl and openssl that ship with macOS and the Xcode Command Line Tools verify certificates against a single file, `/etc/ssl/cert.pem`. When a certificate chains to a root in that file, these tools check neither Apple's block nor whether the certificate has been revoked. Apple writes that the file will be updated in a future macOS update, without saying which version or when.

A Mozilla engineer who set up an explainer page for the incident added a separate page about Apple's tools on 28 October. According to that page, macOS 27.2, released on 26 October, did not fix the problem and undid the workaround of removing the roots by hand. An attacker on the network path could make git fetch attacker-chosen code from `https://` remotes, and could intercept credentials such as GitHub tokens. As of 2 November, we had found no macOS release after 27.2 that fixes it.

Microsoft's 28 October notice in the Microsoft 365 Message Center says the Windows Disallowed Certificate Trust List already blocks the affected certificate authorities. Edge and WebView2 (the component Windows apps use to embed web pages) also receive a CRLSet, a blocklist downloaded in the background, through component updates, with no new browser version to install. The notice adds that Microsoft has released Windows and Edge updates removing certificates related to these hierarchies from the trust list, but gives no date for Edge.

According to the Message Center notice and the Microsoft Security Response Center (MSRC) blog post quoted by The Register, Microsoft released an out-of-band Windows update (one outside the regular schedule) on 26 October that removes seven certificates related to the affected hierarchies from the Windows trust list. The update is meant for devices that cannot reach Microsoft's certificate update service or have automatic trust list updates turned off, and it also carries a known issue from the 13 October update. Certificate lists normally arrive through the update service, so many devices do not need this update.

Google's 20 October blog post said the Chrome Root Store would remove emSign ECC Root CA - G3 on the morning of 27 October Pacific Time. We could not find an announcement from Chrome that the removal was done, but in the Chromium source code we read on 2 November, the Chrome Root Store list no longer includes this root. eMudhra's other root, emSign Root CA - G1, is still on the list, and Mozilla also wrote on the incident ticket on 20 October that it was not removing trust in G1 at that time. Google's 20 October post said it was assessing whether to keep trusting eMudhra's other certificates, and as of 2 November we had found no outcome.

On 27 October the Chrome Root Program replied to community questions on the incident ticket, describing the CRLSet block and the eventual closure of the incident ticket as emergency containment, with follow-up work still to come. According to that comment, within an hour of the report Chrome ran Google's `paranoid_crypto` over every CA certificate Chrome trusts and found no other weak keys of known types. Before the incident, the checking tools in common use in the industry did not test for elliptic-curve private keys that are too small. Chrome has opened an issue in the tooling project of CCADB (the certificate authority database shared by the browser vendors) to require weak-key checks before a CA discloses a certificate.

eMudhra announced on the incident ticket on 25 October that it is leaving the public TLS certificate business, and on 30 October appointed KPMG as an independent external reviewer. According to eMudhra's incident statement page, its leadership's 26 October explanation put the problem down to an error in its own scripts and promised a full root cause analysis through the CCADB process. A 28 October update says about 30,800 certificates under G3 belong to a single customer ecosystem in the United States, which has already switched to issuing new certificates from eMudhra's G1 RSA root. eMudhra also asked the root programs for time to let these customers migrate, and says it will stop issuing TLS certificates from G1 once the migration is complete.

On 20 October the Mozilla Root Program sent eMudhra a list of questions and asked for an initial reply within 24 hours, which it still had not received on 23 October. On 23 October eMudhra blamed the delay on intense attention from social media, investors and customers, and the Chrome Root Program replied that this was not an acceptable reason. eMudhra's 25 October comment argued that CCADB's incident reporting rules give a CA 14 days to submit a full report, and that it was still within the deadline.

eMudhra later wrote on 27 October that it had replied to Mozilla's questions directly, and on 29 October attached a response document for Google to the ticket. As of the last comment on 1 November, eMudhra had not filed a formal incident report on this ticket, and the ticket was still open.

## Perspective {#perspective}

Chrome's CRLSet, Apple's certificate configuration data and the Windows Disallowed Certificate Trust List all update automatically in the background and can block a specific intermediate certificate on its own. The command-line tools built into macOS read only the `/etc/ssl/cert.pem` file, which still contains the G3 root and Sectigo's AAA Certificate Services, so certificates chaining to either root pass verification. Apple's document says these tools do not check revocation, which means eMudhra's revocation of the eight intermediates on 18 October UTC has no effect on them.

According to a count a researcher posted on the incident ticket on 25 October (which we did not verify independently), 107,107 certificates signed with six of the keys were recorded in one operator's Certificate Transparency log (CT log, a public log that records every certificate) between 20 and 21 October UTC. Of these, 106,050 were proof-of-concept certificates naming only google.com, and 106,058 chained to a root through Sectigo's AAA cross-signature. One of the examples the researcher listed embeds signed certificate timestamps (SCTs, proof of inclusion) from three logs, all of which Chrome lists as usable, and from this we infer that requiring CT inclusion proofs alone does not stop such certificates. Almost none of these certificates carry a pointer to revocation information, so programs that check only the revocation status of the website certificate itself will not stop them either, and only programs that check CA certificate revocation at every level, receive a pushed blocklist, or have removed the related roots will reject them.

According to Apple's document, people who do not use Terminal need to do nothing, and people who use the built-in git, curl or python3 on a Mac to reach `https://` URLs can wait for Apple's update. Those who do not want to wait can follow the same document and remove emSign ECC Root CA - G3 from `/etc/ssl/cert.pem` with an administrator account. Removing G3 alone does not block the six Sectigo cross-signed certificates, so AAA Certificate Services has to be removed as well. The same document notes the cost, which is that some websites unrelated to the incident that chain through these roots may also fail verification in these tools.

Apple's document also warns that a macOS update can put the original file back, so until you install a version that contains the fix, check again after every update. Apps and tools that bring their own root certificate list do not read this file and do not apply Apple's block either, and you need to ask their developers. Removing root certificates by hand on a Mac only protects the tools that read this file.

The explainer page's list of who has shipped fixes marks OpenHarmony/HarmonyOS NEXT as pending, and the page says OpenHarmony-based HarmonyOS does not let users disable system-installed roots, so "No user-side workaround is available on these devices until the patched version ships." HarmonyOS is Huawei's operating system, but that list is maintained by the researcher, not published by Huawei, and as of 2 November we had found no statement from Huawei. The same page says HarmonyOS 4.3 and earlier can disable the roots the same way as other Android-based systems, and that the block reaches many Android devices through the Google Play services update channel. GreatFire's last test on 1 November found `play.google.com` fully blocked in mainland China, although GreatFire measures whether the site can be reached, not whether Google Play services on a device can receive updates.

Things to watch next are the macOS update in which Apple fixes `/etc/ssl/cert.pem`, the formal incident report eMudhra files through the CCADB process, and each root program's decision on the G1 root. The customer ecosystem that holds about 30,800 certificates has already moved to issuing from G1. We infer that whether G1 stays trusted will decide how soon these websites have to replace their certificates again.
