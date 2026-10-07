# VPN 的法律規範與法院或行政機關命令封鎖網站的制度

範圍是六個地方（中國大陸、新加坡、印度、日本、台灣、香港）對 VPN 業者或使用者的法律規範，以及法院或行政機關命令網路業者封鎖網站的制度，重點放在盜版網站。只寫法規、官方文件與判決，不寫哪個地區、哪個族群的人在用什麼工具，也不寫人名（來源文件裡的當事人與提案人姓名一律略去）。

第一次整理是寫 anoni-net/news 的猶他州所在地條款與美國網站封鎖法案那篇導讀的時候。查證日期 2026-10-07，下面每一條都是這天查到的內容。

來源分一手與二手：一手是法規原文、政府或法院的公告與判決，二手是媒體、律師事務所與百科的整理。照錄的句子保留原文語言與標點，PDF 與網頁轉文字時多出來的空白已經去掉。

## 中國大陸

### CN-1　國際聯網只能走國家指定的出入口信道，適用單位與個人

- 事實：《計算機信息網絡國際聯網管理暫行規定》第六條規定，直接國際聯網的電腦網路必須使用國家公用電信網提供的國際出入口信道，任何單位和個人不得自行建立或使用其他信道。條文沒有出現 VPN 一詞，適用對象寫明是「單位和個人」 <!-- docs-style-lint: disable-line -->
- 照錄：「计算机信息网络直接进行国际联网，必须使用邮电部国家公用电信网提供的国际出入口信道。」、「任何单位和个人不得自行建立或者使用其他信道进行国际联网。」
- 文件：《中华人民共和国计算机信息网络国际联网管理暂行规定》，1996 年 2 月 1 日国务院令第 195 号发布，1997 年 5 月 20 日修正
- 網址：<https://www.cac.gov.cn/1996-02/02/c_126468621.htm>（國家網信辦網站轉載，另存 WIPO Lex 的副本 <https://www.wipo.int/wipolex/en/text/199708>，未逐句比對）
- 一手（法規原文，政府網站轉載）

### CN-2　違反第六條的罰則，個人與單位都適用

- 事實：第十四條規定違反第六條、第八條、第十條的，由公安機關責令停止聯網、給予警告，可以並處一萬五千元以下罰款，有違法所得的沒收。第十條把「個人、法人和其他組織」都列為使用者，所以個人也在適用範圍內。第十五條另規定同時觸犯其他法律、行政法規的依各自規定處罰，構成犯罪的追究刑事責任
- 照錄：「违反本规定第六条、第八条和第十条的规定的，由公安机关责令停止联网，给予警告，可以并处15000元以下的罚款；有违法所得的，没收违法所得。」 <!-- docs-style-lint: disable-line -->
- 照錄：「个人、法人和其他组织（以下统称用户）使用的计算机或者计算机信息网络，需要进行国际联网的，必须通过接入网络进行国际联网。」
- 照錄：「违反本规定，同时触犯其他有关法律、行政法规的，依照有关法律、行政法规的规定予以处罚；构成犯罪的，依法追究刑事责任。」 <!-- docs-style-lint: disable-line -->
- 文件、網址與日期同 CN-1
- 一手（法規原文，政府網站轉載）

### CN-3　工信部 2017 年通知，跨境專線（含 VPN）需經電信主管部門批准

- 事實：工信部 2017 年的通知在「違規開展跨境業務問題」一項寫明，未經電信主管部門批准，不得自行建立或租用專線（含 VPN）等其他信道開展跨境經營活動。通知的發送對象是各省通信管理局、基礎電信企業與 IDC、ISP、CDN 業務經營者，清理規範工作期限到 2018 年 3 月 31 日。條文限定的是「開展跨境經營活動」，沒有寫個人使用
- 照錄：「违规开展跨境业务问题。未经电信主管部门批准，不得自行建立或租用专线（含虚拟专用网络VPN）等其他信道开展跨境经营活动。基础电信企业向用户出租的国际专线，应集中建立用户档案，向用户明确使用用途仅供其内部办公专用，不得用于连接境内外的数据中心或业务平台开展电信业务经营活动。」
- 照錄：「工业和信息化部决定自即日起至2018年3月31日，在全国范围内对互联网网络接入服务市场开展清理规范工作。」
- 文件：《工业和信息化部关于清理规范互联网网络接入服务市场的通知》，工信部信管函〔2017〕32 号，成文日期 2017-01-17，發布日期 2017-01-22，發布機構信息通信管理局
- 網址：<https://www.miit.gov.cn/jgsj/xgj/wjfb/art/2020/art_ac2095b32d054e22a03e8154c3a44d50.html>
- 一手（部門規範性文件，工信部網站）。官方頁面的文字有多餘空白，上面的引文已正規化

### CN-4　工信部說明，規範對象是無資質經營跨境電信業務的企業或個人

