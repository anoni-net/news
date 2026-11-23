---
title: HERMES and Mercury, open-source systems for sending email over shortwave radio
description: HERMES, built by the nonprofit Rhizomatica, lets communities without mobile signal or internet access exchange email and files over shortwave radio, and Mercury, a modem released in May, has made the whole system open source. Anyone within range can receive a radio signal, and the rules on encryption over amateur radio differ by country. As of 23 November, amateur radio operators in Taiwan may not communicate in code words or ciphers without the regulator's approval, and those in mainland China must communicate in plain language or recognised amateur abbreviations, using public protocols.
date: 2026-11-28T00:00:00+08:00
slug: hermes-hf-radio
categories:
  - civil-society
sources:
  - title: "Rhizomatica’s HERMES and Mercury Expand Open-Source HF Communications for Remote Communities While Appealing to Experimenters"
    url: https://www.ardc.net/rhizomaticas-hermes-and-mercury-expand-open-source-hf-communications-for-remote-communities-while-appealing-to-experimenters/
    publisher: ARDC
    date: 2026-11-06
  - title: "This Digital Radio Gets Messages to the World’s Remotest Locations"
    url: https://spectrum.ieee.org/hermes-shortwave-radio-digital-data
    publisher: IEEE Spectrum
    date: 2026-09-21
  - title: Mercury — The Open-Source HF Modem
    url: https://mercury.hermes.radio/
    publisher: Rhizomatica
  - title: Rhizomatica/mercury
    url: https://github.com/Rhizomatica/mercury
    publisher: GitHub
  - title: Introduction
    url: https://rhizomatica.github.io/hermes-documentation/manual_en_complete/node22.html
    publisher: HERMES manual
  - title: "Further and Safer: Reviving HF Radio in the Digital Age"
    url: https://pitg.gitlab.io/news/techdive/2025/07/19/hermes-hf-radio-communication.html
    publisher: Public Interest Technology Group
    date: 2025-07-19
  - title: The First Social Network
    url: https://www.newyorker.com/magazine/2026/10/19/the-first-social-network
    publisher: The New Yorker
    date: 2026-10-12
  - title: 業餘無線電人員及電臺管理辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060145
    publisher: Laws & Regulations Database of Taiwan
  - title: 业余无线电台管理办法（工业和信息化部令第 67 号）
    url: https://www.waizi.org.cn/doc/227732.html
    publisher: waizi.org.cn (republished)
authors:
  - anoni-net
---

Where there is no mobile signal or internet access, shortwave (HF) radio can carry a signal several hundred kilometres. Rhizomatica, a nonprofit working to bring communications to underserved communities, developed HERMES so that people without much radio or technical experience can send and receive messages, email and files over shortwave. In May, Rhizomatica released Mercury, an open-source modem (software that turns data into signals a radio can transmit). According to a write-up published on 6 November by ARDC, an amateur radio foundation that funds the project, Mercury replaces VARA, a proprietary modem that required a paid license for every radio, and with it the whole of HERMES is now open source.

Shortwave signals are reflected by the ionosphere in the upper atmosphere, so they can reach places where ground infrastructure is hard to build. In an interview with IEEE Spectrum, Rhizomatica's founder said they use small radios with an output of about 20 watts, and can link two radios 400 to 600 kilometres apart fairly reliably. The trade-off is speed. According to the same article, typical shortwave radios carry digital data at only a few hundred bits per second.

In an article on the Public Interest Technology Group website, the founder wrote that HERMES first compresses the data and then passes email along with UUCP, an early protocol designed to cope with interrupted connections. According to the project manual, a gateway station (the point where the shortwave network meets the internet) is usually set up somewhere with internet access, and each community with no other means of communication gets a remote station.

The largest HERMES deployment has nearly 90 radios, and according to ARDC's write-up some of the sites take days to reach on foot or by boat. Rhizomatica works with local partners and concentrates training on a small group of community members, with the aim that communities install, operate and maintain the system themselves. In the interview, the founder described a pilot project that put HERMES on 10 or 11 fishing boats, one of which broke down 100 or 200 kilometres offshore. He said the crew used HERMES to send their GPS position and a distress message, and both the crew and the boat were rescued.

According to ARDC, Mercury can also be used on its own, without HERMES, so amateur radio operators can connect it to their own radios. Some operators are already using it to exchange email, and have reported bugs and contributed changes.

## Perspective {#perspective}

Anyone with a receiver within range can pick up a radio signal, and on shortwave that range can stretch to hundreds of kilometres. In October The New Yorker reported on a rural tradition of passing private messages over AM radio stations, where the messages are often worded vaguely because anyone can hear what is broadcast.

In his Public Interest Technology Group article, the founder argues that with shortwave it is hard to tell where a signal is coming from, and harder still to know who is receiving it. He explained in the IEEE Spectrum interview that the rules on encryption for amateur radio differ by country, which is why encryption in HERMES can be switched on or off. The encryption was built in because some of Rhizomatica's partners are in very sensitive areas and do not want to send information that can easily be intercepted and used against them. The signal itself can still be recorded by anyone, though, and since Mercury's source code is public, whoever records it could in principle use the same software to recover any data that was not encrypted.

Amateur radio in Taiwan is governed by the Regulations Governing Amateur Radio Operators and Stations, issued by the National Communications Commission (NCC) in 2020. As of 23 November, the regulations prohibit amateur radio operators from communicating in code words or ciphers that the competent authority has not approved while operating an amateur station. Under this rule, HERMES cannot be used on Taiwan's amateur bands with encryption switched on unless approval has been obtained.

Mainland China's Measures for the Administration of Amateur Radio Stations (MIIT Order No. 67), issued by the Ministry of Industry and Information Technology and in force since 1 March 2024, limit amateur stations to communicating with one another, technical research and self-training, and bar their use for commercial gain. As of 23 November, the measures also require operators to communicate in plain language or in abbreviations and shorthand recognised in amateur radio, using public technical systems and communication protocols. Encrypted content is not plain language, so going by the republished text of the measures, switching on HERMES's encryption on mainland China's amateur bands may not meet this requirement, although the measures do not mention encryption by name.

Readers who can get online do not need this system. Licensed amateur radio operators who want to try HF data communication can start with Mercury. Its source code is on GitHub, the project page lists support for Linux (including Raspberry Pi) and Windows, and as of 23 November the latest release was v1.9.25, published on 21 November. Anyone trying it on amateur bands in Taiwan or mainland China should treat whatever they send as a public message that anyone within range can receive.
