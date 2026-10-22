---
title: Android 17 裝置端 AI 的隔離執行環境 AISeal
description: Google 10 月 7 日說明 Android 17 的 AISeal，把裝置端 AI 使用的個人資料放進跟作業系統隔離的受保護虛擬機器。依公告，第一階段推出的是個人資料的儲存，模型推論與 AI 代理程式要等之後。到 10 月 20 日為止，Google 沒有公布哪些機型、哪些地區已經啟用，Google 的公告與說明頁沒有提到使用者需要調整的設定。
date: 2026-10-24T00:00:00+08:00
slug: android-aiseal-on-device-ai
categories:
  - mobile
sources:
  - title: Android's Next-Gen Enclave for On-Device AI
    url: https://blog.google/security/enabling-the-next-gen-enclave-architecture-for-on-device-ai-on-android/
    publisher: Google
    date: 2026-10-07
  - title: Android Virtualization Framework (AVF) overview
    url: https://source.android.com/docs/core/virtualization
    publisher: Android Open Source Project
  - title: Security
    url: https://source.android.com/docs/core/virtualization/security
    publisher: Android Open Source Project
  - title: Android’s pKVM Becomes First Globally Certified Software to Achieve Prestigious SESIP Level 5 Security Certification
    url: https://blog.google/security/android-pkvm-certified-sesip-level-5/
    publisher: Google
    date: 2025-08-12
  - title: core/java/android/aiseal - platform/frameworks/base - Git at Google
    url: https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-17.0.0_r1/core/java/android/aiseal/
    publisher: Android Open Source Project
  - title: Private Compute Services
    url: https://github.com/google/private-compute-services
    publisher: Google
  - title: Gemini Nano
    url: https://developer.android.com/ai/gemini-nano
    publisher: Android Developers
  - title: Android On-Device AI Gets a Security Bump With "Next-Gen" Enclaves
    url: https://www.privacyguides.org/news/2026/10/09/android-on-device-ai-gets-a-security-bump-with-next-gen-enclaves/
    publisher: Privacy Guides
    date: 2026-10-09
  - title: Google is building a “black box” for Android AI, but the agents aren’t inside yet
    url: https://www.digitaltrends.com/phones/google-is-building-a-black-box-for-android-ai-but-the-agents-arent-inside-yet/
    publisher: Digital Trends
    date: 2026-10-08
  - title: Android 17 Built a Sealed Room for On-Device AI
    url: https://blog.logcat.ai/2026/06/25/android-17-built-a-sealed-room-for-on-device-ai/
    publisher: logcat.ai
    date: 2026-06-25
watch:
  - date: 2026-12-15
    note: Google 或手機廠商是否公布啟用 AISeal 的機型與地區、模型推論與 AI 代理程式是否移進 AISeal、AICore 的整合進度
authors:
  - anoni-net
---

Google 10 月 7 日在官方部落格說明 Android 17 的 AISeal（Android on-device AI seal），把裝置端 AI 會用到的個人資料，放進一個跟 Android 作業系統隔離的受保護虛擬機器。依公告，設計目標是即使整個作業系統被入侵，個人資料仍然維持加密隔離。第一階段推出的只有個人資料的儲存，模型推論與 AI 代理程式（代替使用者執行多步驟工作的 AI）要等之後。到 10 月 20 日為止，Google 沒有公布哪些機型、哪些地區已經啟用，Google 的公告與說明頁沒有提到使用者需要調整的設定。

根據公告，AISeal 建立在 Android 虛擬化框架（AVF）與 pKVM 這個虛擬機器管理程式（hypervisor，負責切分與隔離虛擬機器的底層軟體）上。這個受保護的空間在設計上可以同時放三類服務，包括加密的個人資料庫、在裝置上執行的模型推論，以及結合兩者的 AI 代理程式。公告舉的例子是助理在隔離空間裡查詢個人資料庫、摘要行事曆，對外的管控設計成只讓最後的答案回到作業系統，這要等推論移進 AISeal 之後才做得到。Android 開放原始碼專案（AOSP）的說明文件寫到，即使主系統（host，也就是平常執行 App 的 Android）被入侵，主系統也讀不到受保護虛擬機器的記憶體。

晶片端，公告提到 MediaTek 的 Dimensity 9600 Pro 已宣布支援，Qualcomm 的 Snapdragon 也會透過 AVF 支援。pKVM 本身 2025 年取得 SESIP（一套資安評估制度）第 5 級的認證，公告稱這是 ISO 15408 底下最高的弱點測試等級（公告沒有寫 AISeal 本身通過認證）。依 Android 17 標籤的原始碼，AOSP 已經包含 AISeal 的框架。依同一份原始碼，服務預設關閉，要把裝置屬性 `service.aiseal.enable` 設為 1 才會啟用（依本文的推論由手機廠商設定）。

## 導讀觀點 {#perspective}

Android 既有的隔離是 App 沙箱、SELinux 規則，以及 Private Compute Core。根據 Private Compute Services 的說明，Private Compute Core 裡的功能不能直接連網，只能透過一組開源的 API 對外。AISeal 多加的一層是虛擬機器管理程式切出的記憶體隔離。AVF 的安全文件列出，pKVM 在虛擬機器管理程式那一層執行的部分約 1 萬行，整個 Linux 核心約 2,000 萬行（攻擊面小了三個數量級）。

同一份安全文件提到，手機廠商與晶片廠商這些經手供應鏈的業者仍然要被信任，主系統可以影響虛擬機器能不能正常運作。文件也寫到，加密儲存沒有區塊層級的防回溯保護（無法察覺加密資料被換回舊的版本）。這些是 pKVM 與受保護虛擬機器的設計限制，依本文的推論，建立在上面的 AISeal 同樣適用。

分析 Android 17 原始碼的一篇技術部落格提到，資料在存進 AISeal 之前的收集當下主系統仍然看得到。同一篇也提到，AISeal 沒有把資料跟使用者選用的 AI 服務業者隔開。

Android 17 標籤的原始碼顯示，AISeal 的管理介面需要 `signature|privileged` 權限，依本文的推論一般第三方 App 無法取得。開發者可以用的 Gemini Nano 是 Google 的裝置端模型，執行在 AICore 這個負責管理裝置端模型的系統服務裡，公告把 AICore 與 AISeal 的整合寫成未來的計畫。Digital Trends 的報導提醒，晶片支援 AISeal 不代表手機上的助理真的在 AISeal 裡執行，要看手機廠商如何實作。

讀者現在不需要調整任何設定，到 10 月 20 日為止，Google 的公告與說明頁也沒有提到給使用者的開關。可以留意的是 Google 或手機廠商何時公布啟用的機型與地區，以及模型推論與 AI 代理程式什麼時候移進 AISeal。

依 Digital Trends 的提醒推論，之後選購手機時，可以看廠商的規格與說明頁有沒有寫明 AI 功能在 AISeal 裡執行。依前述技術部落格的分析，即使在 AISeal 裡執行，資料收集的當下與使用者選用的 AI 服務業者仍然不在隔離的範圍內。
