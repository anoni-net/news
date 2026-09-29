---
title: 检测智能眼镜蓝牙信号的 ZuckOff
description: ZuckOff 比对蓝牙广播，提醒附近有 Ray-Ban Meta 这类带镜头的智能眼镜，但无法判断对方是否正在录像，App 本身也没有公开源代码。
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
authors:
  - anoni-net
---

一款名为 ZuckOff 的 App 可以检测附近有没有人戴着 Ray-Ban Meta、Oakley Meta 或 Snap Spectacles 这类带镜头的智能眼镜。iPhone 与 Android 都有，基本的扫描功能免费，中国大陆、台湾、香港与新加坡的 App Store 都能下载。界面有简体中文，没有正体中文。

开发者自己买了各款眼镜，录下它们广播的蓝牙信号，整理成每一款的特征。App 比对蓝牙广播里的制造商代码，比对到时提醒用户，并根据信号强度估计大概的距离。项目网站写明数据不会离开手机，也不需要注册账号。

限制同样写在项目网站。多数眼镜戴着时会持续广播，少数独立运作的型号不发出信号，App Store 的说明另外写到，眼镜跟主人的手机配对之后也可能停止广播。没检测到不代表没有人在录像，检测到也不代表有人在录像，App 无法得知是谁戴着，信号强度也指不出方向。

Wired 写到，Meta 的智能眼镜 2025 年约卖出七百万副。眼镜拍摄时会亮起白色的指示灯，Meta 的说明页写明，检测到指示灯被遮住、动过手脚或被破坏时，眼镜会自动停用镜头。

## 导读观点 {#perspective}

智能眼镜会通过蓝牙对外广播自己的存在，广播里带着制造商的代码。ZuckOff 在项目网站公开了比对用的代码，例如 Ray-Ban Meta 与 Oakley Meta 所属 Luxottica 的 `0x0D53`。检测的原理不复杂，准确度取决于这张表整理得多完整，App Store 的更新记录就写到，1.4.0 修正了把某些 iPhone 误判成镜头眼镜的问题。

ZuckOff 没有公开源代码，也没有授权声明，外界无法检验 App 实际做了什么，只能相信网站上的说法。它要的权限不多，Android 版只要求蓝牙扫描所需的附近设备权限，并声明不用来推算位置，所以不要求定位权限。

Meta 在 9 月 23 日宣布眼镜在新加坡与韩国开卖。香港、澳门、马来西亚、印度尼西亚与泰国2026 年稍晚也会上市，日本则是 5 月 21 日就已经开卖。

在采访、开会或私人聚会前，想确认现场有没有镜头的人，可以开着蓝牙用 ZuckOff 扫描一次当作提醒，免费的基本扫描就够用。扫描结果只是线索，重要的对话仍然要事先跟在场的人约定，请大家摘下眼镜、把手机留在场外。
