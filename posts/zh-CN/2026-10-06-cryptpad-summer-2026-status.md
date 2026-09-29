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

CryptPad 于 9 月 15 日发布夏季进度报告，介绍新的安全政策、后量子加密研究与官方实例 cryptpad.fr 的客服变动。CryptPad 是采用 AGPL-3.0 许可证的端到端加密协作套件，在浏览器里协同编辑文档与电子表格，可以使用公共实例或自行搭建。使用公共实例的人无需调整设置，自行搭建的管理员要留意升级。

新的安全政策于 6 月公布。漏洞修复发布之后，至少保密 90 天才公开 CVE（公开的漏洞编号），让实例及时升级。严重程度改用 CVSS 4.0 评分。政策也写明版本说明不列出修复的漏洞，只标出最高的 CVSS 分数与升级提醒，推荐的版本一律是每季度的最新版。

据 6 月的事后复盘，服务器此前没有限制 WebSocket 连接的发送频率，反复发送帧就能耗尽资源。cryptpad.fr 在 1 月 28 日因此遭到分布式拒绝服务攻击，修复收录在 3 月 27 日发布的 2026.2.1。当时的政策没有写清楚保密期，CVE 在发布后第 34 天就公开了。

后量子加密（能抵御量子计算机攻击的加密算法）方面，团队选定 NIST 标准化的 ML-KEM 与 ML-DSA，在实验中以混合方式替换原有的公钥加密。多数功能运行正常，部分功能却慢到难以使用。浏览器的 Web Cryptography API 有一份加入这两种算法的草案，进度报告写到预计比外部库快两个数量级。

进度报告写明客服团队已经没有会说法语的成员，cryptpad.fr 将停止提供法语支持。秋季版会包含两个版本分量的改进。

## 导读观点 {#perspective}

使用说明列出的信任前提包括实例运行与 GitHub 公开版本相同的代码，前提都成立时，在浏览器里加密的文档无法由管理员读取或修改。使用说明也写明 CryptPad 的匿名性较弱，实例管理员能看到用户的 IP 地址与浏览器，需要时可以通过 Tor 连接。

WICG（W3C 孵化新规范的社区小组）的草案（9 月 14 日版）截至 9 月 29 日还不在 W3C 的标准流程上，浏览器支持之后，后量子版本的 CryptPad 可能比较容易实现。团队已先把程序改成可替换加密库的架构（crypto-agility）。

GreatFire（监测中国网络审查的网站）判定 `https://cryptpad.fr` 未被封锁，依据只有 9 月 18 日的一次测试。那次连接遭拒，GreatFire 自 8 月底起不再把连接遭拒算作封锁的证据。编辑时还要连到 `api.cryptpad.fr` 与 `sandbox.cryptpad.info`（见实例的公开配置），GreatFire 都未测过。能否在中国大陆正常使用，截至 9 月 29 日仍没有可靠的量测。

公共实例列表只收录通过检查、版本最新的实例。自行搭建的管理员，可以按事后复盘更新 nginx 的频率限制设置。截至 9 月 29 日，GitHub 上最新的正式版是 5 月 26 日发布的 2026.5.1。截至 9 月 27 日的 90 天内，GreatFire 对 `https://github.com` 的 54 次有结论测试中，69% 受到干扰。

用浏览器打开 cryptpad.fr 或列表上的其他实例就能开始试用，不注册也能协同编辑，但文档连续 3 个月没有使用就不再保留。截至 9 月 29 日，列表上的 13 个实例都在欧洲与北美。注册只需要用户名与密码，不需要邮箱，但遗失的密码无法重置。界面有简体与正体中文，使用说明没有中文版，客服页面会列出管理员使用的语言。
