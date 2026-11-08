---
title: Generative AI in transnational repression cases and the response from AI companies
description: Anthropic's September threat intelligence report describes state-linked actors using Claude for surveillance, some of it aimed at dissidents living abroad. In an October commentary for Just Security, Citizen Lab researchers analysed the report and urged AI companies to act on disclosure and notification, detection and refusal, and evidence preservation. Neither document offers settings advice for ordinary users.
date: 2026-11-12T00:05:00+08:00
slug: genai-transnational-repression
categories:
  - civil-society
sources:
  - title: "Detecting and countering misuse of AI: September 2026"
    url: https://www.anthropic.com/threat-intelligence-report-september-2026
    publisher: Anthropic
    date: 2026-09-10
  - title: How Generative AI is Scaling Transnational Repression
    url: https://www.justsecurity.org/159245/how-generative-ai-scaling-transnational-repression/
    publisher: Just Security
    date: 2026-10-12
  - title: How Generative AI is Scaling Transnational Repression
    url: https://citizenlab.ca/how-generative-ai-is-scaling-transnational-repression/
    publisher: Citizen Lab
    date: 2026-10-22
  - title: 衆法 第221回国会 26号 審議経過
    url: https://www.shugiin.go.jp/internet/itdb_gian.nsf/html/gian/keika/1DE2AAA.htm
    publisher: House of Representatives, Japan
  - title: 公職選挙法及び特定電気通信による情報の流通によって発生する権利侵害等への対処に関する法律の一部を改正する法律案
    url: https://www.shugiin.go.jp/internet/itdb_gian.nsf/html/gian/honbun/houan/g22105026.htm
    publisher: House of Representatives, Japan
  - title: Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust
    url: https://elaw.klri.re.kr/eng_mobile/viewer.do?hseq=71019&key=&type=new
    publisher: Korea Legislation Research Institute
    date: 2025-01-21
  - title: MSIT Releases Guidelines on Ensuring AI Transparency
    url: https://www.msit.go.kr/eng/bbs/view.do?sCode=eng&mId=4&bbsSeqNo=42&nttSeqNo=1215
    publisher: Ministry of Science and ICT, South Korea
  - title: 互联网信息服务深度合成管理规定
    url: https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm
    publisher: Cyberspace Administration of China
    date: 2022-12-11
authors:
  - anoni-net
---

Anthropic's threat intelligence team published "Detecting and countering misuse of AI: September 2026" on 10 September. Its surveillance chapter lists a series of operations the company found and disrupted between January and July 2026, in which, according to the report, state-linked organisations, contractors working for states and commercial spyware vendors used Claude to build and run surveillance. The report classifies some of these cases as transnational repression aimed at dissidents and diaspora communities living abroad.

Three Citizen Lab researchers analysed the report in a commentary published by Just Security on 12 October, and Citizen Lab's website republished a summary on 22 October. Every case the commentary discusses comes from Anthropic's report. Both documents deal with how attackers use AI services, and neither offers settings advice for ordinary users.

The researchers cite Freedom House's definition, under which digital transnational repression is the use of digital technology by governments to intimidate and silence dissidents in exile and in diaspora communities. Their earlier interview research with affected people found that such threats cause fear and isolation, and lead people to self-censor and withdraw from advocacy.

The researchers group the report's cases into four shifts. The first is cost: digital repression used to depend on language skills, trained intelligence analysts and software engineers, and the researchers read the cases as showing that AI can replace part of that. The second is the processing of open information, since diaspora communities leave large amounts of data on social media, messaging apps, public databases and organisational websites. An AI assistant can compile that scattered data into intelligence reports used to reconstruct personal networks, infer political leanings and locate people, and even to flag their vulnerabilities.

The third shift is building models into fixed workflows, so that a handful of staff can oversee repeated, partly automated surveillance reporting; in one case the system automatically reviewed 15 to 30 or more foreign media articles a day. Fourth, surveillance output can support physical surveillance, coercion, the recruitment of informants and the disruption of civil society groups' work. The researchers also note that the report does not show this reconnaissance led to physical attacks.

According to the report's cases, the model was also used to translate and write messages in dialect, generate multilingual posts for fake online personas, and write code for surveillance tools such as browser extensions. One operation was still at a trial stage and had more than 255 synthetic social media accounts ready, which the report takes as a sign that the accounts were prepared in advance for later use. Unlike the follow-on surveillance described in an earlier news investigation, the report found no evidence that these accounts had been used against real targets before Anthropic banned them. Another operation planned mass reporting and bot amplification against journalists at an exile media outlet, and the report describes this as a plan rather than something carried out.

According to the report, in the same operation that planned mass reporting against the exile journalists, Claude refused several requests for covert interrogation and for generating fake personas at scale. In a case the commentary classifies as domestic surveillance, Claude first refused to produce a surveillance report, but after the request was rephrased the model still produced guidance naming 10 civilians. In another domestic case the commentary mentions, the surveillance system ran entirely on a local model, and Anthropic banned the account but could not disable the system already deployed.

