---
title: 修补前消息外泄的 PHP 远程代码执行漏洞
description: PHP 10 月 21 日发布 8.5.12、8.4.27、8.3.36、8.2.35，修补两个可能让未登录的攻击者在网站服务器上执行代码的漏洞。漏洞编号在预定披露前两天外泄，PHP 把发布提前一天。漏洞在 PHP 本身，要更新的是服务器上的 PHP，租用主机的人可以向服务商确认。
date: 2026-10-23T00:05:00+08:00
slug: php2shell-leaked-rce
categories:
  - security
sources:
  - title: "Security advisory: Critical remote code execution vulnerabilities, update now"
    url: https://www.php.net/archive/2026.php#2026-10-21-5
    publisher: PHP
    date: 2026-10-21
  - title: RCE via OOM corruption
    url: https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w
    publisher: PHP
    date: 2026-10-21
  - title: RCE via stale global state
    url: https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
    publisher: PHP
    date: 2026-10-21
  - title: Today's PHP Security Release, and How We're Strengthening PHP Security
    url: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
    publisher: The PHP Foundation
    date: 2026-10-21
  - title: "PHP: Supported Versions"
    url: https://www.php.net/supported-versions.php
    publisher: PHP
  - title: Critical PHP Security Release
    url: https://wordpress.org/news/2026/10/critical-php-security-release/
    publisher: WordPress.org
    date: 2026-10-21
  - title: Your Sites Are Protected Against the PHP2Shell Vulnerabilities
    url: https://automattic.com/2026/10/21/php2shell/
    publisher: Automattic
    date: 2026-10-21
  - title: Request handling memory corruption - php (CVE-2026-109618, CVE-2026-109619) - "php2shell"
    url: https://access.redhat.com/security/vulnerabilities/RHSB-2026-013
    publisher: Red Hat
    date: 2026-10-21
  - title: PHP2Shell — AI uncovers critical vulnerabilities in the backbone of the web
    url: https://www.php2shell.com/
    publisher: php2shell.com
  - title: CVE-2026-109618
    url: https://ubuntu.com/security/CVE-2026-109618
    publisher: Ubuntu
    date: 2026-10-21
  - title: PHP 存在2個重大資安漏洞(CVE-2026-109618 和 CVE-2026-109619)
    url: https://www.twcert.org.tw/tw/cp-169-11303-1d68a-1.html
    publisher: TWCERT/CC
    date: 2026-10-22
  - title: Cloudflare deploys protections against php2shell vulnerability
    url: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
    publisher: Cloudflare
    date: 2026-10-21
  - title: "Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619)"
    url: https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities
    publisher: Huntress
    date: 2026-10-20
  - title: Usage Statistics and Market Share of PHP for Websites, October 2026
    url: https://w3techs.com/technologies/details/pl-php
    publisher: W3Techs
  - title: 三部门关于印发网络产品安全漏洞管理规定的通知
    url: https://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm
    publisher: 中国政府网
    date: 2021-07-14
authors:
  - anoni-net
---

PHP 10 月 21 日发布 8.5.12、8.4.27、8.3.36 与 8.2.35，修补两个漏洞 CVE-2026-109618 与 CVE-2026-109619（CVE 是公开漏洞的统一编号），研究者与媒体称这组漏洞为 php2shell。php.net 的公告写两者可能让没有登录的攻击者在服务器上远程执行代码，所有处理网页请求的 PHP 都有风险，建议立刻更新。依 W3Techs 10 月 21 日的统计，在查得到服务器端语言的网站里，69.3% 使用 PHP。WordPress.org 的公告则说明这不是 WordPress 本身的漏洞，不会为此发布 WordPress 更新，要更新的是服务器上的 PHP。

依 PHP Foundation 10 月 21 日的博客，两个漏洞编号在 UTC 10 月 20 日 15:00（北京时间 23:00）前后开始在论坛与社交网站流传。流传的消息附上错误的发布时间与错误的严重度评分（CVSS，满分 10）10.0，PHP 评定的是 9.2，技术细节没有外泄。PHP 在 UTC 19:30（北京时间 10 月 21 日 03:30）提前发出预告，把发布从 UTC 10 月 22 日 14:00 提前到 10 月 21 日 14:00（北京时间 10 月 21 日 22:00）。没有马上发布的原因，是 Linux 发行版（Debian、Ubuntu、Red Hat 这类操作系统）还在打包修补，马上发布会让许多用户没有简便的更新方式。

同一篇博客提到，预告发出后，报告漏洞的一家安全公司误公开了一段演示视频。视频的副本随即在社交网站流传。博客写到，视频是各方加快开发概念验证程序（PoC，证明漏洞能被利用的程序）的原因之一。到公开发布时，PHP 安全团队在流传的 PoC 里没有找到能实际运行的利用程序。

