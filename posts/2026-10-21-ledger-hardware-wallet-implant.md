---
title: Ledger 硬體錢包的植入晶片事件
description: Ledger 10 月 15 日確認，犯罪集團在正品硬體錢包裡加裝設定時擷取復原詞的零件，再經東南亞的經銷商流入市面。到 10 月 13 日為止，Ledger 確認的盜領都跟授權經銷商 CryptoBilis 售出的裝置有關，其他管道的植入物回報還沒有證實。Ledger 的真品驗證偵測不到這類植入物，在 CryptoBilis 買過裝置且已經設定的人，Ledger 建議把資產轉到新裝置與新的復原詞。
date: 2026-10-21T00:05:00+08:00
slug: ledger-hardware-wallet-implant
categories:
  - security
sources:
  - title: Ledger’s Response to the Hardware Implant Attack
    url: https://www.ledger.com/blog-response-hardware-implant-attack
    publisher: Ledger
    date: 2026-10-15
  - title: Check hardware integrity
    url: https://support.ledger.com/article/4404382029329-zd
    publisher: Ledger Support
  - title: Best Practices To Securely Buy Your Ledger Signer
    url: https://www.ledger.com/academy/topics/ledgersolutions/best-practices-to-securely-buy-ledger-signer
    publisher: Ledger Academy
    date: 2026-03-06
  - title: Purchasing from an authorised reseller
    url: https://support.ledger.com/article/Purchasing-from-an-authorised-reseller
    publisher: Ledger Support
  - title: Find a Ledger Reseller around the world
    url: https://shop.ledger.com/pages/resellers
    publisher: Ledger
  - title: Why is Ledger Nano so Secure?
    url: https://www.ledger.com/academy/basic-basics/ledgers-bit-of-it/ledger-nano-security-made-easy
    publisher: Ledger Academy
  - title: Ledger says hardware implant in cryptocurrency wallets stole recovery phrases
    url: https://therecord.media/ledger-cryptocurrency-wallet-implant-theft
    publisher: The Record
    date: 2026-10-13
  - title: "Ledger Nano X: the spy implant."
    url: https://www.tibane.net/research/ledger-nano-x-implant
    publisher: Tibane Labs
  - title: The Ledger CryptoBilis hack took $102.0M from 335 wallets. One thief had all the keys
    url: https://bitquery.io/investigations/ledger-cryptobilis-hack
    publisher: Bitquery
    date: 2026-10-10
  - title: Who Is Planting Backdoors in Ledger Crypto Wallets?
    url: https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/
    publisher: Zero Day
    date: 2026-10-13
  - title: Ledger suspends retail sales in Germany as wallet implant probe continues
    url: https://crypto.news/ledger-suspends-retail-sales-in-germany-as-wallet-implant-probe-continues/
    publisher: crypto.news
    date: 2026-10-13
  - title: Ledger confirms hidden chip in crypto wallet amid $92M theft claims
    url: https://crypto.news/ledger-confirms-hidden-chip-in-crypto-wallet-amid-92m/
    publisher: crypto.news
    date: 2026-10-11
  - title: Ledger reveals how hidden chips stole wallet recovery keys
    url: https://crypto.news/ledger-reveals-how-hidden-chips-stole-recovery-phrases/
    publisher: crypto.news
    date: 2026-10-13
  - title: Ledger asks resellers to halt sales in Southeast Asia and Hong Kong
    url: https://cointelegraph.com/news/ledger-asks-resellers-to-halt-sales-in-southeast-asia-and-hong-kong
    publisher: Cointelegraph
    date: 2026-10-13
watch:
  - date: 2026-11-20
    note: Ledger 是否發布技術報告與產品層面的防護措施，已確認的範圍是否擴大到 CryptoBilis 以外的管道，東南亞與香港的經銷商是否恢復銷售
authors:
  - anoni-net
---

硬體錢包業者 Ledger 10 月 15 日在官方部落格確認，一個犯罪集團花了好幾個月買進正品的 Ledger 裝置。集團打開裝置裝上隱藏的零件，在使用者設定裝置時擷取復原詞（24 個英文單字，可以還原錢包裡的全部資產），再透過東南亞的經銷商流回市面。依鏈上分析公司 Bitquery 的時間線，集體盜領從 10 月 9 日開始。依 The Record 引述 Ledger 10 月 13 日的說明，已確認的盜領都跟 Ledger 授權的東南亞經銷商 CryptoBilis 售出的裝置有關。

依 Cointelegraph 引述，Ledger 10 月 13 日也表示還沒有證實其他管道買的裝置有盜領。Ledger 10 月 15 日的文章提到已請東南亞與香港的經銷商暫停銷售。官方的真品驗證（Genuine Check，連線 Ledger 伺服器確認安全晶片是原廠的檢查）偵測不到這類植入物。

依 Ledger 10 月 15 日的文章，晶片、作業系統與伺服器都沒有缺陷。Ledger 在文章裡把事件定性為裝置離開 Ledger 之後、在經銷管道發生的「localized distribution attack」（區域性的經銷攻擊），The Record 也引述 Ledger 認為受影響的裝置數量有限。依 The Record 引述 Ledger 10 月 13 日的說明，植入物讀取螢幕上顯示的資料，在設定時辨識出復原詞後用內建的 eSIM 經 LTE 行動網路傳出。

