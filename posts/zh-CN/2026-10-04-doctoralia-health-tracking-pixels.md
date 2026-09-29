---
title: 医疗预约网站把就诊信息发给社交平台的追踪代码
description: 医疗预约平台 Doctoralia 在巴西、哥伦比亚、墨西哥等地的网站，把就诊专科、医生姓名与预约时间发给 Google、TikTok 与 LinkedIn。它的母公司没有在中国大陆、香港、澳门与台湾运营。
date: 2026-10-04T07:00:00+08:00
slug: doctoralia-health-tracking-pixels
sources:
  - title: How TikTok and Google ended up with information about doctors’ appointments around the world
    url: https://themarkup.org/pixel-hunt/2026/09/14/how-tiktok-and-google-ended-up-with-information-about-doctors-appointments-around-the-world
    publisher: The Markup
    date: 2026-09-14
  - title: Docplanner Group
    url: https://www.docplanner.com/
    publisher: Docplanner
  - title: This is how you stop data trackers from sucking up your health data
    url: https://themarkup.org/the-breakdown/2025/06/17/this-is-how-you-stop-data-trackers-from-sucking-up-your-health-data
    publisher: The Markup
    date: 2025-06-17
  - title: Blacklight
    url: https://themarkup.org/blacklight
    publisher: The Markup
  - title: the-markup/blacklight-collector
    url: https://github.com/the-markup/blacklight-collector
    publisher: GitHub
  - title: 個人資料保護法 第 6 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6
    publisher: 全國法規資料庫
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 全国人民代表大会
    date: 2021-08-20
  - title: Firefox 正體中文介面字串 preferences.ftl
    url: https://github.com/mozilla-l10n/firefox-l10n/blob/main/zh-TW/browser/browser/preferences/preferences.ftl
    publisher: Mozilla
  - title: Firefox 简体中文界面字符串 preferences.ftl
    url: https://github.com/mozilla-l10n/firefox-l10n/blob/main/zh-CN/browser/browser/preferences/preferences.ftl
    publisher: Mozilla
  - title: 在 Mac 上的 Safari 中進行私密瀏覽
    url: https://support.apple.com/zh-tw/guide/safari/ibrw1069/mac
    publisher: Apple
  - title: 在 Mac 上的 Safari 浏览器中无痕浏览
    url: https://support.apple.com/zh-cn/guide/safari/ibrw1069/mac
    publisher: Apple
  - title: Is https://themarkup.org blocked in mainland China?
    url: https://en.greatfire.org/https/themarkup.org
    publisher: GreatFire
  - title: Is https://duckduckgo.com blocked in mainland China?
    url: https://en.greatfire.org/https/duckduckgo.com
    publisher: GreatFire
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: Is https://chromewebstore.google.com blocked in mainland China?
    url: https://en.greatfire.org/https/chromewebstore.google.com
    publisher: GreatFire
  - title: Is https://addons.mozilla.org blocked in mainland China?
    url: https://en.greatfire.org/https/addons.mozilla.org
    publisher: GreatFire
regions:
  - BR
  - CO
  - MX
authors:
  - anoni-net
---

根据美国媒体 The Markup 与巴西媒体 Agência Pública 在 9 月 14 日发表的调查，医疗预约平台 Doctoralia 在巴西、哥伦比亚、墨西哥等地的网站，把预约信息发给 Google、TikTok 与 LinkedIn 投放广告。母公司 Docplanner 在欧洲、土耳其与拉丁美洲共 13 个国家运营，不包括中国大陆、香港、澳门与台湾。

巴西的网站把搜索的妇产科发给 Google，预约后再发出医生姓名与预约时间。哥伦比亚的网站把各专科的医生姓名与预约时间发给 LinkedIn，哥伦比亚与墨西哥的预约也发到 TikTok。追踪在输入姓名或电子邮件之前就开始。

西班牙版网站在测试中没有把搜索内容发给外部公司，Doctoralia 的总部在西班牙，适用欧盟的 GDPR（《通用数据保护条例》）。Docplanner 在德国的同类网站让用户关闭追踪 cookie，拉丁美洲的网站只告知使用 cookie，没有立即提供关闭选项。

Docplanner 的声明写明追踪代码用来监测自家的社媒广告、不出售个人数据，公司到 9 月 14 日报道刊出时正在进行技术与法律审查。LinkedIn 的回复写明政策禁止在收集敏感数据的页面安装追踪代码，Google 的回复写明禁止收集私人健康信息，TikTok 没有回应。

## 导读观点 {#perspective}

追踪代码是广告平台给网站的程序，由浏览器把用户的浏览与点击发回平台，经常附上唯一标识符。按社交平台的说法，标识符可以关联到平台账号。装在医疗网站上时，发出的科室与医生可能透露健康状况。

巴西负责医师执照的联邦医学委员会认为预约不涉及医疗保密义务，监管私营健保的国家补充医疗保健局则认为预约信息可能透露健康状况。中国大陆《个人信息保护法》第二十八条把医疗健康信息列为敏感个人信息，第二十九条要求处理时取得单独同意。台湾《个人资料保护法》第 6 条原则上禁止收集、处理或利用病历、医疗与健康检查资料，两地条文都没有写明预约信息是否属于此类。

想知道医疗网站是否把数据发给 TikTok 或 Google Analytics，可以到 The Markup 的 Blacklight 输入网址扫描，GreatFire 6 月 12 日测得 `themarkup.org` 可从中国大陆连接。一次约 30 秒到一分钟，界面只有英文，预约过程中才发出的数据可能看不到。部分代码以 GPL-3.0 许可证开源，6 月有新版发布。

依 The Markup 2025 年 6 月发表的测试，调高 Firefox 与 Safari 的内置设置、改用 Brave 或 DuckDuckGo 浏览器、安装 Privacy Badger 或 uBlock Origin Lite 扩展，都能挡下美国州政府医疗保险交易网站上的 LinkedIn、Snapchat 与 Google 追踪代码。扩展测试的是桌面浏览器，TikTok 不在测试范围，VPN 与无痕模式挡不住。据 GreatFire 截至 9 月 29 日的记录，`duckduckgo.com`、`brave.com` 与 Chrome 网上应用店在中国大陆全部或大多被封锁，`addons.mozilla.org` 连接不稳定。

在中国大陆，第一步可以在桌面版 Firefox 设置的「隐私与安全」把「增强型跟踪保护」改成「严格」，在 Mac 的 Safari「高级」设置里则可把「使用高级跟踪和指纹记录保护」用于所有浏览。两项内置设置都不依赖境外商店，也不需要账号，界面有简体中文。代价是某些网站可能出现异常。
