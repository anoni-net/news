# 服務業者的協助執法義務

範圍是法律要求通訊或網路服務業者為執法建立能力、識別發送者或提供解密協助的規定，不含扣押手機後要求持有人交出密碼（那部分見 `compelled-decryption.md`）。第一次整理是寫加拿大 C-22 法案參議院委員會審查那篇的時候，查證日期都是 2026-11-07。

## 印度

- 事實：《資訊科技（中介指南與數位媒體道德準則）規則 2021》第 4(2) 條規定，主要提供訊息服務的重要社群媒體中介者，要在有管轄權的法院命令，或主管機關依第 69 條發出的命令要求時，能識別資訊的第一發送者
    - 照錄：「A significant social media intermediary providing services primarily in the nature of messaging shall enable the identification of the first originator of the information on its computer resource as may be required by a judicial order passed by a court of competent jurisdiction or an order passed under section 69 by the Competent Authority」
    - 來源：Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021（updated as on 6.4.2023），MeitY 公布的 PDF，<https://www.meity.gov.in/static/uploads/2024/02/Information-Technology-Intermediary-Guidelines-and-Digital-Media-Ethics-Code-Rules-2021-updated-06.04.2023-.pdf>
- 事實：命令只能為主權與完整、國家安全、與外國的友好關係、公共秩序相關的罪行，或刑期 5 年以上的強姦、性露骨內容、兒少性剝削內容相關罪行發出。其他侵入性較低的方法有效時不得發出命令，業者也不必揭露訊息內容
    - 照錄：「no order shall be passed in cases where other less intrusive means are effective in identifying the originator of the information」
    - 照錄：「no significant social media intermediary shall be required to disclose the contents of any electronic message, any other information related to the first originator, or any information related to its other users」
    - 來源：同上，第 4(2) 條的但書
- 條文沒有寫端對端加密的服務如何滿足識別第一發送者的要求。相關的訴訟現況與業者聲明沒有查

## 中國大陸

- 事實：《密碼法》（2019-10-26 公布，2020-01-01 施行）第 31 條第 2 款規定，密碼管理部門與有關部門不得要求商用密碼從業單位與商用密碼檢測、認證機構揭露原始碼等與密碼有關的專有資訊
    - 照錄（英譯本）：「Cryptography management departments and relevant departments, as well as their staffs, must not require commercial cryptography work units and commercial cryptography testing and certification bodies to disclose source code and other proprietary information related to cryptography」
    - 來源：Cryptography Law of the P.R.C.，China Law Translate 的英譯本（非官方），<https://www.chinalawtranslate.com/en/cryptography-law/>。人大網的原文抓不到
- 英譯本只讀了條文標題與第 12、13、26 到 32 條，沒有讀到要求業者替執法單位解密的條文，但不能據此說全文沒有
- 要求電信業者與網路服務提供者提供技術介面與解密支援的是《反恐怖主義法》第十八條，來源見 `posts/en/2026-10-20-canada-c22-senate-debate.md` 的 `sources`
- 二手來源：《網路安全法》第 28 條要求網路運營者為公安機關、國家安全機關依法維護國家安全與偵查犯罪提供技術支持與協助，只有搜尋摘要確認。搜尋結果提到該法 2025-10-28 修正、2026-01-01 施行，現行條號沒有核對，引用前要先到官方文本確認

## 新加坡、日本、台灣

- 這次沒有查到類似加拿大 C-22 第二部分、要求業者建立協助執法技術能力的規定。這是沒有搜尋到，不代表沒有，只查了扣押取證（見 `compelled-decryption.md`）
