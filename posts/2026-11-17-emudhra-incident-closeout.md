---
title: eMudhra 憑證事件的事故報告、macOS 修正版與 G1 根的期限
description: 印度憑證機構 eMudhra 的弱私鑰事件在 11 月有三項進展。Apple 11 月 9 日推出 macOS 27.2.1、26.7.3 與 15.8.3，修正內建的 git、curl 等命令列工具。在 Mac 上用這些工具的人要更新系統，其他人不必另外設定。eMudhra 11 月 10 日提交事故報告，交代 11 月 7 日另外撤銷的八張 RSA 中繼憑證。依 11 月 14 日讀到的原始碼，Chrome 與 Mozilla 不再信任 UTC 11 月 16 日之後簽發、以 emSign Root CA - G1 為根的憑證，Microsoft 排定同一天移除 Edge 與 WebView2 對 G1 的信任。
date: 2026-11-17T00:00:00+08:00
slug: emudhra-incident-closeout
categories:
  - security
follows:
  - 2026-11-03-emudhra-key-compromise-followup
sources:
  - title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c82
    publisher: Mozilla Bugzilla
    date: 2026-11-10
  - title: About the compromised eMudhra intermediate CAs
    url: https://support.apple.com/en-us/149555
    publisher: Apple
    date: 2026-11-09
  - title: Apple security releases
    url: https://support.apple.com/en-us/100100
    publisher: Apple
  - title: "MC1529467 - Microsoft Windows: Updates to address compromised eMudhra certificate authority keys"
    url: https://mc.merill.net/message/MC1529467
    publisher: Microsoft 365 Message Center Archive
    date: 2026-11-11
  - title: "Moving Forward Together: InCommon Certificate Service Update"
    url: https://incommon.org/about/news/incommon-certificate-service-update
    publisher: InCommon
    date: 2026-11-10
  - title: eMudhra Statement on Recent Certificate Security Incident
    url: https://emudhra.com/en/post/certificate-security-incident
    publisher: eMudhra
    date: 2026-11-05
  - title: root_store.textproto
    url: https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/root_store.textproto
    publisher: Chromium
  - title: certdata.txt
    url: https://github.com/mozilla-firefox/firefox/blob/main/security/nss/lib/ckfw/builtins/certdata.txt
    publisher: Mozilla
  - title: eMudhra憑證事故擴大，再有8張RSA中繼CA憑證遭撤銷
    url: https://www.ithome.com.tw/news/180445
    publisher: iThome
    date: 2026-11-13
watch:
  - date: 2026-12-01
    note: Apple 是否如 eMudhra 與 InCommon 的轉述在 11 月 30 日移除並不再信任 emSign Root CA - G1，Apple 的支援頁 149555 是否更新
  - date: 2026-12-05
    note: eMudhra 是否在 Bugzilla 2083449 公布 KPMG 獨立審查（預定 12 月 4 日完成）的結果，以及是否回覆撤銷理由用 cessationOfOperation 而非 keyCompromise 的提問
  - date: 2026-12-10
    note: Chrome、Mozilla 是否把 emSign Root CA - G1 整個移出信任清單，Microsoft 11 月 16 日的 Edge 與 WebView2 更新是否已推送、Windows 本身對 G1 的處置
authors:
  - anoni-net
---

印度憑證機構 eMudhra（憑證品牌 emSign）有八張中繼憑證的私鑰可以直接算出，事件 10 月中公開之後，11 月有三項進展。Apple 11 月 9 日推出 macOS 27.2.1、26.7.3 與 15.8.3，修正內建的命令列工具，也更新了根憑證清單檔 `/etc/ssl/cert.pem`。eMudhra 11 月 10 日在 Mozilla 的 Bugzilla 事故單 2083449 提交完整事故報告。Chrome 與 Mozilla 對 eMudhra 的另一張根憑證 emSign Root CA - G1 設下日期限制，Microsoft 則排定移除 Edge 與 WebView2（Windows App 內嵌網頁用的元件）對它的信任。

