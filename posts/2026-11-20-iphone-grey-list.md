---
title: iPhone 鍵盤建議與滑動輸入排除的詞組清單
description: 一位獨立研究者從 iOS 27.0 的鍵盤資料還原出 Apple 未公開的詞組清單，英文有 4,513 條，另有 27 種語言與文字的清單。清單上的詞組不會出現在預測建議，多數也無法用滑動輸入打出，逐字輸入不受影響。Apple 回覆 Reuters 時表示鍵盤的設計是避免提供可能不當或冒犯的建議，到 11 月 15 日為止，說明頁沒有關閉這份清單的設定。
date: 2026-11-20T00:05:00+08:00
slug: iphone-grey-list
categories:
  - mobile
sources:
  - title: "Apple’s predictive text restrictions include ‘Dictator Trump’ and ‘Sleepy Joe,’ researcher finds: Reuters exclusive"
    url: https://www.cp24.com/news/world/2026/11/06/apples-predictive-text-restrictions-include-dictator-trump-and-sleepy-joe-researcher-finds-reuters-exclusive/
    publisher: Reuters（CP24 轉載）
    date: 2026-11-06
  - title: "Swipeblocked: the phrases your iPhone won't suggest"
    url: https://swipeblocked.com/
    publisher: Swipeblocked
  - title: 如何在 iPhone、iPad 或 iPod touch 上使用「自動修正」和預測字詞
    url: https://support.apple.com/zh-tw/104995
    publisher: Apple
    date: 2026-04-13
  - title: 在 iPhone 上設定常用文字的縮寫
    url: https://support.apple.com/zh-tw/guide/iphone/iph6d01d862/ios
    publisher: Apple
  - title: "Revealed: Apple's secret list of slurs, insults, and political phrases that can't be swiped"
    url: https://macworld.com/article/3279221/revealed-apples-secret-list-of-slurs-insults-and-political-phrases-that-cant-be-swiped.html
    publisher: Macworld
    date: 2026-11-07
watch:
  - date: 2026-12-15
    note: Apple 是否公開說明這份詞組清單，或在鍵盤設定加入可關閉的選項。Swipeblocked 的變更頁有沒有記錄新的增減
authors:
  - anoni-net
---

依 Reuters 11 月 6 日的獨家報導，一位獨立研究者發現 iPhone 內建鍵盤帶著一份 Apple 沒有公開的詞組清單。列在清單上的詞組不會出現在預測字詞（predictive text，打字時鍵盤列出的下一個字詞建議）裡，多數也無法用滑動輸入（手指在鍵盤上連續滑過字母來打字）打出來。一個字母一個字母輸入時不受影響，清單不會阻止使用者寫出任何字。清單依語言區分，研究者的網站寫到 Apple 另有 27 種語言與文字的類似清單，並各舉了少數例子。

研究者對 Reuters 表示，他 9 月注意到滑動輸入打「white man」時打不順，打「black man」不會。他借助 AI 程式開發工具在作業系統深處找到這份資料，保守估計各語言合計約 10 萬個詞與詞組（不含漢字）。依 Reuters，一家資安公司的工程師表示另外獨立還原出同一份清單，比對結果幾乎完全吻合。研究者整理的 Swipeblocked 網站列出英文清單 4,513 條，網站也寫到其他語言的清單不少跟英文的一樣長。

研究者對 Reuters 表示，清單上絕大多數是粗俗、冒犯或跟毒品、性、暴力相關的詞組。Reuters 另外寫到其中也有政治上敏感的詞組，Swipeblocked 列出的例子包括「Tibetan independence」、「United Ireland」、「Kashmir dispute」、「sleepy Joe」與「make America great again」。「Taiwan is country」也在清單上，網站註明只擋這個寫法，「Taiwan is a country」不擋。清單也有成對卻只擋一邊的例子，「read gay smut」被擋，「read smut」不擋。

根據 Swipeblocked 的說明，預測字詞從不提供清單上的詞組，即使那是最明顯的下一個詞。多數詞組也無法用滑動輸入打出，鍵盤會改選別的字，有時選得不合常理。鍵盤還可能改掉前一個已經輸入的字，例如網站示範滑出「left wing conspiracy」的 conspiracy 時，前面的 wing 會變成 wrong。比對只認完全相同的詞序，換個說法就可能通過。

Reuters 在 iPhone 上試了研究者列出的一小部分詞組，全部都難以滑動輸入，或不會出現在建議裡。滑動輸入「United Ireland」常變成「United Iceland」，「Sleepy Joe」變成「Sleepy hope」。「Dictator Trump」可以滑動輸入，但不會出現在建議裡，Swipeblocked 也把它列為只排除建議、仍可滑動輸入的詞組。

