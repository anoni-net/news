---
title: Tor Browser 16.0 与 Tails 7.16
description: Tor Browser 16.0 推出桌面版与 Android 版，改以 Firefox ESR 153 为基础。桌面版重新设计设置页，新增默认关闭的通用窗口标题，32 位 x86 Linux 从这一版起不再支持。Tails 7.16 把内置的 Tor Browser 更新到 16.0，Tails 7.0 或更新的版本可以自动升级。
date: 2026-11-05T00:00:00+08:00
slug: tor-browser-16-tails
categories:
  - tracking
sources:
  - title: "New Release: Tor Browser 16.0"
    url: https://blog.torproject.org/new-release-tor-browser-160/
    publisher: Tor Project
    date: 2026-10-29
  - title: Tails 7.16
    url: https://tails.net/news/version_7.16/
    publisher: Tails
    date: 2026-10-30
  - title: Known issues
    url: https://tails.net/support/known_issues/
    publisher: Tails
  - title: How to bypass censorship and connect to Tor from different countries or regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: www.torproject.org
    url: https://en.greatfire.org/https/www.torproject.org
    publisher: GreatFire
  - title: support.torproject.org
    url: https://en.greatfire.org/https/support.torproject.org
    publisher: GreatFire
  - title: 计算机信息网络国际联网管理暂行规定
    url: https://www.cac.gov.cn/1996-02/02/c_126468621.htm
    publisher: 国家网信办（转载）
authors:
  - anoni-net
---

Tor Project 10 月 29 日发布 Tor Browser 16.0，桌面版与 Android 版同时推出，是第一个以 Firefox ESR 153（Firefox 的长期支持版本）为基础的稳定版。Tails（从 U 盘启动、所有连接都经过 Tor 的操作系统）隔天发布 7.16，把内置的 Tor Browser 更新到 16.0。Windows、macOS、Linux 与 Android 的用户都在更新范围内，只有 32 位 x86 的 Linux 电脑从 16.0 起不再支持。

依 Tor Project 的公告，换到新的 ESR 时团队会做每年一次的审查。这次检查并处理了超过 270 条 Bugzilla（Mozilla 的缺陷跟踪系统）议题，对象是 Firefox 一年来可能损害 Tor Browser 用户隐私与安全的变更。变更日志里有多项停用或隐藏的条目，例如 WebGPU（让网页直接使用显卡运算的新接口）在审查完成前停用，AI 设置面板与翻译设置页隐藏起来。Android 版也停用 AI 功能与 Google Lens，这些条目都只有标题，没有说明理由。

桌面版的设置页跟着 Firefox 6 月的改版重新设计，原本的“一般”页拆到外观、下载、标签页与浏览、无障碍、语言几个新页面（页面名称依英文公告翻译）。连接与安全等级这些 Tor Browser 特有的页面，改用 Firefox 的新组件重写。公告提到，开启后可能损害隐私或让浏览器更容易被识别指纹（网站从浏览器设置与设备特征认出同一台设备）的设置，有的隐藏、有的加上警告。原本的偏好设置会保留，找不到的选项可以用设置页顶端的搜索栏。

设置里另外新增通用窗口标题（位置在 Privacy and security → Protections from third-party applications），开启后所有窗口标题都换成“Tor Browser”。依公告的说明，浏览器通常把正在浏览的网页标题当成窗口名称，电脑上的其他程序与操作系统不需要特别权限就能读取。选项默认关闭，公告写到这次的开发周期来不及评估副作用。可能受影响的是使用屏幕阅读器的人，以及高度自定义系统的人（例如使用少见的桌面环境或程序切换器）。

Linux 版新增 64 位 ARM 处理器的原生支持，例如 Raspberry Pi 与安装 Linux 的 Apple Silicon Mac。32 位 x86 Linux 跟着 Firefox 停止支持，公告发布时每天约有 200 次更新检查来自这个平台，2019 年高峰时约 4,000 次。

桌面版内置的用户手册（地址栏输入 `about:manual`，或从菜单 ☰ → Help → Tor Browser manual 打开）换成新支持网站的内容，一样可以离线阅读，连不上 Tor 网络时也能查。Google Play 限制以 APK 发布的 App 不能超过 100 MB，Android 版的手册因此一直无法内置、离线阅读。Android 版的界面大量改用 Material Design 3（Google 为 Android 制定的设计规范），公告写到后续版本还会继续改。变更日志也列出 Android 版移除密码界面、停用所有链接分享功能，以及停用导入书签。

