---
title: AI 時代開源專案收緊的外部貢獻入口
description: curl 停掉漏洞獎金，GitHub 讓維護者限制誰能開 PR 與 issue，開源專案在 2026 年收緊外部貢獻的入口。作者認為收緊處理的是大量低品質投稿的數量問題，信任的問題仍在。xz 後門與 Shai-Hulud 蠕蟲的惡意版本都由已經受信任的開發者帳號發布，缺的是審查人力與權限管理。
date: 2026-11-25T00:15:00+08:00
slug: open-source-contributions-ai
categories: [column]
authors: [toomore]
sources:
  - title: The end of the curl bug-bounty
    url: https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
    publisher: curl 作者的部落格
    date: 2026-01-26
  - title: Contributing to the curl project
    url: https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md
    publisher: curl
  - title: Welcome to the Eternal September of open source. Here's what we plan to do for maintainers.
    url: https://github.blog/open-source/maintainers/welcome-to-the-eternal-september-of-open-source-heres-what-we-plan-to-do-for-maintainers/
    publisher: GitHub
    date: 2026-02-12
  - title: Limit open pull requests for users without write access
    url: https://github.blog/changelog/2026-06-17-limit-open-pull-requests-for-users-without-write-access/
    publisher: GitHub
    date: 2026-06-17
  - title: Restrict issue creation to collaborators only
    url: https://github.blog/changelog/2026-06-29-restrict-issue-creation-to-collaborators-only/
    publisher: GitHub
    date: 2026-06-29
  - title: "Pull request limits: Exempt contributors by age or history"
    url: https://github.blog/changelog/2026-10-28-pull-request-limits-exempt-contributors-by-age-or-history
    publisher: GitHub
    date: 2026-10-28
  - title: All projects
    url: https://osssaysno.com/all
    publisher: Open Source Says No
  - title: About
    url: https://osssaysno.com/about
    publisher: Open Source Says No
  - title: Kernel Guidelines for Tool-Generated Content
    url: https://github.com/torvalds/linux/blob/master/Documentation/process/generated-content.rst
    publisher: Linux kernel
  - title: Open source was not ready for AI-speed contributions
    url: https://frenck.dev/open-source-was-not-ready-for-ai-speed-contributions/
    publisher: Home Assistant 維護者的部落格
    date: 2026-05-31
  - title: XZ Utils backdoor
    url: https://tukaani.org/xz-backdoor/
    publisher: Tukaani
  - title: backdoor in upstream xz/liblzma leading to ssh server compromise
    url: https://www.openwall.com/lists/oss-security/2024/03/29/4
    publisher: oss-security
    date: 2024-03-29
  - title: Timeline of the xz open source attack
    url: https://research.swtch.com/xz-timeline
    publisher: xz 攻擊時間線
  - title: AI cuts coding time, but it's also filling open source's inbox with crap
    url: https://www.theregister.com/ai-and-ml/2026/10/21/ai-cuts-coding-time-but-its-also-filling-open-sources-inbox-with-crap/5304389
    publisher: The Register
    date: 2026-10-21
  - title: Sunsetting Jazzband
    url: https://jazzband.co/news/2026/03/14/sunsetting-jazzband
    publisher: Jazzband
  - title: Widespread Supply Chain Compromise Impacting npm Ecosystem
    url: https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
    publisher: CISA
    date: 2025-09-23
  - title: "Open Source Stewardship Communities: \"We need you, but not your pull request\""
    url: https://arxiv.org/abs/2609.12236
    publisher: arXiv
    date: 2026-09-10
  - title: What Will Replace Pull Requests? Rethinking Software Collaboration for AI Agents
    url: https://arxiv.org/abs/2610.34933
    publisher: arXiv
    date: 2026-10-26
  - title: Stop Closing the Door. Fix the House.
    url: https://angiejones.tech/stop-closing-the-door-fix-the-house/
    publisher: goose 維護者的部落格
    date: 2026-02-07
  - title: In the wake of the xz utils hack, two-thirds of maintainers are less trusting of contributors
    url: https://dev.to/tidelift/in-the-wake-of-the-xz-utils-hack-two-thirds-of-maintainers-are-less-trusting-of-contributors-4kch
    publisher: Tidelift
    date: 2024-10-15
  - title: The Open Source Definition
    url: https://opensource.org/osd
    publisher: Open Source Initiative
  - title: SQLite Copyright
    url: https://sqlite.org/copyright.html
    publisher: SQLite
  - title: "Lua: FAQ"
    url: https://www.lua.org/faq.html
    publisher: Lua
