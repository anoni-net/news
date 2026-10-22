---
title: 修補前消息外流的 PHP 遠端執行程式碼漏洞
description: PHP 10 月 21 日發布 8.5.12、8.4.27、8.3.36、8.2.35，修補兩個可能讓未登入的攻擊者在網站伺服器上執行程式碼的漏洞。漏洞編號在預定揭露前兩天外流，PHP 把發布提前一天。漏洞在 PHP 本身，要更新的是伺服器上的 PHP，租用主機的人可以向業者確認。
date: 2026-10-23T00:05:00+08:00
slug: php2shell-leaked-rce
categories:
  - security
sources:
  - title: "Security advisory: Critical remote code execution vulnerabilities, update now"
    url: https://www.php.net/archive/2026.php#2026-10-21-5
    publisher: PHP
    date: 2026-10-21
  - title: RCE via OOM corruption
    url: https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w
    publisher: PHP
    date: 2026-10-21
  - title: RCE via stale global state
    url: https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp
    publisher: PHP
    date: 2026-10-21
  - title: Today's PHP Security Release, and How We're Strengthening PHP Security
    url: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
    publisher: The PHP Foundation
    date: 2026-10-21
  - title: "PHP: Supported Versions"
    url: https://www.php.net/supported-versions.php
    publisher: PHP
  - title: Critical PHP Security Release
    url: https://wordpress.org/news/2026/10/critical-php-security-release/
    publisher: WordPress.org
    date: 2026-10-21
  - title: Your Sites Are Protected Against the PHP2Shell Vulnerabilities
    url: https://automattic.com/2026/10/21/php2shell/
    publisher: Automattic
    date: 2026-10-21
  - title: Request handling memory corruption - php (CVE-2026-109618, CVE-2026-109619) - "php2shell"
    url: https://access.redhat.com/security/vulnerabilities/RHSB-2026-013
    publisher: Red Hat
    date: 2026-10-21
  - title: PHP2Shell — AI uncovers critical vulnerabilities in the backbone of the web
    url: https://www.php2shell.com/
    publisher: php2shell.com
  - title: CVE-2026-109618
    url: https://ubuntu.com/security/CVE-2026-109618
    publisher: Ubuntu
    date: 2026-10-21
  - title: PHP 存在2個重大資安漏洞(CVE-2026-109618 和 CVE-2026-109619)
    url: https://www.twcert.org.tw/tw/cp-169-11303-1d68a-1.html
    publisher: TWCERT/CC
    date: 2026-10-22
  - title: Cloudflare deploys protections against php2shell vulnerability
    url: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
    publisher: Cloudflare
    date: 2026-10-21
  - title: "Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619)"
    url: https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities
    publisher: Huntress
    date: 2026-10-20
  - title: Usage Statistics and Market Share of PHP for Websites, October 2026
    url: https://w3techs.com/technologies/details/pl-php
    publisher: W3Techs
watch:
  - date: 2026-11-20
    note: 兩個漏洞是否出現確認的實際入侵、是否列入 CISA 的已遭利用漏洞清單，Red Hat 等發行版的更新是否補齊
authors:
  - anoni-net
---

PHP 10 月 21 日發布 8.5.12、8.4.27、8.3.36 與 8.2.35，修補兩個漏洞 CVE-2026-109618 與 CVE-2026-109619（CVE 是公開漏洞的統一編號），研究者與媒體稱這組漏洞為 php2shell。php.net 的公告寫兩者可能讓沒有登入的攻擊者在伺服器上遠端執行程式碼，所有處理網頁請求的 PHP 都有風險，建議立刻更新。依 W3Techs 10 月 21 日的統計，在查得到伺服器端語言的網站裡，69.3% 使用 PHP。WordPress.org 的公告則說明這不是 WordPress 本身的漏洞，不會為此發布 WordPress 更新，要更新的是伺服器上的 PHP。

依 PHP Foundation 10 月 21 日的部落格，兩個漏洞編號在 UTC 10 月 20 日 15:00（台北時間 23:00）前後開始在論壇與社群網站流傳。流傳的訊息附上錯誤的發布時間與錯誤的嚴重度評分（CVSS，滿分 10）10.0，PHP 評定的是 9.2，技術細節沒有外洩。PHP 在 UTC 19:30（台北時間 10 月 21 日 03:30）提前發出預告，把發布從 UTC 10 月 22 日 14:00 提前到 10 月 21 日 14:00（台北時間 10 月 21 日 22:00）。沒有馬上發布的原因，是 Linux 發行版（Debian、Ubuntu、Red Hat 這類作業系統）還在打包修補，馬上發布會讓許多使用者沒有簡便的更新方式。

