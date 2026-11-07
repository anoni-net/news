---
title: 加拿大 C-22 法案的參議院委員會審查與加密弱點的爭論
description: 加拿大的 C-22 合法存取法案 10 月 22 日在參議院二讀通過，交付國家安全、國防與退伍軍人事務委員會審查，到 11 月 7 日為止還沒有三讀。Citizen Lab 的研究員主張 6 月以來 AI 帶動的網路威脅出現重大變化，通訊系統不該再留下弱點。政府 5 月的備詢資料則主張法案不要求建立後門，業者可以拒絕會引入系統性漏洞的要求。加拿大以外的讀者現在不需要調整設定。
date: 2026-11-08T00:05:00+08:00
slug: canada-c22-senate-committee
categories: [encryption]
follows:
  - 2026-10-20-canada-c22-senate-debate
sources:
  - title: C-22 (45-1) - LEGISinfo - Parliament of Canada
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: "Built-In Weakness: Lawful Access and Encryption in the Age of AI-Powered Cyber Threats"
    url: https://citizenlab.ca/built-in-weakness-lawful-access-and-encryption-in-the-age-of-ai-powered-cyber-threats/
    publisher: Citizen Lab
    date: 2026-10-23
  - title: We Shouldn’t Have to Give Up Our Safety Online to Be Safe
    url: https://www.internetsociety.org/blog/2026/10/we-shouldnt-have-to-give-up-our-safety-online-to-be-safe/
    publisher: Internet Society
    date: 2026-10-21
  - title: The Lawful Access Act threatens to blow a hole in Canada’s national security
    url: https://www.theglobeandmail.com/opinion/article-the-lawful-access-act-threatens-to-blow-a-hole-in-canadas-national/
    publisher: The Globe and Mail
    date: 2026-10-09
  - title: Messaging service Signal says minister’s changes to lawful access bill will not persuade it to stay in Canada
    url: https://www.theglobeandmail.com/politics/article-messaging-service-signal-says-ministers-changes-to-lawful-access-bill/
    publisher: The Globe and Mail
    date: 2026-10-06
  - title: Analysis of Proposed Surveillance Law Expansion under Bill C-22
    url: https://citizenlab.ca/research/analysis-of-proposed-surveillance-law-expansion-under-bill-c-22/
    publisher: Citizen Lab
    date: 2026-06-02
  - title: "Parliamentary Committee Notes: appearance before the Standing Committee on Public Safety and National Security (SECU)"
    url: https://publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20260828-1/index-en.aspx
    publisher: Public Safety Canada
    date: 2026-05-05
  - title: Investigatory Powers Act 2016, section 253
    url: https://www.legislation.gov.uk/ukpga/2016/25/section/253
    publisher: legislation.gov.uk
watch:
  - date: 2026-12-08
    note: 參議院國家安全、國防與退伍軍人事務委員會是否提出報告、有沒有修正第二部分，參議院三讀與御准的進度
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法存取法》（Bill C-22）10 月 22 日在參議院完成二讀，同一天交付參議院國家安全、國防與退伍軍人事務常設委員會審查。加拿大國會的法案資料庫 LEGISinfo 列出委員會 11 月 2 日的一次會議，到 11 月 7 日為止委員會還沒有提出報告。法案 6 月已在眾議院三讀通過，參議院 10 月辯論期間，通訊與審查規避工具的業者都公開提出反對的理由。法案還沒有成為法律，加拿大以外的讀者現在不需要調整設定。

法案讓政府能要求通訊與網路服務業者建立協助執法的技術能力，也能以法規要求業者保存詮釋資料（通訊內容以外的紀錄）。參議院到 11 月 7 日沒有通過任何修正，委員會提出報告之後，法案才會進入三讀。

Citizen Lab 是多倫多大學的研究室，10 月 23 日在網站上貼出一場座談的影片。依主辦方之一 Internet Society（在世界各地設有分會、推動開放與安全網際網路的國際組織）的貼文，座談在 10 月初為國會議員舉行，主題是合法存取在 AI 帶動網路威脅的時代代表什麼。頁面只有一段文字，寫到 Citizen Lab 的資深研究員在座談上談法案的法律疑慮。研究員強調應該修補與預防漏洞，不要在日常的通訊系統上「鑽更多洞」。

同一位研究員 10 月 9 日在《環球郵報》（The Globe and Mail）發表評論，主張 6 月以來 AI 帶動的網路威脅出現重大變化。作者在評論裡舉的例子包括 7 月 OpenAI 的 AI agent 逃出沙箱、攻擊軟體公司 Hugging Face，以及外界對 Anthropic 未公開發布的模型 Claude Mythos 的擔憂。評論沒有附這些事件的來源，本文也沒有核對相關公司的原始公告。依評論的結論，政府官員假設科技業者能找到「安全的方式」削弱資安防護，誤判了當前的威脅環境。

