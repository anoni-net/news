---
title: Android 的 VPN 漏洞與 Mullvad 加密 DNS 的停用
description: Android 的一個漏洞讓任何 App 繞過 VPN、洩漏真實 IP，開啟「封鎖沒有 VPN 的連線」也無法阻擋。Mullvad 的公開加密 DNS 將在 11 月 2 日停止服務，手動設定過的人需要更換。
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
  - title: Releases | GrapheneOS
    url: https://grapheneos.org/releases
    publisher: GrapheneOS
  - title: Frequently Asked Questions | GrapheneOS
    url: https://grapheneos.org/faq#supported-devices
    publisher: GrapheneOS
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
  - title: Big Sur and later (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/MacOS/Big_Sur_and_later_%28Encrypted%29/
    publisher: Quad9
  - title: Android 9+ (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/Android/Android_9%2B_%28Encrypted%29/
    publisher: Quad9
  - title: packages/apps/Settings/res/values-zh-rTW/strings.xml
    url: https://github.com/aosp-mirror/platform_packages_apps_settings/blob/main/res/values-zh-rTW/strings.xml
    publisher: Android Open Source Project
  - title: frameworks/base/packages/SettingsLib/res/values-zh-rTW/strings.xml
    url: https://github.com/aosp-mirror/platform_frameworks_base/blob/main/packages/SettingsLib/res/values-zh-rTW/strings.xml
    publisher: Android Open Source Project
watch:
  - date: 2026-11-03
    note: Mullvad 的公開加密 DNS 是否如期在 11 月 2 日停止，GrapheneOS 已合併的修正（9 月 28 日）是否進入正式版本，Android 的 VPN 漏洞是否有修正
authors:
  - anoni-net
---

VPN 業者 Mullvad 在 9 月發布兩則公告，一則影響所有在 Android 上使用 VPN 的人，另一則影響手動設定過 Mullvad 加密 DNS 的人。Android 新發現的漏洞讓任何 App 不需要特殊權限就能繞過 VPN，開啟「封鎖沒有 VPN 的連線」也無法阻擋。研究者估計多數 Android 12 以上的裝置受影響，但並非每個型號都實測過。Mullvad 的公開加密 DNS 則將在 11 月 2 日停止服務。

漏洞出在 keep-alive 封包（為了維持連線、定期送出的小封包）。惡意 App 可以要求 Android 建立一條 keep-alive 連線，由 Android 交給 Wi-Fi 或行動網路晶片自行送出。資安新聞網站 CyberInsider 報導，封包的格式由 Android 決定，無法夾帶任意資料。接收的伺服器仍可以看到裝置在 VPN 之外的真實 IP。

依研究者的揭露時間線，他在 5 月 15 日把漏洞回報給 Google 的 Android 漏洞獎勵計畫，Google 之後把它標記為重複的回報。公開之前，Google 沒有告知修正，也沒有配發 CVE（公開漏洞的統一編號）。Mullvad 的公告寫到，Google 不太可能處理，Mullvad 目前也沒有計畫提供占滿硬體 keep-alive 名額這種理論上的緩解做法。

DNS 那一則是 9 月 3 日的公告，寫明經營注重隱私的公開 DNS 需要高度專業，Mullvad 決定改為資助 Quad9 基金會（提供公開 DNS 的瑞士非營利組織）。使用 Mullvad VPN 的人不受影響，查詢由 VPN 伺服器處理。使用預設設定的 Mullvad Browser 會自動改用 Quad9，手動選過其他 Mullvad DNS 變體的人要改回預設。iOS 與 macOS 上 Mullvad 的 DNS 描述檔則會失效。

## 導讀觀點 {#perspective}

開啟「封鎖沒有 VPN 的連線」時，系統會檢查每條連線是否經過 VPN。keep-alive 交給網路晶片之後，封包直接從網路硬體送出，不經過這道檢查。CyberInsider 的報導寫到，目前沒有可靠的 App 層級修正。

Mullvad 的建議是只安裝信任的 App，可以的話改用 GrapheneOS 這類強化隱私與安全的 Android 版本，不過 GrapheneOS 的正式版本只支援 Pixel 6 以上的 Pixel 裝置。GrapheneOS 關閉這類 keep-alive 的修正在 9 月 28 日合併，到 9 月 29 日為止還沒有進入正式版本。

真實 IP 一旦外洩就有風險的人，可以參考 CyberInsider 報導的做法，讓手機連上強制走 VPN 的路由器。前提是關閉行動網路等其他連線路徑，手機離開那台路由器就沒有這層保護。

手動設定過 Mullvad 加密 DNS 的人可以改用 Quad9，它的隱私政策寫明使用者的 IP 只在處理查詢的極短時間內留在記憶體。政策也寫到會保留依地區、電信網路與協定分類的統計，不含個別的 IP。改用之後，DNS 查詢仍然集中在同一個營運者手上。

更換要在 11 月 2 日前完成。iPhone（iOS 14 以上）與 Mac（Big Sur 以上）要用 Safari 從 Quad9 的說明頁下載描述檔，2027 年 1 月 19 日到期後需重新安裝。Android 9 以上在「私人 DNS」填入主機名稱 `dns.quad9.net`，這個欄位走 DoT（DNS over TLS），不能填 DoH（DNS over HTTPS）網址 `https://dns.quad9.net/dns-query`。

使用 VPN 時，Quad9 的說明頁寫明描述檔與私人 DNS 通常不會生效，要改在 VPN App 的自訂 DNS 設定 Quad9。說明頁有英文、法文、西班牙文與羅馬尼亞文，沒有中文。
