---
title: Signal's screenshot blocking against operating system AI assistants, and its limits
short_title: Signal's screenshot block on OS AI agents
description: Signal now restricts the AI assistants built into iOS and Android from capturing its chats, but the Mac app has no such protection, so Mac users have to exclude Signal in Siri's settings themselves. As of 29 November, Siri AI does not support Chinese, and screen context, Gemini's automatic screen reading, works only in English. If the person on the other end of a chat has these features on, your messages can still be read.
meta_description: Signal restricts AI assistants on iOS and Android from capturing chats. The Mac app is not covered, and a contact's device can still expose messages.
date: 2026-11-30T00:00:00+08:00
slug: signal-ai-agent-screenshots
categories:
  - encryption
follows:
  - 2026-11-03-siri-ai-exclude-apps
sources:
  - title: Signal is Serious About Protecting Your Privacy
    url: https://signal.org/blog/protecting-your-privacy/
    publisher: Signal
    date: 2026-11-20
  - title: By Default, Signal Doesn't Recall
    url: https://signal.org/blog/signal-doesnt-recall/
    publisher: Signal
    date: 2025-05-21
  - title: "Add 'Block Siri AI' setting to Settings > Privacy"
    url: https://github.com/signalapp/Signal-iOS/commit/9256c9583
    publisher: Signal-iOS (GitHub)
    date: 2026-11-02
  - title: AssistantScreenSecurityObserver.kt
    url: https://github.com/signalapp/Signal-Android/blob/main/app/src/main/java/org/thoughtcrime/securesms/components/AssistantScreenSecurityObserver.kt
    publisher: Signal-Android (GitHub)
  - title: Signal Moves to Block AI Agents
    url: https://www.eff.org/deeplinks/2026/11/signal-now-blocks-ai-agents
    publisher: EFF
    date: 2026-11-24
  - title: "Victory! You Can Now Exclude Apps from Siri AI"
    url: https://www.eff.org/deeplinks/2026/10/victory-you-can-now-exclude-apps-siri-ai
    publisher: EFF
    date: 2026-10-28
  - title: About iOS 27 Updates
    url: https://support.apple.com/en-us/149076
    publisher: Apple
  - title: How to get Siri AI
    url: https://support.apple.com/en-us/127893
    publisher: Apple
    date: 2026-11-12
  - title: Use screen actions to chat with the Gemini mobile app
    url: https://support.google.com/gemini/answer/15850607?hl=en
    publisher: Google
  - title: Signal blocks screenshots by Apple, Google operating systems to protect data from AI agents
    url: https://therecord.media/signal-no-screenshots-by-apple-google-operating-systems
    publisher: The Record
    date: 2026-11-23
  - title: iOS 和 iPadOS 27 - 功能的供應狀況 - Apple (香港)
    url: https://www.apple.com/hk/ios/feature-availability/
    publisher: Apple
  - title: iOS 和 iPadOS 27 - 功能特色適用範圍 - Apple (台灣)
    url: https://www.apple.com/tw/ios/feature-availability/
    publisher: Apple
  - title: Gemini mobile app availability
    url: https://support.google.com/gemini/answer/14579026?hl=en
    publisher: Google
authors:
  - anoni-net
---

