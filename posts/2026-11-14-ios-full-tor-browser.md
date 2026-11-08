---
title: iPhone 上的 Tor 選項與完整 Tor Browser 的開發計畫
description: 到 11 月 8 日為止，iPhone 上沒有 Tor Browser，Tor Project 推薦的是 Onion Browser。Guardian Project 公布一年路線圖，Alpha 測試版排在標示為 2027 年 4 月的那一季，Alpha 推出前無法安裝。
date: 2026-11-14T00:00:00+08:00
slug: ios-full-tor-browser
categories:
  - mobile
sources:
  - title: "Brewing Onion Cider: Bringing a full Tor Browser to iOS"
    url: https://guardianproject.info/2026/11/02/brewing-onion-cider-bringing-a-full-tor-browser-to-ios/
    publisher: Guardian Project
    date: 2026-11-02
  - title: How to install Tor Browser
    url: https://support.torproject.org/tormobile/tormobile-3/
    publisher: Tor Project
  - title: FAQs
    url: https://onionbrowser.com/faqs
    publisher: Onion Browser
  - title: Using alternative browser engines in the European Union
    url: https://developer.apple.com/support/alternative-browser-engines/
    publisher: Apple
  - title: Using alternative browser engines in Japan
    url: https://developer.apple.com/support/alternative-browser-engines-jp/
    publisher: Apple
  - title: Onion Browser
    url: https://apps.apple.com/us/app/onion-browser/id519296448
    publisher: Apple
  - title: Orbot
    url: https://apps.apple.com/us/app/orbot/id1609461599
    publisher: Apple
watch:
  - date: 2027-03-31
    note: Guardian Project 是否決定 iOS 版 Tor Browser 的主要路線（Apple 官方商店或側載），是否展示在 iOS 上執行 Gecko 的原型
  - date: 2027-06-30
    note: iOS 版 Tor Browser 的 Alpha 是否經 TestFlight 與側載推出、開放哪些地區，Tor Project 是否同意使用 Tor Browser 的名稱
authors:
  - anoni-net
---

到 11 月 8 日為止，iPhone 上沒有 Tor Browser（經 Tor 網路連線的瀏覽器）。Tor Project 在安裝說明頁推薦改用 Onion Browser，也提醒它的隱私保護比不上 Tor Browser。Guardian Project 在 11 月 2 日公布一年路線圖，目標是把完整的 Tor Browser 帶到 iOS，第一個 Alpha 測試版排在路線圖標示為 2027 年 4 月的那一季。計畫還在決定走哪一條發行路線，Alpha 推出前無法安裝，iPhone 使用者手上的選項沒有改變。

依 Onion Browser 的常見問題頁（FAQ），Tor 能讓監看連線的人看不到你造訪的網站，也讓網站無法得知你的實際位置。在 iPhone 上經 Tor 瀏覽網頁，可以用開源的 Onion Browser。它有兩種連線方式：搭配另一款 App Orbot，或用 App 內建的 Tor（Onion Browser 的 FAQ 裡標註 iOS 17 only）。依 App Store 的資料，到 11 月 8 日為止兩款都免費、最低需求都是 iOS 15，最近一次更新分別在 10 月 20 日與 10 月 15 日。

依 FAQ 的比較，Orbot 比較安全，內建的 Tor 比較穩定。使用內建的 Tor 時，真實 IP 會經由 WebRTC（瀏覽器直接傳輸影音與資料的技術）洩漏給造訪的網站，音訊與影片串流也無法經過 Tor。FAQ 裡的原因是 Apple 提供並強制使用的瀏覽器引擎 WebKit（引擎是解析與顯示網頁的核心元件）。Orbot 使用 Apple 的 Network Extensions（網路擴充功能），Apple 只給它 50 MB 記憶體，Tor 客戶端接近上限時會被終止並重新啟動。

依 FAQ，Onion Browser 會在離開前景時自動清除資料、預設不保留快取與 cookie，也能偵測網站的 .onion 位址並自動切換。至於瀏覽器指紋（網站用裝置與瀏覽器的細節辨識訪客的手法），FAQ 裡的說法是 iOS 內建的 WebKit 能調整的地方很少，最好的做法是跟其他 iOS 使用者看起來一樣。

只想讓整台 iPhone 的連線走 Tor 時，也可以用 Orbot 搭配 Safari。依 FAQ，Orbot 把裝置上所有流量都送進 Tor，搭配 Safari 時同樣有 Tor 的效果。Orbot 被終止時 Safari 的連線會如何，FAQ 裡沒有交代。

