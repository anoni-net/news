---
title: CryptPad 2026 夏季進度與後量子加密的瓶頸
description: 端對端加密協作套件 CryptPad 訂出新的資安政策，漏洞修正發布後至少 90 天才公開細節。後量子加密的實驗讓部分功能慢到難以使用，瀏覽器內建新的演算法之後可望改善。使用公開實例的人不必調整設定，自行架設的管理者要跟上新版。
date: 2026-10-06T00:00:00+08:00
slug: cryptpad-summer-2026-status
sources:
  - title: Summer 2026 status
    url: https://blog.cryptpad.org/2026/09/15/status-2026-09/
    publisher: CryptPad
    date: 2026-09-15
  - title: 2026.2 security fixes and our new security policy
    url: https://blog.cryptpad.org/2026/06/24/2026.2-security-issues/
    publisher: CryptPad
    date: 2026-06-24
  - title: CryptPad Security Policy
    url: https://cryptpad.org/security/
    publisher: CryptPad
    date: 2026-06-23
  - title: Winter fix release (2026.2.1)
    url: https://github.com/cryptpad/cryptpad/releases/tag/2026.2.1
    publisher: GitHub
    date: 2026-03-27
  - title: Spring fix release (2026.5.1)
    url: https://github.com/cryptpad/cryptpad/releases/tag/2026.5.1
    publisher: GitHub
    date: 2026-05-26
  - title: Autumn Release
    url: https://github.com/cryptpad/cryptpad/milestone/20
    publisher: GitHub
  - title: Summer 2025 status
    url: https://blog.cryptpad.org/2025/09/05/status-2025-08/
    publisher: CryptPad
    date: 2025-09-05
  - title: Modern Algorithms in the Web Cryptography API
    url: https://wicg.github.io/webcrypto-modern-algos/
    publisher: WICG
    date: 2026-09-14
  - title: "CryptPad: Collaboration suite, encrypted and open-source"
    url: https://cryptpad.fr/
    publisher: CryptPad
  - title: Security
    url: https://docs.cryptpad.org/en/user_guide/security.html
    publisher: CryptPad
  - title: User Account
    url: https://docs.cryptpad.org/en/user_guide/user_account.html
    publisher: CryptPad
  - title: Support
    url: https://docs.cryptpad.org/en/user_guide/support.html
    publisher: CryptPad
  - title: Public instances
    url: https://cryptpad.org/instances/
    publisher: CryptPad
  - title: Chinese (Traditional Han script)
    url: https://weblate.cryptpad.org/projects/cryptpad/app/zh_Hant/
    publisher: CryptPad Weblate
  - title: Chinese (Simplified Han script)
    url: https://weblate.cryptpad.org/projects/cryptpad/app/zh_Hans/
    publisher: CryptPad Weblate
authors:
  - anoni-net
watch:
  - date: 2026-10-13
    note: CryptPad 秋季版（2026.9.0）是否已在 GitHub 發布，cryptpad.fr 何時停止法文客服
---

CryptPad 在 9 月 15 日發布夏季進度報告，交代新的資安政策、後量子加密研究與 cryptpad.fr 的客服異動。CryptPad 是開源（AGPL-3.0）的端對端加密協作套件，可以在瀏覽器裡共同編輯文件與試算表。使用者可以用公開實例（開放大眾使用的伺服器），也可以自行架設。使用公開實例的人不必調整設定，自行架設的管理者要留意升級。

依 6 月公布的新資安政策，漏洞修正發布後至少保密 90 天，之後才以 CVE（通用的漏洞編號）公開細節。嚴重程度改用 CVSS 4.0（漏洞嚴重度評分）。版本說明不列出修正了哪些漏洞，只標出其中最高的 CVSS 分數與升級提醒。建議的版本一律是最新版，新版每季發布。

依 6 月的事後檢討，伺服器先前沒有限制 WebSocket 連線（瀏覽器與伺服器交換資料的通道）的傳送頻率，有人反覆送出大量訊息就能耗盡資源。官方實例 cryptpad.fr 在 1 月 28 日因此遭到分散式阻斷服務攻擊，服務中斷不到 3 小時就排除，修正收錄在 3 月 27 日發布的 2026.2.1。

團隊原本打算保密 90 天，但當時的政策沒有寫清楚保密期。回報漏洞的人因此提出異議，CVE 在 2026.2.1 發布後第 34 天就公開了。

後量子加密是能抵擋量子電腦攻擊的演算法。團隊選定美國標準機構 NIST 制定的 ML-KEM 與 ML-DSA，前者用來交換金鑰，後者用來做數位簽章。實驗中兩者與原本的公開金鑰加密混合使用，多數功能運作正常，部分功能卻慢到難以使用。

瀏覽器內建的加密介面 Web Cryptography API 有一份草案，要直接加入這兩種演算法。據進度報告估計，速度約是從外部載入函式庫的 100 倍。

進度報告寫明客服團隊已經沒有會說法文的成員，cryptpad.fr 將停止提供法文客服。秋季版會包含相當於兩個版本的改進，到 9 月 29 日還沒有公布發布日期。

## 導讀觀點 {#perspective}

CryptPad 在瀏覽器裡加密文件，伺服器無法取得文件內容。使用說明列出的信任前提有幾項，包括實例執行與 GitHub 公開版本相同的程式碼，以及合作者不把分享連結轉給其他人。這些前提都成立時，管理者無法讀取或修改文件。使用說明也寫明匿名性較弱，管理者可以看到使用者的 IP 位址與瀏覽器資訊，需要時可以透過 Tor 連線。

修正要等實例的管理者升級之後才會生效。依資安政策，90 天的保密期是留給管理者升級的時間。漏洞公開之後，攻擊者也可能開始利用。公開實例清單只收錄通過檢查、版本最新的實例，挑選實例時可以從清單開始。

Web Cryptography API 的草案由 WICG（W3C 討論新規格的社群小組）維護，到 9 月 29 日還沒進入 W3C 的正式標準流程。瀏覽器實作草案之後，後量子版的 CryptPad 可能比較可行。團隊已先把程式改成可抽換加密函式庫的架構（加密敏捷性，crypto-agility）。

依事後檢討，用 nginx 並以官方進階範例設定為基礎的管理者，要盡快改用最新版的範例設定。新版範例加上了連線頻率限制。依資安政策，每個版本的支援期是 90 天。到 9 月 29 日為止，最新版是 5 月 26 日的 2026.5.1。

開啟 cryptpad.fr 或清單上的其他實例就能試用，瀏覽器要啟用 JavaScript。到 9 月 29 日為止，清單上的 13 個實例都在歐洲與北美。不註冊也能共同編輯，但不能上傳圖片、影片與 PDF，文件連續 3 個月沒有使用也不再保留。

註冊只需要使用者名稱與密碼，不必填電子郵件。管理者無法查看、找回或重設密碼，使用說明寫明要把密碼另外記在安全的地方。介面有正體與簡體中文，使用說明沒有中文版。各實例的客服頁面會標出管理者使用的語言。
