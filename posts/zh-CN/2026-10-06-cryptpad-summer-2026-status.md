---
title: CryptPad 2026 夏季进度与后量子加密的瓶颈
description: 端到端加密协作套件 CryptPad 制定新的安全政策，漏洞修复发布后至少 90 天才公开细节。后量子加密的实验让部分功能慢到难以使用，浏览器内置新的算法之后有望改善。使用公共实例的人无需调整设置，自行搭建的管理员要跟上新版。
date: 2026-10-06T07:00:00+08:00
slug: cryptpad-summer-2026-status
sources:
  - title: Summer 2026 status
    url: https://blog.cryptpad.org/2026/09/15/status-2026-09/
    publisher: CryptPad
    date: 2026-09-15
  - title: 2026.2 security fixes and our new security policy
    url: https://blog.cryptpad.org/2026/06/24/2026.2-security-issues/
    publisher: CryptPad
    date: 2026-06-24
  - title: CryptPad Security Policy
    url: https://cryptpad.org/security/
    publisher: CryptPad
    date: 2026-06-23
  - title: Winter fix release (2026.2.1)
    url: https://github.com/cryptpad/cryptpad/releases/tag/2026.2.1
    publisher: GitHub
    date: 2026-03-27
  - title: Spring fix release (2026.5.1)
    url: https://github.com/cryptpad/cryptpad/releases/tag/2026.5.1
    publisher: GitHub
    date: 2026-05-26
  - title: Summer 2025 status
    url: https://blog.cryptpad.org/2025/09/05/status-2025-08/
    publisher: CryptPad
    date: 2025-09-05
  - title: Modern Algorithms in the Web Cryptography API
    url: https://wicg.github.io/webcrypto-modern-algos/
    publisher: WICG
    date: 2026-09-14
  - title: "CryptPad: Collaboration suite, encrypted and open-source"
    url: https://cryptpad.fr/
    publisher: CryptPad
  - title: Security
    url: https://docs.cryptpad.org/en/user_guide/security.html
    publisher: CryptPad
  - title: User Account
    url: https://docs.cryptpad.org/en/user_guide/user_account.html
    publisher: CryptPad
  - title: Support
    url: https://docs.cryptpad.org/en/user_guide/support.html
    publisher: CryptPad
  - title: Public instances
    url: https://cryptpad.org/instances/
    publisher: CryptPad
  - title: Chinese (Traditional Han script)
    url: https://weblate.cryptpad.org/projects/cryptpad/app/zh_Hant/
    publisher: CryptPad Weblate
  - title: Chinese (Simplified Han script)
    url: https://weblate.cryptpad.org/projects/cryptpad/app/zh_Hans/
    publisher: CryptPad Weblate
  - title: cryptpad.fr/api/config
    url: https://cryptpad.fr/api/config
    publisher: CryptPad
  - title: Is https://cryptpad.fr blocked in mainland China?
    url: https://en.greatfire.org/https/cryptpad.fr
    publisher: GreatFire
    date: 2026-09-18
  - title: https://cryptpad.fr（GreatFire API）
    url: https://en.greatfire.org/api/url/https/cryptpad.fr
    publisher: GreatFire
    date: 2026-09-18
  - title: Is https://github.com blocked in mainland China?
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
    date: 2026-09-27
authors:
  - anoni-net

---

CryptPad 于 9 月 15 日发布夏季进度报告，介绍新安全政策、后量子加密研究与客服变动。CryptPad 是开源（AGPL-3.0）的端到端加密协作套件，可以在浏览器里协同编辑文档与电子表格，使用公共实例（向公众开放的服务器）或自行搭建。使用公共实例的人无需调整设置，自行搭建的管理员要留意升级。

按 6 月公布的新安全政策，漏洞修复发布后至少保密 90 天才公开 CVE（通用漏洞编号），让管理员有时间升级。严重程度改用 CVSS 4.0（漏洞严重度评分）。版本说明不列出修复的漏洞，只标出最高的 CVSS 分数与升级提醒，推荐的版本一律是最新版（每季度发布）。

据 6 月的事后复盘，服务器此前没有限制 WebSocket 连接的发送频率，有人反复发送大量消息就能耗尽资源。官方实例 cryptpad.fr 在 1 月 28 日因此遭到分布式拒绝服务攻击，修复收录在 3 月 27 日发布的 2026.2.1。当时的政策没有写清楚保密期，CVE 在 2026.2.1 发布后第 34 天就公开了。

后量子加密（能抵御量子计算机的算法）方面，团队选定美国标准机构 NIST 的 ML-KEM（用于交换密钥）与 ML-DSA（用于数字签名）。实验中两者与原有的公钥加密混合使用，部分功能因此慢到难以使用。浏览器内置的 Web Cryptography API 有草案要加入这两种算法，据进度报告估计，速度约是外部库的 100 倍。

进度报告写明客服团队已没有会说法语的成员，cryptpad.fr 将停止提供法语客服。秋季版会包含相当于两个版本的改进。

## 导读观点 {#perspective}

按用户指南，实例运行与 GitHub 公开版本相同的代码等前提都成立时，管理员无法读取或修改在浏览器里加密的文档。用户指南也写明匿名性较弱，管理员能看到用户的 IP 地址与浏览器信息，需要时可以通过 Tor 连接。

Web Cryptography API 的草案由 WICG（W3C 孵化新规范的社区小组）维护，截至 9 月 29 日尚未进入 W3C 的正式标准流程。浏览器实现后，后量子版的 CryptPad 可能比较可行。团队已先把程序改成可替换加密库的架构（密码敏捷性，crypto-agility）。

截至 9 月 29 日的 90 天内，GreatFire（监测中国网络审查的网站）只在 9 月 18 日测试过 `https://cryptpad.fr`，结果是连接被拒绝。GreatFire 自 8 月底起不把这种结果算作封锁的证据，所以判定未封锁。编辑时还要连到 `api.cryptpad.fr` 与 `sandbox.cryptpad.info`，GreatFire 都未测过。能否在中国大陆正常使用，因此还缺乏可靠的测量数据。

公共实例列表只收录通过检查、版本最新的实例。自行搭建的管理员可以按事后复盘的建议更新 nginx 的频率限制，截至 9 月 29 日最新版是 5 月 26 日的 2026.5.1。搭建时要从 GitHub 下载源代码与新版。截至 9 月 27 日的 90 天内，GreatFire 对 GitHub 的 54 次有明确结果的测试有 69% 受到干扰。

打开 cryptpad.fr 或列表上的其他实例就能试用，不注册也能协同编辑，但文档连续 3 个月未使用就不再保留。截至 9 月 29 日，列表上的 13 个实例都在欧洲与北美。注册只需要用户名与密码，无需邮箱，但忘记密码就无法重置。界面有简体与正体中文，用户指南没有中文版，客服页面会标出管理员的语言。
