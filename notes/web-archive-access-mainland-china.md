# Wayback Machine 在中國大陸的連線狀況與停刊媒體網站的典藏

範圍是從中國大陸連到 Internet Archive 的 Wayback Machine 的狀況，以及停刊或被迫關閉的媒體網站下架之後的存檔情形。第一次整理是寫 anoni-net/news 的 Salon 停刊那篇（`2026-11-29-salon-archive`）的時候，查證日期 2026-11-29。

## 量測

- 事實：長期量測防火長城的 GreatFire，對 `http://web.archive.org` 的結論是無法從中國大陸打開。頁面裡的紀錄是最近 1 次有結論的測試失敗，最後測試日 2026-11-07，首次紀錄的日期是 2012-04-14。同一頁列出 `https://web.archive.org` 的狀態是 Blocked，archive.org 底下 84 個測試過的網址中有 82 個是 blocked。這是第三方的量測，近期有結論的測試只有 1 次，樣本數很少
    - 照錄：「It's blocked — 100% of the last 1 conclusive tests failed in mainland China.」、「GreatFire has recorded interference with http://web.archive.org from mainland China since 2012-04-14.」 <!-- docs-style-lint: disable-line -->
    - 來源：Is http://web.archive.org blocked in mainland China? — GreatFire，<https://en.greatfire.org/web.archive.org> <!-- docs-style-lint: disable-line -->
    - 本站舊稿寫的「2016 年起」與這頁的 2012-04-14 不一致，引用時以這頁為準
- 查不到：Salon Explorer 所在的 `wayback-labs.sf.archive.org` 的量測、Wayback Machine 在其他亞洲地區的連線情形

## 香港

- 事實：Archive Team wiki 的 Stand News（立場新聞）頁裡寫，2021-12-29 超過 200 名香港警務處人員搜查立場新聞，網站與社群帳號當晚關閉。頁面狀態 Offline，Archiving status 標 Partially saved，這是立場新聞整體專案（含網站與社群帳號）的狀態，與下一條主站 ArchiveBot 紀錄的 Saved! 層級不同。Archive Team 是志工團體，這是二手來源
    - 照錄：「On December 29, 2021, Stand News was raided by over 200 officers of the Hong Kong Police Force. The website and social media had shut down that night.」 <!-- docs-style-lint: disable-line -->
    - 來源：Stand News — Archive Team，<https://wiki.archiveteam.org/index.php/Stand_News> <!-- docs-style-lint: disable-line -->
- 事實：同一個團體的 Hong Kong media 頁把立場新聞的 ArchiveBot 紀錄列為 Saved!，並寫網站在 2021-12-29 警方搜查後關閉、首頁換成停刊公告、社群帳號刪除。頁面裡寫 sitemaps 在 6 月與關站前的 12 月各送進 URL 清單一次（原文 once in June, once in December just before shutdown，沒有寫 6 月的年份）
    - 來源：Hong Kong media — Archive Team，<https://wiki.archiveteam.org/index.php/Hong_Kong_media> <!-- docs-style-lint: disable-line -->
- 查不到：蘋果日報 2021 年 6 月停刊後網站下架與志工保存的細節（SCMP 頁面回 403，未讀到原文）、台灣與新加坡新聞網站停刊後的典藏情形
