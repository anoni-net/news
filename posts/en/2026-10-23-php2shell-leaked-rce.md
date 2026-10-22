---
title: PHP remote code execution vulnerabilities and the early leak of their IDs
description: On 21 October PHP released 8.5.12, 8.4.27, 8.3.36 and 8.2.35, fixing two vulnerabilities that may let an attacker who is not logged in run code on a web server. The vulnerability IDs leaked two days before the planned disclosure, and PHP moved the release forward by a day. The flaws are in PHP itself, so the PHP on the server is what needs updating, and people on hosted plans can check with their provider.
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
  - title: 情報セキュリティ早期警戒パートナーシップガイドライン
    url: https://www.ipa.go.jp/security/guide/vuln/ug65p90000019by0-att/partnership_guideline.pdf
    publisher: IPA
    date: 2026-10-01
  - title: 脆弱性関連情報の届出受付
    url: https://www.ipa.go.jp/security/todokede/vuln/uketsuke.html
    publisher: IPA
  - title: TWCERT/CC漏洞揭露政策
    url: https://www.twcert.org.tw/tw/cp-103-2924-7b930-1.html
    publisher: TWCERT/CC
    date: 2025-03-20
authors:
  - anoni-net
---

PHP released 8.5.12, 8.4.27, 8.3.36 and 8.2.35 on 21 October, fixing two vulnerabilities, CVE-2026-109618 and CVE-2026-109619, which researchers and the media call php2shell. The php.net advisory says both may allow an attacker who is not logged in to execute code remotely on the server, that every PHP installation handling web requests is at risk, and that users should update immediately. According to W3Techs statistics for 21 October, 69.3% of websites whose server-side language is known use PHP. WordPress.org's announcement explains that this is not a vulnerability in WordPress itself and that no WordPress update will be released for it, since the PHP on the server is what needs updating.

According to a PHP Foundation blog post on 21 October, the two CVE IDs began circulating on forums and social media at around 15:00 UTC on 20 October (23:00 Taipei time). They came with a wrong release time and a wrong severity score (CVSS, out of 10) of 10.0, where PHP's own rating is 9.2, and no technical details leaked. At 19:30 UTC (03:30 on 21 October, Taipei time) PHP brought its pre-announcement forward and moved the release from 14:00 UTC on 22 October to 14:00 UTC on 21 October (22:00 Taipei time). It did not release at once because Linux distributions such as Debian, Ubuntu and Red Hat were still packaging the fix, and releasing immediately would have left many users without an easy way to update.

The same post says that after the pre-announcement, one of the security firms that had reported the vulnerabilities mistakenly published a demonstration video, and copies quickly spread on social media. In the post's account, the video was one of the reasons various parties sped up work on proofs of concept (PoCs, code showing that a vulnerability can be exploited). By the time of public release, the PHP security team had not found a working exploit among the PoCs in circulation.

Cloudflare's blog post of 21 October says it observed attack traffic aimed at its customers during the leak, and that matching WAF (web application firewall) rules have been enabled by default for free and paid customers since 03:02 UTC on 21 October (11:02 Taipei time). As of 16:30 US Eastern Time on 21 October (04:30 on 22 October, Taipei time), security firm Huntress had not observed exploitation on its partners' systems. After the fixed versions came out, Taiwan's TWCERT/CC (Taiwan Computer Emergency Response Team/Coordination Center) noted in an alert on 22 October that PoCs had appeared online.

## Perspective {#perspective}

According to the PHP Foundation's post, both vulnerabilities sit in memory management and error handling, parts of PHP that nearly every request touches. The php.net advisory describes the first as occurring when memory use reaches its limit, at which point PHP may be interrupted while internal data is only partly initialised. A later clean-up step may then treat that data as valid.

The second involves internal state left behind by an earlier request, which may be used by a later request handled by the same worker process after its memory has been freed. The php.net advisory rates Apache with mod_php (a setup that loads PHP directly into the web server) as the highest risk, and an exploit has been demonstrated in which an unauthenticated request triggers the attack before the site's own code runs.

According to php2shell.com, an explainer site set up by the researchers, the flaws are in PHP itself, so even a securely written site can be affected, including a simple one that only prints "Hello World". Automattic, the company that runs WordPress.com, likewise explains that this is a fix to the runtime, and that updating WordPress, themes or plugins alone does not protect against it.

