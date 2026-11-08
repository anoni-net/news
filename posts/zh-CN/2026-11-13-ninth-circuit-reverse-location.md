---
title: 美国第九巡回法院审理的基站倾印搜索票
description: 美国第九巡回法院审理一件基站倾印（向电信运营商调取某时某地所有手机数据）的上诉案，EFF 与 ACLU 主张倾印搜索票本身违宪。到 11 月 8 日查不到政府一方在上诉审的书状，依本文推论关闭 Google 定位记录挡不了基站倾印。
date: 2026-11-13T00:05:00+08:00
slug: ninth-circuit-reverse-location
categories:
  - surveillance
regions:
  - US
sources:
  - title: We’re Asking the Ninth Circuit to Hold Reverse Location Warrants Categorically Unconstitutional
    url: https://www.eff.org/deeplinks/2026/11/were-asking-ninth-circuit-hold-reverse-location-warrants-categorically
    publisher: EFF
    date: 2026-11-04
  - title: Brief of Amici Curiae, No. 26-689 (9th Cir.)
    url: https://www.eff.org/files/2026/11/03/united_states_v._spurlock_-_eff_aclu_amicus_brief_1.pdf
    publisher: EFF
    date: 2026-11-03
  - title: Uncle Sam seeks time in tower dump data grab case after judge calls it 'unconstitutional'
    url: https://theregister.com/2025/06/19/us_tower_grab_appeal/
    publisher: The Register
    date: 2025-06-19
  - title: Court rules that law enforcement’s use of “geofence warrant” was a “search”
    url: https://www.scotusblog.com/2026/06/court-rules-that-law-enforcements-use-of-geofence-warrant-was-a-search/
    publisher: SCOTUSblog
    date: 2026-06-29
  - title: Supreme Court Holds Geofence Warrants Are Fourth Amendment Searches, But Leaves Other Important Questions for Lower Courts
    url: https://www.zwillgen.com/law-enforcement/supreme-court-holds-geofence-warrants-are-fourth-amendment-searches-leaves-other-important-questions-lower-courts/
    publisher: ZwillGen
    date: 2026-07-02
  - title: Federal Appeals Court Finds Geofence Warrants Are “Categorically” Unconstitutional
    url: https://www.eff.org/deeplinks/2024/08/federal-appeals-court-finds-geofence-warrants-are-categorically-unconstitutional
    publisher: EFF
    date: 2024-08-12
  - title: Supreme Court grapples with limits to 'geofence warrants' over privacy concerns
    url: https://www.goodmorningamerica.com/amp/news/story/supreme-court-weighs-geofence-warrants-cellphone-data-132358022
    publisher: ABC News
    date: 2026-04-28
  - title: No. 25-112 (U.S. June 29, 2026)
    url: https://www.independent.org/article/2026/06/30/supreme-court-geofence-warrants-chatrie/
    publisher: Independent Institute
    date: 2026-06-30
  - title: Updates to Location History and new controls coming soon to Maps
    url: https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/
    publisher: Google
    date: 2023-12-12
  - title: Manage your Google Maps Timeline
    url: https://support.google.com/maps/answer/6258979?hl=en
    publisher: Google Maps Help
  - title: "Apple Transparency Report: Government and Private Party Requests, July 1 - December 31, 2025"
    url: https://www.apple.com/legal/transparency/pdf/requests-2025-h2-en.pdf
    publisher: Apple
  - title: 通信保障及监察法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060044
    publisher: 全国法规资料库
  - title: 中华人民共和国网络安全法（2025 年修正）
    url: https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm
    publisher: 国家互联网信息办公室
    date: 2025-10-28
  - title: 中华人民共和国电信条例
    url: https://fgw.sh.gov.cn/cmsres/8b/8bd9351da1674928b6efa921be6cdb82/39534001789e1fd8fb7e034f70264f37.pdf
    publisher: 上海市发展和改革委员会（转载）
  - title: 中国移动 2025 年可持续发展报告
    url: https://www.chinamobileltd.com/sc/ir/reports/sd2025_ashare.pdf
    publisher: 中国移动
    date: 2026-03-26
