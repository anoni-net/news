---
title: Measurements of censorship and code security gaps in China's open-weight Qwen models
description: In October, two companies that publish modified versions of Qwen models each released their own measurements, one of censorship in answers to political questions in Chinese, the other of a gap in code security that follows the client named in the prompt. The findings concern people who ask Qwen political questions and developers who write code with Qwen3-Coder, whether the model runs locally or through a service. As of 1 November, we had found no third-party replication and no response from the Qwen team.
date: 2026-11-02T00:05:00+08:00
slug: qwen-political-censorship
categories:
  - censorship
regions:
  - CN
sources:
  - title: InterpreticAI/Qwen3.8-27B-Uncensored-v2 · Hugging Face
    url: https://huggingface.co/InterpreticAI/Qwen3.8-27B-Uncensored-v2
    publisher: Interpretic AI
    date: 2026-10-31
  - title: Chinese AI Writes Weaker Code for Beijing’s Adversaries. We Fixed It. A Qwen3-Coder Case Study
    url: https://www.hirundo.io/blog/qwen3-coder-vulnerabilities
    publisher: Hirundo
    date: 2026-10-21
  - title: hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized · Hugging Face
    url: https://huggingface.co/hirundo-io/Qwen3-Coder-30B-A3B-Instruct-Westernized
    publisher: Hirundo
    date: 2026-10-13
  - title: "Westernizing Qwen: Measuring and Mitigating Geopolitical Alignment in Chinese Open-Weight LLMs"
    url: https://www.hirundo.io/blog/westernizing-qwen
    publisher: Hirundo
    date: 2026-10-05
  - title: Political censorship in large language models originating from China
    url: https://doi.org/10.1093/pnasnexus/pgag013
    publisher: PNAS Nexus
    date: 2026-02-17
  - title: Qwen/Qwen3.8-27B
    url: https://huggingface.co/Qwen/Qwen3.8-27B
    publisher: Qwen
    date: 2026-08-05
  - title: Qwen/Qwen3-Coder-30B-A3B-Instruct
    url: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
    publisher: Qwen
    date: 2025-07-31
  - title: Chinese Open Source Model Roundup
    url: https://speechmap.substack.com/p/chinese-open-source-model-roundup
    publisher: SpeechMap
    date: 2025-05-01
  - title: 生成式人工智能服务管理暂行办法
    url: https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
    publisher: Cyberspace Administration of China
    date: 2023-07-13
  - title: 卓揆：公務機關全面禁用Deepseek AI 服務
    url: https://www.ey.gov.tw/Page/9277F759E41CCD91/3ce9fe8f-2f5f-4d1d-8176-6fa4cf622b82
    publisher: Executive Yuan
    date: 2025-02-03
  - title: 公務機關全面禁用DeepSeek AI 服務，未限制一般民間使用
    url: https://moda.gov.tw/ACS/press/news/press/15296
    publisher: Administration for Cyber Security, Ministry of Digital Affairs (Taiwan)
    date: 2025-02-20
  - title: 政务领域人工智能大模型部署应用指引
    url: https://www.cac.gov.cn/2025-10/10/c_1761819469929310.htm
    publisher: Cyberspace Administration of China
    date: 2025-10-10
  - title: 中央网信办、国家发展改革委印发《政务领域人工智能大模型部署应用指引》
    url: https://www.cac.gov.cn/2025-10/10/c_1761819469876932.htm
    publisher: Cyberspace Administration of China
    date: 2025-10-10
  - title: Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust
    url: https://elaw.klri.re.kr/eng_mobile/viewer.do?hseq=71019&key=&type=new
    publisher: Korea Legislation Research Institute
  - title: MSIT Releases Guidelines on Ensuring AI Transparency
    url: https://www.msit.go.kr/eng/bbs/view.do?sCode=eng&mId=4&bbsSeqNo=42&nttSeqNo=1215
    publisher: Ministry of Science and ICT (South Korea)
  - title: Bias in Qwen3-Coder Model
    url: https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html
    publisher: Schneier on Security
    date: 2026-10-26
authors:
  - anoni-net
---

