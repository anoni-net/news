---
title: 瀏覽器指紋與各家瀏覽器的防護
description: 瀏覽器指紋是網站讀取視窗大小、字型與繪圖的細微差異這類特徵，組合出可以重複認出同一個瀏覽器的識別，清除 cookie 或連 VPN 都擋不住。依英國資訊專員辦公室的說明，Google 從 2025 年 2 月起不再禁止廣告客戶使用指紋技術。能擋下多少取決於用哪個瀏覽器，Firefox、Safari、Brave 與 Tor Browser 各有做法。本文 10 月 23 日查看的 Chrome 官方狀態頁，列出的指紋相關項目只有限縮瀏覽器隨每個請求自動附帶的資料。
date: 2026-10-25T00:00:00+08:00
slug: browser-fingerprinting-cookies
categories:
  - tracking
sources:
  - title: Our response to Google's policy change on fingerprinting
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/12/our-response-to-google-s-policy-change-on-fingerprinting/
    publisher: Information Commissioner's Office
    date: 2024-12-19
  - title: Updating our platform policies to reflect innovations in the ads ecosystem
    url: https://support.google.com/marketingplatform/answer/15732590
    publisher: Google Marketing Platform Help
  - title: A new path for Privacy Sandbox on the web
    url: https://privacysandbox.google.com/blog/privacy-sandbox-update
    publisher: Google
    date: 2024-07-22
  - title: Privacy Sandbox feature status
    url: https://privacysandbox.google.com/overview/status
    publisher: Google
  - title: Building a more private web
    url: https://blog.google/products-and-platforms/products/chrome/building-a-more-private-web/
    publisher: Google
    date: 2019-08-22
  - title: Overview of the Platforms programs policies update (February 2025)
    url: https://support.google.com/platformspolicy/answer/15738904
    publisher: Google
  - title: Next steps for Privacy Sandbox and tracking protections in Chrome
    url: https://privacysandbox.google.com/blog/privacy-sandbox-next-steps
    publisher: Google
    date: 2025-04-22
  - title: Update on Plans for Privacy Sandbox Technologies
    url: https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies
    publisher: Google
    date: 2025-10-17
  - title: Mitigating Browser Fingerprinting in Web Specifications
    url: https://www.w3.org/TR/fingerprinting-guidance/
    publisher: W3C
    date: 2025-09-25
  - title: "Firefox expands fingerprint protections: advancing towards a more private web"
    url: https://blog.mozilla.org/en/firefox/fingerprinting-protections/
    publisher: Mozilla
    date: 2025-11-10
  - title: Private Browsing 2.0
    url: https://webkit.org/blog/15697/private-browsing-2-0/
    publisher: WebKit
    date: 2024-07-16
  - title: WebKit Features in Safari 26.0
    url: https://webkit.org/blog/17333/webkit-features-in-safari-26-0/
    publisher: WebKit
    date: 2025-09-15
  - title: Apple elevates the iPhone experience with iOS 26
    url: https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/
    publisher: Apple
    date: 2025-06-09
  - title: Change Advanced settings in Safari on Mac
    url: https://support.apple.com/guide/safari/advanced-ibrw1075/mac
    publisher: Apple Support
  - title: Fingerprinting Protections
    url: https://github.com/brave/brave-browser/wiki/Fingerprinting-Protections
    publisher: Brave
  - title: How do I use Shields while browsing?
    url: https://support.brave.app/hc/en-us/articles/360022806212-How-do-I-use-Shields-while-browsing
    publisher: Brave Help Center
  - title: Fingerprinting protections - Features - Tor Browser
    url: https://support.torproject.org/tor-browser/features/fingerprinting-protections/
    publisher: Tor Project
  - title: Cover Your Tracks
    url: https://coveryourtracks.eff.org/
    publisher: EFF
  - title: Cover Your Tracks
    url: https://coveryourtracks.eff.org/learn
    publisher: EFF
  - title: Fingerprints are the new cookies
    url: https://royfish.dev/fingerprints-are-the-new-cookies
    publisher: royfish.dev
watch:
  - date: 2026-12-15
    note: Firefox 是否在標準模式預設開啟 145 版新增的指紋防護，Chrome 的第三方 cookie 設定與 Privacy Sandbox 是否再有變動
authors:
  - anoni-net
---

一篇個人部落格文章以「Fingerprints are the new cookies」為題，整理網站在 cookie 之外辨識瀏覽器的方式。依 W3C 隱私工作小組 2025 年 9 月的文件，瀏覽器指紋是網站透過設定或其他可觀察的特徵辨識訪客、瀏覽器或裝置的能力，例如視窗大小、字型與繪圖的細微差異。依英國資訊專員辦公室（ICO）2024 年 12 月 19 日的說明，Google 從 2025 年 2 月 16 日起不再禁止使用它廣告產品的組織採用指紋技術。能擋下多少取決於用哪個瀏覽器，Firefox、Safari、Brave 與 Tor Browser 各有做法。

同一份 W3C 文件提到，清除 cookie 或使用 VPN 都無法阻止進一步的關聯，指紋通常也無法清除或重設。依同一份文件，面對有決心的追蹤者，單靠已經廣泛部署的技術手段很難完全消除指紋。文件也認為規格可以減少指紋。