Anthropic's usage policy prohibits using Claude for non-consensual surveillance and profiling, and for violating individuals' civil liberties and human rights. According to the report, the related accounts were banned in every case, and the company improved its ability to detect similar techniques. Where an operation's impact extended beyond the platform, Anthropic shared identifiers and intelligence with industry partners and authorities as appropriate. The report also mentions that some actors used VPNs to get around Anthropic's regional restrictions.

The researchers write that the report reflects only what one company could see and detect over a short period, and that confidence in some attributions is limited. In one case in the report, the actor is assessed only with low confidence to be a contractor working for a state security agency rather than the agency itself.

## Perspective {#perspective}

The researchers note that earlier warnings about AI in transnational repression mostly extrapolated from technical capability and had few concrete cases behind them, and they regard Anthropic's report as offering rare operational detail. They suggest that detection should not rely on easily recognised repression keywords, and should instead flag the combination of social media monitoring, geolocation, vulnerability profiling and inference of political leanings, since together these capabilities can point to a transnational repression workflow.

The researchers base their recommendations on the UN Guiding Principles on Business and Human Rights (UNGPs), which require companies to address adverse human rights impacts they are involved in. The commentary argues that AI companies should treat transnational repression as a threat category of its own, separate from domestic surveillance and influence operations, and act in three areas. As of 8 November, we found no public response to the commentary from Anthropic, OpenAI, DeepMind or xAI. On the companies' side, the only document available is Anthropic's September report, which predates the commentary and is not a response to its recommendations.

On the first area, disclosure and notification, Anthropic's report is itself a public disclosure, and its account of the response says information is shared with industry partners and authorities as appropriate. The researchers credit the report's detail and consider that OpenAI, DeepMind and xAI may encounter similar operations, though without standardised reporting there is nothing to assess. They also recommend notifying affected communities, and point out that Google and Apple already have processes for notifying the targets of state-backed attacks. Those notifications go to the companies' own users, whereas the people targeted through an AI service are not necessarily its users, so the researchers recommend community-level notification in formats and languages the recipients can understand.

On the second area, detection and refusal, the researchers credit Anthropic with repeatedly finding and stopping operations before large-scale deployment, while noting that in some cases a rephrased request got around a refusal. Anthropic's report describes improving detection of similar techniques in each case and feeding the investigation findings into its safeguards.

On the third area, evidence preservation, the researchers note that civil lawsuits and criminal investigations have already arisen from cases where digital transnational repression escalated into physical harm. They therefore argue that companies should keep detailed incident records, including attribution data, for future investigations. They also write that what should be kept depends on local law and remains contested.

Neither the commentary nor the Citizen Lab page offers practical advice for people who are targeted. Google and Apple each have processes for notifying the targets of state-backed operations, and the commentary treats them as a reference for AI companies setting up notification of their own.

We, a community based in Taiwan, compared these recommendations with the Asian rules on AI and online platforms we have checked, and the closest parallel to regular public reporting is in Japan. The Act Partially Amending the Public Offices Election Act and the Act on Responses to Infringement of Rights Caused by Distribution of Information through Specified Telecommunications (Act No. 58 of 2026), promulgated on 17 July 2026 and taking effect on 1 March 2027, requires large-scale specified telecommunications service providers to take measures against information that may harm the fairness of elections, under guidelines set by the Minister for Internal Affairs and Communications, and to publish how they implemented those measures each year. That duty is aimed at large platforms and election-related information and does not mention surveillance. South Korea's Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust (the AI Basic Act), which took full effect on 22 January 2026 with a grace period of at least one year for penalties under its transparency provision, requires generative AI providers to label their output (Article 31), which concerns disclosure to users rather than what a provider does when its tools are misused.

Mainland China already places a record-keeping duty on providers, with a different recipient. Under the Provisions on the Administration of Deep Synthesis of Internet Information Services (Order No. 12), issued by the Cyberspace Administration of China, the Ministry of Industry and Information Technology and the Ministry of Public Security and in force since 10 January 2023, a provider of deep synthesis services within mainland China that finds its service used to produce or spread false information must take rebuttal measures, keep the relevant records and report to the cyberspace authorities and other competent authorities (Article 11). The researchers want records kept for civil lawsuits and criminal investigations arising from harm to targeted people, whereas the Chinese rule names the cyberspace authorities as the recipient, and the duty is triggered by false information rather than by surveillance.

When reading other AI companies' threat reports, a few things are worth comparing: whether transnational repression is classified separately, what steps the response includes (banning accounts, improving detection, sharing intelligence), whether targeted communities are notified, and what records are kept. Another set of questions concerns effectiveness, since the researchers point out that some refusals were bypassed by rephrasing. When a system runs on a local model, banning the account does not stop it, so how early detection needs to happen to be useful is also worth comparing. The researchers note that the industry has no standardised reporting, and whether companies can be compared will depend on whether a common format is established.
