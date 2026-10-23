---
title: Browser fingerprinting and how browsers defend against it
description: A browser fingerprint combines traits a website can read, such as window size, fonts and small differences in rendering, into an identifier that recognises the same browser again, and clearing cookies or using a VPN does not stop it. According to the UK Information Commissioner's Office, Google stopped prohibiting its advertising customers from using fingerprinting in February 2025. How much gets blocked depends on the browser, with Firefox, Safari, Brave and Tor Browser each taking their own approach. The only fingerprinting-related item on Chrome's official status page, as we checked it on 23 October, limits the data the browser attaches to every request automatically.
date: 2026-10-25T00:00:00+08:00
slug: browser-fingerprinting-cookies
categories:
  - tracking
sources:
  - title: Our response to Google's policy change on fingerprinting
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/12/our-response-to-google-s-policy-change-on-fingerprinting/
    publisher: Information Commissioner's Office
    date: 2024-12-19
  - title: Updating our platform policies to reflect innovations in the ads ecosystem
    url: https://support.google.com/marketingplatform/answer/15732590
    publisher: Google Marketing Platform Help
  - title: A new path for Privacy Sandbox on the web
    url: https://privacysandbox.google.com/blog/privacy-sandbox-update
    publisher: Google
    date: 2024-07-22
  - title: Privacy Sandbox feature status
    url: https://privacysandbox.google.com/overview/status
    publisher: Google
  - title: Building a more private web
    url: https://blog.google/products-and-platforms/products/chrome/building-a-more-private-web/
    publisher: Google
    date: 2019-08-22
  - title: Overview of the Platforms programs policies update (February 2025)
    url: https://support.google.com/platformspolicy/answer/15738904
    publisher: Google
  - title: Next steps for Privacy Sandbox and tracking protections in Chrome
    url: https://privacysandbox.google.com/blog/privacy-sandbox-next-steps
    publisher: Google
    date: 2025-04-22
  - title: Update on Plans for Privacy Sandbox Technologies
    url: https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies
    publisher: Google
    date: 2025-10-17
  - title: Mitigating Browser Fingerprinting in Web Specifications
    url: https://www.w3.org/TR/fingerprinting-guidance/
    publisher: W3C
    date: 2025-09-25
  - title: "Firefox expands fingerprint protections: advancing towards a more private web"
    url: https://blog.mozilla.org/en/firefox/fingerprinting-protections/
    publisher: Mozilla
    date: 2025-11-10
  - title: Private Browsing 2.0
    url: https://webkit.org/blog/15697/private-browsing-2-0/
    publisher: WebKit
    date: 2024-07-16
  - title: WebKit Features in Safari 26.0
    url: https://webkit.org/blog/17333/webkit-features-in-safari-26-0/
    publisher: WebKit
    date: 2025-09-15
  - title: Apple elevates the iPhone experience with iOS 26
    url: https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/
    publisher: Apple
    date: 2025-06-09
  - title: Change Advanced settings in Safari on Mac
    url: https://support.apple.com/guide/safari/advanced-ibrw1075/mac
    publisher: Apple Support
  - title: Fingerprinting Protections
    url: https://github.com/brave/brave-browser/wiki/Fingerprinting-Protections
    publisher: Brave
  - title: How do I use Shields while browsing?
    url: https://support.brave.app/hc/en-us/articles/360022806212-How-do-I-use-Shields-while-browsing
    publisher: Brave Help Center
  - title: Fingerprinting protections - Features - Tor Browser
    url: https://support.torproject.org/tor-browser/features/fingerprinting-protections/
    publisher: Tor Project
  - title: Cover Your Tracks
    url: https://coveryourtracks.eff.org/
    publisher: EFF
  - title: Cover Your Tracks
    url: https://coveryourtracks.eff.org/learn
    publisher: EFF
  - title: Fingerprints are the new cookies
    url: https://royfish.dev/fingerprints-are-the-new-cookies
    publisher: royfish.dev
  - title: 指纹识别保护 - 功能 - Tor 浏览器
    url: https://support.torproject.org/zh-CN/tor-browser/features/fingerprinting-protections/
    publisher: Tor Project
  - title: 自分に関する情報が第三者に送信される場合、 自身で確認できるようになります。
    url: https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/gaibusoushin_kiritsu.html
    publisher: Ministry of Internal Affairs and Communications
  - title: 맞춤형 광고에 쓰이는 “행태정보” 처리, 적법성과 투명성 높인다
    url: https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=9888
    publisher: Personal Information Protection Commission
    date: 2024-01-31
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: National People's Congress
    date: 2021-08-20
  - title: 个人信息保护政策法规问答（2026年1月）
    url: https://www.cac.gov.cn/2026-01/09/c_1769688003183197.htm
    publisher: Cyberspace Administration of China
    date: 2026-01-09
authors:
  - anoni-net
---

In a personal blog post titled "Fingerprints are the new cookies", the author surveys the ways websites recognise a browser beyond cookies. According to a September 2025 document from the W3C Privacy Working Group, browser fingerprinting is a website's ability to recognise a visitor, browser or device from its configuration or other observable traits, such as window size, fonts and small differences in rendering. According to the UK Information Commissioner's Office (ICO) on 19 December 2024, Google stopped prohibiting organisations that use its advertising products from employing fingerprinting from 16 February 2025. How much gets blocked depends on the browser, with Firefox, Safari, Brave and Tor Browser each taking their own approach.

According to the same W3C document, clearing cookies or using a VPN does not prevent further correlation, and a fingerprint usually cannot be cleared or reset. In the document's assessment, technical measures already widely deployed are unlikely to remove fingerprinting entirely against a determined tracker, though specifications can still reduce it.

