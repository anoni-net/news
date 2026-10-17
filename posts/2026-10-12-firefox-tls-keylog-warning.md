---
title: Firefox 157 的 TLS 金鑰記錄警告
description: 桌面版 Firefox 157（9 月 29 日發布）在電腦被設定成記錄加密金鑰時會顯示警告。Mozilla 的說明頁提到多半是防毒或安全軟體設定的，出現警告不代表電腦中毒，連不上網站時可以先檢查這類軟體的 HTTPS 掃描功能。
date: 2026-10-12T00:00:00+08:00
slug: firefox-tls-keylog-warning
categories:
  - security
sources:
  - title: Firefox 157.0, See All New Features, Updates and Fixes
    url: https://www.firefox.com/en-US/firefox/157.0/releasenotes/
    publisher: Mozilla
    date: 2026-09-29
  - title: Troubleshoot network errors when TLS key logging is enabled
    url: https://support.mozilla.org/en-US/kb/sslkeylogfile-warning
    publisher: Mozilla
    date: 2026-06-25
  - title: Add a warning to about:neterror when SSLKEYLOGFILE is in use
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2035411
    publisher: Mozilla Bugzilla
    date: 2026-04-28
  - title: RFC 9850 - The SSLKEYLOGFILE Format for TLS
    url: https://www.rfc-editor.org/rfc/rfc9850.html
    publisher: RFC Editor
authors:
  - anoni-net
---

Firefox 9 月 29 日發布的 157 版，在電腦被設定成記錄加密金鑰時，會在網址列盾牌圖示的網站資訊面板與設定頁顯示警告。版本說明只在桌面版列出此項變更，Android 與 iOS 的 157 版版本說明沒有提到。根據 Mozilla 的說明頁，出現警告不代表電腦中毒，多半是防毒或安全軟體在檢查加密連線。

依說明頁，觸發警告的是 `SSLKEYLOGFILE` 這個環境變數（作業系統提供給程式讀取的設定值），它會讓 Firefox 把 HTTPS 連線用的加密金鑰存成檔案。能讀到該檔案的軟體可能可以解密並檢視 HTTPS 流量。視軟體的用法，也可能攔截連線、冒充網站的伺服器並修改資料。部分連線錯誤頁也會多一條橫幅，英文介面顯示「Your connection may not be private」，連到同一份說明頁。

Mozilla 2026 年 4 月在 bug 追蹤系統建立的紀錄提到改動的原因，建立者寫到似乎有不少防毒軟體用該變數解密 HTTPS 流量，有時會讓連線以意想不到的方式出錯。同一則紀錄引用 Mozilla 的使用統計，Windows 上約一成使用者的電腦有該變數。依說明頁的介紹，軟體開發者看到警告，可能是除錯工具開著。

## 導讀觀點 {#perspective}

HTTPS 每次連線都會協商出一組金鑰，平常只留在瀏覽器與網站伺服器兩端，連線經過的網路設備看不到內容。`SSLKEYLOGFILE` 原本是給開發者除錯用的。金鑰寫進檔案之後，讀得到檔案、又取得那段加密流量的程式，就有機會解開這些連線。IETF（制定網際網路技術標準的組織）2026 年 7 月發布的參考性文件 RFC 9850 記載了金鑰檔的格式，同時提醒它只該用在保護測試資料的系統，不能用在正式環境。

看到警告又連不上網站時，說明頁建議先到防毒或安全軟體的設定裡找「HTTPS 掃描」、「加密流量監控」、「網頁防護」這類功能。軟體允許的話先暫時關掉，再看連線問題是否還在。關掉的期間，那套軟體也不會再檢查加密的網頁內容。說明頁有正體中文版，頁首標示是機器翻譯，沒有經過人工校對。

防毒軟體的 HTTPS 掃描要讀得到所有加密連線才能檢查網頁內容，要不要讓它看到，是使用者要做的取捨。依說明頁，只要信任那套軟體看到你在網路上做的一切，就不一定需要擔心。說明頁也提到通常不必停用防毒軟體，Firefox 本身有 Safe Browsing，會警告已知的惡意與詐騙網站。

沒有安裝這類軟體、也沒有在做網路除錯的人看到警告，可能是其他程式設了該變數，也可能是有人手動設定過。這是本文依說明頁列出的原因推斷的，說明頁沒有提供這種情況的處理步驟。本文的建議是請熟悉電腦的人協助檢查系統的環境變數設定。
