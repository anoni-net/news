# Google 服務在中國大陸的連線狀況

範圍是 Gmail 等 Google 服務在中國大陸能不能直接連上。第一次整理是寫 anoni-net/news 的 Gmail 附件預覽釣魚那篇的時候，查證日期 2026-10-07。到這天為止，沒有找到 Google 官方說明 Gmail 在中國大陸能否使用的頁面，Google 透明度報告的流量頁需要 JavaScript，抓不到副本。

## Gmail

- 事實：2014 年 12 月底，Google 透明度報告顯示 Gmail 在中國的流量降到接近零。CSMonitor 當時寫到，這是中國的使用者第一次連透過 Outlook、Apple Mail 這類第三方程式也收不到 Gmail，用 VPN 仍然可以連上
    - 照錄：「According to Google's transparency reports, traffic to Gmail dropped sharply late Dec. 25th and remained near zero on Monday morning.」
    - 照錄：「this is the first time people in China have lost access to Gmail even through third-party programs such as Microsoft Outlook or Apple Mail.」、「It's still possible to access Gmail in China by using a VPN」
    - 來源（二手報導）：Gmail and Google Search access blocked in China，PBS NewsHour，<https://www.pbs.org/newshour/world/gmail-access-blocked-china>，2014-12-29。Gmail gets burned by China's 'Great Firewall'，CSMonitor，<https://www.csmonitor.com/Technology/2014/1229/Gmail-gets-burned-by-China-s-Great-Firewall>，2014-12-29
- 事實：長期量測防火長城的 GreatFire，到 2026 年 10 月 1 日的最後一次測試，`https://mail.google.com` 在中國大陸受到完全干擾，從 2011 年 12 月 27 日起就有干擾紀錄。`https://gmail.com` 到 10 月 4 日的測試是 94% 受到干擾。這是第三方的量測結果，不是官方資料，量的是網址能不能連線，沒有區分瀏覽器與 IMAP 等收信方式
    - 照錄：「As of the last test on 2026-10-01, https://mail.google.com is 100% disrupted in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://mail.google.com from mainland China since 2011-12-27.」
    - 照錄：「As of the last test on 2026-10-04, https://gmail.com is 94% disrupted in mainland China」
    - 來源：GreatFire，<https://en.greatfire.org/https/mail.google.com>、<https://en.greatfire.org/https/gmail.com>

## Google Play

查證日期 2026-10-18，寫 anoni-net/news 的 Signal 備份與 Android 密碼管理器搬移那篇時補上。

- 事實：GreatFire 到 2026 年 10 月 11 日的最後一次測試，`https://play.google.com` 在中國大陸 100% 被封鎖，從 2012 年 3 月 10 日起就有干擾紀錄。這是第三方的量測，量的是網址能不能連線
    - 照錄：「As of the last test on 2026-10-11, https://play.google.com is 100% blocked in mainland China, based on GreatFire's live Great Firewall measurements.」
    - 照錄：「GreatFire has recorded interference with https://play.google.com from mainland China since 2012-03-10.」
    - 來源：GreatFire，<https://en.greatfire.org/https/play.google.com>
- 事實：Android 的密碼管理器搬移（Credential Manager 的 Credentials Transfer API），開發者文件寫的呼叫端檢查以 Google Play 服務的系統元件為準。文件沒有寫沒有 Google Play 服務的手機能不能使用
    - 照錄：「the trusted system credential selector framework (on Android devices with Google Play services, "com.google.android.gms")」
    - 來源：Credential transfer，Android Developers，<https://developer.android.com/identity/sign-in/credential-transfer>，頁尾寫 Last updated 2026-10-16
- 查不到：Google 官方文件直接寫「中國大陸銷售的 Android 手機沒有 Google Play 服務」的頁面。找到的只有 2021 年的二手報導，描述特定廠商，也有說法指部分機型內建，所以不寫「中國大陸的 Android 手機都沒有 Google Play 服務」
