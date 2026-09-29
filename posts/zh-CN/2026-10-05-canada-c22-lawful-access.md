---
title: 加拿大 C-22 合法访问法案与加密
description: 加拿大的 C-22 法案已在众议院三读通过，政府能要求通信与网络服务商建立协助执法的技术能力、保存元数据，部分加拿大以外的服务商也在范围内。加拿大以外的读者现在不需要调整设置。
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
  - title: Signal, DuckDuckGo among firms weighing Canada exit over lawful access bill
    url: https://globalnews.ca/news/11886905/lawful-access-bill-c-22-companies-services-canada/
    publisher: Global News
    date: 2026-06-04
  - title: The UK Is Still Trying to Backdoor Encryption for Apple Users
    url: https://www.eff.org/deeplinks/2025/10/uk-still-trying-backdoor-encryption-apple-users
    publisher: EFF
    date: 2025-10-01
  - title: Apple can no longer offer Advanced Data Protection in the United Kingdom to new users
    url: https://support.apple.com/en-us/122234
    publisher: Apple
    date: 2025-09-22
  - title: iCloud in China mainland
    url: https://support.apple.com/en-us/111754
    publisher: Apple
  - title: 中华人民共和国反恐怖主义法
    url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2018-06/12/content_2055871.htm
    publisher: 中国人大网
    date: 2018-06-12
  - title: 如何開啟「iCloud 進階資料保護」
    url: https://support.apple.com/zh-tw/108756
    publisher: Apple
    date: 2026-04-24
  - title: 如何打开 iCloud 高级数据保护
    url: https://support.apple.com/zh-cn/108756
    publisher: Apple
    date: 2026-04-24
regions:
  - CA
authors:
  - anoni-net
---

加拿大的《合法访问法》（Bill C-22）6 月 18 日在众议院三读通过，到 9 月 29 日为止，参议院的二读还没有完成。法案让政府能要求通信与网络服务商建立协助执法的技术能力，部分加拿大以外的服务商也在适用范围内。数字权利组织 Access Now 与多个欧洲民间组织 9 月致信欧盟要求介入，新闻稿写到法案最快可能在 10 月成为法律。加拿大以外的读者现在不需要调整设置。

技术能力的要求分成两层，第一层适用于「核心服务商」（core providers），这些服务商要按法规具备指定的能力。第二层是公共安全部长的命令，可以要求任何服务商建立特定能力。命令只需要独立的情报专员（Intelligence Commissioner）批准，不必经过法院。收到命令的服务商不得透露命令的存在与内容。

法案也允许以法规要求服务商保存元数据（metadata，通信内容以外的记录）。最长保存期限在初版是一年，众议院通过的版本改成六个月。按多伦多大学研究机构 Citizen Lab 6 月初的分析，元数据很可能包括每个人跟谁联系、行动轨迹，以及用过哪些 App。

条文写明，服务商不必遵守会「引入系统性漏洞」的要求。用户自行加密、服务商手上没有密钥的数据，服务商也不必解密。

Signal 6 月出席众议院委员会作证，立场是被迫在背叛用户与离开市场之间选择时，会离开加拿大。DuckDuckGo 也向加拿大媒体 Global News 确认，法案若按 6 月初、众议院修正前的版本通过，会在加拿大下架 VPN 服务。

## 导读观点 {#perspective}

端到端加密的密钥只存在通信双方的设备上，运营 Signal 这类服务的服务商没有密钥，按条文的文字应该落在解密例外之内。争议集中在部长命令能要求的范围，按 Citizen Lab 的分析，可能包括改变服务的运作方式与在服务里嵌入监控工具。

英国政府 2025 年 1 月依《调查权力法》，对 Apple 发出了同类的技术能力通知（EFF 2025 年 10 月的文章）。Apple 选择在英国撤下 iCloud 高级数据保护，没有建立后门，Apple 的说明页也写明英国的新用户不能开启。类似的协助义务在中国大陆写在《反恐怖主义法》第十八条，电信业务经营者、互联网服务提供者「应当为公安机关、国家安全机关依法进行防范、调查恐怖活动提供技术接口和解密等技术支持和协助」。

到 9 月 29 日为止，法案还需要参议院二读、三读与御准（Royal Assent，成为法律前的最后程序）。实际影响要看部长对哪些服务商下命令。服务商握有密钥的数据不在解密例外之内，例如没有端到端加密的云备份。

想让云备份也改用端到端加密的 iPhone 用户，可以开启 iCloud 的高级数据保护，iCloud 云备份与照片等大部分数据都会纳入。条件是账户已开启双重认证、登录同一账户的所有设备都更新到 iOS 16.2、macOS 13.1 等对应版本以上，管理式账户与儿童账户不能使用。开启前要设置恢复联系人或 28 个字符的恢复密钥，因为 Apple 无法协助找回端到端加密的数据，入口在「设置」的姓名、「iCloud」与「高级数据保护」（Apple 的帮助页面有简体中文版）。中国大陆的 iCloud 由 GCBD（AIPO Cloud (Guizhou) Technology Co. Ltd）运营，Apple 的高级数据保护说明页没有写明中国大陆账户能否开启。
