# 亞洲各地對 Android 電視盒的官方警示

範圍是新加坡、香港、日本、馬來西亞、台灣與中國大陸的主管機關，對預載惡意程式或未認證的 Android 電視盒、機上盒有沒有公開的警示或通報。第一次整理是寫 anoni-net/news 的 XCPE 後門與住宅代理那篇的時候，查證日期 2026-11-08。只列法規與官方狀況，不列各地的感染統計。

## 新加坡

- 事實：新加坡警察部隊（SPF）與網路安全局（CSA）2025 年 11 月的聯合提醒，對象是未認證的電視盒，早於 Google 公布 XCPE 一年。內容提到受影響電視盒裡的惡意程式會把裝置變成殭屍網路的一部分，建議懷疑感染時立即斷網、掃描並移除可疑 App、檢查銀行等帳戶，報案前不要重設，沒有發現惡意程式與未授權交易時可以繼續使用或完整重設。可向 SingCERT 通報。提醒不是針對 XCPE 的建議
    - 照錄：「Certified Android TV boxes will support official, licensed applications such as Netflix and Disney+, while non-certified devices often support illegal streaming sites or distribute malicious applications.」
    - 照錄：「Malware present in affected TV boxes will infect users' devices with malicious applications, turning it into part of a botnet」
    - 照錄：「Do not perform a factory reset before reporting the incident to the police as this could hinder investigations」
    - 來源：Advisory On The Dangers Of Non-Certified Streaming Devices，新加坡警察部隊，<https://www.police.gov.sg/media-hub/news/2025/11/20251112_advisory_on_the_dangers_of_non_certified_streaming_devices>，日期取自網址（2025-11-12），頁面本文沒有標示

## 香港

- 事實：香港海關 2025 年 6 月 11 日及 25 日的特別執法行動，拘捕 2 人，檢獲 99 部涉及 10 多個品牌的電視機頂盒和特定應用程式，涉嫌違反《版權條例》。海關人員說明部分應用程式含木馬與間諜程式，提醒把這類機頂盒接上家中網路會危及個人私隱，也可能牽連其他連接裝置（原文用字為「間諜軟件」、「家居網絡」）。這是二手報導，海關新聞公報原文沒有取得
    - 照錄：「香港海關於6月11日及25日採取特別執法行動，打擊涉嫌銷售非法串流裝置，拘捕2名男子，並檢獲99部涉及10多個不同品牌的電視機頂盒和特定應用程式」
    - 來源（二手）：北角深水埗兩店售侵權機頂盒 標榜永久免費收看 海關拘2人，星島頭條，<https://www.stheadline.com/breaking-news/3468064/>，更新時間 2025-06-26
- 查不到：HKCERT 針對電視盒或 XCPE 的公告（2026-11-08 查）
- 查不到：unwire.hk 2026-11-05 的 XCPE 報導只抓到標題，沒有內文，不引用

## 日本

- 事實：日本警察廳（National Police Agency）是 Google 威脅情報團隊點名的合作單位之一
    - 照錄：「We worked closely with Japan's National Police Agency, Lumen, HUMAN Security, Plume, Synthient, and TrendAI to analyze this malware ecosystem and disrupt its operations.」
    - 來源：Shutting the Door on the XCPE Botnet，Google Threat Intelligence Group，<https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/>，2026-11-02
- 查不到：警察廳自己針對電視盒或 XCPE 的公告（2026-11-08 查）

## 馬來西亞

- 查不到：MCMC、CyberSecurity Malaysia 與 NACSA 針對電視盒惡意程式的公告（2026-11-08 查）
- 事實：The Star 2025-11-13 轉載新加坡的提醒，標題為「'Don't invite danger into your home'」。MCMC 2020 年曾警告供應商不得濫用 SIRIM 與 MCMC 標籤，內容是非法串流，與惡意程式無關。後者是二手來源（SoyaCincau，2020-02-15），原文沒有讀

## 台灣

- 查不到：TWCERT/CC、數位發展部、警政署與經濟部針對非認證電視盒或 XCPE 的公告（2026-11-08 查）
- 查不到：著作權法對侵權機上盒的規定，沒有取得官方文件，不寫

## 中國大陸

- 查不到：國家廣電總局、工信部、公安部與 CNCERT 針對預載惡意程式電視盒的通報，2025 至 2026 年均無結果（2026-11-08 查）
- 事實（二手）：廣電總局 2014 年整頓 OTT 盒子，要求牌照方關閉違規視頻軟體下載通道、未經批准的終端不得上市，針對的是內容與牌照。廣電總局的原文沒有讀到
    - 來源（二手）：前瞻網，〈广电总局加强整顿OTT盒子 乐视网/优酷/PPTV/腾讯视频TV版下架〉，2014-09-02，<https://www.qianzhan.com/indynews/detail/150/140902-2620ee3a.html>
- 事實：Videostrong 是深圳的公司（The Register 引述 Google）。中國主管機關對 Google 指控有無回應，查不到（2026-11-08 查）
- 事實：Google Play 在中國大陸的連線狀況見 `google-services-mainland-china.md`。GreatFire 到 2026-11-01 的測試，`https://play.google.com` 100% 被封鎖。大陸版 Android 電視盒是否另有認證查詢方式，查不到

## 手機的預載軟體

寫導讀歷史 11-15（2016 年的 Adups 預載更新軟體）時補上，範圍是手機，查證日期 2026-11-08。

- 查不到：台灣、香港、新加坡、日本對預載軟體蒐集個資的專門官方說明，電視盒的提醒不算在內。手機這一項的查詢沒有逐一列出查過的機關與頁面，不等於這些地方確認沒有
- 查不到：亞洲各國廉價 Android 手機預載事件的官方通報
- 查不到：BLU 手機在亞洲的銷售狀況
