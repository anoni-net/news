---
title: 家用 Android 电视盒的预装后门与住宅代理
description: 家中有 Android 电视盒的人可能受影响。Google 11 月初公布瓦解预装在超过 130 万台机顶盒的 XCPE 后门，设备被用来转送他人流量，通过认证的机型也在内。到 11 月 8 日为止，Google 没有提供已出货设备的清除步骤，换机与新加坡警方的处理建议并不相同。
date: 2026-11-13T00:00:00+08:00
slug: android-tv-residential-proxy
categories:
  - security
sources:
  - title: Shutting the Door on the XCPE Botnet
    url: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/
    publisher: Google Threat Intelligence Group
    date: 2026-11-02
  - title: Check & fix Play Protect certification status
    url: https://support.google.com/android/answer/10248227
    publisher: Google
  - title: Certified - Partners | Android
    url: https://www.android.com/certified/partners/
    publisher: Google
  - title: The Internals of a Badbox Operation
    url: https://github.com/synthient/public-research/blob/main/2026/11/Videostrong/README.md
    publisher: Synthient
  - title: Google dismantles botnet secretly running on 1.3 million Android TV boxes
    url: https://arstechnica.com/google/2026/11/google-dismantles-botnet-secretly-running-on-1-3-million-android-tv-boxes/
    publisher: Ars Technica
    date: 2026-11-03
  - title: Google Takes Down Massive Android Botnet Infecting 1.3 Million Devices
    url: https://www.channelnews.com.au/google-takes-down-massive-android-botnet-infecting-1-3-million-devices/
    publisher: ChannelNews
    date: 2026-11-03
  - title: Google dismantles massive botnet hidden in Android TV boxes
    url: https://therecord.media/google-dismantles-botnet-hidden-android-tv-boxes
    publisher: The Record
    date: 2026-11-03
  - title: Cops bust botnet of 1.3M infected Android TV boxes
    url: https://www.theregister.com/a/5307045
    publisher: The Register
    date: 2026-11-02
  - title: TrendAI helps disrupt X.CPE botnet in 1.3m devices
    url: https://itbrief.com.au/story/trendai-helps-disrupt-x-cpe-botnet-in-1-3m-devices
    publisher: IT Brief Australia
    date: 2026-11-05
  - title: Advisory On The Dangers Of Non-Certified Streaming Devices
    url: https://www.police.gov.sg/media-hub/news/2025/11/20251112_advisory_on_the_dangers_of_non_certified_streaming_devices
    publisher: Singapore Police Force
    date: 2025-11-12
  - title: 广电总局加强整顿OTT盒子 乐视网/优酷/PPTV/腾讯视频TV版下架
    url: https://www.qianzhan.com/indynews/detail/150/140902-2620ee3a.html
    publisher: 前瞻网
    date: 2014-09-02
  - title: Is https://play.google.com blocked in mainland China?
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
authors:
  - anoni-net
---

家中的对外连接可能正经由插在电视上的 Android 电视盒被转租给陌生人。Google 威胁情报团队（GTIG）11 月初公布，Google 与业界伙伴在前一周瓦解 XCPE 僵尸网络（botnet，受同一方远程控制的大量设备），超过 130 万台机顶盒被 XCPE 后门纳入其中。受害设备绝大多数是 Android 电视盒，也有远程医疗设备、卡拉 OK 机与数字标牌，分布遍及全球。家中有 Android 电视盒（尤其是来源不明的机型）的读者可以先对照机型名单与认证状态，两者都无法单独确认是否受害。

住宅代理（residential proxy）把付费客户的流量转经普通家庭的网络送出去，目的地记录到的来源是那个家庭的 IP。依 GTIG 的分析，XCPE 加载的模块最常见的用途是住宅代理与带宽共享，另外也有广告欺诈模块。一台设备最多同时装了三种代理用的软件开发工具包（SDK）。设备的主人既不知情，也没有同意。

依 IT Brief 对安全厂商 TrendAI 分析的报道，恶意流量经由普通家庭与办公室的 IP 送出，攻击者访问在线服务时就像当地的用户。这些流量来自真实的家庭连接，可以绕过银行、零售商用来验证用户的 IP 信誉与地理位置检查。家中 IP 因此被封锁或被追查的实例与法律责任，到 11 月 8 日为止查到的官方文件没有写。

依 GTIG 的说明，后门本体是软件包 `x.cpe`（部分版本名为 `com.oemservice`），以系统权限预装在固件里。用户卸载之后，重新开机就会从 `/oem/` 分区装回来。它会清除设备上的用户同意设置，关闭 Google Play Protect（Android 内置的恶意 App 防护）的 App 验证，接着静默下载并执行其他文件。GTIG 在多个品牌与机型的固件里都找到同一套后门，时间跨越多年。

GTIG 也记录到运营者截取设备的实时画面、注入按键、外传账号与设备信息，以及开启远程命令行，指令清单里还有探测所在网络的功能。同一份报告也提到，与受害设备的交互绝大部分是安装、移除与设置模块。

依 GTIG 的高度信心评估，Android 设备代工厂 Videostrong 为了牟利蓄意开发、部署并运营 XCPE 后门与僵尸网络，再把访问权卖给犯罪的附属团伙。到报道刊出时，Videostrong 没有回复 The Record 与 The Register 的询问。依 Ars Technica 的报道，受害机型包含通过 Google 认证的机型。GTIG 的解释是 Videostrong 用混淆手法钻了测试的漏洞，在设备首次开机之后才加载恶意代码。

