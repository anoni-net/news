---
title: 紐約與加州的社群平台年齡確認規則與資料保管
description: 美國紐約與加州 2027 年 1 月起要求社群平台確認使用者的年齡，沒有確認年齡、或未成年且沒有家長同意的帳號，不提供依演算法推薦的動態與深夜的通知。紐約的規則限制確認年齡時能蒐集與保存的資料，並要求以政府證件確認年齡的平台另外提供不必出示證件的方式。規則以位在兩州的使用者為對象。
date: 2026-11-30T00:05:00+08:00
slug: age-verification-id-data-ny-ca
categories: [censorship]
sources:
  - title: Attorney General James and Governor Hochul Release Final SAFE for Kids Act Rules to Protect Children Online
    url: https://ag.ny.gov/press-release/2026/attorney-general-james-and-governor-hochul-release-final-safe-kids-act-rules
    publisher: New York State Attorney General
    date: 2026-07-28
  - title: SAFE for Kids Act Rule Text
    url: https://ag.ny.gov/sites/default/files/2026-07/safe_for_kids_act_rule_text.pdf
    publisher: New York State Attorney General
    date: 2026-07-28
  - title: Governor Newsom signs the strongest child safety chatbot and social media laws in the nation
    url: https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/
    publisher: Office of the Governor of California
    date: 2026-09-10
  - title: New York and California Age Gating Rules Go Into Effect in the New Year
    url: https://www.eff.org/deeplinks/2026/11/new-york-and-california-age-gating-rules-go-effect-new-year
    publisher: EFF
    date: 2026-11-24
  - title: Lawmakers warn ID verification companies to bolster security after September hack
    url: https://therecord.media/idscan-data-breach-warning-congressional-letter
    publisher: The Record
    date: 2026-11-24
  - title: FBI Probes Service Selling 153M+ Drivers Licenses
    url: https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/
    publisher: KrebsOnSecurity
    date: 2026-09-01
  - title: "Now open source: our Zero-Knowledge Proof (ZKP) libraries for age assurance"
    url: https://blog.google/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/
    publisher: Google
    date: 2025-07-03
  - title: longfellow-zk
    url: https://github.com/longfellow-zk/longfellow-zk
    publisher: GitHub
regions:
  - US
watch:
  - date: 2027-01-05
    note: 加州 SB 976 的檢察總長規則是否定稿，定稿裡的年齡確認方式與資料保存
  - date: 2027-02-01
    note: 紐約 SAFE for Kids Act 規則生效後，主要平台提供哪幾種年齡確認方式，有沒有採用零知識證明
authors:
  - anoni-net
---

美國紐約與加州從 2027 年 1 月起，社群平台要先確認使用者已成年，才能提供依演算法推薦的動態（平台替使用者挑選內容、不斷往下推送的首頁）與深夜的通知。紐約州檢察總長的新聞稿寫到，這兩項功能與兒少的憂鬱、焦慮、飲食與睡眠障礙有關，加州州長的新聞稿也把禁止對未滿 16 歲的人提供成癮功能列為保護兒少的措施。加州的法律 1 月 1 日生效，紐約為 SAFE for Kids Act 訂定的規則 1 月 25 日生效，兩州以外的讀者不在規則的範圍內。

