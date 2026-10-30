# -*- coding: utf-8 -*-
"""Plate 5 — the eye (book fig. 2-4, p.23) + aqueous outflow + retinal detail."""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from svgkit import *

W, H = 900, 748
CX, CY, R = 276, 250, 196


def pt(deg, r):
    a = math.radians(deg)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def arcpath(r, a1, a2, sweep=1):
    x1, y1 = pt(a1, r)
    x2, y2 = pt(a2, r)
    large = 1 if abs(a2 - a1) > 180 else 0
    return f"M {x1:.1f} {y1:.1f} A {r} {r} 0 {large} {sweep} {x2:.1f} {y2:.1f}"


def globe(b):
    # sclera (open at the front), choroid, retina, vitreous
    b.append(path(arcpath(R, 132, 408), stroke="#d6d3d1", sw=13))
    b.append(path(arcpath(R - 9, 134, 406), stroke="#9f1239", sw=6, opacity=0.6))
    b.append(path(arcpath(R - 17, 136, 404), stroke="#fde68a", sw=7, opacity=0.92))
    b.append(f'<circle cx="{CX}" cy="{CY}" r="{R-24}" fill="#e0f2fe" opacity="0.5"/>')
    # cornea (bulging to the left) + limbus
    cor = (f"M {pt(132, R)[0]:.1f} {pt(132, R)[1]:.1f} Q 92 250 "
           f"{pt(228, R)[0]:.1f} {pt(228, R)[1]:.1f}")
    b.append(path(cor, fill="none", stroke="#93c5fd", sw=11))
    b.append(path(cor, fill="none", stroke="#dbeafe", sw=4))
    b.append(txt(84, 150, "قرنیه", size=10, fill="#1d4ed8"))
    # iris leaves (triangular wedges) with the pupil between them
    b.append(polygon([(152, 158), (172, 168), (166, 212), (150, 204)], fill="#7f1d1d",
                     stroke="#450a0a", sw=1.0))
    b.append(polygon([(152, 342), (172, 332), (166, 288), (150, 296)], fill="#7f1d1d",
                     stroke="#450a0a", sw=1.0))
    # ciliary body at the iridocorneal root
    b.append(polygon([(150, 150), (182, 146), (176, 186)], fill="#a16207", stroke="#713f12", sw=1.0))
    b.append(polygon([(150, 350), (182, 354), (176, 314)], fill="#a16207", stroke="#713f12", sw=1.0))
    for dy in (-34, -18, 18, 34):
        b.append(line(180, 250 + dy * 1.35, 196, 250 + dy * 0.9, stroke=TEAL, sw=1.2))
    b.append(txt(214, 140, "جسم مژگانی", size=8.8, fill="#713f12"))
    b.append(txt(214, 372, "رباط آویزان", size=8.8, fill=TEAL))
    # lens
    b.append(ellipse(196, 250, 21, 47, fill="#dbeafe", stroke="#1d4ed8", sw=1.6, opacity=0.95))
    b.append(ellipse(196, 250, 12, 34, fill="#eff6ff", stroke="#93c5fd", sw=0.9))
    b.append(txt(196, 322, "عدسی", size=9.5, fill="#1d4ed8"))
    b.append(txt(104, 288, "اتاق قدامی", size=8.4, fill="#0369a1"))

    # optic nerve head + retinal vessels that hug the inner wall
    b.append(ellipse(462, 300, 13, 22, fill="#fecaca", stroke="#b91c1c", sw=1.2))
    b.append(path("M 470 300 q 26,4 40,14 q 18,12 34,6", fill="none", stroke="#fca5a5", sw=13,
                  extra='stroke-linecap="round"'))
    b.append(path("M 470 300 q 26,4 40,14 q 18,12 34,6", fill="none", stroke="#b91c1c", sw=2.0))
    for (x2, y2, cx_, cy_) in ((300, 84, 430, 120), (300, 418, 430, 382),
                               (250, 132, 386, 168), (250, 370, 386, 336)):
        b.append(path(f"M 452 298 Q {cx_} {cy_} {x2} {y2}", fill="none", stroke="#dc2626",
                      sw=1.4, opacity=0.7))
    b.append(circle(404, 352, 15, fill="#fde68a", stroke="#b45309", sw=1.0))
    b.append(circle(401, 354, 4.5, fill="#92400e", stroke="none"))
    b.append(txt(404, 380, "لکهٔ زرد", size=8.8, fill="#92400e"))
    b.append(txt(502, 336, "نقطهٔ کور", size=8.8, fill="#991b1b"))
    # extraocular muscle
    b.append(path(f"M {pt(150, R+2)[0]:.1f} {pt(150, R+2)[1]:.1f} q -46,-16 -60,-46", fill="none",
                  stroke="#f87171", sw=8, opacity=0.8))
    b.append(txt(104, 62, "ماهیچهٔ چشم", size=8.8, fill="#b91c1c"))


