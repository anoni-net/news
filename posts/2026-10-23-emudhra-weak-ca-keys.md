---
title: eMudhra 八張中繼憑證的弱私鑰事件
description: 印度憑證機構 eMudhra 有八張中繼憑證的私鑰小於 256，任何人都能立刻算出來，再用來替別人的網站簽發 HTTPS 憑證。研究者 10 月 17 日通報後，Chrome 與 Firefox 在幾個小時內自動封鎖，一般使用者的瀏覽器不必另外設定。不經過瀏覽器的程式各自帶著信任清單，Node.js、Python 的 certifi、Go、Java 與 Linux 發行版從 10 月 19 日起陸續推出更新（到 10 月 22 日還沒全部完成），自行寫程式或維護伺服器的人要逐一更新。
date: 2026-10-23T00:00:00+08:00
slug: emudhra-weak-ca-keys
categories:
  - security
sources:
  - title: Compromised eMudhra Intermediate Certificates
    url: https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE
    publisher: Mozilla dev-security-policy
    date: 2026-10-20
  - title: "2083449 - eMudhra: Private key compromise of Intermediate Certificates"
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
    publisher: Mozilla Bugzilla
    date: 2026-10-18
  - title: Protecting Chrome and Android Users from Compromised eMudhra Intermediate CA Certificates
    url: https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/
    publisher: Google
    date: 2026-10-20
  - title: eMudhra Statement on Recent Certificate Security Incident
    url: https://emudhra.com/en/post/certificate-security-incident
    publisher: eMudhra
    date: 2026-10-20
  - title: eMudhra Statement on distrust of select Global TLS Intermediate and one Root CA
    url: https://emudhra.com/en/press-release/emudhra-statement-distrust-global-tls-intermediate-root-ca
    publisher: eMudhra
    date: 2026-10-21
  - title: Wednesday, October 21, 2026 Security Releases
    url: https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
    publisher: Node.js
    date: 2026-10-21
  - title: "crypto/x509: mitigation for security concerns with a specific Certificate Authority"
    url: https://github.com/golang/go/issues/82345
    publisher: Go
    date: 2026-10-19
  - title: "OpenJDK Vulnerability Advisory: 2026/10/21"
    url: https://openjdk.org/groups/vulnerability/advisories/2026-10-21
    publisher: OpenJDK
    date: 2026-10-21
  - title: Bug #2171507 “ca-certificates update tracking bug” : Bugs : ca-certificates package : Ubuntu
    url: https://bugs.launchpad.net/ubuntu/+source/ca-certificates/+bug/2171507
    publisher: Launchpad
    date: 2026-10-20
  - title: 2556376 – Update to mitigate current issues with eMudhra
    url: https://bugzilla.redhat.com/show_bug.cgi?id=2556376
    publisher: Red Hat Bugzilla
    date: 2026-10-20
  - title: FreeBSD-SA-26:73.caroot
    url: https://www.freebsd.org/security/advisories/FreeBSD-SA-26:73.caroot.asc
    publisher: FreeBSD
    date: 2026-10-21
  - title: eMudhra Intermediate CA Compromise
    url: https://emudhra.we-have-a-problem.com/
    publisher: emudhra.we-have-a-problem.com
    date: 2026-10-20
  - title: 8 eMudhra certificates are compromised. Here's what you need to know
    url: https://blog.cloudflare.com/emudhra-certificate-compromise/
    publisher: Cloudflare
    date: 2026-10-20
watch:
  - date: 2026-10-28
    note: Chrome Root Store 是否如期在太平洋時間 10 月 27 日移除 emSign ECC Root CA - G3
  - date: 2026-11-20
    note: eMudhra 是否提交正式事故報告、回覆 Chrome 在 Bugzilla 的提問，以及 Chrome 對 eMudhra 其他憑證的決定，Apple 與 Microsoft 是否公布處置
authors:
  - anoni-net
---

