---
title: Canada's Bill C-22, lawful access and encryption
description: Canada's Bill C-22 has passed the House of Commons. It would let the government require communications and internet services, including some outside Canada, to build capabilities for law enforcement access and to retain metadata. Readers outside Canada do not need to change any settings now.
date: 2026-10-05T07:05:00+08:00
slug: canada-c22-lawful-access
sources:
  - title: C-22 (45-1) Lawful Access Act, 2026
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: Bill C-22, Third Reading
    url: https://www.parl.ca/documentviewer/en/45-1/bill/C-22/third-reading
    publisher: Parliament of Canada
  - title: The EU must act now to protect privacy and encryption from Canada’s overreaching Bill C-22
    url: https://www.accessnow.org/press-release/the-eu-must-act-now-canadas-overreaching-bill-c-22/
    publisher: Access Now
    date: 2026-09-14
  - title: Analysis of Proposed Surveillance Law Expansion under Bill C-22
    url: https://citizenlab.ca/research/analysis-of-proposed-surveillance-law-expansion-under-bill-c-22/
    publisher: Citizen Lab
    date: 2026-06-02
  - title: "Open Letter on Bill C-22: An Act respecting lawful access"
    url: https://www.globalencryption.org/2026/04/open-letter-on-bill-c-22-an-act-respecting-lawful-access/
    publisher: Global Encryption Coalition
    date: 2026-04-28
  - title: Signal, DuckDuckGo among firms weighing Canada exit over lawful access bill
    url: https://globalnews.ca/news/11886905/lawful-access-bill-c-22-companies-services-canada/
    publisher: Global News
    date: 2026-06-04
  - title: The UK Is Still Trying to Backdoor Encryption for Apple Users
    url: https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users
    publisher: EFF
    date: 2025-10-01
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: Implementation Rules for Article 43 of the Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region gazetted
    url: https://www.info.gov.hk/gia/general/202007/06/P2020070600784.htm
    publisher: Hong Kong Government
    date: 2020-07-06
  - title: 中华人民共和国反恐怖主义法 (Counter-Terrorism Law of the People's Republic of China)
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: National People's Congress
    date: 2018-06-12
  - title: 如何開啟「iCloud 進階資料保護」
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
    date: 2026-04-24
  - title: How to turn on Advanced Data Protection for iCloud
    url: https://support.apple.com/en-us/108756
    publisher: Apple
    date: 2026-04-17
regions:
  - CA
authors:
  - anoni-net
---

Canada's Lawful Access Act, Bill C-22, passed third reading in the House of Commons on 18 June, and as of 29 September the Senate had not completed second reading. It would let the government require communications and internet services to build capabilities that help law enforcement obtain data, and it reaches some providers outside Canada. In September the digital rights group Access Now and several European civil society groups asked the EU to intervene; Access Now's press release says the bill could become law as early as October. Readers outside Canada do not need to change any settings now.

The capability requirements come in two tiers. "Core providers" must have capabilities set out in regulations, and the public safety minister can order any provider, core or not, to build a particular capability. An order needs approval only from the Intelligence Commissioner, an independent official, rather than a court, and the provider may not disclose that it received one or what it says.

Regulations can also require providers to retain metadata, records about communications rather than their content, for up to one year under the first-reading text and six months under the version the House passed. According to an early June analysis by Citizen Lab, a research lab at the University of Toronto, that metadata would likely cover who each person contacts, their movements and the apps they use.

According to Global News, Signal testified to a House committee in June that if forced to choose between betraying its users and leaving a market, it would leave. DuckDuckGo confirmed to the Canadian broadcaster that it would pull its VPN service from Canada if the bill passed as it stood in early June, before the House amendments.

## Perspective {#perspective}

The text exempts providers from requirements that would introduce a "systemic vulnerability" and does not compel them to decrypt data that users encrypted themselves when the provider holds no key. With end-to-end encryption the keys stay on users' devices, so on the text's wording services like Signal would fall inside that exception. The dispute is over the reach of ministerial orders, which according to Citizen Lab could include changing how a service works or embedding surveillance tools in it. According to an April open letter from the Global Encryption Coalition, written about the first-reading text, the definition of systemic vulnerability is vague, and the version the House passed still does not define encryption.

Comparable powers in Asia come with different checks. According to the Hong Kong government's 2020 announcement of the implementation rules for Article 43 of the National Security Law, officers may, under specific circumstances, apply to a magistrate for a warrant authorising police to request identification records or decryption assistance from a service provider. The same announcement says all applications to intercept communications must be approved by the Chief Executive. In mainland China, Article 18 of the Counter-Terrorism Law requires telecom operators and internet service providers to give public security and state security organs technical interfaces and decryption support for preventing and investigating terrorism.

As of 29 September the bill still needed Senate second and third reading and Royal Assent, and its effect will depend on which providers receive orders. According to EFF, the UK government issued Apple a comparable technical capability notice under the Investigatory Powers Act in January 2025, and Apple removed Advanced Data Protection in the UK rather than build a backdoor. Apple's support page says new UK users cannot turn it on. Data a provider can decrypt, such as cloud backups without end-to-end encryption, is outside the decryption exception.

On an iPhone, Advanced Data Protection end-to-end encrypts most iCloud data, including iCloud Backup and Photos. It requires two-factor authentication and iOS 16.2, macOS 13.1 or the matching versions on every device signed in to the account, and managed and child accounts are not eligible. You also need to set up a recovery contact or a 28-character recovery key first, because Apple cannot help recover the data. It is under Settings, your name, iCloud, Advanced Data Protection (Apple's help page is available in Chinese).
