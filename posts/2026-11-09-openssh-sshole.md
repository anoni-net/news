---
title: OpenSSH 在 musl 系統上的長密碼登入繞過漏洞
description: OpenSSH 11 月 5 日發布 10.6p2，修補超長密碼可以登入沒有設密碼帳號的漏洞。只有 Linux 上用 musl libc、不經 PAM 驗證密碼的 sshd 在範圍內，例如 Alpine Linux。依 OpenSSH 維護者與 HKCERT 的說明，Debian、Ubuntu、Red Hat 這類用 glibc 的系統不在範圍內，到 11 月 8 日兩家發行版的追蹤頁還沒有標為不受影響。在 Alpine 上執行 sshd 的人要更新或關閉密碼登入。
date: 2026-11-09T00:00:00+08:00
slug: openssh-sshole
categories:
  - security
sources:
  - title: OpenSSH Release Notes
    url: https://www.openssh.com/releasenotes.html#10.6p2
    publisher: OpenSSH
    date: 2026-11-05
  - title: "Security advisory: openssh-server password authentication bypass"
    url: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
    publisher: Alpine Linux
    date: 2026-11-05
  - title: "\"sshole\": password authentication bypass: OpenSSH + musl libc"
    url: https://www.openwall.com/lists/oss-security/2026/11/05/3
    publisher: oss-security
    date: 2026-11-05
  - title: OpenSSH 10.6p2 has been released with a workaround for a critical vulnerability
    url: https://hachyderm.io/@damienmiller/117563026759098135
    publisher: Hachyderm.io
    date: 2026-11-05
  - title: "*sshole"
    url: https://sshhole.com
    publisher: sshhole.com
  - title: Meet *sshole, the vulnerability that lets hackers SSH into Linux devices
    url: https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/
    publisher: Ars Technica
    date: 2026-11-05
  - title: OpenSSH發布緊急更新，修補可利用長密碼繞過身分驗證的資安漏洞SSHole
    url: https://www.ithome.com.tw/news/180281
    publisher: iThome
    date: 2026-11-06
  - title: CVE-2026-123158
    url: https://access.redhat.com/security/cve/CVE-2026-123158
    publisher: Red Hat
  - title: CVE-2026-123158
    url: https://security-tracker.debian.org/tracker/CVE-2026-123158
    publisher: Debian
  - title: CVE-2026-123158
    url: https://ubuntu.com/security/CVE-2026-123158
    publisher: Ubuntu
    date: 2026-11-06
  - title: OpenSSH Security Restriction Bypass Vulnerability
    url: https://www.hkcert.org/security-bulletin/openssh-multiple-vulnerabilities_20261106
    publisher: HKCERT
    date: 2026-11-06
watch:
  - date: 2026-12-08
    note: musl 是否修改 crypt() 在密碼過長時回傳 `*` 的做法，Debian 與 Ubuntu 追蹤頁的狀態，OpenWrt、Buildroot、Yocto 是否有官方說明，以及有沒有實際被利用的案例
authors:
  - anoni-net
---

OpenSSH 在 11 月 5 日發布 10.6p2，修補一個用超長密碼就能登入「沒有設密碼的帳號」的漏洞，發現者取名為 \*sshole。範圍很窄，只有 Linux 上用 musl libc（C 語言的標準函式庫，程式呼叫系統功能時經過它）、而且不經 PAM（Linux 上統一處理登入驗證的模組）驗證密碼的 sshd（OpenSSH 的伺服器程式）受影響。依 OpenSSH 維護者在 Mastodon 的貼文，以及香港電腦保安事故協調中心（HKCERT）與 Red Hat 的說明，Debian、Ubuntu、Red Hat 這類用 glibc 的系統不在範圍內。需要檢查的是 Alpine Linux（常用來製作容器映像的發行版）上有執行 sshd 的機器，以及其他用 musl、又裝了 OpenSSH 的系統，例如部分嵌入式裝置。

依 Alpine 的安全公告，四個條件同時成立才受影響。sshd 用的是 Alpine 預設不含 PAM 的 `openssh-server`，或是含 PAM 的版本但設成 `UsePAM no`。密碼登入保持開啟，這是 OpenSSH 的預設。機器上有密碼欄位為 `*` 的帳號（只用金鑰登入、沒有設密碼的帳號常是這樣），另外至少還有一個帳號設了密碼。

符合條件時，攻擊者只要知道那個 `*` 帳號的名稱，送出 257 到 1,024 位元組的任意密碼就能登入。公告寫只需要一次連線，每次都會成功。

依同一份公告的說明，不經 PAM 時 sshd 用 `crypt()` 把收到的密碼算成雜湊，再跟帳號的密碼欄位比對。欄位太短、放不下 salt（混進密碼一起計算的隨機值）時，sshd 會借用其他帳號的 salt。musl 的 `crypt()` 遇到超過 256 位元組的密碼時回傳字串 `*` 當作錯誤標記，跟沒有密碼的帳號欄位相同，比對就成立了。依 oss-security 郵件列表上的通報，修補版改成檢查雜湊的最短長度，不再接受 `*`。

