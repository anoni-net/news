---
title: 荷兰 ASN Bank 的 Wero 付款与 Play Integrity 检查
description: 依用户反馈，荷兰 ASN Bank 的 Android App 1.36.3 版（10 月中更新）起在 GrapheneOS 这类没有 Google 认证的系统上不时拦下 Wero 付款，App 仍可打开、查看账户。到 11 月 8 日本文查不到 ASN 的公告。打算改用 GrapheneOS 的人，可以把它当成银行付款功能改用 Google 检查的例子。
date: 2026-11-10T00:00:00+08:00
slug: asn-bank-grapheneos
categories:
  - finance
regions:
  - NL
sources:
  - title: ASN Bank
    url: https://github.com/PrivSec-dev/banking-apps-compat-report/issues/105
    publisher: GitHub
  - title: SNS Bank (De Volksbank) / ASN / Wero
    url: https://github.com/PrivSec-dev/banking-apps-compat-report/issues/1137
    publisher: GitHub
    date: 2026-10-21
  - title: Sneller bestellen en betalen met iDEAL | Wero
    url: https://www.asnbank.nl/asn-app-en-asn-online-bankieren/veilig-bankierennew/sneller-bestellen-en-betalen-met-ideal-wero.html
    publisher: ASN Bank
  - title: Integrity verdicts | Play Integrity | Android Developers
    url: https://developer.android.com/google/play/integrity/verdicts
    publisher: Android Developers
  - title: Attestation compatibility guide | Articles | GrapheneOS
    url: https://grapheneos.org/articles/attestation-compatibility-guide
    publisher: GrapheneOS
  - title: Usage guide | GrapheneOS
    url: https://grapheneos.org/usage#banking-apps
    publisher: GrapheneOS
  - title: Banking Applications Compatibility with GrapheneOS
    url: https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/
    publisher: PrivSec
    date: 2022-01-26
  - title: IDeal eind 2027 volledig vervangen door nieuw betalingssysteem Wero
    url: https://www.security.nl/posting/883786
    publisher: Security.nl
    date: 2025-04-11
  - title: Learn about devices & services available in your region
    url: https://support.google.com/store/answer/2462844?hl=en
    publisher: Google Store Help
  - title: Is https://releases.grapheneos.org blocked in mainland China?
    url: https://en.greatfire.org/https/releases.grapheneos.org
    publisher: GreatFire
authors:
  - anoni-net
---

依用户在 GitHub 上一个银行 App 兼容性反馈项目的留言，荷兰 ASN Bank 的 Android App 从 10 月中更新的 1.36.3 版起，在 GrapheneOS（以 Android 开源代码为基础的隐私强化手机系统）这类没有经过 Google 认证的系统上不时拦下 Wero 付款。到 11 月 8 日本文查不到 ASN 的公告，说法都来自用户贴出的客服与申诉回信。目前的反馈只涉及 ASN 与同属 de Volksbank 的 SNS Bank，一位 SNS Bank App 用户写 App 仍可打开、查看账户，只是无法用 Wero 付款。荷兰以外的读者不会直接遇到，打算改用 GrapheneOS 的人可以把它当成银行付款功能改用 Google 检查的例子。

iDEAL 是荷兰网购常用的付款方式，依 Security.nl 2025 年 4 月引述 Wero 的运营方 EPI（European Payments Initiative）对荷兰《AD》报的说法，iDEAL 要在 2027 年底前完全由 Wero 取代。Wero 集成在各家银行的 App 里，也有独立的 App。ASN 的说明页写 2026 年起 iDEAL 逐步改成 Wero，网店上会看到“iDEAL | Wero”的名称。

PrivSec 的兼容性名单把 ASN 写成“ASN Bank (De Volksbank)”，反馈的用户也说 ASN 与 SNS Bank 是同一套 App 换了品牌。依用户反馈，被拦时 App 显示的消息用的是“iDEAL | Wero”这个名称，内容是手机或 App 的安装不符合银行的安全要求。同一版也有人付款成功，有人反馈时好时坏。反馈者把新旧两条流程分开描述，一位用户写旧的 iDEAL | Wero 流程可以付款，新的 Wero 流程则过不了 Play Integrity（Google 提供给 App 检查设备与系统的服务）。

依用户贴出的 ASN IT 支持回复，GrapheneOS 不支持 Wero，设备须符合 Wero 的安全要求。多位用户贴出的申诉回信内容几乎相同。信中的理由是 iDEAL | Wero 使用普通操作系统的标准安全检查，替代系统绕过或取代了这些内置防护，所以 iDEAL | Wero 不保证交易安全。回信也写 ASN 正与 iDEAL | Wero 研究未来是否支持替代操作系统，目前无法承诺。

