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
  - title: Banks in Singapore to Strengthen Resilience Against Phishing Scams
    url: https://www.mas.gov.sg/news/media-releases/2024/banks-in-singapore-to-strengthen-resilience-against-phishing-scams
    publisher: Monetary Authority of Singapore
    date: 2024-07-09
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: Dangerzone
    url: https://github.com/freedomofpress/dangerzone
    publisher: Freedom of the Press Foundation
authors:
  - anoni-net
---

Freedom of the Press Foundation（FPF）的數位安全訓練團隊 8 月 27 日在專欄回答讀者的提問，整理 AI 被用在釣魚攻擊的研究。釣魚訊息不只出現在 Email，也會透過簡訊、QR code、語音與視訊通話送達。FPF 的結論是，AI 讓釣魚訊息更有說服力，個人該做的防禦卻沒有改變。FPF 列出的做法適用於每個收得到這類訊息的人。

FPF 引用了幾份報告的數字。KnowBe4 估計 2025 年 10 月到 2026 年 3 月之間，用到 AI 的釣魚攻擊增加約 86%。Verizon 2026 年的資料外洩調查報告中，約 44% 被偵測到的事件裡，攻擊者用生成式 AI 製作釣魚誘餌當作入侵的第一步。Microsoft 2025 年的報告寫到，AI 自動化的釣魚信點擊率是 54%，一般的釣魚信是 12%。

研究列出的手法包括自動蒐集目標的資料、寫出更個人化的內容，以及在主旨等地方做細微變化來躲過偵測，也能寫出多種語言的版本。收到的信因此看起來像是專門寫給收件人，例如冒充同事，或提到收件人可能出席的公開活動。

FPF 列出四個警訊：寄件地址跟冒充的對象對不上、連結指向跟服務無關的網址、訊息製造壓力或急迫感，以及不請自來的附件。連結可以不點，改成自行輸入網址前往。可疑的附件可以先用 Google 雲端硬碟預覽，或用 Dangerzone 轉成安全的副本。FPF 的文章也寫到，應開啟兩步驟驗證。

## 導讀觀點 {#perspective}

大型語言模型擅長模仿特定的語氣與用字，靠錯字或生硬翻譯辨認詐騙信的做法會越來越不可靠，中文的釣魚信也可能寫得一樣通順。FPF 的四個警訊都不看文字寫得好不好，看的是寄件地址、網址、情緒與附件，文字變得通順之後仍然適用。

驗證碼本身也可能被騙走。新加坡金融管理局 2024 年 7 月宣布，主要零售銀行在三個月內停用登入用的一次性密碼（OTP），已啟用手機數位 token 的客戶改用 token 登入。理由是詐騙集團能架設仿冒的銀行網站騙取 OTP。Google 的說明頁也寫到，密碼金鑰（passkey）無法分享、複製或意外交給他人，比傳統密碼更能防範網路釣魚。

現在能做的第一步，是替最重要的帳號建立密碼金鑰，Email 帳號通常是第一個。以 Google 帳戶為例，電腦要 Windows 10、macOS Ventura 以上，手機要 Android 9、iOS 16 以上。iPhone 與 Mac 要先開啟 iCloud 鑰匙圈。說明頁有正體中文版，新增密碼金鑰不會移除帳戶原本的驗證與救援方式。

經常需要開啟陌生附件的人，可以考慮 Dangerzone。它以 AGPL-3.0 授權，7 月發布 0.11.0，支援 Windows、macOS 與 Linux。介面只有英文，Windows 版還需要電腦支援並開啟硬體虛擬化。Dangerzone 在沒有網路的沙箱裡把文件轉成像素，再重建成 PDF。代價是轉出來的檔案沒有文字層，要另外開啟 OCR 才能搜尋與複製文字。
