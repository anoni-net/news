---
title: Tor Project 與 Mullvad 合作關係的決定與爭議
description: VPN 服務商 Mullvad 一位共同創辦人的政治捐款引發爭議後，Tor Project 10 月 9 日說明不終止合作，但暫停共同品牌宣傳並修改 Mullvad Browser 的描述。兩款瀏覽器沒有停止維護的公告，聲明下的留言看法分歧。
date: 2026-10-14T00:00:00+08:00
slug: tor-mullvad-relationship
categories:
  - civil-society
sources:
  - title: A statement on the Tor Project's relationship with Mullvad
    url: https://blog.torproject.org/on-tor-relationship-with-mullvad/
    publisher: Tor Project
    date: 2026-10-09
  - title: A statement on the Tor Project's relationship with Mullvad
    url: https://forum.torproject.org/t/a-statement-on-the-tor-projects-relationship-with-mullvad/22247
    publisher: Tor Project Forum
    date: 2026-10-09
  - title: Donation controversy
    url: https://mullvad.net/en/blog/donation-controversy
    publisher: Mullvad
    date: 2026-07-20
  - title: Techprofil ger miljoner till Örebropartiet
    url: https://www.flamman.se/techprofil-ger-miljoner-till-orebropartiet/
    publisher: Flamman
    date: 2026-06-26
  - title: We've Teamed Up With Mullvad VPN to Launch the Mullvad Browser
    url: https://blog.torproject.org/releasing-mullvad-browser/
    publisher: Tor Project
    date: 2023-04-03
  - title: MULLVAD VPN AND THE TOR PROJECT TEAM UP TO RELEASE THE MULLVAD BROWSER.
    url: https://mullvad.net/en/blog/mullvad-vpn-and-the-tor-project-team-up-to-release-the-mullvad-browser
    publisher: Mullvad
    date: 2023-04-03
  - title: What is Mullvad Browser?
    url: https://support.torproject.org/mullvad-browser/faqs/what-is-mullvad-browser/
    publisher: Tor Project
  - title: Releases · mullvad/mullvad-browser
    url: https://github.com/mullvad/mullvad-browser/releases
    publisher: GitHub
  - title: 2023-7-1 thru 2024-6-30 IRS Form 990
    url: https://www.torproject.org/static/findoc/2023-2024-TheTorProject-PublicDisclosureForm990.pdf
    publisher: Tor Project
  - title: Snowflake Daily Operations 2026 July update, and a statement about Mullvad donations
    url: https://forum.torproject.org/t/snowflake-daily-operations-2026-july-update-and-a-statement-about-mullvad-donations/21954
    publisher: Tor Project Forum
    date: 2026-08-05
  - title: A statement on the Tor Project's relationship with Mullvad
    url: https://news.ycombinator.com/item?id=50022266
    publisher: Hacker News
    date: 2026-10-09
watch:
  - date: 2026-12-15
    note: Tor Project 暫停與 Mullvad 共同品牌宣傳是否有期限或恢復，是否公開 Mullvad 近年的資金比例
  - date: 2027-03-31
    note: Tor Project 是否公布 2024 年 7 月之後會計年度的財務報告，Mullvad 的資金占多少
authors:
  - anoni-net
---

VPN 服務商 Mullvad 一位共同創辦人的政治捐款引發爭議之後，Tor Project 10 月 9 日發布聲明，決定不終止跟 Mullvad 的關係。聲明提到要設下清楚的界線，技術合作照雙方範圍很窄的協議繼續，主動的共同品牌宣傳暫停。Tor 自己的管道也修改了 Mullvad Browser 的描述。到 10 月 12 日為止，Tor Browser 與 Mullvad Browser 最近的穩定版都是 9 月底發布的 15.0.24，沒有停止維護的公告。

爭議源自瑞典媒體 Flamman 6 月 26 日的報導，一位共同創辦人 2025 年以個人名義捐出 500 萬瑞典克朗給瑞典的政黨 Örebropartiet，占該黨 2025 年收入的 72%。Flamman 稱該黨為民粹政黨，並形容它主張大規模遣返移民。Mullvad 7 月 20 日在部落格寫這是個人捐款、公司沒有參與，對捐款「不認可也不譴責」，也寫這很可能是個壞主意。

