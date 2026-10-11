---
title: Firefox 157's TLS key logging warning
description: Firefox 157 for desktop, released on 29 September, shows a warning when the computer is set up to record encryption keys. Mozilla's support page says antivirus or security software is the most likely cause and the warning does not mean the computer is infected. If sites fail to load, check that software's HTTPS scanning first.
date: 2026-10-12T00:00:00+08:00
slug: firefox-tls-keylog-warning
categories:
  - security
sources:
  - title: Firefox 157.0, See All New Features, Updates and Fixes
    url: https://www.firefox.com/en-US/firefox/157.0/releasenotes/
    publisher: Mozilla
    date: 2026-09-29
  - title: Troubleshoot network errors when TLS key logging is enabled
    url: https://support.mozilla.org/en-US/kb/sslkeylogfile-warning
    publisher: Mozilla
    date: 2026-06-25
  - title: Add a warning to about:neterror when SSLKEYLOGFILE is in use
    url: https://bugzilla.mozilla.org/show_bug.cgi?id=2035411
    publisher: Mozilla Bugzilla
    date: 2026-04-28
  - title: RFC 9850 - The SSLKEYLOGFILE Format for TLS
    url: https://www.rfc-editor.org/rfc/rfc9850.html
    publisher: RFC Editor
  - title: 关于 Firefox 在中国持续运营但北京火狐关闭及 Firefox 账户服务终止的重要公告
    url: https://web.archive.org/web/20250728090400/https://www.firefox.com.cn/farewell/
    publisher: 北京谋智火狐信息技术有限公司
    date: 2025-07-27
authors:
  - anoni-net
---

Firefox 157, released on 29 September, shows a warning in the site information panel (the shield icon in the address bar) and in Settings when the computer is set up to record its encryption keys. The release notes list the change for desktop only, and the Android and iOS release notes for 157 do not mention it. Mozilla's support page says the warning does not mean the computer is infected, and that antivirus or security software inspecting encrypted connections is the most likely cause. For developers, it may simply mean a debugging tool is running.

According to the support page, the trigger is the `SSLKEYLOGFILE` environment variable (a setting the operating system passes to programs), which makes Firefox save the keys for its HTTPS connections to a file. Software that can read that file may be able to decrypt and inspect HTTPS traffic, and depending on how it uses the keys, intercept connections, impersonate servers and modify data. Some network error pages also gain a "Your connection may not be private" banner linking to the same page. A Mozilla bug report filed in April 2026 says a number of antivirus products seem to use the variable to decrypt HTTPS traffic, sometimes breaking connections, and cites Mozilla usage data showing it on about 10% of Windows users' computers.

## Perspective {#perspective}

Each HTTPS connection negotiates its own keys, which normally stay only with the browser and the website's server. `SSLKEYLOGFILE` was meant for developers debugging their own traffic. Once the keys are written to a file, a program that can read the file and has captured the encrypted traffic may be able to decrypt those connections. RFC 9850, published by the IETF (the body that sets internet technical standards) in July 2026, documents the file format as an informational document and states that it is only for systems where TLS protects test data, never for production.

If you see the warning and sites fail to load, the support page suggests looking in your antivirus or security software for features such as "HTTPS scanning", "Encrypted traffic monitoring" or "Web protection", and temporarily turning them off if the software allows it to see whether the problem remains. While they are off, that software no longer inspects encrypted web content. The page also says that if you trust that software to see everything you do online, this is not necessarily cause for concern. You usually do not need to disable your antivirus, since Firefox has Safe Browsing built in, and whether an extra layer of HTTPS inspection is worth it is up to you.

As of 11 October, the support page has Traditional and Simplified Chinese versions, both marked at the top as unreviewed machine translations. In mainland China, the Beijing company that ran part of Firefox's local business announced on 27 July 2025 that it would end that work after 29 September 2025, and that Mozilla would continue it itself or through authorised third parties. The notice states that the browser itself remains available and updated, with downloads moved to Mozilla's firefox.com/download, and the 157 release notes list no regional limits, so the desktop release from there should carry the same warning.

If you have no such software and are not debugging network traffic, another program may have set the variable, or someone may have set it by hand. That is our inference from the causes the support page lists, and the page has no steps for this case. We suggest asking someone familiar with computers to check the system's environment variables.
