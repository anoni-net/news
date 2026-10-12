---
title: 國碼頂級網域劫持事件與未經授權的 HTTPS 憑證
description: Google 10 月 6 日公告，迦納、獅子山與美屬薩摩亞的國碼頂級網域遭到劫持，攻擊者取得 Google 與其他組織網域的 HTTPS 憑證。Chrome 已封鎖找到的憑證，自己管理網域的人可以監控憑證透明度紀錄。
date: 2026-10-16T00:05:00+08:00
slug: cctld-hijack-counterfeit-certs
categories:
  - security
regions:
  - GH
  - SL
  - AS
sources:
  - title: Chrome's Response to Recent ccTLD Registry Hijacks
    url: https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/
    publisher: Google
    date: 2026-10-06
  - title: Chrome's Response to Recent ccTLD Registry Hijacks
    url: https://community.letsencrypt.org/t/chromes-response-to-recent-cctld-registry-hijacks/251941
    publisher: Let's Encrypt 社群論壇
    date: 2026-10-07
  - title: Hackers obtain counterfeit TLS certificates for Google and other large services
    url: https://arstechnica.com/security/2026/10/hackers-obtain-counterfeit-tls-certificates-for-google-and-other-large-services/
    publisher: Ars Technica
    date: 2026-10-06
  - title: Hackers Impersonate Google and Other Large Services With Counterfeit TLS Certificates
    url: https://www.privacyguides.org/news/2026/10/08/hackers-impersonate-google-and-other-large-services-with-counterfeit-tls-certificates/
    publisher: Privacy Guides
    date: 2026-10-08
  - title: 3個國碼頂級網域遭劫持，攻擊者取得Google等組織HTTPS憑證
    url: https://www.ithome.com.tw/news/179500
    publisher: iThome
    date: 2026-10-09
  - title: Attackers hijack ccTLDs to fake certs for Google
    url: https://www.itnews.com.au/news/attackers-hijack-cctlds-to-fake-certs-for-google-629504
    publisher: iTnews
    date: 2026-10-08
  - title: DNS Hijacks Across Three ccTLDs Linked to 32 Unauthorized HTTPS Certificates
    url: https://circleid.com/posts/dns-hijacks-across-three-cctlds-linked-to-32-unauthorized-https-certificates
    publisher: CircleID
    date: 2026-10-08
  - title: CRLSets
    url: https://www.chromium.org/Home/chromium-security/crlsets/
    publisher: The Chromium Projects
  - title: Certificate Transparency Monitoring
    url: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/
    publisher: Cloudflare
  - title: Cert Spotter - Certificate Transparency Monitor - Detect Security and Availability Problems
    url: https://sslmate.com/certspotter/
    publisher: SSLMate
  - title: Certification Authority Authorization (CAA)
    url: https://letsencrypt.org/docs/caa/
    publisher: Let's Encrypt
watch:
  - date: 2026-11-16
    note: 三個國碼頂級網域的營運單位或簽發的憑證機構，是否公布入侵的層級、時間與完整的憑證清單
authors:
  - anoni-net
---

Google 10 月 6 日公告，.gh（迦納）、.sl（獅子山）與 .as（美屬薩摩亞）三個國碼頂級網域遭到劫持，攻擊者藉此取得多個 Google 網域與其他組織網域的 HTTPS 憑證。國碼頂級網域（ccTLD）是代表國家或地區的頂級網域，例如台灣的 .tw。公告寫明有風險的是以這三個代碼結尾的網域，Google 自家的系統沒有遭到入侵。Chrome 已封鎖找到的憑證，公告寫明 Chrome 使用者不必採取任何行動。

依 Google 的公告，攻擊者入侵的是由第三方營運的這三個頂級網域，改動了權威 DNS 記錄（決定一個網域該連到哪裡的那一份記錄）。公告沒有寫攻擊者從哪個環節入侵（例如營運單位的系統或註冊商帳號）、劫持從何時開始，到 10 月 12 日為止也查不到三個營運單位的說明。Ars Technica 的報導寫明攻擊者控制 DNS 記錄之後通過了憑證機構的網域控制驗證（DCV，確認申請者確實掌控網域的程序），iThome 寫的是可能藉此通過。Google 的公告寫明沒有理由認為簽發憑證的憑證機構做錯了什麼。

