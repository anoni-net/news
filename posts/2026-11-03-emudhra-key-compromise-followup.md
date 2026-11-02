---
title: eMudhra 弱私鑰事件的後續處置與 macOS 命令列工具
description: 印度憑證機構 eMudhra 八張中繼憑證的私鑰被算出之後，Apple、Microsoft 與 Chrome 都已封鎖或移除相關憑證，一般使用者的瀏覽器、手機與電腦不必另外設定。macOS 內建的 git、curl 等命令列工具仍可能接受這些憑證，到 11 月 2 日還沒有查到 Apple 的修正。eMudhra 宣布退出公開 TLS 憑證業務，到 11 月 1 日還沒在事故單提交正式事故報告。
date: 2026-11-03T00:05:00+08:00
slug: emudhra-key-compromise-followup
categories:
  - security
follows:
  - 2026-10-23-emudhra-weak-ca-keys
sources:
  - title: About the compromised eMudhra intermediate CAs
    url: https://support.apple.com/en-us/149555
    publisher: Apple
    date: 2026-10-29
  - title: "MC1529467 - Microsoft Windows: Updates to address compromised eMudhra certificate authority keys"
    url: https://mc.merill.net/message/MC1529467
    publisher: Microsoft 365 Message Center Archive
    date: 2026-10-28
  - title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
    publisher: Mozilla Bugzilla
    date: 2026-10-18
  - title: eMudhra Statement on Recent Certificate Security Incident
    url: https://emudhra.com/en/post/certificate-security-incident
    publisher: eMudhra
    date: 2026-10-20
  - title: Protecting Chrome and Android Users from Compromised eMudhra Intermediate CA Certificates
    url: https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/
    publisher: Google
    date: 2026-10-20
  - title: root_store.textproto
    url: https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.textproto
    publisher: Chromium
  - title: Apple's git still trusts the compromised eMudhra certificates
    url: https://emudhra.we-have-a-problem.com/apple.html
    publisher: emudhra.we-have-a-problem.com
    date: 2026-10-28
  - title: eMudhra Intermediate CA Compromise
    url: https://emudhra.we-have-a-problem.com/
    publisher: emudhra.we-have-a-problem.com
    date: 2026-10-20
  - title: Microsoft releases out-of-band Windows fixes with certificate updates
    url: https://www.theregister.com/a/5305637
    publisher: The Register
    date: 2026-10-27
watch:
  - date: 2026-11-17
    note: Apple 是否推出修正 /etc/ssl/cert.pem 的 macOS 更新，git、curl 等內建命令列工具是否已不接受受影響的憑證
  - date: 2026-11-20
    note: eMudhra 是否在 Bugzilla 2083449 提交正式事故報告，以及 Chrome、Mozilla、Microsoft 對 emSign Root CA - G1 的決定
authors:
  - anoni-net
---

印度憑證機構 eMudhra（憑證品牌 emSign）有八張中繼憑證的私鑰小到可以直接算出，取得私鑰的人能替不屬於自己的網站簽發 HTTPS 憑證。10 月中事件公開之後，Apple 與 Microsoft 陸續公布了各自的處置，Chrome 的信任清單也拿掉了相關的根憑證。一般使用者的瀏覽器、手機與電腦不必另外設定。依 Apple 10 月 29 日的支援文件，macOS 內建的 git、curl 等命令列工具在之後的軟體更新之前，仍可能接受這些憑證。

依 Apple 的支援文件，Apple 從 10 月 19 日起封鎖六張簽發 TLS 憑證的中繼。每張中繼各有兩份憑證，一份連到 eMudhra 的根憑證 emSign ECC Root CA - G3，另一份經 Sectigo 交叉簽署（另一家憑證機構的根再簽一份，讓同一張中繼多一條信任路徑）連到 Sectigo 的根 AAA Certificate Services。Apple 封鎖的是這 12 份憑證，10 月 23 日起也封鎖了 G3 根。封鎖透過憑證設定資料自動送到裝置，不必安裝軟體更新，Safari、Mail 與使用 Apple 網路與安全框架的 App 都會擋下。

