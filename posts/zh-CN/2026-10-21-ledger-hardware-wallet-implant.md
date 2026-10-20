---
title: Ledger 硬件钱包的植入芯片事件
description: Ledger 10 月 15 日确认，犯罪团伙在正品硬件钱包里加装设置时截取恢复短语的部件，再经东南亚的经销商流入市场。到 10 月 13 日为止，Ledger 确认的盗取都与授权经销商 CryptoBilis 售出的设备有关，其他渠道的植入物报告还没有证实。Ledger 的正品验证检测不到这类植入物，在 CryptoBilis 买过设备且已经设置的人，Ledger 建议把资产转到新设备与新的恢复短语。
date: 2026-10-21T00:05:00+08:00
slug: ledger-hardware-wallet-implant
categories:
  - security
sources:
  - title: Ledger’s Response to the Hardware Implant Attack
    url: https://www.ledger.com/blog-response-hardware-implant-attack
    publisher: Ledger
    date: 2026-10-15
  - title: Check hardware integrity
    url: https://support.ledger.com/article/4404382029329-zd
    publisher: Ledger Support
  - title: Best Practices To Securely Buy Your Ledger Signer
    url: https://www.ledger.com/academy/topics/ledgersolutions/best-practices-to-securely-buy-ledger-signer
    publisher: Ledger Academy
    date: 2026-03-06
  - title: Purchasing from an authorised reseller
    url: https://support.ledger.com/article/Purchasing-from-an-authorised-reseller
    publisher: Ledger Support
  - title: Find a Ledger Reseller around the world
    url: https://shop.ledger.com/pages/resellers
    publisher: Ledger
  - title: Why is Ledger Nano so Secure?
    url: https://www.ledger.com/academy/basic-basics/ledgers-bit-of-it/ledger-nano-security-made-easy
    publisher: Ledger Academy
  - title: Ledger says hardware implant in cryptocurrency wallets stole recovery phrases
    url: https://therecord.media/ledger-cryptocurrency-wallet-implant-theft
    publisher: The Record
    date: 2026-10-13
  - title: "Ledger Nano X: the spy implant."
    url: https://www.tibane.net/research/ledger-nano-x-implant
    publisher: Tibane Labs
  - title: The Ledger CryptoBilis hack took $102.0M from 335 wallets. One thief had all the keys
    url: https://bitquery.io/investigations/ledger-cryptobilis-hack
    publisher: Bitquery
    date: 2026-10-10
  - title: Who Is Planting Backdoors in Ledger Crypto Wallets?
    url: https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/
    publisher: Zero Day
    date: 2026-10-13
  - title: Ledger suspends retail sales in Germany as wallet implant probe continues
    url: https://crypto.news/ledger-suspends-retail-sales-in-germany-as-wallet-implant-probe-continues/
    publisher: crypto.news
    date: 2026-10-13
  - title: Ledger confirms hidden chip in crypto wallet amid $92M theft claims
    url: https://crypto.news/ledger-confirms-hidden-chip-in-crypto-wallet-amid-92m/
    publisher: crypto.news
    date: 2026-10-11
  - title: Ledger reveals how hidden chips stole wallet recovery keys
    url: https://crypto.news/ledger-reveals-how-hidden-chips-stole-recovery-phrases/
    publisher: crypto.news
    date: 2026-10-13
  - title: Ledger asks resellers to halt sales in Southeast Asia and Hong Kong
    url: https://cointelegraph.com/news/ledger-asks-resellers-to-halt-sales-in-southeast-asia-and-hong-kong
    publisher: Cointelegraph
    date: 2026-10-13
  - title: Shipping Restrictions and Delivery Options by Country/Region
    url: https://support.ledger.com/article/360006562214-zd
    publisher: Ledger Support
    date: 2026-10-08
  - title: "央行等八部门：虚拟货币业务非法，持续整治“挖矿”！"
    url: https://m.gmw.cn/2026-02/07/content_1304335528.htm
    publisher: 光明网
    date: 2026-02-07
authors:
  - anoni-net
---

硬件钱包厂商 Ledger 10 月 15 日在官方博客确认，一个犯罪团伙花了好几个月买进正品的 Ledger 设备。团伙打开设备装上隐藏的部件，在用户设置设备时截取恢复短语（也常称助记词，24 个英文单词，可以恢复钱包里的全部资产），再通过东南亚的经销商流回市场。依链上分析公司 Bitquery 的时间线，大规模盗取从 10 月 9 日开始。依 The Record 引述 Ledger 10 月 13 日的说明，已确认的盗取都与 Ledger 授权的东南亚经销商 CryptoBilis 售出的设备有关。

依 Cointelegraph 引述，Ledger 10 月 13 日也表示还没有证实其他渠道买的设备发生盗取。Ledger 10 月 15 日的文章提到已请东南亚与香港的经销商暂停销售。官方的正品验证（Genuine Check，连接 Ledger 服务器确认安全芯片是原厂的检查）检测不到这类植入物。

依 Ledger 10 月 15 日的文章，芯片、操作系统与服务器都没有缺陷。Ledger 在文章里把事件定性为设备离开 Ledger 之后、在经销渠道发生的「localized distribution attack」（区域性的经销攻击），The Record 也引述 Ledger 认为受影响的设备数量有限。依 The Record 引述 Ledger 10 月 13 日的说明，植入物读取屏幕上显示的数据，在设置时识别出恢复短语后用内置的 eSIM 经 LTE 移动网络传出。

