# Tor 在中國大陸、台灣與香港的連線狀況

範圍是 Tor 網路在中國大陸、台灣與香港能不能連上，以及 Tor Project 官方對中國大陸使用者的連線建議。洋蔥服務要先連得上 Tor 網路才能存取。第一次整理是寫 anoni-net/news 的 Tor 洋蔥服務靜態網站那篇的時候，查證日期 2026-10-20。

## Tor Project 的官方建議

- 事實：Tor Project 的支援頁寫到，部分國家的網路業者或國家防火牆會封鎖直接連上 Tor 網路。中國大陸的建議是先讓 Tor Browser 的連線輔助（Connection Assist）自動嘗試橋接或 Snowflake，不行再改用 WebTunnel 橋接，其次是 Snowflake 與 meek（meek 頻寬有限、速度較慢）。這份頁面寫的是連上 Tor 網路的方法，沒有寫洋蔥服務在中國大陸能否存取
    - 照錄：「In some countries, Internet service providers or national firewalls block direct access to the Tor network.」
    - 照錄：「Try connecting to Tor using WebTunnel bridges. WebTunnel makes the traffic look like a regular HTTPS connection to a webpage server giving the impression that the user is simply browsing the web.」
    - 來源：How to bypass censorship and connect to Tor from different countries or regions，Tor Project，<https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/>，有正體中文與簡體中文版本，原始檔最後修改 2026-07-22

## Tor Metrics 的使用人數估計

數字是 Tor Metrics 公開的估計值，2026 年 10 月 11 日到 17 日的日平均，只含直接連線的使用者。各地經橋接連線的人數與傳輸方式不寫進筆記，地區加上工具名稱的組合容易成為偵查線索。

- 事實：直接連線的使用者，中國大陸約 1,055 人、台灣約 9,518 人、香港約 8,253 人
- 來源：Tor Metrics，<https://metrics.torproject.org/userstats-relay-country.html>，查詢日 2026-10-20

## OONI 的 Tor 測試

- 事實：OONI 公開 API 的彙總，2026 年 9 月 18 日到 10 月 18 日，中國大陸的 Tor 測試 301 筆，其中 293 筆標為異常、確認封鎖 0 筆。香港 706 筆，異常 7 筆。台灣 4,797 筆，異常 314 筆，其中 311 筆來自同一個 ASN。異常不等於確認封鎖，OONI 的 Tor 測試量的是 Tor 運作所需的伺服器能不能連上，跟洋蔥服務本身無關
    - 來源：OONI API，<https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=tor&since=2026-09-18&until=2026-10-19>（香港、台灣把 `probe_cc` 換成 `HK`、`TW`），查詢日 2026-10-20

## 法規

- 查不到：中國大陸、台灣、香港針對架設洋蔥服務的專門規範。中國大陸國際聯網的一般規定見 `vpn-and-site-blocking.md` 的 CN-1
