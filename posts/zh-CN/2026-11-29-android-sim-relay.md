---
title: 转接境外诈骗电话的 Android 手机与来电号码
description: 台湾刑事警察局 11 月 19 日公布一组案件，诈骗团伙用插着台湾本地 SIM 卡的 Android 手机替境外机房拨出诈骗电话。来电显示台湾手机号码不代表对方人在台湾，接到自称机关的电话，可以挂断后改拨官方号码或台湾的 165 反诈骗咨询专线查证。
date: 2026-11-29T00:00:00+08:00
slug: android-sim-relay
categories: [security]
regions:
  - TW
sources:
  - title: 刑事局攜手NCC與三大電信業者公私聯防 全面查緝DMT詐欺話務轉接機房阻斷詐欺犯罪源頭
    url: https://www.cib.npa.gov.tw/ch/app/news/view?module=news&id=1885&serno=eb9d97b0-d3e4-4d7e-a916-4dbe55bde20d
    publisher: 內政部警政署刑事警察局
    date: 2026-11-19
  - title: Android手機變詐騙話務中繼站、泡芙箱藏上百張SIM卡！刑事局揭露詐團電話轉接新手法
    url: https://www.ithome.com.tw/news/180687
    publisher: iThome
    date: 2026-11-20
  - title: 使用詐騙偵測功能
    url: https://support.google.com/phoneapp/answer/15654065?hl=zh-TW
    publisher: Google
  - title: 在接聽電話前先過濾來電
    url: https://support.google.com/phoneapp/answer/9118387?hl=zh-TW
    publisher: Google
  - title: 在 iPhone 上篩選和封鎖通話
    url: https://support.apple.com/zh-tw/guide/iphone/iphe4b3f7823/ios
    publisher: Apple
  - title: 工信部：2025年累计拦截诈骗电话、短信64.8亿次
    url: https://www.bjnews.com.cn/detail/1781269574129787.html
    publisher: 新京报
    date: 2026-06-13
  - title: Insertion of "+" sign in calling number display to help identify possible telephone scams originating from outside Hong Kong
    url: https://www.info.gov.hk/gia/general/201508/20/P201508200536.htm
    publisher: 香港通訊事務管理局辦公室
    date: 2015-08-20
  - title: OFCA and telecommunications industry join hands in launching new measure to combat fraudulent calls
    url: https://www.info.gov.hk/gia/general/202304/11/P2023041100271.htm
    publisher: 香港通訊事務管理局辦公室
    date: 2023-04-11
related:
  - title: 一般人平常该做到什么
    url: https://anoni.net/docs/zh-cn/scenarios/everyday-baseline/
authors:
  - anoni-net
---

用台湾手机号码接电话的人，看到来电显示是台湾本地号码，打电话的人仍可能在境外。台湾刑事警察局 11 月 19 日公布的一组案件里，诈骗团伙用普通的 Android 手机加上 App 与周边配件，组成能双向转接话务的设备。设备插入台湾电信运营商的 SIM 卡之后，境外的诈骗机房就能远程连接拨号，假冒公务机关、医院或电信客服打给民众。警方在 7 到 9 月查扣以手机组成的转接设备等 18 组。

电信运营商全面推动国际电话语音警示（接听境外来电前先播放提醒的语音）之后，境外诈骗团伙为了避开警示，改在台湾架设 DMT（数字移动电话节费设备）。DMT 把经网络传来的境外通话，改从插在设备里的台湾本地 SIM 卡以移动电话拨出。依 iThome 的报道，这样拨出的电话看似一般本地来电，号码前面没有境外来电通常会有的“+”与国家代码。传统 DMT 这类专用设备遭警方大量查处之后，诈骗团伙改用 Android 手机。

诈骗团伙会以居家兼职、代管设备、借贷或假冒检警要求配合办案为名，请民众接收设备、插入本人名下的 SIM 卡，来电显示的号码因此可能是被招募的民众自己的号码。有人要你把 SIM 卡插进对方给的设备或在家代管设备，就是这类招募。答应的人可能被收取高额通话费，也可能涉及刑事责任与民事索赔。依刑事局的提醒，政府机关、警察与检察官不会要求民众办理手机号码、提供 SIM 卡、安装不明 App 或代为架设通信设备。

## 导读观点 {#perspective}

从来电显示的号码只能知道是哪一张 SIM 卡在台湾拨出电话。刑事局把以手机组成的设备也归为 DMT 转接设备，iThome 又写 DMT 拨出的电话显示为本地来电。从这两点推想，Android 手机转接的电话，来电显示的也是那张 SIM 卡的台湾号码。打电话的人是谁、在哪里，从号码都无法判断。

接到自称公务机关、医院或电信客服的电话，可以先挂断，再从官网、账单或卡片背面这类自己可以找到的渠道查号码拨过去。来电显示的号码与对方给的号码都不要回拨。设备能双向转接话务，照这点推想，拨回那个台湾号码的电话可能会被转回境外机房。不确定时也可以拨 165 反诈骗咨询专线（台湾的专线）。

在大陆，用户接听境外电话或收到境外短信时可以收到号码来源于境外的提示，没有国际及港澳台亲友、不从事跨境业务的用户还可以通过另一项服务关闭境外来电与短信的接收。据新京报报道的工信部 6 月 12 日数据，境外来电提醒服务已累计发出 25.23 亿次提示。同一份数据里，截至 2025 年底信息通信行业协助公安机关缴获“插卡集群设备”（俗称“猫池”）21 万个，另打击非法架设“猫池”的犯罪窝点 11.7 万个。

香港的手机来电显示会为所有来自境外的来电加上“+”前缀，即使主叫号码伪装成香港本地号码也一样，这是香港通讯事务管理局办公室 2015 年 8 月宣布的规定。2023 年 5 月 1 日起，香港的流动网络运营商对“+852”来电发出语音或短信警示，提示来电来自香港境外。这项警示免费，不必预先登记。

到 11 月 29 日为止，Google“电话”App 的诈骗检测与接听前过滤来电都还没有在台湾提供，诈骗检测也只限 Pixel。用 Android 手机的人在台湾接到这类电话，仍要靠挂断再查证。

iPhone 在“设置”的“App”→“电话”里，可以把未知号码的来电设为“询问来电原因”或“静音”。选前者时 iPhone 响铃前会先要求来电者说明来意，选后者时来电会设为静音并转接语音信箱。两个选项都依号码是否存在通讯录判断，只能减少陌生来电的打扰，无法识别从台湾本地号码拨出的诈骗电话。很少需要接陌生电话的人可以考虑改用这两个选项，代价是可能漏接医院、物流这类正当的陌生来电。
