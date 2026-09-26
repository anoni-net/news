# anoni.net 新聞導讀

`anoni.net/news` 的文章與網站原始碼。每週整理國際上隱私、匿名網路與網路審查的新聞，寫成正體中文的導讀，一期 3 到 5 則。每一則附原文連結、來源與日期、用自己的話寫的摘要、跟正體中文使用者的關係，以及連到[文件站](https://anoni.net/docs/)的延伸閱讀。

由[匿名網路社群 anoni.net](https://anoni.net/) 維護，是 anoni.net 底下的產品之一。

## 跟文件站的分工

| 內容 | 放在哪裡 |
|---|---|
| 每週導讀（摘要與評註） | 本 repo |
| 外部文章的全文翻譯 | 文件站的 blog |
| 軟體更新日誌 | 文件站的 `changelog/` |
| 社群公告與活動 | 文件站的 blog |

導讀只寫摘要與評註，不整篇翻譯。原文的著作權屬於原作者，每一則都附上原文連結。

## 狀態

籌備中，建置工具還在選型。規劃中的做法：

- 不依賴 JavaScript，Tor Browser 的最安全等級也能正常閱讀
- 站內連結一律從根目錄 `/news/` 起算，不寫網域，clearnet 與 onion 用同一份產物
- CI 建置後把產物推到 `build` 分支，由伺服器拉取

## 寫作規則

照[貢獻者百科](https://anoni.net/docs/community/contributor-handbook/)的寫作風格規範，本 repo 不另外寫一份。給 AI 協作工具的說明在 [`AGENTS.md`](./AGENTS.md)。

## 授權

文章內容以 [CC-BY 4.0](./LICENSE) 授權。之後加入的程式碼另外標示授權。
