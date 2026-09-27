---
title: Android 的 VPN 漏洞與 Mullvad 加密 DNS 的停用
description: Android 有個漏洞讓任何 App 繞過 VPN 露出真實 IP，開著封鎖未使用 VPN 的連線也擋不住。Mullvad 公開的加密 DNS 也將在 11 月 2 日停止服務。
date: 2026-09-30T07:00:00+08:00
slug: mullvad-android-leak-and-dns-shutdown
sources:
  - title: Another way to leak traffic on Android has been discovered
    url: https://www.mullvad.net/en/blog/2026/9/10/another-way-to-leak-traffic-on-android-has-been-discovered/
    publisher: Mullvad
    date: 2026-09-10
  - title: Shutting down our public encrypted DNS servers and sponsoring Quad9 instead
    url: https://www.mullvad.net/en/blog/2026/9/3/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead/
    publisher: Mullvad
    date: 2026-09-03
  - title: DNS over HTTPS and DNS over TLS
    url: https://mullvad.net/en/help/dns-over-https-and-dns-over-tls
    publisher: Mullvad
    date: 2026-09-03
  - title: Mullvad warns of a new Android VPN leak as GrapheneOS develops a fix
    url: https://cyberinsider.com/mullvad-warns-of-new-android-vpn-leak-as-grapheneos-works-on-fix/
    publisher: CyberInsider
    date: 2026-09-11
  - title: Disable unprivileged hardware keepalives
    url: https://github.com/GrapheneOS/platform_packages_modules_Connectivity/pull/47
    publisher: GrapheneOS
    date: 2026-09-26
  - title: Quad9 Privacy Policy
    url: https://quad9.net/privacy/policy/
    publisher: Quad9
    date: 2026-06-24
  - title: Service Addresses & Features
    url: https://quad9.net/service/service-addresses-and-features/
    publisher: Quad9
  - title: iOS 14 and later (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/iOS/iOS_14_and_later_%28Encrypted%29/
    publisher: Quad9
  - title: Android 9+ (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/Android/Android_9%2B_%28Encrypted%29/
    publisher: Quad9
authors:
  - anoni-net
---

VPN 業者 Mullvad 在 9 月發了兩則公告，都會影響使用者的設定。一則是 Android 新發現的漏洞，任何 App 不需要特殊權限，就能讓部分流量繞過 VPN，即使開著「封鎖所有未使用 VPN 的連線」也一樣。另一則是 Mullvad 公開的加密 DNS 將在 11 月 2 日停止服務，手動設定過的人要換掉。

漏洞出在 keep-alive 封包。惡意 App 可以要求 Android 建立一條 keep-alive 的 UDP 連線，交給 Wi-Fi 或行動網路晶片自行送出，封包直接從硬體出去，就略過了 VPN 的檢查。CyberInsider 報導，研究者估計多數 Android 12 以後的裝置都受影響，這種封包無法夾帶任意資料，但足以露出裝置在 VPN 之外的網路身分。

研究者把漏洞回報給 Google 的漏洞獎勵計畫，被標成重複的回報，公開前沒有修正，也沒有 CVE。Mullvad 的公告寫到，Google 不太可能處理，Mullvad 也沒有打算提供緩解措施。

Mullvad 的公告寫到，經營注重隱私的公開 DNS 需要高度專業，所以把資源改為資助 Quad9 基金會。使用 Mullvad VPN 的人不受影響，連線時由 VPN 伺服器的 DNS 處理查詢。使用預設設定的 Mullvad Browser 會自動改用 Quad9，iOS 與 macOS 的 Mullvad DoH 設定檔則會失效。

## 導讀觀點 {#perspective}

VPN 的鎖定功能，靠作業系統檢查每條連線有沒有經過 VPN。這次的問題出在 Android 把 keep-alive 交給網路晶片處理，封包根本不經過那道檢查。所以 Mullvad 的建議落在源頭，只安裝信任的 App，可以的話改用 GrapheneOS 這類注重隱私與安全的 Android 版本。GrapheneOS 已經有關閉這類 keep-alive 的修正，到 9 月 27 日還沒有合併發布。

真實 IP 一旦外洩就有風險的人，還可以參考 CyberInsider 報導的做法，讓手機接在強制走 VPN 的路由器後面，同時關閉行動網路等其他連線路徑。代價是出門在外就需要另外準備設備。

替代的選項之一是 Mullvad 改為資助的 Quad9，它的隱私政策寫明不蒐集、不記錄使用者的 IP，由瑞士的基金會營運。同一份政策也寫到，Quad9 會保留依地區、電信業者與協定分類的統計數字，這些統計不含個別使用者的 IP，但 DNS 查詢仍然集中在一家業者手上。Mullvad 的說明頁也寫到，已經連上 VPN 時再用公開的加密 DNS，安全上的好處很少，速度一定比用 VPN 伺服器的 DNS 慢。

手動設定過 Mullvad DoH 的人要在 11 月 2 日前換掉，Quad9 的 DoH 位址是 `https://dns.quad9.net/dns-query`。iPhone 與 Mac 可以從 Quad9 的說明頁下載設定描述檔，Android 在「私人 DNS」填入 `dns.quad9.net`，說明頁有英文、法文、西班牙文與羅馬尼亞文，沒有中文。
