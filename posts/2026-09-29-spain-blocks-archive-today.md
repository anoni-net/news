---
title: 西班牙對 archive.today 的行政封鎖
description: 西班牙文化部的智慧財產委員會以行政決定封鎖網頁封存服務 archive.today 與它的鏡像網域，沒有經過法院，OONI 的量測也看得到異常。
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
watch:
  - date: 2026-10-27
    note: 西班牙文化部的封鎖清單是否再擴大、是否有人提出法律挑戰，OONI 的量測是否仍有異常
authors:
  - anoni-net
---

西班牙文化部轄下的智慧財產委員會第二組，下令電信業者封鎖網頁封存服務 archive.today。文化部 9 月 25 日更新的清單列出 7 個網域，除了 archive.today，還有 archive.is、archive.ph、archive.li 等鏡像。封鎖是依一位沒有具名的權利人申訴做出的行政決定，沒有經過法院。西班牙以外的網路不受這次封鎖影響。

西班牙網站 Banda Ancha 最早報導了封鎖。封鎖 8 月中先在部分電信業者生效，到 Banda Ancha 9 月 17 日報導時，已擴大到所有參與智慧財產保護協議的業者。用 HTTPS 連線時會出現連線錯誤，改用 HTTP 則會被導到文化部的頁面，告知這是「非法」網站。

Reclaim The Net 寫到，協議由文化部、權利人與大型電信業者在 2021 年簽署，業者在接到技術委員會通知後 24 小時內封鎖鏡像網站。為了一則侵權內容封鎖整個服務，在西班牙並不是第一次，體育轉播網站也被這樣封鎖過。

OONI 的量測結果也出現變化。9 月 1 日到 27 日，西班牙對 archive.ph 的 641 次量測中有 205 次異常，同期 Internet Archive 的 web.archive.org 在 410 次量測中只有 2 次異常。異常不等於確認封鎖，只代表連線結果跟對照組不同。

## 導讀觀點 {#perspective}

archive.today 存下網頁的快照，讓人在原頁面被刪除或修改之後，仍然可以讀到當時的內容。西班牙封鎖的是整個網域，不是單一快照，存在上面的所有頁面，在多數業者的網路上都讀不到了。程序是行政決定加上業者的協議，不需要法院介入，範圍又擴及鏡像網域。

OONI 6 月到 9 月的量測顯示亞洲也有類似的情況。在中國大陸，archive.ph 的 308 次量測有 273 次異常，GreatFire 也記錄 web.archive.org 從 2016 年起在中國大陸持續被封鎖。在印尼，archive.is 有 155 次量測被 OONI 確認為封鎖。在台灣，archive.ph 的 1183 次量測則只有 41 次異常。

需要大量封存的團隊，可以自架開源的 ArchiveBox，以 MIT 授權，9 月 26 日發布新版。安裝方式是在 Linux 或 macOS 上用 Docker 或 pip 執行指令。存在自己手上的檔案不怕服務被封，但也要自己負責備份，而且無法像公開的封存服務那樣讓別人獨立驗證頁面當時的樣子。

需要保存網頁證據的人，不要只依賴一個封存服務，可以同時存到 Internet Archive 的 Wayback Machine。要把證據留在自己手上，可以用開源的瀏覽器擴充套件 SingleFile 把整頁存成一個 HTML 檔，以 AGPL-3.0 授權，9 月 24 日發布新版。SingleFile 支援 Chrome、Firefox、Edge 與 Safari，介面有正體與簡體中文，裝好之後在要保存的頁面按一下工具列上的按鈕即可。
