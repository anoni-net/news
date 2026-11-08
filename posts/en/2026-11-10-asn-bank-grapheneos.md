---
title: Wero payments and Play Integrity checks in the Dutch ASN Bank app
description: According to user reports, ASN Bank's Android app in the Netherlands has, since version 1.36.3 (updated in mid-October), intermittently blocked Wero payments on systems without Google certification such as GrapheneOS, while the app itself still opens and shows accounts. As of 8 November we could find no announcement from ASN. People planning to switch to GrapheneOS can take it as an example of a bank moving a payment feature onto Google's check.
date: 2026-11-10T00:00:00+08:00
slug: asn-bank-grapheneos
categories:
  - finance
regions:
  - NL
sources:
  - title: ASN Bank
    url: https://github.com/PrivSec-dev/banking-apps-compat-report/issues/105
    publisher: GitHub
  - title: SNS Bank (De Volksbank) / ASN / Wero
    url: https://github.com/PrivSec-dev/banking-apps-compat-report/issues/1137
    publisher: GitHub
    date: 2026-10-21
  - title: Sneller bestellen en betalen met iDEAL | Wero
    url: https://www.asnbank.nl/asn-app-en-asn-online-bankieren/veilig-bankierennew/sneller-bestellen-en-betalen-met-ideal-wero.html
    publisher: ASN Bank
  - title: Integrity verdicts | Play Integrity | Android Developers
    url: https://developer.android.com/google/play/integrity/verdicts
    publisher: Android Developers
  - title: Attestation compatibility guide | Articles | GrapheneOS
    url: https://grapheneos.org/articles/attestation-compatibility-guide
    publisher: GrapheneOS
  - title: Usage guide | GrapheneOS
    url: https://grapheneos.org/usage#banking-apps
    publisher: GrapheneOS
  - title: Banking Applications Compatibility with GrapheneOS
    url: https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/
    publisher: PrivSec
    date: 2022-01-26
  - title: IDeal eind 2027 volledig vervangen door nieuw betalingssysteem Wero
    url: https://www.security.nl/posting/883786
    publisher: Security.nl
    date: 2025-04-11
  - title: Learn about devices & services available in your region
    url: https://support.google.com/store/answer/2462844?hl=en
    publisher: Google Store Help
  - title: Is https://releases.grapheneos.org blocked in mainland China?
    url: https://en.greatfire.org/https/releases.grapheneos.org
    publisher: GreatFire
  - title: Anti-Malware Security Features
    url: https://www.dbs.com.hk/personal/online-security/general-digibank-security-malware-jailbroken-device.page
    publisher: DBS Hong Kong
authors:
  - anoni-net
---

According to user comments on a GitHub project that tracks banking app compatibility, the Android app of Dutch bank ASN Bank has, since version 1.36.3 was released in mid-October, intermittently blocked Wero payments on systems without Google certification, such as GrapheneOS (a privacy-hardened phone operating system built on the Android Open Source Project). As of 8 November we could find no announcement from ASN, and what is known comes from support and complaint replies that users have posted. The reports so far involve only ASN and SNS Bank, which also belongs to de Volksbank, and one SNS Bank app user wrote that the app still opens and shows accounts but can no longer pay with Wero. Readers outside the Netherlands will not run into this directly, but people planning to switch to GrapheneOS can take it as an example of a bank moving a payment feature onto Google's check.

iDEAL is a common way to pay in Dutch online shops. Security.nl reported in April 2025, citing what Wero's operator EPI (European Payments Initiative) told the Dutch newspaper *AD*, that Wero is to replace iDEAL completely by the end of 2027. Wero is built into each bank's app and is also available as a standalone app. ASN's help page says iDEAL is gradually becoming Wero from 2026, and online shops will show the name "iDEAL | Wero".

PrivSec's compatibility list names ASN as "ASN Bank (De Volksbank)", and one reporting user described ASN and SNS Bank as the same app under different branding. According to users, the message the app shows when a payment is blocked uses the "iDEAL | Wero" name and says the phone or app installation does not meet the bank's security requirements. On the same version some people paid successfully, and others reported that it worked only some of the time. Reporters describe the old and new payment flows separately: one user wrote that the old iDEAL | Wero flow goes through, while the new Wero flow fails Play Integrity, a Google service that lets apps check the device and system they run on.

According to a reply from ASN's IT support that a user posted, GrapheneOS is not supported for Wero, and the device has to meet Wero's security requirements. Several users posted almost identical replies to their complaints. The reason given in them is that iDEAL | Wero relies on the standard security checks of mainstream operating systems, and alternative systems bypass or replace these built-in protections, so iDEAL | Wero cannot guarantee that transactions are secure. The replies also state that ASN is looking with iDEAL | Wero into whether alternative operating systems could be supported in future, but cannot make any commitment for now.

