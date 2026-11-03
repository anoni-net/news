---
title: AI 加速找漏洞之后的个人防护与开源维护
description: EFF 10 月 23 日的两篇文章认为前沿 AI 模型让找漏洞变得便宜，电脑被入侵会更频繁。EFF 建议每个人更新浏览器与 App、改用密码管理器并提防钓鱼，也主张依赖开源的企业出钱出人维护。自己架网站的人另外要确认 PHP 已修补。
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
  - title: 网络产品安全漏洞管理规定
    url: https://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm
    publisher: 中国政府网
  - title: 更新你的 iPhone 或 iPad
    url: https://support.apple.com/zh-cn/118575
    publisher: Apple 支持（中国）
    date: 2026-09-22
  - title: 查看和更新 Android 版本
    url: https://support.google.com/android/answer/7680439?hl=zh-Hans
    publisher: Android 帮助
authors:
  - anoni-net
---

美国数字权利组织 EFF 10 月 23 日发表两篇文章，认为 OpenAI、Anthropic 等公司的前沿 AI 模型，让找出零日漏洞（厂商还不知道、还没有修补的漏洞）变得便宜又容易。EFF 预期好转之前情况会先变糟，第一篇给普通用户的建议是基本的数字安全习惯，任何地方用电脑与手机的人都适用。第二篇以 PHP 的漏洞为例，主张依赖开源的企业出钱出人维护。网站用 PHP 的话，另外要确认服务器上的 PHP 已经修补 10 月公开的漏洞。

依 EFF 的第二篇，美国国家漏洞数据库（NVD）自 1988 年起收录约 40 万条 CVE（公开漏洞的统一编号），光是 10 月就新提交 1.3 万条。EFF 据此推算历来登记的漏洞有 3% 是在 10 月找到的，也预估到年底时，史上所有漏洞会有超过四分之一出自 2026 年。数字没有附上一手链接，图说列的来源是 CVE Tracker。网络安全公司 Brandefense 10 月 26 日更新的分析列出，NVD 到 10 月 25 日已发布 86,533 条 CVE 记录，2025 年全年是 48,151 条。

EFF 的第二篇以网站服务器上常用的编程语言 PHP 为例，提到它用在将近七成的网站。W3Techs 11 月 2 日的统计是在已知服务端语言的网站里占 69.1%。PHP 项目 10 月 21 日发布 8.5.12、8.4.27、8.3.36、8.2.35，修补两个可让未登录的攻击者在服务器上执行代码的漏洞。

根据资助 PHP 开发的 PHP Foundation 10 月 21 日的说明，2024 年外部出资的第一次审计时已发现问题的迹象，但没有找到具体的攻击方式。EFF 提到维护者当时找不到利用方式，降低了处理的优先级，漏洞一直没有修补。EFF 的说法是，2026 年 8 月研究者用 OpenAI 与 Anthropic 的最新模型各自重新发现，并找到利用的方法。基金会列出的发现者则是网络安全公司 Calif、OpenAI 与 Wiz，Anthropic 的 Claude Mythos 出现在基金会 2026 年稍早扫描 PHP 的段落，没有列为发现者。

EFF 提到撰文时有超过 3,300 万个网站仍在使用有漏洞的 PHP 版本。The New Stack 10 月 27 日引述网络安全公司 Censys 的网络扫描，约 3,250 万个连上互联网的 PHP 服务回报的是不安全的版本，另有约 6,130 万个无法判断版本。同一篇也提醒，Linux 发行版常把修补移植到旧版本而不改版本号。部分算成未修补的服务因此可能已经修补，依版本号推算的数字可能偏高。

依 EFF 的描述，PHP、OpenSSL、SQLite 这些项目几乎在每台电脑上运行，维护团队有的只有一个人。漏洞报告大量涌入，其中有些是假的，但很多是真的。依基金会的说明，PHP 的安全团队 7 月 1 日到 10 月 21 日发布了 15 个 CVE，另外处理了一百多份无效、重复或无法复现的报告。AI 协助验证报告，每个判断与修补仍由人来做。

## 导读观点 {#perspective}

CVE 是给公开漏洞编号的记录，每一条的严重程度不同，EFF 的第二篇把它们都写成严重的漏洞。Help Net Security 6 月报道安全事件响应团队的国际组织 FIRST 对全年 CVE 数量的预测，文中写到部分增长来自 GitHub Security Advisories 与 VulnCheck 扩大编目、补登旧记录。

