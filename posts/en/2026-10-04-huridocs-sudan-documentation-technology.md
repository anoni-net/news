---
title: Technology trade-offs in wartime human rights documentation
description: "HURIDOCS reflects on an expert meeting about wartime documentation in Sudan. Groups documenting abuses in high-risk settings should weigh whether a tool is worth its cost and whether its data can move between partners' systems; nothing changes for everyday users."
date: 2026-10-04T07:05:00+08:00
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
  - title: Is http://github.com blocked in mainland China?
    url: https://en.greatfire.org/github.com
    publisher: GreatFire
regions:
  - SD
authors:
  - anoni-net
---

HURIDOCS, which helps human rights groups manage their documentation, published a reflection on 15 September from an expert meeting on wartime documentation in Sudan, held in Nairobi in September. Documenters there face displacement, insecurity, intermittent connectivity and limited access to devices. The advice is aimed at groups documenting abuses in conflict and high-risk settings; nothing changes for everyday users.

The meeting discussed how information moves from documenters to researchers and potentially onward to prosecutors. Where documentation may feed into criminal accountability, such as at the International Criminal Court, the author writes that the worst outcome would be discovering years later that it cannot be used because a foreseeable evidentiary standard or chain-of-custody requirement was not fully met.

The author lists what technology can help with, including collecting information offline and securely, preserving provenance and connecting different systems. Every new tool also takes time to learn, needs training, devices, connectivity and maintenance, and can create dependence on vendors or add security risks. The test the author proposes is whether the cost of introducing a technology is worth what it enables.

The author also came away thinking that continuity, more than innovation, is one of the challenges needing more attention. That means connecting what the human rights movement has learned, what documenters know about their own context, and what institutions that may rely on the information will require.

## Perspective {#perspective}

Provenance and chain of custody come down to recording where each file came from, when it was obtained and who has handled it since. Taking a cryptographic hash, a fingerprint computed from the file's contents, at the moment of collection and recomputing it later shows whether the contents have changed.

The author treats interoperability as part of the infrastructure of human rights work, because different organisations have different needs, risks and resources, and writes that the goal is not one enormous system everyone must use. In technical terms, that means systems able to export and import common formats, so information can move between organisations without everyone adopting the same tool.

The digital rights group Access Now recorded three shutdowns in Sudan in 2025 during the ongoing conflict, one of them during school exams in July. In the same month, Sudan's telecoms regulator blocked WhatsApp voice and video calls nationwide.

The highest totals were in Asia: 95 in Myanmar, including cross-border shutdowns, 65 in India and 20 in Pakistan, while China had two. During protest-related shutdowns, authorities publicly acknowledged only 33% of them, with India, where shutdown orders must technically be published by law, as the exception. Wherever the network can be cut, a tool that needs a constant connection stops working until it returns.

HURIDOCS's own Uwazi is a browser-based database for organising human rights records, released under the permissive MIT licence and still shipping new versions as of 28 September. According to its official page, it records every change in an activity log and supports two-factor authentication; the code also includes CSV export for sharing data with partners on other systems. Self-hosting is free but needs Elasticsearch (a full-text search engine), MongoDB and at least 4 GB of RAM, and HURIDOCS also offers hosting.

Groups weighing a tool can turn the article's arguments into a checklist: the staff time to learn and maintain it, whether it can exchange data with partners, whether it preserves provenance, and whether recording can continue when the network goes down. Instructions for trying a demo are on Uwazi's official page. The interface ships in 11 languages, including Arabic but not Chinese, and can be translated into others. In mainland China, GreatFire, which monitors Chinese internet censorship, found access to github.com, where the code is hosted, intermittent as of 29 September, so downloads needed for self-hosting there may fail.
