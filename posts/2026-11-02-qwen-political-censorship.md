---
title: 中國開放權重模型 Qwen 的審查與程式碼差距量測
description: 兩家發布移除版模型的公司在 10 月各自公布 Qwen 的量測，一份是中文政治問題的審查比例，一份是程式碼安全性隨客戶身分出現的差距。量測跟用 Qwen 問政治問題的人、用 Qwen3-Coder 寫程式的開發者有關，無論在自己電腦執行或透過服務使用。到 11 月 1 日為止，我們沒有查到第三方重現，也沒有查到 Qwen 團隊的回應。
date: 2026-11-02T00:05:00+08:00
slug: qwen-political-censorship
categories:
  - censorship
regions:
  - CN
sources:
  - title: InterpreticAI/Qwen3.8-27B-Uncensored-v2 · Hugging Face
    url: https://huggingface.co/InterpreticAI/Qwen3.8-27B-Uncensored-v2
    publisher: Interpretic AI
    date: 2026-10-31
  - title: Chinese AI Writes Weaker Code for Beijing’s Adversaries. We Fixed It. A Qwen3-Coder Case Study
    url: https://www.hirundo.io/blog/qwen3-coder-vulnerabilities
    publisher: Hirundo
    date: 2026-10-21
  - title: hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized · Hugging Face
    url: https://huggingface.co/hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized
    publisher: Hirundo
    date: 2026-10-13
  - title: "Westernizing Qwen: Measuring and Mitigating Geopolitical Alignment in Chinese Open-Weight LLMs"
    url: https://www.hirundo.io/blog/westernizing-qwen
    publisher: Hirundo
    date: 2026-10-05
  - title: Political censorship in large language models originating from China
    url: https://doi.org/10.1093/pnasnexus/pgag013
    publisher: PNAS Nexus
    date: 2026-02-17
  - title: Qwen/Qwen3.8-27B
    url: https://huggingface.co/Qwen/Qwen3.8-27B
    publisher: Qwen
    date: 2026-08-05
  - title: Qwen/Qwen3-Coder-30B-A3B-Instruct
    url: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
    publisher: Qwen
    date: 2025-07-31
  - title: Chinese Open Source Model Roundup
    url: https://speechmap.substack.com/p/chinese-open-source-model-roundup
    publisher: SpeechMap
    date: 2025-05-01
  - title: 生成式人工智能服务管理暂行办法
    url: https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
    publisher: 中国网信网
    date: 2023-07-13
  - title: 卓揆：公務機關全面禁用Deepseek AI 服務
    url: https://www.ey.gov.tw/Page/9277F759E41CCD91/3ce9fe8f-2f5f-4d1d-8176-6fa4cf622b82
    publisher: 行政院
    date: 2025-02-03
  - title: 公務機關全面禁用DeepSeek AI 服務，未限制一般民間使用
    url: https://moda.gov.tw/ACS/press/news/press/15296
    publisher: 資通安全署
    date: 2025-02-20
  - title: Bias in Qwen3-Coder Model
    url: https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html
    publisher: Schneier on Security
    date: 2026-10-26
watch:
  - date: 2026-12-02
    note: 是否有第三方重現 Interpretic AI 與 Hirundo 的量測，CCPC-500 是否公開，阿里巴巴或 Qwen 團隊是否回應
authors:
  - anoni-net
---

兩家公司在 10 月下旬各自公布了阿里巴巴 Qwen 系列開放權重模型的量測（開放權重模型指公開模型檔案、可以下載到自己電腦執行的模型）。Interpretic AI 量測 Qwen3.8-27B 回答中文政治問題時的審查比例，10 月 31 日在 Hugging Face 發布移除審查的版本。依 Hirundo 10 月 21 日在部落格公布的量測，Qwen3-Coder 寫出的程式碼安全性會隨系統提示詞（開發者事先給模型的指示）裡的客戶身分改變，該公司也發布了修改過的版本。

兩份研究都出自發布移除版模型的公司，Hirundo 也替使用開放權重模型的組織評估與修正模型。到 11 月 1 日為止，我們沒有查到第三方重現，下文的數字都是兩家公司各自的量測。用 Qwen 問政治問題的人跟 Interpretic 的量測有關，用 Qwen3-Coder 寫程式的開發者跟 Hirundo 的量測有關。

Interpretic 的模型頁寫到，量測以中文提問兩位研究者發表在期刊 PNAS Nexus 的 145 題政治題目，每個回答由另一個語言模型判定有沒有審查。其中 113 題政治敏感的題目裡，Qwen3.8-27B 原模型有 98 題被判為審查（86.7%），移除版剩 4 題（3.5%）。模型頁沒有寫評分用的是哪一個模型、有沒有人工抽查，移除的方式也只寫了「targeted weight edit」（針對性地修改模型權重），沒有附論文或程式碼。Interpretic 列出的限制是政治題只測了中文，也提醒回答有實質內容不代表正確。

題目集出自 2026 年 2 月發表的論文，研究者比較中國與中國以外開發的基礎模型。根據論文摘要，中國開發的模型對 145 題政治問題拒答較多、回答較短，不準確的回答也較多。所有模型用中文提問時的拒答率都比英文高，不過語言之間的差距小於中國與非中國模型之間的差距。

Hirundo 的部落格寫到，研究請 Qwen3-Coder-30B-A3B-Instruct 反覆寫同一個網頁服務，功能是使用者註冊、登入與儲存私密文字。每次只改系統提示詞裡「程式碼替誰寫」的一句，分成中立客戶、美國國防承包商、中國國防承包商與香港民主倡議團體。寫好的應用程式交給 ETH Zurich 與 LogicStar 的公開基準 BaxBench 實際執行，至少一種現成的攻擊成功就算可被入侵。

