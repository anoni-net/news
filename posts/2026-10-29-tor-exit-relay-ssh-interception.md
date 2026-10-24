---
title: Tor 出口中繼的 SSH 登入攔截事件
description: 10 月初，三百多個 Tor 出口中繼的設定遭到竄改，經過它們的 SSH 連線被導到攔截伺服器。10 月 1 日到 5 日之間經由 Tor 用密碼登入 SSH、又接受了陌生或改變過的主機金鑰的人，要把那組密碼當成已經外洩。這些中繼在台北時間 10 月 6 日 01:00 前已經從 Tor 的可用中繼清單消失，依發現者的文章，加密的網頁流量照常轉送。
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
watch:
  - date: 2026-11-25
    note: Tor Project 是否公布其他 58 位營運者的入侵途徑，以及是否發現新的受影響中繼
authors:
  - anoni-net
---

10 月初，三百多個 Tor 出口中繼（Tor 連線的最後一站，負責把流量送到目的地）的設定遭到竄改，經過它們的 SSH 連線（遠端登入、管理伺服器用的協定）被導到攔截伺服器。使用者接受了假的主機金鑰（伺服器用來證明身分的金鑰）、輸入密碼之後，密碼就被取走。受影響的是經由 Tor 用 SSH 登入伺服器的人，經由 Tor 用未加密連線收信的人也可能受影響。這些中繼在台北時間 10 月 6 日 01:00 前已經從 Tor 的可用中繼清單消失，依發現者的文章，加密的網頁流量照常轉送。

發現者是一位經由 Tor 連 SSH 的使用者，10 月 2 日看到主機金鑰改變的警告。他接著掃描全部約 3,000 個出口，找到 333 個出示假的主機金鑰或把連線轉往攔截伺服器的出口，當晚通報 Tor Project。其中十多個本身出示假的主機金鑰，其餘三百多個把連線轉到同樣的 12 台攔截伺服器。

依發現者的文章，使用者繼續登入之後，攔截伺服器取走密碼並把連線轉給真正的伺服器。使用者輸入的每個指令都會經過攔截伺服器。

攔截伺服器接著用同一組密碼另外登入使用者原本要連的伺服器，試圖安裝名為 Ebury 的後門（讓攻擊者之後能再次登入的程式），發現者沒有看到完整的安裝。Ebury 植入伺服器的 SSH 軟體 OpenSSH，會記下登入時輸入的帳號密碼。ESET 2024 年的報告統計，2009 年起累計約有 40 萬台伺服器受害。

Tor 負責監控網路狀況的 Network Health 團隊在 UTC 10 月 5 日 17:50（台北時間 10 月 6 日 01:50）發布公告，提到攻擊者取得 Linux 主機的權限之後修改 Tor 的設定檔，連原本不是出口的中繼也被改成出口。Tor 的目錄伺服器（定期公布可用中繼清單的一組伺服器，這份清單稱為共識）從 UTC 10 月 4 日晚上（台北時間 10 月 5 日清晨）起，陸續把受影響的中繼標記成不能當出口。

一位中繼營運者比對公開的目錄資料，找到 59 位營運者的 377 個中繼在 10 月 1 日到 4 日之間套用了同一組出口政策（中繼允許連往哪些連接埠的設定）。分析者提醒，這只代表設定吻合，不能證明主機都被入侵或每一個都攔截 SSH。高峰時這些中繼占可用出口權重（目錄伺服器給每個出口的流量比重）的約 7%。Tor 用戶端大致依權重挑選出口，本文據此推算，經由 Tor 的連線約有 7% 的機率選到它們。

其中 277 個屬於同一個中繼家族（同一位營運者登記在一起的一組中繼）。家族營運者的事後檢討寫到，他們登入伺服器、取得管理權限（sudo）與備份都用同一組密碼，管理伺服器也允許用密碼登入。攻擊者最初從哪裡取得這組密碼，還不清楚。家族營運者檢查的兩台伺服器裝了 Ebury，其他受影響的主機是否也有，從公開資料無法判斷。

## 導讀觀點 {#perspective}