Google 先用 CRLSets（Chrome 緊急封鎖特定憑證用的清單）封鎖 Google 網域的憑證，並請簽發的憑證機構撤銷。之後從憑證透明度（CT，公開記錄每一張已簽發憑證的日誌）找到可能受同一波攻擊影響的其他組織，包括幾個全球大型品牌與廣泛使用的線上服務，也在 Chrome 封鎖了這些憑證。

Let's Encrypt 的工作人員在論壇確認，該機構簽發過 Google 與 YouTube 的憑證，已經撤銷。澳洲媒體 iTnews 自行比對 CT 紀錄與 Chrome 的封鎖清單，找到 9 月 22 日到 27 日之間發給攻擊者的 32 張憑證。CircleID 註明這個數字還沒有經過其他人獨立重現。

## 導讀觀點 {#perspective}

HTTPS 憑證用來證明「這個網站就是它聲稱的那一個」，憑證機構簽發之前確認的是申請者能不能掌控網域，其中一種做法是請申請者在 DNS 加上一筆指定的記錄。DNS 從頂級網域一路往下委派，依這個機制推論，上層被劫持時攻擊者一樣能讓驗證通過。底下網域的擁有者即使沒有犯任何錯，也擋不住這種情況。Google 公告寫明，憑證機構可以重用先前完成的驗證結果，縮短憑證效期與驗證結果的重用期間是 Google 列出的長期改善方向。

其他可能受影響的組織，是 Google 從憑證透明度的日誌找到的。Chrome 與 Safari 都要求公開信任的憑證登錄在公開的日誌裡，任何人都能查詢。Google 找到的憑證都是從日誌查到的。依本文的理解，CT 讓這類憑證在簽發之後被發現，簽發當下並不會擋下。

Google 也寫明，Chrome 的封鎖無法可靠地保護其他瀏覽器的使用者，Google 也不能保證已經找出每一個受影響的網域。公告寫明 Google 網域的憑證已請憑證機構撤銷，其他組織的憑證只寫了在 Chrome 封鎖，iTnews 的報導則寫它找到的偽造憑證已由憑證機構撤銷。Privacy Guides 的報導寫 Firefox 用 CRLite（Firefox 檢查憑證是否已撤銷的機制）處理，Safari 與 Edge 到 10 月 12 日查不到相關說明。被攔截的連線有多少，CircleID 寫明到 10 月 8 日都還沒有公開的資料。

Google 建議自己管理網域的人持續監控手上所有網域的 CT 紀錄，包括停放中或各地區的國碼網域，使用 .gh、.sl 或 .as 網域的人要回頭檢查近期有沒有非預期的憑證。Cloudflare 與 Cert Spotter 等服務會在有新憑證簽發時發出通知。Cloudflare 的通知要在它的 Edge Certificates 頁面開啟，預設是關閉的，Cert Spotter 的網站列的是 30 天免費試用。Google 也建議設定 CAA 記錄（DNS 裡指定哪些憑證機構可以簽發的記錄），最好綁定特定的 ACME（Let's Encrypt 等機構自動簽發憑證用的協定）帳號。

Google 寫明 CAA 擋不住劫持進行中的簽發，它的作用在 DNS 控制權恢復之後，可以防止攻擊者拿先前通過的驗證結果繼續申請新憑證。CT 監控同樣是讓人在事後早一點發現，Google 的建議裡沒有網域擁有者能事先擋下這類上層劫持的做法。

到 10 月 12 日，查不到三個營運單位或簽發的憑證機構公布入侵的環節與完整的憑證清單。11 月中可以再查一次，看看有沒有事故報告說明攻擊者從哪裡入侵。
