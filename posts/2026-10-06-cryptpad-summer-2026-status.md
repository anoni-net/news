---
title: CryptPad 2026 夏季進度與後量子加密的瓶頸
description: 端對端加密協作套件 CryptPad 訂出新的資安政策，漏洞修正發布後至少 90 天才公開細節。後量子加密的實驗讓部分功能慢到難以使用，要等瀏覽器內建新的演算法。使用公開實例的人不必調整設定，自行架設的管理者要跟上新版。
date: 2026-10-06T07:00:00+08:00
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
  - date: 2026-11-06
    note: CryptPad 秋季版是否發布、最新版本號，cryptpad.fr 何時停止法文客服
---

CryptPad 在 9 月 15 日發布夏季進度報告，交代新的資安政策、後量子加密研究與官方實例 cryptpad.fr 的客服異動。CryptPad 是以 AGPL-3.0 授權的端對端加密協作套件，在瀏覽器裡共同編輯文件與試算表，可以使用公開實例或自行架設。使用公開實例的人不必調整設定，自行架設的管理者要留意升級的時程。

新的資安政策在 6 月公布。漏洞修正發布之後，至少保密 90 天才公開 CVE（公開的漏洞編號），讓實例有時間升級。嚴重程度改用 CVSS 4.0 評分。政策也寫明修正的漏洞不列在版本說明裡，建議一律使用每季發布的最新版。

依 6 月的事後檢討，伺服器先前沒有限制 WebSocket 連線的傳送頻率，反覆送出訊框就能耗盡資源。cryptpad.fr 在 1 月 28 日因此遭到分散式阻斷服務攻擊，修正收在 3 月 27 日發布的 2026.2.1。當時的政策沒有寫明保密期，CVE 在發布後第 34 天就公開了。

後量子加密（能抵擋量子電腦攻擊的加密演算法）方面，團隊選定 NIST 標準化的 ML-KEM 與 ML-DSA，在實驗中以混合的方式取代原本的公開金鑰加密。多數功能運作正常，部分功能卻慢到難以使用。瀏覽器的 Web Cryptography API 有一份加入這兩種演算法的草案，進度報告寫到預期比外部函式庫快兩個數量級。

cryptpad.fr 的客服團隊目前沒有會說法文的成員，將停止提供法文支援。秋季版會包含兩個版本份量的改進，進度報告沒有寫發布日期。

## 導讀觀點 {#perspective}

CryptPad 的加密在瀏覽器裡執行，使用說明的信任前提之一是實例執行與 GitHub 公開版本相同的程式碼，此時管理者無法讀取或修改文件。各實例何時升級由管理者決定，公開實例清單只收錄通過檢查、版本最新的實例。

WICG（W3C 孵化新規格的社群小組）的草案到 9 月 14 日還不在 W3C 的標準流程上，要等瀏覽器實作，後量子版本的 CryptPad 才比較可能實現。團隊已先把程式改成可以抽換加密函式庫的架構（crypto-agility）。

使用說明寫明 CryptPad 的匿名性較弱，實例管理者看得到使用者的 IP 位址與瀏覽器，需要時可以透過 Tor 連線。註冊只需要使用者名稱與密碼，不需要電子郵件，代價是遺失的密碼無法重設。

自行架設的管理者，可以依事後檢討更新 nginx 的連線頻率限制設定。到 9 月 29 日為止，最新的正式版是 5 月 26 日發布的 2026.5.1。

想試用的人用瀏覽器開啟 cryptpad.fr 或清單上的其他實例就能開始，到 9 月 29 日為止，清單上的 13 個實例都在歐洲與北美。不註冊也能共同編輯，但文件連續 3 個月沒有使用就不再保留。介面有正體與簡體中文，使用說明沒有中文版，客服頁面會列出管理者使用的語言。
