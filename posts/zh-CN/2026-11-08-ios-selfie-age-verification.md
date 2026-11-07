---
title: iOS 27.2 用自拍估算年龄的成年确认
description: Apple 在 iOS 与 iPadOS 27.2 加入用自拍估算年龄、确认用户已成年的选项，依 Apple 的支持文档只在澳大利亚、巴西、新加坡与英国提供。到 11 月 7 日为止，中国大陆不在 Apple 列出需要确认年龄的地区内。
date: 2026-11-08T00:00:00+08:00
slug: ios-selfie-age-verification
categories: [censorship]
sources:
  - title: Confirm that you're an adult with a selfie
    url: https://support.apple.com/en-us/149095
    publisher: Apple
    date: 2026-10-26
  - title: Region-specific rules for managing an Apple Account
    url: https://support.apple.com/en-us/125666
    publisher: Apple
    date: 2026-10-26
  - title: If you're asked to confirm that you're an adult
    url: https://support.apple.com/en-us/125662
    publisher: Apple
    date: 2026-10-26
  - title: Apple Introduces Selfie Age Verification in iOS 27.2
    url: https://www.privacyguides.org/news/2026/10/29/apple-introduces-selfie-age-verification-in-ios-27-2/
    publisher: Privacy Guides
    date: 2026-10-29
  - title: Age assurance developer Q&A
    url: https://developer.apple.com/support/age-assurance/
    publisher: Apple Developer
  - title: Age requirements for managing an Apple Account in Brazil
    url: https://support.apple.com/en-us/126783
    publisher: Apple
    date: 2026-10-26
  - title: Age requirements for managing an Apple Account in the United States (Texas)
    url: https://support.apple.com/en-us/127462
    publisher: Apple
    date: 2026-06-04
  - title: Next steps for apps distributed in Texas
    url: https://developer.apple.com/news/?id=2ezb6jhj
    publisher: Apple Developer
    date: 2025-11-04
  - title: New Online Safety Code of Practice for App Distribution Services Enhances Protection for Singapore Users
    url: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/online-safety-code-of-practice-for-app-distribution-services
    publisher: IMDA
    date: 2025-01-15
  - title: Factsheet on Age Assurance under the ADS Code
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2025/01/ads-code/factsheet-on-age-assurance.pdf
    publisher: IMDA
    date: 2025-01-15
  - title: Internet Age Gates Are a Growing Global Threat
    url: https://www.eff.org/deeplinks/2026/06/internet-age-gates-are-growing-global-threat
    publisher: EFF
    date: 2026-06-05
  - title: "Face Scans to Estimate Our Age: Harmful and Creepy AF"
    url: https://www.eff.org/deeplinks/2025/01/face-scans-estimate-our-age-creepy-af-and-harmful
    publisher: EFF
    date: 2025-01-23
  - title: 未成年人网络保护条例
    url: https://www.gov.cn/zhengce/content/202310/content_6911288.htm
    publisher: 中华人民共和国国务院
    date: 2023-10-24
  - title: 移动互联网未成年人模式建设指南
    url: https://www.cac.gov.cn/2024-11/15/c_1733364304749288.htm
    publisher: 国家互联网信息办公室
    date: 2024-11-15
  - title: 关于《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》公开征求意见的通知
    url: https://www.cac.gov.cn/2026-09/18/c_1791482017777471.htm
    publisher: 国家互联网信息办公室
    date: 2026-09-18
regions:
  - AU
  - BR
  - SG
  - GB
authors:
  - anoni-net
---

Apple 在 iOS 与 iPadOS 27.2 加入一种新的成年确认方式，用户拍下自己的脸，由年龄估算模型判断是否已满 18 岁。依 Apple 10 月 26 日发布的支持文档，自拍选项只在澳大利亚、巴西、新加坡与英国提供。同一份文档列出的年龄确认要求适用于六个地方的 Apple 账户，另外两处是韩国与美国得克萨斯州，这两地没有自拍选项。到 11 月 7 日为止，中国大陆与其他没有列出的地方都不在清单上，当地的用户不必做年龄确认。

隐私指南网站 Privacy Guides 10 月 29 日的短讯报道了这项功能，文末写到住在澳大利亚、巴西、新加坡、韩国、英国或得克萨斯州的人都要确认年龄，没有区分哪些地方提供自拍。本文的地区范围以 Apple 的支持文档为准，韩国与得克萨斯州的用户只能用其他方式确认。

依 Apple 的说明，年龄确认可能出现在创建新账户、更新系统、更改部分安全设置或下载或购买 18+ 分级 App 的时候，实际情况依所在地区而定。选择自拍时，要把脸放在画面中央，慢慢向四个方向转头拍下脸的各个角度。确认成年之后不必再做一次。

同一份说明提到，自拍会同时交给设备上与 Private Cloud Compute（Apple 的云计算服务，Apple 把它描述成设备的安全与隐私保护在云端的延伸）上的年龄估算模型分析，结果在设备上合并。Apple 写明分析过程中包括 Apple 在内的任何人都无法访问自拍。确认之后自拍会删除，不以任何形式保留。Privacy Guides 的文章写成在设备上「或」在 Private Cloud Compute 执行，Apple 的说明则是两边都执行。

自拍之外，Apple 列出的方式还有本人的信用卡与扫描证件（护照、驾驶证或政府核发的身份证件），借记卡与礼品卡不能用。已有账户的人，Apple 会先检查账户里有没有信用卡或其他符合条件的资料。依 Apple 另一份说明，证件影像由 Apple 与服务供应商用来确认年龄与防范欺诈，短暂保存后删除。

