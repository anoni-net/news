---
title: OpenSSH login bypass with long passwords on musl systems
description: OpenSSH released 10.6p2 on 5 November, fixing a flaw that let an overly long password log in to accounts with no password set. Only sshd on Linux built with musl libc and not using PAM to check passwords is in scope, Alpine Linux being one example. According to the OpenSSH maintainer and HKCERT, glibc systems such as Debian, Ubuntu and Red Hat are not in scope, though as of 8 November the Debian and Ubuntu trackers had not marked them unaffected. Anyone running sshd on Alpine should update or turn off password logins.
date: 2026-11-09T00:00:00+08:00
slug: openssh-sshole
categories:
  - security
sources:
  - title: OpenSSH Release Notes
    url: https://www.openssh.com/releasenotes.html#10.6p2
    publisher: OpenSSH
    date: 2026-11-05
  - title: "Security advisory: openssh-server password authentication bypass"
    url: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
    publisher: Alpine Linux
    date: 2026-11-05
  - title: "\"sshole\": password authentication bypass: OpenSSH + musl libc"
    url: https://www.openwall.com/lists/oss-security/2026/11/05/3
    publisher: oss-security
    date: 2026-11-05
  - title: OpenSSH 10.6p2 has been released with a workaround for a critical vulnerability
    url: https://hachyderm.io/@damienmiller/117563026759098135
    publisher: Hachyderm.io
    date: 2026-11-05
  - title: "*sshole"
    url: https://sshhole.com
    publisher: sshhole.com
  - title: Meet *sshole, the vulnerability that lets hackers SSH into Linux devices
    url: https://arstechnica.com/security/2026/11/vulnerability-allows-attackers-to-log-into-some-linux-devices-sans-password/
    publisher: Ars Technica
    date: 2026-11-05
  - title: OpenSSH發布緊急更新，修補可利用長密碼繞過身分驗證的資安漏洞SSHole
    url: https://www.ithome.com.tw/news/180281
    publisher: iThome
    date: 2026-11-06
  - title: CVE-2026-123158
    url: https://access.redhat.com/security/cve/CVE-2026-123158
    publisher: Red Hat
  - title: CVE-2026-123158
    url: https://security-tracker.debian.org/tracker/CVE-2026-123158
    publisher: Debian
  - title: CVE-2026-123158
    url: https://ubuntu.com/security/CVE-2026-123158
    publisher: Ubuntu
    date: 2026-11-06
  - title: OpenSSH Security Restriction Bypass Vulnerability
    url: https://www.hkcert.org/security-bulletin/openssh-multiple-vulnerabilities_20261106
    publisher: HKCERT
    date: 2026-11-06
  - title: 漏洞警訊公告 (Vulnerability alerts)
    url: https://www.twcert.org.tw/tw/lp-169-1.html
    publisher: TWCERT/CC
  - title: JPCERT Coordination Center
    url: https://www.jpcert.or.jp/english/
    publisher: JPCERT/CC
  - title: Japan Vulnerability Notes
    url: https://jvn.jp/en/
    publisher: JVN
  - title: PHP 存在2個重大資安漏洞(CVE-2026-109618 和 CVE-2026-109619)
    url: https://www.twcert.org.tw/tw/cp-169-11303-1d68a-1.html
    publisher: TWCERT/CC
    date: 2026-10-22
  - title: "JVNVU#99905564: PHPにおける複数の任意のコードが実行可能な脆弱性（CVE-2026-109618、CVE-2026-109619）"
    url: https://jvn.jp/vu/JVNVU99905564/
    publisher: JVN
    date: 2026-10-22
authors:
  - anoni-net
---

OpenSSH released 10.6p2 on 5 November, fixing a flaw that let anyone log in to an account with no password set by sending an extremely long password, a flaw its discoverer named \*sshole. The scope is narrow: only sshd (the OpenSSH server) on Linux is affected, and only where it is built with musl libc (a C standard library, the layer programs go through to call system functions) and does not check passwords through PAM (the Linux module that handles login authentication). According to a Mastodon post by an OpenSSH maintainer and to statements from the Hong Kong Computer Emergency Response Team Coordination Centre (HKCERT) and Red Hat, glibc systems such as Debian, Ubuntu and Red Hat are not in scope. The machines to check are those running sshd on Alpine Linux, a distribution widely used to build container images, and other systems that use musl and have OpenSSH installed, such as some embedded devices.

Alpine's security advisory lists four conditions that must all hold. sshd is Alpine's default `openssh-server` package, which has no PAM, or the PAM-enabled build set to `UsePAM no`. Password login is left on, which is the OpenSSH default. The machine has an account whose password field is `*` (common for accounts that log in only with keys and have no password set), and at least one other account with a password.

When the conditions are met, an attacker who knows the name of that `*` account can log in by sending any password between 257 and 1,024 bytes long. According to the advisory, it takes one connection and works every time.

According to the same advisory, without PAM sshd runs the received password through `crypt()` to produce a hash and compares it with the account's password field. When the field is too short to hold a salt (a random value mixed into the password before hashing), sshd borrows the salt from another account. Given a password longer than 256 bytes, musl's `crypt()` returns the string `*` as an error marker, which is identical to the field of an account with no password, so the comparison matches. According to the report on the oss-security mailing list, the fix checks for a minimum hash length and no longer accepts `*`.