同一篇部落格提到，預告發出後，回報漏洞的一家資安公司誤公開了一段示範影片。影片的副本隨即在社群網站流傳。部落格寫到，影片是各方加快開發概念驗證程式（PoC，證明漏洞能被利用的程式）的原因之一。到公開發布時，PHP 安全團隊在流傳的 PoC 裡沒有找到能實際運作的利用程式。

Cloudflare 10 月 21 日的部落格寫到，外洩期間已觀察到針對客戶的攻擊流量，對應的 WAF（網站應用程式防火牆）規則從 UTC 10 月 21 日 03:02（台北時間 11:02）起對免費與付費客戶預設啟用。資安公司 Huntress 到美東時間 10 月 21 日 16:30（台北時間 10 月 22 日 04:30）為止，沒有在合作夥伴的系統觀察到實際利用。修補版發布之後，台灣電腦網路危機處理暨協調中心（TWCERT/CC）在 10 月 22 日的警訊提到網路上已出現 PoC。

## 導讀觀點 {#perspective}

依 PHP Foundation 的部落格，兩個漏洞都位在幾乎每個請求都會用到的記憶體管理與錯誤處理。依 php.net 的公告，第一個漏洞發生在記憶體用量達到上限時，PHP 可能在內部資料只初始化了一部分時中斷。之後的清理步驟可能把這些資料當成有效的。

第二個漏洞是前一個請求留下的內部狀態，在記憶體已經釋放之後，可能被同一個工作行程之後處理的請求使用。php.net 的公告把 Apache 搭配 mod_php（把 PHP 直接載入網頁伺服器的執行方式）列為風險最高，已有示範能讓未登入的請求在網站程式執行前觸發攻擊。

依研究者架設的說明網站 php2shell.com，漏洞出在 PHP 本身，網站程式寫得安全也可能受影響。只印出「Hello World」的簡單網站也一樣。WordPress.com 的營運公司 Automattic 也說明這是執行環境的修補，只更新 WordPress、佈景主題或外掛保護不到。

PHP Foundation 的部落格也檢討了修補為什麼花了這麼久。2024 年的外部安全稽核期間，PHP 的開發者已經發現第一個漏洞的早期跡象，當時還不知道有遠端執行程式碼的路徑。當時想到的幾種修法各有代價，可能破壞相容性、造成阻斷服務（讓網站無法正常運作），或需要改動大量第三方擴充套件。以共識決運作的安全團隊遲遲沒有決定，部落格的說法是延誤屬於結構性的失敗（structural failure），原因是決策流程與資源不足。

依部落格，AI 輔助的漏洞研究讓 PHP 收到的回報比以前多很多。7 月 1 日以來，安全團隊發布了 15 個 CVE，另外處理了超過 100 件無效、重複或無法重現的回報。PHP Foundation 正在調整流程，讓卡在困難取捨的嚴重漏洞更早交到領導層手上。

組織網站與部落格常用 WordPress 這類 PHP 程式架設。依 Automattic，放在 WordPress.com 等自家代管服務的網站已經受到保護，管理者不必另外調整設定。WordPress.org 的公告建議租用主機的人向業者確認更新，也列出在後台的「Tools > Site Health > Info > Server」（英文介面）可以看到 PHP 版本。這個版本號可以對照上面的修補版本，但發行版自行移植修補時會誤判，原因見下一段。

自行管理伺服器的人，用發行版套件安裝的 PHP 要看發行版的安全公告。有些發行版把修補移植到原本的版本，例如 Ubuntu 24.04 修補後的套件是 8.3.6-0ubuntu0.24.04.13，只對照 PHP 的版本號會誤判。Red Hat 10 月 21 日的公告寫 Red Hat Enterprise Linux 預設使用 PHP-FPM（由獨立行程執行 PHP 的方式），實際利用比較困難，部分更新還在準備中。PHP Foundation 的部落格則提到，第一個漏洞也確認過能經由網站程式本身的處理流程，在 PHP-FPM 上遠端執行程式碼。

依 php.net 的支援版本頁，PHP 8.1 以下已經結束支援，8.2 則在 2026 年 12 月 31 日結束支援。這次 PHP 另外替 7.4、8.0、8.1 提供最小的原始碼修補給自行編譯的人，7.3 以下沒有。TWCERT/CC 的警訊列出的受影響版本從 5.4 起。還沒辦法更新的，php.net 列出幾項調整設定的做法可以縮小部分攻擊路徑，但公告也提醒只有更新能完整解決。

兩個漏洞是否出現確認的實際入侵、是否列入美國網路安全暨基礎設施安全局（CISA）的已遭利用漏洞清單，以及 Red Hat 等發行版的更新是否補齊，是接下來可以留意的地方。
