---
title: GLM-5.3 的漏洞利用能力與開放權重的防護
description: Anthropic 9 月 29 日發表對智譜開放權重模型 GLM-5.3 的測試報告，模型能寫出攻擊瀏覽器的程式。在報告的模擬測試裡，偽裝情境等手法可以繞過防護。智譜的發布說明寫到，公開的權重只帶著模型本身的防護，強大的防禦能力也不該只留在少數組織。一般讀者能做的是瀏覽器更新後盡快重新啟動。
date: 2026-10-10T00:00:00+08:00
slug: glm-5-3-cyber-capabilities
categories:
  - security
sources:
  - title: GLM-5.3 and the spread of advanced cyber capabilities
    url: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
    publisher: Anthropic
    date: 2026-09-29
  - title: "Preparing GLM-5.3 for Open Release: A Responsible Path to Cyber Defense"
    url: https://x.com/Zai_org/article/2088280509474320693
    publisher: Z.ai
    date: 2026-08-14
  - title: "GLM-5.3: Frontier Coding with Emergent Cyber Capabilities"
    url: https://z.ai/blog/glm-5.3
    publisher: Z.ai
    date: 2026-08-14
  - title: CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities
    url: https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
    publisher: NIST
    date: 2026-09-17
  - title: How Far Behind the Frontier are Leading Open Weight Models on Cyber?
    url: https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
    publisher: AI Security Institute
    date: 2026-07-17
  - title: Stable Channel Update for Desktop
    url: https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_0153744567.html
    publisher: Google
    date: 2026-06-08
  - title: 更新 Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 管理 Chrome 的安全性
    url: https://support.google.com/chrome/answer/10468685?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 調整 Tor Browser 安全等級以平衡隱私與可用性
    url: https://support.torproject.org/zh-TW/tor-browser/features/security-levels/
    publisher: Tor Project
  - title: 讓你的AI懂臺灣！數位發展部公布臺灣主權AI評測結果，攜手產官打造可信任AI生態系
    url: https://moda.gov.tw/ADI/news/latest-news/20538
    publisher: 數位發展部數位產業署
    date: 2026-09-02
watch:
  - date: 2026-11-10
    note: Anthropic 回報給瀏覽器維護者的漏洞是否已修補公開，智譜是否公開回應這份報告
authors:
  - anoni-net
---

美國 AI 公司 Anthropic 9 月 29 日發表測試報告，對象是中國的智譜（中國以外稱 Z.ai）8 月推出的語言模型 GLM-5.3。報告的結論是，GLM-5.3 能自行找出軟體漏洞並寫成可用的攻擊程式，能力接近 Anthropic 只提供給篩選過的資安防禦方的 Claude Mythos Preview。報告也寫到，在模擬測試裡，偽裝情境等簡單的手法就能繞過 GLM-5.3 的防護。一般讀者不會直接用到這個模型，能做的事跟以往相同，瀏覽器更新後盡快重新啟動。

GLM-5.3 的權重（模型本身的參數）8 月底公開，任何人都能下載與修改。智譜 8 月 14 日在 X 發表的說明寫到，權重公開之後，沒有開發者能保證控制每一種後續的修改與用途。同一份說明還寫到，強大的防禦能力不能只留在少數資源充足的組織，開源專案維護者與獨立研究者也需要。

在 Anthropic 執行的 ExploitBench 基準測試裡（題目是 Chrome 的 JavaScript 引擎 V8 的已知漏洞），GLM-5.3 嘗試 410 次，有 50 次寫出完整的攻擊程式，Claude Mythos Preview 是 56 次。在另一項以開源專案為對象的內部測試裡，GLM-5.3 有 4% 的嘗試能完全控制程式的執行流程，Mythos Preview 是 6%，Claude Opus 4.6、GLM-5.2 等較早的模型一次都沒有成功。美國國家標準暨技術研究院（NIST）轄下的 AI 標準與創新中心（CAISI）9 月 17 日的評估寫到，GLM-5.3 是到當時資安能力最強的開放權重模型，綜合多項測驗落後美國最前沿的模型約四個月。CAISI 對照的美國模型包括只提供給篩選過的使用者的版本。

一位研究者花了大約一天、投入有限的人力，讓 GLM-5.3 在一款常用瀏覽器的 JavaScript 引擎找到數個未知的漏洞。模型把這些漏洞串成一個網頁，訪客用該瀏覽器的 Linux 版本打開，網頁就能讀取訪客電腦上的任意檔案。Anthropic 在報告裡寫到，其他平台也可能受影響，在那些平台上利用的路徑或許更複雜。報告沒有寫出是哪一款瀏覽器，只寫到漏洞已經回報給維護者。

另一位研究者讓較小的 GLM-5.3-Flash 根據 Chrome 漏洞 `CVE-2026-11645` 與另一個已知漏洞的公開資料，寫出串連兩者的攻擊程式。研究者投入 20 分鐘，模型執行 8 小時，依智譜的 API 價格換算約 20.40 美元。Google 在 6 月 8 日的 Chrome 更新修補了 `CVE-2026-11645`，公告寫明已有攻擊程式在外流傳。

