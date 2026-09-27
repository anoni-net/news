---
title: Tracking pixels that sent doctors’ appointments to social platforms
description: The Markup and Agência Pública found that the booking platform Doctoralia sent specialties, doctors’ names and appointment times from its Latin American sites to Google, TikTok and LinkedIn.
date: 2026-10-04T07:00:00+08:00
slug: doctoralia-health-tracking-pixels
sources:
  - title: How TikTok and Google ended up with information about doctors’ appointments around the world
    url: https://themarkup.org/pixel-hunt/2026/09/14/how-tiktok-and-google-ended-up-with-information-about-doctors-appointments-around-the-world
    publisher: The Markup
    date: 2026-09-14
  - title: This is how you stop data trackers from sucking up your health data
    url: https://themarkup.org/the-breakdown/2025/06/17/this-is-how-you-stop-data-trackers-from-sucking-up-your-health-data
    publisher: The Markup
    date: 2025-06-17
  - title: Blacklight
    url: https://themarkup.org/blacklight
    publisher: The Markup
  - title: 個人資料保護法 第 6 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6
    publisher: 全國法規資料庫
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 全国人民代表大会
    date: 2021-08-20
authors:
  - anoni-net
---

Reporters at The Markup and Brazil's Agência Pública found, in an investigation published on 14 September, that Doctoralia, a healthcare booking platform, sent information about people's appointments to Google, TikTok, LinkedIn and other tech companies for advertising. Its parent company, Docplanner, operates in 13 countries. The sites examined were in Brazil, Colombia, Mexico and other Latin American countries.

In Brazil, a search for a gynaecologist sent the specialty to Google, and a completed booking also sent the doctor's name and the appointment date and time. In Colombia and Mexico, bookings with a dermatologist or psychologist sent the doctor's name and appointment time to LinkedIn and TikTok. Doctoralia also appeared to use Facebook trackers, though it sent less sensitive information to Meta in the cases The Markup reviewed. The tracking began before anyone entered a name or email address, often tying visitors to unique IDs. According to their responses to the reporters, Docplanner is conducting a technical and legal review, and Google's and LinkedIn's policies forbid such use on sensitive pages. TikTok did not respond.

## Perspective {#perspective}

A tracking pixel is a snippet an ad platform gives a website so that what visitors view and click is reported back. On a medical site, the specialty someone searches for or the doctor they book already reveals a lot about their health. Even Brazil's regulators disagree on this: the Federal Council of Medicine's position is that booking an appointment involves no medical confidentiality, while the health insurance agency treats the specialty and booking details as information that may reveal aspects of a person's health.

The same sites behaved differently by country. The Spanish version did not send searches to outside companies in The Markup's testing, and the German site offers a pop-up to switch off tracking cookies, while the Latin American sites only announced that cookies were in use. That suggests the differences come from how the operator configured each site.

Across Asia, laws treat health information as a special category, though none spell out booking data. Taiwan's Personal Data Protection Act, Article 6, bars collecting or using medical, health check and medical record data except in listed cases. Mainland China's Personal Information Protection Law lists medical and health information as sensitive personal information in Article 28 and requires separate consent to process it in Article 29. Whether a booking counts is left to interpretation, the same question Brazil's regulators disagree on.

Readers do not have to wait for regulators. To see which trackers a clinic's site loads, The Markup's Blacklight scanner checks a URL for data sent to TikTok, Google Analytics and others; only part of its code is open source.

In earlier tests on other health sites, The Markup found that switching Firefox's Enhanced Tracking Protection from Standard to Strict, turning on Safari's Advanced Tracking and Fingerprinting Protection, using the Brave or DuckDuckGo browsers, or installing Privacy Badger or uBlock Origin Lite blocked the trackers it examined, and all of these are free to install. A VPN or private browsing did not, and blocking third-party cookies in Chrome was not enough.
