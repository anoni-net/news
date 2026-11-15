---
title: Facebook 照片裡的 FBMD 識別碼與 Brave 桌面版的移除功能
description: Brave 桌面版從 1.98 起，儲存或上傳圖片時自動移除 Meta 加在 Facebook 照片裡的 FBMD 識別碼。照片的位置、裝置與拍攝時間不在移除範圍，到 11 月 15 日為止 Android 與 iOS 版也還沒有。
date: 2026-11-21T00:00:00+08:00
slug: brave-photo-metadata
categories: [tracking]
sources:
  - title: Brave removes tracking metadata from Instagram and Facebook photos
    url: https://brave.com/privacy-updates/40-remove-tracking-metadata/
    publisher: Brave
    date: 2026-11-12
  - title: Release Channel 1.98.60
    url: https://community.brave.app/t/release-channel-1-98-60/660299
    publisher: Brave
    date: 2026-10-27
  - title: Strip metadata from images on download/upload
    url: https://github.com/brave/brave-browser/issues/5238
    publisher: GitHub
    date: 2019-07-14
  - title: "IPTC investigates: what does Facebook do with your photo metadata?"
    url: https://iptc.org/news/what-does-facebook-do-with-your-photo-metadata/
    publisher: IPTC
    date: 2019-07-22
  - title: Social Media Sites Photo Metadata Test Results 2019
    url: https://iptc.org/standards/photo-metadata/social-media-sites-photo-metadata-test-results-2019/
    publisher: IPTC
  - title: Automatically delete personal EXIF data from images when uploading
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=743152
    publisher: Mozilla
    date: 2012-04-06
watch:
  - date: 2026-12-21
    note: Brave 的照片識別碼移除是否推出 Android 與 iOS 版，以及移除位置、裝置、日期時間的選項是否上線
authors:
  - anoni-net
---

Brave 11 月 12 日公布，桌面版從 1.98 起，儲存或上傳圖片時會自動移除 Meta 加在 Facebook 照片裡的 `FBMD` 識別碼。用 Brave 桌面版的人更新之後就有這項保護，Android 與 iOS 版到 11 月 15 日為止還沒有，公告寫的是計畫推出。照片的位置、裝置型號與拍攝時間不在這次的移除範圍。

依 Brave 的公告，Meta 把識別碼存在國際新聞電訊委員會（IPTC）定義的照片 metadata（附在檔案裡、平常看不到的資料）裡。IPTC 為新聞業制定標準，攝影師與出版者用它的格式在圖片裡附上圖說、作者與著作權資訊。

IPTC 過去測試 Facebook 如何處理上傳的照片時，發現 Facebook 刪掉大部分原有的 metadata。Facebook 另外在「Special Instructions」欄位加上一串以 `FBMD` 開頭的長字串。另一個人下載同一張照片再上傳，這串值維持不變。Brave 在 7 月重做同樣的測試，識別碼仍然在。

公告假設有人用另一個名字經營 Instagram 帳號，跟家人與同事認識的 Facebook 實名帳號分開。他替兩個帳號各用不同的電子郵件別名，也許還用了 VPN 隱藏 IP 位址。他下載朋友在 Facebook 貼出的投票呼籲圖片、發到自己的 Instagram 之後，識別碼跟著檔案一起過去，Meta 就可能用它把 Instagram 帳號連到朋友的貼文與周圍的實名人際關係。連結一旦存在，Meta 可能向 Facebook 上認識他的人推薦那個 Instagram 帳號，這筆連結也可能外洩或因法律請求而交出。

Brave 的公告提到，Meta 沒有公開識別碼的用途，也沒有說明為何把它加在圖片的 metadata 裡。Brave 也寫到 Meta 可能沒有拿它來追蹤，但在沒有公開資訊時，Brave 會把各種可能與對隱私的影響都納入考量。到 11 月 15 日為止，本文查不到 Meta 對這個識別碼或對 Brave 公告的說明，也查不到 2019 年 IPTC 之後、Brave 以外的重新測試。

儲存圖片時，Brave 在下載完成前拿掉識別碼，之後改用其他瀏覽器或 App 上傳也不會帶著它。上傳圖片到網站時，Brave 送出的是移除後的副本，電腦裡的原始檔案不變。功能列在 10 月 27 日的 1.98.60 版本說明裡，對應的需求 2019 年就開在 Brave 的 GitHub 上。

Brave 公告的標題與第一段把 Instagram 與 Facebook 並列，但文中的測試與示範步驟都用 Facebook 的照片。到 11 月 15 日為止，本文找不到 Instagram 照片也帶著 `FBMD` 的獨立測試。IPTC 2019 年的社群網站測試表在 Instagram 一列只寫網站不提供另存或下載，也沒有顯示嵌入的 metadata。

## 導讀觀點 {#perspective}

IPTC 2016 與 2019 年的測試都發現兩個欄位的值跟上傳的不同，IPTC 推測是 Facebook 填入的。Job Id 欄位每上傳一次就換一個值，「Special Instructions」欄位的 `FBMD` 則在別人重新上傳時保持不變。IPTC 寫明不對這些值的用途做任何假設，2019 年時也找不到 Facebook 的規格或聲明。Brave 的公告只處理 `FBMD`、沒有提到 Job Id，寫的效果是讓 Meta 更難跨帳號與網站連結同一張照片，沒有寫能完全阻止。

照片的其他 metadata 有正當用途，例如相簿 App 依日期與地點整理照片。Brave 把移除位置、裝置與日期時間列為之後想加的功能，並寫到會讓使用者決定何時移除。

Brave 拿 Chrome 當沒有這項保護的對照。2012 年有人在 Firefox 的問題追蹤系統提出上傳時自動刪除 EXIF（相機寫進照片的拍攝資訊）的請求，到 11 月 15 日為止狀態是不修正（WONTFIX）。該請求針對的是 EXIF，跟 `FBMD` 所在的 IPTC 欄位分屬不同格式。

用 Brave 桌面版的人更新到 1.98 以上即可，公告沒有提到需要另外開啟或設定。Brave 的公告附了確認的步驟，先用 Chrome 這類瀏覽器從 `facebook.com` 另存一張照片，再用在瀏覽器裡執行的 image metadata viewer 開啟。「Special Instructions」欄位會出現 `FBMD` 開頭的值。改在 Brave 裡用同一個檢視網站選取該檔案，`FBMD` 的值就不見了。

依儲存與上傳這兩個移除時間點推斷，下載與上傳都沒有經過 Brave 桌面版的檔案不在保護範圍內，在手機上用 App 儲存與分享的照片也一樣。
