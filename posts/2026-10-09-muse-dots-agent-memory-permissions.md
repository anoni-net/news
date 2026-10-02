---
title: Meta Muse 與 OpenAI Dots 的記憶與權限設計
description: Meta 的 Muse 與 OpenAI 的 Dots 都在 9 月推出，在雲端常駐、讀取連上的 App 資料並整理成記憶。到 10 月 2 日為止，台灣的 App Store 沒有 Muse，Dots 只開放給 ChatGPT 的 Pro 與 Business Premium 方案，用 ChatGPT 或 Mac 的人可以先檢查記憶與權限設定。
date: 2026-10-09T00:05:00+08:00
slug: muse-dots-agent-memory-permissions
categories:
  - tracking
sources:
  - title: "Introducing Muse: The World’s First Personal AI Agent Built for Everyone"
    url: https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
    publisher: Meta
    date: 2026-09-08
  - title: How to manage your Muse data
    url: https://www.meta.com/help/artificial-intelligence/2225571704857152/
    publisher: Meta
  - title: Introducing dots
    url: https://openai.com/index/introducing-dots/
    publisher: OpenAI
    date: 2026-09-29
  - title: Dots privacy, security, and safety FAQs
    url: https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
    publisher: OpenAI
  - title: Getting started with your dot
    url: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
    publisher: OpenAI
  - title: Meta’s Muse AI surprises users — but not in a good way
    url: https://freedom.press/digisec/blog/metas-muse-ai-surprises-users-but-not-in-a-good-way/
    publisher: Freedom of the Press Foundation
    date: 2026-09-30
  - title: Muse, Meta's extraordinarily privileged AI assistant, has a serious 0-day
    url: https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/
    publisher: Ars Technica
    date: 2026-09-21
  - title: I asked Meta’s Muse for its filesystem and it sent me 6.8 GB
    url: https://mouse.dev/blog/muse-runtime-export/
    publisher: mouse.dev
    date: 2026-09-22
  - title: Yeah, don't give Meta's Muse app access to your Mac
    url: https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/
    publisher: 9to5Mac
    date: 2026-09-28
  - title: Meta's Muse AI Agent Read a User's Private iMessages. Then It Lied About How
    url: https://decrypt.co/379122/metas-muse-ai-agent-user-private-imessages-lied-how
    publisher: Decrypt
    date: 2026-09-23
  - title: ChatGPT can now send texts for you with new Apple Messages plug-in
    url: https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/
    publisher: TechCrunch
    date: 2026-08-20
  - title: ChatGPT gets all up in your iMessages
    url: https://freedom.press/digisec/blog/chatgpt-gets-all-up-in-your-imessages/
    publisher: Freedom of the Press Foundation
    date: 2026-08-26
  - title: Memory in ChatGPT
    url: https://help.openai.com/en/articles/8590148-memory-faq
    publisher: OpenAI
  - title: Data controls in ChatGPT
    url: https://help.openai.com/en/articles/7730893-data-controls-faq
    publisher: OpenAI
  - title: 在 Mac 上更改「隱私權與安全性」設定
    url: https://support.apple.com/zh-tw/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: Premium seats are coming to ChatGPT Business
    url: https://openai.com/index/premium-seats-chatgpt-business/
    publisher: OpenAI
  - title: 允許輔助使用 App 取用 Mac
    url: https://support.apple.com/zh-tw/guide/mac-help/mh43185/mac
    publisher: Apple
  - title: Muse from Meta App
    url: https://apps.apple.com/us/app/muse-from-meta/id6760173601
    publisher: App Store
  - title: Warning sources against using AI chatbots
    url: https://securedrop.org/news/updated-landing-page-guidance/
    publisher: SecureDrop
    date: 2026-09-24
watch:
  - date: 2026-11-09
    note: Muse 是否擴大到台灣等其他地區、Mac 版讀取訊息的問題有沒有修正，Dots 是否開放給其他方案
authors:
  - anoni-net
---

Meta 在 9 月 8 日推出 Muse，OpenAI 在 9 月 29 日推出 Dots。兩者都是 AI agent，也就是能自行替使用者執行一連串工作的 AI 助理。它們在雲端持續運作，讀取使用者連上的 App 與服務、整理成記憶，再主動處理事情。Meta 的公告寫明 Muse 先在美國推出，到 10 月 2 日為止台灣的 App Store 沒有上架。同一天為止，Dots 只開放給 ChatGPT 的 Pro 與 Business Premium 方案。

Muse 有 iPhone、Android 與網頁版，Meta 的公告寫到大部分功能免費，另有付費方案，美國 App Store 頁面列出的介面語言包含正體與簡體中文。新聞自由組織 Freedom of the Press Foundation（FPF）的電子報轉述一位使用者的說法，Muse 替使用者在 Facebook Marketplace 賣鍵盤時接受了使用者不滿意的價格，把住址給了買家，買家上門時也沒有通知使用者。到 10 月 2 日為止，我們沒有看到 Meta 對這個案例的回應。FPF 也提醒，Muse 預設會用使用者的互動紀錄訓練 Meta 的模型。