印度的憑證機構 eMudhra（憑證品牌 emSign）有八張中繼憑證的私鑰簡單到可以直接算出來。中繼憑證位在根憑證之下，是實際用來簽發網站憑證的那一層。一位研究者在 UTC 10 月 17 日 18:05（台北時間 10 月 18 日 02:05）通報 Apple、Chrome、Microsoft、Mozilla 與 eMudhra，附上用八把私鑰各自簽出的證明。依 Mozilla 10 月 20 日在 dev-security-policy 郵件群組的貼文，取得私鑰的人可以替自己不擁有的網站簽發 HTTPS 憑證。

Chrome 與 Firefox 在通報後幾個小時內就用自動推送的封鎖清單擋下六張 TLS 中繼，多數使用者不必更新或重新啟動瀏覽器。受影響比較大的是不經過瀏覽器的程式，例如用 Node.js、Python、Go 或 Java 寫成的工具與伺服器，各自要等更新才會停止信任。Mozilla 10 月 20 日在事故單上補充，已經有好幾個人各自算出私鑰，其中有些人公開了這件事。

依 Mozilla 工程師在 Bugzilla 事故單的初步分析，八把都是 P-384 橢圓曲線的私鑰，本來應該是一個隨機挑選、長達 384 位元的整數。實際的值卻都小於 256，依序試過 256 個數字就能找出來。八張裡有六張用來簽發網站的 TLS 憑證，受 Chrome、Mozilla、Microsoft 與 Apple 信任。另外兩張用來簽署程式碼，受 Microsoft 信任。

eMudhra 的聲明寫到，八張中繼憑證在 2025 年 4 月 30 日的金鑰產生儀式建立，問題經過約 18 個月、兩次獨立稽核都沒有被發現。依 eMudhra 在事故單上的初步說明，儀式使用的程式有缺陷，在原本的金鑰之外多產生了一組弱金鑰。兩組金鑰的標籤相近，弱金鑰被誤用來申請憑證。eMudhra 10 月 21 日更新的聲明也提到，確切的根本原因還在調查。

依同一份聲明，八張中有七張從沒用在正式環境，正在使用的那一張沒有簽發過任何憑證。eMudhra 也不知道有人在公開之前算出弱金鑰的證據。依 Google 10 月 20 日的部落格，封鎖之前憑證透明度（Certificate Transparency，CT，公開記錄每一張憑證的日誌）裡沒有六張中繼簽出的網站憑證。Chrome 預設只接受記進 CT 的憑證，所以 Google 判斷偽造憑證騙不過 Chrome，也騙不過目標為最新 SDK 或自行啟用 CT 檢查的 Android App。

一位 Mozilla 工程師為事件架設的說明頁另外提到，很多瀏覽器以外的程式不檢查 CT。說明頁也寫到，從 2025 年 4 月憑證建立起就有被濫用的可能，目前不知道攻擊者有沒有利用弱金鑰攻擊這些程式。

## 導讀觀點 {#perspective}

瀏覽器信任一個 HTTPS 網站，是因為網站的憑證由一串憑證機構逐層簽署，最上層的根憑證預先放在瀏覽器或作業系統的信任清單裡。中繼憑證的私鑰可以簽出任何網域的憑證。依 FreeBSD 10 月 21 日的安全公告，能攔截網路流量的攻擊者可以用被算出的私鑰冒充任何 TLS 伺服器，讀取或修改連線內容而不被發現。

Chrome 的 CRLSet 與 Firefox 的 OneCRL 都是瀏覽器在背景自動下載的封鎖清單，可以單獨擋下特定的中繼憑證。再加上 CT 的要求，Chrome 與 Firefox 這一端在通報當天就有兩層保護。依 Mozilla 的發行說明與事故單，停用了自動下載清單（Remote Settings）的 Firefox 要更新到 158.0.1。部分 Android 版 Firefox 的設定檔沒有在啟動時套用清單，要更新到 158.0.2。

