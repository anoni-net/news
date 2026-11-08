---
title: Privacy Badger 的 macOS Safari 版
description: EFF 10 月 19 日推出阻擋追蹤器的擴充套件 Privacy Badger 的 Safari 版，只支援 Mac，需要 Safari 26.5 與 macOS 15.7.7 以上。到 11 月 8 日為止，iPhone 與 iPad 還沒有 Safari 版。
date: 2026-11-12T00:00:00+08:00
slug: privacy-badger-safari-macos
categories:
  - tracking
sources:
  - title: Announcing Privacy Badger for Safari on macOS
    url: https://www.eff.org/deeplinks/2026/10/announcing-privacy-badger-safari-macos
    publisher: EFF
    date: 2026-10-19
  - title: EFF Launches Privacy Badger for Safari on macOS
    url: https://www.eff.org/press/releases/eff-launches-privacy-badger-safari-macos
    publisher: EFF
    date: 2026-10-19
  - title: Privacy Badger | Fight hidden tracking with EFF
    url: https://privacybadger.org/
    publisher: EFF
  - title: Privacy Badger App - App Store
    url: https://apps.apple.com/us/app/privacy-badger/id6761143693
    publisher: Apple
  - title: Support Safari on iOS
    url: https://github.com/EFForg/privacybadger/issues/3248
    publisher: GitHub
  - title: privacybadger/src/_locales
    url: https://github.com/EFForg/privacybadger/tree/master/src/_locales
    publisher: GitHub
  - title: Privacy Badger now supports Safari
    url: https://freedom.press/digisec/blog/privacy-badger-now-supports-safari/
    publisher: Freedom of the Press Foundation
    date: 2026-10-28
  - title: Prevent cross-site tracking in Safari on Mac
    url: https://support.apple.com/guide/safari/prevent-cross-site-tracking-sfri40732/mac
    publisher: Apple
watch:
  - date: 2026-12-12
    note: Privacy Badger 是否推出 iPhone 與 iPad 的 Safari 版，GitHub issue #3248 是否關閉，privacybadger.org 的 FAQ 有沒有更新 iOS 的進度
authors:
  - anoni-net
---

美國數位權利組織 EFF 在 10 月 19 日推出 Privacy Badger 的 Safari 版。Privacy Badger 是 EFF 開發的免費瀏覽器擴充套件，會自動學習辨識並阻擋追蹤器。Safari 版只支援 Mac，需要 Safari 26.5 以上，Mac App Store 頁面列出的系統需求是 macOS 15.7.7 以上。到 11 月 8 日為止，iPhone 與 iPad 的 Safari 還不能安裝。

依 EFF 的公告，Privacy Badger 已有超過 400 萬名使用者。EFF 的技術人員在新聞稿提到，支援 Safari 一直是使用者最常提出的需求之一。公告把 Privacy Badger 能在 Safari 26.5 以上推出，歸功於 Safari 對擴充套件支援的改進。

依公告，Safari 預設的瀏覽模式會限制追蹤器可以取得的資訊，但仍讓追蹤器載入。Privacy Badger 從一開始就不讓追蹤器載入，可以擋下繞過 Safari 防護的追蹤手法。嵌入的推文、留言區與影片播放器這類小工具，即使使用者沒有點擊也可能分享資料，Privacy Badger 會把它們換成點了才載入的預留框。

Privacy Badger 也會自動送出全球隱私控制（Global Privacy Control，GPC）訊號，告訴網站不要出售或分享使用者的個人資料。公告列出加州、科羅拉多、紐澤西、康乃狄克等美國的州，寫明 GPC 在這些地方已具法律效力。

Safari 版要從 Mac App Store 免費安裝，賣家是 EFF。公告提醒 Safari 安裝擴充套件的步驟比其他瀏覽器複雜，附上 Apple 的說明頁。這是 Safari 版的第一個版本，遇到問題可以寄信到 `extension-devs@eff.org` 或在 GitHub 回報。

## 導讀觀點 {#perspective}

依 privacybadger.org 的說明，Privacy Badger 用演算法判斷追蹤器，多數阻擋工具則仰賴人工維護的網域清單。它觀察第三方網域有沒有使用能唯一識別瀏覽器的 cookie、存在本機儲存空間的「超級 cookie」與畫布指紋（canvas fingerprinting，用瀏覽器繪圖的細微差異辨識裝置）。同一個第三方網域在三個不同的網站上追蹤使用者，就會被擋下。廣告沒有追蹤使用者時，Privacy Badger 不會擋。

Privacy Badger 也用清單，預設會定期從 EFF 的訓練專案 Badger Sett 取得 Badger Sett 在數千個熱門網站上找到的追蹤器資料。另有一份黃名單，收錄網站運作需要的第三方網域。Privacy Badger 會載入這些網域的內容，只擋掉第三方 cookie 與 referrer。說明頁把黃名單寫成對實用性的妥協，長期希望不再需要黃名單。

依 Apple 的說明頁，Safari 會刪除使用者沒有直接造訪並互動過的第三方網站的 cookie 與網站資料。Safari 也會向網站呈現簡化過的系統設定，讓每台 Mac 看起來更相似，降低追蹤者辨識裝置的能力。依 EFF 的公告，Privacy Badger 單獨使用就有效。跟廣告封鎖器或 Safari 進階設定裡套用到所有視窗的追蹤防護一起用時，它也能擋下不在其他工具清單裡、或其他工具選擇不擋的追蹤器。

依 privacybadger.org 的說明，GPC 的用意是在有適用隱私法的地方，對所有公司都具法律效力。公告列出的州都在美國。本文推論，其他地方的網站可能不理會這個訊號。說明頁也提到，Privacy Badger 會一併送出 Do Not Track 訊號（請網站不要追蹤使用者的瀏覽器訊號），網域收到兩種訊號之後仍收集唯一識別碼才會被擋下。

安裝時瀏覽器會警告擴充套件可以存取所有網站的資料，privacybadger.org 寫明除非使用者送出網站故障回報，否則不會分享瀏覽資料。Mac App Store 頁面的隱私標示寫「不收集資料」，這項資訊由開發者提供，Apple 沒有驗證。新聞自由組織 Freedom of the Press Foundation 介紹 Safari 版時也提醒，只安裝可信任的擴充套件。除了權限，網站也可能無法正常運作，EFF 的公告提到這時可以只對那個網站停用 Privacy Badger。

用 Mac 版 Safari、想減少跨網站追蹤的人，第一步先確認 Safari 已更新到 26.5 以上、系統是 macOS 15.7.7 以上，再從 Mac App Store 安裝並照 Apple 的說明在 Safari 啟用。擴充套件的介面有正體中文，說明頁 privacybadger.org 到 11 月 8 日為止沒有正體中文版。Privacy Badger 擋的是第三方追蹤器，直接造訪的網站自己收集的資料不在範圍內（例如直接造訪 YouTube 時，YouTube 自己的追蹤與廣告都不會被擋），iPhone 與 iPad 上的瀏覽也還無法保護。
