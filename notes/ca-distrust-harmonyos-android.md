# 憑證機構被移除信任時，HarmonyOS 與沒有 Google Play 服務的 Android

範圍是 eMudhra 中繼憑證私鑰外洩事件（Mozilla Bugzilla 2083449）的修正狀態裡，HarmonyOS 與沒有 Google Play 服務的 Android 這兩件事。第一次整理是寫 anoni-net/news 的 eMudhra 後續那篇，查證日期 2026-11-02。

## HarmonyOS 與 OpenHarmony

- 事實：研究者維護的說明頁「誰已修補」清單，把 OpenHarmony 與 HarmonyOS NEXT 列為尚未修正，寫到這類裝置不允許使用者停用系統根憑證。這份清單是研究者維護的，不是華為的公告
    - 照錄：「No user-side workaround is available on these devices until the patched version ships.」
    - 照錄：「If you are using HarmonyOS 4.3 and earlier, you can disable system-installed roots in the same way as on other Android-based systems.」
    - 來源：eMudhra Intermediate CA Compromise，eMudhra 事件說明頁，<https://emudhra.we-have-a-problem.com/>，頁面沒有寫文件日期，2026-11-02 查證
- 查不到：華為針對這次事件的官方說明。頁面也沒有列出針對台灣、香港、新加坡的系統或發行版

## 沒有 Google Play 服務的 Android

- 事實：說明頁寫 Google 的封鎖經由 Google Play 服務的更新管道送到許多 Android 裝置，並註明部分裝置不允許使用者停用系統根憑證
    - 照錄：「Many Android devices have automatically received an update blocking the affected certificates via the Google Play services update channel」
    - 照錄：「Some Android devices may not allow users to disable system-installed roots.」
    - 來源：eMudhra Intermediate CA Compromise，<https://emudhra.we-have-a-problem.com/>，頁面沒有寫文件日期，2026-11-02 查證
- 事實：GreatFire 到 2026-11-01 的最後一次測試，`https://play.google.com` 在中國大陸 100% 被封鎖。這是第三方量測，量的是網址能不能連線，不能據此確定裝置收不收得到更新
    - 照錄：「As of the last test on 2026-11-01, https://play.google.com is 100% blocked in mainland China」
    - 來源：Is https://play.google.com blocked in mainland China? — GreatFire，<https://en.greatfire.org/https/play.google.com>，頁面標示的最後測試日 2026-11-01，2026-11-02 查證。Google Play 的連線狀況另見 `google-services-mainland-china.md` <!-- docs-style-lint: disable-line -->
- 查不到：中國大陸銷售的 Android 手機有多少帶有 Google Play 服務，所以稿件只寫「沒有 Google Play 服務的裝置」，不寫大陸的手機都沒有
