---
title: SimpleX 支持者徽章的付款與身分
description: SimpleX Chat 販售支持者徽章，購買者可以傳送更大的檔案。依設計，SimpleX 無法從出示的徽章得知是哪一筆購買，但信用卡付款與同一週到期的分組仍會留下線索。
date: 2026-11-23T00:00:00+08:00
slug: simplex-supporter-badges
categories: [finance]
watch:
  - date: 2026-12-21
    note: 白皮書列為計畫的轉移功能是否實作，也就是在網頁用信用卡或加密貨幣買的徽章能否轉移到新裝置
sources:
  - title: SimpleX Supporter Badges — Send Larger Files That Stay Available Longer, Without Being Identified
    url: https://simplex.chat/blog/20260919-simplex-supporter-badges.html
    publisher: SimpleX Chat
    date: 2026-09-19
  - title: SimpleX Supporter Badges
    url: https://github.com/simplex-chat/simplex-chat/blob/master/docs/protocol/badges-overview.md
    publisher: SimpleX Chat
    date: 2026-10-22
  - title: Supporter badges
    url: https://simplex.chat/docs/guide/supporter-badges.html
    publisher: SimpleX Chat
  - title: Releases · simplex-chat/simplex-chat
    url: https://github.com/simplex-chat/simplex-chat/releases
    publisher: GitHub
  - title: The Privacy Pass Architecture
    url: https://www.rfc-editor.org/rfc/rfc9576.html
    publisher: IETF
authors:
  - anoni-net
---

SimpleX 的公告寫到，其他通訊軟體的付費功能附在帳號上，營運者因此知道是誰付了錢、用這項功能做什麼。SimpleX Chat 9 月起販售支持者徽章，購買者傳送的檔案上限從 1 GB 提高到 2 GB（傳奇等級 5 GB），檔案在伺服器上也保存得更久（支持者 7 天、傳奇 21 天）。SimpleX 的網路沒有使用者帳號，徽章改用匿名憑證（anonymous credential）證明持有者付過錢、不透露是誰。到 11 月 21 日，SimpleX Chat App 的 7.1 版已經包含這項功能。

依 SimpleX 的技術白皮書，徽章是一份 BBS 簽章（一種還在制定中的數位簽章規格），由 SimpleX 營運的徽章服務簽發、存在使用者自己的裝置上。App 每次向聯絡人或伺服器出示徽章時，都用它產生一份新的零知識證明（zero-knowledge proof）。零知識證明的作用像是只證明「年滿 18 歲」、不交出整張證件，本站整理[歐盟年齡驗證 App](https://anoni.net/news/2026/09/eu-age-verification-blueprint/) 時也寫過這項技術。聯絡人與伺服器營運者因此只能取得徽章類型與到期日，無法把兩次出示連在一起，也無法連回購買。

SimpleX 的公告寫到，憑證每次只簽發一個月，所有徽章都在一週裡的同一天到期。持有者因此隱身在那一週到期的所有支持者之中。依白皮書，App 每月換新憑證時會把申請新憑證與向聯絡人顯示新徽章排在不同天，讓旁人難以從時間認出持有者。

## 導讀觀點 {#perspective}

網際網路標準組織 IETF 制定的 Privacy Pass 是另一種做法，使用者通過一次驗證取得權杖（token），出示時不必透露身分。依白皮書，這類權杖出示一次就作廢，也不帶到期日與類型。徽章要在每段對話、每次連線一再出示，SimpleX 因此選用可以重複產生新證明的 BBS 簽章。

依白皮書，徽章服務保存每筆購買的付款紀錄，信用卡付款也像其他服務一樣會連到這筆購買。同一週到期的徽章到期日相同，伺服器營運者能把這些支持者的連線歸成一組，持有者隱身其中的人數取決於那一週有多少人到期。剛購買或剛用代碼兌換的徽章會立刻顯示，在徽章服務自己的群組裡領代碼的人，SimpleX 可以從新徽章出現的時間推測是誰兌換。Google Play 的訂閱換裝置時用 Restore purchases（把商店裡的訂閱移到目前個人檔案的功能）搬移，SimpleX 能把前後兩筆購買連在一起，但無法連到持有它們的個人檔案。

從 Google Play 安裝的 Android 版可以在 App 內付款，有單月方案，以及每月、每年自動續訂的方案。iOS 版、從 F-Droid 或 GitHub 安裝的版本與桌面版會開啟瀏覽器的購買頁，用信用卡、Bitcoin 或 Monero 付款後取得一組代碼，貼進 App 的設定就能換成徽章。白皮書寫到，想讓付款本身保密的人可以改用加密貨幣。在網頁購買的徽章不會自動續訂，到 11 月 21 日也還不能搬到新裝置。

徽章只加在一個個人檔案上，匿名（incognito）個人檔案不顯示徽章。徽章無法撤銷，裝置或備份被入侵時，取得徽章資料的人可以一直用到期滿。購買多個月份的，入侵者還能向徽章服務申請剩下月份的新憑證。
