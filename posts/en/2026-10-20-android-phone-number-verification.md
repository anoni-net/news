---
title: Automatic phone number verification on Android and the linking of Google accounts
description: Android phones verify phone numbers automatically by default and add them to every Google Account signed in on the phone, including work and secondary accounts. Verification can be turned off in settings, but according to Android Authority, numbers already added have to be removed from each account one by one. As of 18 October, we had not seen a public response from Google.
date: 2026-10-20T00:00:00+08:00
slug: android-phone-number-verification
categories:
  - tracking
sources:
  - title: Manage phone number verification on your device
    url: https://support.google.com/android/answer/7521240?hl=en
    publisher: Android Help
  - title: 在裝置上管理電話號碼驗證
    url: https://support.google.com/android/answer/7521240?hl=zh-Hant
    publisher: Android 說明
  - title: "PSA: Google is silently linking your phone number across all signed-in accounts"
    url: https://www.androidauthority.com/google-auto-phone-number-verification-android-3723117/
    publisher: Android Authority
    date: 2026-10-14
  - title: Change the phone number on your account & how it's used
    url: https://support.google.com/accounts/answer/3463280?hl=en
    publisher: Google Account Help
  - title: 變更帳戶中的電話號碼與其用途
    url: https://support.google.com/accounts/answer/3463280?hl=zh-Hant
    publisher: Google 帳戶說明
  - title: Learn how Google Play services can use your SMS & MMS messages
    url: https://support.google.com/android/answer/10641045?hl=en
    publisher: Android Help
  - title: 瞭解 Google Play 服務運用簡訊和多媒體訊息的方式
    url: https://support.google.com/android/answer/10641045?hl=zh-Hant
    publisher: Android 說明
  - title: Learn how Google Play services can use your call logs
    url: https://support.google.com/android/answer/10635223?hl=en
    publisher: Android Help
  - title: 瞭解 Google Play 服務運用通話記錄的方式
    url: https://support.google.com/android/answer/10635223?hl=zh-Hant
    publisher: Android 說明
  - title: Google 隱私權政策
    url: https://policies.google.com/privacy?hl=zh-TW
    publisher: Google
    date: 2026-10-16
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
  - title: Real-name Registration Programme for Subscriber Identification Module (SIM) Cards
    url: https://www.ofca.gov.hk/en/consumer_focus/guide/hot_topics/sim_registration/index.html
    publisher: Office of the Communications Authority
  - title: Services-Based Operations (Individual) Licence
    url: https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/licensing/telecommunication/services-based-operations-licence/sbotemplate.pdf
    publisher: IMDA
    date: 2025-12-01
authors:
  - anoni-net
---

Android Authority reported on 14 October that Android phones verify phone numbers automatically and add them to every Google Account signed in on the phone, including work and secondary accounts. According to Google's Android Help page "Manage phone number verification on your device", the feature is on by default and applies to both current and future accounts and phone numbers. Android Authority reports that the on-by-default wording was added to the page between August and October 2025, and we could not find an earlier version of the page to compare. Android Authority has asked Google for comment, and as of 18 October we had not seen a public response.

Any Google Account signed in on an Android phone gets the number, so people who use several accounts on one phone end up with those accounts tied together by the same number. Per the same help page, verification keeps features such as signing in with a phone number, account recovery, emergency location, finding a lost device, RCS (the newer messaging format that succeeds SMS) and Quick Share working. Google and the carrier periodically reverify the numbers, and carrier charges may apply.

Two Google Play services help pages describe how Google Play services may send and access SMS messages and access call logs in the background to discover and verify the number. The English versions of both pages read "If you opt-in to phone number verification", while the Traditional Chinese versions render it as 如果您啟用電話號碼驗證功能 ("if you turn on phone number verification"). The opt-in wording does not match the on-by-default description, and neither page explains the difference.

The Google Account Help page "Change the phone number on your account & how it's used" lists three uses for a number once it is on an account: sign-in and account recovery, helping people find and contact you through Google services, and showing more relevant ads when "Better ads & Google services" is on. Google's privacy policy, in effect from 16 October, lists the same uses, and the account help page adds that Google does not sell personal information, including phone numbers.

According to the device help page, turning on phone number verification also turns on Better sharing on Google, which makes it easier for people to send photos and start video calls through the number. With several accounts on the same phone, this setting is on for only one of them.

## Perspective {#perspective}

Several accounts on one phone are often a personal and a work account, or an account deliberately kept apart from someone's real identity. In the help page's example, a newly added Google Account is linked to every number on the device, and a new number is added to every account. Our inference is that once a number is on an account, anyone who can obtain both the Google Account data and the carrier's registration records, such as authorities making a lawful request, can match the account to the identity registered to the number. Real-name rules for SIM cards differ from place to place, and so does how much identity data sits behind a number.

We are a community based in Taiwan, where Article 77 of the Regulations for Administration of Mobile Broadband Businesses (amended 3 September 2019) requires operators to record each subscriber's name, address and two identity document numbers before activation, prepaid cards included. Operators must keep the records for at least a year after the contract ends and provide them when authorities make an inquiry under the law. In Hong Kong, the Telecommunications (Registration of SIM Cards) Regulation took effect on 1 September 2021, and since 1 March 2022 every SIM service plan and prepaid card has required real-name registration before activation. According to the Office of the Communications Authority, individuals register their name in English and Chinese, date of birth, Hong Kong identity card number and a copy of the card.

In Singapore, the requirement is set in the licence template that the Infocomm Media Development Authority (IMDA) issues to operators, which is not the text of a statute. Version 10 of the template, dated 1 December 2025, requires operators to register prepaid subscribers' name, address, identity document number, contact details and service identifier, and to check and copy the identity document for purchases made in Singapore. The register must be kept for at least 12 months after the service ends, and operators may not provide prepaid service to anyone under 15.

According to Google's help page, account recovery, signing in with a phone number, emergency location and other features depend on verification, so turning it off may affect them, which is our inference from the help page. Google's privacy policy lists carrier name and phone number among the mobile network information it collects. Based on that list, we infer that Google may still obtain the phone's number after verification is turned off and the number is removed. We could not find out whether Google links the accounts internally as a result.

If you are signed in to several accounts on one Android phone and do not want them tied together by the number, go to Settings → Google → All services → Privacy & security → Phone number verification and turn it off. According to Android Authority, turning it off only stops future linking, and numbers already added have to be deleted from each account under Personal info → Phone (Google's help page does not say whether turning it off removes them). You can keep the number on the account you rely on for recovery and remove it only from the accounts you want kept apart, which is our inference. The device and Google Account help pages both have Traditional Chinese versions, whose footers note that they may contain AI-translated content.

Android Authority cites user reports on Reddit that the toggle switched back on after being turned off, which the author had not reproduced by publication. Given those reports, we suggest checking the setting again some time after turning it off.
