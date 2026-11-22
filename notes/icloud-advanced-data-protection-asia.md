# iCloud 進階資料保護的地區可用性

範圍是 Apple 的 iCloud 進階資料保護（ADP）在亞洲各地能不能開啟，以及 Apple 對地區限制的公開說法。第一次整理是寫英國調查權力法庭對 Apple 技術能力通知判決那篇（`posts/2026-11-24-uk-apple-encryption-order.md`）的時候，查證日期都是 2026-11-21。

## 全球

- 事實：Apple 的英國說明頁寫明英國的新使用者不能再開啟 ADP，英國以外的地方繼續提供。這是查到的唯一一句全球性陳述，沒有查到 Apple 逐地區的 ADP 可用性列表。查過的是 iOS 與 iPadOS 27 的「功能可用性」頁（美國、台灣、香港、中國大陸四個版本），都沒有 ADP 的條目
    - 照錄：「Advanced Data Protection continues to be available everywhere else in the world.」
    - 來源：Apple can no longer offer Advanced Data Protection in the United Kingdom to new users，Apple，<https://support.apple.com/en-us/122234>，2025-09-22
- 事實：開啟 ADP 前要先設定復原聯絡人或復原密鑰，開啟後 Apple 沒有協助復原端對端加密資料所需的密鑰。管理式 Apple 帳號與兒童帳號不能開啟
    - 照錄：「Managed Apple Accounts and child accounts are not eligible for Advanced Data Protection.」
    - 來源：How to turn on Advanced Data Protection for iCloud，Apple，<https://support.apple.com/en-us/108756>，2026-04-17

## 台灣

- 事實：Apple 台灣的正體中文說明頁寫了跟英文版相同的開啟步驟，頁面沒有寫地區限制。台灣「可以開啟」的依據只有這一頁加上英國說明頁的全球陳述
    - 照錄：「如果你選擇啟用「進階資料保護」，你的大部分 iCloud 資料（包括「iCloud 備份」、「照片」、「備忘錄」等等）均會使用端對端加密保護。」
    - 來源：如何開啟「iCloud 進階資料保護」，Apple，<https://support.apple.com/zh-tw/108756>，2026-04-24

## 香港

- 事實：Apple 香港的正體中文說明頁寫了跟英文版相同的開啟步驟，頁面沒有寫地區限制。依據的程度跟台灣相同
    - 照錄：「如選擇啟用「iCloud 進階資料保護」，你大部分 iCloud 資料 (包括「iCloud 備份」、「相片」、「備忘錄」等) 均會受點對點加密保護。」
    - 來源：如何開啟「iCloud 進階資料保護」，Apple，<https://support.apple.com/zh-hk/108756>，2026-04-24

## 中國大陸

- 事實：iCloud 在中國大陸由雲上貴州營運，資料存放在中國境內（照錄與來源見 `passkeys-asia.md` 的中國大陸一節）。英文版說明頁另外寫明 iCloud 的服務與資料受雲上貴州的條款規範
    - 照錄：「iCloud in China mainland is operated by GCBD (AIPO Cloud (Guizhou) Technology Co. Ltd).」
    - 來源：Learn more about iCloud in China mainland，Apple，<https://support.apple.com/en-us/111754>，2025-04-15
- 查不到：Apple 對 ADP 在雲上貴州營運的 iCloud 帳號能不能開啟的說法。簡體中文的開啟說明頁（<https://support.apple.com/zh-cn/108756>，2026-04-24）寫了相同的步驟，沒有寫可用，也沒有寫不可用。沒有查到第三方的一手報導，不能寫成可用或不可用
