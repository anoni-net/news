---
title: 浏览器指纹与各家浏览器的防护
description: 浏览器指纹是网站读取窗口大小、字体与绘图的细微差异这类特征，组合出可以反复认出同一个浏览器的标识，清除 cookie 或连接 VPN 都挡不住。依英国信息专员办公室的说明，Google 从 2025 年 2 月起不再禁止广告客户使用指纹技术。能挡下多少取决于用哪个浏览器，Firefox、Safari、Brave 与 Tor Browser 各有做法。本文 10 月 23 日查看的 Chrome 官方状态页，列出的指纹相关项目只有减少浏览器随每个请求自动附带的数据。
date: 2026-10-25T00:00:00+08:00
slug: browser-fingerprinting-cookies
categories:
  - tracking
sources:
  - title: Our response to Google's policy change on fingerprinting
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/12/our-response-to-google-s-policy-change-on-fingerprinting/
    publisher: Information Commissioner's Office
    date: 2024-12-19
  - title: Updating our platform policies to reflect innovations in the ads ecosystem
    url: https://support.google.com/marketingplatform/answer/15732590
    publisher: Google Marketing Platform Help
  - title: A new path for Privacy Sandbox on the web
    url: https://privacysandbox.google.com/blog/privacy-sandbox-update
    publisher: Google
    date: 2024-07-22
  - title: Privacy Sandbox feature status
    url: https://privacysandbox.google.com/overview/status
    publisher: Google
  - title: Building a more private web
    url: https://blog.google/products-and-platforms/products/chrome/building-a-more-private-web/
    publisher: Google
    date: 2019-08-22
  - title: Overview of the Platforms programs policies update (February 2025)
    url: https://support.google.com/platformspolicy/answer/15738904
    publisher: Google
  - title: Next steps for Privacy Sandbox and tracking protections in Chrome
    url: https://privacysandbox.google.com/blog/privacy-sandbox-next-steps
    publisher: Google
    date: 2025-04-22
  - title: Update on Plans for Privacy Sandbox Technologies
    url: https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies
    publisher: Google
    date: 2025-10-17
  - title: Mitigating Browser Fingerprinting in Web Specifications
    url: https://www.w3.org/TR/fingerprinting-guidance/
    publisher: W3C
    date: 2025-09-25
  - title: "Firefox expands fingerprint protections: advancing towards a more private web"
    url: https://blog.mozilla.org/en/firefox/fingerprinting-protections/
    publisher: Mozilla
    date: 2025-11-10
  - title: Private Browsing 2.0
    url: https://webkit.org/blog/15697/private-browsing-2-0/
    publisher: WebKit
    date: 2024-07-16
  - title: WebKit Features in Safari 26.0
    url: https://webkit.org/blog/17333/webkit-features-in-safari-26-0/
    publisher: WebKit
    date: 2025-09-15
  - title: Apple elevates the iPhone experience with iOS 26
    url: https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/
    publisher: Apple
    date: 2025-06-09
  - title: Change Advanced settings in Safari on Mac
    url: https://support.apple.com/guide/safari/advanced-ibrw1075/mac
    publisher: Apple Support
  - title: Fingerprinting Protections
    url: https://github.com/brave/brave-browser/wiki/Fingerprinting-Protections
    publisher: Brave
  - title: How do I use Shields while browsing?
    url: https://support.brave.app/hc/en-us/articles/360022806212-How-do-I-use-Shields-while-browsing
    publisher: Brave Help Center
  - title: Fingerprinting protections - Features - Tor Browser
    url: https://support.torproject.org/tor-browser/features/fingerprinting-protections/
    publisher: Tor Project
  - title: Cover Your Tracks
    url: https://coveryourtracks.eff.org/
    publisher: EFF
  - title: Cover Your Tracks
    url: https://coveryourtracks.eff.org/learn
    publisher: EFF
  - title: Fingerprints are the new cookies
    url: https://royfish.dev/fingerprints-are-the-new-cookies
    publisher: royfish.dev
  - title: 指纹识别保护 - 功能 - Tor 浏览器
    url: https://support.torproject.org/zh-CN/tor-browser/features/fingerprinting-protections/
    publisher: Tor Project
  - title: 在 Mac 上的 Safari 浏览器中更改“高级”设置
    url: https://support.apple.com/zh-cn/guide/safari/ibrw1075/mac
    publisher: Apple 支持
  - title: Firefox 简体中文界面字符串 preferences.ftl
    url: https://github.com/mozilla-l10n/firefox-l10n/blob/main/zh-CN/browser/browser/preferences/preferences.ftl
    publisher: Mozilla
  - title: Is https://www.google.com/chrome blocked in mainland China?
    url: https://en.greatfire.org/https/www.google.com/chrome
    publisher: GreatFire
  - title: Is https://www.google.cn/chrome blocked in mainland China?
    url: https://en.greatfire.org/https/www.google.cn/chrome
    publisher: GreatFire
  - title: Google Chrome 网络浏览器
    url: https://www.google.cn/chrome/
    publisher: Google
  - title: Is https://www.mozilla.org blocked in mainland China?
    url: https://en.greatfire.org/https/www.mozilla.org
    publisher: GreatFire
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: iTunes lookup API (cn, Firefox)
    url: https://itunes.apple.com/lookup?id=989804926&country=cn
    publisher: Apple
  - title: iTunes lookup API (cn, Chrome)
    url: https://itunes.apple.com/lookup?id=535886823&country=cn
    publisher: Apple
  - title: iTunes lookup API (cn, Brave)
    url: https://itunes.apple.com/lookup?id=1052879175&country=cn
    publisher: Apple
  - title: Is https://www.torproject.org blocked in mainland China?
    url: https://en.greatfire.org/https/www.torproject.org
    publisher: GreatFire
  - title: OONI API
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
  - title: Is https://support.torproject.org blocked in mainland China?
    url: https://en.greatfire.org/https/support.torproject.org
    publisher: GreatFire
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 中国人大网
    date: 2021-08-20
  - title: 个人信息保护政策法规问答（2026年1月）
    url: https://www.cac.gov.cn/2026-01/09/c_1769688003183197.htm
    publisher: 国家互联网信息办公室
    date: 2026-01-09
