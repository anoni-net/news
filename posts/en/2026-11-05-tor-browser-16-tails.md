---
title: Tor Browser 16.0 and Tails 7.16
description: Tor Browser 16.0 is out for desktop and Android and is now based on Firefox ESR 153. The desktop version has redesigned Settings and a new generic window titles option that is off by default, and 32-bit x86 Linux is no longer supported from this release. Tails 7.16 updates its built-in Tor Browser to 16.0, and Tails 7.0 or later can upgrade automatically.
date: 2026-11-05T00:00:00+08:00
slug: tor-browser-16-tails
categories:
  - tracking
sources:
  - title: "New Release: Tor Browser 16.0"
    url: https://blog.torproject.org/new-release-tor-browser-160/
    publisher: Tor Project
    date: 2026-10-29
  - title: Tails 7.16
    url: https://tails.net/news/version_7.16/
    publisher: Tails
    date: 2026-10-30
  - title: Known issues
    url: https://tails.net/support/known_issues/
    publisher: Tails
  - title: OONI API, Tor tests, Hong Kong
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=HK&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
  - title: OONI API, Tor tests, Taiwan
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=TW&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
authors:
  - anoni-net
---

The Tor Project released Tor Browser 16.0 for desktop and Android on 29 October, the first stable release based on Firefox ESR 153 (Firefox's Extended Support Release). Tails (an operating system that boots from a USB stick and sends every connection through Tor) followed the next day with 7.16, which updates its built-in Tor Browser to 16.0. The update covers Windows, macOS, Linux and Android users, except for 32-bit x86 Linux computers, which are no longer supported from 16.0.

According to the Tor Project's announcement, the team carries out an annual review whenever it moves to a new ESR. This time it reviewed and handled more than 270 Bugzilla (Mozilla's bug tracker) issues covering a year of Firefox changes that could harm the privacy and security of Tor Browser users. The changelog has several entries that disable or hide features: WebGPU (a new interface that lets web pages run computations directly on the graphics card) is disabled pending review, and the AI settings panel and the translation settings page are hidden. The Android version also disables AI features and Google Lens, and these entries consist of titles only, with no reasons given.

Settings on desktop follow Firefox's June redesign, with the old General page split into new pages for appearance, downloads, tabs and browsing, accessibility, and language. Pages specific to Tor Browser, such as Connection and Security Level, have been rebuilt with Firefox's new components. The announcement says settings that could harm privacy or make the browser easier to fingerprint (to recognize the same device from browser settings and device characteristics) when turned on are either hidden or carry a warning. Existing preferences are kept, and the search bar at the top of Settings finds options that have moved.

Settings also gain a generic window titles option, under Privacy and security → Protections from third-party applications, which replaces every window title with "Tor Browser". As the announcement explains, browsers usually name a window after the page being viewed, and other programs on the computer, as well as the operating system itself, can read that title without special permissions. The option is off by default, because the announcement says there was not enough time in this release cycle to evaluate side effects. Those who may be affected are people using screen readers and people with highly customized systems (for example, less common desktop environments or application switchers).

The Linux version adds native support for 64-bit ARM processors, such as the Raspberry Pi and Apple Silicon Macs running Linux. Support for 32-bit x86 Linux ends along with Firefox's, and when the announcement was published this platform accounted for about 200 update checks a day, down from about 4,000 at its peak in 2019.

The built-in manual on desktop (type `about:manual` in the address bar, or open ☰ → Help → Tor Browser manual) now uses content from the new support site, and it can still be read offline, including when Tor will not connect. Google Play limits apps distributed as APKs to 100 MB, which has kept the manual from being bundled for offline reading on Android. Much of the Android interface now uses Material Design 3 (Google's design guidelines for Android), and the announcement says later releases will continue the work. The changelog also lists the removal of the password interface on Android, the disabling of all link-sharing features, and the disabling of bookmark import.

According to the Tails announcement, 7.16 updates Tor Browser to 16.0, bringing the new Settings with it. The Tor client is updated to 0.4.9.15, and OpenPGP support in Thunderbird has been fixed.

## Perspective {#perspective}

Tor Browser is built on Firefox ESR and moves to a new base version once a year, so each move takes in a year of Firefox changes at once. The 16.0 changelog shows several new features switched off first, with WebGPU, for example, marked as disabled pending review. Firefox's new online search suggestions also remain off. From this we infer that some features Firefox users already have will reach Tor Browser users later or not at all.

Generic window titles deal with other programs on the same computer. The Tor network protects the path a connection takes and does not cover other software installed on the computer. The option changes only the window title, and we infer that other programs reading what is on the screen fall outside what it handles.

Once every window is called "Tor Browser", we infer that people who rely on window names to switch between windows will find them harder to tell apart, which may be the situation for the screen reader users the announcement mentions. In the announcement, the Tor Project invites people who use screen readers or highly customized systems to try the option and report any problems.

The same option has already reached Firefox through the Tor Uplift Project (the effort to send Tor Browser's changes back to Firefox). According to the announcement, advanced Firefox users can get the same effect by setting `privacy.exposeContentTitleInWindow` (normal windows) and `privacy.exposeContentTitleInWindow.pbm` (private browsing windows) to false in `about:config`.

The same announcement says a new circuit display (the panel showing which relays a connection passes through) is coming to the Alpha test release and is not part of 16.0. The new version brings site information into the panel and can draw multi-path circuits, and it will be the first circuit display on Android. According to the announcement, multi-path circuits use extra relays to split traffic into two paths that converge on a single exit (the last relay before the connection leaves the Tor network for the destination site). As of the announcement, connections to regular websites were already randomly assigned to multi-path circuits depending on network availability, while onion services (sites reachable only through Tor) were not.

For readers in Taiwan and Hong Kong, OONI (Open Observatory of Network Interference) Tor tests from 18 September to 18 October, queried on 20 October, found 7 anomalies in 706 tests in Hong Kong and 314 anomalies in 4,797 tests in Taiwan, 311 of the Taiwan anomalies from a single ASN (autonomous system number, which identifies one network). An anomaly is not a confirmed block, and the test checks whether the servers Tor needs to operate can be reached. As of 20 October we had found no rules in either Taiwan or Hong Kong specifically on running onion services.

People using Tor Browser on desktop can find generic window titles under Privacy and security in Settings after updating to 16.0. According to the announcement, turning it on keeps other software from learning browsing history through window titles. From this we infer that people worried about software of unknown origin on their computer can consider turning it on, though it does not help when other programs log keystrokes or take screenshots. For people who need fuller protection against other software on the computer, the announcement recommends Tails.

For anyone moving to Tails on that recommendation, Tails' known issues page said as of 2 November that Macs with Apple chips (M1, M2 and so on) and many other Mac models cannot start Tails at all. Tails 7.0 or later can upgrade to 7.16 automatically, and if the automatic upgrade fails or Tails will not start afterwards, a manual upgrade is the fallback. Reinstalling instead erases the Persistent Storage on the USB stick (the space Tails uses to keep files and settings). According to the Tor Project's announcement, most people still on 32-bit x86 Linux can switch to the 64-bit version, unless their hardware or Linux version is too old.
