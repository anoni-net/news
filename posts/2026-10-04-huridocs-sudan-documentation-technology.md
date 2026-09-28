---
title: 戰時人權紀錄與科技工具的取捨
description: HURIDOCS 整理蘇丹戰時人權紀錄的專家會議。在高風險環境做紀錄的團體，引進新工具前要評估成本是否值得，以及資料能否與合作夥伴互通，一般使用者不需要調整設定。
date: 2026-10-04T07:05:00+08:00
slug: huridocs-sudan-documentation-technology
sources:
  - title: "What wartime documentation demands of technology: Lessons from Sudan"
    url: https://huridocs.org/2026/09/what-wartime-documentation-demands-of-technology-lessons-from-sudan/
    publisher: HURIDOCS
    date: 2026-09-15
  - title: Uwazi
    url: https://huridocs.org/technology/uwazi/
    publisher: HURIDOCS
  - title: huridocs/uwazi
    url: https://github.com/huridocs/uwazi
    publisher: GitHub
    date: 2026-09-28
  - title: "Rising repression meets global resistance: Internet shutdowns in 2025"
    url: https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf
    publisher: Access Now
    date: 2026-03-31
regions:
  - SD
authors:
  - anoni-net
---

協助人權組織管理紀錄的 HURIDOCS 在 9 月 15 日發表文章，整理 9 月在奈洛比舉行的專家會議，主題是蘇丹戰時的人權紀錄。當地紀錄者面對流離失所、安全威脅、時斷時續的網路與裝置不足。文中的建議適用於在戰爭與高風險環境做人權紀錄的團體，一般使用者不需要調整設定。

會議討論資訊如何從紀錄者傳到研究者，之後可能再交給檢察官。紀錄可能用於刑事追訴時（例如國際刑事法院），作者認為最糟的結果是多年後才發現紀錄不能使用，因為當初沒有完全符合可預見的證據標準或保管鏈（chain of custody，證據每次經手的紀錄）的要求。

作者列出科技能協助的事，包括離線且安全地蒐集資訊、保存出處紀錄（provenance），以及連結不同系統裡的資料。但每個新工具都要花時間學習，需要訓練、裝置、網路與維護，還可能造成對廠商的依賴或新的安全問題。作者的評估標準是引進科技的成本是否值得它帶來的效益。

作者認為延續性是需要更多關注的挑戰之一，比創新更值得留意。延續性是讓三種知識能夠銜接，包括人權運動的經驗、紀錄者對自身處境的了解，以及日後可能使用資料的機構所需的條件。

## 導讀觀點 {#perspective}

依數位權利組織 Access Now 的統計，2025 年蘇丹在內戰期間斷網三次，其中一次在 7 月的考試期間。全球最多的是緬甸 95 次（含跨境斷網），其次是印度 65 次、巴基斯坦 20 次。在這些地方，需要一直連網的工具斷網時就無法使用。

出處紀錄與保管鏈在技術上，是替每份檔案記下來源、取得時間與經手的人。取得時先計算檔案的雜湊值（依內容產生的指紋），日後重算比對就能確認內容沒有被改過。

作者把互通性（interoperability）視為人權工作的基礎設施，目標不是建一個所有人共用的大系統。技術上靠各系統都能匯出、匯入共同的格式，資料才能在組織之間移動。

HURIDOCS 維護的 Uwazi 是用瀏覽器操作的人權紀錄資料庫，以 MIT 授權（允許自由使用與修改）開源，9 月 28 日仍有新版本。它用操作紀錄（activity log）記下每次變更，資料可以匯出成 CSV 表格。Uwazi 可以免費自行架設，需要 Elasticsearch（全文搜尋引擎）等元件與至少 4 GB 記憶體，也可以用 HURIDOCS 的代管服務。

評估工具時，可以逐項檢查學習與維護要多少人力、能否與夥伴交換資料、能否保存出處紀錄，以及斷網時能否繼續記錄。想試 Uwazi 可以先照官方頁的說明登入 demo。介面內建 11 種語言，包括阿拉伯文但沒有中文，需要中文介面可以自行翻譯。
