---
title: Zero-click spyware delivered through targeted ads
description: Citizen Lab published a report on 15 October linking, with high confidence, attacks on at least 45 Al Jazeera devices between 2024 and 2025 to targeted ads from the Israeli ad firm Discover-Tech and spyware from Candiru. Al Jazeera is the only confirmed target, and the exploited vulnerabilities are not described. The advice for general readers is to block ads and limit advertising IDs, which according to the report lowers only part of the risk.
date: 2026-10-19T00:00:00+08:00
slug: adfection-targeted-ads-spyware
categories:
  - surveillance
sources:
  - title: "Exposing AdFection: How Discover-Tech Turned Targeted Ads Into a Pipeline for Zero-Click Mercenary Spyware"
    url: https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/
    publisher: Citizen Lab
    date: 2026-10-15
  - title: Exposing AdFection Executive Summary
    url: https://citizenlab.ca/research/exposing-adfection-executive-summary/
    publisher: Citizen Lab
    date: 2026-10-15
  - title: "Re: Citizen Lab Right to Reply"
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Citizen-Lab-Right-to-Reply-IAB.pdf
    publisher: IAB Europe
    date: 2026-10-15
  - title: "Re: Citizen Lab Report Right to Reply"
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Adtimizer-Response-to-Request-for-Comment.pdf
    publisher: Adtimizer
    date: 2026-10-11
  - title: Citizen Lab Right of Reply
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Volasim-Response-to-Request-for-Comment.pdf
    publisher: Volasim
    date: 2026-10-12
  - title: Israeli ad-tech firm helped place spyware on Al Jazeera devices
    url: https://www.aljazeera.com/news/2026/10/15/israeli-ad-tech-firm-helped-spy-on-al-jazeera-devices
    publisher: Al Jazeera
    date: 2026-10-15
  - title: Targeted ads delivered 0-click exploits to install mercenary malware
    url: https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/
    publisher: Ars Technica
    date: 2026-10-15
  - title: Online ads weaponised to deliver ‘zero-click’ spyware, researchers say
    url: https://www.theguardian.com/technology/2026/oct/15/israeli-firm-digital-ads-enabling-installation-of-zero-click-spyware-researchers-say
    publisher: The Guardian
    date: 2026-10-15
  - title: First Zero-Click Mercenary Spyware Delivered Via Targeted Ads Uncovered by CitizenLab
    url: https://www.privacyguides.org/news/2026/10/16/first-mercenary-spyware-delivered-via-targeted-ads-uncovered-by-citizenlab/
    publisher: Privacy Guides
    date: 2026-10-16
  - title: 以色列廣告業者利用定向廣告發動零點擊攻擊，半島電視臺裝置遭間諜軟體入侵
    url: https://www.ithome.com.tw/news/179747
    publisher: iThome
    date: 2026-10-16
  - title: 如果 App 要求追蹤你的活動
    url: https://support.apple.com/zh-tw/102420
    publisher: Apple
  - title: 廣告 ID
    url: https://support.google.com/googleplay/android-developer/answer/6048248?hl=zh-Hant
    publisher: Play 管理中心說明
  - title: If an app asks to track your activity
    url: https://support.apple.com/en-us/102420
    publisher: Apple
  - title: Advertising ID
    url: https://support.google.com/googleplay/android-developer/answer/6048248?hl=en
    publisher: Play Console Help
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021
    publisher: Laws & Regulations Database of the Republic of China (Taiwan)
  - title: 自分に関する情報が第三者に送信される場合、 自身で確認できるようになります。
    url: https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/gaibusoushin_kiritsu.html
    publisher: Ministry of Internal Affairs and Communications
  - title: 맞춤형 광고에 쓰이는 “행태정보” 처리, 적법성과 투명성 높인다
    url: https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=9888
    publisher: Personal Information Protection Commission
    date: 2024-01-31
  - title: Is https://citizenlab.ca blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/citizenlab.ca
    publisher: GreatFire
authors:
  - anoni-net
---

Online ads from the Israeli ad firm Discover-Tech were used to deliver mercenary spyware, the commercial spyware sold to government clients, and an ad only had to appear on screen to trigger it, according to Citizen Lab's AdFection report published on 15 October. Citizen Lab links attacks on Al Jazeera between 2024 and 2025 with high confidence to spyware from the Israeli vendor Candiru, with at least 45 devices targeted. Al Jazeera is the only confirmed target in the report, while Discover-Tech's ads appeared on nearly 200,000 websites and apps, and an ad impression on its own does not mean someone was targeted. The exploited vulnerabilities and affected versions are not described, the sample the researchers obtained was a Windows executable isolated from one victim's device, and the report does not confirm that any phone was infected.

