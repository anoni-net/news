---
title: The Ninth Circuit appeal over a cell tower dump warrant
description: The US Court of Appeals for the Ninth Circuit is hearing an appeal over a tower dump warrant, which demands location data for every phone in a given place at a given time from mobile carriers. EFF and the ACLU argue that these warrants are unconstitutional in themselves. As of 8 November we could not find a government brief in the appeal, and our inference is that turning off Google Location History does not stop a tower dump.
date: 2026-11-13T00:05:00+08:00
slug: ninth-circuit-reverse-location
categories:
  - surveillance
regions:
  - US
sources:
  - title: We’re Asking the Ninth Circuit to Hold Reverse Location Warrants Categorically Unconstitutional
    url: https://www.eff.org/deeplinks/2026/11/were-asking-ninth-circuit-hold-reverse-location-warrants-categorically
    publisher: EFF
    date: 2026-11-04
  - title: Brief of Amici Curiae, No. 26-689 (9th Cir.)
    url: https://www.eff.org/files/2026/11/03/united_states_v._spurlock_-_eff_aclu_amicus_brief_1.pdf
    publisher: EFF
    date: 2026-11-03
  - title: Uncle Sam seeks time in tower dump data grab case after judge calls it 'unconstitutional'
    url: https://theregister.com/2025/06/19/us_tower_grab_appeal/
    publisher: The Register
    date: 2025-06-19
  - title: Court rules that law enforcement’s use of “geofence warrant” was a “search”
    url: https://www.scotusblog.com/2026/06/court-rules-that-law-enforcements-use-of-geofence-warrant-was-a-search/
    publisher: SCOTUSblog
    date: 2026-06-29
  - title: Supreme Court Holds Geofence Warrants Are Fourth Amendment Searches, But Leaves Other Important Questions for Lower Courts
    url: https://www.zwillgen.com/law-enforcement/supreme-court-holds-geofence-warrants-are-fourth-amendment-searches-leaves-other-important-questions-lower-courts/
    publisher: ZwillGen
    date: 2026-07-02
  - title: Federal Appeals Court Finds Geofence Warrants Are “Categorically” Unconstitutional
    url: https://www.eff.org/deeplinks/2024/08/federal-appeals-court-finds-geofence-warrants-are-categorically-unconstitutional
    publisher: EFF
    date: 2024-08-12
  - title: Supreme Court grapples with limits to 'geofence warrants' over privacy concerns
    url: https://www.goodmorningamerica.com/amp/news/story/supreme-court-weighs-geofence-warrants-cellphone-data-132358022
    publisher: ABC News
    date: 2026-04-28
  - title: No. 25-112 (U.S. June 29, 2026)
    url: https://www.independent.org/article/2026/06/30/supreme-court-geofence-warrants-chatrie/
    publisher: Independent Institute
    date: 2026-06-30
  - title: Updates to Location History and new controls coming soon to Maps
    url: https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/
    publisher: Google
    date: 2023-12-12
  - title: Manage your Google Maps Timeline
    url: https://support.google.com/maps/answer/6258979?hl=en
    publisher: Google Maps Help
  - title: "Apple Transparency Report: Government and Private Party Requests, July 1 - December 31, 2025"
    url: https://www.apple.com/legal/transparency/pdf/requests-2025-h2-en.pdf
    publisher: Apple
  - title: 通訊保障及監察法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060044
    publisher: 全國法規資料庫
  - title: 刑事訴訟法（昭和二十三年法律第百三十一号）
    url: https://laws.e-gov.go.jp/law/323AC0000000131
    publisher: e-Gov 法令検索
authors:
  - anoni-net
---

The US Court of Appeals for the Ninth Circuit is hearing an appeal over a tower dump warrant, which requires a mobile carrier to hand over location data for every phone in a given place at a given time, including devices that have nothing to do with the case. On 3 November the digital rights group EFF (Electronic Frontier Foundation) and the American Civil Liberties Union (ACLU) filed an amicus brief, a filing in which a non-party offers its views to the court, arguing that these warrants are unconstitutional in themselves. The case concerns law enforcement in the United States only, and readers elsewhere are not directly affected.