在 Mac 上用內建的 git、curl、python3 等工具連 `https://` 網址的人，要把系統更新到上述其中一個版本，其他人不必另外設定。依 Apple 的支援文件，Safari、Mail 與使用 Apple 網路與安全框架的 App 早已自動封鎖受影響的憑證，不必安裝更新。依 Microsoft 的公告，Edge 與 WebView2 的相關更新透過元件推送。

依 Apple 11 月 9 日改版的支援文件，從 macOS 27.2.1 起，macOS 與 Xcode Command Line Tools 附的命令列工具也會擋下受影響的 12 份中繼憑證。10 月撤銷的八張 ECDSA 中繼裡有六張是 TLS 用的中繼，每張各有兩份憑證，合計 12 份。兩份分別連到 eMudhra 的根 emSign ECC Root CA - G3，以及經 Sectigo 交叉簽署連到 AAA Certificate Services。更新同時從 `/etc/ssl/cert.pem` 移除五張根憑證，包括這兩張根與 emSign Root CA - G1，macOS 26 與 macOS 15 對應的修正版是 26.7.3 與 15.8.3。

依事故報告，eMudhra 在 11 月 7 日撤銷八張 RSA-4096 的中繼憑證（G2B 與 G2C 系列）。加上 10 月 18 日撤銷的八張 ECDSA 中繼，受影響的中繼憑證共 16 張。11 月 7 日填的撤銷理由是停止營運（`cessationOfOperation`），前一批 ECDSA 中繼填的是 CA 私鑰外洩（`caCompromise`）。

依報告，八把 RSA 私鑰沒有弱私鑰的問題，簽章都對得上憑證裡的公鑰。16 把金鑰在 2025 年 4 月 30 日的同一場金鑰產生儀式建立，匯入時私鑰材料經過主機上一支 Python 程式的記憶體，離開了硬體安全模組（HSM，專門產生與保管私鑰的硬體）。eMudhra 因此無法證明這批私鑰的處理符合自家憑證實務作業聲明（CPS，憑證機構公開承諾的作業規範）對私鑰移轉的規定。報告寫 RSA 的問題是在 11 月初、根憑證計畫討論這條規定之後確認，沒有寫是哪一家計畫，也沒有寫撤銷是否出於對方要求。

報告沒有寫有人取得 RSA 私鑰的證據，對整起事件的說法是沒有已知的濫用案例。報告提交當天有人在事故單上留言，問既然無法證明私鑰的處理合規，撤銷理由為何不用私鑰外洩（`keyCompromise`）。到 11 月 14 日，事故單上沒有 eMudhra 對這則提問的回覆。

依報告的附錄，八張裡有六張是 TLS 用的中繼（發行者 emSign Root TLS CA - G1），另外兩張是程式碼簽署用的中繼（發行者 emSign Root CS CA - G2）。兩種中繼各有 G2B 與 G2C 版本，G2B 的四張沒有簽發過終端憑證。G2C 的四張 5 月起在美國投入使用，簽發過網站憑證與程式碼簽署憑證。G2C 最後一次簽發在 11 月 3 日，報告寫終端憑證已經遷移或換發。

依 eMudhra 10 月 28 日的更新，約 3 萬 800 張 G3 憑證所屬的美國客戶生態系，已改由 eMudhra 的 G1 RSA 根簽發。事故報告把 G1 階層的主要服務對象寫成北美的一個大學聯盟。本文對照 10 月 28 日的更新與事故報告推論，那條 G1 RSA 管道包含這次撤銷的 G2C 中繼，兩份文件都沒有直接寫出。報告列的 TLS 中繼發行者是 emSign Root TLS CA - G1，它與 emSign Root CA - G1 的關係，本文沒有查到第一手資料。

