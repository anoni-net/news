---
title: F-Droid 2.0 and Google's Android developer verification
description: F-Droid, the open-source Android app store, released 2.0, a rewrite that requires Android 7, on 24 September. From 30 September Google began requiring apps on seven stores in Brazil, Indonesia, Singapore and Thailand to be registered by identity-verified developers, with a global expansion to certified Android devices planned for 2027. As of 2 October, installing apps from F-Droid is unaffected anywhere.
date: 2026-10-09T00:00:00+08:00
slug: fdroid-2-android-developer-verification
categories:
  - censorship
sources:
  - title: "F-Droid 2.0: A New Chapter for Android Freedom"
    url: https://f-droid.org/en/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html
    publisher: F-Droid
    date: 2026-09-24
  - title: Android developer verification
    url: https://developer.android.com/developer-verification/guides
    publisher: Google
    date: 2026-08-18
  - title: Frequently asked questions | Android developer verification
    url: https://developer.android.com/developer-verification/guides/faq
    publisher: Google
    date: 2026-09-30
  - title: Learn about Android developer verification
    url: https://support.google.com/android/answer/17065026
    publisher: Google
  - title: Register your app on open source platforms
    url: https://developer.android.com/developer-verification/guides/open-source-app-registration
    publisher: Google
    date: 2026-09-30
  - title: "Android developer verification: Building a safer ecosystem together"
    url: https://android-developers.googleblog.com/2026/06/android-developer-verification.html
    publisher: Google
    date: 2026-06-18
  - title: A new layer of security for certified Android devices
    url: https://android-developers.googleblog.com/2025/08/elevating-android-security.html
    publisher: Google
    date: 2025-08-25
  - title: "Breaking Up with Google Play: Why Conversations Is Now Free"
    url: https://gultsch.de/posts/breaking-up-with-google-play/
    publisher: Conversations
    date: 2026-09-24
  - title: F-Droid and Google's Developer Registration Decree
    url: https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html
    publisher: F-Droid
    date: 2025-09-29
  - title: An Open Letter Opposing Android Developer Verification
    url: https://f-droid.org/en/2026/02/24/open-letter-opposing-developer-verification.html
    publisher: F-Droid
    date: 2026-02-24
  - title: What We Talk About When We Talk About Malware
    url: https://f-droid.org/en/2026/07/01/adv-malware.html
    publisher: F-Droid
    date: 2026-07-01
  - title: Keep Android Open
    url: https://keepandroidopen.org/
    publisher: Keep Android Open
  - title: F-Droid
    url: https://f-droid.org/en/packages/org.fdroid.fdroid/
    publisher: F-Droid
  - title: Use Google Play Protect to help keep your apps safe & your data private
    url: https://support.google.com/googleplay/answer/2812853
    publisher: Google
  - title: Piloting new ways to protect Android users from financial fraud
    url: https://security.googleblog.com/2024/02/piloting-new-ways-to-protect-Android-users-from%20financial-fraud.html
    publisher: Google
    date: 2024-02-06
  - title: "OONI Explorer: f-droid.org, China"
    url: https://explorer.ooni.org/chart/mat?probe_cc=CN&test_name=web_connectivity&domain=f-droid.org&since=2026-06-01&until=2026-10-02&axis_x=measurement_start_day
    publisher: OONI
  - title: F-Droid 镜像使用帮助
    url: https://mirrors.tuna.tsinghua.edu.cn/help/fdroid/
    publisher: TUNA, Tsinghua University
  - title: Country availability for Google Play apps & digital content
    url: https://support.google.com/googleplay/answer/2843119?hl=en
    publisher: Google
authors:
  - anoni-net
---

F-Droid, an Android app store that carries only open-source apps, released version 2.0 on 24 September, a full rewrite of its client that requires Android 7. From 30 September, Google began requiring apps on Google Play and six phone makers' stores in Brazil, Indonesia, Singapore and Thailand to be registered by developers who have verified their identity, and plans to extend the requirement to all certified Android devices worldwide in 2027. As of 2 October, installing apps from F-Droid or directly from a website is unaffected everywhere.

According to F-Droid, its team reviews each app's public source code for ads and trackers before building and publishing it. Version 2.0 is rebuilt in Kotlin and Jetpack Compose with three tabs, installs app updates automatically by default while keeping existing preferences, and improves search in Chinese, Japanese and Korean. Version 2.0 has been through an independent security review, and the announcement says the full report will be published once it is cleared for publication.

