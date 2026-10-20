---
title: User data Telegram handed over to US law enforcement
description: A newly filed US federal court record includes a letter in which Telegram provided a user's phone number, user ID and IP address under a court order. Since September 2024, Telegram's privacy policy has allowed it to hand over IP addresses and phone numbers in criminal cases involving violations of its Terms of Service, no longer only for terror suspects, and the clause has no regional limit. As of 20 October, we had not seen a public response from Telegram to the filing.
date: 2026-10-22T00:05:00+08:00
slug: telegram-data-us-court
categories:
  - encryption
sources:
  - title: Telegram Privacy Policy
    url: https://telegram.org/privacy
    publisher: Telegram
  - title: Telegram FAQ
    url: https://telegram.org/faq
    publisher: Telegram
  - title: Telegram Privacy Policy
    url: https://web.archive.org/web/20240901002603/https://telegram.org/privacy
    publisher: Internet Archive
  - title: Scheduled Messages, Reminders, Custom Cloud Themes and More Privacy
    url: https://telegram.org/blog/scheduled-reminders-themes
    publisher: Telegram
    date: 2019-09-05
  - title: Here’s What Telegram Giving Data to the U.S. Government Looks Like
    url: https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/
    publisher: 404 Media
    date: 2026-10-16
  - title: Court filing reveals the user data Telegram is handing over to US authorities
    url: https://cyberinsider.com/telegram-sharing-user-data-with-us-authorities/
    publisher: CyberInsider
    date: 2026-10-17
  - title: Telegram Hands U.S. Authorities Data on Thousands of Users
    url: https://www.404media.co/telegram-hands-u-s-authorities-data-on-thousands-of-users/
    publisher: 404 Media
    date: 2025-01-06
  - title: Crowdsourcing Telegram ‘transparency reports’ to map the network’s claimed compliance with governments around the world
    url: https://meduza.io/en/feature/2024/10/23/crowdsourcing-telegram-transparency-reports-to-map-the-network-s-claimed-compliance-with-governments-around-the-world
    publisher: Meduza
    date: 2024-10-23
  - title: telegram-transparency
    url: https://github.com/Te-k/telegram-transparency
    publisher: GitHub
  - title: Translations
    url: https://translations.telegram.org/zh-hant/
    publisher: Telegram
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
  - title: Real-name Registration Programme for Subscriber Identification Module (SIM) Cards
    url: https://www.ofca.gov.hk/en/consumer_focus/guide/hot_topics/sim_registration/index.html
    publisher: Office of the Communications Authority
  - title: Services-Based Operations (Individual) Licence
    url: https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/licensing/telecommunication/services-based-operations-licence/sbotemplate.pdf
    publisher: IMDA
    date: 2025-12-01
  - title: 전기통신사업법
    url: https://www.law.go.kr/법령/전기통신사업법
    publisher: 국가법령정보센터
  - title: Act on Identity Confirmation, etc. Performed by Mobile Voice Communications Carriers for their Subscribers, etc. and Prevention of Wrongful Use of Mobile Voice Communications Services
    url: https://www.japaneselawtranslation.go.jp/en/laws/view/3770
    publisher: Japanese Law Translation
  - title: 電気通信サービスの不適正利用対策
    url: https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r08/html/nd222640.html
    publisher: Ministry of Internal Affairs and Communications
regions:
  - US
authors:
  - anoni-net
---

404 Media reported on 16 October that a newly filed document in a US federal court includes a letter from Telegram to US authorities, providing a user's phone number, user ID and IP address under a court order. According to CyberInsider, the letter is dated 4 September and was filed on 15 October in a criminal case in the US District Court for the Western District of Louisiana. The clause in Telegram's privacy policy on handing over IP addresses and phone numbers has no regional limit, so users outside the United States are subject to the same rules. As of 20 October, we had not seen a public response from Telegram to the filing.

404 Media's report is paywalled and we could read only its opening, and as of 20 October we could not find the court document itself, so the details of the letter come from CyberInsider's report. The IP address in the letter carries a timestamp in Coordinated Universal Time (UTC) marking the account's last login. In the letter, Telegram describes the disclosure as voluntary and states that providing the data does not mean accepting US jurisdiction.

According to CyberInsider, the attachment contains only account and connection information and no message content, though that does not mean investigators obtained nothing else through other channels. The same report says Telegram usually needs a phone number to look up an account's non-public data. A username or numeric ID sometimes works when the account was previously actioned for content moderation, or when Telegram enabled additional logging after receiving a formal request. The letter does not say whether additional logging was enabled for this account.

Section 8.3 of Telegram's privacy policy, which we checked on 20 October, says that when Telegram receives a valid court order it first carries out a legal analysis and may disclose IP addresses and phone numbers to the relevant authorities. The order must confirm that the user is a suspect in a criminal case involving violations of Telegram's Terms of Service, and such disclosures are included in quarterly transparency reports. An archived copy of the page shows that before the change on 23 September 2024 the section covered only terror suspects and stated "So far, this has never happened".