報告寫到，上面這些寫攻擊程式的任務沒有觸發 GLM-5.3 的拒絕，要求協助開發惡意程式或攻擊遠端目標時，模型則會拒絕。Anthropic 另外在模擬環境要求它攻擊遠端系統，直接提出時模型全部拒絕。告訴模型它在演練中扮演紅隊（模擬攻擊方的測試人員）時，模型有 64% 的情況開始嘗試連線目標系統，預先填入模型的思考內容、讓它看起來已經決定執行時是 92%。用 abliteration 這種手法修改權重、移除拒絕行為之後，比例是 100%。

Anthropic 第一次用 abliteration 修改權重，花了約 2,200 個 GPU 小時、約 4,400 美元，估計熟悉手法的團隊約需 600 個 GPU 小時、約 1,200 美元。修改後的模型在一般科學能力測驗的分數不變，從資安測驗抽樣的題目分數略低。報告也寫到，GLM-5.3 發布後幾天內，已有數個開發者公開了移除拒絕行為的版本。

在 Anthropic 自己的測試裡，透過 API 使用、帶防護的 Claude 擋下了偽裝成紅隊的請求。另外兩種手法對 Claude 一般無法施行，因為 Claude 的 API 不提供預填思考內容的方式，權重也沒有公開。繞過防護的這組測試在模擬環境進行，模型產生的程式碼沒有實際執行，報告寫明模擬無法完整反映真實情況。

## 導讀觀點 {#perspective}

模型拒絕惡意請求的能力是訓練出來的，跟模型的其他能力存在同一組權重裡。透過 API 提供模型時，模型開發者可以在模型外面另外加上過濾與監控。權重公開之後，使用者在自己的電腦上執行，外面那幾層就不存在。修改權重也不需要模型開發者同意。

智譜在 X 的說明寫到，GLM-5.3 有三層防護，分別是請求分類器、評估執行過程風險的監控，以及模型本身的安全訓練。前兩層部署在智譜自己的服務，不會自動跟著模型進到使用者自行架設的環境，公開的權重只帶著第三層。說明也寫到，模型層的防護能提高濫用的門檻，但無法做到絕對的控制。

智譜在同一份說明裡寫到這類能力可攻可守，因此計畫分階段發布，先讓篩選過的資安合作夥伴測試。智譜 8 月 14 日的發布部落格寫到，權重在兩週後、完成安全評估與強化之後公開。

Anthropic 在報告裡的評估是，GLM-5.3 發布時沒有足以限制濫用的防護。報告寫到，同等能力的其他模型發布時都帶有防護，或只透過限制存取的計畫提供，也寫到政府應該對能力足夠的模型做安全測試。到 10 月 5 日為止，查不到智譜針對這份報告的公開回應。

Anthropic 的報告寫到，防禦方應該取得至少跟攻擊方一樣好的模型。Anthropic 透過 Project Glasswing 等計畫把模型提供給篩選過的防禦方，並寫到正在擴大提供的範圍。智譜的說明寫到，防禦能力不能只留在少數組織。智譜的做法是隨 GLM-5.3 推出 OpenVuln 計畫，跟維護者合作審查重要的開源專案，協助通報與修補漏洞。

英國 AI 安全研究所（AISI）7 月的分析寫到，開放權重模型可以私下架設、資料不必回傳給模型開發者，也不會被開發者改版或下架。同一份分析也寫到，一旦公開，防護可以被移除，複製出去的模型也收不回來。AISI 以 6 月推出的 GLM-5.2 等模型測得，開放權重模型的資安能力落後最前沿的封閉模型 4 到 7 個月，2025 年多數時候是 6 到 10 個月。AISI 把這段落差視為能用到最前沿封閉模型的防禦方的準備時間。

讀者無法控制誰使用這些模型，能縮短的是漏洞修補之後、自己的瀏覽器還沒更新的這段時間。在報告的實驗裡，GLM-5.3-Flash 根據已公開的漏洞資料，執行 8 小時就寫出攻擊程式。Chrome 會在背景準備更新，要重新啟動才會套用。長時間不關瀏覽器的人可以到「說明」的「關於 Google Chrome」檢查，出現「重新啟動」按鈕代表更新還沒套用。

更新擋不住還沒修補的漏洞，常造訪陌生網站的人可以再減少網頁程式能用的瀏覽器功能。在 Chrome「隱私權和安全性」的「安全性」裡，可以把「管理 JavaScript 最佳化和安全性」設成「自動在不熟悉的網站上停用 JavaScript 最佳化工具」，部分網站可能因此變慢。Tor Browser 的「較安全」等級會在非 HTTPS 的網站停用 JavaScript，「最安全」在所有網站預設停用，部分網站會無法正常運作。這些設定縮小的是網頁程式攻擊瀏覽器的機會，無法擋下騙你輸入密碼的釣魚網頁。

之後可以留意，開放權重模型的防護要做到什麼程度才算足夠。台灣數位發展部 9 月 2 日公布的 AI 模型評測涵蓋語言、社會文化與價值觀的理解，模型的資安能力要不要也納入政府的測試、由哪個單位負責。AISI 所說的準備時間，是否足夠讓漏洞先被修補。人力不足的開源專案，能否用到跟攻擊方同級的工具。
