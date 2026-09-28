---
title: 加拿大 C-22 合法存取法案與加密
description: 加拿大的 C-22 法案已在眾議院三讀通過，讓政府能要求通訊與網路服務業者建立協助執法的技術能力、保存詮釋資料，範圍包括部分加拿大以外的業者。Signal 與 DuckDuckGo 等業者考慮撤出加拿大。
date: 2026-10-05T07:05:00+08:00
slug: canada-c22-lawful-access
sources:
  - title: C-22 (45-1) Lawful Access Act, 2026
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: Bill C-22, Third Reading
    url: https://www.parl.ca/documentviewer/en/45-1/bill/C-22/third-reading
    publisher: Parliament of Canada
  - title: The EU must act now to protect privacy and encryption from Canada’s overreaching Bill C-22
    url: https://www.accessnow.org/press-release/the-eu-must-act-now-canadas-overreaching-bill-c-22/
    publisher: Access Now
    date: 2026-09-14
  - title: Analysis of Proposed Surveillance Law Expansion under Bill C-22
    url: https://citizenlab.ca/research/analysis-of-proposed-surveillance-law-expansion-under-bill-c-22/
    publisher: Citizen Lab
    date: 2026-06-02
  - title: "Open Letter on Bill C-22: An Act respecting lawful access"
    url: https://www.globalencryption.org/2026/04/open-letter-on-bill-c-22-an-act-respecting-lawful-access/
    publisher: Global Encryption Coalition
    date: 2026-04-28
  - title: Signal, DuckDuckGo among firms weighing Canada exit over lawful access bill
    url: https://globalnews.ca/news/11886905/lawful-access-bill-c-22-companies-services-canada/
    publisher: Global News
    date: 2026-06-04
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
watch:
  - date: 2026-10-31
    note: 參議院二讀、三讀與御准的進度，Signal、VPN 業者是否宣布撤出加拿大
authors:
  - anoni-net
---

加拿大的《合法存取法》（Bill C-22）6 月 18 日在眾議院三讀通過，目前在參議院，二讀還沒有完成。法案讓政府能要求通訊與網路服務業者建立協助執法的技術能力，也適用於部分加拿大以外的業者與使用者。Access Now 與多個歐洲公民團體 9 月發表公開信，請歐盟要求加拿大修改法案，新聞稿寫到法案最快可能在 10 月成為法律。

法案第二部分的第一層是「核心業者」，要依法規具備指定的技術能力，Global News 報導核心業者可能是大型電信與衛星業者。第二層是公共安全部長的命令，可以要求任何業者建立特定能力。命令經情報專員核准即可生效，不必取得法院令狀。業者不得透露自己收到命令，也不得透露命令的內容。

法案也允許以法規要求業者保存詮釋資料（metadata）。Citizen Lab 6 月初分析的版本最長保存一年，眾議院通過的版本改成不超過六個月。Citizen Lab 的分析寫到，詮釋資料至少可能包括每個人跟誰聯絡、行動軌跡，以及用過哪些 App。

條文寫明，業者可以不遵守會「引入系統性漏洞」的要求，也不必替使用者自行加密、業者沒有金鑰的資料解密。Global Encryption Coalition 4 月針對初版的公開信寫到，「系統性漏洞」的定義模糊，「加密」在法案裡也沒有定義。Signal 6 月在眾議院委員會作證，證詞的內容是如果被迫在背叛使用者與離開市場之間選擇，會選擇離開。DuckDuckGo 也向 Global News 確認，法案照目前版本通過，就會在加拿大下架 VPN 服務。

## 導讀觀點 {#perspective}

端對端加密的金鑰只存在通訊兩端的裝置上，服務營運方手上沒有金鑰，條文的解密例外涵蓋的正是這種設計。爭議在於部長命令能要求的範圍，依 Citizen Lab 的分析，這些義務可能包括改變服務的運作方式或在服務裡嵌入監控工具。

為執法建立的存取管道也可能被其他人利用，Global Encryption Coalition 的公開信舉 2024 年的 Salt Typhoon 為例。攻擊者利用一般的軟體漏洞與竊取的帳密進入美國電信網路，接著直接使用電信商依法建置的監聽功能。

類似的制度在英國已有先例，政府依《調查權力法》向 Apple 發出祕密命令後，Apple 不再讓英國的新使用者開啟 iCloud 進階資料保護。依 Global Encryption Coalition 公開信的描述，Apple 選擇停掉這項功能，沒有替政府建立存取加密資料的管道。

加拿大以外的讀者現在不需要調整任何設定。法案還要經過參議院二讀、三讀與御准才會生效，之後的影響要看部長對哪些業者下命令，而收到命令的業者不能公開。解密例外只涵蓋業者沒有金鑰的加密，業者握有金鑰的資料不在例外之內，例如沒有端對端加密的雲端備份。常用 App 的備份是否有端對端加密，可以趁這次檢查一遍。
