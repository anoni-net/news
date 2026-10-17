---
title: Brave 的电子邮件别名
description: Brave 桌面版从 1.94 起提供电子邮件别名，注册网站时用转发邮箱代替真实邮箱。每人免费 5 个，要先创建 Brave 账号。到 10 月 12 日为止手机版还没有，别名能否回信官方没有写。
date: 2026-10-14T00:05:00+08:00
slug: brave-email-aliases
categories:
  - tracking
sources:
  - title: Brave launches Email Aliases to keep your personal email address private from websites
    url: https://brave.com/privacy-updates/39-email-aliases/
    publisher: Brave
    date: 2026-08-27
  - title: "Brave Accounts: your password never leaves your device, ever."
    url: https://brave.com/blog/brave-accounts/
    publisher: Brave
    date: 2026-08-27
  - title: What is a Brave Email Alias?
    url: https://support.brave.app/hc/en-us/articles/45530506862349-What-is-a-Brave-Email-Alias
    publisher: Brave
    date: 2026-08-28
  - title: Brave Browser Privacy Policy
    url: https://brave.com/privacy/browser/
    publisher: Brave
    date: 2026-09-23
  - title: "[Email Aliases] Bubble UI for mobiles"
    url: https://github.com/brave/brave-browser/issues/50818
    publisher: GitHub
    date: 2025-11-13
  - title: Brave Release Notes
    url: https://brave.com/latest/
    publisher: Brave
  - title: brave_components_resources_zh-TW.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-TW.xtb
    publisher: GitHub
  - title: Block bravealias.com disposable email domain
    url: https://github.com/disposable/disposable/issues/288
    publisher: GitHub
    date: 2026-08-29
  - title: 如何在 iPhone 或 iPad 上使用 iCloud+ 的「隱藏電子郵件地址」
    url: https://support.apple.com/zh-tw/102548
    publisher: Apple
    date: 2025-09-30
  - title: Firefox Relay
    url: https://relay.firefox.com/
    publisher: Mozilla
  - title: SimpleLogin Pricing
    url: https://simplelogin.io/pricing/
    publisher: SimpleLogin
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: Is https://relay.firefox.com blocked in mainland China?
    url: https://en.greatfire.org/https/relay.firefox.com
    publisher: GreatFire
  - title: iOS and iPadOS 27 - Feature Availability
    url: https://www.apple.com/ios/feature-availability/
    publisher: Apple
  - title: brave_components_resources_zh-CN.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-CN.xtb
    publisher: GitHub
  - title: 中华人民共和国网络安全法
    url: https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm
    publisher: 国家互联网信息办公室
    date: 2025-12-29
authors:
  - anoni-net
---

Brave 8 月 27 日推出电子邮件别名（Email Aliases），桌面版从 1.94 起可以在注册网站时改用转发邮箱，不交出真实邮箱。每人免费 5 个，要先创建 Brave 账号，这个账号与订阅 Brave VPN 等服务的 Premium 账号分开。到 10 月 12 日为止，Android 与 iOS 版的版本记录都还没有这项功能，帮助页只有英文与日文。

网站的邮箱输入框会出现创建别名的提示，没出现时可以在输入框上点右键选「New Email Alias」，发到别名的邮件会转发到 Brave 账号登记的邮箱。依 Brave 的发布页与隐私政策，Brave 不读邮件内容，只做一般的垃圾邮件与病毒过滤。转发成功后邮件数秒内从服务器删除，主邮箱暂时收不到时最多重试 24 小时，转发服务用的是 Amazon Web Services。发布页也提醒，初期部分转发邮件可能会被分到垃圾邮件箱。

同一天推出的 Brave 账号用 OPAQUE 协议登录，这种协议让服务器不必持有密码也能验证用户，2025 年 7 月发布为 RFC 9807。Brave 账号的博客文章提到密码本身不会发送到 Brave 的服务器。同一篇文章也提醒，OPAQUE 本身挡不了钓鱼网站，也不会让弱密码变强。

## 导读观点 {#perspective}

Brave 的发布页把邮箱称为长期且通用的标识符，并以 Meta、Google、LinkedIn 的广告功能为例，广告主可以上传客户的邮箱来比对用户。这种比对在服务器之间进行，浏览器拦截跟踪器拦不到。每个网站用不同的别名，网站之间就无法用邮箱比对出同一个人。

依发布页，Brave 会加密保存账号邮箱与生成的每个别名，别名与真实邮箱的对应存在 Brave 的服务器上。帮助页列出为了调试会记录收信时间与部分邮件头，但不记录邮件内容与发件人信息，隐私政策写这些记录最长 14 天内删除。在隐私政策里，除非有效的法律要求使 Brave 有义务披露，否则不会披露账号关联的邮箱与别名。官方页面没有写能不能从别名回信，也没有写别名用哪个域名。

一份网站用来拦截一次性邮箱的开源名单，9 月在反馈议题里把 `bravealias.com` 当成 Brave 别名的域名，列入较严格的分级。维护者提到这是转发服务、不是一次性邮箱，与 Firefox Relay、SimpleLogin 属于同一类。所以只列入较严格的分级，采用这一级的网站才会拦截。

Apple 的 Hide My Email（台湾版称「隐藏电子邮件地址」）包含在 iCloud+ 付费方案，可以直接回复。Firefox Relay 免费提供 5 个，匿名回信列在付费方案，付费方案的供应地区名单没有台湾与香港。SimpleLogin 是开源项目，免费方案有 10 个别名并可从别名回信。

第三方监测网站 GreatFire 10 月 12 日的记录显示，brave.com 在中国大陆最近 15 次有效测试都无法打开。account.brave.com 等服务网址没有测试记录，别名功能能否使用不明。relay.firefox.com 最近一次测试可以连接。Apple 的功能供应页把 Hide My Email 列入中国大陆。

2025 年 10 月修正的《网络安全法》第二十六条要求提供信息发布、即时通讯等服务的网络运营者，在与用户签订协议或确认提供服务时要求用户提供真实身份信息。本文的提醒是别名只隐藏邮箱，不改变这项要求。

用 Brave 桌面版的读者更新到 1.94 以上，在地址栏输入 `brave://settings/email-aliases` 创建账号，就能生成别名。源代码里的简体中文界面字符串也已翻译。别名保护的只是邮箱这个标识符，用手机号码、真实姓名或支付信息注册时，网站仍然可以用这些资料比对出同一个人。
