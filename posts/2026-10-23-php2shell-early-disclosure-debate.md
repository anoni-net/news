---
title: PHP 漏洞的協調揭露與修補前的提前公開
description: PHP 兩個漏洞在協調揭露期間消息外流。10 月 21 日修補發布之前，有研究者公開據稱完整的技術細節，發行業者提前推出含修補的映像檔。資安業者也替客戶提前部署了防護，這篇整理各方對禁令與提前公開的看法，以及美國、歐盟與中國大陸的相關說明與法規。
date: 2026-10-23T00:10:00+08:00
slug: php2shell-early-disclosure-debate
categories:
  - security
follows:
  - 2026-10-23-php2shell-leaked-rce
sources:
  - title: Today's PHP Security Release, and How We're Strengthening PHP Security
    url: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
    publisher: The PHP Foundation
    date: 2026-10-21
  - title: PHP blames supply chain security biz Chainguard for putting huge chunks of the web at risk
    url: https://www.theregister.com/security/2026/10/22/php-blames-supply-chain-security-biz-chainguard-for-putting-huge-chunks-of-the-web-at-risk/5304611
    publisher: The Register
    date: 2026-10-22
  - title: PHP says AI review of critical bugs first sparked alarm in August, but signs surfaced in 2024
    url: https://therecord.media/php-foundation-statement-critical-vulnerabilities
    publisher: The Record
    date: 2026-10-21
  - title: Critical flaws strike PHP as disclosure embargo is broken
    url: https://www.itnews.com.au/news/critical-flaws-strike-php-as-disclosure-embargo-is-broken-629794
    publisher: iTnews
    date: 2026-10-21
  - title: Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot
    url: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/
    publisher: Amazon
    date: 2026-10-21
  - title: "PHP2Shell: PHP Remote Code Execution Exploited"
    url: https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/
    publisher: watchTowr
    date: 2026-10-21
  - title: Cloudflare deploys protections against php2shell vulnerability
    url: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/
    publisher: Cloudflare
    date: 2026-10-21
  - title: Vulnerability Disclosure Policy
    url: https://certcc.github.io/certcc_disclosure_policy
    publisher: CERT/CC
  - title: This Guide in a Nutshell
    url: https://certcc.github.io/CERT-Guide-to-CVD/tutorials/cvd_in_a_nutshell/
    publisher: CERT/CC
  - title: Guidelines and Practices for Multi-Party Vulnerability Coordination and Disclosure
    url: https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1
    publisher: FIRST
  - title: mailing-lists:distros
    url: https://oss-security.openwall.org/wiki/mailing-lists/distros
    publisher: Openwall
  - title: Coders' Rights Project Vulnerability Reporting FAQ
    url: https://www.eff.org/issues/coders/vulnerability-reporting-faq
    publisher: EFF
  - title: Article 7 Tools used for committing offences
    url: https://www.legislation.gov.uk/eudr/2013/40/article/7/data.html
    publisher: legislation.gov.uk（Directive 2013/40/EU）
  - title: 三部门关于印发网络产品安全漏洞管理规定的通知
    url: https://www.gov.cn/zhengce/zhengceku/2021-07/14/content_5624965.htm
    publisher: 中国政府网
  - title: Today's PHP security release, and how we're strengthening security
    url: https://news.ycombinator.com/item?id=50182987
    publisher: Hacker News
watch:
  - date: 2026-11-20
    note: PHP 是否調整禁令與提前通知的做法，PHP 與 Chainguard 等各方是否補充書面說明
authors:
  - anoni-net
---

PHP 10 月 21 日修補的兩個漏洞（CVE-2026-109618、CVE-2026-109619），可能讓沒有登入的攻擊者在網站伺服器上執行程式碼，消息在協調揭露期間外流。修補發布之前，有研究者公開據稱完整的技術細節，也有業者提前推出修補或替客戶部署防護。資安社群因此爭論修補發布之前，能不能、該不該提前公開，或提前保護一部分人。網站用 PHP 架設的組織先照前一篇導讀向主機商或外包商確認已套用修補，這場爭論關係到之後的漏洞會在什麼時候、先讓哪些人知道。

