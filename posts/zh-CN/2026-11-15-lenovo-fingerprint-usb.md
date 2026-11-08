---
title: 联想指纹 U 盘的未加密 SD 卡与加密宣称的判断方式
description: 依研究者的幻灯片，联想 ThinkPlus FU100 指纹 U 盘标榜硬件加密与 AES-256，里面却是没有加密的 SD 卡。联想的声明写这批产品只由联想在中国大陆销售，受影响的客户可以安排更换。声明没有回答 AES-256 宣称是否属实（11 月 8 日查证）。其他品牌标榜加密的 U 盘，可以从密钥是否依赖密码来判断。
date: 2026-11-15T00:00:00+08:00
slug: lenovo-fingerprint-usb
categories:
  - encryption
sources:
  - title: Breaking Encrypted USB Drives with Time-Travel Debugging
    url: https://github.com/xusheng6/breaking_encrypted_USB_drives_with_TTD/blob/main/Breaking_Encrypted_USB_Drives_v2.pdf
    publisher: RE//verse 2026
  - title: NVD-CVE-2025-13453
    url: https://nvd.nist.gov/vuln/detail/CVE-2025-13453
    publisher: NVD
    date: 2026-01-14
  - title: "Lenovo's 'encrypted' fingerprint USB drive is just an unencrypted SD card in a fancy case — AI-assisted follow-up finds a backdoor and hardcoded keys in other ‘secure’ USB products (updated)"
    url: https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products
    publisher: Tom's Hardware
    date: 2026-11-01
  - title: Lenovo ThinkPlus Fingerprint USB Drive Sold as Encrypted Was a Plain SD Card Inside
    url: https://hackingpassion.com/lenovo-thinkplus-encrypted-usb-sd-card/
    publisher: HackingPassion
    date: 2026-10-29
  - title: FIPS 140-2 Cerified Flash Drives Have Security Flaw
    url: https://spectrum.ieee.org/fips-1402-cerified-flash-drives-have-security-flaw
    publisher: IEEE Spectrum
    date: 2010-01-12
  - title: Cryptographic Module Validation Program
    url: https://csrc.nist.gov/projects/cryptographic-module-validation-program
    publisher: NIST
  - title: Header Key Derivation, Salt, and Iteration Count
    url: https://veracrypt.io/en/Header%20Key%20Derivation.html
    publisher: VeraCrypt
  - title: VeraCrypt Downloads
    url: https://veracrypt.io/en/Downloads.html
    publisher: VeraCrypt
  - title: BitLocker overview
    url: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/
    publisher: Microsoft
  - title: BitLocker FAQ
    url: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq
    publisher: Microsoft
  - title: Volume encryption with FileVault in macOS
    url: https://support.apple.com/guide/security/volume-encryption-with-filevault-sec4c6dc1b6e/web
    publisher: Apple
  - title: Encrypt and protect a storage device with a password in Disk Utility on Mac
    url: https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac
    publisher: Apple
  - title: Frequently Asked Questions Cryptsetup/LUKS
    url: https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/FAQ.md
    publisher: cryptsetup
  - title: 联想指纹U盘翻车：宣称加密实际明文存储
    url: https://tech.ifeng.com/c/8xh9aBEZS6U
    publisher: 凤凰网（转载 IT之家）
    date: 2026-11-01
authors:
  - anoni-net
---

U 盘标榜“加密”或“指纹解锁”，不代表里面的文件经过加密。一位研究者 2026 年 3 月在逆向工程研讨会 RE//verse 的幻灯片拆解了联想 ThinkPlus FU100 指纹 U 盘，结论是外壳里只有一张 SD 卡，数据没有任何加密。依联想经 Tom's Hardware 转载的声明，这批 ThinkPlus 存储产品为中国市场设计，也只由联想在中国大陆销售。幻灯片另外列出其他受影响的设备，下面的判断方式也可用在其他品牌标榜加密的产品。

拆解与结论都出自幻灯片，以下依幻灯片的文字与 Tom's Hardware、安全博客 HackingPassion 的转述。幻灯片写着“It's just an SD card in a fancy case”（只是装在漂亮外壳里的 SD 卡），指纹识别只控制 USB 连接。依 HackingPassion 的描述，指纹决定的是 U 盘要不要连上电脑，卡上的文件不受它影响。

“硬件加密”与 AES-256（广泛使用的加密算法）两项宣称列在幻灯片的 FU100 介绍页，图片来源标示为 Alibaba.com。到 11 月 8 日，本文查不到联想官网的 FU100 产品页，无法确认联想自己的渠道是否用过同样的文字。

依幻灯片与 HackingPassion，研究者 2025 年 8 月 2 日通报联想。2025 年 8 月 27 日的临时修补是在 SD 卡上覆盖一层环氧树脂（epoxy），完整修补排在 2025 年 12 月。联想的声明提到接获通报后与研究者协调披露，通过硬件与软件升级修复，并在 2026 年 1 月发布安全公告与三个 CVE（公开的漏洞编号）。

联想公告 LEN-210545 的原页在 11 月 8 日查阅时返回 Access Denied，公告内容只能依二手来源与美国国家漏洞数据库（NVD）的记录。NVD 上由联想提交的记录写到，有实体接触的人可能读取 U 盘上的数据，受影响的是 ThinkPlus FU100、FU200、TU800 与 TSD303 的第一代。

