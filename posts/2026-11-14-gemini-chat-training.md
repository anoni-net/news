---
title: Gemini 個人帳戶對話用於模型訓練的範圍與關閉方式
description: 年滿 18 歲的 Gemini 個人帳戶預設開啟「保留活動記錄」，開啟時 Google 會用活動記錄訓練生成式 AI 模型，部分對話經人工審查（依 Google 說明頁，11 月 8 日查閱）。關閉設定或改用臨時對話後，對話不用於訓練（關閉設定時提供意見回饋例外），保留 72 小時。經人工審查的對話最多保留三年。說明頁沒有區分付費與免費方案。
date: 2026-11-14T00:05:00+08:00
slug: gemini-chat-training
categories:
  - tracking
sources:
  - title: Gemini Apps Privacy Hub
    url: https://support.google.com/gemini/answer/13594961?hl=en
    publisher: Google
    date: 2026-10-26
  - title: Gemini 系列應用程式隱私權專區
    url: https://support.google.com/gemini/answer/13594961?hl=zh-Hant
    publisher: Google
    date: 2026-10-26
  - title: 管理及刪除 Gemini 系列應用程式活動記錄
    url: https://support.google.com/gemini/answer/13278892?hl=zh-Hant
    publisher: Google
  - title: 使用 Gemini 系列應用程式
    url: https://support.google.com/gemini/answer/13275745?hl=zh-Hant
    publisher: Google
  - title: 關於透過「連結的應用程式」享有的個人化體驗
    url: https://support.google.com/gemini/answer/16836988?hl=zh-Hant
    publisher: Google
  - title: 在 Gemini 系列應用程式中使用 Gem
    url: https://support.google.com/gemini/answer/15146780?hl=zh-Hant
    publisher: Google
  - title: 和 Gemini Live 自然對話
    url: https://support.google.com/gemini/answer/15274899?hl=zh-Hant
    publisher: Google
  - title: Generative AI in Google Workspace Privacy Hub
    url: https://support.google.com/a/answer/15706919?hl=en
    publisher: Google
    date: 2026-10-06
  - title: "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)"
    url: https://news.ycombinator.com/item?id=50363461
    publisher: Hacker News
    date: 2026-11-04
watch:
  - date: 2026-12-14
    note: Gemini 隱私權專區的兩個更新日期是否改變，付費方案是否另訂規則，72 小時、18 個月、三年這幾個期限與「保留活動記錄」的名稱是否調整
authors:
  - anoni-net
---

年滿 18 歲的使用者登入個人 Google 帳戶使用 Gemini 時，「保留活動記錄」設定預設為開啟。開啟期間，Google 會用活動記錄改良服務與訓練生成式 AI 模型，其中一部分對話會經過人工審查。預設值寫在「管理及刪除活動記錄」說明頁，用途寫在 Gemini 說明中心的隱私權專區（本文於 11 月 8 日查閱），工作或學校帳戶可能適用其他條款。11 月 4 日一則 Hacker News 貼文提到付費訂閱者的對話同樣會用於訓練並引起討論，下文的規則出自 Google 的現行文件，推論處另行標明。

依隱私權專區（隱私權聲明 2026 年 10 月 13 日版、問答 10 月 26 日版），Google 列出的活動記錄用途是提供、開發及改良服務（包括訓練生成式 AI 模型），以及保護 Google、使用者和一般大眾。同一頁提到系統不會使用 Gemini 對話做為顯示廣告的依據（日後調整會提供清楚說明），Google 也不會販售個人資訊。

設定開啟時，對話、上傳的檔案與分享的螢幕畫面都會存進活動記錄，連結應用程式（讓 Gemini 取用其他 Google 應用程式與第三方服務資料的功能）的資料與從其他 AI 平台匯入的對話同樣用於改良服務。活動記錄預設 18 個月後自動刪除，可以改成 3 個月、36 個月或不自動刪除。音訊、Gemini Live（以語音與 Gemini 自然對話的功能）的影片與螢幕分享預設不用於改良服務，需要另外勾選，Live 對話的轉錄稿與分享給 Live 的上傳內容則在「保留活動記錄」開啟時用於改良服務。

隱私權專區提到 Google AI 方案（Google 的付費訂閱方案）時，只把訂閱相關資訊列為蒐集項目，訓練與人工審查的段落沒有區分付費與免費。本文據此推論兩者適用同一份聲明，Google 沒有明文寫出這句話，到 11 月 8 日也查不到 Google AI 方案專屬的隱私文件。

