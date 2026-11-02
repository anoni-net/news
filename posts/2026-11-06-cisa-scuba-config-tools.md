---
title: 檢查 Microsoft 365 與 Google Workspace 設定的 CISA 免費工具
description: 美國 CISA 10 月 22 日發布 ScubaGear v2.0.0 與 ScubaGoggles v1.1.0，免費比對組織的 Microsoft 365 與 Google Workspace 設定跟 CISA 的安全基準，產出報告。用得到的是組織的管理員，ScubaGear 只能在 Windows 執行，ScubaGoggles 要用超級管理員帳號。
date: 2026-11-06T00:00:00+08:00
slug: cisa-scuba-config-tools
categories:
  - security
regions:
  - US
sources:
  - title: Release v2.0.0 · cisagov/ScubaGear
    url: https://github.com/cisagov/ScubaGear/releases/tag/v2.0.0
    publisher: GitHub
    date: 2026-10-22
  - title: Release v1.1.0 · cisagov/ScubaGoggles
    url: https://github.com/cisagov/ScubaGoggles/releases/tag/v1.1.0
    publisher: GitHub
    date: 2026-10-22
  - title: Secure Cloud Business Applications (SCuBA) Project
    url: https://www.cisa.gov/resources-tools/services/secure-cloud-business-applications-scuba-project
    publisher: CISA
  - title: "BOD 25-01: Implementing Secure Practices for Cloud Services"
    url: https://www.cisa.gov/news-events/directives/bod-25-01-implementing-secure-practices-cloud-services
    publisher: CISA
    date: 2024-12-17
  - title: ScubaGear/README.md
    url: https://github.com/cisagov/ScubaGear/blob/main/README.md
    publisher: GitHub
  - title: ScubaGoggles/README.md
    url: https://github.com/cisagov/ScubaGoggles/blob/main/README.md
    publisher: GitHub
  - title: Interactive Permissions
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/prerequisites/interactive.md
    publisher: GitHub
  - title: Dependencies
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/prerequisites/dependencies.md
    publisher: GitHub
  - title: Network Access
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/prerequisites/networkaccess.md
    publisher: GitHub
  - title: Assumptions
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/misc/assumptions.md
    publisher: GitHub
  - title: Reports
    url: https://github.com/cisagov/ScubaGear/blob/main/docs/execution/reports.md
    publisher: GitHub
  - title: Prerequisites
    url: https://github.com/cisagov/ScubaGoggles/blob/main/docs/prerequisites/Prerequisites.md
    publisher: GitHub
  - title: Limitations
    url: https://github.com/cisagov/ScubaGoggles/blob/main/docs/usage/Limitations.md
    publisher: GitHub
  - title: Getting started
    url: https://github.com/cisagov/ScubaGoggles/blob/main/docs/installation/DownloadAndInstall.md
    publisher: GitHub
  - title: CISA提供兩款免費工具，協助檢測M365與Google Workspace的安全設定錯誤
    url: https://www.ithome.com.tw/news/180058
    publisher: iThome
    date: 2026-10-29
authors:
  - anoni-net
---

美國網路安全暨基礎設施安全局（CISA）10 月 22 日在 GitHub 發布 ScubaGear v2.0.0 與 ScubaGoggles v1.1.0。兩款都是免費的評估工具，把組織的 Microsoft 365 或 Google Workspace 設定跟 CISA 的安全設定基準逐條比對，再產出報告。用得到的是管理組織租戶（tenant，組織在雲端服務裡的整套帳號與設定）的管理員，沒有組織管理後台的個人帳號不在範圍內。美國聯邦民事機關另有部署這類工具的義務，其他地方的組織可以自行選用。

依 CISA 的約束性指令 BOD 25-01，聯邦民事機關須替已有 CISA 定稿基準的雲端服務部署 SCuBA 的評估工具。指令發布時只有 Microsoft 365 有定稿基準，頁面沒有提到 Google Workspace。

iThome 10 月 29 日報導了這兩次更新。依 CISA 的專案頁，SCuBA（安全雲端商務應用）專案 2022 年成立，2023 年推出這兩款工具。兩個 repo 除另有註明的部分外，以 CC0（放棄著作權、任何人都能自由使用的授權）公開，基準文件也放在同一處。

