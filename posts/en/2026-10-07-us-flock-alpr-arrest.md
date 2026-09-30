---
title: US Police License Plate Readers and a Florida Arrest
description: How US police use Flock's license plate reader cameras drew a run of developments in August and September, including Flock's changes to retention and auditing, a Senate hearing, restrictions in Florida and Texas, and a civil suit after prosecutors declined to charge a driver. The practices are confined to the US, and readers elsewhere are not directly affected.
date: 2026-10-07T00:00:00+08:00
slug: us-flock-alpr-arrest
sources:
  - title: "Engineering and Operations Memorandum No. 26-01: Revocation of General Use Permits for Automated License Plate Readers"
    url: https://fdotwww.blob.core.windows.net/sitefinity/docs/default-source/design/bulletins/eom26-01.pdf
    publisher: Florida Department of Transportation
    date: 2026-08-31
  - title: Joint Statement on Automated License Plate Recognition (ALPR) Technology
    url: https://www.sheriffs.org/wp-content/uploads/2026/08/Final-Joint-Law-Enforcement-Statement-on-ALPR-August-25-2026.pdf
    publisher: National Sheriffs' Association
    date: 2026-08-25
  - title: Flock Updates Privacy, Accountability, Security, and Transparency Safeguards
    url: https://www.flocksafety.com/blog/flock-guardrails-address-lpr-privacy-concerns-and-police-transparency
    publisher: Flock Safety
    date: 2026-08-13
  - title: Complaint, Case No. 6:26-cv-01263 (M.D. Fla.)
    url: https://storage.courtlistener.com/recap/gov.uscourts.flmd.461176/gov.uscourts.flmd.461176.1.0.pdf
    publisher: CourtListener
    date: 2026-06-08
  - title: "The High Crime of “LMAO”: How Cops Are Treating Flock's Mass Surveillance As a Joke"
    url: https://www.eff.org/deeplinks/2026/09/high-crime-lmao-how-cops-are-treating-mass-surveillance-joke
    publisher: EFF
    date: 2026-09-14
  - title: Texas and Florida Step Back from ALPRs
    url: https://www.eff.org/deeplinks/2026/09/texas-and-florida-step-back-alprs
    publisher: EFF
    date: 2026-09-02
  - title: Innocent woman says police use of Flock camera led to 13 days in jail
    url: https://www.foxnews.com/tech/innocent-woman-says-police-use-flock-camera-led-13-days-jail
    publisher: Fox News
    date: 2026-09-09
  - title: Abbott blocks state agencies from spending money on Flock cameras
    url: https://www.texastribune.org/2026/08/28/texas-greg-abbott-flock-cameras-order-state-money/
    publisher: The Texas Tribune
    date: 2026-08-28
  - title: Flock cameras draw bipartisan concerns at Senate hearing
    url: https://rollcall.com/2026/09/23/flock-cameras-draw-bipartisan-concerns-at-senate-hearing/
    publisher: Roll Call
    date: 2026-09-23
  - title: Pinal County sheriff accuses Flock of ‘dishonesty’ about its cameras
    url: https://cronkitenews.azpbs.org/2026/09/24/flock-dishonesty-pinal-sheriff/
    publisher: Cronkite News
    date: 2026-09-24
  - title: RI Police Departments and Flock Safety’s Non-Transparent “Transparency”
    url: https://www.riaclu.org/news/ri-flock-non-transparent/
    publisher: ACLU of Rhode Island
    date: 2026-08-31
  - title: Police Power Exercise Act
    url: https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=D0080145
    publisher: Laws & Regulations Database of The Republic of China (Taiwan)
  - title: 警察職權行使法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080145
    publisher: Laws & Regulations Database of The Republic of China (Taiwan)
  - title: 運用科技執法查扣車輛之問題探討
    url: https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=6590&pid=217015
    publisher: Legislative Yuan
    date: 2022-01-26
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: National People's Congress
    date: 2021-08-20
regions:
  - US
authors:
  - anoni-net
---

A US Senate Judiciary subcommittee held a hearing on 23 September on Flock Safety's network of automated license plate readers (ALPRs, cameras that log each passing vehicle's plate, time and place for later search). A woman who had been arrested and later cleared by prosecutors testified. Texas and Florida both restricted these cameras at the end of August. All of this happens inside the US, and readers in Asia and elsewhere are not directly affected.

Through public records requests, the Electronic Frontier Foundation (EFF) obtained Flock search logs in which officers gave reasons such as `LOL`, `idk`, `TBD` and strings of keyboard mashing, and more than 30 agencies ran over 6,300 searches with `TBD`. According to the Texas Tribune, the governor of Texas ordered state agencies on the night of 27 August to pause funding for Flock cameras. On 31 August, Florida's Department of Transportation revoked permits for plate readers on state highway rights-of-way, gave 30 days to remove them, and stopped issuing new permits. Per EFF, the Florida order leaves city streets and private land untouched, and the Texas order leaves city, county, federal and private money untouched.

