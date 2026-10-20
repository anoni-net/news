---
title: Tor 洋蔥服務的靜態網站架設
description: 架設洋蔥服務不需要固定 IP、網域或開放連接埠，用 tor 加上一般的網頁伺服器就能把靜態網站放上 Tor 網路。tor 6 月到 10 月連續發布四個安全更新，其中三個的修補涉及洋蔥服務，到 10 月 20 日為止最新版是 0.4.9.14。網站的訪客要透過 Tor 連線，例如用 Tor Browser。
date: 2026-10-23T00:05:00+08:00
slug: tor-onion-service-static-site
categories:
  - censorship
sources:
  - title: Set up Your Onion Service
    url: https://community.torproject.org/onion-services/setup/
    publisher: Tor Project
  - title: How do Onion Services work?
    url: https://community.torproject.org/onion-services/overview/
    publisher: Tor Project
  - title: Operational Security
    url: https://community.torproject.org/onion-services/advanced/opsec/
    publisher: Tor Project
  - title: Client Authorization
    url: https://community.torproject.org/onion-services/advanced/client-auth/
    publisher: Tor Project
  - title: Onion-Location
    url: https://community.torproject.org/onion-services/advanced/onion-location/
    publisher: Tor Project
  - title: Onion Services Properties
    url: https://onionservices.torproject.org/technology/properties/
    publisher: Tor Project
  - title: Changes in version 0.4.9.14 - 2026-10-07
    url: https://gitlab.torproject.org/tpo/core/tor/-/raw/tor-0.4.9.14/ReleaseNotes
    publisher: Tor Project
    date: 2026-10-07
  - title: Onionspray
    url: https://onionservices.torproject.org/apps/web/onionspray/
    publisher: Tor Project
  - title: HTTPS for your Onion Service
    url: https://community.torproject.org/onion-services/advanced/https/
    publisher: Tor Project
  - title: Capability and Limitations
    url: https://arti.torproject.org/guides/capability-limitations/
    publisher: Tor Project
  - title: Arti
    url: https://gitlab.torproject.org/tpo/core/arti
    publisher: Tor Project
  - title: Best Practices for Hosting Onion Services
    url: https://riseup.net/en/security/network-security/tor/onionservices-best-practices
    publisher: Riseup
  - title: Self-Hosting on the Dark Web
    url: https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/
    publisher: 個人部落格
    date: 2026-06-01
watch:
  - date: 2026-11-20
    note: tor 是否再發布影響洋蔥服務的安全更新，Arti 的洋蔥服務伺服端文件是否統一說明可以正式使用
authors:
  - anoni-net
---

一位作者 6 月在個人部落格記錄，把自己的靜態網站放上 Tor 的洋蔥服務（onion service，只能透過 Tor 連線、伺服器位置受到保護的網站）。架站用的是 tor（Tor Project 的主程式）與 nginx（網頁伺服器軟體）。根據 Tor Project 的特性說明，洋蔥服務不需要固定 IP、網域，也不需要開放連接埠。tor 6 月 25 日到 10 月 7 日之間連續發布 0.4.9.11 到 0.4.9.14 四個安全更新，其中三個的修補涉及洋蔥服務，到 10 月 20 日為止最新版是 0.4.9.14。

已經在營運洋蔥服務的人要更新到最新版。網站的訪客要透過 Tor 連線，例如用 Tor Browser。

依原文與官方的設定指南，做法是在 tor 的設定檔 `torrc` 指定一個存放金鑰的目錄與要轉送的本機連接埠。重新啟動 tor 之後，目錄裡的 `hostname` 檔就是網站的 .onion 位址。網頁伺服器只在本機監聽，原文提到 Tor 本身就會加密連線，不需要另外設定 TLS（HTTPS 用的加密）。

同時經營一般網站的人要留意，靜態網站產生器會把網址寫進站內連結。原文因此另外建置一份以 .onion 位址為基準的版本，避免訪客從洋蔥服務點連結又回到一般網址。

設定指南另外建議把轉送的目標從本機的網路連接埠改成 Unix socket（同一台電腦裡程式之間交換資料的通道），避免服務洩漏到區域網路。指南也提醒，照這樣設定的洋蔥服務，任何知道位址的人都能讀取。只想讓特定的人連線時，可以設定客戶授權（client authorization），只有持有私鑰的人連得上。Onion-Location 說明頁提到，已經有 HTTPS 網站的人可以加上這個標頭，讓 Tor Browser 開啟原本的網站時在網址列提示 .onion 版本。

## 導讀觀點 {#perspective}

官方說明提到，洋蔥服務的名稱就是用來驗證連線的公鑰，所以不需要憑證機構（替網站簽發 HTTPS 憑證的機構）。連線由 Tor 從使用者端一路加密到服務端。服務只對外建立連線、可以穿過 NAT（家用與機構網路共用對外 IP 的機制），學校或辦公室這類不能開連接埠的網路也能架設。根據特性說明，連得上 Tor 網路、服務也在線上時就能連到洋蔥服務，不受 DNS 與 IP 封鎖的影響。

依官方的 Operational Security 頁，伺服器位置能否保持隱藏，要看架設的人如何維護系統。網頁伺服器可能透露自己的種類與作業系統，電腦不是一直在線也會洩漏資訊。服務運作越久，位置被找到的風險也越高。同一頁建議加裝 Vanguards（降低入口節點被追查風險的附加元件）防範進階攻擊。

設定指南也寫，要讓伺服器不透露位置「not an easy task」（並不容易），並列出 Operational Security 頁與 Riseup 的指南當參考。Riseup 的指南建議用 NTP（網路校時）自動校正伺服器時間，避免時間誤差被用來辨識伺服器。沒有架過網頁伺服器的人，設定指南提到可以試試有圖形介面、設定比較少的 OnionShare。Tor Project 的 Onionspray 則是替既有的公開網站加上洋蔥服務入口，說明文件列出它不適合純洋蔥網站，也不保護網站的位置。

用 Rust 程式語言重寫的 Arti，文件對能不能架設洋蔥服務說法不一。到 10 月 20 日為止，Arti 的專案頁寫已經實作，能力與限制頁卻寫只完成一部分、預設關閉。Onionspray 的說明也寫在 Arti 有替代方案之前仍仰賴 C 語言實作的 tor，依這幾份文件推論，正式架設時以 tor 比較穩妥。

一般網站被封鎖、但連得上 Tor 的讀者，也能讀到架在洋蔥服務上的網站。依 Operational Security 頁推論，架設需要一台能長時間開機的主機。官方範例以 Debian 為主，過程是在命令列編輯設定檔、不需要寫程式，指南有正體中文翻譯（到 10 月 20 日為止部分段落仍是英文）。

特性說明也列出，使用者登入之後網站仍然記錄得到資料。依 Operational Security 頁推論，網站內容本身透露的資訊要靠架設的人自行把關。
