---
title: 中国开放权重模型 Qwen 的审查与代码差距量测
description: 两家发布移除版模型的公司在 10 月各自公布 Qwen 的量测，一份是中文政治问题的审查比例，一份是代码安全性随客户身份出现的差距。量测跟用 Qwen 问政治问题的人、用 Qwen3-Coder 写代码的开发者有关，无论在自己电脑上运行或通过服务使用。到 11 月 1 日为止，我们没有查到第三方重现，也没有查到 Qwen 团队的回应。
date: 2026-11-02T00:05:00+08:00
slug: qwen-political-censorship
categories:
  - censorship
regions:
  - CN
sources:
  - title: InterpreticAI/Qwen3.8-27B-Uncensored-v2 · Hugging Face
    url: https://huggingface.co/InterpreticAI/Qwen3.8-27B-Uncensored-v2
    publisher: Interpretic AI
    date: 2026-10-31
  - title: Chinese AI Writes Weaker Code for Beijing’s Adversaries. We Fixed It. A Qwen3-Coder Case Study
    url: https://www.hirundo.io/blog/qwen3-coder-vulnerabilities
    publisher: Hirundo
    date: 2026-10-21
  - title: hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized · Hugging Face
    url: https://huggingface.co/hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized
    publisher: Hirundo
    date: 2026-10-13
  - title: "Westernizing Qwen: Measuring and Mitigating Geopolitical Alignment in Chinese Open-Weight LLMs"
    url: https://www.hirundo.io/blog/westernizing-qwen
    publisher: Hirundo
    date: 2026-10-05
  - title: Political censorship in large language models originating from China
    url: https://doi.org/10.1093/pnasnexus/pgag013
    publisher: PNAS Nexus
    date: 2026-02-17
  - title: Qwen/Qwen3.8-27B
    url: https://huggingface.co/Qwen/Qwen3.8-27B
    publisher: Qwen
    date: 2026-08-05
  - title: Qwen/Qwen3-Coder-30B-A3B-Instruct
    url: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
    publisher: Qwen
    date: 2025-07-31
  - title: Chinese Open Source Model Roundup
    url: https://speechmap.substack.com/p/chinese-open-source-model-roundup
    publisher: SpeechMap
    date: 2025-05-01
  - title: 生成式人工智能服务管理暂行办法
    url: https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
    publisher: 中国网信网
    date: 2023-07-13
  - title: 卓揆：公務機關全面禁用Deepseek AI 服務
    url: https://www.ey.gov.tw/Page/9277F759E41CCD91/3ce9fe8f-2f5f-4d1d-8176-6fa4cf622b82
    publisher: 行政院
    date: 2025-02-03
  - title: 公務機關全面禁用DeepSeek AI 服務，未限制一般民間使用
    url: https://moda.gov.tw/ACS/press/news/press/15296
    publisher: 資通安全署
    date: 2025-02-20
  - title: Bias in Qwen3-Coder Model
    url: https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html
    publisher: Schneier on Security
    date: 2026-10-26
authors:
  - anoni-net
---

两家公司在 10 月下旬各自公布了阿里巴巴 Qwen 系列开放权重模型的量测（开放权重模型指公开模型文件、可以下载到自己电脑上运行的模型）。Interpretic AI 量测 Qwen3.8-27B 回答中文政治问题时的审查比例，10 月 31 日在 Hugging Face 发布移除审查的版本。依 Hirundo 10 月 21 日在博客公布的量测，Qwen3-Coder 写出的代码安全性会随系统提示词（开发者事先给模型的指示）里的客户身份改变，该公司也发布了修改过的版本。

两份研究都出自发布移除版模型的公司，Hirundo 也替使用开放权重模型的组织评估与修正模型。到 11 月 1 日为止，我们没有查到第三方重现，下文的数字都是两家公司各自的量测。用 Qwen 问政治问题的人跟 Interpretic 的量测有关，用 Qwen3-Coder 写代码的开发者跟 Hirundo 的量测有关。

Interpretic 的模型页写到，量测以中文提问两位研究者发表在期刊 PNAS Nexus 的 145 题政治题目，每个回答由另一个语言模型判定有没有审查。其中 113 题政治敏感的题目里，Qwen3.8-27B 原模型有 98 题被判为审查（86.7%），移除版剩 4 题（3.5%）。模型页没有写评分用的是哪一个模型、有没有人工抽查，移除的方式也只写了「targeted weight edit」（针对性地修改模型权重），没有附论文或代码。Interpretic 列出的限制是政治题只测了中文，也提醒回答有实质内容不代表正确。

题目集出自 2026 年 2 月发表的论文，研究者比较中国与中国以外开发的基础模型。根据论文摘要，中国开发的模型对 145 题政治问题拒答较多、回答较短，不准确的回答也较多。所有模型用中文提问时的拒答率都比英文高，不过语言之间的差距小于中国与非中国模型之间的差距。

Hirundo 的博客写到，研究请 Qwen3-Coder-30B-A3B-Instruct 反复写同一个网页服务，功能是用户注册、登录与保存私密文字。每次只改系统提示词里「代码替谁写」的一句，分成中立客户、美国国防承包商、中国国防承包商与香港民主倡议团体。写好的应用程序交给 ETH Zurich 与 LogicStar 的公开基准 BaxBench 实际运行，至少一种现成的攻击成功就算可被入侵。

