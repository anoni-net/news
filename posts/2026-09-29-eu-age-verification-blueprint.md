---
title: 歐盟年齡驗證藍圖的隱私缺口
description: 歐盟推動各國在年底前推出年齡驗證 App。依 EDRi 的技術分析，不可連結性被放寬、憑證仍能追溯到使用者，沒有證件的人也會被排除在外。
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
  - title: Social media age restrictions
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions
    publisher: eSafety Commissioner
    date: 2026-09-15
  - title: Under-16
    url: https://www.mcmc.gov.my/en/onsa/under-16
    publisher: Malaysian Communications and Multimedia Commission
watch:
  - date: 2027-01-05
    note: 各會員國的年齡驗證 App 是否在年底前上線，EU KIDS Act 草案的審議進度
authors:
  - anoni-net
---

歐盟執委會在 4 月宣布年齡驗證 App 技術就緒，並建議各會員國在年底前推出。9 月 17 日提出的《EU KIDS Act》草案要求線上服務與 App 商店採用年齡確認工具，13 歲以下不得使用社群平台，15 歲才能自己開帳號。歐洲數位權利組織 EDRi 在 9 月 7 日發表的技術分析，結論是這套工具在「就緒」與「保護隱私」兩方面都做不到。這套 App 只在歐盟推行，歐盟以外的使用者不會用到。

執委會 2025 年 7 月先發布一份藍圖，讓各國據此開發自己的 App。各國的 App 又稱「迷你錢包」，技術規格沿用各國在 2026 年底前要提供的歐盟數位身分錢包。依 EDRi 的分析，27 個會員國可能做出 27 種設計、技術與隱私保護都不同的 App。

法律要求在相關情況下「確保」不可連結性（unlinkability，每次出示的年齡證明無法被串回同一個人）。依 EDRi 的分析，執委會把這項要求改成「阻礙」連結，追蹤會變難，但不保證做不到。App 以國家核發的證件為信任來源，再用臉部辨識綁定使用者，沒有證件、沒有合適的手機或不願做臉部辨識的人都會被排除。

EDRi 引用的規格書條文裡，零知識證明（zero-knowledge proof，只證明條件成立、不交出其他資料的密碼學方法）都寫成非強制的「SHOULD」。即使一次發給多張憑證，憑證裡仍有鹽值、雜湊、公鑰、簽章與時間戳，發證方可以據此追溯到使用者。規格書 9 月 2 日合併的 1.1.0 版裡，零知識證明已改列為首選的機制，不用零知識證明的一般驗證方式保留作為備援。

## 導讀觀點 {#perspective}

匿名的年齡驗證裡，網站只得知「年齡符合」，發證的一方也不會得知你去過哪些網站，兩邊都靠不可連結性保護。照規格書的建議，發證方也同時提供 App。依 EDRi 的分析，發證與出示因此集中在同一方手上，就算強制使用零知識證明，也不足以做到嚴格的不可連結。

執委會的示範 App 以 EUPL-1.2 授權開源，但依 EDRi 的分析，開源的要求只適用於各國的數位身分錢包，不包括各國的年齡驗證 App。丹麥的 App 在用戶端就有專有（非開源）的程式碼，外界無法檢驗。

亞太地區的澳洲從 2025 年 12 月 10 日起要求社群平台阻止 16 歲以下的人開帳號，法律同時禁止平台強迫使用者出示政府證件或使用政府的數位身分。馬來西亞從 2026 年 6 月 1 日起，也依法要求社群平台驗證使用者的年齡。

這套 App 目前不需要讀者做任何設定。關注年齡驗證立法的人，可以拿 EDRi 列出的幾點檢驗各地的做法，包括零知識證明是否強制、發證與出示是否分開、App 是否開源，以及有沒有不需要證件與臉部辨識的替代方式。
