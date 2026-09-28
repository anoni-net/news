---
title: Canada's Bill C-22, lawful access and encryption
description: Canada's Bill C-22 has passed the House of Commons. It would let the government require communications and internet services, including some outside Canada, to build capabilities for law enforcement access and to retain metadata. Signal and DuckDuckGo are weighing an exit.
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
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: Data encryption
    url: https://www.homeaffairs.gov.au/about-us/our-portfolios/national-security/lawful-access-telecommunications/data-encryption
    publisher: Australian Government Department of Home Affairs
  - title: 中华人民共和国反恐怖主义法 (Counter-Terrorism Law of the People's Republic of China)
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: National People's Congress
    date: 2018-06-12
authors:
  - anoni-net
---

Canada's Lawful Access Act, Bill C-22, passed third reading in the House of Commons on 18 June and as of 29 September is before the Senate, where second reading has not been completed. It would let the government require communications and internet services to build capabilities that help law enforcement obtain data, and it reaches some service providers and people outside Canada. In September, Access Now and several European civil society groups wrote to the EU asking it to press Canada for changes, and Access Now's press release says the bill could become law as early as October.

Part 2 works in two tiers. "Core providers", likely large telecom and satellite companies according to Global News, must have capabilities set out in regulations. The public safety minister can also order any provider to build a particular capability, with approval from the Intelligence Commissioner rather than a judicial warrant, and a provider may not disclose that it has received an order or what it contains. Regulations can also require retention of metadata such as transmission data: Citizen Lab's June analysis described up to one year, and the version passed by the House caps it at six months.

According to Global News, Signal testified to a House committee in June that if forced to choose between betraying its users and leaving a market, it would leave, and DuckDuckGo confirmed that it would pull its VPN service from Canada if the bill passes as written.

## Perspective {#perspective}

The text exempts providers from requirements that would introduce a "systemic vulnerability", and does not compel them to decrypt data that users encrypted themselves when the provider does not hold the keys. With end-to-end encryption, the keys stay on users' devices and services like Signal never hold them, which is the design this exception covers. The dispute is over what a ministerial order can demand. According to Citizen Lab, the obligations could include changing how a service operates or embedding surveillance tools in it, and the metadata involved would at least likely cover who each person contacts, their movements and the apps they use. According to an April open letter from the Global Encryption Coalition, written about the first-reading text, the definition of systemic vulnerability is vague and encryption itself is not defined.

Access built for police can also be used by others, and the coalition's letter gives the 2024 Salt Typhoon campaign as an example. Attackers used ordinary software bugs and stolen credentials to get into US telecom networks, then took over the wiretap capabilities those networks were required to build.

The closest precedents are elsewhere in the Five Eyes and in Asia. After a secret UK order to Apple under the Investigatory Powers Act, Apple stopped letting new users in the UK turn on Advanced Data Protection for iCloud. As the coalition's letter describes it, Apple withdrew the feature rather than give the government a way into encrypted data. Australia's Assistance and Access Act 2018 lets agencies require help from industry, and the Department of Home Affairs' page says nothing in it can require companies to break encryption. Citizen Lab's analysis notes that the Australian regime went through 173 amendments before passing and that the parliamentary human rights committee found it incompatible with human rights. In mainland China the obligation is explicit: Article 18 of its Counter-Terrorism Law requires telecom operators and internet service providers to give public security and state security organs technical interfaces and decryption support.

Readers outside Canada do not need to change any settings now. The bill still needs Senate second and third reading and Royal Assent, and its effect will depend on which providers receive orders they are not allowed to disclose. Because the decryption exception only covers encryption where the provider has no key, data the provider can decrypt, such as cloud backups without end-to-end encryption, is outside it. Checking whether the apps you rely on encrypt their backups end to end is a reasonable step regardless of where you live.
