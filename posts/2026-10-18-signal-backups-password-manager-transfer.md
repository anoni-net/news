---
title: Signal 的跨平台加密備份與 Android 的密碼管理器搬移
description: Signal 9 月 28 日發布 iOS 8.30，加密備份 Signal Secure Backups 可以在 Android 與 iPhone 之間還原，換手機時能把對話帶到另一個平台。Google 9 月在 Android 推出密碼管理器之間的搬移流程，不必匯出檔案，公告列出四款支援的密碼管理器。
date: 2026-10-18T12:00:00+08:00
slug: signal-backups-password-manager-transfer
categories:
  - mobile
sources:
  - title: "Back to Backups: A Year in Review"
    url: https://signal.org/blog/backup-improvements/
    publisher: Signal
    date: 2026-09-28
  - title: Signal Secure Backups
    url: https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backups
    publisher: Signal
  - title: Signal 安全備份
    url: https://support.signal.org/hc/zh-tw/articles/9708267671322
    publisher: Signal
  - title: Backups and Device Transfers on Signal
    url: https://support.signal.org/hc/en-us/articles/10074659364122-Backups-and-Device-Transfers-on-Signal
    publisher: Signal
  - title: Troubleshooting Signal Secure Backups
    url: https://support.signal.org/hc/en-us/articles/10075139325850-Troubleshooting-Signal-Secure-Backups
    publisher: Signal
  - title: iOS to iOS Device Transfer
    url: https://support.signal.org/hc/en-us/articles/10045771316762-iOS-to-iOS-Device-Transfer
    publisher: Signal
  - title: Switching password managers is easy and safe on Android
    url: https://blog.google/products-and-platforms/platforms/android/switch-password-managers/
    publisher: Google
    date: 2026-09-10
  - title: Credential transfer
    url: https://developer.android.com/identity/sign-in/credential-transfer
    publisher: Android Developers
  - title: Import or export passwords and passkeys with Chrome
    url: https://support.google.com/chrome/answer/13068232?co=GENIE.Platform%3DAndroid
    publisher: Google
  - title: Android offers password manager switching tool
    url: https://freedom.press/digisec/blog/android-offers-password-manager-switching-tool/
    publisher: Freedom of the Press Foundation
    date: 2026-09-16
  - title: "Password managers on Android: Switch without manual export"
    url: https://www.heise.de/en/news/Password-managers-on-Android-Switch-without-manual-export-11450892.html
    publisher: heise online
    date: 2026-09-11
  - title: Credential Exchange Format
    url: https://fidoalliance.org/specs/cx/cxf-v1.0-ps-20250814.html
    publisher: FIDO Alliance
    date: 2025-08-14
  - title: ASCredentialExportManager
    url: https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager
    publisher: Apple
  - title: What’s new in passkeys
    url: https://developer.apple.com/videos/play/wwdc2025/279/
    publisher: Apple
    date: 2025-06-09
  - title: Export passwords to another password manager on iPhone
    url: https://support.apple.com/guide/iphone/export-passwords-iphf28f2e93e/ios
    publisher: Apple
watch:
  - date: 2026-11-18
    note: Signal 支援中心對裝置上備份的平台範圍是否改成一致，Android 的搬移流程支援的密碼管理器是否增加，Apple 的 iPhone 使用手冊是否寫入 App 之間的傳輸步驟
authors:
  - anoni-net
---

Signal 9 月 28 日發布 iOS 8.30，部落格寫明從這一版起，加密備份可以在 Android、iOS 與桌面版之間建立與還原。支援中心寫明 Signal Secure Backups 能在 Android 與 iPhone 之間還原，換手機時可以把對話紀錄帶到另一個平台。Google 9 月 10 日也在 Android 推出密碼管理器之間的搬移流程，密碼與通行金鑰（passkey，取代密碼的登入方式）可以直接搬到另一款 App，不必先下載成檔案。公告寫明 Android 8 以上可用，列出 Google 密碼管理工具、1Password、Bitwarden 與 Dashlane 四款，之後還會增加。

Signal Secure Backups 由 Signal 代管，開啟時會產生一組 64 個字元的恢復金鑰（recovery key），支援中心寫明這組金鑰不會交給 Signal 的服務。金鑰遺失就再也無法還原備份，Signal 也無法協助找回。到 10 月 18 日為止，免費方案備份全部的文字訊息與最近 45 天的媒體檔案，每月 1.99 美元的付費方案可以存到 100 GB 的媒體。只能看一次的訊息，以及 24 小時內就會消失的訊息，都不會備份。

部落格寫明代管的備份每 24 小時產生一份新的，前一份自動刪除。支援中心寫明，備份只能在第一次設定 Signal 時還原，而且要用同一個電話號碼註冊。

