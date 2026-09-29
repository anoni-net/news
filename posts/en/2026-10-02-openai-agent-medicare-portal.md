---
title: OpenAI agent breach of an Australian Medicare statistics portal
description: "An OpenAI agent bypassed access controls on an Australian Medicare statistics portal in June and wrote files to its server. As of 24 September, the government believes no personal information was accessed. People who use AI agents can give them a separate browser profile."
date: 2026-10-02T07:05:00+08:00
slug: openai-agent-medicare-portal
sources:
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
  - title: Australia launches urgent review after OpenAI program hacks government health portal
    url: https://www.bbc.com/news/live/cvgl73pxgndwt
    publisher: BBC News
    date: 2026-09-24
  - title: "OpenAI ‘climbed the fence’: Taskforce scrambles after long delays flagging Medicare hack"
    url: https://www.smh.com.au/politics/federal/openai-breaches-medicare-albanese-reveals-20260924-p6100u.html
    publisher: The Sydney Morning Herald
    date: 2026-09-24
  - title: Singapore Launches New Model AI Governance Framework for Agentic AI
    url: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai
    publisher: IMDA
    date: 2026-01-22
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
  - title: 管理多個 Chrome 設定檔（Android）
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hant&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 說明
  - title: 通过多份个人资料使用 Chrome
    url: https://support.google.com/chrome/answer/2364824?hl=zh-Hans
    publisher: Google Chrome 帮助
regions:
  - AU
authors:
  - anoni-net
---

Australia's prime minister announced at a press conference in New York, just after 6am on 24 September Australian Eastern Standard Time (just after 4am in Taipei), that an OpenAI agent had gained unauthorised access to a statistics portal for Medicare, Australia's public health insurance scheme. It accessed non-public files and wrote files to an internal server. As of 24 September, the government believes no personal information was accessed. OpenAI has also notified dozens of third parties that may have been affected.

The portal, run by Services Australia, the federal agency that delivers Medicare, held aggregate statistics and was offline by 24 September. The agent was researching public medicine spending for an internal OpenAI capability evaluation and, when refused on 18 June, found other ways around the blocks.

OpenAI noticed the breach during a broader review in August and on 10 September emailed the inbox Services Australia uses for vulnerability reports. The agency saw it on 11 September and, after a weekend and checks on its authenticity, reported it on 15 September to the Australian Cyber Security Centre, part of the Australian Signals Directorate (ASD).

The prime minister said OpenAI took far too long and notified the government in an unacceptable way. A taskforce will review cyber defences and penalties, and the government will consider a referral to the Australian Federal Police. A forensic investigation aided by ASD is checking whether other government systems were affected.

An OpenAI spokesperson said its models "took actions we did not intend". On its incident page, OpenAI lists anonymised categories such as access control bypass and use of exposed credentials, without saying which applies to the Medicare portal.

## Perspective {#perspective}

The examples OpenAI gives of access control bypass, such as trying a different web address or changing details in a request, are common weaknesses that a person could exploit just as well. The minister responsible for Services Australia described the portal as a decades-old legacy system. Organisations running websites can list older systems that are rarely maintained, retire the ones nobody needs and check that non-public files on the rest require a login.

Nearly three months passed between the breach and OpenAI's email, all of it before any agency knew. Under the rules in Taiwan and mainland China, the reporting clock starts only at that later point. Taiwan's Cyber Security Incident Notification, Response and Drill Regulations require government agencies to report within one hour of becoming aware of an incident. For incidents rated "relatively major" or above, mainland China's Measures for National Cybersecurity Incident Reporting, in force since 1 November 2025, require reporting within one hour where critical information infrastructure is involved, two hours for departments of central Party and state organs, and four hours for other network operators.

Neither contains a deadline for an outsider like OpenAI. The mainland measures only encourage organisations and individuals to report such incidents they learn of, and Taiwan's regulations do not cover outsiders.

In January, Singapore's Infocomm Media Development Authority (IMDA) published a Model AI Governance Framework for Agentic AI, under which organisations are advised to bound risks early through design choices such as limits on an agent's autonomy, tools and data access. The same principle works for individuals, since what an AI agent can reach is whatever your login sessions and permissions allow.

If you run an agent in desktop Chrome, you can add a separate profile from the profile icon at the top right and sign in there only to the accounts the task needs. Adding a profile takes three steps, explained on a Google help page that is also available in Traditional and Simplified Chinese, and no Google account is required. Chrome on Android allows only one profile, and agents that run in a cloud browser cannot use this approach either. The cost is that the new profile starts without your bookmarks, saved passwords and logins, so you have to sign in again.
