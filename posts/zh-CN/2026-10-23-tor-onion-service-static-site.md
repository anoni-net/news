---
title: Tor onion 服务的静态网站搭建
description: 搭建 onion 服务不需要固定 IP、域名或开放端口，用 tor 加上一般的网页服务器就能把静态网站放上 Tor 网络。tor 6 月到 10 月连续发布四个安全更新，其中三个的修补涉及 onion 服务，到 10 月 20 日为止最新版是 0.4.9.14。网站的访客要通过 Tor 连接，例如用 Tor Browser。
date: 2026-10-23T00:05:00+08:00
slug: tor-onion-service-static-site
categories:
  - censorship
sources:
  - title: Set up Your Onion Service
    url: https://community.torproject.org/onion-services/setup/
    publisher: Tor Project
  - title: How do Onion Services work?
    url: https://community.torproject.org/onion-services/overview/
    publisher: Tor Project
  - title: Operational Security
    url: https://community.torproject.org/onion-services/advanced/opsec/
    publisher: Tor Project
  - title: Client Authorization
    url: https://community.torproject.org/onion-services/advanced/client-auth/
    publisher: Tor Project
  - title: Onion-Location
    url: https://community.torproject.org/onion-services/advanced/onion-location/
    publisher: Tor Project
  - title: Onion Services Properties
    url: https://onionservices.torproject.org/technology/properties/
    publisher: Tor Project
  - title: Changes in version 0.4.9.14 - 2026-10-07
    url: https://gitlab.torproject.org/tpo/core/tor/-/raw/tor-0.4.9.14/ReleaseNotes
    publisher: Tor Project
    date: 2026-10-07
  - title: Onionspray
    url: https://onionservices.torproject.org/apps/web/onionspray/
    publisher: Tor Project
  - title: HTTPS for your Onion Service
    url: https://community.torproject.org/onion-services/advanced/https/
    publisher: Tor Project
  - title: Capability and Limitations
    url: https://arti.torproject.org/guides/capability-limitations/
    publisher: Tor Project
  - title: Arti
    url: https://gitlab.torproject.org/tpo/core/arti
    publisher: Tor Project
  - title: Best Practices for Hosting Onion Services
    url: https://riseup.net/en/security/network-security/tor/onionservices-best-practices
    publisher: Riseup
  - title: Self-Hosting on the Dark Web
    url: https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/
    publisher: 个人博客
    date: 2026-06-01
  - title: How to bypass censorship and connect to Tor from different countries or regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: Users – Tor Metrics
    url: https://metrics.torproject.org/userstats-relay-country.html
    publisher: Tor Project
  - title: OONI API
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
authors:
  - anoni-net
---

一位作者 6 月在个人博客记录，把自己的静态网站放上 Tor 的 onion 服务（onion service，只能通过 Tor 连接、服务器位置受到保护的网站）。搭建用的是 tor（Tor Project 的主程序）与 nginx（网页服务器软件）。根据 Tor Project 的特性说明，onion 服务不需要固定 IP、域名，也不需要开放端口。tor 6 月 25 日到 10 月 7 日之间连续发布 0.4.9.11 到 0.4.9.14 四个安全更新，其中三个的修补涉及 onion 服务，到 10 月 20 日为止最新版是 0.4.9.14。

已经在运营 onion 服务的人要更新到最新版。网站的访客要通过 Tor 连接，例如用 Tor Browser。

依原文与官方的设置指南，做法是在 tor 的配置文件 `torrc` 指定一个存放密钥的目录与要转发的本机端口。重新启动 tor 之后，目录里的 `hostname` 文件就是网站的 .onion 地址。网页服务器只在本机监听，原文提到 Tor 本身就会加密连接，不需要另外配置 TLS（HTTPS 用的加密）。

同时经营一般网站的人要留意，静态网站生成器会把网址写进站内链接。原文因此另外生成一份以 .onion 地址为基准的版本，避免访客从 onion 服务点链接又回到一般网址。

