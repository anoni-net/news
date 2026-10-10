# 資料外洩的通報與通知規定

範圍是組織發生個人資料外洩（含不正存取）時，法律上有沒有向主管機關通報、向當事人通知的義務，以及時限與門檻。涵蓋日本、台灣、香港、澳門、中國、新加坡、南韓。第一次整理是寫 `japan-data-breaches-2026`（日本 2026 年 9 月起的網站與服務入侵事件）的時候，查證日期都是 2026-10-09。

幾個容易混淆的地方：

- 通報（向主管機關報告）與通知（告知當事人）是兩件事，各地的門檻與時限不同
- 條文沒寫天數而由指引或辦法寫天數的，來源欄標明是指引、辦法或草案
- 已公布但尚未施行的修法，條目內寫明施行狀態
- 這份筆記只寫一般的個資外洩規定，各地針對關鍵基礎設施或特定行業的事故通報另列，不等同個資外洩通報

## 日本

- 事實：個人情報保護法第 26 條第 1 項規定，個人資料處理事業者發生對個人權利利益有重大危害之虞、且屬個人情報保護委員會規則所定的個人資料洩漏、滅失、毀損等事態時，須向個人情報保護委員會報告。受託處理資料的事業者若依規則通知委託方，可免除自己的報告義務
    - 照錄：「個人情報取扱事業者は、その取り扱う個人データの漏えい、滅失、毀損その他の個人データの安全の確保に係る事態であって個人の権利利益を害するおそれが大きいものとして個人情報保護委員会規則で定めるものが生じたときは、個人情報保護委員会規則で定めるところにより、当該事態が生じた旨を個人情報保護委員会に報告しなければならない。」（第 26 條第 1 項）
    - 照錄：「ただし、当該個人情報取扱事業者が、他の個人情報取扱事業者又は行政機関等から当該個人データの取扱いの全部又は一部の委託を受けた場合であって、個人情報保護委員会規則で定めるところにより、当該事態が生じた旨を当該他の個人情報取扱事業者又は行政機関等に通知したときは、この限りでない。」（第 26 條第 1 項但書）
    - 來源：個人情報の保護に関する法律（平成十五年法律第五十七号），e-Gov 法令檢索（API v1 取得的現行條文），<https://laws.e-gov.go.jp/law/415AC0000000057>，查證日期 2026-10-09
- 事實：同條第 2 項規定，負有報告義務的事業者原則上也須通知本人。本人通知有困難時，可採取保護本人權利利益所需的替代措施
    - 照錄：「前項に規定する場合には、個人情報取扱事業者（同項ただし書の規定による通知をした者を除く。）は、本人に対し、個人情報保護委員会規則で定めるところにより、当該事態が生じた旨を通知しなければならない。」（第 26 條第 2 項）
    - 照錄：「ただし、本人への通知が困難な場合であって、本人の権利利益を保護するため必要なこれに代わるべき措置をとるときは、この限りでない。」（第 26 條第 2 項但書）
    - 來源：同上，查證日期 2026-10-09
- 事實：施行規則第 7 條列出四種報告對象事態：含需特別留意個人資料（要配慮個人情報）者、可能因不當利用造成財產損害者、可能出於不正目的之行為造成者，以及本人人數超過 1000 人者（含有發生之虞）。不正存取屬第 3 款，本人人數超過 1000 人時也同時符合第 4 款
    - 照錄：「不正に利用されることにより財産的被害が生じるおそれがある個人データの漏えい等が発生し、又は発生したおそれがある事態」（第 7 條第 2 款）
    - 照錄：「不正の目的をもって行われたおそれがある当該個人情報取扱事業者に対する行為による個人データ（当該個人情報取扱事業者が取得し、又は取得しようとしている個人情報であって、個人データとして取り扱われることが予定されているものを含む。）の漏えい等が発生し、又は発生したおそれがある事態」（第 7 條第 3 款）
    - 照錄：「個人データに係る本人の数が千人を超える漏えい等が発生し、又は発生したおそれがある事態」（第 7 條第 4 款）
    - 來源：個人の権利利益を害するおそれが大きいもの，個人情報の保護に関する法律施行規則，e-Gov 法令檢索，<https://laws.e-gov.go.jp/law/428M60020000003>，查證日期 2026-10-09（「不正存取屬第 3 款」是依條文文字對照的本筆記判斷）
- 事實：施行規則第 8 條規定，知道事態後「速やかに」報告當下已掌握的事項（速報），並在知道事態之日起 30 日以內（第 7 條第 3 款的事態為 60 日以內）報告全部事項（確報）。對本人的通知依第 10 條，在知道事態後依狀況速やかに進行，通知範圍限於保護本人權利利益所必要的事項
    - 照錄：「前条各号に定める事態を知った後、速やかに、当該事態に関する次に掲げる事項（報告をしようとする時点において把握しているものに限る。次条において同じ。）を報告しなければならない。」（第 8 條第 1 項）
    - 照錄：「当該事態を知った日から三十日以内（当該事態が前条第三号に定めるものである場合にあっては、六十日以内）に、当該事態に関する前項各号に定める事項を報告しなければならない。」（第 8 條第 2 項）
    - 照錄：「当該事態の状況に応じて速やかに、当該本人の権利利益を保護するために必要な範囲において、」（第 10 條）
    - 來源：同上，查證日期 2026-10-09
- 事實：「速やか」的天數目安，個人情報保護委員會的指引（通則編）寫為知道事態後概ね 3～5 日以內，這是指引的目安，條文本身沒有寫天數。委員會網頁以圖片標示速報為發覺日起 3〜5 日以內、確報為 30 日以內（不正目的為 60 日以內）
    - 照錄：「「速やか」の日数の目安については、個別の事案によるものの、個人情報取扱事業者が当該事態を知った時点から概ね3～5日以内である。」（指引 3-5-3-3）
    - 照錄：「まずは、速報（新規）発覚日から、3〜5日以内」（網頁圖片的 alt 文字）
    - 來源：個人情報の保護に関する法律についてのガイドライン（通則編），個人情報保護委員会，<https://www.ppc.go.jp/personalinfo/legal/guidelines_tsusoku/>，漏えい等の対応とお役立ち資料，<https://www.ppc.go.jp/personalinfo/legal/leakAction/>，查證日期 2026-10-09
- 事實：違反第 26 條時，委員會可依第 148 條第 1 項勧告，在個人重大權利利益侵害迫切時可依第 2 項命令。違反命令處 1 年以下拘禁刑或 100 萬日圓以下罰金，法人為 1 億日圓以下罰金
    - 照錄：「第百四十八条第二項又は第三項の規定による命令に違反した場合には、当該違反行為をした者は、一年以下の拘禁刑又は百万円以下の罰金に処する。」（第 178 條）
    - 照錄：「一億円以下の罰金刑」（第 184 條第 1 項第 1 款）
    - 來源：個人情報の保護に関する法律，e-Gov 法令檢索，<https://laws.e-gov.go.jp/law/415AC0000000057>，查證日期 2026-10-09
- 事實：2026 年修法已公布但尚未施行：令和 8 年 7 月 10 日成立、7 月 17 日公布，原則上在公布日起 2 年內以政令定施行日。內容含放寬「本人權利利益受害之虞較小時」的本人通知義務（第 26 條第 2 項），並新增課徵金制度。到 2026-10-09 委員會頁面仍寫「引き続き、政令、規則、ガイドライン等の検討を行ってまいります」，因此上列第 26 條與施行規則的現行規定仍適用
    - 照錄：「令和８年７月10日の国会において可決、成立し、令和８年７月17日に「個人情報の保護に関する法律等の一部を改正する法律」が公布されました。」
    - 照錄：「漏えい等発生時について、本人の権利利益の保護に欠けるおそれが少ない場合は、本人への通知義務を緩和する。(第26条第２項)」
    - 照錄：「施行期日 原則として公布の日から起算して２年を超えない範囲内」
    - 來源：令和８年 改正個人情報保護法について，個人情報保護委員会，<https://www.ppc.go.jp/personalinfo/legal/r8kaiseihogohou/>，個人情報保護法等の一部を改正する法律について（令和 8 年 7 月），<https://www.ppc.go.jp/files/pdf/260717_kaiseihounitsuite.pdf>，查證日期 2026-10-09（尚未施行是依委員會頁面未寫施行日期判斷，沒有找到政令）
- 事實：2026-10-07 個人情報保護委員會對大量個人資料處理事業者發出注意喚起，提醒第 23 條安全管理措施與第 22 條不再需要的個人資料應遲滯消去，並預告通則編別添「手法の例示」將於明年 4 月確定修訂。這是行政指導性質的注意喚起，不是新的報告義務
    - 照錄：「見直しの内容の確定は、来年４月を予定していますが、近時の動向を踏まえて、「手法の例示」として、より参考になると考えられるため、見直し予定の内容を先取りする形でお示しします。」
    - 來源：大規模な漏えい等事案を踏まえた対応について（注意喚起）（令和８年10月７日），個人情報保護委員会，<https://www.ppc.go.jp/files/pdf/261007_houdou.pdf>，查證日期 2026-10-09

## 台灣

- 事實：現行有效的個資法第 12 條（2025 年修法施行前）只規定對當事人的通知義務，適用公務機關與非公務機關，沒有向主管機關通報的法定條文，也沒有通知時限（條文為「查明後以適當方式」）。
    - 照錄：「公務機關或非公務機關違反本法規定，致個人資料被竊取、洩漏、竄改或其他侵害者，應查明後以適當方式通知當事人。」（第 12 條）
    - 來源：個人資料保護法歷史法規（民國 112 年 05 月 31 日版，修正前仍有效的條文），https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=I0050021 ，查證日期 2026-10-09
- 事實：2025 年修正的個資法已於民國 114 年 11 月 11 日（2025-11-11）由總統公布，修正第 12 條等條文，但修正條文的施行日期「由行政院定之」，全國法規資料庫於 2026-10-09 仍顯示「部分或全部條文尚未生效，最後生效日期：未定」，所以新版第 12 條尚未施行。
    - 照錄：「中華民國一百十四年十一月十一日總統華總一經字第11400114521號令修正公布第1-1、12、18、21、22～26、41、47～49、52、53、55條條文；增訂第1-2、20-1、21-1～21-5、51-1、53-1條條文及第三章之一章名、第一節節名、第二節節名；並刪除第27條條文；施行日期，由行政院定之」（沿革） <!-- docs-style-lint: disable-line -->
    - 照錄：「※本法規部分或全部條文尚未生效，最後生效日期：未定」（頁首狀態）
    - 來源：個人資料保護法沿革，https://law.moj.gov.tw/LawClass/LawHistory.aspx?pcode=I0050021 ，與 個人資料保護法（全國法規資料庫，法規代碼 I0050021），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021 ，頁面顯示修正日期民國 114 年 11 月 11 日、生效狀態為部分條文尚未生效，查證日期 2026-10-09
