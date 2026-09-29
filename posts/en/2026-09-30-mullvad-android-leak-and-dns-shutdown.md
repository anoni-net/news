---
title: An Android VPN leak and the end of Mullvad's public encrypted DNS
description: A flaw lets any Android app send traffic around a VPN and reveal the real IP, even with "Block connections without VPN" on. Mullvad is also shutting down its public encrypted DNS on 2 November, so anyone who set it up by hand needs to switch.
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
  - title: Is https://mullvad.net blocked in mainland China?
    url: https://en.greatfire.org/https/mullvad.net
    publisher: GreatFire
  - title: Is https://dns.quad9.net/dns-query blocked in mainland China?
    url: https://en.greatfire.org/https/dns.quad9.net/dns-query
    publisher: GreatFire
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
authors:
  - anoni-net
---

Mullvad published two notices in September, one affecting anyone using a VPN on Android and the other anyone who set up Mullvad's public encrypted DNS by hand. A newly disclosed Android flaw lets any app, with no special permission, send some traffic outside the VPN even when "Block connections without VPN" is on. The researcher estimates that most devices on Android 12 and newer are affected, although not every model has been individually tested.

The flaw lies in keep-alive packets, small packets sent at intervals to hold a connection open. An app asks Android for a keep-alive UDP connection, which Android hands to the Wi-Fi or cellular chip to send. CyberInsider, a security news site, reports that the packets cannot carry arbitrary data but still reveal the device's real IP address to a server run by the attacker.

According to the researcher's disclosure timeline, he reported the flaw to Google's Android Vulnerability Reward Program on 15 May, and Google later marked it as a duplicate. No fix or CVE (a public vulnerability identifier) had been communicated before disclosure, and Mullvad's announcement says Google is unlikely to act.

Mullvad's public encrypted DNS shuts down on 2 November. Mullvad's 3 September notice says running a privacy-focused public DNS is highly specialised work, so Mullvad will fund the Quad9 Foundation, a Swiss non-profit, instead. Mullvad VPN users are unaffected, because their queries go to the resolver on the VPN server.

## Perspective {#perspective}

With "Block connections without VPN" on, the operating system checks that each connection goes through the tunnel. Keep-alive packets handed to the network chip leave straight from the hardware and never pass that check, so every VPN app is affected. CyberInsider's 11 September report found no reliable app-level fix, and Mullvad's 10 September notice said it had no plan to ship the theoretical workaround of filling the hardware's keep-alive slots.

Mullvad's advice is to install only apps you trust and, if possible, use a security- and privacy-focused Android fork such as GrapheneOS. GrapheneOS officially supports only Pixel devices from the Pixel 6 onward. It merged a change disabling unprivileged hardware keep-alives on 28 September, and as of 29 September no release included it yet.

For people whose real IP must not leak, CyberInsider mentions putting the phone behind a router that enforces the VPN, provided cellular and other network paths are off. The protection ends when the phone leaves that network.

In mainland China, GreatFire, which tests what the Great Firewall blocks, had recorded all 17 of its tests of mullvad.net over the past 90 days as blocked as of 29 September. The blocked addresses include the download links for Mullvad's apps. Its two most recent conclusive tests of Quad9's DoH (DNS over HTTPS) address both showed interference, the latest on 3 September, so the DNS switch below matters mostly outside mainland China.

Quad9's privacy policy says users' IP addresses stay in memory only for the microseconds to milliseconds needed to answer a query. The same policy says Quad9 keeps aggregate counters by region, carrier network and protocol, without individual IPs. Switching still leaves every DNS query with a single operator.

Mullvad Browser users on default settings move to Quad9 automatically, while those who chose another Mullvad DNS variant should switch back to the default. Anyone else who set it up by hand should switch before 2 November. Mullvad's iOS and macOS profiles will stop working. Quad9's replacements for iPhone (iOS 14 or later) and Mac (Big Sur or later) are downloaded in Safari and expire on 19 January 2027.

On Android 9 or later, enter the hostname `dns.quad9.net` under Private DNS. That setting uses DNS over TLS, so the DoH address `https://dns.quad9.net/dns-query` does not belong there. With another VPN on, Quad9's guides say profiles and Private DNS are generally not used, and Quad9's addresses go in the VPN app's custom DNS setting. The guides come in English, French, Spanish and Romanian only.
