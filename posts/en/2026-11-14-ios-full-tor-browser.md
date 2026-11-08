---
title: Tor options on the iPhone and the plan for a full Tor Browser on iOS
description: As of 8 November there is no Tor Browser for the iPhone, and the Tor Project recommends Onion Browser instead. Guardian Project has published a one-year roadmap that puts the first Alpha in the quarter labelled April 2027, and nothing can be installed until that Alpha ships.
date: 2026-11-14T00:00:00+08:00
slug: ios-full-tor-browser
categories:
  - mobile
sources:
  - title: "Brewing Onion Cider: Bringing a full Tor Browser to iOS"
    url: https://guardianproject.info/2026/11/02/brewing-onion-cider-bringing-a-full-tor-browser-to-ios/
    publisher: Guardian Project
    date: 2026-11-02
  - title: How to install Tor Browser
    url: https://support.torproject.org/tormobile/tormobile-3/
    publisher: Tor Project
  - title: FAQs
    url: https://onionbrowser.com/faqs
    publisher: Onion Browser
  - title: Using alternative browser engines in the European Union
    url: https://developer.apple.com/support/alternative-browser-engines/
    publisher: Apple
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: Onion Browser
    url: https://apps.apple.com/us/app/onion-browser/id519296448
    publisher: Apple
  - title: Orbot
    url: https://apps.apple.com/us/app/orbot/id1609461599
    publisher: Apple
  - title: Apple iTunes lookup, Onion Browser, China storefront
    url: https://itunes.apple.com/lookup?id=519296448&country=cn
    publisher: Apple
  - title: Apple iTunes lookup, Orbot, China storefront
    url: https://itunes.apple.com/lookup?id=1609461599&country=cn
    publisher: Apple
authors:
  - anoni-net
---

As of 8 November there is no Tor Browser (a browser that connects through the Tor onion routing network) for the iPhone. The Tor Project's installation page recommends Onion Browser instead and warns that its privacy protections do not match Tor Browser's. On 2 November Guardian Project published a one-year roadmap for bringing the full Tor Browser to iOS, with the first Alpha scheduled for the quarter the roadmap labels April 2027. The project has not yet chosen a distribution route and nothing can be installed until the Alpha ships, so iPhone users have the same options as before.

According to the Onion Browser FAQ, Tor hides the websites you visit from anyone watching your connection and keeps those websites from learning your physical location. On an iPhone, the open-source Onion Browser is one way to browse through Tor. It connects either alongside a separate app, Orbot, or through a built-in Tor that the FAQ marks as iOS 17 only. App Store data as of 8 November shows Onion Browser and Orbot as free with a minimum of iOS 15, last updated on 20 October and 15 October respectively.

In the FAQ's comparison, Orbot is safer and the built-in Tor is more stable. With the built-in Tor, your real IP address leaks to the sites you visit through WebRTC (the browser technology for sending audio, video and data directly), and audio and video streams cannot go through Tor. The FAQ attributes this to WebKit, the browser engine (the core component that parses and displays web pages) that Apple supplies and requires. Orbot uses Apple's Network Extensions, which Apple limits to 50 MB of memory, and the Tor client is killed and restarted when it nears that limit.

According to the FAQ, Onion Browser clears its data automatically when it leaves the foreground, keeps no cache or cookies by default, and can detect a site's .onion address and switch to it. On browser fingerprinting (identifying visitors from details of their device and browser), the FAQ's advice is that iOS's built-in WebKit has very few settings to change, so the best approach is to look like every other iOS user.

Anyone who only wants all of an iPhone's traffic to go through Tor can use Orbot with Safari. According to the FAQ, Orbot sends all device traffic into Tor, so the benefits of Tor apply with Safari as well. The FAQ does not cover what happens to Safari's connections when Orbot is killed.

The first protection on the FAQ's list of what Onion Browser adds over Safari is that no request goes out until Tor is running and handling it, followed by the automatic clearing and the .onion switching. We infer from what the Tor Project and the FAQ write about WebKit that Safari is bound by the same WebKit limits as Onion Browser and falls just as short of Tor Browser's anti-tracking capabilities.

