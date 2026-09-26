#!/bin/sh
# 從 tools/og.html 產生三個語系的預覽圖（1200×630）：static/og.png、og-zh-cn.png、og-en.png。
# 需要 Chrome 與 Noto Sans CJK TC、SC 字型。
set -eu
cd "$(dirname "$0")/.."
CHROME="${CHROME:-google-chrome}"
for pair in ":og.png" "zh-CN:og-zh-cn.png" "en:og-en.png"; do
  lang="${pair%%:*}"
  file="${pair#*:}"
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --password-store=basic \
    --window-size=1200,630 --screenshot="$PWD/static/$file" "file://$PWD/tools/og.html?lang=$lang"
done
