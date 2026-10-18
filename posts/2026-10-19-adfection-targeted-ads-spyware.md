---
title: 定向廣告投遞的零點擊間諜軟體
description: Citizen Lab 10 月 15 日發表報告，以高信心把半島電視台至少 45 台裝置在 2024 到 2025 年遭到的攻擊，連到以色列廣告公司 Discover-Tech 的定向廣告與 Candiru 的間諜軟體。報告確認的鎖定對象只有半島電視台，也沒有說明被利用的漏洞。給一般讀者的建議是封鎖廣告與限制廣告識別碼，報告也提到這些做法只能降低部分風險。
date: 2026-10-19T00:00:00+08:00
slug: adfection-targeted-ads-spyware
categories:
  - surveillance
sources:
  - title: "Exposing AdFection: How Discover-Tech Turned Targeted Ads Into a Pipeline for Zero-Click Mercenary Spyware"
    url: https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/
    publisher: Citizen Lab
    date: 2026-10-15
  - title: Exposing AdFection Executive Summary
    url: https://citizenlab.ca/research/exposing-adfection-executive-summary/
    publisher: Citizen Lab
    date: 2026-10-15
  - title: "Re: Citizen Lab Right to Reply"
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Citizen-Lab-Right-to-Reply-IAB.pdf
    publisher: IAB Europe
    date: 2026-10-15
  - title: "Re: Citizen Lab Report Right to Reply"
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Adtimizer-Response-to-Request-for-Comment.pdf
    publisher: Adtimizer
    date: 2026-10-11
  - title: Citizen Lab Right of Reply
    url: https://citizenlab.ca/wp-content/uploads/2026/10/Volasim-Response-to-Request-for-Comment.pdf
    publisher: Volasim
    date: 2026-10-12
  - title: Israeli ad-tech firm helped place spyware on Al Jazeera devices
    url: https://www.aljazeera.com/news/2026/10/15/israeli-ad-tech-firm-helped-spy-on-al-jazeera-devices
    publisher: Al Jazeera
    date: 2026-10-15
  - title: Targeted ads delivered 0-click exploits to install mercenary malware
    url: https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/
    publisher: Ars Technica
    date: 2026-10-15
  - title: Online ads weaponised to deliver ‘zero-click’ spyware, researchers say
    url: https://www.theguardian.com/technology/2026/oct/15/israeli-firm-digital-ads-enabling-installation-of-zero-click-spyware-researchers-say
    publisher: The Guardian
    date: 2026-10-15
  - title: First Zero-Click Mercenary Spyware Delivered Via Targeted Ads Uncovered by CitizenLab
    url: https://www.privacyguides.org/news/2026/10/16/first-mercenary-spyware-delivered-via-targeted-ads-uncovered-by-citizenlab/
    publisher: Privacy Guides
    date: 2026-10-16
  - title: 以色列廣告業者利用定向廣告發動零點擊攻擊，半島電視臺裝置遭間諜軟體入侵
    url: https://www.ithome.com.tw/news/179747
    publisher: iThome
    date: 2026-10-16
  - title: 如果 App 要求追蹤你的活動
    url: https://support.apple.com/zh-tw/102420
    publisher: Apple
  - title: 廣告 ID
    url: https://support.google.com/googleplay/android-developer/answer/6048248?hl=zh-Hant
    publisher: Play 管理中心說明
watch:
  - date: 2026-11-18
    note: Citizen Lab 預告的 DARK CARTOGRAPHER 後續報告是否發表，Discover-Tech 或 Candiru 是否公開回應，IAB Europe 是否把 Discover-Tech 正式除名，Apple 或 Google 是否發布相關修補公告
authors:
  - anoni-net
---

依 Citizen Lab 10 月 15 日發表的 AdFection 報告，以色列廣告公司 Discover-Tech 的線上廣告被用來投遞傭兵間諜軟體（賣給政府客戶的商業間諜軟體），廣告顯示在畫面上就能觸發。報告以高信心把半島電視台（Al Jazeera）在 2024 到 2025 年遭到的攻擊連到以色列業者 Candiru 的間諜軟體，至少 45 台裝置遭到鎖定。報告確認的鎖定對象只有半島電視台，Discover-Tech 的廣告則出現在近 20 萬個網站與 App，廣告曝光本身不代表遭到鎖定。報告沒有說明被利用的漏洞與受影響的版本，研究者取得的樣本是從一台受害裝置分離出來的 Windows 程式檔，報告沒有確認手機遭到感染。

