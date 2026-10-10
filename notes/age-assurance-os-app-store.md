# 作業系統與 App 商店層級的年齡驗證規定

範圍是法規把年齡相關的義務放在作業系統（終端裝置）或 App 商店這一層的規定，包含新加坡、中國大陸、日本三個地方。只記法規與制度的文字，不記各地使用者如何使用工具。第一次整理是寫 anoni-net/news 的加州 AB 1856 開源作業系統豁免那篇導讀的時候，查證日期 2026-10-07。

三個地方的規定各自處理不同的事。新加坡管 App 商店的年齡確認，中國大陸管終端的未成年人模式，日本管手機販售時的內容過濾。三者的文件都沒有寫出加州 AB 1043 那種「作業系統在帳號設定時蒐集年齡，再用 API 把年齡範圍傳給 App」的設計，各地的條目另寫明文件裡有沒有對應的條文。

## 新加坡

- 事實：資訊通信媒體發展局（IMDA）依廣播法（Broadcasting Act 1994）第 45L 條發布《Code of Practice for Online Safety – App Distribution Services》，2025 年 3 月 31 日生效，適用於依該法第 45K(1) 條指定的 App 發行服務（App Distribution Services，簡稱 ADS）
    - 照錄：「This Code is called the Code of Practice for Online Safety – App Distribution Services and shall come into effect on 31 March 2025.」
    - 照錄：「This Code applies to App Distribution Services which are designated/will be designated under section 45K(1) of the Broadcasting Act 1994.」
    - 來源（一手）：IMDA，Code of Practice for Online Safety – App Distribution Services，<https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/regulations/codes-of-practice/code-of-practice-app-distribution-services/code-of-practice-for-online-safety-app-distribution-services.pdf>
- 事實：被指定的對象是 Apple App Store、Google Play Store、Huawei AppGallery、Microsoft Store、Samsung Galaxy Store 五個 App 商店
    - 照錄：「IMDA will require designated ADSs with significant reach or impact, namely Apple App Store, Google Play Store, Huawei App Gallery, Microsoft Store and Samsung Galaxy Store, to put in place system-level measures to curtail the risk of exposure to harmful content for users, especially children.」
    - 來源（一手）：IMDA 新聞稿，New Online Safety Code of Practice for App Distribution Services Enhances Protection for Singapore Users，2025-01-15，<https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/online-safety-code-of-practice-for-app-distribution-services>
    - IMDA 的 Keeping Young Users Safe Online 頁面（見下方第五條）在 2026-04-06 更新的段落仍列這五個商店
- 事實：Code 要求 App 商店提供未成年人的差異化帳號，並用年齡驗證或其他年齡確認（age assurance）方式，以合理的準確度判定帳號使用者的年齡或年齡範圍。Code 把未成年人（child）定義為未滿 18 歲
    - 照錄：「the provider of the Service must have in place systems and processes, including age verification, or other means of age assurance, such that the age or age range of an ADS user of an account on the Service can be established with reasonable accuracy.」（第 20 段）
    - 照錄：「“child” means an individual who is below 18 years of age.」（第 6(e) 段）
    - 照錄：「If the provider of the Service has yet to implement age assurance systems and processes, it must set out an implementation plan ... The implementation plan and timeline, including any subsequent variation, is subject to agreement by IMDA.」（第 21 段）
    - 年齡確認要依個人資料保護法（PDPA）辦理，Code 寫明「organisations should practice data minimisation for age assurance purposes」（第 20 段）
    - 來源（一手）：同上一條的 Code 全文
- 事實：IMDA 的說明文件寫明 App 商店可自行選擇年齡估計、年齡驗證或兩者並用，起步要求是擋住最高年齡分級（例如 18+）的 App
    - 照錄：「Designated ADSs can decide the appropriate age assurance measure(s) – either age estimation, age verification, or both – for their services.」
    - 照錄：「For a start, designated ADSs are expected to prevent children from accessing its highest age rated apps, e.g. 18+」
    - 來源（一手）：IMDA，Factsheet on Age Assurance under the ADS Code，<https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2025/01/ads-code/factsheet-on-age-assurance.pdf>，隨 2025-01-15 新聞稿發布
