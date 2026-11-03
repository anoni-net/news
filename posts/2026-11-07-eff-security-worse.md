---
title: AI 加速找漏洞之後的個人防護與開源維護
description: EFF 10 月 23 日的兩篇文章認為前沿 AI 模型讓找漏洞變得便宜，電腦被入侵會更頻繁。EFF 建議每個人更新瀏覽器與 App、改用密碼管理員並提防釣魚，也主張依賴開源的企業出錢出人維護。自己架網站的人另外要確認 PHP 已修補。
date: 2026-11-07T00:00:00+08:00
slug: eff-security-worse
categories:
  - security
watch:
  - date: 2026-12-07
    note: Censys 與其他量測對 PHP2Shell 未修補服務的數字是否下降，EFF 有沒有就資助開源提出具體做法
sources:
  - title: Computer Security Is About to Get a Lot Worse, Here's What You Can Do
    url: https://www.eff.org/deeplinks/2026/10/computer-security-about-get-lot-worse-heres-what-you-can-do
    publisher: EFF
    date: 2026-10-23
  - title: The Vulnerability Apocalypse and Why We Should Fund Open Source
    url: https://www.eff.org/deeplinks/2026/10/vulnerability-apocalypse-and-why-we-should-fund-open-source
    publisher: EFF
    date: 2026-10-23
  - title: Today's PHP Security Release, and How We're Strengthening PHP Security
    url: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
    publisher: The PHP Foundation
    date: 2026-10-21
  - title: "PHP: News Archive - 2026"
    url: https://www.php.net/archive/2026.php
    publisher: PHP
  - title: Usage Statistics and Market Share of PHP for Websites
    url: https://w3techs.com/technologies/details/pl-php
    publisher: W3Techs
  - title: "\"The panic hasn't turned into patching\": What security researchers really think about the PHP2Shell response"
    url: https://thenewstack.io/php2shell-unpatched-php-servers/
    publisher: The New Stack
    date: 2026-10-27
  - title: "CVE Volume vs Real Risk: Making Sense of Vulnpocalypse"
    url: https://brandefense.io/blog/cve-volume-vulnpocalypse-risk-prioritization/
    publisher: Brandefense
    date: 2026-08-26
  - title: AI vulnerability discovery is pushing 2026 CVEs toward 66,000
    url: https://www.helpnetsecurity.com/2026/06/15/first-2026-cve-forecast/
    publisher: Help Net Security
    date: 2026-06-15
  - title: Keeping Your Data Safe
    url: https://ssd.eff.org/module/keeping-your-data-safe
    publisher: EFF Surveillance Self-Defense
  - title: Choosing the Password Manager That's Right for You
    url: https://ssd.eff.org/module/choosing-the-password-manager-that-s-right-for-you
    publisher: EFF Surveillance Self-Defense
  - title: "How to: Avoid Phishing Attacks"
    url: https://ssd.eff.org/module/how-avoid-phishing-attacks
    publisher: EFF Surveillance Self-Defense
  - title: "Privacy Badger: EFF's Free Tracker Blocking Browser Extension"
    url: https://www.eff.org/pages/privacy-badger
    publisher: EFF
  - title: 更新 Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=zh-Hant
    publisher: Google Chrome 說明
  - title: 更新 iPhone 或 iPad
    url: https://support.apple.com/zh-tw/118575
    publisher: Apple 支援
    date: 2026-09-24
  - title: 檢查及更新 Android 版本
    url: https://support.google.com/android/answer/7680439?hl=zh-Hant
    publisher: Android 說明
authors:
  - anoni-net
---

美國數位權利組織 EFF 10 月 23 日發表兩篇文章，認為 OpenAI、Anthropic 等公司的前沿 AI 模型，讓找出零時差漏洞（廠商還不知道、還沒有修補的漏洞）變得便宜又容易。EFF 預期好轉之前情況會先變糟，第一篇給一般使用者的建議是基本的數位安全習慣，任何地方用電腦與手機的人都適用。第二篇以 PHP 的漏洞為例，主張依賴開源的企業出錢出人維護。網站用 PHP 的話，另外要確認伺服器上的 PHP 已經修補 10 月公開的漏洞。

依 EFF 的第二篇，美國國家漏洞資料庫（NVD）自 1988 年起收錄約 40 萬筆 CVE（公開漏洞的統一編號），光是 10 月就新提交 1.3 萬筆。EFF 據此推算歷來登錄的漏洞有 3% 是在 10 月找到的，也預估到年底時，史上所有漏洞會有超過四分之一出自 2026 年。數字沒有附上一手連結，圖說列的來源是 CVE Tracker。資安業者 Brandefense 10 月 26 日更新的分析列出，NVD 到 10 月 25 日已發布 86,533 筆 CVE 紀錄，2025 年全年是 48,151 筆。

EFF 的第二篇以網站伺服器上常用的程式語言 PHP 為例，提到它用在將近七成的網站。W3Techs 11 月 2 日的統計是在已知伺服端語言的網站裡占 69.1%。PHP 專案 10 月 21 日發布 8.5.12、8.4.27、8.3.36、8.2.35，修補兩個可讓未登入的攻擊者在伺服器上執行程式碼的漏洞。

