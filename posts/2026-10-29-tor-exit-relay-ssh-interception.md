---
title: Tor 出口中繼遭入侵、攔截 SSH 登入的事件
description: 2026 年 10 月初，三百多個 Tor 出口中繼的設定被人改掉，經過它們的 SSH 連線被導到攔截伺服器。使用者接受了假的主機金鑰、輸入密碼時，密碼就會被取走。這些中繼在台北時間 10 月 6 日凌晨之後已經不再列在 Tor 網路的共識裡，加密的網頁流量照常轉送。依 The Hacker News 的整理，10 月 1 日到 5 日之間經由 Tor 用密碼登入 SSH、又接受了陌生或改變過的主機金鑰的人，要把那組密碼當成已經外洩。
date: 2026-10-29T00:00:00+08:00
slug: tor-exit-relay-ssh-interception
categories:
  - security
sources:
  - title: Security incident affecting some relay operators
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/WOHPLKCSHYXFTBRZXDENDKJZMBMPLMG5/
    publisher: Tor Project
    date: 2026-10-05
  - title: "Ebury 1.8.3 on two Quetzalcoatl relay servers: timeline, lessons, open questions"
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/QHRD6YOX6RZRDR7NCHNDO7GLCEA6VFM6/
    publisher: tor-relays
    date: 2026-10-07
  - title: "Re: Ebury 1.8.3 on two Quetzalcoatl relay servers: timeline, lessons, open questions"
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/message/Z2B6XYKJZBBQADU77MSNL6FJP7MHZHIV/
    publisher: tor-relays
    date: 2026-10-09
  - title: How I got over 300 Tor exit nodes removed
    url: https://kaba.cx/posts/20261020_Tor/
    publisher: kaba.cx
    date: 2026-10-20
  - title: Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections
    url: https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
    publisher: The Hacker News
    date: 2026-10-21
  - title: "Ebury is alive but unseen: 400k Linux servers compromised for cryptotheft and financial gain"
    url: https://www.welivesecurity.com/en/eset-research/ebury-alive-unseen-400k-linux-servers-compromised-cryptotheft-financial-gain/
    publisher: ESET
    date: 2024-05-14
  - title: ssh(1) - OpenBSD manual pages
    url: https://man.openbsd.org/ssh
    publisher: OpenBSD
  - title: ssh_config(5) - OpenBSD manual pages
    url: https://man.openbsd.org/ssh_config
    publisher: OpenBSD
  - title: 新加坡的 Tor 中繼節點
    url: https://anoni.net/projects/pulse/sg/
    publisher: anoni.net
watch:
  - date: 2026-11-25
    note: Tor Project 是否公布其他 58 位營運者的入侵途徑，以及是否發現新的受影響中繼
authors:
  - anoni-net
---

2026 年 10 月初，三百多個 Tor 出口中繼的設定被人改掉。出口中繼是 Tor 連線的最後一站，負責把流量送到目的地。經過這些中繼的 SSH 連線（遠端登入、管理伺服器用的協定）被導到攔截伺服器，使用者接受了假的主機金鑰、輸入密碼之後，密碼就被取走。主機金鑰是伺服器用來證明自己身分的金鑰。

受影響的是經由 Tor 用 SSH 登入伺服器的人，經由 Tor 用未加密的連線收信的人也可能受影響。依 kaba 的文章，加密的網頁流量照常轉送，他推測攻擊者想收集的是未加密的資料。

依一份目錄資料的分析，Tor 的目錄伺服器從 UTC 10 月 4 日 18:00 起陸續投票，把受影響的中繼標記成不能當出口。21:00（台北時間 10 月 5 日 05:00）起，共識帶有這個標記。UTC 10 月 5 日 17:00（台北時間 10 月 6 日 01:00）起，用了攻擊者設定的中繼已經不再列在共識裡，用戶端不會選到它們。

10 月 20 日發表掃描經過的是一位以 kaba 為名的使用者，他在 10 月 2 日經由 Tor 連 SSH 時看到主機金鑰改變的警告。依他的文章，他接著掃描了全部約 3,000 個出口，找到 333 個有問題。其中約十來個自己出示假的主機金鑰，其餘三百多個把 SSH 連線轉到同樣的 12 台攔截伺服器。他當晚就通報了 Tor Project。

Tor 負責監控網路狀況的 Network Health 團隊在 10 月 5 日發布公告，對象是中繼的營運者。依公告，攻擊者取得 Linux 主機的權限之後修改 Tor 的設定檔，連原本不是出口的中繼也被改成出口。團隊也在調查主機被入侵的途徑。

依 kaba 的文章，使用者不理會警告、繼續登入之後，攔截伺服器會取走密碼。它再把連線轉給真正的伺服器，使用者輸入的每個指令都會經過攔截伺服器。

攔截伺服器接著用同一組密碼另外登入那台伺服器，安裝名為 Ebury 的後門。kaba 的蜜罐只看到安裝程式的開頭，對方就斷線了。Ebury 藏在 OpenSSH 裡竊取登入的帳密，依 ESET 2024 年的報告，從 2009 年起約有 40 萬台伺服器被它入侵。

