---
title: Quad9 退出法國與法國的 DNS 封鎖命令
description: 公共 DNS 解析服務 Quad9 10 月 22 日宣布，11 月 24 日起不再為位於法國的使用者提供服務。依 Quad9 的公告，起因是法國法院依體育轉播的反盜版規定，要求它替法國使用者封鎖一批網域。台灣也有 DNS 層的停止解析程序，對象不包括使用者自行設定的公共解析服務。
date: 2026-10-27T00:00:00+08:00
slug: quad9-exit-france
categories:
  - censorship
regions:
  - FR
sources:
  - title: Farewell, France
    url: https://quad9.net/news/blog/au-revoir-france/
    publisher: Quad9
    date: 2026-10-22
  - title: Frequently Asked Questions
    url: https://quad9.net/support/faq/
    publisher: Quad9
  - title: Locations
    url: https://quad9.net/service/locations/
    publisher: Quad9
  - title: Quad9 Faces New DNS Censorship Legal Challenge in France from Canal+
    url: https://quad9.net/news/press/quad9-faces-new-dns-censorship-legal-challenge-in-france-from-canal/
    publisher: Quad9
    date: 2024-12-10
  - title: Quad9 Turns the Sony Case Around in Dresden
    url: https://quad9.net/news/blog/quad9-turns-the-sony-case-around-in-dresden/
    publisher: Quad9
    date: 2023-12-06
  - title: Quad9’s Opinion of the Recent Court Ruling in Leipzig
    url: https://quad9.net/news/press/quad9-s-opinion-of-the-recent-court-ruling-in-leipzig/
    publisher: Quad9
    date: 2023-03-06
  - title: Tribunal judiciaire de Paris, jugement du 13 mai 2026, RG n° 26/02207
    url: https://torrentfreak.com/images/tribunal-judiciaire_n°2602207_13_05_2026.pdf
    publisher: Tribunal judiciaire de Paris
    date: 2026-05-13
  - title: Blocking Behavior
    url: https://developers.google.com/speed/public-dns/blocking
    publisher: Google for Developers
  - title: 1.1.1.1 Public DNS Resolver
    url: https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/
    publisher: Cloudflare 1.1.1.1 docs
  - title: Innovating to address streaming abuse — and our latest transparency report
    url: https://blog.cloudflare.com/h1-2025-transparency-report/
    publisher: Cloudflare
    date: 2025-12-19
  - title: 著作權法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0070017
    publisher: 全國法規資料庫
  - title: "Mandated DNS Blocking: A Guide for Legal Professionals"
    url: https://www.internetsociety.org/resources/doc/2025/mandated-dns-blocking/
    publisher: Internet Society
    date: 2026-03-30
  - title: 運用 DNS RPZ 自律機制停止解析違法網站處理參考程序
    url: https://www-api.moda.gov.tw/File/Get/moda/zh-tw/Qv1tZuiNEVfsLIl
    publisher: 數位發展部
    date: 2025-01-09
  - title: CANAL+ reaches a new milestone in its fight against audiovisual piracy
    url: https://senalnews.com/en/digital/-canal-reaches-a-new-milestone-in-its-fight-against-audiovisual-piracy
    publisher: Señal News
  - title: DNS Resolver Quad9 Rejects French Piracy Blocks, Weighs Exit as beIN Seeks Up to €580K a Day
    url: https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/
    publisher: TorrentFreak
    date: 2026-10-05
  - title: Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France
    url: https://torrentfreak.com/?p=277758
    publisher: TorrentFreak
    date: 2026-04-01
  - title: OpenDNS Suspends Service in France Due to Canal+ Piracy Blocking Order
    url: https://torrentfreak.com/?p=253822
    publisher: TorrentFreak
    date: 2024-06-29
  - title: France Approves Automated, Real-Time Blocking of Pirate Sports Streams
    url: https://torrentfreak.com/france-approves-automated-real-time-blocking-of-pirate-sports-streams/
    publisher: TorrentFreak
    date: 2026-07-28
  - title: VPNs and Cloudflare Escape beIN’s €10,000-a-Day Piracy Blocking Penalties
    url: https://torrentfreak.com/vpns-and-cloudflare-escape-beins-e10000-a-day-piracy-blocking-penalties/
    publisher: TorrentFreak
    date: 2026-10-16
