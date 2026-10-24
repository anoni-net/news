---
title: Quad9 退出法国与法国的 DNS 封锁命令
description: 公共 DNS 解析服务 Quad9 10 月 22 日宣布，11 月 24 日起不再为位于法国的用户提供服务。依 Quad9 的公告，起因是法国法院依体育转播的反盗版规定，要求它替法国用户封锁一批域名。依 10 月 23 日查到的第三方测量，在中国大陆连接 Quad9 加密 DNS 网址的测试多数标为异常，异常不等于确认封锁。
date: 2026-10-27T00:00:00+08:00
slug: quad9-exit-france
categories:
  - censorship
regions:
  - FR
sources:
  - title: Farewell, France
    url: https://quad9.net/news/blog/au-revoir-france/
    publisher: Quad9
    date: 2026-10-22
  - title: Frequently Asked Questions
    url: https://quad9.net/support/faq/
    publisher: Quad9
  - title: Locations
    url: https://quad9.net/service/locations/
    publisher: Quad9
  - title: Quad9 Faces New DNS Censorship Legal Challenge in France from Canal+
    url: https://quad9.net/news/press/quad9-faces-new-dns-censorship-legal-challenge-in-france-from-canal/
    publisher: Quad9
    date: 2024-12-10
  - title: Quad9 Turns the Sony Case Around in Dresden
    url: https://quad9.net/news/blog/quad9-turns-the-sony-case-around-in-dresden/
    publisher: Quad9
    date: 2023-12-06
  - title: Quad9’s Opinion of the Recent Court Ruling in Leipzig
    url: https://quad9.net/news/press/quad9-s-opinion-of-the-recent-court-ruling-in-leipzig/
    publisher: Quad9
    date: 2023-03-06
  - title: Tribunal judiciaire de Paris, jugement du 13 mai 2026, RG n° 26/02207
    url: https://torrentfreak.com/images/tribunal-judiciaire_n°2602207_13_05_2026.pdf
    publisher: Tribunal judiciaire de Paris
    date: 2026-05-13
  - title: Blocking Behavior
    url: https://developers.google.com/speed/public-dns/blocking
    publisher: Google for Developers
  - title: 1.1.1.1 Public DNS Resolver
    url: https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/
    publisher: Cloudflare 1.1.1.1 docs
  - title: Innovating to address streaming abuse — and our latest transparency report
    url: https://blog.cloudflare.com/h1-2025-transparency-report/
    publisher: Cloudflare
    date: 2025-12-19
  - title: 著作權法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0070017
    publisher: 全國法規資料庫
  - title: "Mandated DNS Blocking: A Guide for Legal Professionals"
    url: https://www.internetsociety.org/resources/doc/2025/mandated-dns-blocking/
    publisher: Internet Society
    date: 2026-03-30
  - title: 運用 DNS RPZ 自律機制停止解析違法網站處理參考程序
    url: https://www-api.moda.gov.tw/File/Get/moda/zh-tw/Qv1tZuiNEVfsLIl
    publisher: 數位發展部
    date: 2025-01-09
  - title: CANAL+ reaches a new milestone in its fight against audiovisual piracy
    url: https://senalnews.com/en/digital/-canal-reaches-a-new-milestone-in-its-fight-against-audiovisual-piracy
    publisher: Señal News
  - title: DNS Resolver Quad9 Rejects French Piracy Blocks, Weighs Exit as beIN Seeks Up to €580K a Day
    url: https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/
    publisher: TorrentFreak
    date: 2026-10-05
  - title: Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France
    url: https://torrentfreak.com/?p=277758
    publisher: TorrentFreak
    date: 2026-04-01
  - title: OpenDNS Suspends Service in France Due to Canal+ Piracy Blocking Order
    url: https://torrentfreak.com/?p=253822
    publisher: TorrentFreak
    date: 2024-06-29
  - title: France Approves Automated, Real-Time Blocking of Pirate Sports Streams
    url: https://torrentfreak.com/france-approves-automated-real-time-blocking-of-pirate-sports-streams/
    publisher: TorrentFreak
    date: 2026-07-28
  - title: VPNs and Cloudflare Escape beIN’s €10,000-a-Day Piracy Blocking Penalties
    url: https://torrentfreak.com/vpns-and-cloudflare-escape-beins-e10000-a-day-piracy-blocking-penalties/
    publisher: TorrentFreak
    date: 2026-10-16
  - title: Is https://dns.quad9.net blocked in mainland China?
    url: https://en.greatfire.org/https/dns.quad9.net
    publisher: GreatFire
  - title: Is https://dns.quad9.net/dns-query blocked in mainland China?
    url: https://en.greatfire.org/https/dns.quad9.net/dns-query
    publisher: GreatFire
  - title: "OONI API aggregation: web_connectivity, dns.quad9.net, CN"
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=web_connectivity&domain=dns.quad9.net&since=2026-07-23&until=2026-10-23
    publisher: OONI
  - title: 中华人民共和国网络安全法
    url: https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm
    publisher: 国家互联网信息办公室
    date: 2025-12-29
  - title: Privacy
    url: https://quad9.net/service/privacy/
    publisher: Quad9
