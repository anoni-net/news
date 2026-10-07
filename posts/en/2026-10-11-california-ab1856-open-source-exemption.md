---
title: "California AB 1856's open source operating system exemption"
description: California's AB 1856, signed in September, amends a state law requiring operating systems to ask for a user's age at account setup. Under the amendment, a person or entity that distributes an operating system or app under a licence allowing copying, redistribution and modification is not a covered operating system provider. The rules apply from 2027 and are aimed at account holders in California.
date: 2026-10-11T00:00:00+08:00
slug: california-ab1856-open-source-exemption
categories:
  - censorship
sources:
  - title: "AB-1856 Age verification signals: software applications."
    url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1856
    publisher: California Legislative Information
    date: 2026-09-11
  - title: "AB 1856: Age verification signals: software applications."
    url: https://calmatters.digitaldemocracy.org/bills/ca_202520260ab1856
    publisher: CalMatters Digital Democracy
    date: 2026-09-10
  - title: "AB-1043 Age verification signals: software applications and online services."
    url: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1043
    publisher: California Legislative Information
    date: 2025-10-14
  - title: "Press release: child safety chatbot and social media laws signed"
    url: https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/
    publisher: Office of the Governor of California
    date: 2026-09-10
  - title: CONCERNING AGE ATTESTATION FOR USERS OF COMPUTING DEVICES.
    url: https://leg.colorado.gov/laws/session-laws/SB26-051/343/download
    publisher: Colorado General Assembly
    date: 2026-06-03
  - title: California Steps Back From Dangerous Expansion of Its Age-Gating Law
    url: https://www.eff.org/deeplinks/2026/07/california-steps-back-dangerous-expansion-its-age-gating-law
    publisher: EFF
    date: 2026-07-15
  - title: A.B. 1043's Internet Age Gates Hurt Everyone
    url: https://www.eff.org/deeplinks/2026/03/ab-1043s-internet-age-gates-hurt-everyone
    publisher: EFF
    date: 2026-03-12
  - title: System76 on Age Verification Laws
    url: https://system76.com/blog/post/system76-on-age-verification
    publisher: System76
    date: 2026-03-05
  - title: Bits from the DPL
    url: https://lists.debian.org/debian-devel-announce/2026/04/msg00001.html
    publisher: Debian
    date: 2026-04-04
  - title: Ubuntu's response to California's Digital Age Assurance Act (AB 1043)
    url: https://discourse.ubuntu.com/t/ubuntus-response-to-californias-digital-age-assurance-act-ab-1043/77948
    publisher: Ubuntu Discourse
    date: 2026-03-04
  - title: "userdb: add birthDate field to JSON user records"
    url: https://github.com/systemd/systemd/pull/40954
    publisher: GitHub
    date: 2026-03-05
  - title: Code of Practice for Online Safety – App Distribution Services
    url: https://www.imda.gov.sg/-/media/imda/files/regulations-and-licensing/regulations/codes-of-practice/code-of-practice-app-distribution-services/code-of-practice-for-online-safety-app-distribution-services.pdf
    publisher: IMDA
  - title: Keeping Young Users Safe Online
    url: https://www.imda.gov.sg/how-we-can-help/age-assurance
    publisher: IMDA
  - title: 移动互联网未成年人模式建设指南
    url: https://www.cac.gov.cn/2024-11/15/c_1733364304749288.htm
    publisher: 国家互联网信息办公室
    date: 2024-11-15
  - title: 青少年が安全に安心してインターネットを利用できる環境の整備等に関する法律
    url: https://laws.e-gov.go.jp/law/420AC1000000079
    publisher: e-Gov
regions:
  - US
authors:
  - anoni-net
---

California's governor signed AB 1856 on 10 September, amending the Digital Age Assurance Act (AB 1043) passed in 2025. The original law requires operating system providers to have the account holder, an adult user or the parent of a minor, enter the user's age at account setup, and then provide the user's age bracket to apps as a signal. AB 1856 adds that a person or entity distributing an operating system or app under licence terms that allow copying, redistribution and modification is not an operating system provider. The rules apply from 1 January 2027 and are aimed at account holders in California, so as of 7 October readers elsewhere do not need to change any settings.

Under AB 1043, age brackets are under 13, 13 to under 16, 16 to under 18, and 18 or older. When an app is downloaded and launched it requests the signal from the operating system provider or app store, and a developer who receives it is deemed to know the user's age range. California's Attorney General can bring civil actions, with penalties of up to $2,500 per affected child for negligent violations and up to $7,500 for intentional ones.