依 Swipeblocked 的變更頁，英文清單在 2020 年的 iOS 14.0 約有 1,700 條，到 iOS 27.0 增加到 4,513 條。Apple 會隨 iOS 新版更新清單，兩版之間也透過 iPhone 在背景下載的語言資料更新。「dictator Trump」在 iOS 16.1 加入，「President Trump」與「President Bush」從 2022 年的一次更新起被擋，在 iOS 26.3 移除。iOS 27.0 唯一新增的是「Zionist propaganda」。

Apple 在給 Reuters 的電子郵件裡沒有直接回應研究者的發現，包括清單的規模、組成，以及收入特定政治詞的理由。Apple 的回覆提到使用者一向可以自行輸入特定的字詞，也可以略過任何預測建議，鍵盤的設計是避免提供可能不當或冒犯的建議。

## 導讀觀點 {#perspective}

依 Swipeblocked 的技術說明，鍵盤列出候選字之前，會以要補完的兩到六個詞比對清單。清單只存每組詞算出來的 32 位元指紋，研究者逐一產生候選詞組來比對，才還原出內容。指紋比對也會誤判，iOS 27.0 的英文清單有 176 組無意義的字串剛好吻合，在 iPhone 上一樣被擋。網站也註明清單有解不出來的部分，詞組列在清單上也不代表知道 Apple 收入的理由。

依 iOS 26.3 的鍵盤程式碼，Swipeblocked 另外寫到一套獨立的單字標籤。標為粗俗的字要使用者自行輸入三次才會出現在建議，標為冒犯的字從不建議。

Macworld 的編輯認為清單不算審查清單，因為逐字輸入一定可以，只是想靠滑動或建議打快一點的人會慢下來。研究者對 Reuters 形容這是非常輕度的審查，他認為以 Apple 的規模，輕輕一碰就有很大的影響。Reuters 的報導寫明清單不是禁令。報導也寫到全球有數億人使用 iPhone，Apple 選擇讓鍵盤建議哪些字，可能悄悄影響他們溝通的方式。

公開與自訂方面，Reuters 引述的 EFF 資深律師認為 Apple 要這麼做就應該讓使用者清楚知道並能夠自訂，不該是秘密。Macworld 的編輯仍認為 Apple 管得太多，建議加一個預設開啟、可以關閉的設定。Reuters 轉述的 Apple 回覆裡沒有提到公開或設定，Apple 支援網站的鍵盤說明頁到 11 月 15 日為止也沒有這樣的選項。同一位 EFF 律師雖然有一部分覺得清單令人不安、對 Apple 的取捨有疑問，也看得出有理由把它當成減少不想要或煽動性建議的方法。

收錄的標準方面，研究者對 Reuters 表示可以理解 Apple 不想讓使用者誤傳不雅訊息或煽動性的口號。他也認為套用得不一致，例如「read gay smut」與「read smut」的差別。Macworld 的編輯推測 Apple 比較可能是想避免官司與公關風波。

依 Swipeblocked 的說明，中文清單上的詞在拼音輸入時仍會出現在候選字裡，選了之後鍵盤就不再預測下一個詞。網站列出的中文例子有「六四」、「台独」、「刘晓波」與「习大大」，中國共產黨的名稱在簡體中文的清單不擋、在繁體中文的清單擋，國民黨則兩份都擋。中文輸入引擎有一部分的程式碼，在詞為英文的「taiwan」或「tibet」時不提供建議。網站只依語言列出清單，沒有比較不同國家或地區設定的 iPhone，說明也沒有提到注音等拼音以外的輸入方式。

用 iPhone 內建鍵盤的人，逐字輸入不受清單影響。習慣滑動輸入的人送出前可以回頭看一遍，鍵盤可能已經改掉前一個字（本文依 Swipeblocked 的示範提出的建議）。依 Apple 支援網站的鍵盤說明頁，「預測字詞」可以在「設定 > 一般 > 鍵盤」關閉。說明頁到 11 月 15 日為止沒有關閉清單的設定，也沒有寫關掉「預測字詞」之後滑動輸入是否仍會改字。

同一頁鍵盤說明另有「替代文字」，可以設定快速鍵，打快速鍵時自動換成一整個詞組。iPhone 使用手冊也寫到「輸入碼」（使用手冊對快速鍵的稱呼）欄位留白、只填字詞，能讓自己常用的字詞不被取代。這兩種做法能否讓清單上的詞組回到建議或滑動輸入，兩份說明都沒有寫，我們也沒有實測。想打出清單上的詞組，Swipeblocked 確認可行的方式是逐字輸入，Macworld 提到代價是打字變慢。
