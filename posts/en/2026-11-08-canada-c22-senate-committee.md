---
title: Senate committee review of Canada's Bill C-22 and the dispute over built-in weaknesses
description: Canada's Bill C-22 on lawful access passed second reading in the Senate on 22 October and went to the Standing Senate Committee on National Security, Defence and Veterans Affairs, and as of 7 November it had not reached third reading. A Citizen Lab researcher argues that AI-driven cyber threats have changed significantly since June and that communications systems should not be left with weaknesses. Public Safety Canada's briefing notes from May argue that the bill does not require backdoors and that providers may decline requirements that would introduce a systemic vulnerability. Readers outside Canada do not need to change any settings now.
date: 2026-11-08T00:05:00+08:00
slug: canada-c22-senate-committee
categories: [encryption]
follows:
  - 2026-10-20-canada-c22-senate-debate
sources:
  - title: C-22 (45-1) - LEGISinfo - Parliament of Canada
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: "Built-In Weakness: Lawful Access and Encryption in the Age of AI-Powered Cyber Threats"
    url: https://citizenlab.ca/built-in-weakness-lawful-access-and-encryption-in-the-age-of-ai-powered-cyber-threats/
    publisher: Citizen Lab
    date: 2026-10-23
  - title: We Shouldn’t Have to Give Up Our Safety Online to Be Safe
    url: https://www.internetsociety.org/blog/2026/10/we-shouldnt-have-to-give-up-our-safety-online-to-be-safe/
    publisher: Internet Society
    date: 2026-10-21
  - title: The Lawful Access Act threatens to blow a hole in Canada’s national security
    url: https://www.theglobeandmail.com/opinion/article-the-lawful-access-act-threatens-to-blow-a-hole-in-canadas-national/
    publisher: The Globe and Mail
    date: 2026-10-09
  - title: Messaging service Signal says minister’s changes to lawful access bill will not persuade it to stay in Canada
    url: https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-06
  - title: Analysis of Proposed Surveillance Law Expansion under Bill C-22
    url: https://citizenlab.ca/research/analysis-of-proposed-surveillance-law-expansion-under-bill-c-22/
    publisher: Citizen Lab
    date: 2026-06-02
  - title: "Parliamentary Committee Notes: appearance before the Standing Committee on Public Safety and National Security (SECU)"
    url: https://publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20260828-1/index-en.aspx
    publisher: Public Safety Canada
    date: 2026-05-05
  - title: Investigatory Powers Act 2016, section 253
    url: https://www.legislation.gov.uk/ukpga/2016/25/section/253
    publisher: legislation.gov.uk
  - title: Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 (updated as on 6.4.2023)
    url: https://www.meity.gov.in/static/uploads/2024/02/Information-Technology-Intermediary-Guidelines-and-Digital-Media-Ethics-Code-Rules-2021-updated-06.04.2023-.pdf
    publisher: Ministry of Electronics and Information Technology, India
    date: 2023-04-06
  - title: Cryptography Law of the P.R.C.
    url: https://www.chinalawtranslate.com/en/cryptography-law/
    publisher: China Law Translate
  - title: 中华人民共和国反恐怖主义法 (Counter-Terrorism Law of the People's Republic of China)
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: National People's Congress
    date: 2018-06-12
regions:
  - CA
authors:
  - anoni-net
---

Canada's Lawful Access Act, Bill C-22, passed second reading in the Senate on 22 October and was referred the same day to the Standing Senate Committee on National Security, Defence and Veterans Affairs. LEGISinfo, Parliament's bill database, lists one committee meeting on 2 November, and as of 7 November the committee had not reported. The bill passed third reading in the House of Commons in June, and during the Senate debate in October, providers of messaging and censorship circumvention tools set out their objections in public. It is not yet law, and readers outside Canada do not need to change any settings now.

The bill would let the government require communications and internet service providers to build technical capabilities that assist law enforcement, and to retain metadata (records about communications other than their content) under regulations. As of 7 November the Senate had passed no amendments, and the bill goes to third reading only after the committee reports.

Citizen Lab, a research lab at the University of Toronto, posted video of a panel discussion on its website on 23 October. The Internet Society (an international organisation with chapters around the world that works for an open and secure internet) was one of the panel's organisers. According to its post, the panel was held for parliamentarians in early October on what lawful access means in an era of AI-powered cyber threats. The Citizen Lab page has a single paragraph of text, which says a senior researcher there spoke about the bill's legal concerns and stressed repairing and preventing vulnerabilities "rather than drilling more holes in our every day communications systems."

In an opinion piece in The Globe and Mail on 9 October, the same researcher argued that AI-driven cyber threats have changed significantly since June. The examples in the piece include OpenAI's AI agents breaking out of their sandbox in July and attacking the software company Hugging Face, and the alarm over Claude Mythos, a model Anthropic has not released publicly. The piece gives no sources for these incidents, and we have not checked the companies' own announcements. Its conclusion is that government officials who assume technology companies can find "safe ways" to weaken cybersecurity protections are misreading the current threat landscape.

Citizen Lab's June submission to the House of Commons committee predates the researcher's October piece and is a legal and policy analysis of the bill, part by part. Its core recommendation is to withdraw Part 2 entirely, the new law governing providers' technical capabilities. One reason given is that the government could impose any obligation on any electronic service provider, including changing how a service operates or embedding surveillance tools in it. The submission mentions AI in only one sentence, which says the bill's potential for intrusiveness will grow as AI-based surveillance techniques increase.

## Perspective {#perspective}

According to Citizen Lab's submission, technical designs altered to meet surveillance obligations are hard to protect, and even the narrower regimes in the United States and New Zealand have been secretly breached by foreign intelligence agencies several times. The submission cites a test by the US National Security Agency (NSA) in which every switch it tested that complied with CALEA, the US law requiring wiretap capability in telecom equipment, had a security flaw. It also cites the intrusion into US lawful intercept systems by Salt Typhoon, a hacking group linked to the Chinese government. Our 7 November summary of [EFF's articles](https://anoni.net/news/en/2026/11/eff-security-worse/) covers how frontier AI models have made finding vulnerabilities cheap, and on 10 October we covered [Anthropic's report on an open-weight model writing browser exploits](https://anoni.net/news/en/2026/10/glm-5-3-cyber-capabilities/).

According to the briefing notes for the public safety minister's appearance before the House committee on 5 May, the government does not support backdoors and the bill does not require them, and the government sets requirements for providers without prescribing a technical solution. A provider that assesses it cannot meet a requirement without introducing a systemic vulnerability (one that affects a whole class of products or many users, not just a single target) does not have to comply. The bill's text now defines systemic vulnerability, and ministerial orders need prior approval from the Intelligence Commissioner, an independent official who reviews intelligence authorisations. Citizen Lab's submission describes the bill's safeguards as flexible and ill-defined, with no limit on their scope.

The Citizen Lab researcher's piece treats AI as a new situation since June, and argues that the government's expectation that providers can meet surveillance obligations and keep systems secure no longer matches the threats. Public Safety Canada's briefing notes predate this argument and relay the view of the Communications Security Establishment (CSE), Canada's signals intelligence and cyber security agency, that the threat of malicious cyber activity already exists. As the notes relay it, CSE assesses that the bill would improve cyber security by moving lawful access from ad hoc, voluntary arrangements to standardised, managed approaches. A spokesperson for the public safety minister's office told The Globe and Mail in early October that the bill does not allow or compel providers to introduce systemic vulnerabilities or backdoors.

The briefing notes say Canada's police and intelligence officers fight tech-savvy criminals and state actors with tools that are decades old, and the government presents the bill as a way to close that gap. In opening remarks at the same panel, the Internet Society's chief executive offered alternatives: stronger digital forensic capacity, better cross-border cooperation, proportionate use of metadata and working relationships with service providers. The premise of the remarks was that once a weakness exists, anyone who finds it can use it.

As of 7 November the bill was still before the Senate committee, and in our assessment readers in Canada do not need to change any settings yet either. The advice in the EFF articles mentioned above, which applies to everyone, is to keep browsers and apps updated, use a password manager and watch for phishing, none of which depends on how the bill turns out. The next things to watch are whether the committee's report amends Part 2 and when the Senate holds third reading.

The United Kingdom's Investigatory Powers Act 2016 also lets the government issue technical capability notices to providers, under section 253. A notice needs approval from a Judicial Commissioner, and the obligations it can impose include removing electronic protection that the provider itself applied. As we covered in September, after Apple received a notice it stopped letting new UK users turn on [iCloud Advanced Data Protection](https://anoni.net/news/en/2026/09/uk-icloud-advanced-data-protection/) from February 2025. In Canada, according to the government's May briefing notes, ministerial orders are approved in advance by the Intelligence Commissioner, and the bill adds an exception that lets providers decline when they assess compliance would introduce a systemic vulnerability.

In our reading, India's rule is narrower than Part 2 of Canada's bill, since it covers identifying who first sent a message rather than technical capabilities in general. Under rule 4(2) of its Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021, a significant social media intermediary that mainly provides messaging must enable identification of the "first originator" of information when a court or the competent authority under section 69 of the Information Technology Act orders it. Such orders are limited to offences involving sovereignty, state security, foreign relations or public order, or rape, sexually explicit material and child sexual abuse material punishable by at least five years, and none may be issued where less intrusive means would be effective. The provider is not required to disclose message contents, other information about the originator or information about its other users, and the rule does not say how an end-to-end encrypted service would meet the requirement.

In mainland China, the duty to give decryption support sits in Article 18 of the Counter-Terrorism Law, which we covered on 20 October. According to an unofficial English translation by China Law Translate, Article 31 of the Cryptography Law, in force since 2020, bars the cryptography management departments, other relevant departments and their staff from requiring commercial cryptography entities and testing and certification bodies to disclose source code and other proprietary information related to cryptography. Article 31 concerns what cryptography regulators may demand of these entities, a separate question from the assistance that Article 18 requires in terrorism cases. In the parts we read (the article headings and Articles 12, 13 and 26 to 32), the translation contains no provision requiring providers to decrypt for law enforcement.

When comparing approaches, it is worth asking who approves an order, whether providers can refuse or disclose it, and who finally decides what counts as a systemic vulnerability. Another question is who reassesses access capabilities already built once the threat environment changes. It is also worth asking whether the investigative goals behind the policy can be met by means that do not weaken encryption, such as digital forensics and cross-border cooperation. Taken from the government's side, the questions are whether standardised access capabilities can close the gap in investigative tools that the briefing notes describe, and whether they can fix the security problems CSE sees in ad hoc, voluntary arrangements.
