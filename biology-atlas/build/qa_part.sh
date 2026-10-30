#!/bin/bash
# QA one part in isolation at print width.
set -e
cd "$(dirname "$0")"
P=${1:?part file}; HH=${2:-1500}; OUT=${3:-part}
{
  echo '<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><style>'
  cat style.css
  echo 'html,body{margin:0}body{padding:0 14mm}</style></head><body>'
  cat "parts/$P"
  echo '</body></html>'
} > /tmp/part_$OUT.html
python3 - <<PY
import re
p='/tmp/part_$OUT.html'; s=open(p,encoding='utf-8').read()
import glob,os
for f in sorted(glob.glob('figs/*.svg')):
    s=s.replace('{{'+os.path.basename(f)[:-4].upper()+'}}', open(f,encoding='utf-8').read())
open(p,'w',encoding='utf-8').write(s)
PY
chromium --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=690,$HH --screenshot=/tmp/$OUT.png "file:///tmp/part_$OUT.html" 2>/dev/null | tail -1
echo /tmp/$OUT.png