watch:
  - date: 2026-11-25
    note: Quad9 是否如期在 11 月 24 日退出法國、Paris 節點是否關閉、Quad9 的上訴結果，法國最高法院對其他公共解析服務上訴的裁決，以及法國新法是否涵蓋公共解析服務
authors:
  - anoni-net
---

Quad9 是瑞士非營利基金會營運的公共 DNS 解析服務，負責把網址裡的網域名稱翻成伺服器的位址，使用者可以自行設定、取代網路業者預設的解析服務。Quad9 10 月 22 日宣布，11 月 24 日起不再為位於法國的使用者提供服務。依 Quad9 的公告，體育轉播業者 beIN 提出請求後，法國法院 10 月 21 日的判決要求它替位於法國的使用者封鎖一批網域的解析。Quad9 表示不會封鎖這些網域，所以選擇退出法國，公告沒有說明會用什麼方式辨識位於法國的使用者。

這類命令的依據是法國運動法典第 L. 333-10 條，轉播權利人可以請求法院命令能協助的對象採取封鎖措施，阻止從法國境內連到盜播網站。巴黎司法法院 5 月 13 日判決 Google 與 Quad9 等被告在送達後 3 天內採取措施，封鎖持續到 WTA 網球賽季最後一場的 11 月 14 日。依判決適用的條文，之後由權利人提供新發現的盜播網站，法國視聽與數位通訊管理局（Arcom）查核後再通報被告。

5 月判決列出的網域依 Quad9 的說法後來追加到 58 個，TorrentFreak 引述 Quad9 表示沒有封鎖這些網域。TorrentFreak 也報導 beIN 回到法院，請求每日最高 58 萬歐元的罰款。beIN 對 TorrentFreak 表示不就進行中的程序評論。Quad9 的公告寫到 10 月的判決仍要求封鎖、罰款定為每日 1,000 歐元（到 11 月 14 日合計 2.4 萬歐元），並提到有一件上訴還在進行，Quad9 承受不了另外約 20 件類似訴訟累積的罰款。

依 Quad9 的公告，它的服務免費、不需要註冊，也沒有把使用者對應到所在國家的資料。Quad9 因此無法判斷判決適用於哪些人，若把網域加進全球的封鎖清單，又會把法國的判決套用到全世界的使用者。

在法國付費電視業者 Canal+ 提出的另一件案子，Quad9 2024 年 12 月的公告寫到，當時它對所有地區的使用者封鎖了清單上的網站。在德國的訴訟中，Quad9 曾依 IP 位址做地區封鎖，權利人用 VPN 連線之後法院認定措施不足並處以罰款。Quad9 後來在 2023 年 12 月的上訴審勝訴，德勒斯登高等法院認定解析服務不負侵權責任。

依 TorrentFreak，Quad9 對德國案與這次做法不同的解釋是德國的封鎖屬於訴訟期間的暫時措施、每個案子各自處理。Canal+ 案與這次的關係，報導沒有說明。

其他公共解析服務的做法也不同。依 TorrentFreak 引用的公告，Cisco 的 OpenDNS 從 2024 年 6 月 28 日起停止在法國與葡萄牙提供服務。到 10 月 23 日，Google Public DNS 的說明頁列出法國等五個會依命令封鎖的地區，被封鎖的網域會直接回覆拒絕查詢。Cloudflare 的文件提到 1.1.1.1 不封鎖也不過濾內容，部落格則提到回應封鎖命令時，有時改在內容傳遞網路（CDN）對網站做地理封鎖。

## 導讀觀點 {#perspective}

