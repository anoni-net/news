---
title: Brave Leo 的端到端加密对话与机密计算
description: Brave 的 AI 助手 Leo 10 月 15 日起，选用 GLM 5.3 Flash 模型的对话会在浏览器端加密，只在硬件隔离的计算区里解密处理。其他模型不在范围内，计算区的证明到 10 月 20 日为止仍由 Brave 的服务器代为检查，iOS 版查不到支持的说明。
date: 2026-10-21T00:00:00+08:00
slug: brave-leo-e2ee-confidential-computing
categories:
  - encryption
sources:
  - title: "Another Brave User-First AI Win: Leo adds End-to-end Encryption, Oblivious HTTP, and Verifiable Confidential Computing"
    url: https://brave.com/blog/browser-ai-e2ee/
    publisher: Brave
    date: 2026-10-15
  - title: near-tee-verifier
    url: https://github.com/brave/near-verifier
    publisher: GitHub
  - title: "[AI Chat] Add support for end-to-end encryption with NEAR models"
    url: https://github.com/brave/brave-browser/issues/55247
    publisher: GitHub
    date: 2026-05-05
  - title: What are the differences between Leo's AI Models?
    url: https://support.brave.app/hc/en-us/articles/26727364100493
    publisher: Brave
  - title: Brave Leo AI
    url: https://brave.com/leo/
    publisher: Brave
  - title: "Verifiable Privacy and Transparency: A new frontier for Brave AI privacy"
    url: https://brave.com/blog/browser-ai-tee/
    publisher: Brave
    date: 2025-11-20
  - title: GLM-5.3-Flash
    url: https://huggingface.co/zai-org/GLM-5.3-Flash
    publisher: Hugging Face
  - title: brave_components_resources_zh-TW.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-TW.xtb
    publisher: GitHub
  - title: Brave adds end-to-end encryption to chats with AI assistant Leo
    url: https://cyberinsider.com/brave-adds-end-to-end-encryption-to-chats-with-ai-assistant-leo/
    publisher: CyberInsider
    date: 2026-10-16
  - title: "TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition"
    url: https://tee.fail/
    publisher: TEE.fail
  - title: brave_components_resources_zh-CN.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-CN.xtb
    publisher: GitHub
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: Is https://laptop-updates.brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/laptop-updates.brave.com
    publisher: GreatFire
  - title: OONI API
    url: https://api.ooni.org/api/v1/measurements?probe_cc=CN&test_name=web_connectivity&domain=ai-chat.bsg.brave.com&since=2026-07-20&until=2026-10-20
    publisher: OONI
  - title: iTunes lookup API (cn)
    url: https://itunes.apple.com/lookup?id=1052879175&country=cn
    publisher: Apple
  - title: iTunes lookup API (tw)
    url: https://itunes.apple.com/lookup?id=1052879175&country=tw
    publisher: Apple
authors:
  - anoni-net
---

Brave 10 月 15 日宣布，AI 助手 Leo 跟 GLM 5.3 Flash 模型的对话改成端到端加密，GLM 5.3 Flash 是智谱（Z.ai）以 MIT 许可证公开权重的模型。对话在浏览器端加密，只在 NEAR AI 运营的可信执行环境（TEE，处理器与 GPU 里跟主机其他部分隔离的计算区）里解密与生成回答。加密要在 Leo 的模型菜单手动选 GLM 5.3 Flash 才会生效，Leo 的其他模型不在范围内，到 10 月 20 日为止 GLM 5.3 Flash 也还标示为测试阶段。依博客，正式版与 Nightly、Beta 两个测试通道都已提供，所有 Brave 用户都能选用。

博客没有写支持哪些平台。GitHub 上的开发议题只标了桌面版与 Android，iPhone 版到 10 月 20 日为止查不到支持的说明。

依 Brave 的博客，浏览器用互联网标准组织 IETF 制定的 Oblivious HTTP（OHTTP）加密每一条提问与分享给 Leo 的网页，解密用的密钥只存在 TEE 里。加密后的消息先送到 Brave 自己运营的 AI Gateway，再转给 NEAR AI。Brave 看得到用户的 IP 地址、读不到内容，NEAR AI 运营的 TEE 在计算区里解密、看不到 IP 地址，博客也提到 NEAR AI 与云主机的运营者都读不到计算区的内容。每一轮对话都用新的一次性密钥重新加密整段记录，记录只存在用户的设备上，Brave 与 NEAR AI 都不保存。

博客接着说明部署前的检查，NEAR AI 的每一次部署都要先通过 Brave 检查程序的检查才会被批准。检查的项目包括 Intel 与 Nvidia 签署的证明（attestation，由硬件签署、证明计算区是真品并记录里面运行哪一份程序的凭据），以及从源代码重新构建、确认跟线上的程序一致。AI Gateway 转发每一条消息前会再核对一次，采用的验证结果不超过一小时，不通过就不转发。检查程序 `near-tee-verifier` 以开源许可证公开，有 NEAR AI 的 API 密钥就能自行对线上服务运行验证。