InCommon（美國大學與研究機構的憑證服務）11 月 10 日的公告寫，自家目前經 G1 簽發的憑證機構已無法再取得公開信任（"Our current G1 issuing Certificate Authority (CA) is no longer viable for public trust"）。同一頁之後的更新寫簽發已從 emSign 改到 SSL.com，並請各機構在 11 月 16 日當天結束前換掉受影響的憑證。InCommon 是否就是報告裡的大學聯盟，報告沒有寫名稱，本文依兩者的描述推論是同一個客戶。

eMudhra 的報告寫 G1 階層的所有簽發在 11 月 16 日前停止，報告 11 月 10 日提交時，這一項列為進行中。本文 11 月 14 日讀到的 Chromium 與 Firefox 原始碼，都對 emSign Root CA - G1 設了日期限制。UTC 11 月 16 日 23:59:59（台北時間 11 月 17 日 07:59:59）之後簽發的憑證不再信任，之前簽發的仍信任。本文沒有查到 Chrome 與 Mozilla 針對 G1 的公告，原始碼也沒有寫正式版何時帶上這項設定。

Microsoft 11 月 11 日更新的公告寫，11 月 16 日推出元件更新，Edge 與 WebView2 收到後移除 G1 在內四張 eMudhra 根的預設信任。到 11 月 14 日，本文沒有查到這項更新推出的結果。

## 導讀觀點 {#perspective}

照 11 月 14 日的原始碼設定，Chrome 的限制看憑證記進憑證透明度日誌（CT log，公開記錄每一張憑證的日誌）的時間，Mozilla 的清單也設了同一天的期限。設定生效後，已經發出的憑證可以用到過期，期限之後的新憑證不被接受。Microsoft 為 Edge 與 WebView2 預定的更新則直接拿掉 G1，macOS 命令列工具更新後也一樣，連到 G1 的網站憑證不論何時簽發都可能無法通過驗證。本文據此推論，還沒換掉 G1 憑證的網站可能在 Chrome 正常開啟，在 Edge 或 Mac 的 curl 裡驗證失敗。

依 eMudhra 11 月 5 日更新的事件聲明，Apple 預定在 11 月 30 日移除並不再信任 G1 根，G1 底下任何時間簽發的憑證都不再被 Apple 的平台信任。InCommon 11 月 10 日的公告也轉述了這個日期。到 11 月 14 日，Apple 11 月 9 日改版的支援文件沒有寫這個日期，只寫了 `/etc/ssl/cert.pem` 移除 G1。

前篇提到，不想等更新的人可以依 Apple 的步驟，從 `/etc/ssl/cert.pem` 手動移除 G3 與 AAA Certificate Services。依同一份支援文件，更新到 27.2.1、26.7.3 或 15.8.3 之後就不必再重做這些步驟。照 Apple 步驟操作時留下的備份檔 `/etc/ssl/cert.pem.orig` 可以用 `sudo rm` 刪掉，也不要還原更新前做的備份。更新後的檔案少了五張根，Apple 提醒只讀這份檔案的工具，可能無法驗證部分憑證連到這些根的網站。

需要更新的命令列工具包括內建的 git、curl、python3、ruby、perl 與 openssl。無法更新到上述版本的 Mac，可以照 Apple 支援文件的步驟從 `/etc/ssl/cert.pem` 手動移除根憑證，需要管理員帳號。自帶根憑證清單的 App 與工具不讀 `/etc/ssl/cert.pem`，也不套用 Apple 的封鎖。系統更新保護不到這些工具，要向開發者確認。

只用 Safari、Mail 與使用 Apple 框架的 App 的人不需要做任何事。接下來可以留意 eMudhra 預定 12 月 4 日完成的 KPMG 獨立審查、Apple 是否在 11 月 30 日對 G1 有所處置，以及到 11 月 14 日只設了日期限制的 Chrome 與 Mozilla，之後會不會把 G1 整個移出信任清單。