authors:
  - anoni-net
---

一篇个人博客文章以「Fingerprints are the new cookies」为题，整理网站在 cookie 之外识别浏览器的方式。依 W3C 隐私工作组 2025 年 9 月的文件，浏览器指纹是网站通过设置或其他可观察的特征识别访客、浏览器或设备的能力，例如窗口大小、字体与绘图的细微差异。依英国信息专员办公室（ICO）2024 年 12 月 19 日的说明，Google 从 2025 年 2 月 16 日起不再禁止使用其广告产品的组织采用指纹技术。能挡下多少取决于用哪个浏览器，Firefox、Safari、Brave 与 Tor Browser 各有做法。

同一份 W3C 文件提到，清除 cookie 或使用 VPN 都无法阻止进一步的关联，指纹通常也无法清除或重置。依同一份文件，面对有决心的追踪者，单靠已经广泛部署的技术手段很难完全消除指纹。文件也认为规范可以减少指纹。

Google 2019 年的博客写到，用户无法清除指纹，也就无法控制信息如何被收集。Google 当时认为用指纹追踪用户是错的。Google 2024 年 12 月对广告客户的公告，写这次政策更新是为了配合隐私增强技术与联网电视等新的广告渠道，公告与 2025 年 2 月的政策更新页都没有提到指纹。「不再禁止」是 ICO 转述 Google 对广告客户的通知，Google 的两份公开页面都没有这个说法，ICO 也形容这项变更不负责任。

ICO 另外提醒，依英国《隐私与电子通信条例》（PECR）等数据保护法规，企业使用指纹技术之前要给用户公平的选择并在必要时取得同意。这些规定适用于英国，台湾有没有针对设备指纹的专门规范，本文没有查到。

Google 原本计划在 Chrome 淘汰第三方 cookie（网页里嵌入的广告或分析服务存进浏览器、用来跨网站认出用户的小文件），2024 年 7 月 22 日改为提议由用户自行选择。2025 年 4 月 22 日，Google 宣布不再推出额外的提示窗口，用户继续在 Chrome 的隐私与安全设置里选择。2025 年 10 月 17 日，Google 又宣布淘汰大部分 Privacy Sandbox（Google 为取代第三方 cookie 提出的一组浏览器技术），其中包括隐藏 IP 地址的 IP Protection。本文 10 月 23 日查看的 Privacy Sandbox 状态页（2026 年 8 月 14 日更新），列出的指纹相关项目只有减少浏览器随每个请求自动附带的数据，例如浏览器版本与操作系统的字符串。

## 导读观点 {#perspective}

WebKit 2024 年介绍 Safari 无痕浏览的文章，把挡指纹的做法分成两种。一种让很多用户共用同一个指纹，另一种让每个网站看到的指纹都不同。Tor Browser 走的是前一种，它的支持页面说明要让所有用户完全相同实际上不可能，目标是减少每一项特征可以区分的组数。

Brave 两种都用。依 Brave 的说明，它一方面让各个 Brave 尽量看起来相似，一方面加入少量随机的噪声。噪声的种子每个会话、每个网站都不同，网站之间就难以把同一个人串起来，Brave 的帮助中心也列出 Shields 默认开启屏蔽指纹。

