---
title: SSH login interception through compromised Tor exit relays
description: In early October the settings of more than 300 Tor exit relays were altered so that SSH connections through them went to interception servers. According to The Hacker News, anyone who logged in to SSH over Tor with a password between 1 and 5 October after accepting an unfamiliar or changed host key should treat that password as stolen. The relays were gone from Tor's list of usable relays by 01:00 on 6 October Taipei time, and according to the person who found them, encrypted web traffic was passed on as usual.
date: 2026-10-29T00:00:00+08:00
slug: tor-exit-relay-ssh-interception
categories:
  - security
sources:
  - title: Security incident affecting some relay operators
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/WOHPLKCSHYXFTBRZXDENDKJZMBMPLMG5/
    publisher: Tor Project
    date: 2026-10-05
  - title: "Ebury 1.8.3 on two Quetzalcoatl relay servers: timeline, lessons, open questions"
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/QHRD6YOX6RZRDR7NCHNDO7GLCEA6VFM6/
    publisher: tor-relays
    date: 2026-10-07
  - title: "Re: Ebury 1.8.3 on two Quetzalcoatl relay servers: timeline, lessons, open questions"
    url: https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/message/Z2B6XYKJZBBQADU77MSNL6FJP7MHZHIV/
    publisher: tor-relays
    date: 2026-10-09
  - title: How I got over 300 Tor exit nodes removed
    url: https://kaba.cx/posts/20261020_Tor/
    publisher: kaba.cx
    date: 2026-10-20
  - title: Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections
    url: https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
    publisher: The Hacker News
    date: 2026-10-21
  - title: How to bypass censorship and connect to Tor from different countries or regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: "Ebury is alive but unseen: 400k Linux servers compromised for cryptotheft and financial gain"
    url: https://www.welivesecurity.com/en/eset-research/ebury-alive-unseen-400k-linux-servers-compromised-cryptotheft-financial-gain/
    publisher: ESET
    date: 2024-05-14
  - title: ssh(1) - OpenBSD manual pages
    url: https://man.openbsd.org/ssh
    publisher: OpenBSD
  - title: ssh_config(5) - OpenBSD manual pages
    url: https://man.openbsd.org/ssh_config
    publisher: OpenBSD
  - title: Tor relays in Singapore
    url: https://anoni.net/projects/pulse/sg/
    publisher: anoni.net
authors:
  - anoni-net
---

In early October 2026 the settings of more than 300 Tor exit relays (the last hop, which carries Tor traffic to its destination) were altered, and SSH connections (the protocol used to log in to and manage servers remotely) passing through them were sent to interception servers. Users who accepted a fake host key (the key a server uses to prove its identity) and typed a password had it captured. People logging in over SSH through Tor were affected, and people fetching mail over unencrypted connections through Tor may have been too. The relays were gone from Tor's list of usable relays by 01:00 on 6 October Taipei time, and according to the person who found them, encrypted web traffic was passed on as usual.

The finder, a user connecting to SSH over Tor, saw a changed-host-key warning on 2 October. They then scanned all of the roughly 3,000 exits and found 333 that either presented a fake host key or forwarded connections to interception servers, and reported it to the Tor Project that night. Around a dozen presented a fake host key themselves, and over 300 forwarded SSH to the same 12 interception servers.

According to the finder's write-up, once a user went on to log in, the interception server took the password and relayed the session to the real server, so every command typed passed through it. It then logged in to the server the user had meant to reach with the same password and tried to install Ebury, a backdoor that lets attackers log in again later; the finder did not see the installation complete. Ebury sits inside OpenSSH, the server's SSH software, and records the credentials typed at login. ESET's 2024 report counts about 400,000 servers compromised since 2009.

The Tor Network Health team, which monitors the network, posted a notice at 17:50 UTC on 5 October (01:50 on 6 October Taipei time) saying the attacker had gained access to Linux hosts and edited Tor's configuration, even turning non-exits into exits. From the evening of 4 October UTC (early on 5 October Taipei time), the Tor directory authorities (the servers that publish the list of usable relays, known as the consensus) began flagging the affected relays as unusable as exits.