---

開源專案的原始碼仍然公開，外人能送進專案的東西卻越來越受限制。我把外人向專案送出程式碼修改、回報問題或通報漏洞的管道，稱為外部貢獻的入口。2026 年有專案停掉漏洞獎金（付錢給回報漏洞的人的計畫），也有程式碼託管平台 GitHub 讓維護者只開放協作者（被專案加入、能直接修改程式碼的成員）發起修改，背後的理由都跟 AI 帶來的大量投稿有關。我想釐清收緊入口能保護到什麼，以及開源專案要為此付出什麼。

我的看法是，關掉外部的 PR（pull request，向專案提出的程式碼修改）能擋下 AI 送進來的大量低品質貢獻，收緊入口的專案提出的理由也多半是保護維護者的時間。**收緊處理的是數量的問題，信任的問題仍在**。我認為供應鏈攻擊（在別人依賴的軟體裡植入惡意程式，隨著更新散布到使用者端）多半從已經受信任的帳號或人進來，開源專案真正缺的是審查人力與權限管理。我擔心的是收緊被當成安全措施，Python 套件的共同維護組織 Jazzband 在結束營運的公告裡，就把開放加入跟能否安全營運連在一起。

AI 工具讓產生程式碼變得又快又容易，審查人力就成了瓶頸，所以我認為開源專案看待貢獻的方式也要跟著調整。開源專案收到一份修改時，維護者要先讀懂程式、確認沒有錯誤或安全問題才會合併，這個步驟稱為審查（review）。審查別人的修改、寫出能重現問題的測試、把問題描述清楚，本來就是維護專案的重要工作，以往多半由維護者自己承擔。現在送來的程式碼變多，我認為這些工作更需要外部貢獻者一起分擔，也應該被當成貢獻看待。

## 外部貢獻入口的收緊 {#tightening}

curl 是一套常用的網路傳輸工具，作者 1 月 26 日在部落格宣布結束漏洞獎金，1 月 31 日正式停止。根據同一篇文章，這個獎金計畫從 2019 年 4 月開始總共確認了 87 個漏洞，發給通報者的獎金合計超過 10 萬美元。作者寫明停掉獎金的目的，是不再讓人有動機捏造報告來領獎金。之後要通報漏洞的人，改用 GitHub 的私下通報功能，或寄信到專案的資安信箱。

依 GitHub 2 月 12 日的部落格文章，維護者已經可以只讓協作者（collaborator）發起 PR，也可以整個關閉 PR。依 GitHub 的更新說明，6 月 17 日起維護者可以設定其他使用者最多能同時開幾個 PR。到了上限，要等舊的被關閉或合併才能再開新的。

草稿狀態的 PR 不算在上限裡，維護者也可以把信任的貢獻者加進例外名單（bypass list）。10 月 28 日 GitHub 再加上自動豁免的規則，讓帳號註冊滿一定天數或已經在該專案合併過一定數量 PR 的人超過上限。

6 月 29 日，GitHub 把同樣的限制延伸到 issue（回報問題或提出需求的討論串），專案可以設定只有協作者能開 issue。依更新說明，開啟這個設定之後，其他人從專案頁面上的任何地方都無法建立 issue。我比較在意這一項，因為我認為 issue 是不寫程式的人回報問題的主要管道。

收緊也發生在各專案自己的貢獻政策上，追蹤 AI 貢獻政策的網站 Open Source Says No 到 11 月 20 日收錄 221 個專案。收錄門檻是 GitHub 上至少 5,000 顆星，或屬於發行版、程式語言執行環境、主要函式庫這類廣泛使用的基礎設施。其中 24 個禁止 AI 生成的貢獻，其餘大多數接受 AI 輔助的貢獻但附帶條件，例如要揭露用了 AI、要經過人工審查。網站在說明頁寫明只整理資訊，不判斷這些政策對不對。

## 產生成本與審查成本的落差 {#review-cost}

