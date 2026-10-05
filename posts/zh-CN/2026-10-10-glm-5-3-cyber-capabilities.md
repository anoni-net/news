---
title: GLM-5.3 的漏洞利用能力与开放权重的防护
description: Anthropic 9 月 29 日发布对智谱开放权重模型 GLM-5.3 的测试报告，模型能写出攻击浏览器的程序。在报告的模拟测试里，伪装场景等手法可以绕过防护。智谱的发布说明写到，公开的权重只带着模型本身的防护，强大的防御能力也不该只留在少数组织。普通读者能做的是浏览器更新后尽快重新启动。
date: 2026-10-10T00:00:00+08:00
slug: glm-5-3-cyber-capabilities
categories:
  - security
sources:
  - title: GLM-5.3 and the spread of advanced cyber capabilities
    url: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
    publisher: Anthropic
    date: 2026-09-29
  - title: "Preparing GLM-5.3 for Open Release: A Responsible Path to Cyber Defense"
    url: https://x.com/Zai_org/article/2088280509474320693
    publisher: Z.ai
    date: 2026-08-14
  - title: "GLM-5.3: Frontier Coding with Emergent Cyber Capabilities"
    url: https://z.ai/blog/glm-5.3
    publisher: Z.ai
    date: 2026-08-14
  - title: CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities
    url: https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
    publisher: NIST
    date: 2026-09-17
  - title: How Far Behind the Frontier are Leading Open Weight Models on Cyber?
    url: https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
    publisher: AI Security Institute
    date: 2026-07-17
  - title: Stable Channel Update for Desktop
    url: https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_0153744567.html
    publisher: Google
    date: 2026-06-08
  - title: 更新 Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=zh-Hans&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 管理 Chrome 的安全性
    url: https://support.google.com/chrome/answer/10468685?hl=zh-Hans&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 調整 Tor Browser 安全等級以平衡隱私與可用性
    url: https://support.torproject.org/zh-TW/tor-browser/features/security-levels/
    publisher: Tor Project
  - title: 讓你的AI懂臺灣！數位發展部公布臺灣主權AI評測結果，攜手產官打造可信任AI生態系
    url: https://moda.gov.tw/ADI/news/latest-news/20538
    publisher: 台湾数字发展部数字产业署
    date: 2026-09-02
  - title: 更新 Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 管理 Chrome 的安全性
    url: https://support.google.com/chrome/answer/10468685?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
authors:
  - anoni-net
---

美国 AI 公司 Anthropic 9 月 29 日发布测试报告，对象是中国的智谱（中国以外称 Z.ai）8 月推出的语言模型 GLM-5.3。报告的结论是，GLM-5.3 能自行找出软件漏洞并写成可用的攻击程序，能力接近 Anthropic 只提供给经过筛选的安全防御方的 Claude Mythos Preview。报告也写到，在模拟测试里，伪装场景等简单的手法就能绕过 GLM-5.3 的防护。普通读者不会直接用到这个模型，能做的事跟以往相同，浏览器更新后尽快重新启动。

GLM-5.3 的权重（模型本身的参数）8 月底公开，任何人都能下载与修改。智谱 8 月 14 日在 X 发表的说明写到，权重公开之后，没有开发者能保证控制每一种后续的修改与用途。同一份说明还写到，强大的防御能力不能只留在少数资源充足的组织，开源项目维护者与独立研究人员也需要。

在 Anthropic 运行的 ExploitBench 基准测试里（题目是 Chrome 的 JavaScript 引擎 V8 的已知漏洞），GLM-5.3 尝试 410 次，有 50 次写出完整的攻击程序，Claude Mythos Preview 是 56 次。在另一项以开源项目为对象的内部测试里，GLM-5.3 有 4% 的尝试能完全控制程序的执行流程，Mythos Preview 是 6%，Claude Opus 4.6、GLM-5.2 等较早的模型一次都没有成功。美国国家标准与技术研究院（NIST）下属的人工智能标准与创新中心（CAISI）9 月 17 日的评估写到，GLM-5.3 是截至当时网络安全能力最强的开放权重模型，综合多项测试落后美国最前沿的模型约四个月。CAISI 对照的美国模型包括只提供给经过筛选的用户的版本。

一位研究人员花了大约一天、投入有限的人力，让 GLM-5.3 在一款常用浏览器的 JavaScript 引擎找到数个未知的漏洞。模型把这些漏洞串成一个网页，访客用该浏览器的 Linux 版本打开，网页就能读取访客电脑上的任意文件。Anthropic 在报告里写到，其他平台也可能受影响，在那些平台上利用的路径或许更复杂。报告没有写出是哪一款浏览器，只写到漏洞已经报告给维护者。

另一位研究人员让较小的 GLM-5.3-Flash 根据 Chrome 漏洞 `CVE-2026-11645` 与另一个已知漏洞的公开信息，写出串联两者的攻击程序。研究人员投入 20 分钟，模型运行 8 小时，按智谱的 API 价格换算约 20.40 美元。Google 在 6 月 8 日的 Chrome 更新修补了 `CVE-2026-11645`，公告写明已有攻击程序在外流传。

