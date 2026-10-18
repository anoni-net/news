# 加密郵件服務在亞洲的連線與封鎖

範圍是 Tuta、Proton Mail 這類加密郵件服務在亞洲各地能不能連上、有沒有封鎖命令，以及加密通訊 App 的封鎖紀錄。第一次整理是寫 anoni-net/news 的 Tuta 與 Nextcloud 整合那篇的時候，查證日期 2026-10-18。

量測資料都是第三方的測試結果，量測者與網路環境不一，不是官方的封鎖名單。OONI 的異常（anomaly）只代表結果與預期不符，確認（confirmed）才是已確認的封鎖指紋。

## 中國大陸

- 事實：GreatFire 到 2026 年 10 月 11 日的最後一次測試，`https://tuta.com` 在最近 17 次有結論的測試中 59% 受到干擾，GreatFire 判定為間歇性，從 2024 年 2 月 13 日起有干擾紀錄
    - 照錄：「As of the last test on 2026-10-11, https://tuta.com is 59% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 來源：GreatFire，<https://en.greatfire.org/https/tuta.com>
- 事實：Tuta 網頁版的主機 `https://app.tuta.com` 到 2026 年 10 月 2 日的測試 100% 受到干擾，但只有 2 次有結論的測試，樣本很少
    - 照錄：「As of the last test on 2026-10-02, https://app.tuta.com is 100% disrupted in mainland China」
    - 來源：GreatFire，<https://en.greatfire.org/https/app.tuta.com>
- 事實：`https://nextcloud.com` 到 2026 年 9 月 23 日的測試 100% 受到干擾，但只有 1 次有結論的測試，從 2017 年 12 月 6 日起有干擾紀錄。`apps.nextcloud.com` 還沒有測試紀錄
    - 照錄：「As of the last test on 2026-09-23, https://nextcloud.com is 100% disrupted in mainland China」
    - 來源：GreatFire，<https://en.greatfire.org/https/nextcloud.com>
- 事實：OONI 2026 年 7 月 18 日到 10 月 18 日在中國大陸對 `tuta.com` 的 178 次網頁連線測試，23 次異常，確認 0 次
    - 來源：OONI API，<https://api.ooni.org/api/v1/aggregation?domain=tuta.com&test_name=web_connectivity&axis_x=probe_cc&since=2026-07-18&until=2026-10-18>，查詢日 2026-10-18

## 亞洲其他地方的 OONI 量測

- 事實：同一期間 OONI 對 `tuta.com` 的量測，亞洲各地只有伊朗有確認的封鎖指紋（462 次，異常 12，確認 5）。台灣 771 次異常 7、香港 51 次異常 2、日本 148 次異常 4、新加坡 157 次異常 0、印度 525 次異常 2，都沒有確認紀錄。伊朗的確認紀錄沒有對應的報導，也沒有逐筆檢視
    - 來源：同上的 OONI API 查詢

## 印度

- 事實：印度網路自由基金會 2023 年 5 月 10 日的文章寫到，2023 年 5 月有報導指 14 個提供端對端加密與點對點通訊的行動 App 被封鎖，封鎖命令沒有公開。這批是即時通訊 App，不是郵件服務
    - 照錄：「In May 2023, 14 mobile apps that provided end-to-end encrypted and peer-to-peer messaging services were reportedly banned.」
    - 來源：Mayday Alert: 14 mobile apps banned, no blocking order released. #WhatTheBlock，Internet Freedom Foundation，<https://internetfreedom.in/14-mobile-apps-banned/>，2023-05-10
- 事實：卡納塔克邦高等法院 2025 年 4 月 29 日命令中央政府機關採取行動封鎖 Proton Mail。MediaNama 寫到報導當時 Proton Mail 在印度仍可使用。後續是否生效，這次沒有查到原文
    - 照錄：「The Karnataka High Court on Tuesday ordered the Central government authorities to take action to block the operation of Proton Mail in India.」
    - 照錄：「As of the time this report was written, Switzerland-based Proton Mail remained active in India.」
    - 來源（二手報導）：Karnataka High Court orders blocking of Proton Mail in India，Bar & Bench，<https://www.barandbench.com/news/karnataka-high-court-orders-blocking-of-proton-mail-in-india>，2025-04-29。Karnataka HC Orders Govt to Block Privacy-Focused Proton Mail，MediaNama，<https://www.medianama.com/2025/04/223-karnataka-court-orders-encrypted-proton-mail-ban/>，2025-04-30
- 查不到：Tuta 在印度被封鎖或下架的官方或可信報導
