---
title: Signal 協定一對一對話的機器檢查證明與美國大陪審團傳票
description: Google DeepMind 用 AI 代理證明 Signal 協定實作 libsignal 在一對一對話的加密性質，群組對話、伺服器與金鑰產生不在範圍內，到 11 月 14 日查不到其他研究者重現。Signal 公開 10 月一份大陪審團傳票，四個電話號碼只有一個有帳號，交出的是建立時間與最後連線日期。使用者不必調整設定。
date: 2026-11-18T00:00:00+08:00
slug: signal-verification-subpoena
categories:
  - encryption
sources:
  - title: "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth"
    url: https://deepmind.google/blog/introducing-alphaproof-code/
    publisher: Google DeepMind
    date: 2026-11-10
  - title: "AlphaProof Code: Verifying Signal’s Security at the Machine-Code Level"
    url: https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf
    publisher: Google DeepMind
    date: 2026-11-10
  - title: Grand jury subpoena for Signal user data in the United States District Court for the District of Columbia (again!)
    url: https://signal.org/bigbrother/district-of-columbia-2/
    publisher: Signal
    date: 2026-11-03
  - title: Grand jury subpoena for Signal user data in the United States District Court for the District of Columbia
    url: https://signal.org/bigbrother/district-of-columbia/
    publisher: Signal
    date: 2026-03-06
  - title: Government Requests
    url: https://signal.org/bigbrother/
    publisher: Signal
  - title: Google DeepMind just mathematically verified key parts of Signal
    url: https://arstechnica.com/ai/2026/11/signals-encryption-just-passed-an-ai-powered-mathematical-checkup/
    publisher: Ars Technica
    date: 2026-11-11
watch:
  - date: 2026-12-18
    note: DeepMind 對 libsignal 的證明有沒有其他研究者重現，以及群組對話、sealed sender 是否納入驗證
authors:
  - anoni-net
---

Google DeepMind 在 11 月 10 日公布，研究團隊用 AI 代理對 Signal 協定的參考實作 libsignal 寫出由電腦逐步檢查的數學證明。證明的範圍是一對一對話建立連線與更新金鑰的步驟，群組對話不在其中。Signal 在 11 月 3 日公開美國華盛頓特區聯邦檢察官辦公室 10 月發出的大陪審團傳票，四個電話號碼裡只有一個有帳號，Signal 交出的是帳號建立時間與最後連線日期。兩件事都跟全球的 Signal 使用者有關，使用者這一端不需要調整設定。

DeepMind 的部落格與技術論文列出，驗證對象是 libsignal v0.105.4。研究者用標準的 Rust 編譯器把它編成 AArch64（64 位元 ARM 架構）的 Linux 機器碼，證明對應到編譯出來的程式，底層的加密函式除外。證明分成兩個部分，一是建立對話時交換金鑰的 PQXDH，混合了傳統演算法與能抵擋未來量子電腦的演算法。二是每一則訊息換一把新金鑰的 Triple Ratchet。

論文列出的性質有前向保密（金鑰外洩時，之前的訊息仍無法解開）與交握的保密、身分驗證。另一項是入侵後復原（post-compromise security）。攻擊者偷到當下的金鑰之後，只要沒有在下一次金鑰更新時主動介入，之後的訊息就恢復保護。論文設定的攻擊者能控制網路與伺服器，也可能偷到長期金鑰或一方的整份狀態。

DeepMind 把這套工具稱為 AlphaProof Code。部落格提到，研究者與 AI 模型一起把 Signal 的安全目標寫成數學規格，每一條都由人類專家審過。證明則由 AI 代理用 Lean 撰寫，Lean 是定理證明器，每一步推論都由程式檢查。論文寫到作者沒有親手寫任何一行證明，AI 代理產生約 650 萬行 Lean 證明，證明工作由五人在四週內完成。

根據論文的統計，讀者需要信任的規格與定義約 18,000 行，另有約 8,000 行描述機器碼行為的規格。為了確認系統能否分辨有問題的程式，研究者把兩個已修正的 libsignal 舊漏洞放回一份隔離的程式碼，兩個版本都被證明不安全。Ars Technica 轉載 WIRED 的報導提到，驗證過的部分沒有找到新漏洞。

