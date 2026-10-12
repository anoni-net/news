---
title: Let's Encrypt 預設憑證的 64 天效期
description: Let's Encrypt 公告 2027 年 2 月 10 日起，預設簽發的憑證效期從 90 天縮短為 64 天。用它架站或自架服務的人，要確認自動更新不是寫死在固定天數，公告沒有針對一般瀏覽者的說明。
date: 2026-10-15T00:05:00+08:00
slug: letsencrypt-64-day-certs
categories:
  - encryption
sources:
  - title: 64-Day Certificate Lifetimes Coming Feb 2027
    url: https://letsencrypt.org/2026/10/07/64-day-certs.html
    publisher: Let's Encrypt
    date: 2026-10-07
  - title: Decreasing Certificate Lifetimes to 45 Days
    url: https://letsencrypt.org/2025/12/02/from-90-to-45.html
    publisher: Let's Encrypt
    date: 2025-12-02
  - title: Shorter Certificate Lifetimes and Rate Limits
    url: https://letsencrypt.org/2026/02/24/rate-limits-45-day-certs.html
    publisher: Let's Encrypt
    date: 2026-02-24
  - title: ACME Renewal Information (ARI) Published as RFC 9773
    url: https://letsencrypt.org/2025/09/16/ari-rfc.html
    publisher: Let's Encrypt
    date: 2025-09-16
  - title: "Ballot SC081v3: Introduce Schedule of Reducing Validity and Data Reuse Periods"
    url: https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/
    publisher: CA/Browser Forum
    date: 2025-04-11
  - title: Let's Encrypt cuts certificate lifetimes to 64 days starting February 2027
    url: https://arstechnica.com/gadgets/2026/10/lets-encrypt-cuts-certificate-lifetimes-to-64-days-starting-february-2027/
    publisher: Ars Technica
    date: 2026-10-08
  - title: Why ninety-day lifetimes for certificates?
    url: https://letsencrypt.org/2015/11/09/why-90-days.html
    publisher: Let's Encrypt
    date: 2015-11-09
  - title: ACME Client Implementations
    url: https://letsencrypt.org/docs/client-options/
    publisher: Let's Encrypt
  - title: Profiles
    url: https://letsencrypt.org/docs/profiles/
    publisher: Let's Encrypt
  - title: certbot/CHANGELOG.md
    url: https://github.com/certbot/certbot/blob/main/certbot/CHANGELOG.md
    publisher: GitHub
  - title: 重要通知─配合國際規範 TWCA SSL / TLS 憑證調整重要通知
    url: https://www.twca.com.tw/news_detail/04f741de-2258-431d-be3a-992268cd5d72
    publisher: TWCA
    date: 2025-12-02
watch:
  - date: 2027-02-11
    note: Let's Encrypt 是否如期在 2 月 10 日改發 64 天憑證，有沒有更新失敗的大規模災情
authors:
  - anoni-net
---

Let's Encrypt 10 月 7 日公告，2027 年 2 月 10 日起簽發與更新的憑證，預設效期從 90 天縮短為 64 天。最後一張 90 天憑證預計 2027 年 5 月 11 日到期，現有的有效憑證不會被撤銷。公告只對架站與自架服務的人提出要求，沒有針對一般瀏覽者的說明。

測試環境（staging）10 月 14 日先改發 64 天憑證，Let's Encrypt 建議正式生效前先在這裡測試。依 2025 年 12 月的公告，2028 年 2 月 16 日預設效期會再縮短為 45 天。想提早改用的人，現在就可以選 45 天或 6 天的憑證類型（profile，申請時指定的一組憑證規格）。

Let's Encrypt 寫明縮短效期是為了降低金鑰外洩與憑證誤發的風險。CA/Browser Forum（憑證機構與瀏覽器廠商共同制定憑證規範的組織）2025 年 4 月通過的決議，把憑證效期上限從 398 天逐步縮短，2026 年 3 月 15 日起 200 天、2027 年 3 月 15 日起 100 天、2029 年 3 月 15 日起 47 天。64 天比 2027 年的上限更短，本文依兩份公告的時程推論，這是 Let's Encrypt 在 2029 年 47 天上限之前自訂的中間階段。

## 導讀觀點 {#perspective}

憑證用來證明「這個網站就是它聲稱的那一個」，金鑰外洩或被誤發的憑證，在到期之前都可能被拿來冒充網站。效期越短，出事之後能被冒用的時間就越短（依 Let's Encrypt 2015 年的說明，這也是當初選擇 90 天的理由之一）。代價是更新變得更頻繁，Let's Encrypt 2 月的說明預期效期縮到 45 天時每天的更新請求會倍增。2025 年 12 月的公告寫明不建議手動更新，10 月的公告也寫明速率限制不受影響。

負責申請與更新憑證的程式稱為 ACME 用戶端，例如 Certbot。已經自動更新、而且用戶端支援 ARI（ACME Renewal Information，讓憑證機構告訴用戶端何時該更新的機制，2025 年成為 RFC 9773）的人，依公告不必做任何改動，Certbot 從 2025 年 6 月的 4.1.0 版起預設會檢查 ARI。把更新時間寫死在固定天數的人，Let's Encrypt 建議改成在效期約三分之二時更新。不確定有沒有寫死的，可以在排程、腳本與作業手冊裡找 83、80、60 這類數字。

臺灣網路認證（TWCA）2025 年 12 月配合 CA/Browser Forum 的決議公告，自 2026 年 3 月 9 日起憑證效期設為 198 天，一年要申請兩次。

用 Let's Encrypt 架站的讀者現在可以先確認用戶端是否支援 ARI，10 月 14 日之後用測試環境執行一次更新，並照公告的建議加上更新失敗的通知。只能透過網頁介面手動上傳憑證的設備，公告沒有專門的說明。依本文推算，每張憑證用滿 64 天一年也要換 6 次，照公告建議在約三分之二時更換約要 9 次。Let's Encrypt 的用戶端清單頁說明不列瀏覽器內的 ACME 用戶端，理由是它們鼓勵手動更新，會增加漏掉更新的風險。
