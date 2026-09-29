---
title: Privacy design and disputes around the EU age verification app
description: The European Commission recommends that member states launch an age verification app by the end of 2026; users outside the EU are not affected. According to the Commission, the app keeps no ID documents or biometric data, while EDRi questions its privacy protections. Under the specification released in September, apps and websites must implement zero-knowledge proofs, falling back only on devices without support to a plain method that an issuer could trace.
date: {created: 2026-09-29T07:00:00+08:00, updated: 2026-09-29T15:38:00+08:00}
slug: eu-age-verification-blueprint
sources:
  - title: The EU approach to age verification
    url: https://digital-strategy.ec.europa.eu/en/policies/eu-age-verification
    publisher: European Commission
    date: 2026-09-22
  - title: EU KIDS Act to restrict social media platforms’ access to children in the EU
    url: https://digital-strategy.ec.europa.eu/en/news/eu-kids-act-restrict-social-media-platforms-access-children-eu
    publisher: European Commission
    date: 2026-09-17
  - title: "EU KIDS Act to restrict social media platforms' access to children in the EU"
    url: https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1890
    publisher: European Commission
    date: 2026-09-17
  - title: Commission urges Member States to rollout EU age verification app
    url: https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app
    publisher: European Commission
    date: 2026-04-29
  - title: Why the EU age-verification tool does not solve privacy concerns
    url: https://edri.org/our-work/eu-age-verification-tool-does-not-solve-privacy-concerns/
    publisher: EDRi
    date: 2026-09-07
  - title: av-doc-technical-specification
    url: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification
    publisher: EU Digital Identity Wallet
    date: 2026-09-02
  - title: av-app-android-wallet-ui
    url: https://github.com/eu-digital-identity-wallet/av-app-android-wallet-ui
    publisher: EU Digital Identity Wallet
    date: 2026-09-03
  - title: Social media age restrictions
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions
    publisher: eSafety Commissioner
    date: 2026-09-15
  - title: Social media 'ban' or delay FAQ
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions/faqs
    publisher: eSafety Commissioner
    date: 2026-09-16
  - title: Under-16
    url: https://www.mcmc.gov.my/en/onsa/under-16
    publisher: Malaysian Communications and Multimedia Commission
    date: 2026-06-15
  - title: 未成年人网络保护条例
    url: https://www.gov.cn/zhengce/content/202310/content_6911288.htm
    publisher: 中华人民共和国国务院
    date: 2023-10-24
regions:
  - EU
authors:
  - anoni-net
---

The European Commission declared its age verification app ready in April and recommended that member states launch their own by the end of the year. The EU KIDS Act, proposed on 17 September, would bar under-13s from social media platforms and set 15 as the minimum age for an account of one's own. Online services and app stores would have to use age assurance tools, with this app as one option. Users outside the EU are not affected.

According to the Commission's policy page, users can prove they are over 18 without sharing any other personal information. The app, also called the "mini wallet", shares the specifications of the EU Digital Identity Wallets due in every member state by the end of 2026. Per the proposal's press release, the app retains no identity documents or biometric data, and 92% of respondents to an EU-wide survey see stronger online protection for children as a top policy priority.

In a technical analysis on 7 September, the digital rights network European Digital Rights (EDRi) concluded that the tools, pitched as "ready" and "privacy-preserving", fail on both counts. EDRi opposes building age verification while refusing is still an option, and in its analysis any age gate would have to meet the highest privacy and data protection standards. By its analysis, the law requires the underlying Digital Identity Wallet to "ensure" unlinkability (age proofs that cannot be tied to one person) where relevant, and the Commission has weakened this to "hindering" linkage.

Credentials in the plain verification method carry salts, signatures and timestamps, so an issuer that keeps records and cooperates with websites can trace users. EDRi quotes specifications older than version 1.1.0, where zero-knowledge proofs (a cryptographic way to prove a condition without revealing anything else) were a non-binding "SHOULD". In version 1.1.0, published on 2 September, apps and websites must both implement them, falling back to the plain method only on devices without support.

## Perspective {#perspective}

In anonymous age verification, a website learns only that you meet the age threshold, and whoever issued the credential does not learn which sites you visited. Under the specification, the issuer is recommended to also provide the app. In EDRi's analysis, that puts issuing and presentation in the same hands, so even mandatory zero-knowledge proofs would not deliver strict unlinkability.

In the threat model published with version 1.1.0, zero-knowledge proofs leave a website nothing to match against issuance records, and the website does not contact the issuer during verification. For the plain method, the risk of an issuer colluding with websites is accepted, since it would require a regulated issuer to break the rules by keeping records.

The reference app is open source under the EUPL-1.2 licence, and in its recommendation the Commission asks member states to ensure compliance with cybersecurity and privacy standards through third-party scrutiny. According to EDRi, the open-source requirement covers only the Digital Identity Wallets, and Denmark's age verification app has proprietary code on the client side.

In EDRi's analysis, the app confirms users through national ID combined with biometric checks, excluding people without ID documents, a suitable phone, or willingness to undergo facial recognition. Other ways to obtain the credential listed in the specification include electronic identity schemes and identity checks by banks and mobile network operators. For people lacking identity documents, its Equity provision includes alternative issuance procedures or human intervention.

Since 10 December 2025, Australia has required social media platforms to take reasonable steps to stop under-16s from holding accounts. Australian law bars platforms from compelling users to provide government ID or use an accredited government digital ID, and platforms that offer it as an option must also offer a reasonable alternative. On the eSafety Commissioner's explainer page, the rule is framed as a delay to having accounts, with no penalties for under-16s or their parents.

Malaysia has required social media platforms by law to verify users' ages since 1 June 2026. Under the technology-neutral approach of its regulator, the Malaysian Communications and Multimedia Commission (MCMC), verification is expected to rely on government-issued records or documents where required. In mainland China, Article 31 of the Regulations on the Protection of Minors Online, in force since 1 January 2024, requires services offering posting, instant messaging and the like to minors to obtain their real identity information and to withhold the service without it.

Readers have nothing to set up for now. Those in the EU can check which specification version their national app follows when it launches by the end of 2026. The same questions help compare approaches anywhere: whether zero-knowledge proofs are mandatory, whether issuing and presentation are kept apart, whether the app is open source, and whether people who do not show ID have an alternative.
