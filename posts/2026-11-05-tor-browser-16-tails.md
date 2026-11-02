---
title: Tor Browser 16.0 與 Tails 7.16
description: Tor Browser 16.0 推出桌面版與 Android 版，改以 Firefox ESR 153 為基礎。桌面版重新設計設定頁，新增預設關閉的通用視窗標題，32 位元 x86 Linux 從這一版起不再支援。Tails 7.16 把內建的 Tor Browser 更新到 16.0，Tails 7.0 或更新的版本可以自動升級。
date: 2026-11-05T00:00:00+08:00
slug: tor-browser-16-tails
categories:
  - tracking
watch:
  - date: 2026-12-05
    note: 新的線路顯示是否已進到 Tor Browser Alpha，Android 版是否出現線路顯示，通用視窗標題是否仍預設關閉
sources:
  - title: "New Release: Tor Browser 16.0"
    url: https://blog.torproject.org/new-release-tor-browser-160/
    publisher: Tor Project
    date: 2026-10-29
  - title: Tails 7.16
    url: https://tails.net/news/version_7.16/
    publisher: Tails
    date: 2026-10-30
  - title: Known issues
    url: https://tails.net/support/known_issues/
    publisher: Tails
authors:
  - anoni-net
---

Tor Project 10 月 29 日發布 Tor Browser 16.0，桌面版與 Android 版同時推出，是第一個以 Firefox ESR 153（Firefox 的長期支援版本）為基礎的穩定版。Tails（從 USB 隨身碟開機、所有連線都經過 Tor 的作業系統）隔天發布 7.16，把內建的 Tor Browser 更新到 16.0。Windows、macOS、Linux 與 Android 的使用者都在更新範圍內，只有 32 位元 x86 的 Linux 電腦從 16.0 起不再支援。

依 Tor Project 的公告，換到新的 ESR 時團隊會做每年一次的審查。這次檢查並處理了超過 270 筆 Bugzilla（Mozilla 的錯誤追蹤系統）議題，對象是 Firefox 一年來可能損害 Tor Browser 使用者隱私與安全的變更。變更紀錄裡有多項停用或隱藏的條目，例如 WebGPU（讓網頁直接使用顯示卡運算的新介面）在審查完成前停用，AI 設定面板與翻譯設定頁隱藏起來。Android 版也停用 AI 功能與 Google Lens，這些條目都只有標題，沒有說明理由。

桌面版的設定頁跟著 Firefox 6 月的改版重新設計，原本的「一般」頁拆到外觀、下載、分頁與瀏覽、無障礙、語言幾個新頁面（頁面名稱依英文公告翻譯）。連線與安全等級這些 Tor Browser 特有的頁面，改用 Firefox 的新元件重寫。公告提到，開啟後可能損害隱私或讓瀏覽器更容易被辨識指紋（網站從瀏覽器設定與裝置特徵認出同一台裝置）的設定，有的隱藏、有的加上警告。原本的偏好設定會保留，找不到的選項可以用設定頁頂端的搜尋列。

設定裡另外新增通用視窗標題（位置在 Privacy and security → Protections from third-party applications），開啟後所有視窗標題都換成「Tor Browser」。依公告的說明，瀏覽器通常把正在瀏覽的網頁標題當成視窗名稱，電腦上的其他程式與作業系統不需要特別權限就能讀取。選項預設關閉，公告寫到這次的開發週期來不及評估副作用。可能受影響的是使用螢幕閱讀器的人，以及高度自訂系統的人（例如使用少見的桌面環境或程式切換器）。

Linux 版新增 64 位元 ARM 處理器的原生支援，例如 Raspberry Pi 與安裝 Linux 的 Apple Silicon Mac。32 位元 x86 Linux 跟著 Firefox 停止支援，公告發布時每天約有 200 次更新檢查來自這個平台，2019 年高峰時約 4,000 次。

