---
title: Salon 停刊與 Wayback Machine 裡的 25 萬篇文章
description: 美國網路媒體 Salon 11 月 5 日宣布停刊，Internet Archive 用 Wayback Machine 近三十年的存檔，推出可以依作者與年份查找的實驗性介面 Salon Explorer。讀者在意的報導，也可以趁還在線上時自行送存或存在自己手上。
date: 2026-11-29T00:05:00+08:00
slug: salon-archive
categories: [press]
regions: [US]
sources:
  - title: Preserving 30 Years of Salon Journalism
    url: https://blog.archive.org/2026/11/12/preserving-30-years-of-salon-journalism/
    publisher: Internet Archive
    date: 2026-11-12
  - title: Goodbye from Salon
    url: https://www.salon.com/2026/11/05/goodbye-from-salon/
    publisher: Salon
    date: 2026-11-05
  - title: Salon.com Article Explorer
    url: https://wayback-labs.sf.archive.org/salon-explorer/
    publisher: Internet Archive
  - title: Save Pages in the Wayback Machine
    url: https://help.archive.org/help/save-pages-in-the-wayback-machine/
    publisher: Internet Archive
  - title: ArchiveWeb.page
    url: https://github.com/webrecorder/archiveweb.page
    publisher: GitHub
  - title: ArchiveBox
    url: https://github.com/ArchiveBox/ArchiveBox
    publisher: GitHub
  - title: Tools & software
    url: https://netpreserve.org/web-archiving/tools-and-software/
    publisher: IIPC
  - title: The WARC Format 1.1
    url: https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/
    publisher: IIPC
watch:
  - date: 2026-12-29
    note: salon.com 上的舊文章是否仍可開啟，Salon Explorer 是否仍是實驗性的介面
authors:
  - anoni-net
---

美國網路媒體 Salon 在 11 月 5 日宣布停刊，結束 1995 年 11 月創刊以來 31 年的出刊。Internet Archive 一週後在部落格公告，透過 Wayback Machine 可以找到超過 25 萬篇 Salon 的文章，同時推出實驗性的查找介面 Salon Explorer。讀過、引用過 Salon 報導的人，停刊之後仍有地方找回原文。

Salon 的告別公告寫到，獨立數位新聞的經營環境多年來改變很大，Salon 自己的出版模式已經無法維持。到 11 月 29 日，Salon 的舊文章會在 `salon.com` 留多久還不確定。一家媒體停止出刊之後，網站可能繼續上線，也可能在主機或網域停止續約時消失。網站消失之後，舊報導還能不能找到，取決於當初有沒有人存過檔。

依公告，Internet Archive 用 Wayback Machine 保存 Salon 的頁面已將近三十年。在 Salon Explorer 上，超過 2 萬名作者的文章可以依作者、年份與時期篩選，也能用關鍵字搜尋全文。習慣用 Wayback Machine 的人，也可以直接輸入 `salon.com` 的網址，依日期瀏覽各時期的頁面。

## 導讀觀點 {#perspective}

網頁典藏服務多半用爬蟲，也就是自動造訪網頁、下載內容的程式，定期存下頁面當下的副本並標上時間。網站關閉之後才想到要存，已經沒有頁面可以存。

讀者自己在意的報導，可以趁還在線上時用 Wayback Machine 的 Save Page Now 送存。依 Internet Archive 的說明頁，在表單貼上網址、按下按鈕，就會存下這一頁並取得一個永久的網址。Chrome、Firefox、Safari 都有擴充套件，iOS 與 Android 也有 App。少數禁止爬取或 SSL（網站的加密連線）設定特殊的網站會送存失敗，Internet Archive 也不保留送存者的 IP 位址。

要把存檔留在自己手上，本站在[西班牙封鎖 archive.today](https://anoni.net/news/2026/09/spain-blocks-archive-today/)那篇介紹過 SingleFile 與 ArchiveBox。SingleFile 是把整頁存成一個 HTML 檔的瀏覽器擴充套件，ArchiveBox 是自架的網頁典藏工具。另一種做法是 Webrecorder 的開源工具 ArchiveWeb.page，有 Chrome 與 Chromium 系瀏覽器的擴充套件與桌面版，可以在瀏覽的同時把頁面存下來。ArchiveBox 與 ArchiveWeb.page 都能存成網頁典藏的標準格式 WARC，WARC 把網址、取得的時間與伺服器回應的內容一起存下，之後可以用典藏工具照原樣重播頁面。

送進 Wayback Machine 的頁面要靠 Internet Archive 的服務持續運作才能開啟。存在自己電腦裡的檔案要自行備份，檔案只在自己手上，別人也無從確認存下之後有沒有被改過。

要讓別人查證與引用的頁面適合送 Save Page Now，想自行保管的頁面用 ArchiveWeb.page 或 ArchiveBox。以 Chrome 的 Wayback Machine 擴充套件為例，裝好之後在頁面上按工具列的圖示、選 Save Page Now 即可送出。Save Page Now 只存送出的那一頁，報導的其他分頁與文中連出去的頁面要另外送存。Wayback Machine 的存檔任何人都能查詢，登入後才能看到或含有個人資料的頁面不適合送存。
