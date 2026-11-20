---
title: Tighter limits on outside contributions to open source projects in the AI era
description: curl ended its bug bounty, and GitHub now lets maintainers limit who can open pull requests and issues; in 2026 open source projects are narrowing the ways outsiders can contribute. The author argues that this addresses the volume problem created by floods of low-quality submissions, but the trust problem remains. The malicious releases in both the xz backdoor and the Shai-Hulud worm were published from developer accounts that were already trusted, and what is missing is review capacity and permission management.
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

The source code of open source projects is still public, but what outsiders can send into those projects is increasingly restricted. By entry points I mean the channels through which outsiders send code changes, report problems or disclose vulnerabilities to a project. In 2026 one project ended its bug bounty and a platform now lets maintainers reserve proposed changes for collaborators, and in each case the reasons had to do with the flood of submissions that AI has brought. I want to work out what tightening these entry points protects, and what open source projects pay for it.

My view is that closing off outside PRs (pull requests, proposed code changes submitted to a project) can hold back the flood of low-quality contributions that AI sends in, and the projects tightening their entry points mostly justify it as protecting maintainers' time. Tightening addresses a problem of volume; what worries me is that it gets treated as a security measure. I believe supply chain attacks mostly come in through accounts or people who are already trusted, so the trust problem remains, and what open source projects really lack is review capacity and permission management.

Now that AI tools make producing code fast and easy, I think open source projects should adjust how they think about contribution. When a project receives a change, a maintainer first has to understand the code and check it for errors and security problems before merging it, and this step is called review. Reviewing other people's changes, writing tests that reproduce a problem and describing a problem clearly have always been important parts of maintaining a project, and until now maintainers have mostly done that work themselves. With more code arriving, I think outside contributors need to share this work, and it should be recognised as contribution.

## Tighter entry points for outside contributions {#tightening}

The author of curl, a widely used network transfer tool, announced on their blog on 26 January that the project's bug bounty was ending, and it officially stopped on 31 January. According to the same post, the programme confirmed 87 vulnerabilities in total over its run from April 2019, and paid out more than 100,000 USD in rewards to researchers. The author wrote that the aim of ending the bounty was to stop giving people a reason to make up reports in order to collect a reward. Anyone who wants to report a vulnerability now uses GitHub's private vulnerability reporting feature or emails the project's security address.

According to GitHub's blog post of 12 February, maintainers could already limit opening PRs to collaborators (members a project has added and given permission to change its code directly), or turn PRs off entirely. From 17 June, per GitHub's changelog, maintainers can set the maximum number of PRs that any other user may have open at the same time. Once someone reaches that limit, they cannot open a new PR until an older one has been closed or merged.

Draft PRs do not count towards the limit, and maintainers can add trusted contributors to a bypass list. On 28 October GitHub added automatic exemption rules, which let people go over the limit if their account is at least a set number of days old or if they have already had a set number of PRs merged in that repository.

On 29 June GitHub extended the collaborators-only option to issues (threads for reporting problems or making requests), so a project can now allow only collaborators to open issues. According to the changelog, once this setting is on, nobody else can create an issue from anywhere in the repository. **This change matters more to me, because I see issues as the main channel through which people who do not write code report problems.**

Open Source Says No, a site that tracks AI contribution policies, listed 221 projects as of 20 November; to be listed, a project needs at least 5,000 stars on GitHub, or must be widely used infrastructure such as a distribution, a language runtime or a major library. Of these, 24 ban AI-generated contributions. Most of the rest accept AI-assisted contributions, but with conditions attached, such as disclosing that AI was used or having the work reviewed by a person. According to its about page, the site is informational only and takes no position on whether those policies are right.

## The gap between the cost of creating and the cost of reviewing {#review-cost}

According to GitHub's February post, a PR can now be generated in seconds, and generative AI makes it easy to produce code, issues and security reports at scale. In the post's words, "The cost to create has dropped but the cost to review has not." According to the same post, maintainers have always dealt with noisy inbound, and low-quality submissions are nothing new. The Linux kernel's contribution rules contain a similar passage: tools can increase the number of contributions, but the time of reviewers and maintainers is limited.

According to curl's author, in earlier years more than 15% of submissions to the bounty programme turned out to be confirmed vulnerabilities, and from 2025 the rate fell below 5%. The author attributes this to an explosion of AI slop, adding that even reports that were not obviously slop had dropped in quality, a decline that began slowly in the second half of 2024 and accelerated badly in 2025. According to the same post, PRs have not been a problem for curl, because no human time needs to go into reviewing a PR until it passes all 200 CI jobs (continuous integration, the tests that run automatically on every change).

