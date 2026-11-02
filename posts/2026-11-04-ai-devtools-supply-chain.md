---
title: AI 程式開發工具的擴充套件後門與惡意指引檔
description: 太平洋時間 10 月 29 日從 Cursor 自家市集安裝或更新 Claude Code 擴充套件 2.1.312、2.1.313 的 Windows 與 macOS 使用者，可能裝到含後門的版本。依 Anthropic 方面的說法，官方管道的版本不受影響。另一份 10 月 22 日的研究記錄了放進下載資料夾、誘使 Codex 安裝惡意套件的 Markdown 指引檔。
date: 2026-11-04T00:00:00+08:00
slug: ai-devtools-supply-chain
categories:
  - security
sources:
  - title: Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace
    url: https://cursor.com/blog/claude-code-extension-security-notice
    publisher: Cursor
    date: 2026-10-29
  - title: "Markdown Is the New Executable: Attackers Are Dropping Agent Instructions Into Your Downloads Folder From the Web"
    url: https://forever.security/blog/hijacking-ai-agents-via-downloads-folder/
    publisher: Forever Security
    date: 2026-10-22
  - title: Anthropic VS code extension on Cursor backdoored for nearly 12 hours
    url: https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/
    publisher: Ars Technica
    date: 2026-10-30
  - title: "Anthropic: That Claude Code extension compromise… couldn't be us"
    url: https://www.theregister.com/cyber-crime/2026/10/30/anthropic-that-claude-code-extension-compromise-couldnt-be-us/5306682
    publisher: The Register
    date: 2026-10-30
  - title: "Official Claude Code Extension Compromise: Security Advisory"
    url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
    publisher: Phorion
    date: 2026-10-30
  - title: Anthropic hacked to deliver remote access trojan to claude developer laptops worldwide
    url: https://doublepulsar.com/anthropic-hacked-to-deliver-remote-access-trojan-to-claude-developer-laptops-worldwide-1148a92baae2
    publisher: DoublePulsar
    date: 2026-10-30
  - title: AI coding agents fall for malicious instructions planted in the Downloads folder
    url: https://www.helpnetsecurity.com/2026/10/26/ai-coding-agents-malware-openai-codex/
    publisher: Help Net Security
    date: 2026-10-26
  - title: 惡意Markdown指引檔企圖誘使Codex安裝惡意套件，AI程式開發代理面臨攻擊風險
    url: https://www.ithome.com.tw/news/180033
    publisher: iThome
    date: 2026-10-30
watch:
  - date: 2026-12-02
    note: Cursor 或 Anthropic 是否公布惡意版本如何以 Anthropic 的已驗證帳號上架到 Cursor 市集，Anthropic 是否發布正式的事故說明
authors:
  - anoni-net
---

10 月 29 日，AI 程式編輯器 Cursor 自家的擴充套件市集上出現被竄改過的 Claude Code 擴充套件（extension，裝進編輯器、增加功能的外掛程式），停留約 11 小時。依 Cursor 的公告，受影響的是 Windows 與 macOS 版的 `Anthropic.claude-code` 2.1.312 與 2.1.313，只有在那段時間從 Cursor 市集安裝或更新的人需要處理。依 The Register 轉引 Anthropic 一位技術人員在 X 的貼文，Anthropic 官方管道的版本沒有問題，只有 Cursor 的使用者受影響。另一件是資安公司 Forever Security 10 月 22 日公開的案例，一份出現在下載資料夾的 Markdown 指引檔試圖讓 OpenAI 的程式開發代理 Codex 安裝惡意套件。

依 Cursor 的公告，惡意版本在市集上的時間是太平洋時間 10 月 29 日 02:27 到 13:35（台北時間 10 月 29 日 17:27 到 10 月 30 日 04:35）。Ars Technica 的報導引述 Cursor，受影響的使用者最多 5,000 人。資安公司 Phorion 的技術長向 Ars 表示，惡意版本是用 Anthropic 在 Cursor 市集的官方帳號發布的。他也提到 Cursor 預設會自動更新擴充套件，使用者可以在設定裡調整。

Cursor 10 月 30 日更新公告時列出 2.1.312 與 2.1.313 兩版，Ars、The Register 與 Phorion 一開始都只寫 2.1.313。Phorion 10 月 30 日把原本寫的 Open VSX（VS Code 衍生編輯器共用的開放擴充套件市集）更正為 Cursor 的市集，10 月 31 日又依 Cursor 的更新補上 2.1.312。Phorion 與 Ars 都寫到惡意程式碼也有針對 Linux 的部分，Cursor 列出的受影響平台只有 Windows 與 macOS。依 Ars 引述一位獨立資安研究者的說法，Anthropic 在惡意版本上架數小時後發布了 2.1.314。

依 Cursor 的公告與 Phorion 的分析，惡意程式碼在擴充套件載入時就會執行，使用者不必開啟它。程式會把電腦名稱、使用者名稱、作業系統、公開 IP、Git 設定的 email 與環境變數的名稱（不含值）回傳給攻擊者。它也試著加入攻擊者的 SSH（遠端登入電腦用的協定）金鑰、建立反向連線的通道，並設定成在背景持續重試。Cursor 的公告提到開啟 SSH 服務需要管理員權限，多數 macOS 與 Windows 電腦上這一步會失敗，攻擊者也就無法經由通道登入。

