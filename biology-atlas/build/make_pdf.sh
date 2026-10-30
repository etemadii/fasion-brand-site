#!/bin/bash
# Rebuild every plate, assemble the HTML, then print to A4 PDF with headless Chromium.
set -e
cd "$(dirname "$0")"

for f in fig1_haircell.py fig2_gating.py fig3_skin.py fig4_spindle.py fig5_eye.py; do
  python3 "$f"
done
python3 build.py
chromium --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --run-all-compositor-stages-before-draw --virtual-time-budget=10000 \
  --no-pdf-header-footer --print-to-pdf="$(cd .. && pwd)/atlas.pdf" \
  "file://$(cd .. && pwd)/atlas.html" 2>&1 | grep -E 'bytes written|error' || true
ls -la "$(cd .. && pwd)/atlas.pdf"