可被入侵的比例在替美國國防承包商寫的應用程式是 70%，中國國防承包商是 59%。私密資料外洩的比較裡，替香港民主倡議團體寫的應用程式近半會讓任何登入的使用者讀到所有人的私密資料，中立客戶約三分之一（部落格算成相對高出 28%）。提示詞另外加上安全指示的那一組，可被入侵的比例在美國承包商是 74%，中立客戶是 59%。部落格用統計檢定判定上述三項差距都不太像是隨機造成的。

部落格的附錄問答也寫到，研究無法判斷差距是否有人刻意放進模型。小模型本來就容易寫出有漏洞的程式，前面提到的中立客戶也有約三分之一會洩漏，研究量的是額外的風險。研究只測了一個模型與一個任務，任務是從 11 個任務的小樣本裡挑出差距最明顯的那一個。美國與香港兩組是刻意挑選的極端案例。

Hirundo 的移除版公開在 Hugging Face，模型頁寫的做法是行為遺忘（behavioral unlearning，用額外的訓練讓模型忘掉特定行為，同時保留其他能力）。根據部落格，移除版在 Hirundo 自建的 500 題基準 CCPC-500 上被判為審查、偏向或宣傳的回答從 46.6% 降到 4.0%，三項程式碼差距也不再顯著。附錄的其他比較裡，移除版替美國承包商寫的應用程式對中立客戶仍有一項顯著差距，部落格的解讀是效果從國家移到組織類型。在其他十個程式任務上，可以正常運作與可被入侵的應用程式比例都跟原模型相近。

## 導讀觀點 {#perspective}

語言模型的回答取決於訓練用的資料，以及訓練後期的對齊（alignment），也就是讓模型照開發者的規範回答的步驟。兩份研究公開的量測都是大量提問、從輸出計算比例，都沒有分開檢驗訓練資料與對齊。Hirundo 的部落格主張移除版的結果證明程式碼的差距存在模型權重裡，支撐主張的是同一家公司自己的移除實驗。

公開研究專案 SpeechMap 2025 年 5 月量測較早的 Qwen3 世代，整理裡寫到 Qwen3 的開放權重模型在批評中國的題目上普遍審查。中文提問時審查得最徹底，英文也有，芬蘭文只在部分情況出現、也比較不一致。同一份整理也提到，商用版 Qwen-Max 回傳大量 API 錯誤，SpeechMap 的解讀是 API 另有一層審查。本文據此推論，透過服務使用模型時，讀到的回答可能同時受模型本身與服務端的過濾影響。

中國的《生成式人工智能服務管理暫行辦法》2023 年 8 月 15 日施行，第四條要求提供與使用生成式 AI 服務時「不得生成煽動顛覆國家政權、推翻社會主義制度」等內容。根據第二條，沒有向中國境內公眾提供服務的研發與應用不適用這份辦法，我們也沒有查到辦法對公開發布模型權重的專門規定。PNAS Nexus 論文的研究者提醒，論文是觀察性的橫斷研究（在同一個時間點比較不同模型、不做實驗），不能證明監管壓力與中國模型的審查行為之間有因果關係。

台灣行政院 2025 年 2 月 3 日要求公務機關全面禁用 DeepSeek AI 服務，新聞稿提到資料上傳中國的資安風險尚未釐清也並未排除，模型訓練也有思想審查等資料偏異。資通安全署 2025 年 2 月 20 日的說明寫到，禁用範圍包含雲端服務、App 與下載到本機的使用方式，當時沒有限制一般民間使用。公告點名的是 DeepSeek，我們沒有查到點名 Qwen 的公告。

Interpretic 的移除版在 100 題有害請求中拒絕的題數從 100 降到 95，一般能力測驗的分數也小幅下降，考慮改用移除版的人要權衡這些副作用。兩家的移除版跟原模型一樣採 Apache 2.0 授權，Interpretic 沒有附論文或程式碼，Hirundo 也只寫了做法的類別。Hirundo 的部落格寫到打算公開自建的 CCPC-500，我們 11 月 1 日查證時資料集的網址無法存取（回應 401 錯誤），不能確認已經公開。SpeechMap 2025 年 5 月整理當時第三方修改過的中國開源模型，寫到英文的改善明顯，中文只有小幅改善。

用 Qwen 查詢政治、歷史這類敏感題目的人，本文建議把同一個問題拿去問不同來源的模型，再對照新聞與原始資料。論文摘要與 SpeechMap 都寫到中文提問時拒答或審查較多，本文據此推論換一種語言再問可能得到不同的回答，不過論文也提到語言的差距小於中國與非中國模型之間的差距。上述研究都沒有評估這些做法能否補上被審查的內容，沒有被測到的題目也不代表沒有偏誤（本文的推論）。

用 Qwen3-Coder 或其他模型寫程式的開發者，程式碼上線前仍要另外審查與測試。根據 Hirundo 的部落格，在提示詞加上安全指示沒有消除差距，常見的靜態掃描工具也不一定抓得到這類洩漏（登入的使用者可以讀到其他人的資料）。移除版在其他十個任務上仍有約四分之一的應用程式可被入侵，中立客戶的應用程式也會洩漏（見上文）。本文據此推論，無論用哪個版本，審查時都可以優先看存取權限的檢查。

到 11 月 1 日為止，我們沒有查到阿里巴巴或 Qwen 團隊對兩份研究或論文的公開回應。12 月初可以留意是否有第三方重現兩家公司的量測、CCPC-500 是否公開，以及 Qwen 團隊有沒有回應。
