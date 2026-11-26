# 維護手冊

寫給加入維護的夥伴，整理每天的發稿節奏、編輯台、合併與上線的做法，以及營運上遇過的問題。寫稿與審稿的規則在 `guides/` 的其他檔案，網站的行為以 `SPEC.md` 為準。本檔只放那些地方沒有寫的部分，細節直接連過去。

## 角色與權限

投稿者與沒有權限的 AI 協作工具照 `AGENTS.md`「寫一篇」開 PR 即可。需要上傳或寫入主機的步驟列在 PR 內文，由維護者處理。下面這些工作需要維護者的權限，加入維護時向現任維護者申請：

| 工作 | 需要的權限 | 說明 |
|---|---|---|
| 合併 PR | `anoni-net/news` 的寫入權限 | 2026-11-26 的分支保護要求 `check` 通過、分支跟 `main` 同步，管理員也一樣，還沒有設定必須經過核可。`SPEC.md`「發布權限」寫的非作者核可尚未套用 |
| 選題與排程 | 編輯台（私有的 GitHub Project）的存取權 | 見下方「編輯台」 |
| 上傳網站圖示、預覽卡片與圖片 | 圖片主機的寫入權限 | 見 `AGENTS.md` 的 `news-publish-assets` 與搬圖 |
| 伺服器、nginx 與 Cloudflare | 主機的登入權限 | 屬於正式主機的寫入，著手前先跟其他維護者確認 |
| Bluesky 主帳號 `@anoni.net` 的轉貼 | 主帳號 | `@news.anoni.net` 由 deploy workflow 自動發文，見 `SPEC.md`「Bluesky」 |
| 流量觀察 | Umami 與 Search Console | 見下方「流量觀察」 |

## 每天與每週的節奏

每天固定三個時段，全部是台北時間：

| 時段 | 內容 |
|---|---|
| 00:00、00:05 | 導讀兩篇，依編輯台的順序直接排 |
| 00:10 | 導讀歷史一則 |
| 週六 00:10 | 每週短訊，跟當天的導讀歷史同一個時段，格式見 `SPEC.md`「每週短訊」 |

最多排到 7 天後，`build.py` 超過就建置失敗。題目多於空位時取捨題目，不放寬天數。AI 協作工具先依選題的優先順序提出建議刪掉的題目，由維護者決定，被排掉的稿等日期進到 7 天內再開 PR。規定的理由是寫稿當下查證的狀態放久了會過期。

每週做一次週規劃，從候選池挑下一週的導讀題目，導讀歷史也一次選好七天的事件。選好的題目與事件都寫進編輯台。候選池在維護者的工作區產生後匯入編輯台。每天的執行從編輯台讀當天的項目，一個發布日開一段新的對話，做法見 `guides/ai-workflow.md`「主對話」與「分派多段對話」。

## 編輯台

選題、排程與每一篇的狀態都記在私有的 GitHub Project「anoni.net/news 編輯台」，一個項目是一個題目，來源與筆記寫在項目內文。

| 欄位 | 值 |
|---|---|
| Status | 候選、選中、查核、撰寫、PR、已排程、已發布、不寫 |
| 形式 | 導讀、短訊 |
| 查證難度 | 低、中、高，判斷方式見 `guides/ai-workflow.md`「開工前估成本」 |
| 其他 | 分類、預計發布日、時段、批次 |

開工時把當天的項目改成「查核」。PR 開好後用 GraphQL 的 `addProjectV2ItemById` 把 PR 也加進編輯台，題目與 PR 兩個項目都改成「PR」，合併、上線時再依序改成「已排程」、「已發布」。導讀歷史的事件寫在 `導讀歷史 YYYY-Www 選題` 這個項目的內文，每天一行，收進短訊的候選照 `guides/brief.md` 封存。

用指令操作編輯台時有三件事要注意：

