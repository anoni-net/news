---
title: Compositor, an open-source image editor, and maintaining and auditing AI-generated code
description: A designer released Compositor, a free, open-source image editor for the Mac that needs no account, and says AI wrote all of its code. The criticism we found centers on the phrase "I built" and on who reviews and maintains AI-written code. As of 12 October it runs only on Apple silicon Macs with macOS 26 or later.
date: 2026-10-17T00:00:00+08:00
slug: compositor-image-editor
categories:
  - tracking
sources:
  - title: Compositor – The Photoshop alternative for Mac
    url: https://robbietilton.com/compositor
    publisher: Compositor
  - title: Compositor/README.md
    url: https://github.com/robbietilton/Compositor/blob/main/README.md
    publisher: GitHub
  - title: Compositor launch post on X
    url: https://x.com/i/status/2100946395972976843
    publisher: X
    date: 2026-09-18
  - title: Compositor developer's reply on X
    url: https://x.com/i/status/2101334715513106496
    publisher: X
    date: 2026-09-19
  - title: Quote post by a concept artist on X
    url: https://x.com/i/status/2101093572720148574
    publisher: X
    date: 2026-09-18
  - title: Thread by a creative tools developer on X
    url: https://x.com/i/status/2103514110843551887
    publisher: X
    date: 2026-09-25
  - title: Thread by a creative tools developer on X (continued)
    url: https://x.com/i/status/2103514716962501046
    publisher: X
    date: 2026-09-25
  - title: Thread by a creative tools developer on X (follow-up)
    url: https://x.com/i/status/2103523639685738691
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's post on ports on X
    url: https://x.com/i/status/2103520923697733898
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's reply on maintenance on X
    url: https://x.com/i/status/2103519019282358348
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's reply on tracking on X
    url: https://x.com/i/status/2108977298905133319
    publisher: X
    date: 2026-10-10
  - title: Compositor releases
    url: https://github.com/robbietilton/Compositor/releases
    publisher: GitHub
  - title: Add Generative Fill, Remove and Expand (optional, with the user's own Gemini key)
    url: https://github.com/robbietilton/Compositor/pull/58
    publisher: GitHub
    date: 2026-09-21
  - title: Add Enlarger, AI upscaling with Real-ESRGAN
    url: https://github.com/robbietilton/Compositor/pull/73
    publisher: GitHub
    date: 2026-09-22
  - title: Fix unsafe formatting of persisted rotation and hue angles
    url: https://github.com/robbietilton/Compositor/pull/10
    publisher: GitHub
    date: 2026-09-19
  - title: "Feature request: Windows version of Compositor"
    url: https://github.com/robbietilton/Compositor/issues/23
    publisher: GitHub
    date: 2026-09-19
  - title: "FYI: Simplified Chinese localization fork (compositor-cn)"
    url: https://github.com/robbietilton/Compositor/issues/222
    publisher: GitHub
    date: 2026-10-07
  - title: Is https://github.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
  - title: Is https://raw.githubusercontent.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/raw.githubusercontent.com
    publisher: GreatFire
authors:
  - anoni-net
---

A designer released Compositor, an image editor for the Mac, on GitHub on 16 September (UTC) and introduced it on X on 18 September. It is open source under the MIT license, free to download and needs no account, and the developer's launch post says it started as a tool for his own use, to get off an Adobe subscription. As of 12 October the latest release is 1.4.10 from 11 October (UTC), it runs only on Apple silicon Macs with macOS 26 or later, and the interface is English only, with translations not being accepted for now.

The launch post had about 2.4 million views by 12 October, but we could not retrieve the replies under it, so what follows draws only on a small number of public posts on X. A concept artist quoted the launch post to criticize calling AI-written software "I built", describing such work as vibe coding, meaning having AI write code from natural-language instructions. Replying to that post, the developer wrote "AI wrote every line of this" and "Code was always the painful part, never the important part." By our count of the GitHub commit history (the record of each change to the code) on 12 October, 282 of 451 commits carry a co-author credit for an AI coding tool.

A developer who builds creative tools, using the project to explore how AI will change the business of creative tools, wrote on X that its code is "decidedly not for human consumption", and asked what would keep the developer maintaining it over the next six months or two years. The developer replied that he will keep maintaining it because he uses it every day. He maintains only the Mac version and wrote on X that he has not tested any of the Windows or Linux ports others have made.

## Perspective {#perspective}

On GitHub the developer describes Compositor as "a local, single-user editor with no network path". The release notes separately say it checks for updates at most once a day when opened, and updates wait for the user to install them. Reading the app's configuration, we confirmed that the update feed it checks is hosted on GitHub. On X the developer also wrote "no login, no account, no tracking".

An outside contributor submitted a pull request (a proposed code change) adding generative fill, which would send images out only if the user turned it on, supplied their own key for Google's Gemini AI service and pressed generate. The pull request itself says this would be the first feature to send user content off the Mac. The developer commented that he wanted to think about how AI should fit into Compositor long term, and the pull request was later closed without being merged. On a separate on-device AI upscaling feature, he wrote that he would rather rethink AI features as a whole, possibly in a v2.

Being open source means these claims can be checked rather than taken on trust. On 12 October we searched the main branch for keywords and found no network requests or analytics code apart from the update check, which is not a full audit. By our count the app has about 37,000 lines of Swift, most of it AI-generated judging by the commit credits. The creative-tools developer's description of that code is "decidedly not for human consumption".

On 19 September an outside contributor opened eight patch pull requests based on a security scan, one of which said crafted project values outside the expected range could make the inspector or adjustment editor stop working. The developer closed them as a batch, writing that the app is used locally by one person with no untrusted input, so these were "robustness questions rather than security ones". His comment does not say whether opening a project file someone else sent you counts as untrusted input.

His closing comment also explains that import, resizing and export are already capped at 100 megapixels and 30,000 pixels per side, and that the added limits risked refusing valid documents. It adds that the pull requests revealed the automated tests had not run for a while, and that after the fix there are 362 tests. He asked anyone who had actually reproduced a crash to open an issue (a problem report on the project) with the file and steps.

The developer says he will keep maintaining a tool he uses himself, and that people who want other platforms can port it under the MIT license, as other developers have done for Windows and other platforms. The creative-tools developer questions whether the author will keep maintaining features users ask for but he does not use himself, adding that software for ordinary users doesn't seem to have the consulting income, from services sold to companies, that supports many open-source projects. The contributor behind a separate Simplified Chinese fork (an independently modified copy) wrote in an issue on the original project that the fork removed automatic updates, so users are not updated back to the English build and do not hit the original update feed.

Anyone with an Apple silicon Mac on macOS 26 or later can try it from GitHub or Homebrew. Downloading requires no sign-up, though reporting problems requires a GitHub account. Based on the developer's statements and our keyword search, editing images involves no network access apart from the update check, which is on by default and leaves installation to the user. We have not fully audited the code, and the developer has not said whether opening project files from others carries any risk.

The official download and update feed are hosted on GitHub, which may matter to readers in mainland China. As of its last tests on 11 and 8 October, GreatFire reports interference in 64% of 56 conclusive tests of github.com over the past 90 days, and in all of its last 4 tests of raw.githubusercontent.com, where the update feed is hosted, a small sample. These are third-party measurements of host names, not of the specific download paths. The interface is English only, and the one Simplified Chinese fork we found is maintained by an outside contributor; we found no Taiwanese news coverage of Compositor and no source linking it to any regulation in Asia.

When comparing tools like this, a few questions apply. The developer values running locally, no login and freedom to modify the code, and those claims can be checked against the source and actual network connections. The critics care about maintenance and what happens to a feature you rely on if a sole maintainer stops updating it. Whether anyone has read the AI-written code, and how outside reports are handled, can also be seen in a project's issues and pull requests.
