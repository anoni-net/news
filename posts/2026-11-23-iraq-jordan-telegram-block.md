---
title: 伊拉克與約旦的 Telegram 封鎖與 OONI 量測
description: 伊拉克與約旦 11 月 16 日宣布封鎖 Telegram。依 OONI Probe 的量測，兩國的 Telegram 測試在 11 月 15 日到 16 日之間（UTC）轉為異常，到 11 月 20 日仍然全部異常。兩國的命令只適用於各自境內的網路，其他地方的讀者不受這次封鎖影響。
date: 2026-11-23T00:05:00+08:00
slug: iraq-jordan-telegram-block
categories:
  - censorship
sources:
  - title: "Iraq and Jordan block Telegram (16 Nov 2026): OONI measurements"
    url: https://github.com/net4people/bbs/issues/686
    publisher: net4people
    date: 2026-11-19
  - title: Iraq
    url: https://explorer.ooni.org/chart/mat?probe_cc=IQ&since=2026-11-01&until=2026-11-21&time_grain=day&axis_x=measurement_start_day&test_name=telegram
    publisher: OONI Explorer
  - title: Jordan
    url: https://explorer.ooni.org/chart/mat?probe_cc=JO&since=2026-11-01&until=2026-11-21&time_grain=day&axis_x=measurement_start_day&test_name=telegram
    publisher: OONI Explorer
  - title: Telegram test
    url: https://ooni.org/nettest/telegram/
    publisher: OONI
  - title: Frequently Asked Questions (FAQ)
    url: https://ooni.org/support/faq/
    publisher: OONI
  - title: "Risks: Things you should know before running OONI Probe"
    url: https://ooni.org/about/risks/
    publisher: OONI
  - title: ooni/probe
    url: https://github.com/ooni/probe
    publisher: GitHub
  - title: Iraqi Government Orders Telegram Ban Over Regulatory Violations
    url: https://www.kurdistan24.net/en/story/953424/iraqi-government-orders-telegram-ban-over-regulatory-violations
    publisher: Kurdistan24
    date: 2026-11-16
  - title: Jordan and Iraq block Telegram app over national security concerns
    url: https://www.al-monitor.com/originals/2026/11/jordan-and-iraq-block-telegram-app-over-national-security-concerns
    publisher: Al-Monitor（轉載路透）
    date: 2026-11-17
  - title: Jordan and Iraq block Telegram over national security concerns
    url: https://www.aljazeera.com/news/2026/11/16/jordan-bans-telegram-messing-app-over-national-security-concerns
    publisher: Al Jazeera
    date: 2026-11-16
watch:
  - date: 2026-12-23
    note: 伊拉克給 Telegram 的 30 天期限過後是否解除封鎖，約旦是否解除封鎖，兩國 OONI 的 Telegram 測試是否回到正常
regions:
  - IQ
  - JO
authors:
  - anoni-net
---

政府宣布封鎖時，公告不一定交代何時生效、涵蓋哪些網路，外界可以從當地網路上的量測確認。伊拉克通訊與媒體委員會 11 月 16 日依總理的指令，宣布在全國封鎖 Telegram，約旦的公共安全局同一天也宣布封鎖。依 OONI Probe（量測網路封鎖的開源軟體）的量測，兩國的 Telegram 測試在 11 月 15 日到 16 日之間（UTC）轉為異常，到 20 日仍然全部異常。兩國的命令只適用於各自境內的網路，其他地方的讀者不受這次封鎖影響。

伊拉克的委員會指 Telegram 沒有處理平台上的違法內容、沒有履行伊拉克法律規定的義務，給營運公司 30 天補正法律地位。Kurdistan24 報導的聲明沒有指出決定依據的是哪些頻道或貼文，也沒有說明期限內要完成哪些步驟、期限過後會如何處理。依 Al Jazeera 的報導，約旦的公共安全局以遏止違法內容與極端主義的內容為由宣布封鎖。路透的報導寫 Telegram 否認伊拉克的指控，Telegram 給路透的聲明提到它打擊恐怖主義的做法超出法律的要求。

OONI Probe 由使用者在自己的網路上執行，量測結果公開，日期以世界協調時間（UTC）計。伊拉克在封鎖前每天有 67 到 80 筆 Telegram 測試，幾乎沒有異常。16 日的 72 筆有 33 筆異常，17 日起全部異常。討論網路審查的公開論壇 net4people 上，一則 11 月 19 日整理兩國量測的貼文提到，同一週伊拉克的 WhatsApp 與 Signal 測試維持平常的水準。

約旦的量測少得多，封鎖前每天只有 1 到 8 筆，都沒有異常。15 日的 13 筆有 7 筆異常，16 日起全部異常。OONI 以 UTC 計日，約旦當地時間比 UTC 快 3 小時。UTC 15 日的最後 3 小時在約旦已經是 16 日，從這些數字分不出異常是否早於公告。

## 導讀觀點 {#perspective}

OONI 的 Telegram 測試在使用者的網路上試著連上 Telegram App 使用的伺服器，也試著開啟網頁版 `web.telegram.org`。依 OONI 的測試說明，App 的伺服器全部無法連線或網頁版無法正常開啟時，Telegram 可能遭到封鎖。量測標為異常，代表結果符合其中一種情況，連線失敗的原因要另外判斷。

伊拉克 11 月 17 日以後有量測的 12 個 AS（網際網路上由同一個業者或機構管理的一組網路），以及約旦 16 日以後的 4 個 AS，每一筆量測都是異常。從這些數字看不出封鎖用什麼技術、在網路的哪一處攔下。一般而言，攔截的方式會影響其他服務是否一併受波及。

能看出兩國的轉折，是因為封鎖前已經有每天正常的量測可以對照。量測只涵蓋有人執行測試的網路，像約旦這樣每天只有個位數測試的網路，很難判斷轉折發生在哪個時刻。想看數字的人不必安裝，在 OONI 公開量測結果的網站 OONI Explorer 選擇國家與 Telegram 測試就能查詢。

在自己的網路上執行 Probe 也有代價。OONI 的常見問題寫到 Probe 不是隱私工具，監控網路活動的人（例如政府、網路業者、雇主）可能看到你在執行它。風險說明頁則寫到，執行 Probe 的潛在風險取決於使用者的威脅模型（自己可能面對誰、對方有什麼能力）與所在國家的法規。本站 11 月 20 日[OONI Probe 的 TLS Middlebox 實驗與資料蒐集問卷](https://anoni.net/news/2026/11/ooni-tls-middlebox/)那篇寫了 App 裡可以選擇執行哪些測試、不送出量測，以及做了這些設定，有人在執行 Probe 仍可能被看到。

伊拉克與約旦以外的讀者不必做任何設定。依路透的報導，伊拉克 2023 年也封鎖過 Telegram，一週後在政府表示公司已回應安全單位的要求之後恢復服務。兩國宣布解除之後，Telegram 測試有沒有回到正常，同樣可以在 OONI Explorer 對照。