依 HackingPassion 与 Tom's Hardware，同一场演讲里的外接 SSD TSD303 有加密数据，问题出在密码验证。设备会把正确的密码以明文经 USB 传回电脑上的程序比对。第一版修补改成加密后传送，密钥却可由程序推算，2025 年 12 月的第二版改由设备自行比对。依 HackingPassion 的整理，幻灯片列出的十款使用相同软件套件的设备（幻灯片上的厂商名称经过遮蔽）有两款把数据未加密存在 micro SD 卡上，八款的问题在密码传送。

联想的声明没有回答 AES-256 与硬件加密的宣称是否属实，也没有承认或否认 SD 卡未加密。依 HackingPassion，联想与研究者都没有提到有人实际遭到攻击，本文到 11 月 8 日也没有查到受害案例。

## 导读观点 {#perspective}

指纹与密码界面控制的可能只是连接，数据有没有受到保护，要看解密密钥从哪里来。依 HackingPassion 的整理，第一种可靠的做法是密钥由密码经过 PBKDF2 或 Argon2 这类刻意放慢的函数衍生，每猜一次都要花时间。另一种是验证完全在设备自己的芯片内进行，密码与密钥都不离开芯片。依幻灯片，FU100 的数据没有加密，两种做法都没有用上（本文的推论）。

存储设备厂商 Netac 的软件加密工具在研究者测试的版本里，AES-256 密钥是写在程序里的固定值，跟用户的密码无关（依 Tom's Hardware 与 HackingPassion）。Tom's Hardware 也写到，Netac 到研究者 2026 年 3 月的演讲时没有修补。软件加密与 FU100 完全没有加密的性质不同，标示 AES-256 同样看不出密钥的来源（本文的归纳）。

FIPS 140（美国政府的密码模块标准）由 NIST 的密码模块验证计划（CMVP）管理，模块交由独立实验室测试。证书可以在 NIST 的清单查询，依 NIST 的页面，FIPS 140-2 的证书在 2026 年 9 月 21 日后移到 Historical List（历史清单）。依 IEEE Spectrum 的报道，德国安全公司 SySS 2009 年 12 月公开绕过多款 FIPS 140-2 认证 U 盘的方法，不论密码为何都能在数秒内还原数据。IEEE Spectrum 引述 GCN 的报道，NIST 当时新闻稿的初步分析把问题指向授权解密的软件（the software authorizing decryption）而非通过认证的密码模块，也提到正在调查认证流程是否需要调整。

到 11 月 8 日，本文查不到 FU100 通过 FIPS 140 或中国商用密码认证（中国对商用密码产品的认证制度）的资料。HackingPassion 的建议是把 U 盘上的指纹或密码界面当成访问的锁，除非厂商说明密钥依赖它。NIST 的初步分析把问题指向软件，本文据此推论，查到证书之后仍需要厂商说明密钥如何生成、密码在哪里验证。

手上有 NVD 列出的四款第一代设备的人，依联想的声明可以联系联想技术支持安排更换。依 HackingPassion 转述，免费升级（free upgrade）要拨打中国的服务专线，设备会送回更换或到场升级固件。同样依 HackingPassion 转述，联想建议送出前先备份数据，再擦除或格式化。

联想的声明写明这批产品只由联想在中国大陆销售，中国大陆的读者手上可能有这些型号，可以先对照上文 NVD 列出的四款第一代设备。IT之家 11 月 1 日的报道经凤凰网转载，标题为“联想指纹U盘翻车：宣称加密实际明文存储”，内容与 HackingPassion 一致。更换专线的来源是 HackingPassion 的转述，联想的声明只写客户可以联系联想技术支持。中国大陆以外的读者若有这些型号，多半是转售或平行进口的产品（本文的推论）。

其他品牌的 U 盘要放敏感文件时，可以在文件放上去之前自行加密，让密钥来自自己设置的密码（HackingPassion 列出的建议之一）。VeraCrypt（开源的磁盘加密软件）的下载页列出 Windows、macOS 与 Linux 版本，非系统卷与文件容器支持 PBKDF2 与 Argon2id 两种密钥衍生方式。代价是每台要打开文件的电脑都要能运行 VeraCrypt。

Microsoft 的说明页只列出 Windows Pro、Enterprise、Education 等版本可以启用 BitLocker，Home 版不在表内。依 BitLocker FAQ，BitLocker To Go 涵盖 USB 闪存盘与 SD 卡，加密后可以在另一台电脑用密码打开。Home 版能否解锁已加密的 U 盘，本文没有核对到官方文档。

Apple 的安全指南写到 FileVault 保护内置与可移除的存储设备，磁盘工具也可以在格式化时用密码加密外接设备，加密前需先擦除设备。LUKS（Linux 常用的磁盘加密格式）依 cryptsetup 的 FAQ 以 PBKDF2 或 Argon2 处理密码，FAQ 也建议备份 LUKS 头（header），头损坏可能无法解密。macOS 加密的外接盘与 LUKS 能否在其他操作系统打开，本文没有核对到官方文档，要跨电脑使用的人需先实际试过。

自行加密可以应对 U 盘遗失或被别人取走的情况，电脑本身已遭入侵、密码太短或忘记密码时都帮不上忙（本文的推论）。只放公开数据的 U 盘不需要多做这一步，要放个人数据或工作文档的人，再衡量每台电脑都要能运行加密软件的代价。