區塊鏈研發公司 Tibane Labs 拆解了兩台分別在日本拍賣網站與 Amazon Japan 賣家買到的 Nano X，頁面也寫明沒有測試過 CryptoBilis 的裝置。植入物是焊在主機板上、接到螢幕資料線的小型電腦，沒有去破解安全晶片（Secure Element，存放私鑰的晶片）。Tibane Labs 比較了三個版本，最新版本的專用天線印有零件編號與版本號，Tibane Labs 據此判斷植入物是量產品。

到 10 月 20 日為止，Ledger 沒有公布受影響的型號、批次、人數與金額。Bitquery 到 10 月 16 日統計出 335 個錢包、共 1.02 億美元被轉走，crypto.news 等早期報導的 9,290 萬美元是 Bitquery 較早版本的數字。Bitquery 的頁面提到鏈上紀錄指向同一個行為者持有所有被盜錢包的金鑰，但鏈上只看得到轉帳，看不出金鑰是從哪裡外洩的。

資安記者的電子報 Zero Day 10 月 13 日報導了 CryptoBilis 以外管道的植入物。一位不具名的日本研究者對 Zero Day 說，他累計向非授權網路賣家買了十台（最早在 3 月），全部都有植入物。同一篇報導引述一位德國買家在 X 的貼文，他在 Ledger 列為德國授權經銷商的 MediaMarkt 兩家門市，買到有植入物的 Nano X。到 10 月 20 日為止，Ledger 沒有證實這些說法。

The Record 引述 Ledger 10 月 13 日的說明，Ledger「also reviewing reports of implants in other signers and locations」。依 crypto.news 的報導，MediaMarkt 在 Ledger 同意下暫停銷售。Ledger 表示德國的案例沒有收到資金損失的回報，也沒有確認德國的回報跟其他案例是否相關。Ledger 10 月 15 日的文章提到曾派人到包括德國在內的市場買裝置拆開檢查，「Every unit examined was clean」，但沒有公布檢查的數量。

## 導讀觀點 {#perspective}

依 Ledger 的教學網站 Ledger Academy，私鑰存在安全晶片裡。復原詞由裝置在初始化時產生，也只在那時顯示一次。依檢查硬體完整性的說明頁，真品驗證確認的是原廠寫入安全晶片的密鑰，用來擋下仿冒品。同一頁也提醒，只要原廠的安全晶片完好，真品驗證就偵測不到植入物這類實體改裝。

The Record 與 Tibane Labs 描述的植入物不碰安全晶片，在復原詞顯示的那一刻從螢幕的資料線讀走復原詞。檢查硬體完整性的說明頁提到，Nano X 與 Nano S Plus 開機時由安全晶片檢查主控晶片的韌體，被改過會出現警告。說明頁另外列出的檢查方式是開殼對照官方的內部照片，確認沒有多出晶片。Tibane Labs 的頁面提到裝置本身不會察覺植入物，最新版本的植入物也塗成跟原廠電路板相同的顏色。

依 The Record 引述 Ledger 10 月 13 日的說明，在 CryptoBilis 買的裝置還沒設定的話不要設定，直接聯絡客服。已經設定的，要盡快把資產轉到新的裝置與新的復原詞，也不要在 CryptoBilis 買的裝置上輸入或還原任何復原詞。受害者要先聯絡 Ledger 與當地警方，再決定是否開殼或寄送裝置。

在其他管道買到來源不明的 Nano X、已經設定過的人，到 10 月 20 日為止 Ledger 沒有提出換復原詞的建議。Tibane Labs 的頁面則建議換掉在來源不明的 Nano X 上顯示過的復原詞，在可信的裝置上產生新的復原詞再把資產轉過去。頁面也提到，被改裝的螢幕顯示過的復原詞，就算裝置從沒連上網路也要當成已經外洩。依檢查硬體完整性的說明頁，懂硬體的人可以開殼對照，但開殼造成的損壞不在保固範圍。

還沒買或剛收到裝置的人，可以參照客服中心的購買說明頁。包裝看起來被打開或重新封裝、盒內已經附上寫好復原詞卡片的裝置都不要使用，直接聯絡客服。Ledger 建議向官方商店或授權經銷商購買，到 10 月 20 日為止經銷商頁列出台灣 6 家與香港 5 家，香港的項目沒有標示暫停銷售。這些說明頁到 10 月 20 日為止沒有正體中文版。

CryptoBilis 與 MediaMarkt 都在 Ledger 的授權名單上，Ledger Academy 的購買指南也寫到「no global supply chain is entirely immune」。依本文的推論，授權通路能降低風險，但不能保證裝置沒被改裝。

Ledger 在 10 月 15 日的文章裡要求經銷商不再把裝置放在貨架與展示櫃，改從庫存直接交給買家，並重申退貨的裝置一律不得轉售。同一篇文章預告之後會公布更完整的技術細節，也在開發產品層面的防護措施。這兩項的後續，以及 Ledger 是否擴大確認的範圍，是接下來可以留意的地方。
