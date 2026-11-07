---
title: OpenSSH 在 musl 系统上的长密码登录绕过漏洞
description: OpenSSH 11 月 5 日发布 10.6p2，修补超长密码可以登录没有设密码账号的漏洞。只有 Linux 上用 musl libc、不经 PAM 验证密码的 sshd 在范围内，例如 Alpine Linux。依 OpenSSH 维护者与 HKCERT 的说明，Debian、Ubuntu、Red Hat 这类用 glibc 的系统不在范围内，到 11 月 8 日两家发行版的跟踪页还没有标为不受影响。到 11 月 8 日，中国的漏洞库（CNVD、CNNVD）无法读取，没有取得相关条目。在 Alpine 上运行 sshd 的人要更新或关闭密码登录。
date: 2026-11-09T00:00:00+08:00
slug: openssh-sshole
categories:
  - security
sources:
  - title: OpenSSH Release Notes
    url: https://www.openssh.com/releasenotes.html#10.6p2
    publisher: OpenSSH
    date: 2026-11-05
  - title: "Security advisory: openssh-server password authentication bypass"
    url: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
    publisher: Alpine Linux
    date: 2026-11-05
  - title: "\"sshole\": password authentication bypass: OpenSSH + musl libc"
    url: https://www.openwall.com/lists/oss-security/2026/11/05/3
    publisher: oss-security
    date: 2026-11-05
  - title: OpenSSH 10.6p2 has been released with a workaround for a critical vulnerability
    url: https://hachyderm.io/@damienmiller/117563026759098135
    publisher: Hachyderm.io
    date: 2026-11-05
  - title: "*sshole"
    url: https://sshhole.com
    publisher: sshhole.com
  - title: Meet *sshole, the vulnerability that lets hackers SSH into Linux devices
    url: https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/
    publisher: Ars Technica
    date: 2026-11-05
  - title: OpenSSH發布緊急更新，修補可利用長密碼繞過身分驗證的資安漏洞SSHole
    url: https://www.ithome.com.tw/news/180281
    publisher: iThome
    date: 2026-11-06
  - title: CVE-2026-123158
    url: https://access.redhat.com/security/cve/CVE-2026-123158
    publisher: Red Hat
  - title: CVE-2026-123158
    url: https://security-tracker.debian.org/tracker/CVE-2026-123158
    publisher: Debian
  - title: CVE-2026-123158
    url: https://ubuntu.com/security/CVE-2026-123158
    publisher: Ubuntu
    date: 2026-11-06
  - title: OpenSSH Security Restriction Bypass Vulnerability
    url: https://www.hkcert.org/security-bulletin/openssh-multiple-vulnerabilities_20261106
    publisher: HKCERT
    date: 2026-11-06
  - title: 資安警訊
    url: https://www.twcert.org.tw/tw/lp-169-1.html
    publisher: TWCERT/CC
  - title: JPCERT/CC
    url: https://www.jpcert.or.jp/english/
    publisher: JPCERT/CC
  - title: JVN
    url: https://jvn.jp/en/
    publisher: JVN
authors:
  - anoni-net
---

OpenSSH 在 11 月 5 日发布 10.6p2，修补一个用超长密码就能登录「没有设密码的账号」的漏洞，发现者取名为 \*sshole。范围很窄，只有 Linux 上用 musl libc（C 语言的标准函数库，程序调用系统功能时经过它）、而且不经 PAM（Linux 上统一处理登录验证的模块）验证密码的 sshd（OpenSSH 的服务器程序）受影响。依 OpenSSH 维护者在 Mastodon 的帖子，以及香港电脑保安事故协调中心（HKCERT）与 Red Hat 的说明，Debian、Ubuntu、Red Hat 这类用 glibc 的系统不在范围内。需要检查的是 Alpine Linux（常用来制作容器镜像的发行版）上有运行 sshd 的机器，以及其他用 musl、又装了 OpenSSH 的系统，例如部分嵌入式设备。

依 Alpine 的安全公告，四个条件同时成立才受影响。sshd 用的是 Alpine 默认不含 PAM 的 `openssh-server`，或是含 PAM 的版本但设成 `UsePAM no`。密码登录保持开启，这是 OpenSSH 的默认值。机器上有密码字段为 `*` 的账号（只用密钥登录、没有设密码的账号常是这样），另外至少还有一个账号设了密码。

符合条件时，攻击者只要知道那个 `*` 账号的名称，发送 257 到 1,024 字节的任意密码就能登录。公告写只需要一次连接，每次都会成功。

依同一份公告的说明，不经 PAM 时 sshd 用 `crypt()` 把收到的密码算成哈希，再跟账号的密码字段比对。字段太短、放不下 salt（混进密码一起计算的随机值）时，sshd 会借用其他账号的 salt。musl 的 `crypt()` 遇到超过 256 字节的密码时返回字符串 `*` 当作错误标记，跟没有密码的账号字段相同，比对就成立了。依 oss-security 邮件列表上的通报，修补版改成检查哈希的最短长度，不再接受 `*`。

发现者的说明页把成因追溯到三个项目各自的修改。2012 年 musl 为了避免超长密码拖慢服务器，把密码限制在 256 字节。2016 年 OpenSSH 改成借用其他账号的 salt，用意是不让攻击者从响应时间判断账号存不存在，Alpine 则在 2022 年的 3.16 版前后把 root 的密码字段改成 `*`。说明页写 OpenSSH 在 OpenBSD 与 glibc 上测试，musl 不测试 sshd，多数发行版又经过 PAM。

