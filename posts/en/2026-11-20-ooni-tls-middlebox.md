---
title: The TLS Middlebox experiment in OONI Probe and a survey on data collection
description: On 10 November OONI announced a TLS Middlebox experiment in OONI Probe for locating censorship equipment, and at announcement the apps supported only its default mode. An advanced mode, which could let others estimate the city a user is in, is available only in the command-line version and only to users who opt in. OONI is also running a survey until 10 December on whether users would accept the collection of more geographic and network data. Readers who neither run Probe nor use OONI data are not affected.
date: 2026-11-20T00:00:00+08:00
slug: ooni-tls-middlebox
categories:
  - censorship
sources:
  - title: New OONI Probe TLS Middlebox Experiment
    url: https://ooni.org/post/2026-ooni-probe-tls-middlebox-experiment/
    publisher: OONI
    date: 2026-11-10
  - title: "Survey: Collecting Additional Geographic and Network-Level Data with OONI Probe"
    url: https://ooni.org/post/2026-tls-middlebox-survey/
    publisher: OONI
    date: 2026-11-10
  - title: OONI Data Policy
    url: https://ooni.org/about/data-policy/
    publisher: OONI
    date: 2026-10-22
  - title: "Risks: Things you should know before running OONI Probe"
    url: https://ooni.org/about/risks/
    publisher: OONI
  - title: TLS middlebox
    url: https://github.com/ooni/spec/blob/master/nettests/ts-037-tlsmiddlebox.md
    publisher: OONI
    date: 2026-10-22
  - title: Frequently Asked Questions (FAQ)
    url: https://ooni.org/support/faq/
    publisher: OONI
  - title: Investigating TLS blocking in India
    url: https://ooni.org/post/2020-tls-blocking-india/
    publisher: OONI, Centre for Internet & Society
    date: 2020-07-08
authors:
  - anoni-net
---

On 10 November OONI (Open Observatory of Network Interference) announced on its blog a new TLS Middlebox experiment in OONI Probe, designed to find where on the network path the equipment that intercepts encrypted (TLS) connections for censorship sits. OONI Probe is software for measuring website blocking that anyone can run on their own network, and its measurements are published as open data. The experiment ships in the command-line version (the one operated by typing commands in a terminal), v3.31.0, and in the mobile and desktop apps, v6.3.0. At announcement the apps supported only the default mode, while an advanced mode that collects more data was available only in the command-line version, and only to users who opt in.

On the same day OONI published a survey asking users whether they would accept OONI collecting more geographic and network-level data, and how useful such data would be to them. The experiment announcement says OONI wants community feedback before adding the advanced mode to the app, which is the version used by most Probe users worldwide. The survey is open until 10 December, and the survey announcement invites readers to pass it on to other Probe users and to people who use OONI measurements in their work. Readers who neither run Probe nor use OONI data do not need to do anything.

A middlebox is a network device sitting between the user and a website that inspects or interferes with traffic. OONI's test specification says the experiment detects devices that block connections based on the SNI (Server Name Indication), the website name sent in cleartext when a TLS connection is set up. According to the announcement, the experiment came out of a research project on transit censorship, where traffic that neither starts nor ends in a given network is blocked as it passes through that network.

In the steps the announcement describes, Probe first uses traceroute (a tool that lists the routers packets pass through along the way) to map the path to a target server. It then sends requests for a control domain and for a censored domain to the same server, making the requests expire at different points along the path. From this OONI can tell where censorship begins and find the network location of the censoring device. The same data can also help show whether the device is deployed close to the user or in another network, or even another country.

For each router on the path, the default mode records three things: the country of its IP address, the AS (autonomous system, a set of networks on the internet run by one operator or institution) it belongs to, and the AS's organisation name. The announcement's assessment is that the default mode brings no new risk beyond other Probe tests and OONI's risk documentation, since a third party cannot do any analysis that identifies a user from routers' countries and ASes alone. The cost is limited usefulness, because a censoring device can only be confirmed in a country or network when it sits deep inside it.

The advanced mode also records each router's IP address and the round-trip time (RTT) for packets to reach each router and come back. The announcement says this exposes users to more risk than existing Probe tests. A third party could use the routers' timing and location to triangulate the city where Probe was run, and could work back from the path to the user's /24 prefix (a block of 256 IP addresses sharing the first three numbers). In the worst case, if only one IP address in that block was in use at the time, the user's IP address could be found as well.

The announcement also describes a more realistic scenario, in which a third party can estimate the user's city and network but would find it hard to single out a specific person. OONI's reasoning is that a network has many live IP addresses and many people in the same city run the test. Because of these risks the advanced mode is opt-in only. In return, it can locate a censoring device even when it sits on the boundary between two countries or two networks, and it allows censorship to be measured city by city, which the announcement says the OONI community has long asked for.

## Perspective {#perspective}

OONI's data policy says OONI does not aim to collect users' IP addresses and takes steps to remove them from its measurement database. The router IP addresses and round-trip times that the advanced mode publishes are the research data OONI wants, and also the data a third party would use to work out where a user is. Our assessment is that the research value and the degree of exposure cannot be adjusted separately.

Another principle in the data policy is that measurements sent to OONI's servers are published, and OONI does not, as a rule, delete measurements unless a user's safety is at stake. We infer that measurements from users who opt in to the advanced mode will stay in data anyone can download, for the long term, and could still be used later to estimate cities and address blocks.

The data policy also lists the user's country code and the ASN (AS number) of their network as fields attached to every measurement, and neither can be opted out of on its own. Running Probe carries risk in itself: OONI's FAQ says Probe is not a privacy tool, and anyone monitoring your internet activity (for example a government, an ISP or an employer) may see that you are running it. The risks page says the potential risks of running Probe depend on the user's threat model (who they might face and what that party can do) and on the laws of the country they are in.

For an Asian comparison, OONI and the Centre for Internet & Society (CIS) in India published a report in July 2020 on TLS blocking on three Indian ISPs, ACT Fibernet, Bharti Airtel and Reliance Jio. The report recorded SNI-based blocking on both Bharti Airtel and Reliance Jio, and found that Reliance Jio also blocked TLS traffic depending on the web server involved in the handshake. According to the report, state authorities order ISPs to block websites under Sections 69A and 79 of the Information Technology Act without giving technical specifications, so each ISP is free to adopt its own method, and regulations under Section 69A require ISPs to keep certain blocking orders confidential. The report cites a study based on OONI data that found website blocking in India "varies primarily from ISP to ISP, rather than from region to region".

The data in that report dates from 2020 and does not describe the situation today. We, a community based in Taiwan, found no OONI report dedicated to TLS middleboxes in Taiwan, Japan, Singapore, Hong Kong or South Korea (checked on 15 November).

As of the 10 November announcement, the apps do not have the advanced mode, and people running Probe through the app do not need to change any settings for it. Probe users with views on OONI collecting more data, and people who use OONI data in their work, can fill in the survey before 10 December. The survey is hosted on Google Forms, the link is in the survey announcement in the source list, and the announcement asks readers to spend a few minutes on it.

Where running Probe could itself draw attention, the risks page describes choosing which tests to run in the app. The data policy also mentions a setting in the app to stop sending measurements, which keeps results from being published. Drawing on the FAQ, we infer that neither step stops someone monitoring the network from seeing that Probe is running. For command-line users considering the advanced mode, the cost is that their city and address block may be estimated, and once measurements are published they are, as a rule, not deleted.
