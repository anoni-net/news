#!/usr/bin/env bash
# 依序合併幾個已經同意合併的 PR，見 guides/ai-workflow.md「合併」。
#
#   tools/merge_prs.sh 281 282 283
#
# 每個 PR 落後 main 就更新分支，等 CI 通過再 squash 合併，確認狀態是 MERGED 才換下一個。
# 有衝突、CI 失敗或合併不成功時停下來，印出停在哪一個 PR，後面的不處理。
# 只印每個 PR 的結果，等 CI 的輸出不印，給 AI 協作工具用時才不會塞滿上下文。
set -uo pipefail

REPO="${NEWS_REPO:-anoni-net/news}"

if [[ $# -eq 0 ]]; then
  echo "用法：tools/merge_prs.sh <PR 編號> ..." >&2
  exit 2
fi

state() {
  gh pr view "$1" --repo "$REPO" --json state,mergeStateStatus -q '.state + " " + .mergeStateStatus'
}

for n in "$@"; do
  read -r st merge < <(state "$n")
  if [[ "$st" == "MERGED" ]]; then
    echo "#$n 已經合併過"
    continue
  fi
  if [[ "$st" != "OPEN" ]]; then
    echo "停在 #$n：狀態是 $st"
    exit 1
  fi
  # GitHub 剛收到前一個合併時，狀態可能還是 UNKNOWN，等它算完
  for _ in 1 2 3 4 5 6; do
    [[ "$merge" != "UNKNOWN" ]] && break
    sleep 10
    read -r st merge < <(state "$n")
  done
  case "$merge" in
    DIRTY)
      echo "停在 #$n：跟 main 有衝突，要在分支上合併 origin/main 並手動解決"
      exit 1 ;;
    BEHIND)
      if ! gh pr update-branch "$n" --repo "$REPO" >/dev/null 2>&1; then
        echo "停在 #$n：更新分支失敗"
        exit 1
      fi
      sleep 15 ;;
  esac
  if ! gh pr checks "$n" --repo "$REPO" --watch --fail-fast >/dev/null 2>&1; then
    echo "停在 #$n：CI 沒有通過，gh pr checks $n --repo $REPO 看是哪一項"
    exit 1
  fi
  if ! gh pr merge "$n" --repo "$REPO" --squash >/dev/null 2>&1; then
    echo "停在 #$n：合併失敗，gh pr view $n --repo $REPO 看原因"
    exit 1
  fi
  read -r st merge < <(state "$n")
  if [[ "$st" != "MERGED" ]]; then
    echo "停在 #$n：合併之後狀態是 $st"
    exit 1
  fi
  echo "#$n 已合併"
done
echo "全部完成"
