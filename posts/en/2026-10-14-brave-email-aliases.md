---
title: Brave's Email Aliases
description: Brave's desktop browser offers email aliases from version 1.94, letting you sign up with a forwarding address instead of your real one. Everyone gets five free, with a Brave account required. As of 12 October there is no mobile version, and Brave does not say whether you can reply from an alias.
date: 2026-10-14T00:05:00+08:00
slug: brave-email-aliases
categories:
  - tracking
sources:
  - title: Brave launches Email Aliases to keep your personal email address private from websites
    url: https://brave.com/privacy-updates/39-email-aliases/
    publisher: Brave
    date: 2026-08-27
  - title: "Brave Accounts: your password never leaves your device, ever."
    url: https://brave.com/blog/brave-accounts/
    publisher: Brave
    date: 2026-08-27
  - title: What is a Brave Email Alias?
    url: https://support.brave.app/hc/en-us/articles/45530506862349-What-is-a-Brave-Email-Alias
    publisher: Brave
    date: 2026-08-28
  - title: Brave Browser Privacy Policy
    url: https://brave.com/privacy/browser/
    publisher: Brave
    date: 2026-09-23
  - title: "[Email Aliases] Bubble UI for mobiles"
    url: https://github.com/brave/brave-browser/issues/50818
    publisher: GitHub
    date: 2025-11-13
  - title: Brave Release Notes
    url: https://brave.com/latest/
    publisher: Brave
  - title: brave_components_resources_zh-TW.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-TW.xtb
    publisher: GitHub
  - title: Block bravealias.com disposable email domain
    url: https://github.com/disposable/disposable/issues/288
    publisher: GitHub
    date: 2026-08-29
  - title: 如何在 iPhone 或 iPad 上使用 iCloud+ 的「隱藏電子郵件地址」
    url: https://support.apple.com/zh-tw/102548
    publisher: Apple
    date: 2025-09-30
  - title: Firefox Relay
    url: https://relay.firefox.com/
    publisher: Mozilla
  - title: SimpleLogin Pricing
    url: https://simplelogin.io/pricing/
    publisher: SimpleLogin
  - title: Real-name Registration Programme for Subscriber Identification Module (SIM) Cards
    url: https://www.ofca.gov.hk/en/consumer_focus/guide/hot_topics/sim_registration/index.html
    publisher: OFCA
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
  - title: 中华人民共和国网络安全法
    url: https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm
    publisher: Cyberspace Administration of China
    date: 2025-12-29
authors:
  - anoni-net
---

Brave launched Email Aliases on 27 August. From desktop version 1.94, you can sign up for websites with a forwarding address instead of your real email. Everyone gets five for free, but you first need a Brave account, which is separate from the Premium account used for services such as Brave VPN. As of 12 October, the Android and iOS release notes do not include the feature, and the help page exists only in English and Japanese.

A prompt to create an alias appears in a site's email field, and if it does not, you can right-click the field and choose "New Email Alias". Brave's announcement and privacy policy say Brave does not read the emails and only performs standard spam and virus filtering. Messages are deleted within seconds of delivery, failed deliveries are retried for up to 24 hours, and the forwarding runs on Amazon Web Services. The announcement also warns that some forwarded mail may land in spam at first.

The Brave account launched the same day signs in with OPAQUE, a protocol that lets a server verify a user without holding the password, published as RFC 9807 in July 2025. Brave's post says the password itself is never sent to its servers. The same post says OPAQUE does not stop phishing on its own and does not make weak passwords strong.

## Perspective {#perspective}

Brave's announcement calls an email address a durable, universal identifier and cites ad tools from Meta, Google and LinkedIn that let advertisers upload customer emails to match users. That matching happens between servers, so tracker blocking in the browser cannot stop it. With a different alias for each site, sites cannot use your email to match you across them.

The announcement says Brave stores the account email and every alias, encrypted at rest, so the link between aliases and the real address sits on Brave's servers. The help page says Brave logs receipt times and some headers for debugging but not message content or sender information, and the privacy policy says these logs are deleted within 14 days at most. The policy also says Brave will not reveal the emails or aliases tied to an account unless obliged by a valid legal request. Brave's pages do not say whether you can reply from an alias or which domain the aliases use.

An open-source list that sites use to block disposable email added `bravealias.com`, reported in an issue as Brave's alias domain, to its stricter tier in September. The maintainer noted that it is a forwarding relay rather than disposable mail, that it belongs in the same category as Firefox Relay and SimpleLogin, which is why it went only into the stricter tier, and only sites that use that tier block such domains.

Apple's Hide My Email comes with a paid iCloud+ plan and supports replies. Firefox Relay gives five free masks, with anonymous replies on the paid plan, whose list of countries does not include Taiwan or Hong Kong. SimpleLogin is open source, and its free plan offers ten aliases with replies.

In Hong Kong, Taiwan and mainland China, aliases do nothing for sites that ask for a phone number at sign-up, because a phone number there is tied to a real name. As of 12 October we found no rules in these places aimed specifically at email aliases or forwarding addresses.

Under Hong Kong's Telecommunications (Registration of SIM Cards) Regulation, all SIM cards have had to be registered under a real name since 2022. Article 77 of Taiwan's Regulations Governing Mobile Broadband Services (in the version we checked) requires carriers to record subscribers' names, addresses and two ID numbers before activation, prepaid cards included. Mainland China's Cybersecurity Law, amended in October 2025, requires operators of services including messaging and posting to collect users' real identity information.

Desktop Brave users on 1.94 or later can type `brave://settings/email-aliases` into the address bar, create an account and start generating aliases. Brave's source code already includes a Traditional Chinese translation of the setting. An alias protects only the email address, so sites can still match you through a phone number, real name or payment details used at sign-up.
