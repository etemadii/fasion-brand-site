#!/bin/bash
# usage: preview.sh fig1  -> /tmp/fig1.png  (visual QA of one plate)
set -e
cd "$(dirname "$0")"
F=${1:-fig1}
BW=${2:-900}
cat > /tmp/prev_$F.html <<H
<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;background:#fff}svg{display:block;width:${BW}px;height:auto}</style>
</head><body>
H
cat figs/$F.svg >> /tmp/prev_$F.html
echo '</body></html>' >> /tmp/prev_$F.html
H2=$(( BW * 3 / 4 + 40 ))
chromium --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=${BW},1400 --screenshot=/tmp/$F.png "file:///tmp/prev_$F.html" 2>/dev/null | tail -1
python3 - <<PY
from struct import unpack
d=open('/tmp/$F.png','rb').read(33)
w,h=unpack('>II', d[16:24]); print('png', w, 'x', h)
PY