- 事實：工信部信息通信管理局負責人答記者問表示，上述規定的主要依據是《國際通信出入口局管理辦法》（原信息產業部令第 22 號），規範對象是未經批准、沒有國際通信業務經營資質，租用國際專線或 VPN 私自開展跨境電信業務經營活動的企業或個人。外貿企業與跨國企業辦公自用，可向依法設置國際通信出入口局的電信業務經營者租用。這是官方對 CN-3 的說明，不是法規條文
- 照錄：「《通知》关于跨境开展经营活动的规定，主要的依据是《国际通信出入口局管理办法》（原信息产业部令第 22 号），规范的对象是未经电信主管部门批准，无国际通信业务经营资质的企业或个人，租用国际专线或VPN，私自开展跨境的电信业务经营活动。」
- 照錄：「外贸企业、跨国企业因办公自用等原因，需要通过专线等方式跨境联网时，可以向依法设置国际通信出入口局的电信业务经营者租用，《通知》的相关规定不会对其正常运转造成影响。」
- 文件：《工业和信息化部信息通信管理局负责人就〈关于清理规范互联网网络接入服务市场的通知〉答记者问》，頁面發布時間 2017-01-24
- 網址：<https://wap.miit.gov.cn/zwgk/zcjd/art/2020/art_6d942fea3c824343bdd1e01f2d6e12af.html>
- 一手（政府機關的官方說明）。《國際通信出入口局管理辦法》本身沒有另外查閱

### CN-5　境外來源的違法資訊由網信與主管部門通知有關機構採取技術措施阻斷

- 事實：《網絡安全法》2025 年修正版（2026 年 1 月 1 日施行）第五十二條規定，國家網信部門與有關部門發現法律、行政法規禁止發布或傳輸的資訊，要求網路運營者停止傳輸，對來源於境外的同類資訊，通知有關機構採取技術措施和其他必要措施阻斷傳播。條文的執行者是行政機關，文字裡沒有寫法院程序。2016 年版本同一條是第五十條，文字相同
- 照錄：「国家网信部门和有关部门依法履行网络信息安全监督管理职责，发现法律、行政法规禁止发布或者传输的信息的，应当要求网络运营者停止传输，采取消除等处置措施，保存有关记录；对来源于中华人民共和国境外的上述信息，应当通知有关机构采取技术措施和其他必要措施阻断传播。」 <!-- docs-style-lint: disable-line -->
- 文件：《中华人民共和国网络安全法》（2016 年 11 月 7 日通過，2025 年 10 月 28 日修正，2026 年 1 月 1 日起施行）
- 網址：2025 年修正版 <https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm>（第五十二條）。修正決定 <https://www.cac.gov.cn/2025-10/29/c_1763461514768457.htm>（「本决定自2026年1月1日起施行」）。2016 年版本 <http://www.npc.gov.cn/zgrdw/npc/xinwen/2016-11/07/content_2001605.htm>（第五十條）
- 一手（法律原文，政府網站）

### CN-6　網站封鎖有沒有公開的法院程序：查不到

- 事實：本次讀過的法規（CN-1、CN-2、CN-5）與官方說明（CN-4）裡，封鎖與阻斷由公安機關、網信部門與有關部門執行，沒有找到要求先經法院裁定的條文，也沒有找到公開的封鎖令聲請程序或判決。這是「本次查到的材料沒有」，不等於確認制度上不存在，引用時寫成「查到的法規沒有規定法院程序」
- 一手與二手都沒有可引用的來源

### CN-7　刑事追訴的實例（二手）

- 事實：The China Project 在 2018-10-10 引述《人民法院報》的報導，寫到上海市寶山區法院判決一名在網站販售 VPN 服務的軟體工程師有期徒刑三年、緩刑三年、罰款一萬元，罪名是提供侵入、非法控制計算機信息系統的程式、工具（英文報導的措辭）。同一篇報導另提到廣西的一件判決，五年半徒刑加罰款五十萬元，理由是 2013 年起未經許可販售 VPN。兩件的被告都是販售服務的業者。報導稱這是上海第一件 VPN 服務提供者被追究刑責的案件
- 照錄：「was also ordered to serve three years probation and pay a fine of 10,000 yuan」、「was charged with “offering illegal tools like computer programs that can invade and control computer information systems.”」
- 照錄：「the People’s Court Daily warns that while VPNs are prevalent in China, such services have always been in a legal “gray area” and have never received official approval from top internet regulators.」（原文為轉述，大小寫已調整）
- 文件：Man in Shanghai gets three-year sentence for selling VPNs，The China Project，2018-10-10
- 網址：<https://thechinaproject.com/2018/10/10/man-in-shanghai-gets-three-year-sentence-for-selling-vpns/>。原報導《人民法院報》2018-10-09 的頁面 <http://rmfyb.chinacourt.org/paper/html/2018-10/09/content_144238.htm> 本次連不上，判決書與刑法條文沒有另外查閱
- 二手（英文媒體引述官方報紙）

## 新加坡

### SG-1　高等法院可命令網路連線業者封鎖「明目張膽侵權的網路位置」

- 事實：《Copyright Act 2021》第 325 條（2022-04-01 起生效）規定，法院依權利人聲請，可命令 NCP 採取合理步驟封鎖某個網路位置，要件有三項：該位置是「flagrantly infringing online location」、曾經或正在被用來對聲請人擁有權利的著作或表演侵權、該 NCP 的服務曾經或正在被用來連上該位置。這裡的「Court」依第 7 條定義是高等法院的 General Division
- 照錄：「The Court may, on application, order a NCP to take reasonable steps to disable access to an online location (called in this Subdivision an access disabling order) if —」（接著是 (a)(b)(c) 三款，內容如上） <!-- docs-style-lint: disable-line -->
- 照錄：「“Court” means the General Division of the High Court」（第 7 條）
- 文件：Copyright Act 2021（Act 22 of 2021），新加坡法規資料庫（Singapore Statutes Online）。第 325 條頁面標示 Act 22 of 2021 wef 01/04/2022
- 網址：<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr325-&ViewType=Within>、<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr7-&ViewType=Within>
- 一手（法規原文）

