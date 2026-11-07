---
title: Selfie-based age estimation for adult confirmation in iOS 27.2
description: Apple has added an option in iOS and iPadOS 27.2 to confirm that a user is an adult by estimating their age from a selfie. Apple's support documents say it is offered only in Australia, Brazil, Singapore and the UK. As of 7 November, Taiwan, Hong Kong, mainland China and Japan are not among the places where Apple requires age confirmation.
date: 2026-11-08T00:00:00+08:00
slug: ios-selfie-age-verification
categories: [censorship]
sources:
  - title: Confirm that you're an adult with a selfie
    url: https://support.apple.com/en-us/149095
    publisher: Apple
    date: 2026-10-26
  - title: Region-specific rules for managing an Apple Account
    url: https://support.apple.com/en-us/125666
    publisher: Apple
    date: 2026-10-26
  - title: If you're asked to confirm that you're an adult
    url: https://support.apple.com/en-us/125662
    publisher: Apple
    date: 2026-10-26
  - title: Apple Introduces Selfie Age Verification in iOS 27.2
    url: https://www.privacyguides.org/news/2026/10/29/apple-introduces-selfie-age-verification-in-ios-27-2/
    publisher: Privacy Guides
    date: 2026-10-29
  - title: Age assurance developer Q&A
    url: https://developer.apple.com/support/age-assurance/
    publisher: Apple Developer
  - title: Age requirements for managing an Apple Account in Brazil
    url: https://support.apple.com/en-us/126783
    publisher: Apple
    date: 2026-10-26
  - title: Age requirements for managing an Apple Account in the United States (Texas)
    url: https://support.apple.com/en-us/127462
    publisher: Apple
    date: 2026-06-04
  - title: Next steps for apps distributed in Texas
    url: https://developer.apple.com/news/?id=2ezb6jhj
    publisher: Apple Developer
    date: 2025-11-04
  - title: New Online Safety Code of Practice for App Distribution Services Enhances Protection for Singapore Users
    url: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/online-safety-code-of-practice-for-app-distribution-services
    publisher: IMDA
    date: 2025-01-15
  - title: Factsheet on Age Assurance under the ADS Code
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2025/01/ads-code/factsheet-on-age-assurance.pdf
    publisher: IMDA
    date: 2025-01-15
  - title: Internet Age Gates Are a Growing Global Threat
    url: https://www.eff.org/deeplinks/2026/06/internet-age-gates-are-growing-global-threat
    publisher: EFF
    date: 2026-06-05
  - title: "Face Scans to Estimate Our Age: Harmful and Creepy AF"
    url: https://www.eff.org/deeplinks/2025/01/face-scans-estimate-our-age-creepy-af-and-harmful
    publisher: EFF
    date: 2025-01-23
  - title: Age requirements for managing an Apple Account in Singapore
    url: https://support.apple.com/en-us/126786
    publisher: Apple
    date: 2026-10-26
  - title: Age requirements for managing an Apple Account in South Korea
    url: https://support.apple.com/en-us/126787
    publisher: Apple
    date: 2026-03-24
  - title: Verify your age when you download or stream mature content in South Korea
    url: https://support.apple.com/en-us/118395
    publisher: Apple
    date: 2025-03-03
  - title: 移动互联网未成年人模式建设指南
    url: https://www.cac.gov.cn/2024-11/15/c_1733364304749288.htm
    publisher: 国家互联网信息办公室
    date: 2024-11-15
  - title: 关于《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》公开征求意见的通知
    url: https://www.cac.gov.cn/2026-09/18/c_1791482017777471.htm
    publisher: 国家互联网信息办公室
    date: 2026-09-18
  - title: 青少年が安全に安心してインターネットを利用できる環境の整備等に関する法律
    url: https://laws.e-gov.go.jp/law/420AC1000000079
    publisher: e-Gov
regions:
  - AU
  - BR
  - SG
  - GB
authors:
  - anoni-net
---

Apple has added a new way to confirm adulthood in iOS and iPadOS 27.2: users take a picture of their face, and an age estimation model judges whether they are 18 or older. According to Apple support documents published on 26 October, the selfie option is offered only in Australia, Brazil, Singapore and the UK. The same document lists six places where age confirmation requirements apply to Apple Accounts, and the other two, South Korea and Texas in the United States, have no selfie option. As of 7 November, Taiwan, Hong Kong and other places not on the list are outside these requirements, and users there do not need to confirm their age.

The privacy advice site Privacy Guides covered the feature in a news brief on 29 October, which ends by saying that anyone living in Australia, Brazil, Singapore, South Korea, the UK or Texas has to confirm their age, without separating the places that offer selfies. We follow Apple's support documents on which places are covered, so users in South Korea and Texas have to use other methods.

Apple's documents say age confirmation may come up when creating a new account, updating the system, changing some safety settings, or downloading or buying apps rated 18+, depending on the region. Users who choose a selfie centre their face on screen and slowly turn their head in four directions so that every angle is captured. Once adulthood is confirmed, it does not have to be done again.

The same document says the selfie is analysed by age estimation models both on the device and on Private Cloud Compute, Apple's cloud computing service, which Apple describes as extending the device's security and privacy protections to the cloud, with the results combined on the device. Apple writes that no one, Apple included, can access the selfie during analysis, and that it is deleted after confirmation and not kept in any form. Privacy Guides describes the model as running on the device "or" on Private Cloud Compute, while Apple's document says it runs on both.

Besides the selfie, Apple lists a credit card in the user's name and scanning an ID (a passport, driver's licence or government-issued ID card), and does not accept debit or gift cards. For existing accounts, Apple first checks whether the account already holds a credit card or other qualifying information. Another Apple document says the ID image is used by Apple and its service providers to confirm age and prevent fraud, and is kept briefly and then deleted.

