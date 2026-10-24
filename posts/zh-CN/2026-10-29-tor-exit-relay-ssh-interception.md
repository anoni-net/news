---
title: Tor 出口中继遭入侵、拦截 SSH 登录的事件
description: 2026 年 10 月初，三百多个 Tor 出口中继的设置被人改掉，经过它们的 SSH 连接被导到拦截服务器。用户接受了假的主机密钥、输入密码时，密码就会被取走。这些中继在北京时间 10 月 6 日凌晨之后已经不再列在 Tor 网络的共识里，加密的网页流量照常转送。依 The Hacker News 的整理，10 月 1 日到 5 日之间经由 Tor 用密码登录 SSH、又接受了陌生或改变过的主机密钥的人，要把那组密码当成已经外泄。
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
  - title: How to bypass censorship and connect to Tor from different countries or regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: 新加坡的 Tor 中继节点
    url: https://anoni.net/projects/pulse/sg/
    publisher: anoni.net
authors:
  - anoni-net
---

2026 年 10 月初，三百多个 Tor 出口中继的设置被人改掉。出口中继是 Tor 连接的最后一站，负责把流量送到目的地。经过这些中继的 SSH 连接（远程登录、管理服务器用的协议）被导到拦截服务器，用户接受了假的主机密钥、输入密码之后，密码就被取走。主机密钥是服务器用来证明自己身份的密钥。

受影响的是经由 Tor 用 SSH 登录服务器的人，经由 Tor 用未加密的连接收信的人也可能受影响。依 kaba 的文章，加密的网页流量照常转送，他推测攻击者想收集的是未加密的数据。

依一份目录数据的分析，Tor 的目录服务器从 UTC 10 月 4 日 18:00 起陆续投票，把受影响的中继标记成不能当出口。21:00（北京时间 10 月 5 日 05:00）起，共识带有这个标记。UTC 10 月 5 日 17:00（北京时间 10 月 6 日 01:00）起，用了攻击者设置的中继已经不再列在共识里，客户端不会选到它们。

10 月 20 日发表扫描经过的是一位以 kaba 为名的用户，他在 10 月 2 日经由 Tor 连 SSH 时看到主机密钥改变的警告。依他的文章，他接着扫描了全部约 3,000 个出口，找到 333 个有问题。其中约十来个自己出示假的主机密钥，其余三百多个把 SSH 连接转到同样的 12 台拦截服务器。他当晚就向 Tor Project 报告。

Tor 负责监控网络状况的 Network Health 团队在 10 月 5 日发布公告，对象是中继的运营者。依公告，攻击者取得 Linux 主机的权限之后修改 Tor 的配置文件，连原本不是出口的中继也被改成出口。团队也在调查主机被入侵的途径。

依 kaba 的文章，用户不理会警告、继续登录之后，拦截服务器会取走密码。它再把连接转给真正的服务器，用户输入的每个命令都会经过拦截服务器。

拦截服务器接着用同一组密码另外登录那台服务器，安装名为 Ebury 的后门。kaba 的蜜罐只看到安装程序的开头，对方就断线了。Ebury 藏在 OpenSSH 里窃取登录的账号密码，依 ESET 2024 年的报告，从 2009 年起约有 40 万台服务器被它入侵。

另一组数字来自一位中继运营者用公开目录数据做的分析。59 位运营者的 377 个中继在 10 月 1 日到 4 日之间发布了攻击者的出口政策，也就是中继允许连往哪些端口的设置。其中 351 个在 UTC 10 月 4 日 01:00 占可用出口权重的 7.46%。客户端大致依权重挑选出口，本文据此推算，选到它们的机会约是这个比例。

分析者注明这只代表设置吻合、不能证明主机都被入侵，跟 kaba 主动扫描得到的 333 是不同的算法。377 个里有 277 个属于同一个中继家族。家族的运营者在事后复盘里写，SSH 登录、sudo 与备份共用同一组密码，管理服务器又开着密码登录。攻击者最初从哪里取得这组密码，还不知道。

家族检查的两台服务器装了 Ebury，其他受影响的主机有没有，公开数据看不出来。另外 58 位运营者的中继为什么出现同样的设置、是否被入侵，到 10 月 24 日为止还不清楚，受害的用户有多少也没有数字。

