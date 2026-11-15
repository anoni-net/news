---
title: Facebook 照片里的 FBMD 标识符与 Brave 桌面版的移除功能
description: Brave 桌面版从 1.98 起，保存或上传图片时自动移除 Meta 加在 Facebook 照片里的 FBMD 标识符。照片的位置、设备与拍摄时间不在移除范围，到 11 月 15 日为止 Android 与 iOS 版也还没有。
date: 2026-11-21T00:00:00+08:00
slug: brave-photo-metadata
categories: [tracking]
sources:
  - title: Brave removes tracking metadata from Instagram and Facebook photos
    url: https://brave.com/privacy-updates/40-remove-tracking-metadata/
    publisher: Brave
    date: 2026-11-12
  - title: Release Channel 1.98.60
    url: https://community.brave.app/t/release-channel-1-98-60/660299
    publisher: Brave
    date: 2026-10-27
  - title: Strip metadata from images on download/upload
    url: https://github.com/brave/brave-browser/issues/5238
    publisher: GitHub
    date: 2019-07-14
  - title: "IPTC investigates: what does Facebook do with your photo metadata?"
    url: https://iptc.org/news/what-does-facebook-do-with-your-photo-metadata/
    publisher: IPTC
    date: 2019-07-22
  - title: Social Media Sites Photo Metadata Test Results 2019
    url: https://iptc.org/standards/photo-metadata/social-media-sites-photo-metadata-test-results-2019/
    publisher: IPTC
  - title: Automatically delete personal EXIF data from images when uploading
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=743152
    publisher: Mozilla
    date: 2012-04-06
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: Is https://laptop-updates.brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/laptop-updates.brave.com
    publisher: GreatFire
  - title: iTunes lookup API (cn)
    url: https://itunes.apple.com/lookup?id=1052879175&country=cn
    publisher: Apple
  - title: iTunes lookup API (tw)
    url: https://itunes.apple.com/lookup?id=1052879175&country=tw
    publisher: Apple
authors:
  - anoni-net
---

Brave 11 月 12 日公布，桌面版从 1.98 起，保存或上传图片时会自动移除 Meta 加在 Facebook 照片里的 `FBMD` 标识符。用 Brave 桌面版的人更新之后就有这项保护，Android 与 iOS 版到 11 月 15 日为止还没有，公告写的是计划推出。照片的位置、设备型号与拍摄时间不在这次的移除范围。

依 Brave 的公告，Meta 把标识符存在国际新闻电信委员会（IPTC）定义的照片元数据（附在文件里、平常看不到的数据）里。IPTC 为新闻业制定标准，摄影师与出版者用它的格式在图片里附上图说、作者与版权信息。

IPTC 过去测试 Facebook 如何处理上传的照片时，发现 Facebook 删掉大部分原有的元数据。Facebook 另外在“Special Instructions”字段加上一串以 `FBMD` 开头的长字符串。另一个人下载同一张照片再上传，这串值维持不变。Brave 在 7 月重做同样的测试，标识符仍然在。

公告假设有人用另一个名字经营 Instagram 账号，跟家人与同事认识的 Facebook 实名账号分开。他替两个账号各用不同的电子邮件别名，也许还用了 VPN 隐藏 IP 地址。他下载朋友在 Facebook 贴出的投票呼吁图片、发到自己的 Instagram 之后，标识符跟着文件一起过去，Meta 就可能用它把 Instagram 账号连到朋友的帖子与周围的实名人际关系。连结一旦存在，Meta 可能向 Facebook 上认识他的人推荐那个 Instagram 账号，这笔连结也可能外泄或因法律请求而交出。

Brave 的公告提到，Meta 没有公开标识符的用途，也没有说明为何把它加在图片的元数据里。Brave 也写到 Meta 可能没有拿它来追踪，但在没有公开信息时，Brave 会把各种可能与对隐私的影响都纳入考量。到 11 月 15 日为止，本文查不到 Meta 对这个标识符或对 Brave 公告的说明，也查不到 2019 年 IPTC 之后、Brave 以外的重新测试。

保存图片时，Brave 在下载完成前拿掉标识符，之后改用其他浏览器或 App 上传也不会带着它。上传图片到网站时，Brave 送出的是移除后的副本，电脑里的原始文件不变。功能列在 10 月 27 日的 1.98.60 版本说明里，对应的需求 2019 年就开在 Brave 的 GitHub 上。

Brave 公告的标题与第一段把 Instagram 与 Facebook 并列，但文中的测试与演示步骤都用 Facebook 的照片。到 11 月 15 日为止，本文找不到 Instagram 照片也带着 `FBMD` 的独立测试。IPTC 2019 年的社交网站测试表在 Instagram 一列只写网站不提供另存或下载，也没有显示嵌入的元数据。

## 导读观点 {#perspective}

IPTC 2016 与 2019 年的测试都发现两个字段的值跟上传的不同，IPTC 推测是 Facebook 填入的。Job Id 字段每上传一次就换一个值，“Special Instructions”字段的 `FBMD` 则在别人重新上传时保持不变。IPTC 写明不对这些值的用途做任何假设，2019 年时也找不到 Facebook 的规格或声明。Brave 的公告只处理 `FBMD`、没有提到 Job Id，写的效果是让 Meta 更难跨账号与网站连结同一张照片，没有写能完全阻止。

照片的其他元数据有正当用途，例如相册 App 依日期与地点整理照片。Brave 把移除位置、设备与日期时间列为之后想加的功能，并写到会让用户决定何时移除。

Brave 拿 Chrome 当没有这项保护的对照。2012 年有人在 Firefox 的问题跟踪系统提出上传时自动删除 EXIF（相机写进照片的拍摄信息）的请求，到 11 月 15 日为止状态是不修复（WONTFIX）。该请求针对的是 EXIF，跟 `FBMD` 所在的 IPTC 字段分属不同格式。

用 Brave 桌面版的人更新到 1.98 以上即可，公告没有提到需要另外开启或设置。Brave 的公告附了确认的步骤，先用 Chrome 这类浏览器从 `facebook.com` 另存一张照片，再用在浏览器里运行的 image metadata viewer 打开。“Special Instructions”字段会出现 `FBMD` 开头的值。改在 Brave 里用同一个查看网站选取该文件，`FBMD` 的值就不见了。

对在中国大陆或海外使用简体中文的读者，GreatFire 到 10 月 18 日的最后一次测试显示 `brave.com` 在中国大陆 100% 被封锁，自 2017 年 5 月 13 日起就有干扰纪录。下载与更新用的 `laptop-updates.brave.com` 最近一次有效测试同样被封锁。Apple 的 iTunes 查询接口在 10 月 20 日的回传里，中国大陆区商店查不到 Brave（这不等于 Brave 或 Apple 公告下架），台湾、香港、日本、韩国与新加坡的商店则查得到 iOS 版 1.96。这项功能到 11 月 15 日只在桌面版，这些地区的 iOS 用户暂时用不到。

依保存与上传这两个移除时间点推断，下载与上传都没有经过 Brave 桌面版的文件不在保护范围内，在手机上用 App 保存与分享的照片也一样。
