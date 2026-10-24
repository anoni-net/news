# 公共 DNS 解析服務在亞洲的可用性與 DNS 層停止解析的制度

範圍是使用者自行設定的公共 DNS 解析服務（Quad9、Google Public DNS 等）在亞洲幾個地方的節點與連線量測，以及以 DNS 修改解析結果來封鎖網站的制度。第一次整理是寫 anoni-net/news 的 Quad9 退出法國那篇導讀的時候，查證日期 2026-10-23，下面每一條都是這天查到的內容。

法院或行政機關命令網路業者封鎖網站的一般制度（包含台灣《著作權法》沒有封鎖條文、日本仍在檢討、印度的動態禁制令）寫在 `vpn-and-site-blocking.md`，這裡不重複。

量測資料都是第三方的測試結果，量測者與網路環境不一，不是官方的封鎖名單。OONI 的異常（anomaly）只代表結果與預期不符，確認（confirmed）才是已確認的封鎖指紋。GreatFire 的判定只看有結論的測試（見 `browser-access-mainland-china.md`）。

## 中國大陸

### CN-1　GreatFire 對 `https://dns.quad9.net` 的量測

- 事實：GreatFire 到 2026 年 10 月 22 日的最後一次測試，`https://dns.quad9.net` 最近 2 次有結論的測試中有 1 次受到干擾，判定是訪問不穩定，從 2020 年 2 月 4 日起就有干擾紀錄。樣本只有 2 次
- 照錄：「As of the last test on 2026-10-22, https://dns.quad9.net is 50% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
- 照錄：「Access is unreliable — 50% of the last 2 conclusive tests showed interference.」 <!-- docs-style-lint: disable-line -->
- 照錄：「GreatFire has recorded interference with https://dns.quad9.net from mainland China since 2020-02-04.」
- 來源：Is https://dns.quad9.net blocked in mainland China? — GreatFire，<https://en.greatfire.org/https/dns.quad9.net> <!-- docs-style-lint: disable-line -->
- 二手（第三方量測）

### CN-2　GreatFire 對加密 DNS 查詢網址 `https://dns.quad9.net/dns-query` 的量測

- 事實：`https://dns.quad9.net/dns-query` 是 Quad9 的 DNS over HTTPS 查詢網址。GreatFire 到 2026 年 9 月 3 日的最後一次測試，最近 2 次有結論的測試都受到干擾，從 2019 年 8 月 3 日起就有干擾紀錄。樣本只有 2 次，最後一次測試距查證日約兩個月
- 照錄：「As of the last test on 2026-09-03, https://dns.quad9.net/dns-query is 100% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
- 照錄：「GreatFire has recorded interference with https://dns.quad9.net/dns-query from mainland China since 2019-08-03.」
- 來源：Is https://dns.quad9.net/dns-query blocked in mainland China? — GreatFire，<https://en.greatfire.org/https/dns.quad9.net/dns-query> <!-- docs-style-lint: disable-line -->
- 二手（第三方量測）
- 同一網站的 `https://quad9.net` 在 2026 年 9 月 4 日的最後一次測試判定為可以連線（只有 1 次有結論的測試，頁面標了「Verdict revised」），`https://www.quad9.net` 在 2026 年 8 月 23 日的 1 次有結論的測試受到干擾。兩者是 Quad9 的官網，不是解析服務本身

### CN-3　OONI 對 `dns.quad9.net` 的網頁連線測試

- 事實：OONI 公開 API 的彙總，2026 年 7 月 23 日到 10 月 23 日，中國大陸對 `dns.quad9.net` 的網路連線測試（Web Connectivity）共 239 次，224 次標為異常，確認封鎖 0 次，測試失敗 14 次，正常 1 次。測試來自 11 個 ASN。測的網址是 `https://dns.quad9.net`（7 次）與 DNS over HTTPS 查詢網址 `https://dns.quad9.net/dns-query`（232 次，含帶查詢參數的網址）。異常不等於確認封鎖，這是能不能連上 Quad9 本身的量測結果，不能拿來判斷封鎖的手法，也不是一般 DNS 查詢的結果
- 來源：OONI API，<https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=web_connectivity&domain=dns.quad9.net&since=2026-07-23&until=2026-10-23>（依網址與 ASN 分組時加 `axis_x=input`、`axis_x=probe_asn`），查詢日 2026-10-23
- 一手（OONI 的量測資料）

### CN-4　9.9.9.9 的一般 DNS 查詢：查不到可用的量測結果

- 事實：GreatFire 量測的是網址能不能連線，沒有量測向 9.9.9.9 發出的一般 DNS 查詢。OONI 的 DNS 檢查實驗（dnscheck）在同一期間對 `dot://9.9.9.9:853/` 等加密 DNS 位址有量測，但公開 API 的彙總把中國大陸的每一筆都標成失敗、沒有異常判定，連中國大陸本地的 `dot://dns.alidns.com/dns-query` 也一樣，所以這些數字不能拿來判斷有沒有受到干擾。查到的資料無法判斷 9.9.9.9 的一般 DNS 查詢在中國大陸是否受到干擾
- 來源：OONI API，<https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=dnscheck&since=2026-07-23&until=2026-10-23&axis_x=input>，查詢日 2026-10-23
- 引用時寫成「沒有找到可以判斷的量測結果」，不寫成「沒有受到干擾」

