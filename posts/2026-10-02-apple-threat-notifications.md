---
title: Apple 威脅通知的辨識與應對
description: Apple 8 月向 110 個國家的使用者發出傭兵間諜軟體的威脅通知，絕大多數人不會成為這類攻擊的目標。說明頁寫明真正的通知出現在哪裡、不會要求密碼與驗證碼，收到之後可以開啟封閉模式並尋求協助。
date: 2026-10-02T00:00:00+08:00
slug: apple-threat-notifications
sources:
  - title: About Apple threat notifications and protecting against mercenary spyware
    url: https://support.apple.com/en-us/102174
    publisher: Apple
    date: 2026-08-13
  - title: Really, pay attention to Apple’s threat notifications
    url: https://freedom.press/digisec/blog/really-pay-attention-to-apples-threat-notifications/
    publisher: Freedom of the Press Foundation
    date: 2026-09-02
  - title: If Apple sends you a push notification alerting you to a spyware attack, take it seriously
    url: https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/
    publisher: TechCrunch
    date: 2026-08-13
  - title: About Lockdown Mode
    url: https://support.apple.com/en-us/105120
    publisher: Apple
    date: 2026-09-14
  - title: Apple says no one using Lockdown Mode has been hacked with spyware
    url: https://techcrunch.com/2026/03/27/apple-says-no-one-using-lockdown-mode-has-been-hacked-with-spyware/
    publisher: TechCrunch
    date: 2026-03-27
  - title: Digital Security Helpline
    url: https://www.accessnow.org/help/
    publisher: Access Now
  - title: Apple warns Indian opposition leaders of state-sponsored iPhone attacks
    url: https://techcrunch.com/2023/10/30/indian-opposition-leaders-says-apple-has-warned-them-of-state-sponsored-iphone-attacks/
    publisher: TechCrunch
    date: 2023-10-31
  - title: 關於封閉模式
    url: https://support.apple.com/zh-tw/105120
    publisher: Apple
    date: 2026-09-18
  - title: 關於 Apple 威脅通知與防範傭兵間諜軟體
    url: https://support.apple.com/zh-tw/102174
    publisher: Apple
    date: 2026-08-13
authors:
  - anoni-net
---

Apple 在 8 月 13 日向 110 個國家的使用者發出威脅通知，告知他們的 iPhone 成為傭兵間諜軟體（民間公司替政府開發的間諜軟體，例如 NSO Group 的 Pegasus）的攻擊目標。Apple 從 2021 年起每年發出多次通知，到 8 月 13 日為止涵蓋 150 多個國家或地區。Apple 的說明頁也寫到，絕大多數人不會成為這類攻擊的目標。

新聞自由組織 Freedom of the Press Foundation（FPF）9 月 2 日在電子報提醒讀者認真看待這類通知。Apple 2026 年 8 月更新的說明頁也寫明通知是可信度極高的警示，應嚴肅看待，但調查無法完全保證。FPF 轉述非營利組織 Access Now 的解說，通知不會交代攻擊是否成功與攻擊者是誰。Apple 也不指明攻擊者或地區，發出通知的原因同樣不公開。

Apple 的說明頁寫明，通知會出現在 iPhone 的鎖定畫面與「設定」裡，同時寄到 Apple 帳號綁定的 Email。2026 年起的寄件者是 `threat-notifications@email.apple.com`。登入 `account.apple.com` 後，頁面頂端也會出現橫幅。通知形式依機型與系統版本而異。

Apple 建議收到通知的人開啟封閉模式（限制部分功能以降低入侵風險的模式），並尋求專家協助，例如 Access Now 全年無休的數位安全求助專線。FPF 也建議 Android 使用者了解類似的「進階保護」功能。

## 導讀觀點 {#perspective}

真正的通知會建議開啟封閉模式等措施，但不會要你點連結、開檔案、安裝 App 或描述檔，也不會索取密碼與驗證碼。收到自稱來自 Apple 的可疑訊息時，不要點連結，自行登入 `account.apple.com` 確認有沒有橫幅。

到 9 月 29 日為止，Access Now 的說明頁寫明專線在兩小時內回覆。專線的十種語言包括英文、西班牙文、他加祿文與阿拉伯文，但沒有中文。中文使用者可以用英文聯絡，或先找熟悉數位安全的在地團體協助。

2023 年 10 月有一批通知寄到印度。Apple 當時給 TechCrunch 的聲明寫到可能有誤報，也可能漏掉部分攻擊。現行說明頁已不提誤報。

TechCrunch 訪問的資安研究者提到，封閉模式擋掉多數訊息附件類型並限制網頁引擎 WebKit，尤其縮小了零點擊攻擊（無需受害者操作）可利用的範圍。Apple 在 3 月 27 日給 TechCrunch 的回覆寫到，沒有發現開啟封閉模式的裝置遭傭兵間諜軟體攻破。同一篇報導也寫到，不排除有未被發現的繞過手法。

代價是除了特定影像、視訊和音訊，大部分訊息附件都會被阻擋，連結與連結預覽也無法使用。部分網站可能無法正常運作。信任的網站與 App 可以排除在外，但會降低防護。

封閉模式需要 iOS 16 以上，位置在「設定」的「隱私權與安全性」，開啟時手機會重新開機。iPad 與 Mac 要分別開啟，配對的 Apple Watch 會跟著 iPhone 開啟。正體中文介面的名稱是「封閉模式」。有充分理由擔心自己成為目標的人，不必等收到通知才開啟。
