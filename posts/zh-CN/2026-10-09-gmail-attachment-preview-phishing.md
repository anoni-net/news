---
title: 冒充 Gmail 附件预览的钓鱼邮件
description: Cisco Talos 披露一批发给台湾学术界、智库与公民社会政策社群的钓鱼邮件。邮件用图片在正文仿制 Gmail 的附件卡片，点击后会在 Windows 电脑上启动感染。在浏览器打开时假卡片与真附件几乎分不出来，经常收到演讲邀请或机构来信的人可以留意。
date: 2026-10-09T00:10:00+08:00
slug: gmail-attachment-preview-phishing
categories:
  - security
sources:
  - title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
    url: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
    publisher: Cisco Talos
    date: 2026-09-30
  - title: 中國駭客UAT-11587鎖定臺灣學術界與智庫，以圖片仿製Gmail附件預覽介面並用政府文件作為誘餌
    url: https://www.ithome.com.tw/news/179344
    publisher: iThome
    date: 2026-10-01
  - title: 防範及檢舉網路釣魚電子郵件
    url: https://support.google.com/mail/answer/8253?hl=zh-Hant
    publisher: Google
  - title: 在 Gmail 中開啟及下載附件
    url: https://support.google.com/mail/answer/30719?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 檢查 Gmail 郵件是否通過驗證
    url: https://support.google.com/mail/answer/180707?hl=zh-Hant
    publisher: Google
  - title: Google 最強大的安全防禦機制，可確保私人資訊的安全。
    url: https://landing.google.com/intl/zh-TW/advancedprotection/
    publisher: Google
  - title: 進階保護計畫常見問題
    url: https://support.google.com/accounts/answer/7539956?hl=zh-Hant
    publisher: Google
  - title: 防范和举报钓鱼邮件
    url: https://support.google.com/mail/answer/8253?hl=zh-Hans
    publisher: Google
  - title: 打开和下载 Gmail 中的附件
    url: https://support.google.com/mail/answer/30719?hl=zh-Hans&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 检查 Gmail 邮件是否通过身份验证
    url: https://support.google.com/mail/answer/180707?hl=zh-Hans
    publisher: Google
  - title: 关于高级保护计划的常见问题
    url: https://support.google.com/accounts/answer/7539956?hl=zh-Hans
    publisher: Google
  - title: Gmail and Google Search access blocked in China
    url: https://www.pbs.org/newshour/world/gmail-access-blocked-china
    publisher: PBS NewsHour
    date: 2014-12-29
  - title: Gmail gets burned by China's 'Great Firewall'
    url: https://www.csmonitor.com/Technology/2014/1229/Gmail-gets-burned-by-China-s-Great-Firewall
    publisher: CSMonitor
    date: 2014-12-29
  - title: Is https://mail.google.com blocked in mainland China?
    url: https://en.greatfire.org/https/mail.google.com
    publisher: GreatFire
regions:
  - TW
authors:
  - anoni-net
---

Cisco Talos 在 9 月 30 日公开一份网络间谍活动的报告，代号 UAT-11587。据报告的内容，2026 年 3 月有一批鱼叉式网络钓鱼邮件（针对特定对象量身写成的钓鱼邮件）发给台湾学术界、智库与公民社会的政策社群。邮件在正文用图片仿制了 Gmail 的附件预览，点击后会在 Windows 电脑上启动感染流程。Talos 写明，在浏览器打开 Gmail 时，假卡片与真正的附件预览在外观上几乎分不出来。

Talos 的报告写到，攻击者用四张内嵌的 PNG 图片拼出 Gmail 附件卡片的样式，再把整张卡片做成链接。链接指向攻击者控制的 Cloudflare Pages 网址，点击后会下载一个 HTA 文件（由 Windows 的 mshta.exe 执行的程序文件）。接着经过五个阶段的感染，最后放入以 Rust 写成的后门 Antino。过程中会打开一份 PDF 诱饵文档给受害者看，后门则在后台安装。