同一份文件也提到，macOS 與 Xcode Command Line Tools 附的 curl、git、python3、ruby、perl 與 openssl，會拿 `/etc/ssl/cert.pem` 這個檔案驗證憑證。憑證連到檔案裡的根時，這些工具不檢查 Apple 的封鎖，也不檢查憑證有沒有被撤銷。Apple 寫這個檔案會在之後的 macOS 更新裡更新，沒有寫是哪個版本、什麼時候推出。

一位 Mozilla 工程師為事件架設了說明頁，10 月 28 日另外寫了一頁談 Apple 的工具。依該頁，10 月 26 日推出的 macOS 27.2 沒有修正問題，還讓使用者手動移除根憑證的處理失效。位在連線路徑上的攻擊者可以讓 git 從 `https://` 遠端取得攻擊者挑的程式碼，也能攔截 GitHub token 這類登入資訊。到 11 月 2 日，本文沒有查到 macOS 27.2 之後的修正版本。

Microsoft 10 月 28 日在 Microsoft 365 訊息中心的公告提到，Windows 的不信任憑證清單（Disallowed Certificate Trust List）已經封鎖受影響的憑證機構。Edge 與 WebView2（Windows App 內嵌網頁用的元件）另外透過元件更新收到 CRLSet，也就是在背景下載的封鎖清單，不必安裝新版瀏覽器。公告也寫到 Microsoft 已發布 Windows 與 Edge 的更新，從信任清單移除這些憑證階層的相關憑證，沒有寫 Edge 的日期。

依 Microsoft 訊息中心的公告與 The Register 引述的 Microsoft 安全回應中心（MSRC）部落格，Microsoft 10 月 26 日發布 Windows 的帶外更新（out-of-band，固定排程以外的更新），從 Windows 的信任清單移除七張跟受影響憑證階層相關的憑證。這份更新給無法連到 Microsoft 憑證更新服務、或停用自動更新信任清單的裝置，也帶著 10 月 13 日更新的已知問題。憑證清單通常經由更新服務送達，很多裝置不需要這份更新。

Google 10 月 20 日的部落格預告，Chrome Root Store 會在太平洋時間 10 月 27 日上午移除 emSign ECC Root CA - G3。本文查不到 Chrome 宣告完成的公告，11 月 2 日讀到的 Chromium 原始碼裡，Chrome Root Store 的清單已經沒有這張根。eMudhra 的另一張根 emSign Root CA - G1 仍在清單上，Mozilla 10 月 20 日也在事故單上寫當時不移除對 G1 的信任。Google 10 月 20 日的部落格寫正在評估 eMudhra 其他憑證是否繼續信任，到 11 月 2 日本文沒有查到結果。

Chrome 根憑證計畫（Chrome Root Program）10 月 27 日在事故單上回覆社群的提問，把 CRLSet 的封鎖與之後的事故單結案稱為緊急圍堵，之後還有後續的工作。依這則留言，Chrome 在通報後一小時內用 Google 的 `paranoid_crypto` 檢查了 Chrome 信任的所有 CA 憑證，沒有找到其他已知類型的弱金鑰。業界常用的檢查工具在事件之前，沒有檢查橢圓曲線私鑰過小的情況。Chrome 已在 CCADB（各家瀏覽器共用的憑證機構資料庫）的工具專案提出議題，要讓 CA 揭露憑證之前先通過弱金鑰檢查。

eMudhra 10 月 25 日在事故單上宣布退出公開 TLS 憑證業務，10 月 30 日任命 KPMG 為獨立的外部審查者。依 eMudhra 的事件聲明頁，領導層 10 月 26 日的說明寫問題出在自家的腳本錯誤，並承諾透過 CCADB 的程序公布完整的根本原因分析。10 月 28 日的更新寫到，G3 底下約 3 萬 800 張憑證屬於美國的單一客戶生態系，這個生態系已改用 eMudhra 的 G1 RSA 根簽發新憑證。eMudhra 也請各家根憑證計畫給時間讓這批客戶轉移，轉移完成後就停止從 G1 簽發 TLS 憑證。