The PHP Foundation's post also looks at why the fix took so long. During an external security audit in 2024, PHP developers had already found early signs of the first vulnerability, though no path to remote code execution was known at the time. Each of the fixes considered then had a cost, whether breaking compatibility, opening up denial of service (making a site stop working normally) or requiring changes to many third-party extensions. The security team, which operates by consensus, struggled to choose, and the post calls the delay "a structural failure, caused by both the security team's decision process and its lack of resources."

The same post says AI-assisted vulnerability research has brought PHP far more reports than before. Since 1 July the security team has published 15 CVEs and handled more than 100 reports that were invalid, duplicates or could not be reproduced. The PHP Foundation is changing its process so that serious vulnerabilities stuck on hard trade-offs reach its leadership sooner.

We, a community based in Taiwan, compared the rules on disclosure timing in mainland China, Japan and Taiwan as of 8 October. What follows summarises each system, and we have not assessed how any of them would apply to this incident.

In mainland China, the Regulations on the Management of Network Product Security Vulnerabilities, in force since September 2021, apply to network product providers and operators in mainland China and to those who discover, collect or publish vulnerabilities. They require providers to report a vulnerability to a platform run by the Ministry of Industry and Information Technology (MIIT) within two days of discovering or learning of it. Anyone publishing vulnerability information may not do so before the provider offers a fix, and those who think early publication is necessary must consult the provider and report to MIIT and the Ministry of Public Security, which assess the case and publish. The regulations do not define whether open source maintainers count as providers, and we could not find whether they apply to maintainers of projects abroad or to researchers outside mainland China.

Under the 2026 edition of the guidelines for Japan's Information Security Early Warning Partnership, published on 1 October, the Information-technology Promotion Agency (IPA) receives reports, and JPCERT/CC, the designated coordination body, contacts developers and arranges when information is published. The target, which is not a legal deadline, is 45 days after JPCERT/CC first tries to reach the developer, taking into account the time a fix needs, coordination with counterparts abroad, the risk of the information leaking and the risk of exploitation. For open source software, JPCERT/CC also notifies distributors and the developers of products that include it when necessary. IPA does not require reporters to keep the information secret, nor does it require developers to fix the flaw.

In Taiwan, TWCERT/CC's vulnerability disclosure policy (version 2.2, March 2025) says it publishes a report's basic details within 90 calendar days of confirming that the report is complete, though it may delay publication after assessing the impact. The full details go on its Taiwan Vulnerability Note (TVN) platform only after the reporter, TWCERT/CC and the vendor all confirm that a fix or mitigation is in place. The policy does not say whether it covers open source projects based abroad, and we did not check reporting obligations under Taiwan's laws such as the Cyber Security Management Act.

Organisations often build their websites and blogs on PHP software such as WordPress. According to Automattic, sites on its own managed services such as WordPress.com are already protected, and their administrators do not need to change any settings. WordPress.org's announcement advises people on hosted plans to check with their host about the update, and notes that the PHP version is shown in the dashboard under "Tools > Site Health > Info > Server" (in the English interface). That version number can be compared with the fixed versions above, but it can mislead when a distribution backports the fix, as the next paragraph explains.

People who run their own servers and installed PHP from distribution packages should check their distribution's security advisories. Some distributions backport the fix to the original version, so comparing only the PHP version number can mislead; Ubuntu 24.04's fixed package, for example, is 8.3.6-0ubuntu0.24.04.13. Red Hat's advisory of 21 October says Red Hat Enterprise Linux uses PHP-FPM (which runs PHP in separate processes) by default, making exploitation harder, and that some updates were still being prepared. The PHP Foundation's post, for its part, says the first vulnerability has also been confirmed to allow remote code execution on PHP-FPM through the site's own request handling.

According to php.net's supported versions page, PHP 8.1 and earlier have reached end of life, and 8.2 reaches end of life on 31 December 2026. For this release PHP also provided minimal source patches for 7.4, 8.0 and 8.1 for people who compile PHP themselves, but none for 7.3 or earlier. TWCERT/CC's alert lists affected versions from 5.4 onwards. For those who cannot update yet, php.net lists several configuration changes that narrow some attack paths, while warning that only updating fully resolves the problem.

Whether either vulnerability turns out to have been used in confirmed intrusions, whether they are added to the Known Exploited Vulnerabilities catalog of the US Cybersecurity and Infrastructure Security Agency (CISA), and whether Red Hat and other distributions complete their updates are the things to watch next.
