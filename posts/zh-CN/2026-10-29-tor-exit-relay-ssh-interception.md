---
title: Tor 出口中继的 SSH 登录拦截事件
description: 10 月初，三百多个 Tor 出口中继的设置遭到窜改，经过它们的 SSH 连接被导到拦截服务器。10 月 1 日到 5 日之间经由 Tor 用密码登录 SSH、又接受了陌生或改变过的主机密钥的人，要把那组密码当成已经外泄。这些中继在北京时间 10 月 6 日 01:00 前已经从 Tor 的可用中继清单消失，依发现者的文章，加密的网页流量照常转送。
date: 2026-10-29T00:00:00+08:00
slug: tor-exit-relay-ssh-interception
categories:
  - security
sources:
  - title: Security incident affecting some relay operators
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/WOHPLKCSHYXFTBRZXDENDKJZMBMPLMG5/
    publisher: Tor Project
    date: 2026-10-05
  - title: "Ebury 1.8.3 on two Quetzalcoatl relay servers: timeline, lessons, open questions"
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/QHRD6YOX6RZRDR7NCHNDO7GLCEA6VFM6/
    publisher: tor-relays
    date: 2026-10-07
  - title: "Re: Ebury 1.8.3 on two Quetzalcoatl relay servers: timeline, lessons, open questions"
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/message/Z2B6XYKJZBBQADU77MSNL6FJP7MHZHIV/
    publisher: tor-relays
    date: 2026-10-09
  - title: How I got over 300 Tor exit nodes removed
    url: https://kaba.cx/posts/20261020_Tor/
    publisher: kaba.cx
    date: 2026-10-20
  - title: Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections
    url: https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
    publisher: The Hacker News
    date: 2026-10-21
  - title: How to bypass censorship and connect to Tor from different countries or regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: "Ebury is alive but unseen: 400k Linux servers compromised for cryptotheft and financial gain"
    url: https://www.welivesecurity.com/en/eset-research/ebury-alive-unseen-400k-linux-servers-compromised-cryptotheft-financial-gain/
    publisher: ESET
    date: 2024-05-14
  - title: ssh(1) - OpenBSD manual pages
    url: https://man.openbsd.org/ssh
    publisher: OpenBSD
  - title: ssh_config(5) - OpenBSD manual pages
    url: https://man.openbsd.org/ssh_config
    publisher: OpenBSD
authors:
  - anoni-net
---

10 月初，三百多个 Tor 出口中继（Tor 连接的最后一站，负责把流量送到目的地）的设置遭到窜改，经过它们的 SSH 连接（远程登录、管理服务器用的协议）被导到拦截服务器。用户接受了假的主机密钥（服务器用来证明身份的密钥）、输入密码之后，密码就被取走。受影响的是经由 Tor 用 SSH 登录服务器的人，经由 Tor 用未加密连接收信的人也可能受影响。这些中继在北京时间 10 月 6 日 01:00 前已经从 Tor 的可用中继清单消失，依发现者的文章，加密的网页流量照常转送。

发现者是一位经由 Tor 连 SSH 的用户，10 月 2 日看到主机密钥改变的警告。他接着扫描全部约 3,000 个出口，找到 333 个出示假的主机密钥或把连接转往拦截服务器的出口，当晚报告 Tor Project。其中十多个本身出示假的主机密钥，其余三百多个把连接转到同样的 12 台拦截服务器。

依发现者的文章，用户继续登录之后，拦截服务器取走密码并把连接转给真正的服务器。用户输入的每个命令都会经过拦截服务器。

拦截服务器接着用同一组密码另外登录用户原本要连的服务器，试图安装名为 Ebury 的后门（让攻击者之后能再次登录的程序），发现者没有看到完整的安装。Ebury 植入服务器的 SSH 软件 OpenSSH，会记下登录时输入的账号密码。ESET 2024 年的报告统计，2009 年起累计约有 40 万台服务器受害。

Tor 负责监控网络状况的 Network Health 团队在 UTC 10 月 5 日 17:50（北京时间 10 月 6 日 01:50）发布公告，提到攻击者取得 Linux 主机的权限之后修改 Tor 的配置文件，连原本不是出口的中继也被改成出口。Tor 的目录服务器（定期公布可用中继清单的一组服务器，这份清单称为共识）从 UTC 10 月 4 日晚上（北京时间 10 月 5 日清晨）起，陆续把受影响的中继标记成不能当出口。

一位中继运营者比对公开的目录数据，找到 59 位运营者的 377 个中继在 10 月 1 日到 4 日之间套用了同一组出口政策（中继允许连往哪些端口的设置）。分析者提醒，这只代表设置吻合，不能证明主机都被入侵或每一个都拦截 SSH。高峰时这些中继占可用出口权重（目录服务器给每个出口的流量比重）的约 7%。Tor 客户端大致依权重挑选出口，本文据此推算，经由 Tor 的连接约有 7% 的几率选到它们。

