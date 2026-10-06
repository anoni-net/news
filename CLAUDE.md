@AGENTS.md

## Claude Code 專屬的設定

共用的內容都在上面引入的 `AGENTS.md`，這裡只放 Claude Code 才讀得到的部分。

### `.claude/agents/`

四個 subagent 對應 `AGENTS.md`「AI 協作工具的寫稿流程」裡的角色。做法與回報格式寫在 `AGENTS.md`，agent 檔只掛上工具與模型，要調整角色先改 `AGENTS.md`。`news-reader` 刻意不讀 `AGENTS.md`，問題清單在 agent 檔另存一份，改「各方的考量」那一條時要一起改。

| agent | 角色 | 模型 | 時機 | 呼叫時要給 |
|---|---|---|---|---|
| `news-research` | 資料蒐集 | Sonnet | 寫稿前 | 題目、原文網址、檔名的 slug |
| `news-reviewer` | 第一輪審稿 | Opus | zh-TW 的第一輪，以及 zh-CN、en 另外查證了新來源時 | 成稿路徑、稿件類型、`/tmp/news-<slug>/` 目錄、維護者已決定的事 |
| `news-rereviewer` | 第二輪、第三輪 | Sonnet | 之後的兩輪，以及 zh-CN、en 的區域段落只引用 `notes/` 時的第一輪 | 成稿路徑、稿件類型、第幾輪、前一輪的意見清單、改了什麼、相關副本摘錄 |
| `news-reader` | 模擬讀者 | Sonnet | 有立場分歧的稿件，審稿修完之後 | 只給成稿路徑 |

派這四個角色時用 agent 名稱，不要用通用的 subagent。通用的 subagent 沒有指定模型時，會沿用主對話的模型。

從工作區或其他目錄開的 session 讀不到這裡的 `.claude/agents/`。這時改用通用的 subagent，明確指定表上的模型，並把對應 agent 檔的內文放進指示，不要另外寫一份更長的指示。
