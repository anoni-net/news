# Telegram 在亞洲各地的連線狀況與透明度數字

範圍是 Telegram 的網站在中國大陸能不能直接連上，以及 Telegram 透明度報告裡亞洲幾個地方的請求數。第一次整理是寫 anoni-net/news 的 Telegram 交給美國執法單位的使用者資料那篇的時候，查證日期 2026-10-20。

## 中國大陸的連線

- 事實：GreatFire 到 2026 年 10 月 18 日的最後一次測試，`https://telegram.org` 在中國大陸 100% 被封鎖，從 2015 年 7 月 10 日起就有干擾紀錄。`https://t.me` 也列為封鎖，`https://web.telegram.org` 大多數測試網址被封鎖。這是第三方的網址量測，量的是網址能不能連線，不是 App 的訊息連線
    - 照錄：「As of the last test on 2026-10-18, https://telegram.org is 100% blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://telegram.org from mainland China since 2015-07-10.」
    - 來源：GreatFire，<https://en.greatfire.org/https/telegram.org>
- 事實：OONI 公開 API 的彙總，2026 年 7 月 18 日到 10 月 18 日在中國的 Telegram 測試共 2877 筆，其中 2819 筆標為異常（anomaly），確認封鎖（confirmed）為 0 筆。異常不等於確認封鎖，引用時不要寫成「已確認封鎖」
    - 來源：OONI API，<https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=telegram&since=2026-07-18&until=2026-10-18>，查詢日 2026-10-20

## 透明度報告的取得方式

- 事實：Telegram 的透明度報告要用 Telegram 帳號向官方機器人 `@transparency` 查詢，機器人只回傳查詢帳號註冊所在國的資料，網頁上沒有公開版本
    - 照錄：「this bot only provides data for the country in which the account demanding data is registered.」
    - 來源：Crowdsourcing Telegram ‘transparency reports’ to map the network’s claimed compliance with governments around the world，Meduza，<https://meduza.io/en/feature/2024/10/23/crowdsourcing-telegram-transparency-reports-to-map-the-network-s-claimed-compliance-with-governments-around-the-world>，2024-10-23

## 亞洲各地的請求數

下面的數字來自 GitHub 上一份由使用者貼上機器人回覆彙整的眾包資料集，不是 Telegram 公開的網頁，引用時要寫明是眾包資料。數字是 Telegram 完成的調取 IP 位址或電話號碼的請求數與涉及的使用者數。

- 事實：南韓 2024 年 1 到 9 月為 0 次，2024 年 10 到 12 月為 270 次、658 位，2025 年全年為 2,101 次、5,454 位
- 事實：新加坡 2024 年全年為 4 次、4 位，2025 年第一季為 14 次、16 位，之後的期間資料集沒有
- 事實：香港、日本與中國大陸只有 2024 年 1 到 9 月的資料，都是 0 次。台灣在資料集裡沒有條目，Meduza 2024 年 10 月彙整的 2024 年 1 到 9 月表格列為 0 次
- 來源：telegram-transparency，GitHub，<https://github.com/Te-k/telegram-transparency>，最近一次提交 2026-10-05
- 查不到：台灣、香港、日本 2024 年 10 月以後的數字，新加坡 2025 年第二季以後的數字