Most online ads are sold through real-time bidding (RTB), an auction held each time an ad is about to be shown, in which advertisers bid to show a given ad to a particular user, and an ad can carry code that runs inside an app or browser. According to the report, many Discover-Tech ads carried a tag that, when displayed, connected back to the company's server and sent the user's advertising ID or cookie ID. The server returned code only for chosen targets, which customers of Discover-Tech's platform could select by a phone's advertising ID, a browser's cookie ID or an IP address, and everyone else received an empty response; in the report's assessment, those customers include spyware vendors such as Candiru. Per the report, this design meant Discover-Tech never had to hand the malicious code, or even a link to it, to the platforms that ran its ads.

The researchers found two world-readable databases on Discover-Tech's website holding about 3.77 billion bid records from March to June 2026, of which about 440 million appear to have been won. At least 720 million of the bids were for ads that, judging by their names, carried a tag connecting back to these servers, and more than 70 percent of all the bids were in apps. The networks where the ads were shown, as listed in the report, include those of NATO, the United Nations, the European Parliament and the governments of more than 20 countries. In Citizen Lab's assessment, these impressions at least let Discover-Tech profile the devices and in some cases may have let other vendors' code run on them, but an impression is not confirmation of targeting or infection.

According to the companies' replies attached to the report, Google ended Discover-Tech's bidding and ad serving on its ad exchange and uses Safe Browsing to show warnings for known domains. Beeswax, Vungle (Liftoff) and Eskimi also stopped or paused their work with the company. According to IAB Europe's letter, Discover-Tech has been suspended since 8 October from the vendor list (GVL) of its Transparency and Consent Framework after an audit found breaches of framework policy, while the report's main text describes it as removed. Discover-Tech and Candiru did not respond by the report's deadline, and as of 18 October we could find no public statement from either.

Two more companies, Adtimizer and Volasim, are named in the report. Adtimizer's reply states that it only assigned some subdomains for general advertising use and that those subdomains were used only within Discover-Tech's infrastructure. Volasim's reply states that Discover-Tech was one of several outside advertising agencies it hired to promote its products, and that it is willing to provide its source code for independent review under a non-disclosure agreement. Citizen Lab sees links between both firms and Discover-Tech but notes that there is no firm evidence either took part knowingly.

## Perspective {#perspective}

The surveillance industry calls platforms that use advertising data to identify and track specific people advertising intelligence (ADINT). According to the report, a company with access to bidding data can follow one person's movement across places and networks from bid requests carrying the same identifier, and in our reading AdFection connects this kind of identification to attack code. Citizen Lab's view is that these industry vendor lists appear to rely mostly on vendors' self-declarations. IAB Europe's letter, for its part, states that being listed does not mean IAB Europe certifies that all of a company's activities comply with the GDPR, and that it has neither the capacity nor the mandate for forensic or criminal investigations.

Citizen Lab's advice for general users is to install a trusted ad-blocking browser extension, switch to a browser that blocks tracking, regularly reset the phone's advertising ID and turn off ad tracking, and block ads at the home router or through a trusted VPN service. For security staff at organisations, its judgement is that the most practical defence for now is to block targeted ads at the network's egress (the gateway), until the industry shows it can reliably stop this technique. With no exploited vulnerability named in the report, there is no way to tell which update fixes it, and Ars Technica separately advises installing updates promptly.

Rules on the data behind targeted ads vary across Asia. Taiwan's Personal Data Protection Act has no provision on advertising identifiers, real-time bidding or targeted ads. Its Article 20 does require a non-government entity that markets with personal data to stop once the person objects, and to offer a way to object the first time it markets to them (we read the current text of the statute as of 18 October, not its enforcement rules or regulators' interpretations; amendments passed on 11 November 2025 take effect on a date the Executive Yuan has yet to set). South Korea's Personal Information Protection Commission published a policy plan on 31 January 2024 to protect the online behavioural data used in targeted ads, though as of 18 October we could not find whether its revised guidelines are in force.

Japan amended its Telecommunications Business Act in June 2022. According to the Ministry of Internal Affairs and Communications page, which shows no update date, websites and apps that send user data to outside parties through tags or information-collection modules must give notice of what is sent, publish it, obtain consent or offer a way to stop it. The rule does not ban targeted ads, and it covers online information services such as messaging, social media, search and news rather than corporate websites or personal blogs. In mainland China, the censorship-monitoring project GreatFire found Citizen Lab's own site, `citizenlab.ca`, where the report is published, fully blocked in tests up to 16 October, based on the last two conclusive tests, with interference recorded since 20 July 2017.

Citizen Lab advises people at higher risk because of their work or identity to seek expert help. Everyone else can start by limiting advertising IDs. On iPhone, go to Settings → Privacy & Security → Tracking and turn off Allow Apps to Request to Track (iOS 14.5 or later). On Android, Google's instructions are Settings → Privacy → Ads → Delete Advertising ID (this requires Google Play services), and we checked both companies' help pages on 18 October.

According to the report, these steps lower only part of the risk. In its advice to organisational security staff, Citizen Lab notes that blocking advertising IDs stops Discover-Tech's current method, but the researchers suspect this kind of attack reaches further. In our reading, resetting a phone's advertising ID does nothing against targets picked by cookie ID or IP address. The vulnerabilities have not been disclosed, so there is no way to tell which update would fix them.
