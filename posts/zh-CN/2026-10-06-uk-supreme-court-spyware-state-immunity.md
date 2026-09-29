---
title: 英国最高法院的间谍软件国家豁免判决
description: 英国最高法院 7 月 27 日以三比二判决，外国从境外远程植入间谍软件、在英国造成人身伤害时，不能在英国法院主张国家豁免。判决只决定英国法院能否受理，巴林否认指控，案件回到高等法院审理，英国以外的法院依各自的法律判断。
date: 2026-10-06T07:05:00+08:00
slug: uk-supreme-court-spyware-state-immunity
sources:
  - title: The Kingdom of Bahrain (Appellant) v Shehabi and another (Respondents)
    url: https://supremecourt.uk/cases/uksc-2024-0152
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: "The Kingdom of Bahrain v Shehabi and another [2026] UKSC 25, Judgment"
    url: https://supremecourt.uk/uploads/uksc_2024_0152_judgment_a1ae6cd3a5.pdf
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: "The Kingdom of Bahrain v Shehabi and another [2026] UKSC 25, Press Summary"
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
  - title: Dissidents win in Supreme Court as it rejects Kingdom of Bahrain's appeal over sovereign immunity from spyware claims
    url: https://www.leighday.co.uk/news/press-releases/2026-news/dissidents-win-in-supreme-court-as-it-rejects-kingdom-of-bahrain-s-appeal-over-sovereign-immunity-from-spyware-claims/
    publisher: Leigh Day
    date: 2026-07-27
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

英国最高法院 7 月 27 日以三比二驳回巴林的上诉，两位住在英国的原告可以继续起诉巴林政府。原告主张巴林从 2011 年 9 月前后用间谍软件 FinSpy 入侵他们的电脑，得知后受到精神伤害。判决只处理英国法院能否受理，巴林否认指控，是否真有入侵留待之后审理。英国以外的法院依各自的法律判断。

依判决书，《1978 年国家豁免法》原则上让外国享有豁免，第 5 条的例外是死亡、人身伤害或有形财产损害由「在英国的作为或不作为」造成。英国加入的《欧洲国家豁免公约》第 11 条另外要求加害者当时身在当地，双方同意本案不符合这个条件。依判决书的假定事实，操作者可能在英国境外、通过位于巴林的指令服务器操作，原告与电脑在英国。

多数大法官认定第 5 条没有在场的要求，是议会有意偏离公约，「作为」也包括通过设备或远程方式完成的行为。从境外远程操控英国境内的电脑，因此就是在英国的作为。

原告 2020 年起诉，高等法院 2023 年、上诉法院 2024 年都驳回了巴林的豁免主张。代理原告的 Leigh Day 律师事务所在新闻稿写到，这份判决是该所其他间谍软件索赔案的基础。截至 9 月 29 日，没有查到巴林政府对判决的公开声明。

## 导读观点 {#perspective}

依判决书，巴林主张造成伤害的是境外输入的指令，原告电脑上的文件损坏、数据复制只是后续事件。其中一位持不同意见的大法官以隔着界河开枪为例，认为行为发生在输入指令的巴林，打开摄像头是行为在英国的效果。原告列出发生在英国的十类行为，包括传送安装文件、覆写主引导记录（Master Boot Record）、打开麦克风与摄像头、记录键盘输入，多数大法官认定合起来就是在英国的监控。

依 Citizen Lab 与 Access Now 的法律研究者在 Lawfare 的文章，不同意见的读法会让派人入境杀人的国家没有豁免，从境外操作无人机的国家却有。多数大法官认为公约允许英国扩大例外，各国的实践也支持这类例外适用于主权行为。巴林主张这样解读让英国违反公约，持不同意见的大法官认为国际习惯法只在加害者身在当地时容许这类例外。

依 2024 年 1 月 1 日施行的中国《外国国家豁免法》第九条，外国国家在中国领域内的相关行为造成人身伤害、死亡或财产损失的赔偿诉讼，不享有管辖豁免。条文与英国第 5 条一样没有写明加害者要身在境内，日本 2009 年的《对外国民事裁判权法》第 10 条则明文要求行为人当时身在日本。

依最高法院的案件页，这次只以原告主张的事实为前提处理豁免。Lawfare 的文章写到，案件回到高等法院后，原告要证明入侵出自巴林、因果关系与伤害。英国《国家豁免法》第 13 条也限制胜诉后的执行，外国的财产除非用于商业或经该国书面同意，不能强制执行。

第 5 条只涵盖死亡、人身伤害与有形财产损害，索赔若只涉及数据泄露或经济损失，不在范围内。Lawfare 的文章写到，另一起英国案件的原告靠专家取证证明手机遭 Pegasus 入侵。

怀疑设备遭间谍软件入侵的人，可以写信给 Access Now 的数字安全热线，免费、不需要账号。说明页写明两小时内回复，受理前会先确认是否属于民间社会对象。热线的十种语言包括英文与阿拉伯文但没有中文，OONI 9 月在中国境内测量其首页 76 次，73 次无异常。比较各地的做法时，可以问远程入侵算不算在当地的行为、受害者要证明到什么程度才能归责外国政府，也可以问扩大例外会不会违反国际法、判决能不能执行。
