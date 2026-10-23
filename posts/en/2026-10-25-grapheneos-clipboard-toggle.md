---
title: The per-app clipboard read toggle in GrapheneOS
description: GrapheneOS, a privacy-hardened mobile operating system officially supported only on Pixel phones, added Secure Paste in a release announced on 18 September, letting users set app by app which apps cannot read content copied in other apps. As of 23 October the feature is off by default and has to be turned on in settings, and the settings GrapheneOS adds are in English only. Stock Android notifies users after an app has read the clipboard, while iPhone asks for permission before an app reads it programmatically. Having a password manager clear the clipboard after copying a password is a step available on both.
date: 2026-10-25T00:05:00+08:00
slug: grapheneos-clipboard-toggle
categories:
  - mobile
sources:
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases#2026091700
    publisher: GrapheneOS
  - title: GrapheneOS version 2026091700 released
    url: https://discuss.grapheneos.org/d/42090-grapheneos-version-2026091700-released
    publisher: GrapheneOS Discussion Forum
    date: 2026-09-18
  - title: Features overview | GrapheneOS
    url: https://grapheneos.org/features#secure-paste
    publisher: GrapheneOS
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#supported-devices
    publisher: GrapheneOS
  - title: Web installer | Install | GrapheneOS
    url: https://grapheneos.org/install/web
    publisher: GrapheneOS
  - title: "GrapheneOS: \"It's an opt-in feature wit…\" - GrapheneOS Mastodon"
    url: https://grapheneos.social/@GrapheneOS/117292361749585692
    publisher: GrapheneOS
    date: 2026-09-18
  - title: platform_packages_apps_Settings/res/values/strings_ext.xml
    url: https://github.com/GrapheneOS/platform_packages_apps_Settings/blob/2026102100/res/values/strings_ext.xml
    publisher: GitHub
  - title: platform_frameworks_base/core/res/res/values/config_ext.xml
    url: https://github.com/GrapheneOS/platform_frameworks_base/blob/2026102100/core/res/res/values/config_ext.xml
    publisher: GitHub
  - title: GrapheneOS translate to other languages - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/5030-grapheneos-translate-to-other-languages
    publisher: GrapheneOS Discussion Forum
  - title: Privacy changes in Android 10
    url: https://developer.android.com/about/versions/10/privacy/changes
    publisher: Android Developers
  - title: "Behavior changes: all apps"
    url: https://developer.android.com/about/versions/12/behavior-changes-all
    publisher: Android Developers
  - title: Features and APIs Overview
    url: https://developer.android.com/about/versions/13/features
    publisher: Android Developers
  - title: UIPasteControl
    url: https://developer.apple.com/documentation/uikit/uipastecontrol
    publisher: Apple Developer Documentation
  - title: iOS 16.1 Introduces New Copy-and-Paste Permission Settings on Per-App Basis
    url: https://www.macrumors.com/2022/10/17/ios-16-1-paste-from-other-apps-settings/
    publisher: MacRumors
    date: 2022-10-17
  - title: Protecting Android clipboard content from unintended exposure
    url: https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/
    publisher: Microsoft Security Blog
    date: 2023-03-06
  - title: Copy and fill passwords into apps that don't work with 1Password
    url: https://support.1password.com/copy-passwords/
    publisher: 1Password Support
    date: 2026-08-17
  - title: platform_packages_apps_Settings/res at 2026102100 · GrapheneOS/platform_packages_apps_Settings · GitHub
    url: https://github.com/GrapheneOS/platform_packages_apps_Settings/tree/2026102100/res
    publisher: GitHub
  - title: Learn about devices & services available in your region - Google Store Help
    url: https://support.google.com/store/answer/2462844?hl=en
    publisher: Google
  - title: Is https://releases.grapheneos.org blocked in mainland China?
    url: https://en.greatfire.org/https/releases.grapheneos.org
    publisher: GreatFire
authors:
  - anoni-net
---

GrapheneOS is a privacy-hardened mobile operating system built on Android's open-source code, and as of 23 October its officially supported devices are the Pixel 6 through the Pixel 10a. Release 2026091700, announced on the official forum on 18 September, added a clipboard control called Secure Paste. According to the release notes, users can turn off clipboard reading app by app, or use a global toggle to make it off by default for all third-party apps. Users can still paste into those apps through the system selection toolbar, keyboard apps, keyboard shortcuts or accessibility services.

According to GrapheneOS's features page, Android only lets the focused app and the keyboard read the clipboard. Android shows a notice when an app reads content copied in another app, but by then the content has already been read. With Secure Paste on, an app cannot read content copied in other apps but can still read what it copied itself.