在紐約，未滿 18 歲或沒有確認年齡的使用者只會看到自己追蹤或選擇的帳號、依固定順序（例如時間排序）排列的內容，午夜到早上 6 點也不會收到通知。有家長同意時例外，沒有同意的人也不會因此被擋在平台之外。加州的 SB 976 同樣要求未滿 18 歲的人取得家長同意，AB 1709 對未滿 16 歲的人則是有家長同意也不提供。[AB 1043](https://anoni.net/news/2026/10/california-ab1856-open-source-exemption/) 是另一套機制，讓作業系統把帳號持有人填寫的年齡範圍提供給 App。

紐約的規則適用於使用者至少兩成時間花在演算法動態上的平台。業者可以自選準確度達到規則標準、能保護使用者資料的確認方式，檢察總長的新聞稿舉的例子有上傳照片或影片，以及驗證電子郵件或電話號碼再比對其他資訊。把政府證件列為確認方式的業者，要另外提供至少一種不必出示證件的方式。提供零知識證明（只證明已成年、不透露其他資料的密碼學方法）的業者，以及依其他法律本來就要蒐集證件的業者，可以不另外提供這種方式。

業者確認年齡時能留下什麼，紐約的規則也有限制。用來確認的資料只能蒐集最少量、不得挪作他用，用完要立即刪除，或者去識別化之後才能繼續使用。要保存五年的是跟帳號連在一起的紀錄，內容有確認的日期、方式與結果，規則寫明除此之外不要求保存其他可以識別個人的資料。平台委託外部的驗證業者時，受託的業者同樣受這些規定約束。

路易斯安那州的證件掃描業者 IDScan 替租車公司、大麻藥局這類實體櫃台掃描證件，9 月傳出雲端平台上的客戶資料被竊。暗網上的販售者宣稱握有美國與加拿大超過 1.53 億張駕照，KrebsOnSecurity 訪問證件被賣的人之後，判斷資料看來來自 IDScan。這起外洩跟社群平台的年齡確認是兩件事，把兩者連在一起的是 KrebsOnSecurity 的觀察與它訪問的隱私研究者。

## 導讀觀點 {#perspective}

交出證件或照片之後，副本可能留在驗證業者手上。The Record 引述 KrebsOnSecurity 的作者，他在 IDScan 事件之後的兩個月裡找到二十幾家常預設保存證件掃描檔的身分驗證業者，委託驗證的公司常要多付費才能停止。KrebsOnSecurity 訪問的隱私研究者認為，以保護兒少為由要求出示駕照的線上身分機制讓敏感資料流向越來越多第三方業者，監督卻跟不上。兩黨的國會議員 11 月 23 日也寫信給數家身分驗證業者，要求盡量少蒐集、分享與保存個人資料。

零知識證明讓業者只收到已成年這個結果，不取得證件本身。歐盟的年齡驗證方案採用這種做法，本站 9 月整理過[它的隱私設計與爭議](https://anoni.net/news/2026/09/eu-age-verification-blueprint/)。Google 在 2025 年 7 月以 Apache-2.0 授權開源零知識證明的函式庫 longfellow-zk，可以搭配現有的數位證件標準。紐約的規則沒有要求平台提供零知識證明，平台會不會採用要等規則生效後才知道。

對同一套規則，電子前哨基金會（EFF，數位權利組織）擔心去識別化的資料被用來訓練 AI 模型、外洩之後被重新識別，也把五年的紀錄列為濫用與外洩的風險。規則要求平台採取合理措施偵測使用者隱藏或謊報所在地，EFF 認為這會擴大位置追蹤，可能波及 VPN 使用者。

成年人也可能被誤判為未成年，這時可以申訴。紐約的規則要求業者在 10 個工作天內答覆或要求補件，申訴時至少要能用一種政府證件以外的資料佐證。成年人被誤判的比率，規則沒有訂上限，只要求每年認證時列出 18 到 30 歲的誤判率。

位在紐約的使用者被要求確認年齡時，可以先讀平台的說明再選擇方式，規則要求平台寫出提供哪些方式、資料的用途與刪除的時間和方式。照片、影片與電話號碼這些替代方式同樣會把資料交給業者。不想確認年齡的人依新聞稿仍可使用平台，看到的是依固定順序排列、只來自追蹤或選擇帳號的內容。加州的規則到 11 月 24 日還是草案，加州的使用者要等定稿才知道平台會提供哪些方式。

比較其他地方的規定時，隱私方面可以看有沒有不出示證件的方式、業者能保存哪些資料與保存多久、委託的驗證業者是否同樣受約束。兒少保護方面可以看被誤判的人如何申訴，以及規則能不能實際阻止未成年人使用這些功能。
