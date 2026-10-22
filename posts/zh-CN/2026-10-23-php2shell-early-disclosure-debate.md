---
title: PHP 漏洞的协调披露与修补前的提前公开
description: PHP 两个漏洞在协调披露期间消息外泄。10 月 21 日修补发布之前，有研究者公开据称完整的技术细节，发行商提前推出含修补的镜像。安全公司也为客户提前部署了防护，这篇整理各方对禁令与提前公开的看法，以及美国、欧盟与中国大陆的相关说明与法规。
date: 2026-10-23T00:10:00+08:00
slug: php2shell-early-disclosure-debate
categories:
  - security
follows:
  - 2026-10-23-php2shell-leaked-rce
sources:
  - title: Today's PHP Security Release, and How We're Strengthening PHP Security
    url: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
    publisher: The PHP Foundation
    date: 2026-10-21
  - title: PHP blames supply chain security biz Chainguard for putting huge chunks of the web at risk
    url: https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611
    publisher: The Register
    date: 2026-10-22
  - title: PHP says AI review of critical bugs first sparked alarm in August, but signs surfaced in 2024
    url: https://therecord.media/php-foundation-statement-critical-vulnerabilities
    publisher: The Record
    date: 2026-10-21
  - title: Critical flaws strike PHP as disclosure embargo is broken
    url: https://www.itnews.com.au/news/critical-flaws-strike-php-as-disclosure-embargo-is-broken-629794
    publisher: iTnews
    date: 2026-10-21
  - title: Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot
    url: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/
    publisher: Amazon
    date: 2026-10-21
  - title: "PHP2Shell: PHP Remote Code Execution Exploited"
    url: https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/
    publisher: watchTowr
    date: 2026-10-21
  - title: Cloudflare deploys protections against php2shell vulnerability
    url: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
    publisher: Cloudflare
    date: 2026-10-21
  - title: Vulnerability Disclosure Policy
    url: https://certcc.github.io/certcc_disclosure_policy
    publisher: CERT/CC
  - title: This Guide in a Nutshell
    url: https://certcc.github.io/CERT-Guide-to-CVD/tutorials/cvd_in_a_nutshell/
    publisher: CERT/CC
  - title: Guidelines and Practices for Multi-Party Vulnerability Coordination and Disclosure
    url: https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1
    publisher: FIRST
  - title: mailing-lists:distros
    url: https://oss-security.openwall.org/wiki/mailing-lists/distros
    publisher: Openwall
  - title: Coders' Rights Project Vulnerability Reporting FAQ
    url: https://www.eff.org/issues/coders/vulnerability-reporting-faq
    publisher: EFF
  - title: Article 7 Tools used for committing offences
    url: https://www.legislation.gov.uk/eudr/2013/40/article/7/data.html
    publisher: legislation.gov.uk（Directive 2013/40/EU）
  - title: 三部门关于印发网络产品安全漏洞管理规定的通知
    url: https://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm
    publisher: 中国政府网
  - title: Today's PHP security release, and how we're strengthening security
    url: https://news.ycombinator.com/item?id=50182987
    publisher: Hacker News
authors:
  - anoni-net
---

PHP 10 月 21 日修补的两个漏洞（CVE-2026-109618、CVE-2026-109619），可能让没有登录的攻击者在网站服务器上执行代码，消息在协调披露期间外泄。修补发布之前，有研究者公开据称完整的技术细节，也有厂商提前推出修补或为客户部署防护。安全社区因此争论修补发布之前，能不能、该不该提前公开，或提前保护一部分人。网站用 PHP 搭建的组织先按前一篇导读向主机服务商或外包商确认已应用修补，这场争论关系到之后的漏洞会在什么时候、先让哪些人知道。

协调披露（coordinated vulnerability disclosure）是发现漏洞的人先私下通知开发者，约定公开的日期。公开日之前的保密期称为禁令（embargo），让开发者与下游的发行商（把 PHP 这类软件打包给用户安装的厂商）有时间准备修补。

