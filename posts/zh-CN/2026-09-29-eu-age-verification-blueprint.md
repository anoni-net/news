---
title: 欧盟年龄验证蓝图的隐私缺口
description: 欧盟推动各国在年底前推出年龄验证 App。依 EDRi 的技术分析，不可关联性被放宽、凭证仍能追溯到用户，没有证件的人也会被排除在外。
date: 2026-09-29T07:00:00+08:00
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
  - title: Social media age restrictions
    url: https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions
    publisher: eSafety Commissioner
    date: 2026-09-15
  - title: Under-16
    url: https://www.mcmc.gov.my/en/onsa/under-16
    publisher: Malaysian Communications and Multimedia Commission
  - title: 未成年人网络保护条例
    url: https://www.gov.cn/zhengce/content/202310/content_6911288.htm
    publisher: 中华人民共和国国务院
    date: 2023-10-16
regions:
  - EU
authors:
  - anoni-net
---

欧盟委员会在 4 月宣布年龄验证 App 技术就绪，并建议各成员国在年底前推出。9 月 17 日提出的《EU KIDS Act》草案要求在线服务与应用商店采用年龄确认工具，13 岁以下不得使用社交平台，15 岁才能自己开账号。欧洲数字权利组织 EDRi 在 9 月 7 日发表的技术分析，结论是这套工具在「就绪」与「保护隐私」两方面都做不到。这套 App 只在欧盟推行，欧盟以外的用户不会用到。

欧盟委员会 2025 年 7 月先发布一份蓝图，让各国据此开发自己的 App。各国的 App 又称「迷你钱包」，技术规范沿用各国在 2026 年底前要提供的欧盟数字身份钱包。依 EDRi 的分析，27 个成员国可能做出 27 种设计、技术与隐私保护都不同的 App。

法律要求在相关情况下「确保」不可关联性（unlinkability，每次出示的年龄证明无法被串回同一个人）。依 EDRi 的分析，欧盟委员会把这项要求改成「阻碍」关联，追踪会变难，但不保证做不到。App 以国家签发的证件为信任来源，再用人脸识别绑定用户，没有证件、没有合适的手机或不愿做人脸识别的人都会被排除。

EDRi 引用的规范条文里，零知识证明（zero-knowledge proof，只证明条件成立、不交出其他数据的密码学方法）都写成非强制的「SHOULD」。即使一次签发多张凭证，凭证里仍有盐值、哈希、公钥、签名与时间戳，签发方可以据此追溯到用户。规范文件 9 月 2 日合并的 1.1.0 版里，零知识证明已改列为首选的机制，不用零知识证明的一般验证方式保留作为备用。

## 导读观点 {#perspective}

匿名的年龄验证里，网站只得知「年龄符合」，签发的一方也不会得知你去过哪些网站，两边都靠不可关联性保护。按规范文件的建议，签发方也同时提供 App。依 EDRi 的分析，签发与出示因此集中在同一方手上，就算强制使用零知识证明，也不足以做到严格的不可关联。

欧盟委员会的示范 App 以 EUPL-1.2 授权开源，但依 EDRi 的分析，开源的要求只适用于各国的数字身份钱包，不包括各国的年龄验证 App。丹麦的 App 在客户端就有专有（非开源）的代码，外界无法检验。

中国大陆 2024 年 1 月 1 日施行的《未成年人网络保护条例》第三十一条要求为未成年人提供信息发布、即时通讯等服务时，取得未成年人的真实身份信息。澳大利亚从 2025 年 12 月 10 日起要求社交平台阻止 16 岁以下的人开账号，法律同时禁止平台强迫用户出示政府证件或使用政府的数字身份。马来西亚从 2026 年 6 月 1 日起，也依法要求社交平台验证用户年龄。

这套 App 目前不需要读者做任何设置。关注年龄验证立法的人，可以拿 EDRi 列出的几点检验各地的做法，包括零知识证明是否强制、签发与出示是否分开、App 是否开源，以及有没有不需要证件与人脸识别的替代方式。
