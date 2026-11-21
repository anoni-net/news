---
title: 用大型語言模型搜尋審查規避策略的 CircumVolve 研究
description: 研究者讓大型語言模型反覆改寫規避程式，在中國、伊朗、巴基斯坦、哈薩克的網路找到 47 個繞過審查設備的策略，同一個策略不一定在每個國家都有效。策略要經過工具開發者整合才會到使用者手上，一般讀者不需要做任何設定。
date: 2026-11-27T00:00:00+08:00
slug: circumvolve
categories:
  - censorship
watch:
  - date: 2026-12-27
    note: 是否有規避工具宣布整合 CircumVolve 找到的策略，程式碼庫是否補上授權檔
sources:
  - title: "CircumVolve: Automated Discovery of Censorship Evasion Strategies Using Large Language Models"
    url: https://gfw.report/publications/ccs26/en/
    publisher: GFW Report
    date: 2026-11-16
  - title: alizohaib/ccs26-circumvolve
    url: https://github.com/alizohaib/ccs26-circumvolve
    publisher: GitHub
  - title: Kkevsterrr/geneva
    url: https://github.com/Kkevsterrr/geneva
    publisher: GitHub
  - title: "obfsgen: a generative approach towards tunnel obfuscation"
    url: https://github.com/net4people/bbs/issues/684
    publisher: GitHub
    date: 2026-11-18
  - title: goose-lab-cuhk/obfsgen
    url: https://github.com/goose-lab-cuhk/obfsgen
    publisher: GitHub
authors:
  - anoni-net
---

審查方換了新的封鎖方式之後，繞過的方法多半要靠研究者人工找出來。研究者要分析封鎖事件、猜測觸發的條件、手寫規避方式再實際測試，論文寫到這個循環往往要數週到數月。GFW Report 網站 11 月 16 日公開一篇資安研討會 ACM CCS 2026 的論文 CircumVolve，研究者讓大型語言模型（LLM）反覆改寫規避程式，在模擬環境與中國、伊朗、巴基斯坦、哈薩克的網路實際測試。論文把它定位成給規避研究者與工具開發者的發現工具，一般讀者不需要做任何設定。

規避策略指改動封包或協定的寫法，讓審查設備無法比對出連線要去被封鎖的網站，伺服器仍能正常回應。研究者把每個策略寫成可執行的 Python 程式，交給 LLM 反覆產生變體，再留下測試表現好的版本繼續修改。整套流程沿用開源的程式演化框架 OpenEvolve，LLM 每一回合依分數、轉成文字的封包與錯誤訊息提出修改。策略要同時躲過審查、從目的伺服器取得正確回應才會得到高分，避免 LLM 用刪掉被封鎖網域這類方式取巧。

既有的自動化工具也能搜尋規避策略，例如 2019 年發表的 Geneva。依論文的描述，這類工具用固定的規則組合封包操作，改不了 TLS（HTTPS 使用的加密協定）與 QUIC（新一代的網頁傳輸協定）這類加密協定裡的內容。LLM 寫出的是一般的 Python 程式，可以在程式裡處理加密，改動加密協定的內容。

在真實的網路上，研究者只能知道繞過成功或失敗。模擬環境改用開源的審查模擬軟體 OpenGFW 扮演審查設備，研究者可以追查策略為什麼有效。策略也送到受審查地區、研究者自己控制的資料中心 VPS（租用的虛擬主機）實測，測試涵蓋 DNS（把網域名稱轉成 IP 位址的查詢）、TCP/IP、HTTP、TLS 與 QUIC 五種協定。每種協定依各國實際的封鎖方式，在其中兩到三國測試，伊朗的實驗都在 2026 年 2 月 28 日全國斷網之前完成。

研究者用 CircumVolve 在五種協定共找到 47 個不同的策略，其中 27 個就作者所知沒有出現在先前的研究。每個國家受測的每種協定都至少找到一種繞過方式，同一個策略則不一定在每個國家都有效。依論文，有找到繞過方式的執行在第一次繞過之前，LLM API 的費用中位數不到 1 美元。論文自述的限制包括全部實驗只用 GPT-5.1 一個模型，QUIC 與 TLS 也只改寫連線的第一個封包。

## 導讀觀點 {#perspective}

論文在倫理段提出的看法是，審查方要正確解析所有協定，規避的一方只要找到一個被忽略的邊角情況就可能繞過。研究者用 CircumVolve 把尋找邊角情況的大量嘗試交給 LLM，LLM 可以依審查設備的反應調整下一輪的修改。論文認為部分 DNS 策略單靠隨機變化輸入的模糊測試（fuzzing）可能很難找到。

系統要靠熟悉審查的研究者定義評估標準、設計提示，論文把自動部署列為未來的工作。想自行執行的研究者要準備自己的 VPS 與 LLM API 金鑰，論文也提醒測試會從測試點送出畸形的封包，測試活動本身可能被審查方辨識出來。

論文寫到已公開程式碼、提示與成功的策略。到 11 月 22 日，CircumVolve 程式碼庫的根目錄沒有授權檔，只有內含的 `openevolve/` 目錄採 Apache-2.0。別的專案要直接沿用其餘的程式碼，條件並不明確。

另一個研究團隊 11 月 18 日在 GitHub 的 net4people 討論區介紹的 obfsgen 同樣用上生成式模型，改的是加密通道流量的封包大小與時序，讓它接近一般的流量。obfsgen 採 MIT 授權，README 寫明還不能用在正式環境。

論文的倫理段寫到，公開可能讓審查方在規避工具採用之前，先找出並修補這些策略。作者發表的理由是資源充足的審查方本來就能自行找出這些手法，而且依論文引用的先前研究，審查方把新技術放進正式系統會延遲一段時間（例如數個月）。從論文提到的低成本、程式碼與提示都已公開來看，我們判斷審查方用同樣的方法測試自家設備並不困難。

依論文的說明，研究者找出策略之後要由工具開發者整合進實際的規避工具，使用者在工具更新後才會用上。在那之前，正在使用規避工具的讀者不需要做任何設定。研究針對的是依規則比對標準協定的審查設備，沒有測試完全加密、整條連線看起來像隨機資料的協定，也沒有測試專有協定。