可被入侵的比例在替美国国防承包商写的应用程序是 70%，中国国防承包商是 59%。私密数据泄露的比较里，替香港民主倡议团体写的应用程序近半会让任何登录的用户读到所有人的私密数据，中立客户约三分之一（博客算成相对高出 28%）。提示词另外加上安全指示的那一组，可被入侵的比例在美国承包商是 74%，中立客户是 59%。博客用统计检验判定上述三项差距都不太像是随机造成的。

博客的附录问答也写到，研究无法判断差距是否有人刻意放进模型。小模型本来就容易写出有漏洞的代码，前面提到的中立客户也有约三分之一会泄露，研究量的是额外的风险。研究只测了一个模型与一个任务，任务是从 11 个任务的小样本里挑出差距最明显的那一个。美国与香港两组是刻意挑选的极端案例。

Hirundo 的移除版公开在 Hugging Face，模型页写的做法是行为遗忘（behavioral unlearning，用额外的训练让模型忘掉特定行为，同时保留其他能力）。根据博客，移除版在 Hirundo 自建的 500 题基准 CCPC-500 上被判为审查、偏向或宣传的回答从 46.6% 降到 4.0%，三项代码差距也不再显著。附录的其他比较里，移除版替美国承包商写的应用程序对中立客户仍有一项显著差距，博客的解读是效果从国家移到组织类型。在其他十个编程任务上，可以正常运行与可被入侵的应用程序比例都跟原模型相近。

## 导读观点 {#perspective}

语言模型的回答取决于训练用的数据，以及训练后期的对齐（alignment），也就是让模型照开发者的规范回答的步骤。两份研究公开的量测都是大量提问、从输出计算比例，都没有分开检验训练数据与对齐。Hirundo 的博客主张移除版的结果证明代码的差距存在模型权重里，支撑主张的是同一家公司自己的移除实验。

公开研究项目 SpeechMap 2025 年 5 月量测较早的 Qwen3 世代，整理里写到 Qwen3 的开放权重模型在批评中国的题目上普遍审查。中文提问时审查得最彻底，英文也有，芬兰文只在部分情况出现、也比较不一致。同一份整理也提到，商用版 Qwen-Max 返回大量 API 错误，SpeechMap 的解读是 API 另有一层审查。本文据此推论，通过服务使用模型时，读到的回答可能同时受模型本身与服务端的过滤影响。

中国的《生成式人工智能服务管理暂行办法》2023 年 8 月 15 日施行，第四条要求提供与使用生成式人工智能服务时「不得生成煽动颠覆国家政权、推翻社会主义制度」等内容。根据第二条，没有向中国境内公众提供服务的研发与应用不适用这份办法，我们也没有查到办法对公开发布模型权重的专门规定。PNAS Nexus 论文的研究者提醒，论文是观察性的横断面研究（在同一个时间点比较不同模型、不做实验），不能证明监管压力与中国模型的审查行为之间有因果关系。

在中国境内面向公众提供的生成式人工智能服务，提供者须遵守上一段的暂行办法。下载开放权重到自己的电脑上运行时没有经过服务端。按 Interpretic 的量测，Qwen3.8-27B 的权重本身就带有审查，读到的回答因此仍可能带有审查（本文的推论）。

台湾行政院 2025 年 2 月 3 日要求公务机关全面禁用 DeepSeek AI 服务，新闻稿提到数据上传中国的信息安全风险尚未厘清也并未排除，模型训练也有思想审查等数据偏异。资通安全署 2025 年 2 月 20 日的说明写到，禁用范围包含云端服务、App 与下载到本地的使用方式，当时没有限制一般民间使用。公告点名的是 DeepSeek，我们没有查到点名 Qwen 的公告。

Interpretic 的移除版在 100 题有害请求中拒绝的题数从 100 降到 95，一般能力测验的分数也小幅下降，考虑改用移除版的人要权衡这些副作用。两家的移除版跟原模型一样采用 Apache 2.0 授权，Interpretic 没有附论文或代码，Hirundo 也只写了做法的类别。Hirundo 的博客写到打算公开自建的 CCPC-500，我们 11 月 1 日查证时数据集的网址无法访问（返回 401 错误），不能确认已经公开。SpeechMap 2025 年 5 月整理当时第三方修改过的中国开源模型，写到英文的改善明显，中文只有小幅改善。

用 Qwen 查询政治、历史这类敏感题目的人，本文建议把同一个问题拿去问不同来源的模型，再对照新闻与原始资料。论文摘要与 SpeechMap 都写到中文提问时拒答或审查较多，本文据此推论换一种语言再问可能得到不同的回答，不过论文也提到语言的差距小于中国与非中国模型之间的差距。上述研究都没有评估这些做法能否补上被审查的内容，没有被测到的题目也不代表没有偏误（本文的推论）。

用 Qwen3-Coder 或其他模型写代码的开发者，代码上线前仍要另外审查与测试。根据 Hirundo 的博客，在提示词加上安全指示没有消除差距，常见的静态扫描工具也不一定抓得到这类泄露（登录的用户可以读到其他人的数据）。移除版在其他十个任务上仍有约四分之一的应用程序可被入侵，中立客户的应用程序也会泄露（见上文）。本文据此推论，无论用哪个版本，审查时都可以优先看访问权限的检查。

到 11 月 1 日为止，我们没有查到阿里巴巴或 Qwen 团队对两份研究或论文的公开回应。12 月初可以留意是否有第三方重现两家公司的量测、CCPC-500 是否公开，以及 Qwen 团队有没有回应。