- 欄位一律用 `gh api graphql` 讀寫。`gh project item-list` 輸出的中文欄位名，第一個字會變成亂碼。`gh` 的權杖需要 `project` scope
- 讀全部項目用 `gh api graphql --paginate`，查詢裡的游標變數一定要叫 `$endCursor`。2026-11-03 寫成 `$cursor`，`gh` 一直重抓第一頁，執行了 10 分鐘才發現
- 不要修改單選欄位的選項，例如在「形式」多加一項。修改會重建選項，既有項目在那個欄位的值會被清掉

## 合併

維護者同意之後，CI 一通過就合併那一個 PR。累積好幾個時用 `tools/merge_prs.sh`，見 `guides/ai-workflow.md`「合併」。腳本只在衝突或 CI 失敗時停下來，下面是手動處理時要注意的地方：

- 衝突用把 `origin/main` 合併進分支的方式解，不要 force push。anoni-net/news#281 之後網站圖示與預覽卡片一頁一個登記檔，稿件的 PR 之間很少再衝突
- 手動合併前先取出 check 的結論確認是成功，不要用 `gh pr view && gh pr merge` 這類串法，2026-09-27 紅燈照樣合併過。版面檢查偶爾因為 Chrome 的偵錯連接埠失敗，看過 log 確認是這個原因再用 `gh run rerun --failed`
- 在 worktree 裡執行 `gh pr merge`，可能出現 `'main' is already used by worktree`。那是合併之後的本機步驟失敗，遠端已經合併，用 `gh pr view <n> --json mergedAt` 確認。不要加 `--delete-branch`
- 要更新別人開的 PR 分支時，用 `git checkout --detach origin/<分支>`，改完再 `git push origin HEAD:<分支>`。不要用 `git checkout -B` 建立同名分支，git 2.43 會默默移動其他 worktree 正在用的分支

## 上線的排查

部署的流程與時間寫在 `SPEC.md`「部署」與「排程發布」，合併到上線最慢約 15 分鐘。排程的文章過了時間還沒出現時，依序檢查：

1. `gh run list -R anoni-net/news -w deploy` 最近一次執行的時間與結果
2. 伺服器上的 `/home/ubuntu/news-dispatch.log`，觸發失敗才會寫進去
3. 伺服器上的 `/home/ubuntu/news-pull.log`，`build` 分支無法 fast-forward 時會停在這裡
4. 都沒有異狀時，手動觸發一次 `gh workflow run deploy -R anoni-net/news --ref main`

觸發 deploy workflow 的 token 在 2027-10-03 到期，換法寫在 `SPEC.md`「部署」第 8 項，到期前要記得換。

## 流量觀察

閱讀量看 Umami，事件與參數的定義見 `SPEC.md`「流量統計」。2026-11 中旬查過一次，外部流量以 Google 搜尋為主，Google 新聞與 Discover 帶來的瀏覽幾乎沒有。Google 帶來的瀏覽過半落在發布八天以後，比較像搜尋的長尾。

談到流量來源或要針對 Google 做調整之前，先看 Search Console 的「Google 新聞」與「Discover」報表，不要假設流量來自 Google 新聞。2026-11-17 曾因為這個誤會，把 anoni-net/news#250 的緣由寫錯。

Umami 的 Google referrer 裡混著一群機器人，特徵是作業系統為 Linux、全部跳出、停留時間為零。Umami 不能用螢幕尺寸篩選，要排除時用 `os=Linux` 當條件。

Googlebot 抓取的情形要看源站的 nginx log，clearnet 的 news 記在官網那一份。Cloudflare 直接回應的請求不會到源站，從 log 算出的次數只是下限。

## 專欄的電子報

專欄的電子報內文寫成推薦序，不寫摘要，也不摘錄專欄的原句。推薦序用社群的口吻從讀者熟悉的經驗談起，留下專欄會回答的問題。外框與完整的寫法在批次郵件工具 mail-mass 的 README，新聞導讀外框那一段。

## 相關文件

- `AGENTS.md`：開發指令、寫一篇的步驟與上傳工具
- `SPEC.md`：網站的行為、部署與排程發布
- `guides/ai-workflow.md`：用 AI 協作工具寫稿的流程、合併與分派多段對話
- `guides/posts.md`、`guides/brief.md`、`guides/history.md`、`guides/column.md`：各類稿件的寫法