依 Bugzilla 事故單，eMudhra 在 UTC 10 月 18 日把八張中繼標為撤銷。依 Mozilla 在事故單上的說法，有些程式不讀撤銷資訊，或沒有機制單獨撤回特定的中繼。NSS 是 Mozilla 維護的加密函式庫，許多程式與發行版沿用它的根憑證清單。為了保護前述的程式，Mozilla 在 10 月 20 日的 NSS 3.131.1 移除六張 TLS 中繼往上連到的根憑證 emSign ECC Root CA - G3。

Node.js 10 月 21 日的 22.23.4、24.22.1、26.12.1 換上了新清單，Go 也發布了 1.27.3 與 1.26.10。依說明頁的修補清單，Python 的 certifi 2026.10.19 與 curl 的 CA bundle 也已更新。依 Ubuntu 的追蹤單，到 10 月 22 日為止 22.04、24.04、26.04 與 26.10 已發布 ca-certificates 的更新，20.04 以前的版本還沒有。Fedora 已送出更新，依 Red Hat Bugzilla 的 bug 單，到 10 月 22 日為止這批更新仍信任簽發兩張程式碼簽署中繼的根憑證。

依說明頁的建議，一般使用者儘快把瀏覽器與作業系統更新到最新版。依 Google 的部落格，Android 裝置在 UTC 10 月 19 日 22:00 前後（台北時間 10 月 20 日 06:00）透過 Google Play 服務收到同樣的封鎖。Google 寫大多數 Android 裝置已經收到，還沒收到的重新開機就能馬上套用。沒有 Google Play 服務的 Android 裝置不在 Google 這段說明的範圍內，本文沒有查到 Android 系統本身的更新。

自行寫程式、維護伺服器或在電腦上執行命令列工具的人，要更新的是各自的執行環境。Go 的修補在標準函式庫的 `crypto/x509` 套件，Go 程式編譯時會把標準函式庫包進執行檔，所以要用新版重新編譯。Python 的 certifi 是個別安裝的套件，每個虛擬環境與容器各有一份，要分別更新。依說明頁，macOS 內建的 curl、python3 等指令讀取 `/etc/ssl/cert.pem` 時不檢查撤銷，到 10 月 22 日這個檔案還沒更新。

依 OpenJDK 10 月 21 日的公告，作業系統套件提供的 Java 多半使用系統的憑證，更新系統就夠。自行安裝的 Java，以及 FreeBSD 與 Homebrew 的套件，要直接更新。

Cloudflare 的部落格提醒，更新之後如果出現憑證錯誤，不要用關閉憑證驗證的方式解決。說明頁準備了用受影響的中繼簽發的測試網址，用 curl 連線出現憑證錯誤，代表 curl 已經不信任這些憑證。Cloudflare 的部落格也寫到，這類測試只代表測到的那個程式，使用其他驗證方式的程式要個別確認。

移除根憑證可以保護不讀撤銷資訊的程式，代價是部分正當網站的憑證也跟著失效。eMudhra 在事故單上估計約 3 萬張憑證需要換掉，聲明寫影響範圍限於美國的單一客戶生態系。Chrome 在事故單上依到 10 月 21 日的 CT 資料統計，這個根底下約 3 萬 800 筆還沒過期的憑證紀錄，有 99.9% 由 Internet2 與 InCommon 的兩張從屬中繼簽發。依 Google 的部落格，Chrome 預計在太平洋時間 10 月 27 日上午從 Chrome Root Store 移除同一個根，也在評估 eMudhra 其他憑證是否繼續信任。

說明頁寫 Apple 裝置從 10 月 19 日起封鎖，Microsoft 平台從 10 月 20 日起封鎖。到 10 月 22 日為止，本文沒有找到兩家自己的公告。依 Bugzilla 事故單，到 UTC 10 月 21 日深夜為止，eMudhra 還沒有提交正式的事故報告。正式報告、eMudhra 對 Chrome 在事故單上所提問題的回覆，以及 Chrome 對 eMudhra 其他憑證的決定，是接下來可以留意的地方。
