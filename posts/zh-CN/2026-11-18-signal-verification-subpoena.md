---
title: Signal 协议一对一对话的机器检查证明与美国大陪审团传票
description: Google DeepMind 用 AI 代理证明 Signal 协议实现 libsignal 在一对一对话的加密性质，群组对话、服务器与密钥生成不在范围内，到 11 月 14 日查不到其他研究者重现。Signal 公开 10 月一份大陪审团传票，四个电话号码只有一个有账号，交出的是创建时间与最后连线日期。用户不必调整设置。
date: 2026-11-18T00:00:00+08:00
slug: signal-verification-subpoena
categories:
  - encryption
sources:
  - title: "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth"
    url: https://deepmind.google/blog/introducing-alphaproof-code/
    publisher: Google DeepMind
    date: 2026-11-10
  - title: "AlphaProof Code: Verifying Signal’s Security at the Machine-Code Level"
    url: https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf
    publisher: Google DeepMind
    date: 2026-11-10
  - title: Grand jury subpoena for Signal user data in the United States District Court for the District of Columbia (again!)
    url: https://signal.org/bigbrother/district-of-columbia-2/
    publisher: Signal
    date: 2026-11-03
  - title: Grand jury subpoena for Signal user data in the United States District Court for the District of Columbia
    url: https://signal.org/bigbrother/district-of-columbia/
    publisher: Signal
    date: 2026-03-06
  - title: Government Requests
    url: https://signal.org/bigbrother/
    publisher: Signal
  - title: Google DeepMind just mathematically verified key parts of Signal
    url: https://arstechnica.com/ai/2026/11/signals-encryption-just-passed-an-ai-powered-mathematical-checkup/
    publisher: Ars Technica
    date: 2026-11-11
  - title: Is https://signal.org blocked in mainland China?
    url: https://en.greatfire.org/https/signal.org
    publisher: GreatFire
  - title: How countries attempt to block Signal Private Messenger App around the world
    url: https://ooni.org/post/2021-how-signal-private-messenger-blocked-around-the-world/
    publisher: OONI
    date: 2021-10-21
  - title: OONI API
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=signal&since=2026-07-18&until=2026-10-18
    publisher: OONI
authors:
  - anoni-net
---

Google DeepMind 在 11 月 10 日公布，研究团队用 AI 代理对 Signal 协议的参考实现 libsignal 写出由计算机逐步检查的数学证明。证明的范围是一对一对话建立连线与更新密钥的步骤，群组对话不在其中。Signal 在 11 月 3 日公开美国华盛顿特区联邦检察官办公室 10 月发出的大陪审团传票，四个电话号码里只有一个有账号，Signal 交出的是账号创建时间与最后连线日期。两件事都跟全球的 Signal 用户有关，用户这一端不需要调整设置。

DeepMind 的博客与技术论文列出，验证对象是 libsignal v0.105.4。研究者用标准的 Rust 编译器把它编成 AArch64（64 位 ARM 架构）的 Linux 机器码，证明对应到编译出来的程序，底层的加密函数除外。证明分成两个部分，一是建立对话时交换密钥的 PQXDH，混合了传统算法与能抵挡未来量子计算机的算法。二是每一条消息换一把新密钥的 Triple Ratchet。

论文列出的性质有前向保密（密钥外泄时，之前的消息仍无法解开）与握手的保密、身份验证。另一项是入侵后恢复（post-compromise security）。攻击者偷到当下的密钥之后，只要没有在下一次密钥更新时主动介入，之后的消息就恢复保护。论文设定的攻击者能控制网络与服务器，也可能偷到长期密钥或一方的整份状态。

DeepMind 把这套工具称为 AlphaProof Code。博客提到，研究者与 AI 模型一起把 Signal 的安全目标写成数学规格，每一条都由人类专家审过。证明则由 AI 代理用 Lean 撰写，Lean 是定理证明器，每一步推论都由程序检查。论文写到作者没有亲手写任何一行证明，AI 代理产生约 650 万行 Lean 证明，证明工作由五人在四周内完成。

根据论文的统计，读者需要信任的规格与定义约 18,000 行，另有约 8,000 行描述机器码行为的规格。为了确认系统能否分辨有问题的程序，研究者把两个已修复的 libsignal 旧漏洞放回一份隔离的代码，两个版本都被证明不安全。Ars Technica 转载 WIRED 的报道提到，验证过的部分没有找到新漏洞。