Mozilla 2025 年 11 月的公告说明，Firefox 145 新增的指纹防护先在隐私浏览与增强型跟踪保护的严格模式开启，公告当时写正在让它成为默认设置。WebKit 2025 年 9 月介绍 Safari 26.0 的文章提到，Safari 会阻止已知的指纹脚本可靠地读取屏幕尺寸、音频等可能透露设备特征的信息。

Safari 另有一项高级指纹保护，可以只用在无痕浏览或用于所有浏览。Apple 2025 年 6 月的 iOS 26 新闻稿写这项保护默认扩及所有浏览，Apple 的 Safari 帮助页面则没有写默认值，本文建议自己打开设置确认。依 WebKit 2024 年那篇文章，iPhone 的位置是英文界面的「Settings > Apps > Safari > Advanced > Advanced Tracking and Fingerprinting Protection」，选「All Browsing」。Mac 是 Safari 设置的「高级」，开启「使用高级追踪和指纹记录保护」并选择用于所有浏览。

用桌面版 Firefox 的读者，可以在「隐私与安全」把「增强型跟踪保护」从「标准」改成「严格」，取得 145 版新增的防护。手机版的默认设置本文没有查到。

需要更强保护、能接受较慢连接的人，可以改用 Tor Browser，本文 10 月 23 日查看的 EFF 说明页也把它列为最实际的选择。Tor Project 的指纹保护说明页有简体中文与正体中文版，所在的 `support.torproject.org` 在 GreatFire 最后一次测试（5 月 7 日）的结果是被封锁，之后没有新的测试。依文档站的整理，Android 有官方的 Tor Browser，iPhone 没有。

想知道自己的浏览器有多容易被认出，可以打开 EFF 的 Cover Your Tracks，本文查到的页面都是英文。页面说明只收集匿名数据，比较的对象是最近来测试的访客，各浏览器防护做法的差别也整理在文档站的[浏览器指纹是什么，为什么很难摆脱](https://anoni.net/docs/zh-cn/basics/browser-fingerprinting/){target="_blank"}。

在中国大陆取得这些浏览器，要先能连上官网或下载页。第三方测量项目 GreatFire 对 Chrome 下载页 `www.google.com/chrome` 最近 2 次有结论的测试都受到干扰（最后一次 10 月 16 日），GreatFire 的判定是访问不稳定。Google 的简体中文 Chrome 下载页 `www.google.cn/chrome` 最近 2 次有结论的测试都连接正常（最后一次 9 月 29 日），`www.mozilla.org` 的判定则是可以连接（最近 4 次有结论的测试都正常）。Apple 的 iTunes 查询 API 在中国大陆的 App Store 可以查到 Firefox 与 Chrome（10 月 23 日查询）。

`brave.com` 最近 14 次有结论的测试都被封锁（最后一次 10 月 18 日），iTunes 查询 API 在中国大陆的 App Store 也没有查到 Brave（10 月 20 日查询，不等于 Brave 或 Apple 公告下架）。`www.torproject.org` 最近 3 次有结论的测试都被封锁（最后一次 10 月 16 日），从 2011 年 9 月 3 日起就有干扰记录。依网络干扰观测项目 OONI 的公开 API，9 月 18 日到 10 月 18 日中国大陆的 Tor 测试 301 次中有 293 次标为异常、确认封锁 0 次。OONI 的 Tor 测试量的是 Tor 运作所需的服务器能否连上，异常也不等于确认封锁。

中国大陆《个人信息保护法》第四条把个人信息定义为与已识别或者可识别的自然人有关的各种信息，不包括匿名化处理后的信息。第二十四条规定通过自动化决策方式向个人进行信息推送、商业营销时，应当同时提供不针对其个人特征的选项，或者提供便捷的拒绝方式。国家互联网信息办公室 1 月发布的个人信息保护政策法规问答，把用户标识符、网页浏览记录、IMEI 等设备信息与用户画像都列为个人信息，两份文件都没有提到浏览器指纹。本文 10 月 23 日只读了这两份文件，没有读《互联网广告管理办法》与相关国家标准，不确定是否另有针对设备指纹的规定。

防护越强，网站越容易出问题。Mozilla 的公告提醒，更激进的屏蔽一定会破坏正常的网站功能，例如日历与会议工具需要真实的时区。Tor 的支持页面提到，特征不一致可能让反机器人系统把 Tor 用户当成机器人，EFF 的说明页也提醒防护本身有时会变成指纹的一部分。

本文的推论是，这些设置减少的是网站在读者没有登录时认出同一个人的能力，Brave 的做法则特别针对跨网站与跨会话的串联。登录同一个账号的网站，仍然知道是谁在浏览。