On 31 May a maintainer of Home Assistant (an open source smart home platform) wrote on their personal site that AI lets contributors send more changes, but each one still has to be verified by a maintainer. As they describe it, a contributor used to have to understand the code, write the change, run the tests and explain the result before they could submit anything, and those steps were a hurdle in themselves. The test they propose is whether the person submitting a change understands it, has validated it and takes responsibility for it, and whether AI was used is not part of the test.

## Risks that tighter entry points can and cannot prevent {#what-it-stops}

In the documents I cited above, the reasons I found for tightening were the volume of submissions and maintainers' time, not protection against supply chain attacks. I put the two together because Jazzband, an organisation that jointly maintained Python packages, tied its open membership model to whether it could operate safely in its announcement that it was shutting down, and cited the xz backdoor as an example of what happens after a lone maintainer burns out.

I see these three measures (ending the bug bounty, limiting the number of PRs and letting only collaborators open issues) as responses to the volume of submissions, and I think they can ease the volume problem. curl's author also cautions that their guesses may be wrong, and that if so they will take further steps. According to a report in The Register on 21 October, curl announced that week that it would move low and medium severity vulnerabilities into public view, and the reason given in the report is to protect curl's security team, which was "almost overwhelmed by AI-assisted reports". Judging from that report, the pressure from incoming reports remained after the bounty ended, and how much tighter entry points relieve it will depend on the numbers that follow.

xz is a compression tool common on Linux systems. Looked at from the entry-point side, the xz backdoor, exposed in March 2024, leads to a different observation from mine, because the account that planted it started out as an outside contributor. According to the xz project's website, the release tarballs (compressed archives) of versions 5.6.0 and 5.6.1 contained the backdoor, and those two tarballs were created and signed by that same account.

According to a public timeline that cites the xz-devel mailing list day by day, the account sent its first innocuous patch in October 2021, and by the end of 2022 it was able to merge changes into the project directly. In February 2024 it hid the backdoor in binary test files and then released 5.6.0.

From that angle, if a project took no outside patches at all, this account could not even have taken its first step. Counting from the dates in the timeline, two years and four months passed between the first patch and the backdoored release. **My view is that tightening entry points can only delay attacks in which someone spends a long time earning trust, and a patient attacker can still trade time for trust**.

According to the message on oss-security, the open source security mailing list, that publicly warned of the backdoor, one portion of it existed only in the release tarballs: a line of build script that was not in the source on git. As I understand it, distributions and users often download tarballs that maintainers package separately and sign digitally, and their contents are not necessarily identical to the public source on git. So my inference is that even careful review of every PR would not have revealed that line, and that what matters is who has permission to create and sign release files.

The original maintainer wrote on the mailing list in 2022 that the effort they could put in was limited (as transcribed in the same timeline). **I think the weakness the xz incident exposed is having too few maintainers, together with how the project managed who was given release permissions. Closing the entry points will not give a project one more person to share reviewing and releasing either**.

Jazzband let anyone join, and its members shared push access (permission to push changes directly into a project); in March it announced it would gradually wind down, and it disabled new sign-ups. According to the announcement, over ten years Jazzband grew to 3,135 members and maintained 84 projects. The reason given in the announcement for winding down is that a flood of AI-generated spam PRs and issues made open membership and shared push access untenable. Its lead also wrote that they could not keep giving push access to everyone who joined while still operating Jazzband safely.

Another problem listed in the announcement is that every project transfer, PyPI (the Python package publishing platform) permission change and infrastructure decision had to go through the lead alone. In the same announcement, the lead describes xz as an example of a lone maintainer burning out and someone malicious filling the gap. The immediate cause given in the announcement is AI submissions, but I see it as a permission management problem, since what became unsustainable was shared push access.

According to an alert from the US Cybersecurity and Infrastructure Security Agency (CISA) dated 23 September 2025, a self-replicating worm called Shai-Hulud compromised over 500 packages on npm (the JavaScript package registry). How the attackers first got in is not stated in the alert, whose account begins after that point: the malware searched the environment for stored credentials, targeting GitHub tokens (keys that let a program sign in to an account in place of a password) and keys for cloud services. The worm then signed in to npm as the compromised developers, added malicious code to other packages and published new versions of them. Among CISA's recommendations are rotating all developer credentials and requiring phishing-resistant multifactor authentication (a second check at login besides the password) on GitHub and npm accounts.

None of the recommendations in CISA's alert is to restrict outside PRs. I think the xz attacker traded time for trust, while Shai-Hulud scanned for and stole developer credentials and published as the compromised developers; in both cases the damage was done through accounts that were already trusted. Two incidents do not amount to a statistic, and the "mostly" in my opening is a judgement I draw from these two examples.

