# SimpleX 在中國大陸的取得狀況

範圍是從中國大陸取得 SimpleX Chat 與購買支持者徽章的入口，最後一節另列台灣、香港、日本、新加坡的 App Store 上架狀態當作對照。第一次整理是寫 anoni-net/news 的 SimpleX 支持者徽章那篇的時候，查證日期 2026-11-21。

## 中國大陸

- 事實：長期量測防火長城的 GreatFire，到 2026-11-17 的最後一次測試，`https://simplex.chat` 在中國大陸 100% 被封鎖。頁面寫最近 1 次有結論的測試失敗，樣本很少，引用時寫出日期與只有 1 次。徽章購買頁與官網下載都在這個網域
    - 照錄：「As of the last test on 2026-11-17, https://simplex.chat is 100% blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://simplex.chat from mainland China since 2023-04-14.」
    - 來源：Is https://simplex.chat blocked in mainland China? — GreatFire，<https://en.greatfire.org/https/simplex.chat>，查詢 2026-11-21 <!-- docs-style-lint: disable-line -->
- 事實：以 iTunes API 用 id `1605771084` 查 country=cn，resultCount 為 0。以 simplex chat 搜尋 country=cn，只出現名為 SimpleChat 的另一個 App（id `6504841658`）。這是 API 結果，不等於 Apple 的公告，也不代表曾被要求下架（下架程序見 `app-store-removal-asia.md`）
    - 來源：iTunes Search API，<https://itunes.apple.com/lookup?id=1605771084&country=cn>，查詢 2026-11-21
- 相關：play.google.com 見 `google-services-mainland-china.md`，github.com 見 `github-access-mainland-china.md`
- 查不到：f-droid.org 的連線量測、GitHub Releases 下載路徑的量測，以及徽章 App 內購買在各地能不能用（說明頁沒有列地區限制）

## 台灣、香港、日本、新加坡（App Store 對照）

- 事實：以 iTunes API 用 id `1605771084` 查 country=tw、hk、jp、sg，各回傳 1 筆 SimpleX Chat: secure messenger，版本 7.1.4。這是 API 結果，只代表 App 在這些地方的 App Store 上架，不代表徽章的 App 內購買在當地可用（說明頁沒有列地區限制，查不到）
    - 來源：iTunes Search API，<https://itunes.apple.com/lookup?id=1605771084&country=tw>、<https://itunes.apple.com/lookup?id=1605771084&country=hk>、<https://itunes.apple.com/lookup?id=1605771084&country=jp>、<https://itunes.apple.com/lookup?id=1605771084&country=sg>，查詢 2026-11-21
