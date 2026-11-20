---
title: Tighter limits on outside contributions to open source projects in the AI era
description: curl ended its bug bounty, and GitHub now lets maintainers limit who can open pull requests and issues; in 2026 open source projects are narrowing the ways outsiders can contribute. The author argues that this solves the volume problem created by floods of low-quality submissions, but the trust problem remains. The malicious releases in both the xz backdoor and the Shai-Hulud worm were published from developer accounts that were already trusted, and what is missing is review capacity and permission management.
date: 2026-11-25T00:15:00+08:00
slug: open-source-contributions-ai
categories: [column]
authors: [toomore]
sources:
  - title: The end of the curl bug-bounty
    url: https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
    publisher: curl author's blog
    date: 2026-01-26
  - title: Contributing to the curl project
    url: https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md
    publisher: curl
  - title: Welcome to the Eternal September of open source. Here's what we plan to do for maintainers.
    url: https://github.blog/open-source/maintainers/welcome-to-the-eternal-september-of-open-source-heres-what-we-plan-to-do-for-maintainers/
    publisher: GitHub
    date: 2026-02-12
  - title: Limit open pull requests for users without write access
    url: https://github.blog/changelog/2026-06-17-limit-open-pull-requests-for-users-without-write-access/
    publisher: GitHub
    date: 2026-06-17
  - title: Restrict issue creation to collaborators only
    url: https://github.blog/changelog/2026-06-29-restrict-issue-creation-to-collaborators-only/
    publisher: GitHub
    date: 2026-06-29
  - title: "Pull request limits: Exempt contributors by age or history"
    url: https://github.blog/changelog/2026-10-28-pull-request-limits-exempt-contributors-by-age-or-history
    publisher: GitHub
    date: 2026-10-28
  - title: All projects
    url: https://osssaysno.com/all
    publisher: Open Source Says No
  - title: About
    url: https://osssaysno.com/about
    publisher: Open Source Says No
  - title: Kernel Guidelines for Tool-Generated Content
    url: https://github.com/torvalds/linux/blob/master/Documentation/process/generated-content.rst
    publisher: Linux kernel
  - title: Open source was not ready for AI-speed contributions
    url: https://frenck.dev/open-source-was-not-ready-for-ai-speed-contributions/
    publisher: Home Assistant maintainer's blog
    date: 2026-05-31
  - title: XZ Utils backdoor
    url: https://tukaani.org/xz-backdoor/
    publisher: Tukaani
  - title: backdoor in upstream xz/liblzma leading to ssh server compromise
    url: https://www.openwall.com/lists/oss-security/2024/03/29/4
    publisher: oss-security
    date: 2024-03-29
  - title: Timeline of the xz open source attack
    url: https://research.swtch.com/xz-timeline
    publisher: xz attack timeline
  - title: AI cuts coding time, but it's also filling open source's inbox with crap
    url: https://www.theregister.com/ai-and-ml/2026/10/21/ai-cuts-coding-time-but-its-also-filling-open-sources-inbox-with-crap/5304389
    publisher: The Register
    date: 2026-10-21
  - title: Sunsetting Jazzband
    url: https://jazzband.co/news/2026/03/14/sunsetting-jazzband
    publisher: Jazzband
  - title: Widespread Supply Chain Compromise Impacting npm Ecosystem
    url: https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
    publisher: CISA
    date: 2025-09-23
  - title: "Open Source Stewardship Communities: \"We need you, but not your pull request\""
    url: https://arxiv.org/abs/2609.12236
    publisher: arXiv
    date: 2026-09-10
  - title: What Will Replace Pull Requests? Rethinking Software Collaboration for AI Agents
    url: https://arxiv.org/abs/2610.34933
    publisher: arXiv
    date: 2026-10-26
---

The source code of open source projects is still public, but what outsiders can send into those projects is increasingly restricted. In 2026 one project ended its bug bounty and a platform now lets maintainers reserve proposed changes for collaborators, and in each case the reasons had to do with the flood of submissions that AI has brought. I want to work out what tightening these entry points protects, and what open source projects pay for it.