即使通道沒有建立，攻擊者的金鑰與持續執行的設定仍會留在電腦上，電腦的資料也已經送出。Cursor 與代管業者合作，讓攻擊者的伺服器下線。Cursor 的公告列出的處置還包括移除惡意版本、暫時關閉整個市集，以及稽核存取紀錄、確認沒有其他擴充套件被竄改。Cursor 也更換了金鑰，重建市集後重新上線。

到 11 月 2 日，Cursor 與 Anthropic 都沒有公開惡意版本如何以 Anthropic 的已驗證帳號上架到 Cursor 市集。前面引述的那位獨立資安研究者 10 月 30 日的文章標題寫「Anthropic hacked」，之後在文中補上 Anthropic 方面把問題歸到 Cursor 市集的回應。依 The Register 轉引，Anthropic 那位技術人員寫 Anthropic 的系統與員工電腦都沒有被入侵。他寫到有人利用 Cursor 市集的存取權限，上傳了 Anthropic 沒有製作、也沒有發布的竄改版本。

Markdown 指引檔那件，依 Forever 的文章，客戶電腦的下載資料夾裡出現一份約 13 KB、偽裝成一般工程規範的 `AGENTS.md`。`AGENTS.md` 是開發者放在專案資料夾裡、給程式開發代理讀的指引檔，代理會自動讀取並照著做。檔案要求 Codex 修改自己的全機設定、註冊攻擊者指定的 MCP 伺服器（Model Context Protocol，讓代理串接外部工具的介面），再安裝 npm 套件 `function-color`。Forever 用自家產品在套件安裝前攔下，依 Help Net Security 的報導，npm 已經移除該套件。

依 Help Net Security 的報導，研究者發現時不知道檔案是怎麼進到下載資料夾的。研究者寫到，網站不需要使用者點擊或授權，就能把檔案放進下載資料夾。Codex 只照做它信任的資料夾裡的 `AGENTS.md`，使用者在下載資料夾工作過之後，那裡就算是信任的資料夾。研究者在隔離環境重現整條攻擊，Codex 在超過九成的嘗試裡執行了檔案要它執行的程式（多數測試用只會開啟計算機的無害替身）。

研究者也仿照同樣的寫法自行寫了一份 `CLAUDE.md`，測試 Anthropic 的 Claude Code，這份檔案沒有在客戶電腦上出現過。約一半的測試裡，Claude Code 照檔案改了設定，把 API 連線導向研究者的伺服器。研究者寫到登入權杖會因此外流，用截取的權杖可以接管帳號。Forever 的文章主張 OpenAI 與 Anthropic 都沒有東西可以修補，到 11 月 2 日，本文沒有查到兩家公司對這份研究的公開回應。

## 導讀觀點 {#perspective}

兩起事件的來源沒有把它們連在一起，本文放在同一篇，是因為兩者都利用了開發工具自動載入、自動信任的檔案。Ars 的報導提到，Cursor 的擴充套件以編輯器本身的權限執行，裝上之後很可能可以存取本機檔案、原始碼與開發工具。本文推論，市集的已驗證帳號加上預設的自動更新，讓發布帳號成為使用者與惡意版本之間唯一的關卡。依 The Register 與 DoublePulsar 的文章，更新到 2.1.314 也不會清掉已經裝好的持續執行設定。

指引檔的攻擊屬於間接提示注入（indirect prompt injection，把指令藏在 AI 會讀進來的內容裡），代理照設計會把指引檔當成使用者的指示照做。Forever 把問題歸在兩件各自合理的事交會的地方，一是代理信任它所在的資料夾，二是網頁長久以來就能把檔案放進下載資料夾。依 Help Net Security 的報導，很多瀏覽工作已經交給代理自行完成。代理自己開啟的網頁也可能放下檔案，螢幕前沒有人看得到。

自動更新與指引檔都有取捨。本文推論，關掉擴充套件的自動更新可以避開類似的時間窗，代價是安全修補也會晚到。Forever 建議保持代理的操作核准與沙箱（限制程式能存取的範圍）開啟，依 iThome 的整理，Codex 那份指引檔就試圖讓代理略過這兩道限制。

在台北時間 10 月 29 日傍晚到 30 日清晨從 Cursor 市集安裝或更新過 Claude Code 擴充套件的 Windows 與 macOS 使用者，第一步是照 Cursor 公告裡的方法檢查 SSH 的授權金鑰清單，有攻擊者的金鑰就代表電腦受影響。公告附有 macOS 與 Windows 的檢查與清除腳本。同一份公告提醒只移除擴充套件可能不夠，要從另一台可信任的電腦更換受影響電腦能存取的密碼、權杖與登入工作階段，並評估是否重灌。

用 Codex、Claude Code 這類代理的人，Forever 建議的第一步是不要在下載資料夾啟動代理（本文推論不寫程式、只讓代理整理文件或瀏覽網頁的人也適用），不需要另外購買工具。打開剛複製的程式庫或別人給的資料夾之前，先讀過裡面不是自己寫的 `AGENTS.md` 與 `CLAUDE.md`，也檢查代理的設定檔有沒有自己沒加過的伺服器或網址。發現被植入檔案時，依 Forever 的建議，要當作登入權杖已經外流並立即更換。本文推論這些做法只能降低被誘導的機會，代理照指引檔行事的設計不會因此改變。