Cloudflare 10 月 21 日的博客写到，外泄期间已观察到针对客户的攻击流量，对应的 WAF（网站应用防火墙）规则从 UTC 10 月 21 日 03:02（北京时间 11:02）起对免费与付费客户默认启用。安全公司 Huntress 到美东时间 10 月 21 日 16:30（北京时间 10 月 22 日 04:30）为止，没有在合作伙伴的系统观察到实际利用。修补版发布之后，台湾电脑网络危机处理暨协调中心（TWCERT/CC）在 10 月 22 日的警讯提到网上已出现 PoC。

## 导读观点 {#perspective}

依 PHP Foundation 的博客，两个漏洞都位于几乎每个请求都会用到的内存管理与错误处理。依 php.net 的公告，第一个漏洞发生在内存用量达到上限时，PHP 可能在内部数据只初始化了一部分时中断。之后的清理步骤可能把这些数据当成有效的。

第二个漏洞是前一个请求留下的内部状态，在内存已经释放之后，可能被同一个工作进程之后处理的请求使用。php.net 的公告把 Apache 搭配 mod_php（把 PHP 直接加载进网页服务器的运行方式）列为风险最高，已有演示能让未登录的请求在网站程序执行前触发攻击。

依研究者架设的说明网站 php2shell.com，漏洞出在 PHP 本身，网站程序写得安全也可能受影响。只输出「Hello World」的简单网站也一样。WordPress.com 的运营公司 Automattic 也说明这是运行环境的修补，只更新 WordPress、主题或插件保护不到。

PHP Foundation 的博客也检讨了修补为什么花了这么久。2024 年的外部安全审计期间，PHP 的开发者已经发现第一个漏洞的早期迹象，当时还不知道有远程执行代码的路径。当时想到的几种修法各有代价，可能破坏兼容性、造成拒绝服务（让网站无法正常运行），或需要改动大量第三方扩展。以共识决运作的安全团队迟迟没有决定，博客的说法是延误属于结构性的失败（structural failure），原因是决策流程与资源不足。

依博客，AI 辅助的漏洞研究让 PHP 收到的报告比以前多很多。7 月 1 日以来，安全团队发布了 15 个 CVE，另外处理了超过 100 件无效、重复或无法重现的报告。PHP Foundation 正在调整流程，让卡在困难取舍的严重漏洞更早交到领导层手上。

以下只整理中国大陆的制度内容，本文没有判断这次事件如何适用。《网络产品安全漏洞管理规定》从 2021 年 9 月 1 日起施行，到本文 10 月 8 日查证时没有查到修订版。规定适用于中国境内的网络产品提供者与网络运营者，以及从事漏洞发现、收集、发布的组织或个人。网络产品提供者发现或获知漏洞后，要在 2 日内向工业和信息化部的网络安全威胁和漏洞信息共享平台报送。

向社会发布漏洞信息的组织或个人，不得在提供者提供修补措施之前发布。认为有必要提前发布的，要与提供者共同评估协商并向工业和信息化部、公安部报告，由两部组织评估后发布。规定没有定义开源项目的维护者是否属于网络产品提供者，本文也查不到规定对境外项目的维护者或境外的发现者是否适用。

组织网站与博客常用 WordPress 这类 PHP 程序架设。依 Automattic，放在 WordPress.com 等自家托管服务的网站已经受到保护，管理者不必另外调整设置。WordPress.org 的公告建议租用主机的人向服务商确认更新，也列出在后台的「Tools > Site Health > Info > Server」（英文界面）可以看到 PHP 版本。这个版本号可以对照上面的修补版本，但发行版自行移植修补时会误判，原因见下一段。

自行管理服务器的人，用发行版软件包安装的 PHP 要看发行版的安全公告。有些发行版把修补移植到原本的版本，例如 Ubuntu 24.04 修补后的软件包是 8.3.6-0ubuntu0.24.04.13，只对照 PHP 的版本号会误判。Red Hat 10 月 21 日的公告写 Red Hat Enterprise Linux 默认使用 PHP-FPM（由独立进程运行 PHP 的方式），实际利用比较困难，部分更新还在准备中。PHP Foundation 的博客则提到，第一个漏洞也确认过能经由网站程序本身的处理流程，在 PHP-FPM 上远程执行代码。

依 php.net 的支持版本页，PHP 8.1 以下已经结束支持，8.2 则在 2026 年 12 月 31 日结束支持。这次 PHP 另外为 7.4、8.0、8.1 提供最小的源代码修补给自行编译的人，7.3 以下没有。TWCERT/CC 的警讯列出的受影响版本从 5.4 起。还没办法更新的，php.net 列出几项调整设置的做法可以缩小部分攻击路径，但公告也提醒只有更新能完整解决。

两个漏洞是否出现确认的实际入侵、是否列入美国网络安全和基础设施安全局（CISA）的已遭利用漏洞清单，以及 Red Hat 等发行版的更新是否补齐，是接下来可以留意的地方。
