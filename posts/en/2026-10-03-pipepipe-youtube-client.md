---
title: PipePipe 5.4.0, an open-source YouTube client
description: PipePipe, an Android fork of NewPipe, plays YouTube, NicoNico and BiliBili without an account. Version 5.4.0, released on 24 September, improves TV controls and fixes a dozen playback bugs.
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
  - title: Is http://youtube.com blocked in mainland China?
    url: https://en.greatfire.org/youtube.com
    publisher: GreatFire
    date: 2026-09-21
authors:
  - anoni-net
---

PipePipe released version 5.4.0 on 24 September. It is a GPL-3.0 Android client for YouTube, NicoNico and BiliBili, forked from NewPipe in early 2022 and developed independently since, without syncing changes in either direction. Its website promises no account, no ads, no trackers and no data collection, alongside SponsorBlock, keyword and channel filters, Shorts blocking, background play and whole-playlist downloads. The new release improves TV controls, adds quality selection for live streams and fixes a dozen bugs, including subtitles vanishing in fullscreen. It is available from F-Droid and IzzyOnDroid, both of which flag the NonFreeNet anti-feature because the app depends on non-free network services. At the time of writing IzzyOnDroid carries 5.4.0, while F-Droid still offers 5.3.1, added on 12 September. APKs are also on the GitHub releases page, where the notes say arm64-v8a suits most devices; F-Droid lists Android 6.0 or newer as the minimum.

## Perspective {#perspective}

A third-party client spares you a Google account; subscription groups and offline playlists live in the app. Requests still go straight to YouTube, though, and when YouTube restricts an anonymous request the app shows "Sign in to confirm you're not a bot". The project's troubleshooting page suggests retrying on another network or VPN exit. PipePipe also supports signing in and says the login cookie is used only when retrieving playback streams, but once you sign in, those requests are tied to your account.

The app's reach in Asia depends on the network more than the app. GreatFire's test on 21 September found youtube.com 100% blocked in mainland China, and the project's documentation says PipePipe needs googleapis.com and google.com subdomains; when they are unreachable, every YouTube video fails. The same symptom appears elsewhere when a DNS ad filter blocks those domains, so users of such filters need to allow both families. Support for NicoNico and BiliBili, video platforms from Japan and China, gives the app a use beyond YouTube for viewers who follow creators there.

To keep up with YouTube's move to its SABR streaming protocol, PipePipe downloads an Ed25519-signed playback policy from a public GitHub repository and runs it only after checking the signature, validity window and revision number, falling back to the built-in version if anything fails. That lets the developer adjust playback logic without shipping a new release, and the source is public for review. It also means the app executes code fetched from the network, which is worth knowing before recommending it to someone whose threat model is strict.

Language support is another regional factor. The interface is available in Simplified and Traditional Chinese, Japanese and Vietnamese, among others, and the project's translation guide says these are AI-assisted. Native speakers who find awkward phrasing can fix individual entries and send a pull request, which is the most direct way for users in the region to improve an app they rely on.

Reporting problems carries its own privacy details. The troubleshooting page asks users not to put cookies, tokens, account email addresses or screen recordings of a login flow in a public issue, and not to publish an IP address. Stating whether you were signed in, and the error you saw, is enough for a first report.