authors:
  - anoni-net
---

Quad9 是瑞士非营利基金会运营的公共 DNS 解析服务，负责把网址里的域名翻译成服务器的地址，用户可以自行设置、取代网络运营商默认的解析服务。Quad9 10 月 22 日宣布，11 月 24 日起不再为位于法国的用户提供服务。依 Quad9 的公告，体育转播商 beIN 提出请求后，法国法院 10 月 21 日的判决要求它替位于法国的用户封锁一批域名的解析。Quad9 表示不会封锁这些域名，所以选择退出法国，公告没有说明会用什么方式识别位于法国的用户。

这类命令的依据是法国《体育法典》第 L. 333-10 条，转播权利人可以请求法院命令能够协助的对象采取封锁措施，阻止从法国境内连到盗播网站。巴黎司法法院 5 月 13 日判决 Google 与 Quad9 等被告在送达后 3 天内采取措施，封锁持续到 WTA 网球赛季最后一场的 11 月 14 日。依判决适用的条文，之后由权利人提供新发现的盗播网站，法国视听与数字通信监管局（Arcom）核查后再通报被告。

5 月判决列出的域名依 Quad9 的说法后来增加到 58 个，TorrentFreak 引述 Quad9 表示没有封锁这些域名。TorrentFreak 也报道 beIN 回到法院，请求每日最高 58 万欧元的罚款。beIN 对 TorrentFreak 表示不就进行中的程序发表评论。Quad9 的公告写到 10 月的判决仍要求封锁、罚款定为每日 1,000 欧元（到 11 月 14 日合计 2.4 万欧元），并提到有一件上诉还在进行，Quad9 承受不了另外约 20 件类似诉讼累积的罚款。

依 Quad9 的公告，它的服务免费、不需要注册，也没有把用户对应到所在国家的数据。Quad9 因此无法判断判决适用于哪些人，若把域名加进全球的封锁清单，又会把法国的判决套用到全世界的用户。

在法国付费电视运营商 Canal+ 提出的另一件案子，Quad9 2024 年 12 月的公告写到，当时它对所有地区的用户封锁了清单上的网站。在德国的诉讼中，Quad9 曾依 IP 地址做地区封锁，权利人用 VPN 连接之后法院认定措施不足并处以罚款。Quad9 后来在 2023 年 12 月的上诉审胜诉，德累斯顿高等法院认定解析服务不负侵权责任。

依 TorrentFreak，Quad9 对德国案与这次做法不同的解释是德国的封锁属于诉讼期间的临时措施、每个案子各自处理。Canal+ 案与这次的关系，报道没有说明。

其他公共解析服务的做法也不同。依 TorrentFreak 引用的公告，Cisco 的 OpenDNS 从 2024 年 6 月 28 日起停止在法国与葡萄牙提供服务。到 10 月 23 日，Google Public DNS 的说明页列出法国等五个会依命令封锁的地区，被封锁的域名会直接回复拒绝查询。Cloudflare 的文档提到 1.1.1.1 不封锁也不过滤内容，博客则提到回应封锁命令时，有时改在内容分发网络（CDN）对网站做地理封锁。

## 导读观点 {#perspective}

DNS 解析服务把网址里的域名翻译成服务器的 IP 地址，DNS 层的封锁让解析服务对特定域名不回复地址，只影响通过这个解析服务的查询。依 Internet Society 2026 年 3 月的报告，解析服务收到的只有域名，没有网页的完整路径。

封锁能不能只限于法国，巴黎司法法院 5 月判决的理由是被告没有证明限定在法国境内会有高成本或技术上不可行，技术方式由被告自行选择。Quad9 的公告则提到它没有用户所在国家的数据，德国的经验也显示依 IP 地址判断会被 VPN 绕过。Internet Society 的报告提到，运营者要在毫秒内准确判断用户的位置并不容易，封锁可能影响管辖范围以外的用户。Google Public DNS 的说明页则列出它会依命令在法国等地区封锁。

对于可以被绕过的封锁还有没有效，Quad9 的公告提到想看的人会改用其他较不可信的解析服务，封锁也不会让内容从服务器上消失。巴黎司法法院的判决写到，改用替代解析服务的人数多寡，不影响权利人请求封锁的权利。依 TorrentFreak 的转述，巴黎上诉法院 3 月在 Canal+ 对 Google、Cloudflare 与 Cisco 的案件中认定，过滤措施可以被绕过不代表措施无效。同一个判决也认为，替代解析服务让用户可以连到盗播网站，并绕过网络运营商的封锁。

