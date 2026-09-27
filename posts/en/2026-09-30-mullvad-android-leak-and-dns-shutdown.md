---
title: An Android VPN leak and the end of Mullvad’s public encrypted DNS
description: A flaw lets any Android app send traffic around a VPN and reveal the real IP, even with "Block all connections without VPN" on. Mullvad is also shutting its public encrypted DNS on 2 November.
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
  - title: Is https://mullvad.net blocked in mainland China?
    url: https://en.greatfire.org/https/mullvad.net
    publisher: GreatFire
  - title: Is https://dns.quad9.net/dns-query blocked in mainland China?
    url: https://en.greatfire.org/https/dns.quad9.net/dns-query
    publisher: GreatFire
  - title: iOS 14 and later (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/iOS/iOS_14_and_later_%28Encrypted%29/
    publisher: Quad9
  - title: Android 9+ (Encrypted)
    url: https://docs.quad9.net/Setup_Guides/Android/Android_9%2B_%28Encrypted%29/
    publisher: Quad9
authors:
  - anoni-net
---

Mullvad published two notices in September that affect how its users set up their devices. The first concerns a newly disclosed Android flaw: any app, with no special permission, can send some traffic outside the VPN tunnel even when "Block all connections without VPN" is on. The second: Mullvad's public encrypted DNS service shuts down on 2 November, so anyone who configured it by hand needs to switch.

The flaw abuses keep-alive packets. An app asks Android to create a keep-alive UDP connection that is offloaded to the Wi-Fi or cellular chip, and because the packets leave straight from the hardware they skip the VPN check. CyberInsider reports that the researcher demonstrated it on a Pixel 8 Pro running Android 16 and believes most Android 12 and newer devices are affected. The packets cannot carry arbitrary data, but they are enough to reveal the device's network identity outside the VPN. Google marked the report as a duplicate, with no fix or CVE before disclosure, and did not respond to CyberInsider's request for comment.

## Perspective {#perspective}

A VPN lockdown relies on the operating system checking that each connection goes through the tunnel. Here the packets are handed to the network chip and never pass that check. Mullvad's announcement says a fix from Google is unlikely and that Mullvad has no plans to ship a mitigation itself. Its advice sits at the source: install only apps you trust and, if possible, use a security-focused Android fork such as GrapheneOS. GrapheneOS has open pull requests that disable unprivileged hardware keep-alives, but as of 27 September they had not been merged or released. For people whose real IP must not leak, CyberInsider's report mentions placing the phone behind a router that enforces the VPN, with cellular and other paths turned off, which costs extra hardware when travelling.

Where you are in Asia changes what matters first. In mainland China, GreatFire's tests show mullvad.net blocked and the Quad9 DoH endpoint disrupted, with its page summarising access as unreliable, so reaching the service at all comes before tuning it. Elsewhere in the region, Mullvad VPN users are unaffected by the DNS change, since queries go to the resolver on the VPN server, and Mullvad Browser users on default settings move to Quad9 automatically. iOS and macOS DoH profiles from Mullvad will stop working.

Mullvad's help page also says that once you are connected to its VPN, a public encrypted DNS brings negligible security benefit and will always be slower than the resolver on the VPN server. Quad9's privacy policy says it does not collect or record users' IP addresses and is run by a Swiss foundation. The same policy says Quad9 keeps aggregate counters by region, carrier network and protocol. Those contain no individual IPs, but the DNS queries themselves still go to a single operator.

Anyone who set Mullvad's DoH by hand for use without the VPN needs to switch before 2 November; Quad9's DoH address is `https://dns.quad9.net/dns-query`. On iPhone and Mac, Quad9's setup guide provides a configuration profile to download, and on Android you enter `dns.quad9.net` under Private DNS. The guides are in English, French, Spanish and Romanian, with no Chinese version.
