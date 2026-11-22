---
title: Native passkey integration in the Bitwarden desktop app for Windows 11 and macOS
description: Relevant to people already using Bitwarden on Windows 11 or macOS. On 18 November Bitwarden announced that its desktop app can be set as the system's passkey provider, so passkeys created on a computer can be saved to the Bitwarden vault and synced with the account. Windows 11 requires the version installed from the Microsoft Store, and according to Privacy Guides' news brief, Linux users will not get the feature this time.
date: 2026-11-24T00:00:00+08:00
slug: bitwarden-native-passkeys
categories:
  - security
sources:
  - title: Integrate Bitwarden with Windows and macOS for native passkey creation and use
    url: https://bitwarden.com/blog/integrate-bitwarden-native-passkeys/
    publisher: Bitwarden
    date: 2026-11-18
  - title: Bitwarden Adds Native Passkey Support for Windows and macOS
    url: https://www.privacyguides.org/news/2026/11/19/bitwarden-adds-native-passkey-support-for-windows-and-macos/
    publisher: Privacy Guides
    date: 2026-11-19
  - title: Autofill Passkeys
    url: https://bitwarden.com/help/storing-passkeys/
    publisher: Bitwarden
  - title: Bitwarden launches passkey management
    url: https://bitwarden.com/blog/bitwarden-launches-passkey-management/
    publisher: Bitwarden
  - title: Windows 11 expands passkey manager support
    url: https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-11-expands-passkey-manager-support/4467572
    publisher: Microsoft
    date: 2025-11-11
  - title: Passkeys
    url: https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/
    publisher: Microsoft
  - title: Export Vault Data
    url: https://bitwarden.com/help/export-your-data/
    publisher: Bitwarden
  - title: Download Credential Exchange Specifications
    url: https://fidoalliance.org/specifications/download-credential-exchange-specifications/
    publisher: FIDO Alliance
  - title: Server Regions
    url: https://bitwarden.com/help/server-geographies/
    publisher: Bitwarden
  - title: Is https://bitwarden.com blocked in mainland China?
    url: https://en.greatfire.org/https/bitwarden.com
    publisher: GreatFire
  - title: Is https://vault.bitwarden.com blocked in mainland China?
    url: https://en.greatfire.org/https/vault.bitwarden.com
    publisher: GreatFire
authors:
  - anoni-net
---

On 18 November Bitwarden announced that its desktop app can be set as the passkey provider (the program on a computer that stores passkeys and supplies them at sign-in) in Windows 11 and macOS. Passkeys replace passwords with the device's screen lock: the site stores only a public key, and the private key used to sign in stays on the device or in a password manager. With the desktop app set as the provider, the system dialog that appears when a website or desktop application creates a passkey lists Bitwarden as a place to save it. Windows 11 requires the version installed from the Microsoft Store, and according to Privacy Guides' news brief, Linux users will not get the feature this time.

Bitwarden began storing passkeys in its browser extension and mobile apps in early 2024. According to Privacy Guides' news brief of 19 November, the extension works for websites, but signing in to a desktop application might mean falling back on a phone or a hardware security key. Passkeys created on a computer might also end up in the default Windows or macOS credential manager rather than in Bitwarden.

A passkey created through the system dialog becomes a login item in the vault and can be managed from any Bitwarden app. If the vault already holds a login item with the same username, the passkey is added to that item automatically. If that item already contains a passkey, an overwrite warning appears first.

## Perspective {#perspective}

The integration matters to people already using Bitwarden on Windows 11 or macOS, and those who do not use Bitwarden are unaffected. Once it is set up, passkeys created on the computer can be saved to Bitwarden and synced with the account to other devices, rather than staying in the system's default tool. In our reading of how the announcement describes syncing, the private keys follow the Bitwarden account, so the way that account is protected and recovered also bears on these passkeys. For anyone who later wants to move them to another password manager, the protocol for direct transfer is still a draft.

The dialogs for creating a passkey and signing in come from Windows 11 and macOS, while the private keys are kept in the Bitwarden vault. According to Microsoft's documentation, when Windows 11 is used with a third-party provider, the passkeys are protected and managed by that provider.

To move or back up passkeys by exporting to a file, only the `.json` format includes them, and Bitwarden recommends the encrypted option on its export page. Only a Password protected encrypted export can be imported into another Bitwarden account, while an Account restricted export can only go back into the account it came from. Passkeys created before Bitwarden 2024.3.1 carry a counter that increases with each use, and according to the export page, exports of passkeys that old should not be used as long-term backups.

On the same export page, direct transfer to another password manager is listed only for phones, with nothing on whether the desktop app can do it (which apps support it is covered in our 19 October piece on [the passkey attestation debate](https://anoni.net/news/en/2026/10/passkey-attestation-debate/)). Direct transfer uses the FIDO Alliance's Credential Exchange Protocol (CXP), and as of 21 November the CXP listed on the FIDO Alliance's page was a working draft from October 2024.

To have new passkeys saved to the Bitwarden vault on Windows 11, use the desktop app from the Microsoft Store; the beta Bitwarden released in November 2025 was installed from GitHub instead. According to Microsoft's announcement, the capability arrived with the November 2025 security update. Next, under Passkey provider in the desktop app's settings, choose Manage in system settings and enable Bitwarden in the system dialog that follows; on macOS, the dialog asks whether to use AutoFill from Bitwarden. On its help page, Bitwarden recommends also turning off the passkey functions in the browser extension to prevent collisions between the two.

Bitwarden's cloud has two regions, the United States and the European Union, with none in mainland China, Hong Kong or Taiwan, and an account exists only in the region where it was created. In mainland China, GreatFire, a project that measures blocking by the Great Firewall, rated `vault.bitwarden.com` as not blocked, last tested on 15 November, and all five of its recent conclusive tests of that address connected normally. GreatFire rated `bitwarden.com` as sometimes accessible, with interference in one of its last four conclusive tests, the latest on 26 October. These tests check whether an address can be opened, which is not the same as whether the apps can sync, so in our reading they do not show whether the desktop app can sync passkeys with Bitwarden's servers from mainland China.

The passkey used to sign in to the Bitwarden account itself is not saved in the vault. Since the vault will not hold that key, people who sign in to Bitwarden with a passkey need to keep it somewhere else. Linux users, and Windows 11 users who would rather not switch to the Store version, can still store and use passkeys on websites through the browser extension, though that does not cover signing in to desktop applications.
