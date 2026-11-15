---
title: OONI Probe 的 TLS Middlebox 實驗與資料蒐集問卷
description: OONI 11 月 10 日公告 Probe 新增定位審查設備的 TLS Middlebox 實驗，公告發布時 App 只支援預設模式。可能推估出使用者所在城市的進階模式只在命令列版本提供，需自行選擇加入。OONI 同時開放問卷到 12 月 10 日，詢問使用者能否接受蒐集更多地理與網路資料。沒有執行 Probe、也不用 OONI 資料的讀者不受影響。
date: 2026-11-20T00:00:00+08:00
slug: ooni-tls-middlebox
categories:
  - censorship
sources:
  - title: New OONI Probe TLS Middlebox Experiment
    url: https://ooni.org/post/2026-ooni-probe-tls-middlebox-experiment/
    publisher: OONI
    date: 2026-11-10
  - title: "Survey: Collecting Additional Geographic and Network-Level Data with OONI Probe"
    url: https://ooni.org/post/2026-tls-middlebox-survey/
    publisher: OONI
    date: 2026-11-10
  - title: OONI Data Policy
    url: https://ooni.org/about/data-policy/
    publisher: OONI
    date: 2026-10-22
  - title: "Risks: Things you should know before running OONI Probe"
    url: https://ooni.org/about/risks/
    publisher: OONI
  - title: TLS middlebox
    url: https://github.com/ooni/spec/blob/master/nettests/ts-037-tlsmiddlebox.md
    publisher: OONI
    date: 2026-10-22
  - title: Frequently Asked Questions (FAQ)
    url: https://ooni.org/support/faq/
    publisher: OONI
watch:
  - date: 2026-12-15
    note: OONI 是否公布 TLS Middlebox 問卷的結果，App 是否加入進階模式
authors:
  - anoni-net
---

OONI 11 月 10 日在部落格公告，OONI Probe 新增一項 TLS Middlebox 實驗，用來找出攔截加密連線（TLS）的審查設備位在網路路徑上的哪個位置。OONI Probe 是量測網站封鎖的軟體，任何人都可以在自己的網路上執行，量測結果公開成開放資料。實驗已放進命令列版本（在終端機輸入指令操作的版本）v3.31.0，以及手機與桌面 App 的 v6.3.0。公告發布時 App 只支援預設模式，蒐集較多資料的進階模式只有命令列版本提供，而且只開放使用者選擇加入。

OONI 同一天發布一份問卷，詢問使用者能否接受 OONI 蒐集更多地理與網路層級的資料，以及這些資料對自己有多少用處。實驗公告提到，OONI 想在把進階模式加進 App 之前先收集社群的意見，App 是全球多數 Probe 使用者使用的版本。問卷開放到 12 月 10 日，問卷公告也歡迎讀者轉給其他 Probe 使用者，以及在工作中使用 OONI 量測資料的人。沒有執行 Probe、也不用 OONI 資料的讀者不必做任何事。

中間設備（middlebox）是位在使用者與網站之間、會檢查或干擾流量的網路設備。OONI 的測試規格寫到，實驗偵測的是依 SNI（建立 TLS 加密連線時以明文送出的網站名稱）攔截連線的設備。根據實驗公告的介紹，實驗出自一項研究過境審查的計畫。過境審查指流量的起點與終點都不在某個網路，經過那個網路時卻被攔下。

公告描述的步驟是先用 traceroute（列出封包沿途經過哪些路由器的工具）畫出 Probe 到目標伺服器的路徑。接著向同一台伺服器分別送出對照用網域與被審查網域的請求，讓請求在路徑上的不同位置失效。OONI 藉此判斷審查從哪一點開始，找出審查設備的網路位置。這些資料也可以幫助判斷審查設備部署在靠近使用者的地方，還是在其他網路、甚至其他國家。

預設模式對路徑上的每個路由器記錄三項，分別是 IP 位址對應的國家、所屬的 AS（自治系統，網際網路上由同一個業者或機構管理的一組網路）與 AS 的組織名稱。公告的評估是，預設模式沒有帶來其他 Probe 測試與 OONI 風險說明以外的新風險，第三方只憑路由器的國家與 AS 無法做出識別使用者的分析。代價是用處有限，審查設備要位在某個國家或網路的深處，才能確認它在那裡。

進階模式另外記錄每個路由器的 IP 位址，以及封包往返每個路由器所需的時間（RTT）。公告寫到使用者因此承擔比現有 Probe 測試更高的風險。第三方可能用路由器的時間與位置三角定位出執行 Probe 的城市，也可能從路徑反推使用者所在的 /24 網段（前三組數字相同、共 256 個位址的 IP 區段）。最壞的情況是執行當下那個網段只有一個使用中的 IP 位址，使用者的 IP 位址也就可能被找出來。

公告也描述了較實際的情境，第三方可以推估出使用者所在的城市與網路，但很難認出特定的人。OONI 的理由是同一網路有許多使用中的 IP 位址，同一城市也有許多人執行這項測試。基於這些風險，進階模式只開放選擇加入。換來的好處是審查設備落在兩個國家或兩個網路的交界時也能定位，還能以城市為單位量測審查，公告提到城市層級的資料是 OONI 社群長期的要求。

## 導讀觀點 {#perspective}

OONI 的資料政策寫到，OONI 不以蒐集使用者的 IP 位址為目標，也會採取措施從量測資料庫移除。進階模式公開的路由器 IP 位址與往返時間，是 OONI 想取得的研究資料，也是第三方用來反推使用者所在地的資料。本文的判斷是，研究價值與曝光程度無法分開調整。

資料政策的另一條原則是送到伺服器的量測都會公開，除非使用者安全有疑慮，OONI 原則上不刪除量測。本文的推論是，選擇加入進階模式的量測會長期留在任何人都能下載的資料裡，日後仍可以用來推估城市與網段。

資料政策同樣列出，送出的每筆量測都會附上使用者的國家代碼與網路的 ASN（AS 的編號），這兩項無法單獨退出。執行 Probe 本身也有風險，OONI 的常見問題寫到 Probe 不是隱私工具，監控網路活動的人（例如政府、網路業者、雇主）可能看到你在執行它。風險說明頁則寫到，執行 Probe 的潛在風險取決於使用者的威脅模型（自己可能面對誰、對方有什麼能力）與所在國家的法規。

依 11 月 10 日的公告，App 還沒有進階模式，用 App 執行 Probe 的人不必為它做任何設定。對 OONI 蒐集更多資料有意見的 Probe 使用者，以及工作中會用到 OONI 資料的人，可以在 12 月 10 日前填寫問卷。問卷架在 Google 表單上，連結在原文清單的問卷公告裡，公告請讀者花幾分鐘填寫。

在執行 Probe 本身就可能引起注意的環境，可以照風險說明頁在 App 裡選擇要執行哪些測試。資料政策也提到，App 的設定裡可以選擇不送出量測。不送出量測可以讓結果不公開，但本文依常見問題推論，這兩種做法都改變不了監控網路的人看得到有人在執行 Probe。命令列版本的使用者考慮開啟進階模式時，代價是所在城市與網段可能被推估出來，而且量測公開後原則上不會刪除。