## Perspective {#perspective}

Age estimation infers roughly how old someone is from an image of their face, without asking for an ID. Privacy Guides writes that its effectiveness depends entirely on the quality of the estimation algorithm and that there will always be errors. An adult can be judged a minor, and the reverse can happen too. As of 7 November we could not find a model name, error rate or accuracy figures published by Apple, nor any independent report verifying that selfies are deleted and inaccessible.

Several of the places on Apple's list have rules requiring app stores to confirm or supply users' ages. Under the Code of Practice for Online Safety – App Distribution Services, Singapore's Infocomm Media Development Authority (IMDA) requires designated app stores to be able, from 1 April 2026, at least to tell whether a user is under 18, leaving each store to choose age estimation, age verification or both. IMDA's press release says the aim is to reduce the risk of users, especially children, being exposed to harmful content, and the Code also requires data minimisation in age assurance.

Texas's App Store Accountability Act (SB 2420) has applied since 4 June 2026 to new Apple Accounts created in Texas. According to an EFF post in June, a law Brazil passed in 2025 requires app stores and operating systems to provide age signals for other services, with full compliance expected in early 2027.

In Privacy Guides' comparison of the methods, a credit card hands over identifying information, though downloading even free apps already requires payment details. Scanning an ID can put sensitive documents in third-party hands, and the article gives Discord as an example, where a third party handling its ID-photo age checks leaked about 70,000 IDs. A poorly built selfie system carries risks as well: Persona, which handles age verification for companies including Roblox and ChatGPT, leaked a database of selfies. The article's view is that Apple's version seems much better in this respect, and at least better than sending documents to a third party.

EFF, the digital rights group, wrote about facial age estimation in January 2025, before Apple launched selfie confirmation (we found no EFF comment on Apple's feature itself), saying that face scans create new threats to privacy and information security. A poorly designed system might store facial data and even link it to the content a user views. EFF's June post says its consistent response to age verification initiatives in Europe has been that mandatory age verification is not the right way to protect young people. Apple's November 2025 developer announcement on the Texas law also said Apple worries that such laws, by requiring sensitive personal information just to download an app, could undermine the privacy of all users.

According to Apple's developer Q&A, apps can get age information through the Declared Age Range API, the interface an app uses to ask the system for a user's age range, and users decide whether to share it. Where the law requires it, Apple supplies apps with the age categories defined by local law. Brazil's page says age ranges are always shared when a developer requests them to comply with local law, and the Texas page says they are always shared, and users in neither place can turn this off.

From iOS 26.5, confirmation by credit card or ID returns a single `confirmed` value that does not say which method was used, and we could not find what is returned after selfie confirmation. California's AB 1043 takes another approach, requiring the operating system to ask for an age at account setup and pass an age range to apps without requiring verification. As amended by AB 1856, AB 1043 applies from 1 January 2027 (see [California AB 1856's open source exemption](https://anoni.net/news/en/2026/10/california-ab1856-open-source-exemption/){target="_blank"}).

In Asia, Apple's list includes only Singapore and South Korea, and the two work differently, with no selfie option in South Korea. Singapore's page asks for confirmation only to download or buy apps rated 18+, in line with IMDA's starting expectation that app stores keep children away from their highest-rated apps, and accepts a credit card, a passport, driving licence, National Registration Identity Card or Foreign Identification Number (FIN) card, or a selfie. Apple's pages for South Korea require users to confirm they are at least legally 19 to download or stream mature content through Apple services. Users verify by entering their name as it appears on their mobile carrier account, their birth date, carrier, mobile number, gender and nationality, then a code sent by text message to that Korean mobile number, and have to verify again once a year.

Taiwan, Hong Kong, mainland China and Japan are not on Apple's list, and as of 7 November we could not find rules in Taiwan or Hong Kong requiring operating systems or app stores to confirm users' ages. Mainland China works through a minors' mode instead: 2024 guidelines from the Cyberspace Administration of China ask devices to offer a birth date, age or age range when the mode is first entered and app distribution platforms to label recommended ages. A draft State Council regulation published for comment in September 2026 would require device makers to add exit verification and anti-circumvention features to the mode. Japan's 2008 law on young people's internet use deals with filtering on phones sold to under-18s and has no age confirmation rule for app stores in its text, and Apple's developer Q&A says that where the law does not require it, apps get an age range only if users choose to share it.

Based on Apple's documents, we infer two situations in which readers in Taiwan, Hong Kong or other unlisted places might meet age confirmation. One is if their Apple Account's region is one of the listed places, or if they create a new account in one of them. Apple's documents do not say whether the account region or the user's location decides this, and the Texas page refers to new accounts created in Texas. The other is if their own government later passes a law requiring app stores to confirm age, since Apple's documents say age confirmation applies where required by law.

People with accounts in Australia, Brazil, Singapore or the UK who are asked to confirm can compare what each method leaves behind. Accounts that already have a credit card may not need any extra step, a selfie is sent to Private Cloud Compute for analysis and then deleted according to Apple, and ID images are kept briefly by Apple and its service providers. As of 7 November Apple had not published error rates, and a user whose selfie fails to confirm adulthood can try again or switch to a credit card or ID. Not confirming still leaves the device usable, at the cost of not being able to download 18+ apps or turn off some safety settings.

Readers in Taiwan, Hong Kong and other places not on Apple's list do not need to change any settings for now. Things to watch include whether Apple extends the selfie option to South Korea, Texas or elsewhere, whether it publishes the accuracy of its estimation model, and how operating systems implement age signals once Brazil reaches full compliance in early 2027.
