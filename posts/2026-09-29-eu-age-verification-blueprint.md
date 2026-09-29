---
title: 歐盟年齡驗證 App 的隱私設計與爭議
description: 歐盟執委會建議各會員國在 2026 年底前推出年齡驗證 App，歐盟以外的使用者不受影響。EDRi 認為憑證仍可能追溯到使用者，執委會在新聞稿裡寫明 App 不保留證件與生物特徵資料。9 月發布的新版規格裡，App 與網站都必須實作零知識證明。
date: 2026-09-29T07:00:00+08:00
slug: eu-age-verification-blueprint
sources:
  - title: The EU approach to age verification
    url: https://digital-strategy.ec.europa.eu/en/policies/eu-age-verification
    publisher: European Commission
    date: 2026-09-22
  - title: EU KIDS Act to restrict social media platforms’ access to children in the EU
    url: https://digital-strategy.ec.europa.eu/en/news/eu-kids-act-restrict-social-media-platforms-access-children-eu
    publisher: European Commission
    date: 2026-09-17
  - title: "EU KIDS Act to restrict social media platforms' access to children in the EU"
    url: https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1890
    publisher: European Commission
    date: 2026-09-17
  - title: Commission urges Member States to rollout EU age verification app
    url: https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app
    publisher: European Commission
    date: 2026-04-29
  - title: Why the EU age-verification tool does not solve privacy concerns
    url: https://edri.org/our-work/eu-age-verification-tool-does-not-solve-privacy-concerns/
    publisher: EDRi
    date: 2026-09-07
  - title: av-doc-technical-specification
    url: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification
    publisher: EU Digital Identity Wallet
    date: 2026-09-02
  - title: av-app-android-wallet-ui
    url: https://github.com/eu-digital-identity-wallet/av-app-android-wallet-ui
    publisher: EU Digital Identity Wallet
    date: 2026-09-03
  - title: Social media age restrictions
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions
    publisher: eSafety Commissioner
    date: 2026-09-15
  - title: Social media 'ban' or delay FAQ
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions/faqs
    publisher: eSafety Commissioner
    date: 2026-09-16
watch:
  - date: 2027-01-05
    note: 各會員國的年齡驗證 App 是否在年底前上線，EU KIDS Act 草案的審議進度
regions:
  - EU
authors:
  - anoni-net
---

歐盟執委會在 4 月宣布年齡驗證 App 技術就緒，建議各會員國在年底前推出自己的 App。依 9 月 17 日提出的《EU KIDS Act》草案，13 歲以下不得使用社群平台，15 歲才能自己開帳號。線上服務與 App 商店要採用年齡確認工具，這套 App 是選項之一，歐盟以外的使用者不會用到。

執委會的說明頁寫明，使用者可以證明自己年滿 18 歲，不必分享其他個人資料。App 又稱迷你錢包（mini wallet），技術規格沿用各國年底前要推出的歐盟數位身分錢包。草案的新聞稿裡寫明 App 不保留身分證件與生物特徵資料，也列出歐盟民調裡 92% 的受訪者把加強兒少網路保護列為優先政策之一。

歐洲數位權利組織 EDRi 在 9 月 7 日發表技術分析，結論是這套工具在「就緒」與「保護隱私」兩方面都做不到。EDRi 反對全面強制年齡驗證，若仍要設年齡門檻，工具要符合最高的隱私與資料保護標準。依 EDRi 的分析，App 沿用的數位身分錢包依法要在相關情況下「確保」不可連結性（unlinkability，每次出示的年齡證明無法被串回同一個人），執委會把要求改成只需「阻礙」連結。

同一篇分析裡也寫到，一般驗證方式的憑證帶有鹽值、簽章與時間戳，發證方與網站合作就能追溯到使用者。EDRi 引用的是 1.1.0 之前的規格書，零知識證明（zero-knowledge proof，只證明條件成立、不交出其他資料的密碼學方法）在那一版是非強制的「SHOULD」。9 月 2 日發布的 1.1.0 版裡，App 與網站都必須實作零知識證明，裝置不支援時才退回一般驗證方式。

## 導讀觀點 {#perspective}

匿名的年齡驗證裡，網站只得知「年齡符合」，發證的一方也不會得知你去過哪些網站。發證方依規格書的建議同時提供 App，EDRi 據此認為即使強制使用零知識證明也做不到嚴格的不可連結。

1.1.0 版附的威脅模型裡，使用零知識證明時網站沒有能跟發證紀錄比對的資料，驗證時也不會連絡發證方。一般驗證方式的串連風險列為可接受，理由是需要受監管的發證方刻意違規保留紀錄，再加上網站配合。

示範 App 以 EUPL-1.2 授權開源，執委會在建議書裡也請各國透過第三方審查確保資安與隱私合規。依 EDRi 的分析，開源要求只涵蓋數位身分錢包，丹麥的年齡驗證 App 在用戶端就有專有（非開源）的程式碼。

依 EDRi 的分析，App 以國家證件搭配生物辨識確認使用者，沒有證件、合適的手機或不願做臉部辨識的人會被排除。規格書列出的取得方式另有電子身分系統與銀行、電信業者的身分驗證。缺少證件的人，公平性（Equity）條款裡另有替代程序或人工處理。

澳洲從 2025 年 12 月 10 日起要求社群平台採取合理措施，阻止 16 歲以下的人持有帳號。依澳洲的法律，平台不得強迫使用者出示政府證件或使用政府認證的數位身分，列為選項時要另外提供合理的替代方式。eSafety 在說明頁寫明這是延後持有帳號，16 歲以下的使用者與家長不受罰。

讀者目前不需要做任何設定。各國的 App 依建議要在年底前上線，屆時可以留意採用的規格版本。比較各地做法時可以問同一組問題：零知識證明是否強制、發證與出示是否分開、App 是否開源、不出示證件的人有沒有替代方式。
