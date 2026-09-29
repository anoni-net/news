---
title: InterSecLab’s technical analysis of Russia’s state messenger Max
description: InterSecLab finds that Max, the messaging app Russia requires on new devices, has no end-to-end encryption. VPN detection, network probing and voice transcription can be switched per account from the server with nothing shown in the app. The mandate applies only to devices sold in Russia.
date: 2026-09-30T00:05:00+08:00
slug: interseclab-max-messenger
sources:
  - title: "The Max Messenger: An Analysis of Russia’s State-Mandated Messaging Application"
    url: https://interseclab.org/research/max/
    publisher: InterSecLab
    date: 2026-09-24
  - title: Правительство включит новые цифровые продукты в перечень программ для обязательной предустановки
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
  - title: DoT issues directions for pre-installation of Sanchar Saathi App in mobile handsets to verify the genuineness of mobile handsets
    url: "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2197140&reg=3&lang=2"
    publisher: Press Information Bureau, Government of India
    date: 2025-12-01
  - title: Government removes mandatory pre-installation of Sanchar Saathi App
    url: "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2198110&reg=3&lang=2"
    publisher: Press Information Bureau, Government of India
    date: 2025-12-03
regions:
  - RU
authors:
  - anoni-net
---

On 24 September the digital security lab InterSecLab published an analysis of Max, the messaging app Russia requires on every smartphone and tablet sold there. With no end-to-end encryption, every message can be read on the servers of VK, the Russian internet company that develops Max. The findings cover one Android build, `26.12.0`, analysed between March and May 2026. Readers outside Russia are unaffected by the mandate.

Russia's government announced in August 2025 that Max would be pre-installed from 1 September 2025. CNN reported that in February 2026 Russia confirmed blocking WhatsApp and directed people to Max. According to InterSecLab's report, Max is increasingly required to reach government services.

VK's servers can switch network probing, VPN detection, voice transcription and elevated logging for one account or many, with no app update and nothing shown on screen. With probing on, each time the app opens or goes to the background it sends VK the public IP address, VPN status, carrier and which services on a list are reachable.

Max stops working when it detects a VPN. When the researchers tried to reply to a message, a full-screen instruction to disable the VPN appeared, with no way around it. The check covers only the device, so a VPN on a router goes unnoticed. Max also uploads the address book in cleartext and has voice messages transcribed on VK's servers.

On 25 September the researchers corrected the report: the Max interface has no "secret chats" feature, and version 1.1 of the PDF, released on 28 September, rewrites that finding. The no-encryption finding, based on plaintext messages captured inside the app, stands.

## Perspective {#perspective}

End-to-end encryption keeps message content from the operator. Max lacks it, and its behaviour can be changed per account from the server, so two people running the same version on the same day may be running different applications. According to the code, live call audio is routed to an on-device model that VK supplies from its servers and can replace without an update. The researchers could see only the settings delivered to their own test accounts, and they collected no evidence that VK or any Russian state body has used these capabilities against a specific person.

In Asia, WeChat has a similar architecture. According to the 2023 WeChat report by the Citizen Lab at the University of Toronto, chat messages are not end-to-end encrypted, giving Tencent visibility into all of them. Accounts registered with mainland Chinese phone numbers are subject to automated keyword censorship, and according to research cited in the same report, messages from accounts outside mainland China were used to train that censorship system. What Max adds is a government mandate to pre-install it.

In India, a pre-installation mandate was reversed within days. On 28 November 2025 India's Department of Telecommunications directed handset makers and importers to pre-install its Sanchar Saathi app on all phones made or imported for use in India, visible at setup and not disabled or restricted. Sanchar Saathi, a government app for checking a handset's IMEI number and reporting fraud, is not a messenger. According to a government press release on 3 December 2025, pre-installation would no longer be mandatory, given the app's growing acceptance.

The researchers advise against sending anything sensitive through Max and say anyone who has it installed should assume VK can read what they send. For people who must use Max in Russia, the report lists three ways to keep circumvention tools working alongside it: run a VPN on a router, isolate Max in a separate Android profile, or keep a separate phone for state apps. None of these protects message content, which VK stores unencrypted.

Readers outside Russia have nothing to install or change. Two follow-ups are worth watching: a Russian translation, to be posted on the report page when ready, and the next version of the report, which will correct how it describes when server-side settings take effect.
