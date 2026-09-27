---
title: 歐盟年齡驗證藍圖的隱私缺口
description: 歐盟推動各國年底前推出年齡驗證 App，EDRi 的技術分析指出，不可連結性被放寬、憑證仍能追溯到使用者，沒有證件的人也會被排除在外。
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
authors:
  - anoni-net
---

歐盟執委會在 4 月宣布年齡驗證 App 技術就緒，並建議各會員國在年底前推出。9 月 17 日提出的《EU KIDS Act》草案要求線上服務與 App 商店採用年齡確認工具，13 歲以下不得使用社群平台，15 歲才能自己開帳號。歐洲數位權利組織 EDRi 在 9 月 7 日發表技術分析，指出這套號稱「就緒」、「保護隱私」的工具兩者都做不到。

執委會 2025 年 7 月先發布的是一份藍圖，讓各國據此開發自己的 App，又稱「迷你錢包」，技術規格沿用各國 2026 年底前要提供的歐盟數位身分錢包。EDRi 擔心，27 個會員國可能做出 27 種設計、技術與隱私保護都不同的 App。

EDRi 指出，法律要求在相關情況下「確保」不可連結性，執委會卻改成「阻礙」連結，讓追蹤變難，但不保證做不到。App 以國家核發的證件為信任來源，再用臉部辨識綁定使用者，沒有證件、沒有合適的手機或不願做臉部辨識的人都會被排除。

EDRi 也寫到，規格書提到零知識證明時都用非強制的「SHOULD」。即使一次發給多張憑證，憑證裡仍有鹽值、雜湊、公鑰、簽章與時間戳，發證方可以據此追溯到使用者。規格書在 9 月 2 日合併的 1.1.0 版已把零知識證明改成首選，但保留不用零知識證明的一般驗證方式作為備援。

## 導讀觀點 {#perspective}

年齡驗證要做到匿名，關鍵在不可連結性，網站只知道「年齡符合」，發證的一方也不知道你去了哪些網站。零知識證明可以證明條件成立而不交出其他資料，但規格書建議發證方同時提供 App，EDRi 認為這把發證與出示集中在同一方手上，光是強制零知識證明也不足以做到嚴格的不可連結。

執委會的示範 App 以 EUPL-1.2 授權開源。EDRi 指出，開源的要求只適用於各國的數位身分錢包，不包括各國的年齡驗證 App，丹麥的 App 在用戶端就有專有程式碼，外界無法檢驗。

亞太地區也在走類似的路。澳洲 2025 年 12 月 10 日起要求社群平台阻止 16 歲以下的人開帳號，但法律禁止平台強迫使用者出示政府證件或使用政府的數位身分。馬來西亞從 2026 年 6 月 1 日起，也依法要求社群平台驗證使用者的年齡。

關注年齡驗證立法的人，可以拿 EDRi 列出的幾點檢驗各地的做法。例如零知識證明是否強制、發證與出示是否分開、App 是否開源，以及有沒有不需要證件與臉部辨識的替代方式。