区块链研发公司 Tibane Labs 拆解了两台分别在日本拍卖网站与 Amazon Japan 卖家买到的 Nano X，页面也写明没有测试过 CryptoBilis 的设备。植入物是焊在主板上、接到屏幕数据线的小型计算机，没有去破解安全芯片（Secure Element，存放私钥的芯片）。Tibane Labs 比较了三个版本，最新版本的专用天线印有零件编号与版本号，Tibane Labs 据此判断植入物是量产品。

到 10 月 20 日为止，Ledger 没有公布受影响的型号、批次、人数与金额。Bitquery 到 10 月 16 日统计出 335 个钱包、共 1.02 亿美元被转走，crypto.news 等早期报道的 9,290 万美元是 Bitquery 较早版本的数字。Bitquery 的页面提到链上记录指向同一个行为者持有所有被盗钱包的密钥，但链上只看得到转账，看不出密钥是从哪里泄露的。

网络安全记者的邮件通讯 Zero Day 10 月 13 日报道了 CryptoBilis 以外渠道的植入物。一位未具名的日本研究者对 Zero Day 说，他累计向非授权网店卖家买了十台（最早在 3 月），全部都有植入物。同一篇报道引述一位德国买家在 X 的帖子，他在 Ledger 列为德国授权经销商的 MediaMarkt 两家门店，买到有植入物的 Nano X。到 10 月 20 日为止，Ledger 没有证实这些说法。

The Record 引述 Ledger 10 月 13 日的说明，Ledger「also reviewing reports of implants in other signers and locations」。依 crypto.news 的报道，MediaMarkt 在 Ledger 同意下暂停销售。Ledger 表示德国的案例没有收到资金损失的报告，也没有确认德国的报告与其他案例是否相关。Ledger 10 月 15 日的文章提到曾派人到包括德国在内的市场买设备拆开检查，「Every unit examined was clean」，但没有公布检查的数量。

## 导读观点 {#perspective}

依 Ledger 的教学网站 Ledger Academy，私钥存在安全芯片里。恢复短语由设备在初始化时生成，也只在那时显示一次。依检查硬件完整性的帮助页，正品验证确认的是原厂写入安全芯片的密钥，用来挡下仿冒品。同一页也提醒，只要原厂的安全芯片完好，正品验证就检测不到植入物这类物理改装。

The Record 与 Tibane Labs 描述的植入物不碰安全芯片，在恢复短语显示的那一刻从屏幕的数据线读走恢复短语。检查硬件完整性的帮助页提到，Nano X 与 Nano S Plus 开机时由安全芯片检查主控芯片的固件，被改过会出现警告。帮助页另外列出的检查方式是拆壳对照官方的内部照片，确认没有多出芯片。Tibane Labs 的页面提到设备本身不会察觉植入物，最新版本的植入物也涂成与原厂电路板相同的颜色。

依 The Record 引述 Ledger 10 月 13 日的说明，在 CryptoBilis 买的设备还没设置的话不要设置，直接联系客服。已经设置的，要尽快把资产转到新的设备与新的恢复短语，也不要在 CryptoBilis 买的设备上输入或恢复任何恢复短语。受害者要先联系 Ledger 与当地警方，再决定是否拆壳或寄送设备。

在其他渠道买到来源不明的 Nano X、已经设置过的人，到 10 月 20 日为止 Ledger 没有提出更换恢复短语的建议。Tibane Labs 的页面则建议换掉在来源不明的 Nano X 上显示过的恢复短语，在可信的设备上生成新的恢复短语再把资产转过去。页面也提到，被改装的屏幕显示过的恢复短语，就算设备从没连上网络也要当成已经泄露。依检查硬件完整性的帮助页，懂硬件的人可以拆壳对照，但拆壳造成的损坏不在保修范围。

还没买或刚收到设备的人，可以参照客服中心的购买说明页，到 10 月 20 日为止客服中心有简体中文版。包装看起来被打开或重新封装、盒内已经附上写好恢复短语卡片的设备都不要使用，直接联系客服。

Ledger 建议向官方商店或授权经销商购买，到 10 月 20 日为止经销商页列出台湾 6 家与香港 5 家，没有中国大陆的项目。香港的项目没有标示暂停销售。官方商店的寄送限制页（页面标示更新日期 2026 年 10 月 8 日）列出不寄送福建省与广州，页面没有列出可以寄送的地区。

中国人民银行等八部门 2026 年 2 月 6 日发布《关于进一步防范和处置虚拟货币等相关风险的通知》，本文依据的是光明网转载的全文，没有取得原发布机关的页面。转载全文把境内的虚拟货币兑换、交易等业务列为涉嫌非法金融活动。投资虚拟货币等违背公序良俗的，相关民事法律行为无效，损失由投资者自行承担。全文没有提到钱包，持有或购买硬件钱包是否违规，本文查不到相关规定（不等于没有）。

CryptoBilis 与 MediaMarkt 都在 Ledger 的授权名单上，Ledger Academy 的购买指南也写到「no global supply chain is entirely immune」。依本文的推论，授权渠道能降低风险，但不能保证设备没被改装。

Ledger 在 10 月 15 日的文章里要求经销商不再把设备放在货架与展示柜，改从库存直接交给买家，并重申退货的设备一律不得转售。同一篇文章预告之后会公布更完整的技术细节，也在开发产品层面的防护措施。这两项的后续，以及 Ledger 是否扩大确认的范围，是接下来可以留意的地方。
