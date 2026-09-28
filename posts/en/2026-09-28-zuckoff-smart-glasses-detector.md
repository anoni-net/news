---
title: ZuckOff, a Bluetooth detector for camera smart glasses
description: ZuckOff matches Bluetooth broadcasts to warn that camera glasses such as Ray-Ban Meta are nearby. It cannot tell whether anyone is recording, and the app itself is closed source.
date: 2026-09-28T07:00:00+08:00
slug: zuckoff-smart-glasses-detector
sources:
  - title: ZuckOff | Camera glasses detector
    url: https://zuckoff.app/
    publisher: ZuckOff
  - title: ZuckOff
    url: https://apps.apple.com/us/app/zuckoff/id6795234035
    publisher: App Store
  - title: How to Tell If Someone Near You Is Wearing Meta Smart Glasses
    url: https://www.wired.me/story/meta-smart-glasses-detector-app-zuckoff
    publisher: WIRED Middle East
    date: 2026-09-15
  - title: Privacy Settings for Meta AI Glasses
    url: https://www.meta.com/ai-glasses/privacy/
    publisher: Meta
  - title: Introducing Ray-Ban Meta Audio and Our Deepest Lineup of AI Glasses Yet
    url: https://www.meta.com/blog/ray-ban-meta-audio-and-deepest-ai-glasses-lineup/
    publisher: Meta
    date: 2026-09-23
  - title: Ray-Ban Meta (Gen 2)およびOakley Meta、5月21日より日本でも販売開始
    url: https://www.meta.com/ja-jp/blog/AI-glasses-Japan-launch/
    publisher: Meta
    date: 2026-05-19
  - title: 中華民國刑法 第 315-1 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=C0000001&flno=315-1
    publisher: Laws & Regulations Database of Taiwan
authors:
  - anoni-net
---

ZuckOff, an app for iPhone and Android, tells you whether someone nearby is wearing camera glasses such as Ray-Ban Meta, Oakley Meta or Snap Spectacles. Basic scanning is free, a paid Pro version adds background monitoring and alerts, and the app is listed in the App Store in Taiwan, Hong Kong, mainland China and Singapore. Its interface includes Simplified Chinese but not Traditional Chinese.

The developer bought the glasses, recorded the Bluetooth signals each model broadcasts, and matched the manufacturer codes inside them. When a code matches, the app alerts you and uses signal strength to estimate rough distance. The project site says nothing leaves your phone and no account is needed.

The site is also clear about the limits. Most pairs keep advertising while worn, but a few standalone models stay silent, and the App Store listing adds that glasses paired to their owner's phone can go quiet too. Silence is not proof that nobody is recording, a detection is not proof that anyone is, and the app cannot tell who is wearing the glasses or in which direction they are.

## Perspective {#perspective}

The technique is simple. Camera glasses announce themselves over Bluetooth, and ZuckOff publishes the codes it matches, such as `0x0D53` for Luxottica, which makes Ray-Ban Meta and Oakley Meta. Accuracy depends on how complete and current that table is. The 1.3.0 update notes say second-generation Ray-Ban Meta frames carry a different manufacturer code from the first, which the app had to learn, and the 1.4.0 notes say it had been mistaking some iPhones for camera glasses.

ZuckOff is closed source and states no license, so nobody outside can check what it actually does. What it asks for is modest. The Android version needs only the nearby-devices permission for Bluetooth scanning, declared as never used to derive location, so it does not ask for location access.

The glasses themselves are spreading across Asia. Ray-Ban Meta and Oakley Meta went on sale in Japan on 21 May 2026, and Meta announced on 23 September that they are available in Singapore and South Korea, with Hong Kong, Macau, Malaysia, Indonesia, Thailand and the Philippines to follow later this year. Meta's help page says the white capture LED blinks while recording and the camera is disabled if the LED is covered or tampered with. According to WIRED, about seven million pairs of Meta glasses were sold in 2025.

Existing law already covers the recording itself. Taiwan's Criminal Code Article 315-1 makes it an offence to record other people's non-public activities or conversations without good reason, punishable by up to three years' imprisonment. The provision applies to any recording device and does not single out wearables.

Before an interview, a meeting or a private gathering, anyone who wants to know whether there is a camera in the room can switch on Bluetooth and run a scan as a prompt; the free basic scan is enough. Treat the result as a hint, not a guarantee. For conversations that matter, agree with everyone present in advance to take off their glasses and leave their phones outside.
