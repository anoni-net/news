---
title: Apple's planned changes to granting Full Disk Access on the Mac
description: Apple said on 2 October that it will require very explicit user action before a Mac app can be granted Full Disk Access, citing some developers' use of the permission and the growing risk from AI agents. Apple gave no version or date, and as of 12 October its release notes do not mention the control.
date: 2026-10-15T00:00:00+08:00
slug: apple-full-disk-access
categories:
  - tracking
follows:
  - 2026-10-09-muse-dots-agent-memory-permissions
sources:
  - title: Updates to Full Disk Access in macOS
    url: https://developer.apple.com/news/?id=p6zjojqw
    publisher: Apple
    date: 2026-10-02
  - title: 在 Mac 上更改「隱私權與安全性」設定
    url: https://support.apple.com/zh-tw/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: macOS 27 Golden Gate Release Notes
    url: https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes
    publisher: Apple
  - title: macOS 27.2 Golden Gate Beta 3 Release Notes
    url: https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes
    publisher: Apple
  - title: Meta disputes claim that Muse read a user's private messages without permission
    url: https://techcrunch.com/2026/09/30/meta-disputes-claim-that-muse-read-a-users-private-messages-without-permission/
    publisher: TechCrunch
    date: 2026-09-30
  - title: Meta Pushes Back on Claim That Muse AI Read a User's Messages Without Consent
    url: https://decrypt.co/379868/meta-muse-ai-agent-read-messages-without-permission
    publisher: Decrypt
    date: 2026-10-01
  - title: Apple says it's tightening macOS 'Full Disk Access' controls due to new risks from AI agents
    url: https://techcrunch.com/2026/10/02/apple-says-its-tightening-macos-full-disk-access-controls-due-to-new-risks-from-ai-agents/
    publisher: TechCrunch
    date: 2026-10-02
  - title: Apple changes full-disk access permissions to curb abuse from AI agents
    url: https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/
    publisher: Ars Technica
    date: 2026-10-02
  - title: 蘋果將增加macOS完全磁碟存取的開關控制
    url: https://www.ithome.com.tw/news/179400
    publisher: iThome
    date: 2026-10-05
  - title: Apple Tightens "Full Disk Access" Permission on macOS in Light of AI Agent Security Concerns
    url: https://www.privacyguides.org/news/2026/10/06/apple-tightens-full-disk-access-permission-on-macos-in-light-of-ai-agent-security-concerns/
    publisher: Privacy Guides
    date: 2026-10-06
  - title: Meta VP of Communications on X
    url: https://x.com/andymstone/status/2105107596734849423
    publisher: X
    date: 2026-09-30
  - title: "Microsoft Execution Containers: Policy-driven containment for AI agents"
    url: https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/
    publisher: Microsoft
    date: 2026-10-07
  - title: Microsoft eXecution Container (MXC)
    url: https://github.com/microsoft/mxc
    publisher: GitHub
  - title: 정보통신망 이용촉진 및 정보보호 등에 관한 법률
    url: https://www.law.go.kr/LSW//lsLawLinkInfo.do?lsJoLnkSeq=900630227&lsId=000030&chrClsCd=010202&print=print
    publisher: 국가법령정보센터
  - title: 人工智慧基本法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=H0160093
    publisher: 全國法規資料庫
    date: 2026-01-14
  - title: 生成 AI サービスの利用に関する注意喚起等について
    url: https://www.ppc.go.jp/files/pdf/230602_kouhou_houdou.pdf
    publisher: 個人情報保護委員会
    date: 2023-06-02
  - title: Muse from Meta App - App Store
    url: https://apps.apple.com/us/app/muse-from-meta/id6760173601
    publisher: App Store
  - title: Change Privacy & Security settings on Mac
    url: https://support.apple.com/guide/mac-help/mchl211c911f/mac
    publisher: Apple
authors:
  - anoni-net
---

