---
title: Phone-number-free registration in the Signal Android beta
description: Signal's Android beta lets people register without a phone number for a one-time fee. The account is tied to neither a SIM card nor the payment, and nothing can recover it if the keys are lost. The iPhone version is still in development.
date: 2026-09-26T01:23:00+08:00
slug: signal-numberless-registration
pin: true
sources:
  - title: Phone Numberless Registration for Android
    url: https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android
    publisher: Signal Support
  - title: Beta feedback for the upcoming Android 8.28 release
    url: https://community.signalusers.org/t/beta-feedback-for-the-upcoming-android-8-28-release/76457
    publisher: Signal Community
    date: 2026-09-16
  - title: Beta feedback for the upcoming Android 8.29 release
    url: https://community.signalusers.org/t/beta-feedback-for-the-upcoming-android-8-29-release/76509
    publisher: Signal Community
    date: 2026-09-23
  - title: Signal tests account registration without phone number on Android
    url: https://cyberinsider.com/signal-tests-account-registration-without-phone-number-on-android/
    publisher: CyberInsider
    date: 2026-09-18
  - title: "Signal Will Let You Sign Up Without a Phone Number — For $3"
    url: https://itsfoss.com/news/signal-numberless-registration/
    publisher: It's FOSS
    date: 2026-09-22
  - title: Signal introduces registration without a phone number
    url: https://freedom.press/digisec/blog/signal-introduces-registration-without-a-phone-number/
    publisher: Freedom of the Press Foundation
    date: 2026-09-23
  - title: I don't like passkeys
    url: https://hawksley.dev/blog/i-dont-like-passkeys
    date: 2026-09-18
  - title: 电话用户真实身份信息登记规定
    url: https://www.gov.cn/gongbao/content/2013/content_2473882.htm
    publisher: Ministry of Industry and Information Technology, China
    date: 2013-07-16
  - title: OFCA steps up publicity and assistance for forthcoming full implementation of real-name registration programme for SIM cards (with photos)
    url: https://www.cedb.gov.hk/en/news/press_release/2023/pr19012023a.html
    publisher: Commerce and Economic Development Bureau, Hong Kong
    date: 2023-01-19
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: Laws & Regulations Database of Taiwan
  - title: How countries attempt to block Signal Private Messenger App around the world
    url: https://ooni.org/post/2021-how-signal-private-messenger-blocked-around-the-world/
    publisher: OONI
    date: 2021-10-21
  - title: Signal Beta
    url: https://support.signal.org/hc/en-us/articles/360007318471-Signal-Beta
    publisher: Signal Support
authors:
  - anoni-net
---

Signal's Android 8.28 beta adds a way to register without a phone number, called Signal Login. The 8.29 beta announcement on 23 September says the feature will stay in beta for another week. As of 26 September, the iPhone version is still in development, and accounts already registered with a number cannot remove it.

Registering this way takes a one-time payment of US$2.99 through Google Play, and prices can differ by country. Devices without Google Play services cannot use it yet. Signal's announcement on its community forum says the payment uses the same zero-knowledge proofs as its donation system, so there is no link between the payment and the account. The fee is there because free accounts would be registered in bulk by spammers.

Registration gives you an Account ID and a Recovery Key, which work like a username and password. There is no PIN and no other recovery mechanism, so losing either one loses the account. A username is optional. Without one, nobody can find the account, and it can only join chats it starts. TOTP two-factor authentication can be added after registration, and Signal plans to add passkeys and hardware keys later.

## Perspective {#perspective}

Signal's end-to-end encryption has always protected message content, but every account started from a phone number. In much of Asia a phone number is itself an identity record. Mainland China has required real-name registration for every phone line since 2013, when the Ministry of Industry and Information Technology obliged carriers to check a valid ID before connecting a user. Hong Kong extended registration to every SIM card, prepaid ones included, and unregistered prepaid cards stopped working after 23 February 2023. In Taiwan, carriers must record a name, an address and the numbers of two identity documents before activating any mobile number, prepaid or not. In all three places, a Signal account registered with a number leads back, through the carrier, to a named person.

The paid route breaks that chain in two places. The account is not tied to a SIM card, and the zero-knowledge payment is not tied to the account. People who want to keep a work identity apart from a personal one no longer need a second SIM card registered in their own name. Signal's Android app is open source under AGPL-3.0, and its interface is available in both Traditional and Simplified Chinese.

Reaching Signal at all is a separate question in mainland China. OONI measurements from April to September 2021 show Signal blocked there, so people inside need a circumvention tool first.

Without a number, a username becomes the only way to be found. According to the Freedom of the Press Foundation, a username you have shared publicly should be kept, because once it is released someone else can claim it and impersonate you. That risk is highest for people who publish a username so that sources can contact them.

According to a separate essay on passkeys, an account is only as secure as its weakest recovery method. Signal's numberless accounts have no recovery method at all. Attackers lose a weak entry point, and users carry the entire risk of loss.

Trying it means subscribing to Signal's beta channel on Google Play and paying the one-time fee there, US$2.99 or a local equivalent. As of 26 September, the option suits people outside the mainland whose phones run Google Play services. After registering, store the Account ID and Recovery Key in a password manager with an offline backup, and if you add TOTP, set up more than one second factor.