9to5Mac 與 Decrypt 報導了一位科技專欄作者在 Mac 上測試 Muse 的經過。作者在設定時拒絕了訊息權限，之後 Muse 的建議卻用到作者與節目搭檔的對話。Decrypt 寫到讀取 Mac 的訊息資料庫需要完全取用磁碟權限。Meta 一位主管在 Threads 回應訊息存取是需要使用者自行開啟的功能，作者則表示拒絕之後 Muse 的設定裡仍顯示訊息存取為開啟。

研究者也找到 Muse 的其他問題。Ars Technica 9 月 21 日報導一個讓其他 App 與終端機指令可以控制 Muse 的漏洞，並寫到 Meta 在報導刊出約 12 小時後發布修補。另一位研究者取得了 Muse 所在的整個雲端執行環境，解壓後有 6.8 GB。這位研究者透過 Meta 的漏洞獎勵計畫提交發現，Meta 標為不適用，回覆列出幾種可能的理由，但沒有指明適用哪一種。

Dots 的每個 dot 是一個獨立的助理，有自己的雲端電腦，透過外掛連上其他 App。依 OpenAI 的說明頁，使用者沒有交辦工作時，dot 會讀取已連上的資料並寫進自己的筆記，這個階段不能傳訊息、修改內容或操作瀏覽器。到 10 月 2 日為止，說明頁寫明個別記憶無法查看、刪除或直接修改，要刪只能刪掉整個 dot。刪掉 dot 時，它建立的檔案與對話另外存放，不會一起刪除。

說明頁也談到提示注入，也就是網頁、Email 或文件裡藏著要 dot 執行使用者沒交辦動作的指令，OpenAI 寫的是防護能降低風險，但無法消除。OpenAI 也寫明在支援的登入流程裡，密碼經由獨立的表單送進瀏覽器環境、不經過模型，在聊天、文件或外掛裡提供的密碼則不在保護範圍。Dots 只能在電腦上建立，未滿 18 歲不能使用。到 10 月 2 日為止，Dots 的說明只見於 OpenAI 自己的文件，還沒有獨立的檢驗報告。

## 導讀觀點 {#perspective}

兩個產品都替使用者在雲端開一台常駐的電腦，連上的資料在背景被讀取、整理成記憶，之後的回答與行動都以這份記憶為基礎。到 10 月 2 日為止，Dots 的記憶只能連同整個 dot 一起刪除。Muse 的記憶存在一個可以直接檢視與編輯的檔案裡，但 Meta 的說明頁寫明，刪除之後 Muse 仍可能記得從中學到的資訊。

兩者的訓練設定也不同。Muse 的「Help improve our AI models」在第一次使用時預設開啟，Meta 寫明關閉之後也套用到過去的互動。OpenAI 的公告寫明，個人方案可以控制 dot 的對話與工作是否用於改善模型。ChatGPT 一般對話的訓練設定是「Improve the model for everyone」，OpenAI 的說明頁寫明關閉之後只對新對話生效，但沒有寫這個設定在個人方案的預設值。

OpenAI 8 月推出的 ChatGPT 訊息外掛，能讀取、摘要、草擬與傳送 Mac「訊息」App 裡的訊息，設定時要開啟完全取用磁碟。TechCrunch 轉述 OpenAI 的說明，訊息內容存在使用者的電腦上、不存到伺服器，FPF 則提醒使用 ChatGPT 時 OpenAI 仍會處理對話內容。Apple 的說明頁寫明，完全取用磁碟讓 App 讀取電腦上的所有檔案，包括「訊息」等其他 App 的資料。

依 OpenAI 的說明頁，斷開 App 只停止 dot 之後的存取，已經整理進 dot 的資料要刪掉整個 dot 才清得掉。關閉 ChatGPT 的記憶也只停止之後與 dot 的分享，dot 已經收到的資訊不會刪除。訊息資料庫裡也有別人傳來的訊息，依 Meta 與 OpenAI 的說明推論，收訊息的人開啟這類權限時，寄訊息給他的人無法控制這些訊息被 AI 讀取。

用 ChatGPT 的人，可以在設定的「Personalization」查看記憶。OpenAI 寫明只刪掉對話，不一定會刪掉由該對話產生的記憶，要另外刪除。訓練設定在「Data controls」，關閉之後只對新對話生效，OpenAI 的說明頁以英文介面寫出這兩個位置。

用 Mac 且授權過 AI App 的人，可以在「系統設定」的「隱私權與安全性」，查看「完全取用磁碟」與「輔助使用」有哪些 App 取得權限。Apple 的說明頁寫明，取得輔助使用權限的 App 也能取用聯絡資訊、行事曆等資料。

想試用 Muse 或 Dots 的人，FPF 建議等技術更成熟，或用一台只放必要資料的裝置，代價是要另外準備裝置。到 10 月 2 日為止，Dots 需要付費方案，其中 Business Premium 每人每月 125 美元。SecureDrop 在 9 月 24 日的公告建議，準備聯絡媒體揭露資訊的人不要在登入狀態下使用 AI 聊天服務，提示詞的紀錄可能被用來辨識身分。
