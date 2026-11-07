---
title: 荷蘭 ASN Bank 的 Wero 付款與 Play Integrity 檢查
description: 依使用者回報，荷蘭 ASN Bank 的 Android App 1.36.3 版（10 月中更新）起在 GrapheneOS 這類沒有 Google 認證的系統上不時擋下 Wero 付款，App 仍可開啟、查看帳戶。到 11 月 8 日本文查不到 ASN 的公告。打算改用 GrapheneOS 的人，可以把它當成銀行付款功能改用 Google 檢查的例子。
date: 2026-11-10T00:00:00+08:00
slug: asn-bank-grapheneos
categories:
  - finance
regions:
  - NL
sources:
  - title: ASN Bank
    url: https://github.com/PrivSec-dev/banking-apps-compat-report/issues/105
    publisher: GitHub
  - title: SNS Bank (De Volksbank) / ASN / Wero
    url: https://github.com/PrivSec-dev/banking-apps-compat-report/issues/1137
    publisher: GitHub
    date: 2026-10-21
  - title: Sneller bestellen en betalen met iDEAL | Wero
    url: https://www.asnbank.nl/asn-app-en-asn-online-bankieren/veilig-bankierennew/sneller-bestellen-en-betalen-met-ideal-wero.html
    publisher: ASN Bank
  - title: Integrity verdicts | Play Integrity | Android Developers
    url: https://developer.android.com/google/play/integrity/verdicts
    publisher: Android Developers
  - title: Attestation compatibility guide | Articles | GrapheneOS
    url: https://grapheneos.org/articles/attestation-compatibility-guide
    publisher: GrapheneOS
  - title: Usage guide | GrapheneOS
    url: https://grapheneos.org/usage#banking-apps
    publisher: GrapheneOS
  - title: Banking Applications Compatibility with GrapheneOS
    url: https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/
    publisher: PrivSec
    date: 2022-01-26
  - title: IDeal eind 2027 volledig vervangen door nieuw betalingssysteem Wero
    url: https://www.security.nl/posting/883786
    publisher: Security.nl
    date: 2025-04-11
watch:
  - date: 2026-12-10
    note: ASN Bank 或 Wero 的營運方 EPI 是否讓 GrapheneOS 等未經 Google 認證的系統使用 Wero 付款，是否發布官方說明
authors:
  - anoni-net
---

依使用者在 GitHub 上一個銀行 App 相容性回報專案的留言，荷蘭 ASN Bank 的 Android App 從 10 月中更新的 1.36.3 版起，在 GrapheneOS（以 Android 開源程式碼為基礎的隱私強化手機系統）這類沒有經過 Google 認證的系統上不時擋下 Wero 付款。到 11 月 8 日本文查不到 ASN 的公告，說法都來自使用者貼出的客服與申訴回信。目前的回報只涉及 ASN 與同屬 de Volksbank 的 SNS Bank，一位 SNS Bank App 使用者寫 App 仍可開啟、查看帳戶，只是無法用 Wero 付款。荷蘭以外的讀者不會直接遇到，打算改用 GrapheneOS 的人可以把它當成銀行付款功能改用 Google 檢查的例子。

iDEAL 是荷蘭網路購物常用的付款方式，依 Security.nl 2025 年 4 月引述 Wero 的營運方 EPI（European Payments Initiative）對荷蘭《AD》報的說法，iDEAL 要在 2027 年底前完全由 Wero 取代。Wero 整合在各家銀行的 App 裡，也有獨立的 App。ASN 的說明頁寫 2026 年起 iDEAL 逐步改成 Wero，網路商店上會看到「iDEAL | Wero」的名稱。

PrivSec 的相容性名單把 ASN 寫成「ASN Bank (De Volksbank)」，回報的使用者也說 ASN 與 SNS Bank 是同一套 App 換了品牌。依使用者回報，被擋時 App 顯示的訊息用的是「iDEAL | Wero」這個名稱，內容是手機或 App 的安裝不符合銀行的安全要求。同一版也有人付款成功，有人回報時好時壞。回報者把新舊兩條流程分開描述，一位使用者寫舊的 iDEAL | Wero 流程可以付款，新的 Wero 流程則過不了 Play Integrity（Google 提供給 App 檢查裝置與系統的服務）。

