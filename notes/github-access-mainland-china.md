# GitHub 在中國大陸的連線狀況

範圍是從中國大陸連到 GitHub 下載軟體或更新清單的狀況。許多開源軟體只在 GitHub 發布安裝檔，自動更新的清單也放在 `raw.githubusercontent.com`。第一次整理是寫 anoni-net/news 的 Compositor 那篇的時候，查證日期 2026-10-12。

## 量測

- 事實：長期量測防火長城的 GreatFire，到 2026-10-11 的最後一次測試，對 `https://github.com` 最近 90 天內 56 次有結論的測試中，64% 受到干擾。這是第三方的量測，測的是主機名稱，不是特定專案的下載路徑
    - 照錄：「Access is unreliable — 64% of the last 56 conclusive tests showed interference.」 <!-- docs-style-lint: disable-line -->
    - 來源：Is https://github.com blocked in mainland China? — GreatFire，<https://en.greatfire.org/https/github.com> <!-- docs-style-lint: disable-line -->
- 事實：GreatFire 到 2026-10-08 的最後一次測試，對 `https://raw.githubusercontent.com` 最近 4 次有結論的測試全部受到干擾，樣本數少
    - 照錄：「Access is unreliable — 100% of the last 4 conclusive tests showed interference.」 <!-- docs-style-lint: disable-line -->
    - 來源：Is https://raw.githubusercontent.com blocked in mainland China? — GreatFire，<https://en.greatfire.org/https/raw.githubusercontent.com> <!-- docs-style-lint: disable-line -->
- 兩頁都寫明「Each verdict covers the last 90 days of tests」。來源網址依 GreatFire 的網址格式與頁面標題對應，副本只存頁面文字
- 查不到：GitHub Releases 下載路徑（`objects.githubusercontent.com` 等）的量測，以及 GitHub 官方對中國大陸連線的說明