Talos 公布的邮件样本以繁体中文写成，邀请收件人担任工作坊讲师，信中写课程约 50 分钟、讲师费 3,500 元。Talos 取得的诱饵文档之一是以“Taiwan Information Warfare”为题的工作坊说明，Talos 写明另一份完整复制了台湾财政部公开的函释《立法委员行使职务支领之各项费用征免税原则》。Talos 也写到，邮件显示的发件人冒用收件人信任的机构。

Talos 检视的一封邮件用攻击者自己的域名作为信封上的发件人，通过了 SPF 验证，但没有通过 DMARC 验证。SPF 与 DMARC 都是收件端核对发件域名的机制。被冒用机构的域名把 DMARC 策略设为不强制执行，所以邮件仍然送达。

Talos 从 2025 年 9 月开始观察 UAT-11587 的活动。到 2026 年 7 月为止，Talos 找到至少 16 个受害或被锁定的机构，约 350 个受感染的终端（电脑或服务器）。Talos 以中到高的置信度评估，锁定的对象分布在台湾、印度、菲律宾、柬埔寨、巴基斯坦、泰国、缅甸与叙利亚八个国家和地区，包括政府、外交、国防、立法机关、智库、大学与公民社会组织。Talos 也以高置信度评估攻击者与中国有关联（原文为 China-nexus）。

## 导读观点 {#perspective}

Talos 的报告写到，Gmail 在浏览器显示邮件时照实呈现了攻击者写的 HTML，所以正文里的图片可以长得与附件卡片一样。iThome 的报道写到假卡片放在邮件正文下方，Gmail 帮助页写的真正附件则在邮件底部。本文推论两者都在邮件下半部，单看位置不容易分辨。据 Gmail 帮助页，将鼠标悬停在真正的附件上时，会出现“下载”与“添加到云端硬盘”图标。

本文从帮助页写的悬停图标推论，鼠标悬停在卡片上却没有出现“下载”与“添加到云端硬盘”图标的，可能只是正文里的图片链接。本文没有实测，Gmail 改版后也可能不适用。推论只适用于电脑版，Talos 的报告没有写手机上的显示情况。Gmail 帮助页另外建议在电脑上点击链接前先悬停查看网址，网址与链接说明不匹配时，链接可能导向钓鱼网站。

据 Gmail 帮助页，点击发件人名字下方的向下箭头时，通过身份验证的邮件会显示“发件人”与“签名者”两个标头和对应的域名。没有通过身份验证时，发件人名字旁会出现问号。帮助页写明邮件通过 SPF 或 DKIM 任一项就算通过验证，Talos 检视的那封邮件 SPF 通过，本文推论可能不会出现问号。

展开后的“发件人”标头（英文界面为 Mailed by，与邮件顶端的发件人名字不同）显示发送邮件的域名，本文推论可以比对它与邮件中自称的机构是否一致。到 10 月 7 日为止，帮助页没有写 DMARC 验证失败的邮件会如何显示。

经常收到演讲邀请、公文或机构来信的人，可以特别留意假附件卡片的手法。收到可疑邮件时，电脑版 Gmail 可以在“回复”图标旁的“更多”图标点击“举报钓鱼邮件”。

据 Google 的说明，容易成为针对性网络攻击目标的人可以加入“高级保护计划”，到 10 月 7 日为止免费使用。登录时一律要用通行密钥或安全密钥，Chrome 下载文件前也会做更严格的检查。代价是要准备通行密钥或另外购买安全密钥，需要应用专用密码的应用会无法使用。到 10 月 7 日为止，Google 的帮助页没有写高级保护计划能否挡下正文里的假附件卡片。

据 PBS 与 CSMonitor 2014 年 12 月 29 日的报道，Google 透明度报告显示 Gmail 在中国的流量在 2014 年 12 月底降到接近零，CSMonitor 也写到使用 VPN 仍然可以连接。长期测量防火长城的 GreatFire 显示，到 2026 年 10 月 1 日的最后一次测试为止，mail.google.com 在中国大陆完全受到干扰。上面的辨识方式适用于能连上 Gmail 的读者，例如在海外使用的人。到 10 月 7 日为止，本文没有查到翻墙工具现在能否连上 Gmail。
