---
title: Compromised Tor exit relays used to intercept SSH logins
description: In early October 2026 the settings of more than 300 Tor exit relays were changed so that SSH connections through them went to interception servers, which captured passwords from users who accepted a fake host key. Encrypted web traffic was passed on as usual, and the relays were out of the Tor consensus by 01:00 on 6 October Taipei time. According to The Hacker News, anyone who logged in to SSH over Tor with a password between 1 and 5 October after accepting an unfamiliar or changed host key should treat that password as stolen.
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

In early October 2026 someone changed the settings of more than 300 Tor exit relays, the last hop that carries Tor traffic to its destination. SSH connections (the protocol used to log in to and manage servers remotely) passing through them were sent to interception servers, and users who accepted a fake host key and typed a password had it captured. A host key is the key a server uses to prove its identity.

People who logged in to servers over SSH through Tor were affected, and people fetching mail over unencrypted connections through Tor may have been too. According to kaba, who published the scan results, encrypted web traffic was passed on as usual, and the attackers were probably after unencrypted data, which kaba describes as speculation.

According to an analysis of public directory data, the Tor directory authorities began voting from 18:00 UTC on 4 October to flag the affected relays as unusable as exits, and the flags were in the consensus from 21:00 UTC (05:00 on 5 October Taipei time). From 17:00 UTC on 5 October (01:00 on 6 October Taipei time), no relay with the attackers' settings was listed in the consensus, so clients could no longer pick them.

kaba saw a changed-host-key warning while connecting to SSH over Tor on 2 October, scanned all of the roughly 3,000 exits and found 333 with problems: around a dozen presented a fake host key themselves, and over 300 forwarded SSH to the same 12 interception servers. He reported it to the Tor Project that night.

The Tor Network Health team posted a notice to relay operators on 5 October saying the attacker was gaining access to Linux hosts and editing Tor's configuration, even turning non-exits into exits, and that the team was investigating how the machines were compromised.

According to kaba, once a user ignored the warning and logged in, the interception server took the password and relayed the session to the real server, seeing every command typed. It then logged in to that server separately with the same password to install Ebury, an OpenSSH backdoor that steals login credentials; kaba's honeypot saw only the start of the installer before the other side disconnected. ESET's 2024 report puts Ebury at about 400,000 servers compromised since 2009.

A relay operator's analysis of public directory data counted 377 relays from 59 operators publishing the attackers' exit policy, the setting that says which ports a relay will connect to, between 1 and 4 October. At 01:00 UTC on 4 October, 351 of them held 7.46% of usable exit weight, and since clients pick exits roughly by weight, we estimate the chance of using one was about that. The analyst notes this is a policy match, not proof of compromise, and a different count from kaba's 333.

277 of the relays belonged to one family, whose operator wrote in a post-mortem that SSH login, sudo and backups shared one password and that the management server allowed password logins. How the attackers first obtained that password is not known. Ebury was confirmed on the two servers that family examined, and the public data does not show whether other affected hosts carry it. Why the other 58 operators' relays showed the same settings, and whether they were compromised, was still unknown as of 24 October, and there is no count of affected users.

## Perspective {#perspective}

Tor only encrypts traffic inside its own network, so an exit relay sees what is sent to the destination. Whether that traffic is encrypted, and whether the other end can be verified, depends on the protocol.

SSH uses the host key to confirm that the server is the real one. Per the OpenSSH manual pages, ssh warns and disables password authentication when a host key changes, and refuses to connect under the default settings, so users had to delete the old record or change their settings to get through. A server contacted for the first time has no record to compare against, and the user only sees the usual prompt, so accepting it means accepting the interception server's key.

The Hacker News infers from RFC 4252, the SSH authentication specification, that only password logins had credentials taken, because a key login's signature is bound to that session and cannot be replayed to the real server. The same report notes that the interceptor could still accept a key login and show a fake shell; our inference is that a sudo password typed there could leak too.

The report defines the exposure as password logins over Tor between 1 and 5 October after accepting an unfamiliar or changed host key, without a time zone. Neither the Tor notice nor kaba draws that line, and the family's post-mortem records unexplained hidden processes on its servers from 30 September, so the start date is only a guide.

The report advises anyone in that group to treat the password as stolen, and the server they logged in to may carry Ebury. The family's operator warns against typing any password on a server that may be compromised, because Ebury records it, and suggests checking with a key login or from a rescue system. Our suggestion is that other services sharing the password can be changed first, and that server only after the check. ESET's detection script picks up this Ebury version only from its 9 October update, and the script itself warns that a clean result is no guarantee.

For future administration over Tor, we suggest key-based logins and confirming the host key fingerprint with the administrator on first connection. Running SSH as an onion service (a service reachable only through Tor, whose connections never leave the Tor network) avoids exit relays altogether. According to the analyst, most affected relays closed the encrypted mail ports and left the plaintext ones open, so anyone reading mail over Tor should check that their client uses an encrypted connection.

Tor relays are run by volunteers and anyone can join, so detection relies on the Network Health team's scans and user reports. Flags appeared about two days after kaba's report, and it took nearly another day before no relay with the attackers' settings was in the consensus.

We, a community based in Taiwan, matched the 377 relay addresses against the IP geolocation database shipped with Tor. None was in Taiwan, Japan, South Korea or Hong Kong, while Singapore had 24, all from the one family; the database may contain errors. Our Tor relay dashboard shows exits in Singapore falling from 34 on 3 October to 9 on 4 October (daily snapshots in UTC), which we take to be the flagging.

From 3 to 5 October Taiwan had two or three exits, Japan two or three, South Korea two and Hong Kong seven, none of them affected. Clients choose exits without regard to where the user is, so a relay's country says nothing about whether a reader was exposed.

For mainland China, the Tor Project's support page recommends letting Tor Browser's Connection Assist try bridges or Snowflake first, then WebTunnel bridges, since direct connections to Tor are blocked in some countries. A bridge replaces only the first hop, and traffic still leaves through an exit relay, so the same advice applies to anyone connecting through one.

As of 24 October the Tor Project had not said how the other operators' relays were changed. An Ebury researcher wrote on the tor-relays list that there are most likely other compromised Tor relays still unnoticed. The Network Health team's findings, and any newly affected relays, are what to watch for next.