協調揭露（coordinated vulnerability disclosure）是發現漏洞的人先私下通知開發者，約定公開的日期。公開日之前的保密期間稱為禁令（embargo），讓開發者與下游的發行業者（把 PHP 這類軟體打包給使用者安裝的業者）有時間準備修補。

依 PHP Foundation 10 月 21 日的部落格，這次的協調揭露直到預定發布日的兩天前都運作正常。UTC 10 月 20 日 15:00 前後（台北時間 23:00 前後），漏洞編號開始在網路上流傳。PHP 在 UTC 19:30（台北時間 10 月 21 日 03:30）發出公告，預告修補改在 10 月 21 日發布，比原定提前一天。

同一篇部落格寫到，預告發出後，一家回報漏洞的資安公司誤公開了示範影片。PHP 從 UTC 10 月 20 日 23:00 前後（台北時間 10 月 21 日 07:00）起提供給少數關鍵基礎設施業者的緩解建議，也可能外流了。發行業者 Chainguard 跟其他發行業者一樣事先收到了修補，在 UTC 10 月 21 日 07:41（台北時間 15:41）公開含修補的容器映像檔（打包好、可以直接部署的軟體環境）。時間比提前後的發布時間早六個多小時，部落格的說法是，攻擊者因此可以在其他使用者還在等待時研究修補的內容。

依 iTnews 10 月 21 日的報導，漏洞編號在社群網站出現幾個小時後，一位研究者在網路上公開了據稱完整的技術細節。iTnews 沒有獨立確認內容是否有效。資安業者 watchTowr 的頁面寫到，它的平台客戶在 PHP 發布修補前 24 小時就有主動防禦。Cloudflare 的部落格寫到，對應的防火牆規則比公開揭露早約 9 小時，對免費與付費客戶預設啟用。

Amazon 10 月 21 日的威脅情報文章寫到，它的誘捕系統（故意放在網路上、用來觀察攻擊的系統）在 10 月 17 日就觀察到利用嘗試，比漏洞編號外流還早。文章也寫到不確定這些嘗試在真實系統上會不會成功，以及不清楚對方如何在揭露前取得資訊。

## 導讀觀點 {#perspective}

美國的漏洞協調中心 CERT/CC 的揭露政策，是收到通報 45 天後公開，有實際利用等情況時可能提前或延後。CERT/CC 的指南寫到，參與的人越多、禁令拖得越久，外流的可能就越高。

發行版之間共用的 distros 郵件列表規定禁令最長 14 天，偏好少於 7 天。成員不能把資訊分享給團隊以外的人，也不能先替客戶部署未說明的修補。PHP 有沒有透過 distros 通知發行版，到 10 月 22 日查不到。

外流之後要不要提前公開是第一個爭點，Chainguard 的執行長對 The Register 表示公司沒有洩漏。他說官方揭露前已經有人遭到攻擊，所以決定先推出修補。執行長說「It's coordinated vulnerability disclosure, unless there's evidence of active exploits in the wild」（除非有實際利用的證據，否則就是協調揭露）。到 10 月 22 日，本文沒有查到 Chainguard 自己發布的書面說明。

資安事件應變團隊的國際組織 FIRST 的多方協調指引，把合理的禁令期間限定在沒有事先公開、包括沒有實際利用的明確證據時。修補發布前，Amazon 的誘捕系統觀察到利用嘗試，但不確定能否在真實系統上成功。Cloudflare 的部落格也寫到，外洩期間觀察到針對客戶的攻擊流量。

依 PHP Foundation 的部落格，Chainguard 單方面打破禁令，無視多方數週的協調。依 The Register 的報導，Chainguard 的執行長則事先通知了 PHP 的協調管道。Hacker News 上有留言認為打破禁令沒有後果就會一再發生，也有留言認為這次已經損害了協調揭露的信任。PHP Foundation 的部落格也寫到，到公開發布時，PHP 安全團隊在流傳的概念驗證程式裡沒有找到能實際運作的利用程式。