Two companies published measurements of Alibaba's Qwen family of open-weight models in late October (open-weight models are models whose files are public and can be downloaded and run on your own computer). Interpretic AI measured how often Qwen3.8-27B censors its answers to political questions in Chinese, and on 31 October released a version with the censorship removed on Hugging Face. According to measurements Hirundo published on its blog on 21 October, the security of the code Qwen3-Coder writes changes with the client named in the system prompt (the instructions a developer gives the model in advance), and the company has also released a modified version.

Both studies come from companies that publish the modified models, and Hirundo also evaluates and fixes models for organisations that run open-weight models. As of 1 November we had found no third-party replication, so all the figures below are each company's own measurements. Interpretic's measurements matter to people who ask Qwen political questions, and Hirundo's to developers who write code with Qwen3-Coder.

According to Interpretic's model page, the test put to the model, in Chinese, a set of 145 political questions that two researchers published in the journal PNAS Nexus, and another language model judged whether each answer was censored. Of the 113 politically sensitive questions in the set, 98 answers from the original Qwen3.8-27B were judged censored (86.7%), against 4 (3.5%) for the modified version. The model page does not say which model did the grading or whether anyone checked samples by hand, and it describes the removal only as a "targeted weight edit", with no paper or code. Interpretic lists as limitations that the political questions were tested only in Chinese, and cautions that a substantive answer is not necessarily a correct one.

The question set comes from a paper published in February 2026, in which the researchers compared foundation models developed in China with those developed elsewhere. According to the abstract, models developed in China refused more of the 145 political questions, gave shorter answers and gave more inaccurate ones. Every model refused more often when asked in Chinese than in English, but the gap between languages was smaller than the gap between Chinese and non-Chinese models.

According to Hirundo's blog, the study asked Qwen3-Coder-30B-A3B-Instruct to write the same web service again and again, with user registration, login and storage of private text. Each time, only the one sentence in the system prompt saying who the code was for changed, naming a neutral client, a US defence contractor, a Chinese defence contractor or a Hong Kong pro-democracy group. The finished apps were run on BaxBench, a public benchmark from ETH Zurich and LogicStar, and an app counted as exploitable if at least one off-the-shelf attack against it succeeded.

Apps written for the US defence contractor were exploitable 70% of the time, against 59% for the Chinese defence contractor. On private data leaks, nearly half of the apps written for the Hong Kong pro-democracy group let any logged-in user read everyone's private data, against about a third for the neutral client (a relative increase of 28%, as the blog calculates it). In the group whose prompts also included security instructions, 74% of the apps for the US contractor were exploitable, against 59% for the neutral client. According to the blog's statistical tests, none of the three gaps is likely to be due to chance.

The Q&A in the blog's appendix also states that the study cannot tell whether anyone put the gap into the model on purpose. Small models write vulnerable code anyway, and about a third of the neutral client's apps leaked as well, so what the study measured is the extra risk on top of that. Only one model and one task were tested, and the task was the one with the clearest gap in a small sample of 11 tasks. The US and Hong Kong groups were deliberately chosen edge cases.

Hirundo's modified model is public on Hugging Face, and its model page describes the method as behavioral unlearning (extra training that makes a model forget a specific behaviour while keeping its other abilities). According to the blog, on CCPC-500, a 500-question benchmark Hirundo built itself, the share of answers judged to contain censorship, bias or propaganda fell from 46.6% to 4.0%, and the three code gaps were no longer significant. In other comparisons in the appendix, the modified model still showed one significant gap for the US contractor against the neutral client, and in the blog's reading the effect moves from the country to the type of organisation. On ten other programming tasks, the shares of apps that worked and of apps that were exploitable were both close to those of the original model.

## Perspective {#perspective}

A language model's answers depend on its training data and on alignment, the later stage of training that makes a model answer according to the developer's rules. Both studies measured by asking large numbers of questions and computing proportions from the output, and neither examined training data and alignment separately. Hirundo's blog argues that the modified model's results prove the code gaps sit in the model weights, and the claim rests on the same company's own removal experiment.

