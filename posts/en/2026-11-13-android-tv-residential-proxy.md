---
title: Preloaded backdoors and residential proxies on home Android TV boxes
description: People with an Android TV box at home may be affected. In early November Google announced the takedown of XCPE, a backdoor preloaded on more than 1.3 million set-top boxes, certified models included, that used them to relay other people's traffic. As of 8 November, Google had published no removal steps for devices already sold, and advice on replacing a box differs from Singapore police guidance.
date: 2026-11-13T00:00:00+08:00
slug: android-tv-residential-proxy
categories:
  - security
sources:
  - title: Shutting the Door on the XCPE Botnet
    url: https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet/
    publisher: Google Threat Intelligence Group
    date: 2026-11-02
  - title: Check & fix Play Protect certification status
    url: https://support.google.com/android/answer/10248227
    publisher: Google
  - title: Certified - Partners | Android
    url: https://www.android.com/certified/partners/
    publisher: Google
  - title: The Internals of a Badbox Operation
    url: https://github.com/synthient/public-research/blob/main/2026/11/Videostrong/README.md
    publisher: Synthient
  - title: Google dismantles botnet secretly running on 1.3 million Android TV boxes
    url: https://arstechnica.com/google/2026/11/google-dismantles-botnet-secretly-running-on-1-3-million-android-tv-boxes/
    publisher: Ars Technica
    date: 2026-11-03
  - title: Google Takes Down Massive Android Botnet Infecting 1.3 Million Devices
    url: https://www.channelnews.com.au/google-takes-down-massive-android-botnet-infecting-1-3-million-devices/
    publisher: ChannelNews
    date: 2026-11-03
  - title: Google dismantles massive botnet hidden in Android TV boxes
    url: https://therecord.media/google-dismantles-botnet-hidden-android-tv-boxes
    publisher: The Record
    date: 2026-11-03
  - title: Cops bust botnet of 1.3M infected Android TV boxes
    url: https://www.theregister.com/a/5307045
    publisher: The Register
    date: 2026-11-02
  - title: TrendAI helps disrupt X.CPE botnet in 1.3m devices
    url: https://itbrief.com.au/story/trendai-helps-disrupt-x-cpe-botnet-in-1-3m-devices
    publisher: IT Brief Australia
    date: 2026-11-05
  - title: Advisory On The Dangers Of Non-Certified Streaming Devices
    url: https://www.police.gov.sg/media-hub/news/2025/11/20251112_advisory_on_the_dangers_of_non_certified_streaming_devices
    publisher: Singapore Police Force
    date: 2025-11-12
  - title: 北角深水埗兩店售侵權機頂盒 標榜永久免費收看 海關拘2人
    url: https://www.stheadline.com/breaking-news/3468064/
    publisher: Sing Tao Headline
    date: 2025-06-26
authors:
  - anoni-net
---

A home internet connection may be getting rented out to strangers through the Android TV box plugged into the television. In early November, Google Threat Intelligence Group (GTIG) reported that Google and industry partners had, the week before, dismantled the XCPE botnet (a large set of devices remotely controlled by one party), into which the XCPE backdoor had enrolled more than 1.3 million set-top boxes. The overwhelming majority of the infected devices are Android TV boxes, along with some telehealth devices, karaoke machines and digital signage, spread around the world. Readers with an Android TV box at home, especially one of unknown origin, can start by checking the model list and certification status, although neither can confirm an infection on its own.

A residential proxy sends a paying customer's traffic out through an ordinary household's connection, so the destination records that household's IP address as the source. According to GTIG's analysis, the modules XCPE loaded were most often tied to residential proxies and bandwidth sharing, with some ad fraud modules as well. As many as three proxy software development kits (SDKs) were installed on a single device. The devices' owners neither knew nor agreed.

According to IT Brief's report on analysis by the security company TrendAI, malicious traffic passed through ordinary home and office IP addresses, so attackers appeared as local users when accessing online services. Because the traffic came from real household connections, it could get past the IP reputation and geolocation checks that banks and retailers use to verify users. As of 8 November, the official documents we found did not address whether a home IP had been blocked or investigated as a result, or whether its owner could face legal liability.

GTIG describes the backdoor as a package named `x.cpe` (`com.oemservice` in some builds), preloaded in firmware with system privileges. If a user uninstalls it, it reinstalls from the `/oem/` partition on reboot. It wipes the device's user consent settings and disables app verification in Google Play Protect (Android's built-in defense against malicious apps), then silently downloads and runs other files. GTIG found the same backdoor in the firmware of many brands and models over multiple years.

GTIG also recorded the operators capturing live screenshots, injecting keystrokes, exfiltrating account and device information and opening remote shells, and the command list includes a function for probing the local network. According to the same report, most interactions with infected devices were about installing, removing and configuring modules.

GTIG assesses with high confidence that the Android device manufacturer Videostrong deliberately developed, deployed and operated the XCPE backdoor and botnet for profit, then sold access to criminal affiliates. Videostrong had not replied to inquiries from The Record or The Register when those outlets published. Ars Technica reported that the affected models include Google-certified ones. GTIG's explanation is that Videostrong used obfuscation to exploit a gap in Google's tests, loading the malicious code after the device's first boot.

The 1.3 million figure is GTIG's count for the XCPE backdoor itself. GTIG separately estimates that taking down the command-and-control (C2, the servers that issue remote instructions) domains of the affiliates' modules will cut off access to at least 10 million more infected devices. The affiliates distribute their malware through channels beyond XCPE, so those 10 million are in addition to the 1.3 million. The Record reported that many of them are not Android devices.

