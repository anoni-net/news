---
title: AI 辅助的钓鱼攻击与防范方式
description: Freedom of the Press Foundation 整理 AI 被用在钓鱼攻击的研究，邮件写得更通顺、更个性化，但识别的危险信号与防御方式没有改变。建议适用于每个收电子邮件与短信的人。
date: 2026-10-05T07:00:00+08:00
slug: ai-phishing-defenses
sources:
  - title: "Ask a security trainer: Does AI make phishing worse?"
    url: https://freedom.press/digisec/blog/ask-a-security-trainer-does-ai-make-phishing-worse/
    publisher: Freedom of the Press Foundation
    date: 2026-08-27
  - title: 2026 Data Breach Investigations Report
    url: https://www.verizon.com/business/resources/T459/reports/2026-dbir-data-breach-investigations-report.pdf
    publisher: Verizon
  - title: Banks in Singapore to Strengthen Resilience Against Phishing Scams
    url: https://www.mas.gov.sg/news/media-releases/2024/banks-in-singapore-to-strengthen-resilience-against-phishing-scams
    publisher: Monetary Authority of Singapore
    date: 2024-07-09
  - title: 使用通行密钥（而非密码）登录
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hans
    publisher: Google
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: So long passwords, thanks for all the phish
    url: https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html
    publisher: Google
    date: 2023-05-03
  - title: Is http://google.com blocked in mainland China?
    url: https://en.greatfire.org/google.com
    publisher: GreatFire
  - title: Is http://github.com blocked in mainland China?
    url: https://en.greatfire.org/github.com
    publisher: GreatFire
  - title: Dangerzone
    url: https://github.com/freedomofpress/dangerzone
    publisher: Freedom of the Press Foundation
authors:
  - anoni-net
---

美国新闻自由组织 Freedom of the Press Foundation（FPF）的数字安全培训团队 2026 年 8 月 27 日在专栏整理 AI 被用在钓鱼攻击的研究。钓鱼消息除了邮件，也会通过短信、二维码、语音与视频通话送达。FPF 的结论是 AI 让钓鱼消息更有说服力，每个人该做的防御却没有改变。

FPF 引用的报告里，安全意识培训公司 KnowBe4 估计 2025 年 10 月到 2026 年 3 月，用到 AI 的钓鱼攻击增加约 86%。Microsoft 2025 年的报告写到，AI 自动化的钓鱼邮件点击率是 54%，一般钓鱼邮件是 12%。

电信公司 Verizon 在 2026 年的数据泄露调查报告分析一家 AI 公司平台上的滥用记录，在攻击者借助 AI 的初始入侵手法里，钓鱼约占 44%（FPF 误写成事件比例）。报告也写到，事件数据里以钓鱼入侵的比例这几年几乎没有变化。

FPF 引用的研究里，自动化的手法包括收集目标信息、写出更个性化的内容、在主题做细微变化躲过检测，以及写出多语言版本。邮件因此像是专门写给收件人，例如冒充同事。

FPF 列出四个危险信号：发件地址与冒充对象不符或只是相似、链接指向跟服务无关的网址、消息制造紧迫感，以及不请自来的附件。链接可以不点，自行输入网址。可疑附件可以用 Google 云端硬盘预览，或用 Dangerzone 转成安全的副本。

## 导读观点 {#perspective}

大语言模型擅长模仿语气，中文钓鱼消息也可能写得通顺。靠错字辨认诈骗会越来越不可靠，四个危险信号都跟文笔无关。

常打开陌生附件的人可以用开源的 Dangerzone（AGPL-3.0 许可证，2026 年 7 月发布 0.11.0）。它在断网的沙箱里把文件转成像素，再到沙箱外重建成没有文字层的 PDF，要开启文字识别（OCR）才能搜索。支持 Windows、macOS 与 Linux，界面只有英文，Windows 版需要电脑支持并开启硬件虚拟化。Windows 与 macOS 版从 GitHub 下载，监测中国网络审查的 GreatFire 把 `github.com` 列为在中国大陆时常受干扰。

FPF 建议的两步验证以手机收到的一次性密码（OTP）为例。新加坡金融管理局与当地银行公会 2024 年 7 月宣布，主要零售银行三个月内逐步停止让已启用数字令牌的客户用 OTP 登录，改由令牌验证。公告的理由是 OTP 容易被骗走，例如仿冒的银行网站。

通行密钥（passkey，用指纹、人脸或锁屏代替密码）同样不必输入可被骗走的代码。Google 的安全博客写到，设备只把登录签名交给 Google 的网站与 App，钓鱼网站拿不到。代价是能解锁设备的人就能登录账号，帮助页面因此写明只在自己专用的设备上创建。

在海外使用 Google 账号的人，第一步可以添加通行密钥（GreatFire 截至 2026 年 9 月 29 日把 `google.com` 列为大多被封锁）。电脑要 Windows 10、macOS Ventura 以上，手机要 Android 9、iOS 16 以上并开启屏幕锁定。浏览器要 Chrome 或 Edge 109、Safari 16、Firefox 122 以上，iPhone 与 Mac 要开启 iCloud 钥匙串。新建的通行密钥可能要 7 天后才能登录，帮助页面有简体中文版。
