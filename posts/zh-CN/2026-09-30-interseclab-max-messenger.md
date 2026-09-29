---
title: 俄罗斯国家通讯 App Max 的技术分析
description: InterSecLab 分析俄罗斯规定预装的通讯 App Max，发现它没有端到端加密。VPN 检测、网络探测与语音转文字都能从服务器针对个别账号切换，界面上没有任何提示。预装规定只在俄罗斯实施。
date: 2026-09-30T07:05:00+08:00
slug: interseclab-max-messenger
sources:
  - title: "The Max Messenger: An Analysis of Russia’s State-Mandated Messaging Application"
    url: https://interseclab.org/research/max/
    publisher: InterSecLab
    date: 2026-09-24
  - title: Правительство включит новые цифровые продукты в перечень программ для обязательной предустановки
    url: http://government.ru/docs/55977/
    publisher: Правительство России
    date: 2025-08-21
  - title: Russia says it has blocked WhatsApp amid wider clampdown on social media
    url: https://www.cnn.com/2026/02/12/tech/russia-whatsapp-social-media-clampdown-intl
    publisher: CNN
    date: 2026-02-12
  - title: "Should We Chat? Privacy in the WeChat Ecosystem"
    url: https://citizenlab.ca/2023/06/privacy-in-the-wechat-ecosystem-full-report/
    publisher: Citizen Lab
    date: 2023-06-28
regions:
  - RU
authors:
  - anoni-net
---

数字安全实验室 InterSecLab 在 9 月 24 日发表报告，分析俄罗斯政府规定预装的通讯 App Max。报告写明 Max 没有端到端加密，开发 Max 的俄罗斯互联网公司 VK 可在服务器上读取每条消息。研究者在 2026 年 3 到 5 月间分析 Android 版 `26.12.0`，结果只代表这个版本。预装规定只适用于俄罗斯销售的手机与平板，俄罗斯以外的读者不受影响。

俄罗斯政府 2025 年 8 月宣布，Max 从 2025 年 9 月 1 日起列入电子设备必须预装的软件。CNN 报道，俄罗斯在 2026 年 2 月证实封锁 WhatsApp，并引导民众改用 Max。据报告，使用政府服务越来越常需要 Max。

报告最重要的发现是，VK 的服务器可以针对一个或一批账号，切换网络探测、VPN 检测、语音转文字等功能。切换时不需要更新 App，界面上也没有提示。网络探测开启后，App 每次启动或切换到后台都会查询设备的公网 IP、检查是否启用 VPN、读取运营商，再上报给 VK。

Max 检测到 VPN 就停止工作。研究者尝试回复消息时，屏幕只剩关闭 VPN 的提示。检测只看设备本身，路由器上的 VPN 不会被发现。

Max 也会把整份通讯录以明文上传给 VK。语音消息则在服务器而非手机上转成文字。

研究者 9 月 25 日在报告页刊出更正，Max 的界面上没有「秘密聊天」这项功能，1.1 版 PDF 已在 9 月 28 日改写相关段落。没有端到端加密的结论不受影响，依据是在 App 内截获的明文消息。

## 导读观点 {#perspective}

端到端加密让运营方也无法读取消息内容，Max 没有这项保护。Max 的功能又能由服务器针对账号切换，同一版 App 在不同账号上的行为可能不同。研究者只能看到测试账号收到的设置，也未收集到 VK 或任何俄罗斯国家机关对特定人士使用这些功能的证据。

多伦多大学的研究室 Citizen Lab 在 2023 年的微信报告写明，微信的聊天消息没有端到端加密，腾讯能看到所有消息。用中国大陆手机号注册的账号，消息会被按关键词自动审查。据同一份报告引述的研究，大陆以外账号的消息也被用来训练审查算法。Citizen Lab 报告的建议是收紧 App 权限、定期更新系统，但高风险用户无法靠这些调整确保安全。

报告的建议是不要用 Max 发送敏感内容，装了 Max 的人应假设内容都能被 VK 读取。报告也列出不得不使用 Max 时的三种做法，把 VPN 设在路由器上、把 Max 装进 Android 的独立用户或资料（profile），或用另一部手机装政府要求的 App。三种做法能让翻墙工具照常工作，但 VK 存储的消息未经加密，内容仍无保护。

俄罗斯以外的读者不需要做任何设置。可以留意报告的俄文译本，以及下一版报告对服务器端设置何时生效的修正。