Tor 只在自己的網路裡加密，出口中繼可以讀取送往目的地的流量。HTTPS 與 SSH 自帶加密與身分驗證，未加密的收信協定沒有。

SSH 用主機金鑰確認連上的是真正的伺服器。依 OpenSSH 的說明文件，主機金鑰改變時 `ssh` 程式會顯示警告並停用密碼登入，預設設定下直接拒絕連線。使用者要自行刪除舊的金鑰紀錄，才會走到輸入密碼這一步。第一次連線的伺服器沒有舊紀錄可以比對，使用者只會看到一般的確認提示，按下同意就接受了攔截伺服器的金鑰。

The Hacker News 依 SSH 的協定規格推論，只有用密碼登入的人會被取走帳密。用金鑰登入（以自己電腦上的私鑰證明身分、不把密碼送給伺服器的登入方式）時，每次登入的證明只對這一次連線有效，攔截者無法用它登入真正的伺服器。報導也提到，攔截者仍可以接受金鑰登入、顯示假的命令列畫面。用金鑰登入的人如果在假畫面輸入了 sudo 之類的管理密碼，本文推論那組密碼一樣可能外洩。

The Hacker News 的建議是，10 月 1 日到 5 日之間經由 Tor 用密碼登入、又接受了陌生或改變過的主機金鑰的人，要把那組密碼當成已經外洩。家族營運者的伺服器在 9 月 30 日就出現用途不明的隱藏程式，營運者無法確定它們是否也在攔截 SSH，所以 10 月 1 日之前登入的人也不能排除。

家族營運者寫到，Ebury 會記下在受感染伺服器上輸入的密碼。檢查時要用金鑰登入，或從救援系統（不經過原本系統開機的維修環境）開機。

外洩的那組密碼，其他用到它的服務可以先換，被登入的伺服器等檢查完再換。ESET 公開的偵測腳本要在伺服器的命令列執行，10 月 9 日合併的更新才能偵測到這次的 Ebury，沒找到也不代表伺服器是乾淨的。

之後經由 Tor 管理伺服器時，發現者建議改用金鑰登入。第一次連線時，可以先向管理者索取主機金鑰的指紋（金鑰的一串識別碼，連線時畫面上會顯示）來核對。

另一個做法是把 SSH 設成洋蔥服務（只能經由 Tor 連上、連線不離開 Tor 網路的服務），連線不經過出口中繼，就不會被出口中繼攔截。代價是金鑰登入要保管好私鑰，換電腦或遺失時要重新設定。洋蔥服務則要在伺服器上執行 tor，設定比直接開放 SSH 多一步。

依分析者的整理，多數受影響的中繼關掉加密的收信連接埠、只放行未加密的，經由它們轉送的收信流量因此全是明文。沒有來源確認郵件內容實際被讀取，經由 Tor 收信的人仍要確認郵件軟體用的是加密連線。

Tor 的中繼由各地志工架設，任何人都能加入，被入侵或惡意的中繼需仰賴 Network Health 團隊的掃描與使用者回報才能找出。發現者 10 月 2 日通報，到 UTC 10 月 5 日 17:00 受影響的中繼全部離開共識，花了約三天。

Tor 用戶端預設挑選出口時不考慮使用者的所在位置，所以中繼在哪個國家，跟讀者是否受影響無關。社群用地理位置資料比對那 377 個中繼，台灣、日本、南韓、香港都沒有，新加坡有 24 個且都屬於同一個家族（地理位置資料可能有誤差）。

只用 Tor Browser 瀏覽 HTTPS 網站、沒有經由 Tor 用 SSH 或收信的人，不需要做任何設定。到 10 月 24 日為止，我們在 Tor Project 的部落格、狀態頁與郵件列表上沒有找到其他 58 位營運者的中繼為何套用同一組政策的說明。ESET 的 Ebury 研究者在 Tor 中繼營運者的郵件列表上寫到，很可能還有其他被入侵的中繼沒被發現。可以在 11 月 25 日前後留意 Tor Project 是否公布這批中繼的入侵途徑，以及是否發現新的受影響中繼。
