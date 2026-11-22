---
title: 英國政府對 Apple 技術能力通知的保密主張與調查權力法庭判決
description: 英國調查權力法庭 11 月 19 日的判決認定政府沒有證明公開確認曾對 Apple 發出技術能力通知會損害國家安全，通知是否合法還沒有審理，內容也沒有公布。雙方表示可望以 2027 年上半年為目標安排實質聽證，依 Apple 的說明頁，到 11 月 21 日英國以外的使用者仍可開啟 iCloud 進階資料保護。
date: 2026-11-24T00:05:00+08:00
slug: uk-apple-encryption-order
categories:
  - encryption
follows:
  - 2026-09-27-uk-icloud-advanced-data-protection
sources:
  - title: OPEN Judgment Apple Inc. and Privacy Int. Ors
    url: https://www.judiciary.uk/wp-content/uploads/2026/11/OPEN-Judgment-Apple-Inc.-and-Privacy-Int.-Ors.pdf
    publisher: Investigatory Powers Tribunal
    date: 2026-11-19
  - title: UK court confirms British government served Apple with secret encryption notice
    url: https://therecord.media/apple-uk-encryption-notice
    publisher: The Record
    date: 2026-11-19
  - title: "Win! Tribunal orders UK Government to come clean about secret order to Apple"
    url: https://privacyinternational.org/news-analysis/5896/win-tribunal-orders-uk-government-come-clean-about-secret-order-apple
    publisher: Privacy International
    date: 2026-11-19
  - title: UK Loses Secrecy Fight Over Apple 'Backdoor' Order
    url: https://www.macrumors.com/2026/11/19/uk-loses-secrecy-fight-over-apple-backdoor-order/
    publisher: MacRumors
    date: 2026-11-19
  - title: UK Government Forced to Admit It Issued Apple a Secret Encryption Order
    url: https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/
    publisher: MacAnorak
    date: 2026-11-19
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: iCloud data security overview
    url: https://support.apple.com/en-us/102651
    publisher: Apple
    date: 2026-01-05
  - title: 如何開啟「iCloud 進階資料保護」
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
    date: 2026-04-24
regions:
  - GB
watch:
  - date: 2027-01-15
    note: 調查權力法庭對 Apple 與倡議組織案件的實質聽證是否排定日期，以及 Apple 是否公布英國已開啟 ADP 的使用者自行關閉的期限
authors:
  - anoni-net
---

英國調查權力法庭（審理部分國家安全案件的法庭）11 月 19 日公布判決，認定政府沒有證明公開確認「曾對 Apple 發出技術能力通知」會損害國家安全。技術能力通知是政府要求業者保有協助調查能力的命令，判決寫明政府確實對 Apple 發出了通知。法庭沒有判斷通知是否合法，也沒有公布通知的內容。

判決處理的是英國政府對 Apple 的要求，Apple 的英國說明頁寫明進階資料保護（ADP，讓 iCloud 備份、照片等資料只有使用者裝置能解密）在英國以外的地方繼續提供。到 11 月 21 日英國的新使用者仍不能開啟 ADP，已經開啟的人之後要自行關閉才能繼續使用 iCloud 帳號。Apple 寫會給這些人一段期間，MacRumors 11 月 19 日的報導寫期限仍沒有公布，我們也沒有查到 Apple 對判決的公開聲明。

媒體從 2025 年 2 月起報導，英國政府依《2016 年調查權力法》要求 Apple 維持以解密形式存取使用者資料的能力。依倡議組織 Privacy International 整理的時間線，英國據報撤回一份通知，《金融時報》之後報導的第二份通知範圍據信只限英國。Apple 與 Privacy International 等倡議組織都對通知提出申訴，法庭這次把兩邊的申訴一起處理。

英國政府對這類通知採取「不證實也不否認」的政策，在法庭上主張連確認通知存在都會損害國安。法庭推斷，《泰晤士報》與《金融時報》引述政府消息來源的報導是經政府授權的說明，因此認定官方確認不會讓惡意者多掌握實質的資訊。法庭同意把通知內容與雙方的證據全部公開會損害國安，哪些細節可以公開要等雙方交換證據之後再決定。之後要審理通知本身是否合法的實質聽證，雙方表示可望以 2027 年上半年為目標安排。

## 導讀觀點 {#perspective}

英國政府在判決後的聲明由 The Record 引述，聲明提到 Apple 多年來依法協助警方與情報機關追查罪犯，「這份技術能力通知只是要求他們維持這樣的能力」。iCloud 預設的標準資料保護會加密資料，金鑰則存放在 Apple 的資料中心，開啟 ADP 後大部分資料的金鑰只留在使用者信任的裝置上。我們依政府聲明的說法推論，要對開啟 ADP 的帳號維持這種能力，Apple 就需要重新取得金鑰。Apple 則在 2025 年 9 月的英國說明頁寫到，從未在任何產品或服務中建置後門或萬能鑰匙，將來也不會。

Apple 在申訴中質疑《調查權力法》的權力能否用來規範公司提供的安全或隱私服務，也質疑通知對歐洲人權公約保障的權利所做的限制，是否超出達成目的所需的程度。政府的聲明則寫到隱私雖然重要也不該以英國民眾的安全為代價，影響民眾安全的決定應由民選政府與獨立的法官做出，不在科技公司的董事會裡決定。

判決沒有改變英國使用者目前的限制。Apple 台灣的正體中文說明頁沒有寫地區限制，iPhone 與 iPad 使用者照頁面的步驟點進「進階資料保護」，還沒開啟的帳號會看到「開啟進階資料保護」。開啟前要先設定復原聯絡人或復原密鑰，開啟後 Apple 沒有協助復原所需的密鑰，無法取用帳號時要靠這些方式或裝置密碼復原資料。開啟之後 iCloud 備份、iCloud 雲碟、照片、備忘錄等資料改用端對端加密，iCloud 郵件、聯絡人與行事曆仍由 Apple 保管金鑰。

之後的實質聽證要處理的問題之一，是《調查權力法》的權力能否用來規範公司提供給客戶的安全或隱私服務。如果可以，在英國提供服務的公司還能不能提供金鑰只留在使用者裝置上的設計？政府想達成的調查效果在這種設計下能否做到？法庭也要在英國民眾了解這項權力範圍的需要，與政府主張公開細節會帶來的國安風險之間，決定審理能公開到什麼程度。
