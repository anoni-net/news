---
title: Telegram 交給美國執法單位的使用者資料
description: 美國聯邦法院新歸檔的文件裡，有一封 Telegram 依法院命令提供使用者電話號碼、使用者 ID 與 IP 位址的信。Telegram 的隱私政策 2024 年 9 月起，把可以提供 IP 位址與電話號碼的範圍從恐怖活動嫌疑人擴大到違反服務條款的犯罪案件，條文沒有限定適用地區。到 10 月 20 日為止，沒有看到 Telegram 對這批文件的公開回應。
date: 2026-10-22T00:05:00+08:00
slug: telegram-data-us-court
categories:
  - encryption
sources:
  - title: Telegram Privacy Policy
    url: https://telegram.org/privacy
    publisher: Telegram
  - title: Telegram FAQ
    url: https://telegram.org/faq
    publisher: Telegram
  - title: Telegram Privacy Policy
    url: https://web.archive.org/web/20240901002603/https://telegram.org/privacy
    publisher: Internet Archive
  - title: Scheduled Messages, Reminders, Custom Cloud Themes and More Privacy
    url: https://telegram.org/blog/scheduled-reminders-themes
    publisher: Telegram
    date: 2019-09-05
  - title: Here’s What Telegram Giving Data to the U.S. Government Looks Like
    url: https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/
    publisher: 404 Media
    date: 2026-10-16
  - title: Court filing reveals the user data Telegram is handing over to US authorities
    url: https://cyberinsider.com/telegram-sharing-user-data-with-us-authorities/
    publisher: CyberInsider
    date: 2026-10-17
  - title: Telegram Hands U.S. Authorities Data on Thousands of Users
    url: https://www.404media.co/telegram-hands-u-s-authorities-data-on-thousands-of-users/
    publisher: 404 Media
    date: 2025-01-06
  - title: Crowdsourcing Telegram ‘transparency reports’ to map the network’s claimed compliance with governments around the world
    url: https://meduza.io/en/feature/2024/10/23/crowdsourcing-telegram-transparency-reports-to-map-the-network-s-claimed-compliance-with-governments-around-the-world
    publisher: Meduza
    date: 2024-10-23
  - title: telegram-transparency
    url: https://github.com/Te-k/telegram-transparency
    publisher: GitHub
  - title: Translations
    url: https://translations.telegram.org/zh-hant/
    publisher: Telegram
  - title: 行動寬頻業務管理規則
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060091
    publisher: 全國法規資料庫
watch:
  - date: 2026-11-20
    note: Telegram 是否回應這批法院文件、法院文件是否公開可查，以及 2026 年第三季的透明度數字
regions:
  - US
authors:
  - anoni-net
---

404 Media 10 月 16 日報導，美國聯邦法院新歸檔的文件裡有一封 Telegram 寫給美國當局的信，依法院命令提供了一位使用者的電話號碼、使用者 ID 與 IP 位址。依 CyberInsider 的報導，信件日期是 9 月 4 日，10 月 15 日在路易斯安那州西區聯邦地區法院的一件刑事案件中歸檔。Telegram 隱私政策裡提供 IP 位址與電話號碼的條文沒有限定地區，美國以外的使用者也適用同一套規則。到 10 月 20 日為止，沒有看到 Telegram 對這批文件的公開回應。

404 Media 的報導有付費牆，寫稿時只讀得到開頭，到 10 月 20 日為止法院文件本身也查不到。信件的細節因此依 CyberInsider 的報導。信中的 IP 位址附有世界協調時間的時間戳記，代表帳號最後一次登入的時間。Telegram 在信中把這次提供描述為自願，並表示提供資料不代表接受美國的管轄。

依 CyberInsider，這份附件只有帳號與連線資訊、沒有訊息內容，但不代表調查人員沒有從其他管道取得別的資料。同一篇也提到，Telegram 通常需要電話號碼才能查到帳號的非公開資料。帳號先前因內容管理被處置過，或 Telegram 收到正式請求後啟用了額外紀錄時，有時用使用者名稱或數字 ID 也可以。信中沒有說這個帳號有沒有啟用額外紀錄。

