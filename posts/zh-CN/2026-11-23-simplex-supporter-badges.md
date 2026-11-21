---
title: SimpleX 支持者徽章的付款与身份
description: SimpleX Chat 销售支持者徽章，购买者可以发送更大的文件。依设计，SimpleX 无法从出示的徽章得知是哪一笔购买，但信用卡付款与同一周到期的分组仍会留下线索。
date: 2026-11-23T00:00:00+08:00
slug: simplex-supporter-badges
categories: [finance]
sources:
  - title: SimpleX Supporter Badges — Send Larger Files That Stay Available Longer, Without Being Identified
    url: https://simplex.chat/blog/20260919-simplex-supporter-badges.html
    publisher: SimpleX Chat
    date: 2026-09-19
  - title: SimpleX Supporter Badges
    url: https://github.com/simplex-chat/simplex-chat/blob/master/docs/protocol/badges-overview.md
    publisher: SimpleX Chat
    date: 2026-10-22
  - title: Supporter badges
    url: https://simplex.chat/docs/guide/supporter-badges.html
    publisher: SimpleX Chat
  - title: Releases · simplex-chat/simplex-chat
    url: https://github.com/simplex-chat/simplex-chat/releases
    publisher: GitHub
  - title: The Privacy Pass Architecture
    url: https://www.rfc-editor.org/rfc/rfc9576.html
    publisher: IETF
  - title: Is https://simplex.chat blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/simplex.chat
    publisher: GreatFire
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
  - title: 中华人民共和国反洗钱法
    url: http://www.npc.gov.cn/npc/c2/c30834/202411/t20241108_440887.html
    publisher: 中国人大网
    date: 2024-11-08
  - title: iTunes Search API
    url: https://itunes.apple.com/lookup?id=1605771084&country=cn
    publisher: Apple
authors:
  - anoni-net
---

SimpleX 的公告写到，其他通信软件的付费功能附在账号上，运营者因此知道是谁付了钱、用这项功能做什么。SimpleX Chat 9 月起销售支持者徽章，购买者发送的文件上限从 1 GB 提高到 2 GB（传奇等级 5 GB），文件在服务器上也保存得更久（支持者 7 天、传奇 21 天）。SimpleX 的网络没有用户账号，徽章改用匿名凭证（anonymous credential）证明持有者付过钱、不透露是谁。到 11 月 21 日，SimpleX Chat App 的 7.1 版已经包含这项功能。

依 SimpleX 的技术白皮书，徽章是一份 BBS 签名（一种还在制定中的数字签名规范），由 SimpleX 运营的徽章服务签发、存在用户自己的设备上。App 每次向联系人或服务器出示徽章时，都用它生成一份新的零知识证明（zero-knowledge proof）。零知识证明的作用像是只证明“年满 18 岁”、不交出整张证件，本站整理[欧盟年龄验证 App](https://anoni.net/news/2026/09/eu-age-verification-blueprint/) 时也写过这项技术。联系人与服务器运营者因此只能获得徽章类型与到期日，无法把两次出示连在一起，也无法连回购买。

SimpleX 的公告写到，凭证每次只签发一个月，所有徽章都在一周里的同一天到期。持有者因此隐身在那一周到期的所有支持者之中。依白皮书，App 每月换新凭证时会把申请新凭证与向联系人显示新徽章排在不同天，让旁人难以从时间认出持有者。

## 导读观点 {#perspective}

互联网标准组织 IETF 制定的 Privacy Pass 是另一种做法，用户通过一次验证获得令牌（token），出示时不必透露身份。依白皮书，这类令牌出示一次就作废，也不带到期日与类型。徽章要在每段对话、每次连接一再出示，SimpleX 因此选用可以重复生成新证明的 BBS 签名。

依白皮书，徽章服务保存每笔购买的付款记录，信用卡付款也像其他服务一样会关联到这笔购买。同一周到期的徽章到期日相同，服务器运营者能把这些支持者的连接归成一组，持有者隐身其中的人数取决于那一周有多少人到期。刚购买或刚用兑换码兑换的徽章会立刻显示，在徽章服务自己的群组里领兑换码的人，SimpleX 可以从新徽章出现的时间推测是谁兑换。Google Play 的订阅换设备时用 Restore purchases（把商店里的订阅移到当前个人资料的功能）搬移，SimpleX 能把前后两笔购买关联起来，但无法关联到持有它们的个人资料。

从 Google Play 安装的 Android 版可以在 App 内付款，有单月方案，以及每月、每年自动续订的方案。iOS 版、从 F-Droid 或 GitHub 安装的版本与桌面版会打开浏览器的购买页，用信用卡、Bitcoin 或 Monero 付款后取得一组兑换码，粘贴进 App 的设置就能换成徽章。白皮书写到，想让付款本身保密的人可以改用加密货币。在网页购买的徽章不会自动续订，到 11 月 21 日也还不能搬到新设备。

提供购买页与官网下载的 simplex.chat，依 GreatFire 11 月 17 日的最近一次测试（样本仅 1 次）在中国大陆 100% 被封锁，Google Play 在 11 月 1 日的测试也是 100% 被封锁。到 11 月 21 日，中国区 App Store 没有 SimpleX Chat 的条目。用中国境内金融机构处理的信用卡付款，如前面所说会连到这笔购买，而《中华人民共和国反洗钱法》第三十四条要求金融机构把交易记录保存至少十年。

徽章只加在一个个人资料上，匿名（incognito）个人资料不显示徽章。徽章无法撤销，设备或备份被入侵时，取得徽章数据的人可以一直用到期满。购买多个月份的，入侵者还能向徽章服务申请剩下月份的新凭证。
