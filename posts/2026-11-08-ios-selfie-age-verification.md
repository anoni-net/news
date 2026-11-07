---
title: iOS 27.2 用自拍估算年齡的成年確認
description: Apple 在 iOS 與 iPadOS 27.2 加入用自拍估算年齡、確認使用者已成年的選項，依 Apple 的支援文件只在澳洲、巴西、新加坡與英國提供。到 11 月 7 日為止，台灣與香港不在 Apple 列出需要確認年齡的地區內。
date: 2026-11-08T00:00:00+08:00
slug: ios-selfie-age-verification
categories: [censorship]
sources:
  - title: Confirm that you're an adult with a selfie
    url: https://support.apple.com/en-us/149095
    publisher: Apple
    date: 2026-10-26
  - title: Region-specific rules for managing an Apple Account
    url: https://support.apple.com/en-us/125666
    publisher: Apple
    date: 2026-10-26
  - title: If you're asked to confirm that you're an adult
    url: https://support.apple.com/en-us/125662
    publisher: Apple
    date: 2026-10-26
  - title: Apple Introduces Selfie Age Verification in iOS 27.2
    url: https://www.privacyguides.org/news/2026/10/29/apple-introduces-selfie-age-verification-in-ios-27-2/
    publisher: Privacy Guides
    date: 2026-10-29
  - title: Age assurance developer Q&A
    url: https://developer.apple.com/support/age-assurance/
    publisher: Apple Developer
  - title: Age requirements for managing an Apple Account in Brazil
    url: https://support.apple.com/en-us/126783
    publisher: Apple
    date: 2026-10-26
  - title: Age requirements for managing an Apple Account in the United States (Texas)
    url: https://support.apple.com/en-us/127462
    publisher: Apple
    date: 2026-06-04
  - title: Next steps for apps distributed in Texas
    url: https://developer.apple.com/news/?id=2ezb6jhj
    publisher: Apple Developer
    date: 2025-11-04
  - title: New Online Safety Code of Practice for App Distribution Services Enhances Protection for Singapore Users
    url: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/online-safety-code-of-practice-for-app-distribution-services
    publisher: IMDA
    date: 2025-01-15
  - title: Factsheet on Age Assurance under the ADS Code
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2025/01/ads-code/factsheet-on-age-assurance.pdf
    publisher: IMDA
    date: 2025-01-15
  - title: Internet Age Gates Are a Growing Global Threat
    url: https://www.eff.org/deeplinks/2026/06/internet-age-gates-are-growing-global-threat
    publisher: EFF
    date: 2026-06-05
  - title: "Face Scans to Estimate Our Age: Harmful and Creepy AF"
    url: https://www.eff.org/deeplinks/2025/01/face-scans-estimate-our-age-creepy-af-and-harmful
    publisher: EFF
    date: 2025-01-23
regions:
  - AU
  - BR
  - SG
  - GB
watch:
  - date: 2026-12-08
    note: Apple 是否把自拍年齡確認擴大到南韓、德州或其他地區，是否公布年齡估算模型的準確度或誤判率
  - date: 2027-01-31
    note: 巴西 2025 年通過的兒少法律預計 2027 年初全面遵循時，App 商店與作業系統提供年齡訊號的做法，以及 Apple 的巴西說明頁有沒有更新
authors:
  - anoni-net
---

Apple 在 iOS 與 iPadOS 27.2 加入一種新的成年確認方式，使用者拍下自己的臉，由年齡估算模型判斷是否已滿 18 歲。依 Apple 10 月 26 日發布的支援文件，自拍選項只在澳洲、巴西、新加坡與英國提供。同一份文件列出的年齡確認要求適用於六個地方的 Apple 帳號，另外兩處是南韓與美國德州，這兩地沒有自拍選項。到 11 月 7 日為止，台灣、香港與其他沒有列出的地方都不在清單上，當地的使用者不必做年齡確認。

隱私指南網站 Privacy Guides 10 月 29 日的短訊報導了這項功能，文末寫到住在澳洲、巴西、新加坡、南韓、英國或德州的人都要確認年齡，沒有區分哪些地方提供自拍。本文的地區範圍以 Apple 的支援文件為準，南韓與德州的使用者只能用其他方式確認。

依 Apple 的說明，年齡確認可能出現在建立新帳號、更新系統、變更部分安全設定或下載或購買 18+ 分級 App 的時候，實際情況依所在地區而定。選擇自拍時，要把臉放在畫面中央，慢慢向四個方向轉頭拍下臉的各個角度。確認成年之後不必再做一次。

同一份說明提到，自拍會同時交給裝置上與 Private Cloud Compute（Apple 的雲端運算服務，Apple 把它描述成裝置的安全與隱私保護在雲端的延伸）上的年齡估算模型分析，結果在裝置上合併。Apple 寫明分析過程中包括 Apple 在內的任何人都無法存取自拍。確認之後自拍會刪除，不以任何形式保留。Privacy Guides 的文章寫成在裝置上「或」在 Private Cloud Compute 執行，Apple 的說明則是兩邊都執行。

