---
title: Android 的自动电话号码验证与多账号关联
description: Android 手机默认会自动验证电话号码，并把号码添加到这部手机登录的每一个 Google 账号，包括工作账号与次要账号。可以在设置里关闭验证，依 Android Authority 的报道，已添加的号码仍要到各个账号逐一移除。到 10 月 18 日为止，没有看到 Google 的公开回应。
date: 2026-10-20T00:00:00+08:00
slug: android-phone-number-verification
categories:
  - tracking
sources:
  - title: 在裝置上管理電話號碼驗證
    url: https://support.google.com/android/answer/7521240?hl=zh-Hant
    publisher: Android 說明
  - title: 管理设备上的电话号码验证
    url: https://support.google.com/android/answer/7521240?hl=zh-Hans
    publisher: Android 帮助
  - title: "PSA: Google is silently linking your phone number across all signed-in accounts"
    url: https://www.androidauthority.com/google-auto-phone-number-verification-android-3723117/
    publisher: Android Authority
    date: 2026-10-14
  - title: 變更帳戶中的電話號碼與其用途
    url: https://support.google.com/accounts/answer/3463280?hl=zh-Hant
    publisher: Google 帳戶說明
  - title: 更改账号绑定的电话号码及其用途
    url: https://support.google.com/accounts/answer/3463280?hl=zh-Hans
    publisher: Google 帐号帮助
  - title: 瞭解 Google Play 服務運用簡訊和多媒體訊息的方式
    url: https://support.google.com/android/answer/10641045?hl=zh-Hant
    publisher: Android 說明
  - title: 了解 Google Play 服务会如何使用您的短信和彩信
    url: https://support.google.com/android/answer/10641045?hl=zh-Hans
    publisher: Android 帮助
  - title: 瞭解 Google Play 服務運用通話記錄的方式
    url: https://support.google.com/android/answer/10635223?hl=zh-Hant
    publisher: Android 說明
  - title: 了解 Google Play 服务如何使用您的通话记录
    url: https://support.google.com/android/answer/10635223?hl=zh-Hans
    publisher: Android 帮助
  - title: Google 隱私權政策
    url: https://policies.google.com/privacy?hl=zh-TW
    publisher: Google
    date: 2026-10-16
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
authors:
  - anoni-net
---

Android Authority 10 月 14 日报道，Android 手机会自动验证电话号码，并把号码添加到这部手机登录的每一个 Google 账号（包括工作账号与次要账号）。Google 的 Android 帮助页「管理设备上的电话号码验证」提到，这项功能默认开启，适用于当前与日后登录的账号与号码。依报道，帮助页在 2025 年 8 月到 10 月之间加入默认开启的写法，本文查不到帮助页的旧版可以对照。报道已向 Google 询问，到 10 月 18 日为止没有看到 Google 的公开回应。

只要在 Android 手机登录 Google 账号，号码都会添加到账号。同一部手机登录多个账号的人，账号之间也会因此用同一个号码关联在一起。依同一份帮助页，验证是为了让用电话号码登录、账号恢复、紧急定位、查找丢失的设备、RCS（新一代的短信格式）消息与快速分享（Quick Share）等功能正常运作。Google 与运营商会定期重新验证，运营商可能收取费用。

另外两份 Google Play 服务的帮助页提到，Google Play 服务可能在后台发送及获取短信、获取通话记录，用来发现并验证号码。两页的英文版写 `If you opt-in to phone number verification`（用户主动选择加入），正体中文版译成「如果您啟用電話號碼驗證功能」，简体中文版是「如果您选择启用电话号码验证设置」。英文版的写法跟默认开启的说法不一致，页面没有说明差别。

号码添加到账号之后的用途，Google 账号帮助页「更改账号绑定的电话号码及其用途」列出三类。第一类是登录与账号恢复，第二类是让别人通过 Google 服务找到并联系你，第三类是在「更贴合您需求的广告和 Google 服务」开启时用来展示更相关的广告。10 月 16 日生效的 Google 隐私权政策列了相同的用途，账号帮助页也提到 Google 不会出售包括电话号码在内的个人信息。

设备的帮助页也提到，电话号码验证开启时会一并开启「改善 Google 上的分享体验」，方便别人通过这个号码发送照片与发起视频通话。同一部手机有多个账号时，这项设置只对其中一个账号开启。

## 导读观点 {#perspective}

同一部手机登录的多个账号，常见的是私人账号与工作账号，或刻意跟真实身份分开使用的账号。依帮助页的示例，新增的 Google 账号会关联设备上所有的号码，新添加的号码也会加到所有账号。各地的手机号码实名规定不同。依本文的推论，号码添加到账号之后，能同时取得 Google 账号数据与运营商登记信息的一方（例如依法查询的机关）就能把账号对应到号码登记的身份。

依 Google 帮助页，账号恢复、用电话号码登录、紧急定位等功能依赖验证，关闭之后这些功能可能受影响（本文依帮助页的推论）。Google 隐私权政策把运营商名称与电话号码列在收集的移动网络信息里。依这份清单，本文推论关闭验证、移除号码后，Google 仍可能取得这部手机的号码。Google 内部会不会因此把账号关联起来，本文查不到。

在中国大陆，第三方测量项目 GreatFire 到 10 月 11 日的最后一次测试显示 `play.google.com` 被完全封锁，2012 年 3 月 10 日起就有干扰记录。GreatFire 只测网址能否连上，没有测手机上的 Google Play 服务能否运作。中国大陆销售的 Android 手机有没有内置 Google Play 服务，本文查不到 Google 的官方说明。依帮助页，号码的查找与验证可能由 Google Play 服务执行（没有 Google Play 服务的设备是否受影响，帮助页没有写）。

在同一部 Android 手机登录多个账号、不想让账号之间用号码关联在一起的人，可以到「设置」的「Google」、「所有服务」，在「隐私与安全」下方的「手机号码验证」关闭。报道提到，关闭只会停止之后的关联，已添加的号码要到每个账号的「个人信息」、「电话」逐一删除（Google 的帮助页没有写关闭后是否会移除）。需要用这个号码恢复的那个账号可以保留，只从不想关联在一起的账号移除（本文的推论）。设备设置与 Google 账号这两份帮助页都有简体中文版与正体中文版，页尾标注可能含有 AI 翻译的内容。

报道引述 Reddit 上的用户反馈，提到关闭后开关会自己恢复，报道作者到发布时没有重现。依这些反馈，本文建议关闭之后隔一段时间再回头确认。
