# 瀏覽器與指紋檢測網站在中國大陸的取得方式

範圍是 Chrome、Firefox 與 Tor Browser 的官方網站或下載頁、兩款瀏覽器在中國大陸 App Store 的上架狀態，以及 EFF 的指紋檢測網站 Cover Your Tracks 在中國大陸能不能連上。Brave 見 `brave-access-asia.md`，Google Play 見 `google-services-mainland-china.md`，Tor 網路本身的連線狀況見 `tor-access-asia.md`。第一次整理是寫 anoni-net/news 的瀏覽器指紋那篇的時候，查證日期 2026-10-23。

GreatFire 是第三方的量測，量的是網址能不能連線，不是官方的封鎖名單，也沒有區分瀏覽器內建的更新管道。

## GreatFire 的判定方式

- 事實：GreatFire 每個網址的判定只看有結論的測試（conclusive tests），頁面會寫出最近幾次有結論的測試、各有幾次受到干擾。引用時寫出次數，次數少的不要寫成「完全被封鎖」
- 事實：頁面標「Verdict revised」代表先前的判定已經更正。連線被直接拒絕（refused）的測試不再計入，GreatFire 從 2026 年 8 月底起不把連線被拒當成封鎖的證據，因為這類拒絕也出現在沒有其他干擾跡象的路徑上。被排除的那次測試日期不能當成最後一次有結論的測試引用
    - 照錄：「3 of the tests behind that verdict, the most recent on 2026-10-21, had their mainland China connections refused outright — and since late August 2026 refusals have been arriving on routes with no other sign of interference, so they no longer count as evidence of blocking.」 <!-- docs-style-lint: disable-line -->
    - 來源：GreatFire，<https://en.greatfire.org/https/www.mozilla.org>，2026-10-23 另用 WebFetch 核對過這一句。方法說明的連結是 <https://en.greatfire.org/data/methodology#connfail>，內文沒有讀

## Chrome

- 事實：`https://www.google.com/chrome` 最近 2 次有結論的測試都受到干擾（2/2，最後一次 2026 年 10 月 16 日），GreatFire 的判定是「Sometimes」，訪問不穩定。從 2012 年 9 月 13 日起就有干擾紀錄
    - 照錄：「Sometimes. Access is unreliable — 100% of the last 2 conclusive tests showed interference.」 <!-- docs-style-lint: disable-line -->
    - 照錄：「As of the last test on 2026-10-16, https://Www.google.com/chrome is 100% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://Www.google.com/chrome from mainland China since 2012-09-13.」
    - 來源：GreatFire，<https://en.greatfire.org/https/www.google.com/chrome>
- 事實：Google 的簡體中文 Chrome 下載頁 `https://www.google.cn/chrome` 最近 2 次有結論的測試都正常連線（0/2 受到干擾，最後一次 2026 年 9 月 29 日），GreatFire 的判定是可以連線。頁面大標題是「Google Chrome 网络浏览器」，頁面上有「下载 Chrome」的按鈕（2026-10-23 從台灣連線讀取頁面）
    - 照錄：「As of the last test on 2026-09-29, https://www.google.cn/chrome is not blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「All 2 recent conclusive tests connected normally.」
    - 來源：GreatFire，<https://en.greatfire.org/https/www.google.cn/chrome>。Google Chrome 网络浏览器，Google，<https://www.google.cn/chrome/>
- 事實：Apple 的 iTunes 查詢 API 在中國大陸的商店（`country=cn`）查得到 Google Chrome（App ID `535886823`，開發者 Google LLC），版本 156.0.8078.54（2026-10-22）。這是 API 的查詢結果，沒有查 Google Play
    - 來源：iTunes lookup API，<https://itunes.apple.com/lookup?id=535886823&country=cn>，查詢日 2026-10-23

## Firefox

- 事實：`https://www.mozilla.org` 最近 4 次有結論的測試都正常連線，GreatFire 的判定是可以連線。頁面標了「Verdict revised」，2026 年 10 月 21 日等 3 次連線被拒的測試沒有計入（見上面「GreatFire 的判定方式」），所以不要寫成「10 月 21 日的測試沒有被封鎖」。不帶 `www` 的 `https://mozilla.org` 頁面寫 17% 受到干擾，從 2014 年 11 月 18 日起有干擾紀錄，這一條沒有核對有結論的測試次數，不引用
    - 照錄：「All 4 recent conclusive tests connected normally.」
    - 照錄：「As of the last test on 2026-10-21, https://mozilla.org is 17% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 來源：GreatFire，<https://en.greatfire.org/https/www.mozilla.org>、<https://en.greatfire.org/https/mozilla.org>
- 事實：iTunes 查詢 API 在中國大陸的商店查得到 Firefox（App ID `989804926`，開發者 Mozilla Corporation，簡體中文名稱「Firefox 快速隐私浏览器」），版本 158.1（2026-10-19）
    - 來源：iTunes lookup API，<https://itunes.apple.com/lookup?id=989804926&country=cn>，查詢日 2026-10-23
- 查不到：`https://www.firefox.com.cn` 在 GreatFire 的最後一次判定是 2026 年 4 月 28 日，結果是部分受到干擾，頁面標示「No recent tests」，到 2026-10-23 約五個月沒有新的有結論的測試（2026 年 8 月 30 日那次連線被拒，沒有計入）。2026-10-23 從台灣連線也沒有取得頁面，這個網站目前的營運狀態沒有查證，不引用

## Tor Browser

- 事實：`https://www.torproject.org` 最近 3 次有結論的測試都被封鎖（3/3，最後一次 2026 年 10 月 16 日），從 2011 年 9 月 3 日起就有干擾紀錄
    - 照錄：「It's blocked — 100% of the last 3 conclusive tests failed in mainland China.」 <!-- docs-style-lint: disable-line -->
    - 照錄：「As of the last test on 2026-10-16, https://www.torproject.org is 100% blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://www.torproject.org from mainland China since 2011-09-03.」
    - 來源：GreatFire，<https://en.greatfire.org/https/www.torproject.org>
- 事實：Tor Project 支援頁所在的 `https://support.torproject.org`，GreatFire 的最後一次測試是 2026 年 5 月 7 日，結果是封鎖，從 2020 年 4 月 14 日起有干擾紀錄。頁面標示「No recent tests」，到 2026-10-23 約五個半月沒有新的測試（頁面自己寫成「6 mo ago」，是四捨五入）。引用時寫出測試日期
    - 照錄：「As of the last test on 2026-05-07 — 6 mo ago — it was blocked in mainland China. We haven't tested it since, so this may have changed.」 <!-- docs-style-lint: disable-line -->
    - 來源：GreatFire，<https://en.greatfire.org/https/support.torproject.org>
- 事實：Tor Project 的指紋保護說明頁有簡體中文版，大標題「指纹识别保护」
    - 來源：指纹识别保护 - 功能 - Tor 浏览器，Tor Project，<https://support.torproject.org/zh-CN/tor-browser/features/fingerprinting-protections/>，查詢日 2026-10-23

## Cover Your Tracks

- 事實：到 2026-10-23 查詢時，`https://coveryourtracks.eff.org` 在 GreatFire 此前 90 天只有 1 次有結論的測試，結果是正常連線（0/1）。頁面標了「Verdict revised」，2026 年 10 月 16 日那次連線被拒，沒有計入，不能寫成「10 月 16 日的測試沒有被封鎖」。只有 1 次，證據很薄
    - 照錄：「All 1 recent conclusive tests connected normally.」
    - 來源：GreatFire，<https://en.greatfire.org/https/coveryourtracks.eff.org>
