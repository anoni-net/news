---
title: 通行密钥的证明机制争议
description: 10 月 10 日一篇评论主张不要使用通行密钥，理由是网站可以用证明（attestation）机制限制用户能用的设备与软件，10 月 14 日有作者撰文回应。双方都同意通行密钥在多数情况下绑定域名、能防钓鱼，争点在证明会不会成为限制，以及该继续用通行密钥还是改用其他方式。
date: 2026-10-19T00:05:00+08:00
slug: passkey-attestation-debate
categories:
  - security
sources:
  - title: Passkeys are a trap. Do not use them.
    url: https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them
    publisher: Non-Functional
    date: 2026-10-10
  - title: Passkeys Are Not a Trap
    url: https://scotthelme.co.uk/passkeys-are-not-a-trap/
    publisher: scotthelme.co.uk
    date: 2026-10-14
  - title: "Web Authentication: An API for accessing Public Key Credentials - Level 3"
    url: https://www.w3.org/TR/webauthn-3/
    publisher: W3C
    date: 2026-08-25
  - title: NIST Special Publication 800-63B
    url: https://pages.nist.gov/800-63-4/sp800-63b.html
    publisher: NIST
  - title: Syncable Authenticators
    url: https://pages.nist.gov/800-63-4/sp800-63b/syncable/
    publisher: NIST
  - title: Passkeys
    url: https://fidoalliance.org/passkeys/
    publisher: FIDO Alliance
  - title: Download Credential Exchange Specifications
    url: https://fidoalliance.org/download-credential-exchange-specifications/
    publisher: FIDO Alliance
  - title: 關於通行密鑰的安全性
    url: https://support.apple.com/zh-tw/102195
    publisher: Apple
    date: 2024-09-27
  - title: 关于通行密钥的安全性
    url: https://support.apple.com/zh-cn/102195
    publisher: Apple
    date: 2024-09-26
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: 使用通行密钥（而非密码）登录
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hans
    publisher: Google
  - title: Sync passkeys securely across your devices
    url: https://blog.google/technology/safety-security/google-password-manager-passkeys-update-september-2024/
    publisher: Google
    date: 2024-09-19
  - title: What are passkeys and why they matter
    url: https://support.microsoft.com/en-us/accounts-billing/security/what-are-passkeys-why-they-matter
    publisher: Microsoft
  - title: Export Vault Data
    url: https://bitwarden.com/help/export-your-data/
    publisher: Bitwarden
  - title: How to export your data from the 1Password apps
    url: https://support.1password.com/export/
    publisher: 1Password
  - title: "KeePassXC: User Guide"
    url: https://keepassxc.org/docs/KeePassXC_UserGuide
    publisher: KeePassXC
  - title: 进一步了解 iCloud（中国大陆）
    url: https://support.apple.com/zh-cn/111754
    publisher: Apple
    date: 2025-04-22
  - title: 适用于中国客户的 Apple 和云上贵州数据隐私声明
    url: https://support.apple.com/zh-cn/121767
    publisher: Apple
    date: 2024-12-10
  - title: "Is https://accounts.google.com blocked in mainland China? — GreatFire"
    url: https://en.greatfire.org/https/accounts.google.com
    publisher: GreatFire
authors:
  - anoni-net
---

通行密钥（passkey）用手机或电脑的屏幕锁定取代密码登录，每组密钥只能用在创建它的域名。10 月 10 日刊在 Substack 的一篇评论以「Passkeys are a trap. Do not use them.」为题，主张网站可以通过证明（attestation，存放密钥的设备或软件向网站出示自身来历的机制）逐步限制用户能用的设备与软件。10 月 14 日有作者以「Passkeys Are Not a Trap」撰文回应，主张多数人用的同步通行密钥（存在密码管理器、会在设备之间同步）不提供证明。两篇都同意密码不安全、通行密钥在多数情况下绑定域名，争点集中在证明，以及该继续用通行密钥还是改用其他方式。

评论的作者先指出，能否复制、存在硬件或软件里各不相同的东西都叫通行密钥，并推测这个命名是刻意让用户不去细看。作者的核心论点是网站可以借证明确认用户用的是核准的密码管理器，等到大多数用户都不受影响，就能开始拒绝没有证明的通行密钥。作者写到证明需要加密处理器、密码管理器、操作系统与固件都通过检查（例如为了延续旧手机而改装 LineageOS 的人可能无法通过）。作者也写到证明有正当用途、多数网站目前不要求，正文建议改用身份验证器 App 生成的一次性密码（TOTP），文末的补充段落另外推荐 YubiKey 这类硬件安全密钥。

