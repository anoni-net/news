---
title: Phishing emails that fake Gmail's attachment preview
description: Cisco Talos found phishing emails sent to Taiwan's academic, think tank and civil society policy community that use images in the message body to imitate Gmail's attachment card, starting an infection on Windows when clicked. Opened in a browser, the fake card is nearly indistinguishable from a real attachment, so people who often receive speaking invitations or institutional mail may want to watch for it.
date: 2026-10-09T00:10:00+08:00
slug: gmail-attachment-preview-phishing
categories:
  - security
sources:
  - title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
    url: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
    publisher: Cisco Talos
    date: 2026-09-30
  - title: 中國駭客UAT-11587鎖定臺灣學術界與智庫，以圖片仿製Gmail附件預覽介面並用政府文件作為誘餌
    url: https://www.ithome.com.tw/news/179344
    publisher: iThome
    date: 2026-10-01
  - title: 防範及檢舉網路釣魚電子郵件
    url: https://support.google.com/mail/answer/8253?hl=zh-Hant
    publisher: Google
  - title: 在 Gmail 中開啟及下載附件
    url: https://support.google.com/mail/answer/30719?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 檢查 Gmail 郵件是否通過驗證
    url: https://support.google.com/mail/answer/180707?hl=zh-Hant
    publisher: Google
  - title: Google 最強大的安全防禦機制，可確保私人資訊的安全。
    url: https://landing.google.com/intl/zh-TW/advancedprotection/
    publisher: Google
  - title: 進階保護計畫常見問題
    url: https://support.google.com/accounts/answer/7539956?hl=zh-Hant
    publisher: Google
  - title: Avoid & report phishing emails
    url: https://support.google.com/mail/answer/8253?hl=en
    publisher: Google
  - title: Open & download attachments in Gmail
    url: https://support.google.com/mail/answer/30719?hl=en&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: Check if your Gmail message is authenticated
    url: https://support.google.com/mail/answer/180707?hl=en
    publisher: Google
  - title: Google's strongest security helps keep your private information safe.
    url: https://landing.google.com/intl/en/advancedprotection/
    publisher: Google
  - title: Common questions with Advanced Protection Program
    url: https://support.google.com/accounts/answer/7539956?hl=en
    publisher: Google
regions:
  - TW
authors:
  - anoni-net
---

Cisco Talos published a report on 30 September about a cyber-espionage cluster it tracks as UAT-11587 and assesses with high confidence to be China-nexus. According to the report, spear-phishing emails sent in March 2026 to Taiwan's academic, think tank and civil society policy community used images in the message body to imitate Gmail's attachment preview, and clicking the fake card started an infection on Windows computers. Talos writes that when the message is opened in a browser, the fake card is visually indistinguishable from a genuine Gmail attachment preview.

Talos's report says the attacker built the card from four inline PNG images and wrapped the whole card in a link to an attacker-controlled Cloudflare Pages address. Clicking it downloads an HTA file, run by Windows's mshta.exe, which leads through a five-stage chain to a Rust-based backdoor called Antino while a decoy PDF is shown to the victim. The sample email, written in traditional Chinese, invited the recipient to speak at a workshop for about 50 minutes for a NT$3,500 fee, and one decoy document copied a public ruling from Taiwan's Ministry of Finance on legislators' expenses word for word.

Talos also writes that the visible sender impersonated an institution the recipient trusted. In one message Talos reviewed, the envelope sender used the attacker's own domain and passed SPF but failed DMARC, both checks that receiving servers use to verify the sending domain. The impersonated institution's domain had a DMARC policy that was not enforced, so the message was still delivered.

## Perspective {#perspective}

Talos's report says Gmail rendered the attacker's HTML faithfully in the browser, which is why an image in the body can look exactly like an attachment card. iThome reported that the fake card sits below the message text, and Gmail's help page places real attachments at the bottom of the message, so in our reading position alone does not tell them apart. According to Gmail's help page, hovering over a real attachment shows a Download icon and an Add to Drive icon.

From that, we infer that a card which shows neither icon on hover may simply be an image link inside the message. We have not tested this, it may stop working if Gmail changes its interface, and it applies only to the desktop version, since Talos's report does not describe how the message appears on phones. Gmail's help page also advises hovering over links before clicking on a computer, and treating a link whose address does not match its description as possible phishing.

Gmail's help page says that clicking the down arrow under the sender's name shows "Mailed by" and "Signed by" headers with their domains for authenticated messages, and a question mark next to the sender's name for messages that are not authenticated. The page counts a message as authenticated if it passes SPF or DKIM, and the message Talos reviewed passed SPF, so we infer that the question mark may not appear.

The "Mailed by" header shows the sending domain, which is different from the sender name at the top of the email, and in our reading it is worth checking whether that domain matches the institution the email claims to come from. As of 7 October, the help page does not say how Gmail displays messages that fail DMARC.

People who often receive speaking invitations, official documents or institutional mail may want to watch for fake attachment cards. On a computer, a suspicious message can be reported from the More menu next to Reply by clicking Report phishing.

According to Google, people at risk of targeted online attacks can enrol in the Advanced Protection Program, which as of 7 October is free to use. Sign-in then always requires a passkey or security key, and Chrome checks downloads more closely. The cost is setting up a passkey or buying a security key, and apps that rely on app passwords are blocked. As of 7 October, Google's pages do not say whether Advanced Protection stops a fake attachment card inside the message body.

Talos's targeting assessment extends well beyond Taiwan. Talos assesses with moderate-to-high confidence that it targeted organisations in Taiwan, India, the Philippines, Cambodia, Pakistan, Thailand, Myanmar and Syria, and as of July 2026 it had identified at least 16 affected or targeted institutions and about 350 compromised endpoints. Talos lists likely audiences for the lure titles, for example the Philippine public sector for a title about the Bajo de Masinloc chart, and it recovered a decoy document about an Indo-Pacific policy forum, though it notes that titles alone do not confirm delivery or compromise. The largest single wave Talos observed came on 8 and 9 June, with around 57 newly observed endpoints associated with India.
