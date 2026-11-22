# Bitwarden 在中國大陸的連線狀況

範圍是 Bitwarden 官方雲端服務的伺服器區域，以及 bitwarden.com 相關網址在中國大陸能不能連線。第一次整理是寫 anoni-net/news 的 Bitwarden 桌面版通行金鑰整合那篇的時候，查證日期 2026-11-21。

## 伺服器區域

- 事實：Bitwarden 官方雲端只有美國與歐盟兩個資料存放區域，沒有中國大陸、台灣、香港的區域，帳號只存在建立時選的區域
    - 照錄：「The Bitwarden cloud is available globally with data storage in both United States and European Union regions.」
    - 照錄：「Bitwarden server regions are separate, and your account or organization only exists in the region where it was first created.」
    - 來源：Server Regions，Bitwarden，<https://bitwarden.com/help/server-geographies/>
- 事實：Bitwarden 的說明頁寫伺服器只存放加密後的資料，保管庫資料存放在 Microsoft Azure 的美國或歐盟區域。這是 Bitwarden 自己的說明
    - 照錄：「Bitwarden servers are only used for storing encrypted data.」
    - 照錄：「Bitwarden processes and stores all vault data securely in the Microsoft Azure Cloud in the US or EU」
    - 來源：Data Storage，Bitwarden，<https://bitwarden.com/help/data-storage/>，查證日期 2026-11-21

## 中國大陸的連線量測

- 事實：GreatFire 對 `https://bitwarden.com` 的評級是 Mixed，近 90 天最近 4 次有結論的測試有 1 次受到干擾，最後一次測試在 2026 年 10 月 26 日，2020 年 8 月 19 日起有干擾紀錄。這是第三方的量測，量的是網址能不能連線，不等於 App 能同步
    - 照錄：「Can you open https://bitwarden.com from mainland China? Sometimes. Access is unreliable — 25% of the last 4 conclusive tests showed interference.」 <!-- docs-style-lint: disable-line -->
    - 照錄：「As of the last test on 2026-10-26, https://bitwarden.com is 25% disrupted in mainland China」
    - 照錄：「GreatFire has recorded interference with https://bitwarden.com from mainland China since 2020-08-19.」
    - 來源：GreatFire，<https://en.greatfire.org/https/bitwarden.com>，讀取日 2026-11-21
- 事實：GreatFire 對 `https://vault.bitwarden.com` 的結論是可以打開，最近 5 次有結論的測試都正常連接，最後一次測試在 2026 年 11 月 15 日。頁面說明先前的「部分受阻」判定已修正，2026 年 8 月下旬起的連線被拒絕出現在沒有其他干擾跡象的路由上，不再算作封鎖的證據
    - 照錄：「Can you open https://vault.bitwarden.com from mainland China? Yes.」
    - 照錄：「As of the last test on 2026-11-15, https://vault.bitwarden.com is not blocked in mainland China」
    - 照錄：「All 5 recent conclusive tests connected normally.」
    - 來源：GreatFire，<https://en.greatfire.org/https/vault.bitwarden.com>，讀取日 2026-11-21
- 查不到：台灣、香港連線 Bitwarden 的受阻記錄（GreatFire 只量中國大陸）。沒找到不等於沒有受阻
- 查不到：Microsoft Store 與 App Store 在中國大陸、香港、台灣是否提供 Bitwarden 桌面版
- 查不到：中國大陸的 Windows 11 對第三方通行金鑰提供者有沒有區域限制（Microsoft 文件沒有寫）
