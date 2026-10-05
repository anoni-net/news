---
title: GLM-5.3's exploit-writing ability and open-weight safeguards
description: Anthropic's report on Zhipu's open-weight model GLM-5.3, published on 29 September, says the model can write working browser exploits and that, in simulated tests, cover stories and similar techniques got past its safeguards. Zhipu's release notes say the public weights carry only the model's own safeguards and that strong defensive capability should not stay with a few organisations. What most readers can do is restart their browser promptly after updates.
date: 2026-10-10T00:00:00+08:00
slug: glm-5-3-cyber-capabilities
categories:
  - security
sources:
  - title: GLM-5.3 and the spread of advanced cyber capabilities
    url: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
    publisher: Anthropic
    date: 2026-09-29
  - title: "Preparing GLM-5.3 for Open Release: A Responsible Path to Cyber Defense"
    url: https://x.com/Zai_org/article/2088280509474320693
    publisher: Z.ai
    date: 2026-08-14
  - title: "GLM-5.3: Frontier Coding with Emergent Cyber Capabilities"
    url: https://z.ai/blog/glm-5.3
    publisher: Z.ai
    date: 2026-08-14
  - title: CAISI’s Assessment of Z.ai’s GLM-5.3 Cyber Capabilities
    url: https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities
    publisher: NIST
    date: 2026-09-17
  - title: How Far Behind the Frontier are Leading Open Weight Models on Cyber?
    url: https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
    publisher: AI Security Institute
    date: 2026-07-17
  - title: More than half of AI Safety Institute assessed models are open-weight, 58 percent Chinese
    url: https://www.digitaltoday.co.kr/en/view/105031/more-than-half-of-ai-safety-institute-assessed-models-are-open-weight-58-percent-chinese
    publisher: Digital Today
    date: 2026-09-18
  - title: 讓你的AI懂臺灣！數位發展部公布臺灣主權AI評測結果，攜手產官打造可信任AI生態系
    url: https://moda.gov.tw/ADI/news/latest-news/20538
    publisher: Administration for Digital Industries, Ministry of Digital Affairs
    date: 2026-09-02
  - title: Stable Channel Update for Desktop
    url: https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_0153744567.html
    publisher: Google
    date: 2026-06-08
  - title: Update Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=en&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: Manage Chrome safety and security
    url: https://support.google.com/chrome/answer/10468685?hl=en&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: Adjusting security levels in Tor Browser to balance privacy and usability
    url: https://support.torproject.org/tor-browser/features/security-levels/
    publisher: Tor Project
  - title: 更新 Google Chrome
    url: https://support.google.com/chrome/answer/95414?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 管理 Chrome 的安全性
    url: https://support.google.com/chrome/answer/10468685?hl=zh-Hant&co=GENIE.Platform%3DDesktop
    publisher: Google
  - title: 調整 Tor Browser 安全等級以平衡隱私與可用性
    url: https://support.torproject.org/zh-TW/tor-browser/features/security-levels/
    publisher: Tor Project
authors:
  - anoni-net
---

On 29 September, the US AI company Anthropic published tests of GLM-5.3, a language model released in August by China's Zhipu (known outside China as Z.ai). The report concludes that GLM-5.3 can find software vulnerabilities and turn them into working exploits on its own, close to the level of Claude Mythos Preview, which Anthropic offers only to vetted cyber defenders. It also found that, in a simulated environment, simple techniques such as cover stories got past GLM-5.3's safeguards. Most readers will never use the model directly, and what they can do has not changed: restart the browser promptly after updates.

GLM-5.3's weights, the model's parameters, have been public since late August, so anyone can download and modify them. Zhipu's notes posted on X on 14 August state that, once weights are public, no developer can guarantee control over every downstream modification or use, and that strong defensive capability cannot stay with a few well-resourced organisations.

Anthropic ran GLM-5.3 on ExploitBench, a benchmark built on known flaws in V8, Chrome's JavaScript engine, where GLM-5.3 produced end-to-end exploits in 50 of 410 attempts, against 56 for Mythos Preview. On Anthropic's internal benchmark of open-source projects, GLM-5.3 achieved a full control-flow hijack in 4% of trials, against 6% for Mythos Preview and none for earlier models such as Claude Opus 4.6 and GLM-5.2. NIST's Center for AI Standards and Innovation (CAISI) assessed on 17 September that GLM-5.3 was the most cyber-capable open-weight model released up to that point. On an aggregate of CAISI's cyber benchmarks, it trailed the US frontier, which includes models released only to vetted users, by about four months.

Over about a day and with limited human attention, a researcher used GLM-5.3 to find several unknown flaws in the JavaScript engine of a popular browser, which the report does not name. The model chained them into a web page that reads arbitrary files from the computer of anyone who opens it in the browser's Linux build. Anthropic believes other platforms may also be affected, though exploitation there may be harder. The flaws have been reported to the maintainer.