- 事實：修正後第 12 條（已公布、尚未施行）：公務機關與非公務機關知悉個資被竊取、竄改、毀損、滅失或洩漏時都應通知當事人，另新增符合一定通報範圍時須通報，非公務機關向主管機關通報（主管機關受理後轉知目的事業主管機關），並要求採取應變措施與保存紀錄。
    - 照錄：「公務機關或非公務機關知悉所保有之個人資料被竊取、竄改、毀損、滅失或洩漏時，應通知當事人。」（第 12 條第 1 項）
    - 照錄：「前項情形符合一定通報範圍者，公務機關或非公務機關應通報下列機關：」（第 12 條第 2 項）
    - 照錄：「二、非公務機關：向主管機關通報。主管機關受理通報後，並轉知其目的事業主管機關。」（第 12 條第 2 項第 2 款）
    - 照錄：「前三項應通知或通報之內容、方式、時限與通報範圍、應變措施、紀錄保存及其他相關事項之辦法，由主管機關定之。」（第 12 條第 4 項）
    - 來源：個人資料保護法（全國法規資料庫，法規代碼 I0050021），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021 ，頁面顯示修正日期民國 114 年 11 月 11 日、生效狀態為部分條文尚未生效，查證日期 2026-10-09
- 事實：修正後的第 12 條只在母法授權辦法訂定通知與通報的「時限」和「通報範圍」，母法條文本身沒有寫出小時數或筆數門檻。
    - 照錄：「前三項應通知或通報之內容、方式、時限與通報範圍、應變措施、紀錄保存及其他相關事項之辦法，由主管機關定之。」（第 12 條第 4 項）
    - 來源：個人資料保護法（全國法規資料庫，法規代碼 I0050021），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021 ，頁面顯示修正日期民國 114 年 11 月 11 日、生效狀態為部分條文尚未生效，查證日期 2026-10-09
- 事實：主管機關是個人資料保護委員會（第 1-1 條，112 年 5 月增訂，施行日期同樣由行政院定之）。個資會須先有組織法才能成立，個資會籌備處於 2025-10-17 的新聞稿表示組織法草案尚待立法程序，行政院將另行指定新法施行日期。
    - 照錄：「本法之主管機關為個人資料保護委員會。」（第 1-1 條）
    - 照錄：「個資會之正式成立，仍須俟組織法立法通過後始有法源依據；目前組織法草案業經立法院「司法及法制委員會」初審完竣，尚待進一步完成立法程序。未來行政院將配合組織法在立法院之審議進度，並審酌相關行政準備作業時間後，另行指定個資法新法之施行日期。」（個資會籌備處新聞稿） <!-- docs-style-lint: disable-line -->
    - 來源：個人資料保護委員會籌備處新聞稿〈立法院三讀通過「個人資料保護法」部分條文修正草案〉（上版日期 114-10-17），https://www.pdpc.gov.tw/News_Content/20/1001/ ，與 個人資料保護法（全國法規資料庫，法規代碼 I0050021），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021 ，頁面顯示修正日期民國 114 年 11 月 11 日、生效狀態為部分條文尚未生效，查證日期 2026-10-09
- 事實：個資會籌備處的修法問答集（114-12-26）明確寫施行日期由行政院於個資會組織法完成立法後另行決定，施行前仍依現行有效個資法辦理。
    - 照錄：「新法之施行日期，將由行政院於個資會組織法完成立法後，審酌個資會成立所需行政作業時間及重要子法整備情形等另行決定。」（Q2）
    - 照錄：「在行政院決定個資法新法施行日期前，仍應依現行有效之個資法規定辦理個人資料保護事項。」（Q2）
    - 來源：個人資料保護委員會籌備處〈個人資料保護法修法問答集〉，上版日期 114-12-26，https://ws.pdpc.gov.tw/FS01/FilePath/3/relfile/30/1072/a842b3f2-3399-4742-96ae-3f6648bd071a.pdf ，查證日期 2026-10-09
- 事實：籌備處在公布當天（2025-11-11）的公告重申修正條文已公布，施行日期另由行政院依第 56 條第 1 項決定。
    - 照錄：「修正條文施行日期，將另由行政院依同法第56條第1項定之。」（籌備處公告）
    - 照錄：「本法施行日期，由行政院定之。」（第 56 條第 1 項）
    - 來源：個人資料保護委員會籌備處公告（上版日期 114-11-11），https://www.pdpc.gov.tw/News_Content/20/1010 ，查證日期 2026-10-09
- 事實：個資會組織法在全國法規資料庫查不到：以「個人資料保護委員會」檢索中央法規，法規名稱只有籌備處的暫行組織規程、編制表與辦事細則三筆（檢索範圍限該站，立法院議事進度未另行查證）。
    - 照錄：「個人資料保護委員會籌備處暫行組織規程」（檢索結果第 1 筆）
    - 來源：全國法規資料庫檢索結果，https://law.moj.gov.tw/Law/LawSearchResult.aspx?ty=ONEBAR&kw=個人資料保護委員會 ，查證日期 2026-10-09
- 事實：通報時限與範圍的辦法尚在草案：個資會籌備處 2026-01-22 預告「個人資料事故通知通報及應變辦法」草案（頁面修改日期 115-03-04），草案規定知悉後 72 小時內個別通知當事人，並訂定通報三種範圍，施行日期由主管機關定之。至 2026-10-09 籌備處網站公告列表最新一則為 115-03-09，未見該辦法正式發布，全國法規資料庫以「個人資料事故通知通報」檢索也查無法規名稱。
    - 照錄：「應於知悉時起七十二小時內以適當方式個別通知當事人。」（草案第 2 條第 1 項）
    - 照錄：「個資事故屬下列通報範圍之一者，事故機關應於知悉時起七十二小時內依主管機關指定之方式向本法第十二條第二項所定機關辦理個資事故之通報：」（草案第 3 條第 1 項）
    - 照錄：「涉有本法第六條第一項所規定之個人資料。」（草案第 3 條第 1 項第 1 款）
    - 照錄：「所涉之資通系統保有個人資料筆數達一萬筆以上。」（草案第 3 條第 1 項第 2 款）
    - 照錄：「所影響之個人資料筆數達一百筆以上。」（草案第 3 條第 1 項第 3 款）
    - 照錄：「本辦法施行日期，由主管機關定之。」（草案第 7 條）
    - 來源：個人資料保護委員會籌備處公告〈預告訂定「個人資料事故通知通報及應變辦法」草案〉，上版日期 115-01-22，https://www.pdpc.gov.tw/News_Content/20/1099 ，附件為草案 docx（草案，非正式發布），查證日期 2026-10-09
- 事實：同一份草案規定事故紀錄至少保存五年，且若事故機關有正當事由未能於 72 小時內通知，須敘明事由並於事由消滅後 72 小時內補行通知（草案，尚未生效）。
    - 照錄：「前項相關紀錄，應於知悉個資事故之翌日起至少保存五年。」（草案第 6 條第 2 項）
    - 照錄：「應敘明具體事由送本法第十二條第二項受理通報之機關，並應於未能如期通知之事由消滅後七十二小時內依第一項規定補行通知。」（草案第 2 條第 4 項）
    - 來源：同上草案（個人資料保護委員會籌備處公告 1099 附件，草案），查證日期 2026-10-09
- 事實：非公務機關目前向目的事業主管機關通報的依據是各產業的個資檔案安全維護辦法（依修正前第 27 條第 3 項訂定），例如金管會的辦法適用金融控股公司、銀行業、證券業、期貨業、保險業、電子支付機構等，重大個資事故須於 72 小時內通報金管會。
    - 照錄：「本辦法依個人資料保護法（以下簡稱本法）第二十七條第三項規定訂定之。」（第 1 條）
    - 照錄：「非公務機關遇有重大個人資料事故者，應依附件格式於七十二小時內通報本會。」（第 6 條第 2 項）
    - 照錄：「前項所稱重大個人資料事故，係指個人資料遭竊取、竄改、毀損、滅失或洩漏，將危及非公務機關正常營運或大量當事人權益之情形。」（第 6 條第 3 項）
    - 照錄：「一、金融控股公司。」（第 2 條第 1 項）
    - 照錄：「二、銀行業。」（第 2 條第 1 項）
    - 照錄：「三、證券業。」（第 2 條第 1 項）
    - 來源：金融監督管理委員會指定非公務機關個人資料檔案安全維護辦法（修正日期民國 110 年 12 月 14 日），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=G0380233 ，查證日期 2026-10-09（頁面法規整編資料截止日民國 115 年 10 月 02 日）
- 事實：數位發展部的辦法適用其附表一所列的數位經濟相關產業業者，知悉個資安全事故將危及正常營運或大量當事人權益時，須於 72 小時內通報數發部（或通報直轄市、縣市政府時副知數發部）。
    - 照錄：「業者遇有個人資料安全事故，將危及其正常營運或大量當事人權益者，應於知悉事故後七十二小時內依附表二格式通報本部，或通報直轄市、縣（市）政府時副知本部。」（第 8 條第 2 項）
    - 照錄：「本辦法所稱數位經濟相關產業（以下簡稱業者），指從事附表一所列行業之自然人、私法人或其他團體。」（第 2 條）
    - 來源：數位經濟相關產業個人資料檔案安全維護管理辦法（發布日期民國 112 年 10 月 12 日），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0010162 ，查證日期 2026-10-09
- 事實：產業辦法沒有統一時限：各辦法各自規定，金管會與數發部這兩個辦法都是 72 小時、限重大或危及營運與大量當事人權益的事故。修正後個資法第 51 條之 1 讓目的事業主管機關在過渡期間仍可訂辦法，籌備處問答集說明原辦法中與新法不同的事故通報等規定須配合修正。
    - 照錄：「原有辦法之內容，如在新法(含授權子法)中已有不同規定，應配合修正。(例如：事故通報等義務)」（問答集關於第 51 條之 1 的一則（未標 Q 編號，位於問答集後段））
    - 來源：個人資料保護委員會籌備處〈個人資料保護法修法問答集〉，https://ws.pdpc.gov.tw/FS01/FilePath/3/relfile/30/1072/a842b3f2-3399-4742-96ae-3f6648bd071a.pdf ，查證日期 2026-10-09
