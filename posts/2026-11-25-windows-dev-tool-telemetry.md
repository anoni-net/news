---
title: Windows 11 診斷資料裡的 coding agent 與開發工具紀錄
description: 一位研究者在一台 Windows 11 虛擬機上實測，系統元件會記錄執行過哪些 coding agent 與哪幾類開發工具，紀錄歸在選用診斷資料並排進了上傳佇列。選用診斷資料可以在設定裡關閉，必要診斷資料的清單另列有一筆判斷是否為開發者的分群事件，Microsoft 沒說明它與上述紀錄的關係。
date: 2026-11-25T00:00:00+08:00
slug: windows-dev-tool-telemetry
categories: [tracking]
watch:
  - date: 2026-12-22
    note: Microsoft 是否說明 Segments.SubCohorts 的用途與啟用範圍，是否有人公開關閉選用診斷資料之後的實測
sources:
  - title: Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use
    url: https://xusheng.dev/posts/windows-coding-agent-telemetry/
    publisher: xusheng.dev
    date: 2026-11-16
  - title: Windows 11, versions 25H2 and 24H2 required diagnostic data events and fields
    url: https://learn.microsoft.com/en-us/windows/privacy/required-diagnostic-events-fields-windows-11-24h2
    publisher: Microsoft
  - title: Configure Windows diagnostic data in your organization
    url: https://learn.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization
    publisher: Microsoft
  - title: Diagnostics, feedback, and privacy in Windows
    url: https://support.microsoft.com/en-us/windows/diagnostics-feedback-and-privacy-in-windows-28808a2b-a31b-dd73-dcd3-4559a5199319
    publisher: Microsoft
  - title: Diagnostic Data Viewer
    url: https://learn.microsoft.com/en-us/windows/privacy/diagnostic-data-viewer-overview
    publisher: Microsoft
  - title: 診斷資料檢視器
    url: https://learn.microsoft.com/zh-tw/windows/privacy/diagnostic-data-viewer-overview
    publisher: Microsoft
authors:
  - anoni-net
---

Windows 11 的診斷資料除了當機紀錄與硬體資訊，還可能包括使用者執行過哪些 coding agent（替使用者撰寫、修改程式碼的 AI 工具）與開發工具。一位研究者 11 月 16 日在個人部落格發表逆向工程（拆解程式、還原它如何運作）與實測的結果，在一個系統元件裡找到 `codex.exe`、`claude.exe`、`copilot.exe`、`cursor.exe` 等 coding agent，以及 `python.exe`、`gcc.exe` 等開發工具的執行檔名稱。元件比對程式執行時的檔名，讀者可以從自己平常執行哪些程式判斷是否相關。coding agent 的檢查只在研究者自己的一台虛擬機上實測，其他電腦是否開啟，他沒有驗證。

依研究者的分析，名為 `MissionControlAggregator` 的元件讀取 Windows 原本就有的程式啟動紀錄，比對成功就在一組位元（bitmap，每個位置只記有或沒有）裡標記。coding agent 逐一記錄，開發工具只記到類別，例如 GCC 與 Clang 屬於同一類。研究者的判讀是，來源紀錄裡的執行時間與互動次數看起來沒有被保留。他沒有在事件裡找到提示詞或原始碼，但認為光是記錄一個人用哪些工具，就有明顯的隱私影響。

Windows 的診斷資料分成必要與選用兩級，依 Microsoft 的支援頁，使用者第一次設定 Windows 時可以選擇是否傳送選用診斷資料。研究者另外用最新的官方映像檔全新安裝一台美國地區設定的 Windows 11 Home，在改任何隱私設定之前，選用資料的開關已經是開啟的。新裝的那台只用來看開關的預設值，他沒有檢查它是否啟用 coding agent 的紀錄。

coding agent 的檢查在研究者的虛擬機上已經啟用，他沒有手動開啟。在允許選用資料的設定下，他在 Windows 的上傳佇列（等待送出的診斷資料暫存區）裡找到工具使用的紀錄，紀錄標為選用資料。原文的結論是資料會上傳到 Microsoft，他列出的證據到排進上傳佇列為止，沒有實際送出的連線紀錄。

## 導讀觀點 {#perspective}

Microsoft 給組織的設定說明裡，選用診斷資料包括應用程式的使用情形，例如啟動了哪些程式、執行多久。同一份說明把完全不送診斷資料的選項只開放給 Windows Server、Enterprise 與 Education，照這份說明整理，Home 與 Pro 的使用者無法關閉必要資料。Microsoft 公開的必要診斷資料清單裡，另列有一筆依應用程式的使用情形、回報使用者是否為開發者（IsDeveloper）的分群事件 `Segments.Cohorts`，跟研究者抓到、歸在選用資料的紀錄是不同的事件。Microsoft 沒有寫判定方式，也沒有說明兩者是否相關。

想確認自己的電腦送出哪些診斷資料的人，可以從 Microsoft Store 安裝診斷資料檢視器（Diagnostic Data Viewer），再到「設定 > 隱私權與安全性 > 診斷與意見反應」（Settings > Privacy & security > Diagnostics & feedback）打開「開啟診斷資料檢視器」的開關。開啟之後 Windows 會把診斷資料存在本機、直到關閉為止，預設最多占用系統磁碟 1 GB，說明頁上的建議因此是看完就關閉。說明頁上也寫了，開啟後要照常使用幾天再回來看，檢視器列出的事件也不一定已經上傳。研究者抓到的工具使用紀錄是否會列在檢視器裡，到 11 月 22 日還沒有人公開驗證。

平常在 Windows 11 執行開發工具或 coding agent、不想讓工具紀錄成為診斷資料一部分的人，可以關閉「診斷資料」底下傳送選用資料的開關（英文介面為 Send optional diagnostic data）。開關在同一個設定頁，新安裝時也可以在設定流程中拒絕，地區不是美國的讀者可以直接到設定頁看開關目前的狀態。

研究者抓到的紀錄標為選用，依這個標記，關閉之後它應該不會再排進上傳佇列。Microsoft 的支援頁寫到，不送選用資料的裝置一樣安全，也會正常運作。原文沒有做關閉選用資料之後的對照實驗，Microsoft 的公開頁面也沒有寫工具使用紀錄的用途。