DeepMind 的博客写到，研究团队第一次用 AI 把广泛部署的加密协议验证到实现代码这一层。博客也宣称，像 Signal 这样广泛部署的协议，实现在此之前没有被任何方法形式化验证过。规格与证明已经开源。博客引述 Signal 首席技术官的话，自动化的定理证明让团队对代码能兑现隐私保证更有信心。

传票的经过公开在 Signal 的「Government Requests」页面，检察官办公室在 10 月 5 日发出传票，期限三天。传票查询的是四个电话号码在一段期间内的「all customer or subscriber account information」。附件举出的项目包括但不限于账号创建的日期与时间，以及最后连线的日期与时间。Signal 判断传票附上的标准指示是为银行写的，其中也列了支票与存款单的影像，页面写到 Signal 没有以能连到账号的方式收集这类数据。

美国公民自由联盟（ACLU）在 10 月 6 日代表 Signal 回复。四个号码里有三个没有 Signal 账号，Signal 交出剩下那个账号的创建日期与时间，以及最后连上 Signal 服务器的日期。Signal 只保留最后连线的日期、不保留时间，所以交不出时间。

这次的传票没有附不披露令（禁止 Signal 对外透露收到传票的法院命令），Signal 遮蔽电话号码、期间与政府人员的身份之后公开了文件。同一个法院在 2025 年发出、Signal 在 3 月公开的前一份传票查询了 37 个账号。其中 7 个不存在，24 个在那段期间没有相关数据，其余 6 个交出了数据。Signal 的页面提到，执法单位的要求越来越集中在 Signal 实际收集的少量数据。

## 导读观点 {#perspective}

协议的证明针对消息在传送途中的保护，攻击者控制网络与服务器、甚至偷到部分密钥时也包括在内，传票的回应则显示服务器端保留了哪些数据。Signal 的页面开头列出消息、通话、联系人、群组、个人资料名称与头像都经过端到端加密，Signal 无法交出从未取得的数据。

论文列出的限定条件中，一组定理采用符号模型，假设加密算法完美无缺。符号模型不谈实际字节的保密程度，但在符号模型下证明了握手的保密能抵挡未来的量子计算机。另一组计算模型的定理只考虑传统计算机的攻击者。Triple Ratchet 里负责后量子的部分叫 SPQR，证明只显示整体不比旧的 Double Ratchet 弱，没有证明 SPQR 额外带来的后量子恢复能力。

密钥生成的程序没有验证，底层的加密函数也只用规格描述应有的行为，本身没有证明。侧信道攻击（从耗电、时间等外部信号推测密钥）与内存里的其他秘密不在范围内。机器码层级的定理只适用于双方各用一台设备的情境。双方一开始就持有对方的身份密钥，第一次联系时确认对方身份的那段流程没有包含在内。

论文把群组对话、sealed sender（隐藏发送者身份的机制）与服务器端的协议列为之后的工作。描述机器码行为的 8,000 行规格无法证明跟实际的硬件一致，论文写到硬件与操作系统内核不是可以证明的对象。Ars Technica 转载的 WIRED 报道也提到，整个 Signal App 并没有被验证。

论文的作者都来自 Google DeepMind 与 Google，致谢列出 Signal 的三位成员对方法提供意见。到 11 月 14 日为止，查不到论文经过同行评审的记录，也查不到 DeepMind 以外的研究者重现的结果。

论文提到 WhatsApp、Meta Messenger 与 Google Messages 也使用 Signal 协议的变体。验证的对象是 libsignal 的代码，不代表那些 App 的实现也通过同样的证明。

Signal 2016 年第一份公开的传票回应就写到，服务器端能交出的只有注册的日期与时间和最后连线的日期。10 月交出的仍是同样两项。以电话号码查询的回复，也让检察官知道四个号码里有三个没有 Signal 账号。

在中国大陆，GreatFire 到 2026 年 10 月 11 日的最后一次测试显示 signal.org 被 100% 封锁，干扰记录从 2017 年 7 月 2 日起算。这项测量的对象是网址，不含 App 的消息连线。OONI 2021 年的分析认为 Signal App 在 2021 年 4 月到 9 月间于中国等地遭到封锁，公开 API 在 2026 年 7 月 18 日到 10 月 17 日的 2847 笔中国 Signal 测试里有 2769 笔标为异常，确认封锁为 0 笔（异常不等于确认封锁）。

用户不需要做任何设置。需要在 Signal 上处理敏感对话的人，判断时可以参考证明的范围只涵盖一对一对话，论文没有对群组对话下结论。依 10 月的回复，服务器端保留账号创建时间与最后连线日期。之后可以留意 DeepMind 开源的证明有没有其他研究者重现，以及验证范围有没有扩及群组对话与 sealed sender，论文没有写出时程。
