---
title: Conditions for GrapheneOS support on the Pixel 11
description: GrapheneOS, a privacy-hardened mobile operating system, advised against buying the Pixel 11 in late August because it lacked the Memory Tagging Extension (MTE). In November GrapheneOS posted that Android 17 QPR2 has added MTE firmware support for the Pixel 11, and that it can support the phones once QPR2 reaches the Android Open Source Project and its port is complete. As of 14 November the Pixel 11 is not on the official supported list, and the recommended devices for purchase are still the Pixel 8 through the Pixel 10a.
date: 2026-11-16T00:00:00+08:00
slug: grapheneos-pixel-11
categories:
  - mobile
related:
  - title: GrapheneOS, a hardened mobile operating system
    url: https://anoni.net/docs/en/tools/grapheneos/
sources:
  - title: Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped
    publisher: GrapheneOS Discussion Forum
    date: 2026-08-29
  - title: 'GrapheneOS: "Our port to the Pixel 11 series was nearly comple…" - GrapheneOS Mastodon'
    url: https://grapheneos.social/@GrapheneOS/117596333575500952
    publisher: GrapheneOS
    date: 2026-11-11
  - title: 'GrapheneOS: "Our port to Android 17 QPR2 is nearly complete. P…" - GrapheneOS Mastodon'
    url: https://grapheneos.social/@GrapheneOS/117596341370458465
    publisher: GrapheneOS
    date: 2026-11-11
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3mzztj5fbk226
    publisher: GrapheneOS
    date: 2026-11-11
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3n277527yrk2u
    publisher: GrapheneOS
    date: 2026-11-13
  - title: 'GrapheneOS: "Motorola Signature 27 meets all of our official s…" - GrapheneOS Mastodon'
    url: https://grapheneos.social/@GrapheneOS/117570889454162312
    publisher: GrapheneOS
    date: 2026-11-06
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3mzogzkzr622p
    publisher: GrapheneOS
    date: 2026-11-06
  - title: '@grapheneos.org on Bluesky'
    url: https://bsky.app/profile/grapheneos.org/post/3mzqmjgfuxs2o
    publisher: GrapheneOS
    date: 2026-11-07
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#recommended-devices
    publisher: GrapheneOS
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases
    publisher: GrapheneOS
  - title: GrapheneOS translate to other languages - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/5030-grapheneos-translate-to-other-languages
    publisher: GrapheneOS Discussion Forum
  - title: Google introduces Pixel 11, Pixel 11 Pro and Pixel 11 Pro XL
    url: https://blog.google/products-and-platforms/devices/pixel/google-pixel-11-pro-xl/
    publisher: Google
    date: 2026-08-12
  - title: Learn when you'll get software updates on Google Pixel phones - Nexus Help
    url: https://support.google.com/nexus/answer/4457705?hl=en
    publisher: Google
  - title: Release notes | Android Developers
    url: https://developer.android.com/about/versions/17/qpr2/release-notes
    publisher: Android Developers
  - title: GrapheneOS Announces Pixel 11 Support Can Be Completed Now
    url: https://www.privacyguides.org/news/2026/11/12/grapheneos-announces-pixel-11-support-can-be-completed-now/
    publisher: Privacy Guides
    date: 2026-11-12
  - title: Learn about devices & services available in your region - Google Store Help
    url: https://support.google.com/store/answer/2462844?hl=en
    publisher: Google
authors:
  - anoni-net
---

GrapheneOS is a privacy-hardened mobile operating system built on Android's open-source code (we have covered its [clipboard read toggle](https://anoni.net/news/en/2026/10/grapheneos-clipboard-toggle/)), and as of 14 November neither its official supported device list nor its releases page includes the Pixel 11 series that Google launched in August. According to GrapheneOS's November posts on Bluesky, Android 17 QPR2 has added firmware support on the Pixel 11 for the Memory Tagging Extension (MTE, a hardware feature that detects and stops attacks exploiting memory errors). GrapheneOS can add the Pixel 11 only after the QPR2 source code is released to the Android Open Source Project (AOSP) and its own port is complete. This matters to people planning to buy a new phone for GrapheneOS, and to people who already own a Pixel 11 and want to switch to GrapheneOS.

According to GrapheneOS's announcement on its official forum on 29 August, the team had a partial port about a week after the Pixel 11 series went on sale on 20 August, but could not complete it because MTE support was missing in software and firmware, and potentially in hardware. In the announcement's words, "It appears Google cut an important security feature to save money", and MTE is the only unmet requirement the announcement names. GrapheneOS strongly recommended against buying the Pixel 11 and wrote that it might skip the whole series and shift its focus to upcoming Motorola devices.

The Pixel 11's security improvements are also listed in the same announcement, including post-quantum secure verified boot (ML-DSA, a signature scheme designed to resist quantum computers) and the new Titan M3 security chip. According to the announcement, the Titan M3 should make it harder to extract data from a phone that has been turned on but not yet unlocked for the first time, which helps people without a strong passphrase. Without MTE, security after the phone has been unlocked drops sharply ("losing MTE craters AFU security"). Per the same announcement, the Pixel 10 is cheaper, with similar hardware and MTE.

According to a GrapheneOS Bluesky post from 1 September quoted by Privacy Guides, the Pixel 11 hardware still has at least bare minimum MTE support. In that post GrapheneOS speculated that Google removed most of the hardware acceleration from the CPU cache to save money, which made MTE perform so poorly that it ended up fully disabled in firmware. GrapheneOS added in the same post that MTE "may still be usable".

