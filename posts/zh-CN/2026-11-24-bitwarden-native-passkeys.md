---
title: Bitwarden 桌面版与 Windows 11、macOS 的通行密钥集成
description: 与已经在 Windows 11 或 macOS 上使用 Bitwarden 的人有关。Bitwarden 11 月 18 日公告桌面版可以设成系统的通行密钥提供者，电脑上创建的通行密钥可以存进 Bitwarden 密码库、跟着账号同步。Windows 11 要用 Microsoft Store 安装的版本，依 Privacy Guides 的新闻简讯，Linux 用户这次无法使用。
date: 2026-11-24T00:00:00+08:00
slug: bitwarden-native-passkeys
categories:
  - security
related:
  - title: 什么是 passkey
    url: https://anoni.net/docs/zh-cn/tools/what-is-passkey/
  - title: 密码管理器入门
    url: https://anoni.net/docs/zh-cn/tools/password-manager/
sources:
  - title: Integrate Bitwarden with Windows and macOS for native passkey creation and use
    url: https://bitwarden.com/blog/integrate-bitwarden-native-passkeys/
    publisher: Bitwarden
    date: 2026-11-18
  - title: Bitwarden Adds Native Passkey Support for Windows and macOS
    url: https://www.privacyguides.org/news/2026/11/19/bitwarden-adds-native-passkey-support-for-windows-and-macos/
    publisher: Privacy Guides
    date: 2026-11-19
  - title: Autofill Passkeys
    url: https://bitwarden.com/help/storing-passkeys/
    publisher: Bitwarden
  - title: Bitwarden launches passkey management
    url: https://bitwarden.com/blog/bitwarden-launches-passkey-management/
    publisher: Bitwarden
  - title: Windows 11 expands passkey manager support
    url: https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-11-expands-passkey-manager-support/4467572
    publisher: Microsoft
    date: 2025-11-11
  - title: Passkeys
    url: https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/
    publisher: Microsoft
  - title: Export Vault Data
    url: https://bitwarden.com/help/export-your-data/
    publisher: Bitwarden
  - title: Download Credential Exchange Specifications
    url: https://fidoalliance.org/specifications/download-credential-exchange-specifications/
    publisher: FIDO Alliance
  - title: Server Regions
    url: https://bitwarden.com/help/server-geographies/
    publisher: Bitwarden
  - title: "Is https://bitwarden.com blocked in mainland China? — GreatFire"
    url: https://en.greatfire.org/https/bitwarden.com
    publisher: GreatFire
  - title: "Is https://vault.bitwarden.com blocked in mainland China? — GreatFire"
    url: https://en.greatfire.org/https/vault.bitwarden.com
    publisher: GreatFire
authors:
  - anoni-net
---

Bitwarden 11 月 18 日公告，桌面版可以设成 Windows 11 与 macOS 的通行密钥提供者（电脑上负责保存通行密钥、登录时交出来使用的程序）。通行密钥（passkey）用设备的屏幕锁定取代密码登录，网站只存公开密钥，登录用的私钥存在设备或密码管理器里。桌面版设成提供者之后，网站或桌面应用程序创建通行密钥时弹出的系统窗口会列出 Bitwarden 作为存放位置。Windows 11 要用从 Microsoft Store 安装的版本，Privacy Guides 的新闻简讯则提到 Linux 用户这次无法使用。

Bitwarden 从 2024 年初开始在浏览器扩展与手机 App 保管通行密钥。依 Privacy Guides 11 月 19 日的新闻简讯，扩展适用网站，登录桌面应用程序时可能要改用手机或硬件安全密钥。在电脑上创建的通行密钥，也可能被存进 Windows 或 macOS 默认的凭据管理工具，没有进到 Bitwarden。

通过系统窗口创建的通行密钥会成为密码库里的一条登录项目，任何一个 Bitwarden App 都能管理。密码库里已经有用户名相同的登录项目时，通行密钥会自动加到这条项目。项目里原本就存了通行密钥时，会先弹出覆盖的警告。

## 导读观点 {#perspective}

已经在 Windows 11 或 macOS 上使用 Bitwarden 的人才与这次的集成有关，没有用 Bitwarden 的人不受影响。设置之后，电脑上创建的通行密钥可以存进 Bitwarden 并跟着账号同步到其他设备，不必留在系统默认的工具里。从公告描述的同步方式来看，私钥跟着 Bitwarden 账号走，账号的保护与恢复因此也牵动这些通行密钥。之后要再搬到其他密码管理器时，直接转移用的协议还在草案阶段。

创建与登录时的窗口由 Windows 11 与 macOS 提供，私钥则存在 Bitwarden 密码库。依 Microsoft 的说明，Windows 11 搭配第三方提供者时，通行密钥由该提供者保护与管理。

要搬走或备份时，导出成文件只有 `.json` 格式包含通行密钥，Bitwarden 在导出页建议选加密的格式。密码保护（Password protected）的加密导出才能导入其他 Bitwarden 账号，限定原账号的只能导回同一个账号。Bitwarden 2024.3.1 版以前创建的通行密钥带有每次使用都会增加的计数器，导出页写了这类导出文件不适合当长期备份。

桌面版能不能直接转移到其他密码管理器，导出页没有写，列出的直接转移只有手机的做法（各家的支持范围见本站 10 月 19 日的[通行密钥证明机制导读](https://anoni.net/news/zh-cn/2026/10/passkey-attestation-debate/)）。直接转移用的是 FIDO 联盟的凭据交换协议（CXP），到 11 月 21 日，FIDO 联盟页面列出的 CXP 是 2024 年 10 月的工作草案。

Bitwarden 官方的云服务器只有美国与欧盟两个区域，没有中国大陆、台湾或香港的区域，账号只存在创建时选的区域。第三方测量项目 GreatFire 对 `vault.bitwarden.com` 最近一次的测试在 11 月 15 日，最近 5 次有结论的测试在中国大陆都正常连接。官网 `bitwarden.com` 最近一次的测试在 10 月 26 日，最近 4 次有结论的测试中有 1 次受到干扰。GreatFire 的测试只针对网址能否连接，不等于 App 能同步。

想让创建的通行密钥存进 Bitwarden 密码库的人，在 Windows 11 上要用 Microsoft Store 版的桌面版，Bitwarden 2025 年 11 月的测试版则是从 GitHub 安装。Microsoft 表示这项能力随 2025 年 11 月的安全更新提供。之后在桌面版设置的 Passkey provider 一项选 Manage in system settings，再照系统弹出的窗口启用 Bitwarden，macOS 弹出的是询问是否使用 Bitwarden 自动填充的窗口。Bitwarden 在说明页建议同时关闭浏览器扩展的通行密钥功能，以免两边冲突。

登录 Bitwarden 账号本身用的通行密钥不会存进密码库。既然密码库不收这把密钥，用通行密钥登录 Bitwarden 的人就要另外保存它。Linux 用户与不想换安装来源的 Windows 11 用户，仍可以用浏览器扩展在网站上保管与使用通行密钥，登录桌面应用程序则不在范围内。
