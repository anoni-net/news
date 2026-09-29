---
title: 英国最高法院的间谍软件国家豁免判决
description: 英国最高法院 7 月 27 日以三比二判决，外国从境外远程植入间谍软件、在英国造成人身伤害时，不能在英国法院主张国家豁免。这次判决只决定英国法院能否受理，巴林否认指控，英国以外的法院依各自的法律判断。
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

英国最高法院 7 月 27 日以三比二驳回巴林的上诉，两位住在英国的原告起诉巴林政府的诉讼不受国家豁免（外国政府原则上不能在别国法院被起诉）阻挡。原告主张巴林从 2011 年 9 月前后用 FinSpy（商业间谍软件）入侵他们的电脑，得知后受到精神伤害。这次判决只决定英国法院能否受理，巴林否认指控，入侵是否属实留待审理。英国以外的法院按各自法律判断。

原告 2020 年起诉，高等法院 2023 年、上诉法院 2024 年都驳回豁免主张。《1978 年国家豁免法》第 5 条把「在英国境内的作为或不作为」（做了或该做而没做的事）造成的死亡、人身伤害或有形财产损害列为例外。只涉及数据泄露或经济损失的索赔不在这个例外内。

英国加入的《欧洲国家豁免公约》第 11 条另外要求加害者当时身在法院所在国，双方都承认本案不符合。判决假定原告的主张属实，操作者可能在英国境外、通过巴林的控制服务器（C2）操作，原告与电脑在英国。

多数大法官认定，第 5 条不要求加害者身在英国，是议会有意与公约不同。他们也认定「作为」包括用设备或远程方式完成的行为，从境外操控英国境内的电脑就算在英国的作为。

## 导读观点 {#perspective}

巴林主张造成伤害的是境外输入的指令，电脑上的文件损坏、数据复制只是后续事件。一位持不同意见的大法官以在界河一岸朝对岸开枪为例，认为行为地在输入指令的巴林，摄像头在英国打开只是结果。原告列出在英国的十类行为，包括打开麦克风与摄像头、键盘记录，多数大法官认定合起来构成在英国的监控。

按巴林的解释，派人入境杀人的国家不享有豁免，从境外遥控无人机杀人的国家却能豁免。多数大法官认为这种区分很武断，公约也允许英国扩大例外，把例外延伸到主权行为（国家行使公权力的行为）有合理依据。持不同意见的大法官回应，1978 年立法时无从预见无人机与网络入侵，以加害者所在地为准的规则也较明确。巴林主张多数意见的解释让英国违反公约，少数大法官也认为习惯国际法只容许加害者身在当地的例外，找不到各国立法或判决支持更大的例外。

中国 2024 年起施行的《外国国家豁免法》第 9 条与英国一样没有写明在场要求，外国国家在中国领域内的行为造成人身伤害、死亡或财产损失的，该国在赔偿诉讼中不享有豁免。日本 2009 年的相关法律第 10 条则要求行为人当时身在日本。

Citizen Lab 与 Access Now 的法律研究者在 Lawfare 的文章写到，回到高等法院后，原告要证明入侵出自巴林并造成伤害。文中另一起英国案件，原告靠专家取证证实手机遭 Pegasus 入侵，但被告国在豁免被驳回后不再参与诉讼。被告实际答辩时原告能否胜诉仍不明。根据《国家豁免法》第 13 条，原告即使胜诉也只有在财产用于商业或该国书面同意时，才能查封外国财产执行判决。

怀疑设备遭间谍软件入侵的人，可以写信给 Access Now 的免费数字安全热线，受理前会先确认是否在服务范围内（如记者与活动人士）。截至 9 月 29 日，说明页写明两小时内回复，十种语言没有中文。OONI（网络干扰观测项目）9 月 1 日至 29 日在中国境内测量 Access Now 网站 76 次，73 次未见干扰迹象。比较各地时，可以问远程入侵算不算当地的行为、要证明到什么程度才算外国政府所为、扩大例外会不会违反国际法，以及判决能不能执行。
