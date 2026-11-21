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

## 中國、巴基斯坦、哈薩克

下面三條出自同一篇論文，寫 anoni-net/news 的 CircumVolve 那篇（2026-11-27）時補上。論文是作者團隊在四國資料中心 VPS 上的實測，各國審查的背景描述另外引用其他文獻，引用的文獻沒有讀過。

- 文件：CircumVolve: Automated Discovery of Censorship Evasion Strategies Using Large Language Models，GFW Report（ACM CCS 2026 論文），<https://gfw.report/publications/ccs26/en/>，2026-11-16
- 查證日期 2026-11-22

### CN-1　中國的 QUIC SNI 檢查（2024 年 4 月起）

- 事實：論文寫到中國自 2024 年 4 月起大規模解密 QUIC 連線的第一個封包並檢查其中的 SNI。依論文的描述，中國的做法混合旁路（on-path）與在路徑上（in-path）兩種，含有被封鎖 SNI 的封包會放行，之後同一組位址與連接埠的封包會被丟棄
    - 照錄：「China began decrypting and inspecting the SNI field of QUIC connections at scale in April 2024」
    - 照錄：「China's mechanism is a hybrid of on-path and in-path systems where the offending packet is allowed through, but subsequent packets on the same three-tuple (srcIP, dstIP, dstPort) are dropped.」
- 事實：論文在中國測試了五種協定（DNS、QUIC、HTTP、TLS、TCP/IP），HTTP 的部分把中國的審查設備描述成旁路注入重設封包（TCP RST）的方式
    - 照錄：「on-path resetters (e.g., China's GFW) observe traffic passively. When they detect forbidden content, they race to inject TCP RST packets to both sides of the connection.」
- 一手（論文的實測與描述），2024 年 4 月的時間點是論文引用的先前研究（論文參考文獻 [81]，未讀）

### PK-1　巴基斯坦的 QUIC SNI 與 HTTP 封鎖

- 事實：論文把巴基斯坦與哈薩克描述成中國審查設備的進口國，兩國都依 SNI 封鎖 QUIC 連線，設備位在路徑上，丟棄含有被封鎖 SNI 的 QUIC 封包，之後持續封鎖該連線
    - 照錄：「Kazakhstan and Pakistan [3], both consumers of China's censorship equipment exports, also deploy SNI-based QUIC connection blocking. Kazakhstan and Pakistan operate with in-path capabilities: they drop QUIC Initial packets containing forbidden SNIs, followed by residual blocking of the connection.」
    - 設備來源是二手：論文引用參考文獻 [3]「The Internet Coup: A Technical Analysis on How a Chinese Company is Exporting The Great Firewall to Autocratic Regimes」（2025-09），未讀
- 事實：HTTP 的部分，論文把巴基斯坦與伊朗的設備描述成在路徑上，偵測到被封鎖的 Host 標頭就丟棄封包並注入偽造的 TCP 重設封包
    - 照錄：「In-path middleboxes (e.g., in Iran and Pakistan) block connections immediately upon detecting a forbidden Host header; they drop the offending packets and inject forged TCP resets」
- 事實：論文在巴基斯坦測試了四種協定（QUIC、HTTP、TLS、TCP/IP）。各國對個別策略的結果不寫進筆記，等於標出哪一國的設備較弱（安全寫作）
- 一手（論文的實測與描述），設備來源見上方的二手標示

### KZ-1　哈薩克的 QUIC 與 TLS SNI 封鎖

- 事實：論文在哈薩克只測試了 QUIC 與 TLS 兩種協定，QUIC 依 SNI 封鎖的方式與巴基斯坦相同（見 PK-1 的照錄）
- 一手（論文的實測與描述）

## 台灣、日本、新加坡、香港、南韓

- 查不到 OONI 針對這幾個地方的 TLS 中間設備（middlebox）專門報告（2026-11-15）

## 待查

- 中國大陸的區域性 SNI 審查：gfw.report 的「A Wall Behind A Wall: Emerging Regional Censorship in China」（IEEE S&P 2025），<https://gfw.report/publications/sp25/en>。只讀過搜尋摘要，沒有讀全文，引用前要讀原文（2026-11-15）
- 伊朗：OONI「Measuring SNI based blocking in Iran」（2020），<https://ooni.org/post/2020-iran-sni-blocking/>。只知道標題，沒有讀內文（2026-11-15）
