---
title: Tuta 加密郵件與 Nextcloud 的整合
description: Tuta 與 Nextcloud 10 月 1 日推出整合，可以在 Nextcloud 裡使用 Tuta，把收到的附件存進 Nextcloud、在 Tuta 行事曆建立 Nextcloud Talk 會議連結。App 要由 Nextcloud 管理員安裝，到 10 月 18 日為止，兩家的公告都沒有交代附件存進 Nextcloud 之後的加密狀態。
date: 2026-10-18T13:59:00+08:00
slug: tuta-nextcloud-integration
categories:
  - encryption
sources:
  - title: The Tuta app has landed in the Nextcloud App Store!
    url: https://tuta.com/blog/tuta-app-on-nextcloud
    publisher: Tuta
    date: 2026-10-01
  - title: Tuta brings end-to-end encrypted email service to Nextcloud
    url: https://nextcloud.com/blog/press_releases/tuta-brings-end-to-end-encrypted-email-service-to-nextcloud/
    publisher: Nextcloud
    date: 2026-10-01
  - title: Tuta brings encrypted email to Nextcloud with new free integration
    url: https://cyberinsider.com/tuta-brings-encrypted-email-to-nextcloud-with-new-free-integration/
    publisher: CyberInsider
    date: 2026-10-01
  - title: Tuta Mail
    url: https://apps.nextcloud.com/apps/tutamail
    publisher: Nextcloud
  - title: tutao/tutanota
    url: https://github.com/tutao/tutanota
    publisher: GitHub
  - title: Tuta Mail
    url: https://github.com/tutao/tutanota/blob/master/integrations/nextcloud/tutamail/README.md
    publisher: GitHub
  - title: Encryption
    url: https://tuta.com/encryption
    publisher: Tuta
  - title: Create a secure email account with Tuta Mail
    url: https://tuta.com/pricing
    publisher: Tuta
  - title: Server-side Encryption
    url: https://docs.nextcloud.com/server/latest/admin_manual/configuration_files/encryption_configuration.html
    publisher: Nextcloud
  - title: Constants
    url: https://nextcloud-talk.readthedocs.io/en/latest/constants/
    publisher: Nextcloud
  - title: Conversations management
    url: https://nextcloud-talk.readthedocs.io/en/latest/conversation/
    publisher: Nextcloud
  - title: Nextcloud Talk
    url: https://nextcloud.com/talk/
    publisher: Nextcloud
watch:
  - date: 2026-11-18
    note: Tuta 或 Nextcloud 是否說明附件存進 Nextcloud 之後的加密狀態、外掛按鈕是否有正體中文、Tuta 是否推出其他官方外掛
authors:
  - anoni-net
---

加密郵件服務 Tuta 與開源協作平台 Nextcloud 10 月 1 日推出整合，Tuta 的公告把它定位為免費。整合分成兩部分，一是 Nextcloud App Store 裡的 Tuta Mail App，裝好之後可以在 Nextcloud 裡使用 Tuta 的網頁版。二是 Tuta 裡的 Nextcloud 外掛，可以把收到的附件一鍵存進 Nextcloud，或在建立 Tuta 行事曆活動時產生 Nextcloud Talk 的會議連結。兩項功能都要自己的 Nextcloud 裝了 Tuta Mail App 才能用（App Store 網頁列出 Nextcloud 33 到 35 版），自架的由管理員安裝，託管的要由服務供應商開放。

依 Tuta 的公告，外掛由 Tuta 帳號的管理員在設定的「Plugins」頁為所有使用者啟用，單人帳號就是自己帳號的管理員。Tuta 在 GitHub 的說明檔列出兩個設定欄位，Nextcloud 的網址與存放附件的資料夾名稱。兩項功能在 Nextcloud 裡、網頁、桌面與手機版的 Tuta 都能使用。依 Nextcloud 的新聞稿，這項整合讓個人與小型企業更容易自架 Nextcloud，郵件交給 Tuta 處理。

到 10 月 18 日為止，Tuta 的公告與定價頁都沒有提到需要哪個方案。Tuta 的 App 有正體中文介面。從 10 月 18 日 Tuta 公開的原始碼來看，正體中文語言檔已有「外掛程式」頁的字串，Nextcloud 外掛自己的設定欄位與「Save to Nextcloud」這類按鈕只有英文與德文。

## 導讀觀點 {#perspective}

Tuta 的加密頁提到，郵件連同主旨與所有附件都端對端加密，金鑰不會交給包括 Tuta 在內的任何人。附件存進 Nextcloud 之後的加密狀態，兩家的公告都沒有說明，本文讀了 10 月 18 日 Tuta 公開的原始碼。存檔按鈕在儲存附件的對話框裡，外掛用 Nextcloud 的檔案存取介面（WebDAV）上傳，傳送前沒有另外加密。依此推論，上傳的是解密後的檔案，存進 Nextcloud 時已經離開 Tuta 的端對端加密。

Nextcloud 的管理手冊區分兩種加密。伺服器端加密由伺服器執行、金鑰也在伺服器上，手冊提醒它擋不住被入侵的伺服器或惡意的管理員。端對端加密則由 Nextcloud 的桌面或手機用戶端在上傳前執行。外掛不經過 Nextcloud 的用戶端上傳，附件在 Nextcloud 上受到多少保護，取決於那台伺服器的設定與管理者（本文依手冊與原始碼的推論）。

外掛產生的 Talk 會議，依原始碼建立的是公開房間，Talk 的 API 文件把公開房間列為允許訪客加入的對話。Nextcloud 的產品頁提到 Talk 支援端對端加密通話，範圍是網頁與新的桌面用戶端，但沒有說明公開房間是否適用。

已經使用 Nextcloud、又用 Tuta 收信的人或團隊，先由 Nextcloud 管理員安裝 Tuta Mail App，再由 Tuta 帳號的管理員啟用外掛。依管理手冊，伺服器端加密擋不住伺服器的管理者。處理敏感附件前，可以先確認有哪些人具備那台伺服器的管理權限。依原始碼與 Talk 的文件，外掛建立的是允許訪客的公開房間，取得連結的人可以用訪客身分加入。
