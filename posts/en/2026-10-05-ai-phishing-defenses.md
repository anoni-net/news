---
title: AI-assisted phishing and the defences that still work
description: Freedom of the Press Foundation rounds up research on attackers using AI to write more fluent, personalised phishing. The warning signs and defences have not changed, and they apply to anyone who receives email or text messages.
date: 2026-10-05T07:00:00+08:00
slug: ai-phishing-defenses
sources:
  - title: "Ask a security trainer: Does AI make phishing worse?"
    url: https://freedom.press/digisec/blog/ask-a-security-trainer-does-ai-make-phishing-worse/
    publisher: Freedom of the Press Foundation
    date: 2026-08-27
  - title: 2026 Data Breach Investigations Report
    url: https://www.verizon.com/business/resources/T459/reports/2026-dbir-data-breach-investigations-report.pdf
    publisher: Verizon
  - title: Banks in Singapore to Strengthen Resilience Against Phishing Scams
    url: https://www.mas.gov.sg/news/media-releases/2024/banks-in-singapore-to-strengthen-resilience-against-phishing-scams
    publisher: Monetary Authority of Singapore
    date: 2024-07-09
  - title: "New Anti-Digital Fraud Measures: “E-Banking Security ABC”"
    url: https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20250411-1-EN/20250411-1-EN.pdf
    publisher: Hong Kong Monetary Authority
    date: 2025-04-14
  - title: Sign in with a passkey instead of a password
    url: https://support.google.com/accounts/answer/13548313?hl=en
    publisher: Google
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: So long passwords, thanks for all the phish
    url: https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html
    publisher: Google
    date: 2023-05-03
  - title: Is http://google.com blocked in mainland China?
    url: https://en.greatfire.org/google.com
    publisher: GreatFire
  - title: Dangerzone
    url: https://github.com/freedomofpress/dangerzone
    publisher: Freedom of the Press Foundation
authors:
  - anoni-net
---

In an advice column on 27 August 2026, the digital security training team at the Freedom of the Press Foundation (FPF), a US press freedom organisation, rounded up research on AI-assisted phishing. Lures arrive by email, text message, QR code, and voice and video calls. FPF's answer is that AI makes them more convincing while the defences everyone should use stay the same.

FPF cites KnowBe4, a security awareness training company, which estimates AI-assisted phishing rose roughly 86% between October 2025 and March 2026. A 2025 Microsoft report put the click-through rate of AI-automated phishing emails at 54%, against 12% for standard ones. In Verizon's 2026 Data Breach Investigations Report, which draws on misuse records from an AI company's platform, phishing made up about 44% of AI-assisted initial access techniques (FPF misreports this as a share of incidents). In Verizon's incident data, the share of breaches starting with phishing has barely moved in years.

The automated techniques in this research include reconnaissance on targets, more personalised lures, small variations such as in subject lines to avoid detection, and lures in several languages. The result reads as if written for the recipient, for example impersonating a colleague.

## Perspective {#perspective}

Large language models imitate a voice well, so spotting scams by bad grammar or clumsy translation is likely becoming unreliable, in Chinese as in English. FPF's four red flags do not depend on the writing: a sender address that does not match, or merely resembles, the claimed organisation; links unrelated to the service; pressure or urgency; and unsolicited attachments. FPF suggests typing addresses yourself and previewing dubious files in Google Drive.

People who often open unsolicited documents can also convert them with Dangerzone, open-source software under AGPL-3.0; version 0.11.0 came out in July 2026. It renders a document to pixels in a sandbox with no network access and rebuilds a PDF outside it, with no text layer unless you turn on optical character recognition (OCR). It runs on Windows, macOS and Linux in English only; Windows needs hardware virtualisation supported and turned on.

FPF also recommends two-factor authentication, such as a code sent to your phone. In July 2024 the Monetary Authority of Singapore and the Association of Banks in Singapore announced that major retail banks would, within three months, progressively phase out one-time passwords (OTPs) for logins by customers who use a digital token. The announcement says OTPs had become easier to phish, for example through fake bank websites.

In an April 2025 circular, the Hong Kong Monetary Authority (HKMA) asked banks to make in-app approval on a bound device, not SMS codes, the default for logins and high-risk transactions. The circular says there are early signs that some fraudsters may have tried to use AI and deepfakes, and that card issuers that implemented an earlier measure, a bound-device default for online card payments required since late 2024, saw fraud rates fall by nearly 80%.

A passkey (a sign-in that uses your fingerprint, face or screen lock instead of a password) likewise needs no code that can be stolen. According to Google's security blog, the device shares its sign-in signature only with Google's websites and apps, never with a phishing site in between. The trade-off is that anyone who can unlock the device can get into the account, so Google's help page says to create them only on devices you personally own and use.

A first step is to add a passkey to your most-used account. For a Google Account (GreatFire, a censorship monitor, listed `google.com` as mostly blocked in mainland China as of 29 September 2026), that means Windows 10, macOS Ventura, Android 9 or iOS 16 or later, a phone screen lock, Chrome or Edge 109, Safari 16 or Firefox 122 or later, and iCloud Keychain on Apple devices. A new passkey may take 7 days to work for sign-in, and the help page is available in Chinese.