def aqueous_card(b):
    x0, y0, w, h = 556, 20, 328, 236
    b.append(rect(x0, y0, w, h, fill="#f8fbfd", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x0 + w - 12, y0 + 24, "مسیر گردش مایع زلالیه", size=11.5, fill=TEAL,
                 anchor="end", weight="700"))
    steps = ["اپیتلیوم مژگانی: تولید", "اتاق خلفی", "مردمک",
             "اتاق قدامی", "شبکهٔ ترابکولار", "کانال شلم", "سیاهرگ‌های صلبیه"]
    y = y0 + 42
    for i, st in enumerate(steps):
        fill = TEAL_L if i == 0 else ("#fdf2f8" if i in (4, 5, 6) else "#f1f5f9")
        stroke = TEAL if i == 0 else (ROSE if i in (4, 5, 6) else LINE)
        b.append(rect(x0 + 84, y, 196, 24, fill=fill, stroke=stroke, sw=1.0, rx=6))
        b.append(txt(x0 + 182, y + 16, st, size=9.4, fill=INK, weight="600"))
        if i:
            b.append(cpath_arrow(f"M {x0+182} {y-4} l 0,-5", color=TEAL, sw=1.4))
        y += 26
    b.append(txt(x0 + w - 12, y0 + 226,
                 "بسته شدن این مسیر ← افزایش فشار ← آب‌سیاه", size=9, fill=INK_SOFT,
                 anchor="end"))


def numbers_card(b):
    x0, y0, w, h = 556, 268, 328, 152
    b.append(rect(x0, y0, w, h, fill="#f9fbfc", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x0 + w - 12, y0 + 24, "اعداد کلیدی چشم", size=11.5, fill=ROSE, anchor="end",
                 weight="700"))
    rows = [("قطر کرهٔ چشم", "24 mm"), ("قدرت کلی (قرنیه + عدسی)", "60 D (40 + 20)"),
            ("شمار میله‌ها / مخروط‌ها", "120 M / 6 M"), ("قطر لکهٔ زرد", "1.5 mm")]
    y = y0 + 52
    for k, v in rows:
        b.append(txt(x0 + w - 12, y, k, size=10, fill=INK_SOFT, anchor="end"))
        b.append(latin(x0 + 12, y, v, size=9.5, fill=INK, anchor="start", weight="700",
                       style="normal"))
        b.append(line(x0 + 132, y - 4, x0 + w - 168, y - 4, stroke=LINE, sw=0.9, dash="2 3"))
        y += 28