According to Google's 2019 blog post, users cannot clear a fingerprint and so cannot control how their information is collected, and Google at the time considered using fingerprints to track users wrong. In its December 2024 announcement to advertisers, Google tied the policy update to privacy-enhancing technologies and new ad channels such as connected TV, and neither that announcement nor the February 2025 policy update page mentions fingerprinting. "No longer prohibited" is the ICO's account of Google's notice to advertisers, a phrase that appears on neither of Google's public pages, and the ICO called the change irresponsible.

According to the ICO, under data protection rules such as the UK's Privacy and Electronic Communications Regulations (PECR), companies must give users a fair choice before using fingerprinting and obtain consent where needed. These rules apply in the UK, and we, a community based in Taiwan, found no rule in Taiwan aimed specifically at device fingerprinting.

Google had planned to phase out third-party cookies in Chrome (small files that ad or analytics services embedded in web pages store in the browser to recognise users across sites), and on 22 July 2024 proposed letting users choose instead. On 22 April 2025 Google announced it would not roll out a separate prompt, leaving users to choose in Chrome's privacy and security settings. On 17 October 2025 Google announced it would retire most of Privacy Sandbox (a set of browser technologies Google proposed to replace third-party cookies), including IP Protection, which masks IP addresses. On the Privacy Sandbox status page as we checked it on 23 October (updated 14 August 2026), the only fingerprinting-related item limits the data the browser attaches to every request automatically, such as the browser version and operating system strings.

## Perspective {#perspective}

In a 2024 WebKit post on Safari's Private Browsing, defences against fingerprinting fall into two kinds. One makes many users share the same fingerprint, the other shows each website a different one. Tor Browser takes the first approach, and according to its support page, making every user exactly identical is practically impossible, so the goal is to reduce the number of distinguishable groups for each trait.

Brave uses both. According to Brave's documentation, it makes Brave browsers look as alike as possible while adding a small amount of random noise. The seed for that noise differs for each session and each site, which makes it hard for sites to link the same person, and Brave's help centre lists blocking fingerprinting as on by default in Shields.

According to Mozilla's November 2025 announcement, the fingerprinting protections added in Firefox 145 are turned on first in Private Browsing and in Enhanced Tracking Protection's Strict mode, and at the time work was under way to make them the default. According to WebKit's September 2025 post on Safari 26.0, Safari prevents known fingerprinting scripts from reliably reading information that can reveal device traits, such as screen dimensions and audio.

Safari also has an advanced fingerprinting protection that can apply to Private Browsing only or to all browsing. Apple's June 2025 iOS 26 press release describes this protection as extending to all browsing by default, while Apple's Safari help page gives no default, so we suggest checking the setting yourself. According to the 2024 WebKit post, on iPhone it is under "Settings > Apps > Safari > Advanced > Advanced Tracking and Fingerprinting Protection", where you choose "All Browsing". On a Mac it is in Safari's Advanced settings, where you turn on "Use advanced tracking and fingerprinting protection" and apply it to all browsing.

Readers using Firefox on desktop can get the protections added in version 145 by switching Enhanced Tracking Protection from Standard to Strict under Privacy & Security. We could not find the default on mobile.

People who need stronger protection and can accept slower connections can switch to Tor Browser, which the EFF page we checked on 23 October also lists as the most practical option. The Tor Project's page on fingerprinting protections is available in Traditional and Simplified Chinese. According to our docs site, Android has an official Tor Browser and iPhone does not.

To see how easily your own browser can be recognised, you can open the EFF's Cover Your Tracks, whose pages we found are all in English. According to the site, it collects only anonymous data and compares you with visitors who tested recently, and how each browser's defences differ is also covered on our docs site in [A browser fingerprint cannot be cleared the way a cookie can](https://anoni.net/docs/en/basics/browser-fingerprinting/){target="_blank"}.

Stronger protection makes websites more likely to break. According to Mozilla's announcement, more aggressive blocking will inevitably break legitimate site features, for example calendar and meeting tools that need the real time zone. According to the Tor support page, inconsistent traits can lead anti-bot systems to treat Tor users as bots, and the EFF page includes a caution that a protection can itself sometimes become part of the fingerprint.

None of the official pages and statutes we read in Japan, South Korea or mainland China mentions browser fingerprinting by name as of 23 October, but each addresses the data behind tracking differently. Japan amended its Telecommunications Business Act in June 2022, in force since 16 June 2023, so that services such as messaging, social media, search and news sites sending users' devices a program that transmits user data to outside parties must give notice of what is sent, publish it, obtain consent or offer an opt-out. According to the Ministry of Internal Affairs and Communications page, information truly necessary to provide the service, such as OS, screen and language settings and browser information, is exempt from the notice-or-publication requirement, as is an ID the service itself stored in a first-party cookie.

South Korea's Personal Information Protection Commission draws the line at identification in a policy plan published on 31 January 2024, a set of recommendations rather than a statute. Under the plan, ad companies may process online behavioural data without consent if they do not identify a specific person, but must keep the data from becoming identifying through accumulation, overlap or combination, and need consent when they do identify someone. According to the plan, revised guidelines were due by the end of 2024, and as of 18 October we could not find whether they were issued or are in force.

Mainland China's Personal Information Protection Law sets its rule at automated decision-making instead. Article 24 requires that information push and commercial marketing based on automated decision-making also offer an option not targeted at personal characteristics, or a convenient way to refuse. The Cyberspace Administration of China's January Q&A on personal information lists user identifiers, browsing records, device information such as the IMEI, and user profiles as personal information.

Our reading is that these settings reduce a website's ability to recognise the same person when the reader is not logged in, while Brave's approach is aimed specifically at linking across sites and sessions. A website where you are logged in to the same account still knows who is browsing.
