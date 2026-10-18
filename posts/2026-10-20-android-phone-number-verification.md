---
title: Android 的自動電話號碼驗證與多帳號連結
description: Android 手機預設會自動驗證電話號碼，並把號碼加到這支手機登入的每一個 Google 帳號，包括工作帳號與次要帳號。可以在設定裡關閉驗證，依 Android Authority 的報導，已加入的號碼仍要到各個帳號逐一移除。到 10 月 18 日為止，沒有看到 Google 的公開回應。
date: 2026-10-20T00:00:00+08:00
slug: android-phone-number-verification
categories:
  - tracking
sources:
  - title: 在裝置上管理電話號碼驗證
    url: https://support.google.com/android/answer/7521240?hl=zh-Hant
    publisher: Android 說明
  - title: "PSA: Google is silently linking your phone number across all signed-in accounts"
    url: https://www.androidauthority.com/google-auto-phone-number-verification-android-3723117/
    publisher: Android Authority
    date: 2026-10-14
  - title: 變更帳戶中的電話號碼與其用途
    url: https://support.google.com/accounts/answer/3463280?hl=zh-Hant
    publisher: Google 帳戶說明
  - title: 瞭解 Google Play 服務運用簡訊和多媒體訊息的方式
    url: https://support.google.com/android/answer/10641045?hl=zh-Hant
    publisher: Android 說明
  - title: 瞭解 Google Play 服務運用通話記錄的方式
    url: https://support.google.com/android/answer/10635223?hl=zh-Hant
    publisher: Android 說明
  - title: Google 隱私權政策
    url: https://policies.google.com/privacy?hl=zh-TW
    publisher: Google
    date: 2026-10-16
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
watch:
  - date: 2026-11-18
    note: Google 是否回應 Android Authority 的詢問，Android 說明頁對電話號碼驗證的預設與連結範圍是否修改
authors:
  - anoni-net
---

Android Authority 10 月 14 日報導，Android 手機會自動驗證電話號碼，並把號碼加到這支手機登入的每一個 Google 帳號（包括工作帳號與次要帳號）。Google 的 Android 說明頁「在裝置上管理電話號碼驗證」寫到，這項功能預設開啟，適用於目前與日後登入的帳號與號碼。依報導，說明頁在 2025 年 8 月到 10 月之間加入預設開啟的寫法，本文查不到說明頁的舊版可以對照。報導已向 Google 詢問，到 10 月 18 日為止沒有看到 Google 的公開回應。

只要在 Android 手機登入 Google 帳號，號碼都會加進帳號。同一支手機登入多個帳號的人，帳號之間也會因此用同一個號碼連在一起。依同一份說明頁，驗證是為了讓用電話號碼登入、帳號救援、緊急定位、尋找遺失的裝置、RCS（新一代的簡訊格式）訊息與快速分享（Quick Share）等功能正常運作。Google 與電信業者會定期重新驗證，電信業者可能收取費用。

另外兩份 Google Play 服務的說明頁提到，Google Play 服務可能在背景傳送及存取簡訊、存取通話記錄，用來找出並驗證號碼。這兩頁的英文版寫 `If you opt-in to phone number verification`（使用者主動選擇加入），正體中文版譯成「如果您啟用電話號碼驗證功能」。這個寫法跟預設開啟的說法不一致，頁面沒有說明差別。

號碼加進帳號之後的用途，Google 帳戶說明頁「變更帳戶中的電話號碼與其用途」列出三類。第一類是登入與帳號救援，第二類是讓別人透過 Google 服務找到並聯絡你，第三類是在「更實用的廣告和 Google 服務」開啟時用來顯示更貼近需求的廣告。10 月 16 日生效的 Google 隱私權政策列了相同的用途，帳戶說明頁也提到 Google 不會販售包括電話號碼在內的個人資訊。

裝置的說明頁也提到，電話號碼驗證開啟時會一併開啟「Google 強化分享模式」，方便別人透過這個號碼傳送照片與發起視訊通話。同一支手機有多個帳號時，這個模式只對其中一個帳號開啟。

## 導讀觀點 {#perspective}

同一支手機登入的多個帳號，常見的是私人帳號與工作帳號，或刻意跟真實身分分開使用的帳號。依說明頁的範例，新增的 Google 帳號會連結裝置上所有的號碼，新加入的號碼也會加到所有帳號。台灣的《行動寬頻業務管理規則》第 77 條（2019 年 9 月修正）要求行動寬頻業者登錄使用者的姓名、住址與兩種身分證明文件號碼，預付卡也一樣，有關機關依法查詢時業者要提供。依本文的推論，號碼加進帳號之後，能同時取得 Google 帳號資料與電信業者登記資料的一方（例如依法查詢的機關）就能把帳號對應到門號登記的身分。

依 Google 說明頁，帳號救援、用電話號碼登入、緊急定位等功能依賴驗證，關閉之後這些功能可能受影響（本文依說明頁的推論）。Google 隱私權政策把電信業者名稱與電話號碼列在蒐集的行動網路資訊裡。依這份清單，本文推論關閉驗證、移除號碼後，Google 仍可能取得這支手機的號碼。Google 內部會不會因此把帳號連起來，本文查不到。

在同一支 Android 手機登入多個帳號、不想讓帳號之間用號碼連在一起的人，可以到「設定」的「Google」、「所有服務」，在「隱私權與安全性」下方的「驗證電話號碼」關閉。報導寫到，關閉只會停止之後的連結，已加入的號碼要到每個帳號的「個人資訊」、「電話」逐一刪除（Google 的說明頁沒有寫關閉後是否會移除）。需要用這個號碼救援的那個帳號可以保留，只從不想連在一起的帳號移除（本文的推論）。裝置設定與 Google 帳戶這兩份說明頁都有正體中文版，頁尾標註可能含有 AI 翻譯的內容。

報導引述 Reddit 上的使用者回報，提到關閉後開關會自己恢復，報導作者到發布時沒有重現。依這些回報，本文建議關閉之後隔一段時間再回頭確認。
