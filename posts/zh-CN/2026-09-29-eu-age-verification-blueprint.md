---
title: 欧盟年龄验证 App 的隐私设计与争议
description: 欧盟委员会建议各成员国在 2026 年底前推出年龄验证 App，欧盟以外的用户不受影响。欧盟委员会写明 App 不保留证件与生物特征数据，EDRi 则质疑它的隐私保护。依 9 月发布的新版规范，App 与网站都必须实现零知识证明，只在设备不支持时退回签发方可能追溯的一般验证方式。
date: {created: 2026-09-29T07:00:00+08:00, updated: 2026-09-29T15:30:00+08:00}
slug: eu-age-verification-blueprint
sources:
  - title: The EU approach to age verification
    url: https://digital-strategy.ec.europa.eu/en/policies/eu-age-verification
    publisher: European Commission
    date: 2026-09-22
  - title: EU KIDS Act to restrict social media platforms’ access to children in the EU
    url: https://digital-strategy.ec.europa.eu/en/news/eu-kids-act-restrict-social-media-platforms-access-children-eu
    publisher: European Commission
    date: 2026-09-17
  - title: "EU KIDS Act to restrict social media platforms' access to children in the EU"
    url: https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1890
    publisher: European Commission
    date: 2026-09-17
  - title: Commission urges Member States to rollout EU age verification app
    url: https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app
    publisher: European Commission
    date: 2026-04-29
  - title: Why the EU age-verification tool does not solve privacy concerns
    url: https://edri.org/our-work/eu-age-verification-tool-does-not-solve-privacy-concerns/
    publisher: EDRi
    date: 2026-09-07
  - title: av-doc-technical-specification
    url: https://github.com/eu-digital-identity-wallet/av-doc-technical-specification
    publisher: EU Digital Identity Wallet
    date: 2026-09-02
  - title: av-app-android-wallet-ui
    url: https://github.com/eu-digital-identity-wallet/av-app-android-wallet-ui
    publisher: EU Digital Identity Wallet
    date: 2026-09-03
  - title: Social media age restrictions
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions
    publisher: eSafety Commissioner
    date: 2026-09-15
  - title: Social media 'ban' or delay FAQ
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions/faqs
    publisher: eSafety Commissioner
    date: 2026-09-16
  - title: 未成年人网络保护条例
    url: https://www.gov.cn/zhengce/content/202310/content_6911288.htm
    publisher: 中华人民共和国国务院
    date: 2023-10-24
regions:
  - EU
authors:
  - anoni-net
---

欧盟委员会在 4 月宣布年龄验证 App 技术就绪，建议各成员国在年底前推出自己的 App。依 9 月 17 日提出的《EU KIDS Act》草案，13 岁以下不得使用社交平台，15 岁才能自己开账号。在线服务与应用商店要采用年龄确认工具，这套 App 是选项之一，欧盟以外的用户不会用到。

欧盟委员会的说明页写明，用户可以证明自己年满 18 岁，不必分享其他个人信息。App 又称迷你钱包（mini wallet），技术规范沿用各国年底前要推出的欧盟数字身份钱包。草案的新闻稿里写明 App 不保留身份证件与生物特征数据，也列出欧盟民调里 92% 的受访者把加强未成年人网络保护列为优先政策之一。

欧洲数字权利组织 EDRi 在 9 月 7 日发表技术分析，结论是这套工具在「就绪」与「保护隐私」两方面都做不到。EDRi 主张应趁还能拒绝时不建设年龄验证，若仍要设年龄门槛，工具要符合最高的隐私与数据保护标准。依 EDRi 的分析，App 沿用的数字身份钱包依法要在相关情况下「确保」不可关联性（unlinkability，每次出示的年龄证明无法被串回同一个人），欧盟委员会把要求改成只需「阻碍」关联。

一般验证方式的凭证带有盐值、签名与时间戳，签发方保留记录并与网站合作，就能追溯到用户。EDRi 引用的是 1.1.0 之前的规范文件，零知识证明（zero-knowledge proof，只证明条件成立、不交出其他数据的密码学方法）在那一版是非强制的「SHOULD」。9 月 2 日发布的 1.1.0 版里，App 与网站都必须实现零知识证明，设备不支持时才退回一般验证方式。

## 导读观点 {#perspective}

匿名的年龄验证里，网站只得知「年龄符合」，签发的一方也不会得知你去过哪些网站。规范文件里建议签发方同时提供 App。依 EDRi 的分析，签发与出示集中在同一方时，即使强制使用零知识证明也做不到严格的不可关联。

1.1.0 版附的威胁模型里，使用零知识证明时网站没有能跟签发记录比对的数据，验证时也不会联系签发方。一般验证方式下签发方与网站串通的风险列为可接受，理由是需要受监管的签发方故意违规保留记录。

示范 App 以 EUPL-1.2 许可证开源，欧盟委员会在建议书里也请各国通过第三方审查确保网络安全与隐私合规。依 EDRi 的分析，开源要求只涵盖数字身份钱包，丹麦的年龄验证 App 在客户端就有专有（非开源）的代码。

依 EDRi 的分析，App 以国家证件搭配生物识别确认用户，没有证件、合适的手机或不愿做人脸识别的人会被排除。规范文件列出的获取方式另有电子身份系统与银行、电信运营商的身份验证。缺少证件的人，公平性（Equity）条款里另有替代程序或人工处理。

澳大利亚从 2025 年 12 月 10 日起要求社交平台采取合理措施，阻止 16 岁以下的人持有账号。依澳大利亚的法律，平台不得强迫用户出示政府证件或使用政府认证的数字身份，列为选项时要另有合理的替代方式。eSafety 在说明页写明这是延后持有账号，16 岁以下的用户与家长不受罚。

中国大陆 2024 年 1 月 1 日施行的《未成年人网络保护条例》第三十一条规定，网络服务提供者为未成年人提供信息发布、即时通讯等服务时，要依法要求提供未成年人的真实身份信息。不提供的，不得提供相关服务。

中国境内的读者不会用到这套 App，也不必做任何设置。身在欧盟的读者，可以在各国 App 年底前上线时留意采用的规范版本。比较各地做法时可以问同一组问题：零知识证明是否强制、签发与出示是否分开、App 是否开源、不出示证件的人有没有替代方式。
