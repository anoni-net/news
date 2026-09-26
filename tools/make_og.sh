#!/bin/sh
# 從 tools/og.html 產生 static/og.png（1200×630）。需要 Chrome 與 Noto Sans CJK TC 字型。
set -eu
cd "$(dirname "$0")/.."
CHROME="${CHROME:-google-chrome}"
"$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --password-store=basic \
  --window-size=1200,630 --screenshot="$PWD/static/og.png" "file://$PWD/tools/og.html"
