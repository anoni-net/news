---
title: BentoPDF, an open-source toolkit for processing PDFs locally in the browser
description: According to its developers, the open-source BentoPDF toolkit merges, compresses, OCRs and strips metadata from PDFs inside the browser, without uploading files to an online converter. It works straight from its website, and some features download code from the third-party jsDelivr service when used.
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
  - title: 涉“文件传输助手”，国安部紧急提醒
    url: https://jcgov.gov.cn/dtxx/zxts/202408/t20240805_2016583.shtml
    publisher: 晋城市人民政府
    date: 2024-08-05
  - title: ChatGPT 等の生成 AI の業務利用に関する申合せ（第２版）
    url: https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/c64badc7-6f43-406a-b6ed-63f91e0bc7cf/e2fe5e16/20230915_meeting_executive_outline_03.pdf
    publisher: デジタル庁
    date: 2023-09-15
authors:
  - anoni-net
---

It's FOSS introduced the open-source PDF toolkit BentoPDF on 10 October; its website lists more than 100 tools. According to its developers, merging, splitting, compressing, OCR (optical character recognition, which turns scanned images into searchable text), encryption and metadata removal all happen in the browser, with no upload to a server. It works straight from the website without sign-up, and the interface is available in Traditional and Simplified Chinese. As of 12 October the latest release is 2.8.8, published on 29 August.

The project's privacy policy says processing is done by JavaScript and WebAssembly libraries running on the user's device and that files are not uploaded, and that the site uses no cookies or analytics. Components such as PyMuPDF, used for compression and PDF-to-Word conversion, are not part of BentoPDF's own source code; the README says the browser downloads them from jsDelivr, a third-party service that distributes code files for websites, when they are used. The OCR page likewise says the OCR engine and selected language packs are downloaded on first use, while the scanned pages and recognized text stay on the device.

The code is published on GitHub under AGPL-3.0, with a separate one-time US$79 commercial license for closed-source products. The project was started by a single developer, and its about page says more than 60 people have since contributed code, translations and fixes. People who would rather not use the website can run it on their own computer or server with Docker, which packages the whole program into a ready-to-run bundle.

## Perspective {#perspective}

Online converters send files to their own servers and back, and how long they keep the files depends on each service's policy. iLovePDF's privacy policy says files are deleted within two hours of processing, except for its e-signature service. Smallpdf's privacy notice says it generally aims to delete files from users who are not logged in "within a reasonable period of time" after they were last opened, with each reopening extending that period, while its blog says files from free use are deleted after one hour. The Taipei City Government's Department of Information Technology also told its staff in 2023 to avoid online conversion and encryption services, because there is no way to be sure how such services store and use the data they receive.

BentoPDF's privacy policy says local processing avoids exposure in transit and on a server. Our inference is that trust shifts to the code on the web page instead. When using the official site, you run whatever version the site serves at that moment, and updates do not require the user's consent. Advanced features also load code from jsDelivr, and the official FAQ separately says a few tools that need external data may need a connection.

One of the security advisories the project has published on GitHub describes how importing a crafted workflow file can send the PDF's SHA-256 hash (a digest calculated from the file's contents, not the file itself) to an attacker's server. The advisory lists 2.8.6 and earlier as affected, and as of 12 October it lists no patched version.

Even when processed locally, a PDF can still carry hidden properties such as its author and creation time. BentoPDF's metadata removal tool clears them, and its "Sanitize PDF" tool also removes annotations and scripts, which is worth doing before sharing a file.

Anyone who needs to merge or convert documents containing personal data without uploading them to an online service can use the website directly, and every tool is free. The official FAQ says there is no file size limit beyond what your own computer can handle.

Those who want to pin a version can self-host with Docker as described in the README, which requires installing Docker and using the command line. Networks with no internet access need the README's separate offline deployment steps, packaging the required components on a connected machine first. The privacy policy also says the safety of files depends on your own computer and browser. Our inference is that local processing offers no protection if the computer itself is compromised.

Official cautions about online services in Asia that we found are addressed to public servants. Besides Taipei's notice to city staff, mainland China's Ministry of State Security warned in August 2024 that staff in classified positions must not upload classified documents to the internet or feed them into text recognition features, listing format conversion among the functions of online office platforms; it does not address ordinary users or PDF converters. Japan's 2023 guidance on generative AI from the executive committee (kanjikai) of the Digital Society Promotion Council says government bodies cannot handle confidential information in cloud services that are used just by accepting standard terms, but it does not name file converters. We, a community based in Taiwan, did not find a notice about online converters from Taiwan's Ministry of Digital Affairs or the Executive Yuan, and could not retrieve an official South Korean text, only press coverage of a generative AI guideline.
