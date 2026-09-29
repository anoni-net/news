---
title: CryptPad's summer 2026 status and the post-quantum bottleneck
description: CryptPad, an end-to-end encrypted collaboration suite, has a new security policy that keeps vulnerability details private for at least 90 days after a fix ships. Its post-quantum experiment left some features too slow to use until browsers support the algorithms natively. People on public instances need not change anything, while self-hosting administrators should keep up with releases.
date: 2026-10-06T07:00:00+08:00
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
  - title: Pricing
    url: https://cryptpad.org/pricing/
    publisher: CryptPad
  - title: cryptpad.fr/api/config
    url: https://cryptpad.fr/api/config
    publisher: CryptPad
  - title: Is https://cryptpad.fr blocked in mainland China?
    url: https://en.greatfire.org/https/cryptpad.fr
    publisher: GreatFire
    date: 2026-09-18
  - title: Is https://github.com blocked in mainland China?
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
    date: 2026-09-27
authors:
  - anoni-net

---

CryptPad published its summer 2026 status on 15 September, covering a new security policy, results from its post-quantum research and a support change on its flagship instance, cryptpad.fr. CryptPad is an end-to-end encrypted collaboration suite, licensed under AGPL-3.0, for editing documents and spreadsheets together in the browser, on a public instance or a self-hosted one. People using public instances need not change anything, while administrators who self-host should watch the upgrade schedule.

The policy, published in June, keeps a CVE private for at least 90 days after the fixed release so that instances have time to upgrade, and scores severity with CVSS 4.0. Fixed vulnerabilities are not listed in release notes, and the policy recommends always running the latest release, which comes out quarterly. According to the June post-mortem, the server did not rate-limit WebSocket frames, and on 28 January cryptpad.fr was hit by a distributed denial-of-service attack exploiting that gap. The fix shipped in 2026.2.1 on 27 March.

For post-quantum cryptography, the team chose NIST's ML-KEM and ML-DSA and, in experiments, swapped them in for CryptPad's public-key cryptography in a hybrid way. Most of CryptPad ran smoothly, but some parts became too slow to use. According to the post, a draft that adds both algorithms to the browser's Web Cryptography API would be two orders of magnitude faster than an external library. cryptpad.fr will drop French-language support because its support team no longer has a French speaker, and an Autumn Release is coming with no date given.

## Perspective {#perspective}

Encryption happens in the browser, and CryptPad's user guide lists as a trust assumption that the instance runs the same code as published on GitHub. Under that assumption, its administrators cannot read or modify your documents. The guide also states that CryptPad offers only weak anonymity, since the instance can see your IP address and browser, and points to Tor for stronger guarantees. The public instance list only includes instances that pass checks for an up-to-date version.

As of its 14 September draft, the WICG proposal is not on the W3C standards track, and post-quantum CryptPad becomes realistic only once browsers implement it. The team has already restructured the code for crypto-agility, so cryptographic libraries can be swapped more easily.

As of 29 September, CryptPad's Weblate shows the interface fully translated into Traditional and Simplified Chinese, 96.6% into Japanese and only 5.8% into Korean. The user guide has a Japanese edition but no Chinese or Korean one. The support page shows which languages an instance's administrators use, and the guide suggests an online translator when needed.

All 13 instances on the public list are hosted in Europe or North America as of 29 September. CryptPad's pricing page lists control over where the encrypted data is stored as one reason to run your own instance, which is the option for anyone who wants the data kept in a particular Asian jurisdiction.

In mainland China, GreatFire's test of `https://cryptpad.fr` on 18 September connected normally, but it was the only conclusive test in 90 days. Hosts the editor also needs, such as `api.cryptpad.fr` and `sandbox.cryptpad.info`, had not been tested as of 29 September. GitHub, where the source code and releases are published, showed interference in 69% of 54 conclusive tests over the 90 days to 27 September.

To try it, open cryptpad.fr or another listed instance in a browser with JavaScript enabled. Without an account you can still create and co-edit documents, but a document unused for three months is no longer kept. Registering needs only a username and password, with no email address, so administrators cannot reset a lost password. Self-hosting administrators can apply the rate limits from the June post-mortem to their nginx configuration, and as of 29 September the latest stable release is 2026.5.1, from 26 May.
