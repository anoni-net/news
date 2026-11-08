---
title: 美國第九巡迴法院審理的基地台傾印搜索票
description: 美國第九巡迴法院審理一件基地台傾印（向電信業者調取某時某地所有手機資料）的上訴案，EFF 與 ACLU 主張傾印搜索票本身違憲。到 11 月 8 日查不到政府一方在上訴審的書狀，依本文推論關閉 Google 定位紀錄擋不了基地台傾印。
date: 2026-11-13T00:05:00+08:00
slug: ninth-circuit-reverse-location
categories:
  - surveillance
regions:
  - US
sources:
  - title: We’re Asking the Ninth Circuit to Hold Reverse Location Warrants Categorically Unconstitutional
    url: https://www.eff.org/deeplinks/2026/11/were-asking-ninth-circuit-hold-reverse-location-warrants-categorically
    publisher: EFF
    date: 2026-11-04
  - title: Brief of Amici Curiae, No. 26-689 (9th Cir.)
    url: https://www.eff.org/files/2026/11/03/united_states_v._spurlock_-_eff_aclu_amicus_brief_1.pdf
    publisher: EFF
    date: 2026-11-03
  - title: Uncle Sam seeks time in tower dump data grab case after judge calls it 'unconstitutional'
    url: https://theregister.com/2025/06/19/us_tower_grab_appeal/
    publisher: The Register
    date: 2025-06-19
  - title: Court rules that law enforcement’s use of “geofence warrant” was a “search”
    url: https://www.scotusblog.com/2026/06/court-rules-that-law-enforcements-use-of-geofence-warrant-was-a-search/
    publisher: SCOTUSblog
    date: 2026-06-29
  - title: Supreme Court Holds Geofence Warrants Are Fourth Amendment Searches, But Leaves Other Important Questions for Lower Courts
    url: https://www.zwillgen.com/law-enforcement/supreme-court-holds-geofence-warrants-are-fourth-amendment-searches-leaves-other-important-questions-lower-courts/
    publisher: ZwillGen
    date: 2026-07-02
  - title: Federal Appeals Court Finds Geofence Warrants Are “Categorically” Unconstitutional
    url: https://www.eff.org/deeplinks/2024/08/federal-appeals-court-finds-geofence-warrants-are-categorically-unconstitutional
    publisher: EFF
    date: 2024-08-12
  - title: Supreme Court grapples with limits to 'geofence warrants' over privacy concerns
    url: https://www.goodmorningamerica.com/amp/news/story/supreme-court-weighs-geofence-warrants-cellphone-data-132358022
    publisher: ABC News
    date: 2026-04-28
  - title: No. 25-112 (U.S. June 29, 2026)
    url: https://www.independent.org/article/2026/06/30/supreme-court-geofence-warrants-chatrie/
    publisher: Independent Institute
    date: 2026-06-30
  - title: Updates to Location History and new controls coming soon to Maps
    url: https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/
    publisher: Google
    date: 2023-12-12
  - title: Manage your Google Maps Timeline
    url: https://support.google.com/maps/answer/6258979?hl=en
    publisher: Google Maps Help
  - title: "Apple Transparency Report: Government and Private Party Requests, July 1 - December 31, 2025"
    url: https://www.apple.com/legal/transparency/pdf/requests-2025-h2-en.pdf
    publisher: Apple
  - title: 通訊保障及監察法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060044
    publisher: 全國法規資料庫
authors:
  - anoni-net
watch:
  - date: 2026-12-01
    note: 第九巡迴法院 No. 26-689 的政府答辯書狀是否提出、內容如何主張，以及口頭辯論是否排定
---

美國第九巡迴上訴法院正在審理一件基地台傾印（tower dump）搜索票的上訴案。傾印搜索票要求行動通訊業者交出某時某地所有手機的位置資料，範圍內跟案件無關的裝置也包含在內。數位權利組織 EFF 與美國公民自由聯盟（ACLU）在 11 月 3 日以法庭之友（amicus，非當事人向法院提出意見）的身分提交書狀，主張傾印搜索票本身違憲。案件只涉及美國的執法，其他地方的讀者不受直接影響。

EFF 的文章把基地台傾印與 geofence（地理圍欄）搜索票都歸為反向位置搜索（reverse location searches），兩者都先劃出時間與地點，再從資料裡找人。基地台傾印向行動通訊業者調取，geofence 向 Google 這類公司調取裝置的位置紀錄，資料來源不同。美國最高法院 6 月 29 日判決的是 geofence，第九巡迴法院的上訴案（案號 `26-689`）是基地台傾印。

依 EFF 的文章，兩名被害人的遺體在加州一條偏遠公路旁被發現，警方在同一條公路數英里外找到其中一人的車。警方隨後聲請涵蓋該路段的基地台傾印搜索票，最後取得近 1,700 支不重複手機的位置資料。

依 The Register 引述的裁定，內華達聯邦地方法院 2025 年認定基地台傾印屬於美國憲法第四修正案（禁止不合理的搜索與扣押）所稱的搜索，本案的搜索票是第四修正案禁止的概括搜索票（general warrant，不限定對象的搜索令狀）。裁定同時沒有排除任何證據，理由是該院看來是第九巡迴法院轄區內第一個這樣認定的法院，而且善意例外（good faith exception，執法人員相信自己依搜索票合法行事時，證據原則上仍可使用）適用。被告其後向第九巡迴法院上訴。

依 EFF 的文章，書狀有三項主張。最高法院的 geofence 判決加強了基地台傾印屬於違憲概括搜索票的論點，沒有相當理由（probable cause，核發搜索票要求的具體依據）認為範圍內所有人都涉案，就不能搜索所有人。即使法院仍允許傾印搜索票，也要限制範圍與期限、通知受影響的人，並在事後刪除無關的資料。書狀也要求法院放下善意例外，實際判斷憲法問題。