依 PHP Foundation 10 月 21 日的博客，这次的协调披露直到预定发布日的两天前都运作正常。UTC 10 月 20 日 15:00 前后（北京时间 23:00 前后），漏洞编号开始在网上流传。PHP 在 UTC 19:30（北京时间 10 月 21 日 03:30）发出公告，预告修补改在 10 月 21 日发布，比原定提前一天。

同一篇博客写到，预告发出后，一家报告漏洞的安全公司误公开了演示视频。PHP 从 UTC 10 月 20 日 23:00 前后（北京时间 10 月 21 日 07:00）起提供给少数关键基础设施企业的缓解建议，也可能外泄了。发行商 Chainguard 和其他发行商一样事先收到了修补，在 UTC 10 月 21 日 07:41（北京时间 15:41）公开含修补的容器镜像（打包好、可以直接部署的软件环境）。时间比提前后的发布时间早六个多小时，博客的说法是，攻击者因此可以在其他用户还在等待时研究修补的内容。

依 iTnews 10 月 21 日的报道，漏洞编号在社交网站出现几个小时后，一位研究者在网上公开了据称完整的技术细节。iTnews 没有独立确认内容是否有效。安全公司 watchTowr 的页面写到，它的平台客户在 PHP 发布修补前 24 小时就有主动防御。Cloudflare 的博客写到，对应的防火墙规则比公开披露早约 9 小时，对免费与付费客户默认启用。

Amazon 10 月 21 日的威胁情报文章写到，它的诱捕系统（故意放在网上、用来观察攻击的系统）在 10 月 17 日就观察到利用尝试，比漏洞编号外泄还早。文章也写到不确定这些尝试在真实系统上会不会成功，以及不清楚对方如何在披露前获取信息。

## 导读观点 {#perspective}

美国的漏洞协调中心 CERT/CC 的披露政策，是收到报告 45 天后公开，有实际利用等情况时可能提前或推迟。CERT/CC 的指南写到，参与的人越多、禁令拖得越久，外泄的可能就越高。

各发行版共用的 distros 邮件列表规定禁令最长 14 天，偏好少于 7 天。成员不能把信息分享给团队以外的人，也不能先为客户部署未说明的修补。PHP 有没有通过 distros 通知发行版，到 10 月 22 日查不到。

外泄之后要不要提前公开是第一个争议点，Chainguard 的首席执行官对 The Register 表示公司没有泄露。他说官方披露前已经有人遭到攻击，所以决定先推出修补。首席执行官说「It's coordinated vulnerability disclosure, unless there's evidence of active exploits in the wild」（除非有实际利用的证据，否则就是协调披露）。到 10 月 22 日，本文没有查到 Chainguard 自己发布的书面说明。

安全事件应急响应团队的国际组织 FIRST 的多方协调指引，把合理的禁令期限定在没有事先公开、包括没有实际利用的明确证据时。修补发布前，Amazon 的诱捕系统观察到利用尝试，但不确定能否在真实系统上成功。Cloudflare 的博客也写到，外泄期间观察到针对客户的攻击流量。

依 PHP Foundation 的博客，Chainguard 单方面打破禁令，无视多方数周的协调。依 The Register 的报道，Chainguard 的首席执行官则事先通知了 PHP 的协调渠道。Hacker News 上有评论认为打破禁令没有后果就会一再发生，也有评论认为这次已经损害了协调披露的信任。PHP Foundation 的博客也写到，到公开发布时，PHP 安全团队在流传的概念验证程序里没有找到能实际运行的利用程序。

提前保护给谁是第二个争议点，Hacker News 上为提前公开辩护的意见认为，协调披露让普通用户无法自保。watchTowr 的平台客户比 PHP 发布修补早 24 小时受到保护，Cloudflare 的防护规则则对免费与付费客户都默认启用。依 The Register 的报道，Chainguard 的镜像任何人都能获取。

PHP 的博客写到，发行商与长期支持（LTS）厂商事先收到修补，缓解建议则交给少数关键基础设施企业。博客说明没有在外泄后立刻发布，是因为发行商还在打包修补，立刻发布会让许多用户没有简便的更新方式。到 10 月 22 日，本文没有查到针对提前通知名单的公开批评。