- 事實：現行有效的罰則（修正前第 48 條）：非公務機關違反通知義務（第 12 條），由中央目的事業主管機關或直轄市、縣（市）政府限期改正，屆期未改正按次處新臺幣 2 萬元以上 20 萬元以下罰鍰。違反安全維護義務（第 27 條）處 2 萬元以上 200 萬元以下罰鍰，情節重大處 15 萬元以上 1,500 萬元以下。
    - 照錄：「二、違反第十條、第十一條、第十二條或第十三條規定。」（第 48 條第 1 項第 2 款）
    - 照錄：「非公務機關違反第二十七條第一項或未依第二項訂定個人資料檔案安全維護計畫或業務終止後個人資料處理方法者，由中央目的事業主管機關或直轄市、縣（市）政府處新臺幣二萬元以上二百萬元以下罰鍰」（第 48 條第 2 項）
    - 照錄：「由中央目的事業主管機關或直轄市、縣（市）政府處新臺幣十五萬元以上一千五百萬元以下罰鍰，並令其限期改正，屆期未改正者，按次處罰。」（第 48 條第 3 項）
    - 來源：個人資料保護法歷史法規（民國 112 年 05 月 31 日版，修正前仍有效的條文），https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=I0050021 ，查證日期 2026-10-09
- 事實：修正後（尚未施行）的罰則：違反通知義務由主管機關令限期改正、屆期未改正按次處 2 萬元以上 20 萬元以下罰鍰。違反通報、應變措施或紀錄保存規定，由主管機關直接處 2 萬元以上 20 萬元以下罰鍰並令限期改正。違反安全維護義務最高 200 萬元，情節重大 15 萬元以上 1,500 萬元以下。
    - 照錄：「三、違反第十二條第一項或依第四項所定辦法中有關通知之內容、方式或時限之規定。」（第 48 條第 1 項第 3 款）
    - 照錄：「非公務機關違反第十二條第二項、第三項或依第四項所定辦法中有關通報之內容、方式、時限、應變措施、紀錄保存之規定者，由主管機關處新臺幣二萬元以上二十萬元以下罰鍰，並令其限期改正，屆期未改正者，按次處罰。」（第 48 條第 2 項）
    - 照錄：「一、違反第二十條之一第一項規定。」（第 48 條第 3 項第 1 款）
    - 來源：個人資料保護法（全國法規資料庫，法規代碼 I0050021），https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021 ，頁面顯示修正日期民國 114 年 11 月 11 日、生效狀態為部分條文尚未生效，查證日期 2026-10-09

## 香港

- 事實：一般個人資料外洩（適用所有資料使用者）目前沒有法定通報義務，向私隱專員公署通報屬建議做法（自願）
    - 照錄：「While it is not a statutory requirement on data users to inform the PCPD about a data breach incident concerning the personal data held by them, data users are nevertheless advised to do so as a recommended practice for proper handling of such incident.」
    - 來源：個人資料私隱專員公署（PCPD）「Data Breach Notification」網頁，https://www.pcpd.org.hk/english/enforcement/data_breach_notification/dbn.html ，頁面無文件日期，查證日期 2026-10-09（該日頁面仍是此寫法）。《個人資料（私隱）條例》（第 486 章）全文在 elegislation.gov.hk 為 JavaScript 動態頁面，未能抓成純文字，法定與否以公署此頁為準

- 事實：香港的外洩通報制度是 2010 年起設立的自願制度（沿革背景）
    - 照錄：「The voluntary notification system was formally established in 2010 in response to a review of PDPO in 2009.」
    - 來源：立法會秘書處資料研究組《Mandatory personal data breach notification》（Essentials ISE02/2019-20），https://www.legco.gov.hk/research-publications/english/essentials-1920ise02-mandatory-personal-data-breach-notification.htm ，為立法會秘書處的研究簡報，屬 2019-20 年度文件（早於現況，僅作沿革），查證日期 2026-10-09

- 事實：公署現行指引為「Guidance on Data Breach Handling and Data Breach Notifications」，2023 年 6 月版，2023-06-30 發布，2026-10-09 公署網站仍連結此版
    - 照錄：「Date: 30 June 2023」
    - 來源：PCPD 新聞稿《Privacy Commissioner's Office Issues New Guidance on Data Breach Handling and Data Breach Notifications To Safeguard Data Security》，https://www.pcpd.org.hk/english/news_events/media_statements/press_20230630.html ，2023-06-30。指引本文 PDF 頁尾標示「June 2023」，https://www.pcpd.org.hk/english/resources_centre/publications/files/guidance_note_dbn_e.pdf ，公署 Data Security 頁 https://www.pcpd.org.hk/english/data_security/ 仍連結同一檔案。查證日期 2026-10-09

- 事實：指引建議在「切實可行範圍內盡快」（as soon as practicable）通報公署與受影響的當事人，原文沒有具體小時數或日數
    - 照錄：「In general, the data user should notify the PCPD and the affected data subjects as soon as practicable after becoming aware of the data breach, particularly if the data breach is likely to result in a real risk of harm to those affected data subjects.」
    - 來源：《Guidance on Data Breach Handling and Data Breach Notifications》（2023 年 6 月），第 6 頁 Step 4，https://www.pcpd.org.hk/english/resources_centre/publications/files/guidance_note_dbn_e.pdf ，全文以 grep 檢索「N hours」、「N days」、「within N」皆無命中，查證日期 2026-10-09

- 事實：指引就通報時點的描述，是不必等內部調查完成
    - 照錄：「A notification should generally be given as soon as practicable after becoming aware of the incident, regardless of the progress of any internal investigation.」
    - 來源：同上指引第 8 頁「When to notify?」，公署 Data Security 頁（https://www.pcpd.org.hk/english/data_security/ ）有相同句子，查證日期 2026-10-09

- 事實：指引提到特定行業另有規範，上市公司與認可機構（銀行）受各自規則約束，與一般資料外洩通報分開。細節未查各規範原文
    - 照錄：「For instance, the disclosure obligations under the Listing Rule apply to listed companies. The guidelines promulgated by the Hong Kong Monetary Authority about reporting data breaches apply to authorised institutions.」
    - 來源：同上指引第 6 頁註腳 4（此為公署指引對他規範的轉述，屬二手，未查證證券上市規則與金管局指引原文），查證日期 2026-10-09

- 事實：政府與公署的修訂建議（建議，非條例草案）包括設立強制性個人資料外洩通報機制，2025-01-22 時政府仍在研究階段，尚無具體條文
    - 照錄：「its preliminary amendment suggestions include: (1) establishing a mandatory personal data breach notification mechanism; (2) directly regulating data processors; (3) requiring data users to establish a personal data retention period policy; (4) strengthening sanctions and empowering the Privacy Commissioner for Personal Data to hand down administrative fines; (5) clarifying the definition of personal data, etc.」
    - 來源：立法會二題《Prevention of personal data breaches and financial crimes》，政制及內地事務局局長書面答覆，https://www.info.gov.hk/gia/general/202501/22/P2025012200305.htm ，2025-01-22，查證日期 2026-10-09

- 事實：2026-02-13 立法會政制事務委員會會議上，政府表示正調整修例建議（考慮分階段實施、行政罰款水平），具體方案完成後才會諮詢委員會，狀態仍是研究中
    - 照錄：「當研究完畢並有具體方案時，政府當局會盡早諮詢事務委員會。」
    - 來源：立法會 CB(2)196/2026(03) 號文件《關於個人資料私隱專員公署的工作的背景資料簡介》，https://www.legco.gov.hk/yr2026/chinese/panels/ca/papers/ca20260213cb2-196-3-c.pdf ，政制事務委員會 2026-02-13 會議文件（秘書處綜述 2025 立法會會期的討論），查證日期 2026-10-09

- 事實：公署在 2026-02-13 會議文件中表示，期望 2026 年內向立法會匯報修例研究進度
    - 照錄：「我們期望今年內向立法會滙報相關工作的進展。」
    - 來源：立法會 CB(2)196/2026(02) 號文件《個人資料私隱專員公署 2025 年工作報告》第 57 段，https://www.legco.gov.hk/yr2026/chinese/panels/ca/papers/ca20260213cb2-196-2-c.pdf ，2026-02-13 會議文件，查證日期 2026-10-09

- 事實：私隱專員在 2026-02-13 會議上說明修例方向是把外洩通報訂為強制，並確認目前並非強制
    - 照錄：「目前的方向是將資料外泄的通報訂為強制性，因為現時並非強制。」
    - 來源：立法會 CB(2)293/2026 號文件，政制事務委員會 2026-02-13 會議紀要，https://www.legco.gov.hk/yr2026/chinese/panels/ca/minutes/ca20260213.pdf （紀要原文用字為「外泄」），查證日期 2026-10-09

- 事實：截至 2026-07-13，政府文件仍寫為「研究優化」條例，立法會議員追問時間表時，官員答覆由相關政策局與部門檢視。2026-10-09 為止查不到已公布的修訂條例草案、諮詢文件或提交立法會的日期，狀態是研究中的建議
    - 照錄：「政府一直與私隱專員公署緊密合作，研究優化《個人資料（私隱）條例》，以有效防止個人資料外洩事故。」
    - 來源：立法會 CB(2)1000/2026(03) 號文件《有關維護資訊保安的工作》（資訊科技及廣播事務委員會 2026-07-13 討論文件），https://www.legco.gov.hk/yr2026/chinese/panels/itb/papers/itb20260713cb2-1000-3-c.pdf ，同次會議紀要 CB(2)1096/2026 號，https://www.legco.gov.hk/yr2026/chinese/panels/itb/minutes/itb20260713.pdf ，官員答覆原文含「至於詳情，可能需由相關政策局和部門說明。」，查證日期 2026-10-09

- 事實：《保護關鍵基礎設施（電腦系統）條例》（第 653 章，2025 年第 4 號條例）自 2026-01-01 實施，是關鍵基礎設施的電腦系統安全規定，與一般個人資料外洩通報分開
    - 照錄：「現根據《保護關鍵基礎設施(電腦系統)條例》(第653章)第1(2)條，指定2026年1月1日為該條例開始實施的日期。」
    - 來源：《〈保護關鍵基礎設施(電腦系統)條例〉(生效日期)公告》（2025 年第 144 號法律公告，保安局局長 2025-06-18 簽署），https://www.legco.gov.hk/yr2025/chinese/subleg/negative/2025ln144-c.pdf ，查證日期 2026-10-09

- 事實：該條例只適用於被指定的關鍵基礎設施營運者（八個界別：能源、資訊科技、銀行及金融服務、航空運輸、陸路運輸、海上運輸、醫護服務、電訊及廣播服務，另可含其他影響重大的設施），通報對象是專員，通報的是電腦系統安全事故，不是個人資料外洩
    - 照錄：「any infrastructure that is essential to the continuous provision in Hong Kong of an essential service in a sector specified in Schedule 1」
    - 來源：《Protection of Critical Infrastructures (Computer Systems) Ordinance》（Cap. 653，2025 年第 4 號條例）第 2 條「critical infrastructure」定義與附表 1，https://www.legco.gov.hk/yr2025/english/ord/2025ord004-e.pdf ，「CI operator」定義為依第 12 條被指定的機構，原文：「CI operator (關鍵基礎設施營運者) means an organization designated under section 12」，查證日期 2026-10-09

