---
title: Apple 對 Mac「完全取用磁碟」權限的授權預告
description: Apple 10 月 2 日預告之後會讓 Mac 使用者只能透過非常明確的操作授予「完全取用磁碟」權限。理由包括部分開發者的用法可能讓使用者資料暴露，以及 AI 代理程式會讓風險增加。Apple 沒有寫版本與上線時間，到 10 月 12 日為止版本說明都沒有寫到這項控制。
date: 2026-10-15T00:00:00+08:00
slug: apple-full-disk-access
categories:
  - tracking
follows:
  - 2026-10-09-muse-dots-agent-memory-permissions
sources:
  - title: Updates to Full Disk Access in macOS
    url: https://developer.apple.com/news/?id=p6zjojqw
    publisher: Apple
    date: 2026-10-02
  - title: 在 Mac 上更改「隱私權與安全性」設定
    url: https://support.apple.com/zh-tw/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: macOS 27 Golden Gate Release Notes
    url: https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes
    publisher: Apple
  - title: macOS 27.2 Golden Gate Beta 3 Release Notes
    url: https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes
    publisher: Apple
  - title: Meta disputes claim that Muse read a user's private messages without permission
    url: https://techcrunch.com/2026/09/30/meta-disputes-claim-that-muse-read-a-users-private-messages-without-permission/
    publisher: TechCrunch
    date: 2026-09-30
  - title: Meta Pushes Back on Claim That Muse AI Read a User's Messages Without Consent
    url: https://decrypt.co/379868/meta-muse-ai-agent-read-messages-without-permission
    publisher: Decrypt
    date: 2026-10-01
  - title: Apple says it's tightening macOS 'Full Disk Access' controls due to new risks from AI agents
    url: https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/
    publisher: TechCrunch
    date: 2026-10-02
  - title: Apple changes full-disk access permissions to curb abuse from AI agents
    url: https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/
    publisher: Ars Technica
    date: 2026-10-02
  - title: 蘋果將增加macOS完全磁碟存取的開關控制
    url: https://www.ithome.com.tw/news/179400
    publisher: iThome
    date: 2026-10-05
  - title: Apple Tightens "Full Disk Access" Permission on macOS in Light of AI Agent Security Concerns
    url: https://www.privacyguides.org/news/2026/10/06/apple-tightens-full-disk-access-permission-on-macos-in-light-of-ai-agent-security-concerns/
    publisher: Privacy Guides
    date: 2026-10-06
  - title: Meta VP of Communications on X
    url: https://x.com/andymstone/status/2105107596734849423
    publisher: X
    date: 2026-09-30
  - title: "Microsoft Execution Containers: Policy-driven containment for AI agents"
    url: https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/
    publisher: Microsoft
    date: 2026-10-07
  - title: Microsoft eXecution Container (MXC)
    url: https://github.com/microsoft/mxc
    publisher: GitHub
  - title: Muse from Meta App - App Store
    url: https://apps.apple.com/us/app/muse-from-meta/id6760173601
    publisher: App Store
watch:
  - date: 2026-12-15
    note: Apple 預告的完全取用磁碟額外控制是否出現在 macOS 版本說明，介面如何、既有授權是否要重新確認
authors:
  - anoni-net
---

Apple 10 月 2 日在開發者新聞預告，之後會為 macOS 的「完全取用磁碟」加入額外的控制，讓真的想授予這項權限的使用者只能透過非常明確的操作完成。Apple 沒有寫是哪個版本、何時上線、介面長什麼樣子，也沒有寫已經授權的 App 要不要重新確認。到 10 月 12 日為止，macOS 27 與 27.2 第三個測試版的版本說明都沒有寫到這項新控制。

Apple 的預告提到，為了讓備份 App 在 Mac 上正常運作，完全取用磁碟大致繞過了保護使用者資料的其他控制。Apple 也寫到，有些開發者使用這項權限的方式，可能讓使用者在不完全知情下暴露檔案、郵件、訊息甚至瀏覽紀錄。預告也提到，AI 代理程式（能代替使用者操作電腦、讀取檔案與 App 的 AI 程式）越來越能自主行動，這類權限的風險會大幅增加。TechCrunch 的報導發出後補了更正，把原本寫的「限制權限」改成增加知情同意的步驟，並註明這不是新的限制。

預告發出前幾天，依 TechCrunch 與 Decrypt 的轉述，一位專欄作者表示 Meta 的 AI 代理程式 Muse 的 Mac 版在完全取用磁碟關閉時讀到他的私人訊息（10 月 9 日的導讀寫過這件事）。依 Decrypt 的轉述，作者設定時拒絕給訊息權限，之後發現 Muse 已同步了 Mac 本機的訊息資料庫。Meta 傳播副總裁 9 月 30 日在 X 表示，要同時開啟完全取用磁碟與 Muse 內的訊息連接器，Muse 才能讀取訊息。Apple 的預告沒有點名任何 App 或開發者，把兩者寫成互相反駁的，是 Ars Technica 與 iThome 的解讀。

## 導讀觀點 {#perspective}

完全取用磁碟是作業系統層級的權限，Apple 的說明頁介紹它讓 App 取用電腦上所有檔案，包括「郵件」、「訊息」等其他 App 的資料與「時光機」備份。Ars Technica 引述的一位 macOS 資安專家表示，取得這項權限的程式讀得到瀏覽紀錄、瀏覽器 cookie 與聊天內容等檔案。Meta 一位主管則表示，讀取訊息要經過 App 內的權限設定與 macOS 系統層級的保護，即使 App 有錯誤也無法繞過（TechCrunch 的轉述）。Apple 的說明頁與資安專家描述的是取得權限後 App 讀得到什麼，Meta 的說法描述的是 Muse 要經過哪些授權步驟。

Microsoft 10 月 7 日發布的 Microsoft Execution Containers（MXC）是另一種做法。依 Microsoft 的部落格，開發者或 IT 管理者用政策定義 AI 代理程式能讀寫哪些檔案、連到哪些網路，政策放在代理程式能控制的範圍之外。MXC 以 MIT 授權開源，在 macOS 上使用 Seatbelt 沙盒（限制程式能存取哪些資源的機制）。README 的描述是嵌進 App 的套件，Microsoft 列出已支援的工具有 GitHub Copilot、OpenAI Codex 等（名單裡沒有 Muse 或 ChatGPT），本文推論一般使用者不會直接設定它。

Microsoft 與 Apple 的文件都沒有提到對方，本文把兩者並列，差別在由誰把關。Apple 預告的做法是在授權那一刻讓使用者更清楚自己給出了什麼，MXC 則是由開發者事先限定代理程式能碰的範圍。Apple 的預告沒有寫到新控制會不會改變完全取用磁碟能讀到的範圍。之後可以留意 macOS 的版本說明何時出現這項控制，以及已授權的 App 要不要重新確認。

用 Mac 的讀者現在就可以打開「系統設定」的「隱私權與安全性」，在「完全取用磁碟」查看哪些 App 取得了這項權限。看到不認得的 App，可以先查清楚它為什麼需要這項權限，備份類的 App 正是 Apple 預告提到的用途。Apple 的說明頁只寫了加入 App 的步驟，Meta 則表示 Muse 的授權可以隨時撤銷。授權之前可以先想清楚，這項權限讓 App 讀得到別人傳給你的訊息與瀏覽紀錄，這部分的判斷 Apple 的新控制上線之後仍然要由使用者自己做。