Google's response included legal action to take down domains used by Videostrong and more than a dozen malware families, and a ban on Videostrong and its future subsidiaries and affiliates building or selling certified Android devices or supplying software to certified vendors. Google's report also says the company is improving firmware integrity checks on certified Android TV devices. As of 8 November, neither that report nor any other official statement we found offered removal steps for devices already sold, or said whether certification would be revoked for the affected models. According to The Record, Google also did not explain whether users would be notified or the malware forcibly removed.

## Perspective {#perspective}

To check certification status, open the Google Play Store's profile menu, then go to Settings and About. We did not test this on a TV box, and the screens may differ from the help page. According to that page, non-certified devices may not be secure, and device certification is separate from Play Protect, which guards against harmful apps. A certified status does not rule out a problem either, since XCPE's affected models include certified ones and the malicious code loaded after first boot.

Synthient, one of GTIG's partners, published 182 model names observed in this case, with a note that a model name alone is not sufficient to confirm compromise. Ars Technica recommended that anyone who bought a MECOOL box, or a white-label Android TV box of unknown origin, check the list. GTIG's report lists no symptoms users can see, and IT Brief's report mentions that a box may appear to work normally. As of 8 November, we had found no method for an ordinary user to confirm whether their home IP is being rented out.

Researchers cited by ChannelNews (the report does not say which firm) recommend disconnecting a confirmed infected device and replacing it, because `x.cpe` is embedded in system firmware and antivirus tools and factory resets may not permanently remove it. That means paying for a new box, and confirming an infection first is not easy. For anyone replacing a box, GTIG recommends buying from reputable manufacturers and points to the partner list on the Android TV website. The linked certified partners page is headed with phones and tablets, and as of 8 November we had not established whether TV boxes are fully listed there.

Singapore's police and Cyber Security Agency issued an advisory in November 2025, ahead of GTIG's disclosure, covering non-certified TV boxes. It advises disconnecting from the internet immediately, scanning for and uninstalling suspicious apps, and checking bank and other accounts. Anyone who finds malware or unauthorized transactions is told to file a report with Singapore police and not to factory-reset the device first, as that could hinder investigations.

The advisory also allows continued use or a full factory reset when no malware or unauthorized transactions turn up, but it was not written for XCPE. GTIG states that users cannot remove `x.cpe`, and ChannelNews reports that antivirus tools and factory resets may not permanently clear it, so our inference is that a clean scan does not show that `x.cpe` is absent.

According to The Record, the head of GTIG's disruption operations, asked about removing the malware, replied that taking down the domains severed the botnet's communications, "effectively rendering the malware benign." Ars Technica's assessment is that the devices should be safe to use, but Play Protect remains disabled and the inactive modules are still installed in the system. According to GTIG's report, operators who are disrupted quickly move to new loaders or other monetization SDKs. Researchers cited by ChannelNews also warn that criminals could set up replacement systems, leaving infected devices open to further abuse.

A home IP can also be rented out through apps people install themselves. GTIG urges extra caution with apps that offer payment for "unused bandwidth" or "sharing your internet," and its report lists them as primary ways for illicit proxy networks to grow. According to GTIG's analysis, proxy operators generally seek consent only when platform policy requires it, and as of 8 November the materials we found included no response from the proxy operators named in the report.

Among the official action on TV boxes we could find in Asia, Singapore's 2025 advisory tells people to use official streaming services or buy certified devices from reputable brands, which on our reading would not by itself have protected against XCPE, since its affected models include certified ones. The Hong Kong news outlet Sing Tao Headline reported in June 2025 that the Customs and Excise Department, in operations on 11 and 25 June against suspected illegal streaming devices, arrested two men on suspicion of breaching the Copyright Ordinance and seized 99 set-top boxes from more than 10 brands along with specific apps. According to that report, customs officers found trojans and spyware in some of the apps and warned that connecting such boxes to a home network would endanger personal privacy and could affect other connected devices. Those findings concern apps, while GTIG found XCPE preloaded in firmware.

Japan's National Police Agency is among the partners GTIG names in the XCPE operation, though we found no notice of the agency's own. As of 8 November we also found no XCPE notice from the computer emergency response teams TWCERT/CC in Taiwan or HKCERT in Hong Kong.

If a TV box's model is on the list, its origin is unknown or it shows as non-certified, the first step is to cut its network connection (both the replacement advice and the Singapore advice begin there), which takes a few minutes. Singapore's advisory tells anyone who believes an account may be compromised to change the password immediately and turn on multi-factor authentication, and we suggest doing that from a different device. GTIG recommends making sure Play Protect is active, which people keeping the device for now can check. According to Ars Technica the backdoor disables Play Protect, and the sources do not say whether it would be turned off again after being re-enabled manually.

Anyone still using the box for now can connect it to the router's guest network, apart from phones and computers, and confirm that the guest network isolates local devices. ChannelNews reported that attackers could investigate other devices on the same home network, and the guest network is our inference from that. Isolation appears in the sources only for businesses, with no assessment of home guest networks, and a guest network does not stop operators from capturing screens, exfiltrating account information or relaying traffic on the box. Disconnecting stops the relaying but cannot recover account information that may already have left, and replacing the box costs the price of a new one.
