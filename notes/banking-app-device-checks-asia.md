# 亞洲各地銀行 App 對 root 與未認證系統的檢查

範圍是台灣、香港、日本與中國大陸的金融監管機關，對行動銀行 App 偵測 root、越獄或未經 Google 認證的系統有沒有公開規範，以及 PrivSec 相容性名單上各地銀行 App 在 GrapheneOS 的附註。第一次整理是寫 anoni-net/news 的 ASN Bank 與 Play Integrity 那篇的時候，查證日期 2026-11-08。

## PrivSec 的相容性名單

- 事實：PrivSec 的「Banking Applications Compatibility with GrapheneOS」名單有台灣、香港、日本與中國大陸的小節。這四節裡跟 Play Integrity 有關的附註只有日本的 Habitto 一項。名單由社群回報，記的是相容性，不是銀行對 root 的政策，GrapheneOS 官方也不保證內容
    - 照錄（Habitto）：「You can't install this app via Google Play because of Play Integrity. However, you can work around this restriction by using the Aurora Store instead.」
    - 照錄（台灣，國泰世華 行動銀行）：「Secure app spawning must be disabled for this app to run!」
    - 照錄（日本，SBI新生銀行）：「Secure app spawning must be disabled for this app to run!」
    - 照錄（日本，三井住友銀行アプリ）：「Secure app spawning may have to be disabled for this app to run!」
    - 來源：Banking Applications Compatibility with GrapheneOS，PrivSec，<https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/>，2022-01-26 發布，2026-10-20 最後更新
- 事實：台灣一節有 12 項（彰銀、行動郵局、e動郵局、國泰世華、一卡通 iPASS MONEY、中國信託、將來銀行、台新、兆豐、玉山 Wallet、永豐金證券等），只有國泰世華一項有附註。香港一節 9 項（BEA、中銀香港、DBS IDEAL、Hang Seng、HSBC HK、Octopus 等），中國大陸一節 10 項（農行、支付寶、交行、工行、中行、招行等），兩節都沒有附註
    - 來源同上

## 台灣

- 查不到：金管會或銀行公會對行動銀行 App 偵測 root、未認證系統的公開規範原文。《金融機構辦理電子銀行業務安全控管作業基準》的相關條文沒有取得，不能確認有沒有偵測 root 或越獄的要求

## 香港

- 查不到：香港金融管理局（HKMA）對 root、未認證系統的明確指引。搜尋結果提到 HKMA 在 2023 年第四季要求認可機構檢視行動 App 的安全，並重申監管政策手冊 TM-E-1，這是二手來源，原文沒有取得，該來源也沒有提到 root
- 事實：DBS 香港的安全說明頁建議 root 或越獄裝置的使用者先回復原廠設定，不行的話改在沒有 root 或越獄的裝置上設定 digibank Mobile，緊急交易可以到 ATM、分行，或在電腦上用功能較少的 iBanking。這是單一銀行的說明，不代表 HKMA 的規範
    - 照錄：「Is your device jailbroken or rooted?」、「You may wish to perform a factory reset on your device.」、「If this does not work, you may need to setup your digibank Mobile on another device which has not been jailbroken or rooted.」
    - 來源：Anti-Malware Security Features，DBS Hong Kong，<https://www.dbs.com.hk/personal/online-security/general-digibank-security-malware-jailbroken-device.page>，頁面沒有標示日期

## 日本

- 查不到：金融廳、FISC 或全國銀行協會對 root、未認證系統的公開說明，也沒有找到三菱 UFJ、Mizuho、三井住友的官方 FAQ

## 中國大陸

- 查不到：法規對 root 或未認證系統的明確條文。中國人民銀行的《移动金融客户端应用软件安全管理规范》JR/T 0092-2019（搜尋結果轉述為 2019-09-27 發布實施，二手來源）沒有取得全文，不能確認有沒有偵測 root 的條款

## 亞洲其他地方（未核對原文）

- 二手來源：泰國 Krungsri 依央行指引，自 2020 年 5 月起擋下 root 或越獄的裝置。越南國家銀行的通告要求銀行 App 自 2026-03-01 起不在 compromised devices 上運作（報導來源 news.baohaiphong.vn）。兩條都只有搜尋結果或報導，引用前要先查原文