## 导读观点 {#perspective}

Tor 只在自己的网络里加密，出口中继看得到送往目的地的流量。连接有没有加密、能不能确认对方的身份，要靠使用的协议。

SSH 用主机密钥确认连上的是真正的服务器。依 OpenSSH 的说明文档，主机密钥改变时 ssh 会警告并停用密码登录，默认设置下直接拒绝连接。用户要自己删掉旧的密钥记录或改掉设置，才连得上。第一次连接的服务器没有旧记录可以比对，用户只会看到一般的确认提示，按下同意就接受了拦截服务器的密钥。

The Hacker News 的报道依 SSH 的协议规格 RFC 4252 推论，只有用密码登录的人会被取走账号密码。用密钥登录时，签名绑定这一次连接，拦截者无法拿去登录真正的服务器。同一篇报道也写到，拦截者仍可以接受密钥登录、显示一个假的命令行界面。本文的推论是，用密钥登录的人如果在那个界面输入了 sudo 之类的密码，那组密码一样可能外泄。

报道据此写出的范围，是 10 月 1 日到 5 日之间经由 Tor 用密码登录、又接受了陌生或改变过的主机密钥的人，报道没有标时区。Tor 的公告与发现者的文章都没有这样界定。家族的事后复盘写到，他们的服务器在 9 月 30 日就出现用途不明的隐藏进程，所以起点只能当参考。

报道建议符合条件的人把那组密码当成已经外泄，被登录的那台服务器也可能已经被装上 Ebury。家族运营者提醒，不要在可能被入侵的服务器上输入密码，因为 Ebury 会记下来。检查要先用密钥登录或从救援系统开机。

本文的建议是，其他用过同一组密码的服务可以先换，被登录的那台等检查完再换。ESET 公开了 Ebury 的检测脚本，10 月 9 日之后的版本才能检测到这次的 Ebury。脚本本身也注明，没找到不代表系统是干净的。

之后经由 Tor 管理服务器时，本文建议改用密钥登录，第一次连接时向管理员确认主机密钥的指纹。也可以把 SSH 设成 onion 服务（只能经由 Tor 连上、连接不离开 Tor 网络的服务），onion 服务的连接不经过出口中继，出口的拦截也就影响不到。依分析者的整理，多数受影响中继的出口政策关掉了加密收信的端口，明文的端口维持开放。经由 Tor 收信的人要确认邮件软件用的是加密连接。

Tor 的中继由各地志愿者架设，任何人都能加入，检测靠 Network Health 团队的扫描与用户报告。这次在 kaba 报告之后约两天出现标记，用了攻击者设置的中继全部不再列在共识里，又花了将近一天。

anoni.net 社区用 Tor 软件包附的 IP 地理位置数据库，比对分析者公开的 377 个中继。台湾、日本、韩国、香港都没有受影响的中继，新加坡有 24 个，全部属于同一个家族。地理位置数据库可能有误差。

社区的 Tor 中继节点观测也记录到，新加坡有出口标记（Exit）的中继从 UTC 10 月 3 日的 34 个降到 10 月 4 日的 9 个，本文推测跟这次的标记有关。客户端挑选出口时不看用户在哪里，所以中继在哪个国家，跟读者有没有受影响无关。

Tor Project 关于从受审查地区连接的支持页有简体中文版本，页面提到部分国家的网络运营商或国家防火墙会封锁直接连接 Tor 网络。页面对中国大陆的建议是先让 Tor Browser 的 Connection Assist（连接辅助功能）自动尝试网桥或 Snowflake，不行再改用 WebTunnel 网桥。网桥取代的是 Tor 线路的第一站，连接最后仍由出口中继送到目的地，所以通过网桥连接的人同样适用上面的建议。在海外使用 Tor 的简体中文读者也一样。

到 10 月 24 日为止，Tor Project 还没有公布其他运营者的中继如何被改。Ebury 的研究者在 tor-relays 邮件列表上写，很可能还有其他被入侵的 Tor 中继没被发现。接下来可以留意 Network Health 团队的调查结果，以及是否发现新的受影响中继。