Telegram's transparency reports are available only by querying an official bot from a Telegram account, and according to Meduza's explainer from October 2024, the bot returns data only for the country where the querying account is registered. 404 Media quoted the bot's reply in January 2025: from January to September 2024, Telegram fulfilled 14 US requests for IP addresses or phone numbers affecting 108 users, and 900 requests affecting 2,253 users over the full year. A crowdsourced dataset on GitHub, compiled from bot replies that users pasted in, lists 1,706 requests affecting 4,807 users for the United States in 2025. Telegram does not publish these figures on the web.

## Perspective {#perspective}

According to Telegram's FAQ and privacy policy, both checked on 20 October, ordinary chats (cloud chats, including one-to-one chats and groups) are encrypted between the client and the server and stored on Telegram's servers. Secret Chats are end-to-end encrypted, meaning only the two participants' devices can decrypt them, and are not stored on the servers, only on the device each participant used to open the chat. The FAQ's section on data requests says the decryption keys for cloud chats are split across different jurisdictions, and that "To this day, we have disclosed 0 bytes of user messages to third parties, including governments". That section covers only message content, while the conditions for handing over IP addresses and phone numbers are in Section 8.3 of the privacy policy.

What Telegram provided in this letter was account data: a phone number, a user ID and an IP address. Section 5.2 of the privacy policy says that, for account security and to prevent spam and abuse, Telegram may collect IP addresses, the devices and apps used, and the history of username changes. Where collected, these records are kept for up to 12 months. Registering an account also requires a phone number.

We are a community based in Taiwan, where Article 77 of the Regulations for Administration of Mobile Broadband Businesses requires operators to record each subscriber's name, address and two identity document numbers, keep them for at least a year after the contract ends, and provide them when authorities make an inquiry under the law. From Section 8.3 of Telegram's privacy policy and this rule, we infer that once the number of an account registered with a Taiwanese number is handed over, Taiwanese authorities making an inquiry under the law can match the account to the subscriber.

Telegram does not publish country figures on the web, so the numbers for other places in Asia also come from the crowdsourced GitHub dataset, which counts requests for IP addresses or phone numbers that Telegram fulfilled. South Korea had 0 from January to September 2024, then 270 requests affecting 658 users from October to December 2024, and 2,101 requests affecting 5,454 users in 2025. Singapore had 4 requests affecting 4 users in 2024 and 14 affecting 16 in the first quarter of 2025, while Hong Kong and Japan appear only for January to September 2024, both at 0. Taiwan has no entry, though Meduza's October 2024 table lists it at 0 for January to September 2024, and we could not find figures for Taiwan, Hong Kong or Japan after September 2024, or for Singapore after the first quarter of 2025.

What a handed-over number can be matched to depends on what the carrier registered behind it, and the rules differ across Asia. In Hong Kong, under a regulation on SIM card registration that took effect on 1 September 2021, every SIM service plan and prepaid card has required real-name registration before activation since 1 March 2022, and individuals register their name in English and Chinese, date of birth, and Hong Kong identity card number with a copy of the card. In Singapore, the licence template that the Infocomm Media Development Authority (IMDA) issues to operators, which is not the text of a statute, requires them to register prepaid subscribers' name, address, identity document number and contact details and keep the register for at least 12 months after the service ends.

Article 32-4 of South Korea's Telecommunications Business Act, in the version in force from 1 October 2026, requires designated carriers to verify, with the subscriber's consent, that the person signing the contract is who they claim to be, and lets them ask for an identity card, including the mobile version, or a driver's licence. In Japan, Article 3 of the Act on Identity Confirmation by Mobile Voice Communications Carriers requires carriers to confirm an individual subscriber's name, address and date of birth at contract, and the 2026 White Paper on Information and Communications from the Ministry of Internal Affairs and Communications says the Act was amended in 2026 to require identity checks for data-only SIMs as well; we did not check when that amendment takes effect. We did not check whether the Korean and Japanese rules cover prepaid SIMs.

According to the FAQ, your phone number is visible by default only to people you have added to your own contacts, and the setting is under Settings > Privacy and Security > Phone Number. A 2019 post on Telegram's blog says that after setting who can see your number to Nobody, you can also limit who can find you by your number to your contacts (names in the current app may differ). According to the same post, strangers who add your number to their contacts then cannot match it to your profile, though the FAQ notes that people who already have your number saved can still see it. Usernames are always public, and the FAQ suggests not setting one if you do not want to be found through search.

For people who handle sensitive conversations, the FAQ recommends using Secret Chats with a self-destruct timer only in official or verifiable open-source apps, and turning on two-step verification and a passcode lock. To start a Secret Chat, open the other person's profile, tap "…" and choose Start Secret Chat, and note that Secret Chats disappear when you log out. Telegram's translation platform has a Traditional Chinese language pack that switches the interface through a share link, while the FAQ and privacy policy have no Chinese version. Our inference from Section 5.2 of the privacy policy and the phone number requirement at sign-up is that none of these steps means Telegram lacks the account's phone number, and whether IP addresses are collected depends on the circumstances described in Section 5.2.