In a post on 11 November, GrapheneOS wrote that Android 17 QPR2 has added MTE support for the Pixel 11 series and that it had confirmed this works with its own QPR2 port. In another post the same day, GrapheneOS described performance with MTE enabled as acceptable and comparable to previous Pixel generations. It also wrote there that the removal described in leaked information concerned designs Google did not end up using.

In a post on 13 November, GrapheneOS wrote that the Pixel 11 can be supported after Android 17 QPR2 is pushed to AOSP and its port to QPR2 is completed. What GrapheneOS is waiting for is the QPR2 source code reaching AOSP, and Google's QPR2 update to Pixel phones does not count (our inference from the wording of the post). As of 14 November, we could not find any record of QPR2 having reached AOSP.

In its 11 November post on QPR2 progress, GrapheneOS wrote that the port is nearly complete and that Pixel 11 support can be added after it ships for the already supported devices. According to the same post, completing support for Motorola's new Signature 27 is the main priority after QPR2, and since Pixel 11 support was essentially finished long ago, it can also ship after QPR2. As of 14 November, GrapheneOS had not announced a timeline for adding the Pixel 11. Privacy Guides ran the story under the headline "GrapheneOS Announces Pixel 11 Support Can Be Completed Now", while GrapheneOS's own posts still put support after QPR2 reaches AOSP and the port is finished.

As of 14 November, the account of the Pixel 11 and MTE comes from GrapheneOS alone. Google's Pixel 11 launch post of 12 August does not mention MTE, the Android Developers release notes for QPR2 have no entry on MTE, and we could not find any explanation from Google about MTE on the Pixel 11.

## Perspective {#perspective}

According to Privacy Guides, MTE is a hardware feature of ARM chips that assigns a tag to a region of memory and the same tag to the pointers that access it. When the two do not match, the code does not continue, which stops attacks that exploit memory safety bugs (such as reading or writing memory locations that should be off limits). According to GrapheneOS's forum announcement, MTE "greatly improves protection against nearly all remote exploits and many local exploits".

Per the same announcement, hardware MTE arrived with the Pixel 8 in October 2023. GrapheneOS began using it that month, and by the time of the announcement had it enabled across the entire base OS, including the kernel and every standard base OS process (it is temporarily disabled for a few device-specific processes). Android and the stock Pixel OS never turned it on by default, and Advanced Protection Mode in Android 16 enables it only for a few processes (how to turn on Advanced Protection is covered in [Known flaws exploited on older iOS and Android](https://anoni.net/news/en/2026/11/ios-android-exploits-lockdown/)). Also according to the announcement, Memory Integrity Enforcement (MIE) on the iPhone 17 is always enabled and is an implementation of MTE using the latest standard extensions.

Hardware memory tagging is on the list of requirements in GrapheneOS's FAQ for devices it will support in the future, alongside at least 5 years of updates and complete monthly Android Security Bulletin patches. In a Bluesky post on 7 November, GrapheneOS wrote that it needs MTE "to have industry standard protection against exploits when comparing to an iPhone" and has considered it required since the hardware shipped.

According to Google's help page on software updates, Pixel 8 and later phones get 7 years of OS and security updates starting from when the device first became available on the Google Store in the US, and the list includes the Pixel 11 series. Counting 7 years from launch, as the GrapheneOS FAQ does, we calculate that the Pixel 11 is covered until about August 2033; Google's page gives no end month. Pixel 11 owners who stay on the stock OS receive these updates as usual. In its 7 November post, GrapheneOS wrote that as of that day Google still used MTE only in Android's Advanced Protection Mode, which enables it for a small number of processes.

In a post on 6 November, GrapheneOS wrote that the Motorola Signature 27 meets all of its security requirements with Qualcomm's implementation of MTE, and that it will be able to provide 7 years of updates from launch for the phone. In another post the same day, it wrote that once the Pixel 11 is added there will be two current-generation device families meeting all of its security requirements.

For anyone buying a phone to install GrapheneOS, the devices the FAQ strongly recommends as of 14 November are the Pixel 8, 8 Pro, 8a, the Pixel 9 series, 9a, the Pixel 10 series and 10a. In the FAQ's support table each has a 7-year OEM minimum support period from launch, ending earliest for the Pixel 8 and 8 Pro in October 2030 and latest for the Pixel 10a in March 2033. As the FAQ puts it, GrapheneOS "can only fully provide security updates to a device provided that the OEM is releasing them". According to a moderator's reply on the GrapheneOS forum, checked on 23 October, the settings and apps GrapheneOS develops itself are in English only.

We, a community based in Taiwan, also checked where the Google Store sells these phones in Asia. As of 14 November, the places in Asia listed on Google Store Help for buying the Pixel 11, 11 Pro, 11 Pro XL and 11 Pro Fold from the Google Store are India, Japan, Singapore and Taiwan, the same four as for the Pixel 10 and 10a on that page. Mainland China, Hong Kong, Macau and South Korea are not on these lists. The page covers only the Google Store itself, not other retailers or carriers, and a buyer's shipping address must be in the same region as the Google Store site.

Pixel 11 owners do not need to change any settings, and the stock OS keeps updating as usual. Those who want to switch to GrapheneOS can watch for when Android 17 QPR2 is pushed to AOSP, and for when GrapheneOS's FAQ and releases page list the Pixel 11. By the comparison in the August forum announcement, the Pixel 10 is cheaper, with similar hardware and MTE, and it is a device GrapheneOS already supports. Its OEM support ends about a year earlier than our estimate for the Pixel 11 (August 2032 in the FAQ's table).