### SG-2　NCP 的定義，以及法院裁量時要考慮的事項

- 事實：第 313 條把「network connection provider」（NCP）定義為提供資料傳輸或路由相關服務、或為傳輸或路由提供連線的人，排除規則另行指定的人。第 325(2) 條要求法院決定是否發令與令的內容時，必須考慮包含權利人受到的損害、NCP 的負擔、技術可行性、令的有效性、對 NCP 業務的不利影響、有沒有負擔較輕的同等有效命令
- 照錄：「“network connection provider” or “NCP” — (a) means a person who provides services relating to, or provides connections for, the transmission or routing of data; but (b) does not include any prescribed person or class of persons」（第 313 條） <!-- docs-style-lint: disable-line -->
- 照錄：「the burden that the making of the order will place on the NCP;」、「whether some other comparably effective order would be less burdensome.」（第 325(2)(b)(f) 款）
- 版本註記：第 313 條頁面上 NSP 定義標示「Act 32 of 2024 wef 25/11/2024」，NCP 的原定義旁有「Deleted by Act 32 of 2024 wef 25/11/2024」字樣，2024 年修正對這一節的影響沒有逐條核對，引用前先回條文確認
- 網址：<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr313-&ViewType=Within>、<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr325-&ViewType=Within>
- 一手（法規原文）

### SG-3　「明目張膽侵權的網路位置」的定義與考量因素

- 事實：第 99 條定義「flagrantly infringing online location」是曾經或正在被用來明目張膽地實施或助長權利侵害的網路位置，並列出必須考慮的因素，包含主要目的、有沒有提供侵權手段的目錄或索引、擁有者是否普遍漠視著作權、是否已被他國法院命令封鎖、是否附有規避封鎖措施或法院命令的指引、流量大小。這些因素針對的是被封鎖的網站本身
- 照錄：「A “flagrantly infringing online location” is an online location that has been or is being used to flagrantly commit or facilitate rights infringements.」
- 照錄：「whether the online location contains guides or instructions to circumvent measures, or any order of any court, that disable access to the online location on the ground of or related to rights infringements;」（第 99(2)(e) 款）
- 網址：<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr99-&ViewType=Within>
- 一手（法規原文）

### SG-4　聲請程序、網站擁有者的權利與命令的變更

- 事實：權利人聲請前須通知網路位置的擁有者與 NCP。法院可在權利人合理努力後仍聯絡不上擁有者時，免除通知。擁有者有受聽取的權利，也有與當事人相同的上訴權。第 327 條讓法院在情況重大改變時變更命令，或在證據顯示不該發令、該網路位置已不再明目張膽侵權時撤銷命令，命令的當事人與網路位置的擁有者都可以聲請
- 照錄：「The owner of the online location has — (a) the right to be heard in the application; and (b) the same right of appeal as any party to the application.」（第 326(6) 條） <!-- docs-style-lint: disable-line -->
- 照錄：「the online location that is the subject of the order ceases to be a flagrantly infringing online location」（第 327(2)(b) 款）
- 網址：<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr326-&ViewType=Within>、<https://sso.agc.gov.sg/Act/CA2021?ProvIds=pr327-&ViewType=Within>
- 一手（法規原文）

### SG-5　對 VPN 業者的專門規定：查不到

- 事實：本次讀過的條文（第 7、99、313、325 到 328 條）沒有出現 VPN 或 virtual private network 字樣。VPN 業者的服務是否落在 NCP 定義的字面範圍內（「provides connections for the transmission or routing of data」），沒有找到官方說明或法院見解，是否適用屬於推論，引用時不要寫成已確認。新加坡法規資料庫的全法文字檢索因為網站限制沒有取得，所以「全法沒有 VPN 條文」不能寫成結論
- 一手與二手都沒有可引用的來源

### SG-6　制度沿革與前例（二手）

- 事實：Osborne Clarke 的文章寫到，新加坡在 2014 年修正舊《Copyright Act》，授權法院對網路服務業者發出封鎖令（舊法第 193DDA 條），2016 年 2 月高等法院依該條命令四家網路業者封鎖一個盜版網站。德里高等法院 2019 年的判決（見 IN-5）在說明動態禁制令時引用新加坡高等法院依舊法第 193DDA 條發出的動態封鎖令，並寫明印度沒有類似的法定程序
- 照錄：「In 2014, Singapore amended its Copyright Act to enable the courts to make an order, requiring a network service provider (NSP) whose services have been or are being used to access an online location to commit or facilitate infringement of copyright, to block access to a “flagrantly infringing online location”.」
- 文件：Copyright: site-blocking in Singapore，Osborne Clarke，頁面標示 Published on 13 July 2021
- 網址：<https://www.osborneclarke.com/insights/copyright-site-blocking-in-singapore/>
- 二手（律師事務所文章）。判決書本身沒有另外查閱

## 印度

### IN-1　CERT-In 2022 年指令，VPN 業者要登記並保存用戶資料五年

