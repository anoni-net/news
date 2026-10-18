---
title: Tuta 加密邮件与 Nextcloud 的集成
description: Tuta 与 Nextcloud 10 月 1 日推出集成，可以在 Nextcloud 里使用 Tuta，把收到的附件存进 Nextcloud、在 Tuta 日历创建 Nextcloud Talk 会议链接。App 要由 Nextcloud 管理员安装，到 10 月 18 日为止，两家的公告都没有交代附件存进 Nextcloud 之后的加密状态。
date: 2026-10-18T13:59:00+08:00
slug: tuta-nextcloud-integration
categories:
  - encryption
sources:
  - title: The Tuta app has landed in the Nextcloud App Store!
    url: https://tuta.com/blog/tuta-app-on-nextcloud
    publisher: Tuta
    date: 2026-10-01
  - title: Tuta brings end-to-end encrypted email service to Nextcloud
    url: https://nextcloud.com/blog/press_releases/tuta-brings-end-to-end-encrypted-email-service-to-nextcloud/
    publisher: Nextcloud
    date: 2026-10-01
  - title: Tuta brings encrypted email to Nextcloud with new free integration
    url: https://cyberinsider.com/tuta-brings-encrypted-email-to-nextcloud-with-new-free-integration/
    publisher: CyberInsider
    date: 2026-10-01
  - title: Tuta Mail
    url: https://apps.nextcloud.com/apps/tutamail
    publisher: Nextcloud
  - title: tutao/tutanota
    url: https://github.com/tutao/tutanota
    publisher: GitHub
  - title: Tuta Mail
    url: https://github.com/tutao/tutanota/blob/master/integrations/nextcloud/tutamail/README.md
    publisher: GitHub
  - title: Encryption
    url: https://tuta.com/encryption
    publisher: Tuta
  - title: Create a secure email account with Tuta Mail
    url: https://tuta.com/pricing
    publisher: Tuta
  - title: Server-side Encryption
    url: https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/encryption_configuration.html
    publisher: Nextcloud
  - title: Constants
    url: https://nextcloud-talk.readthedocs.io/en/latest/constants/
    publisher: Nextcloud
  - title: Conversations management
    url: https://nextcloud-talk.readthedocs.io/en/latest/conversation/
    publisher: Nextcloud
  - title: Nextcloud Talk
    url: https://nextcloud.com/talk/
    publisher: Nextcloud
  - title: Is https://tuta.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/tuta.com
    publisher: GreatFire
  - title: Is https://app.tuta.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/app.tuta.com
    publisher: GreatFire
  - title: Is https://nextcloud.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/nextcloud.com
    publisher: GreatFire
authors:
  - anoni-net
---

加密邮件服务 Tuta 与开源协作平台 Nextcloud 10 月 1 日推出集成，Tuta 的公告把它定位为免费。集成分成两部分，一是 Nextcloud App Store 里的 Tuta Mail App，装好之后可以在 Nextcloud 里使用 Tuta 的网页版。二是 Tuta 里的 Nextcloud 插件，可以把收到的附件一键存进 Nextcloud，或在创建 Tuta 日历活动时生成 Nextcloud Talk 的会议链接。两项功能都要自己的 Nextcloud 装了 Tuta Mail App 才能用（App Store 网页列出 Nextcloud 33 到 35 版），自建的由管理员安装，托管的要由服务提供商开放。

依 Tuta 的公告，插件由 Tuta 账号的管理员在设置的「Plugins」页为所有用户启用，单人账号就是自己账号的管理员。Tuta 在 GitHub 的说明文件列出两个设置字段，Nextcloud 的网址与存放附件的文件夹名称。两项功能在 Nextcloud 里、网页、桌面与手机版的 Tuta 都能使用。依 Nextcloud 的新闻稿，这项集成让个人与小型企业更容易自建 Nextcloud，邮件交给 Tuta 处理。

到 10 月 18 日为止，Tuta 的公告与定价页都没有提到需要哪个方案。Tuta 的 App 有简体与正体中文界面。从 10 月 18 日 Tuta 公开的源代码来看，简体中文语言文件没有「插件」页的字符串，Nextcloud 插件自己的设置字段与「Save to Nextcloud」这类按钮只有英文与德文。

## 导读观点 {#perspective}

Tuta 的加密页提到，邮件连同主题与所有附件都端到端加密，密钥不会交给包括 Tuta 在内的任何人。附件存进 Nextcloud 之后的加密状态，两家的公告都没有说明，本文读了 10 月 18 日 Tuta 公开的源代码。保存按钮在保存附件的对话框里，插件用 Nextcloud 的文件访问接口（WebDAV）上传，上传前没有另外加密。依此推论，上传的是解密后的文件，存进 Nextcloud 时已经离开 Tuta 的端到端加密。

Nextcloud 的管理手册区分两种加密。服务器端加密由服务器执行、密钥也在服务器上，手册提醒它挡不住被入侵的服务器或恶意的管理员。端到端加密则由 Nextcloud 的桌面或手机客户端在上传前执行。插件不经过 Nextcloud 的客户端上传，附件在 Nextcloud 上受到多少保护，取决于那台服务器的设置与管理者（本文依手册与源代码的推论）。

插件生成的 Talk 会议，依源代码创建的是公开房间，Talk 的 API 文档把公开房间列为允许访客加入的对话。Nextcloud 的产品页提到 Talk 支持端到端加密通话，范围是网页与新的桌面客户端，但没有说明公开房间是否适用。

在中国大陆，第三方测量项目 GreatFire 把 `tuta.com` 判定为间歇性受到干扰，到 10 月 11 日最近 17 次有结论的测试中有 59% 受到干扰。Tuta 网页版的主机 `app.tuta.com` 与 `nextcloud.com` 在最近的测试中都受到干扰，但有结论的测试只有 1 到 2 次，样本很少。

已经使用 Nextcloud、又用 Tuta 收信的人或团队，先由 Nextcloud 管理员安装 Tuta Mail App，再由 Tuta 账号的管理员启用插件。依管理手册，服务器端加密挡不住服务器的管理者。处理敏感附件前，可以先确认有哪些人具备那台服务器的管理权限。依源代码与 Talk 的文档，插件创建的是允许访客的公开房间，取得链接的人可以用访客身份加入。
