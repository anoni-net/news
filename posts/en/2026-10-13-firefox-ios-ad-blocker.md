---
title: Firefox for iOS's built-in ad blocker and system-level blocking on Android
description: Firefox on iPhone and iPad now has a built-in ad blocker, first listed in the 156 release notes in mid-September. It is off by default. On Android, the system-level options surveyed in a personal blog post mostly mean trusting whoever runs the service or app.
date: 2026-10-13T00:05:00+08:00
slug: firefox-ios-ad-blocker
categories:
  - mobile
sources:
  - title: "Introducing Ad Blocker for Firefox on iOS: More control, fewer distractions"
    url: https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/
    publisher: Mozilla
    date: 2026-09-01
  - title: 156.0 Firefox for iOS Release
    url: https://www.firefox.com/en-US/firefox/ios/156.0/releasenotes/
    publisher: Mozilla
    date: 2026-09-15
  - title: System-level ad-blocking in Android in 2026
    url: https://kevinboone.me/adblock.html
    publisher: Kevin Boone
    date: 2026-10-01
  - title: 在 Android 手機上管理進階網路設定
    url: https://support.google.com/android/answer/9654714?hl=zh-Hant
    publisher: Google
  - title: Mozilla adds ad blocking to Firefox for iOS
    url: https://www.theregister.com/software/2026/08/17/mozilla-adds-ad-blocking-to-firefox-for-ios/5288585
    publisher: The Register
    date: 2026-08-17
  - title: Firefox 快速隱私瀏覽器
    url: https://apps.apple.com/tw/app/firefox-private-safe-browser/id989804926
    publisher: App Store
  - title: App Review Guidelines
    url: https://developer.apple.com/app-store/review/guidelines/
    publisher: Apple
    date: 2026-06-08
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: Android developer verification
    url: https://developer.android.com/developer-verification
    publisher: Android Developers
authors:
  - anoni-net
---

Mozilla announced on 1 September that Firefox on iPhone and iPad now includes a built-in ad blocker. It is off by default and can be turned on under Settings > Browsing. The feature first appeared in the release notes for version 156, published on 15 September, and Mozilla was quoted as saying it is being rolled out gradually. Desktop and Android versions of Firefox could already install ad-blocking extensions, so the change only affects iOS.

The announcement says the blocker uses Apple's WebKit Content Blocker technology and the EasyList filter list to stop many third-party ads and ad-related trackers before they load. Mozilla says extensions work differently on iOS, so it built the feature into the browser, and that it made the feature optional because advertising funds much of the web. Ads served directly by the site, ads in search results and sponsored shortcuts on Firefox's new tab page are not affected.

For blocking ads across a whole Android phone, a personal blog post published on 1 October surveys four approaches for 2026: an ad-blocking DNS service (DNS turns domain names into IP addresses), a VPN service with ad blocking, a local VPN app that does not need root, and editing the system hosts file with root access. As far as the author knows, all of them work by overriding DNS, mapping known advertisers' hostnames to bogus IP addresses.

## Perspective {#perspective}

Both approaches block known ad addresses before a connection is made, but at different scopes. Firefox's blocker on iOS applies only to pages opened in Firefox, using WebKit's content blocking, and Apple's App Review Guidelines require apps that browse the web to use WebKit, with separate exemption procedures for the EU and Japan. Android's system-level methods cover every app, although, as the author notes, they cannot stop ads built into an app or apps that connect by IP address (which the author says is still rare).

In our reading, the first three methods mean trusting whoever provides the service, since every domain your apps look up passes through it. The author warns that a rogue DNS or VPN operator could even redirect online banking to its own proxy, and suggests that people who care about privacy pick a no-logs provider that supports encrypted DNS. Local VPN apps route all traffic through a single app, so the author advises using only open-source ones. The root method avoids an outside operator, at the cost of checking what gets written to the hosts file.

Apple's guidelines name only the EU and Japan as places where browsers may use engines other than WebKit, with Japan included from iOS 26.2, though Firefox's ad blocker is built on WebKit's content blocking either way. Firefox's source code includes Japanese, Korean and Traditional Chinese strings for the blocker, so the setting is localised in all three markets alike. On Android, Google's developer verification began on 30 September for apps installed from participating stores, with the page listing only Brazil, Indonesia, Singapore and Thailand so far and a global rollout planned for 2027. That matters for the local VPN apps the author says are hard to get through Google Play, though the page names no such apps.

iPhone and iPad users who update Firefox to the latest version, which needs iOS 15.0 or later, should find the switch under Settings > Browsing. The interface text suggests turning it off if a site breaks, and site-served ads, search ads and new tab sponsored content will still appear. On Android, the author suggests that if web ads are the main problem, the simplest approach might be a browser with ad blocking. To block ads in apps too, enter an ad-blocking DNS provider's hostname under Settings > Network & internet > Private DNS (menus vary by manufacturer; prices vary and most offer a free trial), after checking its logging policy, since every app's lookups will go to that provider.
