---
title: 英國 iCloud 進階資料保護的分級現況
description: Apple 從 2025 年 2 月起不再讓英國的新使用者開啟進階資料保護，在那之前開啟的人仍受保護，英國的 iCloud 因此分成兩種加密程度。英國以外的使用者仍可開啟。
date: 2026-09-27T07:28:00+08:00
slug: uk-icloud-advanced-data-protection
sources:
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: iCloud data security overview
    url: https://support.apple.com/en-us/102651
    publisher: Apple
    date: 2026-01-05
  - title: How to turn on Advanced Data Protection for iCloud
    url: https://support.apple.com/en-us/108756
    publisher: Apple
    date: 2026-04-17
  - title: About encrypted backups on your iPhone, iPad, or iPod touch
    url: https://support.apple.com/en-us/108353
    publisher: Apple
    date: 2026-09-21
  - title: Two-Tier Encryption in the UK
    url: https://macanorak.com/two-tier-encryption-in-the-uk/
    publisher: MacAnorak
    date: 2026-09-21
  - title: The UK Is Still Trying to Backdoor Encryption for Apple Users
    url: https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users
    publisher: EFF
    date: 2025-10-01
  - title: Apple Launches New Legal Challenge Against UK Backdoor Demand
    url: https://www.macrumors.com/2026/08/03/apple-legal-challenge-against-uk-demand/
    publisher: MacRumors
    date: 2026-08-03
  - title: 如何開啟 iCloud 進階資料保護
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
regions:
  - GB
authors:
  - anoni-net
---

Apple 從 2025 年 2 月起不再讓英國的新使用者開啟 iCloud 的進階資料保護（Advanced Data Protection，簡稱 ADP），在那之前已經開啟的人仍受保護。一位英國作者在 9 月 21 日的文章寫到，同樣住在英國、用同一款 iPhone 的兩個人，iCloud 的加密程度因此不同。英國以外的地方仍可以開啟 ADP。

起因是《華盛頓郵報》2025 年 2 月的報導，英國政府依《調查權力法》發出技術能力通知，要求 Apple 建立存取加密 iCloud 資料的能力，範圍涵蓋全球的使用者。Apple 在 2 月 21 日宣布英國的新使用者不能再開啟 ADP，說明頁寫明 Apple 從未、也不會在產品中建置後門或萬能鑰匙。

Apple 的說明頁列出影響範圍。預設就端對端加密的 15 類資料不受影響，例如 iCloud 鑰匙圈與健康資料，iMessage 與 FaceTime 也維持端對端加密。沒有開啟 ADP 的英國使用者，iCloud 備份、iCloud 雲碟、照片、備忘錄等 10 類資料改用標準資料保護，金鑰存在 Apple 的資料中心。

已經開啟 ADP 的英國使用者，Apple 無法自動替他們關閉，這個設定只能從使用者信任的裝置更改。Apple 的公告寫到會給這些使用者一段時間自行關閉，原文寫到 9 月 21 日為止還沒有公布期限。

EFF 在 2025 年 10 月的文章寫到，據報導英國改發了一份只針對英國使用者的通知。Apple 在 2026 年 7 月向調查權力法庭提出新的申訴，這場爭議還沒有結果。

## 導讀觀點 {#perspective}

所有 iCloud 資料都有加密，差別在金鑰放在哪裡。標準資料保護的金鑰在 Apple 手上，收到合法的調閱要求時可以解密交出。ADP 讓金鑰只留在使用者信任的裝置上，Apple 沒有鑰匙，要取得內容就只能改變系統的設計，英國的通知與 Apple 就僵持在這一點。

在英國、無法開啟 ADP 的人，Apple 的說明寫明，同時開著 iCloud 備份與「iCloud 中的訊息」時，備份裡會附上訊息的金鑰。關閉 iCloud 備份之後，裝置會產生新的金鑰，之後的訊息維持端對端加密。改用電腦做加密的本機備份，備份也留在自己手上，這個選項預設沒有開啟，要在 Finder 或 Apple 裝置 App 裡勾選。

ADP 的代價是 Apple 無法協助復原端對端加密的資料，遺失所有復原方式就找不回來。開啟之後 iCloud.com 的網頁存取也會關閉，需要時要從信任的裝置核准。

不在英國的人，可以在 iPhone 的「設定」點自己的名字，進入 iCloud 開啟「進階資料保護」，Apple 的說明頁有正體中文的步驟。Apple 帳號需要先啟用雙重認證，並設定復原聯絡人或復原密鑰，所有登入同一帳號的裝置也要更新到 iOS 16.2、macOS 13.1 以上的對應版本。管理式 Apple 帳號與兒童帳號不能開啟。