發現者的說明頁把成因追溯到三個專案各自的修改。2012 年 musl 為了避免超長密碼拖慢伺服器，把密碼限制在 256 位元組。2016 年 OpenSSH 改成借用其他帳號的 salt，用意是不讓攻擊者從回應時間判斷帳號存不存在，Alpine 則在 2022 年的 3.16 版前後把 root 的密碼欄位改成 `*`。說明頁寫 OpenSSH 在 OpenBSD 與 glibc 上測試，musl 不測試 sshd，多數發行版又經過 PAM。

依 Alpine 的公告，OpenSSH 預設的 `PermitRootLogin prohibit-password` 不讓 root 用密碼登入。其他能登入的帳號若能透過 doas（類似 sudo 的提權工具）取得 root 權限，這道設定就擋不住。舊版的官方雲端映像內建一個 `alpine` 帳號，密碼欄位是 `*`，用 doas 也不必輸入密碼。公告提到這些映像第一次開機時是安全的，管理者替任何帳號設了密碼之後（例如主控台的登入密碼）就可以被利用。

OpenSSH 的發布說明寫他們認為根本原因在 sshd 之外，但可以在 sshd 這一端避開。依 Ars Technica 的報導，一位 musl 開發者的立場是問題出在呼叫端的用法，musl 本身沒有 bug。他也提到 musl 計畫在之後的版本修改這個機制。

漏洞之後取得 CVE（公開漏洞的統一編號）CVE-2026-123158，嚴重度評分（CVSS，滿分 10）為 8.1。到 11 月 8 日，OpenSSH、Alpine、Ars Technica 與 iThome 都沒有提到實際被利用的案例，HKCERT 的通報則寫已經有公開的 PoC（證明漏洞能被利用的程式）。依 Ars Technica 引述資安公司 Detectify 的說法，Shodan（掃描全網路裝置的搜尋引擎）列出約 2,200 萬台開著 SSH 22 埠的系統。Ars 的評估是其中只有一部分符合條件，但逐台測試又快又容易，找出受影響的裝置不需要花太多力氣。

## 導讀觀點 {#perspective}

Red Hat 的說明頁寫旗下產品不受影響，因為產品裡的 OpenSSH 連結的是 glibc，也預設使用 PAM。到 11 月 8 日，Debian 的追蹤頁把 bookworm、trixie 的 OpenSSH 標成 vulnerable、緊急程度標 unimportant，Ubuntu 的頁面則標「Needs evaluation」。Debian 的表以 sid 的 `1:10.6p2-1` 為修正版本，更早的版本都標 vulnerable，本文據此推論是依版本號標示。緊急程度標 unimportant，也與 HKCERT、OpenSSH 維護者寫的 glibc 系統不受影響一致。

Ars 的報導寫 Docker Hub 上的 Alpine 基礎映像下載超過 10 億次，不過依 Alpine 的公告，容器裡沒有執行 sshd 的使用者不受影響。用 cloud-init（雲端主機第一次開機時套用設定的工具）寫入 `PasswordAuthentication no` 的雲端映像也不在範圍內。

依 Ars Technica 的報導，Alpine 長年用在路由器、智慧電視與工業控制器，這類裝置很多很難更新。發現者把 OpenWrt、Buildroot、Yocto 列為用 musl 的系統。Ars 補充 OpenWrt 預設的 SSH 伺服器是 Dropbear，另外安裝 OpenSSH 才在範圍內。Ars 也寫發現者說 Buildroot 與 Yocto 受影響，但到 11 月 5 日還沒有確認。

用 Raspberry Pi OS 的樹莓派屬於 Debian 系、用 glibc，本文推論不在範圍內，裝 Alpine 的則照 Alpine 的條件檢查。家用 NAS 與路由器是否受影響，本文參考的來源都沒有提到，到 11 月 8 日也沒有查到廠商的公告。

依維護者的貼文，OpenSSH 團隊得知問題的隔天就發布修正版。理由是團隊最近多次遇到 AI 代理很快重新發現已知的漏洞，有時只隔幾小時。團隊因此認為長時間的保密期是危險的做法，主要對攻擊者有利。發布說明也寫，目前會更頻繁地發布修正版，不再累積到下一個預定版本。

依 Alpine 的公告，在 Alpine 上自己管理 sshd 的人要更新 `openssh` 套件並重新啟動 sshd，只升級套件不會替換已經在執行的服務。Alpine 從 3.16 起的每個版本都有修補套件，包含已經停止支援的版本，版本對照與指令見公告。上游的修正版本是 OpenSSH 10.6p2，各系統的修補套件可能沿用舊的版本號（Alpine 就是如此），本文參考的來源沒有寫其他系統如何更新。

暫時無法更新時可以關閉密碼登入。依 oss-security 的通報，關閉之後就能避開漏洞，代價是不能再用密碼登入。Alpine 的公告提醒先確認金鑰登入可用，並保留目前的連線直到新的登入測試成功。

公告也列出事後檢查的方法，看登入紀錄裡有沒有沒設密碼的帳號出現 `Accepted password`，無法排除時把機器當成已被入侵處理。只用 Debian、Ubuntu、Red Hat 系統的人，依維護者與 HKCERT 的說明不需要為這個漏洞改設定。這是依 glibc 與 PAM 的條件推論，到 11 月 8 日 Debian 與 Ubuntu 的追蹤頁還沒有跟著更新。