- 事實：CERT-In 在 2022-04-28 依《資訊科技法》第 70B(6) 條發出指令，其中第 (v) 項要求資料中心、VPS 業者、雲端業者與 VPN 業者登記七類資料並保存，期間是登記取消或撤回之後五年或法律要求的更長期間。適用對象是這幾類業者，不是 VPN 使用者。七類資料是訂閱者驗證後的姓名、租用期間、配發或使用的 IP、註冊時的電子郵件與 IP 及時間戳記、租用目的、驗證後的地址與聯絡電話、訂閱者的所有權結構
- 照錄：「Data Centres, Virtual Private Server (VPS) providers, Cloud Service providers and Virtual Private Network Service (VPN Service) providers, shall be required to register the following accurate information which must be maintained by them for a period of 5 years or longer duration as mandated by the law after any cancellation or withdrawal of the registration as the case may be:」
- 照錄：「Validated names of subscribers/customers hiring the services」、「IPs allotted to / being used by the members」、「Purpose for hiring services」
- 文件：No. 20(3)/2022-CERT-In, Directions under sub-section (6) of section 70B of the Information Technology Act, 2000 relating to information security practices, procedure, prevention, response and reporting of cyber incidents for Safe & Trusted Internet，Dated 28 April, 2022
- 網址：<https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf>（本次連不上官網，用網路檔案館的 2023 年副本 <https://web.archive.org/web/2023/https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf>）
- 一手（官方指令）

### IN-2　指令的生效時間與 VPN 業者部分的延後

- 事實：指令寫明在發布 60 天後生效。2022-06-27 的另一份通知把 MSME 的生效日延到 2022-09-25，並把 VPN 業者等四類業者的「訂閱者驗證後的姓名」與「驗證後的地址與聯絡電話」兩項，限於這個範圍延到 2022-09-25 生效，其餘項目沒有延後
- 照錄：「This direction will become effective after 60 days from the date on which it is issued.」（2022-04-28 指令）
- 照錄：「the requirement relating to the aspects of registration and maintenance of “Validated names of subscribers/customers hiring the services” and “Validated address and contact numbers” by Data Centres, Virtual Private Server (VPS) providers, Cloud Service providers and Virtual Private Network Service (VPN Service) providers incorporated at paragraph no.(v) a.& f of CERT-In’s Cyber Security Direction No. 20(3)/2022-CERT-In of 28.04.2022, to the said limited extent, will become effective on 25th September, 2022」
- 文件：No. 20(3)/2022-CERT-In, Extension of timelines for enforcement of Cyber Security Directions of 28th April, 2022 ... for MSMEs and also for implementation of mechanism for validation of subscribers/customers details by Data Centres, VPS providers, Cloud Service providers and VPN Service providers，Dated 27 June, 2022
- 網址：<https://www.cert-in.org.in/PDF/CERT-In_directions_extension_MSMEs_and_validation_27.06.2022.pdf>（官網連不上，用網路檔案館副本 <https://web.archive.org/web/2022id_/https://www.cert-in.org.in/PDF/CERT-In_directions_extension_MSMEs_and_validation_27.06.2022.pdf>）
- 一手（官方通知）

### IN-3　同一份指令對所有服務提供者的其他義務與罰則

- 事實：同一份指令要求所有服務提供者、中介者、資料中心與法人，保存 ICT 系統日誌 180 天且存放在印度境內，並在察覺資安事件後 6 小時內通報 CERT-In。不遵守時指令寫的後果是依《資訊科技法》第 70B(7) 條與其他法律追究。第 70B(7) 條的罰則本次沒有取得法條原文：舊版二手整理寫的是一年以下徒刑或十萬盧比以下罰款，2023 年 Jan Vishwas Act 修正後的二手說明寫的是改為罰款最高一千萬盧比（Rs. One crore）、不再有監禁，自 2023-11-30 起生效，兩種說法並存，引用罰則前必須回法條原文確認
- 照錄：「shall mandatorily enable logs of all their ICT systems and maintain them securely for a rolling period of 180 days and the same shall be maintained within the Indian jurisdiction.」
- 照錄：「shall mandatorily report cyber incidents as mentioned in Annexure I to CERT-In within 6 hours of noticing such incidents or being brought to notice about such incidents.」
- 照錄：「may invite punitive action under sub-section (7) of the section 70B of the IT Act, 2000 and other laws as applicable.」
- 文件與網址同 IN-1。罰則的二手來源：Intermediaries may face enhanced fines for data retention breaches from 30.11.2023，Lexplosion Solutions，<https://lexplosion.in/intermediaries-may-face-enhanced-fines-for-data-retention-breaches-from-30-11-2023-meity-notifies-implementation-date-for-amendments-to-it-act-pursuant-to-jan-vishwas-act-2023/>
- 指令部分一手，罰則部分二手

### IN-4　行政機關依第 69A 條命令中介者封鎖資訊

- 事實：《資訊科技法》第 69A 條授權中央政府或其特別授權的官員，基於主權與領土完整、國防、國家安全、與外國的友好關係或公共秩序等理由，以書面記載理由的命令，指示政府機關或中介者封鎖公眾對資訊的存取。中介者不遵守可處最高七年徒刑並科罰金。這是行政命令，條文沒有要求法院裁定，程序與保障措施另依規則。適用範圍是上述公共利益事由，不限於盜版
- 照錄：「it may subject to the provisions of sub-section (2), for reasons to be recorded in writing, by order, direct any agency of the Government or intermediary to block for access by the public or cause to be blocked for access by the public any information generated, transmitted, received, stored or hosted in any computer resource.」
- 照錄：「The intermediary who fails to comply with the direction issued under sub-section (1) shall be punished with an imprisonment for a term which may extend to seven years and also be liable to fine.」
- 文件：The Information Technology Act, 2000，Section 69A（頁面標示 Adoption Date 2000-06-19，Original Text，2008 年修正增訂的條文）
- 網址：<https://sherloc.unodc.org/cld/en/legislation/ind/the_information_technology_act_2000/chapter_xi/section_69_a-b/section_69_a-b.html>（聯合國毒品和犯罪問題辦公室的立法資料庫轉載原文，後續修正是否改動這一條沒有核對）
- 一手（法規原文，國際組織資料庫轉載）