最高法院的 geofence 判決以 6 比 3 認定，警方調取手機位置紀錄屬於搜索，即使時間很短、資料在第三方公司手上也一樣。依法律事務所 ZwillGen 的分析，搜索票是否具體、有沒有相當理由，發回先前審理的第四巡迴法院判斷。反向搜索票是否合憲仍未解決。EFF 的文章把第九巡迴法院的上訴案寫成判決之後第一件進入聯邦上訴法院的同類案件。

## 導讀觀點 {#perspective}

手機開機且未開飛航模式時會連上基地台，這是行動網路的基本運作方式（本文補充的背景，下面的來源沒有直接寫這一句）。SCOTUSblog 整理最高法院 2018 年的基地台案時，把基地台位置資訊描述成手機連上基地台時產生的歷史紀錄。The Register 提到傾印可以涵蓋十分鐘到一小時內連上該基地台的所有連線。

Google 帳號的定位紀錄（Location History，Google Maps 時間軸背後的設定）是另一份資料，存放在裝置上或 Google 的伺服器，本文據此推論關閉它擋不了基地台傾印。查到的來源沒有寫出使用者這一端能避開基地台紀錄的做法，哪些連線會留下可調取的紀錄、業者保存多久也沒有寫。

到 11 月 8 日，本文查不到政府一方在第九巡迴法院上訴案提出的書狀，也查不到相關報導。依聯邦上訴程序的通則，答辯期限通常在上訴人書狀後 30 天，查不到可能只是期限未到（本文推算，未查到案卷）。下一段政府一方的論點都出自別的案件（最高法院的 geofence 案與同案的第四巡迴法院判決），當時的資料來自 Google，跟電信業者無關。

依 ABC News 的報導，政府在最高法院的 geofence 案主張，使用者把位置資訊分享給 App 與 Google 這類服務業者就放棄了隱私期待。第四巡迴法院的多數意見也認為當事人自願讓 Google 持有的兩小時位置資料不能合理期待保密（依 SCOTUSblog）。最高法院的多數意見認定資料由第三方公司持有時當事人仍有隱私期待，2018 年的基地台案判決也已認定取得基地台位置資訊屬於搜索、不適用第三方原則（third-party doctrine，交給第三方的紀錄不受第四修正案保護的見解，依 SCOTUSblog 與 Independent Institute 的整理）。這些來源沒有說明 2018 年的判決是否及於傾印，政府一方會如何主張、法院是否接受，要看上訴案的後續。

EFF 的文章主張反向位置搜索票本身違憲，並舉法律禁止警方搜索犯罪現場附近上百戶住家為例。依 The Register 的報導，密西西比一位聯邦治安法官 2025 年 2 月以缺乏對特定個人的相當理由駁回 FBI 的四張基地台傾印搜索票，政府 2025 年 6 月申請延長決定是否上訴的期限（到 11 月 8 日查不到結果）。ABC News 的報導則寫 geofence 搜索票對調查人員尋找嫌疑人、失蹤兒童與山區迷路者的價值越來越高，也寫專家認為限制可能妨礙執法。最高法院審理 geofence 案的口頭辯論時，一位大法官提出的方向是訂出合理的時間與地理範圍，再交給核發搜索票的法官落實。

地方法院認定搜索票違憲卻不排除證據，依據是善意例外。EFF 的文章主張，法院常迴避新型監控技術的憲法問題，警方可以繼續使用多年甚至數十年卻沒有明確的判決。依 EFF 2024 年的文章，第五巡迴法院在另一件 geofence 案適用善意例外的理由是 2018 年的技術還新穎，警方也向有經驗的機關求教。最高法院的不同意見同樣以善意例外為由，主張第四巡迴法院既已認定善意例外適用，判決對當事人就沒有實際影響。

台灣的《通訊保障及監察法》（全國法規資料庫 2024 年 7 月修正的版本）把位置資訊列入通信紀錄，檢察官調取原則上要向法院聲請調取票，最輕本刑十年以上之罪與條文列舉的罪名（例如詐欺、強盜）可由檢察官依職權或司法警察官經檢察官許可調取。條文沒有寫明某基地台某時段全部連線的傾印是否適用（本文比對法條的觀察，到 11 月 8 日也沒有查到官方說明）。美國上訴案的爭點落在相當理由與搜索範圍是否特定，台灣條文的門檻是必要性及關連性，部分罪名不必經法院（同為本文比對）。

想確認 Google 這一端資料的人，可以到 Android 或 iPhone 版 Google Maps App 的 Your Timeline 設定，查看定位紀錄對應的時間軸（Timeline）是否開啟。依 Google 2023 年的公告與 11 月 8 日查閱的說明頁，時間軸預設關閉、要自行同意才會開啟，資料存在裝置上。使用者另外選擇備份時，Google 伺服器上會有一份加密副本。Apple 2025 年下半年的透明報告寫明沒有資料可回應 geofence 要求。

依最高法院的不同意見與 Independent Institute 的分析，Google 修改定位紀錄服務後已無法再回應 geofence 搜索票。Independent Institute 的分析寫明改變發生在 2025 年 7 月，到 11 月 8 日沒有找到 Google 自己的說明。上面的設定與報告都只涉及 Google、Apple 手上的資料。

看上訴案的後續，第九巡迴法院會實際判斷憲法問題，還是再次停在善意例外。如果允許傾印搜索票，範圍、期限、通知與刪除的限制能否保護無關的路人，又不讓缺少嫌疑人線索的案件失去調查方法。政府一方的書狀會沿用使用者自願交出資料的論點，還是另外說明基地台紀錄跟 Google 資料的差別。
