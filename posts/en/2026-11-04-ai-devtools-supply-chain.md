---
title: A backdoored extension and malicious instruction files in AI coding tools
description: Windows and macOS users who installed or updated the Claude Code extension 2.1.312 or 2.1.313 from Cursor's own marketplace on 29 October, Pacific time, may have received a backdoored version. According to an Anthropic staff member, the versions on Anthropic's official channels are not affected. Separately, research published on 22 October documented a Markdown instruction file placed in a Downloads folder to lure Codex into installing a malicious package.
date: 2026-11-04T00:00:00+08:00
slug: ai-devtools-supply-chain
categories:
  - security
sources:
  - title: Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace
    url: https://cursor.com/blog/claude-code-extension-security-notice
    publisher: Cursor
    date: 2026-10-29
  - title: "Markdown Is the New Executable: Attackers Are Dropping Agent Instructions Into Your Downloads Folder From the Web"
    url: https://forever.security/blog/hijacking-ai-agents-via-downloads-folder/
    publisher: Forever Security
    date: 2026-10-22
  - title: Anthropic VS code extension on Cursor backdoored for nearly 12 hours
    url: https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/
    publisher: Ars Technica
    date: 2026-10-30
  - title: "Anthropic: That Claude Code extension compromise… couldn't be us"
    url: https://www.theregister.com/cyber-crime/2026/10/30/anthropic-that-claude-code-extension-compromise-couldnt-be-us/5306682
    publisher: The Register
    date: 2026-10-30
  - title: "Official Claude Code Extension Compromise: Security Advisory"
    url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
    publisher: Phorion
    date: 2026-10-30
  - title: Anthropic hacked to deliver remote access trojan to claude developer laptops worldwide
    url: https://doublepulsar.com/anthropic-hacked-to-deliver-remote-access-trojan-to-claude-developer-laptops-worldwide-1148a92baae2
    publisher: DoublePulsar
    date: 2026-10-30
  - title: AI coding agents fall for malicious instructions planted in the Downloads folder
    url: https://www.helpnetsecurity.com/2026/10/26/ai-coding-agents-malware-openai-codex/
    publisher: Help Net Security
    date: 2026-10-26
  - title: 惡意Markdown指引檔企圖誘使Codex安裝惡意套件，AI程式開發代理面臨攻擊風險
    url: https://www.ithome.com.tw/news/180033
    publisher: iThome
    date: 2026-10-30
  - title: Supported Regions Policy
    url: https://www.anthropic.com/supported-countries
    publisher: Anthropic
  - title: Regions
    url: https://cursor.com/docs/account/regions
    publisher: Cursor
authors:
  - anoni-net
---

On 29 October a tampered copy of the Claude Code extension (an add-on that installs into the editor and extends what it can do) sat in the extension marketplace run by Cursor, the AI code editor, for about 11 hours. According to Cursor's notice, the affected releases are the Windows and macOS builds of `Anthropic.claude-code` 2.1.312 and 2.1.313, and only people who installed or updated the extension from Cursor's marketplace during that window need to act. The Register quotes a post on X by an Anthropic technical staff member saying the versions on Anthropic's official channels are fine and that only Cursor users are affected. In a separate case published on 22 October, the security company Forever Security described a Markdown instruction file that turned up in a Downloads folder and tried to get Codex, OpenAI's coding agent, to install a malicious package.

According to Cursor's notice, the malicious version was available from 02:27 to 13:35 Pacific Daylight Time on 29 October, which is 09:27 to 20:35 UTC, or 17:27 on 29 October to 04:35 on 30 October in Taipei (UTC+8). Ars Technica cites Cursor as saying at most 5,000 users were affected. The chief technology officer of the security company Phorion told Ars that the malicious version was published from Anthropic's official account on the Cursor marketplace. He also said that Cursor updates extensions automatically by default, which users can change in settings.

When Cursor updated its notice on 30 October it listed two versions, 2.1.312 and 2.1.313, whereas Ars, The Register and Phorion all initially reported only 2.1.313. On 30 October Phorion corrected its reference to Open VSX (the open extension marketplace shared by editors derived from VS Code) to Cursor's marketplace, and on 31 October added 2.1.312 following Cursor's update. Phorion and Ars both report that the malicious code also contains Linux-specific parts, while Cursor lists only Windows and macOS as affected platforms. Ars quotes an independent security researcher as saying Anthropic released 2.1.314 several hours after the malicious version went up.

According to Cursor's notice and Phorion's analysis, the malicious code runs as soon as the extension loads, without the user ever opening it. It sends the attacker the computer name, user name, operating system, public IP address, the email address in the Git configuration and the names of environment variables (not their values). It also tries to add the attacker's SSH key (SSH being the protocol used to log in to a computer remotely), set up a reverse tunnel, and keep retrying in the background. Cursor's notice says enabling the SSH service requires administrator privileges, so on most macOS and Windows machines this step fails and the attacker cannot log in through the tunnel.

