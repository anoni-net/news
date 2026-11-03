---
title: Personal protection and open source maintenance as AI speeds up vulnerability discovery
description: In two posts on 23 October, EFF argued that frontier AI models have made finding vulnerabilities cheap and that computers will be compromised more often. EFF recommends that everyone keep browsers and apps updated, use a password manager and watch for phishing, and argues that companies relying on open source should contribute money and people to its upkeep. People who run their own websites should also check that PHP has been patched.
date: 2026-11-07T00:00:00+08:00
slug: eff-security-worse
categories:
  - security
sources:
  - title: Computer Security Is About to Get a Lot Worse, Here's What You Can Do
    url: https://www.eff.org/deeplinks/2026/10/computer-security-about-get-lot-worse-heres-what-you-can-do
    publisher: EFF
    date: 2026-10-23
  - title: The Vulnerability Apocalypse and Why We Should Fund Open Source
    url: https://www.eff.org/deeplinks/2026/10/vulnerability-apocalypse-and-why-we-should-fund-open-source
    publisher: EFF
    date: 2026-10-23
  - title: Today's PHP Security Release, and How We're Strengthening PHP Security
    url: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
    publisher: The PHP Foundation
    date: 2026-10-21
  - title: "PHP: News Archive - 2026"
    url: https://www.php.net/archive/2026.php
    publisher: PHP
  - title: Usage Statistics and Market Share of PHP for Websites
    url: https://w3techs.com/technologies/details/pl-php
    publisher: W3Techs
  - title: "\"The panic hasn't turned into patching\": What security researchers really think about the PHP2Shell response"
    url: https://thenewstack.io/php2shell-unpatched-php-servers/
    publisher: The New Stack
    date: 2026-10-27
  - title: "CVE Volume vs Real Risk: Making Sense of Vulnpocalypse"
    url: https://brandefense.io/blog/cve-volume-vulnpocalypse-risk-prioritization/
    publisher: Brandefense
    date: 2026-08-26
  - title: AI vulnerability discovery is pushing 2026 CVEs toward 66,000
    url: https://www.helpnetsecurity.com/2026/06/15/first-2026-cve-forecast/
    publisher: Help Net Security
    date: 2026-06-15
  - title: Keeping Your Data Safe
    url: https://ssd.eff.org/module/keeping-your-data-safe
    publisher: EFF Surveillance Self-Defense
  - title: Choosing the Password Manager That's Right for You
    url: https://ssd.eff.org/module/choosing-the-password-manager-that-s-right-for-you
    publisher: EFF Surveillance Self-Defense
  - title: "How to: Avoid Phishing Attacks"
    url: https://ssd.eff.org/module/how-avoid-phishing-attacks
    publisher: EFF Surveillance Self-Defense
  - title: "Privacy Badger: EFF's Free Tracker Blocking Browser Extension"
    url: https://www.eff.org/pages/privacy-badger
    publisher: EFF
  - title: 更新 Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=zh-Hant
    publisher: Google Chrome 說明
  - title: 更新 iPhone 或 iPad
    url: https://support.apple.com/zh-tw/118575
    publisher: Apple 支援
    date: 2026-09-24
  - title: 檢查及更新 Android 版本
    url: https://support.google.com/android/answer/7680439?hl=zh-Hant
    publisher: Android 說明
  - title: 総理「大至急、PHPパッチ適用を」Xで異例の要請 エンジニアは評価「経営層に伝わる」
    url: https://www.itmedia.co.jp/news/article/2610/22/2000002483/
    publisher: ITmedia NEWS
    date: 2026-10-22
  - title: PHPの2件の深刻な脆弱性(CVE-2026-109618、CVE-2026-109619)についてまとめてみた
    url: https://piyolog.hatenadiary.jp/entry/2026/10/21/174516
    publisher: piyolog
    date: 2026-10-21
  - title: PHP 보안취약점(PHP2Shell) 관련 기업 보안 대응 수칙
    url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72228
    publisher: KISA
    date: 2026-10-22
  - title: 網站開發程式語言PHP釋出緊急安全更新 資安署呼籲儘速完成修補
    url: https://moda.gov.tw/ACS/press/news/press/21134
    publisher: Administration for Cyber Security, Ministry of Digital Affairs (Taiwan)
    date: 2026-10-22