- 事實：App 商店實施年齡確認的期限是 2026 年 3 月 31 日，自 4 月 1 日起適用。至少要能判斷使用者是否未滿 18 歲
    - 照錄：「Designated app stores are expected to implement these age assurance measures by 31 March 2026. At the outset, they are required to be able to minimally ascertain whether users are under 18.」（數位發展及新聞部答覆國會質詢，2025-10-14）
    - 照錄：「From 1 April 2026, designated app stores in Singapore are required to implement age assurance measures to prevent users younger than 18 from accessing and downloading age-inappropriate apps.」（IMDA 網頁）
    - IMDA 網頁列的檢查方式有三種，第一種是 App 商店用 Singpass、身分證或護照查生日，第二種是用 AI 做臉部或聲音的年齡估計
    - 來源（一手）：MDDI's Response to PQ on Update on Study On Effectiveness of Mandating Age Limits for Social Media Access，2025-10-14，<https://www.mddi.gov.sg/newsroom/mddi-s-response-to-pq-on-update-on-study-on-effectiveness-of-mandating-age-limits-for-social-media-access/>。IMDA，Keeping Young Users Safe Online，頁面資料的發布日 2026-02-12、最後更新 2026-04-22，<https://www.imda.gov.sg/how-we-can-help/age-assurance>
- 事實：Code 的適用對象只有 App 發行服務，Code 全文沒有出現 operating system 一詞，也沒有要求作業系統提供者蒐集年齡或向 App 傳送年齡訊號。年齡確認發生在 App 商店的帳號與下載流程
    - 來源（一手）：同第一條的 Code 全文。以全文搜尋 operating system 的結果為準，未命中
- 查不到：Code 本文沒有寫罰則，罰則的依據在廣播法，本次沒有查廣播法的條文。各 App 商店實際採用哪種方式，本次只看到 IMDA 頁面的概述，沒有逐一查證各商店的公告

## 中國大陸

- 事實：《未成年人網絡保護條例》（國務院令第 766 號，2023 年 10 月 24 日公布，2024 年 1 月 1 日施行）要求智能終端產品制造者在產品出廠前安裝未成年人網路保護軟體，或用顯著方式告知用戶安裝渠道與方法。條例把智能終端產品定義為具有操作系統、可由用戶自行安裝應用軟體的手機與計算機等網路終端產品 <!-- docs-style-lint: disable-line -->
    - 照錄：「智能终端产品制造者应当在产品出厂前安装未成年人网络保护软件，或者采用显著方式告知用户安装渠道和方法。智能终端产品销售者在产品销售前应当采用显著方式告知用户安装未成年人网络保护软件的情况以及安装渠道和方法。」（第十九条第三款）
    - 照錄：「本条例所称智能终端产品，是指可以接入网络、具有操作系统、能够由用户自行安装应用软件的手机、计算机等网络终端产品。」（第五十九条）
    - 來源（一手）：中華人民共和國國務院，《未成年人网络保护条例》，<https://www.gov.cn/zhengce/content/202310/content_6911288.htm>
    - 條例的義務對象是終端的製造者與銷售者，不是操作系統的開發者。條例沒有寫 App 商店要確認用戶年齡
- 事實：國家互聯網信息辦公室（國家網信辦）2024 年 11 月 15 日發布《移动互联网未成年人模式建设指南》（以下簡稱《指南》），適用對象是移動智能終端、應用程序與應用程序分發平台，要求三者聯動提供未成年人模式
    - 照錄：「本指南主要面向移动智能终端、移动互联网应用程序（以下简称“应用程序”）、移动互联网应用程序分发平台（以下简称“应用程序分发平台”），提出未成年人模式建设的总体方案」
    - 照錄：「移动智能终端、应用程序、应用程序分发平台之间通过必要接口和数据共享，实现三方联动」、「在移动智能终端一键启动/退出未成年人模式后，应用程序、应用程序分发平台自动同步切换。」
    - 來源（一手）：國家網信辦，移动互联网未成年人模式建设指南，2024-11-15，<https://www.cac.gov.cn/2024-11/15/c_1733364304749288.htm>。發布說明：國家互聯網信息辦公室發布《移动互联网未成年人模式建设指南》，2024-11-15，<https://www.cac.gov.cn/2024-11/15/c_1733364304722026.htm>
