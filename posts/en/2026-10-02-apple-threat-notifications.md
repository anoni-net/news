---
title: Recognising and responding to Apple threat notifications
description: Apple sent mercenary spyware threat notifications to users in 110 countries in August, though the vast majority of people will never be targeted. Apple's support page lists where genuine notifications appear and what they never ask for, and recipients can turn on Lockdown Mode and seek help.
date: 2026-10-02T07:00:00+08:00
slug: apple-threat-notifications
sources:
  - title: About Apple threat notifications and protecting against mercenary spyware
    url: https://support.apple.com/en-us/102174
    publisher: Apple
    date: 2026-08-13
  - title: Really, pay attention to Apple’s threat notifications
    url: https://freedom.press/digisec/blog/really-pay-attention-to-apples-threat-notifications/
    publisher: Freedom of the Press Foundation
    date: 2026-09-02
  - title: If Apple sends you a push notification alerting you to a spyware attack, take it seriously
    url: https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/
    publisher: TechCrunch
    date: 2026-08-13
  - title: About Lockdown Mode
    url: https://support.apple.com/en-us/105120
    publisher: Apple
    date: 2026-09-14
  - title: Apple says no one using Lockdown Mode has been hacked with spyware
    url: https://techcrunch.com/2026/03/27/apple-says-no-one-using-lockdown-mode-has-been-hacked-with-spyware/
    publisher: TechCrunch
    date: 2026-03-27
  - title: Digital Security Helpline
    url: https://www.accessnow.org/help/
    publisher: Access Now
  - title: Apple warns Indian opposition leaders of state-sponsored iPhone attacks
    url: https://techcrunch.com/2023/10/30/indian-opposition-leaders-says-apple-has-warned-them-of-state-sponsored-iphone-attacks/
    publisher: TechCrunch
    date: 2023-10-31
  - title: 關於封閉模式
    url: https://support.apple.com/zh-tw/105120
    publisher: Apple
    date: 2026-09-18
  - title: 關於 Apple 威脅通知與防範傭兵間諜軟體
    url: https://support.apple.com/zh-tw/102174
    publisher: Apple
    date: 2026-08-13
  - title: 关于锁定模式
    url: https://support.apple.com/zh-cn/105120
    publisher: Apple
    date: 2026-09-18
  - title: OONI Explorer
    url: https://explorer.ooni.org/chart/mat?probe_cc=CN&since=2026-09-01&until=2026-09-29&time_grain=day&axis_x=measurement_start_day&test_name=web_connectivity&domain=www.accessnow.org
    publisher: OONI
authors:
  - anoni-net
---

On 13 August Apple sent threat notifications to users in 110 countries, warning that their iPhones had been targeted by mercenary spyware, meaning spyware that private companies develop for governments, such as NSO Group's Pegasus. Apple has sent such notifications several times a year since 2021 and had reached users in more than 150 countries as of 13 August. According to Apple's support page, the vast majority of users will never be targeted.

In a 2 September newsletter, the press freedom nonprofit Freedom of the Press Foundation (FPF) urged readers to take the alerts seriously. It relayed an explainer from the digital rights nonprofit Access Now: a notification does not say whether the attack succeeded or who was behind it.

According to Apple's support page, notifications arrive through three channels: an alert on the iPhone Lock Screen and in Settings, an email to the addresses linked to the Apple Account (from `threat-notifications@email.apple.com` as of 2026), and a banner at the top of the page after signing in to `account.apple.com`. The format may vary by device model and software version.

Apple advises recipients to turn on Lockdown Mode, a built-in setting that restricts some features to reduce the risk of compromise, and to seek expert help such as Access Now's round-the-clock Digital Security Helpline. FPF also suggested that Android users look into Google's comparable Advanced Protection.

## Perspective {#perspective}

A genuine notification recommends protective steps such as Lockdown Mode, but never asks you to click links, open files, install apps or profiles, or give an Apple Account password or verification code. If a message claiming to be from Apple does, sign in to `account.apple.com` yourself and check for the banner.

Apple does not attribute attacks to specific attackers or regions, and does not explain what triggers a notification. When a batch reached people in India in October 2023, Apple told TechCrunch that some notifications might be false alarms and some attacks might go undetected. In the support page updated in August 2026, Apple calls the notifications high-confidence alerts that should be taken very seriously, while acknowledging that its investigations can never achieve absolute certainty.

According to Access Now's helpline page, as of 29 September the service replies to every request within two hours and supports ten languages: English, Spanish, French, German, Portuguese, Russian, Tagalog, Arabic, Italian and Ukrainian. Tagalog, spoken in the Philippines, is the only East or Southeast Asian language on the list, so Chinese speakers and others in East Asia may need to write in English. OONI, a project that measures internet censorship, has 76 measurements of the Access Now homepage from mainland China in September, 73 of them without anomalies.

A security researcher quoted by TechCrunch in March said Lockdown Mode blocks most message attachment types and restricts features of the WebKit browser engine, shrinking the attack surface, especially for zero-click exploits that need no action from the victim. On 27 March Apple told TechCrunch it was not aware of any successful mercenary spyware attack against a device with Lockdown Mode on. TechCrunch noted that an undetected bypass cannot be ruled out.

The trade-off is that devices no longer work as usual: apart from certain images, video and audio, most message attachments are blocked, links and link previews are unavailable, and some websites may load slowly or not work correctly. Trusted websites and apps can be excluded, at the cost of weaker protection.

On iPhone, Lockdown Mode needs iOS 16 or later and sits under Settings > Privacy & Security > Lockdown Mode, and turning it on restarts the device. iPad (iPadOS 16 or later) and Mac (macOS Ventura or later) must each be switched on separately, while a paired Apple Watch follows the iPhone. Apple's instructions and the interface are available in both Simplified and Traditional Chinese. People with good reason to think they may be targeted do not need to wait for a notification to turn it on.
