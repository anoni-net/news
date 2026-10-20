---
title: ChatGPT 广告的客户名单比对与对话内容
description: ChatGPT 的广告主可以上传电子邮件、电话号码或手机广告识别码的名单，让广告只出现在名单上的用户面前。广告只显示给 Free 与 Go 方案，台湾 9 月 23 日起陆续推出。依 OpenAI 到 10 月 20 日的帮助页，关闭广告个性化之后，ChatGPT 仍会依当前的对话内容挑选广告。
date: 2026-10-22T00:00:00+08:00
slug: chatgpt-ads-customer-lists
categories:
  - tracking
follows:
  - 2026-09-26-chatgpt-ad-pixel-identifier
sources:
  - title: Set up Custom Audiences for your Campaign
    url: https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign
    publisher: OpenAI
  - title: ChatGPT 中的廣告
    url: https://help.openai.com/zh-hant/articles/20001047-ads-in-chatgpt
    publisher: OpenAI
  - title: Ads in ChatGPT
    url: https://help.openai.com/en/articles/20001047-ads-in-chatgpt
    publisher: OpenAI
  - title: Ad Tools Terms
    url: https://openai.com/policies/ad-tools-terms/
    publisher: OpenAI
    date: 2026-08-24
  - title: Privacy policy
    url: https://openai.com/policies/privacy-policy/
    publisher: OpenAI
    date: 2026-07-30
  - title: ChatGPT Ads expands to Southeast Asia and Taiwan
    url: https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
    publisher: OpenAI
    date: 2026-09-23
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: Supported countries and territories
    url: https://developers.openai.com/api/docs/supported-countries
    publisher: OpenAI
  - title: How ChatGPT Targets Ads To You Based On Your Prompts, Phone Number, and Email
    url: https://www.404media.co/how-chatgpt-targets-ads-to-you-based-on-your-prompts-phone-number-and-email/
    publisher: 404 Media
    date: 2026-10-15
  - title: Here's How ChatGPT Is Targeting You With Ads
    url: https://gizmodo.com/heres-how-chatgpt-is-targeting-you-with-ads-2000826457
    publisher: Gizmodo
    date: 2026-10-16
  - title: About customer list custom audiences
    url: https://www.facebook.com/business/help/341425252616329
    publisher: Meta
  - title: How Google uses Customer Match data
    url: https://support.google.com/google-ads/answer/6334160
    publisher: Google
authors:
  - anoni-net
---

404 Media 10 月 15 日报道，ChatGPT 的广告主可以上传电子邮件、电话号码或手机广告识别码的名单，让广告只出现在名单上的用户面前。OpenAI 面向广告主的帮助页也列出这项功能，名称是自定义受众（Custom Audiences）。ChatGPT 的广告只显示给 Free 与较低价的付费方案 Go，台湾 9 月 23 日起陆续推出，Plus、Pro、Business 等方案没有广告。依 OpenAI 到 10 月 20 日的用户帮助页，关闭广告个性化之后，ChatGPT 仍会依当前的对话内容挑选广告。

根据自定义受众的帮助页，名单可以是电子邮件、电话号码、两者的 SHA-256 哈希值，或 Google 广告 ID（GAID，Android 手机上的广告识别码）。哈希是把数据转成固定长度字符串的单向运算。上传时也可以用没有哈希的原始数据，上传的文件通常在 24 小时内删除。OpenAI 把名单跟 ChatGPT 的用户比对，比对到的人才算进受众。

名单可以用来只对受众投放、排除受众，或提高、降低对受众的出价（广告主愿意为一次曝光或点击支付的价格）。只对受众投放与调整出价时，比对到的用户至少要 25,000 人，排除用的名单可以少于 25,000 人。广告管理工具也不会显示比对到哪些人。

