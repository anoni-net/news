---
title: iOS 浏览器引擎在欧盟与日本的开放条件与争议
description: 欧盟与日本要求 Apple 在 iOS 开放 WebKit 以外的浏览器引擎，Apple 以安全与隐私为由订了条件，Mozilla 则写到这些条件让它未能推出 Gecko 版的 Firefox。依 Mozilla 11 月 20 日的文章，到那时没有开发者推出非 WebKit 的 iOS 浏览器。
date: 2026-11-26T00:00:00+08:00
slug: ios-browser-engines
categories:
  - mobile
sources:
  - title: Why there are still no non-WebKit browsers on iOS
    url: https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/
    publisher: Mozilla
    date: 2026-11-20
  - title: Using alternative browser engines in the European Union
    url: https://developer.apple.com/support/alternative-browser-engines/
    publisher: Apple
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: App Review Guidelines
    url: https://developer.apple.com/app-store/review/guidelines/
    publisher: Apple
    date: 2026-10-16
  - title: Apple announces changes to iOS in Japan
    url: https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/
    publisher: Apple
    date: 2025-12-17
  - title: Outline of the Act on Promotion of Competition for Specified Smartphone Software (Mobile Software Competition Act (MSCA))
    url: https://www.japaneselawtranslation.go.jp/en/outlines/view/154
    publisher: Japan Fair Trade Commission
  - title: The CMA's programme of work across mobile platforms
    url: https://www.gov.uk/guidance/the-cmas-programme-of-work-across-mobile-platforms
    publisher: Competition and Markets Authority
    date: 2026-02-10
  - title: "The Digital Markets Act Is Delivering Real Wins, But Not Yet for Browser Engines"
    url: https://open-web-advocacy.org/blog/the-digital-markets-act-is-delivering-real-wins-but-not-yet-for-browser-engines/
    publisher: Open Web Advocacy
    date: 2026-05-15
  - title: How Apple’s Key Tactic Could Prevent Japan’s Smartphone Act from Improving Browser Competition
    url: https://open-web-advocacy.org/blog/how_apples_key_tactic_could_prevent_japans_smartphone_act_from_improving_browser_competition/
    publisher: Open Web Advocacy
    date: 2026-01-06
  - title: Apple iTunes 查询接口，Chrome，中国大陆区
    url: https://itunes.apple.com/lookup?id=535886823&country=cn
    publisher: Apple
  - title: Apple iTunes 查询接口，Firefox，中国大陆区
    url: https://itunes.apple.com/lookup?id=989804926&country=cn
    publisher: Apple
  - title: Apple iTunes 查询接口，Onion Browser，中国大陆区
    url: https://itunes.apple.com/lookup?id=519296448&country=cn
    publisher: Apple
  - title: Apple iTunes 查询接口，Orbot，中国大陆区
    url: https://itunes.apple.com/lookup?id=1609461599&country=cn
    publisher: Apple
authors:
  - anoni-net
---

iPhone 与 iPad 上的浏览器，不论是 Safari、Chrome、Firefox 还是标榜隐私的浏览器，都使用 Apple 的 WebKit 引擎（解析与显示网页的核心组件）。欧盟与日本的法规要求 Apple 开放其他引擎，Apple 以安全与隐私为由订了两地的条件。Mozilla 11 月 20 日的文章写到，这些条件让它至今未能推出以自家引擎为基础的 Firefox，到发文时也没有任何开发者推出非 WebKit 的 iOS 浏览器。依 Apple 的 App 审核指南，浏览网页的 App 要使用 WebKit，申请例外的条件分别写在欧盟与日本的两份页面。

依 Mozilla 的文章，主要平台里只有 iPhone 与 iPad 有这项限制。在 Apple 自己的 macOS 上，用户也能使用以 Gecko（Mozilla 开发的浏览器引擎）为基础的 Firefox。Firefox 的许多功能实现在 Gecko 里，Mozilla 因此很难把完整的 Firefox 带到 iPhone 上。

依倡议组织 Open Web Advocacy（OWA）的整理，欧盟《数字市场法》（Digital Markets Act，DMA）要求被认定为守门人的大型平台开放其他浏览器引擎，Apple 从 2024 年 3 月起要遵守。日本的《智能手机软件竞争促进法》（日文简称スマホソフトウェア競争促進法，英文 Mobile Software Competition Act，MSCA）也有类似的规定。日本公平交易委员会（JFTC）的法律概要写到，规模达到门槛、由 JFTC 指定的业者，不得以只允许自家引擎这类条件妨碍其他开发者使用别的引擎。业者为了安全、隐私等正当理由时可以例外。

