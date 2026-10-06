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