- 事實：該條例要求關鍵基礎設施營運者在知悉電腦系統安全事故後盡快通報專員，影響核心功能的事故最長 12 小時，其他情況最長 48 小時（適用範圍限關鍵基礎設施營運者）
    - 照錄：「If the computer-system security incident concerned has disrupted, is disrupting or is likely to disrupt the core function of the critical infrastructure concerned—12 hours after the CI operator concerned becomes aware of the incident.」「In any other case—48 hours after the operator becomes aware of the incident.」 <!-- docs-style-lint: disable-line -->
    - 來源：同上條例第 28 條與附表「Specified Time for Notifications under Section 28」，https://www.legco.gov.hk/yr2025/english/ord/2025ord004-e.pdf ，第 28(2)(a) 條原文：「must be made as soon as practicable and in any event within the specified time」，查證日期 2026-10-09

## 澳門

- 事實：第 8/2005 號法律《個人資料保護法》全文查不到資料外洩須通知公權力機關或當事人的條文（以「洩」、「泄」、「事故」檢索全文皆無命中）。與安全相關的是第十五條要求採取適當措施
    - 照錄：「負責處理個人資料的實體應採取適當的技術和組織措施保護個人資料，避免資料的意外或不法損壞、意外遺失、未經許可的更改、傳播或查閱」
    - 來源：第 8/2005 號法律《個人資料保護法》第十五條第一款，《澳門特別行政區公報》第 34 期第一組，2005-08-22，個人資料保護局網站存放的公報檔 https://www.dspdp.gov.mo/file/Laws%20and%20Regulations/%E5%80%8B%E4%BA%BA%E8%B3%87%E6%96%99%E4%BF%9D%E8%AD%B7%E6%B3%95_TC.pdf ，查證日期 2026-10-09

- 事實：該法第二十一條的「通知」義務是向公權力機關通知資料處理（自動化處理的登記性通知），不是外洩通報
    - 照錄：「應從處理開始起八日期限內以書面形式，將為了實現一個或多個相互關聯的目的而進行的一個或一系列、全部或部分自動化處理，通知公共當局。」
    - 來源：同上，第 8/2005 號法律第二十一條第一款（第六章「通知和許可」），查證日期 2026-10-09

- 事實：個人資料保護局（原稱個人資料保護辦公室）網站對外洩的說明只談責任歸屬，沒有外洩通報指引。網站「指引」頁列出的 12 份指引沒有外洩通報主題
    - 照錄：「如資料外洩，負責實體須承擔倘有之法律責任，即使過失亦然；除非負責實體能證明資料的外洩是由他人造成的。」 <!-- docs-style-lint: disable-line -->
    - 來源：個人資料保護局「基本概念」頁，https://www.dspdp.gov.mo/zh_tw/basic_concepts.html ，無文件日期，「指引」頁 https://www.dspdp.gov.mo/zh_tw/legal_guidelines.html ，另有常見問題「如機構的電腦系統被黑客入侵而導致資料外洩，有關機構是否需要承擔責任？」（https://www.dspdp.gov.mo/zh_tw/FAQ_detail/article/l1pva6vj.html ）只引用第十五條與第十四條談責任，查證日期 2026-10-09

- 事實：澳門該機關現稱「個人資料保護局」，2025 年的政府答覆與機關網站標題已使用此名稱（改名時點未查證）
    - 照錄：「經徵詢個人資料保護局及司法警察局之意見」
    - 來源：保安司司長辦公室對立法會議員書面質詢的答覆（簽署日 2025-08-28），https://al.gov.mo/uploads/attachment/2025-09/8949368c1467ddb1a8.pdf ，查證日期 2026-10-09

- 事實：第 13/2019 號法律《網絡安全法》針對關鍵基礎設施營運者，是網絡安全事故通報，不等同個人資料外洩通報。適用對象包括公共與私人營運者 <!-- docs-style-lint: disable-line -->
    - 照錄：「本法律適用於關鍵基礎設施的公共及私人營運者。」
    - 來源：第 13/2019 號法律《網絡安全法》第四條第一款，《澳門特別行政區公報》第 25 期第一組，2019-06-24，立法會網站存放的公報檔 https://al.gov.mo/uploads/attachment/2019-06/650555d104d003759f.pdf ，查證日期 2026-10-09。公報官方站（bo.io.gov.mo、bo.dsaj.gov.mo）在查證環境無法連線或回 403，改用立法會網站的同一份公報頁 <!-- docs-style-lint: disable-line -->

- 事實：私人營運者涵蓋的領域包括供水、銀行財務保險、醫院、污水與垃圾處理、燃料與食品批發、電力與天然氣、公共運輸、港口與機場、視聽廣播、博彩、電信與互聯網接入
    - 照錄：「（12）經營固定或流動的公共電信網絡，以及提供互聯網接入服務；」 <!-- docs-style-lint: disable-line -->
    - 來源：同上，第四條第三款（一）項各分項，查證日期 2026-10-09

- 事實：法律所稱「網絡安全事故」是針對資訊網絡、電腦系統及電腦數據資料的未經許可行為或實際不利影響事件，範圍比個人資料外洩廣也不同 <!-- docs-style-lint: disable-line -->
    - 照錄：「“網絡安全事故”：是指任何構成未經許可的行為的情況，以及通常對資訊網絡、電腦系統及電腦數據資料的安全造成實際不利影響的任何事件」 <!-- docs-style-lint: disable-line -->
    - 來源：同上，第二條第一款（六）項，查證日期 2026-10-09

- 事實：私人營運者在發生網絡安全事故時，須通知網絡安全事故預警及應急中心並告知監管實體。法律條文本身沒有寫出時限（全文以「小時」、「時限」、「期限」檢索，無與通報時限相關的命中） <!-- docs-style-lint: disable-line -->
    - 照錄：「在發生網絡安全事故時，通知預警及應急中心，並將有關事實告知相關監管實體，以及立即開展應對嚴重的網絡安全事故的行動」 <!-- docs-style-lint: disable-line -->
    - 來源：同上，第十一條（三）項（標題「程序性、預防性及應變性義務」），查證日期 2026-10-09

- 事實：公共營運者須在其職責範圍內履行第十一條至第十三條的義務，通報義務同樣涵蓋
    - 照錄：「對內及在由其負責網絡安全的公共部門、機關或實體範圍內，履行和促使履行第十一條至第十三條規定的義務」 <!-- docs-style-lint: disable-line -->
    - 來源：同上，第十四條第一款（三）項，查證日期 2026-10-09

- 事實：《網絡安全法》2019-12-22 生效，通報的具體時限寫在技術規範，官方說明只寫「規定時限」，具體小時數在已存的官方頁面查不到 <!-- docs-style-lint: disable-line -->
    - 照錄：「根據其嚴重性在規定時限內向預警及應急中心和監管實體作出通報，並定期匯報事故的應急處置工作進展情況」
    - 來源：治安警察局「發佈通用技術規範 明確網安義務要求」（頁面檔名編號 SaU200615，約 2020 年 6 月），https://www.fsm.gov.mo/psp/cht/SaU200615.html ，說明《網絡安全—事故預警、應對及通報規範》「已於本年5月13日刊登於《澳門特別行政區公報》，並自5月14日起正式生效」，生效日：政府入口網站新聞「第13/2019號法律《網絡安全法》今（22）日正式生效。」，https://www.gov.mo/zh-hant/news/312095/ ，2019-12-22，查證日期 2026-10-09 <!-- docs-style-lint: disable-line -->

- 事實：2026-10-09 為止，查不到《個人資料保護法》或《網絡安全法》的修法計畫或公布的草案。已公布的是網安中心（網絡安全事故預警及應急中心）更新兩份技術規範（含事故通報規範），屬技術規範不是法律 <!-- docs-style-lint: disable-line -->
    - 照錄：「網安中心已啟動修訂網絡安全規範相關工作，對《網絡安全——管理基準規範》、《網絡安全——事故預警、應對及通報規範》兩份技術規範文件進行全面更新」 <!-- docs-style-lint: disable-line -->
    - 來源：政府入口網站新聞《“2026年國家網絡安全宣傳周 — 澳門分論壇”舉行》，https://www.gov.mo/zh-hant/news/1266967/ ，2026-09-18，2026 年施政報告（2025-11-18 向立法會提出）全文檢索「個人資料保護法」、「網絡安全法」皆無命中，https://www.policyaddress.gov.mo/data/policyAddress/2026/zh-hant/2026_policy_c.pdf ，查證日期 2026-10-09 <!-- docs-style-lint: disable-line -->

- 事實：2025 年政府對立法會質詢的答覆中，網安中心表示會適時研究數據安全制度與配套措施，內容針對數據安全，並未提及修訂《個人資料保護法》或增訂外洩通報
    - 照錄：「適時研究制定有利於促進和保障數據安全的制度及配套措施」
    - 來源：保安司司長辦公室對立法會議員書面質詢的答覆（簽署日 2025-08-28），https://al.gov.mo/uploads/attachment/2025-09/8949368c1467ddb1a8.pdf ，查證日期 2026-10-09

## 新加坡

- 事實：通報義務的對象是 PDPA 適用的組織，資料外洩（data breach）定義為個人資料遭未經授權的存取、蒐集、使用、揭露、複製、修改或處置，或儲存媒體遺失且上述情形很可能發生。
    - 照錄：「In this Part, unless the context otherwise requires」
    - 照錄：「the unauthorised access, collection, use, disclosure, copying, modification or disposal of personal data; or」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26A）
- 事實：構成 notifiable data breach 的條件是對當事人造成或很可能造成重大損害（significant harm），或達到或很可能達到重大規模（significant scale）。僅發生在組織內部的外洩視為不屬於 notifiable。
    - 照錄：「A data breach is a notifiable data breach if the data breach」
    - 照錄：「results in, or is likely to result in, significant harm to an affected individual; or」
    - 照錄：「is, or is likely to be, of a significant scale.」
    - 照錄：「a data breach that relates to the unauthorised access, collection, use, disclosure, copying or modification of personal data only within an organisation is deemed not to be a notifiable data breach.」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26B(1)、s26B(4)）
- 事實：「重大規模」的法定人數門檻為 500 人，授權法規定於 2021 年通報規則第 4 條，PDPC 指引另寫明受影響達 500 人以上即須通報，即使不涉及指定的個人資料類別。
    - 照錄：「the prescribed number of affected individuals is 500.」
    - 照錄：「Where a data breach affects 500 or more」
    - 照錄：「individuals, the organisation is required to notify the Commission, even if the data」
    - 來源：Personal Data Protection (Notification of Data Breaches) Regulations 2021（SL 64/2021），Singapore Statutes Online，https://sso.agc.gov.sg/SL/PDPA2012-S64-2021，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（reg 4），以及 PDPC, Advisory Guidelines on Key Concepts in the Personal Data Protection Act（Issued 23 September 2013，Revised 29 April 2026），https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/ag-on-key-concepts/advisory-guidelines-on-key-concepts-in-the-pdpa-17-may-2022.pdf（檔名帶 2022，內文封面為 Revised 29 April 2026），查證日期 2026-10-09（para 20.20）
