---
title: Conditions and disputes over alternative browser engines on iOS in the EU and Japan
description: The EU and Japan require Apple to allow browser engines other than WebKit on iOS, and Apple has set conditions on security and privacy grounds. Mozilla writes that these conditions have kept it from launching a Gecko-based Firefox, and according to its 20 November post no developer had launched a non-WebKit iOS browser by then.
date: 2026-11-26T00:00:00+08:00
slug: ios-browser-engines
categories:
  - mobile
sources:
  - title: Why there are still no non-WebKit browsers on iOS
    url: https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/
    publisher: Mozilla
    date: 2026-11-20
  - title: Using alternative browser engines in the European Union
    url: https://developer.apple.com/support/alternative-browser-engines/
    publisher: Apple
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: App Review Guidelines
    url: https://developer.apple.com/app-store/review/guidelines/
    publisher: Apple
    date: 2026-10-16
  - title: Apple announces changes to iOS in Japan
    url: https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/
    publisher: Apple
    date: 2025-12-17
  - title: Outline of the Act on Promotion of Competition for Specified Smartphone Software (Mobile Software Competition Act (MSCA))
    url: https://www.japaneselawtranslation.go.jp/en/outlines/view/154
    publisher: Japan Fair Trade Commission
  - title: The CMA's programme of work across mobile platforms
    url: https://www.gov.uk/guidance/the-cmas-programme-of-work-across-mobile-platforms
    publisher: Competition and Markets Authority
    date: 2026-02-10
  - title: "The Digital Markets Act Is Delivering Real Wins, But Not Yet for Browser Engines"
    url: https://open-web-advocacy.org/blog/the-digital-markets-act-is-delivering-real-wins-but-not-yet-for-browser-engines/
    publisher: Open Web Advocacy
    date: 2026-05-15
  - title: How Apple’s Key Tactic Could Prevent Japan’s Smartphone Act from Improving Browser Competition
    url: https://open-web-advocacy.org/blog/how_apples_key_tactic_could_prevent_japans_smartphone_act_from_improving_browser_competition/
    publisher: Open Web Advocacy
    date: 2026-01-06
authors:
  - anoni-net
---

Every browser on the iPhone and iPad, whether Safari, Chrome, Firefox or one marketed on privacy, runs on Apple's WebKit engine (the core component that parses and displays web pages). Laws in the EU and Japan require Apple to allow other engines, and Apple has set conditions in both places on security and privacy grounds. In a post on 20 November, Mozilla writes that these conditions have so far kept it from launching a Firefox built on its own engine, and that not one developer had launched a non-WebKit browser on iOS by the time of the post. Apple's App Review Guidelines require apps that browse the web to use WebKit, and the conditions for an exception are set out on two separate pages, one for the EU and one for Japan.

According to Mozilla's post, iPhones and iPads are the only major platforms with this restriction. On Apple's own macOS, people can use the version of Firefox built on Gecko, the browser engine Mozilla develops. Many of Firefox's features are built into Gecko, which is why Mozilla cannot easily bring the full Firefox to the iPhone.

According to a summary by the advocacy group Open Web Advocacy (OWA), the EU's Digital Markets Act (DMA) requires large platforms designated as gatekeepers to allow other browser engines, an obligation Apple has had to meet since March 2024. Japan's Act on Promotion of Competition for Specified Smartphone Software (Mobile Software Competition Act, MSCA) has a similar provision. In the outline of the act published by the Japan Fair Trade Commission (JFTC), providers that exceed a size threshold and are designated by the JFTC "must not prevent other application developers from using other browser engines, for example, by imposing conditions that only allow the use of designated providers' proprietary browser engines". Exceptions are allowed where there are justifiable reasons such as security and privacy.

Under Apple's developer documentation, a developer who wants to use another engine must first be authorised by Apple, and the app can only be distributed in the EU or in Japan (the Japan conditions were published in December 2025). On security, vulnerabilities that are already being exploited must be mitigated "in a timely manner", and the example given in the documentation is "30 days for the simplest classes of vulnerabilities being actively exploited". On privacy, the engine must block third-party cookies (cookies that can be used to track people across websites) by default.

