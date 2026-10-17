---
title: Signal's cross-platform encrypted backups and password manager transfers on Android
description: Signal released iOS 8.30 on 28 September, and its encrypted Signal Secure Backups can now be restored between Android and iPhone, so chats can follow you to a new platform. In September Google added a way on Android to move passwords and passkeys between password managers without exporting a file, starting with four apps.
date: 2026-10-18T12:00:00+08:00
slug: signal-backups-password-manager-transfer
categories:
  - mobile
sources:
  - title: "Back to Backups: A Year in Review"
    url: https://signal.org/blog/backup-improvements/
    publisher: Signal
    date: 2026-09-28
  - title: Signal Secure Backups
    url: https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backups
    publisher: Signal
  - title: Signal 安全備份
    url: https://support.signal.org/hc/zh-tw/articles/9708267671322
    publisher: Signal
  - title: Backups and Device Transfers on Signal
    url: https://support.signal.org/hc/en-us/articles/10074659364122-Backups-and-Device-Transfers-on-Signal
    publisher: Signal
  - title: Troubleshooting Signal Secure Backups
    url: https://support.signal.org/hc/en-us/articles/10075139325850-Troubleshooting-Signal-Secure-Backups
    publisher: Signal
  - title: iOS to iOS Device Transfer
    url: https://support.signal.org/hc/en-us/articles/10045771316762-iOS-to-iOS-Device-Transfer
    publisher: Signal
  - title: Switching password managers is easy and safe on Android
    url: https://blog.google/products-and-platforms/platforms/android/switch-password-managers/
    publisher: Google
    date: 2026-09-10
  - title: Credential transfer
    url: https://developer.android.com/identity/sign-in/credential-transfer
    publisher: Android Developers
  - title: Import or export passwords and passkeys with Chrome
    url: https://support.google.com/chrome/answer/13068232?co=GENIE.Platform%3DAndroid
    publisher: Google
  - title: Android offers password manager switching tool
    url: https://freedom.press/digisec/blog/android-offers-password-manager-switching-tool/
    publisher: Freedom of the Press Foundation
    date: 2026-09-16
  - title: "Password managers on Android: Switch without manual export"
    url: https://www.heise.de/en/news/Password-managers-on-Android-Switch-without-manual-export-11450892.html
    publisher: heise online
    date: 2026-09-11
  - title: Credential Exchange Format
    url: https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html
    publisher: FIDO Alliance
    date: 2025-08-14
  - title: ASCredentialExportManager
    url: https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager
    publisher: Apple
  - title: What’s new in passkeys
    url: https://developer.apple.com/videos/play/wwdc2025/279/
    publisher: Apple
    date: 2025-06-09
  - title: Export passwords to another password manager on iPhone
    url: https://support.apple.com/guide/iphone/export-passwords-iphf28f2e93e/ios
    publisher: Apple
  - title: Is https://signal.org blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/signal.org
    publisher: GreatFire
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
  - title: My Number Card on Smartphone
    url: https://www.digital.go.jp/en/policies/mynumber/smartphone-certification
    publisher: Digital Agency
    date: 2026-08-25
  - title: Procedures for discontinuing the use of a smartphone for which a electronic certificates on Android smartphones has been registered
    url: https://www.digital.go.jp/en/policies/mynumber/smartphone-certification/attention
    publisher: Digital Agency
    date: 2026-08-25
  - title: 모바일 신분증 - 모바일 주민등록증
    url: https://www.mobileid.go.kr/mip/hps/issuReqstGuidance/issuReqstGuidanceMrc.do
    publisher: Ministry of the Interior and Safety
  - title: Debut of mobile residence cards ushers in digital ID era
    url: https://www.korea.net/NewsFocus/policies/view?articleId=268063
    publisher: Korea.net
    date: 2025-03-14
authors:
  - anoni-net
---

Signal released iOS 8.30 on 28 September, and according to its blog, encrypted backups can now be created and restored across Android, iOS and desktop. The support centre limits this to Signal Secure Backups, which can be restored between Android and iPhone, so chat history can move to a new platform when you change phones. On 10 September Google added a flow on Android for moving passwords and passkeys from one password manager to another without first downloading them to a file. It works on Android 8 and later, and the announcement lists Google Password Manager, 1Password, Bitwarden and Dashlane, with more partners to follow.

According to the support centre, Signal Secure Backups is hosted by Signal and protected by a 64-character recovery key that is never shared with the Signal service. If the key is lost, the backup cannot be restored, and Signal cannot recover it. As of 18 October the free plan backs up all text messages and the last 45 days of media, while a US$1.99 monthly plan stores up to 100 GB of media. View-once messages and messages set to disappear within 24 hours are left out.

