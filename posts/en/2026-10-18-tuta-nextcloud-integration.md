---
title: Tuta encrypted email and its Nextcloud integration
description: Tuta and Nextcloud launched an integration on 1 October that lets you use Tuta inside Nextcloud, save received attachments to Nextcloud and create Nextcloud Talk meeting links from Tuta Calendar. A Nextcloud administrator has to install the app, and as of 18 October neither announcement explains how attachments are protected once they are in Nextcloud.
date: 2026-10-18T12:00:00+08:00
slug: tuta-nextcloud-integration
categories:
  - encryption
sources:
  - title: The Tuta app has landed in the Nextcloud App Store!
    url: https://tuta.com/blog/tuta-app-on-nextcloud
    publisher: Tuta
    date: 2026-10-01
  - title: Tuta brings end-to-end encrypted email service to Nextcloud
    url: https://nextcloud.com/blog/press_releases/tuta-brings-end-to-end-encrypted-email-service-to-nextcloud/
    publisher: Nextcloud
    date: 2026-10-01
  - title: Tuta brings encrypted email to Nextcloud with new free integration
    url: https://cyberinsider.com/tuta-brings-encrypted-email-to-nextcloud-with-new-free-integration/
    publisher: CyberInsider
    date: 2026-10-01
  - title: Tuta Mail
    url: https://apps.nextcloud.com/apps/tutamail
    publisher: Nextcloud
  - title: tutao/tutanota
    url: https://github.com/tutao/tutanota
    publisher: GitHub
  - title: Tuta Mail
    url: https://github.com/tutao/tutanota/blob/master/integrations/nextcloud/tutamail/README.md
    publisher: GitHub
  - title: Encryption
    url: https://tuta.com/encryption
    publisher: Tuta
  - title: Create a secure email account with Tuta Mail
    url: https://tuta.com/pricing
    publisher: Tuta
  - title: Server-side Encryption
    url: https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/encryption_configuration.html
    publisher: Nextcloud
  - title: Constants
    url: https://nextcloud-talk.readthedocs.io/en/latest/constants/
    publisher: Nextcloud
  - title: Conversations management
    url: https://nextcloud-talk.readthedocs.io/en/latest/conversation/
    publisher: Nextcloud
  - title: Nextcloud Talk
    url: https://nextcloud.com/talk/
    publisher: Nextcloud
  - title: Is https://tuta.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/tuta.com
    publisher: GreatFire
  - title: "Mayday Alert: 14 mobile apps banned, no blocking order released. #WhatTheBlock"
    url: https://internetfreedom.in/14-mobile-apps-banned/
    publisher: Internet Freedom Foundation
    date: 2023-05-10
  - title: Karnataka High Court orders blocking of Proton Mail in India
    url: https://www.barandbench.com/news/karnataka-high-court-orders-blocking-of-proton-mail-in-india
    publisher: Bar & Bench
    date: 2025-04-29
  - title: Karnataka HC Orders Govt to Block Privacy-Focused Proton Mail
    url: https://www.medianama.com/2025/04/223-karnataka-court-orders-encrypted-proton-mail-ban/
    publisher: MediaNama
    date: 2025-04-30
authors:
  - anoni-net
---

Encrypted email service Tuta and the open-source collaboration platform Nextcloud launched an integration on 1 October, which Tuta's announcement describes as free. It has two parts: a Tuta Mail app in the Nextcloud App Store that runs Tuta's web client inside Nextcloud, and a Nextcloud plugin in Tuta that saves received attachments to Nextcloud with one click or creates a Nextcloud Talk meeting link when you set up a Tuta Calendar event. Both features need the Tuta Mail app on your own Nextcloud; the App Store page lists Nextcloud 33 to 35. On a self-hosted server the administrator installs it, and on a managed one the provider has to make it available.

According to Tuta's announcement, the account administrator enables the plugin for all users under Settings → Plugins, and a single user is their own administrator. Tuta's README on GitHub lists two settings, the Nextcloud address and the folder for attachments, and the features work inside Nextcloud as well as in Tuta's web, desktop and mobile clients. Per Nextcloud's press release, the integration makes it easier for individuals and small businesses to self-host Nextcloud while leaving email to Tuta.

As of 18 October, neither Tuta's announcement nor its pricing page says which plan is required. Tuta's apps have a Traditional Chinese interface. In Tuta's public source code as of 18 October, the Traditional Chinese language file covers the general Plugins page, while the Nextcloud plugin's own settings and buttons such as "Save to Nextcloud" exist only in English and German.

## Perspective {#perspective}

Tuta's encryption page says emails, including subject lines and all attachments, are end-to-end encrypted and the key is never shared with anyone, Tuta included. Neither announcement explains what happens to that protection once an attachment is saved to Nextcloud, so we read Tuta's public source code as of 18 October. The save button sits in the attachment-saving dialog, and the plugin uploads through Nextcloud's file access interface (WebDAV) without any extra encryption. Our inference is that the uploaded file is the decrypted one, and it leaves Tuta's end-to-end encryption when it reaches Nextcloud.

Nextcloud's administration manual distinguishes two kinds of encryption. Server-side encryption runs on the server with keys stored there, and the manual warns that it does not protect against a compromised server or a malicious administrator. End-to-end encryption is done by Nextcloud's desktop or mobile clients before upload. Because the plugin does not upload through those clients, how well an attachment is protected on Nextcloud depends on that server's settings and who runs it, which is our inference from the manual and the code.

For Talk, the source code shows the plugin creating a public conversation, which Talk's API documentation lists as one that allows guests. Nextcloud's product page says Talk supports end-to-end encrypted calls in the web and new desktop clients, without saying whether public conversations are covered.

In mainland China, the third-party monitor GreatFire rates `tuta.com` as intermittently disrupted, with 59% of the last 17 conclusive tests up to 11 October showing interference. In India, the Internet Freedom Foundation noted reports that 14 end-to-end encrypted and peer-to-peer messaging apps, not email services, were banned in May 2023 without a published order. In April 2025 the Karnataka High Court ordered central authorities to act to block Proton Mail, though MediaNama noted that Proton Mail was still reachable in India when it reported the order. We found no reports of Tuta itself being blocked in India.

People or teams already using Nextcloud and Tuta can have the Nextcloud administrator install the Tuta Mail app, then have the Tuta account administrator enable the plugin. The manual notes that server-side encryption does not protect against the server's administrators, so before saving sensitive attachments it is worth checking who has administrative access to that server. Based on the source code and Talk's documentation, the plugin creates public conversations that allow guests, so anyone with the link can join as a guest.
