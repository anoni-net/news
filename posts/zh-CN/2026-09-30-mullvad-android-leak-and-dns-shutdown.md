---
title: Android 的 VPN 漏洞与 Mullvad 加密 DNS 的停用
description: Android 的一个漏洞让任何 App 绕过 VPN、泄露真实 IP，开启「屏蔽未使用 VPN 的所有连接」也无法阻止。Mullvad 的公共加密 DNS 将在 11 月 2 日停止服务，手动设置过的人需要更换。
date: 2026-09-30T00:00:00+08:00
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
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases
    publisher: GrapheneOS
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#supported-devices
    publisher: GrapheneOS
  - title: Quad9 Privacy Policy
    url: https://quad9.net/privacy/policy/
    publisher: Quad9
    date: 2026-06-24
  - title: Service Addresses & Features
    url: https://quad9.net/service/service-addresses-and-features/
    publisher: Quad9
  - title: iOS 14 and later (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/iOS/iOS_14_and_later_%28Encrypted%29/
    publisher: Quad9
  - title: Big Sur and later (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/MacOS/Big_Sur_and_later_%28Encrypted%29/
    publisher: Quad9
  - title: Android 9+ (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/Android/Android_9%2B_%28Encrypted%29/
    publisher: Quad9
  - title: packages/apps/Settings/res/values-zh-rTW/strings.xml
    url: https://github.com/aosp-mirror/platform_packages_apps_settings/blob/main/res/values-zh-rTW/strings.xml
    publisher: Android Open Source Project
  - title: frameworks/base/packages/SettingsLib/res/values-zh-rTW/strings.xml
    url: https://github.com/aosp-mirror/platform_frameworks_base/blob/main/packages/SettingsLib/res/values-zh-rTW/strings.xml
    publisher: Android Open Source Project
  - title: Is https://mullvad.net blocked in mainland China?
    url: https://en.greatfire.org/https/mullvad.net
    publisher: GreatFire
  - title: Is https://dns.quad9.net/dns-query blocked in mainland China?
    url: https://en.greatfire.org/https/dns.quad9.net/dns-query
    publisher: GreatFire
  - title: packages/apps/Settings/res/values-zh-rCN/strings.xml
    url: https://github.com/aosp-mirror/platform_packages_apps_settings/blob/main/res/values-zh-rCN/strings.xml
    publisher: Android Open Source Project
  - title: frameworks/base/packages/SettingsLib/res/values-zh-rCN/strings.xml
    url: https://github.com/aosp-mirror/platform_frameworks_base/blob/main/packages/SettingsLib/res/values-zh-rCN/strings.xml
    publisher: Android Open Source Project
authors:
  - anoni-net
---

VPN 服务商 Mullvad 9 月的两则公告，分别影响在 Android 上使用 VPN 的人，以及手动设置过 Mullvad 加密 DNS 的人。Android 新发现的漏洞使任何 App 不需要特殊权限就能让部分数据包绕过 VPN，开启「屏蔽未使用 VPN 的所有连接」也无法阻止。研究者估计多数 Android 12 及以上的设备受影响，但并非每个型号都实测过。Mullvad 的公共加密 DNS 则将在 11 月 2 日停止服务。

漏洞出在 keep-alive 数据包（为了维持连接、定期发送的小数据包）。恶意 App 可以要求 Android 建立一条 keep-alive 连接，由 Android 交给 Wi-Fi 或移动网络芯片发送。网络安全新闻网站 CyberInsider 报道，数据包格式由 Android 决定，无法夹带任意数据。接收的服务器仍能看到设备在 VPN 之外的真实 IP。

研究者 5 月 15 日把漏洞报告给 Google 的 Android 漏洞奖励计划，之后被标记为重复报告。公开前，Google 没有告知修复，也没有分配 CVE（公开漏洞的统一编号）。Mullvad 9 月 10 日的公告写到，Google 不太可能处理。

9 月 3 日关于 DNS 的公告写明，运营注重隐私的公共 DNS 需要高度专业，Mullvad 决定改为资助 Quad9 基金会（提供公共 DNS 的瑞士非营利组织）。使用 Mullvad VPN 的人不受影响，查询由 VPN 服务器处理。使用默认设置的 Mullvad Browser 会自动改用 Quad9，手动选过其他 Mullvad DNS 变体的人要改回默认。iOS 与 macOS 上 Mullvad 的 DNS 描述文件则会失效。

## 导读观点 {#perspective}

开启「屏蔽未使用 VPN 的所有连接」时，系统会检查每条连接是否经过 VPN，keep-alive 交给网络芯片后就不经过这道检查。网络硬件能同时维持的 keep-alive 连接有上限，据 Mullvad 的公告，理论上先把名额占满就能挡住恶意 App。Mullvad 不打算这样做，因为占位的连接同样要在 VPN 外发出数据包，恶意 App 也可能在 Mullvad App 启动前就开始泄露。CyberInsider 9 月 11 日的报道写到，当时没有可靠的应用层修复。

Mullvad 的建议是只安装信任的 App，可以的话改用 GrapheneOS 这类强化隐私与安全的 Android 版本，不过 GrapheneOS 的正式版只支持 Pixel 6 及以上的 Pixel 设备。GrapheneOS 关闭这类 keep-alive 的修复在 9 月 28 日合并，到 9 月 29 日为止还没有进入正式版。

真实 IP 一旦泄露就有风险的人，可以参考 CyberInsider 报道的做法，让手机连上强制走 VPN 的路由器。前提是关闭移动网络等其他连接路径。手机离开这台路由器就失去保护。

到 9 月 29 日为止，GreatFire（测试中国大陆网址封锁状况的网站）近 90 天对 mullvad.net 的 17 次测试结果全部是封锁。被封锁的网址也包括 Android、Windows、macOS 与 Linux 版的下载链接。Quad9 的 DoH（DNS over HTTPS）地址最近两次有结果的测试也都受到干扰，最后一次在 9 月 3 日。

身在海外、手动设置过 Mullvad 加密 DNS 的人，要在 11 月 2 日前更换，可以改用 Quad9。iPhone（iOS 14 及以上）与 Mac（Big Sur 及以上）要用 Safari 下载 Quad9 说明页（没有中文版）的描述文件，2027 年 1 月 19 日到期后需重新安装。Android 9 及以上在「专用 DNS」填入主机名 `dns.quad9.net`，这一项走 DoT（DNS over TLS），不能填 DoH 地址 `https://dns.quad9.net/dns-query`。同时使用其他 VPN 的人，描述文件与专用 DNS 通常不会生效，说明页写明要改在 VPN App 的自定义 DNS 设置 Quad9。

Quad9 的隐私政策写明用户的 IP 只在处理查询的极短时间内留在内存，另外保留的统计按地区、电信网络与协议分类，不含个别 IP。改用之后，DNS 查询仍集中在同一个运营方手上。
