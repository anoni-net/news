---
title: iOS 瀏覽器引擎在歐盟與日本的開放條件與爭議
description: 歐盟與日本要求 Apple 在 iOS 開放 WebKit 以外的瀏覽器引擎，Apple 以安全與隱私為由訂了條件，Mozilla 則寫到這些條件讓它未能推出 Gecko 版的 Firefox。依 Mozilla 11 月 20 日的文章，到那時沒有開發者推出非 WebKit 的 iOS 瀏覽器。
date: 2026-11-26T00:00:00+08:00
slug: ios-browser-engines
categories:
  - mobile
sources:
  - title: Why there are still no non-WebKit browsers on iOS
    url: https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/
    publisher: Mozilla
    date: 2026-11-20
  - title: Using alternative browser engines in the European Union
    url: https://developer.apple.com/support/alternative-browser-engines/
    publisher: Apple
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: App Review Guidelines
    url: https://developer.apple.com/app-store/review/guidelines/
    publisher: Apple
    date: 2026-10-16
  - title: Apple announces changes to iOS in Japan
    url: https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/
    publisher: Apple
    date: 2025-12-17
  - title: Outline of the Act on Promotion of Competition for Specified Smartphone Software (Mobile Software Competition Act (MSCA))
    url: https://www.japaneselawtranslation.go.jp/en/outlines/view/154
    publisher: Japan Fair Trade Commission
  - title: The CMA's programme of work across mobile platforms
    url: https://www.gov.uk/guidance/the-cmas-programme-of-work-across-mobile-platforms
    publisher: Competition and Markets Authority
    date: 2026-02-10
  - title: "The Digital Markets Act Is Delivering Real Wins, But Not Yet for Browser Engines"
    url: https://open-web-advocacy.org/blog/the-digital-markets-act-is-delivering-real-wins-but-not-yet-for-browser-engines/
    publisher: Open Web Advocacy
    date: 2026-05-15
  - title: How Apple’s Key Tactic Could Prevent Japan’s Smartphone Act from Improving Browser Competition
    url: https://open-web-advocacy.org/blog/how_apples_key_tactic_could_prevent_japans_smartphone_act_from_improving_browser_competition/
    publisher: Open Web Advocacy
    date: 2026-01-06
watch:
  - date: 2026-12-22
    note: 歐盟或日本是否出現第一款非 WebKit 的 iOS 瀏覽器，歐盟執委會、英國 CMA 或日本 JFTC 是否對 Apple 的瀏覽器引擎條件採取措施，Apple 是否回應 Mozilla 11 月 20 日的文章
authors:
  - anoni-net
---

iPhone 與 iPad 上的瀏覽器，不論是 Safari、Chrome、Firefox 還是標榜隱私的瀏覽器，都使用 Apple 的 WebKit 引擎（解析與顯示網頁的核心元件）。歐盟與日本的法規要求 Apple 開放其他引擎，Apple 以安全與隱私為由訂了兩地的條件。Mozilla 11 月 20 日的文章寫到，這些條件讓它至今未能推出以自家引擎為基礎的 Firefox，到發文時也沒有任何開發者推出非 WebKit 的 iOS 瀏覽器。依 Apple 的 App 審核指南，瀏覽網頁的 App 要使用 WebKit，申請例外的條件分別寫在歐盟與日本的兩份頁面。

依 Mozilla 的文章，主要平台裡只有 iPhone 與 iPad 有這項限制。在 Apple 自己的 macOS 上，使用者也能使用以 Gecko（Mozilla 開發的瀏覽器引擎）為基礎的 Firefox。Firefox 的許多功能實作在 Gecko 裡，Mozilla 因此很難把完整的 Firefox 帶到 iPhone 上。

依倡議組織 Open Web Advocacy（OWA）的整理，歐盟《數位市場法》（Digital Markets Act，DMA）要求被認定為守門人的大型平台開放其他瀏覽器引擎，Apple 從 2024 年 3 月起要遵守。日本的《智慧型手機軟體競爭促進法》（Mobile Software Competition Act，MSCA）也有類似的規定。日本公平交易委員會（JFTC）的法律概要寫到，規模達到門檻、由 JFTC 指定的業者，不得以只允許自家引擎這類條件妨礙其他開發者使用別的引擎。業者為了安全、隱私等正當理由時可以例外。

