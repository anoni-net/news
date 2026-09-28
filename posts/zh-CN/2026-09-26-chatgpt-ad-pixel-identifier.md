---
title: ChatGPT 广告像素的跨站识别码
description: 一份流量分析发现，ChatGPT 的广告系统会设置一个跟账号关联的 cookie，买广告的网站再通过 OpenAI 的像素，把它连同浏览数据发回 OpenAI。目前只在 Android 版 Chrome 观察到。
date: 2026-09-26T01:24:00+08:00
slug: chatgpt-ad-pixel-identifier
sources:
  - title: ChatGPT now knows what you do on other websites via ad collector
    url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
    publisher: Buchodi's Threat Intel
    date: 2026-09-20
  - title: ChatGPT Ads expands to Southeast Asia and Taiwan
    url: https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
    publisher: OpenAI
    date: 2026-09-23
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: 在 Chrome 中刪除、允許使用與管理 Cookie
    url: https://support.google.com/chrome/answer/95647?hl=zh-Hant&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 說明
  - title: 在 Chrome 中删除、允许和管理 Cookie
    url: https://support.google.com/chrome/answer/95647?hl=zh-Hans&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 帮助
authors:
  - anoni-net
---

一位安全研究者分析 ChatGPT 的广告流量，发现使用 ChatGPT 时，OpenAI 的广告收集器 `bzr.openai.com` 会设置一个名为 `__obi` 的 cookie。它跟 ChatGPT 账号关联，有效期一年，而且允许在其他网站的请求中发出。研究者只在 Android 版 Chrome 观察到这个机制，iOS 上的浏览器都会拦截。OpenAI 在 9 月 23 日宣布 ChatGPT 广告开始在七个亚洲市场推出，广告只显示给 Free 与 Go 方案的用户。

在 ChatGPT 投放广告的商家，会在自己的网站装上 OpenAI 的像素。用户之后访问广告主的网站时，像素会把 `__obi` 连同页面数据发回 OpenAI，包括网址路径、表单字段与网页上的文字。电子邮件、电话与姓名经过 SHA-256 哈希，国家、地区、城市与邮政编码则是明文。研究者观察到的网址都去掉了查询字符串，但路径本身有时就透露了病症等敏感信息。

用户在退出登录的状态下同样会被设置 `__obi`。研究者检查的每一个同步令牌，同意类别都标为「分析」。用户只要允许分析，即使拒绝营销也会收到 `__obi`。

研究者在自己的手机上复现，用两种方式抓取流量，另外分析了 936 个广告主像素、超过一千个域名。原文也写明了几项限制：约五分之一的 ChatGPT 会话产生同步令牌，桌面版 Chrome 没有测试。OpenAI 在服务器端把识别码对应回账号，是研究者从设计推论，没有直接观察到。研究者 9 月 14 日去信询问，OpenAI 的客服收到后没有回答提问。

## 导读观点 {#perspective}

OpenAI 公布的支持地区不含中国大陆、香港与澳门。9 月 23 日新增的七个亚洲市场包括新加坡、马来西亚与台湾等地，在当地使用免费或 Go 方案的人会看到广告。

广告主网站上的像素把访问记录发回广告平台，研究者把它比作零售商早已安装的 Meta 与 Google 追踪代码。差别在于 ChatGPT 账号里还有用户跟 AI 的对话，许多人会在对话里提到健康、工作与个人问题，对话内容与其他网站的浏览记录可能因此连到同一个账号。

`__obi` 通过第三方 cookie 在其他网站发出。Safari 默认拦截跨站追踪，iOS 上的浏览器又都使用 Safari 的 WebKit 引擎，所以研究者在 iOS 上都没有观察到。Firefox 默认把第三方 cookie 按网站隔离，Brave 默认屏蔽。

同意横幅的分类由商家自行定义，在这次的案例里，「分析」这个选项也涵盖了广告用途的识别码同步。只拒绝「营销」不足以避开广告追踪。

研究者观察到的情境是在 Android 手机上用 Chrome 登录 ChatGPT，用 iPhone 的人不必另外设置。在海外用 Android 版 Chrome 登录 ChatGPT 的人，可以在 Chrome 的「设置」依次点按「网站设置」、「第三方 Cookie」，选择「阻止第三方 Cookie」，Google 的帮助页面有简体中文的步骤。阻止之后部分网站可能无法正常运行，可以把需要的网站加入例外列表。不想更改 Chrome 设置的人，也可以换一个浏览器专门使用 ChatGPT。