Citizen Lab 6 月提交給眾議院委員會的意見書早於研究員 10 月的評論，內容是逐部分檢視條文的法律與政策分析。意見書的核心建議是整個撤回法案第二部分，也就是規範業者技術能力的新法。理由之一是政府可以對任何電子服務業者施加任何義務，包括改變服務的運作方式或在服務裡嵌入監控工具。意見書只有一句提到 AI，內容是隨著 AI 監控技術增加，法案的侵入性也會跟著提高。

## 導讀觀點 {#perspective}

依 Citizen Lab 的意見書，為了配合監控義務而修改的技術設計很難保護，範圍比加拿大更窄的美國與紐西蘭制度也多次被外國情報機關秘密入侵。意見書引用美國國家安全局（NSA）的測試，NSA 測試的符合美國監聽能力法 CALEA 的交換器每一台都有安全漏洞，也引用與中國政府有關的駭客組織 Salt Typhoon 入侵美國監聽能力系統的事件。依本站 11 月 7 日整理的 [EFF 文章](https://anoni.net/news/2026/11/eff-security-worse/)，前沿 AI 模型讓找漏洞變得便宜。10 月 10 日那篇則整理了 [Anthropic 測試開放權重模型寫出攻擊瀏覽器程式的報告](https://anoni.net/news/2026/10/glm-5-3-cyber-capabilities/)。

依公共安全部長 5 月 5 日到眾議院委員會備詢的資料，政府不支持、法案也不要求建立後門，政府只訂定對業者的要求、不指定技術做法。業者評估某項要求無法在不引入系統性漏洞（影響整類產品或大量使用者、不只針對單一目標的漏洞）的情況下遵守時，就不必遵守。系統性漏洞已經在條文裡定義，部長命令也要事先經情報專員（審查情報授權的獨立官員）核准。Citizen Lab 的意見書則把法案的保障評為彈性大、定義不清，適用範圍也沒有設限。

Citizen Lab 研究員的評論把 AI 當成 6 月之後的新情況，主張政府期待業者兼顧監控義務與資安的前提，已經跟不上威脅的變化。公共安全部的備詢資料早於這波論點，資料轉述通訊安全局（CSE，加拿大負責訊號情報與網路安全的機關）的意見，認為惡意網路活動的威脅本來就存在。依備詢資料轉述的 CSE 評估，法案讓合法存取從臨時、自願的做法改成標準化的管理，能改善資安。公共安全部長辦公室的發言人 10 月初向《環球郵報》表示，法案不允許或強迫業者引入系統性漏洞或後門。

依備詢資料，加拿大的警察與情報人員對付懂科技的犯罪者與國家行為者時，用的是數十年前的工具。政府把法案定位成補上這個落差的做法。Internet Society 執行長在同一場座談的開場演說中，提出的替代做法是加強數位鑑識能力、改善跨境合作、相稱地使用詮釋資料，以及跟服務業者建立合作關係。演說的前提是弱點一旦存在，任何找到它的人都能利用。

法案到 11 月 7 日仍在參議院委員會審查，依本文的判斷，在加拿大的讀者現在也不需要調整設定。前面提到的 EFF 文章給每個人的建議是更新瀏覽器與 App、改用密碼管理員並提防釣魚，這些做法跟法案的結果無關。接下來可以留意委員會的報告有沒有修正第二部分，以及參議院三讀的時間。

英國的《調查權力法》（Investigatory Powers Act 2016）第 253 條同樣讓政府對業者發出技術能力通知，通知要經司法專員核准，可以規定的義務包括移除業者自己施加的電子保護。依本站 9 月的整理，Apple 收到通知之後，從 2025 年 2 月起不再讓英國的新使用者開啟 [iCloud 進階資料保護](https://anoni.net/news/2026/09/uk-icloud-advanced-data-protection/)。依政府 5 月的備詢資料，加拿大的部長命令由情報專員事先核准。法案也另設例外，業者評估會引入系統性漏洞時可以不遵守。

比較各地做法時，可以問命令由誰核准、業者能不能拒絕或公開命令，以及系統性漏洞最後由誰認定。也可以問威脅環境改變之後，誰負責重新評估已經建立的存取能力。另外要問政策想達成的調查目的，能不能用數位鑑識、跨境合作這類不削弱加密的方法做到。也可以從政府的標準問，標準化的存取能力能不能補上備詢資料提到的調查工具落差，又能不能改善 CSE 提到的臨時、自願做法的資安問題。
