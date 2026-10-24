---
title: Quad9's exit from France and French DNS blocking orders
description: Public DNS resolver Quad9 announced on 22 October that from 24 November it will stop serving users located in France. According to Quad9, a French court applying anti-piracy rules for sports broadcasts ordered it to block a list of domains for users in France. We compare how Taiwan, India and Japan handle site blocking.
date: 2026-10-27T00:00:00+08:00
slug: quad9-exit-france
categories:
  - censorship
regions:
  - FR
sources:
  - title: Farewell, France
    url: https://quad9.net/news/blog/au-revoir-france/
    publisher: Quad9
    date: 2026-10-22
  - title: Frequently Asked Questions
    url: https://quad9.net/support/faq/
    publisher: Quad9
  - title: Locations
    url: https://quad9.net/service/locations/
    publisher: Quad9
  - title: Quad9 Faces New DNS Censorship Legal Challenge in France from Canal+
    url: https://quad9.net/news/press/quad9-faces-new-dns-censorship-legal-challenge-in-france-from-canal/
    publisher: Quad9
    date: 2024-12-10
  - title: Quad9 Turns the Sony Case Around in Dresden
    url: https://quad9.net/news/blog/quad9-turns-the-sony-case-around-in-dresden/
    publisher: Quad9
    date: 2023-12-06
  - title: Quad9’s Opinion of the Recent Court Ruling in Leipzig
    url: https://quad9.net/news/press/quad9-s-opinion-of-the-recent-court-ruling-in-leipzig/
    publisher: Quad9
    date: 2023-03-06
  - title: Tribunal judiciaire de Paris, jugement du 13 mai 2026, RG n° 26/02207
    url: https://torrentfreak.com/images/tribunal-judiciaire_n°2602207_13_05_2026.pdf
    publisher: Tribunal judiciaire de Paris
    date: 2026-05-13
  - title: Blocking Behavior
    url: https://developers.google.com/speed/public-dns/blocking
    publisher: Google for Developers
  - title: 1.1.1.1 Public DNS Resolver
    url: https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/
    publisher: Cloudflare 1.1.1.1 docs
  - title: Innovating to address streaming abuse — and our latest transparency report
    url: https://blog.cloudflare.com/h1-2025-transparency-report/
    publisher: Cloudflare
    date: 2025-12-19
  - title: 著作權法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0070017
    publisher: 全國法規資料庫
  - title: "Mandated DNS Blocking: A Guide for Legal Professionals"
    url: https://www.internetsociety.org/resources/doc/2025/mandated-dns-blocking/
    publisher: Internet Society
    date: 2026-03-30
  - title: 運用 DNS RPZ 自律機制停止解析違法網站處理參考程序
    url: https://www-api.moda.gov.tw/File/Get/moda/zh-tw/Qv1tZuiNEVfsLIl
    publisher: 數位發展部
    date: 2025-01-09
  - title: CANAL+ reaches a new milestone in its fight against audiovisual piracy
    url: https://senalnews.com/en/digital/-canal-reaches-a-new-milestone-in-its-fight-against-audiovisual-piracy
    publisher: Señal News
  - title: DNS Resolver Quad9 Rejects French Piracy Blocks, Weighs Exit as beIN Seeks Up to €580K a Day
    url: https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/
    publisher: TorrentFreak
    date: 2026-10-05
  - title: Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France
    url: https://torrentfreak.com/?p=277758
    publisher: TorrentFreak
    date: 2026-04-01
  - title: OpenDNS Suspends Service in France Due to Canal+ Piracy Blocking Order
    url: https://torrentfreak.com/?p=253822
    publisher: TorrentFreak
    date: 2024-06-29
  - title: France Approves Automated, Real-Time Blocking of Pirate Sports Streams
    url: https://torrentfreak.com/france-approves-automated-real-time-blocking-of-pirate-sports-streams/
    publisher: TorrentFreak
    date: 2026-07-28
  - title: VPNs and Cloudflare Escape beIN’s €10,000-a-Day Piracy Blocking Penalties
    url: https://torrentfreak.com/vpns-and-cloudflare-escape-beins-e10000-a-day-piracy-blocking-penalties/
    publisher: TorrentFreak
    date: 2026-10-16
  - title: UTV Software Communication Ltd. v. 1337X.TO, CS(COMM) 724/2017
    url: https://globalfreedomofexpression.columbia.edu/wp-content/uploads/2019/07/UTV-Software-Communications-Ltd.-v.-1337X.TO_.pdf
    publisher: Delhi High Court
    date: 2019-04-10
  - title: インターネット上の海賊版に対する総合的な対策メニュー及び工程表
    url: https://www.cas.go.jp/jp/seisakukaigi/titeki2/pdf/kaizokuban_taisaku_r808.pdf
    publisher: 内閣府ほか
    date: 2026-08-25