依 GitHub 2 月那篇部落格，PR 現在幾秒鐘就能產生，生成式 AI 讓人大量產出程式碼、issue 與資安通報。文中的說法是產生的成本降了，審查的成本沒有降。同一篇也提到維護者一直都在處理雜訊，低品質的投稿早就存在。Linux 核心的貢獻規則也有相近的說法：工具可能讓貢獻的數量增加，但審查者與維護者的時間有限。

依 curl 作者的文章，漏洞獎金計畫前幾年有超過 15% 的通報確認是漏洞，2025 年起降到 5% 以下。作者把原因歸到 AI 生成的劣質報告（原文 AI slop）暴增，就算是一眼看不出是劣質內容的報告，品質也在下降。情況從 2024 年下半年開始，2025 年急遽惡化。

同一篇也提到 PR 在 curl 沒有造成問題，因為在一份 PR 通過全部 200 項 CI 工作（持續整合，每次修改都會自動執行的測試）之前，專案不必花任何人力看它。我把這看成用自動檢查降低維護者驗證成本的例子，curl 收緊的是漏洞通報這個入口，PR 仍然開著。

Home Assistant（開源的智慧家庭平台）的一位維護者 5 月 31 日在個人網站提到，貢獻者借助 AI 能送出更多修改，但每一份仍要由維護者驗證。依這位維護者的描述，以前貢獻者要先讀懂程式、寫出修改、執行測試、說明結果才能送出一份修改，這些步驟本身就是一道門檻。這位維護者提出的判斷標準是，送出修改的人是否理解自己的修改、驗證過、願意負責，有沒有用到 AI 則不在標準裡。我讀起來，這個標準跟 curl 的自動檢查一樣，在意的都是驗證由誰承擔。

## 收緊入口能防範與無法防範的風險 {#what-it-stops}

我在前面引用的幾份文件裡，讀到的收緊理由都是投稿的數量與維護者的時間，沒有讀到防範供應鏈攻擊。前言提到的 Jazzband 公告是例外，它把開放加入的模式跟能否安全營運連在一起，也舉了 xz 後門當作獨自維護的人倦怠之後的例子。所以我把收緊入口跟供應鏈安全放在一起看。

取消漏洞獎金、限制 PR 的數量、只讓協作者開 issue，我把這三項措施都看成針對大量投稿的做法，也認為能減輕數量的問題。curl 的作者也提醒，停掉獎金的判斷可能有錯，錯了會再採取進一步的做法。依 The Register 10 月 21 日的報導，curl 當週宣布把低與中度嚴重性的漏洞移到公開處理，報導寫的理由是 curl 的資安團隊幾乎被 AI 輔助產生的通報壓垮。從這則報導看，停掉獎金之後通報的壓力仍在，收緊入口能減輕多少要看之後的數字。

xz 是 Linux 系統常見的壓縮工具。從入口的角度看 2024 年 3 月曝光的 xz 後門，會認為收緊入口有助於防範這類攻擊，跟我的看法不同。植入後門的帳號一開始就是外部貢獻者。依 xz 專案網站的說明，5.6.0 與 5.6.1 兩個版本的發行壓縮檔（tarball）含有後門，這兩個壓縮檔就是由那個帳號製作並簽署的。

依一份逐日引用 xz-devel 郵件列表的公開時間線，那個帳號 2021 年 10 月寄出第一個無害的修補，到了 2022 年底已經可以直接把修改合併進專案。2024 年 2 月，該帳號把後門藏進測試用的二進位檔，接著發行 5.6.0。

從這個角度看，如果專案完全不收外部的修補，這個帳號連第一步都踏不進來。依時間線的日期計算，從第一個修補到發行含後門的版本，中間隔了兩年四個月。**我的看法是，收緊入口只能延後這類花長時間取得信任的攻擊，有耐心的攻擊者仍然可以用時間換取信任**。

依開源資安郵件列表 oss-security 上公開警告後門的那封信，後門有一部分只存在發行的壓縮檔裡，是 git 上的原始碼沒有的一行建置腳本。我的理解是，發行版與使用者常下載維護者另外打包並加上數位簽章的壓縮檔，內容不一定跟 git 上公開的原始碼相同。所以我推論，就算仔細審查每一個 PR 也看不到那行腳本，關鍵在於誰有權限製作並簽署發行檔。

