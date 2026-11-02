---
title: The Excluded Apps setting for Siri AI in iOS 27.2
description: iOS 27.2 adds Excluded Apps under Siri in Settings, for choosing apps that Siri, Search and suggestions may not read. According to EFF, on-screen awareness also stops working for excluded apps. Siri AI on iPhone and iPad is not offered in the EU or mainland China, and as of 2 November its languages do not include Chinese, so people whose device and Siri language are set to Chinese cannot use it for now.
date: 2026-11-03T00:00:00+08:00
slug: siri-ai-exclude-apps
categories:
  - tracking
follows:
  - 2026-09-27-ios27-siri-ai-data-access
sources:
  - title: About iOS 27 Updates
    url: https://support.apple.com/en-us/149076
    publisher: Apple
    date: 2026-10-26
  - title: "Victory! You Can Now Exclude Apps from Siri AI"
    url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
    publisher: EFF
    date: 2026-10-28
  - title: About iPadOS 27 Updates
    url: https://support.apple.com/en-us/149075
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-10-22
  - title: Siri AI, a profoundly more capable and personal assistant, is here
    url: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/
    publisher: Apple
    date: 2026-09-14
  - title: iOS 和 iPadOS 27 - 功能的供應狀況 - Apple (香港)
    url: https://www.apple.com/hk/ios/feature-availability/
    publisher: Apple
  - title: iOS 和 iPadOS 27 - 功能特色適用範圍 - Apple (台灣)
    url: https://www.apple.com/tw/ios/feature-availability/
    publisher: Apple
  - title: iOS and iPadOS 27 - Feature Availability - Apple (SG)
    url: https://www.apple.com/sg/ios/feature-availability/
    publisher: Apple
authors:
  - anoni-net
---

Apple's release notes, published on 26 October, say iOS 27.2 adds Excluded Apps, a setting under Siri in Settings for choosing which apps Siri, Search and suggestions can access. Siri AI is the new Siri introduced in iOS 27, which can read app content to answer questions, and it runs on the iPhone 15 Pro, 15 Pro Max and iPhone 16 or later. Excluded Apps is listed in the Siri AI section of the release notes, and the iPadOS 27.2 notes list the same item. Siri AI on iPhone and iPad is not offered in the EU or mainland China, and as of 2 November its supported languages do not include Chinese, so people whose device and Siri language are set to Chinese cannot use Siri AI for now.

The same release notes say 27.2 adds French, Japanese, Korean, Portuguese and Spanish to Siri AI, making six languages with English. Apple's "How to get Siri AI" support page, published on 22 October, still said on 2 November that Siri AI is available only in English, and we go by the later release notes. According to Apple's September press release, the other Apple Intelligence features support simplified and traditional Chinese, while Siri AI has a language list of its own.

EFF's post of 28 October says Excluded Apps fulfils one of the asks in its Encrypt It Already campaign from earlier in 2026. The concern behind it is that many AI features require cloud processing, so even with privacy protections built into these systems, content from secure messaging apps may leave the device without the user knowing. EFF had asked for a way to tell the operating system's AI not to access a given app, even at the cost of some features, through a setting that is simple to understand.

According to EFF, after updating to 27.2 you open Excluded Apps under Siri in Settings and tap Add Apps to choose the apps to exclude. Siri AI then cannot access that app's content, and some features may stop working. EFF's example is that once Messages is excluded, you can no longer have Siri AI read or reply to messages for you. On-screen awareness, which lets you call up Siri and ask about what is on screen, also stops working for excluded apps, so with Signal excluded you cannot ask Siri to pick out any information on the Signal screen.

EFF writes that when Siri AI launched, blocking it from an app took several toggles, and the alternative was turning Siri AI off entirely. Our 27 September post, based on EFF's earlier article, said neither users nor app developers could block on-screen awareness, and that the way to limit access was turning off Show Content in Search app by app. The 27.2 exclusion list puts this in one place and covers on-screen awareness too, and in EFF's view the lost features show that the setting works.

EFF also checked where Android stands. According to EFF, in the Gemini app you tap your profile picture and go to Settings > Personal Intelligence > Connected Apps to revoke apps you do not want Gemini to access. EFF likes that the list is opt-in but finds the process less than intuitive. Signal does not support Gemini's app access feature at all, so it is not on the list, and Gemini cannot read Signal's content directly.

EFF also writes that once Device Assistance is turned on in Connected Apps, Gemini can read notifications. Basic features such as setting a timer need Device Assistance too, so EFF reckons most people already have it on.

Screen context is controlled by the Use screen and app data option in Gemini's settings, under Device controls > Screen context, and stays active until that option is turned off. Use screen and app data cannot be set per app. According to EFF, when users choose to use notification reading and screen context, both may read Signal's content or notifications. EFF wants Google to let users turn both features off per app.

## Perspective {#perspective}

Our September post noted that a Siri AI request may be processed on the phone or sent to Private Cloud Compute (the cloud servers Apple runs to handle AI requests), and nothing on screen says which. From that we inferred in September that anyone who wants to keep using Siri AI can only limit, at the source, which apps it may read. According to EFF, Siri AI cannot access the content of an excluded app, and from this we infer that such content is not sent off the device with a request either. In EFF's view Apple should go further and offer an option to use only on-device AI features, similar to what Samsung offered with Galaxy AI.

The iOS 27.2 release notes also list more sources Siri AI can draw on, including photos attached in Messages, Calendar event attendees, voicemails, and Safari history and Reading List, and Siri AI can now recall past conversations. Going by the release notes, people already using Siri AI will find it can reach more sources after the update than before.

Apple's release notes do not say what Siri can still do once an app is excluded, only that the setting governs which apps Siri, Search and suggestions can access. Our inference from that sentence is that an excluded app's content may also stay out of Search and suggestions.

On Android, EFF compares Gemini's app list with the iOS exclusion list and finds the Android process less direct than Apple's new setting. According to EFF, people using Gemini on an Android phone can check two places, Device Assistance in Connected Apps and Use screen and app data, and each can only be turned off as a whole. Turning off Device Assistance also takes away basic features such as timers.

People whose device and Siri language are set to Chinese cannot use Siri AI for now. As of 2 November, Apple's support pages do not say whether people who have not turned on Siri AI can see Excluded Apps in Settings, or whether setting it affects Search and suggestions for them.

According to Apple's release notes and its support page, Siri AI is not available in mainland China. Apple's September press release states that Siri AI and the other new Apple Intelligence features will not be available in China while Apple works through regulatory requirements, with no timeline given. Japanese and Korean are among the five languages added in 27.2, though the support page says only that availability varies by region and platform, and we found no country-by-country listing for them. On Apple's feature availability pages for Hong Kong, Taiwan and Singapore, Siri AI was still listed on 2 November as available in English and not offered in mainland China or the EU, and those pages may not yet reflect 27.2.

People who already have Siri AI on can, after updating to iOS 27.2, go to Siri in Settings, tap Excluded Apps and add the apps to exclude (the option names follow the English interface in EFF's post). According to EFF, those who prefer the older version can still turn off Siri AI and go back to Siri Classic for now. The exclusion list only covers your own phone. We infer that if another member of a group has not excluded the same app and calls up Siri AI over the same conversation, the content may still leave from that person's phone.
