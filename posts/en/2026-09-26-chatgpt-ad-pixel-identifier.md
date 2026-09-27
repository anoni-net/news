---
title: The cross-site identifier behind ChatGPT's ad pixel
description: A traffic analysis found that ChatGPT's ad system sets a cookie linked to the user's account, which advertisers' sites then send back to OpenAI through its pixel along with browsing data. So far it has only been seen in Chrome on Android.
date: 2026-09-26T01:24:00+08:00
slug: chatgpt-ad-pixel-identifier
sources:
  - title: ChatGPT now knows what you do on other websites via ad collector
    url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
    publisher: Buchodi's Threat Intel
    date: 2026-09-20
  - title: ChatGPT Ads expands to Southeast Asia and Taiwan
    url: https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/
    publisher: OpenAI
    date: 2026-09-23
  - title: ChatGPT Supported Countries
    url: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
    publisher: OpenAI
  - title: 在 Chrome 中刪除、允許使用與管理 Cookie
    url: https://support.google.com/chrome/answer/95647?hl=zh-Hant&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome 說明
  - title: Delete, allow, and manage cookies in Chrome
    url: https://support.google.com/chrome/answer/95647?hl=en&co=GENIE.Platform%3DAndroid
    publisher: Google Chrome Help
authors:
  - anoni-net
---

A security researcher found that while you use ChatGPT, OpenAI's ad collector `bzr.openai.com` sets a cookie called `__obi` that is linked to your account, lasts a year and can be sent along with requests on other sites. So far it has only been observed in Chrome on Android. Browsers on iOS block it. On 23 September OpenAI began rolling out ChatGPT ads in seven more Asian markets, shown only on the Free and Go plans.

Advertisers install OpenAI's pixel on their own sites. When you visit one, the pixel returns `__obi` to OpenAI with the URL path, form fields and text on the page. Email addresses, phone numbers and names are hashed with SHA-256, while country, region, city and postcode are sent in the clear. Query strings were stripped, but a path alone can reveal something like a medical condition.

The cookie is set even when you are logged out. Every sync token examined was filed under the consent category "analytics", so allowing analytics while refusing marketing still delivers `__obi`.

The researcher reproduced this on their own phone, captured traffic in two ways and analysed 936 advertiser pixels on more than a thousand domains. The write-up states its limits: sync tokens appeared in about one in five sessions, desktop Chrome was not tested, and the server-side mapping back to accounts is inferred from the design rather than observed. OpenAI's support team received the researcher's questions on 14 September without answering them.

## Perspective {#perspective}

Pixels on advertisers' sites that report visits back to an ad platform are not new, and the researcher compares this one to the Meta and Google tracking code retailers have installed for years. What differs is the account on the other end. A ChatGPT account also holds conversations with an AI, where many people discuss health, work and personal problems, and those conversations could end up linked to browsing on unrelated sites.

The timing matters for readers in Asia. OpenAI's announcement names Indonesia, Malaysia, the Philippines, Singapore, Thailand, Vietnam and Taiwan, after earlier Asia-Pacific launches in Australia, New Zealand, Japan, South Korea and India, and puts the total at more than 60 countries. OpenAI's list of supported countries leaves out mainland China, Hong Kong and Macau, so people there are outside ChatGPT's official service altogether. Elsewhere in the region, people on the Free and Go plans now see ads, while Plus, Pro and Enterprise stay ad-free.

`__obi` travels as a third-party cookie. Safari blocks cross-site tracking by default, and every browser on iOS is built on Safari's WebKit engine, which is why the researcher saw nothing on iOS. On Android and desktop you can block third-party cookies in the browser settings. Firefox isolates third-party cookies per site by default, and Brave blocks them.

Consent banners let each company define its own categories. Here, "analytics" also covered syncing an advertising identifier, so refusing only "marketing" does not keep you out of ad tracking.

The behaviour was observed with ChatGPT logged in through Chrome on Android, so iPhone users need not change anything. Android users of Chrome can go to Settings > Site settings > Third-party cookies and choose Block third-party cookies; Google's help page gives the steps in Chinese as well as English. Some sites may stop working as expected once third-party cookies are blocked, and adding them to the exception list fixes that. Anyone who would rather not change Chrome's settings can instead use ChatGPT in a separate browser from the one used for everything else.
