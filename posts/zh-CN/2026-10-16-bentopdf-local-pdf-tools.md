---
title: 在浏览器本地处理 PDF 的开源工具 BentoPDF
description: 开源的 PDF 工具集 BentoPDF 依官方说明在浏览器里完成合并、压缩、OCR 与删除元数据，不必把文件上传到在线转换网站。打开官网就能用，界面有简体中文，部分功能使用时要从第三方网站 jsDelivr 下载程序。
date: 2026-10-16T00:00:00+08:00
slug: bentopdf-local-pdf-tools
categories:
  - security
sources:
  - title: Privacy Policy
    url: https://www.bentopdf.com/privacy
    publisher: BentoPDF
    date: 2026-08-29
  - title: Frequently Asked Questions
    url: https://www.bentopdf.com/faq
    publisher: BentoPDF
  - title: OCR PDF Free Online - Make Scanned PDFs Searchable | BentoPDF
    url: https://www.bentopdf.com/ocr-pdf
    publisher: BentoPDF
  - title: Remove Metadata - Strip Hidden Data from PDF - BentoPDF
    url: https://www.bentopdf.com/remove-metadata
    publisher: BentoPDF
  - title: bentopdf/README.md
    url: https://github.com/alam00000/bentopdf/blob/main/README.md
    publisher: GitHub
  - title: Licensing for BentoPDF
    url: https://www.bentopdf.com/licensing
    publisher: BentoPDF
  - title: About BentoPDF - Privacy-First Free PDF Tools | Our Story
    url: https://www.bentopdf.com/about
    publisher: BentoPDF
  - title: Workflow Import Allows Unvalidated TSA URL Leading to PDF Hash Exfiltration via RFC 3161 Requests
    url: https://github.com/alam00000/bentopdf/security/advisories/GHSA-cx8x-7rrr-r9x8
    publisher: GitHub
    date: 2026-08-23
  - title: BentoPDF Handles PDFs Locally, So You Don’t Have to Upload Them to Websites
    url: https://itsfoss.com/bentopdf/
    publisher: It's FOSS
    date: 2026-10-10
  - title: Privacy Policy
    url: https://www.ilovepdf.com/help/privacy
    publisher: iLovePDF
    date: 2026-02-19
  - title: Privacy Notice
    url: https://smallpdf.com/privacy
    publisher: Smallpdf
    date: 2025-07-29
  - title: Is Smallpdf Safe?
    url: https://smallpdf.com/blog/is-smallpdf-safe
    publisher: Smallpdf
    date: 2026-07-14
  - title: 請同仁避免使用線上轉檔、加解密服務，以防資安事件發生
    url: https://doit.gov.taipei/News_Content.aspx?n=9B8993131395DA3F&sms=93D47212F58C7A57&s=46FD091DEE0322E4
    publisher: 臺北市政府資訊局
    date: 2023-10-17
  - title: https://bentopdf.com — GreatFire
    url: https://en.greatfire.org/https/bentopdf.com
    publisher: GreatFire
  - title: Is https://cdn.jsdelivr.net blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/cdn.jsdelivr.net
    publisher: GreatFire
  - title: bentopdf/src/js/config/font-mappings.ts
    url: https://github.com/alam00000/bentopdf/blob/main/src/js/config/font-mappings.ts
    publisher: GitHub
  - title: Is https://rawcdn.githack.com blocked in mainland China? — GreatFire
    url: https://en.greatfire.org/https/rawcdn.githack.com
    publisher: GreatFire
  - title: 涉“文件传输助手”，国安部紧急提醒
    url: https://jcgov.gov.cn/dtxx/zxts/202408/t20240805_2016583.shtml
    publisher: 晋城市人民政府
    date: 2024-08-05
authors:
  - anoni-net
---

It's FOSS 10 月 10 日介绍开源的 PDF 工具集 BentoPDF，官网写有 100 多项工具。依官方说明，合并、拆分、压缩、OCR（光学字符识别，把扫描的图片转成可以搜索的文字）、加密与删除元数据都在浏览器里处理，不必把文件上传到服务器。打开官网就能用，不必注册，界面有简体中文与繁体中文。到 10 月 12 日为止，最新版是 8 月 29 日发布的 2.8.8。

