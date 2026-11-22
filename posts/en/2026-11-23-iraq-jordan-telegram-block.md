---
title: OONI measurements of the Telegram blocks in Iraq and Jordan
description: Iraq and Jordan announced blocks on Telegram on 16 November. In OONI Probe measurements, Telegram tests in both countries turned anomalous between 15 and 16 November (UTC) and were all still anomalous on 20 November. Both orders apply only to networks inside each country, and readers elsewhere are not affected by these blocks.
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
    publisher: Al-Monitor (via Reuters)
    date: 2026-11-17
  - title: Jordan and Iraq block Telegram over national security concerns
    url: https://www.aljazeera.com/news/2026/11/16/jordan-bans-telegram-messing-app-over-national-security-concerns
    publisher: Al Jazeera
    date: 2026-11-16
  - title: "OONI API aggregation: telegram, CN"
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=telegram&since=2026-08-22&until=2026-11-21
    publisher: OONI
  - title: "OONI API aggregation: telegram, TW"
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=TW&test_name=telegram&since=2026-08-22&until=2026-11-21
    publisher: OONI
  - title: "OONI API aggregation: telegram, HK"
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=HK&test_name=telegram&since=2026-08-22&until=2026-11-21
    publisher: OONI
  - title: Is https://telegram.org blocked in mainland China?
    url: https://en.greatfire.org/https/telegram.org
    publisher: GreatFire
regions:
  - IQ
  - JO
authors:
  - anoni-net
---

A government that announces a block does not always state when it takes effect or which networks it covers, and people outside can check both against measurements taken on local networks. On 16 November Iraq's Communications and Media Commission announced a nationwide block on Telegram on the Prime Minister's instructions, and Jordan's Public Security Directorate announced a block the same day. In measurements from OONI Probe, open-source software from OONI (Open Observatory of Network Interference) for measuring network censorship, Telegram tests in both countries turned anomalous between 15 and 16 November (UTC) and were all still anomalous on the 20th. Both orders apply only to networks inside each country, and readers elsewhere are not affected by these blocks.

According to the commission's announcement, Telegram had not dealt with unlawful content on the platform or met its obligations under Iraqi law, and the operating company has 30 days to regularise its legal status. In the statement as Kurdistan24 reported it, there is no mention of which channels or posts the decision rested on, what steps must be taken within the 30 days, or what happens once they are up. According to Al Jazeera, Jordan's Public Security Directorate gave curbing illegal and extremist content as the reason for its block. Reuters reported that Telegram denies Iraq's accusations, and in the statement Telegram gave Reuters, its efforts to combat terrorism are described as going beyond what the law requires.

OONI Probe is run by users on their own networks, its results are published, and its dates are counted in Coordinated Universal Time (UTC). Before the block Iraq had 67 to 80 Telegram tests a day, with almost no anomalies. On the 16th, 33 of 72 tests were anomalous, and from the 17th every test was. According to a 19 November post compiling both countries' measurements on net4people, a public forum for discussing internet censorship, WhatsApp and Signal tests in Iraq stayed at their usual level that same week.

Jordan has far fewer measurements, between 1 and 8 a day before the block, none of them anomalous. On the 15th, 7 of 13 were anomalous, and from the 16th all of them were. Since OONI counts days in UTC and Jordan's local time is three hours ahead, the last three hours of 15 November UTC already fell on the 16th in Jordan. From these figures it is not possible to tell whether the anomalies began before the announcement.

## Perspective {#perspective}

In OONI's Telegram test, Probe connects from the user's network to the servers the Telegram app uses, and also loads the web version at `web.telegram.org`. According to OONI's description of the test, Telegram is likely blocked when none of the app's servers can be reached or when the web version does not load properly. A measurement flagged as anomalous means its result matches one of these cases, and the reason the connection failed has to be worked out separately.

An AS (autonomous system) is a set of networks on the internet run by one operator or institution. Every measurement was anomalous on the 12 ASes in Iraq with data from 17 November onward, and on the 4 ASes in Jordan with data from the 16th onward. From these numbers it is not possible to tell what technique the blocks use or where in the network traffic is stopped. In general, the way traffic is intercepted affects whether other services are caught up as well.

The turning point is visible in both countries because normal daily measurements from before the blocks were already there to compare against. Measurements only cover networks where someone runs the test, and on networks like Jordan's, with single-digit tests a day, it is hard to pin down when the change happened. Anyone who wants to see the figures does not need to install anything, since OONI Explorer, OONI's public site for measurement results, can be searched by country and by the Telegram test.

Running Probe on your own network has a cost too. In OONI's FAQ, Probe is described as not a privacy tool, and anyone monitoring network activity (for example a government, an ISP or an employer) may be able to see that you are running it. On OONI's risks page, the potential risks of running Probe depend on the user's threat model (who they might face and what that party can do) and on the laws of the country they are in. On 20 November we covered choosing which tests to run in the app and not sending measurements, in [the TLS Middlebox experiment in OONI Probe and a survey on data collection](https://anoni.net/news/en/2026/11/ooni-tls-middlebox/), and that even with those settings someone may still be able to see that Probe is running.

Between 22 August and 21 November, 2,231 of the 2,324 OONI Telegram tests in mainland China (about 96%) were flagged as anomalous, a label for signs of possible interference that on its own does not establish a block. Over the same period Taiwan had 177 anomalies in 11,530 tests (about 1.5%) and Hong Kong 15 in 2,485 (about 0.6%), so most tests in both places came back normal. GreatFire, which tests whether web addresses can be reached from mainland China, has recorded interference with `telegram.org` since July 2015 and found the site 100% blocked in its last test, on 18 October, though that figure is for the website rather than the app's message connections. Because about 96% of the tests in mainland China over that period were already anomalous, our reading is that a new block there would not show up as a jump in the anomaly share, the way the blocks in Iraq and Jordan did against days of normal results.

Readers outside Iraq and Jordan do not need to change any settings. According to Reuters, Iraq also blocked Telegram in 2023 and restored the service a week later, after a government statement that the company had responded to the security authorities' requirements. Once the two countries announce that the blocks are lifted, OONI Explorer is also where to check whether the Telegram tests return to normal.