In a second session, the smaller GLM-5.3-Flash chained public details of the Chrome flaw `CVE-2026-11645` and another known flaw into a working exploit, using 20 minutes of a researcher's attention and eight hours of model time, about US$20.40 at Zhipu's API prices; Google fixed `CVE-2026-11645` on 8 June and said an exploit for it exists in the wild.

According to the report, the exploit-writing tasks did not trigger refusals; refusals came when the model was asked to build malware or attack remote targets. In a simulation, GLM-5.3 refused every direct request to attack a remote system. A red-team cover story got it to start connecting to the target 64% of the time and prefilling its reasoning 92%, while "abliteration", a change to the weights that strips out refusals, brought the rate to 100%.

Anthropic's first abliteration took about 2,200 GPU hours (roughly US$4,400), and it estimates an experienced team would need about 600 (roughly US$1,200). The modified model scored the same on a general science test and a few percent lower on a sampled cyber benchmark. The report says several developers released abliterated versions within days of the model's release.

In Anthropic's own testing, safeguarded Claude models used through the API blocked the cover story, and the other two techniques are not generally feasible against Claude, since its API offers no way to prefill reasoning and its weights are not released. No model-generated code ran in these bypass tests, which the report calls an imperfect measure of real-world behaviour.

## Perspective {#perspective}

A model's tendency to refuse harmful requests is trained into the same weights as everything else it can do. When a model is served through an API, its developer can add filters and monitoring around it. Once the weights are public, people run the model on their own machines without those outer layers, and nobody needs the developer's permission to change the weights.

Zhipu's notes describe three layers of protection: a request classifier, a monitor that assesses risk during task execution, and the model's own safety training. The first two apply to Zhipu's hosted services and do not come with the model when people run it themselves, so the public weights carry only the third. The notes add that model-level safeguards raise the barrier to abuse but cannot provide absolute control.

Citing the dual-use risk, Zhipu planned a staged release starting with vetted security partners. Its launch blog, published on 14 August, said the weights would follow two weeks later, once safety evaluation and hardening were complete.

Anthropic's report assesses that GLM-5.3 was released without meaningful safeguards, unlike other similarly capable models, all of which shipped with safeguards or through limited-access programmes. It also says governments should safety-test sufficiently capable models, including GLM-5.3's successors. As of 5 October, we could not find a public response from Zhipu to the report.

Anthropic writes that defenders should have frontier models at least as good as their adversaries', and it is widening access for vetted defenders through programmes such as Project Glasswing. Zhipu, which writes that strong defensive capability should reach open-source maintainers and independent researchers, launched the OpenVuln initiative alongside GLM-5.3, working with maintainers to audit important open-source projects and support disclosure and fixes.

The UK's AI Security Institute set out both the benefits and the risks in July. Open-weight models can be hosted privately with no data returning to the provider, and cannot be changed or withdrawn by it, but released safeguards can be removed and copies cannot be recalled. Testing GLM-5.2 and other models released by June, the institute measured open models trailing the closed frontier on cyber tasks by 4 to 7 months, down from 6 to 10 months for most of 2025. It describes that gap as preparation time for defenders with access to the most capable closed models.

Who tests models like these, and for what, differs between South Korea and Taiwan. South Korea's AI Safety Institute assessed 34 models from January to August, 19 of them open-weight and 11 of those Chinese, including Zhipu's GLM, and depending on the model its checks covered cybersecurity and web exploits. Digital Today reported on 18 September that the institute ran its in-house assessments on 16 Nvidia H200 GPUs and was short of staff and computing for the number of models it needed to cover. In Taiwan, where we are based, the Ministry of Digital Affairs published a model evaluation on 2 September that measures understanding of Taiwanese language, society and values; the announcement does not mention cyber capability.

Readers cannot control who uses these models, but they can shorten the time between a fix being published and their own browser installing it. In the experiment above, GLM-5.3-Flash needed eight hours of run time to turn public details of known flaws, one of them patched in June, into an exploit. Chrome prepares updates in the background but applies them only on restart. Under Help, About Google Chrome, a Relaunch button means an update has not been applied yet.

Updates do not help against flaws that have not been fixed, so people who often visit unfamiliar sites can also limit what web page code can use. In Chrome, under Privacy and security, Security, "Manage JavaScript optimization & security" can be set to "Automatically disable JavaScript optimizers on unfamiliar sites", which may make some sites slower. In Tor Browser, the Safer level disables JavaScript on non-HTTPS sites and Safest disables it by default on all sites, and some sites will break. These settings narrow attacks that use web page code against the browser, and do nothing against a phishing page that asks for your password.

Questions worth following: what level of safeguards is enough for an open-weight model, and whether governments should test such models for cyber capability, and who. Whether the preparation time the AI Security Institute describes is long enough for flaws to be fixed first. And whether under-resourced open-source projects can get tools on a par with those their attackers use.
