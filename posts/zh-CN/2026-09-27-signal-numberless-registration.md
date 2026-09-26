---
title: Signal 免手机号注册的 Android 测试版
description: Signal 的 Android 测试版可以不用手机号注册，付一次费用换一个不绑定号码的账号，代价是账号丢失后没有任何恢复渠道。
date:
  created: 2026-09-27
  updated: 2026-09-28
slug: signal-numberless-registration
pin: true
sources:
  - title: Beta feedback for the upcoming Android 8.28 release
    url: https://community.signalusers.org/t/beta-feedback-for-the-upcoming-android-8-28-release/76457
    publisher: Signal Community
    date: 2026-09-16
  - title: Signal tests account registration without phone number on Android
    url: https://cyberinsider.com/signal-tests-account-registration-without-phone-number-on-android/
    publisher: CyberInsider
    date: 2026-09-18
  - title: "Signal Will Let You Sign Up Without a Phone Number — For $3"
    url: https://itsfoss.com/news/signal-numberless-registration/
    publisher: It's FOSS
    date: 2026-09-22
  - title: Signal introduces registration without a phone number
    url: https://freedom.press/digisec/blog/signal-introduces-registration-without-a-phone-number/
    publisher: Freedom of the Press Foundation
    date: 2026-09-23
  - title: I don't like passkeys
    url: https://hawksley.dev/blog/i-dont-like-passkeys
    date: 2026-09-18
  - title: 电话用户真实身份信息登记规定
    url: https://www.gov.cn/gongbao/content/2013/content_2473882.htm
    publisher: 中华人民共和国工业和信息化部
    date: 2013-07-16
  - title: How countries attempt to block Signal Private Messenger App around the world
    url: https://ooni.org/post/2021-how-signal-private-messenger-blocked-around-the-world/
    publisher: OONI
    date: 2021-10-21
authors:
  - anoni-net
---

Signal 在 Android 8.28 测试版加入不用手机号的注册方式。目前只有 Android 测试版可以使用，iPhone 版还在开发，已经用手机号注册的账号也还不能移除号码。

注册时选择不使用手机号，要通过 Play 商店的应用内购买支付一次 3 美元的费用，各国价格可能不同。没有安装 Google Play 服务的设备，暂时无法用这个方式注册。

Signal 在社区论坛的公告写明，付款使用跟捐款系统相同的零知识证明，付款记录与账号之间没有关联。收费的原因也写在公告里，免费的话，发送垃圾信息的人可以大量申请账号。

注册完成后会得到一组 Account Id 与 Account Key，作用相当于账号与密码。账号没有 PIN，也没有其他恢复渠道，其中任一项丢失，账号就无法找回。

用户名可以另外设置，没有设置的话，别人无法搜索到这个账号，只能参与自己发起的对话。注册后可以在设置里加上两步验证，目前支持 TOTP 验证器，passkey 与硬件密钥会在之后加入。

## 导读观点 {#perspective}

在中国大陆，每个电话号码都要实名登记。工业和信息化部 2013 年施行的《电话用户真实身份信息登记规定》要求电信业者为用户办理入网手续时，查验有效证件、登记真实身份信息。用手机号注册的通讯账号，因此能通过电信业者连回真实身份。改成付费加上零知识证明之后，账号跟手机号、付款都脱钩。Signal 的 Android 版以 AGPL-3.0 授权公开源代码，界面有简体中文。

身在中国境内的人还有另一道门槛。OONI 在 2021 年 4 月到 9 月的量测显示 Signal 在中国遭到封锁，要先有翻墙工具才能连上。免手机号注册目前又只能通过 Google Play 付款，比较适合身在海外、手机装有 Google Play 服务的人。

没有手机号之后，别人只能通过用户名找到这个账号。Freedom of the Press Foundation 提醒，公开分享过的用户名要一直保留，否则别人可以取得同一个名称来冒充。用用户名接受消息来源联系的人，被冒充的后果更严重。

另一篇讨论 passkey 的观点文章认为，一个账号的安全程度取决于最弱的那一种恢复方式。Signal 的免手机号账号没有任何恢复方式，攻击者少了一个较弱的入口，丢失的风险则全部落在用户身上。Account Id 与 Account Key 要存进密码管理器并保留离线备份，设置 TOTP 时也要准备不只一个第二因素。