- 事實：組織有理由相信發生外洩時，須以合理且迅速的方式評估是否屬 notifiable。法條本身沒有寫 30 天，30 calendar days 是 PDPC 指引的一般期待，超過時應準備向 PDPC 說明原因。
    - 照錄：「conduct, in a reasonable and expeditious manner, an assessment of whether the data breach is a notifiable data breach.」
    - 照錄：「organisations should generally do so within 30 calendar days.」
    - 照錄：「unable to complete its assessment within 30 days, it would be prudent for the」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26C(2)），以及 PDPC, Advisory Guidelines on Key Concepts in the Personal Data Protection Act（Issued 23 September 2013，Revised 29 April 2026），https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/ag-on-key-concepts/advisory-guidelines-on-key-concepts-in-the-pdpa-17-may-2022.pdf（檔名帶 2022，內文封面為 Revised 29 April 2026），查證日期 2026-10-09（para 20.4）
- 事實：評估認定屬 notifiable 後，須盡速通報 PDPC，最遲在作出評估當日之後 3 個曆日（calendar days）內。通報須含規則列明的資訊，延遲通報須另附理由與佐證。
    - 照錄：「the organisation must notify the Commission as soon as is practicable, but in any case no later than 3 calendar days after the day the organisation makes that assessment.」
    - 照錄：「the notification to the Commission must additionally specify the reasons for the late notification and include any supporting evidence.」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26D(1)），以及 Personal Data Protection (Notification of Data Breaches) Regulations 2021（SL 64/2021），Singapore Statutes Online，https://sso.agc.gov.sg/SL/PDPA2012-S64-2021，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（reg 5(2)）
