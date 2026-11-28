---
title: Salon 停刊与 Wayback Machine 里的 25 万篇文章
description: 美国网络媒体 Salon 11 月 5 日宣布停刊，Internet Archive 用 Wayback Machine 近三十年的存档，推出可以按作者与年份查找的实验性界面 Salon Explorer。读者在意的报道，也可以趁还在线上时自行提交存档或保存在自己手上。
date: 2026-11-29T00:05:00+08:00
slug: salon-archive
categories: [press]
regions: [US]
sources:
  - title: Preserving 30 Years of Salon Journalism
    url: https://blog.archive.org/2026/11/12/preserving-30-years-of-salon-journalism/
    publisher: Internet Archive
    date: 2026-11-12
  - title: Goodbye from Salon
    url: https://www.salon.com/2026/11/05/goodbye-from-salon/
    publisher: Salon
    date: 2026-11-05
  - title: Salon.com Article Explorer
    url: https://wayback-labs.sf.archive.org/salon-explorer/
    publisher: Internet Archive
  - title: Save Pages in the Wayback Machine
    url: https://help.archive.org/help/save-pages-in-the-wayback-machine/
    publisher: Internet Archive
  - title: ArchiveWeb.page
    url: https://github.com/webrecorder/archiveweb.page
    publisher: GitHub
  - title: ArchiveBox
    url: https://github.com/ArchiveBox/ArchiveBox
    publisher: GitHub
  - title: Tools & software
    url: https://netpreserve.org/web-archiving/tools-and-software/
    publisher: IIPC
  - title: The WARC Format 1.1
    url: https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/
    publisher: IIPC
  - title: Is http://web.archive.org blocked in mainland China?
    url: https://en.greatfire.org/web.archive.org
    publisher: GreatFire
  - title: Stand News
    url: https://wiki.archiveteam.org/index.php/Stand_News
    publisher: Archive Team
  - title: Hong Kong media
    url: https://wiki.archiveteam.org/index.php/Hong_Kong_media
    publisher: Archive Team
authors:
  - anoni-net
---

美国网络媒体 Salon 在 11 月 5 日宣布停刊，结束 1995 年 11 月创刊以来 31 年的出刊。Internet Archive 一周后在博客发布公告，通过 Wayback Machine 可以找到超过 25 万篇 Salon 的文章，同时推出实验性的查找界面 Salon Explorer。读过、引用过 Salon 报道的人，停刊之后仍有地方找回原文。

Salon 的告别公告写到，独立数字新闻的经营环境多年来改变很大，Salon 自己的出版模式已经无法维持。到 11 月 29 日，Salon 的旧文章会在 `salon.com` 留多久还不确定。一家媒体停止出刊之后，网站可能继续上线，也可能在主机或域名停止续约时消失。网站消失之后，旧报道还能不能找到，取决于当初有没有人存过档。

依公告，Internet Archive 用 Wayback Machine 保存 Salon 的页面已将近三十年。在 Salon Explorer 上，超过 2 万名作者的文章可以按作者、年份与时期筛选，也能用关键词搜索全文。习惯用 Wayback Machine 的人，也可以直接输入 `salon.com` 的网址，按日期浏览各时期的页面。

## 导读观点 {#perspective}

网页存档服务多半用爬虫，也就是自动访问网页、下载内容的程序，定期存下页面当下的副本并标上时间。网站关闭之后才想到要存，已经没有页面可以存。

读者自己在意的报道，可以趁还在线上时用 Wayback Machine 的 Save Page Now 提交存档。依 Internet Archive 的说明页，在表单粘贴网址、点击按钮，就会存下这一页并得到一个永久的网址。Chrome、Firefox、Safari 都有扩展，iOS 与 Android 也有 App。少数禁止爬取或 SSL（网站的加密连接）设置特殊的网站会提交失败，Internet Archive 也不保留提交者的 IP 地址。

要把存档留在自己手上，本站在[西班牙封锁 archive.today](https://anoni.net/news/zh-cn/2026/09/spain-blocks-archive-today/)那篇介绍过 SingleFile 与 ArchiveBox。SingleFile 是把整页存成一个 HTML 文件的浏览器扩展，ArchiveBox 是自建的网页存档工具。另一种做法是 Webrecorder 的开源工具 ArchiveWeb.page，有 Chrome 与 Chromium 系浏览器的扩展与桌面版，可以在浏览的同时把页面存下来。ArchiveBox 与 ArchiveWeb.page 都能存成网页存档的标准格式 WARC，WARC 把网址、获取的时间与服务器响应的内容一起存下，之后可以用存档工具照原样重放页面。

送进 Wayback Machine 的页面要靠 Internet Archive 的服务持续运行才能打开。存在自己电脑里的文件要自行备份，文件只在自己手上，别人也无从确认存下之后有没有被改过。

监测中国大陆网络审查的 GreatFire 在页面上记录，从 2012 年 4 月 14 日起观察到对 Wayback Machine 网址 `web.archive.org` 的干扰。截至 11 月 29 日，最近一次有结论的测试在 11 月 7 日，结果是无法连上。有结论的测试只有这 1 次。因此 Save Page Now 与 Wayback Machine 在大陆境内可能无法连上，提交前先确认。

媒体被迫关站时，网站可能当晚就下架，之后能读到多少要看先前有没有人存过档。2021 年 12 月 29 日，超过 200 名香港警务处人员搜查立场新闻，网站与社交媒体当晚关闭。志愿者团体 Archive Team 的维基记录，立场新闻整体的存档状态是部分保存（Partially saved）。主站的 ArchiveBot 记录是已保存，网站地图在 6 月与关站前的 12 月各送去存档一次。

要让别人查证与引用的页面适合提交 Save Page Now，想自行保管的页面用 ArchiveWeb.page 或 ArchiveBox。以 Chrome 的 Wayback Machine 扩展为例，装好之后在页面上点工具栏的图标、选 Save Page Now 即可提交。Save Page Now 只存提交的那一页，报道的其他分页与文中链接出去的页面要另外提交。Wayback Machine 的存档任何人都能查询，登录后才能看到或含有个人资料的页面不适合提交存档。
