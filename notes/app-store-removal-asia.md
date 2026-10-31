# 政府要求 App 商店下架特定 App 的規定與實例

範圍是政府要求 App 商店下架特定 App 時引用的法規、命令公不公開，以及開發者與使用者有沒有說明或救濟的程序，包含中國大陸、台灣、香港三個地方。網站與 DNS 的封鎖寫在 `vpn-and-site-blocking.md`，網路內容的處置程序寫在 `online-content-categories-asia.md`，這份不重複。第一次整理是寫 anoni-net/news 的 Bitchat 在印度下架那篇導讀的時候，查證日期 2026-10-31。

各條的 App Store 上架狀態用 Apple 的 iTunes 查詢 API（`itunes.apple.com/lookup`，帶 `id` 與 `country`）查詢，這是 API 的回傳結果，不等於 Apple 或開發者的公告。不寫哪個地區、哪個族群的人在用什麼工具。

## 中國大陸

- 事實：Apple 2026-02-28 通知 Bitchat 的開發者，依國家網信辦（CAC）的要求從中國的 App Store 下架，通知引用《具有舆论属性或社会动员能力的互联网信息服务安全评估规定》第三條，沒有寫違反哪一款，也沒有附命令本身。開發者 2026-04-05 在 X 公開通知截圖
    - 照錄：「We are writing to notify you that your application, per demand from the CAC (Cyberspace Administration of China), will be removed from the China App Store because it includes content that is illegal in China, which is not in compliance with the App Review Guidelines:」
    - 照錄：「According to the CAC, your app violates Articles 3 of the Provisions on the Security Assessment of Internet-based Information Services with Attribute of Public Opinions or Capable of Social Mobilization (具有舆论属性或社会动员能力的互联网信息服务安全评估规定).」
    - 來源（一手，當事人公開的平台通知）：開發者的 X 貼文 <https://x.com/jack/status/2040924565111537983>，UTC 2026-04-05 22:48:29
    - 來源（二手）：GIGAZINE，Bitchat, a P2P chat app created by the founder of Twitter, has been removed from the Chinese App Store.，<https://gigazine.net/gsc_news/en/20260406-bitchat-pulled-china-app-store/>，2026-04-06
    - 查證日期：2026-10-31
- 事實：iTunes 查詢 API 在 `country=cn` 查不到 Bitchat（`id=6748219622`），`country=tw`、`hk`、`us`、`jp` 各查到 1 筆
    - 查證日期：2026-10-31
- 事實：《具有舆论属性或社会动员能力的互联网信息服务安全评估规定》2018-11-30 施行。第三條要求互聯網信息服務提供者在服務上線、增設相關功能、用戶規模顯著增加等情形下自行開展安全評估，並對評估結果負責。條文沒有出現「下架」與「应用商店」 <!-- docs-style-lint: disable-line -->
    - 照錄：「互联网信息服务提供者具有下列情形之一的，应当依照本规定自行开展安全评估，并对评估结果负责：（一）具有舆论属性或社会动员能力的信息服务上线，或者信息服务增设相关功能的；」（第三條，後面另有四款） <!-- docs-style-lint: disable-line -->
    - 照錄：「本规定自2018年11月30日起施行。」（第十七條）
    - 來源（一手）：中國網信網，<https://www.cac.gov.cn/2018-11/15/c_1123716072.htm>，頁面日期 2018-11-15，頁面本文沒有列出發布機關
    - 查證日期：2026-10-31
