---
title: AISeal, the isolated environment for on-device AI in Android 17
description: On 7 October Google described AISeal in Android 17, which keeps the personal data used by on-device AI in a protected virtual machine isolated from the operating system. According to the announcement, the first phase covers storing personal data, with model inference and AI agents to follow. As of 20 October, Google had not said which devices or regions have it enabled, and there is nothing in Google's announcement or help pages about settings that users need to change.
date: 2026-10-23T00:00:00+08:00
slug: android-aiseal-on-device-ai
categories:
  - mobile
sources:
  - title: Android's Next-Gen Enclave for On-Device AI
    url: https://blog.google/security/enabling-the-next-gen-enclave-architecture-for-on-device-ai-on-android/
    publisher: Google
    date: 2026-10-07
  - title: Android Virtualization Framework (AVF) overview
    url: https://source.android.com/docs/core/virtualization
    publisher: Android Open Source Project
  - title: Security
    url: https://source.android.com/docs/core/virtualization/security
    publisher: Android Open Source Project
  - title: Android’s pKVM Becomes First Globally Certified Software to Achieve Prestigious SESIP Level 5 Security Certification
    url: https://blog.google/security/android-pkvm-certified-sesip-level-5/
    publisher: Google
    date: 2025-08-12
  - title: core/java/android/aiseal - platform/frameworks/base - Git at Google
    url: https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-17.0.0_r1/core/java/android/aiseal/
    publisher: Android Open Source Project
  - title: Private Compute Services
    url: https://github.com/google/private-compute-services
    publisher: Google
  - title: Gemini Nano
    url: https://developer.android.com/ai/gemini-nano
    publisher: Android Developers
  - title: Android On-Device AI Gets a Security Bump With "Next-Gen" Enclaves
    url: https://www.privacyguides.org/news/2026/10/09/android-on-device-ai-gets-a-security-bump-with-next-gen-enclaves/
    publisher: Privacy Guides
    date: 2026-10-09
  - title: Google is building a “black box” for Android AI, but the agents aren’t inside yet
    url: https://www.digitaltrends.com/phones/google-is-building-a-black-box-for-android-ai-but-the-agents-arent-inside-yet/
    publisher: Digital Trends
    date: 2026-10-08
  - title: Android 17 Built a Sealed Room for On-Device AI
    url: https://blog.logcat.ai/2026/06/25/android-17-built-a-sealed-room-for-on-device-ai/
    publisher: logcat.ai
    date: 2026-06-25
  - title: Where you can use the Gemini web app
    url: https://support.google.com/gemini/answer/13575153?hl=en
    publisher: Google
  - title: Gemini mobile app availability
    url: https://support.google.com/gemini/answer/14579026?hl=en
    publisher: Google
  - title: Get personal suggestions on your Pixel with Magic Cue
    url: https://support.google.com/pixelphone/answer/16508057?hl=en
    publisher: Google
authors:
  - anoni-net
---

On 7 October, Google described on its official blog how AISeal (Android on-device AI seal) in Android 17 puts the personal data that on-device AI uses into a protected virtual machine isolated from the Android operating system. According to the announcement, it is designed so that personal data stays cryptographically isolated even if the whole operating system is compromised. The first phase covers only storing personal data, with model inference and AI agents (AI that carries out multi-step tasks on the user's behalf) to come later. As of 20 October, Google had not said which devices or regions have it enabled, and there is nothing in Google's announcement or help pages about settings that users need to change.

According to the announcement, AISeal is built on the Android Virtualization Framework (AVF) and pKVM, a hypervisor (the low-level software that partitions and isolates virtual machines). The protected space is designed to hold three kinds of services at once: an encrypted personal database, model inference running on the device, and AI agents that combine the two. In the announcement's example, an assistant queries the personal database and summarizes your schedule inside the isolated space, and outbound controls are designed to let only the final answer return to the operating system (something only possible once inference moves into AISeal). According to the Android Open Source Project (AOSP) documentation, even if the host (the Android system that normally runs apps) is compromised, it cannot read the protected virtual machine's memory.

On the chip side, according to the announcement, MediaTek has announced support on the Dimensity 9600 Pro, and Qualcomm's Snapdragon chipsets will support AISeal through AVF. pKVM itself received SESIP (a security evaluation scheme) Level 5 certification in 2025, described in the announcement as the highest vulnerability testing tier under ISO 15408 (the announcement does not say AISeal itself is certified). According to the source code tagged Android 17, AOSP already includes the AISeal framework. In the same source code, the service is off by default and only starts once the device property `service.aiseal.enable` is set to 1, a step that by our inference the phone maker takes.

## Perspective {#perspective}

Android's existing isolation consists of the app sandbox, SELinux policies and Private Compute Core. According to the Private Compute Services documentation, features inside Private Compute Core cannot connect to the network directly and reach it only through a set of open-source APIs. What AISeal adds is a layer of memory isolation carved out by the hypervisor. According to the AVF security documentation, the part of pKVM that runs at the hypervisor level is roughly 10,000 lines of code, against roughly 20 million for the whole Linux kernel (an attack surface three orders of magnitude smaller).

According to the same security documentation, companies that handle the supply chain, such as phone makers and chip vendors, still have to be trusted, and the host can affect whether a virtual machine runs normally. Encrypted storage, per the same document, has no rollback protection at the block level (there is no way to detect encrypted data being swapped back to an older version). These are design limits of pKVM and protected virtual machines, and by our inference they apply equally to AISeal, which is built on top of them.

According to a technical blog post analysing the Android 17 source code, the host can still see data at the moment it is collected, before it is stored in AISeal. By the same analysis, AISeal does not separate the data from the AI service provider the user chooses.

In the source code tagged Android 17, AISeal's management interface requires the `signature|privileged` permission, which by our inference ordinary third-party apps cannot obtain. Gemini Nano, Google's on-device model available to developers, runs in AICore, the system service that manages on-device models, and integrating AICore with AISeal is listed in the announcement as a future plan. Digital Trends cautioned that chip support for AISeal does not mean the assistant on a phone actually runs inside AISeal, since that depends on how the phone maker implements it.

According to Google's help pages, as of 20 October both the Gemini web app and the Gemini mobile apps are available in Hong Kong, Japan, Macau, Singapore, South Korea and Taiwan. Mainland China is missing from the mobile app list and limited to Workspace accounts on the web.

We found no list of the devices, countries or languages where AISeal is enabled in Google's announcement, the AOSP documentation or news coverage, so Gemini's availability in a place is no indication of AISeal there. Other features' regional lists are no guide either. According to its help page, Magic Cue, Pixel's personal suggestions feature, lists Japan but not Taiwan, Hong Kong, South Korea or mainland China, and nothing on that page says Magic Cue uses AISeal.

Readers do not need to change any settings now, and as of 20 October there is no user-facing switch in Google's announcement or help pages. What is worth watching is when Google or phone makers publish the devices and regions where AISeal is enabled, and when model inference and AI agents move into it.

Following Digital Trends' caveat, our inference is that when buying a phone you can check whether the maker's specifications and help pages state that AI features run inside AISeal. Per the technical blog analysis cited above, even with features running inside AISeal, data at the moment of collection and the AI service provider the user chooses remain outside the isolation.