AB 1856 limits the operating system duty to systems with an account setup feature, and requires app stores to request the signal from the operating system and pass it to developers. Anyone not required by law may not request a signal. Earlier versions also covered browsers and websites, which a Senate amendment in July removed.

The open source exemption was added in the 18 May Assembly amendments. Its only condition is that the licence lets recipients copy, redistribute and modify the software. The text does not mention open source or Linux, does not require non-commercial distribution and does not name any licence, and the exemption appears only in the definition of an operating system provider, not in those of app stores or developers.

Colorado's SB26-051, signed in June, has a similar exemption with the same licence condition plus one more: the distributor must not use technical or contractual restrictions to stop users installing modified versions. Colorado's rules apply from 1 July 2028.

## Perspective {#perspective}

The operating system asks for an age at account setup, and apps query it through an interface the system provides. The law requires an age bracket rather than a birth date, does not require the entered age to be verified, and does not specify the interface format or where the data is stored. In March systemd, the component many Linux distributions use to manage the system and user accounts, merged a change adding a birth date field to user records that only administrators can modify, citing laws in California, Colorado and Brazil. We could not find which distributions will use it.

Supporters care about letting a child's age travel with the device. A committee analysis quotes the bill's author saying AB 1043 creates a privacy-first path to age assurance without interfering with apps' existing account features or parental controls. When signing AB 1043 in 2025, the governor wrote that parents who let a child be a device's main user can configure it to tell app developers the child's age. Common Sense Media, a children's advocacy group, wrote in support of a version that still included browsers and websites, saying that signals following the child stop platforms from skipping protections when a child switches routes.

Debian and Canonical had not reached conclusions in public statements made before the exemption was added. In April, Debian's project leader wrote that it was not yet clear how such rules apply to a volunteer project that does not sell software and distributes it in a highly decentralised way. In March, Canonical, the company behind Ubuntu, posted on the Ubuntu forum that it was reviewing AB 1043 with legal counsel and had no concrete plans.

In March, the digital rights group EFF wrote that AB 1043's burdens fall especially on developers without big-company resources, such as open source developers. In July EFF wrote that the expansion to browsers and websites had been dropped and that the exemption reduced the threat to the open source community. EFF therefore withdrew its opposition to AB 1856, while still considering AB 1043 unconstitutional.

The law limits operating systems to sending the minimum information necessary, and the Los Angeles Unified School District's support letter lists data minimisation among AB 1856's provisions. Linux computer maker System76 wrote that whoever enters the age can lie, and that a child can create an adult account in a virtual machine. System76 also wrote that if this approach becomes the standard, apps and websites will treat users as the lowest age bracket when no signal is sent. The law does not say what apps should do without a signal.

Several places in Asia put age-related duties at the app store or device level, but in different ways from California. The Code of Practice from Singapore's Infocomm Media Development Authority (IMDA) for app distribution services, in force since 31 March 2025, applies to five designated app stores, including Apple's App Store and Google Play. From 1 April 2026 they must use age assurance to stop users under 18 downloading age-inappropriate apps, and the Code does not mention operating systems.

In mainland China, 2024 guidelines from the Cyberspace Administration of China ask devices, apps and app distribution platforms to link up in a minors' mode, which limits usage times and duration and needs parental verification to exit, with the device offering ways to set a birth date or age range when the mode is first used. The guidelines set no effective date or penalties. Japan's 2008 law on young people's internet use requires mobile carriers to enable filtering on phones sold to people under 18 unless a guardian opts out, and device makers to build in or make it easy to use filtering software. Developers of the software that directly controls a device, in effect the operating system, have only a duty to make efforts to support this, and the law contains no age signal.

Based on the text, we infer that from 2027 users in California may be asked for the user's age when creating accounts on operating systems whose licences do not allow copying, redistribution and modification. On the same basis, Linux distributions that meet the exemption are not bound by this duty, though the law does not name which ones qualify. As of 7 October we could not find announcements from Apple, Google, Microsoft, Debian or Canonical on how they will respond after AB 1856.

When reading future laws that ask operating systems or app stores to handle age, a few questions help. Who enters the age, is it verified, and does a birth date or only an age bracket leave the device? Are open source and volunteer-maintained systems covered, and does an exemption depend only on the licence or also on not restricting modification? Can the approach let parents protect children with less data than uploading an ID?