Secure Paste does not block reads by default: GrapheneOS described it as an opt-in feature in a reply on Mastodon, and the default in the settings code allows reads. According to the settings code, the toggle is at "Settings > Security & privacy > Privacy controls > Clipboard access", a path the official usage guide does not give. The global default can be "Allow" or "Blocked", and each app can be set to "Allow", "Paste only" or "Follow system clipboard access setting" to follow the global default, with a note in the settings code that Paste only may break some apps. Release 2026091900 then cut the interval between notices about blocked reads from 1 minute to 6 seconds (the notice can be turned off per app), release 2026092500 improved the settings screen, and the release notes list no further clipboard changes up to release 2026102100 on 21 October.

Per the descriptions in the settings code, the global toggle does not apply to system apps, and the current keyboard plus some apps and system features can always read the clipboard. Apps can still see whether the clipboard has content, its type and when it was copied, and accessibility services that can view and act on screen content can trigger a paste and may obtain what is pasted. According to the features page, with Paste only set, pasting into apps that draw their own selection toolbar (such as apps written with Flutter, a cross-platform development framework) means using the keyboard's paste button instead. GrapheneOS added that button to its default keyboard and Gboard already has one, according to replies on the official forum, so people using other keyboards should check that theirs can paste.

## Perspective {#perspective}

According to Microsoft's security blog in 2023, mobile users often use the clipboard to copy sensitive content such as passwords and payment information. Android apps can read and write the clipboard without user consent or any specific permission.

In the same post Microsoft published its findings that an old version of a shopping app read the clipboard periodically and sent the content back to a server when it matched a certain format. The post adds that Microsoft was not aware of any specific malicious intent, and the behaviour was removed in May 2022. Since Android 10, background apps cannot read the clipboard, but that restriction does nothing about apps in the foreground.

According to the Android developer documentation, since Android 12 the system shows a notice the first time an app reads content copied in another app. Android 13 also shows a preview when content is copied, to confirm the copy worked. Apple's developer documentation states that since iOS 16 the system asks the user for permission before an app reads the clipboard programmatically. MacRumors reported in 2022 that from iOS 16.1, apps that have requested to paste get a "Paste from Other Apps" option in Settings, which we have not checked against the current iOS.

We suggest that GrapheneOS users first switch a few apps to Paste only, then decide whether to set the global default to Blocked, pasting through the toolbar or keyboard instead (after checking that their keyboard has a paste key). Both the warning in the settings code and the limitations GrapheneOS lists suggest that blocking everything at once is more likely to break some apps. If an app stops working properly after the change, it can be switched back to Allow.

According to GrapheneOS's features page, Secure Paste replaces the standard approach of desktop and mobile operating systems, and stock Android phones have no per-app toggle. On iPhone an app asks before reading programmatically, and on both platforms users can start by checking their password manager. 1Password's support page states that passwords copied from it are cleared automatically after 90 seconds by default on every platform. We suggest that people using other password managers look in the settings for an option to clear the clipboard, keeping in mind that timed clearing only shortens how long content stays on the clipboard, and the focused app can still read it before it is cleared.

Anyone who wants to install GrapheneOS first needs a supported Pixel, and according to the official FAQ GrapheneOS cannot be installed on carrier-locked devices, mainly those from US carriers. The official web installer page lists the requirements: the device running the installer needs at least 2GB of free memory and 32GB of free storage, and it can be a computer or an Android phone or tablet. By our inference from the settings code directory as checked on 23 October, the settings and apps GrapheneOS adds are in English only, while the rest of the system keeps Android's own translations, including Simplified and Traditional Chinese.

We, a community based in Taiwan, also checked the Google Store's list of regions in Asia for the supported phones. As of 23 October, Google Store Help lists the Asian places where the Pixel 10a, a GrapheneOS-supported model, can be bought as India, Japan, Singapore and Taiwan, while mainland China, Hong Kong, Macau and South Korea are not on the list. The page covers only the Google Store itself, not other retailers or carriers.

According to GrapheneOS's FAQ, its System Updater fetches update information and update files from `releases.grapheneos.org`. GreatFire, which measures censorship in mainland China, recorded interference with that address in its last test on 2 October, the only conclusive test in the 90 days before 23 October. By our inference, downloading system updates over a direct connection from mainland China may not go smoothly.

GrapheneOS users who switch apps to Paste only are blocking apps from reading on their own, but not accessibility services they have turned on or the keyboard they are using. The cost is that some apps need the keyboard's paste key instead.