The woman at the hearing was arrested over a hit-and-run on Interstate 4 in Florida in October 2025 that killed three people. According to her federal complaint, a Flock camera recorded her black Dodge Durango about three miles west of the scene two minutes before the crash, and from time and distance the complaint argues she had already passed the crash site. State troopers arrested her in April 2026 on eight felony charges, and she spent 13 days in jail. Prosecutors declined to proceed on 22 May, and another woman, alleged to have driven a maroon Durango, was arrested later.

In a civil rights suit against two troopers, she alleges that they claimed damage on her car in the warrant affidavit and in court testimony that was not there, and left out a 911 call describing a maroon Durango with a partial plate. As of 1 October, no public response from the two troopers could be found, and the Florida Highway Patrol did not respond to Fox News.

## Perspective {#perspective}

According to Flock's announcement of 13 August, its system reads plates with machine-learning models trained on each state's plate designs and attaches a confidence score to every read. Low-confidence reads do not trigger alerts to officers. According to the Texas Tribune, Flock also logs make, model and colour, and agencies in its national lookup can search one another's data. The same announcement cut the recommended default retention from 30 days to 7, and existing customers keep their current settings.

In a joint statement on 25 August, ten law enforcement associations wrote that a plate reader provides an investigative lead, does not establish guilt, and must be verified before enforcement action. In a statement to Fox News, Flock wrote that its cameras do not identify perpetrators or make arrest decisions, and that the read in the Florida case accurately placed the woman's car three miles away two minutes before the crash. A specialised Florida Highway Patrol team later examined her car at prosecutors' request and found no damage suggesting a collision. In an interview, she put the problem on how police interpreted the camera data.

EFF writes that Flock announced in late 2025 that free-text reasons would give way to a dropdown menu, and that the system does not require proof that the chosen reason matches the real purpose. Among agencies EFF contacted, some replied that officers had been counselled or that case numbers are now required, and one sheriff's office replied that its `idk` searches all related to active investigations. Under Flock's announcement, every law enforcement search will need a case code by the end of 2026, with emergency searches allowed through but flagged for administrator review. Audit Assistance, which flags abnormal searches, will also become mandatory by then, and accounts that meet abnormal-use criteria will be suspended pending review.

In their joint statement, the law enforcement associations stress that sharing and searching across jurisdictions is critical, governed by access controls, audits and accountability. In a letter to a sheriff in Arizona, Flock wrote that a fixed camera capturing a vehicle in plain view at a specific moment does not violate the Fourth Amendment, the US constitutional protection against unreasonable searches. EFF writes that police need a warrant from a judge to obtain phone location records but not to search ALPR databases. The Institute for Justice, a public interest law firm, released revised model legislation in September requiring a warrant for historical location data in most cases, and its witness at the hearing said this would not stop police from finding a missing child or a stolen car.

Florida's transportation memo gives its reasons as the rapid growth of deployments along with reports of misuse, data privacy concerns and surveillance schemes. In a statement to the Texas Tribune, Flock wrote that its technology helps officers solve serious crimes, find missing people and recover stolen vehicles, and its announcement puts the July figures at more than 1,000 missing people and over 20,000 stolen cars detected. A sheriff in Arizona ended his county's Flock contract in August and testified that the company's account of whether its newer cameras use AI did not match what he later found. His county still uses non-Flock plate readers on other vehicles.

In Taiwan, the Police Power Exercise Act lets police collect data with cameras or other technology tools in public places where crime is frequent or reasonably expected. The data must be destroyed within one year unless needed to investigate a suspect or an illegal act. A 2022 research note published by the Legislative Yuan treated plate numbers as indirectly identifying personal data and questioned a pilot, run by the Administrative Enforcement Agency with police from December 2021 on the Suhua Highway, that used plate readers to stop drivers with unpaid fines and seize their cars. According to the note, such reuse would need its own legal basis, so the Taiwanese debate turns on reusing data collected for one purpose, while the US debate turns on whether a search needs a judge's approval.

In mainland China, the Personal Information Protection Law classes whereabouts as sensitive personal information, to be processed only for a specific purpose with sufficient necessity. Image-capture and identity-recognition devices in public places must be necessary for public security, and what they collect may be used only for that purpose. State organs must act within their statutory authority and procedures and must notify the people concerned, unless notice would impede their duties. Where the US argument centres on judicial approval, the Chinese law works through purpose limits and statutory authority.

Readers outside the US have nothing to change. Readers living in the US can check whether their local police publish a Flock transparency portal, which, according to Flock, more than 1,500 agencies do, listing policy, retention, sharing partners and search activity. The Rhode Island affiliate of the American Civil Liberties Union (ACLU) wrote in August that these portals are public web pages with no login, yet hard to find through search engines, and that some agencies leave out their sharing partners.

Developments to watch include the outcome of the Florida civil suit, the investigation the subcommittee chair announced in August, and whether the case codes and audit requirements Flock promised by the end of 2026 arrive. When comparing places, on privacy ask whether a search needs a judge's approval and how long records are kept. On public safety, ask how many missing people and stolen vehicles the systems actually help find, and whether cases still get solved after cameras come down.
