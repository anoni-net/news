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
  - title: google.com
    url: https://en.greatfire.org/google.com
    publisher: GreatFire
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: Dangerzone
    url: https://github.com/freedomofpress/dangerzone
    publisher: Freedom of the Press Foundation
authors:
  - anoni-net
---

In an advice column published on 27 August, the digital security training team at the Freedom of the Press Foundation (FPF) answered a reader's question about whether AI makes phishing worse. Phishing now arrives by email, text message, QR code, and voice and video calls, and FPF's answer is that AI makes lures more convincing while the defences individuals should use stay the same. The advice applies to anyone who receives these messages.

Among the reports FPF cites, KnowBe4 estimates that phishing attacks using AI in some way rose by roughly 86% between October 2025 and March 2026. In Verizon's 2026 Data Breach Investigations Report, attackers used generative AI to develop phishing lures as the initial point of access in about 44% of detected incidents. According to a 2025 Microsoft report, AI-automated phishing emails reached a 54% click-through rate, against 12% for standard attempts.

The techniques in this research include automated reconnaissance on targets, more personalised lures, small variations between similar messages to avoid detection, and lures drafted in several languages. The result reads as if it were written for the recipient, for example by impersonating a colleague or mentioning a public event the recipient may attend.

## Perspective {#perspective}

Large language models are good at imitating a particular voice, so spotting scams by clumsy grammar or awkward machine translation is becoming unreliable, in Chinese and other Asian languages as much as in English. FPF's four red flags do not depend on the quality of the writing: a sender address that does not match the organisation it claims to be, links that have nothing to do with the service, pressure or urgency, and attachments nobody asked for. Its advice is to skip the link and type the address yourself, preview dubious files in a sandbox such as Google Drive or convert them with Dangerzone, and turn on two-factor authentication.

One-time codes can be phished too, and regulators in Asia have acted on that. In July 2024 the Monetary Authority of Singapore and the Association of Banks in Singapore announced that major retail banks would phase out one-time passwords for logins by customers who use a digital token on their phone, within three months. The reason given was that scammers set up fake bank websites to trick customers into handing over the codes. In an April 2025 circular, the Hong Kong Monetary Authority asked banks to make authentication in the banking app on a bound device the default, instead of SMS codes, for internet banking logins and high-risk transactions. According to the same circular, there are early signs of fraudsters using AI and deepfakes, and card-issuing banks that had already moved online card payments to bound devices saw fraud rates fall by nearly 80%.

For personal accounts, the equivalent step is a passkey. Google's help page says passkeys cannot be shared, copied or accidentally given to someone else, which makes them more resistant to phishing. Setting one up for a Google Account needs a computer running at least Windows 10 or macOS Ventura, or a phone on Android 9 or iOS 16, with iCloud Keychain turned on for Apple devices. Adding a passkey does not remove the account's existing verification or recovery options, and the help page is available in Chinese. GreatFire's tests show `google.com` is largely blocked in mainland China, so readers there will need to apply the same idea to the accounts they actually use.

People who open unsolicited documents for work can try Dangerzone. It is released under AGPL-3.0, version 0.11.0 came out in July, and it runs on Windows, macOS and Linux, with an English-only interface. It renders a document to pixels inside a sandbox with no network access and rebuilds it as a PDF. The trade-off is that the result has no text layer unless you turn on OCR, and the Windows version needs hardware virtualisation enabled.
