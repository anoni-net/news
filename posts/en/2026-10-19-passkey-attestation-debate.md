---
title: The passkey attestation debate
description: On 10 October a commentary argued against using passkeys because sites can use attestation to restrict which devices and software people may use, and on 14 October an author published a response. Both agree that passkeys are, in most cases, bound to a domain and resist phishing; they disagree on whether attestation will become a restriction, and on whether to keep using passkeys or switch to something else.
date: 2026-10-19T00:05:00+08:00
slug: passkey-attestation-debate
categories:
  - security
sources:
  - title: Passkeys are a trap. Do not use them.
    url: https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them
    publisher: Non-Functional
    date: 2026-10-10
  - title: Passkeys Are Not a Trap
    url: https://scotthelme.co.uk/passkeys-are-not-a-trap/
    publisher: scotthelme.co.uk
    date: 2026-10-14
  - title: "Web Authentication: An API for accessing Public Key Credentials - Level 3"
    url: https://www.w3.org/TR/webauthn-3/
    publisher: W3C
    date: 2026-08-25
  - title: NIST Special Publication 800-63B
    url: https://pages.nist.gov/800-63-4/sp800-63b.html
    publisher: NIST
  - title: Syncable Authenticators
    url: https://pages.nist.gov/800-63-4/sp800-63b/syncable/
    publisher: NIST
  - title: Passkeys
    url: https://fidoalliance.org/passkeys/
    publisher: FIDO Alliance
  - title: Download Credential Exchange Specifications
    url: https://fidoalliance.org/download-credential-exchange-specifications/
    publisher: FIDO Alliance
  - title: 關於通行密鑰的安全性
    url: https://support.apple.com/zh-tw/102195
    publisher: Apple
    date: 2024-09-27
  - title: About the security of passkeys
    url: https://support.apple.com/en-us/102195
    publisher: Apple
    date: 2024-09-16
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: Sign in with a passkey instead of a password
    url: https://support.google.com/accounts/answer/13548313?hl=en
    publisher: Google
  - title: Sync passkeys securely across your devices
    url: https://blog.google/technology/safety-security/google-password-manager-passkeys-update-september-2024/
    publisher: Google
    date: 2024-09-19
  - title: What are passkeys and why they matter
    url: https://support.microsoft.com/en-us/accounts-billing/security/what-are-passkeys-why-they-matter
    publisher: Microsoft
  - title: Export Vault Data
    url: https://bitwarden.com/help/export-your-data/
    publisher: Bitwarden
  - title: How to export your data from the 1Password apps
    url: https://support.1password.com/export/
    publisher: 1Password
  - title: "KeePassXC: User Guide"
    url: https://keepassxc.org/docs/KeePassXC_UserGuide
    publisher: KeePassXC
  - title: "「金融商品取引業者等向けの総合的な監督指針」等の一部改正（案）に対するパブリックコメントの結果等の公表について"
    url: https://www.fsa.go.jp/news/r7/shouken/20251015/20251015.html
    publisher: Financial Services Agency
    date: 2025-10-15
  - title: 業界団体との意見交換会において金融庁が提起した主な論点（日本証券業協会）
    url: https://www.fsa.go.jp/common/ronten/202511/06.pdf
    publisher: Financial Services Agency
    date: 2025-11-18
  - title: Banks in Singapore to Strengthen Resilience Against Phishing Scams
    url: https://www.mas.gov.sg/news/media-releases/2024/banks-in-singapore-to-strengthen-resilience-against-phishing-scams
    publisher: Monetary Authority of Singapore
    date: 2024-07-09
  - title: "Singpass Launches Passkeys: A Safer Login Method"
    url: https://www.tech.gov.sg/media/singpass-launches-passkeys-a-safer-login-method/
    publisher: GovTech
    date: 2026-06-30
  - title: Understanding Passwordless Authentication
    url: https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-011/
    publisher: Cyber Security Agency of Singapore
    date: 2026-08-26
  - title: 數位發展部加入國際標準組織 FIDO 聯盟 加速身分識別標準、接軌國際、擴大產業應用
    url: https://moda.gov.tw/ADI/news/latest-news/3687
    publisher: Ministry of Digital Affairs
    date: 2023-02-06
  - title: "「金融行動身分識別標準化機制」簡稱自即日起更改為「金融Fast-ID」"
    url: https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0&mcustomize=news_view.jsp&dataserno=202408160001&dtable=News
    publisher: Financial Supervisory Commission
    date: 2024-08-16
authors:
  - anoni-net
---

Passkeys replace passwords with the screen lock on a phone or computer, and each passkey works only on the domain where it was created. A commentary published on Substack on 10 October under the title "Passkeys are a trap. Do not use them." argues that sites can use attestation, a mechanism by which the device or software storing a key shows a site where it comes from, to gradually restrict which devices and software people can use.

On 14 October an author responded with "Passkeys Are Not a Trap", arguing that the synced passkeys most people use, stored in a password manager and synced between devices, provide no attestation. Both pieces agree that passwords are not secure and that passkeys are, in most cases, bound to a domain; the dispute centres on attestation, and on whether to keep using passkeys or switch to something else.

The commentary's author first points out that things differing in whether they can be copied, and in whether they live in hardware or software, are all called passkeys, and speculates that the name was chosen so users would not look closely. The author's core argument is that sites can use attestation to confirm a user has an approved password manager, and once most users are unaffected, start rejecting passkeys without attestation. According to the author, attestation requires the crypto processor, password manager, operating system and firmware all to pass checks, so people who install LineageOS to keep an old phone going, for example, might fail. The author also writes that attestation has legitimate uses and that most sites do not require it at the time of writing, recommends one-time codes from an authenticator app (TOTP) in the main text, and in a note at the end separately recommends hardware security keys such as YubiKey.

