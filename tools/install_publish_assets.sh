#!/usr/bin/env bash
# 在維護者的機器上安裝 news-publish-assets，每台要上傳的機器執行一次，重複執行不會重複加入設定。
#
#   tools/install_publish_assets.sh --dest <主機>:<路徑>   # 第一次，寫入上傳目的地
#   tools/install_publish_assets.sh                       # 之後更新指令與設定
#
# 做三件事：
# 1. 把 tools/news-publish-assets 複製到 ~/.local/bin/
# 2. 把上傳目的地寫進 ~/.config/anoni-news/assets-rsync（不進 repo）
# 3. 在 ~/.claude/settings.json 加上允許規則 Bash(news-publish-assets *) 與 autoMode.environment 的說明，
#    讓 Claude Code 的 auto mode 直接放行這個指令。改之前先備份成 settings.json.bak-<時間>
#
# 連到圖片主機的 SSH 設定（Tailscale、金鑰、~/.ssh/config）要另外準備，這支腳本不處理。
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dest=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dest) dest="$2"; shift 2 ;;
    *) echo "不認得的參數：$1" >&2; exit 2 ;;
  esac
done

mkdir -p "$HOME/.local/bin"
install -m 755 "$here/news-publish-assets" "$HOME/.local/bin/news-publish-assets"
echo "已安裝 ~/.local/bin/news-publish-assets"

config="$HOME/.config/anoni-news/assets-rsync"
mkdir -p "$(dirname "$config")"
if [[ -n "$dest" ]]; then
  printf '%s\n' "$dest" > "$config"
  echo "已寫入上傳目的地：$config"
elif [[ ! -s "$config" ]]; then
  echo "還沒有上傳目的地，請加上 --dest <主機>:<路徑> 再執行一次" >&2
  exit 1
fi

settings="$HOME/.claude/settings.json"
python3 - "$settings" <<'PY'
import json, shutil, sys, time
from pathlib import Path

path = Path(sys.argv[1])
rule = "Bash(news-publish-assets *)"
env_note = ("This is the anoni.net news maintainer's own machine. Uploading news assets (site favicons, "
            "social preview cards) for the anoni-net/news repo to the community's own image host behind "
            "assets.anoni.net with the news-publish-assets command, or with that repo's tools/fetch_favicons.py "
            "and tools/make_cards.py, is routine work the maintainer has authorized.")
data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
before = json.dumps(data, sort_keys=True)
allow = data.setdefault("permissions", {}).setdefault("allow", [])
if rule not in allow:
    allow.append(rule)
environment = data.setdefault("autoMode", {}).setdefault("environment", ["$defaults"])
if env_note not in environment:
    environment.append(env_note)
if json.dumps(data, sort_keys=True) == before:
    print(f"{path} 已經有這兩項設定，沒有修改")
else:
    if path.exists():
        backup = path.with_name(f"{path.name}.bak-{time.strftime('%Y%m%d%H%M%S')}")
        shutil.copy2(path, backup)
        print(f"已備份 {backup}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"已更新 {path}：permissions.allow 加入 {rule}，autoMode.environment 加入圖片主機的說明")
PY
echo "設定在下一個新開的 Claude Code session 生效"
