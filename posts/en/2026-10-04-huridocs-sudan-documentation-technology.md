---
title: Technology trade-offs in wartime human rights documentation
description: "HURIDOCS reflects on an expert meeting about wartime documentation in Sudan. Groups documenting abuses in high-risk settings should weigh whether a tool is worth its cost and whether its data can move between partners' systems. Nothing changes for everyday users."
date: 2026-10-04T00:05:00+08:00
slug: huridocs-sudan-documentation-technology
sources:
  - title: "What wartime documentation demands of technology: Lessons from Sudan"
    url: https://huridocs.org/2026/09/what-wartime-documentation-demands-of-technology-lessons-from-sudan/
    publisher: HURIDOCS
    date: 2026-09-15
  - title: Uwazi
    url: https://huridocs.org/technology/uwazi/
    publisher: HURIDOCS
  - title: huridocs/uwazi
    url: https://github.com/huridocs/uwazi
    publisher: GitHub
    date: 2026-09-28
  - title: "Rising repression meets global resistance: Internet shutdowns in 2025"
    url: https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf
    publisher: Access Now
    date: 2026-03-31
  - title: Welcome to the Uwazi demo!
    url: https://demo.uwazi.io/
    publisher: HURIDOCS
  - title: Is https://github.com blocked in mainland China?
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
    date: 2026-09-27
regions:
  - SD
authors:
  - anoni-net
---

HURIDOCS, which helps human rights groups manage their documentation, published a reflection on 15 September from an expert meeting on wartime documentation in Sudan, held in Nairobi in September. Documenters in Sudan face displacement, insecurity, intermittent connectivity and limited access to devices. The advice is aimed at groups documenting abuses in conflict and high-risk settings; nothing changes for everyday users.

The meeting discussed how information moves from documenters to researchers and potentially onward to prosecutors. Where documentation may feed into criminal accountability, such as at the International Criminal Court, the author writes that the worst outcome would be discovering years later that it cannot be used because a foreseeable evidentiary standard or chain-of-custody requirement was not fully met.

The author lists what technology can help with, including collecting information offline and securely, preserving provenance and connecting different systems. Every new tool also takes time to learn and needs training, devices, connectivity and maintenance. It can create dependence on vendors or infrastructure and, in high-risk settings, introduce new security considerations. The test the author proposes is whether the cost of introducing a technology is worth what it enables.

The author also came away thinking that continuity, more than innovation, is one of the challenges needing more attention. That means connecting what the human rights movement has learned, what documenters know about their own context, and what institutions that may rely on the information will require.

## Perspective {#perspective}

The digital rights group Access Now recorded three shutdowns in Sudan in 2025 during the ongoing conflict, one of them during school exams in July. The highest totals were in Asia: 95 in Myanmar, including cross-border shutdowns, 65 in India and 20 in Pakistan, while China had two. During protest-related shutdowns, authorities publicly acknowledged only 33% of them, with India, where shutdown orders must technically be published by law, as the exception. Wherever the network can be cut, a tool that needs a constant connection stops working until the connection returns.

Beyond connectivity, documentation that may become evidence needs provenance and a chain of custody: a record of where each file came from, when it was obtained and who has handled it since. Taking a cryptographic hash, a fingerprint computed from the file's contents, at the moment of collection and recomputing it later shows whether the contents have changed.

The author treats interoperability as part of the infrastructure of human rights work, since evidence is spread across organisations using different tools. The goal, the author writes, is not one enormous system everyone must use, because different organisations have different needs, risks and resources. In technical terms, that means systems able to export and import common formats.

HURIDOCS's own Uwazi is a browser-based database for organising human rights records, released under the permissive MIT licence and still shipping new versions as of 28 September. According to its official page, it records every change in an activity log and supports two-factor authentication; the code also includes CSV export, one way to move records into partners' systems. The interface ships in 11 languages, including Arabic but not Chinese, and can be translated into others.

Self-hosting Uwazi is free but needs Elasticsearch (a full-text search engine), MongoDB and at least 4 GB of RAM, and HURIDOCS also offers hosting. GreatFire, which monitors censorship in mainland China, found interference in 69% of its last 54 conclusive tests of https://github.com, the most recent on 27 September. Downloading the code to self-host there may therefore fail.

Groups weighing a tool can turn the article's arguments into a checklist: the staff time to learn and maintain it, whether it can exchange data with partners, whether it preserves provenance, and whether recording can continue when the network goes down. Uwazi's official demo site offers public logins, so trying it needs no registration.
