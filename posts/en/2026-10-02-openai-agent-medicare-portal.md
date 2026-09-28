---
title: OpenAI agent breach of an Australian Medicare statistics portal
description: "An OpenAI agent bypassed access controls on an Australian Medicare statistics portal in June and wrote files to its server. The government learned of it in September, via a public inbox. No personal information is believed to have been accessed."
date: 2026-10-02T07:05:00+08:00
slug: openai-agent-medicare-portal
sources:
  - title: Australia launches urgent review after OpenAI program hacks government health portal
    url: https://www.bbc.com/news/live/cvgl73pxgndwt
    publisher: BBC News
    date: 2026-09-24
  - title: "OpenAI ‘climbed the fence’: Taskforce scrambles after long delays flagging Medicare hack"
    url: https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html
    publisher: The Sydney Morning Herald
    date: 2026-09-24
  - title: Press conference - New York
    url: https://www.pm.gov.au/media/press-conference-new-york
    publisher: Prime Minister of Australia
    date: 2026-09-24
  - title: Press Conference, Sydney
    url: https://www.minister.defence.gov.au/transcripts/2026-09-24/press-conference-sydney
    publisher: Australian Minister for Defence
    date: 2026-09-24
  - title: The Hugging Face incident and other third-party impact from misaligned models
    url: https://openai.com/hugging-face-incident-and-misalignment/
    publisher: OpenAI
    date: 2026-09-25
  - title: Factsheet - Model AI Governance Framework for Agentic AI
    url: https://www.imda.gov.sg/-/media/imda/files/news-and-events/media-room/media-releases/2026/01/factsheet-model-ai-governance-framework-for-agentic-ai.pdf
    publisher: IMDA
    date: 2026-01-22
  - title: 資通安全事件通報應變及演練辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=A0030305
    publisher: 全國法規資料庫
    date: 2026-01-05
  - title: 国家网络安全事件报告管理办法
    url: https://www.cac.gov.cn/2025-09/15/c_1759583017717009.htm
    publisher: 国家互联网信息办公室
    date: 2025-09-15
  - title: 管理多個 Chrome 設定檔
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hant
    publisher: Google Chrome 說明
regions:
  - AU
authors:
  - anoni-net
---

On 24 September, Australia's prime minister announced in New York that an OpenAI agent had gained unauthorised access to the Medicare Statistics Reporting Service portal run by Services Australia. It accessed public and non-public files and wrote files to the internal server, and the Australian Signals Directorate (ASD) is assisting a forensic investigation.

The portal, taken offline by 24 September, held non-sensitive statistics such as spending, and no personal information is believed to have been accessed. The agent was researching public medicine spending for an internal OpenAI evaluation and, when refused, found other ways around the blocks.

The breach happened on 18 June. OpenAI became aware of it during a broader review in August and on 10 September emailed a public Services Australia inbox that is checked once a day. The agency saw it the next day and reported it to the Australian Cyber Security Centre on 15 September. The prime minister called the notification unacceptable, and a taskforce will review cyber defences and penalties. An OpenAI spokesperson said its models accessed "several Australian government websites and services" and "took actions we did not intend". Its incident page says it has notified dozens of third parties and lists anonymised categories including access control bypass and use of exposed credentials.

## Perspective {#perspective}

The techniques in OpenAI's list, such as trying a different web address, changing details in a request or riding on a login session with more access than expected, are ordinary access control weaknesses that a human could exploit just as well. According to The Sydney Morning Herald, the Medicare portal was an old website used mainly by academics. Any organisation running websites can start by listing older systems that are still online but rarely maintained, retiring the ones nobody needs and checking that non-public files on the rest really require a login.

Most of the delay in Australia came before any agency knew. Rules elsewhere in the region set deadlines only after that point. Taiwan's Cyber Security Incident Notification, Response and Drill Regulations require government agencies to report an incident within one hour of becoming aware of it. Mainland China's Measures for National Cybersecurity Incident Reporting, in force since 1 November 2025, give network operators one hour for incidents involving critical information infrastructure and four hours for most others, for incidents rated "relatively major" or above. The mainland measures also encourage organisations and individuals to report such incidents they learn of, and the cyberspace authorities run a 12387 hotline and website to receive them. Neither document sets a deadline for an outsider like OpenAI, and in this case the notice sat in a general inbox before reaching the agency responsible for cyber security.

Singapore has taken a different route. In January its Infocomm Media Development Authority (IMDA) published a voluntary Model AI Governance Framework for Agentic AI, under which organisations are advised to bound risks early through design choices such as limits on an agent's autonomy, tools and data access. That advice scales down to individuals. When you let an AI agent browse or fill in forms for you, what it can reach is whatever your login sessions and permissions allow. Desktop Chrome lets you add a separate profile from the profile icon at the top right. Running the agent there, signed in only to the accounts the task needs, keeps an unexpected detour from reaching everything else you use.
