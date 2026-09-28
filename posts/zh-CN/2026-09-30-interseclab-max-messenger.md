---
title: 俄罗斯国家通讯 App Max 的技术分析
description: InterSecLab 分析俄罗斯规定预装的通讯 App Max，发现没有端到端加密，VPN 检测、网络探测与语音转文字都能从服务器针对个别账号开启，界面上看不出来。
date: 2026-09-30T07:05:00+08:00
slug: interseclab-max-messenger
sources:
  - title: "The Max Messenger: An Analysis of Russia’s State-Mandated Messaging Application"
    url: https://interseclab.org/research/max/
    publisher: InterSecLab
    date: 2026-09-24
  - title: О включении цифровой платформы Max в список программ для предварительной установки
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

研究监控与审查技术的 InterSecLab 在 9 月 24 日发表报告，分析俄罗斯政府规定预装的通讯 App Max。报告写明 Max 没有端到端加密，运营方 VK 的服务器可以读取每条消息，也没有任何模式能让内容不被运营方读取。研究者分析的是 2026 年 3 到 5 月的 Android 版。预装的规定只在俄罗斯实施。

报告列为最重要的发现，是网络探测、VPN 检测、语音转文字、加强日志等功能都由 VK 的服务器针对一个或一批账号开启。开启时不需要更新 App，界面上也看不出来。网络探测开启时，App 每次打开或切到后台，都会查询设备的公网 IP、检查有没有开 VPN、读取运营商，并测试一串网络服务能否连上。结果全部报告给 VK。

Max 检测到设备上有 VPN 就会停止工作，研究者回复消息时，界面上只有关闭 VPN 的提示，没有其他选项。Max 也会把整份通讯录以明文上传给 VK，语音消息则在 VK 的服务器上转成文字。

俄罗斯政府 2025 年 8 月宣布，Max 从 9 月 1 日起列入电子设备必须预装的软件。CNN 报道，俄罗斯在 2026 年 2 月证实封锁 WhatsApp，并引导民众改用 Max。

报告写明，研究结果不代表 VK 或俄罗斯的政府机关已经对特定的人使用这些功能。研究者在 9 月 25 日更正报告网页，撤回 PDF 里关于「秘密聊天」的说法，因为 Max 没有这项功能，没有端到端加密的结论不受影响。

## 导读观点 {#perspective}

端到端加密的意义，在于连运营方都无法读取内容。Max 没有这一层，每条消息 VK 都能读取。Max 的功能还能由服务器针对账号开关，同一个 App 对不同的人可能做不同的事。用户从界面上无从察觉，外界也只能靠逆向分析发现。

简体中文读者对类似的架构并不陌生，Citizen Lab 2023 年对微信的研究结论是，微信没有端到端加密，腾讯能访问平台上所有消息。中国大陆账号的消息还会被按关键词自动审查，Max 则多了一层政府规定的预装。

不得不在俄罗斯使用 Max 的人，报告的建议是把 VPN 设在路由器上、把 Max 放在独立的 Android 工作资料，或用另一部手机专门安装政府要求的 App。报告也写明，这些做法都无法保护消息内容，因为 VK 以未加密的方式存储消息。

俄罗斯以外的读者不需要做任何设置。面对任何被要求安装的通讯 App，可以先问三件事：有没有端到端加密、功能能不能从服务器远程开关、有没有独立的研究者检验过。敏感的对话，仍然要留给有端到端加密的工具。