My view is that closing off outside PRs (pull requests, proposed code changes submitted to a project) can hold back the flood of low-quality contributions that AI sends in, and the projects tightening their entry points mostly justify it as protecting maintainers' time. Tightening solves a problem of volume; what worries me is that it gets treated as a security measure. I believe supply chain attacks mostly come in through accounts or people who are already trusted, so the trust problem remains, and what open source projects really lack is review capacity and permission management.

Now that code has become cheap, I think what counts as a contribution should shift as well. Reviewing other people's changes, writing tests that reproduce a problem and describing a problem clearly should all count.

## Tighter entry points for outside contributions {#tightening}

The author of curl, the network transfer tool, announced on their blog on 26 January that its bug bounty was ending, and it officially stopped on 31 January. According to the same post, the programme confirmed 87 vulnerabilities from April 2019 onward and paid researchers over 100,000 USD. Ending the bounty was meant to remove the incentive to submit made-up reports, and reports now go through GitHub's private vulnerability reporting feature or to the project's security email address.

According to GitHub's blog post of 12 February, maintainers could already limit opening PRs to collaborators or turn PRs off entirely. From 17 June, per GitHub's changelog, maintainers can set how many PRs a user without write access may have open at once, and anyone who reaches the limit has to close or merge an existing one before opening another. Draft PRs do not count towards the limit, and maintainers can add trusted contributors to a bypass list. On 28 October GitHub added automatic exemption rules that let people through based on the age of their account in days or on how many of their PRs have been merged in that repository.

On 29 June the collaborators-only restriction was extended to issues (threads for reporting problems or making requests). According to the changelog, once the setting is on, people without write access cannot create issues from entry points across the repository, including the Issues page, comments, Discussions, Projects and Copilot. This change matters more to me, because I see issues as the main channel through which people who do not write code report problems.

Open Source Says No, a site that tracks AI contribution policies, listed 221 projects as of 20 November. To be listed, a project needs at least 5,000 stars on GitHub, or must be widely used infrastructure such as a distribution, a language runtime or a major library. Of these, 24 ban AI-generated contributions, and most of the rest accept AI-assisted contributions under conditions such as disclosure or human review. According to its about page, the site is informational only and takes no position on whether those policies are right.

## The gap between the cost of creating and the cost of reviewing {#review-cost}

According to GitHub's February post, a PR can now be generated in seconds, and generative AI makes it easy to produce code, issues and security reports at scale. In the post's words, "The cost to create has dropped but the cost to review has not." According to the same post, maintainers have always dealt with noisy inbound, and low-quality submissions are nothing new. The Linux kernel's contribution rules are written along similar lines: tools can increase the volume of contributions, while reviewer and maintainer time is a scarce resource.

According to curl's author, in earlier years more than 15% of submissions to the bounty programme turned out to be confirmed vulnerabilities, and from 2025 the rate fell below 5%. The author attributes this to an explosion of AI slop, adding that even reports that were not obviously slop had dropped in quality, a decline that began slowly in the second half of 2024 and accelerated badly in 2025. The same post says that PRs have not been a problem for curl, since no human time needs to go into a PR until it passes all 200 CI jobs (continuous integration, the tests that run automatically on every change).

On 31 May a maintainer of Home Assistant (an open source smart home platform) wrote on their personal site that contributors are being amplified while maintainers are still the verification bottleneck. As they describe it, a change used to require understanding the code, writing the change, running the tests and explaining the result before it was sent, so there was some friction before a maintainer ever saw it. The test they propose is whether the person submitting the work understands it, has validated it and takes responsibility for it, and whether AI was used is not part of the test.

## Risks that tighter entry points can and cannot prevent {#what-it-stops}

None of the projects cited above claims that tightening the entry points protects against supply chain attacks. I put the two together because Jazzband, an organisation that jointly maintained Python packages, linked its open membership model, safe operation and the xz backdoor in its announcement that it was shutting down.

