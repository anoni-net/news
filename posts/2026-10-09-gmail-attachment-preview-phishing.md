---
title: 冒充 Gmail 附件預覽的釣魚信
description: Cisco Talos 揭露一批寄給台灣學術界、智庫與公民社會政策社群的釣魚信。信件用圖片在內文仿製 Gmail 的附件卡片，點下去會在 Windows 電腦上啟動感染。在瀏覽器開啟時假卡片跟真的附件幾乎分不出來，經常收到演講邀請或機構來信的人可以留意。
date: 2026-10-09T00:10:00+08:00
slug: gmail-attachment-preview-phishing
categories:
  - security
sources:
  - title: China-nexus UAT-11587 targets government and policy organizations across Asia with Antino backdoor
    url: https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/
    publisher: Cisco Talos
    date: 2026-09-30
  - title: 中國駭客UAT-11587鎖定臺灣學術界與智庫，以圖片仿製Gmail附件預覽介面並用政府文件作為誘餌
    url: https://www.ithome.com.tw/news/179344
    publisher: iThome
    date: 2026-10-01
  - title: 防範及檢舉網路釣魚電子郵件
    url: https://support.google.com/mail/answer/8253?hl=zh-Hant
    publisher: Google
  - title: 在 Gmail 中開啟及下載附件
    url: https://support.google.com/mail/answer/30719?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 檢查 Gmail 郵件是否通過驗證
    url: https://support.google.com/mail/answer/180707?hl=zh-Hant
    publisher: Google
  - title: Google 最強大的安全防禦機制，可確保私人資訊的安全。
    url: https://landing.google.com/intl/zh-TW/advancedprotection/
    publisher: Google
  - title: 進階保護計畫常見問題
    url: https://support.google.com/accounts/answer/7539956?hl=zh-Hant
    publisher: Google
regions:
  - TW
authors:
  - anoni-net
---

Cisco Talos 在 9 月 30 日公開一份網路間諜活動的報告，代號 UAT-11587。依報告的內容，2026 年 3 月有一批魚叉式網路釣魚信（針對特定對象量身寫成的釣魚信）寄給台灣學術界、智庫與公民社會的政策社群。信件在內文用圖片仿製了 Gmail 的附件預覽，點下去會在 Windows 電腦上啟動感染流程。Talos 寫明，在瀏覽器開啟 Gmail 時，假卡片跟真正的附件預覽在外觀上幾乎分不出來。

Talos 的報告寫到，攻擊者用四張內嵌的 PNG 圖片拼出 Gmail 附件卡片的樣式，再把整張卡片做成連結。連結指向攻擊者控制的 Cloudflare Pages 網址，點下去會下載一個 HTA 檔（由 Windows 的 mshta.exe 執行的程式檔）。接著經過五個階段的感染，最後放入以 Rust 寫成的後門 Antino。過程中會開啟一份 PDF 誘餌文件給受害者看，後門則在背景安裝。

Talos 公布的信件樣本以正體中文寫成，邀請收件者擔任工作坊講師，信中寫課程約 50 分鐘、講師費 3,500 元。Talos 取得的誘餌文件之一是以「Taiwan Information Warfare」為題的工作坊說明，Talos 寫明另一份完整複製了財政部公開的函釋「立法委員行使職務支領之各項費用徵免稅原則」。Talos 也寫到，信件顯示的寄件者冒用收件者信任的機構。

Talos 檢視的一封信用攻擊者自己的網域當信封上的寄件者，通過了 SPF 驗證，但沒有通過 DMARC 驗證。SPF 與 DMARC 都是收件端核對寄件網域的機制。被冒用機構的網域把 DMARC 政策設為不強制執行，所以信件仍然送達。

Talos 從 2025 年 9 月開始觀察 UAT-11587 的活動。到 2026 年 7 月為止，Talos 找到至少 16 個受害或被鎖定的機構，約 350 個受感染的端點（電腦或伺服器）。Talos 以中到高信心評估，鎖定的對象分布在台灣、印度、菲律賓、柬埔寨、巴基斯坦、泰國、緬甸與敘利亞八國，包括政府、外交、國防、立法機關、智庫、大學與公民社會組織。Talos 也以高信心評估攻擊者與中國有關聯（原文為 China-nexus）。

## 導讀觀點 {#perspective}

Talos 的報告寫到，Gmail 在瀏覽器顯示信件時照實呈現了攻擊者寫的 HTML，所以內文裡的圖片可以長得跟附件卡片一樣。iThome 的報導寫到假卡片放在郵件本文下方，Gmail 說明頁寫的真正附件則在郵件底部。本文推論兩者都在信件下半部，單看位置不容易分辨。依 Gmail 說明頁，游標懸停在真正的附件上時，會出現「下載」與「新增至雲端硬碟」的圖示。

本文從說明頁寫的懸停圖示推論，游標懸停在卡片上卻沒有出現「下載」與「新增至雲端硬碟」圖示的，可能只是內文裡的圖片連結。本文沒有實測，Gmail 改版後也可能不適用。推論只適用於電腦版，Talos 的報告沒有寫手機上的顯示狀況。Gmail 說明頁另外建議在電腦上點連結前先懸停查看網址，網址跟說明不相符時，連結可能導向網路釣魚網站。

依 Gmail 說明頁，點寄件者名稱下方的向下箭頭時，通過驗證的郵件會顯示「寄件者」與「簽署者」兩個標頭和對應的網域。沒有通過驗證時，寄件者名稱旁會出現問號。說明頁寫明郵件通過 SPF 或 DKIM 任一項就算通過驗證，Talos 檢視的那封信 SPF 通過，本文推論可能不會出現問號。

展開後的「寄件者」標頭（英文介面為 Mailed by，跟信件頂端的寄件者名稱不同）顯示寄送郵件的網域，本文推論可以比對它跟信中自稱的機構是否一致。到 10 月 7 日為止，說明頁沒有寫 DMARC 驗證失敗的信件會如何顯示。

經常收到演講邀請、公文或機構來信的人，可以特別留意假附件卡片的手法。收到可疑的信時，電腦版 Gmail 可以在「回覆」圖示旁的「更多」選單按「回報為網路釣魚郵件」。

依 Google 的說明，容易成為針對性線上攻擊目標的人可以註冊「進階保護計畫」，到 10 月 7 日為止免費使用。登入時一律要用密碼金鑰或安全金鑰，Chrome 下載檔案前也會做更嚴密的檢查。代價是要準備密碼金鑰或另外購買安全金鑰，使用應用程式密碼的第三方應用程式會被封鎖。到 10 月 7 日為止，Google 的說明頁沒有寫進階保護計畫能否擋下內文裡的假附件卡片。