责任与成本由谁负担，Quad9 的公告认为让私人企业决定网络上能看到什么是危险的问题。Internet Society 报告的结论是 DNS 封锁不适合用来执行公共政策，报告也提到小型与非营利运营者可能负担不起逐国封锁的成本。依 Señal News 转载的 Canal+ 新闻稿，上诉法院的判决符合 Canal+ 要求各类技术中介承担打击盗播责任的策略。5 月的判决则提到，封锁的成本依 Arcom 主持的协议由各方分摊。

台湾的数字发展部 2025 年 1 月订定的参考程序也有 DNS 层的停止解析，由台湾网络信息中心（TWNIC）与自愿参与的网络接入服务商修改特定域名的解析结果，要依法院判决、裁定或机关依法作出的处分才能启动。程序写明停止解析不包括禁止用户通过公共解析服务或 VPN 浏览的技术，说明栏也提到这在技术上做不到，举的例子包括 OpenDNS、Cloudflare DNS 与 Quad9。启动的依据例如诈骗犯罪与儿童及少年性剥削的相关法律，到 10 月 7 日查证时，台湾的《著作权法》没有授权封锁网站的条文。

公共解析服务在不在封锁范围内，法国与台湾的方向不同。本文的法国案件由法院判决命令解析服务自己封锁域名，判决后新增的网站由 Arcom 核查后通报，台湾的程序则把公共解析服务排除在外。中国大陆的《网络安全法》（2026 年 1 月 1 日起施行的 2025 年修正版）第五十二条规定，来源于境外、法律和行政法规禁止发布或者传输的信息，由网信部门和有关部门通知有关机构采取技术措施阻断传播。条文写的是通知有关机构，没有写到公共解析服务，本文查到的中国大陆法规也没有规定法院程序。

依 Quad9 10 月 23 日的节点数据，中国大陆、香港与澳门都没有 Quad9 的节点。节点只是服务器的所在地，没有节点不代表无法使用。依 Quad9 的隐私页，Quad9 退出某个国家时当地用户仍可使用服务（除非当地自己阻止），由邻近国家的节点提供。该页写的是退出某国的情形，没有针对中国大陆、香港或澳门说明。

中国大陆这一边，查得到的是第三方测量能不能连上 Quad9 本身的结果。第三方测量项目 GreatFire 到 10 月 22 日的最后一次测试，`https://dns.quad9.net` 最近 2 次有结论的测试中有 1 次受到干扰，从 2020 年 2 月 4 日起就有干扰记录。加密 DNS 查询用的 `https://dns.quad9.net/dns-query`，最近 2 次有结论的测试（最后一次 9 月 3 日）都受到干扰，两个网址的测试次数都不多。

依网络干扰观测项目 OONI 的公开 API，7 月 23 日到 10 月 23 日在中国大陆对 `dns.quad9.net` 做了 239 次网页连接测试（Web Connectivity），其中 232 次测的是加密 DNS 查询用的网址。239 次中 224 次标为异常，确认封锁 0 次。异常不等于确认封锁，GreatFire 与 OONI 的测量结果也都不能用来判断封锁的手法。本文没有找到能判断用 9.9.9.9 做一般 DNS 查询在中国大陆是否受到干扰的测量结果。

想确认自己是否在用 Quad9，可以打开 Quad9 提供的 `on.quad9.net` 检查页。11 月 24 日之后人在法国、设备或路由器又固定设置成 Quad9 的人，可能无法解析网址，公告没有说明停止服务的方式。改用网络运营商默认或其他解析服务的人，会失去 Quad9 拦截恶意域名的保护。依 10 月 23 日的节点数据，Quad9 在台北、东京、新加坡、首尔等地的节点都在运行，公告没有提到法国以外的用户会有任何变动。

读者可以从几个问题比较两方的标准。一是限定在一国境内封锁的成本与可行性由谁证明，法院认为被告没有证明，Quad9 与 Internet Society 则提出定位的限制。二是可以被绕过的封锁算不算有效，法院认为可绕过不代表无效，Quad9 认为用户会转向其他服务。三是技术中介该不该分担打击盗播的责任，以及小型与非营利的解析服务能否负担逐国封锁。

之后可以留意 Quad9 上诉的结果，以及 11 月 24 日的退出是否如期。依 TorrentFreak 10 月 16 日的报道，数个 DNS 运营者已就 3 月与 5 月的判决上诉到法国最高法院。TorrentFreak 7 月报道法国新通过的法律改由 Arcom 以自动化系统实时推送新增的封锁目标，依当时的报道，正式实施要到 2026 年稍晚。新法是否涵盖公共解析服务，本文没有查证。
