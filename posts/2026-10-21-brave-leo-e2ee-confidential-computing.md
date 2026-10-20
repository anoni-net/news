---
title: Brave Leo 的端對端加密對話與機密運算
description: Brave 的 AI 助理 Leo 10 月 15 日起，選用 GLM 5.3 Flash 模型的對話會在瀏覽器端加密，只在硬體隔離的運算區裡解密處理。其他模型不在範圍內，運算區的證明到 10 月 20 日為止仍由 Brave 的伺服器代為檢查，iOS 版查不到支援的說明。
date: 2026-10-21T00:00:00+08:00
slug: brave-leo-e2ee-confidential-computing
categories:
  - encryption
sources:
  - title: "Another Brave User-First AI Win: Leo adds End-to-end Encryption, Oblivious HTTP, and Verifiable Confidential Computing"
    url: https://brave.com/blog/browser-ai-e2ee/
    publisher: Brave
    date: 2026-10-15
  - title: near-tee-verifier
    url: https://github.com/brave/near-verifier
    publisher: GitHub
  - title: "[AI Chat] Add support for end-to-end encryption with NEAR models"
    url: https://github.com/brave/brave-browser/issues/55247
    publisher: GitHub
    date: 2026-05-05
  - title: What are the differences between Leo's AI Models?
    url: https://support.brave.app/hc/en-us/articles/26727364100493
    publisher: Brave
  - title: Brave Leo AI
    url: https://brave.com/leo/
    publisher: Brave
  - title: "Verifiable Privacy and Transparency: A new frontier for Brave AI privacy"
    url: https://brave.com/blog/browser-ai-tee/
    publisher: Brave
    date: 2025-11-20
  - title: GLM-5.3-Flash
    url: https://huggingface.co/zai-org/GLM-5.3-Flash
    publisher: Hugging Face
  - title: brave_components_resources_zh-TW.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-TW.xtb
    publisher: GitHub
  - title: Brave adds end-to-end encryption to chats with AI assistant Leo
    url: https://cyberinsider.com/brave-adds-end-to-end-encryption-to-chats-with-ai-assistant-leo/
    publisher: CyberInsider
    date: 2026-10-16
  - title: "TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition"
    url: https://tee.fail/
    publisher: TEE.fail
watch:
  - date: 2026-11-20
    note: Leo 的說明中心是否補上 GLM 5.3 Flash 與端對端加密的說明、iOS 版是否支援、瀏覽器是否開始自行檢查 attestation
authors:
  - anoni-net
---

Brave 10 月 15 日宣布，AI 助理 Leo 跟 GLM 5.3 Flash 模型的對話改成端對端加密，GLM 5.3 Flash 是 Z.ai 以 MIT 授權公開權重的模型。對話在瀏覽器端加密，只在 NEAR AI 營運的可信執行環境（TEE，處理器與 GPU 裡跟主機其他部分隔離的運算區）裡解密與產生回答。加密要在 Leo 的模型選單手動選 GLM 5.3 Flash 才會生效，Leo 的其他模型不在範圍內，到 10 月 20 日為止 GLM 5.3 Flash 也還標示為測試階段。依部落格，正式版與 Nightly、Beta 兩個測試通道都已提供，所有 Brave 使用者都能選用。

部落格沒有寫支援哪些平台。GitHub 上的開發議題只標了桌機與 Android，iPhone 版到 10 月 20 日為止查不到支援的說明。

依 Brave 的部落格，瀏覽器用網際網路標準組織 IETF 制定的 Oblivious HTTP（OHTTP）加密每一則提問與分享給 Leo 的網頁，解密用的金鑰只存在 TEE 裡。加密後的訊息先送到 Brave 自己營運的 AI Gateway，再轉給 NEAR AI。Brave 看得到使用者的 IP 位址、讀不到內容，NEAR AI 營運的 TEE 在運算區裡解密、看不到 IP 位址，部落格也提到 NEAR AI 與雲端主機的營運者都讀不到運算區的內容。每一輪對話都用新的一次性金鑰重新加密整段紀錄，紀錄只存在使用者的裝置上，Brave 與 NEAR AI 都不保存。

