---
title: US Police License Plate Readers and a Florida Arrest
description: Flock's license plate reader cameras, used by US police, saw a run of developments in August and September. Flock shortened its default data retention, a Senate subcommittee held a hearing, and Florida and Texas restricted the cameras. A woman who was arrested and then not prosecuted sued two state troopers. The practices are confined to the US, and readers elsewhere are not directly affected.
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

A US Senate subcommittee held a hearing on 23 September on Flock Safety's network of automated license plate readers (ALPRs), cameras that log each passing vehicle's plate, time and place so police can later look up where a car has been. One witness was a woman who had been arrested in a case involving a plate reader record and whom prosecutors later declined to charge. Taiwan also uses plate readers in traffic enforcement, and a 2022 research report for its Legislative Yuan examined whether that data may be reused for other purposes.

The Electronic Frontier Foundation (EFF) requested Flock search logs from agencies under public records laws and published its analysis on 14 September. Officers are supposed to give a reason for each search, and the logs EFF found include `LOL`, `idk`, `TBD` and strings of keyboard mashing, with more than 30 agencies running over 6,300 searches with `TBD`. According to the Texas Tribune, the governor of Texas ordered state agencies on the night of 27 August to pause funding for Flock cameras. On 31 August, Florida's Department of Transportation ordered plate readers removed from state highways within 30 days and stopped issuing new permits, though per EFF the order does not reach city streets or private land, and Texas agencies can still use other funding.

The woman at the hearing was arrested over a hit-and-run on Interstate 4 in Florida in October 2025 that killed three people. According to her federal complaint, a Flock camera recorded her black Dodge Durango heading east about three miles west of the scene two minutes before the crash, and by the complaint's time-and-distance reckoning she had already driven past the crash site when it happened. State troopers arrested her in April 2026 on eight felony charges, and she spent 13 days in jail. Prosecutors declined to proceed on 22 May, and another woman, alleged to have driven a maroon Durango, was arrested later.

In a civil rights suit against two troopers, she alleges that they claimed damage on her car in the warrant affidavit and in court testimony that was not there, and that the affidavit did not mention a 911 call describing a maroon Durango with a partial plate. As of 1 October, the two troopers' response to these allegations was not available to read, and the Florida Highway Patrol did not respond to Fox News.

## Perspective {#perspective}

According to Flock's announcement of 13 August, its system reads plates with machine-learning models trained on each state's plate designs and gives every read a confidence score. Low-confidence reads do not trigger alerts to officers. According to the Texas Tribune, Flock also logs make, model and colour, and agencies in its national lookup can search one another's data. The same announcement cut the recommended default retention from 30 days to 7, and existing customers keep their current settings.

In a joint statement on 25 August, ten law enforcement associations wrote that a plate reader provides an investigative lead, does not establish guilt, and must be verified before enforcement action. In a statement to Fox News, Flock wrote that its cameras do not identify perpetrators or make arrest decisions, and that the read in the Florida case accurately placed the woman's car three miles away two minutes before the crash. A specialised Florida Highway Patrol team later examined her car at prosecutors' request and found no damage suggesting a collision. In an interview, she put the problem on how police interpreted the camera data.

EFF writes that Flock switched search reasons from free text to a dropdown menu in late 2025, and that officers do not have to show the option they pick matches the real purpose. Among agencies EFF contacted, some replied that officers had been counselled or that case numbers are now required, and one sheriff's office replied that its `idk` searches all related to active investigations. Under Flock's announcement, every search will need a case number by the end of 2026, and the system will flag unusual searches for each agency's administrators to review.

In their joint statement, the law enforcement associations stress that sharing and searching across jurisdictions is critical, governed by access controls, audits and accountability. In a letter to a sheriff in Arizona, Flock argued that a fixed camera capturing a vehicle in plain view at a specific moment does not violate the Fourth Amendment, the US constitutional protection against unreasonable searches. EFF writes that police need a warrant from a judge to obtain phone location records but not to search ALPR databases. The Institute for Justice, a public interest law firm, released revised model legislation in September, a template for state lawmakers that would require a warrant for historical location data in most cases, and its legislative counsel told the hearing this would not stop police from finding a missing child or a stolen car.

Florida's transportation memo gives its reasons as the rapid growth of deployments along with reports of misuse, data privacy concerns and surveillance schemes. In a statement to the Texas Tribune, Flock wrote that its technology helps officers solve serious crimes, find missing people and recover stolen vehicles, and its announcement puts the July figures at more than 1,000 missing people and over 20,000 stolen cars detected. A sheriff in Arizona ended his county's Flock contract in August and testified that the company's account of whether its newer cameras use AI did not match what he later found. His county's anti-smuggling unit still uses non-Flock plate readers on its vehicles and trailers.

In Taiwan, the Police Power Exercise Act lets police collect data with cameras or other technology tools in public places where crime is frequent or reasonably expected. The data must be destroyed within one year unless needed to investigate a suspect or an illegal act. The 2022 research report for the Legislative Yuan treated plate numbers as indirectly identifying personal data and questioned a pilot, run by the Administrative Enforcement Agency with police from December 2021 on the Suhua Highway, that used plate readers to stop drivers with unpaid fines and seize their cars. According to the report, such reuse would need its own legal basis, so the Taiwanese debate turns on reusing data collected for one purpose, while the US debate turns on whether a search needs a judge's approval.

In mainland China, the Personal Information Protection Law classes whereabouts as sensitive personal information, to be processed only for a specific purpose with sufficient necessity. Image-capture and identity-recognition devices in public places must be necessary for public security, and what they collect may be used only for that purpose. State organs must act within their statutory authority and procedures and must notify the people concerned, unless notice would impede their duties. Where the US argument centres on judicial approval, the Chinese law works through purpose limits and statutory authority.

Readers living in the US can check whether their local police publish a Flock transparency portal, which, according to Flock's announcement, lists retention, sharing partners and search activity. Readers elsewhere have nothing to change, and developments to watch include the outcome of the Florida civil suit, the investigation the subcommittee chair announced in August, and whether the audit requirements Flock promised by the end of 2026 arrive.

When comparing places, on privacy ask whether a search needs a judge's approval and how long records are kept. On public safety, ask how many missing people and stolen vehicles the systems actually help find, and whether cases still get solved after cameras come down.