依使用者貼出的 ASN IT 支援回覆，GrapheneOS 不支援 Wero，裝置須符合 Wero 的安全要求。多位使用者貼出的申訴回信內容幾乎相同。信中的理由是 iDEAL | Wero 使用一般作業系統的標準安全檢查，替代系統略過或取代了這些內建防護，所以 iDEAL | Wero 不保證交易安全。回信也寫 ASN 正與 iDEAL | Wero 研究未來是否支援替代作業系統，目前無法承諾。

使用者也去信 EPI。依使用者轉貼的回信，EPI 目前集中支援使用最廣的行動銀行平台與裝置。信中也寫，此做法可能排除不用行動銀行的人，以及偏好 Apple 與 Android 生態系以外系統與裝置的人。到 11 月 8 日本文查不到這幾封信的公開版本。

## 導讀觀點 {#perspective}

依 Android 開發者文件，Play Integrity 回傳的判定分成幾個等級。基本完整性（MEETS_BASIC_INTEGRITY）只要求通過基本的系統完整性檢查，bootloader（開機載入程式）可以解鎖，裝置也可以沒有經過認證。裝置完整性（MEETS_DEVICE_INTEGRITY）要求 App 在真正且經過認證的 Android 裝置（genuine and certified Android device）上執行，Android 13 起還要有硬體證明 bootloader 已鎖、載入的是經過認證的製造商映像檔。文件裡沒有出現 GrapheneOS，本文依裝置完整性的條件推論，未經 Google 認證的系統拿不到這項判定。

GrapheneOS 的使用說明也寫，它通過基本的完整性檢查，但沒有經過 Google 認證。GrapheneOS 不打算繞過檢查，理由是檢查一改進就會再失效。

ASN 要求哪一個等級，本文查不到官方資料。一位用 LineageOS（另一套未經認證的 Android 系統）的使用者回報基本完整性通過、裝置完整性未通過，只有 Wero 轉帳不能用（單一案例）。依使用者回報（未經銀行證實），Triodos 與 N26 的 App 在 GrapheneOS 上可以用 Wero 付款，bunq 可以設定 Wero。

依使用者轉貼的內容，EPI 在後來的另一封回信裡說明採用 Play Integrity 的理由。信中寫 Android 的硬體金鑰證明（hardware key attestation）可以驗證一組金鑰是在 TEE、StrongBox 這類跟一般系統隔開的硬體環境裡產生，而且沒有離開那裡，但驗證不了呼叫的 App 與執行中的作業系統是否完整。Play Integrity 把裝置、系統與 App 的訊號合在一份有簽章的權杖裡，由後端伺服器驗證。信中的結論是硬體金鑰證明單獨提供不了 EPI 的風險與詐騙模型需要的驗證。

GrapheneOS 則在相容性指南裡主張銀行改用標準的 Android 硬體證明 API，把 GrapheneOS 公開的官方簽章金鑰列進允許清單。依指南，這套 API 可以驗證硬體、韌體、作業系統與 App，產生的金鑰憑證帶有 App 的 ID、簽章金鑰指紋、版本號與系統的驗證開機金鑰指紋。指南的評估是硬體證明比 Play Integrity 更強，不必依賴 Google Play 服務與 Google 的伺服器，也提到 Play Integrity 最高的強完整性（MEETS_STRONG_INTEGRITY）等級本身就建立在硬體金鑰證明上。兩邊對同一套 API 能驗證到哪裡的說法不同，本文沒有查證哪一方正確。

只有一位使用者寫舊流程可以付款，其他人的回報時好時壞，本文推論不宜把它當成穩定的做法。多位使用者已經向 ASN 與 EPI 申訴，GrapheneOS 也在指南裡鼓勵使用者寫信給 App 開發者並附上指南連結。

打算改用 GrapheneOS 的人，可以先查常用的銀行與支付 App 在 PrivSec 相容性名單上的狀況。名單由社群回報、GrapheneOS 官方不保證內容，也收錄台灣多家銀行與支付 App。到 11 月 8 日，名單上 ASN 那一項仍沒有附註（名單最後更新在 10 月 20 日，比第一則 Wero 回報早一天），App 更新之後名單可能還沒跟上。

本文的推論是，也可以另外保留一支經過 Google 認證的手機只用來付款，有使用者提到自己有備用手機、受到的影響較小。代價是多一支裝置要更新與保管，那支手機上的付款仍要通過 Google 的檢查。