根據資助 PHP 開發的 PHP Foundation 10 月 21 日的說明，2024 年外部出資的第一次稽核時已發現問題的徵兆，但沒有找到具體的攻擊方式。EFF 提到維護者當時找不到利用方式，降低了處理的優先順序，漏洞一直沒有修補。EFF 的說法是，2026 年 8 月研究者用 OpenAI 與 Anthropic 的最新模型各自重新發現，並找到利用的方法。基金會列出的發現者則是資安公司 Calif、OpenAI 與 Wiz，Anthropic 的 Claude Mythos 出現在基金會 2026 年稍早掃描 PHP 的段落，沒有列為發現者。

EFF 提到撰文時有超過 3,300 萬個網站仍在使用有漏洞的 PHP 版本。The New Stack 10 月 27 日引述資安公司 Censys 的網路掃描，約 3,250 萬個連上網際網路的 PHP 服務回報的是不安全的版本，另有約 6,130 萬個無法判斷版本。同一篇也提醒，Linux 發行版常把修補移植到舊版本而不改版本號。部分算成未修補的服務因此可能已經修補，依版本號推估的數字可能偏高。

依 EFF 的描述，PHP、OpenSSL、SQLite 這些專案幾乎在每台電腦上執行，維護團隊有的只有一個人。漏洞通報大量湧入，其中有些是假的，但很多是真的。依基金會的說明，PHP 的資安團隊 7 月 1 日到 10 月 21 日發布了 15 個 CVE，另外處理了一百多份無效、重複或無法重現的通報。AI 協助驗證通報，每個判斷與修補仍由人來做。

## 導讀觀點 {#perspective}

CVE 是替公開漏洞編號的紀錄，每一筆的嚴重程度不同，EFF 的第二篇把它們都寫成嚴重的漏洞。Help Net Security 6 月報導資安事件應變團隊的國際組織 FIRST 對全年 CVE 數量的預測，文中寫到部分成長來自 GitHub Security Advisories 與 VulnCheck 擴大編目、補登舊紀錄。

Brandefense 的同一份分析列出，美國 CISA 的已知遭利用漏洞目錄（KEV）2026 年到 10 月 23 日新增 272 筆，約每千筆 CVE 三筆。分析也提醒 KEV 收錄舊的 CVE，這個比例只能當粗略的參考。依本文的推論，紀錄增加的倍數不等於遭利用的漏洞增加的倍數，但需要套用的修補確實變多了。

在資助開源方面，EFF 主張企業應該投入金錢與人力維護它們所依賴的開源專案，沒有提出金額、機制或具體的基金。PHP Foundation 對資源的描述跟 EFF 不同，EFF 提到維護靠少數志工在空閒時間進行，基金會則表示 PHP 本身的資安工作仰賴一小群基金會出資的開發者與少數志工。基金會呼籲三類對象支持，分別是用 PHP 開發產品的公司、主機商與雲端及 Linux 發行版、政府與公共機構。基金會也承認修補延後是結構性的失誤，原因出在資安團隊的決策流程與資源不足。

EFF 給個人的第一項建議是讓瀏覽器與所有 App 隨時更新到最新的修補。EFF 的 Surveillance Self-Defense（SSD，監控自我防衛指南）提到，更新常會修補攻擊可利用的舊程式碼，部分舊的作業系統連安全性更新都不再提供。依 Chrome 的說明，有新版時瀏覽器會在背景自動更新，通常在關閉再重新開啟時完成。長時間不關瀏覽器的話，畫面上會出現等待更新的提示。

EFF 也建議安裝密碼管理員，每個網站各用一組密碼，一個網站被入侵時其他帳號的密碼不受影響。依 SSD 的說明，Apple、Google、Mozilla 內建的密碼管理員也可以用。Apple 的「密碼」App 預設端對端加密，Google 的密碼管理員要自行到設定裡用通關密語開啟裝置端加密。SSD 也列了 Bitwarden、KeePassXC 等獨立的密碼管理員，並提醒自動填入密碼是防範釣魚的重要保護。

EFF 另外建議考慮安裝阻擋追蹤器的工具，例如 EFF 免費的瀏覽器擴充功能 Privacy Badger，10 月 23 日的文章提到它已有 Safari 版。EFF 同一句也提醒要留意釣魚，SSD 說明釣魚是用假連結騙取密碼。EFF 也提醒資料外洩可能變多，常用的網站可能遭受比平常多的攻擊，部分服務可能因此中斷。

架設部落格或網站的人，EFF 建議確認自己或主機商已經修補 PHP 的漏洞。依 php.net 10 月 21 日的公告，這兩個漏洞沒有完整的緩解方式，更新是唯一安全的選擇。PHP 專案對 7.4、8.0、8.1 另外提供了給從原始碼建置者用的最小回補，其他舊版要看發行版或 LTS 業者有沒有回補。依本文從 EFF 這項建議推論，租用主機的人可以請業者確認是否已套用這次的修補。

每個用電腦與手機的人都適用的第一步，是開啟系統與 App 的自動更新，並定期關閉再重開瀏覽器。iPhone 的位置在「設定」、「一般」、「軟體更新」、「自動更新」，依 Apple 的說明會在充電且連上 Wi-Fi 時於夜間安裝。Android 的說明則寫大部分的安全性修補會自動安裝，時間依製造商與電信業者而不同，舊款裝置可能無法升級。依本文的推論，這些設定擋不住網站本身被入侵造成的資料外洩，各網站用不同的密碼能讓一處外洩不擴及其他帳號。