设置指南另外建议把转发的目标从本机的网络端口改成 Unix socket（同一台电脑里程序之间交换数据的通道），避免服务泄露到局域网。指南也提醒，照这样设置的 onion 服务，任何知道地址的人都能读取。只想让特定的人连接时，可以设置客户端授权（client authorization），只有持有私钥的人连得上。Onion-Location 说明页提到，已经有 HTTPS 网站的人可以加上这个响应头，让 Tor Browser 打开原本的网站时在地址栏提示 .onion 版本。

## 导读观点 {#perspective}

官方说明提到，onion 服务的名称就是用来验证连接的公钥，所以不需要证书颁发机构（替网站签发 HTTPS 证书的机构）。连接由 Tor 从用户端一路加密到服务端。服务只对外建立连接、可以穿过 NAT（家用与机构网络共用对外 IP 的机制），学校或办公室这类不能开端口的网络也能搭建。根据特性说明，连得上 Tor 网络、服务也在线时就能连到 onion 服务，不受 DNS 与 IP 封锁的影响。

依官方的 Operational Security 页，服务器位置能否保持隐藏，要看搭建的人如何维护系统。网页服务器可能透露自己的种类与操作系统，电脑不是一直在线也会泄露信息。服务运行越久，位置被找到的风险也越高。同一页建议加装 Vanguards（降低入口节点被追查风险的附加组件）防范高级攻击。

设置指南也写，要让服务器不透露位置「not an easy task」（并不容易），并列出 Operational Security 页与 Riseup 的指南当参考。Riseup 的指南建议用 NTP（网络校时）自动校正服务器时间，避免时间误差被用来识别服务器。没有搭建过网页服务器的人，设置指南提到可以试试有图形界面、设置比较少的 OnionShare。Tor Project 的 Onionspray 则是替既有的公开网站加上 onion 服务入口，说明文档列出它不适合纯 onion 网站，也不保护网站的位置。

用 Rust 编程语言重写的 Arti，文档对能不能搭建 onion 服务说法不一。到 10 月 20 日为止，Arti 的项目页写已经实现，能力与限制页却写只完成一部分、默认关闭。Onionspray 的说明也写在 Arti 有替代方案之前仍依赖 C 语言实现的 tor，依这几份文档推论，正式搭建时以 tor 比较稳妥。

一般网站被封锁、但连得上 Tor 的读者，也能读到架在 onion 服务上的网站。依 Operational Security 页推论，搭建需要一台能长时间开机的主机。官方示例以 Debian 为主，过程是在命令行编辑配置文件、不需要写代码，设置指南有正体中文翻译（到 10 月 20 日为止部分段落仍是英文）。

在中国大陆访问 onion 服务，要先连上 Tor 网络。Tor Project 关于从受审查地区连接的支持页有简体中文版本，页面提到部分国家的网络运营商或国家防火墙会封锁直接连接 Tor 网络。页面对中国大陆的建议是先让 Tor Browser 的 Connection Assist（连接辅助功能）自动尝试网桥或 Snowflake，不行再改用 WebTunnel 网桥，其次是 Snowflake 与 meek（meek 带宽有限、速度较慢）。页面只说明连上 Tor 网络的方法，没有写 onion 服务在中国大陆能否访问。

根据 Tor Metrics 的估计，10 月 11 日到 17 日从中国大陆直接连接的日均用户约 1,055 人（只是估计值，不含经网桥连接的用户）。

OONI（网络干扰观测项目）9 月 18 日到 10 月 18 日在中国大陆的 Tor 测试有 301 笔，其中 293 笔标为异常、确认封锁 0 笔。异常不等于确认封锁，OONI 的 Tor 测试检查 Tor 运行所需的服务器能否连上，与 onion 服务本身无关。到 10 月 20 日为止，查不到中国大陆针对搭建 onion 服务的专门规范。

特性说明也列出，用户登录之后网站仍然记录得到数据。依 Operational Security 页推论，网站内容本身透露的信息要靠搭建的人自行把关。
