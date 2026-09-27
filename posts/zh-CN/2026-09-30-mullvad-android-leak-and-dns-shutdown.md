---
title: Android 的 VPN 漏洞与 Mullvad 加密 DNS 的停用
description: Android 有个漏洞让任何 App 绕过 VPN 暴露真实 IP，开着阻止未使用 VPN 的连接也挡不住。Mullvad 公开的加密 DNS 也将在 11 月 2 日停止服务。
date: 2026-09-30T07:00:00+08:00
slug: mullvad-android-leak-and-dns-shutdown
sources:
  - title: Another way to leak traffic on Android has been discovered
    url: https://www.mullvad.net/en/blog/2026/9/10/another-way-to-leak-traffic-on-android-has-been-discovered/
    publisher: Mullvad
    date: 2026-09-10
  - title: Shutting down our public encrypted DNS servers and sponsoring Quad9 instead
    url: https://www.mullvad.net/en/blog/2026/9/3/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead/
    publisher: Mullvad
    date: 2026-09-03
  - title: DNS over HTTPS and DNS over TLS
    url: https://mullvad.net/en/help/dns-over-https-and-dns-over-tls
    publisher: Mullvad
    date: 2026-09-03
  - title: Mullvad warns of a new Android VPN leak as GrapheneOS develops a fix
    url: https://cyberinsider.com/mullvad-warns-of-new-android-vpn-leak-as-grapheneos-works-on-fix/
    publisher: CyberInsider
    date: 2026-09-11
  - title: Disable unprivileged hardware keepalives
    url: https://github.com/GrapheneOS/platform_packages_modules_Connectivity/pull/47
    publisher: GrapheneOS
    date: 2026-09-26
  - title: Quad9 Privacy Policy
    url: https://quad9.net/privacy/policy/
    publisher: Quad9
    date: 2026-06-24
  - title: Service Addresses & Features
    url: https://quad9.net/service/service-addresses-and-features/
    publisher: Quad9
  - title: Is https://mullvad.net blocked in mainland China?
    url: https://en.greatfire.org/https/mullvad.net
    publisher: GreatFire
  - title: Is https://dns.quad9.net/dns-query blocked in mainland China?
    url: https://en.greatfire.org/https/dns.quad9.net/dns-query
    publisher: GreatFire
  - title: iOS 14 and later (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/iOS/iOS_14_and_later_%28Encrypted%29/
    publisher: Quad9
  - title: Android 9+ (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/Android/Android_9%2B_%28Encrypted%29/
    publisher: Quad9
authors:
  - anoni-net
---

VPN 服务商 Mullvad 在 9 月发了两则公告，都会影响用户的设置。一则是 Android 新发现的漏洞，任何 App 不需要特殊权限，就能让部分流量绕过 VPN，即使开着「阻止所有未使用 VPN 的连接」也一样。另一则是 Mullvad 公开的加密 DNS 将在 11 月 2 日停止服务，手动设置过的人要换掉。

漏洞出在 keep-alive 数据包。恶意 App 可以要求 Android 建立一条 keep-alive 的 UDP 连接，交给 Wi-Fi 或移动网络芯片自行发送，数据包直接从硬件出去，就绕过了 VPN 的检查。CyberInsider 报道，研究者估计多数 Android 12 以后的设备都受影响，这种数据包无法夹带任意数据，但足以暴露设备在 VPN 之外的网络身份。

研究者把漏洞报告给 Google 的漏洞奖励计划，被标记为重复报告，公开前没有修复，也没有 CVE。Mullvad 的公告写到，Google 不太可能处理，Mullvad 也没有打算提供缓解措施。

Mullvad 的公告写到，运营注重隐私的公共 DNS 需要高度专业，所以把资源改为资助 Quad9 基金会。使用 Mullvad VPN 的人不受影响，连接时由 VPN 服务器的 DNS 处理查询。使用默认设置的 Mullvad Browser 会自动改用 Quad9，iOS 与 macOS 的 Mullvad DoH 配置文件则会失效。

## 导读观点 {#perspective}

VPN 的锁定功能，靠操作系统检查每条连接有没有经过 VPN。这次的问题出在 Android 把 keep-alive 交给网络芯片处理，数据包根本不经过那道检查。所以 Mullvad 的建议落在源头，只安装信任的 App，可以的话改用 GrapheneOS 这类注重隐私与安全的 Android 版本。GrapheneOS 已经有关闭这类 keep-alive 的修复，到 9 月 27 日还没有合并发布。

在中国大陆，GreatFire 的测试显示 Mullvad 的网站被封锁，Quad9 的 DoH 地址连接也不稳定。身在境内的人要用 Mullvad，需先解决连接本身的问题，漏洞与 DNS 的调整是那之后的事。

替代的选项之一是 Mullvad 改为资助的 Quad9，它的隐私政策写明不收集、不记录用户的 IP，由瑞士的基金会运营。同一份政策也写到，Quad9 会保留按地区、运营商与协议分类的统计数字，这些统计不含个别用户的 IP，但 DNS 查询仍然集中在一家服务商手上。真实 IP 一旦泄露就有风险的人，还可以参考 CyberInsider 报道的做法，让手机接在强制走 VPN 的路由器后面，同时关闭移动网络等其他连接路径。

身在海外、手动设置过 Mullvad DoH 的人，要在 11 月 2 日前换掉，Quad9 的 DoH 地址是 `https://dns.quad9.net/dns-query`。iPhone 与 Mac 可以从 Quad9 的说明页下载配置描述文件，Android 在「私人 DNS」填入 `dns.quad9.net`，说明页有英文、法文、西班牙文与罗马尼亚文，没有中文。