### CN-5　Quad9 在中國大陸、香港與澳門沒有節點

- 事實：Quad9 節點頁載入的節點資料（191 筆）沒有中國大陸、香港與澳門的條目。台北、東京、大阪、新加坡、首爾等地有節點，狀態是 ONLINE
- 來源：Locations，Quad9，<https://quad9.net/service/locations/>，節點資料 <https://quad9.net/images/locations/data.csv>，查詢日 2026-10-23
- 一手（服務商的資料）
- Quad9 的隱私頁寫到，退出某個國家不代表該國使用者無法使用服務（除非該國自己阻止），服務會由鄰近國家的節點提供
- 照錄：「This does not mean users within that country would be prevented from using the Quad9 service (unless the country itself prevented them); the service will operate from locations in nearby countries.」
- 來源：Privacy，Quad9，<https://quad9.net/service/privacy/>
- 引用節點資料時寫明這只是伺服器的所在地，沒有節點不代表無法使用。隱私頁這一句寫的是 Quad9 退出某個國家的情況，套用到本來就沒有節點的香港、澳門時，寫成「依隱私頁的說明」，不寫成 Quad9 對當地的保證

## 台灣

### TW-1　DNS RPZ 自律機制的停止解析程序，不涵蓋公共解析服務

- 事實：數位發展部 2025 年 1 月 9 日函訂定的參考程序，由台灣網路資訊中心（TWNIC）協調自願參與的網際網路接取服務提供者，修改 DNS 解析結果來停止解析特定網域，要依法院判決、裁定或處分機關依法處分才能啟動。程序寫明停止解析不包含禁止使用者透過公共解析器或 VPN 瀏覽，說明欄舉的公共解析器例子是 OpenDNS、Cloudflare DNS 與 Quad9 DNS，並寫明技術上無法禁止。適用範圍是參與的接取業者自己的解析服務，不涵蓋使用者自行設定的公共解析服務
- 照錄：「DNS RPZ 自律機制須依法院判決、裁定或處分機關依法處分，始得啟動。」
- 照錄：「透過 DNS RPZ 自律機制停止解析，不含以下技術：」、「4.禁止使用者透過公共解析器、虛擬私人網路（VPN）或其他特殊技術瀏覽違法網域名稱或網站。」
- 照錄（說明欄）：「第 3 款第 4 目所稱之公共解析器（例如 OpenDNS、Cloudflare DNS 及 Quad9 DNS 等）係由用戶自行設定替代 IASP 之網域名稱解析系統，提供網域名稱解析之服務」
- 照錄（說明欄）：「DNS RPZ 自律機制技術上並無法禁止透過該等方式瀏覽違法網域名稱」
- 文件：運用 DNS RPZ 自律機制停止解析違法網站處理參考程序，數位發展部 114 年 1 月 9 日字數位資源字第 1136003057 號函訂定（行政院 114 年 7 月 7 日院臺科字第 1141004128 號函核復同意）
- 網址：<https://www-api.moda.gov.tw/File/Get/moda/zh-tw/Qv1tZuiNEVfsLIl>
- 一手（行政規則）
- 處分的依據在文件裡舉的例子是《詐欺犯罪危害防制條例》與《兒童及少年性剝削防制條例》，這份程序不是針對著作權。《著作權法》沒有封鎖條文，見 `vpn-and-site-blocking.md` 的 TW-1
- TWNIC 的 DNS RPZ 說明頁與透明度報告需要 JavaScript，沒有取得內容

## 印度

### IN-1　Google Public DNS 依命令封鎖的地區包含印度

- 事實：Google Public DNS 的 Blocking Behavior 頁列出它依法院與政府命令封鎖網域解析的司法管轄區，共五個：比利時、法國、印度、義大利、葡萄牙。被封鎖的網域回覆 REFUSED。頁面內嵌的摘要寫法國是唯一一個，與列表不一致，以列表為準
- 照錄：「For these jurisdictions, Google Public DNS will comply with enforceable court and governmental orders to block DNS resolution of all names under specified domains.」
- 照錄：列表「Belgium (BE)」、「France (FR)」、「India (IN)」、「Italy (IT)」、「Portugal (PT)」
- 來源：Blocking Behavior，Google for Developers，<https://developers.google.com/speed/public-dns/blocking>，頁面標示最後更新 2025-12-02
- 一手（服務商的說明頁）
- 頁面沒有列出印度的命令是哪些法院或機關發出、依據哪條法律。印度法院命令封鎖盜版網站的判決見 `vpn-and-site-blocking.md` 的 IN-5

## 未能取得或需要再確認的項目

- 9.9.9.9 一般 DNS 查詢在中國大陸的量測：見 CN-4
- 香港、澳門有沒有以 DNS 停止解析為名的制度：沒有找到官方制度文件
- 南韓的 DNS 層封鎖：本次沒有查
