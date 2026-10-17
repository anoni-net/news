# Signal 在中國大陸的連線狀況

範圍是 Signal 的網站與 App 在中國大陸能不能直接連上。第一次整理是寫 anoni-net/news 的 Signal 備份與 Android 密碼管理器搬移那篇的時候，查證日期 2026-10-18。

## 網站

- 事實：GreatFire 到 2026 年 10 月 11 日的最後一次測試，`https://signal.org` 在中國大陸 100% 被封鎖，從 2017 年 7 月 2 日起就有干擾紀錄。`support.signal.org` 與 `updates.signal.org` 在同一頁也列為封鎖。這是第三方的量測，量的是網址能不能連線，不是 App 的訊息連線
    - 照錄：「As of the last test on 2026-10-11, https://signal.org is 100% blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://signal.org from mainland China since 2017-07-02.」
    - 來源：GreatFire，<https://en.greatfire.org/https/signal.org>

## App 的連線

- 事實：OONI 2021 年的分析寫到，Signal App 在 2021 年 4 月到 9 月間於中國等地遭到封鎖
    - 照錄：「OONI data analysis suggests that the Signal Private Messenger app has been blocked over the last months in Iran, China, Cuba, and Uzbekistan.」
    - 來源：How countries attempt to block Signal Private Messenger App around the world，OONI，<https://ooni.org/post/2021-how-signal-private-messenger-blocked-around-the-world/>，2021-10-21
- 事實：OONI 公開 API 的彙總，2026 年 7 月 18 日到 10 月 17 日在中國的 Signal 測試共 2847 筆，其中 2769 筆標為異常（anomaly），確認封鎖（confirmed）為 0 筆。異常不等於確認封鎖，引用時不要寫成「已確認封鎖」
    - 來源：OONI API，<https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=signal&since=2026-07-18&until=2026-10-18>，查詢日 2026-10-18

## 說明文件的語言

- 事實：Signal 支援中心的語系有 `zh-tw`，沒有 `zh-cn`
    - 來源：Signal 支援中心的語系清單 <https://support.signal.org/api/v2/help_center/locales.json>，查詢日 2026-10-18