Guardian Project describes itself in the announcement as having more than ten years of experience developing and distributing Onion Browser and Orbot for iOS. The new project aims to bring iOS a Tor Browser built on Firefox's Gecko engine with the Tor Project's patches, while continuing to maintain Onion Browser and Orbot. According to the announcement, Onion Browser was deliberately given a different name because it is not the full Tor Browser. An iOS app using the Tor Browser name still needs the Tor Project's approval.

The roadmap runs by quarter. Q2, labelled January 2027, is for showing a prototype running Gecko on iOS and choosing a main route. Q3, labelled April 2027, is for shipping the first Alpha through TestFlight (Apple's channel for distributing test builds) and sideloading (installing apps without the App Store). Only in Q4, labelled July 2027, does the project decide whether the next step is a Beta or a full release.

Guardian Project acknowledges in the announcement that the best path is still uncertain, and the roadmap has two. The Apple route rests on the European Union's Digital Markets Act (DMA), which requires Apple to allow third-party browser engines on iOS, and on Japan's alternative browser engine programme. Gecko would run through BrowserEngineKit (the development kit Apple provides for alternative engines) and ship through the official store. The open route uses sideloading channels such as AltStore, a way, in the announcement's words, to "break free from App Store censorship and limitations".

## Perspective {#perspective}

According to the Tor Project's support page, Apple requires browsers on iOS to use WebKit, which is why Onion Browser cannot have the same privacy protections as Tor Browser (the EU and Japan have separate programmes, covered in the next paragraph). The FAQ explains that Tor Browser on desktop and Android is built on Firefox's Gecko, which offers more control and more reliability when implementing proxying and anti-tracking. Our reading is that moving to Gecko addresses the limits at the engine layer, since Onion Browser can already connect through Tor today.

Apple's developer documents, as of 8 November, require iOS 17.4 or iPadOS 18 or later for the EU programme and iOS 26.2 or later for Japan's. An app must first be authorised by Apple and can only be distributed locally (the Japan document allows exceptions that Apple expressly permits). We infer from these conditions that, unless Apple grants separate permission, iPhone users outside the EU and Japan could not get an Apple-route Tor Browser from the official store. The announcement also allows for being limited to Europe and Japan, and Guardian Project plans to push Apple to open third-party browser engines worldwide.

Guardian Project uses the phrase "malicious compliance" for how Apple has complied with the DMA, and the roadmap includes a risk analysis of Apple as a platform and distributor. Under Apple's documents, only developers who meet specific criteria and commit to ongoing privacy and security requirements are authorised to use alternative engines. According to the announcement, the official store reaches ordinary users in Europe and Japan who only get apps through Apple's official channels. Whether sideloading would help users who already face App Store censorship more is left as a question in the announcement, with no conclusion.

The Alpha's timing comes from the roadmap, and the announcement has no information on where it could be installed. On shipping Tor Browser for iOS through the EU and Japan app stores, the wording in the announcement is "when and if it is ready to go that way".

Japan is the only place in Asia that Apple's two programmes cover, and there only on iOS 26.2 or later. We infer that, unless Apple grants separate permission, an Apple-route Tor Browser would not reach the App Store outside the EU and Japan.

Apple's iTunes lookup API on 8 November returned no listing for Onion Browser or Orbot in the mainland China storefront and one listing each in the US storefront. This is an API result, not an Apple announcement, and we neither opened the storefronts with local accounts nor could find out whether the two apps were removed from the mainland China store or never listed there.

For anyone who needs to hide their IP address from the sites they visit, the FAQ's comparison favours Onion Browser with Orbot (both are free where the App Store lists them and need iOS 15 or later). If Orbot keeps restarting, the built-in Tor is more stable, at the cost of the IP leak and of audio and video staying outside Tor. All of these options still use WebKit. We infer from the Tor Project's support page that anyone who needs Tor Browser's full protection has to move to a computer or Android for now.

Readers who do not need to hide their IP address from the sites they visit have nothing to set up now, and two points are worth coming back to. The quarter labelled January 2027 is when the main route gets chosen, and we infer that the choice will affect whether readers outside the EU and Japan can get the browser. The quarter labelled April 2027 will show whether the Alpha ships on schedule and in which regions. Guardian Project plans to keep maintaining Onion Browser and Orbot, and Q3 of the roadmap (labelled April 2027) also includes work on helping users decide between Onion Browser and Tor Browser for iOS.
