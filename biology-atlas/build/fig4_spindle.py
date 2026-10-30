# -*- coding: utf-8 -*-
"""Plate 4 — proprioceptors: muscle spindle and Golgi tendon organ (book fig. 2-3, p.22)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from svgkit import *

W, H = 900, 660
MUSC = "url(#musG)"


def muscle_scheme(b):
    x0, y0 = 24, 56
    b.append(rect(x0, 118, 66, 40, fill="#e7e5e4", stroke="#a8a29e", sw=1.2, rx=10))
    b.append(rect(x0 + 314, 118, 66, 40, fill="#e7e5e4", stroke="#a8a29e", sw=1.2, rx=10))
    b.append(rect(x0 + 64, 124, 34, 28, fill="#f5e6c8", stroke="#c9a227", sw=1.1, rx=6))
    b.append(rect(x0 + 302, 124, 34, 28, fill="#f5e6c8", stroke="#c9a227", sw=1.1, rx=6))
    b.append(path(f"M {x0+96} 138 q 60,-42 120,-42 q 60,0 120,42 q -60,42 -120,42 q -60,0 -120,-42",
                  fill=MUSC, stroke="#b45309", sw=1.3))
    for k in range(9):
        xx = x0 + 112 + k * 19
        b.append(line(xx, 112, xx + 6, 166, stroke="#f59e0b", sw=0.8, opacity=0.6))
    b.append(txt(x0 + 168, 104, "ماهیچه (فیبرهای برون‌دوکی)", size=10, fill="#9a3412"))
    b.append(ellipse(x0 + 168, 138, 30, 11, fill="#fce7f3", stroke=ROSE, sw=1.3))
    b.append(path(f"M {x0+142} 138 q 26,-7 52,0", fill="none", stroke=ROSE, sw=1.0))
    b.append(txt(x0 + 168, 186, "دوک عضلانی (موازی)", size=9.5, fill=ROSE, weight="700"))
    b.append(ellipse(x0 + 318, 138, 15, 9, fill="#fef9c3", stroke="#a16207", sw=1.3))
    for k in range(3):
        b.append(line(x0 + 306 + k * 8, 132, x0 + 306 + k * 8, 144, stroke="#a16207", sw=0.8))
    b.append(txt(x0 + 318, 186, "اندام وتری (سری)", size=9.5, fill="#a16207", weight="700"))
    b.append(txt(x0 + 34, 176, "استخوان", size=9.5, fill="#78716c"))


def spindle_detail(b):
    x0, y0 = 430, 60
    b.append(path(f"M {x0+18} 150 q 62,-56 152,-56 q 90,0 152,56 q -62,56 -152,56 q -90,0 -152,-56",
                  fill="#fff1f2", stroke=ROSE, sw=1.6))
    fibres = [(122, "bag"), (140, "bag"), (158, "chain"), (174, "chain"), (190, "chain")]
    for yy, kind in fibres:
        b.append(line(x0 + 34, yy, x0 + 306, yy, stroke="#9d174d", sw=2.8, opacity=0.45))
        if kind == "bag":
            b.append(ellipse(x0 + 172, yy, 16, 7.0, fill="#fbcfe8", stroke=ROSE, sw=1.0))
            for k in range(4):
                b.append(circle(x0 + 163 + k * 6, yy, 1.9, fill="#9d174d", stroke="none"))
        else:
            for k in range(7):
                b.append(circle(x0 + 146 + k * 9, yy, 1.8, fill="#9d174d", stroke="none"))
    # Ia annulospiral rings around the equatorial bag region
    for k in range(4):
        b.append(ellipse(x0 + 172, 116 + k * 16, 27, 5.5, fill="none", stroke=TEAL, sw=1.7))
    # II flower-spray at the polar region
    for dy in (-14, 0, 14):
        b.append(path(f"M {x0+280} {170+dy} q 14,-6 20,-14", fill="none", stroke=BLUE, sw=1.3))
    # gamma motor endings at both poles
    for px in (x0 + 66, x0 + 288):
        for dy in (-10, 10):
            b.append(path(f"M {px} {176+dy} l 10,0 l 6,4", fill="none", stroke="#7c3aed", sw=1.5))
    b.append(path(f"M {x0+172} 96 q 4,-22 22,-32", fill="none", stroke=TEAL, sw=2.6))
    b.append(latin(x0 + 208, 58, "Ia", size=11, fill=TEAL, weight="700"))
    b.append(path(f"M {x0+300} 166 q 16,-12 28,-24", fill="none", stroke=BLUE, sw=2.2))
    b.append(latin(x0 + 336, 134, "II", size=10.5, fill=BLUE, weight="700"))
    b.append(path(f"M {x0+60} 186 q -14,14 -26,22", fill="none", stroke="#7c3aed", sw=2.0))
    b.append(latin(x0 + 24, 214, "gamma", size=9, fill="#7c3aed", weight="700"))
    b.append(txt(x0 + 160, 230, "دوک عضلانی — برش طولی (بزرگ‌نمایی)", size=9.5, fill=INK_SOFT))


def gto_detail(b):
    x0, y0 = 24, 290
    b.append(txt(x0 + 190, y0 - 8, "اندام وتری گلژی: حسگر نیرو (سری با فیبر عضلانی)", size=11,
                 fill=AMBER, weight="700"))
    b.append(rect(x0, y0 + 22, 380, 116, fill="#fffbeb", stroke="#fcd34d", sw=1.2, rx=10))
    for k in range(7):
        y = y0 + 40 + k * 13
        b.append(path(f"M {x0+22} {y} q 90,-6 170,0 q 90,6 166,0", fill="none",
                      stroke="#d6b26a", sw=1.6))
    b.append(ellipse(x0 + 190, y0 + 80, 150, 44, fill="none", stroke="#a16207", sw=1.4,
                     dash="4 3"))
    b.append(txt(x0 + 190, y0 + 132, "کپسول: بسته‌های کلاژن بین دوک و تاندون", size=9.5,
                 fill="#92400e"))
    b.append(path(f"M {x0+340} {y0+80} q 24,-6 34,-22", fill="none", stroke=ROSE, sw=2.4))
    b.append(latin(x0 + 356, y0 + 44, "Ib", size=10.5, fill=ROSE, weight="700"))


def circuits(b):
    x0, y0 = 430, 292
    b.append(txt(x0 + 220, y0 - 8, "دو بازخورد عصبی-عضلانی", size=11, fill=TEAL, weight="700"))
    b.append(rect(x0 + 46, y0 + 12, 348, 104, fill="#f8fafc", stroke="#94a3b8", sw=1.2, rx=12))
    b.append(txt(x0 + 384, y0 + 28, "نخاع", size=9, fill=INK_SOFT, anchor="end"))
    # monosynaptic stretch reflex
    b.append(latin(x0 + 62, y0 + 44, "Ia", size=9.5, fill=TEAL, weight="700"))
    b.append(cpath_arrow(f"M {x0+78} {y0+40} q 44,0 62,0", color=TEAL, sw=1.8))
    b.append(circle(x0 + 158, y0 + 40, 9, fill=TEAL_L, stroke=TEAL, sw=1.2))
    b.append(latin(x0 + 158, y0 + 44, "α", size=7.6, fill=TEAL, weight="700"))
    b.append(cpath_arrow(f"M {x0+168} {y0+40} q 26,0 40,0", color=TEAL, sw=1.8))
    b.append(txt(x0 + 214, y0 + 44, "انقباض", size=9, fill=TEAL, anchor="start"))
    # disynaptic GTO reflex
    b.append(latin(x0 + 62, y0 + 88, "Ib", size=9.5, fill=ROSE, weight="700"))
    b.append(cpath_arrow(f"M {x0+78} {y0+84} q 26,0 36,0", color=ROSE, sw=1.8))
    b.append(circle(x0 + 124, y0 + 84, 8, fill="#fef2f2", stroke=ROSE, sw=1.2))
    b.append(latin(x0 + 124, y0 + 87, "In", size=7.2, fill=ROSE, weight="700"))
    b.append(cpath_arrow(f"M {x0+132} {y0+84} q 14,0 18,0", color=ROSE, sw=1.8))
    b.append(circle(x0 + 158, y0 + 84, 9, fill="#f1f5f9", stroke=INK_SOFT, sw=1.2))
    b.append(latin(x0 + 158, y0 + 87, "α", size=7.6, fill=INK_SOFT, weight="700"))
    b.append(latin(x0 + 172, y0 + 80, "(-)", size=8.5, fill=ROSE, weight="700"))
    b.append(txt(x0 + 214, y0 + 88, "شل شدن", size=9, fill=INK_SOFT, anchor="start"))
    b.append(txt(x0 + 220, y0 + 108, "یک‌سیناپسی / دوسیناپسی", size=8.5, fill=MUTED))


def plate():
    b = []
    b.append(txt(16, 30, "شکل ۳ — گیرنده‌های حس وضعیت بدن", size=15, fill=INK, anchor="start",
                 weight="700"))
    b.append(txt(884, 30, "دوک: کشش و طول ماهیچه · اندام وتری: نیرو", size=11,
                 fill=INK_SOFT, anchor="end"))
    muscle_scheme(b)
    spindle_detail(b)
    gto_detail(b)
    circuits(b)

    on_plate = [
        (1, (52, 214), (60, 158)),
        (2, (392, 214), (346, 148)),
        (3, (436, 100), (452, 120)),
        (4, (556, 246), (600, 144)),
        (5, (640, 256), (600, 188)),
        (6, (700, 62), (614, 112)),
        (7, (452, 232), (496, 176)),
        (8, (796, 190), (734, 166)),
        (9, (250, 264), (214, 352)),
        (10, (470, 250), (520, 336)),
        (11, (720, 252), (588, 378)),
    ]
    for n, (bx, by), (tx, ty) in on_plate:
        b.append(line(bx, by, tx, ty, stroke=ROSE, sw=1.1, dash="3 3", opacity=0.85))
        b.append(circle(tx, ty, 3.0, fill=ROSE, stroke="#ffffff", sw=1.0))
        b.append(badge(n, bx, by, r=11, fill=ROSE, size=11.5))

    items = [
        (1, "دوک عضلانی — muscle spindle"),
        (2, "اندام وتری — Golgi tendon organ"),
        (3, "کپسول و فضای لنف — capsule"),
        (4, "فیبر کیسه‌ای — nuclear bag"),
        (5, "فیبر زنجیره‌ای — nuclear chain"),
        (6, "پایانهٔ حلقه‌ای — Ia afferent"),
        (7, "نورون حرکتی گاما — gamma MNs"),
        (8, "پایانهٔ گل‌افشانی — group II"),
        (9, "کلاژن و پایانهٔ — Ib afferent"),
        (10, "قوس کشش — monosynaptic"),
        (11, "بازداری بازگشتی — disynaptic"),
    ]
    b.append(rect(20, 492, 864, 152, fill="#ffffff", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(870, 516, "راهنمای شماره‌ها", size=11.5, fill=ROSE, anchor="end", weight="700"))
    b.append(line(34, 524, 870, 524, stroke=ROSE_L, sw=1.0))
    for i, (n, text) in enumerate(items):
        c, r = i // 4, i % 4
        bx = 870 - c * 288
        by = 550 + r * 26
        b.append(badge(n, bx - 12, by - 5, r=10.5, fill=ROSE, size=11))
        b.append(txt(bx - 28, by, text, size=10.5, fill=INK, anchor="end"))
    return svg(W, H, "".join(b), """
    <linearGradient id="musG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fdba74"/><stop offset="0.55" stop-color="#f97316"/>
      <stop offset="1" stop-color="#c2410c"/></linearGradient>""")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "figs", "fig4.svg")
    save(out, plate())
    print("wrote", out)