自拍之外，Apple 列出的方式還有本人的信用卡與掃描證件（護照、駕照或政府核發的身分證件），金融卡與禮品卡不能用。已有帳號的人，Apple 會先檢查帳號裡有沒有信用卡或其他符合條件的資料。依 Apple 另一份說明，證件影像由 Apple 與服務供應商用來確認年齡與防範詐騙，短暫保存後刪除。

## 導讀觀點 {#perspective}

年齡估算從臉部影像推測一個人大約幾歲，不需要出示證件。Privacy Guides 的文章提到，效果完全取決於估算演算法的品質，而且一定會有誤判。成年人可能被判成未成年，也可能有相反的情況。到 11 月 7 日為止，本文查不到 Apple 公布的模型名稱、誤判率或準確度資料，也沒有查到獨立驗證自拍刪除與無法存取的報告。

Apple 列出的地方，有幾處的法規要求 App 商店確認或提供使用者的年齡。新加坡資訊通信媒體發展局（IMDA）依《Code of Practice for Online Safety – App Distribution Services》，要求指定的 App 商店 2026 年 4 月 1 日起至少能判斷使用者是否未滿 18 歲，年齡估算、年齡驗證或兩者並用由商店自行選擇。IMDA 的新聞稿寫到，目的是降低使用者、尤其是兒童接觸有害內容的風險，Code 也要求年齡確認做到資料最小化。

德州的 App 商店責任法（App Store Accountability Act，SB 2420）從 6 月 4 日起適用於在德州建立的新 Apple 帳號。依 EFF 6 月的文章，巴西 2025 年通過的法律要求 App 商店與作業系統替其他服務提供年齡訊號，預計 2027 年初全面遵循。

Privacy Guides 的文章逐一比較各種方式，信用卡會交出可識別身分的資料，但下載免費 App 本來就要填付款資訊。掃描證件可能讓敏感文件落到第三方手上，文中舉 Discord 為例，替它處理證件照年齡確認的第三方外洩了約 7 萬份證件。自拍做不好同樣有風險，替 Roblox 與 ChatGPT 等公司處理年齡驗證的 Persona 外洩了自拍資料庫。文章的看法是 Apple 的版本在這方面看來好得多，至少比把證件交給第三方好。

數位權利組織 EFF 2025 年 1 月討論臉部年齡估算的文章早於 Apple 推出自拍確認（本文沒有查到 EFF 針對 Apple 這項功能的評論），文中寫到臉部掃描對隱私與資訊安全帶來新的威脅。設計不良的系統可能保存臉部資料，甚至跟使用者瀏覽的內容連結起來。EFF 6 月的文章提到，它對歐洲各項年齡驗證倡議的回應一直是，強制年齡驗證不是保護年輕人的正確方式。Apple 2025 年 11 月針對德州法律的開發者公告也寫到，這類法律為了讓人下載一個 App 就要求蒐集敏感個資，Apple 擔心會損害所有使用者的隱私。

依 Apple 給開發者的問答，App 可以透過 Declared Age Range API（App 向系統查詢使用者年齡區間的介面）取得年齡資訊，使用者可以決定要不要分享。在法律要求的地方，Apple 會把當地法律定義的年齡類別提供給 App。依巴西的說明頁，開發者為遵守當地法律提出要求時一律分享年齡區間。德州的說明頁則寫一律分享，兩地的使用者都不能關閉。

iOS 26.5 起，用信用卡或證件確認的結果只回傳一個不區分方式的 `confirmed` 值，本文沒有查到自拍確認之後回傳什麼。加州的 AB 1043 走另一種做法，要求作業系統在帳號設定時詢問年齡、把年齡範圍提供給 App 而不要求驗證。AB 1043 經 AB 1856 修改後 2027 年 1 月 1 日起適用（見[加州 AB 1856 的開源作業系統豁免](https://anoni.net/news/2026/10/california-ab1856-open-source-exemption/)）。

台灣與香港不在 Apple 列出的年齡確認地區。到 11 月 7 日為止，本文查不到台灣與香港針對作業系統或 App 商店要求年齡確認的法規。依開發者問答，在法律沒有要求的地方，App 只有在使用者自己選擇分享時才能取得年齡區間。

本文依 Apple 的文件推論，台灣與香港的讀者可能碰到年齡確認的情況有兩種。一是 Apple 帳號的地區屬於清單上的地方，或是在那些地方建立新帳號。Apple 的文件沒有寫明以帳號地區還是所在位置判斷，德州的說明頁寫的是在德州建立的新帳號。二是當地之後立法要求 App 商店確認年齡，Apple 的文件寫的是依法才適用年齡確認。

帳號在澳洲、巴西、新加坡或英國的人被要求確認時，可以比較各種方式留下的資料。已綁信用卡的帳號可能不必另外操作，自拍依 Apple 的說明會送到 Private Cloud Compute 分析後刪除，證件影像則由 Apple 與服務供應商短暫保存。到 11 月 7 日為止 Apple 沒有公布誤判率，自拍無法確認成年時可以重拍，或改用信用卡、證件。不確認也能繼續使用裝置，代價是不能下載 18+ App，也不能關閉部分安全設定。

台灣與香港的讀者現在不需要調整任何設定。之後可以留意 Apple 會不會把自拍選項擴大到南韓、德州或其他地方，會不會公布估算模型的準確度。另一項是巴西預計 2027 年初全面遵循時，作業系統提供的年齡訊號如何實作。