## 导读观点 {#perspective}

年龄估算从脸部影像推测一个人大约几岁，不需要出示证件。Privacy Guides 的文章提到，效果完全取决于估算算法的质量，而且一定会有误判。成年人可能被判成未成年，也可能有相反的情况。到 11 月 7 日为止，本文查不到 Apple 公布的模型名称、误判率或准确度资料，也没有查到独立验证自拍删除与无法访问的报告。

Apple 列出的地方，有几处的法规要求 App 商店确认或提供用户的年龄。新加坡资讯通信媒体发展局（IMDA）依《Code of Practice for Online Safety – App Distribution Services》，要求指定的 App 商店 2026 年 4 月 1 日起至少能判断用户是否未满 18 岁，年龄估算、年龄验证或两者并用由商店自行选择。IMDA 的新闻稿写到，目的是降低用户、尤其是儿童接触有害内容的风险，Code 也要求年龄确认做到数据最小化。

得克萨斯州的 App 商店责任法（App Store Accountability Act，SB 2420）从 6 月 4 日起适用于在得克萨斯州创建的新 Apple 账户。依 EFF 6 月的文章，巴西 2025 年通过的法律要求 App 商店与操作系统替其他服务提供年龄信号，预计 2027 年初全面遵循。

Privacy Guides 的文章逐一比较各种方式，信用卡会交出可识别身份的资料，但下载免费 App 本来就要填付款信息。扫描证件可能让敏感文件落到第三方手上，文中举 Discord 为例，替它处理证件照年龄确认的第三方泄露了约 7 万份证件。自拍做不好同样有风险，替 Roblox 与 ChatGPT 等公司处理年龄验证的 Persona 泄露了自拍数据库。文章的看法是 Apple 的版本在这方面看来好得多，至少比把证件交给第三方好。

数字权利组织 EFF 2025 年 1 月讨论脸部年龄估算的文章早于 Apple 推出自拍确认（本文没有查到 EFF 针对 Apple 这项功能的评论），文中写到脸部扫描对隐私与信息安全带来新的威胁。设计不良的系统可能保存脸部资料，甚至跟用户浏览的内容关联起来。EFF 6 月的文章提到，它对欧洲各项年龄验证倡议的回应一直是，强制年龄验证不是保护年轻人的正确方式。Apple 2025 年 11 月针对得克萨斯州法律的开发者公告也写到，这类法律为了让人下载一个 App 就要求收集敏感个人信息，Apple 担心会损害所有用户的隐私。

依 Apple 给开发者的问答，App 可以通过 Declared Age Range API（App 向系统查询用户年龄区间的接口）获取年龄信息，用户可以决定要不要分享。在法律要求的地方，Apple 会把当地法律定义的年龄类别提供给 App。依巴西的说明页，开发者为遵守当地法律提出要求时一律分享年龄区间。得克萨斯州的说明页则写一律分享，两地的用户都不能关闭。

iOS 26.5 起，用信用卡或证件确认的结果只回传一个不区分方式的 `confirmed` 值，本文没有查到自拍确认之后回传什么。加利福尼亚州的 AB 1043 走另一种做法，要求操作系统在账户设置时询问年龄、把年龄范围提供给 App 而不要求验证。AB 1043 经 AB 1856 修改后 2027 年 1 月 1 日起适用（见[加州 AB 1856 的开源操作系统豁免](https://anoni.net/news/2026/10/california-ab1856-open-source-exemption/)）。

中国大陆不在 Apple 列出的年龄确认地区，也不在提供自拍的地区，说明页只在儿童账户的年龄门槛里列了中国大陆（未满 14 岁）。本文依 Apple 的文档推论，中国大陆的读者可能碰到年龄确认的情况有两种。一是 Apple 账户的地区属于清单上的地方，或在那些地方创建新账户（文档没有写明以账户地区还是所在位置判断）。二是当地之后立法要求 App 商店确认年龄，因为 Apple 的文档写的是依法才适用年龄确认。

中国大陆现行的《未成年人网络保护条例》2024 年 1 月 1 日施行，要求智能终端产品制造者在出厂前安装未成年人网络保护软件或显著告知安装渠道。国家网信办 2024 年 11 月 15 日的《移动互联网未成年人模式建设指南》提出终端要提供设置生日、选择年龄或年龄区间的方式、分发平台要设未成年人专区并标注推荐年龄，属于指引而没有施行日期与罚则。国家网信办 2026 年 9 月 18 日公开征求意见的《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》第十条拟要求终端制造者设置未成年人模式的联动、一键切换与退出核验，尚未施行。三份文件都没有要求用自拍估算年龄，而依 Apple 给开发者的问答，法律没有要求时 App 只有在用户自己选择分享后才能获取年龄区间。

账户在澳大利亚、巴西、新加坡或英国的人被要求确认时，可以比较各种方式留下的资料。已绑定信用卡的账户可能不必另外操作，自拍依 Apple 的说明会送到 Private Cloud Compute 分析后删除，证件影像则由 Apple 与服务供应商短暂保存。到 11 月 7 日为止 Apple 没有公布误判率，自拍无法确认成年时可以重拍，或改用信用卡、证件。不确认也能继续使用设备，代价是不能下载 18+ App，也不能关闭部分安全设置。

中国大陆的读者现在不需要调整任何设置。之后可以留意 Apple 会不会把自拍选项扩大到韩国、得克萨斯州或其他地方，会不会公布估算模型的准确度。另一项是巴西预计 2027 年初全面遵循时，操作系统提供的年龄信号如何实现。
