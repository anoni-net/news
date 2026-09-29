---
title: 醫療預約網站把看診資訊送給社群平台的追蹤碼
description: 醫療預約平台 Doctoralia 在巴西、哥倫比亞、墨西哥等地的網站，把看診專科、醫師姓名與預約時間送給 Google、TikTok 與 LinkedIn。它的母公司在台灣、香港、澳門沒有營運。
date: 2026-10-04T07:00:00+08:00
slug: doctoralia-health-tracking-pixels
sources:
  - title: How TikTok and Google ended up with information about doctors’ appointments around the world
    url: https://themarkup.org/pixel-hunt/2026/09/14/how-tiktok-and-google-ended-up-with-information-about-doctors-appointments-around-the-world
    publisher: The Markup
    date: 2026-09-14
  - title: Docplanner Group
    url: https://www.docplanner.com/
    publisher: Docplanner
  - title: This is how you stop data trackers from sucking up your health data
    url: https://themarkup.org/the-breakdown/2025/06/17/this-is-how-you-stop-data-trackers-from-sucking-up-your-health-data
    publisher: The Markup
    date: 2025-06-17
  - title: Blacklight
    url: https://themarkup.org/blacklight
    publisher: The Markup
  - title: the-markup/blacklight-collector
    url: https://github.com/the-markup/blacklight-collector
    publisher: GitHub
  - title: 個人資料保護法 第 6 條
    url: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6
    publisher: 全國法規資料庫
  - title: Firefox 正體中文介面字串 preferences.ftl
    url: https://github.com/mozilla-l10n/firefox-l10n/blob/main/zh-TW/browser/browser/preferences/preferences.ftl
    publisher: Mozilla
  - title: 在 Mac 上的 Safari 中進行私密瀏覽
    url: https://support.apple.com/zh-tw/guide/safari/ibrw1069/mac
    publisher: Apple
regions:
  - BR
  - CO
  - MX
watch:
  - date: 2026-11-04
    note: Docplanner 技術與法律審查的結果，拉丁美洲的 Doctoralia 網站是否停止把預約資訊送給 Google、TikTok 與 LinkedIn
authors:
  - anoni-net
---

根據美國媒體 The Markup 與巴西媒體 Agência Pública 在 9 月 14 日發表的調查，醫療預約平台 Doctoralia 在巴西、哥倫比亞、墨西哥等地的網站，把預約資訊送給 Google、TikTok 與 LinkedIn 投放廣告。母公司 Docplanner 在歐洲、土耳其與拉丁美洲共 13 個國家營運，不包括台灣、香港、澳門。

巴西的網站把使用者搜尋的婦產科送給 Google，預約後再送出醫師姓名與預約時間。哥倫比亞的網站把各專科的醫師姓名與預約時間送給 LinkedIn，哥倫比亞與墨西哥的預約也送到 TikTok。追蹤在輸入姓名或電子郵件之前就開始。

Doctoralia 的總部在西班牙，適用歐盟的 GDPR（一般資料保護規則），西班牙版網站在測試中沒有把搜尋內容送給外部公司。Docplanner 在德國的同類網站讓使用者關閉追蹤 cookie，拉丁美洲的網站只告知使用 cookie，沒有立即提供關閉選項。

Docplanner 的聲明寫明追蹤碼用來監測自家的社群廣告、不販售個人資料，公司到 9 月 14 日報導刊出時正在進行技術與法律審查。LinkedIn 的回覆寫明政策禁止在蒐集敏感資料的頁面安裝追蹤碼，Google 的回覆寫明禁止蒐集私人健康資訊，TikTok 沒有回應。

## 導讀觀點 {#perspective}

追蹤碼是廣告平台提供給網站的程式，由瀏覽器把使用者的瀏覽與點擊連同唯一的識別碼送回平台。依社群公司的說明，識別碼可以連到社群帳號。裝在醫療網站上時，送出的科別與醫師可能透露健康狀況。

巴西的聯邦醫學委員會認為預約不涉及醫療保密義務，監理私人健保的國家補充健康局則認為預約資訊可能透露健康狀況。台灣的《個人資料保護法》第 6 條原則上禁止蒐集、處理或利用病歷、醫療與健康檢查的個人資料，預約資訊是否屬於醫療的個人資料，條文沒有明寫。

想知道醫療網站是否把資料送給 TikTok 或 Google Analytics，可以到 The Markup 的 Blacklight 輸入網址掃描。一次約 30 秒到一分鐘，介面只有英文，預約過程中才送出的資料可能看不到。部分程式碼以 GPL-3.0 授權公開在 GitHub，6 月有新版發布。

The Markup 在 2025 年 6 月測試美國州政府的健保網站時，Firefox 與 Safari 的內建設定、Brave 與 DuckDuckGo 瀏覽器、Privacy Badger 與 uBlock Origin Lite 擴充套件都擋下當時檢查的 LinkedIn、Snapchat 與 Google 追蹤碼。TikTok 不在當時的測試範圍，擴充套件限桌機瀏覽器，VPN 與無痕模式則擋不下。

第一步可以在桌機版 Firefox 設定的「隱私權與安全性」，把「加強型追蹤保護」從「標準」改成「嚴格」。改一個選項就好，不需要帳號，介面有正體中文。代價是某些網站可能會故障，設定畫面上也有這項提醒。在 Mac 的 Safari「進階」設定裡，可以把「使用進階追蹤和指紋保護」套用到所有瀏覽，部分網站功能同樣可能受影響。