原維護者 2022 年在郵件列表提到自己能投入的心力有限（依同一份時間線轉錄）。**我認為 xz 事件暴露的弱點，是維護者太少，以及發行權限交給誰的管理問題。關掉入口，也不會讓專案多出一位能分擔審查與發行的人**。

Jazzband 開放任何人加入，成員共用 push 權限（直接把修改推進專案的權限），3 月宣布逐步結束營運、關閉新註冊。依公告，Jazzband 十年間累積 3,135 名成員、維護過 84 個專案。公告列出的原因是 AI 生成的大量垃圾 PR 與 issue，讓開放加入、共用 push 權限的做法撐不下去。負責人也表示，不能再一邊把 push 權限交給每個加入的人，一邊還要安全地營運。

公告也列出另一個問題：每一次專案轉移、PyPI（Python 的套件發布平台）權限變更與基礎設施的決定，都要經過負責人一個人。負責人在同一篇公告把 xz 描述成獨自維護的人倦怠之後、由惡意的人補上空缺的例子。

公告寫的直接原因是 AI 投稿，我則把它看成權限管理的問題。在 Jazzband，任何人加入就能取得 push 權限，可以直接把修改推進組織裡的專案。垃圾投稿變多之後，我認為負責人難以判斷每個加入的人是否可信，也沒有其他人能分擔把關。加入就給權限的做法，因此撐不下去。

Shai-Hulud 蠕蟲則是盜用受信任帳號的例子。依美國網路安全暨基礎設施安全局（CISA）2025 年 9 月 23 日的警示，這個會自我複製的蠕蟲入侵了 500 多個 npm（JavaScript 的套件登錄庫）套件。警示沒有寫攻擊者一開始如何入侵，只寫到惡意程式會搜尋環境裡存放的憑證，鎖定 GitHub 的權杖（讓程式代替密碼登入帳號的金鑰）與雲端服務的金鑰。蠕蟲接著以被入侵的開發者身分登入 npm，把惡意程式碼加進其他套件，再發布新版本。

CISA 的警示建議更換所有開發者的憑證，並在 GitHub 與 npm 帳號強制使用防釣魚的多因素驗證（登入時除了密碼，另外要求一道驗證）。這些建議裡沒有一項是限制外部 PR。我認為 xz 的攻擊者用時間換取信任，Shai-Hulud 則掃描並竊取開發者的憑證、以被入侵的開發者身分發布，**兩者造成傷害時都利用了已經受信任的帳號**。差別在於 xz 的帳號是自己花時間累積信任，Shai-Hulud 則是盜用別人已經累積的信任。

## 新維護者的來源 {#new-maintainers}

GitHub 2 月那篇部落格也提到，這些限制可能對第一次參與、出於善意的貢獻者影響特別大，所以 GitHub 把它們做成選用、可以調整的設定。我的推論是，不符合自動豁免條件的新人要等維護者手動加進例外名單，才能超過同時開啟 PR 的數量上限。

兩位軟體工程研究者 9 月在 arXiv（學術論文的預印本平台）公開一篇論文。依摘要，AI 讓寫出一份修改的成本降低，審查別人的貢獻卻仍然很花力氣。因此有些專案限制誰可以提交程式碼，同時歡迎其他形式的參與。論文認為，這些專案限制的原因是那些程式碼已經不值得花力氣審查，跟程式碼是不是 AI 寫的無關。

研究者把這種形態稱為管家型社群（stewardship community）。在這種社群裡，只有一小群核心成員能把程式碼寫進專案，其他人不寫程式碼也仍然能影響軟體。依論文的定義，在這種社群裡想寫程式碼越來越需要先經過核准，不能自己主動送出。摘要也提醒，AI 可能取代原本由外部貢獻者提供的寫程式人力，同時削弱開源社群自我更新（培養新成員接手）的方式。

另一篇 10 月在 arXiv 公開的論文，研究者整理了 31 個組織或個人的 50 份灰色文獻（部落格、公告這類沒有經過學術出版的文件）。依摘要，大多數做法仍然保留 PR 再加上工具或限制，其中最常被採用的是加上限制。我的推論是，收緊入口已經是最常見的回應，越來越多專案會遇到新維護者從哪裡來的問題。

我預期入口收緊之後，專案更難從外部貢獻者裡培養新的維護者，維護者不足的問題就會一直存在。我認為這個代價跟 xz 的弱點是同一件事，維護者太少，攻擊者才有空缺可以補。

