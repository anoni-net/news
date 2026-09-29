---
title: AI 輔助的釣魚攻擊與防範方式
description: Freedom of the Press Foundation 整理 AI 被用在釣魚攻擊的研究，信件寫得更通順、更個人化，但辨識的警訊與防禦方式沒有改變。建議適用於每個收 Email 與簡訊的人。
date: 2026-10-05T07:00:00+08:00
slug: ai-phishing-defenses
sources:
  - title: "Ask a security trainer: Does AI make phishing worse?"
    url: https://freedom.press/digisec/blog/ask-a-security-trainer-does-ai-make-phishing-worse/
    publisher: Freedom of the Press Foundation
    date: 2026-08-27
  - title: 2026 Data Breach Investigations Report
    url: https://www.verizon.com/business/resources/T459/reports/2026-dbir-data-breach-investigations-report.pdf
    publisher: Verizon
  - title: Banks in Singapore to Strengthen Resilience Against Phishing Scams
    url: https://www.mas.gov.sg/news/media-releases/2024/banks-in-singapore-to-strengthen-resilience-against-phishing-scams
    publisher: Monetary Authority of Singapore
    date: 2024-07-09
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: So long passwords, thanks for all the phish
    url: https://security.googleblog.com/2023/05/so-long-passwords-thanks-for-all-phish.html
    publisher: Google
    date: 2023-05-03
  - title: Dangerzone
    url: https://github.com/freedomofpress/dangerzone
    publisher: Freedom of the Press Foundation
authors:
  - anoni-net
---

美國新聞自由組織 Freedom of the Press Foundation（FPF）的數位安全訓練團隊 2026 年 8 月 27 日在專欄整理 AI 被用在釣魚攻擊的研究。釣魚訊息除了 Email，也會透過簡訊、QR code、語音與視訊通話送達。FPF 的結論是 AI 讓釣魚訊息更有說服力，每個人該做的防禦卻沒有改變。

FPF 引用的報告裡，資安意識訓練公司 KnowBe4 估計 2025 年 10 月到 2026 年 3 月之間，用到 AI 的釣魚攻擊增加約 86%。Microsoft 2025 年的報告寫到，AI 自動化的釣魚信點擊率是 54%，一般的釣魚信是 12%。

電信公司 Verizon 在 2026 年的資料外洩調查報告分析一家 AI 公司平台上的濫用紀錄，在攻擊者借助 AI 的初始入侵手法裡，釣魚約占 44%（FPF 誤寫成事件比例）。同一份報告也寫到，Verizon 的事件資料裡以釣魚入侵的比例這幾年幾乎沒有變化。

FPF 引用的研究裡，自動化的手法包括蒐集目標資料、寫出更個人化的內容、在主旨做細微變化來躲過偵測，以及寫出多種語言的版本。信件因此像是專門寫給收件人，例如冒充同事。

FPF 列出四個警訊：寄件地址與冒充對象不符或只是相似、連結指向跟服務無關的網址、訊息製造急迫感，以及不請自來的附件。連結可以不點，自行輸入網址。可疑附件可以用 Google 雲端硬碟預覽，或用 Dangerzone 轉成安全的副本。

## 導讀觀點 {#perspective}

大型語言模型擅長模仿語氣，中文釣魚信也可能寫得通順。靠錯字辨認詐騙信會越來越不可靠，FPF 的四個警訊則都跟文筆無關。

常開啟陌生附件的人可以用開源的 Dangerzone（AGPL-3.0 授權，2026 年 7 月發布 0.11.0）。它在斷網的沙箱裡把文件轉成像素，再到沙箱外重建成沒有文字層的 PDF，要開啟文字辨識（OCR）才能搜尋。支援 Windows、macOS 與 Linux，介面只有英文，Windows 版需要電腦支援並開啟硬體虛擬化。

FPF 建議開啟兩步驟驗證，舉的例子是寄到手機的一次性密碼（OTP）。新加坡金融管理局與當地銀行公會 2024 年 7 月宣布，主要零售銀行三個月內逐步停止讓已啟用數位令牌（digital token）的客戶用 OTP 登入，改由令牌驗證。公告的理由是 OTP 容易被騙走，例如透過仿冒的銀行網站。

密碼金鑰（passkey，以指紋、臉孔或螢幕鎖定取代密碼）同樣不必輸入可被騙走的代碼。Google 的安全性網誌寫到，裝置只把登入簽章交給 Google 的網站與 App，不會交給釣魚網站。代價是能解鎖裝置的人就能登入帳戶，說明頁因此寫明只在自己專用的裝置上建立。

現在能做的第一步，是替最常用的帳號建立密碼金鑰。以 Google 帳戶為例，電腦要 Windows 10、macOS Ventura 以上，手機要 Android 9、iOS 16 以上並開啟螢幕鎖定。瀏覽器要 Chrome 或 Edge 109、Safari 16、Firefox 122 以上，iPhone 與 Mac 要開啟 iCloud 鑰匙圈。密碼金鑰建立後可能要 7 天才能用來登入，說明頁有正體中文版。
