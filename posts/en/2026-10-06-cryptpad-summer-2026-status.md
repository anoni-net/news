---
title: CryptPad's summer 2026 status and the post-quantum bottleneck
description: CryptPad, an end-to-end encrypted collaboration suite, has a new security policy that keeps vulnerability details private for at least 90 days after a fix ships. Its post-quantum experiment left some features too slow to use, and native browser support for the algorithms may change that. People on public instances need not change anything, while self-hosting administrators should keep up with releases.
date: 2026-10-06T00:00:00+08:00
slug: cryptpad-summer-2026-status
sources:
  - title: Summer 2026 status
    url: https://blog.cryptpad.org/2026/09/15/status-2026-09/
    publisher: CryptPad
    date: 2026-09-15
  - title: 2026.2 security fixes and our new security policy
    url: https://blog.cryptpad.org/2026/06/24/2026.2-security-issues/
    publisher: CryptPad
    date: 2026-06-24
  - title: CryptPad Security Policy
    url: https://cryptpad.org/security/
    publisher: CryptPad
    date: 2026-06-23
  - title: Winter fix release (2026.2.1)
    url: https://github.com/cryptpad/cryptpad/releases/tag/2026.2.1
    publisher: GitHub
    date: 2026-03-27
  - title: Spring fix release (2026.5.1)
    url: https://github.com/cryptpad/cryptpad/releases/tag/2026.5.1
    publisher: GitHub
    date: 2026-05-26
  - title: Autumn Release
    url: https://github.com/cryptpad/cryptpad/milestone/20
    publisher: GitHub
  - title: Summer 2025 status
    url: https://blog.cryptpad.org/2025/09/05/status-2025-08/
    publisher: CryptPad
    date: 2025-09-05
  - title: Modern Algorithms in the Web Cryptography API
    url: https://wicg.github.io/webcrypto-modern-algos/
    publisher: WICG
    date: 2026-09-14
  - title: "CryptPad: Collaboration suite, encrypted and open-source"
    url: https://cryptpad.fr/
    publisher: CryptPad
  - title: Security
    url: https://docs.cryptpad.org/en/user_guide/security.html
    publisher: CryptPad
  - title: User Account
    url: https://docs.cryptpad.org/en/user_guide/user_account.html
    publisher: CryptPad
  - title: Support
    url: https://docs.cryptpad.org/en/user_guide/support.html
    publisher: CryptPad
  - title: Public instances
    url: https://cryptpad.org/instances/
    publisher: CryptPad
  - title: Chinese (Traditional Han script)
    url: https://weblate.cryptpad.org/projects/cryptpad/app/zh_Hant/
    publisher: CryptPad Weblate
  - title: Chinese (Simplified Han script)
    url: https://weblate.cryptpad.org/projects/cryptpad/app/zh_Hans/
    publisher: CryptPad Weblate
  - title: Japanese
    url: https://weblate.cryptpad.org/projects/cryptpad/app/ja/
    publisher: CryptPad Weblate
  - title: Korean
    url: https://weblate.cryptpad.org/projects/cryptpad/app/ko/
    publisher: CryptPad Weblate
  - title: cryptpad.fr/api/config
    url: https://cryptpad.fr/api/config
    publisher: CryptPad
  - title: Is https://cryptpad.fr blocked in mainland China?
    url: https://en.greatfire.org/https/cryptpad.fr
    publisher: GreatFire
    date: 2026-09-18
  - title: https://cryptpad.fr (GreatFire API)
    url: https://en.greatfire.org/api/url/https/cryptpad.fr
    publisher: GreatFire
    date: 2026-09-18
  - title: Is https://github.com blocked in mainland China?
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
    date: 2026-09-27
authors:
  - anoni-net

---

CryptPad published its summer 2026 status on 15 September, covering a new security policy, post-quantum research and a support change on cryptpad.fr, its flagship instance. CryptPad is an AGPL-3.0 end-to-end encrypted suite for co-editing documents and spreadsheets in the browser. You can use a public instance or host your own. Users of public instances need not change anything, while self-hosting administrators should watch for upgrades.

According to the June post-mortem, the server did not rate-limit WebSocket connections, the channel through which the browser and server exchange data, so repeatedly sending frames could exhaust its resources. On 28 January cryptpad.fr was hit by a distributed denial-of-service attack exploiting that gap, and the resulting outage was resolved in under three hours. The fix shipped in 2026.2.1 on 27 March.

The team had intended a 90-day embargo, but the reporter disputed it because the previous policy did not state it clearly. The CVE was published 34 days after that release. The new policy, published in June, keeps a CVE private for at least 90 days after the fixed release.

For post-quantum cryptography, the team chose NIST's ML-KEM, used to exchange keys, and ML-DSA, used for digital signatures. In experiments the two were combined with CryptPad's existing public-key cryptography in a hybrid way. Most of CryptPad ran smoothly, but some parts became too slow to use. According to the post, a draft adding both algorithms to the browser's Web Cryptography API should be two orders of magnitude faster than an external library.

cryptpad.fr will drop French-language support because the support team no longer has a French speaker. An Autumn Release bundling two releases' worth of improvements is coming, with no release date announced as of 29 September.

## Perspective {#perspective}

CryptPad encrypts documents in the browser, and the server has no access to their content. The user guide lists several trust assumptions, including that the instance runs the same code as published on GitHub and that collaborators do not forward sharing links to others. When they all hold, administrators cannot read or modify your documents. The guide also states that CryptPad offers only weak anonymity, since the instance can see your IP address and browser, and points to Tor for stronger guarantees.

A fix takes effect only once an instance's administrators upgrade. Under the security policy, the 90-day embargo gives them time to do so before the vulnerability is published and attackers may start exploiting it. The public instance list only includes instances that pass checks for an up-to-date version, so it is a good place to start when choosing one.

The draft is maintained by the WICG, a W3C community group for new specifications, and as of 29 September it was not on the W3C standards track. Browser support may make a post-quantum CryptPad more realistic. The team has already restructured the code for crypto-agility, so cryptographic libraries can be swapped more easily.

As of 29 September, CryptPad's Weblate shows the interface fully translated into Traditional and Simplified Chinese, 96.6% into Japanese and only 5.8% into Korean. The user guide has a Japanese edition but no Chinese or Korean one. The support page shows which languages an instance's administrators use, and the guide suggests an online translator when needed.

In mainland China, GreatFire rates `https://cryptpad.fr` as not blocked as of 29 September, based on a single test on 18 September whose connection was refused. Since late August GreatFire no longer counts refusals as evidence of blocking. The hosts the editor also needs, such as `api.cryptpad.fr` and `sandbox.cryptpad.info`, had not been tested, so as of 29 September there was no reliable measurement. GitHub, where the source code and releases are published, showed interference in 69% of 54 conclusive tests over the 90 days to 27 September.

To try it, open cryptpad.fr or another listed instance in a browser with JavaScript enabled. All 13 instances on the public list are hosted in Europe or North America as of 29 September. Without an account you can still co-edit documents, but you cannot upload images, videos or PDFs, and a document unused for three months is no longer kept.

Registering needs only a username and password, with no email address. Because of the encryption, administrators cannot view, retrieve or reset a password, so the guide advises noting it somewhere safe.

According to the post-mortem, administrators running CryptPad behind nginx with a variation of the official advanced configuration should switch to the latest example configuration as soon as possible, since it adds rate limiting. Severity is now scored with CVSS 4.0, and release notes list only the highest score among fixed vulnerabilities plus a notice to upgrade. Each version is supported for 90 days, and the recommended version is always the latest release, which as of 29 September was 2026.5.1 from 26 May.
