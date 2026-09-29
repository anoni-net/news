---
title: 歐盟年齡驗證 App 的隱私設計與爭議
description: 歐盟執委會建議各會員國在 2026 年底前推出年齡驗證 App，歐盟以外的使用者不受影響。執委會寫明 App 不保留證件與生物特徵資料，EDRi 則質疑它的隱私保護。依執委會 9 月發布的新版規格，App 與網站都必須實作零知識證明，只在裝置不支援時退回發證方可能追溯的一般驗證方式。
date: {created: 2026-09-29T07:00:00+08:00, updated: 2026-09-29T16:08:00+08:00}
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

歐盟執委會在 4 月宣布年齡驗證 App 技術就緒，建議各會員國年底前推出自己的 App。依 9 月 17 日提出的《EU KIDS Act》草案，13 歲以下不得使用社群平台，15 歲才能自己開帳號。線上服務與 App 商店要採用年齡確認工具，這套 App 是選項之一，歐盟以外的使用者用不到。

依執委會的新聞稿，社群與影音平台要在新開帳號時驗證年齡，既有帳號改用帳號建立日期、信用卡資料等合理的替代指標推估年齡。13 到 15 歲由家長設立迷你帳號（mini accounts），每天最多使用一小時。執委會規格書附的威脅模型裡，成年人在旁代為驗證或替孩子的手機註冊列為可接受的殘餘風險，每次出示都比對臉部的做法因過度侵犯隱私被否決。

依執委會的說明頁與新聞稿，使用者不必分享其他個人資料就能證明年滿 18 歲，App 也不保留身分證件與生物特徵資料。年齡驗證 App 的暱稱是迷你錢包（mini wallet），技術規格沿用歐盟數位身分錢包。

歐洲數位權利組織 EDRi 在 9 月 7 日發表技術分析，結論是這套工具在「就緒」與「保護隱私」兩方面都做不到，並主張拒絕建置年齡驗證。分析裡寫到，數位身分錢包依法要在相關情況下「確保」不可連結性（unlinkability，多次出示無法串回同一個人），執委會把要求改成只需「阻礙」連結。

執委會 9 月 2 日發布的 1.1.0 版規格書裡，App 與網站都必須實作零知識證明（zero-knowledge proof，只證明條件成立、不交出其他資料的方法），裝置不支援時才退回一般驗證方式。EDRi 引用的是更早、零知識證明仍非強制的版本。一般驗證方式下，發證方保留紀錄並與網站串通就能追溯使用者。

## 導讀觀點 {#perspective}

執委會的威脅模型裡，使用零知識證明時網站沒有可比對發證紀錄的資料。一般驗證方式的追溯風險列為可接受，理由是發證方列在執委會信任清單上並受各國監管。依 EDRi 的分析，規格書建議發證方同時提供 App，讓發證與出示集中在同一方。分析的結論是即使強制零知識證明，也做不到嚴格的不可連結。

依 EDRi 的分析，App 以國家證件搭配生物辨識確認使用者，沒有證件、合適的手機或不願做臉部辨識的人會被排除。執委會的規格書另列電子身分系統與銀行、電信業者的身分驗證，威脅模型裡只有掃描證件要做臉部比對。缺少證件的人另有規格書公平性（Equity）條款的替代程序或人工處理。

執委會的示範 App 以 EUPL-1.2 授權開源，建議書裡請各國透過第三方審查確保資安與隱私合規。依 EDRi 的分析，開源要求只涵蓋數位身分錢包，丹麥的 App 在用戶端就有非開源的程式碼。

澳洲從 2025 年 12 月 10 日起要求社群平台採取合理措施，阻止 16 歲以下的人持有帳號。在排除的爭點上，澳洲的法律禁止平台強迫出示政府證件，列為選項時要另有合理的替代方式。沒做到的平台可能受罰，16 歲以下的使用者與家長不受罰。

讀者目前不必做設定，身在歐盟的人可以留意各國 App 的規格版本。比較各地做法時，隱私方面可以問發證方能不能追溯使用者、App 是否開源、沒有證件的人有沒有替代方式。兒少保護方面可以問未成年人能不能輕易繞過驗證。
