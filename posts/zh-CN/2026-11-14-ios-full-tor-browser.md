---
title: iPhone 上的 Tor 选项与完整 Tor Browser 的开发计划
description: 到 11 月 8 日为止，iPhone 上没有 Tor Browser，Tor Project 推荐的是 Onion Browser。Guardian Project 公布一年路线图，Alpha 测试版排在标示为 2027 年 4 月的那一季，Alpha 推出前无法安装。
date: 2026-11-14T00:00:00+08:00
slug: ios-full-tor-browser
categories:
  - mobile
sources:
  - title: "Brewing Onion Cider: Bringing a full Tor Browser to iOS"
    url: https://guardianproject.info/2026/11/02/brewing-onion-cider-bringing-a-full-tor-browser-to-ios/
    publisher: Guardian Project
    date: 2026-11-02
  - title: How to install Tor Browser
    url: https://support.torproject.org/tormobile/tormobile-3/
    publisher: Tor Project
  - title: FAQs
    url: https://onionbrowser.com/faqs
    publisher: Onion Browser
  - title: Using alternative browser engines in the European Union
    url: https://developer.apple.com/support/alternative-browser-engines/
    publisher: Apple
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: Onion Browser
    url: https://apps.apple.com/us/app/onion-browser/id519296448
    publisher: Apple
  - title: Orbot
    url: https://apps.apple.com/us/app/orbot/id1609461599
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

到 11 月 8 日为止，iPhone 上没有 Tor Browser（经 Tor 网络连接的浏览器）。Tor Project 在安装说明页推荐改用 Onion Browser，也提醒它的隐私保护比不上 Tor Browser。Guardian Project 在 11 月 2 日公布一年路线图，目标是把完整的 Tor Browser 带到 iOS，第一个 Alpha 测试版排在路线图标示为 2027 年 4 月的那一季。计划还在决定走哪一条发行路线，Alpha 推出前无法安装，iPhone 用户手上的选项没有改变。

依 Onion Browser 的常见问题页（FAQ），Tor 能让监看连接的人看不到你访问的网站，也让网站无法得知你的实际位置。在 iPhone 上经 Tor 浏览网页，可以用开源的 Onion Browser。它有两种连接方式：搭配另一款 App Orbot，或用 App 内建的 Tor（Onion Browser 的 FAQ 里标注 iOS 17 only）。依 App Store 的资料，到 11 月 8 日为止两款都免费、最低要求都是 iOS 15，最近一次更新分别在 10 月 20 日与 10 月 15 日。

依 FAQ 的比较，Orbot 比较安全，内建的 Tor 比较稳定。使用内建的 Tor 时，真实 IP 会经由 WebRTC（浏览器直接传输音视频与数据的技术）泄露给访问的网站，音频与视频流也无法经过 Tor。FAQ 里的原因是 Apple 提供并强制使用的浏览器引擎 WebKit（引擎是解析与显示网页的核心组件）。Orbot 使用 Apple 的 Network Extensions（网络扩展），Apple 只给它 50 MB 内存，Tor 客户端接近上限时会被终止并重新启动。

依 FAQ，Onion Browser 会在离开前台时自动清除数据、默认不保留缓存与 cookie，也能检测网站的 .onion 地址并自动切换。至于浏览器指纹（网站用设备和浏览器的细节识别访客的手法），FAQ 里的说法是 iOS 内建的 WebKit 能调整的地方很少，最好的做法是跟其他 iOS 用户看起来一样。

只想让整台 iPhone 的连接走 Tor 时，也可以用 Orbot 搭配 Safari。依 FAQ，Orbot 把设备上所有流量都送进 Tor，搭配 Safari 时同样有 Tor 的效果。Orbot 被终止时 Safari 的连接会如何，FAQ 里没有交代。

FAQ 里 Onion Browser 比 Safari 多的保护，首先是确认 Tor 正在运行并接手请求之后才发出连接，另外还有自动清除与 .onion 切换。本文依 Tor Project 与 FAQ 对 WebKit 的说明推论，Safari 与 Onion Browser 一样受 WebKit 限制，同样达不到 Tor Browser 的反追踪能力。

Guardian Project 在公告自述有十年以上开发与发行 Onion Browser、iOS 版 Orbot 的经验。新计划要在 iOS 上提供以 Firefox 的 Gecko 引擎为基础、纳入 Tor Project 补丁的 Tor Browser，同时继续维护 Onion Browser 与 Orbot。依公告，Onion Browser 特意取了不同的名字，因为它并非完整的 Tor Browser。iOS 版要使用 Tor Browser 的名称，还要取得 Tor Project 的批准。