According to Mozilla, using Gecko would mean it could not simply update the Firefox app people already have, and would instead have to build "a whole separate app, a second Firefox". Users would then have to download the new app, move their bookmarks, passwords and history across, and switch over by hand. Mozilla writes that "[a] significant proportion of people would understandably give up, including many who picked Firefox from the EU's choice screen". One of the conditions bars Mozilla from disclosing non-public information about the project, but it still gave this example of what it is up against.

Browser engines constantly handle untrusted and potentially malicious content and have visibility of sensitive user data, which, according to Apple's developer documentation, makes them "one of the most common attack vectors for bad actors". Apple therefore only authorises developers who meet specific criteria and commit to ongoing security and privacy requirements. As quoted by OWA, Apple's vice president for legal said at a 2025 DMA workshop that third parties such as Google and Mozilla are able to bring their own engines, adding, "for whatever reason, they have chosen not to do so".

In a May post, OWA wrote that no browser vendor had brought its own engine to iOS in the EU, and asked the European Commission to investigate whether Apple is complying with the DMA in practice. As of 22 November we had found no Commission decision on Apple's browser engine conditions, and no public response from Apple to Mozilla's post.

The UK's Competition and Markets Authority (CMA) designated Apple's mobile platform as having strategic market status in October 2025, with the designation covering mobile browsers and browser engines. Following the designation, the CMA can impose targeted measures on Apple. On the CMA's programme of work page as of 22 November, work on Apple "concerning browsers (removal of the WebKit restriction)" is among the things the CMA expects to progress next, with no timetable given.

## Perspective {#perspective}

Switching to another browser on iOS changes the interface, the default settings and the extra features, but the engine is WebKit every time. As this site's [14 November article on Tor options for the iPhone](https://anoni.net/news/en/2026/11/ios-full-tor-browser/) set out from the Tor Project's documentation, Tor Browser is built on Firefox's Gecko, and Onion Browser on the iPhone (an open-source browser that connects through the Tor onion routing network) cannot offer the same protection because of WebKit's limits. The [built-in ad blocker in Firefox for iOS](https://anoni.net/news/en/2026/10/firefox-ios-ad-blocker/), covered in October, is likewise built on WebKit's content blocking technology, while Firefox on desktop and Android can install extensions directly.

Our reading of the local-distribution condition is that even if browsers with other engines appear in the EU or Japan, iPhone users in Taiwan, Hong Kong and elsewhere would still get WebKit browsers from the App Store. The exceptions would be separate permission from Apple, or a local law that also requires other engines to be allowed. The plan for an iOS Tor Browser covered in the 14 November article would face the same condition if it were distributed through the App Store.

Japan is the only place in Asia covered by Apple's alternative engine programmes, from iOS 26.2 onwards. According to Mozilla, no developer had launched a non-WebKit browser there either, almost a year after Apple published its Japan conditions. The conditions on Apple's Japan page match the EU page item by item, except that they cover iOS only, not iPadOS, allow distribution elsewhere only where "expressly permitted by Apple", and limit embedded engines for in-app browsing to browser engine stewards (organisations primarily responsible for operating an engine). Everywhere else, the App Review Guidelines require WebKit and list exceptions only for the EU and Japan, so going by the text of the guidelines, the same rule applies in mainland China, Taiwan and Hong Kong, and as of 22 November no local law requiring Apple to allow other engines could be found in any of the three.

Apple's two public pages of conditions include security and privacy requirements and the local-distribution limit, but no wording about building a separate app. Mozilla, for its part, writes that a confidentiality condition prevents it from disclosing the details. On why no browser has launched, Mozilla and OWA point to Apple's conditions, while Apple's vice president for legal, at the 2025 workshop, pointed to the vendors' own choice.

Anyone who needs to browse through Tor on an iPhone can use Onion Browser, covered in the 14 November article, together with Orbot (an app that sends the phone's connections into the Tor network). Pages are handled by WebKit in this setup too, and according to the same article, very little can be adjusted against browser fingerprinting (identifying visitors from details of their device and browser). Tor Browser exists only for desktop and Android, so anyone who needs its full protection has to use one of those devices, and the same goes for anyone who wants Firefox extensions. Readers who only use Safari or another browser have nothing to change now.

In comparing how different places handle this, Apple's 30-day example offers a security test, whether vulnerabilities can still be dealt with in time once other engines are allowed, and the migration cost Mozilla describes offers a competition test, whether users drop away when they have to switch apps.
