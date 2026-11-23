---
title: 透過短波無線電收發電子郵件的開源系統 HERMES 與 Mercury
description: 非營利組織 Rhizomatica 的 HERMES 讓沒有手機訊號與網際網路的社區透過短波無線電收發電子郵件與檔案，5 月釋出的數據機軟體 Mercury 讓整套系統全部開源。無線電訊號在接收範圍內人人都能接收，業餘頻段可否加密各國規定不同。到 11 月 23 日，台灣的業餘無線電不得使用未經主管機關核准的密語或密碼通信。
date: 2026-11-28T00:00:00+08:00
slug: hermes-hf-radio
categories:
  - civil-society
sources:
  - title: "Rhizomatica’s HERMES and Mercury Expand Open-Source HF Communications for Remote Communities While Appealing to Experimenters"
    url: https://www.ardc.net/rhizomaticas-hermes-and-mercury-expand-open-source-hf-communications-for-remote-communities-while-appealing-to-experimenters/
    publisher: ARDC
    date: 2026-11-06
  - title: "This Digital Radio Gets Messages to the World’s Remotest Locations"
    url: https://spectrum.ieee.org/hermes-shortwave-radio-digital-data
    publisher: IEEE Spectrum
    date: 2026-09-21
  - title: Mercury — The Open-Source HF Modem
    url: https://mercury.hermes.radio/
    publisher: Rhizomatica
  - title: Rhizomatica/mercury
    url: https://github.com/Rhizomatica/mercury
    publisher: GitHub
  - title: Introduction
    url: https://rhizomatica.github.io/hermes-documentation/manual_en_complete/node22.html
    publisher: HERMES 手冊
  - title: "Further and Safer: Reviving HF Radio in the Digital Age"
    url: https://pitg.gitlab.io/news/techdive/2025/07/19/hermes-hf-radio-communication.html
    publisher: Public Interest Technology Group
    date: 2025-07-19
  - title: The First Social Network
    url: https://www.newyorker.com/magazine/2026/10/19/the-first-social-network
    publisher: The New Yorker
    date: 2026-10-12
  - title: 業餘無線電人員及電臺管理辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060145
    publisher: 全國法規資料庫
authors:
  - anoni-net
---

在沒有手機訊號與網際網路的地方，短波（HF）無線電可以把訊號送到幾百公里外。推動偏遠社區通訊的非營利組織 Rhizomatica 開發了 HERMES，讓沒有太多無線電與技術經驗的人也能透過短波收發訊息、電子郵件與檔案。Rhizomatica 在 5 月釋出開源的數據機軟體 Mercury（把資料轉成無線電能傳送的訊號）。依補助 HERMES 的業餘無線電基金會 ARDC 11 月 6 日刊出的介紹，Mercury 取代了每台電台都要付授權費的專有數據機 VARA，整套 HERMES 從此全部開源。

短波訊號經大氣上層的電離層反射，能連到難以架設地面基礎設施的地方。Rhizomatica 的創辦人在 IEEE Spectrum 的訪談提到，他們用輸出約 20 瓦的小型電台，兩台之間大致能穩定連上 400 到 600 公里。短波的限制是速度，同一篇報導裡提到，一般短波電台的數位傳輸速率只有每秒幾百位元。

創辦人在公共利益技術小組（Public Interest Technology Group）網站的一篇文章寫到，HERMES 會先壓縮資料，再用 UUCP 這種早期、能容忍連線中斷的協定傳遞郵件。依專案手冊，有網際網路的地方通常設一座閘道站（短波網路與網際網路的交接點），沒有其他通訊方式的社區各設一座遠端站。

HERMES 最大的一次部署有近 90 台電台，ARDC 的介紹裡提到部分站點要步行或搭船好幾天才能抵達。Rhizomatica 跟在地夥伴合作，把訓練集中在一小群社區成員身上，目標是讓社區自行安裝、操作與維護。創辦人在訪談裡提到，一項試辦計畫在 10 或 11 艘漁船上裝了 HERMES，其中一艘在離岸 100 或 200 公里處故障。他說船員用 HERMES 傳出 GPS 位置與求救訊號，人和船都獲救。

依 ARDC 的介紹，Mercury 也能脫離 HERMES 單獨使用，業餘無線電操作者可以把它接上自己的電台。已經有操作者用它收發電子郵件，也回報錯誤、貢獻修改。

## 導讀觀點 {#perspective}

無線電訊號在接收範圍內，任何有接收機的人都能接收，而短波的接收範圍可達數百公里。《紐約客》10 月報導過鄉間透過 AM 廣播電台互傳私人訊息的傳統，因為廣播的訊息人人都能聽到，訊息常用含糊的措辭寫成。

創辦人在公共利益技術小組的文章主張，短波很難判斷訊號從哪裡發出，更難知道誰在接收。他在 IEEE Spectrum 的訪談解釋，各國對業餘無線電加密的規定不同，所以 HERMES 的加密可以開也可以關。內建加密是因為部分合作夥伴身處非常敏感的地區，不想送出容易被截收、被用來對付自己的資訊。不過訊號本身仍然任何人都能錄下，從 Mercury 的原始碼公開這點推想，錄下的人用同一套軟體原則上就能還原沒有加密的資料。

台灣的業餘無線電由國家通訊傳播委員會 2020 年訂定的《業餘無線電人員及電臺管理辦法》規範。到 11 月 23 日，辦法規定業餘無線電人員操作業餘電臺時，不得使用未經主管機關核准的密語或密碼通信。依這條規定，在台灣的業餘頻段使用 HERMES 時，加密功能沒有取得核准就不能開啟。

能上網的讀者不需要這套系統，已經有業餘無線電執照、想試短波數據通訊的人，可以從 Mercury 開始。Mercury 的原始碼放在 GitHub，專案頁列出支援 Linux（含 Raspberry Pi）與 Windows，到 11 月 23 日最新的版本是 11 月 21 日釋出的 v1.9.25。在台灣的業餘頻段試用時，送出的內容要當成任何人都能接收的公開訊息。