authors:
  - anoni-net
---

美国第九巡回上诉法院正在审理一件基站倾印（tower dump）搜索票的上诉案。倾印搜索票要求移动通信运营商交出某时某地所有手机的位置数据，范围内跟案件无关的设备也包含在内。数字权利组织 EFF 与美国公民自由联盟（ACLU）在 11 月 3 日以法庭之友（amicus，非当事人向法院提出意见）的身份提交书状，主张倾印搜索票本身违宪。案件只涉及美国的执法，其他地方的读者不受直接影响。

EFF 的文章把基站倾印与 geofence（地理围栏）搜索票都归为反向位置搜索（reverse location searches），两者都先划出时间与地点，再从数据里找人。基站倾印向移动通信运营商调取，geofence 向 Google 这类公司调取设备的位置记录，数据源不同。美国最高法院 6 月 29 日判决的是 geofence，第九巡回法院的上诉案（案号 `26-689`）是基站倾印。

依 EFF 的文章，两名受害人的遗体在加州一条偏远公路旁被发现，警方在同一条公路数英里外找到其中一人的车。警方随后申请涵盖该路段的基站倾印搜索票，最后取得近 1,700 支不重复手机的位置数据。

依 The Register 引述的裁定，内华达联邦地方法院 2025 年认定基站倾印属于美国宪法第四修正案（禁止不合理的搜索与扣押）所称的搜索，本案的搜索票是第四修正案禁止的概括搜索票（general warrant，不限定对象的搜索令状）。裁定同时没有排除任何证据，理由是该院看来是第九巡回法院辖区内第一个这样认定的法院，而且善意例外（good faith exception，执法人员相信自己依搜索票合法行事时，证据原则上仍可使用）适用。被告其后向第九巡回法院上诉。

依 EFF 的文章，书状有三项主张。最高法院的 geofence 判决加强了基站倾印属于违宪概括搜索票的论点，没有相当理由（probable cause，核发搜索票要求的具体依据）认为范围内所有人都涉案，就不能搜索所有人。即使法院仍允许倾印搜索票，也要限制范围与期限、通知受影响的人，并在事后删除无关的数据。书状也要求法院放下善意例外，实际判断宪法问题。

最高法院的 geofence 判决以 6 比 3 认定，警方调取手机位置记录属于搜索，即使时间很短、数据在第三方公司手上也一样。依法律事务所 ZwillGen 的分析，搜索票是否具体、有没有相当理由，发回先前审理的第四巡回法院判断。反向搜索票是否合宪仍未解决。EFF 的文章把第九巡回法院的上诉案写成判决之后第一件进入联邦上诉法院的同类案件。

## 导读观点 {#perspective}

手机开机且未开飞行模式时会连上基站，这是移动网络的基本运作方式（本文补充的背景，下面的来源没有直接写这一句）。SCOTUSblog 整理最高法院 2018 年的基站案时，把基站位置信息描述成手机连上基站时产生的历史记录。The Register 提到倾印可以涵盖十分钟到一小时内连上该基站的所有连接。

Google 账号的定位记录（Location History，Google Maps 时间轴背后的设置）是另一份数据，存放在设备上或 Google 的服务器，本文据此推论关闭它挡不了基站倾印。查到的来源没有写出用户这一端能避开基站记录的做法，哪些连接会留下可调取的记录、运营商保存多久也没有写。

到 11 月 8 日，本文查不到政府一方在第九巡回法院上诉案提出的书状，也查不到相关报道。依联邦上诉程序的通则，答辩期限通常在上诉人书状后 30 天，查不到可能只是期限未到（本文推算，未查到案卷）。下一段政府一方的论点都出自别的案件（最高法院的 geofence 案与同案的第四巡回法院判决），当时的数据来自 Google，跟电信运营商无关。

