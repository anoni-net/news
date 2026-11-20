---
title: AI 時代開源專案收緊的外部貢獻入口
description: curl 停掉漏洞獎金，GitHub 讓維護者限制誰能開 PR 與 issue，開源專案在 2026 年收緊外部貢獻的入口。作者認為收緊解決了大量低品質投稿的數量問題，信任的問題仍在。xz 後門與 Shai-Hulud 蠕蟲的惡意版本都由已經受信任的開發者帳號發布，缺的是審查人力與權限管理。
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
---

開源專案的原始碼仍然公開，外人能送進專案的東西卻越來越受限制。2026 年有專案停掉漏洞獎金，也有平台讓維護者只開放協作者發起修改，背後的理由都跟 AI 帶來的大量投稿有關。我想釐清收緊入口能保護到什麼，以及開源專案要為此付出什麼。

我的看法是，關掉外部的 PR（pull request，向專案提出的程式碼修改）能擋下 AI 送進來的大量低品質貢獻，收緊入口的專案提出的理由也多半是保護維護者的時間。收緊解決的是數量的問題，我擔心的是它被當成安全措施。我認為供應鏈攻擊多半從已經受信任的帳號或人進來，信任的問題仍在，開源專案真正缺的是審查人力與權限管理。

程式碼變得便宜之後，我認為可以算作貢獻的事也要跟著轉向。審查別人的修改、寫出能重現問題的測試、把問題描述清楚，都應該算進去。

## 外部貢獻入口的收緊 {#tightening}

網路傳輸工具 curl 的作者 1 月 26 日在部落格宣布結束漏洞獎金，1 月 31 日正式停止。依同一篇文章，計畫從 2019 年 4 月起共確認 87 個漏洞，付給研究者超過 10 萬美元。停掉獎金是為了取消提交捏造報告的誘因，通報改走 GitHub 的私下漏洞通報功能，或寄到專案的資安信箱。

依 GitHub 2 月 12 日的部落格文章，維護者已經可以把發起 PR 的權限限制在協作者，或整個關閉 PR。依 GitHub 的更新說明，6 月 17 日起維護者可以設定沒有寫入權限的使用者同時能開啟幾個 PR，到了上限要先關閉或合併舊的才能再開。草稿 PR 不計入上限，維護者也可以把信任的貢獻者加進例外名單（bypass list）。10 月 28 日再加上自動豁免的規則，依帳號註冊的天數或在該專案已合併的 PR 數放行。

只開放協作者的限制在 6 月 29 日延伸到 issue（回報問題或提出需求的討論串）。依更新說明，設定之後沒有寫入權限的人從 issue 頁面、留言、Discussions、Projects 與 Copilot 等入口都無法建立 issue。我比較在意這一項，因為我認為 issue 是不寫程式的人回報問題的主要管道。

追蹤 AI 貢獻政策的網站 Open Source Says No 到 11 月 20 日收錄 221 個專案，收錄門檻是 GitHub 上至少 5,000 顆星，或屬於發行版、程式語言執行環境、主要函式庫這類廣泛使用的基礎設施。其中 24 個禁止 AI 生成的貢獻，其餘多數在揭露、人工審查等條件下接受 AI 輔助的貢獻。網站在說明頁寫明只整理資訊，不判斷這些政策對不對。

## 產生成本與審查成本的落差 {#review-cost}

依 GitHub 2 月那篇部落格，PR 現在幾秒鐘就能產生，生成式 AI 讓人大量產出程式碼、issue 與資安通報。文中的說法是產生的成本降了，審查的成本沒有降。同一篇也提到維護者一直都在處理雜訊，低品質的投稿早就存在。Linux 核心的貢獻規則有相近的寫法，工具可能增加貢獻的數量，審查者與維護者的時間則是稀缺的資源。

依 curl 作者的文章，漏洞獎金計畫前幾年有超過 15% 的通報確認是漏洞，2025 年起降到 5% 以下。作者把原因歸到 AI 生成的劣質報告（原文 AI slop）暴增，連不明顯屬於劣質內容的報告，品質也在下降。情況從 2024 年下半年開始，2025 年急遽惡化。同一篇也提到 PR 在 curl 沒有造成問題，200 項 CI 工作（持續整合，每次修改都自動執行的測試）全部通過，才值得投入人力審查。

Home Assistant（開源的智慧家庭平台）的一位維護者 5 月 31 日在個人網站提到，貢獻者的產出被放大，維護者仍然是驗證的瓶頸。依這位維護者的描述，以前送出修改前需先讀懂程式、寫出修改、執行測試、說明結果，維護者看到之前已經有一道摩擦。這位維護者提出的判準是送出的人是否理解、驗證過、願意負責，有沒有用到 AI 不在判準裡。

