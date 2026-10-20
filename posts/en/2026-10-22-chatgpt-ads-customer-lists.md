---
title: Customer-list matching and conversation context in ChatGPT ads
description: Advertisers on ChatGPT can upload lists of email addresses, phone numbers or mobile advertising IDs so that their ads reach only the people on those lists. Ads appear only on the Free and Go plans and began rolling out in Taiwan on 23 September. According to OpenAI's help page as of 20 October, ChatGPT still picks ads based on the current conversation after ad personalisation is turned off.
date: 2026-10-22T00:00:00+08:00
slug: chatgpt-ads-customer-lists
categories:
  - tracking
follows:
  - 2026-09-26-chatgpt-ad-pixel-identifier
sources:
  - title: Set up Custom Audiences for your Campaign
    url: https://help.openai.com/en/articles/20001346-set-up-custom-audiences-for-your-campaign
    publisher: OpenAI
  - title: ChatGPT 中的廣告
    url: https://help.openai.com/zh-hant/articles/20001047-ads-in-chatgpt
    publisher: OpenAI
  - title: Ads in ChatGPT
    url: https://help.openai.com/en/articles/20001047-ads-in-chatgpt
    publisher: OpenAI
  - title: Ad Tools Terms
    url: https://openai.com/policies/ad-tools-terms/
    publisher: OpenAI
    date: 2026-08-24
  - title: Privacy policy
    url: https://openai.com/policies/privacy-policy/
    publisher: OpenAI
    date: 2026-07-30
  - title: ChatGPT Ads expands to Southeast Asia and Taiwan
    url: https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
    publisher: OpenAI
    date: 2026-09-23
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: Supported countries and territories
    url: https://developers.openai.com/api/docs/supported-countries
    publisher: OpenAI
  - title: How ChatGPT Targets Ads To You Based On Your Prompts, Phone Number, and Email
    url: https://www.404media.co/how-chatgpt-targets-ads-to-you-based-on-your-prompts-phone-number-and-email/
    publisher: 404 Media
    date: 2026-10-15
  - title: Here's How ChatGPT Is Targeting You With Ads
    url: https://gizmodo.com/heres-how-chatgpt-is-targeting-you-with-ads-2000826457
    publisher: Gizmodo
    date: 2026-10-16
  - title: About customer list custom audiences
    url: https://www.facebook.com/business/help/341425252616329
    publisher: Meta
  - title: How Google uses Customer Match data
    url: https://support.google.com/google-ads/answer/6334160
    publisher: Google
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021
    publisher: Laws & Regulations Database of the Republic of China (Taiwan)
  - title: 自分に関する情報が第三者に送信される場合、 自身で確認できるようになります。
    url: https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/gaibusoushin_kiritsu.html
    publisher: Ministry of Internal Affairs and Communications
  - title: 맞춤형 광고에 쓰이는 “행태정보” 처리, 적법성과 투명성 높인다
    url: https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=9888
    publisher: Personal Information Protection Commission
    date: 2024-01-31
authors:
  - anoni-net
---

Advertisers on ChatGPT can upload lists of email addresses, phone numbers or mobile advertising IDs so that their ads are shown only to the people on those lists, 404 Media reported on 15 October. The feature appears on OpenAI's help page for advertisers under the name Custom Audiences. Ads appear only on the Free plan and the cheaper paid Go plan, not on Plus, Pro, Business or other plans, and began rolling out in Taiwan on 23 September. According to OpenAI's user help page as of 20 October, ChatGPT still picks ads based on the current conversation after ad personalisation is turned off.

According to the Custom Audiences help page, a list can contain email addresses, phone numbers, SHA-256 hashes of either, or Google Advertising IDs (GAID, the advertising identifier on Android phones). A hash is a one-way function that turns data into a fixed-length string. Advertisers can also upload raw, unhashed data, and uploaded files are usually deleted within 24 hours. OpenAI matches the list against ChatGPT users, and only the people matched count towards the audience.

A list can be used to show ads only to that audience, to exclude it, or to raise or lower the bid (what the advertiser is willing to pay for an impression or click) for it. Targeting an audience or adjusting bids requires at least 25,000 matched users, while an exclusion list can match fewer than 25,000. Ads Manager does not show which individuals were matched.

According to Gizmodo's account of the 404 Media report, 404 Media ran two ad campaigns on ChatGPT to test the system. Per the same account, it is unclear whether OpenAI hashes raw data after receiving it. The 404 Media report is paywalled, with only its first two paragraphs public, so the remaining details rely on Gizmodo's account.

