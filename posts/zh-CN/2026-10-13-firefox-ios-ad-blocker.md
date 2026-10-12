---
title: Firefox iOS 版的内置广告拦截与 Android 的系统层做法
description: iPhone 与 iPad 上的 Firefox 内置广告拦截，9 月中的 156 版版本说明首次列出。功能默认关闭，要自己到设置开启。一篇个人博客整理的 Android 系统层做法多半要信任提供服务的运营方或 App。
date: 2026-10-13T00:05:00+08:00
slug: firefox-ios-ad-blocker
categories:
  - mobile
sources:
  - title: "Introducing Ad Blocker for Firefox on iOS: More control, fewer distractions"
    url: https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/
    publisher: Mozilla
    date: 2026-09-01
  - title: 156.0 Firefox for iOS Release
    url: https://www.firefox.com/en-US/firefox/ios/156.0/releasenotes/
    publisher: Mozilla
    date: 2026-09-15
  - title: System-level ad-blocking in Android in 2026
    url: https://kevinboone.me/adblock.html
    publisher: Kevin Boone
    date: 2026-10-01
  - title: 在 Android 手機上管理進階網路設定
    url: https://support.google.com/android/answer/9654714?hl=zh-Hant
    publisher: Google
  - title: 在 Android 手机上管理高级网络设置
    url: https://support.google.com/android/answer/9654714?hl=zh-Hans
    publisher: Google
  - title: Firefox 快速隐私浏览器
    url: https://apps.apple.com/cn/app/firefox-private-safe-browser/id989804926
    publisher: App Store
  - title: Mozilla adds ad blocking to Firefox for iOS
    url: https://www.theregister.com/software/2026/08/17/mozilla-adds-ad-blocking-to-firefox-for-ios/5288585
    publisher: The Register
    date: 2026-08-17
  - title: Firefox 快速隱私瀏覽器
    url: https://apps.apple.com/tw/app/firefox-private-safe-browser/id989804926
    publisher: App Store
  - title: App Review Guidelines
    url: https://developer.apple.com/app-store/review/guidelines/
    publisher: Apple
    date: 2026-06-08
  - title: Is https://dns.adguard-dns.com blocked in mainland China?
    url: https://en.greatfire.org/https/dns.adguard-dns.com
    publisher: GreatFire
  - title: Is https://f-droid.org blocked in mainland China?
    url: https://en.greatfire.org/https/f-droid.org
    publisher: GreatFire
authors:
  - anoni-net
---

Mozilla 9 月 1 日公告，iPhone 与 iPad 上的 Firefox 内置广告拦截，默认关闭。用户要自己到设置的浏览（Browsing）区开启，源代码里的简体中文界面字符串写作「广告拦截器」。版本说明在 9 月 15 日发布的 156 版首次列出这项功能。依外媒转述的 Mozilla 说法，功能是逐步开放的，到 10 月 12 日 App Store 上的最新版是 158.0。

公告写明，广告拦截用 Apple 的 WebKit 内容拦截技术与 EasyList 过滤列表，在许多第三方广告与广告相关的跟踪器加载之前拦下。Mozilla 的说法是，iOS 上的扩展运作方式跟其他平台不同，所以直接把功能做进浏览器。公告也写明广告支撑许多网站，所以功能设计成可选用。网站自己直接放的广告、搜索结果里的广告与 Firefox 新标签页上的赞助快捷方式，都不受这项功能影响。

电脑版与 Android 版的 Firefox 本来就能安装广告拦截的扩展，这次的变更只影响 iOS 版。想在 Android 整台手机拦广告的人，有另一套做法。10 月 1 日一篇个人博客的作者整理了 2026 年在 Android 系统层拦截广告的四种做法，分别是拦截型的 DNS（把域名转成 IP 地址的服务）服务、附广告拦截的 VPN 服务、不需要 root 的本地 VPN App，以及需要 root（取得手机系统的最高权限）改写系统 hosts 文件的做法。就作者所知，这几种都是改写 DNS 的行为，把已知广告商的主机名对应到假的 IP 地址。

## 导读观点 {#perspective}

两边都是在连接之前拦下已知的广告网址，差在作用的范围。iOS 版的广告拦截只作用在 Firefox 打开的网页，用的是 WebKit 的内容拦截技术，Apple 的审核指南也规定浏览网页的 App 要使用 WebKit（欧盟与日本另有申请例外的办法）。Android 的系统层做法作用在所有 App。依作者的说明，广告内置在 App 里、或 App 直接用 IP 地址连接（作者写明目前还少见）时，改写 DNS 就拦不住。

依本文的推论，前三种做法要信任提供服务的那一方，因为所有 App 查询的域名都会经过它。作者提醒，恶意的 DNS 或 VPN 运营方甚至可能把网上银行的连接导到自己的代理服务器，在意隐私的人可以挑不留记录、支持加密 DNS 的服务。本地 VPN App 会让所有流量经过同一个 App，作者建议只用开源的。需要 root 的做法不必信任外部运营方，作者写的取舍是要自行检查写进 hosts 文件的内容。

Firefox 同样在 App Store 中国区上架，10 月 12 日的版本也是 158.0，商店页的宣传文字就是这项广告拦截。10 月 12 日查询第三方监测网站 GreatFire 时，AdGuard DNS 默认服务器的 HTTPS 网址近期只有 2 次有效测试且都无法打开，F-Droid 最近 5 次也都失败。GreatFire 量的是网址能否打开，不是 Android 设置里专用 DNS（用来指定 DNS 服务主机名的设置）的实际连接方式，测试次数也少。本文依此推断，在中国大陆用专用 DNS 填入境外的拦截型服务可能连不上，从 F-Droid 取得本地 VPN App 也有同样的问题。

用 iPhone 或 iPad 的读者把 Firefox 更新到最新版，设置的浏览区应该就有广告拦截的开关，App Store 标示需要 iOS 15.0 以上。简体中文界面的说明写明，网站功能异常时可以尝试关闭。开启之后，网站自己放的广告、搜索结果的广告与新标签页的赞助内容仍会出现。

主要在意网页广告的 Android 用户，作者认为最简单的做法可能是改用支持广告拦截的浏览器，不必动到系统设置。想连 App 里的广告一起拦，可以在设置的「网络和互联网」里找到专用 DNS（部分说明页称「私人 DNS」，不同品牌的菜单位置可能不同），填入拦截型 DNS 服务的主机名。作者写明这类服务价格不一，多数有免费试用。填了之后，所有 App 的域名查询都会交给那家运营方处理，要先确认它的日志保存政策。