- 事實：《指南》的性質是指引，用詞是「应当对标《未成年人网络保护条例》要求，结合自身发展实际，积极探索推进未成年人模式建设」，文中沒有寫施行日期與罰則
    - 來源（一手）：同上《指南》全文
- 事實：《指南》對終端的要求包含三項。第一，入口至少要有開機提醒、桌面圖標、系統設置三種方式。第二，首次進入模式時，終端要提供設置生日、選擇年齡或年齡區間的方式。第三，退出模式要家長驗證，預設的使用時長依年齡分級，未滿 16 歲預設推薦總時長不超過 1 小時，16 歲以上未滿 18 歲不超過 2 小時，每日 22 時至次日 6 時預設不提供服務
    - 照錄：「用户在首次登录未成年人模式时，移动智能终端应当在入口提供设置生日、选择年龄或年龄区间等多种方式供用户自行选择，并允许设置多个未成年人用户。」
    - 照錄：「退出未成年人模式，需要家长进行验证同意。」
    - 照錄：「在未成年人模式下，移动智能终端每日22时至次日6时期间默认不向未成年人提供服务，同时提供家长豁免操作」
    - 來源（一手）：同上《指南》全文，第四章
- 事實：《指南》對應用程序分發平台的要求是設立未成年人專區，審核在未成年人模式下上架與更新的應用程序，評估應用程序的適齡範圍並在顯著位置標註推薦年齡
    - 照錄：「应用程序分发平台应当提供未成年人专区」
    - 照錄：「科学评估应用程序适龄范围，并在显著位置标注应用程序推荐年龄。」
    - 來源（一手）：同上《指南》全文，第六章
- 事實：《指南》沒有規定終端向 App 傳送年齡訊號的格式。終端與 App、分發平台之間的資料交換只寫到「必要接口和数据共享」，年齡區間（第四章）是模式內的設定，條文沒有寫成對 App 的 API
    - 來源（一手）：同上《指南》全文。以全文閱讀為準
- 事實：2026 年 9 月 18 日國家網信辦公開徵求意見《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》，意見反饋截止日 2026 年 10 月 17 日。草案第十條要求智能終端產品制造者設置未成年人模式的聯動、一鍵切換、退出核驗與防繞過等功能，應用程序分發平台對不符合適用年齡的應用程序要限制下載與安裝。草案的施行日期欄位空白（「自2026年 月 日起施行」）
    - 照錄：「智能终端产品制造者应当为智能终端产品设置未成年人模式联动、一键切换、退出核验、防绕过以及使用时段、时长、功能和内容管理等功能。」
    - 照錄：「对于不符合应用程序适用年龄的，应当限制下载、安装该应用程序。」
    - 照錄：「国务院电信主管部门将移动智能终端未成年人模式纳入电信设备进网许可检测，会同国家网信部门制定移动智能终端未成年人模式电信设备进网许可检测项目。」（第十二條第三款）
    - 草案全文沒有出現「操作系统」一詞，義務對象寫的是智能終端產品制造者。草案另要求提供未成年人模式的終端製造者向省級網信部門備案
    - 來源（一手，草案）：國家網信辦，关于《国务院关于保障未成年人健康安全使用网络的规定（征求意见稿）》公开征求意见的通知，2026-09-18，<https://www.cac.gov.cn/2026-09/18/c_1791482017777471.htm>
- 查不到：《指南》發布後各手機廠商實際預置未成年人模式的現況，以及草案是否已定稿，本次沒有找到一手資料。《指南》是否有對應的國家標準，本次沒有查到

## 日本