开发者要使用其他引擎，依 Apple 的开发者文档需先取得授权，App 也只能在欧盟或日本当地发行（日本的条件在 2025 年 12 月公布）。安全方面，已经遭到攻击利用的漏洞要及时修补，文档举的例子是最简单的类别在 30 天内处置。隐私方面，引擎要默认拦截第三方 cookie（可以用来跨网站追踪的 cookie）。

依 Mozilla 的说法，要使用 Gecko 就不能直接更新用户已经安装的 Firefox，需要另做第二个 Firefox。用户得下载新 App，迁移书签、密码与浏览记录，再手动切换。Mozilla 写到相当比例的人会因此放弃，包括从欧盟的浏览器选择界面挑了 Firefox 的人。条件之一要求 Mozilla 不得披露项目的非公开信息，它仍举了这个例子说明面对的难处。

浏览器引擎经常处理不受信任、可能恶意的内容，也能接触用户的敏感数据，依 Apple 的开发者文档是最常见的攻击途径之一。Apple 因此只授权符合标准、承诺持续遵守安全与隐私要求的开发者。依 OWA 的引述，Apple 的法务副总裁在 2025 年的 DMA 工作坊提到 Google、Mozilla 等第三方可以带入自己的引擎，「for whatever reason, they have chosen not to do so」（不论出于什么原因，它们选择不这么做）。

OWA 在 5 月的文章写到没有浏览器业者在欧盟推出自家引擎，并请欧盟执委会调查 Apple 是否确实遵守 DMA。到 11 月 22 日，我们没有查到执委会针对 Apple 浏览器引擎条件的决定，也没有查到 Apple 对 Mozilla 这篇文章的公开回应。

英国竞争与市场管理局（CMA）2025 年 10 月把 Apple 的移动平台认定为具有策略市场地位（strategic market status），范围包括移动浏览器与浏览器引擎。认定之后，CMA 可以对 Apple 采取针对性的措施。到 11 月 22 日，CMA 的工作计划页把移除 Apple 要求浏览器使用 WebKit 的限制列为接下来预期推进的工作，页面没有写时程。

## 导读观点 {#perspective}

iOS 上换一款浏览器，界面、默认设置与附加功能会不同，引擎都是 WebKit。本站 [11 月 14 日的导读](https://anoni.net/news/2026/11/ios-full-tor-browser/)依 Tor Project 的说明整理过，Tor Browser 以 Firefox 的 Gecko 为基础，iPhone 上的 Onion Browser（经 Tor 连接的开源浏览器）受 WebKit 限制而达不到同样的保护。10 月整理的 [Firefox iOS 版广告拦截](https://anoni.net/news/2026/10/firefox-ios-ad-blocker/)也是用 WebKit 的内容拦截技术实现的，电脑版与 Android 版的 Firefox 则能直接安装扩展。

照 Apple 只能在当地发行的条件推想，即使欧盟或日本之后出现使用其他引擎的浏览器，台湾、香港与其他地区的 iPhone 用户从 App Store 获取的仍会是 WebKit 浏览器。例外是 Apple 另外许可，或当地的法规也要求开放。11 月 14 日那篇整理的 iOS 版 Tor Browser 开发计划，经 App Store 发行时同样受这项条件限制。

Apple 公开的两份条件页列了安全与隐私要求，也列了只能在当地发行的限制，其中没有另做一个 App 的文字。Mozilla 则写到自己受保密条件限制，无法公开细节。对于没有浏览器上架，Mozilla 与 OWA 归因于 Apple 的条件，Apple 的法务副总裁在 2025 年的工作坊上则归因于业者自己的选择。

在 iPhone 上需要经 Tor 浏览网页的人，可以用 11 月 14 日那篇整理的 Onion Browser 搭配 Orbot（把手机连接送进 Tor 网络的 App）。网页仍由 WebKit 处理，依同一篇整理的说明，浏览器指纹（网站用设备与浏览器的细节识别访客的手法）能调整的地方很少。Tor Browser 只有电脑与 Android 版，需要它完整防护的人要改用这两种设备，想用 Firefox 扩展的人也一样。只用 Safari 或其他浏览器上网的读者现在不需要调整设置。

Apple 的两份条件页只写了欧盟与日本，没有为中国大陆另订浏览器引擎规定，我们也没有找到中国大陆要求开放的当地法规。App 审核指南要求浏览网页的 App 使用 WebKit，例外只列了欧盟与日本。按指南的文字，中国大陆区 App Store 里的 Chrome 与 Firefox（10 月 23 日时有上架）应该仍是 WebKit 浏览器。

11 月 8 日时，中国大陆区 App Store 没有上架前面提到的 Onion Browser 与 Orbot，台湾、香港、日本与美国区有上架。

比较各地的做法时，安全方面可以用 Apple 举的 30 天例子看开放之后漏洞能否及时处置，竞争方面可以用 Mozilla 描述的迁移数据成本看用户是否因此流失。
