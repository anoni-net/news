#!/bin/sh
# m6 上觸發 deploy workflow，讓排程發布準時上線。由 ubuntu 的 crontab 在台北時間午夜後執行三次
# （m6 的時區是 Asia/Taipei）：
#
#   3,13,23 0 * * * /home/ubuntu/news-dispatch.sh
#
# 本檔是那支腳本的原始檔，改了之後要複製到 m6 的 /home/ubuntu/news-dispatch.sh。
# GitHub 的 schedule 實際上 4 到 8 小時才執行一次，文章排在 00:00 與 00:05、導讀歷史排在 00:10，
# 只靠 schedule 會晚好幾個小時上線。00:03 與 00:13 各接一批，00:23 補前兩輪失敗的情況。
#
# token 是只有 anoni-net/news 的 Actions 讀寫權限的 fine-grained token，放在
# /home/ubuntu/.config/news-dispatch-token（權限 600），2027-10-03 到期，換法見 SPEC.md「部署」。
# 成功時安靜結束，失敗才寫 log。
set -eu

TOKEN_FILE=/home/ubuntu/.config/news-dispatch-token
LOG=/home/ubuntu/news-dispatch.log
URL=https://api.github.com/repos/anoni-net/news/actions/workflows/deploy.yml/dispatches

code=$(curl -s -o /tmp/news-dispatch.out -w '%{http_code}' --max-time 30 -X POST \
    -H "Authorization: Bearer $(cat "$TOKEN_FILE")" \
    -H "Accept: application/vnd.github+json" \
    -d '{"ref":"main"}' "$URL") || code=000
if [ "$code" != 204 ]; then
    echo "$(date -Iseconds) HTTP $code $(head -c 300 /tmp/news-dispatch.out 2>/dev/null)" >>"$LOG"
    exit 1
fi
