---
title: Memory and permission design in Meta Muse and OpenAI Dots
description: Meta's Muse and OpenAI's Dots, both launched in September, run continuously in the cloud, read data from connected apps and turn it into memory. As of 2 October, Muse was not in the App Store in Taiwan, Hong Kong, Japan or South Korea, and Dots required ChatGPT's Pro or Business Premium plan. ChatGPT memory settings and Mac permissions can be checked today.
date: 2026-10-09T00:05:00+08:00
slug: muse-dots-agent-memory-permissions
categories:
  - tracking
sources:
  - title: "Introducing Muse: The World’s First Personal AI Agent Built for Everyone"
    url: https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
    publisher: Meta
    date: 2026-09-08
  - title: How to manage your Muse data
    url: https://www.meta.com/help/artificial-intelligence/2225571704857152/
    publisher: Meta
  - title: Introducing dots
    url: https://openai.com/index/introducing-dots/
    publisher: OpenAI
    date: 2026-09-29
  - title: Dots privacy, security, and safety FAQs
    url: https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
    publisher: OpenAI
  - title: Getting started with your dot
    url: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
    publisher: OpenAI
  - title: Meta’s Muse AI surprises users — but not in a good way
    url: https://freedom.press/digisec/blog/metas-muse-ai-surprises-users-but-not-in-a-good-way/
    publisher: Freedom of the Press Foundation
    date: 2026-09-30
  - title: Muse, Meta's extraordinarily privileged AI assistant, has a serious 0-day
    url: https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/
    publisher: Ars Technica
    date: 2026-09-21
  - title: I asked Meta’s Muse for its filesystem and it sent me 6.8 GB
    url: https://mouse.dev/blog/muse-runtime-export/
    publisher: mouse.dev
    date: 2026-09-22
  - title: Yeah, don't give Meta's Muse app access to your Mac
    url: https://9to5mac.com/2026/09/28/yeah-dont-give-metas-muse-app-access-to-your-mac/
    publisher: 9to5Mac
    date: 2026-09-28
  - title: Meta's Muse AI Agent Read a User's Private iMessages. Then It Lied About How
    url: https://decrypt.co/379122/metas-muse-ai-agent-user-private-imessages-lied-how
    publisher: Decrypt
    date: 2026-09-23
  - title: ChatGPT can now send texts for you with new Apple Messages plug-in
    url: https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/
    publisher: TechCrunch
    date: 2026-08-20
  - title: ChatGPT gets all up in your iMessages
    url: https://freedom.press/digisec/blog/chatgpt-gets-all-up-in-your-imessages/
    publisher: Freedom of the Press Foundation
    date: 2026-08-26
  - title: Memory in ChatGPT
    url: https://help.openai.com/en/articles/8590148-memory-faq
    publisher: OpenAI
  - title: Data controls in ChatGPT
    url: https://help.openai.com/en/articles/7730893-data-controls-faq
    publisher: OpenAI
  - title: 在 Mac 上更改「隱私權與安全性」設定
    url: https://support.apple.com/zh-tw/guide/mac-help/mchl211c911f/mac
    publisher: Apple
  - title: Premium seats are coming to ChatGPT Business
    url: https://openai.com/index/premium-seats-chatgpt-business/
    publisher: OpenAI
  - title: 允許輔助使用 App 取用 Mac
    url: https://support.apple.com/zh-tw/guide/mac-help/mh43185/mac
    publisher: Apple
  - title: Allow accessibility apps to access your Mac
    url: https://support.apple.com/guide/mac-help/mh43185/mac
    publisher: Apple
  - title: Muse from Meta App
    url: https://apps.apple.com/us/app/muse-from-meta/id6760173601
    publisher: App Store
  - title: Warning sources against using AI chatbots
    url: https://securedrop.org/news/updated-landing-page-guidance/
    publisher: SecureDrop
    date: 2026-09-24
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: Protecting Personal Data Privacy in the Use of Agentic AI
    url: https://www.pcpd.org.hk/english/resources_centre/publications/files/pcpd_use_of_agentic_ai.pdf
    publisher: Office of the Privacy Commissioner for Personal Data, Hong Kong
  - title: AI가 내 정보 보고 직접 일한다...'어디까지 맡길지' 연말 기준 나온다
    url: https://news.mtn.co.kr/news-detail/2026092316363993251
    publisher: MTN
    date: 2026-09-23
  - title: Change Privacy & Security settings on Mac
    url: https://support.apple.com/guide/mac-help/mchl211c911f/mac
    publisher: Apple
authors:
  - anoni-net
---

Meta launched Muse on 8 September and OpenAI launched Dots on 29 September. Both are AI agents, assistants that carry out multi-step tasks on a user's behalf: they run continuously in the cloud, read data from connected apps and services, turn it into memory and act on it. Meta says Muse is rolling out in the US first. As of 2 October, Dots was limited to ChatGPT's Pro and Business Premium plans, with Business Premium at $125 per user per month.