- 事實：同一份規定對沒有開展評估的提供者，寫的是網信部門和公安機關先通知其開展評估（第十二條），拒不開展的經全國互聯網安全管理服務平台向公眾提示安全風險，並依職責監督檢查、依法處理違法行為（第十三條）。逐條讀過全文（第一到第十七條），沒有出現「下架」、「申诉」、「复议」與「法院」，條文沒有寫到下架前讓提供者說明或事後申訴的程序。一般的行政復議與行政訴訟規定這次沒有查，引用時寫成「這份規定本身沒有寫」 <!-- docs-style-lint: disable-line -->
    - 照錄：「发现具有舆论属性或社会动员能力的互联网信息服务提供者未按本规定开展安全评估的，网信部门和公安机关应当通知其按本规定开展安全评估。」（第十二條第 2 項） <!-- docs-style-lint: disable-line -->
    - 照錄：「网信部门和公安机关发现具有舆论属性或社会动员能力的互联网信息服务提供者拒不按照本规定开展安全评估的，应当通过全国互联网安全管理服务平台向公众提示该互联网信息服务存在安全风险，并依照各自职责对该互联网信息服务实施监督检查，发现存在违法行为的，应当依法处理。」（第十三條） <!-- docs-style-lint: disable-line -->
    - 來源（一手）：同上
    - 查證日期：2026-10-31
- 事實：《網絡安全法》2025 年修正版（2026-01-01 施行）第五十條第一款禁止任何個人和組織提供的應用軟體含有法律、行政法規禁止發布或者傳輸的資訊，第二款要求應用軟體下載服務提供者知道其用戶有這類行為時停止提供服務、採取消除等處置措施、保存記錄並向主管部門報告。條文沒有寫法院程序 <!-- docs-style-lint: disable-line -->
    - 照錄：「任何个人和组织发送的电子信息、提供的应用软件，不得设置恶意程序，不得含有法律、行政法规禁止发布或者传输的信息。」（第五十條第一款） <!-- docs-style-lint: disable-line -->
    - 照錄：「电子信息发送服务提供者和应用软件下载服务提供者，应当履行安全管理义务，知道其用户有前款规定行为的，应当停止提供服务，采取消除等处置措施，保存有关记录，并向有关主管部门报告。」（第五十條第二款） <!-- docs-style-lint: disable-line -->
    - 來源（一手）：中华人民共和国网络安全法（2025 年修正版），中國網信網，<https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm>。施行日期見 `vpn-and-site-blocking.md` 的 CN-5
    - 查證日期：2026-10-31
- 事實：同法第六十九條第三款規定，應用軟體下載服務提供者不履行第五十條第二款的義務，依同條前兩款處罰：由主管部門責令改正、警告、通報，可處五萬到五十萬元罰款；拒不改正或情節嚴重的處五十萬到二百萬元，並可責令暫停相關業務、停業整頓、關閉網站或者應用程序、吊銷許可證或營業執照。處罰的對象是不履行義務的下載服務提供者 <!-- docs-style-lint: disable-line -->
    - 照錄：「电子信息发送服务提供者、应用软件下载服务提供者，不履行本法第五十条第二款规定的安全管理义务的，依照前两款规定处罚。」（第六十九條第三款） <!-- docs-style-lint: disable-line -->
    - 照錄：「拒不改正或者情节严重的，处五十万元以上二百万元以下罚款，并可以责令暂停相关业务、停业整顿、关闭网站或者应用程序、吊销相关业务许可证或者吊销营业执照」（第六十九條第一款節錄） <!-- docs-style-lint: disable-line -->
    - 來源（一手）：同上
    - 查證日期：2026-10-31
- 查不到：國家網信辦對 Bitchat 下架的公開命令、期限與說明，以及開發者有沒有收過評估規定第十二條的通知
- 境外來源資訊的阻斷見 `vpn-and-site-blocking.md` 的 CN-5（《網絡安全法》第五十二條）。Apple 的通知沒有引用第五十條、第五十二條或第六十九條

## 台灣

- 事實：《詐欺犯罪危害防制條例》第 42 條讓各目的事業主管機關或司法警察機關在詐欺犯罪防制緊急案件中，命網際網路接取服務提供者停止解析或限制接取。處置的對象是網路接取業者，條文沒有出現「下架」與 App 商店
    - 照錄：「為處理詐欺犯罪防制緊急案件，及時防制民眾接觸詐欺網站，各目的事業主管機關或司法警察機關認有即時處置之必要時，得令網際網路接取服務提供者為停止解析或限制接取之處置。」（第 42 條）
    - 來源（一手）：詐欺犯罪危害防制條例，全國法規資料庫，<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080226>，頁面標示修正日期民國 115 年 01 月 21 日
    - 查證日期：2026-10-31