EFF's article groups tower dumps and geofence warrants together as "reverse location searches", in which police start from a time and a place and then look for people in the data. A tower dump is demanded from a mobile carrier and a geofence warrant from a company such as Google that holds device location records, so the data comes from different sources. The US Supreme Court's 29 June ruling dealt with geofence warrants, while the Ninth Circuit appeal (case number `26-689`) concerns a tower dump.

According to EFF's article, the bodies of two victims were found beside a remote highway in California, and police found a car belonging to one of them several miles away on the same highway. Police then sought a tower dump warrant covering that stretch of road and eventually obtained location data on nearly 1,700 unique phones.

According to the ruling as quoted by The Register, a federal district court in Nevada held in 2025 that a tower dump is a search under the Fourth Amendment to the US Constitution, which bars unreasonable searches and seizures, and that the warrant in this case was a general warrant (one not limited to particular targets) forbidden by the amendment. The court still suppressed no evidence, because it appeared to be the first court within the Ninth Circuit to reach that conclusion and because the good faith exception applied. Under that exception, evidence can generally still be used when officers believed they were acting lawfully under a warrant. The defendant then appealed to the Ninth Circuit.

EFF and the ACLU make three arguments in the brief, according to EFF's article. The Supreme Court's geofence ruling strengthens the case that tower dumps are unconstitutional general warrants, since police cannot search everyone in an area without probable cause, the concrete grounds a warrant requires, to believe all of them were involved. If the court still allows these warrants, it must limit their scope and duration, require notice to the people affected and require irrelevant data to be deleted afterwards. The brief also asks the court to set aside the good faith exception and actually decide the constitutional question.

By 6 to 3, the Supreme Court held in the geofence case that police carry out a search when they demand a phone's location records, even for a short period and even when a third-party company holds the data. According to an analysis by the law firm ZwillGen, the Court sent back to the Fourth Circuit, which had heard the case earlier, the question of whether that warrant was sufficiently particular and supported by probable cause, and the constitutionality of reverse warrants remains unresolved. EFF's article describes the Ninth Circuit appeal as the first case of its kind before a federal appeals court since the ruling.

## Perspective {#perspective}

A phone that is powered on and not in airplane mode connects to cell towers, which is how mobile networks work (background we are adding, which the sources below do not state directly). SCOTUSblog, summarizing the Supreme Court's 2018 cell-site case, describes cell-site location information as a historical record created when a phone connects to a cell site. According to The Register, a tower dump can cover all connections to a tower within windows ranging from ten minutes to one hour.

Location History on a Google account, the setting behind Google Maps Timeline, is separate data kept on the device or on Google's servers, and on that basis we infer that turning it off does not stop a tower dump. The sources we found describe no way for users to avoid tower records, and they do not say which connections leave records that can be demanded or how long carriers keep them.

As of 8 November we could find neither a government brief in the Ninth Circuit appeal nor any reporting on one. Under the general rule of federal appellate procedure a response brief is usually due 30 days after the appellant's, so the absence may only mean the deadline has not arrived (this is our own calculation, and we did not find the docket). The government arguments in the next paragraph all come from a different case, the Supreme Court's geofence case and the Fourth Circuit decision in that same case, where the data came from Google and no carrier was involved.

According to ABC News, the government argued in the geofence case that users give up their expectation of privacy when they share location information with apps and service providers such as Google. The Fourth Circuit's majority also held, per SCOTUSblog, that the defendant could not reasonably expect two hours of location data, voluntarily left with Google, to be kept private. The Supreme Court's majority held that a person keeps an expectation of privacy even when a third-party company holds the data, and its 2018 cell-site ruling had already treated obtaining cell-site location information as a search outside the third-party doctrine, the view that records handed to a third party are not protected by the Fourth Amendment (as summarized by SCOTUSblog and the Independent Institute). These sources do not say whether the 2018 ruling reaches tower dumps, so how the government will argue and whether the court will accept it depends on how the appeal proceeds.

