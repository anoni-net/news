---
title: 加州 AB 1856 的開源作業系統豁免
description: 美國加州 9 月簽署的 AB 1856，修改了要求作業系統在帳號設定時詢問使用者年齡的州法。修改後，發行作業系統或 App 時用的授權若允許複製、再散布與修改，發行的人或組織就不算受規範的作業系統業者。規定 2027 年起適用，條文以加州的帳號持有人為對象。
date: 2026-10-11T00:00:00+08:00
slug: california-ab1856-open-source-exemption
categories:
  - censorship
sources:
  - title: "AB-1856 Age verification signals: software applications."
    url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1856
    publisher: California Legislative Information
    date: 2026-09-11
  - title: "AB 1856: Age verification signals: software applications."
    url: https://calmatters.digitaldemocracy.org/bills/ca_202520260ab1856
    publisher: CalMatters Digital Democracy
    date: 2026-09-10
  - title: "AB-1043 Age verification signals: software applications and online services."
    url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1043
    publisher: California Legislative Information
    date: 2025-10-14
  - title: "Press release: child safety chatbot and social media laws signed"
    url: https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/
    publisher: Office of the Governor of California
    date: 2026-09-10
  - title: CONCERNING AGE ATTESTATION FOR USERS OF COMPUTING DEVICES.
    url: https://leg.colorado.gov/laws/session-laws/SB26-051/343/download
    publisher: Colorado General Assembly
    date: 2026-06-03
  - title: California Steps Back From Dangerous Expansion of Its Age-Gating Law
    url: https://www.eff.org/deeplinks/2026/07/california-steps-back-dangerous-expansion-its-age-gating-law
    publisher: EFF
    date: 2026-07-15
  - title: A.B. 1043's Internet Age Gates Hurt Everyone
    url: https://www.eff.org/deeplinks/2026/03/ab-1043s-internet-age-gates-hurt-everyone
    publisher: EFF
    date: 2026-03-12
  - title: System76 on Age Verification Laws
    url: https://system76.com/blog/post/system76-on-age-verification
    publisher: System76
    date: 2026-03-05
  - title: Bits from the DPL
    url: https://lists.debian.org/debian-devel-announce/2026/04/msg00001.html
    publisher: Debian
    date: 2026-04-04
  - title: Ubuntu's response to California's Digital Age Assurance Act (AB 1043)
    url: https://discourse.ubuntu.com/t/ubuntus-response-to-californias-digital-age-assurance-act-ab-1043/77948
    publisher: Ubuntu Discourse
    date: 2026-03-04
  - title: "userdb: add birthDate field to JSON user records"
    url: https://github.com/systemd/systemd/pull/40954
    publisher: GitHub
    date: 2026-03-05
regions:
  - US
watch:
  - date: 2026-12-15
    note: AB 1043 與 AB 1856 2027 年 1 月 1 日開始適用前，主要的作業系統業者與 Linux 發行版有沒有公布年齡訊號的做法，以及 Debian、Fedora 等專案是否說明豁免的適用
authors:
  - anoni-net
---

美國加州州長 9 月 10 日簽署 AB 1856，修改 2025 年通過的 Digital Age Assurance Act（AB 1043，數位年齡確認法）。原法要求作業系統業者在帳號設定時，讓帳號持有人（成年使用者本人，或未成年使用者的家長）填寫使用者的年齡，再把年齡範圍以訊號（signal）的形式提供給 App。AB 1856 另外規定，發行作業系統或 App 時用的授權若允許複製、再散布與修改，發行的人或組織就不算作業系統業者。規定 2027 年 1 月 1 日起適用，條文以加州的帳號持有人為對象，到 10 月 7 日為止加州以外的讀者不需要調整設定。

依 AB 1043 的條文，年齡訊號分成未滿 13 歲、13 到未滿 16 歲、16 到未滿 18 歲與 18 歲以上四級。App 下載並啟動時要向作業系統業者或 App 商店要求年齡訊號，收到訊號的開發者就視為知道使用者的年齡範圍。違反規定時由加州檢察總長提起民事訴訟，過失違規時每名受影響的兒童最高罰 2,500 美元，故意違規最高 7,500 美元。

