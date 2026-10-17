---
title: 開源影像編輯軟體 Compositor 與 AI 生成程式碼的維護和稽核
description: 一位設計師 9 月發布 Mac 上的開源影像編輯軟體 Compositor，免費、不用帳號，作者自述程式全由 AI 寫成。本文讀到的批評集中在「我做的」這個說法，以及 AI 寫的程式碼由誰檢查、誰維護。到 10 月 12 日只支援 Apple 晶片、macOS 26 以上的 Mac。
date: 2026-10-17T00:00:00+08:00
slug: compositor-image-editor
categories:
  - tracking
sources:
  - title: Compositor – The Photoshop alternative for Mac
    url: https://robbietilton.com/compositor
    publisher: Compositor
  - title: Compositor/README.md
    url: https://github.com/robbietilton/Compositor/blob/main/README.md
    publisher: GitHub
  - title: Compositor launch post on X
    url: https://x.com/i/status/2100946395972976843
    publisher: X
    date: 2026-09-18
  - title: Compositor developer's reply on X
    url: https://x.com/i/status/2101334715513106496
    publisher: X
    date: 2026-09-19
  - title: Quote post by a concept artist on X
    url: https://x.com/i/status/2101093572720148574
    publisher: X
    date: 2026-09-18
  - title: Thread by a creative tools developer on X
    url: https://x.com/i/status/2103514110843551887
    publisher: X
    date: 2026-09-25
  - title: Thread by a creative tools developer on X (continued)
    url: https://x.com/i/status/2103514716962501046
    publisher: X
    date: 2026-09-25
  - title: Thread by a creative tools developer on X (follow-up)
    url: https://x.com/i/status/2103523639685738691
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's post on ports on X
    url: https://x.com/i/status/2103520923697733898
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's reply on maintenance on X
    url: https://x.com/i/status/2103519019282358348
    publisher: X
    date: 2026-09-25
  - title: Compositor developer's reply on tracking on X
    url: https://x.com/i/status/2108977298905133319
    publisher: X
    date: 2026-10-10
  - title: Compositor releases
    url: https://github.com/robbietilton/Compositor/releases
    publisher: GitHub
  - title: Add Generative Fill, Remove and Expand (optional, with the user's own Gemini key)
    url: https://github.com/robbietilton/Compositor/pull/58
    publisher: GitHub
    date: 2026-09-21
  - title: Add Enlarger, AI upscaling with Real-ESRGAN
    url: https://github.com/robbietilton/Compositor/pull/73
    publisher: GitHub
    date: 2026-09-22
  - title: Fix unsafe formatting of persisted rotation and hue angles
    url: https://github.com/robbietilton/Compositor/pull/10
    publisher: GitHub
    date: 2026-09-19
  - title: "Feature request: Windows version of Compositor"
    url: https://github.com/robbietilton/Compositor/issues/23
    publisher: GitHub
    date: 2026-09-19
  - title: "FYI: Simplified Chinese localization fork (compositor-cn)"
    url: https://github.com/robbietilton/Compositor/issues/222
    publisher: GitHub
    date: 2026-10-07
watch:
  - date: 2026-12-15
    note: Compositor 是否在 v2 加入 AI 功能、會不會把使用者內容送出電腦，以及是否開放在地化
authors:
  - anoni-net
---

一位設計師 9 月 16 日（UTC）在 GitHub 發布 Mac 上的影像編輯軟體 Compositor，9 月 18 日在 X 公開介紹。軟體以 MIT 授權開源、免費下載，不需要帳號，作者的發布貼文寫起初是為了擺脫 Adobe 的訂閱而做給自己用。到 10 月 12 日為止，最新版是 10 月 11 日（UTC）發布的 1.4.10，只支援搭載 Apple 晶片、macOS 26 以上的 Mac。介面只有英文，作者也暫時不接受翻譯。

發布貼文到 10 月 12 日累積約 240 萬次瀏覽，貼文底下的回覆本文沒有取得，以下只根據 X 上少數公開貼文。一位影視概念設計師引用發布貼文，批評把 AI 寫成的軟體說成「I built」（我做的），認為這類作品都是 vibe coding（用自然語言指示 AI 寫程式）。作者回覆這則貼文時寫「AI wrote every line of this」，也寫「Code was always the painful part, never the important part.」依本文 10 月 12 日統計 GitHub 的 commit（程式碼的每一次修改紀錄），451 個有 282 個帶 AI 程式碼工具的共同作者署名。

另一位開發創作工具的開發者在 X 借這個專案探討 AI 如何改變創作工具的生態，寫這個專案的程式碼「decidedly not for human consumption」，並問作者接下來半年、兩年維護它的誘因在哪裡。作者回覆會繼續維護，因為自己每天都在用。作者只維護 Mac 版，在 X 寫其他人做的 Windows 與 Linux 移植他都沒有測試。

## 導讀觀點 {#perspective}

作者在 GitHub 寫 Compositor 是「a local, single-user editor with no network path」。發布說明另外提到會檢查更新，開啟時每天最多一次，更新要使用者自行確認才安裝。本文讀設定檔確認，檢查的對象是 GitHub 上的更新清單。作者也在 X 寫「no login, no account, no tracking」。

外部貢獻者曾提交 PR（向專案提出的程式碼修改）加入生成式填色，預設關閉，使用者要自備 Google 的 Gemini AI 服務金鑰、按下產生才會把圖片送出。PR 內文自己寫這是第一個讓使用者內容離開電腦的功能。作者留言要再想想長期如何在 Compositor 放進 AI，這個 PR 之後關閉、沒有合併。另一個在本機執行的 AI 放大功能，作者留言寧可整體重新規劃 AI 功能（可能在 v2），不要一項一項加。

開源讓這些主張可以被檢查，不必只聽作者的說法。本文 10 月 12 日用關鍵字搜尋過主分支的原始碼，除了更新檢查之外沒有找到網路請求或統計分析的程式，這不是完整的稽核。依本文計算，Swift 程式碼約 3.7 萬行，從 commit 署名推論大多由 AI 產生。前述開發者對這些程式碼的說法是「decidedly not for human consumption」。

9 月 19 日有外部開發者依一份資安掃描提出八個修補 PR，其中一個提到特製的專案檔數值超出範圍時，會讓程式的屬性面板或調整編輯器停止運作。作者把這批 PR 一起關閉，留言寫軟體在本機單人使用、沒有不受信任的輸入，這些屬於程式穩定性的範圍（「robustness questions rather than security ones」）。作者的留言沒有說明，打開別人傳來的專案檔算不算不受信任的輸入。

作者的關閉留言也寫，匯入、縮放與匯出都已統一限制在 1 億像素、單邊 3 萬像素，新加的限制可能拒絕正常的檔案。留言另外寫到，這批 PR 讓作者發現自動測試已經一段時間無法執行，修好之後有 362 個測試。作者請提交者在實際重現當機時，附上檔案與步驟另開 issue（專案的問題回報）。

作者的說法是自用的工具會持續維護，需要其他平台的人可以依 MIT 授權自行移植，已有其他開發者做出 Windows 等平台的移植版。前述開發者懷疑作者是否會持續維護使用者要求、作者自己不用的功能，一般人用的軟體似乎沒有開源專案常見的顧問收入（替企業提供服務、支撐開發的收入）。另有開發者做了簡體中文的分支（另外複製一份、自行修改的版本），在原專案的 issue 寫分支移除了自動更新。理由是避免使用者被更新回英文版，也不連到原專案的更新清單。

用搭載 Apple 晶片、macOS 26 以上的 Mac 處理圖片的人，可以從 GitHub 或 Homebrew 下載試用。下載不必註冊，回報問題要有 GitHub 帳號。依作者的說法與本文的關鍵字搜尋，編輯圖片時除了更新檢查不會連網，更新檢查預設開啟、裝不裝由使用者決定。本文沒有完整稽核程式碼，作者也沒有說明打開別人傳來的專案檔是否有風險。

比較這類工具時，可以從幾個方面問。作者重視的是軟體在本機執行、不用登入、可以自行修改，這些主張能不能從原始碼與實際的網路連線確認。批評的一方在意的是維護，維護者只有一人時，自己需要的功能停止更新要怎麼辦。AI 寫成的程式碼有沒有人讀過，外部回報的問題又如何處理，也可以從專案的 issue 與 PR 看出來。