其中 277 个属于同一个中继家族（同一位运营者登记在一起的一组中继）。家族运营者的事后复盘写到，他们登录服务器、取得管理权限（sudo）与备份都用同一组密码，管理服务器也允许用密码登录。攻击者最初从哪里取得这组密码，还不清楚。家族运营者检查的两台服务器装了 Ebury，其他受影响的主机是否也有，从公开数据无法判断。

## 导读观点 {#perspective}

Tor 只在自己的网络里加密，出口中继可以读取送往目的地的流量。HTTPS 与 SSH 自带加密与身份验证，未加密的收信协议没有。

SSH 用主机密钥确认连上的是真正的服务器。依 OpenSSH 的说明文档，主机密钥改变时 `ssh` 程序会显示警告并停用密码登录，默认设置下直接拒绝连接。用户要自行删除旧的密钥记录，才会走到输入密码这一步。第一次连接的服务器没有旧记录可以比对，用户只会看到一般的确认提示，按下同意就接受了拦截服务器的密钥。

The Hacker News 依 SSH 的协议规格推论，只有用密码登录的人会被取走账号密码。用密钥登录（以自己电脑上的私钥证明身份、不把密码送给服务器的登录方式）时，每次登录的证明只对这一次连接有效，拦截者无法用它登录真正的服务器。报道也提到，拦截者仍可以接受密钥登录、显示假的命令行界面。用密钥登录的人如果在假界面输入了 sudo 之类的管理密码，本文推论那组密码一样可能外泄。

The Hacker News 的建议是，10 月 1 日到 5 日之间经由 Tor 用密码登录、又接受了陌生或改变过的主机密钥的人，要把那组密码当成已经外泄。家族运营者的服务器在 9 月 30 日就出现用途不明的隐藏进程，运营者无法确定它们是否也在拦截 SSH，所以 10 月 1 日之前登录的人也不能排除。

家族运营者写到，Ebury 会记下在受感染服务器上输入的密码。检查时要用密钥登录，或从救援系统（不经过原本系统开机的维护环境）开机。

外泄的那组密码，其他用到它的服务可以先换，被登录的服务器等检查完再换。ESET 公开的检测脚本要在服务器的命令行运行，10 月 9 日合并的更新才能检测到这次的 Ebury，没找到也不代表服务器是干净的。

之后经由 Tor 管理服务器时，发现者建议改用密钥登录。第一次连接时，可以先向管理员索取主机密钥的指纹（密钥的一串识别码，连接时界面上会显示）来核对。

另一个做法是把 SSH 设成 onion 服务（只能经由 Tor 连上、连接不离开 Tor 网络的服务），连接不经过出口中继，就不会被出口中继拦截。代价是密钥登录要保管好私钥，换电脑或遗失时要重新设置。onion 服务则要在服务器上运行 tor，设置比直接开放 SSH 多一步。

依分析者的整理，多数受影响的中继关掉加密的收信端口、只放行未加密的，经由它们转送的收信流量因此全是明文。没有来源确认邮件内容实际被读取，经由 Tor 收信的人仍要确认邮件软件用的是加密连接。

Tor 的中继由各地志愿者架设，任何人都能加入，被入侵或恶意的中继需仰赖 Network Health 团队的扫描与用户报告才能找出。发现者 10 月 2 日报告，到 UTC 10 月 5 日 17:00 受影响的中继全部离开共识，花了约三天。

Tor 客户端默认挑选出口时不考虑用户的所在位置，所以中继在哪个国家，跟读者是否受影响无关。社区用地理位置数据比对那 377 个中继，台湾、日本、韩国、香港都没有，新加坡有 24 个且都属于同一个家族（地理位置数据可能有误差）。

Tor Project 关于从受审查地区连接的支持页有简体中文版本，页面提到部分国家的网络运营商或国家防火墙会封锁直接连接 Tor 网络。页面对中国大陆的建议是先让 Tor Browser 的 Connection Assist（连接辅助功能）自动尝试网桥或 Snowflake，不行再改用 WebTunnel 网桥。网桥取代的是 Tor 线路的第一站，连接最后仍由出口中继送到目的地，所以通过网桥连接的人同样适用上面的建议。在海外使用 Tor 的简体中文读者也一样。

只用 Tor Browser 浏览 HTTPS 网站、没有经由 Tor 用 SSH 或收信的人，不需要做任何设置。到 10 月 24 日为止，我们在 Tor Project 的博客、状态页与邮件列表上没有找到其他 58 位运营者的中继为何套用同一组政策的说明。ESET 的 Ebury 研究者在 Tor 中继运营者的邮件列表上写到，很可能还有其他被入侵的中继没被发现。可以在 11 月 25 日前后留意 Tor Project 是否公布这批中继的入侵途径，以及是否发现新的受影响中继。
