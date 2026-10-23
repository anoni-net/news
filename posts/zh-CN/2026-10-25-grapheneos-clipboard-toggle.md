---
title: GrapheneOS 的剪贴板读取开关
description: 官方只支持 Pixel 的隐私强化手机系统 GrapheneOS，9 月 18 日公告的版本加入 Secure Paste，可以逐一设置哪些 App 不能读取其他 App 复制的内容。到 10 月 23 日功能默认没有开启，要自己到设置里调整，GrapheneOS 自己新增的设置也只有英文。一般 Android 手机在 App 读取剪贴板之后才通知，iPhone 则在 App 用程序读取前请用户同意。复制密码之后让密码管理器自动清除剪贴板，是两边都能做的一步。
date: 2026-10-25T00:05:00+08:00
slug: grapheneos-clipboard-toggle
categories:
  - mobile
sources:
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases#2026091700
    publisher: GrapheneOS
  - title: GrapheneOS version 2026091700 released
    url: https://discuss.grapheneos.org/d/42090-grapheneos-version-2026091700-released
    publisher: GrapheneOS Discussion Forum
    date: 2026-09-18
  - title: Features overview | GrapheneOS
    url: https://grapheneos.org/features#secure-paste
    publisher: GrapheneOS
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#supported-devices
    publisher: GrapheneOS
  - title: Web installer | Install | GrapheneOS
    url: https://grapheneos.org/install/web
    publisher: GrapheneOS
  - title: "GrapheneOS: \"It's an opt-in feature wit…\" - GrapheneOS Mastodon"
    url: https://grapheneos.social/@GrapheneOS/117292361749585692
    publisher: GrapheneOS
    date: 2026-09-18
  - title: platform_packages_apps_Settings/res/values/strings_ext.xml
    url: https://github.com/GrapheneOS/platform_packages_apps_Settings/blob/2026102100/res/values/strings_ext.xml
    publisher: GitHub
  - title: platform_frameworks_base/core/res/res/values/config_ext.xml
    url: https://github.com/GrapheneOS/platform_frameworks_base/blob/2026102100/core/res/res/values/config_ext.xml
    publisher: GitHub
  - title: GrapheneOS translate to other languages - GrapheneOS Discussion Forum
    url: https://discuss.grapheneos.org/d/5030-grapheneos-translate-to-other-languages
    publisher: GrapheneOS Discussion Forum
  - title: Privacy changes in Android 10
    url: https://developer.android.com/about/versions/10/privacy/changes
    publisher: Android Developers
  - title: "Behavior changes: all apps"
    url: https://developer.android.com/about/versions/12/behavior-changes-all
    publisher: Android Developers
  - title: Features and APIs Overview
    url: https://developer.android.com/about/versions/13/features
    publisher: Android Developers
  - title: UIPasteControl
    url: https://developer.apple.com/documentation/uikit/uipastecontrol
    publisher: Apple Developer Documentation
  - title: iOS 16.1 Introduces New Copy-and-Paste Permission Settings on Per-App Basis
    url: https://www.macrumors.com/2022/10/17/ios-16-1-paste-from-other-apps-settings/
    publisher: MacRumors
    date: 2022-10-17
  - title: Protecting Android clipboard content from unintended exposure
    url: https://www.microsoft.com/en-us/security/blog/2023/03/06/protecting-android-clipboard-content-from-unintended-exposure/
    publisher: Microsoft Security Blog
    date: 2023-03-06
  - title: Copy and fill passwords into apps that don't work with 1Password
    url: https://support.1password.com/copy-passwords/
    publisher: 1Password Support
    date: 2026-08-17
  - title: platform_packages_apps_Settings/res at 2026102100 · GrapheneOS/platform_packages_apps_Settings · GitHub
    url: https://github.com/GrapheneOS/platform_packages_apps_Settings/tree/2026102100/res
    publisher: GitHub
  - title: Learn about devices & services available in your region - Google Store Help
    url: https://support.google.com/store/answer/2462844?hl=en
    publisher: Google
  - title: Is https://releases.grapheneos.org blocked in mainland China?
    url: https://en.greatfire.org/https/releases.grapheneos.org
    publisher: GreatFire
authors:
  - anoni-net
---

GrapheneOS 是以 Android 开源代码为基础的隐私强化手机系统，到 10 月 23 日官方支持的机型是 Pixel 6 到 Pixel 10a。9 月 18 日官方论坛公告的 2026091700 版，加入名为 Secure Paste 的剪贴板控制。依发布记录，用户可以逐一关闭 App 读取剪贴板的权限，也可以用全局开关把所有第三方 App 默认设为关闭。关闭之后，用户仍可以通过系统的选择工具栏、键盘、键盘快捷键或无障碍服务，把内容粘贴进这些 App。

依 GrapheneOS 的功能介绍页，Android 只允许当前获得焦点、正在操作的 App 与键盘读取剪贴板。App 读到其他 App 复制的内容时 Android 会显示通知，但通知出现时内容已经被读走了。开启 Secure Paste 之后，App 读不到其他 App 复制的内容，仍可读取自己复制的内容。

