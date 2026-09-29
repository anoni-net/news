---
title: Privacy design and disputes around the EU age verification app
description: The European Commission recommends that member states launch an age verification app by the end of 2026; users outside the EU are not affected. According to the Commission, the app keeps no ID documents or biometric data, while EDRi questions its privacy protections. Under the Commission's specification released in September, apps and websites must implement zero-knowledge proofs, falling back only on devices without support to a plain method that an issuer could trace.
date: {created: 2026-09-29T07:00:00+08:00, updated: 2026-09-29T16:25:00+08:00}
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

The European Commission declared its age verification app ready in April and urged member states to launch their own by year-end. The EU KIDS Act, proposed on 17 September, would bar under-13s from social media platforms and set 15 as the minimum age for an account of one's own. Online services and app stores would have to use age assurance tools, with this app as one option. Users outside the EU are not affected.

Per the Commission's press release, social media and video-sharing platforms would check age when an account is opened and estimate existing users' ages from proxies such as account creation date. Children aged 13 to under 15 would use mini accounts set up by a guardian, limited to one hour a day.

On the Commission's policy page, users can prove they are over 18 without sharing other personal data, and per the press release the app retains no identity documents or biometric data. The app is nicknamed the "mini wallet" and shares the technical specifications of the EU Digital Identity Wallets. In version 1.1.0 of the specification, published on 2 September, apps and websites must implement zero-knowledge proofs (a way to prove a condition without revealing anything else), falling back to a plain method only on devices without support. Under the plain method, an issuer that keeps records and colludes with websites can trace users.

In a technical analysis on 7 September, European Digital Rights (EDRi) concluded that the tools, pitched as "ready" and "privacy-preserving", fail on both counts. The analysis is based on an earlier version of the specification, in which zero-knowledge proofs were optional, and as of 29 September the article carries no update or correction. EDRi argues that online safety can be reached by other routes and calls for refusing to build age verification. By its analysis, the law requires the underlying wallet to "ensure" unlinkability (proofs that cannot be tied to one person) where relevant, and the Commission has weakened this to "hindering" linkage.

## Perspective {#perspective}

In the threat model attached to the Commission's specification, zero-knowledge proofs leave a website nothing to match against issuance records. The plain method's tracing risk is accepted, because it would take deliberate wrongdoing by an issuer on the EU Trusted List published by the Commission and under national supervision. Under the Commission's specification, issuers are also recommended to provide the app. In EDRi's analysis, that puts issuing and presentation in the same hands, so even mandatory zero-knowledge proofs would not deliver strict unlinkability.

In EDRi's analysis, the app confirms users through national ID combined with biometric checks, excluding people without ID documents, a suitable phone, or willingness to undergo facial recognition. The Commission's specification also lists electronic identity schemes and identity checks by banks and mobile network operators, and under its threat model only scanning a passport or ID card involves a face match. For people lacking documents, the specification's Equity provision includes alternative issuance procedures or human intervention.

The Commission's reference app is open source under the EUPL-1.2 licence, and in its recommendation the Commission asks member states to ensure compliance with cybersecurity and privacy standards through third-party scrutiny. According to EDRi, the open-source requirement covers only the Digital Identity Wallets, and Denmark's app has proprietary code on the client side.

In the Commission's threat model, an adult helping in person or enrolling a minor's phone is an accepted residual risk. Circumvention is not discussed in EDRi's analysis. Checking the face at every presentation was rejected in the threat model as a disproportionate invasion of privacy.

Since 10 December 2025, Australia has required social media platforms to stop under-16s from holding accounts, with penalties for platforms that fail but none for under-16s or their parents. On exclusion, Australian law bars platforms from compelling users to provide government ID, and platforms that offer it as an option must also offer a reasonable alternative.

Malaysia has required social media platforms by law to verify users' ages since 1 June 2026. Under the technology-neutral approach of its regulator, the Malaysian Communications and Multimedia Commission (MCMC), verification is expected to use government-issued records or documents where required. In mainland China, Article 31 of the Regulations on the Protection of Minors Online, in force since 1 January 2024, requires services offering posting, instant messaging and the like to minors to obtain their real identity information. On tracing, that points in a different direction from the EU design, where a website learns only that the age threshold is met.

Readers have nothing to set up for now. On privacy, the questions to compare are whether the issuer can trace users and whether people without ID have an alternative. On child protection, they are whether minors can easily get around the checks and how existing accounts are handled.
