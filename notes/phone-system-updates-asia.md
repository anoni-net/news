# 手機系統更新的官方說明

範圍是 Apple 與 Google 在台灣、中國大陸的中文說明頁，對手機自動更新與安全性修補寫了什麼。第一次整理是寫 anoni-net/news 的導讀歷史 11-02（1988 年的網際網路蠕蟲）的時候，查證日期 2026-11-01。Apple 與 Google 的英文版說明頁沒有取得副本。2026-11-08 寫 Sekoia 手機水坑式攻擊那篇時，補上 Apple 封閉模式與 Android 進階保護在中國大陸的說明。

## 台灣

- 事實：Apple 的台灣說明頁把持續更新軟體列為維護裝置安全最重要的措施之一，並說明「自動安裝」會在 iPhone 充電且連接 Wi-Fi 時於夜間下載並安裝更新，安裝前會通知。設定路徑是「設定」、「一般」、「軟體更新」、「自動更新」
    - 照錄：「為維護你的 Apple 產品安全性，持續將軟體更新至最新版本，是你可以採取的最重要措施之一。」
    - 照錄：「自動安裝：有可用的更新時，iPhone 會在充電且連接 Wi-Fi 的情況下，於夜間下載並安裝更新。在 iPhone 安裝更新項目之前，你會收到通知。」
    - 來源：更新 iPhone 或 iPad，Apple 支援（台灣），<https://support.apple.com/zh-tw/118575>，頁面的發佈日期 2026-09-24
- 事實：Google 的 Android 說明頁（正體中文）寫大部分系統更新與安全性修補程式會自動安裝，更新時間依裝置、製造商與電信業者而不同，舊款裝置可能無法執行較新的 Android 版本。這是 Google 的通用說明，頁面寫 Pixel 以外的 Android 裝置要向製造商或電信業者查詢更新時間
    - 照錄：「大部分的系統更新和安全性修補程式都會自動安裝。」
    - 照錄：「更新時間表會依裝置、製造商和行動電信業者而有所不同。」
    - 照錄：「舊款裝置可能無法執行較新的 Android 版本。」
    - 來源：檢查及更新 Android 版本，Android 說明，<https://support.google.com/android/answer/7680439?hl=zh-Hant>，頁面沒有日期
- 查不到：台灣要求民眾開啟自動更新的規定

## 中國大陸

- 事實：Apple 的中國說明頁內容跟台灣版相同，同樣把及時更新軟體列為最重要的措施之一，也有「自动安装」的說明
    - 照錄：「要让你的 Apple 产品保持安全性，及时更新软件是你可以采取的一项最重要举措。」
    - 照錄：「自动安装：当有可用的更新后，iPhone 会在夜间下载并安装更新，前提是设备处于充电状态且已接入无线局域网。」
    - 來源：更新你的 iPhone 或 iPad，官方 Apple 支持（中国），<https://support.apple.com/zh-cn/118575>，頁面的發布日期 2026-09-22
- 事實：Google 的 Android 說明頁有簡體中文版，內容跟正體版相同
    - 照錄：「大部分系统更新和安全补丁都会自动安装。」
    - 照錄：「更新时间安排因设备、制造商和移动运营商而异。」
    - 照錄：「旧款设备不一定能运行较新的 Android 版本。」
    - 來源：查看和更新 Android 版本，Android 帮助，<https://support.google.com/android/answer/7680439?hl=zh-Hans>，頁面沒有日期
- Google Play 在中國大陸的連線狀況見 `google-services-mainland-china.md`「Google Play」，那是第三方量測，沒有寫到系統更新
- 查不到：中國大陸銷售的 Android 手機如何取得系統更新的官方說明，以及手機停止收到安全性更新之後的官方建議
- 事實：Apple 的中國說明頁有「锁定模式」（英文 Lockdown Mode，台灣譯「封閉模式」），內容跟英文頁一致，頁面沒有任何地區限制的說明（搜尋「中国大陆」、「不适用」、「不可用」沒有結果）
    - 照錄：「“锁定模式”是一项可选的极端保护模式，专为极少数个人用户设计」
    - 來源：关于“锁定模式”，官方 Apple 支持（中国），<https://support.apple.com/zh-cn/105120>，頁面日期 2026-09-18。台灣版：關於「封閉模式」，<https://support.apple.com/zh-tw/105120>，頁面日期 2026-09-18，沒有逐字比對
    - 查證日期：2026-11-08
    - 查不到：中國大陸銷售的 iPhone 上封閉模式實際能否使用的官方聲明，頁面只是沒有寫限制
- 查不到：Android 進階保護（Advanced Protection）在中國大陸銷售的手機上能否使用的官方說明。Google 的英文說明頁（Improve device security with Advanced Protection for Android，<https://support.google.com/android/answer/16339980?hl=en>，沒有日期）沒有地區限制的條目。不要寫成「不能用」，Google Play 的連線狀況見 `google-services-mainland-china.md`（2026-11-08）
- 查不到：中國 CNVD 對 CVE-2025-43529、CVE-2026-3910 的條目。站內搜索需要登入或 JavaScript，直接查詢回傳空白，不等於沒有。來源：<https://www.cnvd.org.cn/>