authors:
  - anoni-net
---

Quad9, a public DNS resolver run by a Swiss non-profit foundation, translates the domain names in web addresses into server addresses, and users can set it up in place of the default resolver from their network provider. On 22 October Quad9 announced that from 24 November it will no longer serve users located in France. According to its announcement, a French court ruling of 21 October, issued at the request of the sports broadcaster beIN, requires Quad9 to block resolution of a list of domains for users in France. Quad9's announcement says it will not block them and that it has chosen to leave France instead, and the announcement does not say how it will identify users located there.

Orders like this rest on Article L. 333-10 of the French Sports Code, under which broadcast rightsholders can ask a court to order anyone in a position to help to take blocking measures against pirate sites reached from France. On 13 May the Paris Judicial Court ordered defendants including Google and Quad9 to act within 3 days of notification and to keep the blocks in place until 14 November, the last match of the WTA tennis season. Under the provision the ruling applies, rightsholders then report newly found pirate sites, and the French audiovisual and digital communications regulator (Arcom) verifies them before notifying the defendants.

According to Quad9, the list of domains in the May ruling later grew to 58, and TorrentFreak quotes Quad9 as saying it has not blocked them. TorrentFreak also reports that beIN went back to court seeking fines of up to €580,000 a day, and according to TorrentFreak, beIN does not comment on ongoing proceedings. Quad9's announcement says the October ruling still requires the blocks and sets the fine at €1,000 a day (€24,000 in total up to 14 November). The announcement adds that an appeal is under way and that Quad9 could not bear the fines that around 20 similar lawsuits would add up to.

Quad9's announcement says its service is free, requires no registration, and holds no data mapping users to countries. Quad9 therefore cannot tell whom the ruling applies to, and adding the domains to its global blocklist would apply a French ruling to users worldwide.

In a separate case brought by the French pay-TV company Canal+, Quad9's December 2024 announcement says it then blocked the listed sites for users in all regions. In litigation in Germany, Quad9 once blocked by region based on IP address, and after the rightsholder connected through a VPN, the court found the measure insufficient and imposed a fine. Quad9 won on appeal in December 2023, when the Higher Regional Court of Dresden held that a resolver is not liable for infringement.

According to TorrentFreak, Quad9's explanation for the difference between the German case and this one is that the German block was an interim measure during litigation and each case is handled on its own. How the Canal+ case relates to this one is not explained in the report.

Other public resolvers have taken different paths. According to the announcement cited by TorrentFreak, Cisco's OpenDNS stopped serving France and Portugal on 28 June 2024. As of 23 October, Google Public DNS's help page lists France among five jurisdictions where it blocks under orders, answering queries for blocked domains with a refusal. Cloudflare's documentation says 1.1.1.1 does not block or filter content, and its blog says that in response to blocking orders it sometimes geo-blocks sites on its content delivery network (CDN) instead.

## Perspective {#perspective}

A DNS resolver translates the domain name in a web address into a server's IP address. A DNS-level block makes the resolver withhold the address for specific domains, which affects only queries sent through that resolver. According to an Internet Society report from March 2026, a resolver receives only the domain name, not the full path of the page.

