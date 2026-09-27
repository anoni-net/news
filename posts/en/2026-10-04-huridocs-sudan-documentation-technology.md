---
title: Technology trade-offs in wartime human rights documentation
description: "HURIDOCS draws lessons from documenting the war in Sudan: before adopting a tool, ask whether it is worth its burden, whether it can exchange data with others, and whether it can last."
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
    date: 2026-09-25
  - title: "Rising repression meets global resistance: Internet shutdowns in 2025"
    url: https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf
    publisher: Access Now
    date: 2026-03-28
authors:
  - anoni-net
---

HURIDOCS, which builds tools for human rights documentation, published a reflection on 15 September from an expert meeting held in Nairobi on documenting the war in Sudan, which brought together people working across documentation, technology, accountability and international justice. Documenters there face displacement, insecurity, intermittent connectivity, limited access to devices, and serious risks to themselves and the people whose experiences they record.

The meeting covered gathering initial information without a full witness interview, informed consent, keeping in touch with witnesses, security and connectivity, and how information moves from documenters to researchers and onward to prosecutors. According to the article, the worst outcome would be discovering, years later, that information which could have supported accountability cannot be used because a foreseeable evidentiary standard or chain-of-custody requirement was not met.

## Perspective {#perspective}

In the article, tool choice comes down to one question: is the cost of introducing this technology worth what it enables? Technology can help collect information offline and securely, preserve provenance, and connect information held in different systems. But every new tool takes time to learn, needs training, devices, connectivity and maintenance, changes workflows, can create dependence on vendors or infrastructure, and in high-risk settings may add new security considerations. The article also says the harder problem is continuity rather than innovation, because evidence has to survive long enough to be used.

Another question in the article is how information can move between civil society groups, researchers, investigators and accountability mechanisms without everyone using the same tool, and it says the goal is not one enormous system. For small teams, that makes interoperability more important than picking the single right platform.

Shutdowns make these trade-offs concrete across Asia as well as in Sudan. Access Now's count for 2025 records three shutdowns in Sudan during the conflict, including one during school exams in July, when the regulator also blocked WhatsApp voice and video calls nationwide, but the highest totals were in Asia: 95 in Myanmar, 65 in India and 20 in Pakistan. Authorities publicly acknowledged a shutdown in only 33% of cases, India being the exception because its shutdown orders must be published by law. In places like these, a tool that needs a constant connection cannot be used during a shutdown.

HURIDOCS's own Uwazi is a concrete example of these trade-offs. It is an MIT-licensed database for organising human rights collections, still releasing updates as of 25 September, and it can run on your own server or on HURIDOCS hosting. It is also a web application that needs Elasticsearch and other components to self-host, and its bundled interface translations include Korean, Burmese and Thai but not Chinese.

Groups documenting abuses in risky environments can turn the article into a checklist: how many people it takes to learn and maintain a tool, whether it can exchange data with partners, whether it preserves provenance well enough for future evidentiary standards, and whether recording can continue when the network goes down.