## 貢獻的轉向與讀者可以留意的訊號 {#what-readers-can-do}

也有人認為關掉入口違背了開源的精神。AI 代理工具 goose 的一位維護者 2 月在部落格寫，關上大門不是解方，開源特別的地方不能放棄。這位維護者主張把貢獻的門檻寫清楚，交給 CI 自動檢查。Tidelift 2024 年在 xz 事件後做的維護者調查裡，也有受訪者表示預設信任新人才是開源的作法，應該維持下去。

我的看法不同，「精神」的說法因人而異，能當共同基準的是開源定義。依開放原始碼促進會（OSI）的開源定義，條文規範的是自由散布、取得原始碼與修改這些授權條件，沒有要求專案接受外部的貢獻。SQLite 與 Lua 的官方說明都自稱開源軟體，SQLite 只接受簽署聲明、把貢獻放進公有領域的人送來的修補，Lua 則請大家不要送 PR。**我認為授權保障的是每個人都能取用、修改程式碼，治理方式可以由各專案依自己的人力決定**。

我不反對專案收緊入口，面對大量投稿，維護者需要先保護自己的時間。我希望**省下來的時間投進審查與權限管理**，例如誰能合併、誰能發行、權杖如何保管，前面提到的 CISA 建議可以當作檢查的起點。goose 那位維護者提的做法是把門檻寫清楚、交給 CI 自動檢查，我也認為值得做，同樣是在降低驗證成本。

我認為值得算作貢獻的，是**降低維護者驗證成本的工作**。xz 後門被發現的起點，是一位開發者在 Linux 發行版 Debian 的開發中版本上注意到用 ssh 遠端登入時異常耗用 CPU，以及 valgrind（檢查記憶體錯誤的工具）回報的錯誤。這位開發者追查之後在 oss-security 公開警告，我把那封信看成一份問題描述，價值不下於一份修補。

想參與的人可以先讀專案的貢獻政策。依 Open Source Says No 收錄的政策，Linux 核心要求貢獻者理解自己送出的所有內容，並且能為它辯護。依 curl 的貢獻文件，專案接受 AI 輔助寫成的程式碼，前提是符合程式風格、文件與測試等一般要求。用 AI 工具找問題的通報者，也要在報告裡揭露。

不寫程式的人也能參與，回報問題時寫清楚版本、操作步驟與能否重現，就能省下維護者驗證的時間。專案把 issue 限制在協作者時，先看貢獻文件有沒有寫其他回報管道。

使用隱私工具的人，我建議看專案有幾位活躍的維護者、貢獻政策有沒有寫清楚 AI 與權限的規則，以及漏洞從通報到修補花了多久（貢獻文件、版本紀錄與資安公告多半可以找到）。到 11 月 20 日，Open Source Says No 沒有收錄 Tor、Tails、Signal 等工具。這份清單只收 GitHub 星數或使用範圍達到門檻的專案，沒收錄不代表沒有規定，要到各專案的貢獻文件確認。

這些訊號只能當作參考，維護者人數多也不保證安全。xz 的 README 在 2022 年底列了兩位維護者（依前面那份時間線），其中一位就是後來植入後門的帳號。

你常用的隱私工具，貢獻文件有沒有寫到 AI 與權限的規則？如果專案不再接受外部的 PR，你會用什麼方式參與？

## 延伸閱讀 {#further-reading}

- [AI 加速找漏洞之後的個人防護與開源維護](https://anoni.net/news/2026/11/eff-security-worse/)：PHP 的資安團隊一邊修補真漏洞，一邊處理一百多份無效或無法重現的通報，處境跟 curl 相近
- [AI 程式開發工具的擴充套件後門與惡意指引檔](https://anoni.net/news/2026/11/ai-devtools-supply-chain/)：被竄改的擴充套件以已驗證的帳號出現在市集上，另一起經由受信任的發布管道進來的事件
- [開源影像編輯軟體 Compositor 與 AI 生成程式碼的維護和稽核](https://anoni.net/news/2026/10/compositor-image-editor/)：作者自述程式全由 AI 寫成，外部開發者送來的八個修補 PR 被一起關閉，從作者這一端看 AI 程式碼的審查
