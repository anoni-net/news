---
title: 偵測智慧眼鏡藍牙訊號的 ZuckOff
description: ZuckOff 比對藍牙廣播，提醒附近有 Ray-Ban Meta 這類帶鏡頭的智慧眼鏡，但無法判斷對方是否正在錄影，App 本身也沒有公開原始碼。
date: 2026-09-28T07:00:00+08:00
slug: zuckoff-smart-glasses-detector
sources:
  - title: ZuckOff | Camera glasses detector
    url: https://zuckoff.app/
    publisher: ZuckOff
  - title: ZuckOff
    url: https://apps.apple.com/us/app/zuckoff/id6795234035
    publisher: App Store
  - title: How to Tell If Someone Near You Is Wearing Meta Smart Glasses
    url: https://www.wired.me/story/meta-smart-glasses-detector-app-zuckoff
    publisher: WIRED Middle East
    date: 2026-09-15
  - title: Privacy Settings for Meta AI Glasses
    url: https://www.meta.com/ai-glasses/privacy/
    publisher: Meta
  - title: Introducing Ray-Ban Meta Audio and Our Deepest Lineup of AI Glasses Yet
    url: https://www.meta.com/blog/ray-ban-meta-audio-and-deepest-ai-glasses-lineup/
    publisher: Meta
    date: 2026-09-23
  - title: Ray-Ban Meta (Gen 2)およびOakley Meta、5月21日より日本でも販売開始
    url: https://www.meta.com/ja-jp/blog/AI-glasses-Japan-launch/
    publisher: Meta
    date: 2026-05-19
authors:
  - anoni-net
---

一支名為 ZuckOff 的 App 可以偵測附近有沒有人戴著 Ray-Ban Meta、Oakley Meta 或 Snap Spectacles 這類帶鏡頭的智慧眼鏡。iPhone 與 Android 都有，基本的掃描功能免費，台灣、香港的 App Store 都能下載。介面有簡體中文，沒有正體中文。

開發者自己買了各款眼鏡，錄下它們廣播的藍牙訊號，整理成每一款的特徵。App 比對藍牙廣播裡的製造商代碼，比對到時提醒使用者，並依訊號強度估計大概的距離。專案網站寫明資料不會離開手機，也不需要註冊帳號。

限制同樣寫在專案網站。多數眼鏡戴著時會持續廣播，少數獨立運作的型號不發出訊號，App Store 的說明另外寫到，眼鏡跟主人的手機配對之後也可能停止廣播。沒偵測到不代表沒有人在錄影，偵測到也不代表有人在錄影，App 無法得知是誰戴著，訊號強度也指不出方向。

Wired 寫到，Meta 的智慧眼鏡 2025 年約賣出七百萬副。眼鏡拍攝時會亮起白色的指示燈，Meta 的說明頁寫明，偵測到指示燈被遮住、動過手腳或破壞時，眼鏡會自動停用鏡頭。

## 導讀觀點 {#perspective}

智慧眼鏡會透過藍牙對外廣播自己的存在，廣播裡帶著製造商的代碼。ZuckOff 在專案網站公開了比對用的代碼，例如 Ray-Ban Meta 與 Oakley Meta 所屬 Luxottica 的 `0x0D53`。偵測的原理不複雜，準確度取決於這張表整理得多完整，App Store 的更新紀錄就寫到，1.4.0 修正了把某些 iPhone 誤判成鏡頭眼鏡的問題。

ZuckOff 沒有公開原始碼，也沒有授權聲明，外界無法檢驗 App 實際做了什麼，只能相信網站上的說法。它要的權限不多，Android 版只要求藍牙掃描所需的附近裝置權限，並宣告不用來推算位置，所以不要求定位權限。

Meta 在 9 月 23 日宣布眼鏡在新加坡與南韓開賣。香港、澳門、馬來西亞等地 2026 年稍晚也會上市，日本則是 5 月 21 日就已經開賣。

在採訪、開會或私人聚會前想確認現場有沒有鏡頭的人，可以開著藍牙用 ZuckOff 掃描一次。免費的基本掃描就夠用，iPhone 與 Android 都有，不需要註冊帳號。遇到重要的對話，可以事先跟在場的人約定，請大家摘下眼鏡、把手機留在場外。掃描結果只能當作線索，獨立運作或已跟主人手機配對而停止廣播的眼鏡，ZuckOff 可能偵測不到。