根据官方隐私政策，处理由在用户设备上运行的 JavaScript 与 WebAssembly 库完成，文件不会上传。政策另外提到网站不使用 cookie 与统计分析服务。压缩、PDF 转 Word 等功能用到的 PyMuPDF 这类组件不包含在 BentoPDF 的源代码里，README 的说明是它们在使用时由浏览器从 jsDelivr 下载（jsDelivr 是替网站分发程序文件的第三方服务）。OCR 工具页也提醒第一次使用时要下载 OCR 引擎与所选的语言包，扫描的页面与识别出的文字留在设备上。

源代码以 AGPL-3.0 许可证公开在 GitHub，另有 79 美元一次买断的商业许可，给要用在闭源产品的人。项目由一位开发者发起，官网的介绍页写已有 60 多人贡献代码、翻译与修正。不想用官网的人，可以用 Docker（把整套程序打包成一个可以直接运行的软件包）在自己的电脑或服务器上部署。

## 导读观点 {#perspective}

在线转换网站把文件传到自己的服务器处理再传回，文件在对方手上多久，要看各家的政策。依 iLovePDF 的隐私政策，处理后两小时内删除，电子签名服务除外。Smallpdf 的隐私声明提到，没有登录的用户的文件通常在最后一次打开后的合理期间内删除（重新打开会延长），官方博客则写免费使用的文件一小时后删除。台北市政府资讯局 2023 年也提醒工作人员避免使用在线转换与加解密服务，理由是无法确保这些服务取得资料后如何保存与使用。

依 BentoPDF 的隐私政策，本地处理避开的是传输途中与服务器上的泄露。本文的推论是，要信任的对象因此换成网页上的程序。用官网版本时，运行的是官网当下提供的那一份，更新不需要用户同意。高级功能还会从 jsDelivr 加载代码，官方 FAQ 另外提醒少数需要外部数据的工具可能需要联网。

项目在 GitHub 公开的安全公告中有一则，导入特制的工作流文件会把 PDF 的 SHA-256 哈希值（由文件内容算出的一串摘要，不是文件本身）发送到攻击者的服务器。公告列的影响范围是 2.8.6 与更早的版本，到 10 月 12 日为止没有列出修复版本。

文件在本地处理，PDF 本身仍可能带着作者、创建时间这类隐藏的属性。BentoPDF 的删除元数据工具可以清掉它们，「Sanitize PDF」工具另外删除注释与脚本，分享文件之前可以先处理一次。

需要合并或转换含个人信息的文件、又不想上传到在线服务的人，可以直接用官网，所有工具免费。依官方 FAQ，没有设文件大小的限制，上限取决于自己电脑的性能。

想固定版本的人可以照 README 用 Docker 自行部署，需要先安装 Docker、会操作命令行。不能联网的环境要另外照 README 的离线部署步骤，先在能联网的电脑打包需要的组件再搬进去。隐私政策也提到，文件的安全取决于自己的电脑与浏览器。依本文的推论，电脑本身被入侵时，本地处理保护不到。

到 10 月 12 日，GreatFire 还没有测试过 bentopdf.com 在中国大陆能否连接，官网能否直接打开查不到。压缩这类功能要从 jsDelivr 下载组件，GreatFire 对 cdn.jsdelivr.net 最近两次测试都正常连接。这项测试只代表 cdn.jsdelivr.net 这个主机名，没有测具体的组件路径，同一页也显示 jsdelivr.net 底下另有网址被封锁。依 BentoPDF 的源代码，OCR 文字层的字体来自 rawcdn.githack.com，GreatFire 最后一次测试（2026 年 3 月 2 日）显示遭到封锁。

国家安全部 2024 年 8 月的提示列出网上办公平台的格式转化等功能，要求涉密岗位人员不得把涉密文件上传互联网、使用文字识别时不得输入涉密文件。提示的对象是涉密人员，没有针对一般用户或 PDF 转换网站。
