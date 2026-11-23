---
title: 通过短波无线电收发电子邮件的开源系统 HERMES 与 Mercury
description: 非营利组织 Rhizomatica 的 HERMES 让没有手机信号与互联网的社区通过短波无线电收发电子邮件与文件，5 月发布的调制解调器软件 Mercury 让整套系统全部开源。无线电信号在接收范围内人人都能接收，业余频段可否加密各国规定不同。到 11 月 23 日，台湾的业余无线电不得使用未经主管机关核准的密语或密码通信。中国大陆的业余无线电台通信要使用明语或公认的缩略语、简语与公开的通信协议。
date: 2026-11-28T00:00:00+08:00
slug: hermes-hf-radio
categories:
  - civil-society
sources:
  - title: "Rhizomatica’s HERMES and Mercury Expand Open-Source HF Communications for Remote Communities While Appealing to Experimenters"
    url: https://www.ardc.net/rhizomaticas-hermes-and-mercury-expand-open-source-hf-communications-for-remote-communities-while-appealing-to-experimenters/
    publisher: ARDC
    date: 2026-11-06
  - title: "This Digital Radio Gets Messages to the World’s Remotest Locations"
    url: https://spectrum.ieee.org/hermes-shortwave-radio-digital-data
    publisher: IEEE Spectrum
    date: 2026-09-21
  - title: Mercury — The Open-Source HF Modem
    url: https://mercury.hermes.radio/
    publisher: Rhizomatica
  - title: Rhizomatica/mercury
    url: https://github.com/Rhizomatica/mercury
    publisher: GitHub
  - title: Introduction
    url: https://rhizomatica.github.io/hermes-documentation/manual_en_complete/node22.html
    publisher: HERMES 手册
  - title: "Further and Safer: Reviving HF Radio in the Digital Age"
    url: https://pitg.gitlab.io/news/techdive/2025/07/19/hermes-hf-radio-communication.html
    publisher: Public Interest Technology Group
    date: 2025-07-19
  - title: The First Social Network
    url: https://www.newyorker.com/magazine/2026/10/19/the-first-social-network
    publisher: The New Yorker
    date: 2026-10-12
  - title: 業餘無線電人員及電臺管理辦法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060145
    publisher: 全国法规数据库
  - title: 业余无线电台管理办法（工业和信息化部令第 67 号）
    url: https://www.waizi.org.cn/doc/227732.html
    publisher: waizi.org.cn（转载）
authors:
  - anoni-net
---

在没有手机信号与互联网的地方，短波（HF）无线电可以把信号送到几百公里外。推动偏远社区通信的非营利组织 Rhizomatica 开发了 HERMES，让没有太多无线电与技术经验的人也能通过短波收发消息、电子邮件与文件。Rhizomatica 在 5 月发布开源的调制解调器软件 Mercury（把数据转成无线电能传送的信号）。依资助 HERMES 的业余无线电基金会 ARDC 11 月 6 日刊出的介绍，Mercury 取代了每台电台都要付授权费的专有调制解调器 VARA，整套 HERMES 从此全部开源。

短波信号经大气上层的电离层反射，能连到难以架设地面基础设施的地方。Rhizomatica 的创办人在 IEEE Spectrum 的访谈提到，他们用输出约 20 瓦的小型电台，两台之间大致能稳定连上 400 到 600 公里。短波的限制是速度，同一篇报道里提到，一般短波电台的数字传输速率只有每秒几百比特。

创办人在公共利益技术小组（Public Interest Technology Group）网站的一篇文章写到，HERMES 会先压缩数据，再用 UUCP 这种早期、能容忍连接中断的协议传递邮件。依项目手册，有互联网的地方通常设一座网关站（短波网络与互联网的交接点），没有其他通信方式的社区各设一座远程站。

HERMES 最大的一次部署有近 90 台电台，ARDC 的介绍里提到部分站点要步行或乘船好几天才能抵达。Rhizomatica 跟本地伙伴合作，把培训集中在一小群社区成员身上，目标是让社区自行安装、操作与维护。创办人在访谈里提到，一项试点计划在 10 或 11 艘渔船上装了 HERMES，其中一艘在离岸 100 或 200 公里处故障。他说船员用 HERMES 传出 GPS 位置与求救信号，人和船都获救。

依 ARDC 的介绍，Mercury 也能脱离 HERMES 单独使用，业余无线电操作者可以把它接上自己的电台。已经有操作者用它收发电子邮件，也反馈错误、贡献修改。

## 导读观点 {#perspective}

无线电信号在接收范围内，任何有接收机的人都能接收，而短波的接收范围可达数百公里。《纽约客》10 月报道过乡间通过 AM 广播电台互传私人消息的传统，因为广播的消息人人都能听到，消息常用含糊的措辞写成。

创办人在公共利益技术小组的文章主张，短波很难判断信号从哪里发出，更难知道谁在接收。他在 IEEE Spectrum 的访谈解释，各国对业余无线电加密的规定不同，所以 HERMES 的加密可以开也可以关。内置加密是因为部分合作伙伴身处非常敏感的地区，不想送出容易被截收、被用来对付自己的信息。不过信号本身仍然任何人都能录下，从 Mercury 的源代码公开这点推想，录下的人用同一套软件原则上就能还原没有加密的数据。

台湾的业余无线电由国家通讯传播委员会 2020 年订定的《业余无线电人员及电台管理办法》规范。到 11 月 23 日，办法规定业余无线电人员操作业余电台时，不得使用未经主管机关核准的密语或密码通信。依这条规定，在台湾的业余频段使用 HERMES 时，加密功能没有取得核准就不能开启。

中国大陆的《业余无线电台管理办法》（工业和信息化部令第 67 号）2024 年 3 月 1 日起施行，规定业余无线电台只能用于相互通信、技术研究和自我训练，不得用于谋取商业利益。办法要求通信过程中使用明语或者业余无线电领域公认的缩略语、简语，以及公开的技术体制和通信协议。加密后的内容不属于明语，依转载的办法全文，在大陆的业余频段开启 HERMES 的加密可能不符这项要求。办法限定业余无线电台的用途，社区日常邮件是否落在范围内，办法没有明写。

能上网的读者不需要这套系统，已经有业余无线电执照、想试短波数据通信的人，可以从 Mercury 开始。Mercury 的源代码放在 GitHub，项目页列出支持 Linux（含 Raspberry Pi）与 Windows，到 11 月 23 日最新的版本是 11 月 21 日发布的 v1.9.25。在业余频段试用时，送出的内容要当成任何人都能接收的公开消息。