工作與學校帳戶的活動記錄設定由 Google Workspace 管理員控管，適用的規則可能不同。Workspace 的生成式 AI 隱私權專區（10 月 6 日版）只適用符合資格的 Workspace 版本，未經 Workspace 客戶（訂閱的組織）事先許可或指示，客戶資料不會用於訓練模型。這些版本的 Gemini 應用程式裡，對話與上傳檔案未經許可不會在組織網域之外由人工審查，也不用於訓練生成式 AI 模型。

依隱私權專區，人工審查員會評估回覆是否品質低落、不準確或有害，並提出更好的回覆。對話也會為了維護安全、處理違反服務條款的行為而接受審查。頁面只寫「部分對話」，沒有公布比例。

對話送交受過專業訓練的服務供應商審查之前，會先解除與帳戶的連結。審查過的對話與相關資料（例如使用語言、裝置類型、位置資訊）最多保留三年，頁面沒有區分審查原因，使用者刪除活動記錄時也不會一併刪除。本文據此推論，關閉設定後為保護用途審查過的對話，保留時間也可能超過 72 小時。使用者在對話裡寫下的姓名或地址仍在文字之中，這也是本文的推論。

## 導讀觀點 {#perspective}

維持開啟時，一般對話預設保留 18 個月，用於訓練並有部分經人工審查。關閉「保留活動記錄」後，日後的對話除提供意見回饋的情況外不用於訓練、不經改善服務的人工審查，保留 72 小時。臨時對話（逐次使用、不顯示在活動記錄與近期對話、離開後無法再存取的對話模式）同樣保留 72 小時，不用於訓練，也不經改善服務的人工審查。三種做法都不影響為保護 Google、使用者和一般大眾而處理對話（「過程中可能會借助人工審查」），審查過的對話最多保留三年，Gemini 設定也無法控管把對話處理成去識別化資料、藉以改良 Google 服務的程序。

「保留活動記錄」同時控管對話的儲存與模型訓練，查閱的說明頁沒有列出只保留對話、不用於訓練的選項。隱私權專區的句子只涵蓋日後的對話，沒有提到關閉之前已存進活動記錄的對話（包括已用於訓練的資料）之後如何處理。關閉之後的短期保留，隱私權專區列出的用途是回覆使用者、處理意見回饋與保護 Google、使用者和一般大眾，舉的例子是系統發生故障時資料可以存取。

隱私權專區寫到 Gemini 設定無法控管去識別化處理，也寫到關閉設定且不提供意見回饋時，日後的對話不會用於改良 AI 模型。兩句的關係頁面沒有說明。

設定關閉時提交意見回饋，Google 會蒐集回饋內容、過去 24 小時內的對話，以及對話裡的上傳項目與連結應用程式的資料。回饋與相關對話會交由受過訓練的團隊審查，並依 Google 隱私權政策用於改良產品與機器學習技術。

依設定說明頁，關閉之後可用的連結應用程式有裝置小幫手、Gemini Notebook（存放筆記本來源檔案的服務）、訊息、電話與 WhatsApp。以 Gem（使用者建立並儲存、用來取得符合特定需求回覆的自訂項目）建立的對話不會保留，Gem 本身留在帳戶裡。關閉期間的對話事後無法在活動記錄查閱。

不想關閉設定的人可以逐次使用臨時對話。Google 訊息與 Chrome 裡的 Gemini 沒有這項功能，工作與學校帳戶也不能用。對話中無法使用 Gem、需要開啟「保留活動記錄」的連結應用程式與個人化回覆，也無法提供意見回饋。

對話能否用於訓練，牽涉使用者對自己資料的控制與產品改良兩種考量。Google 在隱私權專區的說明是審查員的建議會用來改善模型日後的回覆，並請使用者不要輸入不想讓審查員看到、或不願供 Google 改良服務的機密資訊。到 11 月 8 日，查不到 Google 對 Hacker News 貼文的公開回應，也查不到消費者團體或資料保護機構針對 Gemini 個人對話訓練的正式文件。本文呈現的只有 Google 這一方的文件。

電腦版的路徑是在 `gemini.google.com` 依序點按「設定與說明」、「活動記錄」，再到畫面上方點「開啟」，選「關閉」或「關閉並刪除活動記錄」（說明頁有正體中文與行動 App 的步驟）。依隱私權專區的規則推論，不希望對話用於訓練的人可以關閉設定或每次改用臨時對話。需要長期保留對話、或在個人帳戶連結 Google Workspace 這類應用程式的人可以維持開啟，敏感內容改用臨時對話。機密內容能否輸入，需要依各種做法留下的保留期與審查範圍自行評估。
