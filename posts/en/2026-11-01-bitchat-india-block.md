---
title: Dispute over the removal of the Bluetooth mesh messaging app Bitchat in India
description: Bitchat, an open-source messaging app that sends messages over a Bluetooth mesh network without the internet, was removed from the App Store in India on 3 October at the request of India's Ministry of Electronics and Information Technology. As of 31 October, neither the order nor its reasons had been published, and on 11 November the Kerala High Court will hear a public interest petition seeking to suspend the block. Readers outside India are not affected by this removal.
date: 2026-11-01T00:05:00+08:00
slug: bitchat-india-block
categories:
  - censorship
regions:
  - IN
sources:
  - title: "[…]'s Bitchat disappears from app stores in India after government order"
    url: https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/
    publisher: TechCrunch
    date: 2026-10-03
  - title: SFLC.in Condemns the Blocking of Bitchat in India
    url: https://sflc.in/sflc-in-condemns-the-blocking-of-bitchat-in-india/
    publisher: SFLC.in
    date: 2026-10-05
  - title: "Blocking BitChat is unconstitutional: MeitY must publish and withdraw its secret order"
    url: https://internetfreedom.in/blocking-bitchat-is-unconstitutional-meity-must-publish-and-withdraw-its-secret-order/
    publisher: Internet Freedom Foundation
    date: 2026-10-03
  - title: THE INFORMATION TECHNOLOGY ACT, 2000
    url: https://www.indiacode.nic.in/bitstream/123456789/13116/1/it_act_2000_updated.pdf
    publisher: India Code
  - title: Information Technology (Procedure and Safeguards for Blocking for Access of Information by Public) Rules, 2009
    url: https://www.meity.gov.in/static/uploads/2024/10/91f628cb778f94e76df356bc3fd3ac60.pdf
    publisher: Ministry of Electronics and Information Technology
    date: 2009-10-27
  - title: WP(PIL) No. 207 of 2026
    url: https://www.medianama.com/wp-content/uploads/2026/10/BitChatOrder.pdf
    publisher: High Court of Kerala (via MediaNama)
    date: 2026-10-14
  - title: "BitChat blocking challenge: Kerala HC gives Govt. 4 weeks to respond"
    url: https://www.medianama.com/2026/10/223-bitchat-blocking-challenge-kerala-hc/
    publisher: MediaNama
    date: 2026-10-15
  - title: Telegram FZ LLC & Anr. v. Union of India & Ors., W.P.(C) 8259/2026
    url: https://www.livelaw.in/pdf_upload/2026/06/19/telegram-681140.pdf
    publisher: High Court of Delhi (via LiveLaw)
    date: 2026-06-19
  - title: permissionlesstech/bitchat
    url: https://github.com/permissionlesstech/bitchat
    publisher: GitHub
  - title: "Fix security audit findings: 3 critical, 7 high"
    url: https://github.com/permissionlesstech/bitchat/pull/1345
    publisher: GitHub
    date: 2026-06-17
  - title: Identity Is A Bitchat Challenge (MITM Flaw)
    url: https://www.supernetworks.org/pages/blog/agentic-insecurity-vibes-on-bitchat
    publisher: Supernetworks
    date: 2025-07-07
  - title: "Building secure messaging is hard: A nuanced take on the Bitchat security debate"
    url: https://blog.trailofbits.com/2025/07/18/building-secure-messaging-is-hard-a-nuanced-take-on-the-bitchat-security-debate/
    publisher: Trail of Bits
    date: 2025-07-18
  - title: Bitchat, a P2P chat app created by the founder of Twitter, has been removed from the Chinese App Store.
    url: https://gigazine.net/gsc_news/en/20260406-bitchat-pulled-china-app-store/
    publisher: GIGAZINE
    date: 2026-04-06
  - title: 具有舆论属性或社会动员能力的互联网信息服务安全评估规定
    url: https://www.cac.gov.cn/2018-11/15/c_1123716072.htm
    publisher: 中国网信网
    date: 2018-11-15
  - title: 詐欺犯罪危害防制條例
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080226
    publisher: 全國法規資料庫
  - title: 台灣將封鎖小紅書一年！刑事局揭違規內幕 300萬用戶影響一次看
    url: https://www.nownews.com/news/6761411
    publisher: NOWnews
    date: 2025-12-04
  - title: Implementation Rules for Article 43 of the Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region
    url: https://www.gld.gov.hk/egazette/pdf/20202449e/cs220202449139.pdf
    publisher: Hong Kong Government Gazette