def retina_card(b):
    x0, y0, w, h = 556, 432, 328, 142
    b.append(rect(x0, y0, w, h, fill="#f9fbfc", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x0 + w - 12, y0 + 22, "همگرایی: دقت در برابر حساسیت", size=11, fill=AMBER,
                 anchor="end", weight="700"))
    b.append(txt(x0 + 20, y0 + 46, "مرکز بینایی: ۱ مخروط ← ۱ دوقطبی ← ۱ گانگلیون", size=8.2,
                 fill=INK, anchor="start"))
    b.append(circle(x0 + 26, y0 + 70, 8, fill="#fbbf24", stroke="#b45309", sw=1.0))
    b.append(circle(x0 + 58, y0 + 70, 7, fill="#a5b4fc", stroke="#4338ca", sw=1.0))
    b.append(circle(x0 + 90, y0 + 70, 7, fill="#fca5a5", stroke="#b91c1c", sw=1.0))
    b.append(arrow(x0 + 36, y0 + 70, x0 + 50, y0 + 70, color=INK_SOFT, sw=1.2))
    b.append(arrow(x0 + 66, y0 + 70, x0 + 82, y0 + 70, color=INK_SOFT, sw=1.2))
    b.append(txt(x0 + 20, y0 + 102, "حاشیه: چند میله ← یک گانگلیون (همگرایی بالا)", size=8.2,
                 fill=INK_SOFT, anchor="start"))
    for k in range(4):
        b.append(circle(x0 + 26 + k * 11, y0 + 122 - (k % 2) * 9, 4.5, fill="#94a3b8",
                        stroke="#475569", sw=0.8))
    b.append(circle(x0 + 82, y0 + 118, 7, fill="#a5b4fc", stroke="#4338ca", sw=1.0))
    b.append(circle(x0 + 114, y0 + 118, 7, fill="#fca5a5", stroke="#b91c1c", sw=1.0))
    b.append(txt(x0 + w - 14, y0 + 134, "شبکیهٔ وارونه", size=8.2, fill=MUTED, anchor="end"))


def plate():
    b = []
    b.append(txt(16, 30, "شکل ۴ — ساختار کرهٔ چشم", size=15, fill=INK, anchor="start",
                 weight="700"))
    b.append(txt(884, 30, "برش افقی · چشم چپ از بالا", size=10.5, fill=INK_SOFT, anchor="end"))
    globe(b)
    aqueous_card(b)
    numbers_card(b)
    retina_card(b)

    on_plate = [
        (1, (108, 104), (100, 166)),
        (2, (92, 240), (128, 238)),
        (3, (246, 300), (162, 250)),
        (4, (250, 132), (176, 168)),
        (5, (430, 62), (386, 92)),
        (6, (250, 470), (156, 393)),
        (7, (390, 466), (365, 405)),
        (8, (150, 432), (178, 296)),
        (9, (112, 352), (168, 286)),
        (10, (296, 176), (300, 214)),
        (11, (486, 392), (418, 346)),
        (12, (40, 40), (78, 86)),
    ]
    for n, (bx, by), (tx, ty) in on_plate:
        b.append(line(bx, by, tx, ty, stroke=ROSE, sw=1.1, dash="3 3", opacity=0.85))
        b.append(circle(tx, ty, 3.0, fill=ROSE, stroke="#ffffff", sw=1.0))
        b.append(badge(n, bx, by, r=11, fill=ROSE, size=11.5))

    items = [
        (1, "قرنیه — cornea، شفاف و بی‌رگ"),
        (2, "اتاق قدامی و زلالیه"),
        (3, "مردمک و عنبیه"),
        (4, "جسم مژگانی و زونول"),
        (5, "صلبیه — sclera"),
        (6, "مشیمیه — choroid"),
        (7, "شبکیه و عروق آن"),
        (8, "عدسی — lens"),
        (9, "اتاق خلفی"),
        (10, "زجاجیه — vitreous"),
        (11, "لکهٔ زرد و مرکز بینایی"),
        (12, "ماهیچهٔ بیرونی چشم"),
    ]
    b.append(rect(20, 588, 864, 148, fill="#ffffff", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(870, 612, "راهنمای شماره‌ها", size=11.5, fill=ROSE, anchor="end", weight="700"))
    b.append(line(34, 620, 870, 620, stroke=ROSE_L, sw=1.0))
    for i, (n, text) in enumerate(items):
        c, r = i // 4, i % 4
        bx = 870 - c * 288
        by = 646 + r * 24
        b.append(badge(n, bx - 12, by - 5, r=10, fill=ROSE, size=10.5))
        b.append(txt(bx - 28, by, text, size=10.2, fill=INK, anchor="end"))
    return svg(W, H, "".join(b))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "figs", "fig5.svg")
    save(out, plate())
    print("wrote", out)