On whether a block can be limited to France, the Paris Judicial Court's May ruling reasoned that the defendants had not shown that confining it to France would be costly or technically impossible, and left the technical method to them. Quad9's announcement says it has no data on users' countries, and in the German case an IP-based block was bypassed with a VPN. The Internet Society report says it is hard for operators to determine users' locations accurately within milliseconds, so blocks may affect users outside the jurisdiction. Google Public DNS's help page lists France among the jurisdictions where it blocks under orders.

On whether a block that can be bypassed still works, Quad9's announcement says people who want the content will switch to other, less trustworthy resolvers, and blocking does not remove content from the servers. The Paris Judicial Court's ruling says the number of people using alternative resolvers does not affect a rightsholder's right to seek a block. According to TorrentFreak, the Paris Court of Appeal held in March, in Canal+'s case against Google, Cloudflare and Cisco, that a filtering measure that can be bypassed is not therefore ineffective. The same ruling found that alternative resolvers let users reach pirate sites and get around blocks by network providers.

On who bears responsibility and cost, Quad9's announcement calls letting private companies decide what can be seen online a dangerous problem. The Internet Society report concludes that DNS blocking is the wrong tool for enforcing public policy, and says small and non-profit operators may not be able to afford country-by-country blocking. According to the Canal+ press release republished by Señal News, the appeal ruling fits Canal+'s strategy of making all kinds of technical intermediaries share responsibility for fighting piracy. The May ruling says blocking costs are shared among the parties under an agreement overseen by Arcom.

We, a community based in Taiwan, compared three places in Asia on who can order site blocking and whether public resolvers are covered. In Taiwan, a January 2025 procedure from the Ministry of Digital Affairs lets the Taiwan Network Information Center (TWNIC) and participating access providers stop resolving specific domains on a court judgment or ruling or a lawful administrative decision, for example under laws on fraud or child sexual exploitation. Suspension under the procedure does not include stopping users from reaching sites through public resolvers or VPNs, and its explanatory notes say this is technically impossible, citing OpenDNS, Cloudflare DNS and Quad9. As of 7 October Taiwan's Copyright Act had no provision authorising site blocking.

India is one of the five jurisdictions on Google Public DNS's list, where the page says it complies with enforceable court and government orders, though the page does not say which orders or laws apply there. In a 2019 piracy case the Delhi High Court ordered internet providers to block the sites and let rightsholders add mirror sites through the court registrar without a new lawsuit. The order is addressed to internet providers and does not mention public resolvers, although the judgment quotes a study noting that users can switch to an alternative DNS server not subject to blocking orders.

In Japan, the government published an anti-piracy roadmap in August 2026, whose attached measures menu (dated May 2024) says legislation on blocking remains under consideration. That note covers site blocking in general, not DNS specifically. As of 7 October, the official documents we checked contain no Japanese law authorising courts or agencies to order piracy sites blocked.

To check whether you are using Quad9, open its `on.quad9.net` check page. After 24 November, people in France whose device or router is fixed to Quad9 may be unable to resolve web addresses, and the announcement does not say how the service will stop. Those who switch to their network provider's default resolver or another service lose Quad9's blocking of malicious domains. As of 23 October, Quad9's node data shows nodes in Taipei, Tokyo, Singapore, Seoul and elsewhere online, and the announcement mentions no change for users outside France.

A few questions help compare the two sides' standards. First, who must show the cost and feasibility of confining a block to one country: the court found that the defendants had not shown it, while Quad9's announcement and the Internet Society report point to the limits of locating users. Second, does a block that can be bypassed count as effective: the court held that being bypassable does not make it ineffective, while Quad9's announcement says users will move to other services. Third, should technical intermediaries share responsibility for fighting piracy, and can small and non-profit resolvers afford country-by-country blocking?

Things to watch next are the outcome of Quad9's appeal and whether the exit on 24 November goes ahead as planned. According to TorrentFreak on 16 October, several DNS providers have appealed the March and May rulings to France's highest court. TorrentFreak reported in July that a newly passed French law has Arcom push new blocking targets in real time through an automated system, and according to that report it is due to take effect later in 2026. We have not checked whether the new law covers public resolvers.