提前保護給誰是第二個爭點，Hacker News 上替提前公開辯護的意見認為，協調揭露讓一般使用者無法自保。watchTowr 的平台客戶比 PHP 發布修補早 24 小時受到保護，Cloudflare 的防護規則則對免費與付費客戶都預設啟用。依 The Register 的報導，Chainguard 的映像檔任何人都能取得。

PHP 的部落格寫到，發行業者與長期支援的業者事先收到修補，緩解建議則交給少數關鍵基礎設施業者。部落格說明沒有在外流後立刻發布，是因為發行業者還在打包修補，立刻發布會讓許多使用者沒有簡便的更新方式。到 10 月 22 日，本文沒有查到針對提前通知名單的公開批評。

Chainguard 的執行長也對 The Register 表示，光是知道某個軟體有漏洞就足以找到它，他認為這是新的常態。Amazon 的文章同樣認為禁令只在別人找到同一個漏洞之前有效，但協調揭露仍然是正確的模式。文章提醒防守的一方，不應假設公開日就是最早被利用的日子，AI 輔助的分析讓從修補或公告做出可用的攻擊程式變得更便宜。

修補前公開漏洞細節是否違法，各地的規定不同。數位權利倡議組織 EFF 在寫給美國研究者的 FAQ 裡的立場是，法律應該很少管到揭露，「負責任揭露」模式之外的揭露也可能合法。FAQ 註明內容不是法律意見。同一份 FAQ 也寫到，揭露裡可以直接執行的程式碼越多，法律風險越高。

中國大陸 2021 年 9 月起施行的《网络产品安全漏洞管理规定》，適用於境內的網路產品提供者，以及從事漏洞發現、收集、發布的組織或個人。條文沒有寫明「境內」是否也限定後者。規定禁止在產品提供者推出修補措施之前發布漏洞資訊，認為有必要提前發布時，要與提供者協商並報工業和信息化部、公安部評估後發布。規定也禁止發布專門用於利用漏洞、從事危害網路安全活動的程式與工具。

歐盟《資訊系統攻擊指令》（Directive 2013/40/EU）第 7 條，要求會員國處罰意圖用於犯罪、未經授權而製作或提供主要為犯罪設計的程式，至少針對非輕微的案件。各會員國如何納入國內法，以及歐盟對公開漏洞資訊本身的指引，到 10 月 22 日查不到。本文比較 EFF 的整理與歐盟指令，兩者看的是意圖與內容。中國大陸的規定除了內容，也直接限制公開的時間點。

本文的建議是，網站用 PHP 架設的組織請主機商或外包商確認已套用修補，並檢查紀錄。Amazon 建議檢查紀錄時至少從 10 月 17 日查起，因為它在那一天就觀察到利用嘗試。Amazon 建議面向網際網路的系統遇到嚴重漏洞時，以小時計算修補與緩解的時程，認為 7 天或 30 天的處理期限已經不夠。要問主機商或外包商的問題，以及修補後的檢查，見文件站的[組織網站遇到重大漏洞時的確認與應對](https://anoni.net/docs/scenarios/org-website-vulnerability/){target="_blank"}。

PHP Foundation 的部落格提到正在調整安全團隊的決策流程，讓卡在困難取捨的漏洞更早交到領導層。Chainguard 的執行長則對 The Record 表示，業界要想辦法更快、更協調地處理這類情況。到 10 月 22 日為止，部落格沒有提到修改禁令的長度、提前通知的名單或對打破禁令者的處理。FIRST 的指引建議分享資訊的社群可以對破壞信任的成員設罰則，例如移出名單。

比較各方的做法時，讀者可以問幾個問題。禁令保護的是哪些人，提前收到通知與防護的名單如何決定，一般使用者在禁令期間有沒有自保的方法。提前推出修補時，還在等待的多數使用者是否先暴露給攻擊者。若如 Amazon 所說，AI 輔助的分析讓攻擊程式更快完成，禁令還能爭取到多少時間。