Secure Paste 默认不阻止读取，GrapheneOS 在 Mastodon 的回复说明这是要自己开启的功能，设置代码的默认值也是允许读取。依设置代码，开关在「Settings > Security & privacy > Privacy controls > Clipboard access」，官方的使用说明没有写路径。全局默认的选项是「Allow」与「Blocked」，每个 App 另外可以选「Allow」、「Paste only」，或用「Follow system clipboard access setting」跟随全局默认。设置代码的说明文字也提醒，改成 Paste only 可能让某些 App 无法正常运行。

之后的 2026091900 版把拦下读取时的通知间隔从 1 分钟缩短为 6 秒，这则通知可以逐个 App 关闭。2026092500 版改善了设置界面，到 10 月 21 日的 2026102100 版，发布记录没有再列出剪贴板相关的条目。

依设置代码的说明文字，全局开关不适用于系统 App。当前使用的键盘以及部分 App 与系统功能，一律可以读取剪贴板。

App 仍可看到剪贴板有没有内容、内容类型与复制时间，能查看并操作屏幕内容的无障碍服务也可以触发粘贴，并可能取得粘贴的内容。依功能介绍页，设成 Paste only 之后，要粘贴到自行实现选择工具栏的 App（例如用 Flutter 这套跨平台开发框架写的 App）需改用键盘上的粘贴按钮。依官方论坛的回复，GrapheneOS 在默认键盘加了这个按钮，Gboard 原本就有。使用其他键盘的人要先确认有没有粘贴功能。

## 导读观点 {#perspective}

依 Microsoft 2023 年的安全博客，手机用户常用剪贴板复制密码、支付信息这类敏感内容。Android 的 App 读写剪贴板不需要用户同意，也不需要特定权限。

Microsoft 在同一篇文章公布调查结果，一款购物 App 的旧版本会定期读取剪贴板，内容符合特定格式就传回服务器。文中也提到并未得知特定的恶意意图，该行为在 2022 年 5 月已移除。Android 10 起后台 App 不能读剪贴板，但这项限制挡不住前台的 App。

依 Android 开发者文档，Android 12 起 App 第一次读取其他 App 复制的内容时，系统会显示通知。Android 13 另外在复制时显示预览，用来确认复制成功。依 Apple 的开发者文档，iOS 16 起 App 用程序读取剪贴板时，系统会先请用户同意。MacRumors 2022 年的报道提到，iOS 16.1 起请求过粘贴的 App 在设置里多了「Paste from Other Apps」选项，本文没有在现行 iOS 核对。

本文建议用 GrapheneOS 的读者先挑几个 App 改成 Paste only，再视情况把全局默认改成 Blocked，粘贴时改用工具栏或键盘（先确认自己的键盘有粘贴键）。设置代码的提醒与官方列出的限制都显示，一次全部拦下比较容易遇到无法正常运行的 App。改了之后某个 App 无法正常运行，可以把那个 App 改回 Allow。

依 GrapheneOS 的功能介绍页，Secure Paste 取代了桌面与手机系统的标准做法，一般 Android 手机没有逐个 App 的开关。iPhone 则是 App 用程序读取时会先询问，两边都可以先调整密码管理器，1Password 的帮助页写各平台复制出去的密码默认 90 秒后自动清除。本文建议用其他密码管理器的人，在设置里找清除剪贴板的选项。定时清除只缩短内容留在剪贴板的时间，清除之前获得焦点的 App 仍可读取。

想安装 GrapheneOS 的人要先有一部支持的 Pixel，官方 FAQ 提醒运营商锁定的机型无法安装，主要发生在美国的运营商。依官方网页安装器的说明，运行安装器的设备要有至少 2GB 可用内存与 32GB 可用存储空间，电脑或 Android 手机、平板都可以。依 10 月 23 日查到的设置代码目录推断，GrapheneOS 自己新增的设置与 App 只有英文，系统其他部分沿用 Android 的简体中文。

依 Google Store 的帮助页，GrapheneOS 支持的 Pixel 10a 在 Google Store 可以购买的亚洲地区是印度、日本、新加坡与台湾，到 10 月 23 日清单里没有中国大陆、香港与澳门。该页只涵盖 Google Store 本身，不包括其他零售渠道与运营商。

依 GrapheneOS 的 FAQ，系统更新程序从 `releases.grapheneos.org` 获取更新信息并下载更新文件。依专门监测中国网络审查的 GreatFire 的测量，10 月 2 日最后一次测试记录到这个地址在中国大陆受到干扰。到 10 月 23 日查询时，此前 90 天内只有这 1 次有结果的测试。依本文的推论，在中国大陆直接连接时，系统更新可能无法顺利下载。

已经在用 GrapheneOS 的人改成 Paste only 之后，拦下的是 App 自行读取，挡不到已开启的无障碍服务与当前使用的键盘。代价是部分 App 要改用键盘的粘贴键。