另一組數字來自一位中繼營運者用公開目錄資料做的分析。59 位營運者的 377 個中繼在 10 月 1 日到 4 日之間發布了攻擊者的出口政策，也就是中繼允許連往哪些連接埠的設定。其中 351 個在 UTC 10 月 4 日 01:00 占可用出口權重的 7.46%。用戶端大致依權重挑選出口，本文據此推算，選到它們的機會約是這個比例。

分析者註明這只代表設定吻合、不能證明主機都被入侵，跟 kaba 主動掃描得到的 333 是不同的算法。377 個裡有 277 個屬於同一個中繼家族。家族的營運者在事後檢討裡寫，SSH 登入、sudo 與備份共用同一組密碼，管理伺服器又開著密碼登入。攻擊者最初從哪裡取得這組密碼，還不知道。

家族檢查的兩台伺服器裝了 Ebury，其他受影響的主機有沒有，公開資料看不出來。另外 58 位營運者的中繼為什麼出現同樣的設定、是否被入侵，到 10 月 24 日為止還不清楚，受害的使用者有多少也沒有數字。

## 導讀觀點 {#perspective}

Tor 只在自己的網路裡加密，出口中繼看得到送往目的地的流量。連線有沒有加密、能不能確認對方的身分，要靠使用的協定。

SSH 用主機金鑰確認連上的是真正的伺服器。依 OpenSSH 的說明文件，主機金鑰改變時 ssh 會警告並停用密碼登入，預設設定下直接拒絕連線。使用者要自己刪掉舊的金鑰紀錄或改掉設定，才連得上。第一次連線的伺服器沒有舊紀錄可以比對，使用者只會看到一般的確認提示，按下同意就接受了攔截伺服器的金鑰。

The Hacker News 的報導依 SSH 的協定規格 RFC 4252 推論，只有用密碼登入的人會被取走帳密。用金鑰登入時，簽章綁定這一次連線，攔截者無法拿去登入真正的伺服器。同一篇報導也寫到，攔截者仍可以接受金鑰登入、顯示一個假的命令列畫面。本文的推論是，用金鑰登入的人如果在那個畫面輸入了 sudo 之類的密碼，那組密碼一樣可能外洩。

報導據此寫出的範圍，是 10 月 1 日到 5 日之間經由 Tor 用密碼登入、又接受了陌生或改變過的主機金鑰的人，報導沒有標時區。Tor 的公告與發現者的文章都沒有這樣界定。家族的事後檢討寫到，他們的伺服器在 9 月 30 日就出現用途不明的隱藏程序，所以起點只能當參考。

報導建議符合條件的人把那組密碼當成已經外洩，被登入的那台伺服器也可能已經被裝上 Ebury。家族營運者提醒，不要在可能被入侵的伺服器上輸入密碼，因為 Ebury 會記下來。檢查要先用金鑰登入或從救援系統開機。

本文的建議是，其他用過同一組密碼的服務可以先換，被登入的那台等檢查完再換。ESET 公開了 Ebury 的偵測腳本，10 月 9 日之後的版本才能偵測到這次的 Ebury。腳本本身也註明，沒找到不代表系統是乾淨的。

之後經由 Tor 管理伺服器時，本文建議改用金鑰登入，第一次連線時向管理者確認主機金鑰的指紋。也可以把 SSH 設成洋蔥服務（只能經由 Tor 連上、連線不離開 Tor 網路的服務），洋蔥服務的連線不經過出口中繼，出口的攔截也就影響不到。依分析者的整理，多數受影響中繼的出口政策關掉了加密收信的連接埠，明文的連接埠維持開放。經由 Tor 收信的人要確認郵件軟體用的是加密連線。

Tor 的中繼由各地志工架設，任何人都能加入，偵測靠 Network Health 團隊的掃描與使用者回報。這次在 kaba 通報之後約兩天出現標記，用了攻擊者設定的中繼全部不再列在共識裡，又花了將近一天。

anoni.net 社群用 Tor 套件附的 IP 地理位置資料庫，比對分析者公開的 377 個中繼。台灣、日本、南韓、香港都沒有受影響的中繼，新加坡有 24 個，全部屬於同一個家族。地理位置資料庫可能有誤差。

社群的 Tor 中繼節點觀測也記錄到，新加坡有出口旗標（Exit）的中繼從 UTC 10 月 3 日的 34 個降到 10 月 4 日的 9 個，本文推測跟這次的標記有關。用戶端挑選出口時不看使用者在哪裡，所以中繼在哪個國家，跟讀者有沒有受影響無關。

到 10 月 24 日為止，Tor Project 還沒有公布其他營運者的中繼如何被改。Ebury 的研究者在 tor-relays 郵件列表上寫，很可能還有其他被入侵的 Tor 中繼沒被發現。接下來可以留意 Network Health 團隊的調查結果，以及是否發現新的受影響中繼。