Brandefense 的同一份分析列出，美国 CISA 的已知被利用漏洞目录（KEV）2026 年到 10 月 23 日新增 272 条，约每千条 CVE 三条。分析也提醒 KEV 收录旧的 CVE，这个比例只能当粗略的参考。依本文的推论，记录增加的倍数不等于被利用的漏洞增加的倍数，但需要安装的修补确实变多了。

在资助开源方面，EFF 主张企业应该投入资金与人力维护它们所依赖的开源项目，没有提出金额、机制或具体的基金。PHP Foundation 对资源的描述跟 EFF 不同，EFF 提到维护靠少数志愿者在空闲时间进行，基金会则表示 PHP 本身的安全工作依靠一小群基金会出资的开发者与少数志愿者。基金会呼吁三类对象支持，分别是用 PHP 开发产品的公司、托管商与云及 Linux 发行版、政府与公共机构。基金会也承认修补延后是结构性的失误，原因出在安全团队的决策流程与资源不足。

EFF 给个人的第一项建议是让浏览器与所有 App 随时更新到最新的修补。EFF 的 Surveillance Self-Defense（SSD，监控自我防卫指南）提到，更新常会修补攻击可利用的旧代码，部分旧的操作系统连安全更新都不再提供。依 Chrome 的说明，有新版时浏览器会在后台自动更新，通常在关闭再重新打开时完成。长时间不关浏览器的话，界面上会出现等待更新的提示。

EFF 也建议安装密码管理器，每个网站各用一组密码，一个网站被入侵时其他账号的密码不受影响。依 SSD 的说明，Apple、Google、Mozilla 内置的密码管理器也可以用。Apple 的“密码”App 默认端到端加密，Google 的密码管理器要自行到设置里用密码短语开启设备端加密。SSD 也列了 Bitwarden、KeePassXC 等独立的密码管理器，并提醒自动填充密码是防范钓鱼的重要保护。

EFF 另外建议考虑安装拦截追踪器的工具，例如 EFF 免费的浏览器扩展 Privacy Badger，10 月 23 日的文章提到它已有 Safari 版。EFF 同一句也提醒要留意钓鱼，SSD 说明钓鱼是用假链接骗取密码。EFF 也提醒数据泄露可能变多，常用的网站可能遭受比平常多的攻击，部分服务可能因此中断。

架设博客或网站的人，EFF 建议确认自己或托管商已经修补 PHP 的漏洞。依 php.net 10 月 21 日的公告，这两个漏洞没有完整的缓解方式，更新是唯一安全的选择。PHP 项目对 7.4、8.0、8.1 另外提供了给从源码构建者用、向旧版本移植的最小修补，其他旧版要看发行版或 LTS 厂商有没有回补。依本文从 EFF 这项建议推论，租用主机的人可以请厂商确认是否已应用这次的修补。

中国大陆的《网络产品安全漏洞管理规定》（工信部联网安〔2021〕66 号，2021 年 9 月 1 日起施行，到 2026 年 10 月 8 日没有查到修订版）要求网络产品提供者发现或获知漏洞后，2 日内向工信部的漏洞信息共享平台报送，并通知上游产品或组件的提供者。公开漏洞信息不得早于提供者给出修补措施，认为有必要提前发布的，须与提供者协商并向工信部、公安部报告。未公开的漏洞信息也不得提供给提供者以外的境外组织或个人。条文没有写明开源项目的维护者算不算网络产品提供者，依本文的推论，开源维护者与研究者发现漏洞时要先对照报送与公开的规定。

Apple 的中国大陆说明页（2026 年 9 月 22 日）内容跟台湾版相同，Android 帮助页的简体中文版也跟正体版相同。在中国大陆销售的 Android 手机如何取得系统更新、停止更新之后官方有什么建议，截至 2026 年 11 月 1 日没有查到官方说明。

每个用电脑与手机的人都适用的第一步，是开启系统与 App 的自动更新，并定期关闭再重开浏览器。iPhone 的位置在“设置”、“通用”、“软件更新”、“自动更新”，依 Apple 的说明会在充电且连上 Wi-Fi 时于夜间安装。Android 的说明则写大部分的安全补丁会自动安装，时间依制造商与运营商而不同，旧款设备可能无法升级。依本文的推论，这些设置挡不住网站本身被入侵造成的数据泄露，各网站用不同的密码能让一处泄露不扩及其他账号。