依 ScubaGear 的 README，工具用 PowerShell 向 Microsoft 365 的 API 查詢設定，再交給 OPA（Open Policy Agent，依規則檔比對資料的政策引擎）比對。比對用的規則照基準文件寫成，結果輸出成 HTML、JSON 與 CSV。基準涵蓋 Entra ID、Exchange Online、Teams、SharePoint 與 OneDrive、Power BI、Power Platform，以及進階威脅防護的 Security Suite。依 ScubaGear 的報告說明，報告存在執行那台電腦的資料夾裡，其中只列未通過強制項目的 `ActionPlan.csv` 可以填寫原因與改善時程。

ScubaGoggles 的做法相近，主要透過 Google Admin SDK 匯出設定與管理記錄，再輸出 HTML 與 JSON 的報告。基準涵蓋 Gmail、雲端硬碟與文件、Meet、日曆、Chat、Classroom、協作平台、群組與 Gemini 等服務。ScubaGear 的 README 寫到控制項已對應 NIST SP 800-53（美國聯邦資訊系統的安全控制目錄）與 MITRE ATT&CK（攻擊手法的分類知識庫），ScubaGoggles 的 README 也列有對照表。

依版本說明，ScubaGear 2.0.0 新增 Power BI 的檢查、一條封鎖高風險 Entra AI 代理程式的政策，以及比較兩次執行結果的功能。ScubaGoggles 1.1.0 新增一條 Meet 的政策與比較功能的初版，Gemini 的基準從 Alpha 改為 Beta。BOD 25-01 要求的設定在 ScubaGoggles 這一版沒有新增、移除或修改。

## 導讀觀點 {#perspective}

雲端辦公服務的設定分散在好幾個管理後台，兩款工具把它們讀出來，集中跟一份公開的規則對照。依 ScubaGear 的網路需求說明，工具透過 HTTPS 連到 Microsoft 的服務讀取租戶設定，報告寫在本機。本文查過的 README 與幾份說明文件裡，沒有寫到把結果自動上傳給 CISA 的機制，程式碼則沒有檢查。依 BOD 25-01 的頁面，機關可以自行把工具的結果接到 CISA 的持續監控方案自動回報，或每季以 CISA 核可的機器可讀格式提交用最新版評估工具產生的結果。

依 ScubaGear 的權限說明，以互動方式登入時，多數產品最低要全域讀取者（Global Reader）角色。角色門檻的例外是 2.0.0 新增檢查的 Power BI 要 Fabric 管理員或全域管理員，Power Platform 則要 Power Platform 管理員。工具向 Microsoft Graph 申請的權限都是讀取類。ScubaGoggles 的前置說明則要求執行者是超級管理員，同意畫面上的範圍多數帶 `readonly`，只有 `apps.licensing` 與 `apps.groups.settings` 兩項沒有。

同一份說明提到 Groups Settings API 本身不提供唯讀範圍，所以改用群組讀取者（Groups Reader）角色搭配委派管理服務帳戶（DASA）限縮權限。兩款工具的說明都只寫評估，但 ScubaGoggles 執行時登入的仍是超級管理員，ScubaGear 檢查 Power BI 與 Power Platform 時也要用管理員角色。依本文的推論，執行工具的電腦與保存的登入憑證，安全程度要比照管理後台。

依 ScubaGoggles 的限制說明，部分檢查要從管理記錄推斷設定，從未改過預設值的設定因此無從判斷。管理記錄也只保留 6 個月，文件提醒這類結果可能漏報，要保留懷疑。ScubaGear 的 README 則提醒，沒有設好 YAML 設定檔時，工具採用的預設值未必符合組織實際的政策。設定檔也可以把組織接受的風險記成排除或註記。

ScubaGear 的假設說明列出，測試用的租戶是 E3、G3 或 E5、G5 的授權組合，部分檢查依賴 Entra ID P2 或 Defender for Office 365。依本文的推論，用較低階方案的小型組織看到未通過的項目時，要先分辨原因出在設定或方案本來就沒有那項功能。

管理組織 Microsoft 365 的人要先準備一台 Windows 電腦，ScubaGear 依賴只有 Windows 版的 PowerShell 5，安裝之後還要下載 OPA 等元件。管理 Google Workspace 的人執行 ScubaGoggles，需要 64 位元系統與 Python 3.11 以上，並在 Google Cloud 專案啟用 Admin SDK 等四個 API。安裝與登入的步驟見兩個 repo 的說明文件。

ScubaGear 的 README 提到，不帶設定檔的第一次執行只會產生現況的報告、不會修改設定，README 也沒有描述自動修改設定的功能。要不要改、先改哪幾項，由管理員依組織的處境判斷。依本文的推論，報告只涵蓋基準列出的設定，帳號是否已被入侵、檔案是否已經外流都不在比對的範圍內。