## 收緊入口能防範與無法防範的風險 {#what-it-stops}

前面引用的專案，沒有一個宣稱收緊入口能防範供應鏈攻擊。我把兩件事放在一起看，是因為 Python 套件的共同維護組織 Jazzband 在結束營運的公告裡，把開放加入的模式、安全的營運與 xz 後門連在一起。

漏洞獎金取消金錢誘因、PR 設上限、issue 只開放協作者，我把三項措施都讀成針對大量投稿的做法，也認為對數量的問題有效。curl 的作者也提醒他們的判斷有可能錯，錯了會再採取進一步的做法。依 The Register 10 月 21 日的報導，curl 當週宣布把低與中度嚴重性的漏洞移到公開處理，報導的說法是為了保護幾乎被 AI 輔助的通報壓垮的資安團隊。我讀起來停掉獎金之後數量的壓力仍在，入口收緊能減輕多少，要看之後的數字。

xz 是 Linux 系統常見的壓縮工具，2024 年 3 月曝光的 xz 後門是對我的主張最不利的例子，植入後門的帳號一開始是外部貢獻者。依 xz 專案網站的說明，5.6.0 與 5.6.1 兩版的發行壓縮檔（tarball）含有後門，由那個帳號製作並簽署。

依一份逐日引用 xz-devel 郵件列表的公開時間線，那個帳號 2021 年 10 月寄出第一個無害的修補，2022 年底開始直接合併修改。2024 年 2 月，該帳號把後門藏進測試用的二進位檔，接著發行 5.6.0。

我承認，一個完全不收外部修補的專案，不會給這個帳號第一個修補的起點。依時間線的日期計算，從第一個修補到發行含後門的版本隔了兩年四個月。我的看法是收緊只能延後這類長期取信的攻擊，有耐心的攻擊者仍然可以用時間換取信任。

依開源資安郵件列表 oss-security 上公開警告後門的那封信，後門有一部分只存在發行的壓縮檔裡，是 git 上的原始碼沒有的一行建置腳本。發行版與使用者常下載的是維護者另外打包並加上數位簽章的壓縮檔，內容不一定跟 git 上公開的原始碼相同。我的推論是審查 PR 也看不到那行腳本，關鍵在誰能製作與簽署發行檔。

原維護者 2022 年在郵件列表提到自己能投入的心力有限（依同一份時間線轉錄）。我認為 xz 暴露的弱點在維護者太少與權限管理，關掉入口不會讓專案多出一位能分擔審查與發行的人。

Jazzband 開放任何人加入，成員共用 push 權限（直接把修改推進專案的權限），3 月宣布逐步結束營運、關閉新註冊。依公告，Jazzband 十年間累積 3,135 名成員、維護過 84 個專案。公告把 AI 生成的垃圾 PR 與 issue 列為開放加入、共用 push 權限撐不下去的原因，負責人也表示無法繼續把 push 權限交給每個加入的人，同時安全地營運。

公告另外列了一人包辦的問題，每一次專案轉移、PyPI（Python 的套件發布平台）權限變更與基礎設施的決定，都經過負責人一個人。負責人在同一篇公告把 xz 描述成獨自維護的人倦怠之後、由惡意的人補上空缺的例子。公告寫的觸發原因是 AI 投稿，我把它歸到權限管理的問題，撐不下去的是共用的 push 權限。

依美國網路安全暨基礎設施安全局（CISA）2025 年 9 月 23 日的警示，名為 Shai-Hulud 的自我複製蠕蟲入侵了 500 多個 npm（JavaScript 的套件登錄庫）套件。警示沒有寫攻擊者如何取得初步存取，之後惡意程式掃描環境裡的憑證，鎖定 GitHub 的權杖與雲端服務的金鑰。蠕蟲接著以被入侵的開發者身分，把程式碼注入其他套件並發布新版本。CISA 的警示建議更換所有開發者的憑證，並在 GitHub 與 npm 帳號強制使用防釣魚的多因素驗證（登入時除了密碼，另外要求一道驗證）。

CISA 的警示列出的建議裡，沒有一項是限制外部 PR。我認為 xz 的攻擊者用時間換取信任，Shai-Hulud 則掃描並竊取開發者的憑證、以被入侵的開發者身分發布，兩者造成傷害時都利用了已經受信任的帳號。兩起事件不足以構成統計，「多半」是我從這兩個例子推出的判斷。

## 新維護者的來源 {#new-maintainers}