authors:
  - anoni-net
---

Bitchat, an open-source messaging app that sends messages over a Bluetooth mesh network (phones relay messages to one another without going through the internet), was removed from the App Store in India on 3 October. According to the Apple notice the developer made public, the removal followed a demand from India's Ministry of Electronics and Information Technology (MeitY) under Section 69A of the Information Technology Act, 2000, and no illegal content was identified in it. When TechCrunch checked that day, Bitchat could not be found on Google Play in India either, and Apple, Google and MeitY did not respond to requests for comment. The removal applies only in India, and as of 31 October the App Store lookup interface still returned Bitchat for Taiwan and Hong Kong, though not for mainland China, where it was removed separately in February (see Perspective).

Under Section 69A, the central government may, in the interest of sovereignty, defence, state security, public order and similar grounds, direct intermediaries by an order with reasons recorded in writing to block public access to information. Under the 2009 Information Technology (Procedure and Safeguards for Blocking for Access of Information by Public) Rules, the designated officer is to make all reasonable efforts to notify the person or intermediary hosting the information to appear before a committee chaired by the designated officer, with representatives of the law, home affairs and other ministries. In an emergency, the ministry's secretary may issue directions without a hearing, and the designated officer must bring the request before the committee within 48 hours. Under the same rules, all blocking requests and actions taken must be kept confidential.

As of 31 October, we, a community based in Taiwan, had found no public explanation from the government for the October removal, and two Indian digital rights groups, SFLC.in and the Internet Freedom Foundation (IFF), both wrote in statements in early October that the order and its reasons could not be found. Bitchat's developer has only posted Apple's notice on X, and we found no formal response or legal action. In its notice, Apple asks the developer to contact MeitY directly.

The government reasons we did find come from a different notice in July. On 23 July, the Indian Cyber Crime Coordination Centre of the Ministry of Home Affairs, relying on a different provision, asked GitHub to remove Bitchat's code repositories, on the grounds that apps of this kind need no registration or phone number verification and that their architecture impedes lawful interception and law enforcement investigations. According to the same notice, such tools could be used to coordinate unlawful activity during internet shutdowns or public order incidents. According to IFF and the Indian tech policy outlet MediaNama, the July notices were reportedly withdrawn or not enforced after they became public.

## Perspective {#perspective}

Bitchat lets nearby phones relay messages directly, up to 7 hops, with no account or phone number. When a connection is available, messages can also travel through relays on Nostr (an open, decentralised messaging protocol). According to the developer's documentation, private messages are encrypted with the Noise protocol (a framework for setting up encrypted sessions). Live sessions have forward secrecy (a key leaked later cannot decrypt earlier messages), while messages stored for offline delivery do not.

According to the developer's privacy assessment, public channel content is visible to everyone taking part. Device identifiers do not rotate, so people nearby can recognise the same device across time and places, and can tell that someone is using the app.

Bitchat is maintained by volunteers, and the iOS version is released into the public domain (anyone may freely use and modify the code). Soon after its launch in July 2025, a researcher pointed out that its identity verification was open to a man-in-the-middle attack (a third party impersonating one side of a conversation), and the security firm Trail of Bits wrote in a commentary that it should not be relied on for sensitive messages at the time. The developer then moved to Noise encryption, and according to a fix merged in June 2026, one audit found ten critical or high-risk issues. The auditor is not named in the fix, and as of 31 October we had found no complete audit report from an independent organisation.

According to SFLC.in's statement, the block appears to have no end date, and using Section 69A to block an entire messaging app is disproportionate. IFF's position is that the block is unconstitutional: Section 69A permits blocking unlawful information, and a messaging tool that works during internet shutdowns falls outside that. In the Telegram case in June, the Delhi High Court held that Section 69A can be used to block an entire app, and according to the committee opinion quoted in that judgment, that block was temporary and limited in duration.

SFLC.in notes in its statement that the removal came right after an internet shutdown on 2 October, and infers that the app may have been targeted because it allows communication during shutdowns. IFF's view is that the government objects to what the app can do, not to the content it carries. The government's reasoning in the July notice is that the architecture of such apps impedes lawful interception, and that because they keep working during shutdowns and network restrictions, they could be used to get around those restrictions.