回应文章的作者写到，网站就算要求证明，iCloud 钥匙串、Google 密码管理工具、1Password 或 Bitwarden 里的同步通行密钥也只会返回「none」（表示没有证明）。依这位作者的推论，消费者网站如果只收有证明的通行密钥，会立刻挡掉几乎所有用户。回应文章也提到，证明只告诉网站验证器（存放密钥的手机、密码管理器或安全密钥）的厂牌与型号，不包含操作系统、浏览器、扩展程序、固件版本或手机是否越狱。对 YubiKey 的建议，作者的回应是每支 YubiKey 出厂都带有 Yubico 签发的证明证书，担心证明的人反而会被推向证明。

## 导读观点 {#perspective}

W3C 2026 年 8 月发布的 WebAuthn Level 3 规范把证明的默认值定为 none，证明的格式由验证器决定。网站可以表达偏好，也可以依自己的政策决定接受哪些证明。规范以 AAGUID（标示验证器型号的 128 位标识符）标示类型，也提醒证明证书可能被用来追踪用户（缓解方式包括大量设备共用同一张证书、交给匿名化的证书颁发机构）。规范里已列为弃用的 Android SafetyNet 格式，证明内容包含平台健康状态的信息（回应文章提到证明不含操作系统状态，依本文的整理要看格式而定）。

依同一份规范，可能包含能识别个别设备信息的企业证明（enterprise），要浏览器或验证器的设置允许该网站时才会提供。美国国家标准与技术研究院（NIST）给联邦机构的身份验证指南（SP 800-63-4）提到，面向大众的服务不应因为取不到证明而挡下同步通行密钥，否则用户可能被推向容易被钓鱼的方式。同一份指南也建议有证明时服务端应该用它判断信任程度，联邦机构的内部系统应实现证明。服务端也可以依「可备份」标志（标示密钥能否同步或备份的字段）限制同步通行密钥。

回应文章从 2026 年 10 月的现况出发，消费者网站多半不要求证明，主要的同步服务也不提供。回应文章也写到，如果消费者网站真的开始要求证明，值得大声反对。评论担心的则是之后的走向，作者的推论是受影响的只有改装系统的少数人，网站因此能在不引起注意的情况下逐步收紧。

回应文章的作者写到 TOTP 可能被输入到假网站，Evilginx 这类钓鱼工具（架在用户与真网站之间的转发服务器）能实时转发密码与验证码。NIST 的指南把需要手动输入的一次性密码排除在防钓鱼验证器之外，设置正确的同步通行密钥则列为能防钓鱼。评论的正文建议 TOTP，理由是用户可以自由选择软件与硬件。文末的补充段落提到通行密钥在多数情况下绑定域名、能抵挡中间人攻击，并推荐安全密钥。

两篇都只带过换设备与迁移，评论提到换手机时要能带走密钥，回应文章则建议想迁移的人挑支持迁移的提供者。依 FIDO 联盟的说明，同步通行密钥经端到端加密在设备之间同步。依两家的说明页，Apple 通过 iCloud 钥匙串托管恢复，Google 要用密码管理工具的 PIN 或旧 Android 设备的屏幕锁定。两家的简体中文说明页都写「通行密钥」。

到 10 月 18 日为止，Bitwarden 与 1Password 能通过 FIDO 的凭据交换协议直接导出通行密钥，这套协议仍是草案。两家都需要 iOS 26 或 Android 14 以上（Bitwarden 的导出页写 Android 10 以上），对方的 App 也要支持。KeePassXC 则把通行密钥导出成没有加密的文件。

根据 Apple 的说明页，iCloud 在中国大陆由云上贵州运营，个人信息与 iCloud 数据都存放在中国境内。到 10 月 18 日为止，Apple 的页面没有说明 iCloud 钥匙串与通行密钥在云上贵州运营的 iCloud 能否使用。第三方测量项目 GreatFire 对 `https://accounts.google.com` 最近 6 次有结论的测试，到 10 月 4 日为止都显示在中国大陆受到干扰，2012 年 2 月 22 日起就有干扰记录。GreatFire 的测试只针对网址，本文没有查证 Google 密码管理工具的通行密钥在中国大陆能否同步。

依回应文章，到 10 月 18 日为止消费者网站多半不要求证明，已经在用同步通行密钥的人登录不受影响。依 NIST 的指南，设置正确的通行密钥登录时，假网站无法取得可重复使用的登录信息。账号原有的密码与验证码仍可能被钓走，Google 的说明页也提到新增通行密钥不会移除既有的验证方式。担心被绑在某个平台的人，可以挑能直接导出通行密钥的密码管理器。

在意证明的人可以比较两种做法。依回应文章，同步通行密钥不提供证明，YubiKey 则出厂带有 Yubico 签发的证明证书。

NIST 建议服务端让用户绑定多个验证方式供恢复，依本文的推论，对用户来说就是保留两种以上的登录或恢复方式。Microsoft 的说明也提醒，只存在单一设备的通行密钥，设备丢失又没有其他恢复方式时就会失去它。