A relay operator comparing public directory data found 377 relays from 59 operators that adopted the same exit policy, the setting that says which ports a relay will connect to, between 1 and 4 October. The analyst notes that this is a settings match and proves neither that every host was compromised nor that every relay intercepted SSH. At the peak these relays held about 7% of usable exit weight (the share of traffic the directory assigns each exit), and since clients pick exits roughly by weight, we estimate a Tor connection had about a 7% chance of using one.

277 of them belonged to one relay family (a set of relays one operator declares together). The family's operator wrote in a post-mortem that server logins, admin rights (sudo) and backups shared one password, and that the management server accepted password logins. How the attackers first got that password is not known. Ebury was found on the two servers the operator examined, and the public data does not show whether other affected hosts carry it.

## Perspective {#perspective}

Tor only encrypts traffic inside its own network, so an exit relay can read what is sent to the destination. HTTPS and SSH carry their own encryption and authentication; unencrypted mail protocols do not.

SSH uses the host key to confirm that the server is the real one. Per the OpenSSH manual pages, when a host key changes `ssh` shows a warning, disables password authentication and, under the default settings, refuses to connect. A password prompt only appears after the user deletes the old key record themselves. A server contacted for the first time has no record to compare against, so the user only sees the usual prompt, and accepting it means accepting the interception server's key.

The Hacker News infers from the SSH specification that only password logins had credentials taken. With a key login (proving identity with a private key on your own computer, without sending a password to the server), each proof is valid only for that session, so the interceptor cannot reuse it against the real server. The report also notes that the interceptor could still accept a key login and show a fake command line. Our inference is that a sudo or other admin password typed there could leak too.

The Hacker News advises anyone who logged in with a password over Tor between 1 and 5 October after accepting an unfamiliar or changed host key to treat that password as stolen. The family's servers had unexplained hidden processes from 30 September, and the operator cannot tell whether those were intercepting SSH too, so earlier logins cannot be ruled out.

The family's operator warns that Ebury records any password typed on an infected server. Checks should be done with a key login or by booting a rescue system, a maintenance environment that does not start the original system.

Other services that used the exposed password can be changed first, and the server that was logged in to after it has been checked. ESET's detection script runs on the server's command line, and only the update merged on 9 October detects this Ebury version; a clean result is no guarantee.

For future administration over Tor, the finder recommends key-based logins. On first connection, the host key fingerprint (a string identifying the key, shown when connecting) can be checked against one obtained from the administrator.

Another option is running SSH as an onion service (a service reachable only through Tor, whose connections never leave the Tor network), which avoids exit relays and so cannot be intercepted by one. The cost is that a private key has to be kept safe and set up again after changing or losing a computer. An onion service needs tor running on the server, one more step than exposing SSH directly.

According to the analyst, most affected relays closed the encrypted mail ports and left the unencrypted ones open, so mail fetched through them travelled in plaintext. No source confirms that mail was actually read, but anyone fetching mail over Tor should still check that their client uses an encrypted connection.

Tor relays are run by volunteers and anyone can join, so finding compromised or malicious relays relies on the Network Health team's scans and user reports. From the finder's report on 2 October to the last affected relay leaving the consensus at 17:00 UTC on 5 October took about three days.

Clients choose exits without regard to where the user is, so a relay's country says nothing about whether a reader was exposed. We, a community based in Taiwan, matched the 377 relays against geolocation data: none was in Taiwan, Japan, South Korea or Hong Kong, while Singapore had 24, all from the one family (geolocation data may contain errors). Our Tor relay dashboard shows exits in Singapore falling from 34 on 3 October to 9 on 4 October (daily snapshots in UTC), which we take to be the flagging. From 3 to 5 October Taiwan had two or three exits, Japan two or three, South Korea two and Hong Kong seven, none of them affected.

For mainland China, the Tor Project's support page recommends letting Tor Browser's Connection Assist try bridges or Snowflake first, then WebTunnel bridges, since direct connections to Tor are blocked in some countries. A bridge replaces only the first hop, and traffic still leaves through an exit relay, so the same advice applies to anyone connecting through one.

People who only use Tor Browser to visit HTTPS sites, and do not use SSH or fetch mail over Tor, need not change anything. As of 24 October we had found no explanation on the Tor Project's blog, status page or mailing lists of why the other 58 operators' relays adopted the same policy. ESET's Ebury researcher wrote on the relay operators' mailing list that there are most likely other compromised relays still unnoticed. Around 25 November is a good time to check whether the Tor Project has published how these relays were compromised, or found any more.