桌面版內建的使用手冊（網址列輸入 `about:manual`，或從選單 ☰ → Help → Tor Browser manual 開啟）換成新支援網站的內容，一樣可以離線閱讀，連不上 Tor 網路時也能查。Google Play 限制以 APK 發布的 App 不能超過 100 MB，Android 版的手冊因此一直無法內建、離線閱讀。Android 版的介面大量改用 Material Design 3（Google 為 Android 訂的設計規範），公告寫到後續版本還會繼續改。變更紀錄也列出 Android 版移除密碼介面、停用所有連結分享功能，以及停用匯入書籤。

依 Tails 的公告，7.16 把 Tor Browser 更新到 16.0，連帶換上新的設定頁。Tor 用戶端更新到 0.4.9.15，Thunderbird 的 OpenPGP 支援也修正了。

## 導讀觀點 {#perspective}

Tor Browser 建立在 Firefox ESR 上，每年換一次基礎版本，等於一次接收 Firefox 一年份的變更。從 16.0 的變更紀錄看，多項新功能先關掉，例如 WebGPU 標明審查完成前停用。Firefox 新的線上搜尋建議也維持關閉。本文據此推論，Firefox 使用者已經有的部分功能，Tor Browser 的使用者會比較晚用到或用不到。

通用視窗標題處理的是同一台電腦上的其他程式。Tor 網路保護的是連線經過的路徑，電腦上安裝的其他軟體不在範圍內。選項只換掉視窗標題，其他程式讀取畫面內容不在它處理的範圍內（本文的推論）。

所有視窗都叫「Tor Browser」之後，本文推論依賴視窗名稱切換視窗的人會比較難分辨，公告提到的螢幕閱讀器使用者可能就是這種情況。Tor Project 在公告裡邀請使用螢幕閱讀器或高度自訂系統的人試用，回報遇到的問題。

同一個選項已經透過 Tor Uplift Project（把 Tor Browser 的修改送回 Firefox 的計畫）進到 Firefox。依公告，熟悉進階設定的 Firefox 使用者可以在 `about:config` 把 `privacy.exposeContentTitleInWindow`（一般視窗）與 `privacy.exposeContentTitleInWindow.pbm`（私密瀏覽視窗）設為 false，效果相同。

同一篇公告也預告新的線路顯示（circuit display，顯示連線經過哪幾個中繼站的面板）即將進入 Alpha 測試版，不在 16.0 裡。新版會把網站資訊整合進面板，也能畫出多路徑線路，Android 版第一次會有線路顯示。依公告，多路徑線路用額外的中繼站把流量分成兩條路徑，在同一個出口節點（連線離開 Tor 網路、連到目的網站前的最後一個中繼站）匯合。到公告發布時，一般網站的連線已經會依網路的可用狀況隨機分配到多路徑線路，洋蔥服務（只能透過 Tor 連上的網站）還沒有。

用 Tor Browser 桌面版的人更新到 16.0 之後，可以在設定的 Privacy and security 找到通用視窗標題（選項名稱照英文公告）。依公告，開啟後其他軟體無法從視窗標題得知瀏覽紀錄。本文據此推論，擔心電腦上裝了來源不明軟體的人可以考慮開啟，但其他程式記錄按鍵或截圖時仍然保護不到。需要更完整地防範電腦上其他軟體的人，Tor Project 在公告裡推薦的是 Tails。

想照公告改用 Tails 的人，Tails 的已知問題頁到 11 月 2 日仍寫著，使用 Apple 晶片（M1、M2 等）的 Mac 與許多其他機型的 Mac 完全無法啟動 Tails。Tails 7.0 或更新的版本可以自動升級到 7.16，自動升級失敗或升級後無法啟動時改用手動升級。改成重新安裝的話，USB 隨身碟上的持久儲存區（Persistent Storage，Tails 用來保存檔案與設定的空間）會消失。還在用 32 位元 x86 Linux 的人，依公告多數可以改裝 64 位元版本，硬體或 Linux 版本太舊的除外。