Signal has announced that on iPhone and Android it is restricting the AI agents built into the operating system (AI assistants that can read the screen and operate apps on the user's behalf) from capturing chats, while the Mac app gets no such protection. As of 29 November, Apple's Siri AI (the new Siri introduced in iOS 27) does not support Chinese, and screen context, the feature that lets Google's Gemini read the screen automatically, is limited to English. Most people who use their phones in Chinese have not turned these features on yet. According to Signal's blog, captured data puts everyone in the conversation at risk, including when it is the person on the other end who has these features on.

Operating system AI agents get their information by scanning the screen, and Signal's blog post of 20 November says that Google and Apple are integrating agentic features such as Gemini and Siri AI deep into their operating systems, and that Signal chats are being captured as a result. In Signal's account, the captured content goes into whatever local database or remote server the agent is using at that moment, after which it is outside Signal's control. Signal dealt with a similar problem in May 2025, when it turned on Screen security (a setting that stops the Signal window from being screenshotted) by default on Windows 11 to block Microsoft Recall.

On iPhone, Signal blocks screenshots outright on iOS 27, both inside the app and in the App Switcher (the thumbnails shown when switching between apps). The setting is called Block Siri AI and sits in Signal's privacy settings, a name taken from the Signal-iOS source code. People who want to take screenshots can turn it off, and EFF's post of 24 November states that it is on by default.

The Android app turns on Screen security automatically only when it detects an AI assistant asking to read the screen, after which nothing in Signal can be screenshotted until the user turns it off. Signal's blog says that on many vendors' versions of Android other than Pixel, Signal has no reliable way to tell that a user tried to take a screenshot once screenshots are disabled. Disabling screenshots outright would make them fail silently and confuse users, so Signal chose to detect AI assistants instead. When the setting switches on automatically, a prompt lets the user turn it back off, and according to the Signal-Android source code, the prompt will not appear again for 90 days after that.

In the same post, Signal asks operating system vendors to give developers an easy, documented way to opt their apps out of AI reading and processing. The Record reports that Apple did not immediately respond, and that Microsoft and Google declined to comment.

## Perspective {#perspective}

End-to-end encryption protects messages in transit and on the server, so only the devices of the people in the conversation can decrypt them. By the time a message is on screen it has already been decrypted, and the screen content the operating system can access is the same as what the user sees, so a built-in AI reading the screen does not need to break any encryption. Signal's blog says that the operating system's AI features weaken Signal's ability to guarantee privacy on its own.

Blocking screenshots does not deal with other possible routes, such as an AI agent reading content already on the device through the file system, and Signal calls the remedy incomplete in the same post. According to Signal, the Mac app does not block Siri AI because Signal has found no API that can reliably block screenshots. Most agents read app data precisely through screenshots, yet macOS only protects against continuous screen recording. So for Mac users, Signal's advice is about the system settings instead.

When a member of a group has turned the protection off, uses a Mac, or has an Android model on which Signal cannot detect the AI assistant, the conversation may still be read by AI from that person's device. Signal's blog says that turning the protection off may expose both your own and your contacts' Signal content to AI agents.

Siri AI cannot yet be used in Chinese, and in mainland China a region rule adds a further limit. As of 29 November, Siri AI does not work if the Apple Account region is in mainland China, and it needs the device language and the Siri language set to the same supported language. Apple lists six such languages, Japanese and Korean among them but not Chinese, and Apple's feature availability pages for Hong Kong and Taiwan show the same six. As of 20 October, the Gemini mobile app was offered in Hong Kong, Japan, Macau, Singapore, South Korea and Taiwan, and mainland China was not on its list.

The operating system settings matter only to people who have turned on Siri AI or Gemini's screen context, while everyone who uses Signal should check Signal's own setting once. After updating the app, iPhone users can go to Signal's privacy settings to check whether Block Siri AI is on, and Android users can choose to keep Screen security when the prompt appears. According to the Signal-Android source code, what switches on when an assistant is detected is the same Screen security setting, so you can turn it on yourself without waiting for the prompt, at the cost of not being able to take screenshots in Signal.

On the Apple side, iOS 27.2 already adds a setting users can change, Excluded Apps under Siri in Settings, for choosing apps that Siri, Search and suggestions may not read. macOS 27 has the same item in System Settings, and Signal's only recommendation for Mac users is to add Signal to it, to keep Siri AI from proactively reading message content. EFF's October post says that once Signal is excluded, you cannot even call up Siri to ask about what is on the Signal screen. Signal's Block Siri AI stops screenshots inside Signal, which is a separate mechanism, so iPhone users can turn on both.

Android users with Gemini can turn off screen context, the feature that reads the screen automatically, under Screen context in Gemini's settings, where it is split into two options, Use text from screen and Use screenshot. Google's help page lists no per-app option and EFF's October post states that there is none, so as of 29 November screen context can only be turned off for all apps at once. Asking about the screen manually with "Ask about…" is not affected by these two options.
