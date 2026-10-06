@AGENTS.md

## Claude Code 專屬的設定

共用的內容都在上面引入的 `AGENTS.md`，這裡只放 Claude Code 才讀得到的部分。

### `.claude/agents/`

四個 subagent 對應 `guides/ai-workflow.md` 裡的角色。做法與回報格式寫在 `guides/ai-workflow.md`，agent 檔只掛上工具與模型，要調整角色先改那份。`news-reader` 刻意不讀 `AGENTS.md` 與 `guides/`，問題清單在 agent 檔另存一份，改 `guides/posts.md`「各方的考量」那一條時要一起改。

| agent | 角色 | 模型 | 時機 | 呼叫時要給 |
|---|---|---|---|---|
| `news-research` | 資料蒐集 | Sonnet | 寫稿前 | 題目、原文網址、檔名的 slug |
| `news-reviewer` | 第一輪審稿 | Opus | zh-TW 的第一輪，以及 zh-CN、en 另外查證了新來源時 | 成稿路徑、稿件類型、`/tmp/news-<slug>/` 目錄、維護者已決定的事 |
| `news-rereviewer` | 第二輪、第三輪 | Sonnet | 之後的兩輪，以及 zh-CN、en 的區域段落只引用 `notes/` 時的第一輪 | 成稿路徑、稿件類型、第幾輪、前一輪的意見清單、改了什麼、相關副本摘錄 |
| `news-reader` | 模擬讀者 | Sonnet | 有立場分歧的稿件，審稿修完之後 | 只給成稿路徑 |

派這四個角色時用 agent 名稱，不要用通用的 subagent。通用的 subagent 沒有指定模型時，會沿用主對話的模型。

從工作區或其他目錄開的 session 讀不到這裡的 `.claude/agents/`。這時改用通用的 subagent，明確指定表上的模型，並把對應 agent 檔的內文放進指示，不要另外寫一份更長的指示。

### 主對話的工作目錄

session 從 anoni-net/news 的上層目錄或其他 repo 開啟、再進來工作時，盡量不要把主對話的工作目錄切進本 repo 或它的 worktree。Claude Code 在工作目錄改變時會自動載入本檔與它引入的 `AGENTS.md`，之後一直留在對話裡。`guides/` 底下的寫作指南不會自動載入，2026-10 拆檔之前 `AGENTS.md` 約 1.5 萬 token。已載入的內容會走 prompt cache，每回合重讀的成本不高，主要的影響是對話變長、比較早被壓縮。

執行建置、lint 或 `prose_check.py` 時可以用子 shell，例如 `(cd <repo 路徑> && uv run build.py --check)`。讀取子目錄裡的檔案也可能觸發載入，這個做法只能減少，不能保證不載入。

沒有自動載入不代表可以略過規則。寫稿或改規則之前，主對話仍要照 `AGENTS.md` 的索引讀 `guides/` 裡對應的檔案，例如寫導讀先讀 `guides/posts.md` 與 `guides/ai-workflow.md`。直接在本 repo 開 session 的不受影響，本檔與 `AGENTS.md` 開場就會載入。