I read all three measures (taking the money out of the bug bounty, capping open PRs and limiting issues to collaborators) as responses to the volume of submissions, and I think they work on the volume problem. curl's author also cautions that their guesses may be wrong, and that if so they will take further steps. According to a report in The Register on 21 October, curl announced that week that it would move low and medium severity vulnerabilities into public view, in the report's words to protect a security team "almost overwhelmed by AI-assisted reports". My reading is that the pressure of volume remained after the bounty ended, and how much tighter entry points relieve it will depend on the numbers that follow.

xz is a compression tool common on Linux systems, and the xz backdoor exposed in March 2024 is the example least favourable to my argument, because the account that planted it started out as an outside contributor. According to the xz project's website, the release tarballs (compressed archives) of versions 5.6.0 and 5.6.1 contained the backdoor, and they were created and signed by that account.

According to a public timeline that cites the xz-devel mailing list day by day, the account sent its first innocuous patch in October 2021 and was merging changes directly by the end of 2022. In February 2024 it hid the backdoor in binary test files and then released 5.6.0.

I accept that a project taking no outside patches at all would not have given this account the starting point of that first patch. Counting from the dates in the timeline, two years and four months passed between the first patch and the backdoored release. My view is that tightening can only delay this kind of long-term effort to earn trust, and a patient attacker can still trade time for trust.

According to the message on oss-security, the open source security mailing list, that publicly warned of the backdoor, one portion of it existed only in the release tarballs: a line of build script that was not in the source on git. Distributions and users often download tarballs that maintainers package separately and sign digitally, and their contents are not necessarily identical to the public source on git. My inference is that reviewing PRs would not have revealed that line either, and that what matters is who can create and sign release files.

The original maintainer wrote on the mailing list in 2022 that the effort they could put in was limited (as transcribed in the same timeline). I think the weakness xz exposed lies in having too few maintainers and in permission management, and closing the entry points will not give a project one more person to share reviewing and releasing.

Jazzband let anyone join, and its members shared push access (permission to push changes directly into a project); in March it announced it would gradually wind down, and it disabled new sign-ups. According to the announcement, over ten years Jazzband grew to 3,135 members and maintained 84 projects. In the announcement, AI-generated spam PRs and issues are given as the reason open membership and shared push access became untenable, and its lead also wrote that giving push access to everyone who joins could not go on alongside operating Jazzband safely.

Another problem listed in the announcement is that one person handled everything: every project transfer, PyPI (the Python package publishing platform) permission change and infrastructure decision went through the lead. In the same announcement, the lead describes xz as an example of a lone maintainer burning out and someone malicious filling the gap. The trigger given in the announcement is AI submissions, but I file it under permission management, since what became unsustainable was shared push access.

According to an alert from the US Cybersecurity and Infrastructure Security Agency (CISA) dated 23 September 2025, a self-replicating worm called Shai-Hulud compromised over 500 packages on npm (the JavaScript package registry). How the attackers gained initial access is not stated in the alert; after that, the malware scanned the environment for credentials, targeting GitHub tokens and keys for cloud services. The worm then published new versions of other packages with injected code, acting as the compromised developers. Among CISA's recommendations are rotating all developer credentials and requiring phishing-resistant multifactor authentication (a second check at login besides the password) on GitHub and npm accounts.

None of the recommendations in CISA's alert is to restrict outside PRs. I think the xz attacker traded time for trust, while Shai-Hulud scanned for and stole developer credentials and published as the compromised developers; in both cases the damage was done through accounts that were already trusted. Two incidents do not make a statistic, and "mostly" is a judgement I draw from these two examples.

## Sources of new maintainers {#new-maintainers}

According to GitHub's February post, restrictions can disproportionately affect first-time contributors acting in good faith, which is why the controls are optional and configurable. My inference is that a newcomer who does not meet the automatic exemption rules has to wait for a maintainer to add them to the bypass list by hand before they can go over the cap on open PRs.

