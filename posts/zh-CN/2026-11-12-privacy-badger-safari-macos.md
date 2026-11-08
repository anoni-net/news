---
title: Privacy Badger 的 macOS Safari 版
description: EFF 10 月 19 日推出阻止追踪器的扩展 Privacy Badger 的 Safari 版，只支持 Mac，需要 Safari 26.5 与 macOS 15.7.7 以上。到 11 月 8 日为止，iPhone 与 iPad 还没有 Safari 版。
date: 2026-11-12T00:00:00+08:00
slug: privacy-badger-safari-macos
categories:
  - tracking
sources:
  - title: Announcing Privacy Badger for Safari on macOS
    url: https://www.eff.org/deeplinks/2026/10/announcing-privacy-badger-safari-macos
    publisher: EFF
    date: 2026-10-19
  - title: EFF Launches Privacy Badger for Safari on macOS
    url: https://www.eff.org/press/releases/eff-launches-privacy-badger-safari-macos
    publisher: EFF
    date: 2026-10-19
  - title: Privacy Badger | Fight hidden tracking with EFF
    url: https://privacybadger.org/
    publisher: EFF
  - title: Privacy Badger App - App Store
    url: https://apps.apple.com/us/app/privacy-badger/id6761143693
    publisher: Apple
  - title: Support Safari on iOS
    url: https://github.com/EFForg/privacybadger/issues/3248
    publisher: GitHub
  - title: privacybadger/src/_locales
    url: https://github.com/EFForg/privacybadger/tree/master/src/_locales
    publisher: GitHub
  - title: Privacy Badger now supports Safari
    url: https://freedom.press/digisec/blog/privacy-badger-now-supports-safari/
    publisher: Freedom of the Press Foundation
    date: 2026-10-28
  - title: Prevent cross-site tracking in Safari on Mac
    url: https://support.apple.com/guide/safari/prevent-cross-site-tracking-sfri40732/mac
    publisher: Apple
  - title: GreatFire：www.eff.org
    url: https://en.greatfire.org/https/www.eff.org
    publisher: GreatFire
  - title: GreatFire：privacybadger.org
    url: https://en.greatfire.org/https/privacybadger.org
    publisher: GreatFire
  - title: 隐私獾
    url: https://privacybadger.org/zh-cn/
    publisher: EFF
  - title: iTunes Search API（中国大陆店面）
    url: https://itunes.apple.com/lookup?id=6761143693&country=cn
    publisher: Apple
authors:
  - anoni-net
---

美国数字权利组织 EFF 在 10 月 19 日推出 Privacy Badger 的 Safari 版。Privacy Badger 是 EFF 开发的免费浏览器扩展，会自动学习识别并阻止追踪器。Safari 版只支持 Mac，需要 Safari 26.5 以上，Mac App Store 页面列出的系统要求是 macOS 15.7.7 以上。到 11 月 8 日为止，iPhone 与 iPad 的 Safari 还不能安装。

依 EFF 的公告，Privacy Badger 已有超过 400 万名用户。EFF 的技术人员在新闻稿提到，支持 Safari 一直是用户最常提出的需求之一。公告把 Privacy Badger 能在 Safari 26.5 以上推出，归功于 Safari 对扩展支持的改进。

依公告，Safari 默认的浏览模式会限制追踪器可以获取的信息，但仍让追踪器加载。Privacy Badger 从一开始就不让追踪器加载，可以挡下绕过 Safari 防护的追踪手法。嵌入的推文、评论区与视频播放器这类小组件，即使用户没有点击也可能共享数据，Privacy Badger 会把它们换成点了才加载的占位框。

Privacy Badger 也会自动发出全球隐私控制（Global Privacy Control，GPC）信号，告诉网站不要出售或共享用户的个人数据。公告列出加州、科罗拉多、新泽西、康涅狄格等美国的州，写明 GPC 在这些地方已具法律效力。

Safari 版要从 Mac App Store 免费安装，卖家是 EFF。公告提醒 Safari 安装扩展的步骤比其他浏览器复杂，附上 Apple 的说明页。这是 Safari 版的第一个版本，遇到问题可以发邮件到 `extension-devs@eff.org` 或在 GitHub 反馈。

## 导读观点 {#perspective}

依 privacybadger.org 的说明，Privacy Badger 用算法判断追踪器，多数阻止工具则依赖人工维护的域名列表。它观察第三方域名有没有使用能唯一识别浏览器的 cookie、存在本地存储空间的「超级 cookie」与画布指纹（canvas fingerprinting，用浏览器绘图的细微差异识别设备）。同一个第三方域名在三个不同的网站上追踪用户，就会被挡下。广告没有追踪用户时，Privacy Badger 不会挡。

Privacy Badger 也用列表，默认会定期从 EFF 的训练项目 Badger Sett 获取 Badger Sett 在数千个热门网站上找到的追踪器数据。另有一份黄名单，收录网站运作需要的第三方域名。Privacy Badger 会加载这些域名的内容，只挡掉第三方 cookie 与 referrer。说明页把黄名单写成对实用性的妥协，长期希望不再需要黄名单。

依 Apple 的说明页，Safari 会删除用户没有直接访问并互动过的第三方网站的 cookie 与网站数据。Safari 也会向网站呈现简化过的系统设置，让每台 Mac 看起来更相似，降低追踪者识别设备的能力。依 EFF 的公告，Privacy Badger 单独使用就有效。跟广告拦截器或 Safari 高级设置里应用到所有窗口的追踪防护一起用时，它也能挡下不在其他工具列表里、或其他工具选择不挡的追踪器。

依 privacybadger.org 的说明，GPC 的用意是在有适用隐私法的地方，对所有公司都具法律效力。公告列出的州都在美国。本文推论，其他地方的网站可能不理会这个信号。说明页也提到，Privacy Badger 会一并发出 Do Not Track 信号（请网站不要追踪用户的浏览器信号），域名收到两种信号之后仍收集唯一标识符才会被挡下。

安装时浏览器会警告扩展可以访问所有网站的数据，privacybadger.org 写明除非用户提交网站故障报告，否则不会共享浏览数据。Mac App Store 页面的隐私标示写「不收集数据」，这项信息由开发者提供，Apple 没有验证。新闻自由组织 Freedom of the Press Foundation 介绍 Safari 版时也提醒，只安装可信任的扩展。除了权限，网站也可能无法正常运作，EFF 的公告提到这时可以只对那个网站停用 Privacy Badger。

在中国大陆，GreatFire 对 `www.eff.org` 的判定是访问不稳定，最近 61 次有结论的测试中有 23% 受到干扰（最后一次在 10 月 12 日）。`privacybadger.org` 5 月 31 日最后一次测试时可以连接，之后没有新的测试。依 iTunes 查询接口（API），中国大陆的 Mac App Store 店面查得到这个 App，没有用大陆账号实际打开商店页。privacybadger.org 的简体中文说明页名称是「隐私獾」，扩展界面也有简体中文。

用 Mac 版 Safari、想减少跨网站追踪的人，第一步先确认 Safari 已更新到 26.5 以上、系统是 macOS 15.7.7 以上，再从 Mac App Store 安装并照 Apple 的说明在 Safari 启用。Privacy Badger 挡的是第三方追踪器，直接访问的网站自己收集的数据不在范围内（例如直接访问 YouTube 时，YouTube 自己的追踪与广告都不会被挡），iPhone 与 iPad 上的浏览也还无法保护。