SpeechMap, a public research project, tested the earlier Qwen3 generation in May 2025, and according to its roundup Qwen3's open-weight models were broadly censored on topics critical of China. The censorship was most thorough with questions asked in Chinese, present in English too, and appeared in Finnish only in some cases and less consistently. The same roundup records a high number of API errors from the commercial Qwen-Max, which SpeechMap reads as an additional layer of censorship at the API. From this we infer that when a model is used through a service, the answers may be shaped both by the model itself and by filtering on the service side.

China's Interim Measures for the Management of Generative Artificial Intelligence Services took effect on 15 August 2023, and Article 4 requires that providing and using generative AI services must not generate content inciting subversion of state power or the overthrow of the socialist system, among other categories. Under Article 2, research and application that do not provide services to the public in mainland China fall outside the Measures, and we found no provision specifically on publishing model weights. The researchers behind the PNAS Nexus paper caution that their study is observational and cross-sectional (it compares different models at a single point in time, without experiments) and "does not establish a causal linkage between regulatory pressures and censorship behaviors of China-originating LLMs".

On 3 February 2025, Taiwan's Executive Yuan required all public agencies to stop using DeepSeek AI services, and its press release noted that the security risk of data being uploaded to China had been neither clarified nor ruled out, and that the model's training involved data bias such as ideological censorship. According to the Administration for Cyber Security on 20 February 2025, the ban covered cloud services, apps and locally downloaded use, and at the time placed no restriction on use by the general public. The notices named DeepSeek, and we found none naming Qwen.

We, a community based in Taiwan, compared rules on generative AI from mainland China, Taiwan and South Korea, and neither the Taiwanese nor the South Korean rules discussed here regulate the political position of a model's answers. Besides Article 4 of the Interim Measures, mainland China has guidelines on deploying large AI models in government work, issued by the Office of the Central Cyberspace Affairs Commission and the National Development and Reform Commission and published on 10 October 2025 as a reference for government departments' own use, which call on those departments to use mature models and services that have completed filing with the cyberspace authorities for general-purpose tasks such as question answering and drafting documents (filing is a condition of entry, and the guidelines do not say what it examines). Taiwan's DeepSeek ban works on use instead, limiting which products public agencies may use. Article 31 of South Korea's Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust, in full force since 22 January 2026, requires a business providing generative AI to label the output as generated by generative AI, and according to the Ministry of Science and ICT, fact-finding investigations and penalties under this transparency provision are deferred for a grace period of at least one year (checked on 1 November).

In Interpretic's tests, the modified model refused 95 of 100 harmful requests, down from 100, and its scores on general ability tests dropped slightly, side effects that anyone thinking of switching to it has to weigh. Both companies' modified models keep the original's Apache 2.0 licence, but Interpretic published no paper or code, and Hirundo described only the category of its method. Hirundo's blog states that it intends to release CCPC-500, but when we checked on 1 November the dataset's address could not be accessed (it returned a 401 error), so we cannot confirm that it is public. According to SpeechMap's roundup of May 2025, third-party modifications of the Chinese open-source models of the time had brought clear improvements in English and only modest ones in Chinese.

For people who use Qwen to look up sensitive subjects such as politics or history, we suggest putting the same question to models from different sources, then checking the answers against news coverage and primary materials. According to both the paper's abstract and SpeechMap, asking in Chinese produced more refusals or censorship, and from this we infer that asking again in another language may produce a different answer, though the paper also notes that the language gap is smaller than the gap between Chinese and non-Chinese models. None of these studies evaluated whether such approaches recover censored content, and questions that were not tested are not necessarily free of bias (our inference).

Developers writing code with Qwen3-Coder or any other model still need to review and test it separately before it goes into production. According to Hirundo's blog, adding security instructions to the prompt did not remove the gap, and common static analysis tools may not catch this kind of leak, where a logged-in user can read other people's data. On the ten other tasks, about a quarter of the apps written by the modified model were still exploitable, and the neutral client's apps leaked too (see above). From this we infer that, whichever version you use, access control checks are a good place to start a review.

As of 1 November, we had found no public response from Alibaba or the Qwen team to either study or to the paper. In early December, it will be worth watching whether any third party replicates the two companies' measurements, whether CCPC-500 is published, and whether the Qwen team responds.
