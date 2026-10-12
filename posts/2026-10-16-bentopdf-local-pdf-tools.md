---
title: 在瀏覽器本機處理 PDF 的開源工具 BentoPDF
description: 開源的 PDF 工具組 BentoPDF 依官方說明在瀏覽器裡完成合併、壓縮、OCR 與移除中繼資料，不必把檔案上傳到線上轉檔網站。打開官網就能用，介面有正體中文，部分功能使用時要從第三方網站 jsDelivr 下載程式。
date: 2026-10-16T00:00:00+08:00
slug: bentopdf-local-pdf-tools
categories:
  - security
sources:
  - title: Privacy Policy
    url: https://www.bentopdf.com/privacy
    publisher: BentoPDF
    date: 2026-08-29
  - title: Frequently Asked Questions
    url: https://www.bentopdf.com/faq
    publisher: BentoPDF
  - title: OCR PDF Free Online - Make Scanned PDFs Searchable | BentoPDF
    url: https://www.bentopdf.com/ocr-pdf
    publisher: BentoPDF
  - title: Remove Metadata - Strip Hidden Data from PDF - BentoPDF
    url: https://www.bentopdf.com/remove-metadata
    publisher: BentoPDF
  - title: bentopdf/README.md
    url: https://github.com/alam00000/bentopdf/blob/main/README.md
    publisher: GitHub
  - title: Licensing for BentoPDF
    url: https://www.bentopdf.com/licensing
    publisher: BentoPDF
  - title: About BentoPDF - Privacy-First Free PDF Tools | Our Story
    url: https://www.bentopdf.com/about
    publisher: BentoPDF
  - title: Workflow Import Allows Unvalidated TSA URL Leading to PDF Hash Exfiltration via RFC 3161 Requests
    url: https://github.com/alam00000/bentopdf/security/advisories/GHSA-cx8x-7rrr-r9x8
    publisher: GitHub
    date: 2026-08-23
  - title: BentoPDF Handles PDFs Locally, So You Don’t Have to Upload Them to Websites
    url: https://itsfoss.com/bentopdf/
    publisher: It's FOSS
    date: 2026-10-10
  - title: Privacy Policy
    url: https://www.ilovepdf.com/help/privacy
    publisher: iLovePDF
    date: 2026-02-19
  - title: Privacy Notice
    url: https://smallpdf.com/privacy
    publisher: Smallpdf
    date: 2025-07-29
  - title: Is Smallpdf Safe?
    url: https://smallpdf.com/blog/is-smallpdf-safe
    publisher: Smallpdf
    date: 2026-07-14
  - title: 請同仁避免使用線上轉檔、加解密服務，以防資安事件發生
    url: https://doit.gov.taipei/News_Content.aspx?n=9B8993131395DA3F&sms=93D47212F58C7A57&s=46FD091DEE0322E4
    publisher: 臺北市政府資訊局
    date: 2023-10-17
watch:
  - date: 2026-11-16
    note: BentoPDF 的資安公告 GHSA-cx8x-7rrr-r9x8 是否列出修正版本
authors:
  - anoni-net
---

It's FOSS 10 月 10 日介紹開源的 PDF 工具組 BentoPDF，官網寫有 100 多項工具。依官方說明，合併、分割、壓縮、OCR（光學字元辨識，把掃描的圖片轉成可以搜尋的文字）、加密與移除中繼資料都在瀏覽器裡處理，不必把檔案上傳到伺服器。打開官網就能用，不必註冊，介面有正體中文與簡體中文。到 10 月 12 日為止，最新版是 8 月 29 日發布的 2.8.8。

官方隱私權政策寫明，處理由在使用者裝置上執行的 JavaScript 與 WebAssembly 函式庫完成，檔案不會上傳。政策也寫明網站不使用 cookie 與統計分析服務。壓縮、PDF 轉 Word 等功能用到的 PyMuPDF 這類元件不包含在 BentoPDF 的原始碼裡，README 寫明它們在使用時由瀏覽器從 jsDelivr 下載（jsDelivr 是替網站分送程式檔的第三方服務）。OCR 工具頁也寫明第一次使用時要下載 OCR 引擎與選擇的語言包，掃描的頁面與辨識出的文字留在裝置上。

程式碼以 AGPL-3.0 授權公開在 GitHub，另有 79 美元一次買斷的商業授權，給要用在閉源產品的人。專案由一位開發者起頭，官網的介紹頁寫已有 60 多人貢獻程式碼、翻譯與修正。不想用官網的人，可以用 Docker（把整套程式包成一個可以直接執行的套件）在自己的電腦或伺服器上架設。

## 導讀觀點 {#perspective}

線上轉檔網站把檔案傳到自己的伺服器處理再傳回，檔案在對方手上多久，要看各家的政策。iLovePDF 的隱私權政策寫明處理後兩小時內刪除，電子簽署服務除外。Smallpdf 的隱私權聲明寫明，沒有登入的使用者的檔案通常在最後一次開啟後的合理期間內刪除（重新開啟會延長），官方部落格則寫免費使用的檔案一小時後刪除。臺北市政府資訊局 2023 年也提醒同仁避免使用線上轉檔與加解密服務，理由是無法確保這些服務取得資料後如何保存與使用。

BentoPDF 的隱私權政策寫明，本機處理避開的是傳輸途中與伺服器上的外洩。本文的推論是，要信任的對象因此換成網頁上的程式。用官網版本時，執行的是官網當下提供的那一份，更新不需要使用者同意。進階功能還會從 jsDelivr 載入程式碼，官方 FAQ 另外寫明少數需要外部資料的工具可能需要連線。

專案在 GitHub 公開的資安公告中有一則，匯入特製的工作流程檔會把 PDF 的 SHA-256 雜湊值（由檔案內容算出的一串摘要，不是檔案本身）送到攻擊者的伺服器。公告列的影響範圍是 2.8.6 與更早的版本，到 10 月 12 日為止沒有列出修正版本。

檔案在本機處理，PDF 本身仍可能帶著作者、建立時間這類隱藏的屬性。BentoPDF 的移除中繼資料工具可以清掉它們，「Sanitize PDF」工具另外移除註解與腳本，分享檔案之前可以先處理一次。

需要合併或轉換含個資的文件、又不想上傳到線上服務的人，可以直接用官網，所有工具免費。官方 FAQ 寫明沒有設檔案大小的限制，上限取決於自己電腦的效能。

想固定版本的人可以照 README 用 Docker 自架，需要先安裝 Docker、會操作命令列。不能連外的環境要另外照 README 的離線部署步驟，先在能連網的電腦打包需要的元件再搬進去。隱私權政策也寫明，檔案的安全取決於自己的電腦與瀏覽器。依本文的推論，電腦本身被入侵時，本機處理保護不到。