Chainguard 的首席执行官也对 The Register 表示，光是知道某个软件有漏洞就足以找到它，他认为这是新的常态。Amazon 的文章同样认为禁令只在别人找到同一个漏洞之前有效，但协调披露仍然是正确的模式。文章提醒防守的一方，不应假设公开日就是最早被利用的日子，AI 辅助的分析让从修补或公告做出可用的攻击程序变得更便宜。

修补前公开漏洞细节是否违法，各地的规定不同。数字权利倡导组织 EFF 在写给美国研究者的 FAQ 里的立场是，法律应该很少管到披露，「负责任披露」模式之外的披露也可能合法。FAQ 注明内容不是法律意见。同一份 FAQ 也写到，披露里可以直接执行的代码越多，法律风险越高。

中国大陆 2021 年 9 月起施行的《网络产品安全漏洞管理规定》，适用于境内的网络产品提供者，以及从事漏洞发现、收集、发布的组织或个人。条文没有写明「境内」是否也限定后者。规定禁止在产品提供者推出修补措施之前发布漏洞信息，认为有必要提前发布时，要与提供者协商并报工业和信息化部、公安部评估后发布。规定也禁止发布专门用于利用漏洞、从事危害网络安全活动的程序和工具。

欧盟《信息系统攻击指令》（Directive 2013/40/EU）第 7 条，要求成员国处罚意图用于犯罪、未经授权而制作或提供主要为犯罪设计的程序，至少针对非轻微的案件。各成员国如何转化为国内法，以及欧盟对公开漏洞信息本身的指引，到 10 月 22 日查不到。本文比较 EFF 的整理与欧盟指令，两者看的是意图与内容。中国大陆的规定除了内容，也直接限制公开的时间点。

依本文 10 月 8 日查证的规定全文，网络产品提供者发现或获知漏洞后，要在 2 日内向工业和信息化部的网络安全威胁和漏洞信息共享平台报送。上游产品或组件的漏洞，要立即通知相关的产品提供者。向社会发布漏洞信息时要同步发布修补或防范措施，国家举办重大活动期间未经公安部同意不得发布。未公开的漏洞信息，也不得提供给网络产品提供者以外的境外组织或个人。

违反规定收集、发布漏洞信息的，由工业和信息化部、公安部依各自职责处理，构成《网络安全法》第六十二条规定情形的依该条处罚。规定本身没有写出罚款额度，本文也没有查证第六十二条的内容。到 10 月 8 日，本文没有查到这份规定的修订版，也没有判断这次事件如何适用。规定没有定义开源项目的维护者是否属于网络产品提供者，本文也查不到规定对境外项目的维护者或境外发现者是否适用，以及实际的执法案例。

本文的建议是，网站用 PHP 搭建的组织请主机服务商或外包商确认已应用修补，并检查日志。Amazon 建议检查日志时至少从 10 月 17 日查起，因为它在那一天就观察到利用尝试。Amazon 建议面向互联网的系统遇到严重漏洞时，以小时计算修补与缓解的时间，认为 7 天或 30 天的处理期限已经不够。要问主机服务商或外包商的问题，以及修补后的检查，见文档站的[组织网站遇到重大漏洞时的确认与应对](https://anoni.net/docs/zh-cn/scenarios/org-website-vulnerability/){target="_blank"}。

PHP Foundation 的博客提到正在调整安全团队的决策流程，让卡在困难取舍的漏洞更早交到领导层。Chainguard 的首席执行官则对 The Record 表示，业界要想办法更快、更协调地处理这类情况。到 10 月 22 日为止，博客没有提到修改禁令的长度、提前通知的名单或对打破禁令者的处理。FIRST 的指引建议分享信息的社区可以对破坏信任的成员设罚则，例如移出名单。

比较各方的做法时，读者可以问几个问题。禁令保护的是哪些人，提前收到通知与防护的名单如何决定，普通用户在禁令期间有没有自保的方法。提前推出修补时，还在等待的多数用户是否先暴露给攻击者。若如 Amazon 所说，AI 辅助的分析让攻击程序更快完成，禁令还能争取到多少时间。
