# 圖示

頁面用到的圖示，建置時由 `build.py` 的 `icon()` 內嵌進 HTML，不透過字型或 CDN 載入，onion 版本一樣可用。只放用到的圖示，要新增時從下面的來源取原始 SVG，檔名照來源的圖示名稱。

| 檔案 | 來源 | 授權 |
|---|---|---|
| `rss.svg`、`email-outline.svg`、`home-outline.svg`、`file-document-multiple-outline.svg`、`arrow-left.svg`、`arrow-right.svg`、`translate.svg`、`web.svg`、`information-outline.svg`、`message-alert-outline.svg`、`history.svg`、`book-open-outline.svg`、`volume-high.svg`、`pause.svg`、`tune-variant.svg` | [Material Design Icons](https://pictogrammers.com/library/mdi/)（`Templarian/MaterialDesign-SVG` 的 `svg/`，commit `9e04201`） | Apache 2.0 |
| `torproject.svg`、`bluesky.svg` | [Simple Icons](https://simpleicons.org/)（`simple-icons/simple-icons` 的 `icons/`，commit `d0b3c2d`） | CC0 1.0 |

跟文件站用同一套：文件站的 `:material-*:` 是 Material Design Icons，Tor 這類品牌圖示用 Simple Icons。Tor 的洋蔥圖示與 Bluesky 的蝴蝶圖示分別是 Tor Project 與 Bluesky 的商標，這裡只用來標示 onion 版本與 Bluesky 帳號的連結。