Even where the tunnel was never set up, the attacker's key and the persistence settings remain on the machine, and the machine's details have already been sent. Cursor worked with the hosting provider to take the attacker's server offline. The other steps listed in Cursor's notice were removing the malicious version, temporarily shutting down the whole marketplace, and auditing access logs to confirm that no other extensions had been tampered with. Cursor also rotated its keys, rebuilt the marketplace and brought it back online.

As of 2 November neither Cursor nor Anthropic had disclosed how the malicious version came to be published under Anthropic's verified account on Cursor's marketplace. The independent researcher quoted above titled a 30 October post "Anthropic hacked", and later added Anthropic's response, which places the problem with Cursor's marketplace, to the text. As quoted by The Register, the Anthropic staff member wrote that neither Anthropic's systems nor its employees' laptops had been compromised. He wrote that someone had used access to Cursor's marketplace to upload a tampered copy that Anthropic had neither built nor published.

In the Markdown case, Forever's post describes an `AGENTS.md` of about 13 KB, disguised as ordinary engineering guidelines, that appeared in the Downloads folder on a customer's computer. `AGENTS.md` is an instruction file that developers keep in a project folder for coding agents, which read it automatically and follow it. This one asked Codex to change its own machine-wide settings, register an MCP server chosen by the attacker (MCP, the Model Context Protocol, is the interface agents use to connect to outside tools), and then install the npm package `function-color`. Forever's own product stopped the package before it was installed, and according to Help Net Security, npm has since removed it.

According to Help Net Security, the researchers did not know how the file got into the Downloads folder when they found it. They wrote that a website can put a file in the Downloads folder without a click or any permission from the user. Codex only follows an `AGENTS.md` in a folder it trusts, and the Downloads folder counts as trusted once the user has worked there. Reproducing the full attack in an isolated environment, the researchers found that Codex ran the program the file told it to run in more than 90 percent of attempts (most tests used a harmless stand-in that only opens a calculator).

The researchers also wrote their own `CLAUDE.md` along the same lines to test Anthropic's Claude Code; this file was never found on a customer's computer. In about half of the tests, Claude Code changed its settings as the file instructed and pointed its API connection at the researchers' server. The researchers wrote that this leaks the login token, which can be captured and used to take over the account. Forever's post argues that there is nothing for OpenAI or Anthropic to patch, and as of 2 November we had found no public response to the research from either company.

## Perspective {#perspective}

The sources do not connect the two incidents, and we cover them together because both exploit files that developer tools load and trust automatically. Ars reports that Cursor extensions run with the editor's own permissions, so once installed one can very likely reach local files, source code and developer tools. Our inference is that a verified marketplace account combined with automatic updates by default left the publishing account as the only checkpoint between users and a malicious version. According to The Register and DoublePulsar, updating to 2.1.314 does not remove the persistence settings already installed.

The instruction-file attack is a form of indirect prompt injection (hiding instructions in content an AI will read), and agents are designed to follow an instruction file as though it came from the user. Forever places the problem where two individually reasonable things meet: agents trust the folder they are working in, and web pages have long been able to drop files into the Downloads folder. According to Help Net Security, much browsing is now handed to agents to do on their own. A page an agent opens by itself can also drop a file, with no one at the screen to notice.

Both automatic updates and instruction files involve trade-offs. Our inference is that turning off automatic extension updates avoids a window like this one, at the cost of receiving security fixes later too. Forever advises keeping the agent's action approvals and sandbox (which limits what a program can access) switched on, and according to iThome's summary, the instruction file aimed at Codex tried to get the agent to bypass exactly those two limits.

Anthropic's Supported Regions Policy is marked "Effective Nov 12, 2026", a date later than our check on 2 November, and lists Japan, Singapore, South Korea and Taiwan among the places in Asia where its products, Claude Code included, will be available under that policy. The page also states, "Any country or region not listed is unsupported." Mainland China, Hong Kong and Macao are not on the list. Cursor's documentation says only that some of its model providers have location-based restrictions, so certain models may not appear in Cursor in some regions while the others remain usable, and the page does not name the regions.

Windows and macOS users who installed or updated the Claude Code extension from Cursor's marketplace between the evening of 29 October and the early hours of 30 October, Taipei time (the morning and early afternoon of 29 October, Pacific time), can start by checking the list of authorised SSH keys as described in Cursor's notice; finding the attacker's key there means the machine is affected. The notice includes check and clean-up scripts for macOS and Windows. It also warns that removing the extension alone may not be enough, and advises changing, from a separate trusted computer, the passwords, tokens and login sessions the affected machine could reach, and considering a reinstall.

For people using agents such as Codex or Claude Code, the first step Forever recommends is not starting an agent in the Downloads folder, which requires no extra tools (our inference is that this also applies to people who do not write code and only use agents to sort documents or browse the web). Before opening a freshly cloned repository or a folder someone else sent, read any `AGENTS.md` and `CLAUDE.md` inside that you did not write, and check the agent's configuration files for servers or URLs you did not add yourself. If you find a planted file, Forever advises treating your login tokens as leaked and changing them immediately. Our inference is that these steps only reduce the chance of an agent being misled, and do not change the design that has agents act on instruction files.