130 万台是 GTIG 对 XCPE 后门本身的数字。GTIG 另外估计，取下附属团伙模块的指挥控制（C2，远程下达指令的服务器）域名，会再切断至少 1000 万台受感染设备的访问。附属团伙在 XCPE 之外还有别的传播渠道，所以 1000 万台算在 130 万台之外。依 The Record 的报道，其中许多不是 Android 设备。

Google 的处置包括以法律行动取下 Videostrong 与十几个恶意程序家族使用的域名，也禁止 Videostrong 及其未来的子公司、关联公司制造销售认证的 Android 设备，或向认证厂商供应软件。Google 也写到正在改进认证 Android TV 设备的固件完整性检查。到 11 月 8 日为止，GTIG 的报告与查到的其他官方说明都没有提供已出货设备的清除步骤，也没有写是否撤销受害机型的认证。依 The Record 的报道，Google 也没有说明是否通知用户或强制清除。

## 导读观点 {#perspective}

要查认证状态，可以打开 Google Play 商店的个人资料菜单，再进入“设置”的“关于”。本文没有在电视盒上实测，界面可能与说明页不同。依说明页，未认证的设备可能不安全，设备认证与防护恶意 App 的 Play Protect 是两件事。显示已认证也无法排除问题，XCPE 的受害机型包含认证机型，恶意代码在首次开机之后才加载。

GTIG 的合作单位 Synthient 公开了 182 个在这起事件观察到的机型名称，清单的说明写到，单凭机型名称不足以确认设备已遭入侵。Ars Technica 建议买过 MECOOL 或来源不明白牌电视盒的人对照这份清单。GTIG 的报告没有列出用户可以看到的迹象，IT Brief 的报道也提到盒子可能看起来一切正常。到 11 月 8 日为止查到的资料里，没有普通用户可以确认家中 IP 是否正被出租的方法。

ChannelNews 转述的研究人员（报道没有写是哪一家）建议把确认感染的设备断网后换掉，因为 `x.cpe` 嵌在系统固件里，杀毒软件与出厂重置可能无法永久清除。代价是要另外花钱买新机，要先确认感染也不容易。要换机时，GTIG 建议向信誉良好的制造商购买，并指向 Android TV 网站的合作伙伴名单。链接到的认证伙伴页页首写的是手机与平板，电视盒是否完整列入，到 11 月 8 日为止本文没有查到。

新加坡警方与网络安全局 2025 年 11 月的提醒早于 GTIG 这次公布（到 11 月 8 日为止，没有查到台湾 TWCERT/CC 与香港 HKCERT 针对 XCPE 的公告），对象是未认证的电视盒，建议立即断网、扫描并移除可疑 App、检查银行等账户。发现恶意程序或未授权交易时要向新加坡警方报案，报案前不要重置，以免妨碍调查。该提醒也写到，没有发现恶意程序与未授权交易时可以继续使用或完整重置，但它不是针对 XCPE 的建议。GTIG 写明用户无法移除 `x.cpe`，ChannelNews 也写杀毒软件与出厂重置可能无法永久清除，本文推论扫描没有发现异常不代表 `x.cpe` 不在。

依 The Record 的报道，GTIG 反制业务的主管被问到如何移除恶意程序时表示，取下域名实际上让恶意程序不再造成危害（“effectively rendering the malware benign”）。依 Ars Technica 的评估，设备应该可以安全使用，但 Play Protect 仍然关闭、失效的模块还装在系统里。GTIG 的报告提到运营者被打断后会很快换用新的加载程序或其他变现 SDK。ChannelNews 转述的研究人员也警告，犯罪者可能另建替代系统，受感染的设备仍可能再遭利用。

家中 IP 也可能经由自己安装的 App 被出租，GTIG 呼吁对“用闲置带宽换钱”、“分享网络”的 App 格外小心，报告把它们列为非法代理网络扩张的主要渠道。依 GTIG 的分析，代理服务商通常只在平台政策要求时才征求同意，到 11 月 8 日为止查到的资料里没有报告列出的代理服务商的回应。

到 11 月 8 日为止，查不到中国国家广电总局、工信部、公安部或 CNCERT 针对预装恶意程序的电视盒发布的通报。较早的监管背景只有二手来源。依前瞻网 2014 年 9 月的报道，广电总局要求牌照方关闭违规视频应用的下载通道、未经批准的终端产品不得销售，针对的是内容与牌照。Videostrong 是深圳的公司（The Register 引述 Google），中国主管机关对 Google 的指控有无回应，同样查不到。

上文查认证状态的路径经过 Google Play 商店。GreatFire 的第三方测量量的是网址能否连接，到 11 月 1 日的最后一次测试，`https://play.google.com` 在中国大陆 100% 被封锁。中国大陆销售的电视盒是否另有认证查询方式，本文没有查到，不推测。

电视盒机型在名单上、来源不明或显示未认证的人，第一步是中断它的网络连接（换机与新加坡的两种建议都从断网开始），只需要几分钟。依新加坡的提醒，认为账号可能遭入侵时要立即更改密码并启用多因素验证，本文建议改用其他设备操作。GTIG 建议确认 Play Protect 已启用，暂时留着设备的人可以检查。依 Ars Technica 的报道，后门会关闭 Play Protect，来源没有写手动开启之后是否会再次被关闭。

暂时还要使用的人可以把电视盒接到路由器的访客网络，与手机、电脑分开，也要确认访客网络有隔离局域网设备。ChannelNews 的报道写到攻击者可以探查同一家用网络上的其他设备，访客网络是本文由此做的推论。来源只提到企业的隔离，没有评估家用访客网络，访客网络也挡不住运营者在盒子上截取画面、外传账号信息与转送流量。断网可以停止转送流量，但收不回可能已经外传的账号信息，换新机则要付出购机费用。