报告写到，上面这些写攻击程序的任务没有触发 GLM-5.3 的拒绝，要求协助开发恶意程序或攻击远程目标时，模型则会拒绝。Anthropic 另外在模拟环境要求它攻击远程系统，直接提出时模型全部拒绝。告诉模型它在演练中扮演红队（模拟攻击方的测试人员）时，模型有 64% 的情况开始尝试连接目标系统，预先填入模型的思考内容、让它看起来已经决定执行时是 92%。用 abliteration 这种手法修改权重、移除拒绝行为之后，比例是 100%。

Anthropic 第一次用 abliteration 修改权重，花了约 2,200 个 GPU 小时、约 4,400 美元，估计熟悉手法的团队约需 600 个 GPU 小时、约 1,200 美元。修改后的模型在一般科学能力测试的分数不变，从网络安全测试抽样的题目分数略低。报告也写到，GLM-5.3 发布后几天内，已有数个开发者公开了移除拒绝行为的版本。

在 Anthropic 自己的测试里，通过 API 使用、带防护的 Claude 拦下了伪装成红队的请求。另外两种手法对 Claude 一般无法实施，因为 Claude 的 API 不提供预填思考内容的方式，权重也没有公开。绕过防护的这组测试在模拟环境进行，模型生成的代码没有实际执行，报告写明模拟无法完整反映真实情况。

## 导读观点 {#perspective}

模型拒绝恶意请求的能力是训练出来的，跟模型的其他能力存在同一组权重里。通过 API 提供模型时，模型开发者可以在模型外面另外加上过滤与监控。权重公开之后，用户在自己的电脑上运行，外面那几层就不存在。修改权重也不需要模型开发者同意。

智谱在 X 的说明写到，GLM-5.3 有三层防护，分别是请求分类器、评估执行过程风险的监控，以及模型本身的安全训练。前两层部署在智谱自己托管的服务，不会自动跟着模型进到用户自行部署的环境，公开的权重只带着第三层。说明也写到，模型层的防护能提高滥用的门槛，但无法做到绝对的控制。

智谱在同一份说明里写到这类能力可攻可守，因此计划分阶段发布，先让经过筛选的安全合作伙伴测试。智谱 8 月 14 日的发布博客写到，权重在两周后、完成安全评估与加固之后公开。

Anthropic 在报告里的评估是，GLM-5.3 发布时没有足以限制滥用的防护。报告写到，同等能力的其他模型发布时都带有防护，或只通过限制访问的计划提供，也写到政府应该对能力足够的模型做安全测试。截至 10 月 5 日，查不到智谱针对这份报告的公开回应。

Anthropic 的报告写到，防御方应该获得至少跟攻击方一样好的模型。Anthropic 通过 Project Glasswing 等计划把模型提供给经过筛选的防御方，并写到正在扩大提供的范围。智谱的说明写到，防御能力不能只留在少数组织。智谱的做法是随 GLM-5.3 推出 OpenVuln 计划，跟维护者合作审查重要的开源项目，协助报告与修补漏洞。

英国 AI 安全研究所（AISI）7 月的分析写到，开放权重模型可以私下部署、数据不必回传给模型开发者，也不会被开发者改版或下架。同一份分析也写到，一旦公开，防护可以被移除，复制出去的模型也收不回来。AISI 以 6 月推出的 GLM-5.2 等模型测得，开放权重模型的网络安全能力落后最前沿的闭源模型 4 到 7 个月，2025 年多数时候是 6 到 10 个月。AISI 把这段差距视为能用到最前沿闭源模型的防御方的准备时间。

读者无法控制谁使用这些模型，能缩短的是漏洞修补之后、自己的浏览器还没更新的这段时间。在报告的实验里，GLM-5.3-Flash 根据已公开的漏洞信息，运行 8 小时就写出攻击程序。Chrome 会在后台准备更新，要重新启动才会生效。长时间不关浏览器的人可以到“帮助”的“关于 Google Chrome”检查，出现“重新启动”按钮表示更新还没生效。

更新挡不住还没修补的漏洞，经常访问陌生网站的人可以再减少网页脚本能用的浏览器功能。在 Chrome“隐私与安全”的“安全”里，可以把“管理 JavaScript 优化和安全性”设为“自动在不熟悉的网站上停用 JavaScript 优化工具”，部分网站可能因此变慢。这个设置缩小的是网页脚本攻击浏览器的机会，挡不住骗你输入密码的钓鱼网页。

之后可以留意，开放权重模型的防护要做到什么程度才算足够。模型的网络安全能力要不要纳入政府的测试、由哪个机构负责。AISI 所说的准备时间，是否足够让漏洞先被修补。人手不足的开源项目，能否用到跟攻击方同级的工具。
