---
title: Privacy gaps in the EU age verification blueprint
description: The EU wants member states to launch an age verification app by the end of the year. EDRi finds that unlinkability has been weakened, credentials can still be traced back to users, and people without ID are shut out.
date: 2026-09-29T07:00:00+08:00
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
  - title: Social media age restrictions
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions
    publisher: eSafety Commissioner
    date: 2026-09-15
  - title: Under-16
    url: https://www.mcmc.gov.my/en/onsa/under-16
    publisher: Malaysian Communications and Multimedia Commission
  - title: 未成年人网络保护条例
    url: https://www.gov.cn/zhengce/content/202310/content_6911288.htm
    publisher: 中华人民共和国国务院
    date: 2023-10-16
authors:
  - anoni-net
---

The European Commission declared its age verification app technically ready in April and urged member states to launch it by the end of the year. On 17 September it proposed the EU KIDS Act, under which online services and app stores must use age assurance tools, children under 13 are kept off social media, and 15 becomes the minimum age for an account of one's own. On 7 September the digital rights network EDRi published a technical analysis arguing that tools pitched as "ready" and "privacy-preserving" fail on both counts.

What the Commission released in July 2025 was a blueprint, nicknamed the "mini wallet", for each country to build its own app on the specifications of the EU Digital Identity Wallet. EDRi's main points are that the Commission has weakened the legal duty to "ensure" unlinkability to merely "hindering" it; that anchoring the app to state ID plus facial recognition excludes people without ID, a suitable phone, or willingness to be scanned; and that credentials still carry salts, hashes, public keys, signatures and timestamps an issuer could link back to a person. EDRi also noted that the specification only said implementations "SHOULD" use zero-knowledge proofs. Version 1.1.0 of the specification, merged on 2 September, makes them the preferred method but keeps a plain verification fallback.

## Perspective {#perspective}

Anonymous age verification rests on unlinkability: a site should learn only that you are old enough, and whoever issued the credential should not learn where you used it. Zero-knowledge proofs can show that a condition holds without revealing anything else, but the specification still recommends that the credential issuer also runs the app. EDRi argues this puts issuing and presentation in the same hands, and that mandating zero-knowledge proofs alone would not deliver strict unlinkability.

Openness is patchy too. The Commission's reference apps are open source under EUPL-1.2, but EDRi points out that the open-source requirement covers national identity wallets, not national age verification apps, and that Denmark's app has proprietary code on the client side. With 27 member states, EDRi expects 27 different designs and levels of protection.

Asia-Pacific governments are already choosing their own models, and they differ on exactly the points EDRi raises. Since 10 December 2025, Australia has required platforms to keep under-16s off social media, while its law bars platforms from compelling anyone to provide government ID or use the government's digital ID. eSafety reports that platforms had removed access to 4.7 million under-16 accounts by mid-December 2025. Malaysia has required social media platforms to verify users' ages since 1 June 2026. In mainland China, the Regulations on the Protection of Minors Online, in force since 1 January 2024, require services offering posting and instant messaging to minors to obtain the minor's real identity information.

For anyone following these laws, EDRi's analysis doubles as a checklist. Ask whether zero-knowledge proofs are mandatory, whether the issuer and the app are kept separate, whether the app is open source, and whether there is an alternative that needs neither ID documents nor a face scan.
