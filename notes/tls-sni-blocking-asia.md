# 亞洲的 TLS 與 SNI 封鎖量測

範圍是亞洲各地依 SNI（建立 TLS 連線時以明文送出的網站名稱）或 TLS 交握攔截連線的量測報告，以及審查設備位在網路的哪個位置。第一次整理是寫 anoni-net/news 的 OONI Probe TLS Middlebox 實驗那篇（2026-11-20），查證日期 2026-11-15。

量測報告都有年份，只代表當時的網路狀況，引用時寫出資料年份。

## 印度

### IN-1　OONI 與 CIS 的 TLS 封鎖報告（2020）

- 事實：OONI 與印度 Centre for Internet & Society（CIS）在 ACT Fibernet、Bharti Airtel、Reliance Jio 三家 ISP 的網路上做實驗，在 Bharti Airtel 與 Reliance Jio 都記錄到依 SNI 的封鎖。Reliance Jio 另外會依 TLS 交握涉及的網頁伺服器封鎖
    - 照錄：「We recorded SNI-based blocking on both Bharti Airtel and Reliance Jio.」
    - 照錄：「We also discovered that Reliance Jio blocks TLS traffic not just based on the SNI value, but also on the web server involved with the TLS handshake.」
- 事實：報告寫到印度的網站封鎖由政府機關依《資訊科技法》（Information Technology Act）第 69A 條與第 79 條命令 ISP 執行，政府沒有給技術規格，各家 ISP 自行決定封鎖方式。依第 69A 條發布的規則要求 ISP 對部分封鎖命令保密
    - 照錄：「State authorities draw these powers from Section 69A and Section 79 of the Information Technology (IT) Act. Since there are no technical specifications given by the government, each ISP is at the liberty to adopt their own method of blocking websites.」
    - 照錄：「regulations notified under Section 69A require ISPs to maintain confidentiality over certain website blocking orders.」
- 事實：報告引用一份以 OONI 資料研究印度一個邦的審查的研究，結論是封鎖的差異主要在 ISP 之間，不在地區之間
    - 照錄：「website blocking within the country varies primarily from ISP to ISP, rather than from region to region」
- 文件：Investigating TLS blocking in India，OONI，<https://ooni.org/post/2020-tls-blocking-india/>，2020-07-08
- 一手（OONI 與 CIS 的報告），查證日期 2026-11-15

## 台灣、日本、新加坡、香港、南韓

- 查不到 OONI 針對這幾個地方的 TLS 中間設備（middlebox）專門報告（2026-11-15）

## 待查

- 中國大陸的區域性 SNI 審查：gfw.report 的「A Wall Behind A Wall: Emerging Regional Censorship in China」（IEEE S&P 2025），<https://gfw.report/publications/sp25/en>。只讀過搜尋摘要，沒有讀全文，引用前要讀原文（2026-11-15）
- 伊朗：OONI「Measuring SNI based blocking in Iran」（2020），<https://ooni.org/post/2020-iran-sni-blocking/>。只知道標題，沒有讀內文（2026-11-15）
