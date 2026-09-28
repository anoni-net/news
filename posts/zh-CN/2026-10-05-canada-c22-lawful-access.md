---
title: 加拿大 C-22 合法访问法案与加密
description: 加拿大的 C-22 法案已在众议院三读通过，让政府能要求通信与网络服务商建立协助执法的技术能力、保存元数据，范围包括部分加拿大以外的服务商。Signal 与 DuckDuckGo 等服务商考虑撤出加拿大。
date: 2026-10-05T07:05:00+08:00
slug: canada-c22-lawful-access
sources:
  - title: C-22 (45-1) Lawful Access Act, 2026
    url: https://www.parl.ca/legisinfo/en/bill/45-1/c-22
    publisher: Parliament of Canada
  - title: Bill C-22, Third Reading
    url: https://www.parl.ca/documentviewer/en/45-1/bill/C-22/third-reading
    publisher: Parliament of Canada
  - title: The EU must act now to protect privacy and encryption from Canada’s overreaching Bill C-22
    url: https://www.accessnow.org/press-release/the-eu-must-act-now-canadas-overreaching-bill-c-22/
    publisher: Access Now
    date: 2026-09-14
  - title: Analysis of Proposed Surveillance Law Expansion under Bill C-22
    url: https://citizenlab.ca/research/analysis-of-proposed-surveillance-law-expansion-under-bill-c-22/
    publisher: Citizen Lab
    date: 2026-06-02
  - title: "Open Letter on Bill C-22: An Act respecting lawful access"
    url: https://www.globalencryption.org/2026/04/open-letter-on-bill-c-22-an-act-respecting-lawful-access/
    publisher: Global Encryption Coalition
    date: 2026-04-28
  - title: Signal, DuckDuckGo among firms weighing Canada exit over lawful access bill
    url: https://globalnews.ca/news/11886905/lawful-access-bill-c-22-companies-services-canada/
    publisher: Global News
    date: 2026-06-04
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: 中华人民共和国反恐怖主义法
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: 中国人大网
    date: 2018-06-12
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法访问法》（Bill C-22）6 月 18 日在众议院三读通过，到 9 月 29 日为止还在参议院，二读还没有完成。法案让政府能要求通信与网络服务商建立协助执法的技术能力，也适用于部分加拿大以外的服务商与用户。Access Now 与多个欧洲公民团体 9 月发表公开信，请欧盟要求加拿大修改法案，新闻稿写到法案最快可能在 10 月成为法律。

法案第二部分的第一层是「核心服务商」，要按法规具备指定的技术能力，Global News 报道核心服务商可能是大型电信与卫星运营商。第二层是公共安全部长的命令，可以要求任何服务商建立特定能力。命令经情报专员核准即可生效，不必取得法院令状。服务商不得透露自己收到命令，也不得透露命令的内容。

法案也允许以法规要求服务商保存元数据（metadata）。Citizen Lab 6 月初分析的版本最长保存一年，众议院通过的版本改成不超过六个月。Citizen Lab 的分析写到，元数据至少可能包括每个人跟谁联系、行动轨迹，以及用过哪些 App。

条文写明，服务商可以不遵守会「引入系统性漏洞」的要求，也不必替用户自行加密、服务商没有密钥的数据解密。Global Encryption Coalition 4 月针对初版的公开信写到，「系统性漏洞」的定义模糊，「加密」在法案里也没有定义。Signal 6 月在众议院委员会作证，证词的内容是如果被迫在背叛用户与离开市场之间选择，会选择离开。DuckDuckGo 也向 Global News 确认，法案按目前版本通过，就会在加拿大下架 VPN 服务。

## 导读观点 {#perspective}

端到端加密的密钥只存在通信两端的设备上，服务运营方手上没有密钥，条文的解密例外涵盖的正是这种设计。争议在于部长命令能要求的范围，按 Citizen Lab 的分析，这些义务可能包括改变服务的运作方式或在服务里嵌入监控工具。

为执法建立的访问通道也可能被其他人利用，Global Encryption Coalition 的公开信举 2024 年的 Salt Typhoon 为例。攻击者利用普通的软件漏洞与窃取的账号密码进入美国电信网络，接着直接使用电信运营商依法建置的监听功能。

类似的制度在英国已有先例，政府依《调查权力法》向 Apple 发出秘密命令后，Apple 不再让英国的新用户开启 iCloud 高级数据保护。按 Global Encryption Coalition 公开信的描述，Apple 选择停掉这项功能，没有替政府建立访问加密数据的通道。中国的《反恐怖主义法》第十八条则直接规定，电信业务经营者、互联网服务提供者应当为公安机关、国家安全机关提供技术接口和解密等技术支持和协助。

加拿大以外的读者现在不需要调整任何设置。法案还要经过参议院二读、三读与御准才会生效，之后的影响要看部长对哪些服务商下命令，而收到命令的服务商不能公开。解密例外只涵盖服务商没有密钥的加密，服务商握有密钥的数据不在例外之内，例如没有端到端加密的云备份。常用 App 的备份是否有端到端加密，可以趁这次检查一遍。
