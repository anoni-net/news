---
title: Firefox 157 的 TLS 密钥记录警告
description: 桌面版 Firefox 157（9 月 29 日发布）在电脑被设置成记录加密密钥时会显示警告。Mozilla 的帮助页提到多半是杀毒或安全软件设置的，出现警告不代表电脑中毒，打不开网站时可以先检查这类软件的 HTTPS 扫描功能。
date: 2026-10-12T00:00:00+08:00
slug: firefox-tls-keylog-warning
categories:
  - security
sources:
  - title: Firefox 157.0, See All New Features, Updates and Fixes
    url: https://www.firefox.com/en-US/firefox/157.0/releasenotes/
    publisher: Mozilla
    date: 2026-09-29
  - title: Troubleshoot network errors when TLS key logging is enabled
    url: https://support.mozilla.org/en-US/kb/sslkeylogfile-warning
    publisher: Mozilla
    date: 2026-06-25
  - title: Add a warning to about:neterror when SSLKEYLOGFILE is in use
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2035411
    publisher: Mozilla Bugzilla
    date: 2026-04-28
  - title: RFC 9850 - The SSLKEYLOGFILE Format for TLS
    url: https://www.rfc-editor.org/rfc/rfc9850.html
    publisher: RFC Editor
  - title: 关于 Firefox 在中国持续运营但北京火狐关闭及 Firefox 账户服务终止的重要公告
    url: https://web.archive.org/web/20250728090400/https://www.firefox.com.cn/farewell/
    publisher: 北京谋智火狐信息技术有限公司
    date: 2025-07-27
authors:
  - anoni-net
---

Firefox 9 月 29 日发布的 157 版，在电脑被设置成记录加密密钥时，会在地址栏盾牌图标的网站信息面板与设置页显示警告。版本说明只在桌面版列出此项变更，Android 与 iOS 的 157 版版本说明没有提到。根据 Mozilla 的帮助页，出现警告不代表电脑中毒，多半是杀毒或安全软件在检查加密连接。

依帮助页，触发警告的是 `SSLKEYLOGFILE` 这个环境变量（操作系统提供给程序读取的设置值），它会让 Firefox 把 HTTPS 连接用的加密密钥存成文件。能读到该文件的软件可能可以解密并查看 HTTPS 流量。视软件的用法，也可能拦截连接、冒充网站的服务器并修改数据。部分连接错误页也会多一条横幅，英文界面显示「Your connection may not be private」，链接到同一份帮助页。

Mozilla 2026 年 4 月在 bug 跟踪系统建立的记录提到改动的原因，建立者写到似乎有不少杀毒软件用该变量解密 HTTPS 流量，有时会让连接以意想不到的方式出错。同一则记录引用 Mozilla 的使用统计，Windows 上约一成用户的电脑有该变量。依帮助页的介绍，软件开发者看到警告，可能是调试工具开着。

## 导读观点 {#perspective}

HTTPS 每次连接都会协商出一组密钥，平常只留在浏览器与网站服务器两端，连接经过的网络设备看不到内容。`SSLKEYLOGFILE` 原本是给开发者调试用的。密钥写进文件之后，读得到文件、又取得那段加密流量的程序，就有机会解开这些连接。IETF（制定互联网技术标准的组织）2026 年 7 月发布的参考性文件 RFC 9850 记载了密钥文件的格式，同时提醒它只该用在保护测试数据的系统，不能用在正式环境。

看到警告又打不开网站时，帮助页建议先到杀毒或安全软件的设置里找「HTTPS 扫描」、「加密流量监控」、「网页防护」这类功能。软件允许的话先暂时关掉，再看连接问题是否还在。关掉的期间，那套软件也不会再检查加密的网页内容。帮助页有简体中文版，页首标示是机器翻译，没有经过人工校对。

杀毒软件的 HTTPS 扫描要读得到所有加密连接才能检查网页内容，要不要让它看到，是用户要做的取舍。依帮助页，只要信任那套软件看到你在网上做的一切，就不一定需要担心。帮助页也提到通常不必停用杀毒软件，Firefox 本身有 Safe Browsing，会警告已知的恶意与诈骗网站。

北京谋智火狐 2025 年 7 月 27 日的公告提到，它在 2025 年 9 月 29 日之后终止自己负责的 Firefox 中国大陆业务，Mozilla 将自行或通过授权的第三方继续负责。公告也提到浏览器本身在大陆继续可用并保持更新，下载改到 Mozilla 的 firefox.com/download。157 版的版本说明没有写区域限制，从那里下载的桌面版应同样带有此项警告。

没有安装这类软件、也没有在做网络调试的人看到警告，可能是其他程序设置了该变量，也可能是有人手动设置过。这是本文依帮助页列出的原因推断的，帮助页没有提供这种情况的处理步骤。本文的建议是请熟悉电脑的人协助检查系统的环境变量设置。
