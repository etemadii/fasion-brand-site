# -*- coding: utf-8 -*-
"""Plate 1 — hair-cell stereocilia bundle (book p.19, SEM cover plate).

Redrawn as vector art so that every callout stays crisp in print.
Scale: 1 micrometre = 60 px inside the SEM field.
"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from svgkit import *

W, H = 900, 520
UM = 60.0


def halo(x, y, s, size=13.5, fill="#fff8e8", anchor="middle", weight="700", stroke="#150c04"):
    return txt(x, y, s, size=size, fill=fill, anchor=anchor, weight=weight,
               extra=f'stroke="{stroke}" stroke-width="3.2" paint-order="stroke"')


def base_point(t):
    """Feet of the rods lie on a wide V (the crease of the bundle), t = 0..1."""
    if t <= 0.5:
        f = t / 0.5
        return 262 - 232 * (1 - f), 322 - 74 * f, 0
    f = (t - 0.5) / 0.5
    return 262 + 232 * f, 322 - 74 * (1 - f), 0


def rod(bx, by, h, w, gid, tilt, shade=0.0):
    tw = w * 0.74
    tx = bx + math.sin(math.radians(tilt)) * h
    ty = by - h
    d = (f"M {bx - w/2:.1f} {by:.1f} L {tx - tw/2:.1f} {ty + tw*0.6:.1f} "
         f"Q {tx - tw/2:.1f} {ty:.1f} {tx:.1f} {ty:.1f} "
         f"Q {tx + tw/2:.1f} {ty:.1f} {tx + tw/2:.1f} {ty + tw*0.6:.1f} "
         f"L {bx + w/2:.1f} {by:.1f} Z")
    out = [ellipse(bx + 2.0, by + 1.0, w * 0.85, w * 0.30, fill="#140d04", stroke="none", opacity=0.35)]
    out.append(path(d, fill=f"url(#{gid})", stroke="#6b210f", sw=0.7))
    out.append(line(bx - w * 0.20, by - 3, tx - tw * 0.22, ty + 5, stroke="#ffe9b8",
                    sw=1.15, opacity=0.8))
    out.append(line(bx + w * 0.30, by - 2, tx + tw * 0.30, ty + 5, stroke="#7a2a10",
                    sw=0.9, opacity=0.55))
    if shade:
        out.append(path(d, fill="#2a1305", stroke="none", opacity=shade))
    return "".join(out)


def sem_background(b):
    b.append(f'<rect width="{W}" height="{H}" fill="url(#semG)"/>')
    b.append(path("M0,520 L0,352 C58,320 116,340 174,328 C230,316 266,298 310,306 "
                  "C354,314 390,338 450,332 C510,326 554,308 602,316 "
                  "C648,324 688,302 738,310 C798,320 854,302 900,318 L900,500 Z",
                  fill="url(#cellG)", stroke="none"))
    rnd = random.Random(11)
    for _ in range(260):
        x, y = rnd.uniform(2, 898), rnd.uniform(300, 496)
        r = rnd.uniform(1.3, 7.0)
        b.append(ellipse(x, y, r, r * rnd.uniform(0.5, 1.0), fill="#ffd9a0",
                         stroke="none", opacity=rnd.uniform(0.04, 0.20)))
    for _ in range(40):  # shallow microvilli on the apical surface
        x, y = rnd.uniform(10, 890), rnd.uniform(330, 470)
        b.append(ellipse(x, y - 3, 3.2, 4.4, fill="#8a6a2e", stroke="#c9a55e",
                         sw=0.4, opacity=0.55))
    b.append(path("M664,352 q6,-26 -2,-44 q10,16 12,44", fill="none", stroke="#f3c98b", sw=2.1))
    b.append(ellipse(716, 300, 8.5, 6.5, fill="#b45309", stroke="none", opacity=0.5))


def bundle(b):
    b.append(f'<ellipse cx="262" cy="252" rx="205" ry="26" fill="#0b0600" opacity="0.5" filter="url(#blur8)"/>')
    rows = [(0, 0.56, 1.00, 0.0, 9), (1, 0.78, 0.95, 0.0, -8), (2, 1.00, 0.90, 0.0, -26)]
    rnd = random.Random(3)
    for r, hs, ws, shade, dy in reversed(rows):
        n = 41
        for i in range(n):
            t = (i + 0.5) / n
            bx, by, _ = base_point(t)
            by -= dy
            # height: tallest just left of centre, tapering towards both ends
            prof = 0.46 + 0.54 * math.exp(-((t - 0.5) ** 2) / 0.13)
            h = 198 * prof * hs * rnd.uniform(0.95, 1.05)
            b.append(rod(bx - r * 5, by, h, 9.6 * ws,
                         "rgA" if r == 0 else "rgB", -12 + 24 * t, shade))



def screen(b):
    # scale bar, top left
    b.append(line(46, 44, 46 + UM, 44, stroke="#fff8e8", sw=4.0))
    b.append(line(46, 37, 46, 51, stroke="#fff8e8", sw=4.0))
    b.append(line(46 + UM, 37, 46 + UM, 51, stroke="#fff8e8", sw=4.0))
    b.append(halo(46 + UM / 2, 26, "۱ میکرومتر", size=14))
    b.append(halo(602, 30, "SEM · فصل ۲ — حواس", size=13, anchor="end"))


def callouts(b):
    """Numbered badges on the structures + a key strip below (no leader crosses text)."""
    X0, Y0, X1, Y1 = 14, 336, 602, 508
    b.append(rect(X0, Y0, X1 - X0, Y1 - Y0, fill="#ffffff", stroke="#ffffff", sw=0,
                  rx=12, opacity=0.94, extra='filter="url(#soft)"'))
    b.append(txt(X1 - 14, Y0 + 24, "راهنمای شماره‌ها", size=12.5, fill=ROSE,
                 anchor="end", weight="700"))
    b.append(line(X0 + 14, Y0 + 32, X1 - 14, Y0 + 32, stroke=ROSE_L, sw=1.0))

    key = [
        (1, (566, 374), "آرایش هلالی سه‌ردیفی"),
        (2, (566, 416), "استریوسیلیا: میکروویلی اکتینی"),
        (3, (566, 458), "ردیف پله‌ای: کوتاه ← بلند"),
        (4, (286, 374), "بلندترین ردیف = قطب مثبت"),
        (5, (286, 416), "سطح رأسی یاختهٔ مویی"),
        (6, (286, 458), "بزرگ‌نمایی: پیوند نوکی"),
    ]
    for n, (bx, by), label in key:
        b.append(badge(n, bx, by, fill=ROSE, size=13))
        b.append(txt(bx - 22, by + 4.7, label, size=12.5, fill=INK, anchor="end"))

    # badges that sit on the plate itself, with a short stub to the structure
    on_plate = [
        (1, (372, 100), (306, 132)),
        (2, (40, 150), (74, 232)),
        (3, (492, 150), (452, 232)),
        (4, (238, 34), (258, 92)),
        (5, (520, 300), (486, 320)),
        (6, (642, 44), (712, 78)),
    ]
    for n, (bx, by), (tx, ty) in on_plate:
        b.append(line(bx, by, tx, ty, stroke=ROSE, sw=1.2, dash="3 3", opacity=0.9))
        b.append(circle(tx, ty, 3.2, fill=ROSE, stroke="#ffffff", sw=1.1))
        b.append(badge(n, bx, by, fill=ROSE, size=13))



def vignette(b):
    b.append(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')


def inset(b):
    x0, y0, w, h = 620, 12, 268, 252
    b.append(rect(x0, y0, w, h, fill="#fffdf8", stroke=ROSE, sw=1.6, rx=10,
                  opacity=0.98, extra='filter="url(#soft)"'))
    b.append(txt(x0 + w - 12, y0 + 22, "بزرگ‌نمایی ۸× — پیوند نوکی", size=12,
                 fill=ROSE, anchor="end", weight="700"))
    b.append(line(300, 130, x0, y0 + 40, stroke=ROSE, sw=1.0, dash="5 4", opacity=0.42))
    b.append(line(392, 200, x0, y0 + h - 40, stroke=ROSE, sw=1.0, dash="5 4", opacity=0.42))

    # tall rod (right) and short rod (left)
    b.append(rect(x0 + 136, y0 + 44, 34, 148, fill="url(#rgA)", stroke="#6b210f", sw=1.0))
    b.append(rect(x0 + 78, y0 + 100, 32, 92, fill="url(#rgA)", stroke="#6b210f", sw=1.0))
    for k in range(4):
        b.append(line(x0 + 156 + k * 7, y0 + 50, x0 + 156 + k * 7, y0 + 188,
                      stroke="#fff3d0", sw=0.9, opacity=0.5))
    for k in range(3):
        b.append(line(x0 + 71 + k * 7, y0 + 106, x0 + 71 + k * 7, y0 + 188,
                      stroke="#fff3d0", sw=0.9, opacity=0.5))
    b.append(txt(x0 + 194, y0 + 152, "اکتین", size=10.5, fill=MUTED, anchor="start"))

    # apical membrane + MET channel at the tip of the short row
    b.append(path(f"M {x0+60} {y0+100} q 20,-12 40,0", fill="none", stroke=BLUE, sw=2.2))
    b.append(rect(x0 + 74, y0 + 86, 14, 13, fill="#dbeafe", stroke=BLUE, sw=1.5, rx=3))
    b.append(latin(x0 + 58, y0 + 130, "TMC1/2", size=9.5, fill=BLUE, anchor="end"))

    # tip link (stiff spring: CDH23 + PCDH15)
    x1, y1 = x0 + 100, y0 + 86
    x2, y2 = x0 + 136, y0 + 60
    pts = [(x1, y1)]
    for k in range(1, 9):
        f = k / 9
        pts.append((x1 + (x2 - x1) * f, y1 + (y2 - y1) * f + (3.4 if k % 2 else -3.4)))
    pts.append((x2, y2))
    b.append(poly(pts, stroke="#0f172a", sw=1.8))
    b.append(latin(x0 + 118, y0 + 38, "CDH23 + PCDH15", size=9, fill=INK, anchor="middle"))

    # adaptation motor at the upper insertion
    b.append(ellipse(x0 + 142, y0 + 52, 8.5, 5.5, fill=ROSE_L, stroke=ROSE, sw=1.4))
    b.append(latin(x0 + 196, y0 + 52, "MYO1C", size=9, fill=ROSE, anchor="start"))

    # deflection arrow
    b.append(cpath_arrow(f"M {x0+52} {y0+212} q 56,-10 88,-32", color=TEAL, sw=2.0))
    b.append(txt(x0 + 58, y0 + 228, "کشش", size=10.5, fill=TEAL, anchor="start"))


    b.append(badge(7, x0 + 20, y0 + 146, r=11, size=12))
    b.append(line(x0 + 31, y0 + 146, x0 + 80, y0 + 92, stroke=ROSE, sw=1.1, dash="3 2"))
    b.append(circle(x0 + 80, y0 + 92, 3.2, fill=ROSE, stroke="#fff", sw=1.2))
    b.append(badge(8, x0 + 238, y0 + 74, r=11, size=12))
    b.append(line(x0 + 228, y0 + 78, x0 + 160, y0 + 54, stroke=ROSE, sw=1.1, dash="3 2"))
    b.append(txt(x0 + w / 2, y0 + 244,
                 "۶ پیوند نوکی · ۷ کانال مکانیکی · ۸ موتور میوزین",
                 size=10.5, fill=INK_SOFT, anchor="middle"))


def numbers(b):
    x0, y0, w, h = 620, 274, 268, 168
    b.append(rect(x0, y0, w, h, fill="#f8fbfc", stroke=LINE, sw=1.2, rx=10, opacity=0.97))
    b.append(txt(x0 + w - 14, y0 + 26, "اعداد کلیدی", size=12.5, fill=TEAL, anchor="end",
                 weight="700"))
    rows_info = [
        ("قطر (میکرومتر)", "0.1 - 0.2"),
        ("ارتفاع ردیف‌ها (میکرومتر)", "1 - 10"),
        ("شمار در هر دسته", "50 - 100"),
        ("یاختهٔ مویی در هر گوش", "~ 16000"),
    ]
    y = y0 + 56
    for k, v in rows_info:
        b.append(txt(x0 + w - 14, y, k, size=10.8, fill=INK_SOFT, anchor="end"))
        b.append(latin(x0 + 14, y, v, size=10.5, fill=INK, anchor="start", weight="700",
                       style="normal"))
        b.append(line(x0 + 82, y - 4, x0 + w - 140, y - 4, stroke=LINE, sw=0.9, dash="2 3"))
        y += 27


def plate():
    b = []
    sem_background(b)
    bundle(b)
    vignette(b)
    screen(b)
    callouts(b)
    inset(b)
    numbers(b)
    grads = """
    <linearGradient id="rgA" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffe0a8"/><stop offset="0.30" stop-color="#fb923c"/>
      <stop offset="0.66" stop-color="#ea580c"/><stop offset="0.92" stop-color="#b91c1c"/>
      <stop offset="1" stop-color="#7f1d1d"/></linearGradient>
    <linearGradient id="rgB" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#e9c294"/><stop offset="0.30" stop-color="#d97706"/>
      <stop offset="0.70" stop-color="#b45309"/><stop offset="1" stop-color="#7c2d12"/></linearGradient>
    <radialGradient id="semG" cx="40%" cy="34%" r="80%">
      <stop offset="0" stop-color="#6b5528"/><stop offset="0.5" stop-color="#3d2f17"/>
      <stop offset="1" stop-color="#150f06"/></radialGradient>
    <linearGradient id="cellG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5a4620"/><stop offset="1" stop-color="#1e160a"/></linearGradient>
    <filter id="blur8" x="-40%" y="-60%" width="180%" height="240%"><feGaussianBlur stdDeviation="9"/></filter>
  <radialGradient id="vig" cx="46%" cy="42%" r="72%">
      <stop offset="0.45" stop-color="#000000" stop-opacity="0"/>
      <stop offset="1" stop-color="#050300" stop-opacity="0.55"/></radialGradient>"""
    return svg(W, H, "".join(b), grads)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "figs", "fig1.svg")
    save(out, plate())
    print("wrote", out)