用户也去信 EPI。依用户转贴的回信，EPI 目前集中支持使用最广的移动银行平台与设备。信中也写，此做法可能排除不用移动银行的人，以及偏好 Apple 与 Android 生态系以外系统与设备的人。到 11 月 8 日本文查不到这几封信的公开版本。

## 导读观点 {#perspective}

依 Android 开发者文档，Play Integrity 返回的判定分成几个等级。基本完整性（MEETS_BASIC_INTEGRITY）只要求通过基本的系统完整性检查，bootloader（引导加载程序）可以解锁，设备也可以没有经过认证。设备完整性（MEETS_DEVICE_INTEGRITY）要求 App 在真正且经过认证的 Android 设备（genuine and certified Android device）上运行，Android 13 起还要有硬件证明 bootloader 已锁、加载的是经过认证的制造商镜像。文档里没有出现 GrapheneOS，本文依设备完整性的条件推论，未经 Google 认证的系统拿不到这项判定。

GrapheneOS 的使用说明也写，它通过基本的完整性检查，但没有经过 Google 认证。GrapheneOS 不打算绕过检查，理由是检查一改进就会再失效。

ASN 要求哪一个等级，本文查不到官方资料。一位用 LineageOS（另一套未经认证的 Android 系统）的用户反馈基本完整性通过、设备完整性未通过，只有 Wero 转账不能用（单一案例）。依用户反馈（未经银行证实），Triodos 与 N26 的 App 在 GrapheneOS 上可以用 Wero 付款，bunq 可以设置 Wero。

依用户转贴的内容，EPI 在后来的另一封回信里说明采用 Play Integrity 的理由。信中写 Android 的硬件密钥证明（hardware key attestation）可以验证一组密钥是在 TEE、StrongBox 这类跟普通系统隔开的硬件环境里生成，而且没有离开那里，但验证不了调用的 App 与运行中的操作系统是否完整。Play Integrity 把设备、系统与 App 的信号合在一份有签名的令牌里，由后端服务器验证。信中的结论是硬件密钥证明单独提供不了 EPI 的风险与欺诈模型需要的验证。

GrapheneOS 则在兼容性指南里主张银行改用标准的 Android 硬件证明 API，把 GrapheneOS 公开的官方签名密钥列进允许清单。依指南，这套 API 可以验证硬件、固件、操作系统与 App，生成的密钥证书带有 App 的 ID、签名密钥指纹、版本号与系统的验证启动密钥指纹。指南的评估是硬件证明比 Play Integrity 更强，不必依赖 Google Play 服务与 Google 的服务器，也提到 Play Integrity 最高的强完整性（MEETS_STRONG_INTEGRITY）等级本身就建立在硬件密钥证明上。两边对同一套 API 能验证到哪里的说法不同，本文没有查证哪一方正确。

只有一位用户写旧流程可以付款，其他人的反馈时好时坏，本文推论不宜把它当成稳定的做法。多位用户已经向 ASN 与 EPI 申诉，GrapheneOS 也在指南里鼓励用户写信给 App 开发者并附上指南链接。

在中国大陆境内或在海外使用简体中文的读者，可以先看设备与更新的取得。Google Store 的 Pixel 销售地区清单（以 Pixel 10a 为例，10 月 23 日查证）里，亚洲只有印度、日本、新加坡与台湾，没有中国大陆、香港、澳门与韩国。清单只涵盖 Google Store，购买时收货地址须与所选的 Google Store 地区一致。

GreatFire 的量测显示，`releases.grapheneos.org` 到 10 月 2 日最后一次测试仍在中国大陆受到干扰，近 90 天只有 1 次有结果的测试。本文推论在大陆直连时，系统更新可能无法顺利下载。本文查不到中国对银行 App 在 root 或未经认证系统上运行的公开规范，《移动金融客户端应用软件安全管理规范》（JR/T 0092-2019）的全文没有取得。PrivSec 兼容性名单也收录中国大陆的银行与支付 App，可以先查再决定。

打算改用 GrapheneOS 的人，可以先查常用的银行与支付 App 在 PrivSec 兼容性名单上的状况。名单由社区反馈、GrapheneOS 官方不保证内容，也收录台湾多家银行与支付 App。到 11 月 8 日，名单上 ASN 那一项仍没有附注（名单最后更新在 10 月 20 日，比第一则 Wero 反馈早一天），App 更新之后名单可能还没跟上。

本文的推论是，也可以另外保留一台经过 Google 认证的手机只用来付款，有用户提到自己有备用手机、受到的影响较小。代价是多一台设备要更新与保管，那台手机上的付款仍要通过 Google 的检查。
