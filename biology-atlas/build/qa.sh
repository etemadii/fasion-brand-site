#!/bin/bash
# QA: screenshot the atlas at print width (≈690px) scrolled to an anchor.
# usage: ./qa.sh sec3 out3 [height]
set -e
cd "$(dirname "$0")"
SEC=${1:-sec1}; OUT=${2:-qa}; HH=${3:-1900}
cat > /tmp/qa.html <<H
<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#888}
iframe{width:690px;height:90000px;border:0;display:block;background:#fff}</style></head><body>
<iframe src="file://$(cd .. && pwd)/atlas.html#$SEC"></iframe></body></html>
H
chromium --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=690,$HH --screenshot=/tmp/$OUT.png "file:///tmp/qa.html" 2>/dev/null | tail -1
echo "/tmp/$OUT.png"
