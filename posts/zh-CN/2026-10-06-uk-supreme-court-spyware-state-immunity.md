---
title: 英国最高法院的间谍软件国家豁免判决
description: 英国最高法院 7 月 27 日以三比二判决，外国政府从国外远程入侵英国境内的电脑、造成人身伤害时，不能主张豁免（外国政府不受别国法院审理的权利）。判决只决定英国法院能否受理，入侵是否属实还没审，英国以外的法院按各自的法律判断。
date: 2026-10-06T00:05:00+08:00
slug: uk-supreme-court-spyware-state-immunity
sources:
  - title: "[2026] UKSC 25, Case UKSC/2024/0152"
    url: https://supremecourt.uk/cases/uksc-2024-0152
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: Judgment (PDF)
    url: https://supremecourt.uk/uploads/uksc_2024_0152_judgment_a1ae6cd3a5.pdf
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: Press summary (PDF)
    url: https://supremecourt.uk/uploads/uksc_2024_0152_press_summary_800976eda1.pdf
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: State Immunity Act 1978
    url: https://www.legislation.gov.uk/ukpga/1978/33
    publisher: legislation.gov.uk
  - title: U.K. Supreme Court Opens Door for Spyware Victims to Sue Foreign States
    url: https://citizenlab.ca/uk-supreme-court-opens-door-for-spyware-victims-to-sue-foreign-states/
    publisher: Citizen Lab
    date: 2026-09-02
  - title: U.K. Supreme Court Opens Door for Spyware Victims to Sue Foreign States
    url: https://www.lawfaremedia.org/article/u.k.-supreme-court-opens-door-for-spyware-victims-to-sue-foreign-states
    publisher: Lawfare
    date: 2026-08-28
  - title: Digital Security Helpline
    url: https://www.accessnow.org/help/
    publisher: Access Now
  - title: 中华人民共和国外国国家豁免法
    url: http://www.npc.gov.cn/npc/c2/c30834/202309/t20230901_431424.html
    publisher: 中国人大网
    date: 2023-09-01
  - title: 外国等に対する我が国の民事裁判権に関する法律
    url: https://laws.e-gov.go.jp/law/421AC0000000024
    publisher: e-Gov 法令検索
  - title: OONI Explorer
    url: https://explorer.ooni.org/chart/mat?probe_cc=CN&since=2026-09-01&until=2026-09-29&time_grain=day&axis_x=measurement_start_day&test_name=web_connectivity&domain=www.accessnow.org
    publisher: OONI
regions:
  - GB
  - BH
authors:
  - anoni-net
---

英国最高法院 7 月 27 日以三比二驳回巴林政府的上诉，两位住在英国的原告可以继续告巴林。一般情况下外国政府不能在别国法院被告，这叫国家豁免，巴林主张适用。原告主张巴林用 FinSpy（间谍软件）入侵他们的电脑，巴林否认指控。判决只决定英国法院能不能受理，英国以外的法院按各自的法律判断。

《1978 年国家豁免法》第 5 条规定，外国政府在英国做的事造成死亡、人身伤害或有形财物损坏时，不能主张豁免。原告主张的是人身伤害，也就是得知遭入侵后出现精神伤害。只有数据泄露或经济损失、没有人身伤害或财物损坏的索赔，不在这个例外内。

案子的核心问题是黑客从国外远程操作、入侵在英国的电脑，算不算在英国做的事。按原告的主张，操作者可能人在国外，通过位于巴林的控制服务器下指令。《欧洲国家豁免公约》要求加害者当时身在当地，英国法律的条文没有明写这一点，双方都承认本案不符合公约的条件。

三位多数大法官认为，议会有意不把公约的这项要求写进英国法律。他们也认为，用设备或远程方式完成的动作也算在英国做的事，从国外操控英国境内的电脑因此符合例外。

## 导读观点 {#perspective}

巴林主张，造成伤害的是在国外输入的指令，电脑上发生的事只是后续结果。一位持不同意见的大法官以隔着界河开枪为例，认为开枪这个动作发生在开枪的那一岸（输入指令的巴林），摄像头在英国打开是结果。多数大法官则认为，原告列出的打开麦克风和摄像头等动作发生在英国。

多数大法官举例，按巴林的解释，派人入境杀人的国家不能主张豁免、改用国外遥控的无人机却可以。他们认为这种差别不合理，公约也允许各国放宽例外。持不同意见的大法官回应，1978 年立法时没人想得到无人机和网络入侵，以加害者所在地为准也比较明确。巴林主张这种解释违反公约和国际法，少数大法官认为按国际习惯法（各国长期遵行、具有约束力的做法），例外只限加害者在场。

中国 2024 年起施行的《外国国家豁免法》有类似的例外，条文同样没有写明加害者要不要人在中国。日本的相关法律则要求加害者当时人在日本。

回到高等法院后，原告要证明入侵出自巴林并造成伤害。即使胜诉，也只有在外国政府的财产用于商业或该国书面同意时，原告才能扣押来执行判决。支持原告的研究者在 Lawfare 的文章写到，英国另一起案件的原告靠专家取证证明手机遭 Pegasus（另一款间谍软件）入侵，被告国在法院认定不能主张豁免后就不再参与诉讼。研究者的评估是外国政府实际出庭答辩时，这类诉讼的结果仍难预料。

怀疑设备遭间谍软件入侵的人，可以写信给 Access Now 的免费数字安全热线，截至 9 月 29 日说明页写明两小时内回复、受理前会先确认是否在服务范围。热线支持的十种语言没有中文，可以用英文联系。OONI（网络干扰观测项目）9 月 1 日至 29 日在中国境内测量 Access Now 网站 76 次，73 次未见干扰迹象。比较各地的法律时，可以问远程入侵算不算当地发生的事、要证明到什么程度才算外国政府所为、放宽豁免的例外会不会违反国际法，以及判决能不能执行。