依 Alpine 的公告，OpenSSH 默认的 `PermitRootLogin prohibit-password` 不让 root 用密码登录。其他能登录的账号若能通过 doas（类似 sudo 的提权工具）获取 root 权限，这道设置就挡不住。旧版的官方云镜像内置一个 `alpine` 账号，密码字段是 `*`，用 doas 也不必输入密码。公告提到这些镜像第一次开机时是安全的，管理者替任何账号设了密码之后（例如控制台的登录密码）就可以被利用。

OpenSSH 的发布说明写他们认为根本原因在 sshd 之外，但可以在 sshd 这一端避开。依 Ars Technica 的报道，一位 musl 开发者的立场是问题出在调用端的用法，musl 本身没有 bug。他也提到 musl 计划在之后的版本修改这个机制。

漏洞之后获得 CVE（公开漏洞的统一编号）CVE-2026-123158，严重度评分（CVSS，满分 10）为 8.1。到 11 月 8 日，OpenSSH、Alpine、Ars Technica 与 iThome 都没有提到实际被利用的案例，HKCERT 的通报则写已经有公开的 PoC（证明漏洞能被利用的程序）。依 Ars Technica 引述安全公司 Detectify 的说法，Shodan（扫描全网络设备的搜索引擎）列出约 2,200 万台开着 SSH 22 端口的系统。Ars 的评估是其中只有一部分符合条件，但逐台测试又快又容易，找出受影响的设备不需要花太多力气。

## 导读观点 {#perspective}

Red Hat 的说明页写旗下产品不受影响，因为产品里的 OpenSSH 链接的是 glibc，也默认使用 PAM。到 11 月 8 日，Debian 的跟踪页把 bookworm、trixie 的 OpenSSH 标成 vulnerable、紧急程度标 unimportant，Ubuntu 的页面则标「Needs evaluation」。Debian 的表以 sid 的 `1:10.6p2-1` 为修正版本，更早的版本都标 vulnerable，本文据此推论是依版本号标示。紧急程度标 unimportant，也与 HKCERT、OpenSSH 维护者写的 glibc 系统不受影响一致。

Ars 的报道写 Docker Hub 上的 Alpine 基础镜像下载超过 10 亿次，不过依 Alpine 的公告，容器里没有运行 sshd 的用户不受影响。用 cloud-init（云主机第一次开机时应用设置的工具）写入 `PasswordAuthentication no` 的云镜像也不在范围内。

依 Ars Technica 的报道，Alpine 长年用在路由器、智能电视与工业控制器，这类设备很多很难更新。发现者把 OpenWrt、Buildroot、Yocto 列为用 musl 的系统。Ars 补充 OpenWrt 默认的 SSH 服务器是 Dropbear，另外安装 OpenSSH 才在范围内。Ars 也写发现者说 Buildroot 与 Yocto 受影响，但到 11 月 5 日还没有确认。

用 Raspberry Pi OS 的树莓派属于 Debian 系、用 glibc，本文推论不在范围内，装 Alpine 的则照 Alpine 的条件检查。家用 NAS 与路由器是否受影响，本文参考的来源都没有提到，到 11 月 8 日也没有查到厂商的公告。

香港的 HKCERT 在 11 月 6 日发布通报，风险评级 Medium，写明有公开的 PoC。通报也写 Red Hat、SUSE、Ubuntu、Debian 等主流 Linux 发行版用 glibc，不受影响。到 11 月 8 日，台湾 TWCERT/CC 的资安警讯列表与日本 JPCERT/CC、JVN 的首页查不到相关条目（首页只列最新项目，查不到不等于没有）。

中国的 CNVD 到 11 月 8 日无法打开，CNNVD 的页面没有内容，也没有搜到中国机构的通报。本文没有取得中国机构的说明可对照，中国境内的读者可以参考 HKCERT 的通报与 Alpine 的公告，海外的读者也一样。境内哪些设备用 musl 加 OpenSSH，本文参考的来源没有提到。

依维护者的帖子，OpenSSH 团队得知问题的隔天就发布修正版。理由是团队最近多次遇到 AI 代理很快重新发现已知的漏洞，有时只隔几小时。团队因此认为长时间的保密期是危险的做法，主要对攻击者有利。发布说明也写，目前会更频繁地发布修正版，不再累积到下一个预定版本。

依 Alpine 的公告，在 Alpine 上自己管理 sshd 的人要更新 `openssh` 软件包并重新启动 sshd，只升级软件包不会替换已经在运行的服务。Alpine 从 3.16 起的每个版本都有修补软件包，包含已经停止支持的版本，版本对照与命令见公告。上游的修正版本是 OpenSSH 10.6p2，各系统的修补软件包可能沿用旧的版本号（Alpine 就是如此），本文参考的来源没有写其他系统如何更新。

暂时无法更新时可以关闭密码登录。依 oss-security 的通报，关闭之后就能避开漏洞，代价是不能再用密码登录。Alpine 的公告提醒先确认密钥登录可用，并保留当前的连接直到新的登录测试成功。

公告也列出事后检查的方法，看登录日志里有没有没设密码的账号出现 `Accepted password`，无法排除时把机器当成已被入侵处理。只用 Debian、Ubuntu、Red Hat 系统的人，依维护者与 HKCERT 的说明不需要为这个漏洞改设置。这是依 glibc 与 PAM 的条件推论，到 11 月 8 日 Debian 与 Ubuntu 的跟踪页还没有跟着更新。
