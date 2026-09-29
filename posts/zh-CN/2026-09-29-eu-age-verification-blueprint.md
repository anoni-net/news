---
title: 欧盟年龄验证 App 的隐私设计与争议
description: 欧盟委员会建议各成员国在 2026 年底前推出年龄验证 App，欧盟以外的用户不受影响。欧委会写明 App 不保留证件与生物特征数据，EDRi 则质疑它的隐私保护。依欧委会 9 月发布的新版规范，App 与网站都必须实现零知识证明，只在设备不支持时退回签发方可能追溯的一般验证方式。
date: {created: 2026-09-29T07:00:00+08:00, updated: 2026-09-29T16:25:00+08:00}
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

欧盟委员会 4 月宣布年龄验证 App 技术就绪，建议各成员国年底前推出自己的 App。依 9 月 17 日提出的《EU KIDS Act》草案，13 岁以下不得使用社交平台，15 岁才能自己开账号。在线服务与应用商店要采用年龄确认工具，这套 App 是选项之一，欧盟以外的用户用不到。

依欧委会的新闻稿，社交与视频平台要在新开账号时验证年龄，已有账号改用账号创建日期等指标推估年龄。13 岁到未满 15 岁由家长设立迷你账号（mini accounts），每天最多使用一小时。

依欧委会的说明页与新闻稿，用户不必分享其他个人信息就能证明年满 18 岁，App 也不保留证件与生物特征数据。App 的昵称是迷你钱包（mini wallet），技术规范沿用欧盟数字身份钱包。9 月 2 日的 1.1.0 版规范文件里，App 与网站都必须实现零知识证明（zero-knowledge proof，只证明条件成立、不交出其他数据的方法），设备不支持时才退回一般验证方式。一般验证方式下，签发方保留记录并与网站串通就能追溯用户。

欧洲数字权利组织 EDRi 在 9 月 7 日发表技术分析，结论是工具在「就绪」与「保护隐私」两方面都做不到。分析里引用的是零知识证明仍非强制的旧版规范文件，文章到 9 月 29 日没有更正或更新的注记。EDRi 主张网络安全另有做法，应拒绝建设年龄验证。分析里也写到，数字身份钱包依法要「确保」不可关联性（unlinkability，多次出示无法串回同一人），欧委会改成只需「阻碍」关联。

## 导读观点 {#perspective}

欧委会规范文件附的威胁模型里，使用零知识证明时网站没有可比对签发记录的数据。一般验证方式的追溯风险列为可接受，理由是列在欧委会发布的欧盟可信列表、受各国监管的签发方要故意违规才会发生。欧委会的规范文件也建议签发方同时提供 App。依 EDRi 的分析，这让签发与出示集中在同一方，即使强制零知识证明也做不到严格的不可关联。

依 EDRi 的分析，App 以国家证件搭配生物识别确认用户，没有证件、合适的手机或不愿做人脸识别的人会被排除。欧委会的规范文件另列电子身份系统与银行、电信运营商的身份验证，威胁模型里只有扫描证件要做人脸比对。缺少证件的人另有规范文件公平性（Equity）条款的替代程序或人工处理。

欧委会的示范 App 以 EUPL-1.2 许可证开源，建议书里请各国通过第三方审查确保网络安全与隐私合规。依 EDRi 的分析，开源要求只涵盖数字身份钱包，丹麦的 App 在客户端就有非开源的代码。

欧委会的威胁模型里，大人在旁代为验证或替孩子的手机注册都列为可接受的残余风险。EDRi 的分析里没有谈到绕过。每次出示都比对人脸的做法，在威胁模型里因过度侵犯隐私被否决。

澳大利亚从 2025 年 12 月 10 日起要求社交平台阻止 16 岁以下的人持有账号，没做到的平台可能受罚，用户与家长不受罚。在排除的争点上，澳大利亚的法律禁止平台强迫出示政府证件，列为选项时要另有合理的替代方式。依中国大陆 2024 年 1 月 1 日施行的《未成年人网络保护条例》第三十一条，为未成年人提供信息发布、即时通讯等服务时要依法要求提供其真实身份信息，在追溯的争点上与欧盟规范让网站只得知年龄符合的方向不同。

中国境内的读者不会用到这套 App。比较各地时，隐私方面可以问签发方能不能追溯用户、没有证件的人有没有替代方式。未成年人保护方面可以问孩子能不能轻易绕过验证、已有账号如何处理。