DNS 解析服務把網址裡的網域名稱翻成伺服器的 IP 位址，DNS 層的封鎖讓解析服務對特定網域不回覆位址，只影響透過這個解析服務的查詢。依 Internet Society 2026 年 3 月的報告，解析服務收到的只有網域名稱，沒有網頁的完整路徑。

封鎖能不能只限於法國，巴黎司法法院 5 月判決的理由是被告沒有證明限定在法國境內會有高成本或技術上不可行，技術方式由被告自行選擇。Quad9 的公告則提到它沒有使用者所在國家的資料，德國的經驗也顯示依 IP 位址判斷會被 VPN 繞過。Internet Society 的報告提到，業者要在毫秒內準確判斷使用者的位置並不容易，封鎖可能影響管轄範圍以外的使用者。Google Public DNS 的說明頁則列出它會依命令在法國等地區封鎖。

對於可以被繞過的封鎖還有沒有效，Quad9 的公告提到想看的人會改用其他較不可信的解析服務，封鎖也不會讓內容從伺服器上消失。巴黎司法法院的判決寫到，改用替代解析服務的人數多寡，不影響權利人請求封鎖的權利。依 TorrentFreak 的轉述，巴黎上訴法院 3 月在 Canal+ 對 Google、Cloudflare 與 Cisco 的案件中認定，過濾措施可以被繞過不代表措施無效。同一個判決也認為，替代解析服務讓使用者可以連到盜播網站，並繞過網路業者的封鎖。

責任與成本由誰負擔，Quad9 的公告認為讓私人企業決定網路上能看到什麼是危險的問題。Internet Society 報告的結論是 DNS 封鎖不適合用來執行公共政策，報告也提到小型與非營利業者可能負擔不起逐國封鎖的成本。依 Señal News 轉載的 Canal+ 新聞稿，上訴法院的判決符合 Canal+ 要求各類技術中介負起打擊盜播責任的策略。5 月的判決則提到，封鎖的成本依 Arcom 主持的協議由各方分攤。

台灣數位發展部 2025 年 1 月訂定的參考程序也有 DNS 層的停止解析，由台灣網路資訊中心與自願參與的網路接取業者修改特定網域的解析結果，要依法院判決、裁定或機關依法處分才能啟動。程序寫明停止解析不包括禁止使用者透過公共解析服務或 VPN 瀏覽的技術，說明欄也提到這在技術上做不到，舉的例子包括 OpenDNS、Cloudflare DNS 與 Quad9。啟動的依據例如詐欺犯罪與兒少性剝削的相關法律，到 10 月 7 日查證時，《著作權法》沒有授權封鎖網站的條文。

想確認自己是否在用 Quad9，可以打開 Quad9 提供的 `on.quad9.net` 檢查頁。11 月 24 日之後人在法國、裝置或路由器又固定設成 Quad9 的人，可能無法解析網址，公告沒有說明停止服務的方式。改用網路業者預設或其他解析服務的人，會失去 Quad9 阻擋惡意網域的保護。依 10 月 23 日的節點資料，Quad9 在台北、東京、新加坡、首爾等地的節點都在運作，公告沒有提到法國以外的使用者會有任何變動。

讀者可以從幾個問題比較兩方的標準。一是限定在一國境內封鎖的成本與可行性由誰證明，法院認為被告沒有證明，Quad9 與 Internet Society 則提出定位的限制。二是可以被繞過的封鎖算不算有效，法院認為可繞過不代表無效，Quad9 認為使用者會轉往其他服務。三是技術中介該不該分擔打擊盜播的責任，以及小型與非營利的解析服務能否負擔逐國封鎖。

之後可以留意 Quad9 上訴的結果，以及 11 月 24 日的退出是否如期。依 TorrentFreak 10 月 16 日的報導，數個 DNS 業者已就 3 月與 5 月的判決上訴到法國最高法院。TorrentFreak 7 月報導法國新通過的法律改由 Arcom 以自動化系統即時推送新增的封鎖目標，依當時的報導，正式實施要到 2026 年稍晚。新法是否涵蓋公共解析服務，本文沒有查證。