Blocking requests are to be kept confidential under the 2009 rules, yet Apple passed the notice on to the developer. IFF is asking the government to publish the order and its reasons, and Apple to disclose the demand in its transparency report, and says it will seek a copy of the order under the Right to Information Act (the law that lets people request information from public authorities). On 14 October, the Kerala High Court heard a public interest litigation (a case brought in the public interest) and, without yet deciding whether it is maintainable, directed all respondents to file affidavits first, with the next hearing on 11 November. The respondents include government ministries and the Indian subsidiaries of Apple and Google.

According to IFF's statement, the removal does not delete the app from phones where it is already installed, but new users cannot download it and existing users stop receiving security updates. Anyone considering Bitchat can start with the white paper and privacy assessment the developer publishes on GitHub. According to these documents, public channel content is visible to everyone taking part, people nearby can detect a device running the app, and security fixes ship only in the latest version.

The iOS version requires iOS 16 or later and the Android version requires Android 8.0 or later, and both offer Traditional and Simplified Chinese interfaces. For people who care about being recognised by those nearby, this risk remains after they start using the app, and the developer lists rotating identifiers as future work.

In February 2026, the Cyberspace Administration of China (CAC) also asked Apple to remove Bitchat from the App Store in mainland China. According to the notice the developer made public in April, summarised by the Japanese tech outlet GIGAZINE, Apple named the provision relied on: Article 3 of the Provisions on the Security Assessment of Internet-based Information Services with Attribute of Public Opinions or Capable of Social Mobilization. As of 31 October, the App Store lookup interface returned no result for Bitchat in mainland China.

Under Article 3, providers of services with public opinion attributes or social mobilisation capability must carry out their own security assessments when, for example, they launch such a service, add such features or see users grow significantly, and removal is not mentioned in the article itself. Under the same provisions, a provider that has not done an assessment is first notified to do one, and one that refuses faces a public risk warning and inspection, and any violations found are to be dealt with according to law. The provisions themselves do not mention an appeal or a court, and we did not check general administrative review or judicial review. We found no published order and no end date.

According to media reports, Taiwan's Ministry of the Interior publicly announced action against Xiaohongshu (RedNote) in December 2025, requiring network access providers under the Fraud Crime Hazard Prevention Act to stop resolving its domains (so that addresses no longer lead to its servers) and restrict access, for a provisional period of one year. Unlike India's case, where neither the order nor its reasons are public, the government announced this action and cited the law. It was directed at network access providers, and app stores are not mentioned in the reports. We checked only that act and the Copyright Act, which often comes up in discussions of website blocking and in its current form contains no provision for ordering blocks, and found no provision empowering the government to order an app store to remove a particular app.

In Hong Kong, we also found no provision that specifically empowers the government to order an app store to remove a particular app. Under Schedule 4 of the Implementation Rules for Article 43 of the Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region (as published in 2020; we have not checked later amendments), a designated officer authorised by the Commissioner of Police with the approval of the Secretary for Security may require a platform service provider to take a disabling action on an electronic message likely to constitute an offence endangering national security, without first going to a court. Schedule 4 is about electronic messages on electronic platforms, app stores are not mentioned in it, and we have not checked whether its "platform service provider" includes them.

Under Schedule 4, requirements must be in writing. A service provider charged with failing to comply has a defence if compliance could not reasonably be expected because the necessary technology was not reasonably available, or because of a risk of substantial loss to, or substantial prejudice to the rights of, a third party. Schedule 4 itself has no provision on giving reasons or a route of appeal, and we did not check general judicial review.

For both the Indian and the mainland Chinese removals, we found no published order and no end date, and Apple named only the legal basis in its notices. India's rules require the designated officer to make all reasonable efforts to notify the host or intermediary to appear before a committee, though in an emergency directions can be issued without a hearing, and a public interest petition against this removal has been filed, with the court yet to decide whether it is maintainable. In mainland China, Article 12 of the assessment provisions does provide for prior notice, but the notice asks the provider to carry out an assessment, rather than giving the developer a chance to be heard before removal. Taiwan's action against Xiaohongshu was announced publicly with the law and a one-year term, but it targeted network access rather than an app store.

When comparing approaches, it helps to ask whether a removal order is published, whether it gives reasons and an end date, and whether developers and users have a chance to be heard before removal or to seek a remedy afterwards. The intended effect of the policy belongs in the comparison too. Removal does not delete installed copies of the app, and we could find no public assessment of whether the block achieves the law enforcement aims the government has stated.