- 事實（二手）：內政部 2025-12-04 公開宣布依第 42 條對小紅書發布停止解析與限制接取的命令，暫定一年。報導沒有提到 Apple 或 Google 在台灣下架
    - 照錄：「內政部將對「小紅書」APP發布網際網路停止解析及限制接取之命令，暫定期間一年。」
    - 來源（二手）：NOWnews，台灣將封鎖小紅書一年！刑事局揭違規內幕 300萬用戶影響一次看，<https://www.nownews.com/news/6761411>，2025-12-04
    - 查證日期：2026-10-31
- 查不到：授權政府命令 App 商店下架特定 App 的條文。這次只查了詐欺條例與《著作權法》（見 `vpn-and-site-blocking.md` 的 TW-1），沒有窮盡搜尋
- 事實：iTunes 查詢 API 在 `country=tw` 查得到 Bitchat
    - 查證日期：2026-10-31

## 香港

- 查不到：授權政府命令 App 商店下架特定 App 的條文。國安法實施細則附表 4（以下各條依 2020 年公布的版本，之後的修訂沒有核對） 針對的是電子平台上的電子訊息（見 `vpn-and-site-blocking.md` 的 HK-4 與 `online-content-categories-asia.md` 的「香港」），條文沒有出現應用程式商店。附表 4 的「平台服務商」是否涵蓋 App 商店，這次沒有核對，引用時不要寫成條文涵蓋
- 事實：iTunes 查詢 API 在 `country=hk` 查得到 Bitchat
    - 查證日期：2026-10-31
- 事實：附表 4 第 15 條規定本附表的要求或通知須以書面發出，送到當事人提供的收信地址（包含電郵地址與傳真號碼），沒有提供地址時以電子訊息發送。附表 4 沒有寫到向發布者或服務商說明理由或提供上訴途徑（見 `online-content-categories-asia.md` 的「香港」）。一般的司法覆核這次沒有查，引用時寫成「附表 4 本身沒有寫」
    - 照錄：「A requirement or notification under this Schedule must be in writing.」（附表 4 第 15(1) 條）
    - 照錄：「it is sent to the person at an address (including an email address and fax number) provided by the person for receiving correspondences; or」（附表 4 第 15(2)(a) 條）
    - 來源（一手）：L.N. 139 of 2020，Schedule 4，<https://www.gld.gov.hk/egazette/pdf/20202449e/cs220202449139.pdf>（用網路檔案館副本 <https://web.archive.org/web/2021id_/https://www.gld.gov.hk/egazette/pdf/20202449e/cs220202449139.pdf>）
    - 查證日期：2026-10-31
- 事實：附表 4 第 12 條，服務商不遵從第 7 條的要求構成罪行，但可以用「指明辯解」（specified excuse）抗辯。辯解成立的情形是無法合理期望服務商遵從，原因是服務商無法合理取得遵從所需的科技，或遵從會招致第三方蒙受重大損失或權利受到重大損害的風險。舉證門檻是提出足夠證據引起爭議，而控方未能在無合理疑點下證明相反
    - 照錄：「It is a defence for a service provider charged under subsection (1) for a failure to comply with a requirement issued under section 7 of this Schedule to show that the service provider had a specified excuse for the failure.」（附表 4 第 12(2) 條）
    - 照錄：「(a) sufficient evidence is adduced to raise an issue that the defendant had such an excuse; and (b) the contrary is not proved by the prosecution beyond reasonable doubt.」（附表 4 第 12(3) 條）
    - 照錄：「the technology necessary for complying with the requirement was not reasonably available to the service provider; or (b) there was a risk of incurring substantial loss to, or otherwise substantially prejudicing the right of, a third party.」（附表 4 第 12(4) 條）
    - 來源（一手）：同上
    - 查證日期：2026-10-31