線上廣告多半透過即時競價（RTB，每次顯示廣告前即時舉行的拍賣）決定，廣告主出價爭取把某則廣告顯示給特定使用者，廣告裡也可以帶著在 App 或瀏覽器裡執行的程式碼。依報告，Discover-Tech 的許多廣告帶有一段標籤，顯示時會連回它的伺服器並送出使用者的廣告識別碼或 cookie 識別碼。伺服器只對選定的目標回傳程式碼，Discover-Tech 平台的客戶（報告認為包括 Candiru 這類間諜軟體業者）可以用手機的廣告識別碼、瀏覽器的 cookie 識別碼或 IP 位址挑選目標，其他人收到的是空白回應。依報告，這個設計讓 Discover-Tech 不必把惡意程式碼、甚至指向它的連結交給替它刊登廣告的平台。

研究者在 Discover-Tech 的網站找到兩個公開可讀的資料庫，2026 年 3 到 6 月的競價紀錄約 37.7 億筆，看起來得標約 4.4 億筆。其中至少 7.2 億筆競價的廣告從名稱判斷帶有連回這類伺服器的標籤，七成以上的競價發生在 App 裡。報告列出曾有廣告曝光的網路，包括北約、聯合國、歐洲議會與二十多個國家的政府網路。報告評估這些曝光至少讓 Discover-Tech 能剖析裝置，部分情況可能讓其他業者的程式碼在裝置上執行，但曝光不等於確認遭到鎖定或感染。

依報告附的各家回覆，Google 終止 Discover-Tech 在廣告交易平台的出價與投放，並用安全瀏覽（Safe Browsing）對已知的網域顯示警告。Beeswax、Vungle（Liftoff）與 Eskimi 也停止或暫停了合作。依 IAB Europe 的回信，Discover-Tech 從 10 月 8 日起在供應商名錄（GVL，參與其透明與同意框架的廠商清單）遭到暫停（報告正文寫的是移除），原因是稽核發現違反框架政策。Discover-Tech 與 Candiru 沒有在報告給的期限內回覆，到 10 月 18 日也查不到兩家的公開聲明。

報告另外點名 Adtimizer 與 Volasim 兩家公司。Adtimizer 的回信表示只把一些子網域配給一般廣告用途，那些子網域只在 Discover-Tech 的基礎設施裡使用。Volasim 的回信表示 Discover-Tech 是它委託推廣產品的外部廣告商之一，並願意在保密協議下提供原始碼供獨立審查。報告認為兩家跟 Discover-Tech 有關聯，但也提到沒有確切證據顯示兩家知情參與。

## 導讀觀點 {#perspective}

監控產業把利用廣告資料辨識與追蹤特定人的平台稱為廣告情報（ADINT）。依報告，能取得競價資料的公司可以從同一個識別碼的出價請求看出一個人在不同地點與網路之間的移動，AdFection 則把這套辨識接上了攻擊程式（本文的理解）。報告的評價是這些廣告業名錄看起來大多靠廠商自我聲明。IAB Europe 的回信則表示，列入名錄不代表 IAB Europe 認證該公司的所有活動都符合 GDPR，該組織也沒有能力與職權做鑑識或刑事調查。

Citizen Lab 給一般使用者的建議是在瀏覽器裝可信的廣告封鎖擴充功能、改用會擋追蹤的瀏覽器、定期重設手機的廣告識別碼並關閉廣告追蹤，也可以在家中的路由器或可信的 VPN 服務擋廣告。給組織資安人員的建議，報告判斷目前最可行的防護是在組織網路的出口（閘道）擋掉定向廣告，直到業界證明能可靠擋下這類手法。報告沒有寫出被利用的漏洞，無法判斷更新到哪個版本能修補，Ars Technica 另外提醒及時安裝更新。

因工作或身分而面臨較高風險的人，報告建議尋求專家協助。一般讀者可以先限制廣告識別碼。iPhone 到「設定」的「隱私權與安全性」、「追蹤」，關閉「允許 App 發出追蹤請求」（iOS 14.5 以上）。Android 依 Google 的說明到「設定」的「隱私權」、「廣告」選「刪除廣告 ID」（需要 Google Play 服務），兩家的說明頁都有正體中文版（10 月 18 日查證）。

依報告，這些做法降低的是部分風險。報告在給組織資安人員的建議裡提到，封鎖廣告識別碼能擋下 Discover-Tech 目前的做法，但研究者推測這類攻擊的範圍更大。依本文的理解，重設手機的廣告識別碼擋不到用 cookie 識別碼或 IP 位址挑選的目標。漏洞沒有公開，更新到哪個版本能修補也無從判斷。
