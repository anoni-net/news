---
title: 醫療預約網站把看診資訊送給社群平台的追蹤碼
description: The Markup 與巴西媒體 Agência Pública 發現，醫療預約平台 Doctoralia 在拉丁美洲的網站，把醫師專科、姓名與預約時間送給 Google、TikTok 與 LinkedIn。
date: 2026-10-04T07:00:00+08:00
slug: doctoralia-health-tracking-pixels
sources:
  - title: How TikTok and Google ended up with information about doctors’ appointments around the world
    url: https://themarkup.org/pixel-hunt/2026/09/14/how-tiktok-and-google-ended-up-with-information-about-doctors-appointments-around-the-world
    publisher: The Markup
    date: 2026-09-14
  - title: This is how you stop data trackers from sucking up your health data
    url: https://themarkup.org/the-breakdown/2025/06/17/this-is-how-you-stop-data-trackers-from-sucking-up-your-health-data
    publisher: The Markup
    date: 2025-06-17
  - title: Blacklight
    url: https://themarkup.org/blacklight
    publisher: The Markup
  - title: 個人資料保護法 第 6 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6
    publisher: 全國法規資料庫
authors:
  - anoni-net
---

美國媒體 The Markup 與巴西媒體 Agência Pública 在 9 月 14 日發表調查，醫療預約平台 Doctoralia 在巴西、哥倫比亞、墨西哥等地的網站，把使用者預約看診的資訊送給 Google、TikTok 與 LinkedIn 等科技公司，用於廣告。Doctoralia 的母公司 Docplanner 在 13 個國家營運，這次報導的是拉丁美洲的網站。

在巴西，搜尋婦產科醫師時，網站把搜尋的專科送給 Google，完成預約後，醫師姓名、預約日期與時間也一併送出。在哥倫比亞與墨西哥，預約皮膚科或心理師時，醫師姓名與預約時間送到了 LinkedIn 與 TikTok。

追蹤在使用者輸入電子郵件或姓名之前就開始了，追蹤碼通常會用唯一的識別碼標記使用者。西班牙版的網站在測試中沒有把搜尋送出，德國的網站有彈出視窗讓使用者關閉追蹤 cookie，拉丁美洲的網站只告知使用了 cookie，沒有馬上提供關閉的選項。

Docplanner 表示正在進行技術與法律審查。Google 與 LinkedIn 都說政策禁止在收集健康資訊的頁面使用這類工具，TikTok 沒有回應。

## 導讀觀點 {#perspective}

追蹤碼是廣告平台提供給網站的一段程式，頁面載入時就把使用者看了什麼、按了什麼送回平台。醫療網站裝上它，搜尋的科別、預約的醫師本身就透露了健康狀況。巴西的主管機關對此看法不一，醫師公會認為預約看診不涉及醫療秘密，主管健康保險的機構則認為科別與預約資訊可能透露一個人的健康。

在台灣，《個人資料保護法》第 6 條把病歷、醫療與健康檢查的個人資料列為特種個資，原則上不得蒐集、處理或利用。預約資訊算不算在內，法條沒有逐項列出，但讀者自己可以先擋下追蹤。

The Markup 去年針對其他醫療網站的測試，列出幾種擋得住追蹤碼的做法：Firefox 把「強化型追蹤保護」從標準調到嚴格、Safari 開啟進階追蹤與指紋保護，或改用 Brave、DuckDuckGo 瀏覽器，也可以裝 Privacy Badger、uBlock Origin Lite 擴充套件。VPN 與無痕模式擋不住，在 Chrome 封鎖第三方 cookie 也不夠。

想知道常用的醫療網站裝了哪些追蹤碼，可以用 The Markup 的 Blacklight 輸入網址掃描。它檢查的項目包括網站是否把使用者資料送給 TikTok 與 Google Analytics，程式碼只開源了一部分。
