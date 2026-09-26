---
title: Data access settings for Siri AI in iOS 27
description: The new Siri in iOS 27 can read Notes, Messages and Mail by default, and requests may be processed on Apple's servers. EFF has listed the settings that narrow what it can read.
date: 2026-09-27T03:21:00+08:00
slug: ios27-siri-ai-data-access
sources:
  - title: How to Limit What Apple's New Siri AI Can Access in iOS 27
    url: https://www.eff.org/deeplinks/2026/09/how-limit-what-apples-new-siri-ai-can-access-ios-27
    publisher: EFF
    date: 2026-09-18
  - title: Turn off and restrict access to Apple Intelligence features on Mac
    url: https://support.apple.com/guide/mac-help/turn-restrict-access-apple-intelligence-mchlb2e44f94/mac
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-09-22
  - title: How to get the next generation of Apple Intelligence
    url: https://support.apple.com/en-us/121115
    publisher: Apple
    date: 2026-09-14
authors:
  - anoni-net
---

iOS 27 brings a new Siri, Siri AI, merged with Spotlight into one interface, so swiping down on the Home Screen to search also opens Siri. It runs on the iPhone 15 Pro, 15 Pro Max and iPhone 16 or later. Siri AI is in beta, supports only English, and is not yet available in every region.

By default Siri AI can read Apple's own apps such as Notes, Messages and Mail, and third-party apps once their developers add support. A request may be handled on the phone or sent to Apple's Private Cloud Compute servers, and nothing on screen says which. EFF warns people using Advanced Data Protection, whose iCloud data is end-to-end encrypted, that cloud processing changes their risk assessment.

On-screen awareness lets you ask Siri about whatever is on screen. EFF's example is summarising an encrypted Signal group chat, whose content may then go to Private Cloud Compute. Neither users nor app developers can currently block it.

EFF's settings: to keep Siri AI out of an app, turn off Show Content in Search for that app in Settings. To return to the old Siri, set Allowed Siri Version to Siri Classic under Screen Time, Content & Privacy Restrictions. Siri AI does not train on your interactions by default, and consent given during setup can be withdrawn by turning off Improve Siri & Dictation under Privacy & Security, Analytics & Improvements. Apple's help page covers the Mac, where macOS 27 offers Siri Classic after Siri is turned off and each summary feature has its own switch.

## Perspective {#perspective}

EFF notes that the "Private" in Private Cloud Compute means the system is designed so that Apple cannot see or keep the data. It does not promise that the data stays encrypted or stays on the device. Using it means trusting that Apple's servers behave as designed, whereas end-to-end encryption only needs the keys to stay on your own devices.

Where you are in Asia decides whether any of this applies yet. Apple's support page says Siri AI does not currently work when the Apple Account region is mainland China, and Apple Intelligence features do not work on supported devices bought in mainland China. Apple Intelligence itself supports Chinese (simplified and traditional), Japanese, Korean and Vietnamese, but Siri AI needs both the device language and the Siri language set to a supported language, which today means English. For the iPhone, Apple's page names only two exclusions, the EU and Apple Accounts in mainland China, and adds that availability varies by region. Elsewhere in Asia, the practical requirement is running the iPhone and Siri in English. The per-app search settings exist on every iPhone and can be changed now, without waiting for Siri AI to support your language.

Because you cannot tell which requests left the phone, the only lever is limiting which apps Siri AI can read. People using Advanced Data Protection can start with apps that hold work material or personal records, such as Notes and Mail.

On-screen awareness cannot be blocked, so whether an encrypted conversation stays on devices depends on everyone in it. If any member of a group calls up Siri over the chat, the content may leave from that person's phone, and end-to-end encryption does not cover that step. People who discuss sensitive matters in group chats can agree with the other members not to use on-screen awareness on the conversation, and can consider switching back to Siri Classic themselves.