FAQ 裡 Onion Browser 比 Safari 多的保護，首先是確認 Tor 正在運作並接手請求之後才送出連線，另外還有自動清除與 .onion 切換。本文依 Tor Project 與 FAQ 對 WebKit 的說明推論，Safari 與 Onion Browser 一樣受 WebKit 限制，同樣達不到 Tor Browser 的反追蹤能力。

Guardian Project 在公告自述有十年以上開發與發行 Onion Browser、iOS 版 Orbot 的經驗。新計畫要在 iOS 上提供以 Firefox 的 Gecko 引擎為基礎、納入 Tor Project 修補的 Tor Browser，同時繼續維護 Onion Browser 與 Orbot。依公告，Onion Browser 特意取了不同的名字，因為它並非完整的 Tor Browser。iOS 版要使用 Tor Browser 的名稱，還要取得 Tor Project 的核准。

路線圖以季為單位，標示為 2027 年 1 月的第二季要展示在 iOS 上執行 Gecko 的原型，並選定主要路線。標示為 2027 年 4 月的第三季要透過 TestFlight（Apple 的測試版發放管道）與側載（不經 App Store 安裝 App）推出第一個 Alpha。標示為 2027 年 7 月的第四季才要決定下一步是 Beta 還是正式推出。

公告裡也寫到哪條路最好仍不確定，路線圖列了兩條。Apple 路線的依據是歐盟《數位市場法》（Digital Markets Act，DMA）要求 Apple 在 iOS 上開放第三方瀏覽器引擎，以及日本的替代瀏覽器引擎方案。Gecko 會透過 BrowserEngineKit（Apple 提供給替代引擎的開發工具）執行，經官方商店發行。開放路線改走 AltStore 這類側載管道，公告的用語是擺脫 App Store 的審查與限制。

## 導讀觀點 {#perspective}

依 Tor Project 的說明頁，Apple 要求 iOS 上的瀏覽器使用 WebKit，Onion Browser 因此無法具備與 Tor Browser 相同的隱私保護（歐盟與日本另有方案，見下一段）。FAQ 裡的說明是 Tor Browser 在電腦與 Android 上以 Firefox 的 Gecko 為基礎，實作代理與反追蹤時有更多控制空間，也更可靠。本文的理解是，換成 Gecko 處理的是引擎這一層的限制，經 Tor 連線本身 Onion Browser 現在就能做到。

Apple 的開發者文件到 11 月 8 日為止列出的條件是歐盟方案需要 iOS 17.4 或 iPadOS 18 以上、日本方案需要 iOS 26.2 以上。App 要先通過 Apple 的授權，也只能在當地發行（日本的文件另有 Apple 明確許可的例外）。本文依這些條件推論，除非 Apple 另外許可，歐盟與日本以外的 iPhone 使用者無法從官方商店取得走 Apple 路線的 Tor Browser。公告裡也有只能在歐洲與日本發行的假設，Guardian Project 打算推動 Apple 在全球開放第三方瀏覽器引擎。

公告裡以 malicious compliance（惡意遵從）形容 Apple 遵循 DMA 的做法，路線圖也排了針對 Apple 這個平台與發行者的風險分析。Apple 的文件裡寫的是，只授權符合特定標準、承諾持續遵守隱私與安全要求的開發者使用替代引擎。依公告，官方商店能觸及歐洲與日本只會從 Apple 官方管道取得 App 的一般使用者。側載對已經面臨 App Store 審查的使用者是否更有幫助，公告裡只有問句，沒有結論。

Alpha 的時程來自路線圖，公告裡沒有它能在哪些地區安裝的資訊。公告對經歐盟與日本商店發行 iOS 版 Tor Browser 的說法是 when and if（準備好才會進行）。

要對造訪的網站隱藏 IP 的人，依 FAQ 的比較適合讓 Onion Browser 搭配 Orbot（兩款都可以從 App Store 免費安裝，需要 iOS 15 以上）。Orbot 反覆重新啟動時，內建的 Tor 比較穩定，代價是前面提到的 IP 洩漏與影音不經 Tor。以上做法都仍用 WebKit。本文依 Tor Project 的說明推論，需要 Tor Browser 完整防護的人目前要改到電腦或 Android 上使用。

不需要對造訪的網站隱藏 IP 的讀者現在不必做任何設定，要回來看的時間點有兩個。標示為 2027 年 1 月的那一季會選定主要路線，本文推論路線的選擇會影響歐盟與日本以外的讀者能否取得。標示為 2027 年 4 月的那一季要看 Alpha 是否如期推出、開放哪些地區。Guardian Project 規劃繼續維護 Onion Browser 與 Orbot，路線圖的第三季（標示為 2027 年 4 月）也排了協助使用者判斷該用 Onion Browser 或 iOS 版 Tor Browser 的工作。
