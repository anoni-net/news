---
title: 医疗预约网站把就诊信息发给社交平台的追踪代码
description: The Markup 与巴西媒体 Agência Pública 发现，医疗预约平台 Doctoralia 在拉丁美洲的网站，把医生专科、姓名与预约时间发给 Google、TikTok 与 LinkedIn。
date: 2026-10-04T07:00:00+08:00
slug: doctoralia-health-tracking-pixels
sources:
  - title: How TikTok and Google ended up with information about doctors’ appointments around the world
    url: https://themarkup.org/pixel-hunt/2026/09/14/how-tiktok-and-google-ended-up-with-information-about-doctors-appointments-around-the-world
    publisher: The Markup
    date: 2026-09-14
  - title: This is how you stop data trackers from sucking up your health data
    url: https://themarkup.org/the-breakdown/2025/06/17/this-is-how-you-stop-data-trackers-from-sucking-up-your-health-data
    publisher: The Markup
    date: 2025-06-17
  - title: Blacklight
    url: https://themarkup.org/blacklight
    publisher: The Markup
  - title: 個人資料保護法 第 6 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6
    publisher: 全國法規資料庫
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 全国人民代表大会
    date: 2021-08-20
authors:
  - anoni-net
---

美国媒体 The Markup 与巴西媒体 Agência Pública 在 9 月 14 日发表调查，医疗预约平台 Doctoralia 在巴西、哥伦比亚、墨西哥等地的网站，把用户预约就诊的信息发给 Google、TikTok 与 LinkedIn 等科技公司，用于广告。Doctoralia 的母公司 Docplanner 在 13 个国家运营，这次报道的是拉丁美洲的网站。

在巴西，搜索妇产科医生时，网站把搜索的专科发给 Google。完成预约后，医生姓名、预约日期与时间也一并发出。在哥伦比亚与墨西哥，预约皮肤科或心理咨询师时，医生姓名与预约时间发到了 LinkedIn 与 TikTok。

追踪在用户输入电子邮件或姓名之前就开始了，追踪代码通常会用唯一的标识符标记用户。西班牙版的网站在测试中没有把搜索发出，德国的网站有弹窗让用户关闭追踪 cookie，拉丁美洲的网站只告知使用了 cookie，没有马上提供关闭的选项。

Docplanner 给媒体的回复是正在进行技术与法律审查。Google 与 LinkedIn 的回复都提到，政策禁止在收集健康信息的页面使用这类工具，TikTok 没有回应。

## 导读观点 {#perspective}

追踪代码是广告平台提供给网站的一段程序，页面加载时就把用户看了什么、点了什么发回平台。医疗网站装上它，搜索的科室、预约的医生本身就透露了健康状况。巴西的主管机关对此看法不一，医师委员会的立场是预约就诊不涉及医疗秘密，主管健康保险的机构则把科室与预约信息视为可能透露健康状况的数据。

在中国大陆，《个人信息保护法》第二十八条把医疗健康信息列为敏感个人信息，第二十九条要求处理敏感个人信息取得个人的单独同意。预约信息是否属于医疗健康信息，法条没有逐项列出。

想知道常用的医疗网站装了哪些追踪代码，可以先用 The Markup 的 Blacklight 输入网址扫描。它检查的项目包括网站是否把用户数据发给 TikTok 与 Google Analytics，代码只开源了一部分。

The Markup 去年针对其他医疗网站的测试，列出几种可以挡下追踪代码的做法：Firefox 把「增强型跟踪保护」从标准调到严格、Safari 开启高级跟踪与指纹保护，或改用 Brave、DuckDuckGo 浏览器，也可以装 Privacy Badger、uBlock Origin Lite 扩展。这些浏览器与扩展都可以免费安装，VPN 与无痕模式则无法挡下，在 Chrome 屏蔽第三方 cookie 也不够。
