# GrapheneOS 與 Pixel 在亞洲各地的取得與更新

範圍是 Pixel 在亞洲各地能不能從 Google Store 購買、GrapheneOS 的安裝與更新伺服器在中國大陸的連線量測，以及 GrapheneOS 設定程式的中文語系。第一次整理是寫 anoni-net/news 的 GrapheneOS 剪貼簿讀取開關那篇的時候，查證日期 2026-10-23。

## Google Store 的 Pixel 銷售地區

- 事實：Google Store 說明頁列出可以在 Google Store 購買各款 Pixel 的地區。Pixel 10a 的清單裡，亞洲有印度、日本、新加坡與台灣，沒有中國大陸、香港、澳門與南韓。這一頁只涵蓋 Google Store 本身，不代表其他零售通路或電信業者沒有販售
    - 照錄：「Here's where you can find devices available for purchase on the Google Store.」
    - 照錄（Pixel 10a）：「Australia, Austria, Belgium, Canada, Czech Republic, Denmark, Finland, France, Germany, India, Ireland, Italy, Japan, Netherlands, Norway, Poland, Portugal, Singapore, Spain, Sweden, Switzerland, Taiwan, United Kingdom, United States (except Puerto Rico)」
    - 照錄：「To buy a device from the Google Store, your shipping address must be in the same region as the Google Store site you want to buy it from.」
    - 來源：Learn about devices & services available in your region，Google Store Help，<https://support.google.com/store/answer/2462844?hl=en>，頁面沒有標示日期
- 事實：同一頁的 Pixel 10、Pixel 9a、Pixel 9 系列與 Pixel 11 系列，亞洲的地區與 Pixel 10a 相同，都是印度、日本、新加坡與台灣
    - 來源同上
- 查不到：Google 官方說明「Pixel 不在中國大陸銷售」的頁面。只能寫 Google Store 的清單裡沒有中國大陸，不寫 Pixel 在中國大陸沒有任何販售管道

## GrapheneOS 的安裝與更新伺服器

- 事實：GrapheneOS 的系統更新程式從 `releases.grapheneos.org` 取得更新資訊與下載更新檔，App 商店使用的 `apps.grapheneos.org` 是同一組伺服器的另一個名稱
    - 照錄：「The GrapheneOS System Updater app fetches update metadata from https://releases.grapheneos.org/DEVICE-CHANNEL approximately once every six hours when connected to a permitted network for updates.」
    - 照錄：「Once an update is available, it tries to download https://releases.grapheneos.org/DEVICE-incremental-OLD_VERSION-NEW_VERSION.zip for a delta update, and then falls back to https://releases.grapheneos.org/DEVICE-ota_update-NEW_VERSION.zip.」
    - 照錄：「The GrapheneOS app repository client (App Store) fetches generic signed update metadata and signed package updates (APKs) from https://apps.grapheneos.org/ (a separate name for the same servers as https://releases.grapheneos.org).」
    - 來源：Frequently Asked Questions | GrapheneOS，<https://grapheneos.org/faq#default-connections>
- 事實：官方網頁安裝器的程式碼把下載來源設為 `releases.grapheneos.org`。這是從程式碼讀出來的，安裝頁的說明文字沒有寫下載來源
    - 照錄：`const t="https://releases.grapheneos.org"`
    - 來源：<https://grapheneos.org/js/f0b77f84.web-install.js>（由 Web installer | Install | GrapheneOS，<https://grapheneos.org/install/web> 載入）
- 事實：長期量測防火長城的 GreatFire，到 2026 年 10 月 2 日的最後一次測試，`https://releases.grapheneos.org` 在中國大陸受到干擾，從 2026 年 1 月 31 日起有干擾紀錄。過去 90 天只有 1 次有結果的測試。這是第三方的量測，不是官方資料
    - 照錄：「As of the last test on 2026-10-02, https://releases.grapheneos.org is 100% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「Access is unreliable — 100% of the last 1 conclusive tests showed interference.」 <!-- docs-style-lint: disable-line -->
    - 照錄：「GreatFire has recorded interference with https://releases.grapheneos.org from mainland China since 2026-01-31.」
    - 來源：Is https://releases.grapheneos.org blocked in mainland China?，GreatFire，<https://en.greatfire.org/https/releases.grapheneos.org>
- 推論：在中國大陸直接連線時，系統更新可能無法順利下載。GreatFire 測的是根網址，不是更新檔的路徑，90 天內也只有 1 次有結果的測試
- 事實：同一個量測，官方網站 `https://grapheneos.org` 到 2026 年 8 月 19 日的最後一次測試沒有被封鎖
    - 照錄：「As of the last test on 2026-08-19, https://grapheneos.org is not blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 來源：Is https://grapheneos.org blocked in mainland China?，GreatFire，<https://en.greatfire.org/https/grapheneos.org>
- 查不到：GrapheneOS 官方對中國大陸連線狀況的說明，以及在中國大陸實際安裝或更新的結果

## GrapheneOS 設定程式的中文語系

- 事實：GrapheneOS 的設定程式（`platform_packages_apps_Settings`，標籤 `2026102100`）有 `values-zh-rCN`、`values-zh-rTW` 與 `values-zh-rHK` 三個中文目錄，裡面是 `arrays.xml`、`config.xml` 與 `strings.xml`，也就是從 Android 開源專案（AOSP）沿用的字串。GrapheneOS 新增的字串放在 `res/values/strings_ext.xml`，整個 repo 只有這一份，沒有任何語系的翻譯版本
    - 來源：GrapheneOS/platform_packages_apps_Settings，GitHub，<https://github.com/GrapheneOS/platform_packages_apps_Settings/tree/2026102100/res>，以 GitHub API 列出標籤 `2026102100` 的完整檔案樹
- 事實：GrapheneOS 官方論壇的管理者回覆寫到，GrapheneOS 自己新增的設定與 App 目前只有英文。回覆的發文日期頁面上沒有顯示
    - 照錄：「Currently, GrapheneOS-specific settings and apps developed by GrapheneOS are in English only.」
    - 來源：GrapheneOS translate to other languages - GrapheneOS Discussion Forum，<https://discuss.grapheneos.org/d/5030-grapheneos-translate-to-other-languages>
- 推論：系統設定裡沿用 AOSP 的部分，在簡體中文與正體中文系統上會顯示中文，GrapheneOS 新增的畫面（例如剪貼簿存取的設定）顯示英文。這是從檔案目錄推出來的，沒有在實機確認
