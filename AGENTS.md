# AGENTS.md

本文件寫給在 anoni-net/news 工作的 AI 協作工具與使用它們的貢獻者，不限定哪一家的服務。Claude Code 從 `CLAUDE.md` 引入本文件。

## 專案概述

`anoni.net/news` 是匿名網路社群 anoni.net 的新聞導讀，整理國際上隱私、匿名網路與網路審查的新聞，一則寫成一篇。跟文件站（`anoni-net/docs`，網址 `anoni.net/docs`）的分工寫在 [`README.md`](./README.md)。

目前在籌備階段。建置程式的規格在 [`SPEC.md`](./SPEC.md)，實作之後這份文件會補上目錄結構與開發指令。

## 寫作規則

寫作與協作的規則以[貢獻者百科](https://anoni.net/docs/community/contributor-handbook/)為準，要調整規則時改百科，不要在這裡另存一份。檢查工具沿用文件站的 `tools/docs_style_lint.py`。

導讀另有三條界線：

- 只寫摘要與評註，不整篇翻譯。引用原文時照錄原始標題，引述盡量短
- 不把內容跟特定基金會或具名的個人綁在一起，原文提到的人名與組織只在理解新聞必要時保留
- 不描述特定地區、特定族群使用哪些工具。地區、族群與產品名稱同時出現，就足以構成偵查線索
