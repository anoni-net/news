---
title: Payment and identity in SimpleX supporter badges
description: SimpleX Chat sells supporter badges that let buyers send larger files. By SimpleX's design, the service cannot tell which purchase a badge came from when it is shown, but card payments and badges grouped by expiry week still leave traces. The badges are useful to people who need to send large files over SimpleX.
date: 2026-11-23T00:00:00+08:00
slug: simplex-supporter-badges
categories: [finance]
sources:
  - title: SimpleX Supporter Badges — Send Larger Files That Stay Available Longer, Without Being Identified
    url: https://simplex.chat/blog/20260919-simplex-supporter-badges.html
    publisher: SimpleX Chat
    date: 2026-09-19
  - title: SimpleX Supporter Badges
    url: https://github.com/simplex-chat/simplex-chat/blob/master/docs/protocol/badges-overview.md
    publisher: SimpleX Chat
    date: 2026-10-22
  - title: Supporter badges
    url: https://simplex.chat/docs/guide/supporter-badges.html
    publisher: SimpleX Chat
  - title: Releases · simplex-chat/simplex-chat
    url: https://github.com/simplex-chat/simplex-chat/releases
    publisher: GitHub
  - title: The Privacy Pass Architecture
    url: https://www.rfc-editor.org/rfc/rfc9576.html
    publisher: IETF
  - title: Is https://simplex.chat blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/simplex.chat
    publisher: GreatFire
    date: 2026-11-17
  - title: Is https://play.google.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/play.google.com
    publisher: GreatFire
    date: 2026-11-01
  - title: iTunes lookup API (cn)
    url: https://itunes.apple.com/lookup?id=1605771084&country=cn
    publisher: Apple
  - title: 中华人民共和国反洗钱法
    url: http://www.npc.gov.cn/npc/c2/c30834/202411/t20241108_440887.html
    publisher: National People's Congress of the People's Republic of China
    date: 2024-11-08
  - title: Money Laundering Control Act
    url: https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=G0380131
    publisher: Laws & Regulations Database of Taiwan
    date: 2024-07-31
authors:
  - anoni-net
---

SimpleX's announcement says that in other messaging apps a paid feature is attached to the account, so the operator knows who paid and what they do with the feature. Since September SimpleX Chat has sold supporter badges, which raise the file size limit from 1 GB to 2 GB (5 GB with a legend badge) and keep files on servers for longer (7 days for supporters, 21 days for legends). The SimpleX network has no user accounts, so a badge is an anonymous credential that proves the holder paid without revealing who they are. As of 21 November, version 7.1 of the SimpleX Chat app includes the feature.

According to SimpleX's technical white paper, a badge is a BBS signature (a digital signature scheme still being standardised), issued by a badge service that SimpleX operates and stored on the user's own device. Each time the app shows the badge to a contact or presents it to a server, it generates a new zero-knowledge proof from it. A zero-knowledge proof works like proving you are over 18 without handing over your whole ID card, a technique we also covered in our piece on the [EU age verification app](https://anoni.net/news/en/2026/09/eu-age-verification-blueprint/). Contacts and servers therefore see only the badge type and expiry date, and cannot link two presentations to each other or trace either one back to the purchase.

SimpleX's announcement says credentials are issued one month at a time, and all badges expire on the same day of the week. A holder is therefore mixed in with every supporter whose badge expires that week. According to the white paper, at each monthly renewal the app requests the new credential from the badge service and shows the new badge to contacts on different days, so that others find it harder to pick out a holder by timing.

## Perspective {#perspective}

Privacy Pass, developed by the Internet Engineering Task Force (IETF), takes a different approach: a user passes a check once in exchange for tokens, and can present them without revealing who they are. According to the white paper, these tokens are spent once presented and carry no expiry date or type. A badge has to be presented again and again, in every conversation and on every connection, so SimpleX chose BBS signatures, from which the app can keep generating new proofs.

The white paper says the badge service keeps the payment record of each purchase, and a card payment is linked to the purchase, as with any other service. Because badges expiring in the same week share one expiry date, server operators can group those supporters' connections together, and how many people a holder is mixed in with depends on how many badges expire that week. A badge that has just been bought or redeemed from a code is shown right away, so for people who get a code in the badge service's own group, the service can guess from when the new badge appears who redeemed it. When a Google Play subscription is moved to a new device with Restore purchases (the feature that moves the store's subscription to the current profile), the service links the two purchases, though not the profiles that hold them.

The Android version installed from Google Play takes payment inside the app, with a one-month plan and monthly or annual plans that renew automatically. The iOS version, versions installed from F-Droid or GitHub, and the desktop version open a purchase page in the browser, where paying by card, Bitcoin or Monero gives you a code to paste into the app's settings in exchange for a badge. The white paper says that people who want the payment itself to be private can pay with cryptocurrency instead. Badges bought on the web do not renew automatically and, as of 21 November, cannot be moved to a new device.

Mainland China and Taiwan, for example, differ in how readers can get the app: as of 21 November the China App Store had no listing for SimpleX Chat while the Taiwan store did, and GreatFire (a project that measures blocking by the Great Firewall) found play.google.com blocked in mainland China as of 1 November. GreatFire also found simplex.chat, where the announcement sends badge buyers, blocked in mainland China in its latest test on 17 November, based on a single sample. For those who pay by card, the payment record may also stay with the card issuer. A card issuer covered by mainland China's Anti-Money Laundering Law must keep customer identity data and transaction records for at least ten years (Article 34), while Taiwan's Money Laundering Control Act requires covered institutions to keep customer identification records for at least five years after the relationship or an occasional transaction ends (Article 8).

A badge is attached to a single profile, and incognito profiles do not show it. Badges cannot be revoked, so if a device or backup is compromised, whoever obtains the badge data can use it until it expires. If several months were bought, the intruder can also request new credentials for the remaining months from the badge service.
