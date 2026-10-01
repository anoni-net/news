---
title: Spain’s administrative block on archive.today
description: A commission under Spain's Ministry of Culture has ordered ISPs to block the archive.today web archive and its mirror domains without any court ruling, and OONI measurements show the effect.
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

The Second Section of Spain's Intellectual Property Commission, part of the Ministry of Culture, has ordered telecom operators to block the web archive archive.today. The ministry's list, updated on 25 September, names seven domains: archive.today and its mirrors archive.fo, archive.is, archive.li, archive.md, archive.ph and archive.vn. The block is an administrative decision on a complaint from an unnamed rights holder, not a court ruling. Networks outside Spain are not affected by this block.

Spanish site Banda Ancha, which first reported the block, reports that it took effect at some operators in mid-August and has since spread to every operator in the intellectual property protocol. Over HTTPS the sites fail with a connection error, and over plain HTTP users are redirected to a ministry page calling the site "illegal". According to Reclaim The Net, that protocol, signed in 2021 by the ministry, rights holders and major ISPs, commits operators to block mirror sites within 24 hours of notice from a technical committee. The domains were missing from the ministry's published list of blocked sites when the first reports appeared, after its 11 September update, and were added in the update of 25 September.

## Perspective {#perspective}

archive.today saves snapshots of web pages so that people can still read them after the original is removed or altered. Spain blocked the whole service rather than a single snapshot, which, according to Reclaim The Net, is not new there: the same method has been used against sites carrying sports broadcasts. Everything stored on the service is now unreachable for most users in Spain, through a procedure that needs no court and extends to mirrors.

OONI data shows the effect. Between 1 and 27 September, 205 of 641 measurements of archive.ph from Spain were anomalous, against 2 of 410 for the Internet Archive's web.archive.org. An anomaly is not a confirmed block, only a result that differs from the control.

Across Asia, access to web archives already varies widely. From June to September, 273 of 308 OONI measurements of archive.ph in mainland China were anomalous, and GreatFire records web.archive.org as continuously blocked there since 2016. In Indonesia, OONI confirmed 155 measurements of archive.is as blocked. In Taiwan, only 41 of 1,183 measurements of archive.ph were anomalous.

Anyone who cites archived pages as evidence should avoid relying on a single archive, since whether readers can open an archived copy depends on where they are. Where the Wayback Machine is reachable, saving a copy there as well adds a public snapshot. To keep evidence in your own hands, the open-source browser extension SingleFile, licensed under AGPL-3.0 and updated on 24 September, saves a whole page as one HTML file. It works in Chrome, Firefox, Edge and Safari, its interface includes Traditional and Simplified Chinese, and saving a page takes one click on its toolbar button.

Teams archiving at scale can self-host ArchiveBox, which takes lists of URLs, browser history or bookmarks and saves HTML, JavaScript, PDFs and media. It is MIT-licensed, was updated on 26 September, and installs with Docker or pip on Linux or macOS. Copies you keep yourself cannot be blocked, but you are responsible for backing them up, and others cannot verify them independently the way they can check a public archive.