In September two software engineering researchers posted a paper on arXiv (a preprint platform for academic papers). According to the abstract, AI has lowered the cost of implementing changes, while reviewing someone else's contribution remains comparatively expensive. Some projects therefore restrict who may contribute implementations while still welcoming other kinds of participation. The authors argue that the reason is that such code no longer justifies the cost of review, whether or not AI generated it.

The researchers call this form a stewardship community, in which a small core keeps the authority to implement changes while a broader community shapes the software without writing code. By the paper's definition, writing code in such a community increasingly depends on approval. The authors also caution in the abstract that AI can replace implementation labour while weakening how open source communities renew themselves.

In another paper posted on arXiv in October, its authors reviewed 50 grey literature documents (blog posts, announcements and other material not published through academic channels) from 31 organisations or individuals. According to the abstract, most responses kept pull requests in some form while adding tools or restrictions, and restriction was the response most often reported as adopted.

After Jazzband announced it was winding down, its projects had to find new homes. In the announcement, Django-related projects are directed to Django Commons, and some have already moved; at the time of the announcement Django Commons had 5 admins and 15 active projects. For projects outside Django, such as pip-tools and tablib, the lead wrote that they were not aware of an equivalent.

I expect that once entry points are tightened, projects will find it harder to develop new maintainers from among outside contributors, and the shortage of maintainers will still be there next time. I see this cost as the same weakness xz had: an attacker only has a gap to fill because there are too few maintainers.

## A shift in what counts as contribution, and signals for readers {#what-readers-can-do}

I am not against projects tightening their entry points; facing a flood of submissions, maintainers need to protect their time first. I hope the time saved goes into review and permission management, such as who can merge, who can release and how tokens are kept, and the CISA recommendations mentioned above can serve as a starting point for that check.

I think the work worth counting as contribution is work that lowers maintainers' cost of verification. The xz backdoor was found because a developer noticed ssh logins taking a lot of CPU on Debian's development branch (sid), along with errors reported by valgrind (a tool for checking memory errors). The developer traced the cause and posted a public warning on oss-security, and I see that message as a problem description worth no less than a patch.

Anyone who wants to get involved can start by reading a project's contribution policy. Among the policies collected by Open Source Says No, the Linux kernel's requires contributors to understand and be able to defend every part of what they submit. According to curl's contribution document, the project accepts code written with the help of AI as long as it meets the usual requirements on coding style, documentation and tests. Reporters who use AI tools to find problems also have to disclose this in their reports.

People who do not write code can take part too: when reporting a problem, writing down the version, the steps taken and whether it can be reproduced saves maintainers verification time. When a project limits issues to collaborators, check its contribution document first for other ways to report.

For people who use privacy tools, I suggest looking at how many active maintainers a project has, whether its contribution policy spells out rules on AI and permissions, and how long vulnerabilities take from report to fix (contribution documents, release notes and security advisories usually cover this). As of 20 November, Open Source Says No did not list tools such as Tor (the onion routing network), Tails (an amnesic live operating system) or Signal (an encrypted messaging app), so whether they have such rules has to be checked in each project's contribution documents. At the end of 2022 the xz README listed two maintainers (according to the same timeline), one of whom was the account that later planted the backdoor. So these signals are only a reference and cannot guarantee safety.

## Further reading {#further-reading}

- [Personal protection and open source maintenance as AI speeds up vulnerability discovery](https://anoni.net/news/en/2026/11/eff-security-worse/): PHP's security team patched real vulnerabilities while working through more than 100 reports that turned out to be invalid or not reproducible, a situation close to curl's
- [A backdoored extension and malicious instruction files in AI coding tools](https://anoni.net/news/en/2026/11/ai-devtools-supply-chain/): a tampered extension appeared in a marketplace under a verified account, another case that came in through a trusted publishing channel
- [Compositor, an open-source image editor, and maintaining and auditing AI-generated code](https://anoni.net/news/en/2026/10/compositor-image-editor/): the developer says AI wrote all of the code, and eight patch PRs from an outside contributor were closed together, a look at reviewing AI-written code from the developer's side