AB 1856 把作業系統業者的義務限定在有帳號設定功能的作業系統，也要求 App 商店向作業系統要求年齡訊號、再提供給開發者。法律沒有要求的人，不得向作業系統業者或 App 商店索取年齡訊號。法案曾經把瀏覽器與網站納入，參議院 7 月的修正案刪掉了這部分。

開源豁免在 5 月 18 日的眾議院修正版加入，條文只有一個條件，發行時用的授權要允許接收者複製、再散布與修改。條文沒有出現 open source 或 Linux，沒有要求非商業，也沒有指定哪一種授權。豁免只寫在作業系統業者的定義，App 商店與開發者的定義沒有同樣的句子。

科羅拉多州 6 月簽署的 SB26-051 有類似的豁免，條件同樣是授權允許複製、再散布與修改。另外多一個條件，發行者不得用技術或契約限制使用者安裝修改過的版本。科羅拉多的規定 2028 年 7 月 1 日起適用。

## 導讀觀點 {#perspective}

年齡訊號的做法是由作業系統在帳號設定時詢問年齡，App 再透過作業系統提供的介面查詢，條文要求提供的是年齡範圍而非生日。條文沒有要求驗證填寫的年齡是否正確，也沒有指定介面的格式與資料存放的位置。許多 Linux 發行版用來管理系統與使用者帳號的元件 systemd 在 3 月合併了一項修改，在使用者紀錄裡加上只有管理者能修改的生日欄位，提交說明寫到加州、科羅拉多州與巴西的法律。各發行版是否採用，本文沒有查到。

支持的一方在乎家長能不能讓孩子的年齡跟著裝置走。委員會的法案分析引述提案的州眾議員，AB 1043 提供一條以隱私優先的年齡確認途徑，不會干涉 App 既有的帳號功能與家長控制。加州州長 2025 年簽署 AB 1043 時寫到，讓孩子當主要使用者的家長，可以設定裝置把孩子的年齡告訴 App 開發者。兒少團體 Common Sense Media 針對還包含瀏覽器與網站的版本寫信支持，信中寫到年齡訊號跟著孩子走，平台就不能因為孩子換了使用途徑而不套用保護措施。

Debian 與 Canonical 在豁免加入之前的公開說明，都還沒有定論。Debian 專案負責人 4 月寫到，還不清楚這類規定如何適用於不賣軟體、以高度分散方式提供軟體的志工專案。Ubuntu 的開發公司 Canonical 3 月在 Ubuntu 論壇的公告寫明，正在請律師檢視 AB 1043，還沒有具體計畫。

數位權利組織 EFF 3 月的文章寫到，AB 1043 的負擔特別落在開源軟體這類沒有大公司資源的開發者身上。EFF 7 月的文章寫到，瀏覽器與網站的擴大已經放棄，豁免也降低了對開源社群的威脅。EFF 因此撤回對 AB 1856 的反對，但仍認為 AB 1043 違憲。

條文規定作業系統只能送出必要的最少資訊，洛杉磯的公立學區洛杉磯聯合學區在支持信裡也把資料最少化列為 AB 1856 的內容。Linux 電腦製造商 System76 的文章寫到，填寫年齡的人可以說謊，孩子也可以在虛擬機器（在電腦裡模擬另一台電腦的軟體）裡建立成年帳號。System76 也寫到，如果這種做法成為標準，App 與網站在沒有收到訊號時會把使用者當成最低的年齡範圍。條文沒有規定沒有訊號時 App 要如何處理。

本文依條文推論，加州的使用者 2027 年起在授權不允許複製、再散布與修改的作業系統建立帳號時，可能會被要求填寫使用者的年齡。同樣依條文推論，符合豁免條件的 Linux 發行版不受這項義務約束，但條文沒有逐一認定哪些發行版符合。到 10 月 7 日為止，本文查不到 Apple、Google、Microsoft，以及 Debian 與 Canonical 在 AB 1856 通過後公布的做法。

之後讀到要求作業系統或 App 商店處理年齡的法律時，可以比較幾件事。年齡由誰填寫、有沒有驗證，離開裝置的是生日還是年齡範圍。開源與志工維護的系統在不在範圍內，豁免的條件是授權方式，還是另外要求不得限制使用者修改。年齡訊號的做法能不能讓家長在孩子的裝置上，用比上傳證件更少的資料達成保護。
