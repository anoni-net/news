---
title: 英国最高法院的间谍软件国家豁免判决
description: 英国最高法院 7 月 27 日以三比二判决，外国政府从国外远程入侵英国境内的电脑、造成人身伤害时，不能用豁免权挡下英国法院的审理。判决只决定英国法院能否受理，入侵是否属实还没审，巴林否认指控。英国以外的法院按各自的法律判断。
date: 2026-10-06T07:05:00+08:00
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

英国最高法院 7 月 27 日以三比二驳回巴林政府的上诉，两位住在英国的原告可以继续告巴林。一般情况下外国政府不能在别国法院被告，这叫国家豁免，巴林主张自己适用。原告主张巴林从 2011 年 9 月前后用 FinSpy（商业间谍软件）入侵他们的电脑，得知后受到精神伤害，巴林否认指控。判决只决定英国法院能不能受理，入侵是否属实还没审，英国以外的法院按各自的法律判断。

英国法律开了一个例外：外国政府在英国做的事造成死亡、人身伤害或有形财物损坏时，不能拿豁免当挡箭牌（《1978 年国家豁免法》第 5 条）。只涉及数据泄露或经济损失的索赔不在这个例外内。

案子的核心问题是黑客从国外远程操作、入侵在英国的电脑，算不算在英国做的事。按原告的主张，操作者很可能人在国外，通过巴林的控制服务器（C2）下指令。英国签的一项欧洲公约另外要求加害者当时人在法院所在国，双方都承认这个案子不符合。

三位多数大法官认为，英国的例外条文没有要求加害者人在英国，是议会有意与公约不同。他们也认为，通过设备或远程方式完成的动作同样算数，所以从国外操控英国境内的电脑就算在英国做的事。

## 导读观点 {#perspective}

巴林主张，造成伤害的是在国外输入的指令，电脑上的文件损坏只是后续的事。一位持不同意见的大法官以隔着界河开枪为例，认为事情发生在开枪的那一岸（输入指令的巴林），摄像头在英国打开只是结果。原告列出十类发生在英国的动作，例如打开麦克风和摄像头，多数大法官认定合起来就是在英国进行的监控。

多数大法官举的例子是，派人入境杀人的国家不能主张豁免，从国外遥控无人机杀人的国家却可以。他们认为按巴林的解释会出现这种不合理的差别，公约也允许英国放宽例外，用在外国政府行使公权力的行为上有合理依据。持不同意见的大法官回应，1978 年立法时没人想得到无人机和网络入侵，以加害者所在地为准的规则也比较明确。巴林主张多数的读法会让英国违反公约，少数大法官也认为国际惯例只容许加害者在场时才有例外。

中国 2024 年起施行的《外国国家豁免法》也有类似的例外，外国国家在中国境内的行为造成人身伤害、死亡或财产损失时不享有豁免，条文没有写明行为人要不要人在中国。日本的相关法律则要求行为人当时人在日本。

案子回到高等法院后，原告要证明入侵出自巴林并造成伤害。原告即使胜诉，也只有在外国财产用于商业或该国书面同意时，才能查封来执行判决。支持原告的研究者在 Lawfare 的文章提到英国另一起案件，原告靠专家取证证实手机遭 Pegasus 入侵，被告国在豁免被驳回后就不再参与诉讼。被告实际答辩时的胜负，截至 9 月 29 日仍不明朗。

怀疑设备遭间谍软件入侵的人，可以写信给 Access Now 的免费数字安全热线。截至 9 月 29 日，说明页写明两小时内回复，受理前会先确认是否在服务范围内（如记者与活动人士）。说明页的十种语言没有中文，OONI（网络干扰观测项目）9 月 1 日至 29 日在中国境内测量 Access Now 网站 76 次，73 次未见干扰迹象。比较各地的法律时，可以问远程入侵算不算当地发生的事、要证明到什么程度才算外国政府所为、放宽豁免的例外会不会违反国际法，以及判决能不能执行。