### IN-5　德里高等法院的動態禁制令（盜版網站）

- 事實：德里高等法院在 2019-04-10 對盜版網站作出永久禁制令判決，命令 ISP 封鎖被告網站，並要求電信部（DoT）與電子資訊技術部（MeitY）通知各網路與電信業者封鎖。法院在這份判決裡創設動態禁制令：權利人可以向法院書記官提出宣誓書與證據，證明新網站是已被禁制網站的鏡像、重新導向或替代網址，經書記官確認後，直接發令 ISP 封鎖，不必重新起訴。法院在判決裡寫明印度沒有類似新加坡的法定程序，依民事訴訟法第 151 條的固有權力作成。封鎖範圍限於被告網站與它們的鏡像網站
- 照錄：「Though the dynamic injunction was issued by the Singapore High Court under the provisions of Section 193 DDA of the Singapore Copyright Act, and no similar procedure exists in India, yet in order to meet the ends of justice and to address the menace of piracy, this Court in exercise of its inherent power under Section 151 CPC permits the plaintiffs to implead the mirror/redirect/alphanumeric websites under Order I Rule 10 CPC」（第 99 段）
- 照錄：「ISPs ought not to be tasked with the role of arbiters, contrary to their strictly passive and neutral role as intermediaries.」（第 100 段）
- 照錄：「A decree is also passed directing the ISPs to block access to the said defendant-websites. DoT and MEITY are directed to issue a notification calling upon the various internet and telecom service providers registered under it to block access to the said defendant-websites.」（第 107 段）
- 文件：UTV Software Communication Ltd. and Ors v. 1337X.TO and Ors，CS(COMM) 724/2017，Delhi High Court，Date of Decision 10 April 2019
- 網址：<https://globalfreedomofexpression.columbia.edu/wp-content/uploads/2019/07/UTV-Software-Communications-Ltd.-v.-1337X.TO_.pdf>（哥倫比亞大學 Global Freedom of Expression 網站放的判決全文）
- 一手（判決書，第三方網站轉載）
- 判決全文只有在引用他國研究的統計時提到 VPN（寫到封鎖後 VPN 網站的訪問增加百分之三十，基數很小），沒有針對 VPN 業者的命令

## 日本

### JP-1　2018-04-13 的緊急對策，要求民間業者自主封鎖三個網站

- 事實：2018-04-13 的知識財產戰略本部與犯罪對策閣僚會議決定「インターネット上の海賊版サイトに対する緊急対策」，整理出封鎖的法律解釋：封鎖可能形式上侵害通信秘密，但符合刑法第 37 條緊急避難要件時，違法性被阻卻。當下的做法是在法制整備前，以臨時且緊急的措施，由民間業者自主封鎖三個點名網站與被視為同一的網站。下面的原文引自會議資料的「案」（概要版），國立國會圖書館的報導記載會議決定時沿用這個措辭，最終定稿的全文沒有另外取得
- 照錄：「ブロッキングは、「通信の秘密」を形式的に侵害する可能性があるが、仮にそうだとしても、侵害コンテンツの量、削除や検挙など他の方法による権利の保護が不可能であることなどの事情に照らし、緊急避難（刑法第３７条）の要件を満たす場合には、違法性が阻却されるものと考えられる。」
- 照錄：「当面の対応としては、法制度整備が行われるまでの間の臨時的かつ緊急的な措置として、民間事業者による自主的な取組として、「漫画村」、「Anitube」、「Miomio」の３サイト及びこれと同一とみなされるサイトに限定してブロッキングを行うことが適当と考えられる。」
- 文件：資料１－１「インターネット上の海賊版サイトに対する緊急対策（案）（概要）」，平成30年4月13日 知的財産戦略本部・犯罪対策閣僚会議
- 網址：議事次第 <https://www.kantei.go.jp/jp/singi/titeki2/180413/gijisidai.html>（現在轉址到內閣官房網站，本次用網路檔案館的副本 <https://web.archive.org/web/2019/https://www.kantei.go.jp/jp/singi/titeki2/180413/siryou1.pdf>）。決定的報導 <https://current.ndl.go.jp/car/35859>（2018-04-17）
- 一手（政府會議資料，標示為案）。決定的事實由 NDL 的報導確認，屬二手

### JP-2　NTT 集團 2018-04-23 宣布實施封鎖

- 事實：NTT 與 NTT Communications、NTT docomo、NTT Plala 在 2018-04-23 發布新聞稿，宣布依內容業者團體的要求與 4 月 13 日的政府決定，由後三家公司在法制整備前以短期緊急措施封鎖三個盜版網站，準備好就實施，並請政府儘快整備法制
- 照錄：「サイトブロッキングに関する法制度が整備されるまでの短期的な緊急措置として、海賊版3サイトに対してブロッキングを行うこととし、準備が整い次第実施します。なお、政府において、可及的速やかに法制度を整備していただきたいと考えています。」
- 文件：インターネット上の海賊版サイトに対するブロッキングの実施について，NTT 持株會社新聞稿，2018-04-23
- 網址：<http://www.ntt.co.jp/news2018/1804/180423a.html>（原網址已搬遷，本次用網路檔案館副本 <https://web.archive.org/web/2018/http://www.ntt.co.jp/news2018/1804/180423a.html>）
- 一手（企業新聞稿）