authors:
  - anoni-net
---

EFF, the US digital rights organisation, published two posts on 23 October arguing that frontier AI models from companies such as OpenAI and Anthropic have made it cheap and easy to find zero-day vulnerabilities (flaws the vendor does not yet know about and has not fixed). EFF expects things to get worse before they get better, and its first post offers basic digital security habits that apply to anyone using a computer or phone, wherever they are. The second post uses vulnerabilities in PHP as its example and argues that companies relying on open source should contribute money and people to its upkeep. Anyone whose website runs on PHP should also check that the PHP on the server has been patched against the vulnerabilities disclosed in October.

According to EFF's second post, the US National Vulnerability Database (NVD) holds around 400,000 CVEs (the shared identifiers for publicly disclosed vulnerabilities) filed since 1988, and 13,000 new ones were submitted in October alone. From this EFF calculates that 3% of all vulnerabilities ever logged were found in October, and says it is likely that by the end of the year more than a quarter of all vulnerabilities ever found will date from 2026. There is no primary link for these figures in the post, and the source given in the chart caption is CVE Tracker. An analysis by the security firm Brandefense, updated on 26 October, lists 86,533 CVE records published in the NVD by 25 October, against 48,151 for the whole of 2025.

EFF's second post takes PHP, a programming language widely used on web servers, as its example and says it powers nearly 70% of websites. W3Techs statistics for 2 November put the figure at 69.1% of websites whose server-side language is known. On 21 October the PHP project released 8.5.12, 8.4.27, 8.3.36 and 8.2.35, fixing two vulnerabilities that allow an attacker who is not logged in to execute code on the server.

According to a 21 October post by the PHP Foundation, which funds PHP development, signs of the problem had surfaced during the first externally funded audit in 2024, but no concrete attack path was found. According to EFF, because the maintainers could not find a way to exploit it at the time, they lowered its priority and the vulnerability went unfixed. In EFF's account, researchers working with the latest models from OpenAI and Anthropic independently rediscovered it in August 2026 and found a way to exploit it. The foundation lists the security firm Calif, OpenAI and Wiz as the discoverers, and mentions Anthropic's Claude Mythos only in a section on its own scan of PHP earlier in 2026, not as a discoverer.

According to EFF, at the time of writing more than 33 million websites were still running vulnerable versions of PHP. On 27 October The New Stack cited internet-wide scans by the security firm Censys, in which about 32.5 million internet-facing PHP services reported unsafe versions and about 61.3 million could not be identified by version. According to the same article, Linux distributions often backport fixes to older versions without changing the version number. Some services counted as unpatched may therefore already be patched, and estimates based on version numbers may run high.

In EFF's description, projects such as PHP, OpenSSL and SQLite run on nearly every computer, and some are maintained by teams as small as one person. Vulnerability reports are now pouring in, some of them false but many of them real. According to the foundation, PHP's security team published 15 CVEs between 1 July and 21 October and worked through more than 100 reports that turned out to be invalid, duplicates or not reproducible. AI helps the team validate reports, but a person makes every decision and works on every patch.

## Perspective {#perspective}

A CVE is a numbered record of a publicly disclosed vulnerability, and records vary widely in severity, yet EFF's second post calls them all critical security bugs. In June, Help Net Security reported a full-year CVE forecast from FIRST, the international association of incident response teams, and noted that part of the growth comes from GitHub Security Advisories and VulnCheck expanding their cataloguing and backfilling old records.

According to the same Brandefense analysis, there were 272 additions in 2026, up to 23 October, to the Known Exploited Vulnerabilities (KEV) catalog of the US Cybersecurity and Infrastructure Security Agency (CISA), or about three for every thousand CVEs. The analysis adds that KEV includes older CVEs, so the ratio is only a rough guide. Our inference is that the growth in CVE records does not translate into the same growth in exploited vulnerabilities, though the number of patches people need to apply has gone up.

