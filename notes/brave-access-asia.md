# Brave 與 Leo 在亞洲各地的取得方式

範圍是 Brave 瀏覽器的網站、下載網址與 AI 助理 Leo 在中國大陸能不能連上，以及 Brave 在幾個亞洲 App Store 有沒有上架。第一次整理是寫 anoni-net/news 的 Brave Leo 端對端加密那篇的時候，查證日期 2026-10-20。

## 中國大陸

- 事實：GreatFire 到 2026 年 10 月 18 日的最後一次測試，`https://brave.com` 在中國大陸 100% 被封鎖，從 2017 年 5 月 13 日起就有干擾紀錄。這是第三方的量測，量的是網址能不能連線
    - 照錄：「As of the last test on 2026-10-18, https://brave.com is 100% blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://brave.com from mainland China since 2017-05-13.」
    - 來源：GreatFire，<https://en.greatfire.org/https/brave.com>
- 事實：同一個量測裡，下載與更新用的 `laptop-updates.brave.com` 最近一次有效測試也是封鎖
    - 來源：GreatFire，<https://en.greatfire.org/https/laptop-updates.brave.com>
- 事實：Leo 的後端 `ai-chat.bsg.brave.com` 沒有量測資料。OONI 公開 API 在 2026 年 7 月 20 日到 10 月 20 日之間，中國的網路連線測試（Web Connectivity）對這個主機沒有任何一筆，GreatFire 也沒有測過。Leo 在中國大陸能不能連線，查不到直接證據
    - 來源：OONI API，<https://api.ooni.org/api/v1/measurements?probe_cc=CN&test_name=web_connectivity&domain=ai-chat.bsg.brave.com&since=2026-07-20&until=2026-10-20>，查詢日 2026-10-20
- 事實：Apple 的 iTunes 查詢 API 在中國大陸的商店（`country=cn`）查不到 Brave（App ID `1052879175`）。這是 API 的查詢結果，不等於 Brave 或 Apple 公告下架。Google Play 沒有查
    - 來源：iTunes lookup API，<https://itunes.apple.com/lookup?id=1052879175&country=cn>，查詢日 2026-10-20
- 事實：Brave 的說明中心沒有寫 Leo 在中國大陸提供或不提供
    - 來源：Brave 說明中心的 258 篇英文文章全文，查詢日 2026-10-20

## 日本、韓國、香港、新加坡、台灣

- 事實：iTunes 查詢 API 在台灣、香港、日本、韓國、新加坡的商店都查得到 Brave，版本 1.96（2026-10-06）
    - 來源：iTunes lookup API，<https://itunes.apple.com/lookup?id=1052879175&country=tw>（其他地區把 `country` 換成 `hk`、`jp`、`kr`、`sg`），查詢日 2026-10-20
- 事實：Brave 的說明中心沒有限制 Leo 使用地區的條文，Leo 的介紹頁寫桌機與手機版都提供 Leo
    - 照錄：「Brave Leo is currently available in the Brave browser for desktop (macOS, Windows, and Linux) and mobile (Android and iOS).」
    - 來源：Brave Leo AI，<https://brave.com/leo/>，查詢日 2026-10-20
- 事實：brave-core 開發分支的翻譯檔有 Leo 端對端加密功能的正體中文、簡體中文、日文與韓文字串，翻譯檔在開發分支不等於正式版已經提供
    - 來源：brave-core 的 `components/resources/strings/brave_components_resources_*.xtb`，<https://github.com/brave/brave-core/tree/master/components/resources/strings>，查詢日 2026-10-20
