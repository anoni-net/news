---
title: Coordinated disclosure of the PHP vulnerabilities and publication before the fix
description: News of two PHP vulnerabilities leaked during coordinated disclosure. Before the fix came out on 21 October, a researcher published what were claimed to be full technical details, and a distributor released images containing the fix early. Security firms also deployed protections for their customers ahead of time. This piece sets out the different views on embargoes and early publication, the relevant guidance and rules in the US, the EU and mainland China, and how Japan and Taiwan handle disclosure timing.
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
    publisher: legislation.gov.uk (Directive 2013/40/EU)
  - title: 三部门关于印发网络产品安全漏洞管理规定的通知
    url: https://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm
    publisher: 中国政府网
  - title: Today's PHP security release, and how we're strengthening security
    url: https://news.ycombinator.com/item?id=50182987
    publisher: Hacker News
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

News of two vulnerabilities that PHP fixed on 21 October (CVE-2026-109618 and CVE-2026-109619), which may let an attacker who is not logged in run code on a web server, leaked while coordinated disclosure was under way. Before the fix was released, a researcher published what were claimed to be full technical details, and some companies shipped the fix early or deployed protections for their customers. Security practitioners have since been debating whether anyone can or should publish before a fix is released, or protect some people first. Organisations whose websites run on PHP should first confirm with their host or contractor that the fix has been applied, as our previous article describes, while this debate bears on when future vulnerabilities become known and who hears about them first.

In coordinated vulnerability disclosure, whoever finds a vulnerability tells the developers privately first, and they agree on a date for publication. The period of secrecy before that date is called an embargo, and it gives the developers and downstream distributors (companies that package software such as PHP for users to install) time to prepare a fix.

According to a PHP Foundation blog post on 21 October, the coordinated disclosure worked well until two days before the planned release date. At around 15:00 UTC on 20 October (around 23:00 Taipei time), the vulnerability IDs began circulating online. At 19:30 UTC (03:30 on 21 October, Taipei time) PHP issued an announcement moving the release forward by a day, to 21 October.

The same post says that after the announcement, one of the security firms that had reported the vulnerabilities mistakenly published a demonstration video. Mitigation advice that PHP had given a small number of critical infrastructure providers from around 23:00 UTC on 20 October (07:00 on 21 October, Taipei time) may also have leaked. Chainguard, a distributor that had received the fix in advance like the other distributors, published container images (pre-packaged software environments ready to deploy) containing the fix at 07:41 UTC on 21 October (15:41 Taipei time). That was more than six hours before the brought-forward release, and in the post's words, "Any attacker could now study the fix in binary form while every other PHP user was still waiting for the release."

According to an iTnews report on 21 October, a few hours after the vulnerability IDs appeared on social media, a researcher published what were claimed to be the full technical details online. iTnews had not independently confirmed that the material was valid. Security firm watchTowr's page says customers of its platform had active defences in place 24 hours before PHP released the fix. Cloudflare's blog post says its matching firewall rules went live about 9 hours before public disclosure and are enabled by default for free and paid customers.

Amazon's threat intelligence post of 21 October says its honeypot (a system deliberately placed on the internet to observe attacks) recorded exploitation attempts as early as 17 October, before the vulnerability IDs leaked. The post also says it is unclear whether these attempts would have succeeded against real-world systems, and how the attacker obtained the information before disclosure.

## Perspective {#perspective}

Under the disclosure policy of CERT/CC, the US vulnerability coordination centre, vulnerabilities are published 45 days after the initial report, possibly earlier or later in circumstances such as active exploitation. CERT/CC's guide to coordinated disclosure notes that the more parties are involved and the longer an embargo lasts, the more likely a leak becomes.

The distros mailing list shared among distributions sets a maximum embargo of 14 days and prefers less than 7. Members may not share the information with anyone outside their team, nor deploy undocumented fixes for customers in advance. As of 22 October, we could not find out whether PHP notified distributions through distros.

