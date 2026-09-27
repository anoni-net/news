#!/bin/sh
# m6 上拉 anoni.net/news 的 build 分支，由 ubuntu 的 crontab 每 5 分鐘執行一次：
#
#   */5 * * * * /home/ubuntu/news-pull.sh
#
# 本檔是那支腳本的原始檔，改了之後要複製到 m6 的 /home/ubuntu/news-pull.sh。
# 只接受 fast-forward。build 分支的歷史被改寫時停下來寫進 log，不強制覆蓋，等人處理。
# 有更新時才寫 log，沒有變動就安靜結束。上一輪還沒跑完時這一輪直接略過。
set -eu

REPO=/srv/anoni-net-news
LOG=/home/ubuntu/news-pull.log

exec 9>/tmp/news-pull.lock
flock -n 9 || exit 0

before=$(git -C "$REPO" rev-parse HEAD)
if ! git -C "$REPO" pull --ff-only -q origin build 2>>"$LOG"; then
    echo "$(date -Iseconds) 無法 fast-forward，停在 $before，需要人工處理" >>"$LOG"
    exit 1
fi
after=$(git -C "$REPO" rev-parse HEAD)
if [ "$before" != "$after" ]; then
    echo "$(date -Iseconds) $before -> $after $(git -C "$REPO" log -1 --format=%s)" >>"$LOG"
fi