開發者要使用其他引擎，依 Apple 的開發者文件需先取得授權，App 也只能在歐盟或日本當地發行（日本的條件在 2025 年 12 月公布）。安全方面，已經遭到攻擊利用的漏洞要及時修補，文件舉的例子是最簡單的類別在 30 天內處置。隱私方面，引擎要預設封鎖第三方 cookie（可以用來跨網站追蹤的 cookie）。

依 Mozilla 的說法，要使用 Gecko 就不能直接更新使用者已經安裝的 Firefox，需要另做第二個 Firefox。使用者得下載新 App，搬移書籤、密碼與瀏覽紀錄，再手動切換。Mozilla 寫到相當比例的人會因此放棄，包括從歐盟的瀏覽器選擇畫面挑了 Firefox 的人。條件之一要求 Mozilla 不得揭露專案的非公開資訊，它仍舉了這個例子說明面對的難處。

瀏覽器引擎經常處理不受信任、可能惡意的內容，也能接觸使用者的敏感資料，依 Apple 的開發者文件是最常見的攻擊途徑之一。Apple 因此只授權符合標準、承諾持續遵守安全與隱私要求的開發者。依 OWA 的引述，Apple 的法務副總在 2025 年的 DMA 工作坊提到 Google、Mozilla 等第三方可以帶入自己的引擎，「for whatever reason, they have chosen not to do so」（不論出於什麼原因，它們選擇不這麼做）。

OWA 在 5 月的文章寫到沒有瀏覽器業者在歐盟推出自家引擎，並請歐盟執委會調查 Apple 是否確實遵守 DMA。到 11 月 22 日，我們沒有查到執委會針對 Apple 瀏覽器引擎條件的決定，也沒有查到 Apple 對 Mozilla 這篇文章的公開回應。

英國競爭與市場管理局（CMA）2025 年 10 月把 Apple 的行動平台認定為具有策略市場地位（strategic market status），範圍包括行動瀏覽器與瀏覽器引擎。認定之後，CMA 可以對 Apple 採取針對性的措施。到 11 月 22 日，CMA 的工作計畫頁把移除 Apple 要求瀏覽器使用 WebKit 的限制列為接下來預期推進的工作，頁面沒有寫時程。

## 導讀觀點 {#perspective}

iOS 上換一款瀏覽器，介面、預設設定與附加功能會不同，引擎都是 WebKit。本站 [11 月 14 日的導讀](https://anoni.net/news/2026/11/ios-full-tor-browser/)依 Tor Project 的說明整理過，Tor Browser 以 Firefox 的 Gecko 為基礎，iPhone 上的 Onion Browser（經 Tor 連線的開源瀏覽器）受 WebKit 限制而達不到同樣的保護。10 月整理的 [Firefox iOS 版廣告封鎖](https://anoni.net/news/2026/10/firefox-ios-ad-blocker/)也是用 WebKit 的內容封鎖技術實作的，電腦版與 Android 版的 Firefox 則能直接安裝擴充套件。

照 Apple 只能在當地發行的條件推想，即使歐盟或日本之後出現使用其他引擎的瀏覽器，台灣、香港與其他地區的 iPhone 使用者從 App Store 取得的仍會是 WebKit 瀏覽器。例外是 Apple 另外許可，或當地的法規也要求開放。11 月 14 日那篇整理的 iOS 版 Tor Browser 開發計畫，經 App Store 發行時同樣受這項條件限制。

Apple 公開的兩份條件頁列了安全與隱私要求，也列了只能在當地發行的限制，其中沒有另做一個 App 的文字。Mozilla 則寫到自己受保密條件限制，無法公開細節。對於沒有瀏覽器上架，Mozilla 與 OWA 歸因於 Apple 的條件，Apple 的法務副總在 2025 年的工作坊上則歸因於業者自己的選擇。

在 iPhone 上需要經 Tor 瀏覽網頁的人，可以用 11 月 14 日那篇整理的 Onion Browser 搭配 Orbot（把手機連線送進 Tor 網路的 App）。網頁仍由 WebKit 處理，依同一篇整理的說明，瀏覽器指紋（網站用裝置與瀏覽器的細節辨識訪客的手法）能調整的地方很少。Tor Browser 只有電腦與 Android 版，需要它完整防護的人要改用這兩種裝置，想用 Firefox 擴充套件的人也一樣。只用 Safari 或其他瀏覽器上網的讀者現在不需要調整設定。

比較各地的做法時，安全方面可以用 Apple 舉的 30 天例子看開放之後漏洞能否及時處置，競爭方面可以用 Mozilla 描述的搬資料成本看使用者是否因此流失。