部落格接著說明部署前的檢查，NEAR AI 的每一次部署都要先通過 Brave 檢查程式的檢查才會被核准。檢查的項目包括 Intel 與 Nvidia 簽署的證明（attestation，由硬體簽署、證明運算區是真品並記錄裡面執行哪一份程式的憑據），以及從原始碼重新建置、確認跟線上的程式一致。AI Gateway 轉送每一則訊息前會再核對一次，採用的驗證結果不超過一小時，不通過就不轉送。檢查程式 `near-tee-verifier` 以開源授權公開，有 NEAR AI 的 API 金鑰就能自行對線上服務執行驗證。

Brave 2025 年 11 月在 Nightly 試行過第一版，部落格提到當時的保護建立在政策上，檢查也要信任 Brave。新版的檢查程式公開，有 API 金鑰就能自行執行。到 10 月 20 日為止，瀏覽器端的檢查仍由 Brave 的伺服器代為處理。

到 10 月 20 日為止，說明中心沒有 GLM 5.3 Flash 端對端加密的文章。Leo 的模型說明頁列的仍是 GLM 4.7 Flash，也寫所有模型都由 Brave 自行營運。開發議題標了不列入版本紀錄，各平台的版本紀錄都沒有提到端對端加密。

## 導讀觀點 {#perspective}

一般的 AI 對話服務在伺服器上解開提問，營運者在技術上讀得到內容，使用者只能相信隱私政策。OHTTP 把「誰在問」跟「問了什麼」拆給兩方，轉送的一方只知道 IP 位址，處理的一方只看到內容。TEE 的設計是讓主機的營運者也讀不到運算區的記憶體，attestation 讓外界確認裡面執行的是公開過的程式。Brave 的部落格把 Leo 的新做法描述成從政策承諾改成密碼學的證明。

根據部落格，10 月 15 日發布時瀏覽器仍依賴 Brave 的 AI Gateway 做檢查，之後才會分階段改成由瀏覽器直接驗證硬體的證明。部落格也列出整條驗證鏈最後要信任的對象，包括 Intel 與 Nvidia、TEE 的作業系統 dstack、建置紀錄的 Sigstore、GitHub、Hugging Face 與公共 DNS。`near-tee-verifier` 的說明則提醒，重新建置只證明線上程式來自指定的版本，不能證明那個版本裡沒有後門。執行模型的推論軟體是第三方套件，依部落格與 `near-tee-verifier` 的說明沒有從原始碼重新建置，改用硬體證明的部署紀錄鎖定版本。

資安會議 IEEE S&P 2026 收錄的論文 TEE.fail 中，研究者在伺服器的 DDR5 記憶體匯流排接入監聽裝置，在部分情況下取出 Intel TDX（Intel 處理器上的 TEE 技術）簽署證明用的金鑰。用這把金鑰偽造的證明可以通過驗證，也能用來攻破 Nvidia GPU 的機密運算。依研究網站，攻擊需要實體接觸伺服器，Intel 不把這類實體攻擊列入 TDX 要防範的範圍。研究者也寫到，就他們所知還沒有被實際利用。

研究網站另有一節示範 dstack，惡意的伺服器提供者可以偽造全部證明，也能借用別處 Nvidia GPU 的證明。網站給 dstack 使用者的建議是留意自己要信任實際管理 TDX 硬體的營運者。論文沒有分析 Brave 與 NEAR AI 的部署，本文 10 月 20 日搜尋時也沒有找到針對 Leo 的獨立分析。

依 `near-tee-verifier` 的說明，GPU 的證明沒有綁進 TDX 的證明裡，無法確認回答來自哪一張 GPU。要排除這個缺口，需要 NEAR AI 補上兩者的綁定。

想在 AI 對話裡處理不願讓服務業者讀到的文字或網頁內容，可以在 Brave 桌機版或 Android 版打開 Leo，從模型選單選 GLM 5.3 Flash。依原始碼開發分支的正體中文翻譯，模型選單在 GLM 5.3 Flash 旁顯示「以 NEAR AI TEE 驗證隱私」，回答旁有「已驗證」的標章。依原始碼與部落格推論，標章反映的是 Brave 伺服器的檢查結果，到 10 月 20 日為止瀏覽器本身還沒有驗證。Leo 不需要帳號，說明頁提到免費版有使用次數的限制，但沒有列出數字。

Brave 沒有寫 Leo 的回答支援哪些語言，Hugging Face 上 GLM 5.3 Flash 的模型說明頁（模型卡）標示的語言是英文與中文。依部落格的說明，加密只及於對話內容，轉送訊息的 Brave 仍看得到 IP 位址。模型產生的搜尋查詢也會離開 TEE 送到 Brave Search（不綁 IP 位址）。
