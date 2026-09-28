---
title: 西班牙对 archive.today 的行政封锁
description: 西班牙文化部的知识产权委员会以行政决定封锁网页存档服务 archive.today 与它的镜像域名，没有经过法院，OONI 的测量也看得到异常。
date: 2026-09-29T07:05:00+08:00
slug: spain-blocks-archive-today
sources:
  - title: Nombres de dominios Web objeto de resolución final firme de la S2CPI (2012 – 2026)
    url: https://www.cultura.gob.es/cultura/propiedadintelectual/lucha-contra-la-pirateria/s2cpi/listadowebs.html
    publisher: Ministerio de Cultura
    date: 2026-09-25
  - title: Spain orders blocks on Archive.today and its mirrors
    url: https://reclaimthenet.org/spain-blocks-archive-today-and-mirrors
    publisher: Reclaim The Net
    date: 2026-09-18
  - title: Archive.today pasa a ser una una web "ilegal" en España por orden del Ministerio de Cultura
    url: https://bandaancha.eu/articulos/archive-today-pasa-ser-web-ilegal-espana-11923
    publisher: Banda Ancha
    date: 2026-09-17
  - title: OONI Explorer
    url: https://explorer.ooni.org/
    publisher: OONI
  - title: Is http://web.archive.org blocked in mainland China?
    url: https://en.greatfire.org/web.archive.org
    publisher: GreatFire
  - title: SingleFile
    url: https://github.com/gildas-lormeau/SingleFile
    publisher: GitHub
  - title: ArchiveBox
    url: https://github.com/ArchiveBox/ArchiveBox
    publisher: GitHub
regions:
  - ES
authors:
  - anoni-net
---

西班牙文化部下属的知识产权委员会第二组，下令电信运营商封锁网页存档服务 archive.today。文化部 9 月 25 日更新的清单列出 7 个域名，除了 archive.today，还有 archive.is、archive.ph、archive.li 等镜像。封锁是依一位没有具名的权利人投诉做出的行政决定，没有经过法院。西班牙以外的网络不受这次封锁影响。

西班牙网站 Banda Ancha 最早报道了封锁。封锁 8 月中先在部分运营商生效，到 Banda Ancha 9 月 17 日报道时，已扩大到所有参与知识产权保护协议的运营商。用 HTTPS 连接时会出现连接错误，改用 HTTP 则会被导到文化部的页面，告知这是「非法」网站。

Reclaim The Net 写到，协议由文化部、权利人与大型电信运营商在 2021 年签署，运营商在接到技术委员会通知后 24 小时内封锁镜像网站。为了一则侵权内容封锁整个服务，在西班牙并不是第一次，体育转播网站也被这样封锁过。

OONI 的测量结果也出现变化。9 月 1 日到 27 日，西班牙对 archive.ph 的 641 次测量中有 205 次异常，同期 Internet Archive 的 web.archive.org 在 410 次测量中只有 2 次异常。异常不等于确认封锁，只代表连接结果跟对照组不同。

## 导读观点 {#perspective}

archive.today 存下网页的快照，让人在原页面被删除或修改之后，仍然可以读到当时的内容。西班牙封锁的是整个域名，不是单一快照，存在上面的所有页面，在多数运营商的网络上都读不到了。程序是行政决定加上运营商的协议，不需要法院介入，范围又扩及镜像域名。

OONI 6 月到 9 月的测量显示，中国大陆早就连不上这类存档服务，archive.ph 的 308 次测量有 273 次异常。GreatFire 也记录 web.archive.org 从 2016 年起在中国大陆持续被封锁。在印度尼西亚，archive.is 有 155 次测量被 OONI 确认为封锁。

需要大量存档的团队，可以自建开源的 ArchiveBox，以 MIT 授权，9 月 26 日发布新版。安装方式是在 Linux 或 macOS 上用 Docker 或 pip 执行命令。存在自己手上的文件不怕服务被封，但也要自己负责备份，而且无法像公开的存档服务那样让别人独立验证页面当时的样子。

在境内需要保存网页证据的人，与其依赖公开的存档服务，不如把证据存在自己手上。开源的浏览器扩展 SingleFile 可以把整页存成一个 HTML 文件，以 AGPL-3.0 授权，9 月 24 日发布新版。它支持 Chrome、Firefox、Edge 与 Safari，界面有简体中文，装好之后在要保存的页面点一下工具栏上的按钮即可。身在境外的人也可以同时存到 Wayback Machine，多留一份公开的快照。
