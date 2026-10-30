#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble atlas.html from build/parts/*.html + build/figs/*.svg.

Usage:  python3 build.py           -> ../atlas.html
        ./make_pdf.sh              -> ../atlas.pdf
"""
import glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def main():
    css = read(os.path.join(HERE, "style.css"))
    figs = {}
    for path in glob.glob(os.path.join(HERE, "figs", "*.svg")):
        key = os.path.splitext(os.path.basename(path))[0].upper()  # FIG1
        figs["{{" + key + "}}"] = read(path)

    parts = sorted(glob.glob(os.path.join(HERE, "parts", "*.html")))
    body = "\n".join(read(p) for p in parts)
    for k, v in figs.items():
        body = body.replace(k, v)

    # give every top-level section an anchor for QA / deep links
    counter = {"n": 0}
    def _id(m):
        counter["n"] += 1
        return f'<section id="sec{counter["n"]}"'
    body = re.sub(r"<section", _id, body)

    left = re.findall(r"\{\{[A-Z0-9_]+\}\}", body)
    if left:
        print("WARNING unresolved placeholders:", sorted(set(left)))
    if "{{CSS}}" in body:
        raise SystemExit("CSS placeholder found inside body parts")

    html = f"""<!doctype html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<title>اطلس مشروح گیرنده‌های حسی — فصل ۲: حواس</title>
<style>
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""
    out = os.path.join(ROOT, "atlas.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", out, f"({len(html) // 1024} KB, {len(parts)} parts)")


if __name__ == "__main__":
    main()
