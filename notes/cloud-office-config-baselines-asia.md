# 雲端辦公服務的設定基準與檢查工具

範圍是官方有沒有出針對 Microsoft 365 或 Google Workspace 租戶設定的安全基準與自動檢查工具，對照美國 CISA 的 ScubaGear 與 ScubaGoggles。新加坡、香港、中國三地都只查到雲端服務的一般性指引或雲服務商的評估制度，沒有查到同類的檢查工具。第一次整理是寫 anoni-net/news 的 CISA SCuBA 工具那篇（`2026-11-06-cisa-scuba-config-tools`）的時候，查證日期都是 2026-11-02。「查不到」不等於不存在。

## 新加坡

- 事實：CSA 在 2023-10-17 與 Cloud Security Alliance 合作發布雲端安全配套指南（Cloud Security Companion Guides），對應 Cyber Essentials（中小企業，訂閱 SaaS）與 Cyber Trust（較大或較數位化的組織），AWS、Google Cloud、Microsoft 參與編寫。新聞稿沒有提到自動化評估工具
    - 來源：Launch of Cloud Security Companion Guides for Organisations，CSA，<https://www.csa.gov.sg/news-events/press-releases/launch-of-cloud-security-companion-guides-for-organisations/>，2023-10-17
- 事實：CSA 的〈Cloud Security for Organisations〉頁面列有與 Microsoft 合作的 Microsoft Cloud Security Companion Guide for Cyber Essentials（2022），以及與 Google 合作的 Google Workspace Cloud Security Companion Guide for Cyber Essentials（2022）。頁面沒有提到設定檢查清單。這兩項是指南文件，不是檢查工具
    - 來源：Cloud Security for Organisations，CSA，<https://www.csa.gov.sg/our-programmes/support-for-enterprises/sg-cyber-safe-programme/cloud-security-for-organisations/>，2026-11-02 查證（WebFetch 摘要，頁面無日期）
- 事實（二手來源，文章頁面無日期，2026-11-02 查證）：律師事務所 Allen & Gledhill 的文章寫 CSA 於 2026-07-22 宣布，將在 2026 年下半年發布 Cybersecurity Code of Practice for Cloud Services，規範架設在雲端上的關鍵資訊基礎設施（CII）系統，並與雲端業者編寫各業者專屬的配套指南
    - 照錄：「through appropriate configurations and the effective use of cloud-native services and security capabilities」
    - 來源（二手）：Allen & Gledhill，<https://www.allenandgledhill.com/sg/publication/articles/33410/>
- 查不到：CSA 關於上述守則的一手公告，守則的正式發布（到 2026-11-02 未見）

## 香港

- 事實：數字政策辦公室的〈Information and Cyber Security Within the Government〉頁面列有 Practice Guide for Cloud Computing Security（ISPG-SM04），描述為政府採用雲端運算技術的實務指引與參考，對象是政府部門
    - 照錄：「the practical guidance and reference for the secure adoption of cloud computing technology in the Government」
    - 來源：Information and Cyber Security Within the Government，數字政策辦公室，<https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/information_cyber_security/government/>，2026-11-02 查證（WebFetch 摘要，頁面無版本與日期）
- 查不到：官方 PDF 的版本與日期（第三方副本顯示 v1.2，2021-06，未回官方核對）、對應 Microsoft 365 或 Google Workspace 設定的檢查工具。HKCERT 沒有另外查

## 中國

- 事實：國家網信辦等四部門的《云计算服务安全评估办法》2019-07-02 簽署，2019-07-22 在 cac.gov.cn 公告，2019-09-01 施行。評估對象是黨政機關與關鍵信息基礎設施運營者採購使用的雲計算服務，評估雲服務商的資信與經營、人員背景、供應鏈、安全管理與防護、資料遷移、業務連續性等，結果有效期 3 年。這是評估雲平台的制度，不檢查客戶租戶的設定
    - 照錄：「为提高党政机关、关键信息基础设施运营者采购使用云计算服务的安全可控水平，制定本办法。」
    - 來源：《云计算服务安全评估办法》，國家互聯網信息辦公室等，<https://www.cac.gov.cn/2019-07/22/c_1124781475.htm>，2019-07-22
- 事實（二手來源）：GB/T 22239-2019《网络安全等级保护基本要求》含雲計算安全擴展要求，2019-12-01 實施。GB/T 31168《云计算服务安全能力要求》是雲服務評估的基礎標準。來自 secrss.com 與 CAC 的二手資料，沒有保留實際網址，標準本身的發布日期也沒有查（僅知 GB/T 22239-2019 的實施日），沒有取得標準全文，也沒有核對現行版本。引用前要重查。查證日期 2026-11-02
- 查不到：對應 Microsoft 365 或 Google Workspace 租戶設定的官方檢查工具

## 歸納

三地都沒有查到官方出的「Microsoft 365 或 Google Workspace 租戶設定基準加自動檢查工具」。新加坡有給 SaaS 訂閱者的配套指南（文件），香港有政府部門用的雲端安全指引，中國是雲服務商的評估制度。Microsoft 365 與 Google Workspace 在各地的供應狀況、授權方式沒有查。查證日期 2026-11-02。