The response's author writes that even if a site asks for attestation, synced passkeys in iCloud Keychain, Google Password Manager, 1Password or Bitwarden return only "none", meaning no attestation. By this author's reasoning, a consumer site that accepted only attested passkeys would immediately lock out almost all of its users. According to the response, attestation tells a site only the make and model of the authenticator (the phone, password manager or security key that stores the key), and does not include the operating system, browser, extensions, firmware version or whether the phone is jailbroken. To the YubiKey recommendation, the author replies that every YubiKey ships with an attestation certificate signed by Yubico, so people worried about attestation would be pushed towards it.

## Perspective {#perspective}

The WebAuthn Level 3 specification, published by the W3C in August 2026, sets the default for attestation to none and leaves the attestation format to the authenticator. A site can state a preference and decide under its own policy which attestations to accept. The specification identifies authenticator types by AAGUID, a 128-bit identifier for an authenticator model, and its privacy considerations include the risk that attestation certificates are used to track users, with mitigations such as sharing one certificate across a large batch of devices or using an anonymization CA. In the Android SafetyNet format, which the specification already lists as deprecated, the attestation includes information on the platform's health; according to the response, attestation does not include the state of the operating system, but in our reading that depends on the format.

Under the same specification, enterprise attestation, which may include information that identifies an individual device, is provided only when the browser or authenticator settings allow it for that site. Under the digital identity guidelines that the US National Institute of Standards and Technology (NIST) issues for federal agencies (SP 800-63-4), public-facing services should not reject synced passkeys because attestation is unavailable, since that could push users towards methods that are easy to phish. The same guidelines also recommend that services use attestation, when present, to decide how much to trust an authenticator, and that internal federal systems implement it. Services can also restrict synced passkeys using the backup eligibility flag, a field showing whether a key can be synced or backed up.

The response's author starts from the situation in October 2026, when most consumer sites do not require attestation and the major sync services do not provide it. The same author writes that if consumer sites really did start requiring attestation, it would be worth objecting loudly. The commentary's concern is where things go next, and its author reasons that only the small number of people running modified systems would be affected, so sites could tighten their requirements gradually without drawing attention.

The response's author writes that TOTP codes can be typed into a fake site, and that phishing tools such as Evilginx, a relay server placed between the user and the real site, can forward passwords and codes in real time. Under NIST's guidelines, one-time passwords that must be entered by hand do not count as phishing-resistant authenticators, while properly configured synced passkeys do. In the commentary's main text, the author recommends TOTP because users can freely choose their software and hardware. In the note at the end, the author mentions that passkeys are, in most cases, bound to a domain and can withstand man-in-the-middle attacks, and recommends security keys.

Both pieces touch only briefly on changing devices and moving passkeys: the commentary's author mentions needing to take keys along when changing phones, and the response's author suggests that people who want to move them choose a provider that supports it. According to the FIDO Alliance, synced passkeys are end-to-end encrypted as they sync between devices. Per the two companies' help pages, Apple recovers passkeys through iCloud Keychain escrow, while Google requires the Google Password Manager PIN or the screen lock of an old Android device.

As of 18 October, Bitwarden and 1Password can export passkeys directly using the FIDO Alliance's Credential Exchange Protocol (CXP), which is still a draft. Both require iOS 26 or Android 14 or later (Bitwarden's export page lists Android 10 or later), and the receiving app must support it too. KeePassXC, by contrast, exports passkeys to an unencrypted file.

In Japan, the Financial Services Agency (FSA) amended its supervisory guidelines for securities firms, effective 15 October 2025, to look for phishing-resistant multi-factor authentication, turned on by default, for important operations such as logging in, withdrawing funds and changing the bank account for withdrawals. Passkeys and PKI-based authentication appear in the text only as examples, and firms are not limited to passkeys. According to materials from a November 2025 exchange of views between the FSA and the Japan Securities Dealers Association, securities firms are expected, in principle, to have this in place by the end of June 2026.

In Singapore, the Monetary Authority of Singapore (MAS) and the Association of Banks in Singapore announced on 9 July 2024 that major retail banks would progressively phase out one-time passwords for login by digital token users within three months, with no mention of passkeys or FIDO in the press release. Singpass, the government's digital identity, opened a beta of passkey login on 1 July 2026, starting with iPhone, with Android to follow and existing login methods kept; in guidance from the Cyber Security Agency of Singapore (CSA), passkeys are listed as phishing-resistant and SMS one-time passwords are not. In Taiwan, the Ministry of Digital Affairs joined the FIDO Alliance as a government member in January 2023, the second government body to do so after the Ministry of the Interior, and the Financial Supervisory Commission (FSC) has promoted a standardised mobile identity mechanism for finance since 2021, renamed Finance Fast-ID in August 2024. We, a community based in Taiwan, found no rule from Taiwan's financial regulators requiring passkeys.

According to the response, as of 18 October most consumer sites do not require attestation, and people already using synced passkeys can sign in as before. Under NIST's guidelines, a fake site cannot obtain reusable sign-in credentials when a properly configured passkey is used. The account's existing password and codes can still be phished, and according to Google's help page, adding a passkey does not remove existing verification methods. People worried about being tied to one platform can choose a password manager that exports passkeys directly.

People concerned about attestation can compare two approaches. According to the response, synced passkeys provide no attestation, while each YubiKey ships with an attestation certificate signed by Yubico.

NIST recommends that services let users register more than one authenticator for recovery; by our inference, for users this means keeping two or more ways to sign in or recover an account. According to Microsoft's help page, a passkey stored on only one device is lost if that device goes missing and there is no other recovery method.