DeepMind 的部落格寫到，研究團隊第一次用 AI 把廣泛部署的加密協定驗證到實作程式碼這一層。部落格也宣稱，像 Signal 這樣廣泛部署的協定，實作在此之前沒有被任何方法形式化驗證過。規格與證明已經開源。部落格引述 Signal 技術長的話，自動化的定理證明讓團隊對程式碼能兌現隱私保證更有信心。

傳票的經過公開在 Signal 的「Government Requests」頁面，檢察官辦公室在 10 月 5 日發出傳票，期限三天。傳票查詢的是四個電話號碼在一段期間內的「all customer or subscriber account information」。附件舉出的項目包括但不限於帳號建立的日期與時間，以及最後連線的日期與時間。Signal 判斷傳票附上的標準指示是為銀行寫的，其中也列了支票與存款單的影像，頁面寫到 Signal 沒有以能連到帳號的方式收集這類資料。

美國公民自由聯盟（ACLU）在 10 月 6 日代表 Signal 回覆。四個號碼裡有三個沒有 Signal 帳號，Signal 交出剩下那個帳號的建立日期與時間，以及最後連上 Signal 伺服器的日期。Signal 只保留最後連線的日期、不保留時間，所以交不出時間。

這次的傳票沒有附不揭露令（禁止 Signal 對外透露收到傳票的法院命令），Signal 遮蔽電話號碼、期間與政府人員的身分之後公開了文件。同一個法院在 2025 年發出、Signal 在 3 月公開的前一份傳票查詢了 37 個帳號。其中 7 個不存在，24 個在那段期間沒有相關資料，其餘 6 個交出了資料。Signal 的頁面提到，執法單位的要求越來越集中在 Signal 實際收集的少量資料。

## 導讀觀點 {#perspective}

協定的證明針對訊息在傳送途中的保護，攻擊者控制網路與伺服器、甚至偷到部分金鑰時也包括在內，傳票的回應則顯示伺服器端保留了哪些資料。Signal 的頁面開頭列出訊息、通話、聯絡人、群組、個人資料名稱與頭像都經過端對端加密，Signal 無法交出從未取得的資料。

論文列出的限定條件中，一組定理採用符號模型，假設加密演算法完美無缺。符號模型不談實際位元組的保密程度，但在符號模型下證明了交握的保密能抵擋未來的量子電腦。另一組計算模型的定理只考慮傳統電腦的攻擊者。Triple Ratchet 裡負責後量子的部分叫 SPQR，證明只顯示整體不比舊的 Double Ratchet 弱，沒有證明 SPQR 額外帶來的後量子復原能力。

金鑰產生的程式沒有驗證，底層的加密函式也只用規格描述應有的行為，本身沒有證明。側通道攻擊（從耗電、時間等外部訊號推測金鑰）與記憶體裡的其他秘密不在範圍內。機器碼層級的定理只適用於雙方各用一台裝置的情境。雙方一開始就持有對方的身分金鑰，第一次聯繫時確認對方身分的那段流程沒有包含在內。

論文把群組對話、sealed sender（隱藏寄件者身分的機制）與伺服器端的協定列為之後的工作。描述機器碼行為的 8,000 行規格無法證明跟實際的硬體一致，論文寫到硬體與作業系統核心不是可以證明的對象。Ars Technica 轉載的 WIRED 報導也提到，整個 Signal App 並沒有被驗證。

論文的作者都來自 Google DeepMind 與 Google，致謝列出 Signal 的三位成員對方法提供意見。到 11 月 14 日為止，查不到論文經過同儕審查的紀錄，也查不到 DeepMind 以外的研究者重現的結果。

論文提到 WhatsApp、Meta Messenger 與 Google Messages 也使用 Signal 協定的變體。驗證的對象是 libsignal 的程式碼，不代表那些 App 的實作也通過同樣的證明。

Signal 2016 年第一份公開的傳票回應就寫到，伺服器端能交出的只有註冊的日期與時間和最後連線的日期。10 月交出的仍是同樣兩項。以電話號碼查詢的回覆，也讓檢察官知道四個號碼裡有三個沒有 Signal 帳號。

使用者不需要做任何設定。需要在 Signal 上處理敏感對話的人，判斷時可以參考證明的範圍只涵蓋一對一對話，論文沒有對群組對話下結論。依 10 月的回覆，伺服器端保留帳號建立時間與最後連線日期。之後可以留意 DeepMind 開源的證明有沒有其他研究者重現，以及驗證範圍有沒有擴及群組對話與 sealed sender，論文沒有寫出時程。