根據 Tor 的聲明，這項合作改善了 Tor Browser 程式碼的結構、可維護性與可稽核性，也讓更多人多一個免費的開源隱私工具。依 Tor 公開的 2023 年 7 月到 2024 年 6 月美國國稅局（IRS）990 表，Mullvad 提供約 140 萬美元，是企業來源中最大的一筆。聲明本身沒有寫金額，到 10 月 12 日為止，Tor 財務報告頁最新只到 2024 年 6 月的會計年度。

## 導讀觀點 {#perspective}

Mullvad Browser 是 2023 年 4 月推出的瀏覽器，由 Mullvad 發布，Tor 的說法是「不走 Tor 網路的 Tor Browser」。兩者的版本號與發布日期同步，Mullvad Browser 也由 Tor Browser 的開發者簽章，本文的推論是兩者大部分程式碼共用。差別在連線方式，Tor Browser 走 Tor 網路、可以連 onion 服務並內建規避審查的功能，Mullvad Browser 則搭配使用者自己信任的 VPN 或直接連線。

依 Tor 的聲明，它捍衛言論自由，但強烈反對威脅其他人權與自由的言論。聲明也提到，隱私工作的資源嚴重不足，有時需要做困難的妥協。Mullvad 的部落格則寫公司主張言論自由、資訊自由與隱私權，並把創辦人個人的看法跟公司的使命分開。營運一座 Snowflake 橋接器（讓網路受封鎖的人連上 Tor 的入口之一）的志工小組（自稱不屬於 Tor Project）8 月 5 日宣布拒收 Mullvad 的捐款，理由是捐款對象是他們所稱「危險的民粹政黨」，即使所需年度開銷因此只剩約四分之一有著落。

Tor 部落格這篇聲明底下的論壇留言，到 10 月 12 日共 8 則，支持維持合作與批評或譴責的各 3 則（留言是自願發言的少數，不代表社群整體）。支持的留言寫到 Mullvad 的使命跟 Tor 一致，失去 Mullvad Browser 會傷害使用者。

批評的一方有留言直接表示譴責。一則自稱前 Tor Browser 開發者的留言寫，Mullvad 沒有開發者參與、只提供資金，「技術合作」的說法有誤導之嫌。Tor 的支援頁寫這款瀏覽器由 Tor Project 與 Mullvad 合作開發，Mullvad 的公告寫由 Tor 的工程師開發，兩邊都沒有寫 Mullvad 是否派人參與。

Tor 的聲明提到，決定之前做過社群、員工與董事會的討論、員工調查與財務分析，但沒有公開調查結果與財務數字。論壇有一則留言要求公開 Mullvad 占預算的比例，也問是否所有捐款都經過同樣的審查。到 10 月 12 日為止，Tor Project 人員沒有在留言中回應，Mullvad 的部落格也沒有針對這份聲明的新文章。

Hacker News 上同一篇聲明的討論串到 10 月 12 日有 353 則留言，看得到內容的頂層留言有 22 則（另有 11 則被標記而看不到內容），這些留言同樣不代表社群整體。表示理解或支持維持合作的頂層留言有 4 則，其中兩則的理由是這類工具的資金難得，斷絕關係不見得比較有利於使命。有 5 則反對聲明劃出的言論界線，例如主張言論自由本質上是絕對的，回覆裡的反駁則認為 Tor 只是不想跟這些言論連在一起。另有 3 則批評聲明沒有交代捐款與政黨的細節或語氣像公關稿，也有頂層留言擔心 Tor 依賴 Mullvad 的資金之後，獨立性會受影響。

用 Tor Browser 或 Mullvad Browser 的讀者，到 10 月 12 日為止不必做任何設定。這次的爭議在資金與組織的立場，兩款瀏覽器的隱私保護機制沒有因此改變，這是本文依聲明「技術合作照協議繼續」的推論。介意資金來源的讀者可以留意，兩款瀏覽器都由 Tor Project 的工程師維護，改用另一款不會改變 Tor 與 Mullvad 之間的資金關係。之後可以留意共同品牌宣傳的暫停是否有期限、Tor 是否公開 Mullvad 近年的資金比例，以及下一份財務報告。

比較這件事時可以問，隱私工具的開發組織接受企業資金時用什麼標準審查捐款者、標準是否一體適用，公司與創辦人個人的政治捐款又能否分開看待。暫停宣傳與修改描述，是否足以讓使用者分辨合作的範圍與組織的立場。斷絕合作之後，一款仍在維護的開源瀏覽器能否找到其他資金繼續發布。