F-Droid's 2.0 announcement recommends Tor VPN in place of the old "Use Tor" option, which became generic proxy settings. The panic-triggered app wipe was removed for the time being, and the announcement advises people who rely on it to postpone updating. As of 2 October the download on F-Droid's homepage is 2.0.1, while the package page still labels 2.0 as beta and suggests 1.23.2.

On 24 September, the developer of the open-source messaging app Conversations wrote that Google Play had repeatedly rejected the app's updates and twice removed it, and that one update had been waiting 14 days for review when the post was published. The developer argues that Google does not distinguish feature updates from security updates and that delaying security updates is dangerous. The post says F-Droid has become the app's main channel, with reproducible builds signed by the developer's own key. As of 2 October the previously paid Google Play version is free. As of the same date we had found only the developer's account of Google Play's review process.

Google's verification asks developers to prove their identity and register package names with an APK signed by their private key. As of 2 October, Google's FAQ says the first phase covers only the seven participating stores, and that other stores and sideloading (installing outside a store) are not affected. Under Google's plan, from 2027 unregistered apps on certified devices can be installed only with the developer tool ADB or through what Google calls the advanced flow.

The advanced flow involves turning on developer mode, confirming no one is coaching you, restarting and re-authenticating, then waiting one day before confirming with a fingerprint, face or PIN to allow unverified apps for 7 days or indefinitely. Google's help page says the requirement does not apply to devices running AOSP (the Android Open Source Project), uncertified devices or regions where Google Mobile Services are unsupported.

## Perspective {#perspective}

The two models answer "can I trust this app?" differently. Google asks developers to prove who they are, while F-Droid relies on public source code and signs apps with its own key, or with the original developer's key when the build is reproducible. Under Google's rules, only the developer can register a package name. F-Droid wrote in September 2025 that it cannot require developers to register with Google or take over the package names of the open-source apps it distributes.

Google's August 2025 announcement says its own analysis found over 50 times more malware from internet-sideloaded sources than on Google Play, and that the first phase targets countries specifically affected by fraudulent app scams. In July 2026 F-Droid argued that the Android Developer Console terms let Google terminate accounts for distributing malware without defining the word anywhere in the document.

Keep Android Open, a campaign joined by free software and digital rights groups, counts nine steps in the advanced flow and notes that the flow runs through Google Play services rather than Android itself, which in its view means Google can change it at any time. Google's FAQ says the one-day wait exists to break the urgency of scammers coaching victims over a live call, that developer mode need not stay on afterwards, and that ADB installs are not subject to the wait.

In an open letter in February 2026, F-Droid advised developers against signing up, now or ever. F-Droid's 2025 statement said the requirement would end F-Droid and similar open-source distribution as they work today. Google has published a registration guide for open-source platforms: developers register package names under their own accounts, and platforms that re-sign apps add their key's fingerprint. The guide says users then keep today's install experience.

Three of the four first-phase countries are in Southeast Asia. Google's 2025 announcement quotes Indonesia's Ministry of Communications and Digital Affairs calling the plan a "balanced approach", and Thailand's Ministry of Digital Economy and Society calling it a "positive and proactive measure". Singapore had already hosted a 2024 Google pilot, run with the Cyber Security Agency of Singapore, in which Play Protect blocked internet-sideloaded apps that request sensitive permissions. As of 2 October we could not find a public statement from the Singapore government on developer verification itself.

As of 2 October Google Play does not operate in mainland China, and Google's help page exempts regions where Google Mobile Services are unsupported without saying whether mainland China is one of them. Reaching F-Droid is a separate problem there. OONI, which measures internet censorship, recorded 1,506 tests of `f-droid.org` from mainland China between 1 June and 2 October 2026, of which 1,179 showed anomalies, 288 failed, 37 were normal and 2 were confirmed as blocked by OONI. A mirror run by Tsinghua University's TUNA association was in sync with the official repository on 1 October.

As of 2 October, people who install apps through F-Droid or a website do not need to change anything. Anyone who wants to try F-Droid can download the roughly 12.5 MB APK from its homepage and allow the browser to install unknown apps. As of 2 October the client is fully translated into Simplified Chinese, while 2.0's new category names are only about 40% translated into Traditional Chinese.

To see whether a phone would fall under the 2027 rules, open the Google Play Store, tap the profile icon, then Settings and About, and check for Play Protect certification. On a certified phone, installing apps from unregistered developers would mean turning on the advanced flow a day ahead, and switching it off later stops those apps from updating. As of 2 October Google had published no month or country order for the 2027 expansion.