Per Signal's blog, a new hosted backup is created every 24 hours and the previous one is deleted. The troubleshooting page notes that a backup can only be restored during first-time setup, using the same phone number.

If both phones are at hand and on the same platform, a device-to-device transfer moves the chat history to the new phone and leaves nothing on the old one. In iOS 8.30, Signal uses Wi-Fi Aware to set up a local end-to-end encrypted link between two iPhones, which the blog credits with better speed and reliability.

On-device backup files, according to the blog, can be created on Android, iOS and desktop in a cross-platform format. As of 18 October the support centre pages describe this differently from the blog and from each other: a page updated on 11 October lists all three platforms but restores work only within the same platform, while a troubleshooting page updated on 3 October limits them to Android to Android. Both the backups and transfers page and the desktop backups page note that an Android or desktop backup file cannot be restored on an iPhone.

In Google's announcement, the move starts in the new password manager, where you choose to import from another provider. Android then lists the password managers on the phone that can export, and you select, review and authorise the transfer in the old one. According to Google's developer documentation, the transfer happens between two apps on the same device without exposing raw credentials to the Android OS or unauthenticated apps. It uses the FIDO Alliance's Credential Exchange Format (CXF) and covers passwords, passkeys, addresses and custom fields; the FIDO Alliance is the industry group behind passkeys and other sign-in standards.

Apple offers developers of password managers a similar export and import API from iOS 26 and macOS 26, and in the flow its documentation describes, the operating system confirms the identities of both apps and writes nothing to the file system. A WWDC25 developer session notes that the data format was built with members of the FIDO Alliance. As of 18 October, the export and import pages of Apple's iPhone User Guide still cover only CSV files, and the export page warns that exported passwords are not encrypted.

## Perspective {#perspective}

Signal backups are encrypted with the user's recovery key, and without it no one, including Signal, can read or restore a backup. iCloud backups do not carry Signal chats either; the support centre's FAQ lists them as not compatible with Signal.

Signal Secure Backups adds a supplemental key that rotates daily and is kept in a trusted execution environment (TEE, an isolated area of a processor) on Signal's hosted service. This key cannot decrypt a backup without the recovery key, and the blog describes its sole purpose as forward secrecy, meaning past data stays protected even if a key leaks later. On-device backups cannot use the same TEE to get forward secrecy. The blog calls a TEE the best current way to protect this key, though that may change as research continues.

According to Google's announcement, moving passwords used to mean downloading them into an unencrypted text file, and passkeys could not be moved at all. On Apple's side, the new transfer writes nothing to the file system. On Android, the two apps pass data through a secure content URI backed by temporary cache files. The documentation's reason is that a whole vault can exceed Android's 1MB limit for a single transaction between processes.

According to heise, whether a whole vault can move depends on whether both apps have implemented the standard. Google's help page explains that importing into Google Password Manager requires signing in to the other password manager, and importing passkeys may also prompt for a recovery key. The page also reminds users to make sure they trust the other password manager before importing.

In parts of Asia, changing phones also involves a government ID stored on the phone. Japan's Digital Agency, on its machine-translated English page last updated on 25 August, advises users to delete the My Number Card from a smartphone before giving it up or changing models. For electronic certificates on Android phones, the law obliges users to revoke them themselves, and initialising the phone does not delete them.

In South Korea, the Ministry of the Interior and Safety's mobile ID site, available only in Korean, explains that a mobile resident registration card must be reissued after changing phones. Holders of IC cards can tap the card on the new phone and verify their identity, while holders of older cards can apply for an IC card or visit a community centre and complete the reissue with a QR code at the counter. Korea.net, the government portal, reported in March 2025 that each person can have a mobile ID on only one smartphone.

In mainland China, the third-party monitor GreatFire found both `signal.org` and `play.google.com` fully blocked in tests up to 11 October. GreatFire measures whether websites can be reached, not whether the Signal app can send messages. In Android's developer documentation, the caller check for this transfer flow is tied to the Google Play services system component, with nothing on whether phones without Google Play services can use it.

Signal users planning to switch phones can turn on backups in Signal's settings on the old phone and keep the recovery key safe before switching. The key can be saved to a password manager or stored manually; if it goes into a password manager, you will need to be able to open that manager on the new phone or another device, which is our inference from the setup flow. Signal Secure Backups covers a lost phone or a platform change, but cannot be restored with a new phone number, and the blog reminds users never to share the recovery key.

To switch password managers on Android, open the new app and look for an import option, and both apps need to support the flow. Google's 10 September announcement lists Google Password Manager, 1Password, Bitwarden and Dashlane. Importing into Google Password Manager also requires verifying your identity with the phone's screen lock. iPhone users moving passwords through a CSV file should note Apple's warning that the exported file is not encrypted and anyone who can access it can read it.