依 Gizmodo 转述 404 Media 的报道，404 Media 自己在 ChatGPT 投放了两组广告活动测试这套系统。依同一篇转述，OpenAI 收到没有哈希的原始数据后会不会再哈希，并不清楚。404 Media 的报道有付费墙，付费墙之前公开的只有开头两段，其余细节依 Gizmodo 的转述。

依 OpenAI 的用户帮助页，OpenAI 不会把用户的对话、记忆、姓名、电子邮件、精确位置与 IP 地址交给广告主，广告主只会收到观看与点击次数这类汇总的效果数据。用户通过广告给广告主发消息时，广告主看得到那些消息。个人健康、心理健康与政治等敏感话题的对话附近不放广告，被判断为未满 18 岁的账号与临时对话也不显示广告。

## 导读观点 {#perspective}

用客户名单投放广告在业界很常见，Google 的 Customer Match 与 Meta 的客户名单自定义受众都是同类功能。依 Meta 的帮助页，Meta 会先哈希名单再比对，Google 的帮助页则写 Google 不接收实际的电子邮件地址。OpenAI 的帮助页列出的上传格式包含没有哈希的原始数据。404 Media 的报道也提到，ChatGPT 的广告还会依用户输入的提示词挑选。

依 OpenAI 面向广告主的 Ad Tools Terms（广告工具条款），名单只能是广告主自己收集的第一方数据，不得取自数据经纪商（收集并转售个人数据的商家）。广告主要保证已依规定告知当事人，并取得必要的同意或其他法律依据，条款没有写 OpenAI 如何核实。到 10 月 20 日，用户帮助页没有提到能不能查自己在哪些广告主的名单里。广告菜单里有「About this ad」可以了解为什么看到某则广告，帮助页没有提到它会不会显示客户名单。

9 月 26 日那篇导读写的是像素（广告主装在自己网站上的追踪代码），它会把其他网站的浏览数据发回 OpenAI。OpenAI 的隐私政策（EEA、英国与瑞士以外的版本）提到，OpenAI 可能从广告主收到用户在广告主那里的购买记录这类信息，用来显示更相关的广告。

到 10 月 20 日，中国大陆、香港与澳门不在 OpenAI 列出的 ChatGPT 支持国家和地区清单内，API 的支持清单同样没有列出。依 ChatGPT 的清单页，在清单以外的地方使用可能导致账号被封锁或停用。ChatGPT 广告 9 月 23 日起在印尼、马来西亚、菲律宾、新加坡、泰国、越南与台湾陆续推出，在这之前亚太地区已在澳大利亚、新西兰、日本、韩国与印度推出。下面的设置写给在广告已推出的地方使用 Free 或 Go 方案的人。

用 Free 或 Go 方案的人，可以到 ChatGPT 的「Settings」、「Ad Controls」关闭「Personalize ads」，也可以关闭「Past chats and memory」这个只影响广告的开关（选项名称照英文版帮助页）。同一处也可以删除广告数据，最多 30 天后从服务器移除。帮助页提到手机 App 看不到这个选项时，要先更新到最新版。关闭个性化不会移除广告，系统仍会依当前的对话挑选广告。

不想看到广告的人可以改用 Plus 或 Pro，Free 方案也有无广告的选项，帮助页提到供应情况可能因地区和时间而不同。无广告选项的代价是每天能发的消息较少，也不能使用图片生成等工具，Go 方案的用户要先切回 Free 才能使用。帮助中心有简体中文版，切换步骤以英文版的「Change plan to go ad-free」为准。依帮助页「Temporary Chats will not show ads」，本文推论不想让某段对话影响广告的人可以改用临时对话。

名单可以包含电子邮件、电话号码与 GAID，OpenAI 没有说明比对时用的是账号的哪些数据。若比对的是账号登记的邮箱与电话（本文的推论），跟购物、会员用的不同时，名单可能比对不到。OpenAI 之后会不会说明收到原始数据后如何处理、关闭个性化是否也排除名单比对，是接下来可以留意的地方。