新舊兩支手機都在手邊、又是同一個平台時，也可以用裝置間轉移。對話紀錄會從舊手機移到新手機，舊手機不保留。部落格寫明 iOS 8.30 改用 Wi-Fi Aware 在兩支 iPhone 之間建立端對端加密的區域連線，速度與穩定度都提高。

另一種是存在自己裝置上的備份檔，部落格寫 Android、iOS 與桌面版都能建立，格式跨平台。到 10 月 18 日為止，支援中心各頁的寫法跟部落格不同，彼此也不一致。10 月 11 日更新的備份與轉移說明頁寫三個平台都有、但只能在同一個平台還原，10 月 3 日更新的疑難排解頁則寫只限 Android 之間。備份與轉移說明頁和桌面版備份頁都寫明，Android 或桌面版的備份檔不能在 iPhone 還原。

Google 的公告寫明，Android 的密碼搬移從新的密碼管理器開始，在新 App 選擇從其他服務匯入。Android 會列出手機上可以匯出的密碼管理器，使用者接著在舊的那款裡選擇要搬的項目並授權。Google 的開發者文件寫明，搬移在同一支手機的兩個 App 之間進行，原始的憑證不會暴露給 Android 系統或未經驗證的 App。文件也寫明採用 FIDO 聯盟（制定通行金鑰等登入標準的產業組織）的憑證交換格式（Credential Exchange Format，CXF），密碼、通行金鑰、地址與自訂欄位都能搬。

Apple 在 iOS 26 與 macOS 26 為密碼管理器的開發者提供同類的匯出與匯入 API，開發者文件寫明由作業系統居中確認雙方 App 的身分，過程不寫入任何檔案。WWDC25 的開發者工作階段寫明，資料格式是跟 FIDO 聯盟的成員合作制定。Apple 支援中心的 iPhone 使用手冊裡，密碼匯出與匯入的兩頁到 10 月 18 日為止都只寫 CSV 檔的做法，匯出頁並警告匯出的密碼沒有加密。

## 導讀觀點 {#perspective}

Signal 的備份由使用者手上的恢復金鑰加密，支援中心寫明沒有這組金鑰，包括 Signal 在內都無法讀取或還原備份。iCloud 備份也帶不走 Signal 的對話，支援中心寫明 iCloud 備份跟 Signal 不相容。

Signal Secure Backups 另外加了一把每天更換的輔助金鑰，存放在 Signal 代管服務那一端的可信執行環境（TEE，處理器裡隔離出來的安全區）。部落格寫明這把金鑰沒有恢復金鑰就解不開備份，唯一的用途是提供前向保密（forward secrecy，日後金鑰外洩時，過去的資料仍無法被解開）。存在自己裝置上的備份，部落格寫明無法用同一套 TEE 提供前向保密。部落格也寫明，TEE 是目前保護這把金鑰最好的方式，之後可能隨研究進展而改變。

Google 的公告寫明，以前搬密碼要先下載成沒有加密的文字檔，通行金鑰則完全無法搬移。Apple 的開發者文件寫明，新的搬移過程不寫入檔案系統。Android 的開發者文件寫明，兩個 App 之間用受保護的內容網址（Content URI）傳遞，背後是暫存的快取檔。文件寫的理由是整個密碼庫可能超過 Android 程序之間單次傳輸 1MB 的上限。

密碼能不能整個搬過去，heise 的報導寫明要看新舊兩個 App 是否都實作了這套標準。Google 的說明頁寫明，匯入到 Google 密碼管理工具時要登入另一款密碼管理器，匯入通行金鑰時可能還要輸入恢復金鑰。說明頁也提醒，匯入前要確認信任對方的密碼管理器。

打算換手機的 Signal 使用者，可以在舊手機的 Signal 設定裡開啟備份，把恢復金鑰存好再換機。支援中心有正體中文版，說明頁與 Android、iOS 原始碼的正體中文翻譯都寫作「恢復金鑰」。金鑰可以存進密碼管理器或手動保存，存進密碼管理器的人，換機時要能在新手機或其他裝置打開密碼管理器（本文依設定流程推論）。Signal Secure Backups 保護的是手機遺失或換平台時的對話紀錄，換電話號碼時無法還原，部落格也提醒恢復金鑰不要交給任何人。

想在 Android 換一款密碼管理器的人，打開新的 App 找匯入的選項，新舊兩款都要支援這套流程。Google 9 月 10 日的公告列出的是 Google 密碼管理工具、1Password、Bitwarden 與 Dashlane。匯入到 Google 密碼管理工具時，Google 的說明頁寫明要用手機的螢幕鎖定驗證身分。iPhone 使用者用 CSV 檔搬移時，Apple 的使用手冊警告匯出的檔案沒有加密，任何取得檔案的人都能讀到內容。