Google 2019 年的部落格寫到，使用者無法清除指紋，也就無法控制資訊如何被收集。Google 當時認為用指紋追蹤使用者是錯的。Google 2024 年 12 月對廣告客戶的公告，寫這次政策更新是為了配合隱私強化技術與連網電視等新的廣告管道，公告與 2025 年 2 月的政策更新頁都沒有提到指紋。「不再禁止」是 ICO 轉述 Google 對廣告客戶的通知，Google 的兩份公開頁面都沒有這個說法，ICO 也形容這項變更不負責任。

ICO 另外提醒，依英國《隱私與電子通訊規則》（PECR）等資料保護法規，業者使用指紋技術之前要給使用者公平的選擇並在必要時取得同意。這些規定適用於英國，台灣有沒有針對裝置指紋的專門規範，本文沒有查到。

Google 原本計畫在 Chrome 淘汰第三方 cookie（網頁裡嵌入的廣告或分析服務存進瀏覽器、用來跨網站認出使用者的小檔案），2024 年 7 月 22 日改提議由使用者自行選擇。2025 年 4 月 22 日，Google 宣布不再推出額外的提示視窗，使用者繼續在 Chrome 的隱私權與安全性設定裡選擇。2025 年 10 月 17 日，Google 又宣布淘汰多數 Privacy Sandbox（Google 為取代第三方 cookie 提出的一組瀏覽器技術），其中包括遮蔽 IP 位址的 IP Protection。本文 10 月 23 日查看的 Privacy Sandbox 狀態頁（2026 年 8 月 14 日更新），列出的指紋相關項目只有限縮瀏覽器隨每個請求自動附帶的資料，例如瀏覽器版本與作業系統的字串。

## 導讀觀點 {#perspective}

WebKit 2024 年介紹 Safari 私密瀏覽的文章，把擋指紋的做法分成兩種。一種讓很多使用者共用同一個指紋，另一種讓每個網站看到的指紋都不同。Tor Browser 走的是前一種，它的支援頁說明要讓所有使用者完全相同實際上不可能，目標是減少每一項特徵可以分辨的組數。

Brave 兩種都用。依 Brave 的說明，它一方面讓各個 Brave 盡量看起來相似，一方面加入少量隨機的雜訊。雜訊的種子每個工作階段、每個網站都不同，網站之間就難以把同一個人串起來，Brave 的說明中心也列出 Shields 預設開啟封鎖指紋。

Mozilla 2025 年 11 月的公告說明，Firefox 145 新增的指紋防護先在私密瀏覽與加強型追蹤保護的嚴格模式開啟，公告當時寫正在讓它變成預設。WebKit 2025 年 9 月介紹 Safari 26.0 的文章提到，Safari 會阻止已知的指紋腳本可靠地讀取螢幕尺寸、音訊等可能透露裝置特徵的資訊。

Safari 另有一項進階指紋保護，可以只用在私密瀏覽或套用到全部瀏覽。Apple 2025 年 6 月的 iOS 26 新聞稿寫這項保護預設擴及全部瀏覽，Apple 的 Safari 說明頁則沒有寫預設值，本文建議自己打開設定確認。依 WebKit 2024 年那篇文章，iPhone 的位置是英文介面的「Settings > Apps > Safari > Advanced > Advanced Tracking and Fingerprinting Protection」，選「All Browsing」。Mac 是 Safari 設定的「進階」，開啟「使用進階追蹤和指紋保護」並選擇套用到所有瀏覽。

用桌機版 Firefox 的讀者，可以在「隱私權與安全性」把「加強型追蹤保護」從「標準」改成「嚴格」，取得 145 版新增的防護。手機版的預設本文沒有查到。

需要更強保護、能接受較慢連線的人，可以改用 Tor Browser，本文 10 月 23 日查看的 EFF 說明頁也把它列為最實際的選擇。Tor Project 的指紋保護說明頁有正體中文版。依文件站的整理，Android 有官方的 Tor Browser，iPhone 沒有。

想知道自己的瀏覽器有多容易被認出，可以打開 EFF 的 Cover Your Tracks，本文查到的頁面都是英文。頁面說明只收集匿名資料，比較的對象是最近來測試的訪客，各瀏覽器防護做法的差別也整理在文件站的[瀏覽器指紋是什麼，為什麼很難擺脫](https://anoni.net/docs/basics/browser-fingerprinting/){target="_blank"}。

防護越強，網站越容易出問題。Mozilla 的公告提醒，更激進的封鎖一定會破壞正常的網站功能，例如行事曆與會議工具需要真實的時區。Tor 的支援頁提到，特徵不一致可能讓防機器人系統把 Tor 使用者當成機器人，EFF 的說明頁也提醒防護本身有時會變成指紋的一部分。

本文的推論是，這些設定減少的是網站在讀者沒有登入時認出同一個人的能力，Brave 的做法則特別針對跨網站與跨工作階段的串聯。登入同一個帳號的網站，仍然知道是誰在瀏覽。
