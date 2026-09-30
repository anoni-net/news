---
title: 英国最高法院的间谍软件国家豁免判决
description: 巴林政府被控从国外用间谍软件入侵英国境内的电脑、造成原告精神伤害，英国最高法院判决它不能以外国政府不受别国法院审理为由挡下这场诉讼。判决只决定英国法院能否受理，入侵是否属实还没审。
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

英国最高法院 7 月 27 日以三比二驳回巴林政府的上诉，两位住在英国的原告可以继续告巴林。一般情况下外国政府不能在别国法院被告，这叫国家豁免，巴林主张自己享有这项豁免。原告主张巴林用 FinSpy（间谍软件）入侵他们的电脑，巴林否认指控。判决只决定英国法院能不能受理，英国以外的法院按各自的法律判断。

《1978 年国家豁免法》第 5 条规定，外国政府在英国做的事造成死亡、人身伤害或有形财物损坏时，不能主张豁免。原告主张的是人身伤害，也就是得知遭入侵后出现精神伤害。只有数据泄露或经济损失、没有人身伤害或财物损坏的索赔，不在这个例外内。

案子的核心问题是黑客从国外远程操作、入侵在英国的电脑，算不算在英国做的事。按原告的主张，操作者可能人在国外，通过位于巴林的控制服务器下指令。

英国加入了《欧洲国家豁免公约》，公约有类似的例外，另外要求加害者当时人在法院所在的国家。双方都承认，按原告的主张，本案不符合公约的这项条件。但英国《国家豁免法》第 5 条的条文没有明写这个条件，所以争点变成第 5 条要不要按公约的条件来读。

五位大法官里，三位多数大法官认为，议会有意不把公约的这项要求写进第 5 条。他们还认为通过软件或设备远程操作的动作也算在英国做的事，所以从国外操控英国境内的电脑符合例外。另外两位持不同意见的少数大法官则认为，第 5 条应该按公约的条件来读，也就是要求加害者当时人在英国。

## 导读观点 {#perspective}

巴林主张，造成伤害的是在国外输入的指令，电脑上发生的事只是后续结果。其中一位少数大法官以隔着界河开枪为例，认为下指令的动作跟开枪一样发生在巴林这一岸，摄像头在英国打开只是结果。原告列出十类发生在英国的动作，例如传送安装文件、打开麦克风和摄像头、记录键盘输入。多数大法官认为，这些动作合起来就是在英国进行的监控。

多数大法官举例，外国政府派人入境杀人时不能主张豁免，巴林也同意这一点。按巴林的解释，改用国外遥控的无人机杀人却可以主张豁免，多数大法官认为这种差别不合理。同一位少数大法官回应，1978 年立法时没人想得到无人机和网络入侵，法律要按立法当时的背景解读。他也认为，以加害者所在地为准比较明确，容易判断。

另一个争点是放宽例外会不会让英国违反国际法。国际法除了公约，还有各国长期一致遵行、当成义务的做法，称为习惯国际法。多数大法官认为公约允许各国放宽例外，英国把例外用在外国政府行使国家权力的行为上，也有习惯国际法上的合理依据。行使国家权力的行为指政府以国家身份做的事，相对于一般的商业往来，本案指控的入侵双方都同意属于前者。

巴林主张放宽例外会让英国违反公约和习惯国际法。同一位少数大法官也同意，因为公约允许的放宽不能超出习惯国际法。他指出，习惯国际法只容许加害者身在当地时的例外，也找不到任何一个国家在加害者不在当地时不给豁免。

中国 2024 年起施行的《外国国家豁免法》有类似的例外，条文同样没有写明加害者要不要人在中国。日本 2009 年制定的相关法律则明文要求加害者当时人在日本。条文没写明加害者要不要在场时，能不能读出这个条件，正是英国两派大法官分歧的地方。

案子回到一审的高等法院后才会审入侵是否属实，原告要证明入侵出自巴林，也要证明入侵造成了伤害。Citizen Lab 与 Access Now 的研究者在 Lawfare 的文章提到英国另一起案件，原告靠专家取证证明手机遭另一款间谍软件 Pegasus 入侵。被告国在法院认定不能主张豁免之后就不再参与诉讼，法院最后判原告胜诉。研究者也写到，外国政府实际出庭答辩时，这类诉讼的结果仍难预料。

原告就算胜诉，外国政府的财产原则上也不能扣押来执行判决。依《国家豁免法》，只有财产用于商业或该国书面同意时，原告才能扣押。

怀疑设备遭间谍软件入侵的人，可以写信给 Access Now 的免费数字安全热线，截至 9 月 29 日说明页写明两小时内回复。受理前会先确认是否在服务范围，热线支持的十种语言没有中文，可以用英文联系。OONI（网络干扰观测项目）9 月 1 日至 29 日在中国境内测量 Access Now 网站 76 次，73 次未见干扰迹象。比较各地的法律时，可以问远程入侵算不算当地发生的事、要证明到什么程度才算外国政府所为、放宽豁免的例外会不会违反国际法，以及判决能不能执行。