依 ABC News 的报道，政府在最高法院的 geofence 案主张，用户把位置信息分享给 App 与 Google 这类服务商就放弃了隐私期待。第四巡回法院的多数意见也认为当事人自愿让 Google 持有的两小时位置数据不能合理期待保密（依 SCOTUSblog）。最高法院的多数意见认定数据由第三方公司持有时当事人仍有隐私期待，2018 年的基站案判决也已认定取得基站位置信息属于搜索、不适用第三方原则（third-party doctrine，交给第三方的记录不受第四修正案保护的见解，依 SCOTUSblog 与 Independent Institute 的整理）。这些来源没有说明 2018 年的判决是否及于倾印，政府一方会如何主张、法院是否接受，要看上诉案的后续。

EFF 的文章主张反向位置搜索票本身违宪，并举法律禁止警方搜索犯罪现场附近上百户住家为例。依 The Register 的报道，密西西比一位联邦治安法官 2025 年 2 月以缺乏对特定个人的相当理由驳回 FBI 的四张基站倾印搜索票，政府 2025 年 6 月申请延长决定是否上诉的期限（到 11 月 8 日查不到结果）。ABC News 的报道则写 geofence 搜索票对调查人员寻找嫌疑人、失踪儿童与山区迷路者的价值越来越高，也写专家认为限制可能妨碍执法。最高法院审理 geofence 案的口头辩论时，一位大法官提出的方向是订出合理的时间与地理范围，再交给核发搜索票的法官落实。

地方法院认定搜索票违宪却不排除证据，依据是善意例外。EFF 的文章主张，法院常回避新型监控技术的宪法问题，警方可以继续使用多年甚至数十年却没有明确的判决。依 EFF 2024 年的文章，第五巡回法院在另一件 geofence 案适用善意例外的理由是 2018 年的技术还新颖，警方也向有经验的机关求教。最高法院的不同意见同样以善意例外为由，主张第四巡回法院既已认定善意例外适用，判决对当事人就没有实际影响。

中国大陆的《网络安全法》（2025 年 10 月 28 日修正，2026 年 1 月 1 日起施行）第三十条规定，网络运营者（网络的所有者、管理者和网络服务提供者）应当为公安机关、国家安全机关依法维护国家安全和侦查犯罪的活动提供技术支持和协助（电信运营商是否属于此类，本文没有查证）。条文没有写明某基站某时段全部连线的倾印是否适用（本文比对法条的观察），到 11 月 8 日也没有查到官方说明。《电信条例》第六十五条规定的是检查电信内容的机关与程序，条文没有写通话记录这类非内容的资料。到 11 月 8 日，在中国移动 2025 年的可持续发展报告里没有找到政府调取用户资料的件数，中国电信与中国联通的同类披露没有查。

想确认 Google 这一端数据的人，可以到 Android 或 iPhone 版 Google Maps App 的 Your Timeline 设置，查看定位记录对应的时间轴（Timeline）是否打开。依 Google 2023 年的公告与 11 月 8 日查阅的说明页，时间轴默认关闭、要自行同意才会打开，数据存在设备上。用户另外选择备份时，Google 服务器上会有一份加密副本。Apple 2025 年下半年的透明报告写明没有数据可回应 geofence 要求。

依最高法院的不同意见与 Independent Institute 的分析，Google 修改定位记录服务后已无法再回应 geofence 搜索票。Independent Institute 的分析写明改变发生在 2025 年 7 月，到 11 月 8 日没有找到 Google 自己的说明。上面的设置与报告都只涉及 Google、Apple 手上的数据。

看上诉案的后续，第九巡回法院会实际判断宪法问题，还是再次停在善意例外。如果允许倾印搜索票，范围、期限、通知与删除的限制能否保护无关的路人，又不让缺少嫌疑人线索的案件失去调查方法。政府一方的书状会沿用用户自愿交出数据的论点，还是另外说明基站记录跟 Google 数据的差别。
