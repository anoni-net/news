---
title: ChatGPT 廣告的客戶名單比對與對話內容
description: ChatGPT 的廣告主可以上傳電子郵件、電話號碼或手機廣告識別碼的名單，讓廣告只出現在名單上的使用者面前。廣告只顯示給 Free 與 Go 方案，台灣 9 月 23 日起陸續推出。依 OpenAI 到 10 月 20 日的說明頁，關閉廣告個人化之後，ChatGPT 仍會依目前的對話內容挑選廣告。
date: 2026-10-22T00:00:00+08:00
slug: chatgpt-ads-customer-lists
categories:
  - tracking
follows:
  - 2026-09-26-chatgpt-ad-pixel-identifier
sources:
  - title: Set up Custom Audiences for your Campaign
    url: https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign
    publisher: OpenAI
  - title: ChatGPT 中的廣告
    url: https://help.openai.com/zh-hant/articles/20001047-ads-in-chatgpt
    publisher: OpenAI
  - title: Ad Tools Terms
    url: https://openai.com/policies/ad-tools-terms/
    publisher: OpenAI
    date: 2026-08-24
  - title: Privacy policy
    url: https://openai.com/policies/privacy-policy/
    publisher: OpenAI
    date: 2026-07-30
  - title: ChatGPT Ads expands to Southeast Asia and Taiwan
    url: https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
    publisher: OpenAI
    date: 2026-09-23
  - title: How ChatGPT Targets Ads To You Based On Your Prompts, Phone Number, and Email
    url: https://www.404media.co/how-chatgpt-targets-ads-to-you-based-on-your-prompts-phone-number-and-email/
    publisher: 404 Media
    date: 2026-10-15
  - title: Here's How ChatGPT Is Targeting You With Ads
    url: https://gizmodo.com/heres-how-chatgpt-is-targeting-you-with-ads-2000826457
    publisher: Gizmodo
    date: 2026-10-16
  - title: About customer list custom audiences
    url: https://www.facebook.com/business/help/341425252616329
    publisher: Meta
  - title: How Google uses Customer Match data
    url: https://support.google.com/google-ads/answer/6334160
    publisher: Google
watch:
  - date: 2026-11-20
    note: OpenAI 是否說明收到未雜湊的電子郵件與電話後如何處理、關閉個人化是否排除名單比對，以及台灣是否有主管機關回應
authors:
  - anoni-net
---

404 Media 10 月 15 日報導，ChatGPT 的廣告主可以上傳電子郵件、電話號碼或手機廣告識別碼的名單，讓廣告只出現在名單上的使用者面前。OpenAI 給廣告主的說明頁也列出這項功能，名稱是自訂受眾（Custom Audiences）。ChatGPT 的廣告只顯示給 Free 與較低價的付費方案 Go，台灣 9 月 23 日起陸續推出，Plus、Pro、Business 等方案沒有廣告。依 OpenAI 到 10 月 20 日的使用者說明頁，關閉廣告個人化之後，ChatGPT 仍會依目前的對話內容挑選廣告。

根據自訂受眾的說明頁，名單可以是電子郵件、電話號碼、兩者的 SHA-256 雜湊值，或 Google 廣告 ID（GAID，Android 手機上的廣告識別碼）。雜湊是把資料轉成固定長度字串的單向運算。上傳時也可以用沒有雜湊的原始資料，上傳的檔案通常在 24 小時內刪除。OpenAI 把名單跟 ChatGPT 的使用者比對，比對到的人才算進受眾。

名單可以用來只對受眾投放、排除受眾，或提高、降低對受眾的出價（廣告主願意為一次曝光或點擊付的價格）。只對受眾投放與調整出價時，比對到的使用者至少要 25,000 人，排除用的名單可以少於 25,000 人。廣告管理工具也不會顯示比對到哪些人。

依 Gizmodo 轉述 404 Media 的報導，404 Media 自己在 ChatGPT 刊登了兩組廣告活動測試這套系統。依同一篇轉述，OpenAI 收到沒有雜湊的原始資料後會不會再雜湊，並不清楚。404 Media 的報導有付費牆，付費牆之前公開的只有開頭兩段，其餘細節依 Gizmodo 的轉述。

依 OpenAI 的使用者說明頁，OpenAI 不會把使用者的對話、記憶、姓名、電子郵件、精確位置與 IP 位址交給廣告主，廣告主只會收到觀看與點擊次數這類彙總的成效數字。使用者透過廣告傳訊息給廣告主時，廣告主看得到那些訊息。個人健康、心理健康與政治等敏感主題的對話附近不放廣告，被判斷為未滿 18 歲的帳號與暫存對話也不顯示廣告。

## 導讀觀點 {#perspective}

用客戶名單投放廣告在業界很常見，Google 的 Customer Match 與 Meta 的客戶名單自訂受眾都是同類功能。依 Meta 的說明頁，Meta 會先雜湊名單再比對，Google 的說明頁則寫 Google 不接收實際的電子郵件地址。OpenAI 的說明頁列出的上傳格式包含沒有雜湊的原始資料。404 Media 的報導也提到，ChatGPT 的廣告還會依使用者輸入的提示詞挑選。

依 OpenAI 給廣告主的 Ad Tools Terms（廣告工具條款），名單只能是廣告主自己蒐集的第一方資料，不得取自資料掮客（蒐集並轉售個人資料的業者）。廣告主要保證已依規定告知當事人，並取得必要的同意或其他法律依據，條款沒有寫 OpenAI 如何查證。到 10 月 20 日，使用者說明頁沒有提到能不能查自己在哪些廣告主的名單裡。廣告選單裡有「關於這則廣告」可以了解為什麼看到某則廣告，說明頁沒有提到它會不會顯示客戶名單。

9 月 26 日那篇導讀寫的是像素（廣告主裝在自己網站上的追蹤程式碼），它會把其他網站的瀏覽資料送回 OpenAI。OpenAI 的隱私權政策（EEA、英國與瑞士以外的版本）提到，OpenAI 可能從廣告主收到使用者在廣告主那裡的購買紀錄這類資訊，用來顯示更相關的廣告。

用 Free 或 Go 方案的人，可以到 ChatGPT 的「設定」、「廣告控制功能」關閉廣告個人化，也可以關閉「過去的聊天和記憶」這個只影響廣告的開關。同一處也可以刪除廣告資料，最多 30 天後從伺服器移除。說明頁提到手機 App 看不到這個選項時，要先更新到最新版。關閉個人化不會移除廣告，系統仍會依目前的對話挑選廣告。

不想看到廣告的人可以改用 Plus 或 Pro，Free 方案也有無廣告的選項，說明頁提到供應情況可能因地區和時間而不同。無廣告選項的代價是每天能傳的訊息較少，也不能使用圖片生成等工具，Go 方案的使用者要先切回 Free 才能使用。正體中文說明頁的切換步驟寫「輕觸變更方案以享受 Go 無廣告體驗」，跟英文版的「Change plan to go ad-free」意思不同，照做時以英文版為準。依說明頁「暫存對話不會顯示廣告」，本文推論不想讓某段對話影響廣告的人可以改用暫存對話。

名單可以包含電子郵件、電話號碼與 GAID，OpenAI 沒有說明比對時用的是帳號的哪些資料。若比對的是帳號登記的信箱與電話（本文的推論），跟購物、會員用的不同時，名單可能比對不到。OpenAI 之後會不會說明收到原始資料後如何處理、關閉個人化是否也排除名單比對，是接下來可以留意的地方。