GitHub 2 月那篇部落格也提到，限制可能不成比例地影響出於善意的第一次貢獻者，所以這些控制都是選用、可以調整的。我的推論是，不符合自動豁免條件的新人要等維護者手動加進例外名單，才能超過同時開啟 PR 的數量上限。

兩位軟體工程研究者 9 月在 arXiv（學術論文的預印本平台）公開一篇論文。依摘要，AI 降低了實作修改的成本，審查別人的貢獻相對仍然昂貴。有些專案因此限制誰能提交實作、同時歡迎其他形式的參與。論文認為原因在那些程式碼已經不值得付出審查的成本，跟是否由 AI 生成無關。

研究者把這種形態稱為管家型社群（stewardship community），一小群核心成員保留實作的權限，更廣的社群不寫程式碼也能影響軟體。依論文的定義，在這種社群裡寫程式碼越來越要先經過核准。摘要也提醒，AI 可能取代實作的人力，同時削弱開源社群自我更新的方式。

另一篇 10 月在 arXiv 公開的論文，研究者整理了 31 個組織或個人的 50 份灰色文獻（部落格、公告這類沒有經過學術出版的文件）。依摘要，多數做法以某種形式保留 PR 再加上工具或限制，其中限制最常被回報採用。

Jazzband 宣布結束營運之後，專案要另外找地方。公告建議 Django 相關的專案轉到 Django Commons，部分專案已經轉過去，公告當時 Django Commons 有 5 位管理者與 15 個活躍的專案。pip-tools、tablib 這些不屬於 Django 的專案，負責人表示不知道有對等的去處。

我預期入口收緊之後，專案更難從外部貢獻者裡培養新的維護者，維護者不足的問題仍會留到下一次。我認為這個代價跟 xz 的弱點是同一件事，維護者太少，攻擊者才有空缺可以補。

## 貢獻的轉向與讀者可以留意的訊號 {#what-readers-can-do}

我不反對專案收緊入口，面對大量投稿，維護者需要先保護自己的時間。我希望省下來的時間投進審查與權限管理，例如誰能合併、誰能發行、權杖如何保管，前面提到的 CISA 建議可以當作檢查的起點。

我認為值得算作貢獻的，是降低維護者驗證成本的工作。xz 後門被發現的起點，是一位開發者在 Debian 的開發版（sid）上注意到 ssh 登入異常耗用 CPU，以及 valgrind（檢查記憶體錯誤的工具）回報的錯誤。這位開發者追查之後在 oss-security 公開警告，我把那封信看成一份問題描述，價值不下於一份修補。

想參與的人可以先讀專案的貢獻政策。依 Open Source Says No 收錄的政策，Linux 核心要求貢獻者理解並能為送出的每一部分辯護。依 curl 的貢獻文件，專案接受 AI 輔助寫成的程式碼，前提是符合程式風格、文件與測試等一般要求。用 AI 工具找問題的通報者，也要在報告裡揭露。

不寫程式的人也能參與，回報問題時寫清楚版本、操作步驟與能否重現，就能省下維護者驗證的時間。專案把 issue 限制在協作者時，先看貢獻文件有沒有寫其他回報管道。

使用隱私工具的人，我建議看專案有幾位活躍的維護者、貢獻政策有沒有寫清楚 AI 與權限的規則，以及漏洞從通報到修補花了多久（貢獻文件、版本紀錄與資安公告多半可以找到）。到 11 月 20 日，Open Source Says No 沒有收錄 Tor、Tails、Signal 等工具，有沒有相關規定要到各專案的貢獻文件確認。xz 的 README 在 2022 年底列了兩位維護者（依前面那份時間線），其中一位就是後來植入後門的帳號。因此這些訊號只能當作參考，不能保證安全。

## 延伸閱讀 {#further-reading}

- [AI 加速找漏洞之後的個人防護與開源維護](https://anoni.net/news/2026/11/eff-security-worse/)：PHP 的資安團隊一邊修補真漏洞，一邊處理一百多份無效或無法重現的通報，處境跟 curl 相近
- [AI 程式開發工具的擴充套件後門與惡意指引檔](https://anoni.net/news/2026/11/ai-devtools-supply-chain/)：被竄改的擴充套件以已驗證的帳號出現在市集上，另一起經由受信任的發布管道進來的事件
- [開源影像編輯軟體 Compositor 與 AI 生成程式碼的維護和稽核](https://anoni.net/news/2026/10/compositor-image-editor/)：作者自述程式全由 AI 寫成，外部開發者送來的八個修補 PR 被一起關閉，從作者這一端看 AI 程式碼的審查
