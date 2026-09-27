---
title: Pixel-only APIs in Android 17 QPR1
description: Android 17 QPR1 adds new APIs for app developers without releasing the source to AOSP, so non-Pixel phones and systems such as GrapheneOS wait until QPR2 in December.
date: 2026-09-28T07:05:00+08:00
slug: android-17-qpr1-pixel-only-apis
sources:
  - title: Android Open Source Project
    url: https://source.android.com/
    publisher: Google
  - title: Android 17 QPR1 is the first release since Android Honeycomb (3.x) adding new APIs for app developers without a release to the Android Open Source Project
    url: https://grapheneos.social/@GrapheneOS/117282080803799576
    publisher: GrapheneOS
    date: 2026-09-16
  - title: Android API Differences Report
    url: https://developer.android.com/sdk/api_diff/37.1/changes/changes-summary
    publisher: Android Developers
  - title: Google rolling out Android 17 QPR1 for Pixel
    url: https://9to5google.com/2026/09/15/android-17-qpr1-pixel/
    publisher: 9to5Google
    date: 2026-09-15
  - title: Android 16 QPR1's source code is now available on AOSP
    url: https://www.androidauthority.com/android-16-qpr1-source-code-available-3614853/
    publisher: Android Authority
    date: 2025-11-11
  - title: "Exclusive: Google will develop the Android OS fully in private, here's why"
    url: https://www.androidauthority.com/google-android-development-aosp-3538503/
    publisher: Android Authority
    date: 2025-03-26
  - title: Frequently Asked Questions
    url: https://grapheneos.org/faq
    publisher: GrapheneOS
  - title: GrapheneOS changelog
    url: https://grapheneos.org/releases
    publisher: GrapheneOS
  - title: Create Wear OS apps for China
    url: https://developer.android.com/training/wearables/creating-app-china
    publisher: Android Developers
  - title: "Huawei Mate 70 launch: HarmonyOS Next details, specs, price"
    url: https://www.cnbc.com/2024/11/26/huawei-mate-70-launch-harmonyos-next-details-specs-price-.html
    publisher: CNBC
    date: 2024-11-26
authors:
  - anoni-net
---

Android 17 QPR1, which Google began rolling out on 15 September to every Pixel from the Pixel 6 through the Pixel 11 series, adds new APIs for app developers at API level 37.1, including a new `android.hardware.hid` package. Its source code has not been released to the Android Open Source Project (AOSP). GrapheneOS points out that no release since Android 3.x has added new APIs without going through AOSP. Non-Pixel phones and AOSP-based systems will get them with Android 17 QPR2 in December.

GrapheneOS says it had ported its code to QPR1 before the release but does not yet have permission to ship it, so it is backporting Pixel firmware, kernel drivers and HALs to Android 17 instead. It also notes that the September Pixel Update Bulletin carries patches to standard Android components that were missing from the September Android Security Bulletin, and that a GPL source request it made on 1 September took more than two weeks to be answered.

## Perspective {#perspective}

This follows from how Google now ships Android. In March 2025 Google confirmed to Android Authority that Android development would move fully in private, with the internal branch restricted to companies holding a Google Mobile Services (GMS) licence. The AOSP site states that from 2026 source code is published only in Q2 and Q4. Android 16 QPR1 still reached AOSP, weeks late. As of 27 September, AOSP has only the Android 17 release branch and nothing for QPR1. Anyone building from AOSP, whether a phone maker without a GMS licence or a project like GrapheneOS, now works months behind Pixels, and non-Google makers who want patches on time need Google's security preview access, which GrapheneOS says it has through another manufacturer.

Across Asia, the effect depends on what a phone is built on. Google's own developer guide for China tells app makers to account for handsets without Google Play services pre-installed. Huawei's HarmonyOS NEXT, according to CNBC, reportedly no longer uses Android's open-source code at all, so the AOSP schedule does not bind it. For the other Android makers in the region, GrapheneOS notes that non-Google manufacturers can ship the yearly and QPR2 releases along with security backports. The QPR1 APIs therefore reach their phones only with QPR2 in December, and after that whenever each manufacturer pushes the update.

For privacy-focused users the options are narrow. GrapheneOS is released under OSI-approved open source licences, supports only Pixels officially, and has kept shipping updates through September, including a 17 September build that backported QPR1 modem firmware and a 19 September build adding matching carrier settings. GrapheneOS says it can ship some of the withheld patches early by reverse engineering them.

The project also says Pixels are now significantly harder to support than many other devices, and that upcoming Motorola phones will be easier because it will receive official firmware and driver code. Until those arrive, anyone who wants GrapheneOS still has to buy a Pixel, and the supported models are listed in the GrapheneOS FAQ.
