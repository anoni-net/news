---
title: A static website hosted as a Tor onion service
description: Hosting an onion service needs no fixed IP address, domain name or open port, and tor plus an ordinary web server is enough to put a static site on the Tor network. tor shipped four security updates between June and October, three with fixes involving onion services, and as of 20 October the latest is 0.4.9.14. Visitors need to connect through Tor, for example with Tor Browser.
date: 2026-10-23T00:05:00+08:00
slug: tor-onion-service-static-site
categories:
  - censorship
sources:
  - title: Set up Your Onion Service
    url: https://community.torproject.org/onion-services/setup/
    publisher: Tor Project
  - title: How do Onion Services work?
    url: https://community.torproject.org/onion-services/overview/
    publisher: Tor Project
  - title: Operational Security
    url: https://community.torproject.org/onion-services/advanced/opsec/
    publisher: Tor Project
  - title: Client Authorization
    url: https://community.torproject.org/onion-services/advanced/client-auth/
    publisher: Tor Project
  - title: Onion-Location
    url: https://community.torproject.org/onion-services/advanced/onion-location/
    publisher: Tor Project
  - title: Onion Services Properties
    url: https://onionservices.torproject.org/technology/properties/
    publisher: Tor Project
  - title: Changes in version 0.4.9.14 - 2026-10-07
    url: https://gitlab.torproject.org/tpo/core/tor/-/raw/tor-0.4.9.14/ReleaseNotes
    publisher: Tor Project
    date: 2026-10-07
  - title: Onionspray
    url: https://onionservices.torproject.org/apps/web/onionspray/
    publisher: Tor Project
  - title: HTTPS for your Onion Service
    url: https://community.torproject.org/onion-services/advanced/https/
    publisher: Tor Project
  - title: Capability and Limitations
    url: https://arti.torproject.org/guides/capability-limitations/
    publisher: Tor Project
  - title: Arti
    url: https://gitlab.torproject.org/tpo/core/arti
    publisher: Tor Project
  - title: Best Practices for Hosting Onion Services
    url: https://riseup.net/en/security/network-security/tor/onionservices-best-practices
    publisher: Riseup
  - title: Self-Hosting on the Dark Web
    url: https://david.alvarezrosa.com/posts/self-hosting-on-the-dark-web/
    publisher: Personal blog
    date: 2026-06-01
  - title: How to bypass censorship and connect to Tor from different countries or regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: Users – Tor Metrics
    url: https://metrics.torproject.org/userstats-relay-country.html
    publisher: Tor Project
  - title: OONI API, Tor tests, mainland China
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=CN&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
  - title: OONI API, Tor tests, Hong Kong
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=HK&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
  - title: OONI API, Tor tests, Taiwan
    url: https://api.ooni.org/api/v1/aggregation?probe_cc=TW&test_name=tor&since=2026-09-18&until=2026-10-19
    publisher: OONI
authors:
  - anoni-net
---

In June, an author described on a personal blog how they put their static website on a Tor onion service (a site reachable only through Tor, with the server's location protected), using tor, the Tor Project's core program, and the nginx web server. According to the Tor Project's page on onion service properties, an onion service needs no fixed IP address, no domain name and no open port. Between 25 June and 7 October, tor shipped four security releases, 0.4.9.11 to 0.4.9.14, three of them with fixes involving onion services, and as of 20 October the latest is 0.4.9.14.

Anyone already running an onion service should update to the latest version. Visitors to such a site need to connect through Tor, for example with Tor Browser.

Following the post and the official setup guide, the operator names a directory for the keys and a local port to forward to in tor's configuration file, `torrc`. After tor restarts, the `hostname` file in that directory holds the site's .onion address. The web server listens only on the local machine, and according to the post Tor already encrypts the connection, so no separate TLS (the encryption behind HTTPS) is needed. Static site generators write the site's address into internal links, so the author builds a second copy based on the .onion address, which keeps visitors on the onion service from being sent back to the ordinary address.

The setup guide's further advice is to forward to a Unix socket (a channel that programs on the same computer use to exchange data) instead of a local network port, so the service does not leak onto the local network. The guide also warns that an onion service set up this way can be read by anyone who knows the address. To limit it to particular people, client authorization lets only those holding a private key connect. According to the Onion-Location page, operators of an existing HTTPS site can add that header so Tor Browser shows the .onion version in the address bar when someone opens the original site.

## Perspective {#perspective}

According to the official overview, an onion service's name is the public key used to authenticate the connection, so no certificate authority (the bodies that issue HTTPS certificates to websites) is needed. Tor encrypts the connection all the way from the user to the service. The service only makes outbound connections and can get through NAT (the mechanism home and organisational networks use to share one public IP address), so it can run on school or office networks where ports cannot be opened. According to the properties page, an onion service is reachable whenever the user can reach the Tor network and the service is online, regardless of DNS and IP blocking.

According to the official Operational Security page, whether the server's location stays hidden depends on how the operator maintains the system. A web server may reveal its software and operating system, and a computer that is not always online also leaks information. The longer a service runs, the higher the risk that its location is found. The same page recommends adding Vanguards (an add-on that reduces the risk of a service's entry relays being traced) to guard against advanced attacks.

The setup guide calls keeping a server from revealing its location "not an easy task" and lists the Operational Security page and Riseup's guide for reference. Riseup's guide recommends NTP (network time synchronisation) to keep the server clock correct, so clock drift cannot be used to identify the server. For people who have never run a web server, the setup guide suggests trying OnionShare, which has a graphical interface and fewer settings. The Tor Project's Onionspray adds an onion entrance to an existing public website, and its documentation lists that it is not suited to onion-only sites and does not protect the site's location.

The documentation for Arti, the Tor implementation rewritten in the Rust programming language, is inconsistent on whether it can host onion services. As of 20 October, Arti's project page says this is implemented, while its capability and limitations page says it is only partly done and off by default. The Onionspray documentation also says it relies on the C implementation of tor until Arti offers an alternative. Our inference from these documents is that tor is the safer choice for a production deployment.

Readers whose access to ordinary websites is blocked but who can still reach Tor can also read sites hosted as onion services. Our inference from the Operational Security page is that hosting one needs a machine that can stay on for long periods. The official examples mainly use Debian, the process is editing a configuration file on the command line with no programming required, and the guide has a Traditional Chinese translation (as of 20 October some sections are still in English).

Tor Metrics and OONI publish figures for mainland China, Taiwan and Hong Kong. Tor Metrics estimates, as daily averages for 11 to 17 October, about 1,055 users connecting directly from mainland China, against about 9,518 from Taiwan and about 8,253 from Hong Kong. These are estimates of direct connections only and leave out users who connect through bridges.

OONI (Open Observatory of Network Interference) Tor tests from 18 September to 18 October numbered 301 in mainland China, 293 of them flagged as anomalies and none confirmed as blocked. Hong Kong had 706 tests with 7 anomalies, and Taiwan 4,797 tests with 314 anomalies, 311 of them from a single ASN (autonomous system number, which identifies one network). An anomaly is not a confirmed block, and the test checks whether the servers Tor needs to operate are reachable, not onion services themselves.

For mainland China, the Tor Project's support page advises letting Tor Browser's Connection Assist try bridges or Snowflake automatically first, then WebTunnel bridges, then Snowflake and meek (meek has limited bandwidth and is slower). That page covers reaching the Tor network and does not say whether onion services are reachable from mainland China. As of 20 October we found no rules specifically on running onion services in mainland China, Taiwan or Hong Kong.

According to the properties page, a site can still record data about users once they log in. Our inference from the Operational Security page is that what the site's own content reveals is up to the operator.
