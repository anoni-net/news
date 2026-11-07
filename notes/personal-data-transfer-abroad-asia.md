# 個資傳到國外的限制與監督機關的獨立性

範圍是業者把個人資料提供給國外的第三者時，法律上要符合哪些條件，以及監督個資的機關在法律上是否獨立行使職權，另外記錄歐洲理事會《個人資料自動化處理之個人保護公約》（Convention 108）官方頁面把亞洲各地列在哪一類。第一次整理是寫 anoni-net/news 導讀歷史 11/08（議定書 ETS 181 開放簽署）的時候，查證日期 2026-11-07。台灣與中國的條文見 zh-TW 與 zh-CN 稿的 `sources`，這份先收日本與 Convention 108 的部分。

## 日本

- 事實：個人情報保護法第 28 條規定，個人資料處理事業者把個人資料提供給國外的第三者時，除了第 27 條第 1 項各款的例外，須事先取得本人同意。個人情報保護委員會以規則指定為保護水準與日本相當的國家，以及具備符合委員會規則所定基準體制的接收者，不在此限
    - 照錄：「個人情報取扱事業者は、外国（本邦の域外にある国又は地域をいう。以下この条及び第三十一条第一項第二号において同じ。）（個人の権利利益を保護する上で我が国と同等の水準にあると認められる個人情報の保護に関する制度を有している外国として個人情報保護委員会規則で定めるものを除く。…）にある第三者（…個人情報保護委員会規則で定める基準に適合する体制を整備している者を除く。…）に個人データを提供する場合には、前条第一項各号に掲げる場合を除くほか、あらかじめ外国にある第三者への提供を認める旨の本人の同意を得なければならない。」（第 28 條第 1 項）
    - 來源：個人情報の保護に関する法律（平成十五年法律第五十七号），e-Gov 法令檢索（API v1 取得的現行條文），<https://laws.e-gov.go.jp/law/415AC0000000057>，查證日期 2026-11-07
- 事實：同條第 2 項規定，事業者依第 1 項取得本人同意前，須依委員會規則先向本人提供該外國的個資保護制度、該第三者採取的保護措施及其他可供本人參考的資訊
    - 照錄：「個人情報取扱事業者は、前項の規定により本人の同意を得ようとする場合には、個人情報保護委員会規則で定めるところにより、あらかじめ、当該外国における個人情報の保護に関する制度、当該第三者が講ずる個人情報の保護のための措置その他当該本人に参考となるべき情報を当該本人に提供しなければならない。」（第 28 條第 2 項） <!-- docs-style-lint: disable-line -->
    - 來源同上，查證日期 2026-11-07
- 事實：同條第 3 項規定，事業者把個人資料提供給具備上述體制的國外第三者後，須依委員會規則採取必要的措施，確保該第三者持續實施相當措施，並應本人要求提供這些措施的資訊
    - 照錄：「個人情報取扱事業者は、個人データを外国にある第三者（第一項に規定する体制を整備している者に限る。）に提供した場合には、個人情報保護委員会規則で定めるところにより、当該第三者による相当措置の継続的な実施を確保するために必要な措置を講ずるとともに、本人の求めに応じて当該必要な措置に関する情報を当該本人に提供しなければならない。」（第 28 條第 3 項） <!-- docs-style-lint: disable-line -->
    - 來源同上，查證日期 2026-11-07
- 事實：同法第 133 條規定，個人情報保護委員會的委員長與委員獨立行使職權
    - 照錄：「委員会の委員長及び委員は、独立してその職権を行う。」（第 133 條，條文標題「職権行使の独立性」）
    - 來源同上，查證日期 2026-11-07
- 2026 年修法已公布但尚未施行，見 `data-breach-notification.md` 日本一節（查證日期 2026-10-09）。這次沒有查修法是否改動第 28 條與第 133 條

## Convention 108 的締約方與觀察員

- 事實：歐洲理事會的「National information」頁把日本列在「observers to Convention 108」，南韓（Republic of Korea）與泰國列在「non parties to Convention 108」，香港與台灣列在「other territories」。「parties」一類沒有日本、南韓、泰國、香港、台灣
    - 來源：National information，Council of Europe，<https://www.coe.int/en/web/data-protection/national-information>，經 Archive 取得，快照日期不確定，頁面本身沒有日期，查證日期 2026-11-07
    - 注意：副本把分類標題與國名攤平成文字，各國的歸屬建議再看原頁
- 事實（矛盾）：2018 年的 T-PD 文件「Observers: state of play and admission criteria」把日本、南韓與菲律賓的國家隱私委員會（National Privacy Commission）列為觀察員，跟上一條把南韓列在「non parties」不一致
    - 來源：<https://rm.coe.int/observers-state-of-play-and-admission-criteria/16808fdc4d>，查證日期 2026-11-07
    - 查不到：南韓與菲律賓 2026 年的觀察員現況原文
- 事實：議定書 ETS 181 只開放給已加入公約的國家，簽署方也要先批准或同時批准公約
    - 照錄：「After the entry into force of this Protocol, any State which has acceded to the Convention may also accede to the Protocol.」（Art. 3(4)(a)）
    - 照錄：「A Signatory to this Protocol may not ratify, accept or approve it unless it has previously or simultaneously ratified, accepted or approved the Convention or has acceded to it.」（Art. 3(2)）
    - 來源：Additional Protocol to the Convention for the Protection of Individuals with regard to Automatic Processing of Personal Data regarding supervisory authorities and transborder data flows，Council of Europe，<https://rm.coe.int/1680080626>，文本日期 2001-11-08，查證日期 2026-11-07

## 查不到

- 香港個人資料私隱專員公署、南韓個人情報保護委員會的官方頁面這次抓回空頁，沒有再試。新加坡沒有查