### JP-3　NTT 於 2018 年 8 月取消封鎖計畫（二手）

- 事實：媒體報導共同通信在 2018-08-03 報導 NTT 集團決定中止封鎖，理由是對象網站停止運作使效果變薄。同日日本經濟新聞報導 NTT 的方針沒有變，網站復活時會依政府方針再度實施。這兩則是轉述，NTT 的官方公告沒有取得，實際上有沒有執行過封鎖沒有查到一手來源
- 照錄：「共同通信は、NTTグループがブロッキングを中止する方針を固めたと、8月3日21時37分に報じました。理由は対象サイトの停止で効果が薄れたため。」
- 文件：NTT、ブロッキング一旦取りやめ。ブロッキング恒久停止と公式漫画村で事態打開を，すまほん!!，2018-08-04
- 網址：<https://smhn.info/201808-ntt-stop-blocking>
- 二手（部落格轉述通訊社與報紙）

### JP-4　2018-10-15 檢討會議沒有就封鎖立法達成結論（二手）

- 事實：內閣府知識財產推進事務局的「インターネット上の海賊版対策に関する検討会議」第 9 次會議在 2018-10-15 舉行，原訂要整理封鎖立法與否，贊成與反對意見沒有交集，開了三個半小時，連要不要寫報告書都沒有結論，會議無限期延期
- 照錄：「内閣府 知的財産推進事務局は10月15日、インターネット上の海賊版サイトの対策に関する検討会議の第9回を行った。」
- 文件：「ブロッキング法制化」結論出ず　3時間半の激論、政府検討会は無期限延期に，ITmedia，2018-10-15
- 網址：<https://www.itmedia.co.jp/news/article/1810/15/1181015131/>
- 二手（新聞報導）。會議紀錄與報告書沒有另外查閱

### JP-5　現況：封鎖的法制整備仍在「檢討」，沒有立法

- 事實：內閣府等機關 2026-08-25 公布的「インターネット上の海賊版に対する総合的な対策メニュー及び工程表」，所附對策メニュー（標示 2019 年 10 月策定、2024 年 5 月更新，版本日期 2024-05-28）的註記寫明，封鎖的法制整備要看其他措施的效果與被害狀況再檢討。同一份文件列出已經立法的是 2020 年著作權法修正引進的連結網站（リーチサイト）對策與侵權內容下載違法化。查到的官方資料沒有任何授權法院或行政機關命令封鎖盜版網站的日本法律
- 照錄：「（注）ブロッキングに係る法制度整備については、他の取組の効果や被害状況等を見ながら検討」
- 照錄：「2020年著作権法改正により導入されたリーチサイト対策、侵害コンテンツのダウンロード違法化の周知・普及啓発を含め、官民で連携しながら、著作権教育・意識啓発のより一層の効果的な展開を図る」
- 文件：インターネット上の海賊版に対する総合的な対策メニュー及び工程表（對策メニュー 2024 年 5 月 28 日版，工程表 2026 年 8 月 25 日），內閣府、警察庁、総務省、法務省、外務省、文部科学省、文化庁、経済産業省
- 網址：<https://www.cas.go.jp/jp/seisakukaigi/titeki2/pdf/kaizokuban_taisaku_r808.pdf>
- 一手（政府文件）。「沒有立法」是從這份文件的措辭與本次未找到任何封鎖法推論，引用時寫成「截至該文件，仍在檢討」
- 日本對 VPN 業者或使用者的法律規範：本次沒有查，不在這份筆記的範圍

## 台灣

### TW-1　現行《著作權法》沒有命令封鎖網站的條文

- 事實：全國法規資料庫的《著作權法》（修正日期民國 111 年 6 月 15 日，其中 111 年 5 月 4 日修正的第 91、91-1、100、117 條與刪除第 98、98-1 條，施行日期由行政院另定，頁面標示最後生效日期未定）在全文裡，與網路服務提供者和侵害救濟直接相關的是兩處：第六章之一（第 90-4 到 90-12 條）的網路服務提供者民事免責事由，與第 84 條的侵害排除與防止請求權。免責事由的條文要求資訊儲存、快速存取、搜尋等服務提供者在接獲通知後移除或使他人無法進入侵權內容，沒有任何條文授權法院或行政機關命令連線服務提供者封鎖 IP 位址或網域。全文以「封鎖」、「網域」、「境外」搜尋沒有命中相關條文
- 照錄：「著作權人或製版權人對於侵害其權利者，得請求排除之，有侵害之虞者，得請求防止之。」（第 84 條）
- 照錄：「經著作權人或製版權人通知其使用者涉有侵權行為後，立即移除或使他人無法進入該涉有侵權之內容或相關資訊。」（第 90-7 條第三款）
- 文件：著作權法，全國法規資料庫，修正日期民國 111 年 06 月 15 日
- 網址：<https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0070017>
- 一手（法規原文）。「沒有」是依本次抓到的條文全文判斷，引用時註明查證日期

### TW-2　2013 年智慧財產局研擬行政命令封鎖，同年宣布停止推動（二手）

