---
title: InterSecLab’s technical analysis of Russia’s state messenger Max
description: InterSecLab finds that Max, the messaging app Russia requires on new devices, has no end-to-end encryption, and that VPN detection, network probing and voice transcription can be switched on per account from the server.
date: 2026-09-30T07:05:00+08:00
slug: interseclab-max-messenger
sources:
  - title: "The Max Messenger: An Analysis of Russia’s State-Mandated Messaging Application"
    url: https://interseclab.org/research/max/
    publisher: InterSecLab
    date: 2026-09-24
  - title: О включении цифровой платформы Max в список программ для предварительной установки
    url: http://government.ru/docs/55977/
    publisher: Правительство России
    date: 2025-08-21
  - title: Russia says it has blocked WhatsApp amid wider clampdown on social media
    url: https://www.cnn.com/2026/02/12/tech/russia-whatsapp-social-media-clampdown-intl
    publisher: CNN
    date: 2026-02-12
  - title: "Should We Chat? Privacy in the WeChat Ecosystem"
    url: https://citizenlab.ca/2023/06/privacy-in-the-wechat-ecosystem-full-report/
    publisher: Citizen Lab
    date: 2023-06-28
authors:
  - anoni-net
---

InterSecLab, which researches surveillance and censorship technology, published an analysis on 24 September of Max, the messaging app the Russian government requires to be pre-installed on devices. Max has no end-to-end encryption: every message is readable by VK's servers, and there is no mode that protects content from the operator. The researchers examined the Android app between March and May 2026. The pre-installation rule applies only in Russia.

The report's central finding is the server-side switches. Network probing, VPN detection, voice transcription, elevated logging and the list of services allowed to receive a user's identity are all turned on from VK's servers, for one account or many, without an app update and with nothing shown in the interface. With probing on, each time the app opens or goes to the background it looks up the public IP address, checks for a VPN, reads the carrier and tests which services are reachable, reporting it all to VK. Max stops working when a VPN is detected on the device, uploads the entire address book in cleartext, and transcribes voice messages on VK's servers. According to the code, live call audio is routed to an on-device model that VK supplies from its servers and can replace without an update.

## Perspective {#perspective}

End-to-end encryption exists so that even the operator cannot read your messages. Max lacks it, but the per-account switches go further: the same app can behave differently for different people, and users cannot tell from the interface. The report states that it does not claim VK or any Russian state body has used these capabilities against a specific person. On 25 September the researchers withdrew a claim in the PDF about "secret chats", a feature Max does not have, and noted that the encryption finding is unaffected.

Russia's government announced in August 2025 that Max would join the list of software that must be pre-installed from 1 September, and CNN reported in February 2026 that Russia confirmed blocking WhatsApp while steering people to Max.

The architecture has a familiar counterpart in Asia. According to Citizen Lab's 2023 study of WeChat, the app has no end-to-end encryption, Tencent can see all messages, and mainland China accounts are subject to automated keyword censorship. What Max adds is a government mandate to install it. For readers across the region, the useful comparison is not between countries but between designs: whether a messenger encrypts end to end, whether its behaviour can be changed remotely per account, and whether independent researchers have been able to examine it.

For people who must use Max in Russia, the report's suggestions, since Max's VPN check covers only the device itself, are running a VPN on a router, isolating Max in a separate Android work profile, or keeping a separate phone for state apps. The report also states that none of this protects message content, which VK stores unencrypted. Readers outside Russia have nothing to install or configure, and sensitive conversations still belong in tools with end-to-end encryption.
