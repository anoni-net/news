---
title: 加拿大 C-22 合法存取法案與加密
description: 加拿大的 C-22 法案已在眾議院三讀通過，政府能要求通訊與網路服務業者建立協助執法的技術能力、保存詮釋資料，部分加拿大以外的業者也在範圍內。加拿大以外的讀者現在不需要調整設定。
date: 2026-10-05T00:05:00+08:00
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
  - title: Signal, DuckDuckGo among firms weighing Canada exit over lawful access bill
    url: https://globalnews.ca/news/11886905/lawful-access-bill-c-22-companies-services-canada/
    publisher: Global News
    date: 2026-06-04
  - title: The UK Is Still Trying to Backdoor Encryption for Apple Users
    url: https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users
    publisher: EFF
    date: 2025-10-01
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: 如何開啟「iCloud 進階資料保護」
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
    date: 2026-04-24
watch:
  - date: 2026-10-31
    note: 參議院二讀、三讀與御准的進度，Signal、VPN 業者是否宣布撤出加拿大
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法存取法》（Bill C-22）6 月 18 日在眾議院三讀通過，到 9 月 29 日為止，參議院的二讀還沒有完成。法案讓政府能要求通訊與網路服務業者建立協助執法的技術能力，部分加拿大以外的業者也在適用範圍內。數位權利組織 Access Now 與多個歐洲公民團體 9 月致信歐盟要求介入，新聞稿寫到法案最快可能在 10 月成為法律。加拿大以外的讀者現在不需要調整設定。

技術能力的要求分成兩層，第一層適用於「核心業者」（core providers），這些業者要依法規具備指定的能力。第二層是公共安全部長的命令，可以要求任何業者建立特定能力。命令只需要獨立的情報專員（Intelligence Commissioner）核准，不必經過法院。收到命令的業者不得透露命令的存在與內容。

法案也允許以法規要求業者保存詮釋資料（metadata，通訊內容以外的紀錄）。最長保存期限在初版是一年，眾議院通過的版本改成六個月。依多倫多大學研究單位 Citizen Lab 6 月初的分析，詮釋資料很可能包括每個人跟誰聯絡、行動軌跡，以及用過哪些 App。

條文寫明，業者不必遵守會「引入系統性漏洞」的要求。使用者自行加密、業者手上沒有金鑰的資料，業者也不必解密。

Signal 6 月出席眾議院委員會作證，立場是被迫在背叛使用者與離開市場之間選擇時，會離開加拿大。DuckDuckGo 也向加拿大媒體 Global News 確認，法案若照 6 月初、眾議院修正前的版本通過，會在加拿大下架 VPN 服務。

## 導讀觀點 {#perspective}

端對端加密的金鑰只存在通訊雙方的裝置上，營運 Signal 這類服務的業者沒有金鑰，照條文的文字應該落在解密例外之內。爭議集中在部長命令能要求的範圍，依 Citizen Lab 的分析，可能包括改變服務的運作方式與在服務裡嵌入監控工具。

英國政府 2025 年 1 月依《調查權力法》，對 Apple 發出了同類的技術能力通知（EFF 2025 年 10 月的文章）。Apple 選擇在英國撤下 iCloud 進階資料保護，沒有建立後門，Apple 的說明頁也寫明英國的新使用者不能開啟。

到 9 月 29 日為止，法案還需要參議院二讀、三讀與御准（Royal Assent，成為法律前的最後程序）。實際影響要看部長對哪些業者下命令。業者握有金鑰的資料不在解密例外之內，例如沒有端對端加密的雲端備份。

想讓雲端備份也改用端對端加密的 iPhone 使用者，可以開啟 iCloud 的進階資料保護，iCloud 備份與照片等大部分資料都會納入。條件是帳號已開啟雙重認證、登入同一帳號的所有裝置都更新到 iOS 16.2、macOS 13.1 等對應版本以上，管理式帳號與兒童帳號不能使用。開啟前要設定復原聯絡人或 28 個字元的復原密鑰，因為 Apple 無法協助找回端對端加密的資料。在「設定」點你的姓名，再依序點「iCloud」與「進階資料保護」即可開啟（Apple 的說明頁有正體中文版）。