According to OpenAI's user help page, OpenAI does not give advertisers users' conversations, memories, names, email addresses, precise location or IP addresses, and advertisers receive only aggregate performance figures such as views and clicks. If a user messages an advertiser through an ad, the advertiser can see those messages. Ads are not placed near conversations on sensitive topics such as personal health, mental health and politics, and are not shown in Temporary Chats or to accounts judged to belong to under-18s.

## Perspective {#perspective}

Targeting ads with customer lists is common in the industry, and Google's Customer Match and Meta's customer list custom audiences are the same kind of feature. According to Meta's help page, Meta hashes a list before matching it, and according to Google's, Google does not receive the actual email addresses. The upload formats on OpenAI's help page include unhashed raw data. 404 Media also reported that ChatGPT ads are chosen based on the prompts users type.

Under OpenAI's Ad Tools Terms for advertisers, a list may contain only first-party data the advertiser collected itself, not data obtained from data brokers (companies that collect and resell personal data). Advertisers must warrant that they have given the required notice and obtained any necessary consent or other legal basis, and nothing in the terms describes how OpenAI verifies this. As of 20 October, the user help page has nothing on how to find out which advertisers' lists you are on. The ad menu has an "About this ad" option for seeing why a particular ad was shown, and the help page does not cover whether it reveals customer lists.

Our 26 September piece covered the pixel (tracking code advertisers install on their own sites), which sends browsing data from other sites back to OpenAI. Under OpenAI's privacy policy (the version for users outside the EEA, the UK and Switzerland), OpenAI may receive information from advertisers, such as purchases users make from them, and use it to show more relevant ads.

As of 20 October, mainland China, Hong Kong and Macau are not on OpenAI's list of countries and territories where ChatGPT is supported, nor on the list for its API. According to the ChatGPT list, using the service from outside the listed places may get an account blocked or suspended. ChatGPT ads began rolling out on 23 September in Indonesia, Malaysia, the Philippines, Singapore, Thailand, Vietnam and Taiwan, following earlier Asia-Pacific launches in Australia, New Zealand, Japan, South Korea and India. According to OpenAI's help page, personalised ads are initially unavailable in the European Economic Area and Switzerland, with no other exceptions named, so no Asian market is set apart in the same way.

Customer lists are built from data advertisers hold about their own customers, and the rules in the places we checked differ. Taiwan's Personal Data Protection Act has no provision specifically on advertising identifiers, real-time bidding or targeted ads, and the Chinese word for advertising (廣告) does not appear in its text. Its Article 20 does require a non-government entity that markets with personal data to stop once the person objects, and to offer a way to object the first time it markets to them. We read only the statute itself as of 18 October, not its enforcement rules or regulators' interpretations, and amendments dated 11 November 2025 are to take effect on a date set by the Executive Yuan.

Japan amended its Telecommunications Business Act in June 2022. According to the Ministry of Internal Affairs and Communications page, which we checked as of 18 October and which shows no update date, online information services such as messaging, social media, search and news that send user data to outside parties through tags or information-collection modules must give notice of or publish what is sent, or obtain consent or offer a way to stop it, though the rule does not ban targeted ads and does not cover corporate websites or personal blogs. South Korea's Personal Information Protection Commission published a policy plan on 31 January 2024 to protect the online behavioural data used in targeted ads and set out to revise its targeted-advertising guidelines, though as of 18 October we could not find whether the revised guidelines are in force.

People on the Free or Go plan can go to Settings > Ad Controls in ChatGPT to turn off Personalize ads, and can also turn off Past chats and memory, a toggle that affects only ads. Ads data can be deleted in the same place, and is removed from OpenAI's servers within 30 days. According to the help page, people who cannot see these options in the mobile app should update it to the latest version. Turning off personalisation does not remove ads, and ChatGPT still picks them based on the current conversation.

People who do not want ads can switch to Plus or Pro, and the Free plan also has an ad-free option, though according to the help page its availability may vary by region and over time. The ad-free option comes with fewer messages per day and no access to tools such as image generation, and Go users have to switch back to Free to use it. In the Traditional Chinese version of the help page, the step "Change plan to go ad-free" appears as 「輕觸變更方案以享受 Go 無廣告體驗」, which reads as enjoying an ad-free Go plan, so follow the English wording. Because Temporary Chats do not show ads according to the help page, we infer that people who do not want a particular conversation to shape their ads can use a Temporary Chat.

Lists can contain email addresses, phone numbers and GAIDs, and as of 20 October OpenAI has not explained which account data it matches them against. If matching uses the email address and phone number registered to the ChatGPT account (our inference), a list built from a different address or number used for shopping or memberships may not match. Whether OpenAI will explain how it handles the raw data it receives, and whether turning off personalisation also excludes people from list matching, are the points to watch.