根據 10 月 20 日查閱的 Telegram 隱私政策第 8.3 條，收到有效的司法命令時 Telegram 會先做法律分析，可能向相關機關提供 IP 位址與電話號碼。命令要確認使用者是違反服務條款的犯罪案件嫌疑人，提供之後會寫進每季的透明度報告。網頁封存的舊版本顯示，2024 年 9 月 23 日修改以前這一條只限恐怖活動嫌疑人，還寫到「So far, this has never happened」（到目前為止從未發生）。

透明度報告要用 Telegram 帳號向官方機器人查詢，依 Meduza 2024 年 10 月的說明，機器人只回傳查詢者帳號註冊所在國的資料。404 Media 2025 年 1 月引述機器人的回覆，2024 年 1 到 9 月 Telegram 完成美國調取 IP 位址或電話號碼的請求 14 次、涉及 108 位使用者，全年則是 900 次、2,253 位。另有一份由使用者貼上機器人回覆、在 GitHub 彙整的眾包資料集，2025 年美國是 1,706 次、4,807 位。Telegram 沒有在網頁上公開這些數字。

## 導讀觀點 {#perspective}

依 10 月 20 日查閱的 Telegram FAQ 與隱私政策，一般對話（雲端對話，包括一對一對話與群組）在用戶端與伺服器之間加密，訊息存在 Telegram 的伺服器上。私密對話（Secret Chats）是端對端加密（只有對話雙方的裝置能解開），不存在伺服器上，只留在雙方各自開啟這段對話的那台裝置。FAQ 的資料請求一節寫到，雲端對話的解密金鑰分散在不同司法管轄區，「To this day, we have disclosed 0 bytes of user messages to third parties, including governments」（至今沒有向包括政府在內的第三方揭露任何使用者訊息）。這一節只涉及訊息內容，IP 位址與電話號碼的提供條件寫在隱私政策第 8.3 條。

Telegram 在這封信提供的是電話號碼、使用者 ID 與 IP 位址這類帳號資料。隱私政策第 5.2 條提到，為了帳號安全與防止垃圾訊息和濫用，Telegram 可能蒐集 IP 位址、使用過的裝置與 App、使用者名稱的變更紀錄。有蒐集的話，這些紀錄最多保存 12 個月。註冊帳號也需要電話號碼。

台灣的《行動寬頻業務管理規則》第 77 條要求經營者登錄門號使用者的姓名、住址與兩種身分證明文件號碼，保存到契約終止後至少一年，有關機關依法查詢時要提供。從 Telegram 隱私政策第 8.3 條與這條規定可以推出，用台灣門號註冊的帳號一旦號碼被交出，經國內機關依法查詢就能對應到申辦人。

根據 FAQ，電話號碼預設只有你存進通訊錄的聯絡人看得到，路徑是 Settings > Privacy and Security > Phone Number（中文介面的用字以 App 為準）。官方部落格 2019 年的說明提到，把誰能看到號碼設成 Nobody 之後，還可以把誰能用號碼找到你設成只限聯絡人（現行介面的名稱以 App 為準）。依同一篇說明，把你的號碼加進聯絡人的陌生人就對應不到你的個人檔案（FAQ 提醒已經存了你號碼的人仍然看得到）。使用者名稱一律公開，FAQ 也建議不想被搜尋找到的人不要設定。

對於需要處理敏感對話的人，FAQ 建議只在官方或可驗證的開源 App 裡使用私密對話並搭配自毀計時，也建議開啟兩步驟驗證與密碼鎖。私密對話要在對方的個人頁點選「…」再選 Start Secret Chat，登出後私密對話會消失。Telegram 的翻譯平台上有正體中文語言包，用分享連結就能切換介面，FAQ 與隱私政策則沒有中文版。依隱私政策第 5.2 條與註冊需要電話號碼推論，這些做法不會讓 Telegram 手上沒有帳號號碼，IP 位址有沒有被蒐集則依第 5.2 條的情況而定。
