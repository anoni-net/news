---
title: 轉接境外詐騙電話的 Android 手機與來電號碼
description: 刑事局 11 月 19 日公布一組案件，詐團用插著國內 SIM 卡的 Android 手機替境外機房撥出詐騙電話。來電顯示台灣門號不代表對方人在台灣，接到自稱機關的電話，可以掛斷改撥官方號碼或 165 查證。
date: 2026-11-29T00:00:00+08:00
slug: android-sim-relay
categories: [security]
regions:
  - TW
sources:
  - title: 刑事局攜手NCC與三大電信業者公私聯防 全面查緝DMT詐欺話務轉接機房阻斷詐欺犯罪源頭
    url: https://www.cib.npa.gov.tw/ch/app/news/view?module=news&id=1885&serno=eb9d97b0-d3e4-4d7e-a916-4dbe55bde20d
    publisher: 內政部警政署刑事警察局
    date: 2026-11-19
  - title: Android手機變詐騙話務中繼站、泡芙箱藏上百張SIM卡！刑事局揭露詐團電話轉接新手法
    url: https://www.ithome.com.tw/news/180687
    publisher: iThome
    date: 2026-11-20
  - title: 使用詐騙偵測功能
    url: https://support.google.com/phoneapp/answer/15654065?hl=zh-TW
    publisher: Google
  - title: 在接聽電話前先過濾來電
    url: https://support.google.com/phoneapp/answer/9118387?hl=zh-TW
    publisher: Google
  - title: 在 iPhone 上篩選和封鎖通話
    url: https://support.apple.com/zh-tw/guide/iphone/iphe4b3f7823/ios
    publisher: Apple
related:
  - title: 一般人平常該做到什麼
    url: https://anoni.net/docs/scenarios/everyday-baseline/
authors:
  - anoni-net
---

用台灣門號接電話的人，看到來電顯示是國內號碼，打電話的人仍可能在境外。刑事警察局 11 月 19 日公布的一組案件裡，詐團用一般的 Android 手機加上 App 與周邊配件，組成能雙向轉接話務的設備。設備插入國內電信的 SIM 卡之後，境外的詐欺機房就能遠端連線發話，假冒公務機關、醫院或電信客服打給民眾。警方在 7 到 9 月查扣以手機組成的轉接設備等 18 組。

電信業者全面推動國際電話語音警示（接聽境外來電前先播放提醒的語音）之後，境外詐團為了避開警示，改在台灣架設 DMT（數位行動電話節費設備）。DMT 把經網路傳來的境外通話，改從插在設備裡的國內 SIM 卡以行動電話撥出。依 iThome 的報導，這樣撥出的電話看似一般國內來電，號碼前面沒有境外來電通常會有的「+」與國碼。傳統 DMT 這類專用設備遭警方大量查緝之後，詐團改用 Android 手機。

詐團會以居家兼職、代管設備、借貸或假冒檢警要求配合辦案為名，請民眾接收設備、插入本人名下的 SIM 卡，來電顯示的號碼因此可能是被招募的民眾自己的門號。有人要你把 SIM 卡插進對方給的設備或在家代管設備，就是這類招募。答應的人可能被收取高額通話費，也可能涉及刑事責任與民事求償。依刑事局的提醒，政府機關、警察與檢察官不會要求民眾申辦門號、提供 SIM 卡、安裝不明 App 或代為架設通訊設備。

## 導讀觀點 {#perspective}

從來電顯示的號碼只能知道是哪一張 SIM 卡在台灣撥出電話。刑事局把以手機組成的設備也歸為 DMT 轉接設備，iThome 又寫 DMT 撥出的電話顯示為國內來電。從這兩點推想，Android 手機轉接的電話，來電顯示的也是那張 SIM 卡的國內號碼。打電話的人是誰、在哪裡，從號碼都無法判斷。

接到自稱公務機關、醫院或電信客服的電話，可以先掛斷，再從官網、帳單或卡片背面這類可以自行找到的管道查號碼撥過去。來電顯示的號碼與對方給的號碼都不要回撥。設備能雙向轉接話務，照這點推想，撥回那個國內門號的電話可能會被轉回境外機房。不確定時也可以撥 165 反詐騙諮詢專線。

到 11 月 29 日為止，Google「電話」App 的詐騙偵測與接聽前過濾來電都還沒有在台灣提供，詐騙偵測也只限 Pixel。用 Android 手機的人在台灣接到這類電話，仍要靠掛斷再查證。

iPhone 在「設定」的「App」→「電話」裡，可以把未知號碼的來電設成「詢問致電原因」或「靜音」。選前者時 iPhone 響鈴前會先要求來電者說明來意，選後者時來電會設為靜音並轉接語音信箱。兩個選項都依號碼是否存在通訊錄判斷，只能減少陌生來電的打擾，無法辨識從國內門號撥出的詐騙電話。很少需要接陌生電話的人可以考慮改用這兩個選項，代價是可能漏接醫院、物流這類正當的陌生來電。
