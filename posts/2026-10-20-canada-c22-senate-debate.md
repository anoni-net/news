---
title: 加拿大 C-22 法案的參議院二讀與業者的表態
description: 加拿大的 C-22 合法存取法案 10 月 8 日在參議院進行二讀辯論，到 10 月 18 日為止還沒有二讀通過。Signal 的副總裁在座談上表示，若被命令蒐集更多詮釋資料就只能撤出加拿大，公共安全部長辦公室則表示法案不要求解密端對端加密的資訊。加拿大以外的讀者現在不需要調整設定。
date: 2026-10-20T00:05:00+08:00
slug: canada-c22-senate-debate
categories:
  - encryption
follows:
  - 2026-10-05-canada-c22-lawful-access
sources:
  - title: C-22 (45-1) - LEGISinfo - Parliament of Canada
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: Debates, Issue 92 (October 8, 2026)
    url: https://sencanada.ca/en/content/sen/chamber/451/debates/092db_2026-10-08-e
    publisher: Senate of Canada
    date: 2026-10-08
  - title: "Parliamentary Committee Notes: appearance before the Standing Committee on Public Safety and National Security (SECU)"
    url: https://publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20260828-1/index-en.aspx
    publisher: Public Safety Canada
    date: 2026-05-05
  - title: Messaging service Signal says minister’s changes to lawful access bill will not persuade it to stay in Canada
    url: https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-06
  - title: Toronto-based VPN provider plans to quit Canada over lawful-access bill
    url: https://www.theglobeandmail.com/politics/article-psiphon-vpn-provider-plans-to-quit-canada-over-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-04
  - title: The Lawful Access Act threatens to blow a hole in Canada’s national security
    url: https://www.theglobeandmail.com/opinion/article-the-lawful-access-act-threatens-to-blow-a-hole-in-canadas-national/
    publisher: The Globe and Mail
    date: 2026-10-09
  - title: The Lawful Access Act’s threats to Canada’s national security
    url: https://citizenlab.ca/the-lawful-access-acts-threats-to-canadas-national-security/
    publisher: Citizen Lab
    date: 2026-10-16
  - title: Telecommunications and Other Legislation Amendment (Assistance and Access) Act 2018
    url: https://www.legislation.gov.au/C2018A00148/latest/text
    publisher: Federal Register of Legislation
watch:
  - date: 2026-11-20
    note: 參議院 10 月 20 日復會後是否二讀通過、交付哪個委員會，Signal 與 Psiphon 是否宣布撤出加拿大的日期
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法存取法》（Bill C-22）6 月在眾議院三讀通過，參議院 10 月 8 日進行二讀辯論後休會，下次開會是 10 月 20 日。依加拿大國會的法案資料庫 LEGISinfo，到 10 月 18 日為止法案還沒有二讀通過，也沒有交付委員會或御准（總督簽署成為法律）的紀錄。10 月 4 日到 16 日之間，Signal、審查規避工具 Psiphon 與多倫多大學的研究室 Citizen Lab 都公開提出反對的理由，代表政府在參議院推動法案的參議員（提案人）則在二讀演說中說明法案的保障。法案尚未通過、業者的撤出也都附有條件，依本文的判斷，加拿大以外的讀者現在不需要調整設定。

Signal 的策略與全球事務副總裁 10 月 5 日在網際網路協會加拿大分會的座談上發言，《環球郵報》（The Globe and Mail）隔天報導。依報導，這位副總裁主張法律對加密的保護要涵蓋用金鑰解密以外的情況，被要求大幅改動軟體同樣會抵銷加密的目的。Signal 只保存使用者的電話號碼、加入日期與最後登入資訊，若被命令蒐集更多詮釋資料（通訊內容以外的紀錄）並保存最長六個月，就只能撤出加拿大。到 10 月 18 日為止，Signal 的部落格與 Bluesky 帳號沒有發表關於 C-22 的書面聲明。

Psiphon 10 月 2 日向《環球郵報》表示已開始擬定把營運搬出加拿大的計畫，條件是法案照現狀通過。公司的副總裁在書面回覆中寫到，開源程式碼的每一行都公開，法案若要求建立存取能力就會被全世界看到（包括使用者想躲避的威權政府）。Citizen Lab 一位資深研究員 10 月 9 日在同一份報紙發表評論，主張不存在只讓執法單位進得去、其他攻擊者卻沒有機會利用的設計，Citizen Lab 10 月 16 日在網站上轉載了摘要。

依提案人 10 月 8 日的二讀演說，法案第二部分規範業者技術能力的新法，本身不會給執法單位或加拿大安全情報局（CSIS）新的取得資訊權力。部長命令要經情報專員（審查情報授權的獨立官員）核准、接受獨立審查，效期最長兩年。詮釋資料保存限於指定的類別、最長六個月，不包含通訊內容與瀏覽紀錄。公共安全部長辦公室的發言人向《環球郵報》表示，法案明文不要求解密端對端加密的資訊，也不允許或強迫業者引入系統性漏洞或後門。

## 導讀觀點 {#perspective}

依公共安全部 5 月的委員會備詢資料，業者評估某項要求無法在不引入系統性漏洞（影響整類產品或大量使用者、不只針對單一目標的漏洞）的情況下遵守時就不必遵守，政府用這個詞劃出業者不必遵守的範圍。提案人在演說中也提到，委員會要聽取技術證據，了解一項能力被描述成針對特定目標、卻可能影響整個產品或更新系統時這個詞如何運作。Psiphon 被一位參議員引用的意見則是開源軟體裡任何法定的存取機制都會公開，無法只限於加拿大機關或單一調查。

監督方式是另一個爭點。一位參議員在辯論中批評部長命令被排除在《法定文書法》（規定法規送交國會審查的法律）之外，另一位參議員引用 Citizen Lab 與一個公民自由團體的聯合意見書，寫到法案的義務可以在沒有司法授權的情況下施加。提案人在演說中則提到，命令與佐證資料要送交國家安全與情報審查機構（NSIRA，審查情報與安全機關的獨立機構），並引用警察團體代表對法案的支持。

公共安全部的備詢資料提到澳洲有類似的保障。澳洲 2018 年的《協助與存取法》同樣規定，技術能力通知（要求業者建立特定能力的書面命令）不得要求業者建立系統性弱點或系統性漏洞。澳洲法把系統性弱點定義為影響整類技術的弱點，不包括只針對特定人刻意引入的弱點（若會危及他人的資訊安全仍算）。Citizen Lab 研究員的評論則引用澳洲的經驗，寫到一家公司表示信任流失造成約 10 億澳幣的經濟損失。

比較各地做法時，可以問命令由誰核准、需不需要法院，以及業者能不能公開命令的存在。系統性漏洞由誰判斷、詮釋資料保存的範圍與期限，也是可以對照的地方。另外可以問政策想達成的調查目的，能不能在不削弱加密的情況下做到。

Signal 與 Psiphon 的撤出都附有條件，到 10 月 18 日為止兩家都沒有宣布撤出的日期。參議院 10 月 20 日復會後的二讀表決，以及法案交付哪個委員會，是接下來可以觀察的進度。在加拿大的讀者會受什麼影響，要看法案最後的條文與業者的決定。