Brave 2025 年 11 月在 Nightly 试行过第一版，博客提到当时的保护建立在政策上，检查也要信任 Brave。新版的检查程序公开，有 API 密钥就能自行运行。到 10 月 20 日为止，浏览器端的检查仍由 Brave 的服务器代为处理。

到 10 月 20 日为止，帮助中心没有 GLM 5.3 Flash 端到端加密的文章。Leo 的模型说明页列的仍是 GLM 4.7 Flash，也写所有模型都由 Brave 自行运营。开发议题标了不列入版本记录，各平台的版本记录都没有提到端到端加密。

## 导读观点 {#perspective}

一般的 AI 对话服务在服务器上解开提问，运营者在技术上读得到内容，用户只能相信隐私政策。OHTTP 把「谁在问」跟「问了什么」拆给两方，转发的一方只知道 IP 地址，处理的一方只看到内容。TEE 的设计是让主机的运营者也读不到计算区的内存，attestation 让外界确认里面运行的是公开过的程序。Brave 的博客把 Leo 的新做法描述成从政策承诺改成密码学的证明。

根据博客，10 月 15 日发布时浏览器仍依赖 Brave 的 AI Gateway 做检查，之后才会分阶段改成由浏览器直接验证硬件的证明。博客也列出整条验证链最后要信任的对象，包括 Intel 与 Nvidia、TEE 的操作系统 dstack、构建记录的 Sigstore、GitHub、Hugging Face 与公共 DNS。`near-tee-verifier` 的说明则提醒，重新构建只证明线上程序来自指定的版本，不能证明那个版本里没有后门。运行模型的推理软件是第三方软件包，依博客与 `near-tee-verifier` 的说明没有从源代码重新构建，改用硬件证明的部署记录锁定版本。

安全会议 IEEE S&P 2026 收录的论文 TEE.fail 中，研究者在服务器的 DDR5 内存总线接入监听装置，在部分情况下取出 Intel TDX（Intel 处理器上的 TEE 技术）签署证明用的密钥。用这把密钥伪造的证明可以通过验证，也能用来攻破 Nvidia GPU 的机密计算。依研究网站，攻击需要物理接触服务器，Intel 不把这类物理攻击列入 TDX 要防范的范围。研究者也写到，就他们所知还没有被实际利用。

研究网站另有一节演示 dstack，恶意的服务器提供者可以伪造全部证明，也能借用别处 Nvidia GPU 的证明。网站给 dstack 用户的建议是留意自己要信任实际管理 TDX 硬件的运营者。论文没有分析 Brave 与 NEAR AI 的部署，本文 10 月 20 日搜索时也没有找到针对 Leo 的独立分析。

依 `near-tee-verifier` 的说明，GPU 的证明没有绑进 TDX 的证明里，无法确认回答来自哪一张 GPU。要排除这个缺口，需要 NEAR AI 补上两者的绑定。

第三方监测网站 GreatFire 到 10 月 18 日的最后一次测试显示，`brave.com` 在中国大陆 100% 被封锁，从 2017 年 5 月 13 日起就有干扰记录。下载与更新用的 `laptop-updates.brave.com` 最近一次有效测试也是封锁。Leo 的后端 `ai-chat.bsg.brave.com` 没有测量数据，7 月 20 日到 10 月 20 日之间 OONI 公开 API 里中国的网络连接测试（Web Connectivity）没有一条针对这个主机，GreatFire 也没有测过。Leo 在中国大陆能否连接，查不到直接证据。

Apple 的 iTunes 查询 API 在中国大陆的商店查不到 Brave（Google Play 没有查询），这是 API 的查询结果，不等于 Brave 或 Apple 公告下架。Brave 的帮助中心没有写 Leo 在中国大陆提供或不提供，Leo 的介绍页写桌面版与手机版都提供 Leo。同一个 API 在台湾、香港、日本、韩国、新加坡的 App Store 都查得到 Brave，帮助中心也没有限制 Leo 使用地区的条文。

想在 AI 对话里处理不愿让服务商读到的文字或网页内容，可以在 Brave 桌面版或 Android 版打开 Leo，从模型菜单选 GLM 5.3 Flash。依源代码开发分支的简体中文翻译，模型菜单在 GLM 5.3 Flash 旁显示「通过 NEAR AI TEE 实现可验证的隐私保护」，回答旁有「已验证」的徽章。依源代码与博客推论，徽章反映的是 Brave 服务器的检查结果，到 10 月 20 日为止浏览器本身还没有验证。Leo 不需要账号，说明页提到免费版有使用次数的限制，但没有列出数字。

Brave 没有写 Leo 的回答支持哪些语言，Hugging Face 上 GLM 5.3 Flash 的模型说明页（模型卡）标示的语言是英文与中文。依博客的说明，加密只及于对话内容，转发消息的 Brave 仍看得到 IP 地址。模型生成的搜索查询也会离开 TEE 送到 Brave Search（不绑 IP 地址）。
