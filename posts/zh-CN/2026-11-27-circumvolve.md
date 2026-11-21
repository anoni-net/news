---
title: 用大型语言模型搜索审查规避策略的 CircumVolve 研究
description: 研究者让大型语言模型反复改写规避程序，在中国、伊朗、巴基斯坦、哈萨克斯坦的网络找到 47 个绕过审查设备的策略，同一个策略不一定在每个国家都有效。策略要经过工具开发者整合才会到用户手上，一般读者不需要做任何设置。
date: 2026-11-27T00:00:00+08:00
slug: circumvolve
categories:
  - censorship
sources:
  - title: "CircumVolve: Automated Discovery of Censorship Evasion Strategies Using Large Language Models"
    url: https://gfw.report/publications/ccs26/en/
    publisher: GFW Report
    date: 2026-11-16
  - title: "CircumVolve：利用大语言模型自动发现审查规避策略"
    url: https://gfw.report/publications/ccs26/zh/
    publisher: GFW Report
    date: 2026-11-16
  - title: alizohaib/ccs26-circumvolve
    url: https://github.com/alizohaib/ccs26-circumvolve
    publisher: GitHub
  - title: Kkevsterrr/geneva
    url: https://github.com/Kkevsterrr/geneva
    publisher: GitHub
  - title: "obfsgen: a generative approach towards tunnel obfuscation"
    url: https://github.com/net4people/bbs/issues/684
    publisher: GitHub
    date: 2026-11-18
  - title: goose-lab-cuhk/obfsgen
    url: https://github.com/goose-lab-cuhk/obfsgen
    publisher: GitHub
authors:
  - anoni-net
---

审查方换了新的封锁方式之后，绕过的方法多半要靠研究者人工找出来。研究者要分析封锁事件、猜测触发的条件、手写规避方式再实际测试，论文写到这个循环往往要数周到数月。GFW Report 网站 11 月 16 日公开一篇安全研讨会 ACM CCS 2026 的论文 CircumVolve，研究者让大型语言模型（LLM）反复改写规避程序，在模拟环境与中国、伊朗、巴基斯坦、哈萨克斯坦的网络实际测试。论文把它定位成给规避研究者与工具开发者的发现工具，一般读者不需要做任何设置。

规避策略指改动数据包或协议的写法，让审查设备无法比对出连接要去被封锁的网站，服务器仍能正常响应。研究者把每个策略写成可执行的 Python 程序，交给 LLM 反复产生变体，再留下测试表现好的版本继续修改。整套流程沿用开源的程序演化框架 OpenEvolve，LLM 每一回合依分数、转成文字的数据包与错误信息提出修改。策略要同时躲过审查、从目的服务器取得正确响应才会得到高分，避免 LLM 用删掉被封锁域名这类方式取巧。

既有的自动化工具也能搜索规避策略，例如 2019 年发表的 Geneva。依论文的描述，这类工具用固定的规则组合数据包操作，改不了 TLS（HTTPS 使用的加密协议）与 QUIC（新一代的网页传输协议）这类加密协议里的内容。LLM 写出的是一般的 Python 程序，可以在程序里处理加密，改动加密协议的内容。

在真实的网络上，研究者只能知道绕过成功或失败。模拟环境改用开源的审查模拟软件 OpenGFW 扮演审查设备，研究者可以追查策略为什么有效。策略也送到受审查地区、研究者自己控制的数据中心 VPS（租用的虚拟主机）实测，测试涵盖 DNS（把域名转成 IP 地址的查询）、TCP/IP、HTTP、TLS 与 QUIC 五种协议。每种协议依各国实际的封锁方式，在其中两到三国测试，伊朗的实验都在 2026 年 2 月 28 日全国断网之前完成。

研究者用 CircumVolve 在五种协议共找到 47 个不同的策略，其中 27 个就作者所知没有出现在先前的研究。每个国家受测的每种协议都至少找到一种绕过方式，同一个策略则不一定在每个国家都有效。依论文，有找到绕过方式的运行在第一次绕过之前，LLM API 的费用中位数不到 1 美元。论文自述的限制包括全部实验只用 GPT-5.1 一个模型，QUIC 与 TLS 也只改写连接的第一个数据包。

## 导读观点 {#perspective}

论文在伦理段提出的看法是，审查方要正确解析所有协议，规避的一方只要找到一个被忽略的边角情况就可能绕过。研究者用 CircumVolve 把寻找边角情况的大量尝试交给 LLM，LLM 可以依审查设备的反应调整下一轮的修改。论文认为部分 DNS 策略单靠随机变化输入的模糊测试（fuzzing）可能很难找到。

系统要靠熟悉审查的研究者定义评估标准、设计提示，论文把自动部署列为未来的工作。想自行运行的研究者要准备自己的 VPS 与 LLM API 密钥，论文也提醒测试会从测试点送出畸形的数据包，测试活动本身可能被审查方识别出来。

论文写到已公开代码、提示与成功的策略。到 11 月 22 日，CircumVolve 代码库的根目录没有许可文件，只有内含的 `openevolve/` 目录采用 Apache-2.0。别的项目要直接沿用其余的代码，条件并不明确。

另一个研究团队 11 月 18 日在 GitHub 的 net4people 讨论区介绍的 obfsgen 同样用上生成式模型，改的是加密隧道流量的数据包大小与时序，让它接近一般的流量。obfsgen 采用 MIT 许可，README 写明还不能用在生产环境。

中国自 2024 年 4 月起大规模解密 QUIC 连接并检查其中的 SNI（连接要访问的域名），论文的 QUIC 测试以此为背景。论文只在数据中心主机上测试，我们判断家用宽带与移动网络的审查设备是否会得到相同的结果，需要另外测试才能确定。

论文的伦理段写到，公开可能让审查方在规避工具采用之前，先找出并修补这些策略。作者发表的理由是资源充足的审查方本来就能自行找出这些手法，而且依论文引用的先前研究，审查方把新技术放进生产系统会延迟一段时间（例如数个月）。从论文提到的低成本、代码与提示都已公开来看，我们判断审查方用同样的方法测试自家设备并不困难。

依论文的说明，研究者找出策略之后要由工具开发者整合进实际的规避工具，用户在工具更新后才会用上。在那之前，正在使用规避工具的读者不需要做任何设置。研究针对的是依规则比对标准协议的审查设备，没有测试完全加密、整条连接看起来像随机数据的协议，也没有测试专有协议。
