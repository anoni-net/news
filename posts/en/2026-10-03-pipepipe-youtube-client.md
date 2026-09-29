---
title: PipePipe 5.4.0, an open-source YouTube client
description: PipePipe, an Android fork of NewPipe, plays YouTube, NicoNico and BiliBili without an account or Google Play. Version 5.4.0 improves TV controls and fixes 12 bugs.
date: 2026-10-03T07:05:00+08:00
slug: pipepipe-youtube-client
sources:
  - title: PipePipe v5.4.0
    url: https://github.com/InfinityLoop1308/PipePipe/releases/tag/v5.4.0
    publisher: PipePipe
    date: 2026-09-24
  - title: PipePipe
    url: https://pipepipe.dev
    publisher: PipePipe
  - title: InfinityLoop1308/PipePipe
    url: https://github.com/InfinityLoop1308/PipePipe
    publisher: GitHub
  - title: PipePipe
    url: https://f-droid.org/packages/InfinityLoop1309.NewPipeEnhanced/
    publisher: F-Droid
  - title: PipePipe
    url: https://apt.izzysoft.de/fdroid/index/apk/InfinityLoop1309.NewPipeEnhanced
    publisher: IzzyOnDroid
  - title: PipePipe SABR policies
    url: https://github.com/InfinityLoop1308/PipePipeSabrPolicies
    publisher: GitHub
  - title: YouTube playback, network, and sign-in
    url: https://priveetee.github.io/Docs-PipePipe/issues/youtube-playback.html
    publisher: PipePipe Wiki
  - title: TRANSLATION.md
    url: https://github.com/InfinityLoop1308/PipePipe/blob/main/TRANSLATION.md
    publisher: GitHub
  - title: "[Important] YouTube playback will fail if your DNS blocks googleapis.com or google.com"
    url: https://github.com/InfinityLoop1308/PipePipe/issues/2757
    publisher: GitHub
    date: 2026-07-24
  - title: SABR
    url: https://priveetee.github.io/Docs-PipePipe/developer-guide/introduction.html
    publisher: PipePipe Wiki
  - title: Is http://youtube.com blocked in mainland China?
    url: https://en.greatfire.org/youtube.com
    publisher: GreatFire
    date: 2026-09-21
  - title: Is http://google.com blocked in mainland China?
    url: https://en.greatfire.org/google.com
    publisher: GreatFire
    date: 2026-09-27
  - title: Is http://googleapis.com blocked in mainland China?
    url: https://en.greatfire.org/googleapis.com
    publisher: GreatFire
    date: 2026-08-16
  - title: "OONI Explorer: www.youtube.com, Hong Kong"
    url: https://explorer.ooni.org/chart/mat?test_name=web_connectivity&domain=www.youtube.com&probe_cc=HK&since=2026-08-29&until=2026-09-28&axis_x=measurement_start_day&time_grain=day
    publisher: OONI
  - title: "OONI Explorer: www.youtube.com, Taiwan"
    url: https://explorer.ooni.org/chart/mat?test_name=web_connectivity&domain=www.youtube.com&probe_cc=TW&since=2026-08-29&until=2026-09-28&axis_x=measurement_start_day&time_grain=day
    publisher: OONI
authors:
  - anoni-net
---

PipePipe, a GPL-3.0 open-source Android client for YouTube, the Japanese video platform NicoNico and China's BiliBili, released version 5.4.0 on 24 September (UTC) and installs without Google Play. The release improves TV controls, adds quality selection for live streams and fixes 12 bugs, including subtitles vanishing in fullscreen.

The developer forked NewPipe, an earlier open-source YouTube client, in early 2022 to create PipePipe, and the two projects have not synced changes since. The website lists no account, no ads, no trackers and no data collection. The app integrates SponsorBlock, a crowd-sourced service for skipping sponsored segments, along with keyword and channel filters, Shorts blocking, background play and whole-playlist downloads.

It is available from F-Droid, a repository of open-source Android apps, and IzzyOnDroid, a third-party repository for F-Droid clients. Both flag the NonFreeNet anti-feature because the app depends on non-free network services. As of 29 September, IzzyOnDroid carries 5.4.0, while F-Droid still offers 5.3.1, added on 12 September. APKs are also on the GitHub releases page, where the notes say `arm64-v8a` suits most devices.

## Perspective {#perspective}

With a third-party client you need no Google account, but requests still go straight to YouTube. When YouTube restricts an anonymous request, the app shows "Sign in to confirm you're not a bot". The community-maintained PipePipe Wiki's fix is to retry once, then try another network or VPN exit.

PipePipe also supports signing in, and its README states that the YouTube login cookie is used only to retrieve playback streams. Those requests then carry the cookie and can be tied to your account. According to the Wiki, login is best kept for IP blocks, age-restricted videos and channel-member content, at the cost of audio-only downloads and rewinding live streams in progress.

The developer's pinned GitHub issue `#2757` lists the domains PipePipe needs: `googleapis.com`, `google.com` and their subdomains. A DNS ad filter that blocks them can make YouTube playback fail, and the Wiki's fix is to allowlist them rather than switch filtering off.

GreatFire, which monitors censorship in mainland China, found `youtube.com` unreachable in all of its last three conclusive tests, most recently on 21 September, and `google.com` blocked in 87% of its last 23, most recently on 27 September. Its last three tests of `googleapis.com`, the latest on 16 August, all showed interference. PipePipe is therefore unlikely to play YouTube on a mainland network.

OONI (Open Observatory of Network Interference) collected 909 measurements of `www.youtube.com` from Hong Kong between 29 August and 27 September, and 4,966 from Taiwan, 574 of which failed to complete. Hong Kong had 3 anomalies, results that differ from a control measurement, and Taiwan had 1. Neither had a confirmed block.

The Wiki's developer guide describes SABR (Server Adaptive BitRate), which YouTube increasingly uses, as a session where the client reports playback state and receives media in small pieces. PipePipe downloads a playback policy from a public GitHub repository and runs it only after checking its Ed25519 signature, which shows the developer signed it unaltered, plus its validity window and revision number. It falls back to the built-in version on failure. By design, the developer can adjust playback without a new release, and the policy source is public, but the app executes code fetched from the network.

For bug reports, the Wiki's guidance is to keep cookies, tokens, account emails, screen recordings of a login and IP addresses out of public issues. Your sign-in state and the error you saw are enough for a first report.

To try it you need an Android phone running 6.0 or later, per F-Droid's listing, and the quickest route is the `arm64-v8a` APK from GitHub. Installing through an F-Droid client gives you update notifications. The official F-Droid repository lacks 5.4.0 so far; the IzzyOnDroid repository, added by hand in the official client, has it. According to the project's translation guide, the interface's Simplified and Traditional Chinese are AI-assisted; the Wiki and issue tracker are mostly in English.