Whether to publish early once a leak has happened is the first point of contention, and Chainguard's chief executive told The Register the company did not leak anything. He said people were already being attacked before the official disclosure, so the company decided to ship the fix first. In his words, "It's coordinated vulnerability disclosure, unless there's evidence of active exploits in the wild." As of 22 October, we had not found a written statement published by Chainguard itself.

The multi-party coordination guidelines of FIRST, the international body of incident response teams, limit a reasonable embargo to cases where there is no clear evidence of prior public disclosure, including active exploitation. Before the fix was released, Amazon's honeypot recorded exploitation attempts, though it was uncertain whether they would succeed against real systems. Cloudflare's blog post also says attack traffic aimed at its customers was observed during the leak.

According to the PHP Foundation's post, Chainguard broke the embargo unilaterally, disregarding weeks of coordination by many parties. According to The Register, Chainguard's chief executive had notified PHP's coordinated disclosure channel in advance. On Hacker News, some commenters argued that if breaking an embargo has no consequences it will keep happening, and others that this case had already damaged the trust coordinated disclosure depends on. The PHP Foundation's post also says that by the time of public release, the PHP security team had not found a working exploit among the proofs of concept in circulation.

Who gets protected early is the second point of contention, and Hacker News comments defending early publication argued that coordinated disclosure left ordinary users unable to protect themselves. Customers of watchTowr's platform were protected 24 hours before PHP released the fix, while Cloudflare's protective rules were enabled by default for both free and paid customers. According to The Register, Chainguard's images were available to anyone.

PHP's post says that distributions and long-term support vendors received the fix in advance, while the mitigation advice went to a small number of critical infrastructure providers. The post explains that PHP did not release immediately after the leak because distributions were still packaging the fix, and releasing at once would have left many users without an easy way to update. As of 22 October, we had found no public criticism of who was on the advance notification list.

Chainguard's chief executive also told The Register that just being told a piece of software has a vulnerability is enough to find it, which he sees as the new normal. Amazon's post likewise holds that an embargo protects defenders only until someone else finds the same bug, while maintaining that coordinated disclosure is still the right model. It reminds defenders not to assume the public disclosure date is the earliest date of exploitation, since AI-assisted analysis makes it cheaper to turn a patch or advisory into a working exploit.

Whether publishing vulnerability details before a fix is illegal depends on where it happens. The digital rights group EFF, in an FAQ written for US researchers, takes the position that the law should only rarely police disclosures, and that disclosure outside the "responsible disclosure" model may also be legal. The FAQ notes that it is not legal advice. It also says that the more functional code a disclosure contains, the riskier it is.

Mainland China's Regulations on the Management of Network Product Security Vulnerabilities, in force since September 2021, apply to network product providers within the People's Republic of China and to organisations or individuals who discover, collect or publish vulnerabilities. The text does not say whether "within" also limits the latter group. The regulations prohibit publishing vulnerability information before the product provider offers a fix, and anyone who thinks early publication is necessary must consult the provider and report to the Ministry of Industry and Information Technology (MIIT) and the Ministry of Public Security, which assess the case before publication. They also prohibit publishing programs and tools designed specifically to exploit vulnerabilities for activities that endanger network security.

Article 7 of the EU Directive on attacks against information systems (Directive 2013/40/EU) requires member states to punish, at least in cases that are not minor, the production or making available without right of programs designed primarily to commit offences, with the intention that they be used for such offences. As of 22 October, we could not find how member states have transposed it into national law, or any EU guidance on publishing vulnerability information as such. Comparing the EFF's summary with the EU directive, we found that both look at intent and content. Mainland China's regulations look at content too, but also restrict the timing of publication directly.