路线图以季为单位，标示为 2027 年 1 月的第二季要展示在 iOS 上运行 Gecko 的原型，并选定主要路线。标示为 2027 年 4 月的第三季要通过 TestFlight（Apple 的测试版分发渠道）与侧载（不经 App Store 安装 App）推出第一个 Alpha。标示为 2027 年 7 月的第四季才要决定下一步是 Beta 还是正式推出。

公告里也写到哪条路最好仍不确定，路线图列了两条。Apple 路线的依据是欧盟《数字市场法》（Digital Markets Act，DMA）要求 Apple 在 iOS 上开放第三方浏览器引擎，以及日本的替代浏览器引擎方案。Gecko 会通过 BrowserEngineKit（Apple 提供给替代引擎的开发工具）运行，经官方商店发行。开放路线改走 AltStore 这类侧载渠道，公告的用语是摆脱 App Store 的审查与限制。

## 导读观点 {#perspective}

依 Tor Project 的说明页，Apple 要求 iOS 上的浏览器使用 WebKit，Onion Browser 因此无法具备与 Tor Browser 相同的隐私保护（欧盟与日本另有方案，见下一段）。FAQ 里的说明是 Tor Browser 在电脑与 Android 上以 Firefox 的 Gecko 为基础，实现代理与反追踪时有更多控制空间，也更可靠。本文的理解是，换成 Gecko 处理的是引擎这一层的限制，经 Tor 连接本身 Onion Browser 现在就能做到。

Apple 的开发者文档到 11 月 8 日为止列出的条件是欧盟方案需要 iOS 17.4 或 iPadOS 18 以上、日本方案需要 iOS 26.2 以上。App 要先通过 Apple 的授权，也只能在当地发行（日本的文档另有 Apple 明确许可的例外）。本文依这些条件推论，除非 Apple 另外许可，欧盟与日本以外的 iPhone 用户无法从官方商店获取走 Apple 路线的 Tor Browser。公告里也有只能在欧洲与日本发行的假设，Guardian Project 打算推动 Apple 在全球开放第三方浏览器引擎。

公告里以 malicious compliance（恶意遵从）形容 Apple 遵循 DMA 的做法，路线图也排了针对 Apple 这个平台与发行者的风险分析。Apple 的文档里写的是，只授权符合特定标准、承诺持续遵守隐私与安全要求的开发者使用替代引擎。依公告，官方商店能触及欧洲与日本只会从 Apple 官方渠道获取 App 的普通用户。侧载对已经面临 App Store 审查的用户是否更有帮助，公告里只有问句，没有结论。

Alpha 的时间表来自路线图，公告里没有它能在哪些地区安装的信息。公告对经欧盟与日本商店发行 iOS 版 Tor Browser 的说法是 when and if（准备好才会进行）。

要对访问的网站隐藏 IP 的人，依 FAQ 的比较适合让 Onion Browser 搭配 Orbot（两款都可以从 App Store 免费安装，需要 iOS 15 以上）。Orbot 反复重新启动时，内建的 Tor 比较稳定，代价是前面提到的 IP 泄露与音视频不经 Tor。以上做法都仍用 WebKit。本文依 Tor Project 的说明推论，需要 Tor Browser 完整防护的人目前要改到电脑或 Android 上使用。

依 Apple 的 iTunes 查询接口在 11 月 8 日的回传，中国大陆区 App Store 查不到 Onion Browser 与 Orbot（各 0 笔），美国区各查到 1 笔。结果只是接口的回传，没有用各地账号实际打开商店页，下架或从未上架的原因与时间点也查不到。公告里没有讨论大陆区商店查不到这两款 App 时，Apple 路线与侧载路线各有什么影响。

不需要对访问的网站隐藏 IP 的读者现在不必做任何设置，要回来看的时间点有两个。标示为 2027 年 1 月的那一季会选定主要路线，本文推论路线的选择会影响欧盟与日本以外的读者能否获取。标示为 2027 年 4 月的那一季要看 Alpha 是否如期推出、开放哪些地区。Guardian Project 规划继续维护 Onion Browser 与 Orbot，路线图的第三季（标示为 2027 年 4 月）也排了协助用户判断该用 Onion Browser 或 iOS 版 Tor Browser 的工作。
