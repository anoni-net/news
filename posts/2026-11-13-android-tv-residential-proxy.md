---
title: 家用 Android 電視盒的預載後門與住宅代理
description: 家中有 Android 電視盒的人可能受影響。Google 11 月初公布瓦解預載在超過 130 萬台機上盒的 XCPE 後門，裝置被用來轉送他人流量，通過認證的機型也在內。到 11 月 8 日為止，Google 沒有提供已出貨裝置的清除步驟，換機與新加坡警方的處理建議並不相同。
date: 2026-11-13T00:00:00+08:00
slug: android-tv-residential-proxy
categories:
  - security
sources:
  - title: Shutting the Door on the XCPE Botnet
    url: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/
    publisher: Google Threat Intelligence Group
    date: 2026-11-02
  - title: Check & fix Play Protect certification status
    url: https://support.google.com/android/answer/10248227
    publisher: Google
  - title: Certified - Partners | Android
    url: https://www.android.com/certified/partners/
    publisher: Google
  - title: The Internals of a Badbox Operation
    url: https://github.com/synthient/public-research/blob/main/2026/11/Videostrong/README.md
    publisher: Synthient
  - title: Google dismantles botnet secretly running on 1.3 million Android TV boxes
    url: https://arstechnica.com/google/2026/11/google-dismantles-botnet-secretly-running-on-1-3-million-android-tv-boxes/
    publisher: Ars Technica
    date: 2026-11-03
  - title: Google Takes Down Massive Android Botnet Infecting 1.3 Million Devices
    url: https://www.channelnews.com.au/google-takes-down-massive-android-botnet-infecting-1-3-million-devices/
    publisher: ChannelNews
    date: 2026-11-03
  - title: Google dismantles massive botnet hidden in Android TV boxes
    url: https://therecord.media/google-dismantles-botnet-hidden-android-tv-boxes
    publisher: The Record
    date: 2026-11-03
  - title: Cops bust botnet of 1.3M infected Android TV boxes
    url: https://www.theregister.com/a/5307045
    publisher: The Register
    date: 2026-11-02
  - title: TrendAI helps disrupt X.CPE botnet in 1.3m devices
    url: https://itbrief.com.au/story/trendai-helps-disrupt-x-cpe-botnet-in-1-3m-devices
    publisher: IT Brief Australia
    date: 2026-11-05
  - title: Advisory On The Dangers Of Non-Certified Streaming Devices
    url: https://www.police.gov.sg/media-hub/news/2025/11/20251112_advisory_on_the_dangers_of_non_certified_streaming_devices
    publisher: Singapore Police Force
    date: 2025-11-12
authors:
  - anoni-net
watch:
  - date: 2026-12-08
    note: Google 的 Android TV 認證流程與韌體完整性檢查有哪些改動、是否撤銷相關機型的認證或提供已出貨裝置的處理方式，以及 Videostrong 的法律程序與回應
---

家中的對外連線可能正經由插在電視上的 Android 電視盒被轉租給陌生人。Google 威脅情報團隊（GTIG）11 月初公布，Google 與業界夥伴在前一週瓦解 XCPE 殭屍網路（botnet，受同一方遠端控制的大量裝置），超過 130 萬台機上盒被 XCPE 後門納入其中。受害裝置絕大多數是 Android 電視盒，也有遠距醫療裝置、卡拉 OK 機與數位看板，分布遍及全球。家中有 Android 電視盒（尤其是來源不明的機型）的讀者可以先對照機型名單與認證狀態，兩者都無法單獨確認是否受害。

住宅代理（residential proxy）把付費客戶的流量轉經一般家庭的網路送出去，目的地記錄到的來源是那個家庭的 IP。依 GTIG 的分析，XCPE 載入的模組最常見的用途是住宅代理與頻寬分享，另外也有廣告詐欺模組。一台裝置最多同時裝了三種代理用的軟體開發套件（SDK）。裝置的主人既不知情，也沒有同意。

依 IT Brief 對資安業者 TrendAI 分析的報導，惡意流量經由一般家庭與辦公室的 IP 送出，攻擊者存取線上服務時就像當地的使用者。這些流量來自真實的家庭連線，可以繞過銀行、零售商用來驗證使用者的 IP 信譽與地理位置檢查。家中 IP 因此被封鎖或被追查的實例與法律責任，到 11 月 8 日為止查到的官方文件沒有寫。

依 GTIG 的說明，後門本體是套件 `x.cpe`（部分版本名為 `com.oemservice`），以系統權限預載在韌體裡。使用者解除安裝之後，重新開機就會從 `/oem/` 分割區裝回來。它會清除裝置上的使用者同意設定，關閉 Google Play Protect（Android 內建的惡意 App 防護）的 App 驗證，接著靜默下載並執行其他檔案。GTIG 在多個品牌與機型的韌體裡都找到同一套後門，時間跨越多年。

GTIG 也記錄到營運者擷取裝置的即時畫面、注入按鍵、外傳帳號與裝置資訊，以及開啟遠端命令列，指令清單裡還有探測所在網路的功能。同一份報告也提到，與受害裝置的互動絕大部分是安裝、移除與設定模組。

依 GTIG 的高度信心評估，Android 裝置代工廠 Videostrong 為了營利蓄意開發、部署並營運 XCPE 後門與殭屍網路，再把存取權賣給犯罪的附屬業者。到報導刊出時，Videostrong 沒有回覆 The Record 與 The Register 的詢問。依 Ars Technica 的報導，受害機型包含通過 Google 認證的機型。GTIG 的解釋是 Videostrong 用混淆手法鑽了測試的漏洞，在裝置首次開機之後才載入惡意程式碼。

