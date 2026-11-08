---
title: Scope and opt-out of model training on Gemini personal account chats
description: Keep Activity is on by default for Gemini personal accounts held by people 18 or over, and while it is on Google uses activity to train generative AI models, with a subset of chats going to human reviewers (per Google's help pages, checked on 8 November). With the setting off (feedback excepted) or in a Temporary Chat, chats are not used for training and are kept for 72 hours, while human-reviewed chats are kept for up to three years. The help pages do not distinguish between paid and free plans.
date: 2026-11-14T00:05:00+08:00
slug: gemini-chat-training
categories:
  - tracking
sources:
  - title: Gemini Apps Privacy Hub
    url: https://support.google.com/gemini/answer/13594961?hl=en
    publisher: Google
    date: 2026-10-26
  - title: Gemini 系列應用程式隱私權專區
    url: https://support.google.com/gemini/answer/13594961?hl=zh-Hant
    publisher: Google
    date: 2026-10-26
  - title: 管理及刪除 Gemini 系列應用程式活動記錄
    url: https://support.google.com/gemini/answer/13278892?hl=zh-Hant
    publisher: Google
  - title: 使用 Gemini 系列應用程式
    url: https://support.google.com/gemini/answer/13275745?hl=zh-Hant
    publisher: Google
  - title: 關於透過「連結的應用程式」享有的個人化體驗
    url: https://support.google.com/gemini/answer/16836988?hl=zh-Hant
    publisher: Google
  - title: 在 Gemini 系列應用程式中使用 Gem
    url: https://support.google.com/gemini/answer/15146780?hl=zh-Hant
    publisher: Google
  - title: 和 Gemini Live 自然對話
    url: https://support.google.com/gemini/answer/15274899?hl=zh-Hant
    publisher: Google
  - title: Generative AI in Google Workspace Privacy Hub
    url: https://support.google.com/a/answer/15706919?hl=en
    publisher: Google
    date: 2026-10-06
  - title: "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)"
    url: https://news.ycombinator.com/item?id=50363461
    publisher: Hacker News
    date: 2026-11-04
  - title: Manage & delete your activity in Gemini Apps
    url: https://support.google.com/gemini/answer/13278892?hl=en
    publisher: Google
  - title: Use Gemini Apps
    url: https://support.google.com/gemini/answer/13275745?hl=en
    publisher: Google
  - title: About personalization with Connected Apps
    url: https://support.google.com/gemini/answer/16836988?hl=en
    publisher: Google
  - title: Advisory Guidelines on Use of Personal Data in Generative AI
    url: https://www.pdpc.gov.sg/assets/143cb9d4-532e-4cca-9a77-bcc0415ca294
    publisher: Personal Data Protection Commission, Singapore
    date: 2026-07-20
  - title: 안전한 인공지능 개발을 위한 개인정보 활용 특례 신설 「개인정보 보호법」 개정안 국회 본회의 통과
    url: https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12391
    publisher: Personal Information Protection Commission, South Korea
    date: 2026-08-20
  - title: "개인정보 보호법 AI 특례 일부개정법률 공포: 시행 대비 실무 가이드"
    url: https://www.bkl.co.kr/law/insight/newsletter/6749
    publisher: BKL
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021
    publisher: Laws & Regulations Database of the Republic of China (Taiwan)
authors:
  - anoni-net
---

Keep Activity is on by default for anyone 18 or over who uses Gemini with a personal Google Account. While it is on, Google uses activity to improve its services and train generative AI models, and a subset of chats goes to human reviewers. The default is stated on Google's "Manage & delete your activity in Gemini Apps" help page and the uses on the Privacy Hub in the Gemini help center (checked on 8 November), and work or school accounts may be subject to different terms. A Hacker News post on 4 November about paid subscribers' chats also being used for training prompted discussion; the rules below come from Google's current documents, and our inferences are marked as such.

The Privacy Hub (Privacy Notice last updated 13 October 2026, privacy questions last updated 26 October) lists the uses of activity as providing, developing and improving services, including training generative AI models, and protecting Google, its users and the public. According to the same page, Gemini chats are not being used to show ads, Google will clearly communicate any change to that, and Google does not sell personal information.

With the setting on, chats, uploaded files and shared screens are saved in activity. Data from Connected Apps (which let Gemini use data from other Google apps and third-party services) and chats imported from other AI platforms are also used to improve services. Activity is auto-deleted after 18 months by default, and the period can be changed to 3 months, 36 months or no auto-delete. Audio and the videos and screenshares from Gemini Live (spoken conversation with Gemini) are not used to improve services by default and need a separate opt-in, while transcripts of Live chats and uploads shared with Live are used to improve services when Keep Activity is on.

Where the Privacy Hub mentions Google AI plans (Google's paid subscriptions), it lists only subscription information as data collected, and the sections on training and human review do not distinguish paid from free. We infer from this that both fall under the same notice. Google has not written that sentence, and as of 8 November we could not find a privacy document specific to Google AI plans.

Activity settings on work and school accounts are controlled by a Google Workspace administrator, and different rules may apply. The Generative AI in Google Workspace Privacy Hub (last updated 6 October) covers only qualifying Workspace editions, and under it customer data is not used to train models without the prior permission or instruction of the customer, meaning the subscribing organization. In the Gemini app on those editions, chats and uploaded files are not reviewed by human reviewers or otherwise used to train generative AI models outside the customer's domain without permission.

According to the Privacy Hub, human reviewers assess whether Gemini's responses were low-quality, inaccurate or harmful and suggest better ones. Chats are also reviewed to keep Gemini safe and to address violations of the Google Terms of Service. The page describes the reviewed portion only as a "subset" and gives no proportion.

Chats are disconnected from the account before being sent to Google's trained service providers for review. Reviewed chats and related data (such as language, device type and location info) are retained for up to three years, the page makes no distinction by reason for review, and deleting activity does not delete them. We infer that chats reviewed for protection purposes after the setting is turned off may also be kept for longer than 72 hours. Names or addresses a user types into a chat remain in the text, which is also our inference.

## Perspective {#perspective}

With Keep Activity left on, ordinary chats are kept for 18 months by default and used for training, and some are reviewed by humans. With it off, future chats are not used for training unless the user sends feedback, are not reviewed by humans to improve services, and are kept for 72 hours. Temporary Chat (a per-chat mode whose chats do not appear in activity or recent chats and cannot be reopened after leaving) has the same 72-hour retention and is likewise outside training and service-improvement review. None of the three changes Google's use of chats to protect Google, its users and the public, "including with help from human reviewers", with reviewed chats kept for up to three years, and Gemini settings do not control the processing of chats into anonymized data to improve Google services.

Keep Activity controls both chat storage and model training, and the help pages we read list no option to keep chats while excluding them from training. The Privacy Hub's sentences cover only future chats and do not address what happens to chats already in activity before the setting was turned off, including data already used for training. For the short-term retention after turning it off, the Privacy Hub lists responding to the user, processing feedback, and protecting Google, its users and the public, with a potential system failure as the example of why chats remain available.

Two statements sit side by side on the Privacy Hub: Gemini settings do not control processing into anonymized data, and with the setting off and no feedback submitted, future chats are not used to improve AI models. How they relate is not explained on the page.

If a user submits feedback while the setting is off, Google collects the feedback, the last 24 hours of chats, and any uploads and Connected Apps data in those chats. The feedback and associated chats are reviewed by specially trained teams and used, consistent with the Google Privacy Policy, to improve products and machine-learning technologies.

According to the activity help page, the Connected Apps still available with the setting off are Device assistance, Gemini Notebook (a service that holds notebook source files), Messages, Phone and WhatsApp. Chats created with Gems (custom items a user creates and saves to get responses suited to a particular need) are not saved, though the Gems stay in the account. Chats held while the setting is off cannot be looked up in activity afterwards.

People who would rather leave the setting on can use Temporary Chat case by case. It is not available in Gemini in Google Messages or Gemini in Chrome, or on work and school accounts. Inside a Temporary Chat, Gems, Connected Apps that require Keep Activity, and personalized responses are unavailable, and feedback cannot be given.

Whether chats can be used for training involves two concerns, users' control over their own data and product improvement. In the Privacy Hub, Google explains that reviewers' suggestions are used to help its models respond better in the future and asks users not to enter confidential information they would not want a reviewer to see or Google to use to improve its services. As of 8 November we could find no public response from Google to the Hacker News post, and no formal document from a consumer group or data protection authority on training with Gemini personal chats. This article presents only Google's side, from its own documents.

Singapore's Personal Data Protection Commission (PDPC) addresses training on data from a service's own users in its Advisory Guidelines on Use of Personal Data in Generative AI, issued on 20 July 2026, which are guidance rather than statute. Under the guidelines, User Data means personal data an individual provides to an organization or that is created through use of its products or services (which, in our reading, would include chats typed into an assistant such as Gemini, though the guidelines do not name it), and organizations may consider exceptions to the consent requirement or deemed consent for model development but must obtain consent if those alternatives do not apply. Where consent is the route, the PDPC's view is that a general notice is insufficient for large-scale training, and organizations must state explicitly that the purpose includes AI development. Organizations are also encouraged, to the extent practicable, to explain how people can decline or withdraw consent, for example with step-by-step instructions or an easily accessible opt-out.

South Korea's National Assembly passed an amendment to the Personal Information Protection Act on 20 August 2026 that creates a special provision for using lawfully collected personal information in AI development, limited to cases where pseudonymized or anonymized data would not suffice and there is a public or social need. According to a newsletter from the law firm BKL, it was promulgated on 8 September 2026 and takes effect on 9 March 2027, so it is not yet current law. Taiwan's Personal Data Protection Act has no provision on AI training: Article 20 generally confines private-sector use of personal data to the specific purpose of collection, which we read as covering training, and Article 3 bars waiving the right to ask for that use to stop. None of these three texts is specific to Gemini, though in our reading personal data typed into a chat and then used for training is the kind of use they govern, and we did not review court rulings or agency interpretations in Taiwan.

On desktop, the path at `gemini.google.com` is Settings & help > Activity, then click On near the top and choose Turn off or Turn off and delete activity (the help page also has steps for the mobile apps). From the Privacy Hub's rules, we infer that people who do not want chats used for training can turn the setting off or use Temporary Chat each time. People who need to keep chats long-term, or who connect apps such as Google Workspace to a personal account, can leave it on and use Temporary Chat for sensitive content. Whether to enter confidential content at all has to be weighed against the retention periods and review scope of each option.
