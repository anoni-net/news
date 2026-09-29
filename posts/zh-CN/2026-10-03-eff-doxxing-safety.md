---
title: 人肉搜索的预防与应对
description: EFF 8 月底发布两篇人肉搜索防护指南，从盘点自己的数字足迹开始，到事发时记录事件、加固账号与请运营商加设密码。指南以美国读者为对象，盘点足迹与加固账号的步骤在其他地方同样适用。
date: 2026-10-03T07:00:00+08:00
slug: eff-doxxing-safety
sources:
  - title: "Doxxing Safety Pt I: Prevention and Footprint Management"
    url: https://www.eff.org/deeplinks/2026/08/doxxing-safety-pt-i-prevention-and-footprint-management
    publisher: Electronic Frontier Foundation
    date: 2026-08-31
  - title: "Doxxing Safety Part II: Incident Response"
    url: https://www.eff.org/deeplinks/2026/08/doxxing-safety-part-ii-incident-response
    publisher: Electronic Frontier Foundation
    date: 2026-08-31
  - title: The Personal Data (Privacy) (Amendment) Ordinance 2021
    url: https://www.pcpd.org.hk/english/data_privacy_law/amendments_2021/amendment_2021.html
    publisher: Office of the Privacy Commissioner for Personal Data, Hong Kong
    date: 2021-10-08
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawOldVer.aspx?pcode=I0050021
    publisher: 全國法規資料庫
    date: 2023-05-31
  - title: 最高人民法院 最高人民检察院 公安部印发《关于依法惩治网络暴力违法犯罪的指导意见》的通知
    url: http://gongbao.court.gov.cn/Details/12dfb372281fcfc26a1489d012108b.html
    publisher: 最高人民法院公报
    date: 2023-09-20
  - title: "Have I Been Pwned: Check if your email address has been exposed in a data breach"
    url: https://haveibeenpwned.com/
    publisher: Have I Been Pwned
  - title: FAQs - Have I Been Pwned
    url: https://haveibeenpwned.com/FAQs
    publisher: Have I Been Pwned
  - title: DROP for data brokers
    url: https://privacy.ca.gov/data-brokers
    publisher: California Privacy Protection Agency
  - title: Connecting to Tor from censored regions
    url: https://support.torproject.org/tor-browser/circumvention/connecting-from-censored-regions/
    publisher: Tor Project
  - title: Is http://www.torproject.org blocked in mainland China?
    url: https://en.greatfire.org/www.torproject.org
    publisher: GreatFire
  - title: Is https://haveibeenpwned.com blocked in mainland China?
    url: https://en.greatfire.org/https/haveibeenpwned.com
    publisher: GreatFire
authors:
  - anoni-net
---

美国数字权利组织电子前哨基金会（EFF）于 8 月 31 日发布两篇人肉搜索（doxxing）防护指南。EFF 把人肉搜索定义为刻意公开他人的个人信息，用来霸凌、骚扰或恐吓。第一篇的主题是事前预防，第二篇是事发时的应对。指南以美国读者为对象，但盘点足迹与加固账号的步骤各地都适用。

预防从盘点自己开始，先查信息有没有出现在泄露数据库中，再用用户名搜索工具列出自己注册过的网站。EFF 也写明这类工具的结果不一定准确。社交账号可以改为私密。

数据经纪商（收集并转卖个人信息的公司）常是人肉搜索所用信息的来源。据 EFF 引用的研究，自行申请删除比付费代办服务有效。自行申请相当耗时，不想自己处理的人仍可考虑付费服务。

事发时先建立事件记录，写下时间、地点、相关的人与看到的内容。查看骚扰者聚集的论坛时，EFF 建议用 Tor Browser（隐藏连接来源的浏览器），不与任何人互动。监看与记录可以分给信任的朋友，事先也可以准备分为主要、替代、备用、紧急或撤离四层的 PACE 应对计划。

仍要使用的账号开启双重验证，成为攻击目标的账号可以先停用。电信与银行账户如果提供安全密码或 PIN 码，可以先加设，防止对方冒充本人转走号码（SIM swapping）后接管其他账号。

## 导读观点 {#perspective}

人肉搜索靠的是把零碎信息拼成个人档案。指南里有些工具只在美国有，例如部分州用代转地址取代住址的地址保密计划、让加州居民一次向所有登记的数据经纪商申请删除的 DROP。据 GreatFire 的测试记录（9 月 29 日查阅），Tor Project 官网在中国大陆被封锁。Tor Project 在说明页建议境内用户通过 GetTor 取得 Tor Browser，再用网桥（未公开的 Tor 入口）连接。

依最高人民法院、最高人民检察院与公安部 2023 年 9 月印发的网络暴力指导意见，组织“人肉搜索”、违法收集并向不特定多数人发布公民个人信息且情节严重的，以侵犯公民个人信息罪定罪处罚。受害人有证据证明侵害正在发生或即将发生时，可以依民法典第 997 条向法院申请人格权侵害禁令。

香港 2021 年 10 月起把“起底”列为罪行，最高可处罚款港币 100 万元及监禁 5 年。当地的个人资料私隐专员（个人资料主管机关的首长）还可以发出停止披露通知，要求移除起底内容。台湾《个人资料保护法》第 41 条的刑度是 5 年以下有期徒刑，可并处新台币 100 万元以下罚金。适用对象是意图为自己或第三人谋取不法利益、或损害他人利益，违法收集、利用个人资料而足以造成损害的人。

报案或投诉都需要证据，事件记录最好从第一条骚扰就附上截图与网址。要不要报警因人而异，EFF 在第二篇写到，许多人报警只会让情况更糟。

现在就能做的第一步，是到 Have I Been Pwned（泄露事件查询网站）输入自己的邮箱，点击查询就能知道是否泄露。到 9 月 29 日为止，查询免费、不需要注册账号，网站只有英文界面。据 GreatFire 2 月 9 日的测试，网站在中国大陆可以打开。查到泄露时可以更换邮箱或电话号码，EFF 也写明这样做非常不方便。
