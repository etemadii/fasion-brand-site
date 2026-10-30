# -*- coding: utf-8 -*-
"""Plate 2 — pressure -> channel -> generator potential -> nerve impulse (book fig. 2-1, p.20)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from svgkit import *

W, H = 900, 640
ORM = "url(#endG)"


def charges(b, x0, x1, y, sign, color, step=32):
    x = x0
    while x <= x1:
        b.append(latin(x, y, sign, size=14, fill=color, anchor="middle", weight="700",
                       style="normal"))
        x += step


def panel(b, cx, state):
    """state: 'rest' | 'bend' | 'ap' — longitudinal section of a mechanoreceptive ending."""
    top, bot = 208, 300
    left, right = cx - 106, cx + 106
    # connective-tissue sheath + gel over the ending
    b.append(rect(left - 14, top - 36, (right - left) + 28, 18, fill="#dbeafe",
                  stroke="#60a5fa", sw=1.0, rx=8, opacity=0.92))
    if state == "rest":
        b.append(txt(cx, top - 42, "پوشش بافت پیوندی و ژل", size=10.5, fill="#1d4ed8"))
    b.append(rect(left, top, right - left, bot - top, fill=ORM, stroke="#9a3412",
                  sw=1.2, rx=15))
    # membrane double line (top / bottom) + charges
    b.append(line(left + 4, top, right - 4, top, stroke="#c2410c", sw=3.0))
    b.append(line(left + 4, bot, right - 4, bot, stroke="#c2410c", sw=3.0))
    charges(b, left + 16, right - 16, top - 8, "+", "#b91c1c")
    charges(b, left + 16, right - 16, bot + 18, "+", "#b91c1c")
    charges(b, left + 16, right - 16, top + 24, "-", "#1d4ed8")
    charges(b, left + 16, right - 16, bot - 26, "-", "#1d4ed8")

    # stretch-gated channel through the upper membrane
    gx = cx
    b.append(rect(gx - 21, top - 16, 14, 32, fill="#eff6ff", stroke=BLUE, sw=1.5, rx=2.5))
    b.append(rect(gx + 7, top - 16, 14, 32, fill="#eff6ff", stroke=BLUE, sw=1.5, rx=2.5))
    if state == "rest":
        b.append(line(gx - 7, top + 1, gx + 7, top + 1, stroke=BLUE, sw=2.4))
    else:
        b.append(line(gx - 8, top - 6, gx + 8, top + 7, stroke=BLUE, sw=2.2))
        b.append(line(gx - 8, top + 7, gx + 8, top - 6, stroke=BLUE, sw=2.2))

    # pressure arrow
    if state != "rest":
        b.append(cpath_arrow(f"M {cx} 132 q 0,24 0,44", color="#dc2626", sw=2.8))
        b.append(txt(cx - 10, 150, "فشار", size=12, fill="#dc2626", anchor="end",
                     weight="700"))
    # Na+ entering
    if state == "ap":
        for dx in (-8, 0, 8):
            b.append(cpath_arrow(f"M {cx+dx} {top-30} q 0,12 0,20", color=TEAL, sw=1.5))
        for dx, dy in ((-40, 46), (30, 54), (-4, 62)):
            b.append(circle(cx + dx, top + dy, 5.6, fill="#ccfbf1", stroke=TEAL, sw=1.2))
            b.append(latin(cx + dx, top + dy + 3.2, "Na", size=7.2, fill=TEAL,
                           anchor="middle", style="normal", weight="700"))

    # axon leaving towards the CNS
    ax = right
    b.append(path(f"M {ax} {top+44} q 22,8 30,34", fill="none", stroke="#7c2d12", sw=9,
                  extra='stroke-linecap="round"'))
    b.append(path(f"M {ax} {top+44} q 22,8 30,34", fill="none", stroke="#fdba74", sw=4,
                  extra='stroke-linecap="round"'))
    if state == "ap":
        b.append(path(f"M {ax+18} {top+66} l 6,-11 l 6,11", fill="none", stroke=ROSE, sw=2.0))
        b.append(txt(cx, bot + 40, "پیام عصبی به دستگاه عصبی مرکزی", size=10, fill=INK_SOFT))



def graded_graph(b):
    x0, y0, w, h = 44, 372, 392, 244
    b.append(txt(x0 + w / 2, y0 - 12, "پتانسیل مولد (گیرنده): دامنهٔ درجه‌بندی‌شده", size=12.5,
                 fill=ROSE, weight="700"))
    b.append(rect(x0, y0, w, h, fill="#fffaf6", stroke="#f6d6cc", sw=1.0, rx=8))
    base = y0 + h - 70
    b.append(line(x0 + 34, base, x0 + w - 16, base, stroke=INK_SOFT, sw=1.3))
    b.append(line(x0 + 34, y0 + 18, x0 + 34, base, stroke=INK_SOFT, sw=1.3))
    b.append(latin(x0 + 28, y0 + 30, "Vm", size=10, fill=INK_SOFT, anchor="end"))
    b.append(txt(x0 + w - 18, base + 18, "زمان ←", size=10.5, fill=INK_SOFT, anchor="end"))
    b.append(txt(x0 + 44, y0 + 30, "بدون آستانه · بدون دورهٔ مقاوم · جمع‌پذیر", size=10.5,
                 fill=INK_SOFT, anchor="start"))
    data = [(56, 22, 12), (166, 48, 26), (276, 92, 40)]
    for sx, amp, bar in data:
        x = x0 + sx
        d = (f"M {x} {base} Q {x+10} {base-amp*0.72:.1f} {x+24} {base-amp} "
             f"Q {x+58} {base-amp*0.16:.1f} {x+112} {base}")
        b.append(path(d, stroke=ROSE, sw=2.4))
        b.append(circle(x + 24, base - amp, 2.8, fill=ROSE, stroke="none"))
        b.append(rect(x, base + 12, 46, bar, fill="#e0f2fe", stroke="#0ea5e9", sw=0.9, rx=2))
    b.append(txt(x0 + 44, base + 58, "محرک", size=10, fill="#0284c7", anchor="start"))
    b.append(txt(x0 + w - 18, y0 + h - 10, "دپلاریزاسیون موضعی، کاهش با فاصله", size=9.5,
                 fill=MUTED, anchor="end"))


def spike_graph(b):
    x0, y0, w, h = 470, 372, 396, 244
    b.append(txt(x0 + w / 2, y0 - 12, "عصب: کدگذاری شدت با بسامد", size=12.5, fill=TEAL,
                 weight="700"))
    rows = [(y0 + 56, 3, "محرک ضعیف"), (y0 + 116, 6, "محرک متوسط"), (y0 + 176, 10, "محرک شدید")]
    for y, n, cap in rows:
        b.append(line(x0 + 16, y, x0 + w - 16, y, stroke="#cbd5e1", sw=1.0))
        for k in range(n):
            sx = x0 + 24 + k * (w - 60) / n
            b.append(path(f"M {sx} {y} l 6,-17 l 6,17 l 4,-7 l 7,0", fill="none",
                          stroke=TEAL, sw=1.7))
        b.append(txt(x0 + 16, y - 26, cap, size=10, fill=INK_SOFT, anchor="start"))
    b.append(txt(x0 + w / 2, y0 + 214,
                 "شدت بیشتر ← بسامد بیشتر (دامنهٔ پیام عصبی ثابت می‌ماند)",
                 size=10.5, fill=INK_SOFT))


def plate():
    b = []
    b.append(txt(16, 30, "شکل ۱ — مولد پیام عصبی در یک گیرندهٔ مکانیکی", size=15, fill=INK,
                 anchor="start", weight="700"))
    b.append(txt(884, 30, "فشار ← کشش غشا ← باز شدن کانال ← پتانسیل مولد ← پیام عصبی",
                 size=11, fill=INK_SOFT, anchor="end"))
    titles = [(152, "الف", "استراحت: کانال بسته", "اختلاف پتانسیل غشا پایدار"),
              (452, "ب", "فشار مکانیکی: کانال باز", "کشش لیپیدهای غشا ← دروازه باز"),
              (752, "پ", "دپلاریزاسیون: پتانسیل مولد", "عبور از آستانه ← پیام عصبی")]
    for cx, letter, t1, t2 in titles:
        b.append(tag(cx - 44, 48, 88, 28, f"({letter})", fill=ROSE_L, stroke=ROSE,
                     color=ROSE, size=13))
        b.append(txt(cx, 98, t1, size=12, fill=INK, weight="700"))
        b.append(txt(cx, 116, t2, size=10.5, fill=INK_SOFT))
    for cx, letter, _, _ in titles:
        panel(b, cx, {"الف": "rest", "ب": "bend", "پ": "ap"}[letter])
    graded_graph(b)
    spike_graph(b)
    return svg(W, H, "".join(b), """
    <linearGradient id="endG" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fdba74"/><stop offset="0.5" stop-color="#f97316"/>
      <stop offset="1" stop-color="#ea580c"/></linearGradient>""")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "figs", "fig2.svg")
    save(out, plate())
    print("wrote", out)