Users also wrote to EPI. In a reply reposted by one user, EPI describes its current focus as supporting the most widely used mobile banking platforms and devices, and acknowledges that this may exclude people who do not use mobile banking and people who prefer systems and devices outside the Apple and Android ecosystems. As of 8 November we could find no public version of these letters.

## Perspective {#perspective}

According to the Android developer documentation, Play Integrity returns verdicts at several levels. Basic integrity (MEETS_BASIC_INTEGRITY) only requires passing basic system integrity checks; the bootloader (the program that loads the operating system at startup) may be unlocked, and the device need not be certified. Device integrity (MEETS_DEVICE_INTEGRITY) requires the app to run on a "genuine and certified Android device", and from Android 13 also requires hardware-backed proof that the bootloader is locked and that a certified manufacturer image is loaded. GrapheneOS is not mentioned in the documentation, and it is our inference from the device integrity conditions that a system without Google certification cannot obtain that verdict.

GrapheneOS's usage guide states that it passes the basic integrity check but is not certified by Google. GrapheneOS does not intend to work around the check, on the grounds that any workaround would break again whenever the check is improved.

We could find no official information on which level ASN requires. One user running LineageOS (another uncertified Android system) reported passing basic integrity and failing device integrity, with only Wero transfers not working (a single case). According to user reports not confirmed by the banks, the Triodos and N26 apps can make Wero payments on GrapheneOS, and Wero can be set up in bunq.

According to a later reply reposted by a user, EPI explained why it uses Play Integrity. By the letter's account, Android hardware key attestation can verify that a key was generated in a hardware environment kept apart from the main system, such as a TEE or StrongBox, and has never left it, but cannot verify the integrity of the calling app or of the running operating system. Play Integrity combines device, system and app signals in a signed token that EPI's backend server verifies. The conclusion in the letter is that hardware key attestation on its own cannot provide the verification EPI's risk and fraud models require.

GrapheneOS, for its part, argues in its attestation compatibility guide that banks should use the standard Android hardware attestation API and add GrapheneOS's published official signing keys to an allowlist. According to the guide, this API can verify the hardware, firmware, operating system and app, and the key certificates it produces carry the app's ID, signing key fingerprint and version number, along with the fingerprint of the system's verified boot key. In the guide's assessment, hardware attestation is stronger than Play Integrity and does not depend on Google Play services or Google's servers, and Play Integrity's highest level, strong integrity (MEETS_STRONG_INTEGRITY), is itself built on hardware key attestation. The two sides give different accounts of what the same API can verify, and we have not checked which is correct.

Only one user wrote that the old flow works, and others report that it works only some of the time, so our inference is that it should not be treated as a reliable option. Several users have already complained to ASN and EPI, and GrapheneOS's guide encourages users to write to app developers with a link to the guide.

People planning to switch to GrapheneOS can first check where the banking and payment apps they use stand on PrivSec's compatibility list. The list is built from community reports, GrapheneOS makes no guarantee about its contents, and it includes many banking and payment apps from Taiwan. As of 8 November the ASN entry still carried no note (the list was last updated on 20 October, a day before the first Wero report), so the list may not yet reflect the app update.

GrapheneOS's attestation compatibility guide lists Pixel phones as the supported devices. Google Store's help page, as we checked it on 23 October, lists India, Japan, Singapore and Taiwan as the places in Asia where Pixel phones can be bought from Google Store, and does not include mainland China, Hong Kong, Macau or South Korea; the page covers Google Store only, not other retailers or carriers. In mainland China, GreatFire's Great Firewall measurements have recorded interference with GrapheneOS's update server, `releases.grapheneos.org`, since 31 January 2026, although only one test in the 90 days before 2 October produced a conclusive result.

PrivSec's list, as updated on 20 October, has sections for Taiwan, Hong Kong, Japan and mainland China, and the only entry among them with a Play Integrity note is one Japanese app, which according to the list cannot be installed from Google Play because of the check. The other entries in those sections carry no Play Integrity note, and the list records what users report about compatibility, not any bank's policy. We could find no public rule on banking apps detecting rooted or uncertified systems from Taiwan's Financial Supervisory Commission, the Hong Kong Monetary Authority or Japan's Financial Services Agency, and could not obtain the full text of the People's Bank of China's 2019 security standard for mobile financial apps (JR/T 0092-2019) to check whether it contains one. The only Hong Kong statement on rooted devices we found is a single bank's page: DBS Hong Kong suggests that people with a rooted or jailbroken device try a factory reset, or set up its mobile banking app on another device.

We can also infer that keeping a separate Google-certified phone just for payments is another option, and some users mentioned that having a spare phone left them less affected. The cost is one more device to update and look after, and payments on that phone still have to pass Google's check.