依 Tails 的公告，7.16 把 Tor Browser 更新到 16.0，连带换上新的设置页。Tor 客户端更新到 0.4.9.15，Thunderbird 的 OpenPGP 支持也修复了。

## 导读观点 {#perspective}

Tor Browser 建立在 Firefox ESR 上，每年换一次基础版本，等于一次接收 Firefox 一年份的变更。从 16.0 的变更日志看，多项新功能先关掉，例如 WebGPU 标明审查完成前停用。Firefox 新的在线搜索建议也维持关闭。本文据此推论，Firefox 用户已经有的部分功能，Tor Browser 的用户会比较晚用到或用不到。

通用窗口标题处理的是同一台电脑上的其他程序。Tor 网络保护的是连接经过的路径，电脑上安装的其他软件不在范围内。选项只换掉窗口标题，其他程序读取屏幕内容不在它处理的范围内（本文的推论）。

所有窗口都叫“Tor Browser”之后，本文推论依赖窗口名称切换窗口的人会比较难分辨，公告提到的屏幕阅读器用户可能就是这种情况。Tor Project 在公告里邀请使用屏幕阅读器或高度自定义系统的人试用，反馈遇到的问题。

同一个选项已经通过 Tor Uplift Project（把 Tor Browser 的修改送回 Firefox 的计划）进到 Firefox。依公告，熟悉高级设置的 Firefox 用户可以在 `about:config` 把 `privacy.exposeContentTitleInWindow`（一般窗口）与 `privacy.exposeContentTitleInWindow.pbm`（隐私浏览窗口）设为 false，效果相同。

同一篇公告也预告新的线路显示（circuit display，显示连接经过哪几个中继节点的面板）即将进入 Alpha 测试版，不在 16.0 里。新版会把网站信息整合进面板，也能画出多路径线路，Android 版第一次会有线路显示。依公告，多路径线路用额外的中继节点把流量分成两条路径，在同一个出口节点（连接离开 Tor 网络、连到目的网站前的最后一个中继节点）汇合。到公告发布时，一般网站的连接已经会依网络的可用状况随机分配到多路径线路，洋葱服务（只能通过 Tor 连上的网站）还没有。

在中国境内取得 Tor Browser 与连上 Tor，Tor Project 的支持页有专门写给中国的一节。取得更新版 Tor Browser 先试 Telegram 机器人 @gettor_bot，不行再寄信到 gettor@torproject.org，主题依操作系统写 windows、macos、linux 或 android。第三方量测网站 GreatFire 的结果是，`www.torproject.org` 最近 3 次有结论的测试全部被封锁（最后一次 2026 年 10 月 16 日）。`support.torproject.org` 最后一次测试在 2026 年 5 月 7 日，结果同样是封锁，之后没有再测（两项都查证于 11 月 2 日）。

支持页写到 Tor 被封锁时，Connection Assist 会自动尝试网桥或 Snowflake。不行就改用中国可用的网桥，首选 WebTunnel（从 Telegram 的 @GetBridgesBot 或 bridges 网站取得），其次是 Snowflake 与 meek（meek 有带宽限制，速度会相当慢）。16.0 的变更日志列了“Update Bridge settings when connection failed”与 Android 版“Add frequent regions to tor connection assist”两个条目，只有标题，没有写适用哪些地区。法规方面，《计算机信息网络国际联网管理暂行规定》第六条要求直接国际联网使用国家公用电信网提供的国际出入口信道，“任何单位和个人”都不得自行建立或使用其他信道（条文没有出现 Tor 或网桥的字样，查到的官方资料也没有说明是否适用于使用 Tor）。

用 Tor Browser 桌面版的人更新到 16.0 之后，可以在设置的 Privacy and security 找到通用窗口标题（选项名称照英文公告）。依公告，开启后其他软件无法从窗口标题得知浏览记录。本文据此推论，担心电脑上装了来源不明软件的人可以考虑开启，但其他程序记录按键或截图时仍然保护不到。需要更完整地防范电脑上其他软件的人，Tor Project 在公告里推荐的是 Tails。

想照公告改用 Tails 的人，Tails 的已知问题页到 11 月 2 日仍写着，使用 Apple 芯片（M1、M2 等）的 Mac 与许多其他机型的 Mac 完全无法启动 Tails。Tails 7.0 或更新的版本可以自动升级到 7.16，自动升级失败或升级后无法启动时改用手动升级。改成重新安装的话，U 盘上的持久存储（Persistent Storage，Tails 用来保存文件与设置的空间）会消失。还在用 32 位 x86 Linux 的人，依公告多数可以改装 64 位版本，硬件或 Linux 版本太旧的除外。
