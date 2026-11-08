---
title: Privacy Badger for Safari on macOS
description: On 19 October, EFF released a Safari version of Privacy Badger, its tracker-blocking browser extension. It runs only on the Mac and requires Safari 26.5 and macOS 15.7.7 or later. As of 8 November, there is no Safari version for iPhone or iPad.
date: 2026-11-12T00:00:00+08:00
slug: privacy-badger-safari-macos
categories:
  - tracking
sources:
  - title: Announcing Privacy Badger for Safari on macOS
    url: https://www.eff.org/deeplinks/2026/10/announcing-privacy-badger-safari-macos
    publisher: EFF
    date: 2026-10-19
  - title: EFF Launches Privacy Badger for Safari on macOS
    url: https://www.eff.org/press/releases/eff-launches-privacy-badger-safari-macos
    publisher: EFF
    date: 2026-10-19
  - title: Privacy Badger | Fight hidden tracking with EFF
    url: https://privacybadger.org/
    publisher: EFF
  - title: Privacy Badger App - App Store
    url: https://apps.apple.com/us/app/privacy-badger/id6761143693
    publisher: Apple
  - title: Support Safari on iOS
    url: https://github.com/EFForg/privacybadger/issues/3248
    publisher: GitHub
  - title: privacybadger/src/_locales
    url: https://github.com/EFForg/privacybadger/tree/master/src/_locales
    publisher: GitHub
  - title: Privacy Badger now supports Safari
    url: https://freedom.press/digisec/blog/privacy-badger-now-supports-safari/
    publisher: Freedom of the Press Foundation
    date: 2026-10-28
  - title: Prevent cross-site tracking in Safari on Mac
    url: https://support.apple.com/guide/safari/prevent-cross-site-tracking-sfri40732/mac
    publisher: Apple
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021
    publisher: Laws & Regulations Database of the Republic of China (Taiwan)
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: National People's Congress
    date: 2021-08-20
  - title: 自分に関する情報が第三者に送信される場合、 自身で確認できるようになります。
    url: https://www.soumu.go.jp/main_sosiki/joho_tsusin/d_syohi/gaibusoushin_kiritsu.html
    publisher: Ministry of Internal Affairs and Communications
  - title: iTunes lookup API (cn)
    url: https://itunes.apple.com/lookup?id=6761143693&country=cn
    publisher: Apple
  - title: iTunes lookup API (tw)
    url: https://itunes.apple.com/lookup?id=6761143693&country=tw
    publisher: Apple
  - title: iTunes lookup API (hk)
    url: https://itunes.apple.com/lookup?id=6761143693&country=hk
    publisher: Apple
  - title: iTunes lookup API (jp)
    url: https://itunes.apple.com/lookup?id=6761143693&country=jp
    publisher: Apple
  - title: iTunes lookup API (kr)
    url: https://itunes.apple.com/lookup?id=6761143693&country=kr
    publisher: Apple
  - title: www.eff.org
    url: https://en.greatfire.org/https/www.eff.org
    publisher: GreatFire
  - title: privacybadger.org
    url: https://en.greatfire.org/https/privacybadger.org
    publisher: GreatFire
authors:
  - anoni-net
---

The Electronic Frontier Foundation (EFF), a US digital rights group, released a Safari version of Privacy Badger on 19 October. Privacy Badger is a free browser extension developed by EFF that automatically learns to recognise and block trackers. The Safari version supports only the Mac and needs Safari 26.5 or later, and the system requirement listed on its Mac App Store page is macOS 15.7.7 or later. As of 8 November, it cannot be installed in Safari on iPhone or iPad.

According to EFF's announcement, Privacy Badger already has more than 4 million users. In the press release, EFF's technical staff mention that Safari support has long been one of the most frequent requests from users. The announcement credits improvements in Safari's extension support for making a release possible for Safari 26.5 and later.

According to the announcement, Safari's default browsing mode limits the information trackers can access but still lets them load. Privacy Badger stops trackers from loading in the first place, so it can block tracking techniques that get around Safari's protections. Widgets such as embedded tweets, comment sections and video players can share data even if the user never clicks them, and Privacy Badger replaces them with placeholders that load only when clicked.

Privacy Badger also automatically sends the Global Privacy Control (GPC) signal, which tells websites not to sell or share the user's personal data. The announcement lists US states including California, Colorado, New Jersey and Connecticut as places where GPC already has legal effect.