Mozilla 根憑證計畫 10 月 20 日向 eMudhra 寄出問題清單，要求 24 小時內初步回覆，到 10 月 23 日還沒收到。eMudhra 10 月 23 日把延遲歸因於社群媒體與投資人、客戶的密集關注，Chrome 根憑證計畫回覆這不是可以接受的理由。eMudhra 10 月 25 日的留言主張，CCADB 的事故通報規定給 CA 14 天提交完整報告，自己仍在期限內。

之後 eMudhra 在 10 月 27 日的留言寫已經直接回覆 Mozilla 的問題，10 月 29 日在事故單附上給 Google 的回覆文件。到 11 月 1 日事故單的最後一則留言為止，eMudhra 還沒有在這張單上提交正式事故報告，事故單的狀態仍是處理中。

## 導讀觀點 {#perspective}

Chrome 的 CRLSet、Apple 的憑證設定資料與 Windows 的不信任憑證清單都在背景自動更新，可以單獨擋下特定的中繼憑證。macOS 內建的命令列工具只讀 `/etc/ssl/cert.pem` 一個檔案，檔案裡還有 G3 根與 Sectigo 的 AAA Certificate Services，連到這兩張根的憑證就會通過驗證。Apple 的文件寫這些工具不檢查撤銷，所以 eMudhra 在 UTC 10 月 18 日撤銷八張中繼，對它們沒有作用。

依一位研究者 10 月 25 日在事故單上的統計（本文沒有另外核對），UTC 10 月 20 日到 21 日之間有 107,107 張用其中六把金鑰簽出的憑證，被記進一家業者的憑證透明度日誌（CT log，公開記錄每一張憑證的日誌）。其中 106,050 張是只寫 google.com 的概念驗證憑證，106,058 張經由 Sectigo 的 AAA 交叉簽署連到根。這位研究者列出的例子裡有一張內嵌了三家日誌的收錄證明（SCT），三家都是 Chrome 列為可用的日誌，本文據此推論只要求 CT 收錄證明擋不下這類憑證。這些憑證幾乎都沒有撤銷資訊的指標，只檢查網站憑證本身撤銷狀態的程式也擋不下，只有逐層檢查 CA 憑證撤銷、收到推送的封鎖清單或已移除相關根憑證的程式會拒絕。

依 Apple 的文件，不用終端機的人不需要做任何事，在 Mac 上用內建的 git、curl 或 python3 連 `https://` 網址的人可以等 Apple 的更新。不想等的人可以依同一份文件，用管理員權限從 `/etc/ssl/cert.pem` 移除 emSign ECC Root CA - G3。只移除 G3 擋不下 Sectigo 交叉簽署的那六份，需一起移除 AAA Certificate Services。依同一份文件，代價是經由這張根、跟事件無關的部分網站，也可能在這些工具裡驗證失敗。

Apple 的文件另外提醒，macOS 更新可能換回原本的檔案。安裝到含修正的版本之前，每次更新後都要重新檢查。自帶根憑證清單的 App 與工具不讀這個檔案，也不套用 Apple 的封鎖，要向開發者確認。在 Mac 上手動移除根憑證，保護到的只有讀這個檔案的工具。

接下來可以留意 Apple 修正 `/etc/ssl/cert.pem` 的 macOS 更新、eMudhra 依 CCADB 程序提交的正式事故報告，以及各家根憑證計畫對 G1 根的決定。約 3 萬 800 張憑證所屬的客戶生態系已經改用 G1 簽發。本文推論，G1 是否繼續被信任，會影響這批網站多久之後要再換一次憑證。