The researcher's explainer traces the cause to separate changes in three projects. In 2012 musl capped passwords at 256 bytes to stop overly long ones from slowing servers down. In 2016 OpenSSH started borrowing other accounts' salts so attackers could not tell from response times whether an account exists, and around Alpine 3.16 in 2022 Alpine changed root's password field to `*`. The explainer notes that OpenSSH tests on OpenBSD and glibc, musl does not test sshd, and most distributions go through PAM.

According to Alpine's advisory, OpenSSH's default `PermitRootLogin prohibit-password` stops root from logging in with a password. That setting does not help if another account that can log in is able to gain root through doas (a privilege tool similar to sudo). Older official cloud images include an `alpine` account whose password field is `*` and which can use doas without a password. The advisory says these images are safe on first boot but become exploitable once an administrator sets a password for any account, such as a console login password.

The OpenSSH release notes say the team considers the root cause to lie outside sshd, though it can be avoided in sshd. According to Ars Technica, a musl developer takes the position that the problem is the caller's misuse and that musl itself has no bug. He also said musl plans to change the mechanism in a later release.

The flaw was later assigned CVE-2026-123158 (CVE being the shared numbering for public vulnerabilities), with a severity score (CVSS, out of 10) of 8.1. As of 8 November, none of OpenSSH, Alpine, Ars Technica or iThome had mentioned any case of the flaw being exploited, while HKCERT's bulletin says a public PoC (code demonstrating that the flaw can be exploited) is available. Ars Technica cites security firm Detectify as saying Shodan, a search engine that scans devices across the internet, lists around 22 million systems with SSH open on port 22. Ars assesses that only a fraction meet the conditions, but testing each one is quick and easy, so finding vulnerable devices would take little effort.

## Perspective {#perspective}

Red Hat's page says its products are not affected, because the OpenSSH in them links against glibc and uses PAM by default. As of 8 November, Debian's tracker marked OpenSSH in bookworm and trixie as vulnerable with an urgency of unimportant, and Ubuntu's page said "Needs evaluation". Debian's table gives `1:10.6p2-1` in sid as the fixed version and marks every earlier version vulnerable, from which we infer that the labels follow version numbers. The unimportant urgency is also consistent with HKCERT and the OpenSSH maintainer saying glibc systems are unaffected.

Ars reports that Alpine's base image on Docker Hub has been downloaded more than a billion times, but according to Alpine's advisory, container users who do not run sshd inside the container are unaffected. Cloud images configured through cloud-init (the tool that applies settings when a cloud server first boots) to write `PasswordAuthentication no` are also out of scope.

According to Ars Technica, Alpine has long been used in routers, smart TVs and industrial controllers, many of which are hard to update. The researcher lists OpenWrt, Buildroot and Yocto as systems that use musl. Ars adds that OpenWrt's default SSH server is Dropbear, so it is in scope only if OpenSSH is installed separately. Ars also reports that the researcher said Buildroot and Yocto are affected, though this had not been confirmed as of 5 November.

A Raspberry Pi running Raspberry Pi OS is Debian-based and uses glibc, so we infer it is out of scope, while one running Alpine should be checked against Alpine's conditions. None of the sources we consulted say whether home NAS devices or routers are affected, and as of 8 November we had found no vendor advisories.

According to the maintainer's post, the OpenSSH team released the fix the day after learning of the problem. The reason given is that the team has recently seen several cases of AI agents quickly rediscovering known bugs, sometimes within hours. The team therefore considers long embargo periods a dangerous practice that mainly benefits attackers. The release notes add that the project will, for now, release fixes more often instead of holding them for the next planned release.

Among official bodies in Asia, HKCERT published a bulletin on 6 November rating the risk as medium, noting that a PoC is public and that mainstream distributions such as Red Hat, SUSE, Ubuntu and Debian use glibc and are unaffected. As of 8 November we found no OpenSSH item on the vulnerability alert list of Taiwan's TWCERT/CC (Taiwan Computer Emergency Response Team / Coordination Center), and none on the front pages of Japan's JPCERT/CC (Japan Computer Emergency Response Team Coordination Center) and its vulnerability database JVN (Japan Vulnerability Notes), though those front pages show only recent items. The sites of mainland China's vulnerability databases, CNVD and CNNVD, did not load for us, and we found no notice from a Chinese agency.

For comparison, the [PHP vulnerabilities we covered on 23 October](https://anoni.net/news/en/2026/10/php2shell-leaked-rce/), in a far more widely deployed product, drew alerts from TWCERT/CC and JVN on 22 October. None of the sources we consulted say which products sold in Taiwan, mainland China, Hong Kong or Japan run OpenSSH on musl, so owners of embedded devices there have no list to check against.

According to Alpine's advisory, anyone managing sshd on Alpine themselves should update the `openssh` package and restart sshd, since upgrading the package alone does not replace the running service. Fixed packages are available for every Alpine release from 3.16 onward, including releases no longer supported, and the advisory lists the versions and commands. The upstream fix is OpenSSH 10.6p2, but a system's fixed package may keep an older version number (Alpine's do), and the sources we consulted do not say how other systems should update.

If updating is not possible right away, password login can be turned off. According to the oss-security report, doing so avoids the flaw, at the cost of no longer being able to log in with a password. Alpine's advisory recommends confirming that key login works first and keeping the current session open until a new login has been tested.

The advisory also describes how to check afterwards: look in the login logs for `Accepted password` on an account with no password, and treat the machine as compromised if a login cannot be ruled out. People who run only Debian, Ubuntu or Red Hat systems do not need to change settings for this flaw, according to the maintainer and HKCERT. This is an inference from the glibc and PAM conditions; as of 8 November the Debian and Ubuntu trackers had not been updated to match.