- 事實：《青少年が安全に安心してインターネットを利用できる環境の整備等に関する法律》（平成二十年法律第七十九号，簡稱青少年インターネット環境整備法）把青少年定義為未滿 18 歲，管制對象是手機通信業者、終端製造者與作業系統開發者，管制內容是有害資訊的過濾軟體，沒有年齡訊號的規定
    - 照錄：「この法律において「青少年」とは、十八歳に満たない者をいう。」（第二条第一項）
    - 來源（一手）：e-Gov 法令檢索，法令 ID `420AC1000000079`，查證時的現行版本為 2026-06-24 施行的版本（`420AC1000000079_20260624_508AC0000000046`），<https://laws.e-gov.go.jp/law/420AC1000000079>
    - 全文搜尋「年齢」一詞沒有命中，法條不要求蒐集或傳送年齡
- 事實：手機通信業者販售手機時，如果契約對象或使用者是青少年，要對該手機實施過濾有效化措施，保護者申請不要時除外
    - 照錄：「携帯電話インターネット接続役務提供事業者等は、携帯電話端末等 ... を販売する場合において、当該特定携帯電話端末等に係る役務提供契約の相手方又は当該特定携帯電話端末等の使用者が青少年であるときは、当該特定携帯電話端末等について、青少年有害情報フィルタリング有効化措置を講じなければならない。」（第十六条，中間省略的括號內容為對適用除外的定義） <!-- docs-style-lint: disable-line -->
    - 來源（一手）：同上
- 事實：製造青少年使用的連網機器的業者，銷售前要內建過濾軟體或用其他方法讓使用者容易使用過濾軟體或服務
    - 照錄：「インターネットと接続する機能を有する機器であって青少年により使用されるもの ... を製造する事業者は、青少年有害情報フィルタリングソフトウェアを組み込むことその他の方法により青少年有害情報フィルタリングソフトウェア又は青少年有害情報フィルタリングサービスの利用を容易にする措置を講じた上で、インターネット接続機器を販売しなければならない。」（第十八条） <!-- docs-style-lint: disable-line -->
    - 來源（一手）：同上
- 事實：開發直接控制連網機器運作的程式（作業系統）的業者，只有努力義務（法條用「努めなければならない」），要讓手機業者的過濾措施與製造者的過濾軟體可以順利運作
    - 照錄：「プログラムの実行をするためにインターネット接続機器の動作を直接制御する機能を有するプログラムを開発する事業者は、携帯電話インターネット接続役務提供事業者等の青少年有害情報フィルタリング有効化措置及び当該インターネット接続機器を製造する事業者の青少年有害情報フィルタリングソフトウェア又は青少年有害情報フィルタリングサービスの利用を容易にする措置が円滑に講ぜられるように、当該プログラムを開発するよう努めなければならない。」（第十九条） <!-- docs-style-lint: disable-line -->
    - 「作業系統」是本筆記對該條文字的歸納，法條沒有出現「オペレーティングシステム」一詞（全文搜尋未命中）
    - 來源（一手）：同上
- 查不到：這部法沒有 App 商店層級的年齡確認規定。其他法律有沒有，本次沒有逐一檢視。法條中的罰則與監督手段，本次沒有查

## 未取得一手來源的地方

下面三個地方做過初步搜尋，因為沒有取得一手來源，不列條目，使用前要自行查證。

- 馬來西亞：《Online Safety Act 2025》與兒少保護守則的執行日期據律師事務所文章是 2026 年 6 月 1 日，文章列的義務對象是持照的服務提供者，沒有看到 App 商店或作業系統的條款
- 印尼：政府規章 2025 年第 17 號（PP Tunas）據律師事務所文章已於 2026 年 3 月 1 日起適用，要求電子系統提供者依風險等級驗證兒童用戶。App 商店或作業系統是否為義務對象，本次沒有查到
- 南韓：據二手文章，電氣通信事業法第 32-7 條要求電信業者在賣手機給青少年時提供有害媒體的阻擋手段。本次沒有查法條原文，也沒有確認近期是否有 App 市場年齡確認的立法
