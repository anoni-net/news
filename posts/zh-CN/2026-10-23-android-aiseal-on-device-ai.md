---
title: Android 17 端侧 AI 的隔离执行环境 AISeal
description: Google 10 月 7 日说明 Android 17 的 AISeal，把端侧 AI 使用的个人数据放进跟操作系统隔离的受保护虚拟机。依公告，第一阶段推出的是个人数据的存储，模型推理与 AI 智能体要等之后。到 10 月 20 日为止，Google 没有公布哪些机型、哪些地区已经启用，Google 的公告与帮助页没有提到用户需要调整的设置。
date: 2026-10-23T00:00:00+08:00
slug: android-aiseal-on-device-ai
categories:
  - mobile
sources:
  - title: Android's Next-Gen Enclave for On-Device AI
    url: https://blog.google/security/enabling-the-next-gen-enclave-architecture-for-on-device-ai-on-android/
    publisher: Google
    date: 2026-10-07
  - title: Android Virtualization Framework (AVF) overview
    url: https://source.android.com/docs/core/virtualization
    publisher: Android Open Source Project
  - title: Security
    url: https://source.android.com/docs/core/virtualization/security
    publisher: Android Open Source Project
  - title: Android’s pKVM Becomes First Globally Certified Software to Achieve Prestigious SESIP Level 5 Security Certification
    url: https://blog.google/security/android-pkvm-certified-sesip-level-5/
    publisher: Google
    date: 2025-08-12
  - title: core/java/android/aiseal - platform/frameworks/base - Git at Google
    url: https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-17.0.0_r1/core/java/android/aiseal/
    publisher: Android Open Source Project
  - title: Private Compute Services
    url: https://github.com/google/private-compute-services
    publisher: Google
  - title: Gemini Nano
    url: https://developer.android.com/ai/gemini-nano
    publisher: Android Developers
  - title: Android On-Device AI Gets a Security Bump With "Next-Gen" Enclaves
    url: https://www.privacyguides.org/news/2026/10/09/android-on-device-ai-gets-a-security-bump-with-next-gen-enclaves/
    publisher: Privacy Guides
    date: 2026-10-09
  - title: Google is building a “black box” for Android AI, but the agents aren’t inside yet
    url: https://www.digitaltrends.com/phones/google-is-building-a-black-box-for-android-ai-but-the-agents-arent-inside-yet/
    publisher: Digital Trends
    date: 2026-10-08
  - title: Android 17 Built a Sealed Room for On-Device AI
    url: https://blog.logcat.ai/2026/06/25/android-17-built-a-sealed-room-for-on-device-ai/
    publisher: logcat.ai
    date: 2026-06-25
  - title: Gemini mobile app availability
    url: https://support.google.com/gemini/answer/14579026?hl=en
    publisher: Google
  - title: Where you can use the Gemini web app
    url: https://support.google.com/gemini/answer/13575153?hl=en
    publisher: Google
authors:
  - anoni-net
---

Google 10 月 7 日在官方博客说明 Android 17 的 AISeal（Android on-device AI seal），把端侧 AI 会用到的个人数据，放进一个跟 Android 操作系统隔离的受保护虚拟机。依公告，设计目标是即使整个操作系统被入侵，个人数据仍然保持加密隔离。第一阶段推出的只有个人数据的存储，模型推理与 AI 智能体（代替用户执行多步骤任务的 AI）要等之后。到 10 月 20 日为止，Google 没有公布哪些机型、哪些地区已经启用，Google 的公告与帮助页没有提到用户需要调整的设置。

根据公告，AISeal 建立在 Android 虚拟化框架（AVF）与 pKVM 这个虚拟机监控程序（hypervisor，负责切分与隔离虚拟机的底层软件）上。这个受保护的空间在设计上可以同时放三类服务，包括加密的个人数据库、在设备上运行的模型推理，以及结合两者的 AI 智能体。公告举的例子是助手在隔离空间里查询个人数据库、整理日程摘要，对外的管控设计成只让最后的答案回到操作系统，这要等推理移进 AISeal 之后才做得到。Android 开源项目（AOSP）的说明文档写到，即使主系统（host，也就是平常运行 App 的 Android）被入侵，主系统也读不到受保护虚拟机的内存。

芯片方面，公告提到 MediaTek 的 Dimensity 9600 Pro 已宣布支持，Qualcomm 的 Snapdragon 也会通过 AVF 支持。pKVM 本身 2025 年取得 SESIP（一套信息安全评估制度）第 5 级的认证，公告称这是 ISO 15408 下最高的漏洞测试等级（公告没有写 AISeal 本身通过认证）。依 Android 17 标签的源代码，AOSP 已经包含 AISeal 的框架。依同一份源代码，服务默认关闭，要把设备属性 `service.aiseal.enable` 设为 1 才会启用（依本文的推论由手机厂商设置）。

## 导读观点 {#perspective}

Android 既有的隔离是 App 沙箱、SELinux 规则，以及 Private Compute Core。根据 Private Compute Services 的说明，Private Compute Core 里的功能不能直接联网，只能通过一组开源的 API 对外。AISeal 多加的一层是虚拟机监控程序切出的内存隔离。AVF 的安全文档列出，pKVM 在虚拟机监控程序那一层运行的部分约 1 万行，整个 Linux 内核约 2,000 万行（攻击面小了三个数量级）。

同一份安全文档提到，手机厂商与芯片厂商这些经手供应链的企业仍然要被信任，主系统可以影响虚拟机能不能正常运行。文档也写到，加密存储没有块级别的防回滚保护（无法察觉加密数据被换回旧的版本）。这些是 pKVM 与受保护虚拟机的设计限制，依本文的推论，建立在上面的 AISeal 同样适用。

分析 Android 17 源代码的一篇技术博客提到，数据在存进 AISeal 之前的收集当下主系统仍然看得到。同一篇也提到，AISeal 没有把数据跟用户选用的 AI 服务提供商隔开。

Android 17 标签的源代码显示，AISeal 的管理接口需要 `signature|privileged` 权限，依本文的推论一般第三方 App 无法取得。开发者可以用的 Gemini Nano 是 Google 的端侧模型，运行在 AICore 这个负责管理端侧模型的系统服务里，公告把 AICore 与 AISeal 的整合写成未来的计划。Digital Trends 的报道提醒，芯片支持 AISeal 不代表手机上的助手真的在 AISeal 里运行，要看手机厂商如何实现。

AISeal 启用的机型、国家与语言，Google 的公告、AOSP 文档与相关报道都没有列出。作为同一家公司服务的对照，到 10 月 20 日为止 Google 帮助页列出的 Gemini 移动 App 支持地区包括香港、澳门、台湾、日本、韩国与新加坡，没有中国大陆（网页版在中国大陆只限 Workspace 账号使用）。Gemini 可以使用的地区不能拿来推论 AISeal 的地区。

读者现在不需要调整任何设置，到 10 月 20 日为止，Google 的公告与帮助页也没有提到给用户的开关。可以留意的是 Google 或手机厂商何时公布启用的机型与地区，以及模型推理与 AI 智能体什么时候移进 AISeal。

依 Digital Trends 的提醒推论，之后选购手机时，可以看厂商的规格与说明页有没有写明 AI 功能在 AISeal 里运行。依前述技术博客的分析，即使在 AISeal 里运行，数据收集的当下与用户选用的 AI 服务提供商仍然不在隔离的范围内。