- 事實：通知當事人的義務只適用於「對當事人可能造成重大損害」的外洩（s26B(1)(a)），僅因規模達 500 人而 notifiable 的案件，法條不要求通知當事人。通知須在通報 PDPC 當下或之後，以「在該情況下合理的方式」進行。
    - 照錄：「the organisation must also notify each affected individual affected by a notifiable data breach mentioned in section 26B(1)(」
    - 照錄：「in any manner that is reasonable in the circumstances.」
    - 照錄：「at the same time or after notifying the Commission.」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26D(2)），以及 PDPC, Advisory Guidelines on Key Concepts in the Personal Data Protection Act（Issued 23 September 2013，Revised 29 April 2026），https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/ag-on-key-concepts/advisory-guidelines-on-key-concepts-in-the-pdpa-17-may-2022.pdf（檔名帶 2022，內文封面為 Revised 29 April 2026），查證日期 2026-10-09（para 20.22(b)）
- 事實：通知當事人的例外：組織已採取使重大損害不太可能發生的補救行動、或外洩前已有技術性保護措施（如加密）時，不必通知當事人。執法機關指示或 PDPC 指示時則不得通知。PDPC 可依書面申請豁免。
    - 照錄：「renders it unlikely that the notifiable data breach will result in significant harm to the affected individual」
    - 照錄：「An organisation must not notify any affected individual in accordance with subsection (2) if」
    - 照錄：「The Commission may, on the written application of an organisation, waive the requirement to notify an affected individual under subsection (2)」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26D(5)、(6)、(7)）
- 事實：資料中介者（data intermediary）發現外洩時，須「無不當延遲」通知委託它處理資料的組織，由委託組織負責評估與通報。為公部門機關處理資料的中介者則通知該機關。
    - 照錄：「the data intermediary must, without undue delay, notify that other organisation of the occurrence of the data breach」
    - 照錄：「the organisation must, without undue delay, notify the public agency of the occurrence of the data breach.」
    - 來源：Personal Data Protection Act 2012（2020 Revised Edition，Act 26 of 2012）第 6A 部分，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=P16A-，頁面標示 Current version as at 09 Oct 2026，查證日期 2026-10-09（s26C(3)、s26E）
- 事實：PDPC 官網「Required to Notify The PDPC」頁與法條一致，寫明最遲 3 個曆日，並寫明通知當事人須在通報 PDPC 當下或之後。
    - 照錄：「three (3) calendar days.」
    - 照錄：「Organisations must notify affected individuals as soon as practicable, at the same time or after notifying the PDPC.」
    - 來源：PDPC, Required to Notify The PDPC，https://www.pdpc.gov.sg/required-to-notify-the-pdpc，頁面標示 Published on 01 Sep 2026（內文為前端 JSON 內嵌的頁面內容轉成純文字，存於 sg-pdpc-required-to-notify-content.txt），查證日期 2026-10-09
- 事實：PDPC 官網「Report Your Organisation’s Data Breach」頁為通報入口與步驟說明（評估是否 notifiable、通報 PDPC 與當事人、事後處理），並指向自我評估工具與電子表單。
    - 照錄：「It explains how to determine if a breach is notifiable, meet the three-day deadline,」
    - 照錄：「Use this tool to determine if the breach is notifiable」
    - 照錄：「Use our e-service form to submit your notification.」
    - 來源：PDPC, Report Your Organisation’s Data Breach，https://www.pdpc.gov.sg/organisations/e-services/report-your-organisations-data-breach，頁面標示 Published on 22 Apr 2026，查證日期 2026-10-09
- 事實：逾期的後果：PDPC 該頁寫明錯過 3 日期限可能違反通報義務，PDPC 可採取執法行動，含罰款與指令。
    - 照錄：「Organisations that miss the 3-day notification deadline may be in breach of the Data Breach Notification Obligation under the PDPA.」
    - 照錄：「which may include financial penalties and/or directions.」
    - 來源：PDPC, Report Your Organisation’s Data Breach（FAQ），同上網址，Published on 22 Apr 2026，查證日期 2026-10-09
- 事實：PDPC 的資料外洩指引：《Guide on Managing and Notifying Data Breaches Under the PDPA》取代 Guide to Managing Data Breaches 2.0，2021-03-15 更新並納入強制通報要求，2021-02-01 起強制通報生效。本次未取得該指引 PDF 本文，期限數字改以上列法條與 Advisory Guidelines 為準。
    - 照錄：「Revisions to Guide (updated 15 March 2021)」
    - 照錄：「This guide replaces the Guide to Managing Data Breaches 2.0」
    - 照錄：「as part of the enhanced PDPA which came into force on 1 February 2021.」
    - 來源：PDPC, Guide on Managing and Notifying Data Breaches Under the PDPA（頁面），https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic/data-breach-management-guide，頁面標示 Published on 13 Sep 2021，指引更新日 15 March 2021，查證日期 2026-10-09
- 事實：PDPC 2021-03-15 的新聞頁說明已更新外洩管理指引與 Guide on Active Enforcement。
    - 照錄：「The PDPC has updated Guide to Managing Data Breaches 2.0 (now known as the Guide on Managing and Notifying Data Breaches under the PDPA) with details of the mandatory data breach notification requirement under the PDPA.」
    - 來源：PDPC, Revised Guides on Managing Data Breach and Active Enforcement Now Available，https://www.pdpc.gov.sg/media-events/revised-guides-on-managing-data-breach-and-active-enforcement-now-available，頁面標示 Published on 15 Mar 2021，查證日期 2026-10-09
- 事實：罰則上限：PDPC 認定組織故意或過失違反第 6A 部分（含通報義務）時可令其繳納財務罰款（financial penalty），上限為在新加坡年營業額超過 1,000 萬新加坡元者取該年營業額的 10%，其他情形為 100 萬新加坡元（並非「兩者取高」，營業額未逾 1,000 萬者上限仍是 100 萬）。
    - 照錄：「an organisation has intentionally or negligently contravened any provision of Part 3, 4, 5, 6, 6A or 6B」
    - 照錄：「whose annual turnover in Singapore exceeds $10 million — 10% of the annual turnover in Singapore of the organisation;」 <!-- docs-style-lint: disable-line -->
    - 照錄：「in any other case — $1 million.」 <!-- docs-style-lint: disable-line -->
    - 來源：Personal Data Protection Act 2012 s48J，Singapore Statutes Online，https://sso.agc.gov.sg/Act/PDPA2012?ProvIds=pr48J-，頁面標示 Current version as at 09 Oct 2026（本款標註 Act 40 of 2020 wef 01/10/2022），查證日期 2026-10-09

## 南韓

- 事實：개인정보 보호법 第 34 條第 1 項：個資處理者得知個資外洩等時，須「지체 없이」（不得延遲）通知當事人，通知須含外洩項目、時點與經過、當事人可採取的措施、處理者的因應與救濟程序、受理窗口、損害賠償與爭議調解等法律權利等事項。第 2 項（2026-03-10 新設）要求對「有外洩可能」的情形也通知所有可能受影響的當事人。
    - 照錄：「개인정보처리자는 개인정보가 유출등이 되었음을 알게 되었을 때에는 지체 없이 해당 정보주체에게 다음 각 호의 사항을 알려야 한다.」
    - 照錄：「1. 유출등이 된 개인정보의 항목」
    - 照錄：「지체 없이 유출등의 가능성이 있는 모든 정보주체에게 피해를 최소화하기 위한 정보 등」
    - 照錄：「<신설 2026. 3. 10.>」
    - 來源：개인정보 보호법（법률 제21445호，2026-03-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357（lsiSeq=283839，頁面標示「[시행 2026. 9. 11.] [법률 제21445호, 2026. 3. 10., 일부개정]」），查證日期 2026-10-09（제34조 제1항、제2항，條文標題「개인정보 유출등의 통지ㆍ신고」）
- 事實：개인정보 보호법 第 34 條第 4 項：處理者得知外洩等時，須依總統令向 PIPC 或總統令指定的專門機關申報。專門機關依施行令第 40 條第 3 項為韓國網路振興院（KISA）。
    - 照錄：「개인정보처리자는 개인정보의 유출등이 있음을 알게 되었을 때에는 개인정보의 유형, 유출등의 경로 및 규모 등을 고려하여」
    - 照錄：「으로 정하는 바에 따라 제1항 각 호의 사항을 지체 없이 보호위원회 또는」
    - 照錄：「각각 한국인터넷진흥원을 말한다.」
    - 來源：개인정보 보호법（법률 제21445호，2026-03-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357（lsiSeq=283839，頁面標示「[시행 2026. 9. 11.] [법률 제21445호, 2026. 3. 10., 일부개정]」），查證日期 2026-10-09（제34조 제4항），以及 개인정보 보호법 시행령（대통령령 제36671호，2026-09-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=289537（頁面標示「[시행 2026. 9. 11.] [대통령령 제36671호, 2026. 9. 10., 일부개정]」），查證日期 2026-10-09（제40조 제3항）
- 事實：施行令第 39 條第 1 項（2026-09-10 修正，2026-09-11 施行）：通知當事人的期限為得知外洩後 72 小時內，以書面等方式為之。為阻止擴散而需緊急處置、或天災等不得已事由時，可於事由消除後立即通知。
    - 照錄：「개인정보처리자는 개인정보가 유출등이 되었음을 알게 되었을 때에는 서면등의 방법으로 72시간 이내에」
    - 照錄：「2. 천재지변이나 그 밖에 부득이한 사유로 인하여 72시간 이내에 통지하기 곤란한 경우」
    - 照錄：「<개정 2026. 9. 10.>」
    - 來源：개인정보 보호법 시행령（대통령령 제36671호，2026-09-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=289537（頁面標示「[시행 2026. 9. 11.] [대통령령 제36671호, 2026. 9. 10., 일부개정]」），查證日期 2026-10-09（제39조 제1항）
- 事實：施行令第 40 條第 1 項：下列情形之一的外洩，須於得知後 72 小時內向 PIPC 或 KISA 申報：1,000 人以上當事人的個資外洩、敏感資訊或固有識別資訊外洩、因對個資處理系統等的外部非法存取而外洩（第 3 款不設人數門檻）。若外洩路徑已確認並回收、刪除個資而使侵害可能性顯著降低，可以不申報。
    - 照錄：「개인정보처리자는 다음 각 호의 어느 하나에 해당하는 경우로서 개인정보가 유출등이 되었음을 알게 되었을 때에는 72시간 이내에」
    - 照錄：「1. 1천명 이상의 정보주체에 관한 개인정보가 유출등이 된 경우」
    - 照錄：「2. 민감정보 또는 고유식별정보가 유출등이 된 경우」
    - 照錄：「3. 개인정보처리시스템 또는 개인정보취급자가 개인정보 처리에 이용하는 정보기기에 대한 외부로부터의 불법적인 접근에 의해 개인정보가 유출등이 된 경우」
    - 照錄：「해당 개인정보를 회수ㆍ삭제하는 등의 조치를 통해 정보주체의 권익 침해 가능성이 현저히 낮아진 경우에는 신고하지 않을 수 있다.」
    - 來源：개인정보 보호법 시행령（대통령령 제36671호，2026-09-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=289537（頁面標示「[시행 2026. 9. 11.] [대통령령 제36671호, 2026. 9. 10., 일부개정]」），查證日期 2026-10-09（제40조 제1항，本款 2026-09-10 修正）
- 事實：內容尚未確認時可先通報：施行令規定當事人通知與 PIPC 申報都可先寫「已外洩的事實、至今確認的內容」及其他事項，其餘確認後立即補報。
    - 照錄：「추가로 확인되는 내용에 대해서는 확인되는 즉시 통지해야 한다.」
    - 照錄：「추가로 확인되는 내용에 대해서는 확인되는 즉시 신고해야 한다.」
    - 來源：개인정보 보호법 시행령（대통령령 제36671호，2026-09-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=289537（頁面標示「[시행 2026. 9. 11.] [대통령령 제36671호, 2026. 9. 10., 일부개정]」），查證日期 2026-10-09（제39조 제2항、제40조 제2항）
- 事實：2026-09-11 起新增「外洩可能性通知」：施行令第 39 條之 2 列出兩種情形（對系統或設備的非法存取而疑似外洩但難以特定當事人，個資遭第三人交易而確認部分外洩、其他當事人也可能外洩），須自得知時起 72 小時內通知所有可能受影響的當事人。
    - 照錄：「해당 불법적인 접근을 알게 된 때」
    - 照錄：「해당 사실을 알게 된 때」
    - 照錄：「4. 유출등의 여부가 확정될 경우 추가 통지를 하겠다는 사실」
    - 照錄：「[본조신설 2026. 9. 10.]」
    - 來源：개인정보 보호법 시행령（대통령령 제36671호，2026-09-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=289537（頁面標示「[시행 2026. 9. 11.] [대통령령 제36671호, 2026. 9. 10., 일부개정]」），查證日期 2026-10-09（제39조의2、제39조의3 第 1 項）
- 事實：無法取得當事人聯絡方式等正當事由時，可改在自家網站（無網站者在營業處所明顯處）公告 30 日以上以代替通知。
    - 照錄：「자신의 인터넷 홈페이지에 30일 이상 게시하는 것으로 제1항 및 제2항의 통지를 갈음할 수 있다.」
    - 來源：개인정보 보호법 시행령（대통령령 제36671호，2026-09-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=289537（頁面標示「[시행 2026. 9. 11.] [대통령령 제36671호, 2026. 9. 10., 일부개정]」），查證日期 2026-10-09（제39조 제3항）
- 事實：公布與施行時程：2026-03-10 公布的修正法律於公布後 6 個月（即 2026-09-11）施行，第 34 條第 1 項、第 4 項自施行後得知外洩者起適用，第 2 項自施行後得知外洩可能性者起適用。ISMS-P 認證義務化相關條文（第 32 條之 2 第 1 項但書等）則延到 2027-07-01 施行。
    - 照錄：「이 법은 공포 후 6개월이 경과한 날부터 시행한다.」
    - 照錄：「제34조제1항 및 제4항의 개정규정은 이 법 시행 이후 개인정보가 유출등이 되었음을 알게 된 경우부터 적용한다.」
    - 照錄：「제32조의2제1항 단서 및 제75조제2항제15호의 개정규정은 2027년 7월 1일부터 시행한다.」
    - 來源：개인정보 보호법（법률 제21445호，2026-03-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357（lsiSeq=283839，頁面標示「[시행 2026. 9. 11.] [법률 제21445호, 2026. 3. 10., 일부개정]」），查證日期 2026-10-09（附則 제1조、제2조）
- 事實：PIPC 2026-09-10 新聞稿確認法律與施行令自 9 月 11 日施行，修正重點含：重複或故意、重大過失外洩的懲罰性課徵金（全體營收 10% 以內）、外洩可能性通知制、外洩通知項目擴大，以及竄改、毀損（如勒索軟體）亦納入外洩申報與通知對象。
    - 照錄：「구체화한 개정 ｢개인정보 보호법 시행령｣(이하 ‘시행령’)이 9월 11일부터 시행된다.」
    - 照錄：「징벌적 과징금(전체 매출액 10% 이내)」
    - 照錄：「개인정보 유출 가능성 통지제를 신설하고」
    - 照錄：「개인정보의 위조·변조·훼손(랜섬웨어 등)도 유출신고·통지 대상에 포함하였다.」
    - 照錄：「2027년 7월 1일부터 시행될 예정이다.」
    - 來源：개인정보보호위원회 보도자료「개인정보 유출 사전예방·피해구제 강화를 위한 개인정보 보호법·시행령·고시, 9월 11일부터 시행」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12459，作成日 2026-09-10，查證日期 2026-10-09
- 事實：課徵金（과징금）上限：第 64 條之 2 第 1 項維持全體營收 3% 以內（無營收等情形 20 億韓元以內），個資外洩（第 1 項第 9 款）屬於適用事由，但已盡第 29 條安全措施者除外。
    - 照錄：「전체 매출액의 100분의 3을 초과하지 아니하는 범위에서 과징금을 부과할 수 있다.」
    - 照錄：「9. 개인정보처리자가 처리하는 개인정보가 유출등이 된 경우.」
    - 照錄：「20억원을 초과하지 아니하는 범위에서 과징금을 부과할 수 있다.」
    - 來源：개인정보 보호법（법률 제21445호，2026-03-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357（lsiSeq=283839，頁面標示「[시행 2026. 9. 11.] [법률 제21445호, 2026. 3. 10., 일부개정]」），查證日期 2026-10-09（제64조의2 제1항）
- 事實：新增加重上限：第 64 條之 2 第 2 項（2026-03-10 新設，已於 2026-09-11 施行）規定下列情形課徵金可達全體營收 10% 以內（無營收等情形 50 億韓元以內）：受課徵金處分後 3 年內再違反且各次均有故意或重大過失、故意或重大過失致被害規模 1,000 萬人以上、違反糾正命令致發生第 9 款外洩。附則規定第 1 款適用於施行後發生的違反行為、第 2 款亦適用於施行時尚未終了的違反行為。
    - 照錄：「전체 매출액의 100분의 10을 초과하지 아니하는 범위에서 과징금을 부과할 수 있다.」
    - 照錄：「50억원을 초과하지 아니하는 범위에서 과징금을 부과할 수 있다.」
    - 照錄：「정보주체의 피해 규모가 1천만명 이상인 경우」
    - 照錄：「<신설 2026. 3. 10.>」
    - 照錄：「제64조의2제2항제2호의 개정규정은 이 법 시행 당시 종료되지 아니한 위반행위에 대해서도 적용한다.」
    - 來源：개인정보 보호법（법률 제21445호，2026-03-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357（lsiSeq=283839，頁面標示「[시행 2026. 9. 11.] [법률 제21445호, 2026. 3. 10., 일부개정]」），查證日期 2026-10-09（제64조의2 제2항，附則 제3조）
- 事實：預防投資減輕：第 64 條之 2 第 6 項（2026-03-10 新設）規定，投入預算、人力、設備等總統令所定事由時應減輕課徵金，但故意或重大過失除外。
    - 照錄：「개인정보 보호를 위하여 예산ㆍ인력ㆍ설비ㆍ장치 등을 투자하고 운영하는 등」
    - 照錄：「다만, 개인정보처리자의 고의 또는 중대한 과실로 위반행위를 한 경우는 제외한다.」
    - 來源：개인정보 보호법（법률 제21445호，2026-03-10 일부개정，시행 2026-09-11），국가법령정보센터，https://www.law.go.kr/LSW/lsInfoP.do?lsId=011357（lsiSeq=283839，頁面標示「[시행 2026. 9. 11.] [법률 제21445호, 2026. 3. 10., 일부개정]」），查證日期 2026-10-09（제64조의2 제6항）
- 事實：2026 年 PIPC 已公布的外洩處分（供對照，非 7–9 月事件）：2026-06-11 對 Coupang 課徵金 6,246 億 8,100 萬韓元，認定因簽章金鑰管理與存取控制疏失致約 3,755 萬人個資外洩。2026-07-29 全體會議對 KT 課徵金 539 億 7,900 萬韓元（毫微微蜂窩基地台，16,647 人）。
    - 照錄：「과징금 6,246억 8,100만 원과 과태료 1,680만 원 부과」
    - 照錄：「인증 서명키 관리 및 접근통제 소홀 등 기본적인 안전관리 체계 미흡으로 약 3,755만 명의 개인정보 유출」
    - 照錄：「펨토셀을 통한 개인정보 유출에 대해 안전조치 의무 위반으로 과징금 539억 7,900만 원 부과」
    - 來源：PIPC 보도자료 nttId=12171（作成日 2026-06-11）、nttId=12349（2026-07-30 刊出，全體會議為 7 月 29 日），https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12171 與 …nttId=12349，查證日期 2026-10-09
- 事實：PIPC 2026-10-02 公布外洩申報件數：2022 年 167 件、2023 年 318 件、2025 年 447 件，2026 年僅上半年就受理 432 件。同日提出快速調查方案（重大案件 12 個月、一般案件 6 個月、輕微案件 3 個月內處理為原則），這是方案不是法規。
    - 照錄：「개인정보 유출 신고는 2022년 167건에서 2023년 318건으로 증가한 데이어, 2025년에는 447건까지 증가했으며, 2026년에는 상반기에만 432건이 접수돼 2025년 연간 신고 건수에 육박하고 있다.」
    - 照錄：「※ 중요사건 12개월, 일반사건 6개월, 경미사건 3개월 이내 처리 원칙」
    - 來源：PIPC 보도자료「개인정보 유출·침해사고, 더 빠르게 더 공정하게 더 투명하게 조사」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12555，作成日 2026-10-02，查證日期 2026-10-09
- 事實：【草案】ISMS-P 認證審查改善的施行令修正案於 2026-09-16 至 10-26 預告立法，內容為認證審查，不是外洩通報規定。
    - 照錄：「9월 16일부터 10월 26일까지 입법예고한다고 밝혔다.」
    - 來源：PIPC 보도자료「개인정보 보호 인증(ISMS-P) 심사 개선을 위한 개인정보 보호법 시행령 개정안 입법예고」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12500，作成日 2026-09-16（草案，預告期間至 2026-10-26），查證日期 2026-10-09
- 事實：【國會】個資法修正案（人工智慧開發的個資利用特例）2026-08-20 國會本會議通過，公布後 6 個月施行。內容與外洩通報無關，本次未查到其公布日期或法律編號。
    - 照錄：「개인정보 보호법」 개정안이 8월 20일 국회 본회의를 통과했다고 밝혔다.」
    - 照錄：「공포 후 6개월 뒤부터 시행된다.」
    - 來源：PIPC 보도자료 https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12391，作成日 2026-08-20，查證日期 2026-10-09
- 事實：PIPC 2026-07-08 發布 API 外洩預防呼籲（非處分）：指出權限管理不足的 API 近來接連發生外洩，只驗證登入、不驗證查詢權限，或 API 回應含服務不需要的個資，「비정상적인 API 호출만으로도」即可造成大規模外洩。舉三個匿名案例（A 公司約 3,700 萬人資料、B 公司約 13.5 萬人、C 公司舊版 API 無權限確認），頁面未點名公司。
    - 照錄：「최근 국내외에서 권한 관리가 미흡한 API를 통한 개인정보 유출 사고가 잇따라 발생하고 있다.」
    - 照錄：「비정상적인 API 호출만으로도 대규모 개인정보 유출로 이어질 수 있다.」
    - 照錄：「(A사) 권한 관리가 이루어지지 않은 API에 대한 비정상 접근으로 약 3,700만여명의 이름, 주소, 이메일, 전화번호, 생년월일 등 유출」
    - 照錄：「로그인 여부만 확인하고 개인정보 조회 권한을 확인하지 않거나」
    - 來源：PIPC 보도자료「개인정보위, 응용프로그램 인터페이스(API) 활용 확대에 따른 개인정보 유출 예방 당부」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12241，作成日 2026-07-08，查證日期 2026-10-09
- 事實：PIPC 2026-07-08 第 13 次全體會議對 3 家業者處分，合計課徵金 7 億 100 萬韓元、罰款 540 萬韓元。其中兩家是網站管理員頁面未做 IP 限制等（2024 年事件），一家為郵件伺服器漏洞（2024 年事件），事件發生時間均不在 2026 年 7–9 月。
    - 照錄：「총 7억 100만 원의 과징금 및 540만 원의 과태료를 부과하고」
    - 照錄：「해커는 2024년 4월 ㈜유베이스가 운영하는 대표 홈페이지 관리자 계정으로 접속하여」
    - 照錄：「해커는 2024년 8월 썬포토㈜가 운영하는 웹사이트의 관리자 계정으로 접속하여 회원 약 17만 명의 개인정보」
    - 照錄：「웹사이트 관리자 페이지에 대한 접속 권한을 인터넷 프로토콜(IP) 주소 등으로 제한하지 않았고」
    - 來源：PIPC 보도자료「개인정보위, 안전조치 의무 위반 3개 사업자 제재」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12242，作成日 2026-07-08，查證日期 2026-10-09
- 事實：PIPC 2026-08-26 第 17 次全體會議（新聞稿 08-31）對 GS Retail 課徵金 128 億 3,600 萬韓元、罰款 300 萬韓元：以撞庫攻擊（credential stuffing）登入 GS SHOP 網站（2024-06-21 至 2025-02-13）與 GS25 網站，經會員資訊修改頁外洩，GS SHOP 1,581,025 人、GS25 79,128 人。事件期間為 2024–2025 年，處分在 2026 年 8 月。
    - 照錄：「과징금 128억 3,600만 원, 과태료 300만 원 부과」
    - 照錄：「GS SHOP에서 1,581,025명, GS25에서 79,128명의 개인정보」
    - 照錄：「크리덴셜 스터핑」
    - 來源：PIPC 보도자료「개인정보위, ㈜지에스리테일 유출사고에 대해 과징금 128억 3,600만 원, 과태료 300만 원 부과」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12425，作成日 2026-08-31，查證日期 2026-10-09
- 事實：PIPC 2026-10-06 的新聞參考資料提到「最近一部分金融業個資外洩」，提醒防範詐騙。頁面寫明密碼與 OTP 資訊未外洩，頁面未描述外洩手法是否與網站或 API 有關。
    - 照錄：「최근 일부 금융권 개인정보 유출로 인한 피싱·스미싱 등 2차 피해 우려 확산」
    - 照錄：「비밀번호·OTP 정보 등은 유출되지 않았으나」
    - 來源：PIPC 보도참고자료「최근 금융권 개인정보 유출사고에 따른 보이스피싱·스미싱 등 피해에 주의하세요.」，https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12560，作成日 2026-10-06，查證日期 2026-10-09

## 中國

- 事實：《個人信息保護法》第 57 條規定，個人信息處理者（適用於所有處理個人信息的組織與個人，不分公私）發生或可能發生個人信息洩露、篡改、丟失時，須立即採取補救措施，並通知履行個人信息保護職責的部門和個人。條文只寫「立即」，沒有寫天數，也沒有設報告門檻（可能發生也算）
    - 照錄：「发生或者可能发生个人信息泄露、篡改、丢失的，个人信息处理者应当立即采取补救措施，并通知履行个人信息保护职责的部门和个人。」（第 57 條第 1 款）
    - 來源（一手）：中华人民共和国个人信息保护法（2021 年 8 月 20 日第十三届全国人民代表大会常务委员会第三十次会议通过，2021 年 11 月 1 日起施行），中国人大网，<http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html>，同文亦見國家網信辦 <https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm>，查證日期 2026-10-09（頁面未見修正註記，未另查有無後續修法）
- 事實：同條規定通知內容須包含三項：洩露等事件的資訊種類、原因與可能危害。處理者採取的補救措施與個人可採取的減輕危害措施。處理者的聯絡方式
    - 照錄：「（一）发生或者可能发生个人信息泄露、篡改、丢失的信息种类、原因和可能造成的危害；」（第 57 條第 1 款第 1 項） <!-- docs-style-lint: disable-line -->
    - 照錄：「（二）个人信息处理者采取的补救措施和个人可以采取的减轻危害的措施；」（第 57 條第 1 款第 2 項） <!-- docs-style-lint: disable-line -->
    - 照錄：「（三）个人信息处理者的联系方式。」（第 57 條第 1 款第 3 項）
    - 來源：同上，查證日期 2026-10-09
- 事實：採取措施能有效避免危害時，處理者可以不通知個人（但仍須通知主管部門，條文文字只免除通知個人）。主管部門認為可能造成危害時，有權要求處理者通知個人
    - 照錄：「个人信息处理者采取措施能够有效避免信息泄露、篡改、丢失造成危害的，个人信息处理者可以不通知个人；履行个人信息保护职责的部门认为可能造成危害的，有权要求个人信息处理者通知个人。」（第 57 條第 2 款） <!-- docs-style-lint: disable-line -->
    - 來源：同上，查證日期 2026-10-09（「仍須通知主管部門」是依條文文字對照的本筆記判斷）
- 事實：個人信息保護法的本文沒有規定通知個人或通報主管部門的天數，也沒有訂定比第 57 條更細的通報範圍（本筆記查了該法全文的第 51 條與第 57 條，第 51 條只要求處理者制定並實施個人信息安全事件應急預案）。天數規定見下一條的國家網信辦辦法，但那份辦法的對象是「網絡安全事件」，不是個人信息洩露本身 <!-- docs-style-lint: disable-line -->
    - 照錄：「制定并组织实施个人信息安全事件应急预案；」（第 51 條第 5 項） <!-- docs-style-lint: disable-line -->
    - 來源：同上，查證日期 2026-10-09。尚未查證國家標準、行業規定中有無個人信息洩露專屬的時限，查不到的部分以「查不到」處理，不推測
- 事實：違反個人信息保護法規定、未履行保護義務的處罰見第 66 條：責令改正、警告、沒收違法所得，拒不改正處 100 萬元以下罰款。情節嚴重處 5000 萬元以下或上一年度營業額 5% 以下罰款，並可責令暫停業務或停業整頓。第 66 條是概括條款，沒有點名第 57 條
    - 照錄：「拒不改正的，并处一百万元以下罚款」（第 66 條第 1 款，截自該款）
    - 照錄：「并处五千万元以下或者上一年度营业额百分之五以下罚款」（第 66 條第 2 款，截自該款）
    - 來源：同上，查證日期 2026-10-09
- 事實：《國家網絡安全事件報告管理辦法》由國家互聯網信息辦公室於 2025-09-11 發布，自 2025-11-01 起施行，適用於在中國境內建設、運營網絡或通過網絡提供服務的網絡運營者。辦法的依據條文列出《個人信息保護法》等四部法規 <!-- docs-style-lint: disable-line -->
    - 照錄：「（2025年9月11日 国家互联网信息办公室）」（辦法標題下的發布日期）
    - 照錄：「本办法自2025年11月1日起施行。」（第 14 條）
    - 照錄：「在中华人民共和国境内建设、运营网络或者通过网络提供服务的网络运营者，在发生网络安全事件时，应当按照本办法的规定进行报告。」（第 2 條）
    - 來源（一手）：国家网络安全事件报告管理办法，中国网信网（國家網信辦），發布頁面日期 2025-09-15，<https://www.cac.gov.cn/2025-09/15/c_1759583017717009.htm>，查證日期 2026-10-09（辦法正文與附件《網絡安全事件分級指南》在同一頁） <!-- docs-style-lint: disable-line -->
- 事實：辦法依《網絡安全事件分級指南》研判，屬「較大以上」事件才須報告。一般網絡運營者最遲 4 小時內向屬地省級網信部門報告。涉及關鍵信息基礎設施的最遲 1 小時內向保護工作部門、公安機關報告。中央和國家機關各部門及其直屬單位最遲 2 小時內向本部門網信工作機構報告。重大、特別重大事件的上級通報時限另有 1 小時或半小時的規定 <!-- docs-style-lint: disable-line -->
    - 照錄：「网络运营者在发现或获知涉及本单位的网络安全事件时，应当按照《网络安全事件分级指南》（见附件）进行研判，属于较大以上网络安全事件的，按以下程序报告：」（第 4 條前段）
    - 照錄：「涉及关键信息基础设施的，网络运营者应当第一时间向保护工作部门、公安机关报告，最迟不得超过1小时。」（第 4 條第 1 項）
    - 照錄：「其他网络运营者应当及时向属地省级网信部门报告，最迟不得超过4小时。」（第 4 條）
    - 照錄：「属于重大、特别重大网络安全事件的，省级网信部门在收到报告后，应当第一时间向国家网信部门报告，最迟不得超过1小时，并同时向同级有关部门通报。」（第 4 條）
    - 照錄：「网络运营者属于中央和国家机关各部门及其直属单位的，应当及时向本部门网信工作机构报告，最迟不得超过2小时。」（第 4 條）
    - 來源：同上，查證日期 2026-10-09
- 事實：附件的分級指南中，與個人信息數量有關的「通常情況下」判別門檻有三級：洩露 100 萬人以上公民個人信息為「較大」事件（需報告，一般運營者 4 小時）。1000 萬人以上為「重大」事件。1 億人以上為「特別重大」事件。「以上」包含本數。不足 100 萬人時，是否仍屬較大以上，要看指南其他「較大量公民個人信息丟失或被竊取」等概括條款，指南未給數字，本筆記查不到更低的量化標準，所以 100 萬人以下的外洩依這份辦法沒有確定的報告時限
    - 照錄：「泄露100万人以上公民个人信息。」（附件三「較大網絡安全事件」第 5 項） <!-- docs-style-lint: disable-line -->
    - 照錄：「泄露1000万人以上公民个人信息。」（附件二「重大網絡安全事件」第 5 項） <!-- docs-style-lint: disable-line -->
    - 照錄：「泄露1亿人以上公民个人信息。」（附件一「特別重大網絡安全事件」第 5 項） <!-- docs-style-lint: disable-line -->
    - 照錄：「重要数据、较大量公民个人信息丢失或被窃取、篡改、假冒，对国家安全和社会稳定构成较严重威胁。」（附件三第 2 項，概括條款）
    - 照錄：「注：本指南中的“以上”均包括本数。」（附件末）
    - 來源：同上，查證日期 2026-10-09（「100 萬人以下沒有確定時限」是本筆記對條文的判斷）
- 事實：報告內容、補報與總結：報告至少要有涉事單位與系統概況、事件發現時間、類型、級別、已造成的影響與已採取的措施。規定時間內無法判定原因、影響的，可先報告前兩項，其餘補報。處置結束後 30 日內須提交處置總結報告。涉嫌違法犯罪的，須及時向公安機關報案
    - 照錄：「对于规定时间内不能判定事发原因、影响或发展趋势等网络安全事件情况的，可先报告第一项、第二项内容，其他情况及时补报。」（第 7 條第 2 款）
    - 照錄：「网络安全事件处置工作结束后，网络运营者应当于30日内对相关事件发生原因、应急处置措施、造成的危害、责任追究、完善整改情况、教训等进行全面分析总结，形成事件处置总结报告按照原渠道上报。」（第 8 條）
    - 照錄：「涉嫌违法犯罪的，网络运营者应当及时向公安机关报案。」（第 4 條）
    - 來源：同上，查證日期 2026-10-09
- 事實：違反辦法的處罰：沒有在辦法內另訂罰則，由主管部門依有關法律、行政法規處罰。遲報、漏報、謊報或瞞報造成重大危害後果的從重處罰。已採取合理必要的防護措施、依應急預案處置並及時報告的，可視情從輕或不予追究
    - 照錄：「网络运营者未按照本办法规定报告网络安全事件的，有关主管部门按照有关法律、行政法规的规定进行处罚。」（第 10 條第 1 款）
    - 照錄：「可视情从轻或不予追究相关单位和人员责任。」（第 11 條，截自該條）
    - 來源：同上，查證日期 2026-10-09
- 事實：國家網信辦的「專家解讀」文章（二手解說，不是條文）說明辦法依事件級別規定不同的報告時限、對重大與特別重大事件規定更嚴格的逐級上報。解讀文章沒有逐條補充個人信息洩露的細節，本筆記只取其對辦法目的的說明
    - 照錄：「对不同等级的事件规定了相应的报告时限」（專家解讀，截自該句）
    - 來源（二手，官方解讀）：专家解读｜规范网络安全事件报告筑牢数字空间安全防线，中国网信网，發布頁面日期 2025-09-15，<https://www.cac.gov.cn/2025-09/15/c_1759583022641161.htm>，查證日期 2026-10-09
- 事實：《網絡數據安全管理條例》（國務院令第 790 號，2024-09-24 公布，2025-01-01 起施行）第 11 條規定，網絡數據處理者發生網絡數據安全事件時，須立即啟動應急預案、防止危害擴大、按規定向有關主管部門報告。事件對個人、組織合法權益造成危害時，須及時通知利害關係人，通知內容與方式有列舉。條文沒有天數，向哪個主管部門報告「按照規定」，轉到行業與其他規定。第 11 條涵蓋「網絡數據」安全事件，個人信息洩露是其中一類 <!-- docs-style-lint: disable-line -->
    - 照錄：「网络数据处理者应当建立健全网络数据安全事件应急预案，发生网络数据安全事件时，应当立即启动预案，采取措施防止危害扩大，消除安全隐患，并按照规定向有关主管部门报告。」（第 11 條第 1 款）
    - 照錄：「网络数据安全事件对个人、组织合法权益造成危害的，网络数据处理者应当及时将安全事件和风险情况、危害后果、已经采取的补救措施等，以电话、短信、即时通信工具、电子邮件或者公告等方式通知利害关系人；法律、行政法规规定可以不通知的，从其规定。」（第 11 條第 2 款） <!-- docs-style-lint: disable-line -->
    - 照錄：「《网络数据安全管理条例》已经2024年8月30日国务院第40次常务会议通过，现予公布，自2025年1月1日起施行。」（國務院令）
    - 來源（一手）：网络数据安全管理条例（国务院令第 790 号），中国政府网，頁面日期 2024-09-30，<https://www.gov.cn/zhengce/content/202409/content_6977766.htm>，同文亦見國家網信辦 <https://www.cac.gov.cn/2024-09/30/c_1729384452307680.htm>，查證日期 2026-10-09
- 事實：同條例第 11 條對「通知利害關係人」另開例外，只能依法律、行政法規。與個人信息保護法第 57 條第 2 款可不通知個人的規定合併適用，所以個人信息洩露的通知個人義務，實務上有兩處條文依據（一是個人信息保護法，一是此條例）。條例第 11 條的違反沒有點名罰則：第 57 條罰則只列第 29 條第 2 款、第 30 條第 2、3 款、第 31 條、第 32 條，不含第 11 條，須回到上位法判斷
    - 照錄：「违反本条例第二十九条第二款、第三十条第二款和第三款、第三十一条、第三十二条规定的，由网信、电信、公安等主管部门依据各自职责责令改正，给予警告，可以并处5万元以上50万元以下罚款」（條例第 57 條，截自該條）
    - 來源：同上，查證日期 2026-10-09（「兩處條文依據」與「須回到上位法」是本筆記依條文文字對照的判斷）
- 事實：條例第 28 條規定處理 1000 萬人以上個人信息的網絡數據處理者，須比照重要數據處理者遵守第 30 條、第 32 條（與重要數據處理者的義務相同，細節不在本筆記範圍）。這個 1000 萬人門檻與事件分級指南的「重大」門檻（洩露 1000 萬人以上）數字相同，但屬於不同規定 <!-- docs-style-lint: disable-line -->
    - 照錄：「网络数据处理者处理1000万人以上个人信息的，还应当遵守本条例第三十条、第三十二条对处理重要数据的网络数据处理者（以下简称重要数据的处理者）作出的规定。」（第 28 條）
    - 來源：同上，查證日期 2026-10-09
- 事實：條例第 11 條的前一條（第 10 條）另規定網絡產品與服務的安全缺陷、漏洞：發現後立即補救、按規定告知用戶並向主管部門報告。涉及危害國家安全、公共利益的，須在 24 小時內向主管部門報告。這是漏洞風險的報告時限，不是個人信息洩露事件的時限 <!-- docs-style-lint: disable-line -->
    - 照錄：「涉及危害国家安全、公共利益的，网络数据处理者还应当在24小时内向有关主管部门报告。」（第 10 條）
    - 來源：同上，查證日期 2026-10-09（第 10 條條號是本筆記依頁面順序確認，條文位於第 11 條之前）
- 事實：《數據安全法》第 29 條規定開展數據處理活動時發現數據安全缺陷、漏洞等風險，須立即補救。發生數據安全事件時，須立即採取處置措施，按規定及時告知用戶並向有關主管部門報告。條文沒有天數，也沒有區分個人信息與其他數據
    - 照錄：「开展数据处理活动应当加强风险监测，发现数据安全缺陷、漏洞等风险时，应当立即采取补救措施；发生数据安全事件时，应当立即采取处置措施，按照规定及时告知用户并向有关主管部门报告。」（第 29 條） <!-- docs-style-lint: disable-line -->
    - 來源（一手）：中华人民共和国数据安全法（2021 年 6 月 10 日第十三届全国人民代表大会常务委员会第二十九次会议通过，2021 年 9 月 1 日起施行），中国人大网，<http://www.npc.gov.cn/npc/c2/c30834/202106/t20210610_311888.html>，查證日期 2026-10-09
    - 照錄：「本法自2021年9月1日起施行。」（附則）
- 事實：不履行數據安全法第 29 條等義務的罰則見第 45 條：責令改正、警告，可並處 5 萬元以上 50 萬元以下罰款。拒不改正或造成大量數據洩露等嚴重後果的，處 50 萬元以上 200 萬元以下罰款，並可責令暫停業務、停業整頓、吊銷許可證或營業執照
    - 照錄：「开展数据处理活动的组织、个人不履行本法第二十七条、第二十九条、第三十条规定的数据安全保护义务的，由有关主管部门责令改正，给予警告，可以并处五万元以上五十万元以下罚款」（第 45 條，截自該條）
    - 照錄：「拒不改正或者造成大量数据泄露等严重后果的，处五十万元以上二百万元以下罚款」（第 45 條，截自該條）
    - 來源：同上，查證日期 2026-10-09