## Sources of new maintainers {#new-maintainers}

According to GitHub's February post, these restrictions can disproportionately affect first-time contributors acting in good faith, which is why GitHub made them optional, configurable settings. My inference is that a newcomer who does not meet the automatic exemption rules has to wait for a maintainer to add them to the bypass list by hand before they can go over the cap on open PRs.

In September two software engineering researchers posted a paper on arXiv (a preprint platform for academic papers). According to the abstract, AI has made it cheaper to write a change, while reviewing someone else's contribution still takes comparatively more effort. Some projects have therefore restricted who may submit code, while still welcoming other kinds of participation. The authors argue that these projects impose the restriction not because the code was written by AI, but because such code is no longer worth the effort of reviewing.

The researchers call this form a stewardship community. In this kind of community, only a small group of core members can put code into the project, while other people can still shape the software without writing code. By the paper's definition, writing code there increasingly requires approval first, rather than being something contributors can start on their own. The authors also caution in the abstract that AI can replace the coding work that outside contributors used to supply, while weakening how open source communities renew themselves (by bringing in new members who can take over).

In another paper posted on arXiv in October, its authors reviewed 50 grey literature documents (blog posts, announcements and other material not published through academic channels) from 31 organisations or individuals. According to the abstract, most responses kept pull requests in some form while adding tools or restrictions, and restriction was the response most often reported as adopted.

After Jazzband announced it was winding down, the projects it had maintained needed someone else to take them over. In the announcement, Django-related projects are directed to Django Commons, and some have already moved; at the time of the announcement Django Commons had 5 admins and 15 active projects. For projects outside Django, such as pip-tools and tablib, the lead wrote that they were not aware of an equivalent.

I expect that once entry points are tightened, projects will find it harder to develop new maintainers from among outside contributors, and the shortage of maintainers will persist. I see this cost as the same weakness xz had: an attacker only has a gap to fill because there are too few maintainers.

## A shift in what counts as contribution, and signals for readers {#what-readers-can-do}

I am not against projects tightening their entry points; facing a flood of submissions, maintainers need to protect their time first. I hope the time saved goes into review and permission management, such as who can merge, who can release and how tokens are kept, and the CISA recommendations mentioned above can serve as a starting point for that check.

I think the work worth counting as contribution is **work that lowers maintainers' cost of verification**. The xz backdoor was found because a developer noticed ssh logins taking a lot of CPU on Debian's development branch (sid), along with errors reported by valgrind (a tool for checking memory errors). The developer traced the cause and posted a public warning on oss-security, and I see that message as a problem description worth no less than a patch.

Anyone who wants to get involved can start by reading a project's contribution policy. Among the policies collected by Open Source Says No, the Linux kernel's requires contributors to understand everything they submit and to be able to defend it. According to curl's contribution document, the project accepts code written with the help of AI as long as it meets the usual requirements on coding style, documentation and tests. Reporters who use AI tools to find problems also have to disclose this in their reports.

People who do not write code can take part too: when reporting a problem, writing down the version, the steps taken and whether it can be reproduced saves maintainers verification time. When a project limits issues to collaborators, check its contribution document first for other ways to report.

For people who use privacy tools, I suggest looking at how many active maintainers a project has, whether its contribution policy spells out rules on AI and permissions, and how long vulnerabilities take from report to fix (contribution documents, release notes and security advisories usually cover this). As of 20 November, Open Source Says No did not list tools such as Tor (the onion routing network), Tails (an amnesic live operating system) or Signal (an encrypted messaging app), so whether they have such rules has to be checked in each project's contribution documents. At the end of 2022 the xz README listed two maintainers (according to the same timeline), one of whom was the account that later planted the backdoor. So these signals are only a reference and cannot guarantee safety.

Does the contribution guide of the privacy tool you rely on say anything about AI or permissions? If the project stopped accepting outside PRs, how would you take part?

## Further reading {#further-reading}

- [Personal protection and open source maintenance as AI speeds up vulnerability discovery](https://anoni.net/news/en/2026/11/eff-security-worse/): PHP's security team patched real vulnerabilities while working through more than 100 reports that turned out to be invalid or not reproducible, a situation close to curl's
- [A backdoored extension and malicious instruction files in AI coding tools](https://anoni.net/news/en/2026/11/ai-devtools-supply-chain/): a tampered extension appeared in a marketplace under a verified account, another case that came in through a trusted publishing channel
- [Compositor, an open-source image editor, and maintaining and auditing AI-generated code](https://anoni.net/news/en/2026/10/compositor-image-editor/): the developer says AI wrote all of the code, and eight patch PRs from an outside contributor were closed together, a look at reviewing AI-written code from the developer's side
