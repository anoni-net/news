---
title: Apple 威胁通知的辨识与应对
description: Apple 8 月向 110 个国家的用户发出雇佣间谍软件的威胁通知，绝大多数人不会成为这类攻击的目标。说明页写明真正的通知出现在哪里、不会要求密码与验证码，收到之后可以开启锁定模式并寻求协助。
date: 2026-10-02T07:00:00+08:00
slug: apple-threat-notifications
sources:
  - title: About Apple threat notifications and protecting against mercenary spyware
    url: https://support.apple.com/en-us/102174
    publisher: Apple
    date: 2026-08-13
  - title: Really, pay attention to Apple’s threat notifications
    url: https://freedom.press/digisec/blog/really-pay-attention-to-apples-threat-notifications/
    publisher: Freedom of the Press Foundation
    date: 2026-09-02
  - title: If Apple sends you a push notification alerting you to a spyware attack, take it seriously
    url: https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/
    publisher: TechCrunch
    date: 2026-08-13
  - title: About Lockdown Mode
    url: https://support.apple.com/en-us/105120
    publisher: Apple
    date: 2026-09-14
  - title: Apple says no one using Lockdown Mode has been hacked with spyware
    url: https://techcrunch.com/2026/03/27/apple-says-no-one-using-lockdown-mode-has-been-hacked-with-spyware/
    publisher: TechCrunch
    date: 2026-03-27
  - title: Digital Security Helpline
    url: https://www.accessnow.org/help/
    publisher: Access Now
  - title: Apple warns Indian opposition leaders of state-sponsored iPhone attacks
    url: https://techcrunch.com/2023/10/30/indian-opposition-leaders-says-apple-has-warned-them-of-state-sponsored-iphone-attacks/
    publisher: TechCrunch
    date: 2023-10-31
  - title: 關於封閉模式
    url: https://support.apple.com/zh-tw/105120
    publisher: Apple
    date: 2026-09-18
  - title: 關於 Apple 威脅通知與防範傭兵間諜軟體
    url: https://support.apple.com/zh-tw/102174
    publisher: Apple
    date: 2026-08-13
  - title: 关于锁定模式
    url: https://support.apple.com/zh-cn/105120
    publisher: Apple
    date: 2026-09-18
  - title: 关于 Apple 威胁通知和防范雇佣间谍软件的攻击
    url: https://support.apple.com/zh-cn/102174
    publisher: Apple
    date: 2026-08-13
  - title: OONI Explorer
    url: https://explorer.ooni.org/chart/mat?probe_cc=CN&since=2026-09-01&until=2026-09-29&time_grain=day&axis_x=measurement_start_day&test_name=web_connectivity&domain=www.accessnow.org
    publisher: OONI
authors:
  - anoni-net
---

Apple 在 8 月 13 日向 110 个国家的用户发出威胁通知，称他们的 iPhone 成为雇佣间谍软件（私营公司为政府开发的间谍软件，例如 NSO Group 的 Pegasus）的攻击目标。Apple 从 2021 年起每年发出多次通知，至 8 月 13 日覆盖 150 多个国家或地区。Apple 的说明页也写道，绝大多数人不会成为这类攻击的目标。

新闻自由组织 Freedom of the Press Foundation（FPF）9 月 2 日在简报中提醒读者重视这类通知。Apple 2026 年 8 月更新的说明页也写明通知是高可信度的警报，应高度重视，但调查无法绝对可靠。FPF 转述非营利组织 Access Now 的解说，通知不会交代攻击是否成功与攻击者是谁。Apple 也不指明攻击者或地区，发出通知的原因同样不公开。

Apple 的说明页写明，通知会出现在 iPhone 的锁定屏幕与「设置」里，同时发到 Apple 账户关联的邮箱。2026 年起的发件人是 `threat-notifications@email.apple.com`。登录 `account.apple.com` 后，页面顶部也会显示横幅。通知形式因机型与系统版本而异。

Apple 建议收到通知的人开启锁定模式（限制部分功能以降低风险的模式），并寻求专家协助，例如 Access Now 全天候数字安全帮助热线。FPF 也建议 Android 用户了解类似的「高级保护」功能。

## 导读观点 {#perspective}

真正的通知会建议开启锁定模式等措施，但不会要你点链接、打开文件、安装 App 或描述文件，也不索取密码与验证码。收到自称来自 Apple 的可疑消息时，不要点链接，自行登录 `account.apple.com` 查看有没有横幅。

截至 9 月 29 日，Access Now 的说明页写明热线在两小时内回复。热线的十种语言包括英文、西班牙文、他加禄文与阿拉伯文，但没有中文。网络干扰观测项目 OONI 9 月在中国境内测量了 Access Now 首页 76 次，73 次无异常。中文用户可以用英文联系，海外读者也可求助当地数字安全团体。

2023 年 10 月有一批通知发到印度。Apple 当时给 TechCrunch 的声明写道可能有误报，也可能漏掉部分攻击。现行说明页已不提误报。

TechCrunch 采访的安全研究者提到，锁定模式阻止多数信息附件类型并限制网页引擎 WebKit，尤其缩小了零点击攻击（无需受害者操作）可利用的范围。Apple 3 月 27 日给 TechCrunch 的回复写道，没有发现开启锁定模式的设备被雇佣间谍软件攻破。同一篇报道也写道，不排除有未被发现的绕过手法。

代价是除某些图像、视频和音频外，大多数信息附件都会被阻止，链接和链接预览也无法使用。部分网站可能无法正常运行。信任的网站与 App 可以排除在外，但会削弱保护。

锁定模式需要 iOS 16 以上，位置在「设置」的「隐私与安全性」，打开时会重启。iPad 与 Mac 要分别打开，配对的 Apple Watch 会跟着 iPhone 打开。简体中文界面称为「锁定模式」。有充分理由担心自己成为目标的人，不必等收到通知才打开。