Muse runs on iPhone, Android and the web, and Meta says it is free for most uses, with paid plans. Freedom of the Press Foundation (FPF) relayed one user's account that Muse, selling a keyboard on Facebook Marketplace, accepted a price the user was unhappy with and gave the buyer the user's home address. The account adds that Muse did not notify the user when the buyer came to the door.

As of 2 October we found no response from Meta to this case. FPF also notes that Muse trains on users' interactions by default.

9to5Mac and Decrypt reported that a tech columnist testing Muse on a Mac found it drawing on the columnist's Messages history, although that permission had been declined during setup. Decrypt notes that reading the Messages database requires macOS Full Disk Access. A Meta executive replied on Threads that Messages access is an opt-in feature, while the columnist says Muse's settings showed it enabled despite the refusal.

Ars Technica reported on 21 September a flaw that let other apps and terminal commands control Muse, and wrote that Meta shipped a fix about 12 hours after publication. A separate researcher obtained the contents of Muse's entire 6.8 GB cloud environment and submitted the finding through Meta's bug bounty programme. Meta marked it "Not Applicable", listing several possible grounds without saying which applied.

Each dot has its own cloud computer and connects to other apps through plug-ins. According to OpenAI's help pages, when it has not been given a task, a dot reads connected sources and saves private notes, but at that stage it cannot send messages, change content or control a browser. As of 2 October, individual dot memories cannot be viewed, deleted or edited, and the only way to remove them is to delete the whole dot. Deleting a dot leaves the files and conversations it created in place, and disconnecting an app stops new access without deleting what the dot has already absorbed.

Prompt injection means instructions hidden in web pages, emails or documents that try to make the dot do something the user did not ask for. OpenAI's pages say its protections "help reduce the risk … but they do not eliminate it". For supported sign-in flows, passwords go through a separate form to the browser environment without reaching the model, though passwords shared in chats, documents or plug-ins are not covered.

OpenAI's pages also say Dots can only be created on a computer and are not available to users under 18. As of 2 October we found no independent testing of Dots.

## Perspective {#perspective}

Both products give users an always-on cloud computer that reads connected data in the background and builds memory from it. As of 2 October, Dots' memory can only be removed by deleting the whole dot. Muse keeps its memory in a file users can view and edit, though Meta's help page warns that Muse "may still remember information it learned from what you deleted".

The training settings also differ. Muse's "Help improve our AI models" is on when you first use it, and Meta says switching it off also applies to previous interactions. OpenAI's announcement says personal plans can control whether a dot's conversations and work are used to improve its models. ChatGPT's training setting for ordinary conversations is "Improve the model for everyone", and OpenAI's help page says switching it off covers only new conversations but does not state its default on personal plans.

As of 2 October, Muse was not in the App Store in Taiwan, Hong Kong, Japan, South Korea, Singapore or India. The US listing offers both Simplified and Traditional Chinese. As of the same date, OpenAI's supported-country list included Taiwan, Japan, South Korea, Singapore and India but not mainland China, Hong Kong or Macao. Since OpenAI offers Dots within ChatGPT, we take this to mean Dots is unavailable in those three places, while elsewhere it still needs a Pro or Business Premium plan.

Hong Kong's Privacy Commissioner for Personal Data published guidance on agentic AI in August 2026. It states that "AI agents are not legal persons", so organisations using them remain accountable, and says several of its recommendations also apply to individual users. Among them, its checklist suggests regularly reviewing and manually managing the contents of an agent's long-term memory.

In South Korea, the Personal Information Protection Commission met with industry on 23 September to discuss how far AI agents may access personal data. Korean broadcaster MTN reported that guidance is expected by the end of 2026.

OpenAI's ChatGPT plug-in for Apple Messages, released in August, can read, summarise, draft and send texts, and requires Mac Full Disk Access. TechCrunch relayed OpenAI's statement that message content is stored on the user's computer rather than its servers, while FPF notes that OpenAI still processes ChatGPT conversations. Apple describes Full Disk Access as access to "all files on your computer, including data from other apps (for example, Mail, Messages, Safari, and Home)".

According to OpenAI's help pages, disconnecting an app only stops a dot's future access, and what it has already absorbed stays until the dot is deleted. Turning off ChatGPT memory likewise only stops future sharing with the dot. A Messages database also holds what other people sent. Our inference from Meta's and OpenAI's descriptions is that people who message someone who has granted such permissions cannot control whether an AI app reads those messages.

If you use ChatGPT, memory is under Settings > Personalization, and OpenAI notes that deleting a chat does not necessarily delete a memory created from it. Training is under Settings > Data controls, and switching it off covers only new conversations.

If you have granted AI apps access on a Mac, System Settings > Privacy & Security lists which apps hold Full Disk Access and Accessibility rights. Apple notes that Accessibility access also reaches contacts, calendars and other information.

FPF suggests that anyone keen to try these agents wait for the technology to mature or use a separate device holding only what the task needs, at the cost of a second device. In its 24 September update, SecureDrop advises people preparing to contact journalists not to use AI chatbots while logged in, as prompt histories may be used to identify them.