We, a community based in Taiwan, also compared how Japan and Taiwan set the timing of disclosure, using the rules as we checked them on 8 October, without assessing how either would apply to this incident. Japan's Information Security Early Warning Partnership has operated since July 2004 under public notices of the Ministry of Economy, Trade and Industry, with the Information-technology Promotion Agency (IPA) receiving reports and JPCERT/CC (Japan Computer Emergency Response Team Coordination Center) contacting developers and coordinating when information is published. Its guidelines, in a 2026 edition published on 1 October, set a target of 45 days after JPCERT/CC first tries to reach the developer, taking into account the time a fix needs, coordination with counterparts abroad, the risk of the information leaking and the risk of exploitation.

The Japanese guidelines also cover who hears first. A developer may warn its users before the publication date, after coordinating with JPCERT/CC, where it judges this would reduce user risk, and for open source software JPCERT/CC notifies the developers or development community and, where necessary, distributors and the developers of products that include it. Under the 2026 edition, IPA also promptly notifies the Cabinet Office of vulnerabilities that are exploited or suspected of being exploited, or that are severe and would have a wide impact if exploited, and the Cabinet Office may pass information to developers, government bodies, infrastructure operators and users before IPA and JPCERT/CC publish, in parallel with the usual process, under which JPCERT/CC's coordination and publication normally proceed as before.

In Taiwan, the vulnerability disclosure policy of TWCERT/CC (Taiwan Computer Emergency Response Team/Coordination Center), version 2.2 dated 18 March 2025, says it publishes a report's basic details within 90 calendar days of confirming that the report is complete, and may delay publication or limit the detail after assessing the impact. The full details go on its Taiwan Vulnerability Note (TVN) platform only after the reporter, TWCERT/CC and the vendor all confirm that a fix or mitigation is in place. The policy defines a vendor as the manufacturer of the affected product and does not mention open source projects or development communities, and does not say whether it applies to ones based abroad.

In Japan, IPA does not require reporters to keep information secret or developers to fix the flaw, and the guidelines contain no penalty provisions, though they note that IPA accepting a report does not relieve the reporter of legal liability for how the vulnerability was found. Taiwan's policy says it follows the CVE program's rules (the system that assigns vulnerability IDs) and the laws of the Republic of China without citing a specific statute, and we did not check reporting obligations under Taiwan's Cyber Security Management Act or other laws. In our reading, the documents in both places set the timing that the coordinating body itself works to, which puts them closer to the CERT/CC policy and the distros list than to mainland China's regulations, where publication before a fix is generally prohibited and violations are referred to MIIT and the Ministry of Public Security, with penalties under Article 62 of the PRC Cybersecurity Law where it applies. The regulations themselves set no fine, and we did not check that article.

Our advice is that organisations whose websites run on PHP ask their host or contractor to confirm that the fix has been applied, and check their logs. Amazon recommends checking logs from at least 17 October, because it recorded exploitation attempts that day. Amazon also recommends measuring patch and mitigation timelines in hours for critical vulnerabilities in internet-facing systems, saying a 7-day or 30-day deadline is no longer enough. For the questions to ask your host or contractor, and the checks to run after patching, see [Checking and responding to a critical vulnerability on your organisation's website](https://anoni.net/docs/en/scenarios/org-website-vulnerability/){target="_blank"} on the docs site.

The PHP Foundation's post says the foundation is changing the security team's decision-making so that vulnerabilities stuck on hard trade-offs reach its leadership sooner. Chainguard's chief executive told The Record that the industry has to figure out how to get through such situations "faster and more coordinated and better." As of 22 October, the post did not mention changing the length of embargoes, the advance notification list or how those who break an embargo are handled. FIRST's guidelines suggest that sharing communities could set penalties for members who violate trust, such as removal from the community.

Readers comparing these approaches can ask a few questions. Whom does an embargo protect, how is the list of those who get early notice and protection decided, and do ordinary users have any way to protect themselves during the embargo? When a fix ships early, are the majority who are still waiting exposed to attackers first? And if, as Amazon says, AI-assisted analysis speeds up building exploits, how much time can an embargo still buy?