- 事實：2013 年 5 月，經濟部智慧財產局表示要修《著作權法》，由智慧財產局直接命令 ISP 以 IP 位址或 DNS 技術封鎖「一望即知重大侵權的境外網站」，後來因外界批評行政機關擅自認定而考慮改由法院裁定。維基百科的整理寫到智慧財產局在 2013-06-03 召開記者會，表示因箝制言論自由的質疑不斷，停止推動修法。智慧財產局原始新聞稿沒有取得，細節與日期引用前需回官方文件確認
- 照錄：「經濟部智慧財產局研擬封鎖境外侵權網站事件 發生於2013年5月，起因為 中華民國 經濟部智慧財產局 發表新聞研擬修法，將由智慧財產局直接下令 ISP 業者，以 IP位址 或 DNS 技術等方式封鎖「一望即知重大侵權的境外網站」」
- 文件：經濟部智慧財產局研擬封鎖境外侵權網站事件，維基百科（頁面更新時間 2026-05-13）
- 網址：<https://zh.wikipedia.org/zh-tw/%E7%B6%93%E6%BF%9F%E9%83%A8%E6%99%BA%E6%85%A7%E8%B2%A1%E7%94%A2%E5%B1%80%E7%A0%94%E6%93%AC%E5%B0%81%E9%8E%96%E5%A2%83%E5%A4%96%E4%BE%B5%E6%AC%8A%E7%B6%B2%E7%AB%99%E4%BA%8B%E4%BB%B6>
- 二手（百科）

### TW-3　2017 年立法委員連署提案增訂第 84 條之 1，沒有通過

- 事實：2017-09-20 印發的立法院第 9 屆第 4 會期議案文件（院總第 553 號、委員提案第 21044 號），由 20 位立法委員提出《著作權法》增訂第 84 條之 1 草案，內容包含著作權人得聲請法院命電信業者或網際網路服務業者封鎖侵權境外網站的 IP 位址或網域，並命臺灣網際網路中心（TWNIC）不得解析該網頁。現行《著作權法》全文沒有第 84 條之 1（見 TW-1），所以這份提案沒有成為法律。提案後續的審查紀錄（有沒有付委、有沒有退回）沒有查到
- 照錄：「著作權人得聲請法院令電信業者封鎖該 IP 位址或網域。」（說明第三點第 4 款）
- 照錄：「著作權人得聲請法院令網際網路服務業者封鎖該 IP 位址或網域，並令臺灣網際網路中心（TWNIC）不得解析該網頁。」（草案條文第五款）
- 文件：立法院議案關係文書，院總第 553 號，委員提案第 21044 號，中華民國 106 年 9 月 20 日印發
- 網址：<http://lci.ly.gov.tw/LyLCEW/agenda1/02/pdf/09/04/01/LCEWA01_090401_00101.pdf>（原網址已失效，本次用網路檔案館副本 <https://web.archive.org/web/20171001122203/http://lci.ly.gov.tw/LyLCEW/agenda1/02/pdf/09/04/01/LCEWA01_090401_00101.pdf>）
- 一手（立法院議案文件）。「沒有通過」是從 TW-1 條文全文推論

### TW-4　2017 年之後是否有新的封鎖草案或法案：查不到

- 事實：本次用「智慧局」、「著作權法修正草案」、「封鎖」、「境外侵權網站」等關鍵字搜尋 2018 到 2026 年的資料，沒有找到智慧財產局或立法院提出新的封鎖盜版網站條文，也沒有在智慧財產局網站「網路相關著作權問題之說明」頁面看到相關說明。這是搜尋範圍內沒有找到，不等於確認沒有，引用時寫成「查到的法規與提案到 2017 年為止」，並建議到立法院議案系統再查一次
- 一手與二手都沒有可引用的來源
- 台灣對 VPN 業者或使用者的法律規範：本次沒有查，不在這份筆記的範圍

## 香港

### HK-1　版權條例沒有專門的封鎖網站條文，政府認為高等法院的一般禁制令權力足夠

- 事實：香港政府 2022 年向立法會提出《2022 年版權（修訂）條例草案》時，在立法會參考資料摘要寫明，高等法院條例第 21L 條已讓版權擁有人有途徑申請禁制令，網路服務提供者在適當情況下可被命令封鎖侵權網路位置的存取，因為封鎖禁制令對資訊自由的影響有許多爭議，認為沒有必要另設專門針對版權侵害的司法封鎖機制。2021 年 11 月的諮詢文件已經寫明香港目前沒有版權專門的封鎖禁制令法定條文
- 照錄：「As for judicial site blocking, section 21L of the High Court Ordinance (Cap. 4) already provides copyright owners with a ready avenue to seek injunctions against online copyright infringements under which an OSP may in appropriate cases be ordered to block the access to one or more online location(s) from which infringing activities originate.」
- 照錄：「we consider it not necessary to introduce a judicial site blocking mechanism specifically for copyright infringements.」（以上兩句出自立法會參考資料摘要第 23(b) 段）
- 照錄：「There are currently no copyright-specific statutory provisions for site blocking injunctions in Hong Kong.」（諮詢文件第 6.6 段）
- 照錄：「The Court of First Instance may by order (whether interlocutory or final) grant an injunction or appoint a receiver in all cases in which it appears to the Court of First Instance to be just or convenient to do so.」（高等法院條例第 21L(1) 條）
- 文件：Legislative Council Brief, Copyright Ordinance (Chapter 528), Copyright (Amendment) Bill 2022，File Ref. CITB CR 07/09/28（行政會議 2022-05-17 通過，檔名日期 2022-05-25）。Consultation Paper on Updating Hong Kong's Copyright Regime（商務及經濟發展局，2021-11-24 公布）。High Court Ordinance (Cap. 4) s.21L
- 網址：立法會參考資料摘要 <https://www.legco.gov.hk/yr2022/english/brief/citbcr070928_22020525-e.pdf>（本次用網路檔案館副本 <https://web.archive.org/web/2023if_/https://www.legco.gov.hk/yr2022/english/brief/citbcr070928_22020525-e.pdf>）。諮詢文件 <https://www.cedb.gov.hk/archive/assets/resources/citb/consultations-and-punblications/%28Eng%29%20Consultation%20Paper%20on%20Copyright.pdf>（網址的 punblications 是官網原有的拼法）。高等法院條例 <https://www.wipo.int/wipolex/en/text/187130>（WIPO Lex 轉載）
- 一手（政府文件與法規原文）