130 萬台是 GTIG 對 XCPE 後門本身的數字。GTIG 另外估計，取下附屬業者模組的指揮控制（C2，遠端下達指令的伺服器）網域，會再切斷至少 1000 萬台受感染裝置的存取。附屬業者在 XCPE 之外還有別的散布管道，所以 1000 萬台算在 130 萬台之外。依 The Record 的報導，其中許多不是 Android 裝置。

Google 的處置包括以法律行動取下 Videostrong 與十幾個惡意程式家族使用的網域，也禁止 Videostrong 及其未來的子公司、關聯公司製造販售認證的 Android 裝置，或供應軟體給認證廠商。Google 也寫到正在改進認證 Android TV 裝置的韌體完整性檢查。到 11 月 8 日為止，GTIG 的報告與查到的其他官方說明都沒有提供已出貨裝置的清除步驟，也沒有寫是否撤銷受害機型的認證。依 The Record 的報導，Google 也沒有說明是否通知使用者或強制清除。

## 導讀觀點 {#perspective}

要查認證狀態，可以開啟 Google Play 商店的個人資料選單，再進入「設定」的「關於」。本文沒有在電視盒上實測，畫面可能與說明頁不同。依說明頁，未認證的裝置可能不安全，裝置認證與防護惡意 App 的 Play Protect 是兩件事。顯示已認證也無法排除問題，XCPE 的受害機型包含認證機型，惡意程式碼在首次開機之後才載入。

GTIG 的合作單位 Synthient 公開了 182 個在這起事件觀察到的機型名稱，清單的說明寫到，單憑機型名稱不足以確認裝置已遭入侵。Ars Technica 建議買過 MECOOL 或來源不明白牌電視盒的人對照這份清單。GTIG 的報告沒有列出使用者可以看到的徵兆，IT Brief 的報導也提到盒子可能看起來一切正常。到 11 月 8 日為止查到的資料裡，沒有一般使用者可以確認家中 IP 是否正被出租的方法。

ChannelNews 轉述的研究人員（報導沒有寫是哪一家）建議把確認感染的裝置斷線後換掉，因為 `x.cpe` 嵌在系統韌體裡，防毒軟體與原廠重設可能無法永久清除。代價是要另外花錢買新機，要先確認感染也不容易。要換機時，GTIG 建議向信譽良好的製造商購買，並指向 Android TV 網站的合作夥伴名單。連結到的認證夥伴頁頁首寫的是手機與平板，電視盒是否完整列入，到 11 月 8 日為止本文沒有查到。

新加坡警方與網路安全局 2025 年 11 月的提醒早於 GTIG 這次公布（到 11 月 8 日為止，沒有查到台灣 TWCERT/CC 與香港 HKCERT 針對 XCPE 的公告），對象是未認證的電視盒，建議立即斷網、掃描並移除可疑 App、檢查銀行等帳戶。發現惡意程式或未授權交易時要向新加坡警方報案，報案前不要重設，以免妨礙調查。該提醒也寫到，沒有發現惡意程式與未授權交易時可以繼續使用或完整重設，但它不是針對 XCPE 的建議。GTIG 寫明使用者無法移除 `x.cpe`，ChannelNews 也寫防毒軟體與原廠重設可能無法永久清除，本文推論掃描沒有發現異常不代表 `x.cpe` 不在。

依 The Record 的報導，GTIG 反制業務的主管被問到如何移除惡意程式時表示，取下網域實際上讓惡意程式不再造成危害（「effectively rendering the malware benign」）。依 Ars Technica 的評估，裝置應該可以安全使用，但 Play Protect 仍然關閉、失效的模組還裝在系統裡。GTIG 的報告提到營運者被打斷後會很快換用新的載入程式或其他變現 SDK。ChannelNews 轉述的研究人員也警告，犯罪者可能另建替代系統，受感染的裝置仍可能再遭利用。

家中 IP 也可能經由自己安裝的 App 被出租，GTIG 呼籲對「用閒置頻寬換錢」、「分享網路」的 App 格外小心，報告把它們列為非法代理網路擴張的主要管道。依 GTIG 的分析，代理業者通常只在平台政策要求時才徵求同意，到 11 月 8 日為止查到的資料裡沒有報告列出的代理業者的回應。

電視盒機型在名單上、來源不明或顯示未認證的人，第一步是中斷它的網路連線（換機與新加坡的兩種建議都從斷網開始），只需要幾分鐘。依新加坡的提醒，認為帳號可能遭入侵時要立即更改密碼並啟用多因素驗證，本文建議改用其他裝置操作。GTIG 建議確認 Play Protect 已啟用，暫時留著裝置的人可以檢查。依 Ars Technica 的報導，後門會關閉 Play Protect，來源沒有寫手動開啟之後是否會再次被關閉。

暫時還要使用的人可以把電視盒接到路由器的訪客網路，與手機、電腦分開，也要確認訪客網路有隔離區網裝置。ChannelNews 的報導寫到攻擊者可以探查同一家用網路上的其他裝置，訪客網路是本文由此做的推論。來源只提到企業的隔離，沒有評估家用訪客網路，訪客網路也擋不住營運者在盒子上擷取畫面、外傳帳號資訊與轉送流量。斷網可以停止轉送流量，但收不回可能已經外傳的帳號資訊，換新機則要付出購機費用。
