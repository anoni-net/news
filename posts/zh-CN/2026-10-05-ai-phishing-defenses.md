---
title: AI 辅助的钓鱼攻击与防范方式
description: Freedom of the Press Foundation 整理 AI 被用在钓鱼攻击的研究，邮件写得更通顺、更个性化，但识别的警讯与防御方式没有改变。建议适用于每个收电子邮件与短信的人。
date: 2026-10-05T07:00:00+08:00
slug: ai-phishing-defenses
sources:
  - title: "Ask a security trainer: Does AI make phishing worse?"
    url: https://freedom.press/digisec/blog/ask-a-security-trainer-does-ai-make-phishing-worse/
    publisher: Freedom of the Press Foundation
    date: 2026-08-27
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
  - title: google.com
    url: https://en.greatfire.org/google.com
    publisher: GreatFire
  - title: Dangerzone
    url: https://github.com/freedomofpress/dangerzone
    publisher: Freedom of the Press Foundation
authors:
  - anoni-net
---

Freedom of the Press Foundation（FPF）的数字安全培训团队 8 月 27 日在专栏回答读者的提问，整理 AI 被用在钓鱼攻击的研究。钓鱼消息不只出现在电子邮件，也会通过短信、二维码、语音与视频通话送达。FPF 的结论是，AI 让钓鱼消息更有说服力，个人该做的防御却没有改变。FPF 列出的做法适用于每个收得到这类消息的人。

FPF 引用了几份报告的数字。KnowBe4 估计 2025 年 10 月到 2026 年 3 月之间，用到 AI 的钓鱼攻击增加约 86%。Verizon 2026 年的数据泄露调查报告中，约 44% 被检测到的事件里，攻击者用生成式 AI 制作钓鱼诱饵作为入侵的第一步。Microsoft 2025 年的报告写到，AI 自动化的钓鱼邮件点击率是 54%，一般的钓鱼邮件是 12%。

研究列出的手法包括自动收集目标的资料、写出更个性化的内容，以及在主题等地方做细微变化来躲过检测，也能写出多种语言的版本。收到的邮件因此看起来像是专门写给收件人，例如冒充同事，或提到收件人可能出席的公开活动。

FPF 列出四个警讯：发件地址跟冒充的对象对不上、链接指向跟服务无关的网址、消息制造压力或紧迫感，以及不请自来的附件。链接可以不点，改成自行输入网址前往。可疑的附件可以先用 Google 云端硬盘预览，或用 Dangerzone 转成安全的副本。FPF 的文章也写到，应开启两步验证。

## 导读观点 {#perspective}

大语言模型擅长模仿特定的语气与用词，靠错字或生硬翻译辨认诈骗消息的做法会越来越不可靠，中文的钓鱼消息也可能写得一样通顺。FPF 的四个警讯都不看文字写得好不好，看的是发件地址、网址、情绪与附件，文字变得通顺之后仍然适用。

验证码本身也可能被骗走。新加坡金融管理局 2024 年 7 月宣布，主要零售银行在三个月内停用登录用的一次性密码（OTP），已启用手机数字令牌的客户改用令牌登录。理由是诈骗集团能架设仿冒的银行网站骗取 OTP。Google 的帮助页面也写到，通行密钥（passkey）无法分享、复制或意外泄露给他人，有助于防范钓鱼式攻击。

现在能做的第一步，是不点消息里要求登录、付款或验证身份的链接，改为自行输入网址或打开官方 App。在海外使用 Google 账号的人，可以替账号添加通行密钥。电脑要 Windows 10、macOS Ventura 以上，手机要 Android 9、iOS 16 以上，iPhone 与 Mac 要先开启 iCloud 钥匙串。帮助页面有简体中文版，添加通行密钥不会移除账号原本的验证与恢复方式。GreatFire 的检测显示，`google.com` 在中国大陆大多被封锁。

经常需要打开陌生附件的人，可以考虑 Dangerzone。它以 AGPL-3.0 授权，7 月发布 0.11.0，支持 Windows、macOS 与 Linux。界面只有英文，Windows 版还需要电脑支持并开启硬件虚拟化。Dangerzone 在没有网络的沙箱里把文件转成像素，再重建成 PDF。代价是转出来的文件没有文字层，要另外开启 OCR 才能搜索与复制文字。