Apple said in a developer news post on 2 October that it will add controls to macOS Full Disk Access so that users who genuinely want to grant it can only do so with very explicit user action. Apple did not say which version, when, what the interface will look like, or whether apps already granted access will need confirming again. As of 12 October, neither the macOS 27 nor the macOS 27.2 beta 3 release notes mention the new control.

Apple's post says Full Disk Access largely sidesteps the controls that protect user data so that backup apps can work on the Mac. It also says some developers use it in ways that could expose files, mail, messages and even browsing history without users' full knowledge, and that the risk will grow substantially as AI agents (AI programs that can operate a computer and read files and apps on a user's behalf) become more capable and autonomous. TechCrunch later corrected its report, which had described the change as Apple "limiting" permissions, to say it is about informed consent and is not a new limit.

A few days earlier, according to TechCrunch and Decrypt, a columnist said Meta's AI agent Muse for Mac had read his private messages while Full Disk Access was off (our 9 October post covered this). According to Decrypt, he had declined Messages access during setup and later found Muse had synced the Mac's local Messages database. Meta's VP of Communications said on X on 30 September that Muse can only read Messages if both Full Disk Access and Muse's own Messages connector are enabled. Apple's post names no app or developer, and it was Ars Technica and iThome that framed the two as contradicting each other.

## Perspective {#perspective}

Full Disk Access is an operating-system permission, and Apple's support page says it lets an app access all files on the computer, including data from other apps such as Mail and Messages and Time Machine backups. A macOS security expert quoted by Ars Technica said a program with this permission can read files such as browsing history, browser cookies and chats. A Meta executive said, as relayed by TechCrunch, that reading Messages goes through in-app permissions and macOS system-level protections that cannot be bypassed even if the app had a bug. Apple's support page and the security expert describe what an app can read once it has the permission, while Meta's statements describe which authorisation steps Muse requires.

Microsoft Execution Containers (MXC), released by Microsoft on 7 October, takes a different approach. According to Microsoft's post, developers or IT administrators write a policy defining which files and network destinations an AI agent can use, and the policy sits outside the agent's control. MXC is open source under the MIT licence and uses the macOS Seatbelt sandbox (a mechanism that limits which resources a program can reach). Its README says it is an SDK built into apps, and Microsoft's list of supported tools includes GitHub Copilot and OpenAI Codex but not Muse or ChatGPT, so in our reading ordinary users will not configure it directly.

Neither Microsoft's nor Apple's documents mention the other, and it is our choice to set them side by side. The difference is who acts as the gatekeeper: Apple's plan makes users more aware of what they are granting at the moment of consent, while MXC lets developers limit in advance what an agent can touch. Apple's post does not say whether the new control will change what Full Disk Access can read. Things to watch are when the control appears in macOS release notes and whether existing grants need reconfirming.

We compared South Korea, Japan and Taiwan on one question: is there a rule requiring operating-system or app makers to provide ways to grant and withdraw access permissions? South Korea has one. Article 22-2(3) of its Act on Promotion of Information and Communications Network Utilization and Information Protection (the version in force from 2 October 2026, checked on 12 October) requires mobile operating-system makers, device makers and software suppliers to take measures such as providing ways for users to consent to and withdraw app access permissions, though it covers mobile devices and is not aimed at AI agents. What we found for Japan is a June 2023 warning from the Personal Information Protection Commission to users about entering personal data into generative AI services (we did not check for later updates), and for Taiwan, the AI Basic Act of January 2026, which places privacy-by-design duties on government agencies rather than on app or operating-system makers.

Mac users can open System Settings, then Privacy & Security, then Full Disk Access to see which apps have it. For an unfamiliar app, it is worth finding out why it needs the permission, bearing in mind that backup apps are the use Apple's post names. Apple's support page only describes adding apps, while Meta says Muse's access can be revoked at any time. Before granting it, remember that it lets an app read messages other people have sent you and your browsing history, a judgement that will still be yours to make after Apple's new control arrives.