On funding open source, EFF argues that companies should put money and people into maintaining the open source projects they depend on, without proposing amounts, mechanisms or a specific fund. The PHP Foundation's account of PHP's resources differs from EFF's: in EFF's post maintenance depends on a small number of volunteers working in their free time, while in the foundation's post security work on PHP itself depends on a small group of foundation-funded developers and a little volunteer help. The foundation asks for support from three groups, namely companies that build products with PHP, hosting providers along with cloud providers and Linux distributions, and governments and public institutions. It also acknowledges that the delayed fix was "a structural failure, caused by both the security team's decision process and its lack of resources."

EFF's first recommendation for individuals is to keep the browser and all apps up to date with the latest patches. According to EFF's Surveillance Self-Defense guide (SSD), updates often fix security problems in older code that attacks can exploit, and some older operating systems no longer receive even security updates. According to Chrome's help page, the browser updates itself in the background when a new version is available, usually completing the update when it is closed and reopened. If the browser stays open for a long time, an indicator shows that an update is waiting.

EFF also recommends installing a password manager and using a different password for each website, so that one compromised site does not expose the passwords for other accounts. According to SSD, the password managers built in by Apple, Google and Mozilla are also an option. Apple's Passwords app is end-to-end encrypted by default, while Google's password manager only gets on-device encryption if users go into the settings and set a passphrase themselves. Standalone password managers such as Bitwarden and KeePassXC are also on SSD's list, and according to the same guide, automatically filling in a password is an important protection against phishing.

EFF further suggests considering a tracker-blocking tool such as Privacy Badger, its free browser extension, available for Safari according to the 23 October post. The same sentence urges vigilance against phishing, which according to SSD means tricking people into handing over their passwords through a deceptive link. EFF also warns that data breaches may become more likely and that the websites people visit may face more attacks than usual, so some services may be disrupted.

For people who run a blog or website, EFF recommends making sure that they or their hosting provider have patched the PHP vulnerabilities. According to the php.net advisory of 21 October, there are no complete mitigations and updating is the only safe choice. The PHP project also provided minimal backports for 7.4, 8.0 and 8.1 for people who build PHP from source, while for other older versions it depends on whether a distribution or a long-term support (LTS) vendor offers a backport. From EFF's advice that site owners or their hosting provider should patch, our inference is that people on hosted plans can ask their provider to confirm that this fix has been applied.

Disruption of the kind EFF warns about appeared in Japan around the PHP release, although what we found were organisations going offline ahead of the fix rather than confirmed attacks. On the evening of 21 October, according to ITmedia NEWS, Japan's prime minister urged organisations on X to prepare to apply the fix that night, adding that temporarily taking a website offline is one way to reduce the risk where patching is difficult. The security blog piyolog, compiling organisations' notices and news reports rather than official statistics, counted 211 organisations in Japan that had suspended services or announced emergency maintenance, in a count made during the 01:00 hour, Japan time, on 22 October. These included 2 national government bodies, 4 local governments and 7 financial institutions, though some of the notices did not name PHP and some organisations were counted on the basis of news reports.

In South Korea, the Korea Internet & Security Agency (KISA) published guidance for companies on 22 October, advising those who can neither update nor apply interim settings to consider blocking external access or temporarily suspending services. Taiwan's Administration for Cyber Security, under the Ministry of Digital Affairs, issued a press release the same day asking organisations to take stock of their PHP systems, patch them and then review their system logs, without asking anyone to suspend services. As of 22 October we, a community based in Taiwan, found no notices of Taiwanese organisations going offline over these flaws, and no confirmed intrusions in Japan, South Korea or Taiwan.

The first step that applies to everyone using a computer or phone is to turn on automatic updates for the system and apps, and to close and reopen the browser from time to time. On iPhone the setting is under Settings > General > Software Update > Automatic Updates (our translation of the menu names on Apple's Taiwan support page), and according to Apple's support page updates install overnight while the phone is charging and connected to Wi-Fi. According to Android's help page, most security patches install automatically, on a schedule that varies by manufacturer and carrier, and older devices may not be able to run newer Android versions. Our inference is that these settings cannot prevent breaches caused by a website itself being compromised, while using a different password on each site keeps one breach from spreading to other accounts.
