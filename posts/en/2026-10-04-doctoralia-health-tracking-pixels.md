---
title: Tracking pixels that sent doctors' appointments to social platforms
description: Doctoralia's sites in Brazil, Colombia, Mexico and elsewhere in Latin America sent specialties, doctors' names and appointment times to Google, TikTok and LinkedIn. Its parent company does not operate in Asia.
date: 2026-10-04T07:00:00+08:00
slug: doctoralia-health-tracking-pixels
sources:
  - title: How TikTok and Google ended up with information about doctors’ appointments around the world
    url: https://themarkup.org/pixel-hunt/2026/09/14/how-tiktok-and-google-ended-up-with-information-about-doctors-appointments-around-the-world
    publisher: The Markup
    date: 2026-09-14
  - title: Docplanner Group
    url: https://www.docplanner.com/
    publisher: Docplanner
  - title: This is how you stop data trackers from sucking up your health data
    url: https://themarkup.org/the-breakdown/2025/06/17/this-is-how-you-stop-data-trackers-from-sucking-up-your-health-data
    publisher: The Markup
    date: 2025-06-17
  - title: Blacklight
    url: https://themarkup.org/blacklight
    publisher: The Markup
  - title: the-markup/blacklight-collector
    url: https://github.com/the-markup/blacklight-collector
    publisher: GitHub
  - title: 個人資料保護法 第 6 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6
    publisher: 全國法規資料庫
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 全国人民代表大会
    date: 2021-08-20
  - title: Firefox 正體中文介面字串 preferences.ftl
    url: https://github.com/mozilla-l10n/firefox-l10n/blob/main/zh-TW/browser/browser/preferences/preferences.ftl
    publisher: Mozilla
  - title: Firefox en-US interface strings preferences.ftl
    url: https://github.com/mozilla-firefox/firefox/blob/main/browser/locales/en-US/browser/preferences/preferences.ftl
    publisher: Mozilla
  - title: 在 Mac 上的 Safari 中進行私密瀏覽
    url: https://support.apple.com/zh-tw/guide/safari/ibrw1069/mac
    publisher: Apple
  - title: Browse privately in Safari on Mac
    url: https://support.apple.com/guide/safari/browse-privately-ibrw1069/mac
    publisher: Apple
regions:
  - BR
  - CO
  - MX
authors:
  - anoni-net
---

The Markup, a US outlet, and Agência Pública, a Brazilian investigative nonprofit, reported on 14 September that the booking platform Doctoralia sent appointment information to Google, TikTok and LinkedIn for advertising from its sites in Brazil, Colombia, Mexico and elsewhere in Latin America. Parent company Docplanner lists 13 markets in Europe, Turkey and Latin America, none in Asia.

In Brazil, the site sent searched specialties such as gynaecology to Google, then the doctor's name and appointment time after a booking. In Colombia, it sent the doctor's name and appointment time for any specialist to LinkedIn, and bookings in Colombia and Mexico also went to TikTok. Tracking started before visitors entered a name or email. Doctoralia also appeared to use Facebook trackers, sending less sensitive information to Meta.

Doctoralia is based in Spain, under the EU's General Data Protection Regulation, and its Spanish site sent no searches to outside companies in testing. Docplanner's similar platform in Germany offers a pop-up to switch off tracking cookies, while the Latin American sites announced cookies without immediately offering a way to turn them off.

Docplanner wrote that the trackers measured its own social media campaigns and that it does not sell personal data. As of 14 September it was conducting a technical and legal review. LinkedIn said its policies prohibit its Insight Tag on pages collecting sensitive data, Google cited policies against collecting private health information, and TikTok did not respond.

## Perspective {#perspective}

A tracking pixel is code an ad platform gives a website. The visitor's browser sends what they view and click back to the platform, often with a unique ID, and social media companies say such IDs can be tied to a person's profile. On a medical site, the specialty someone searches for or the doctor they book can reveal aspects of their health.

Two Brazilian regulators disagree on whether this counts as health data. The Federal Council of Medicine, which licenses and regulates doctors, holds that booking an appointment involves no medical confidentiality. The National Supplementary Health Agency, which regulates private health insurance, says the specialty sought and other booking details may reveal aspects of a person's health.

In Taiwan and mainland China, health information is a special category of personal data, though neither law spells out booking data. Taiwan's Personal Data Protection Act, Article 6, bars collecting, processing or using medical records, medical care and health check data except in listed cases. Mainland China's Personal Information Protection Law lists medical and health information as sensitive personal information in Article 28 and requires separate consent to process it in Article 29.

The Markup's Blacklight scanner tests a URL for data sent to TikTok, Google Analytics and others. A scan normally takes 30 seconds to a minute, the interface is in English only, and scans run from Ohio, California or Europe. Blacklight scans the address entered, so data sent later in a booking flow may not show up. Part of its code is on GitHub under the GPL-3.0 licence, with the latest release in June.

In June 2025 tests on US state health-insurance exchange sites, The Markup found that Firefox's and Safari's built-in settings, the Brave and DuckDuckGo browsers, and the Privacy Badger and uBlock Origin Lite extensions blocked the LinkedIn, Snapchat and Google trackers it examined. TikTok's tracker was not part of those tests, the extensions were tested on desktop browsers, and a VPN or private browsing did not help.

In desktop Firefox, a first step is to switch Enhanced Tracking Protection from Standard to Strict under Settings, Privacy and security. It is one change, needs no account and is available in Traditional Chinese. The trade-off appears on the same page as the warning "Some sites may break with strict tracking protection." On a Mac, users can set "Use advanced tracking and fingerprinting protection" in Safari's Advanced settings to cover all browsing; according to Apple's help page, some website features may be affected.