### HK-2　2022 年版權修訂條例沒有加入封鎖機制

- 事實：《2022 年版權（修訂）條例》（2022 年第 16 號條例，行政長官日期 2022-12-15）的英文全文沒有出現 block 字樣，內容是傳播權、連線服務提供者的責任限制與合理使用等修訂，與 HK-1 政府不另設機制的立場一致。這個結論來自對條例全文做字串檢索
- 文件：Copyright (Amendment) Ordinance 2022（Ord. No. 16 of 2022）
- 網址：<https://www.legco.gov.hk/yr2022/english/ord/2022ord016-e.pdf>（網路檔案館副本 <https://web.archive.org/web/2023if_/https://www.legco.gov.hk/yr2022/english/ord/2022ord016-e.pdf>）
- 一手（條例原文）

### HK-3　實際有沒有法院依第 21L 條對盜版網站發過封鎖令：查不到

- 事實：政府文件寫的是版權擁有人「可以考慮」申請，沒有舉出已發出的案例。本次搜尋沒有找到香港法院對版權侵權網站發出 ISP 封鎖令的判決，有一則搜尋摘要稱截至查到的資料為止沒有這類判決，但沒有取得該文章原文，不能引用
- 一手與二手都沒有可引用的來源

### HK-4　國安法實施細則附表 4，警方可要求服務商移除或封鎖危害國家安全的訊息

- 事實：《香港特別行政區維護國家安全法第四十三條實施細則》（2020 年第 139 號法律公告，2020-07-06 訂立，2020-07-07 實施）附表 4 讓警務處處長在保安局局長批准下授權指定人員，要求發布者移除訊息、要求平台服務商、主機服務商，在前兩者不遵從或不可行時要求網路服務供應商採取「禁制行動」。禁制行動包含移除訊息或限制、停止他人的存取。服務商不遵從的罰則是罰款十萬元與監禁六個月。適用範圍是相當可能構成危害國家安全罪行的電子訊息，與版權無關，由警方行政要求，條文沒有要求法院裁定
- 照錄：「network service provider (網絡服務商) means a person that supplies an internet service, or a specified network service, to the public or a section of the public.」 <!-- docs-style-lint: disable-line -->
- 照錄：「specified network service (指明網絡服務) means a carriage service that enables end-users to access an electronic platform via a connection tunnelled through one or more electronic communication networks.」（附表 4 第 4(2) 條） <!-- docs-style-lint: disable-line -->
- 照錄：「If a service provider fails to comply with a requirement issued under section 7 or 9(3) of this Schedule, the service provider commits an offence and is liable on conviction on indictment to a fine of $100,000 and to imprisonment for 6 months.」（附表 4 第 12(1) 條）
- 註記：條文沒有出現 VPN 一詞，「經由隧道連線存取電子平台」的描述是否對應 VPN 類服務，是本筆記的推論，引用時不要寫成條文明指 VPN。2020 年公布版本之後有沒有修訂與目前生效版本，沒有核對
- 文件：Implementation Rules for Article 43 of the Law of the People's Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region（L.N. 139 of 2020），Schedule 4 Rules on Removing Messages Endangering National Security and on Requiring Assistance
- 網址：<https://www.gld.gov.hk/egazette/pdf/20202449e/cs220202449139.pdf>（官網本次回傳網頁，用網路檔案館副本 <https://web.archive.org/web/2021id_/https://www.gld.gov.hk/egazette/pdf/20202449e/cs220202449139.pdf>）
- 一手（憲報法律公告）

### HK-5　香港對 VPN 的專門法律規範：查不到

- 事實：本次沒有找到規範 VPN 業者或使用者的香港法例或政府聲明。僅有的相關法條文字是 HK-4 對 specified network service 的定義。搜尋到的資料多是 VPN 業者與媒體的二手說法，沒有取得可引用的官方說明
- 一手與二手都沒有可引用的來源

## 未能取得或需要再確認的項目

- CN-6、SG-5、TW-4、HK-3、HK-5：查不到，上面各條已寫明
- IN-3 的第 70B(7) 條罰則：兩種二手說法並存，要回法條原文
- JP-1 的最終決定全文：只取得會議資料的案
- JP-3 的 NTT 取消封鎖：沒有一手來源
- TW-2 的智慧財產局原始新聞稿：沒有取得
- 新加坡 Copyright Act 2021 的全法文字檢索：網站限制沒有取得
