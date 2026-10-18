---
title: Senate second reading of Canada's Bill C-22 and providers' responses
description: Canada's Bill C-22 on lawful access went to second reading debate in the Senate on 8 October and, as of 18 October, had not passed second reading. A Signal vice president said at a panel that Signal would have to leave Canada if ordered to collect more metadata, while the public safety minister's office said the bill does not require decrypting end-to-end encrypted information. Readers outside Canada do not need to change any settings now.
date: 2026-10-20T00:05:00+08:00
slug: canada-c22-senate-debate
categories:
  - encryption
follows:
  - 2026-10-05-canada-c22-lawful-access
sources:
  - title: C-22 (45-1) - LEGISinfo - Parliament of Canada
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: Debates, Issue 92 (October 8, 2026)
    url: https://sencanada.ca/en/content/sen/chamber/451/debates/092db_2026-10-08-e
    publisher: Senate of Canada
    date: 2026-10-08
  - title: "Parliamentary Committee Notes: appearance before the Standing Committee on Public Safety and National Security (SECU)"
    url: https://publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20260828-1/index-en.aspx
    publisher: Public Safety Canada
    date: 2026-05-05
  - title: Messaging service Signal says minister’s changes to lawful access bill will not persuade it to stay in Canada
    url: https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-06
  - title: Toronto-based VPN provider plans to quit Canada over lawful-access bill
    url: https://www.theglobeandmail.com/politics/article-psiphon-vpn-provider-plans-to-quit-canada-over-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-04
  - title: The Lawful Access Act threatens to blow a hole in Canada’s national security
    url: https://www.theglobeandmail.com/opinion/article-the-lawful-access-act-threatens-to-blow-a-hole-in-canadas-national/
    publisher: The Globe and Mail
    date: 2026-10-09
  - title: The Lawful Access Act’s threats to Canada’s national security
    url: https://citizenlab.ca/the-lawful-access-acts-threats-to-canadas-national-security/
    publisher: Citizen Lab
    date: 2026-10-16
  - title: Telecommunications and Other Legislation Amendment (Assistance and Access) Act 2018
    url: https://www.legislation.gov.au/C2018A00148/latest/text
    publisher: Federal Register of Legislation
  - title: Implementation Rules for Article 43 of the Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region gazetted
    url: https://www.info.gov.hk/gia/general/202007/06/P2020070600784.htm
    publisher: Hong Kong Government
    date: 2020-07-06
  - title: 中华人民共和国反恐怖主义法 (Counter-Terrorism Law of the People's Republic of China)
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: National People's Congress
    date: 2018-06-12
regions:
  - CA
authors:
  - anoni-net
---

Canada's Lawful Access Act, Bill C-22, passed third reading in the House of Commons in June, and the Senate adjourned after its second reading debate on 8 October, with its next sitting on 20 October. According to LEGISinfo, Parliament's bill database, as of 18 October the bill had not passed second reading, and there was no record of it being referred to a committee or receiving Royal Assent (the Governor General's signature that makes it law). Between 4 and 16 October, Signal, the censorship circumvention tool Psiphon and Citizen Lab, a research lab at the University of Toronto, set out their objections in public, while the senator sponsoring the bill for the government (the sponsor) explained its safeguards in a second reading speech. The bill has not passed and the providers' exits are conditional, so in our assessment readers outside Canada do not need to change any settings now.

Signal's vice president of strategy and global affairs spoke at a panel held by the Internet Society's Canada chapter on 5 October, and The Globe and Mail reported it the next day. According to the report, the vice president argued that legal protection for encryption has to cover more than decryption with keys, and that being required to make major changes to the software would equally defeat the purpose of encryption. Signal keeps only users' phone numbers, the date they joined and their last login information, and if ordered to collect more metadata (records about communications rather than their content) and keep it for up to six months, it would have to leave Canada. As of 18 October, Signal's blog and Bluesky account had not published a written statement on C-22.

Psiphon told The Globe and Mail on 2 October that it had begun drawing up plans to move its operations out of Canada if the bill passes as it stands. In a written reply, the company's vice president wrote that every line of its open source code is public, so any access capability the bill required would be visible to the whole world, including the authoritarian governments its users are trying to evade. A senior researcher at Citizen Lab argued in an opinion piece in the same newspaper on 9 October that no design lets law enforcement in while giving other attackers no chance to exploit it, and Citizen Lab republished a summary on its website on 16 October.

According to the sponsor's second reading speech on 8 October, the new law in Part 2 of the bill, which regulates providers' technical capabilities, does not in itself give law enforcement or the Canadian Security Intelligence Service (CSIS) new powers to obtain information. Ministerial orders need approval from the Intelligence Commissioner, an independent official who reviews intelligence authorisations, are subject to independent review and last at most two years. Metadata retention is limited to specified categories for up to six months and excludes communications content and browsing history. A spokesperson for the public safety minister's office told The Globe and Mail that the bill explicitly does not require decrypting end-to-end encrypted information, and does not allow or compel providers to introduce systemic vulnerabilities or backdoors.

## Perspective {#perspective}

According to Public Safety Canada's committee briefing notes from May, a provider that assesses it cannot meet a requirement without introducing a systemic vulnerability (one that affects a whole class of products or many users, not just a single target) does not have to comply, and the government uses the term to mark out what providers need not do. The sponsor also told the Senate that the committee needs to hear technical evidence on how the term works when a capability described as targeted could affect an entire product or update system. A senator quoted Psiphon's view that any legally mandated access mechanism in open source software would be public and could not be limited to Canadian agencies or a single investigation.

Oversight is another point of dispute. In the debate, one senator criticised the exclusion of ministerial orders from the Statutory Instruments Act, the law that sends regulations to Parliament for scrutiny, and another cited a joint brief from Citizen Lab and a civil liberties group saying the bill's obligations can be imposed without judicial authorisation. The sponsor said in the speech that orders and supporting material must go to the National Security and Intelligence Review Agency (NSIRA), an independent body that reviews intelligence and security agencies, and cited support for the bill from a representative of police organisations.

According to Public Safety Canada's briefing notes, Australia has a similar safeguard. Australia's Assistance and Access Act of 2018 likewise provides that a technical capability notice, a written order requiring a provider to build a particular capability, may not require it to build a systemic weakness or systemic vulnerability. The Australian law defines a systemic weakness as one that affects a whole class of technology, excluding a weakness selectively introduced to target a particular person unless it would jeopardise the security of other people's information. In the opinion piece, the Citizen Lab researcher cited Australia's experience, including one company's statement that lost trust caused economic losses of about A$1 billion.

When comparing approaches, it is worth asking who approves an order, whether a court is involved and whether providers may disclose that an order exists. Who decides what counts as a systemic vulnerability, and the scope and duration of metadata retention, can also be compared. Another question is whether the investigative goals behind the policy can be met without weakening encryption.

In Hong Kong, according to the government's 2020 announcement of the implementation rules for Article 43 of the National Security Law, officers may, under specific circumstances, apply to a magistrate for a warrant authorising police to request identification records or decryption assistance from a service provider, and all applications to intercept communications must be approved by the Chief Executive. In mainland China, Article 18 of the Counter-Terrorism Law requires telecom operators and internet service providers to give public security and state security organs technical interfaces and decryption support for preventing and investigating terrorism. Article 18 itself names no approving body and has no exception like Canada's systemic vulnerability. For mainland China we checked only Article 18, and for both places we have not looked into whether providers may disclose a request they receive.

Signal's and Psiphon's exits are both conditional, and as of 18 October neither had announced a date. The Senate's second reading vote after it resumes on 20 October, and which committee the bill goes to, are the next steps to watch. How readers in Canada will be affected depends on the bill's final text and the providers' decisions.