The Safari version is a free install from the Mac App Store, with EFF as the seller. The announcement warns that installing an extension in Safari takes more steps than in other browsers, and links to Apple's instructions. This is the first release of the Safari version, and problems can be reported by email to `extension-devs@eff.org` or on GitHub.

## Perspective {#perspective}

According to privacybadger.org, Privacy Badger identifies trackers algorithmically, whereas most blocking tools rely on manually maintained lists of domains. It watches whether third-party domains use cookies that can uniquely identify a browser, "supercookies" kept in local storage, and canvas fingerprinting (identifying a device from subtle differences in how its browser draws graphics). A third-party domain caught tracking the user on three different websites gets blocked. Ads that do not track the user are left alone.

Privacy Badger uses lists as well. By default it regularly pulls in data from Badger Sett, EFF's training project, on the trackers Badger Sett has found across thousands of popular websites. A separate yellowlist holds third-party domains that websites need in order to work, and for these Privacy Badger loads the content and blocks only third-party cookies and the referrer. On the same site, the yellowlist is described as a compromise for usability that EFF hopes to do without in the long run.

According to Apple's support page, Safari deletes cookies and website data from third-party sites the user has not visited and interacted with directly. Safari also presents websites with a simplified version of the system configuration, so that every Mac looks more alike and trackers find it harder to identify a device. According to EFF's announcement, Privacy Badger is effective on its own. Used alongside an ad blocker, or with the tracking protection in Safari's Advanced settings applied to all windows, it can also block trackers that are missing from other tools' lists or that those tools choose not to block.

According to privacybadger.org, GPC is meant to be a legally binding request to every company wherever an applicable privacy law exists. The states listed in the announcement are all in the US, and our inference is that websites elsewhere may ignore the signal. According to the same site, Privacy Badger also sends the Do Not Track signal (a browser signal asking websites not to track the user). A domain is blocked only if it keeps collecting unique identifiers after receiving both signals.

During installation, the browser warns that the extension can access data on all websites, and according to privacybadger.org, browsing data is not shared unless the user submits a broken-site report. The privacy label on the Mac App Store page reads "Data Not Collected", information provided by the developer that Apple has not verified. Freedom of the Press Foundation, a press freedom organisation, also reminded readers in its introduction to the Safari version to install only extensions they trust. Beyond permissions, a website may stop working properly, and according to EFF's announcement, Privacy Badger can then be disabled for that site alone.

Among the Asian rules on ad tracking that we, a community based in Taiwan, have collected, Article 20 of Taiwan's Personal Data Protection Act requires a non-government entity using personal data for marketing to stop once the person refuses, and to offer a way to refuse the first time it markets to them. Article 24 of mainland China's Personal Information Protection Law requires anyone pushing information or commercial marketing to individuals through automated decision-making to also offer an option that does not target their personal characteristics, or a convenient way to refuse. Japan's amended Telecommunications Business Act, in force since 16 June 2023, requires online information services such as messaging, social media, search and news to give notice of or publish the user data they send to outside parties through tags or modules, or else obtain consent or offer a way to opt out. None of these provisions mentions GPC or Do Not Track, and we have not checked whether regulators in these places treat either signal as a refusal or an opt-out.

An iTunes lookup API query on 8 November returned the app in the Mac App Store storefronts for mainland China, Taiwan, Hong Kong, Japan and South Korea, free in each and at the same version, 2026.10.22, though we did not open those storefronts with local accounts. The listing's 28 languages include Japanese and Chinese but not Korean. In mainland China, GreatFire rated www.eff.org as unreliable, with interference in 23% of the last 61 conclusive tests up to its latest test on 12 October. privacybadger.org was reachable from mainland China at GreatFire's last test on 31 May, and has not been tested since.

If you use Safari on a Mac and want less cross-site tracking, first make sure Safari is at 26.5 or later and the system at macOS 15.7.7 or later, then install the extension from the Mac App Store and enable it in Safari following Apple's instructions. The extension's interface is available in Traditional Chinese, though as of 8 November privacybadger.org has no Traditional Chinese version. Privacy Badger blocks third-party trackers, and data collected by the sites you visit directly is outside its scope (when you visit YouTube directly, for example, neither YouTube's own tracking nor its ads are blocked). As of 8 November, there is no version for browsing on iPhone and iPad.