EFF's article argues that reverse location warrants are unconstitutional in themselves, and compares them to the rule that bars police from searching the houses of a hundred people near a crime scene. According to The Register, a federal magistrate judge in Mississippi rejected four FBI tower dump warrants in February 2025 for lack of probable cause as to specific individuals, and in June 2025 the government asked for more time to decide whether to appeal (as of 8 November we could not find the outcome). ABC News reported that geofence warrants have become increasingly valuable to investigators looking for criminal suspects, missing children and hikers lost in the wilderness, and that experts believe limits could hamper law enforcement. At oral argument in the geofence case, one justice suggested setting reasonable limits on time and geography and leaving it to the judges who issue warrants to apply them.

The district court found the warrant unconstitutional but kept the evidence because of the good faith exception. EFF's article argues that courts too often avoid the constitutional questions raised by new surveillance techniques, leaving police able to keep using them for years or even decades with no definitive ruling. According to EFF's 2024 article, the Fifth Circuit applied the good faith exception in a separate geofence case because the technology was still novel in 2018 and police had sought guidance from more experienced agencies. A dissent at the Supreme Court also rested on good faith, reasoning that since the Fourth Circuit had already found the exception applied, the ruling would have no practical effect on the defendant.

To check the Google side, open the Your Timeline settings in the Google Maps app on Android or iPhone and see whether Timeline, the view tied to Location History, is turned on. According to Google's 2023 announcement and its help page as read on 8 November, Timeline is off by default, turns on only if you opt in, and is stored on the device. If you choose to back it up, an encrypted copy is kept on Google's servers. Apple's transparency report for the second half of 2025 states that Apple has no data to provide in response to geofence requests.

According to a Supreme Court dissent and the Independent Institute's analysis, Google has changed its Location History service so that it can no longer respond to geofence warrants. The Independent Institute's analysis dates the change to July 2025, and as of 8 November we had found no statement from Google itself. The settings and report above concern only data held by Google and Apple.

Taiwan's Communication Security and Surveillance Act (通訊保障及監察法, in the version amended in July 2024 on the Laws & Regulations Database) counts location information among communication records. A prosecutor must in principle apply to a court for a retrieval order (調取票), but for offences with a minimum sentence of ten years and for listed offences such as fraud and robbery, a prosecutor can obtain the records on their own authority, or a judicial police officer can with a prosecutor's approval. The Act does not say whether it covers a dump of every connection to a given tower in a given period (our own reading of the text, and as of 8 November we had found no official explanation). The US appeal turns on probable cause and how specific a search must be, while Taiwan's text sets a threshold of necessity and relevance and lets some offences bypass the court (also our own comparison).

Under Japan's Code of Criminal Procedure (刑事訴訟法), Article 197(2) lets investigators send an inquiry (照会) to public offices and to public or private organizations and ask them to report necessary matters, and Article 197(3) lets prosecutors, their assistant officers and judicial police officers ask carriers to keep specified communication logs (通信履歴), such as sender, recipient and time, from being erased for up to 30 days, for the purpose of seizure or an order to provide electronic records, a preservation request that does not itself hand over the data. As of 8 November we could not find an official explanation of whether cell tower location data is obtained through a court warrant (令状) for seizure or inspection or through an inquiry.

Whether the Ninth Circuit actually decides the constitutional question or stops again at the good faith exception remains open. If tower dump warrants stay available, it is also unclear whether limits on scope, duration, notice and deletion can protect bystanders without taking an investigative method away from cases with no leads on a suspect. Nor is it known whether the government's brief will repeat the argument that users hand over their data voluntarily, or explain how carrier records differ from Google's data.
