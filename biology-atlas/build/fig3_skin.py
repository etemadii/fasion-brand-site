# -*- coding: utf-8 -*-
"""Plate 3 — cutaneous receptors (book fig. 2-2, p.21) + acuity and fibre-speed insets."""
import os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from svgkit import *

W, H = 900, 690
SKIN_L, SKIN_R = 20, 556
EPI_TOP, EPI_BOT, DERM_BOT, FAT_BOT = 78, 148, 330, 412


def skin_block(b):
    # epidermis
    b.append(rect(SKIN_L, EPI_TOP, SKIN_R - SKIN_L, EPI_BOT - EPI_TOP, fill="#fde8d7",
                  stroke="#e7b58f", sw=1.0, rx=4))
    for k in range(5):  # stratum corneum waves
        y = EPI_TOP + 4 + k * 9
        b.append(path(f"M {SKIN_L+4} {y} q 40,5 80,0 q 40,-5 80,0 q 40,5 80,0 q 40,-5 80,0 "
                      f"q 40,5 80,0 q 40,-5 80,0", stroke="#e9c6ac", sw=1.0, opacity=0.8))
    b.append(rect(SKIN_L, EPI_BOT, SKIN_R - SKIN_L, DERM_BOT - EPI_BOT, fill="#fbe3d2",
                  stroke="none"))
    # dermal papillae (wavy border)
    d = f"M {SKIN_L+4} {EPI_BOT} "
    x = SKIN_L + 4
    while x < SKIN_R - 30:
        d += f"q 15,12 30,0 q 15,-12 30,0 "
        x += 60
    b.append(path(d, stroke="#d69a6c", sw=1.6))
    b.append(rect(SKIN_L, DERM_BOT, SKIN_R - SKIN_L, FAT_BOT - DERM_BOT, fill="#fdf2e0",
                  stroke="none"))
    # fat lobules
    rnd = random.Random(5)
    for i in range(26):
        cx = rnd.uniform(SKIN_L + 14, SKIN_R - 24)
        cy = rnd.uniform(DERM_BOT + 12, FAT_BOT - 12)
        b.append(ellipse(cx, cy, rnd.uniform(9, 17), rnd.uniform(6, 11), fill="#fff8ea",
                         stroke="#ecd9b6", sw=0.9))
    # collagen texture in dermis
    for i in range(60):
        x1 = rnd.uniform(SKIN_L + 6, SKIN_R - 20)
        y1 = rnd.uniform(EPI_BOT + 6, DERM_BOT - 6)
        b.append(line(x1, y1, x1 + rnd.uniform(-16, 22), y1 + rnd.uniform(-5, 5),
                      stroke="#f2cdb4", sw=0.8, opacity=0.7))
    b.append(rect(SKIN_L, EPI_TOP, SKIN_R - SKIN_L, FAT_BOT - EPI_TOP, fill="none",
                  stroke="#c89068", sw=1.4, rx=4))
    # layer labels
    b.append(txt(SKIN_R - 10, EPI_TOP + 18, "روپوست", size=11, fill="#9a3412", anchor="end",
                 weight="700"))
    b.append(txt(SKIN_R - 10, EPI_TOP + 32, "درم", size=11, fill="#9a3412",
                 anchor="end"))
    b.append(txt(SKIN_L + 12, DERM_BOT + 22, "بافت زیرپوستی و چربی", size=10.5, fill="#8a6a3a",
                 anchor="start"))
    b.append(txt(SKIN_L + 10, EPI_TOP + 16, "سطح پوست", size=10.5, fill="#8a5a3a",
                 anchor="start"))


def hair_and_glands(b):
    # hair follicle, oblique
    b.append(path(f"M 96 {EPI_TOP-6} q 18,60 34,120 q 8,34 -2,56", fill="none",
                  stroke="#a16207", sw=1.4))
    b.append(path(f"M 124 {EPI_TOP-6} q 14,58 26,118 q 6,30 -4,52", fill="none",
                  stroke="#a16207", sw=1.4))
    b.append(path(f"M 96 {EPI_TOP-6} q 18,60 34,120 q 8,34 -2,56", fill="none",
                  stroke="#facc15", sw=3.2, opacity=0.85))
    b.append(path(f"M 92 {EPI_TOP-4} q 20,64 36,124 q 8,36 -2,58", fill="none",
                  stroke="#f9a8d4", sw=7, opacity=0.55))
    b.append(ellipse(152, 322, 15, 11, fill="#fde68a", stroke="#a16207", sw=1.0))
    # arrector pili
    b.append(path(f"M 150 250 q 34,-16 44,-52", fill="none", stroke="#c2410c", sw=2.4))
    # sebaceous gland
    b.append(ellipse(74, 214, 15, 11, fill="#fef3c7", stroke="#b45309", sw=1.1))


def nerve(b, pts, color="#ea580c", sw=2.4):
    d = "M " + " L ".join(f"{x} {y}" for x, y in pts)
    b.append(path(d, fill="none", stroke=color, sw=sw, extra='stroke-linecap="round"'))


def receptors(b):
    # --- free nerve endings (nociceptor / thermo) : arborise into the epidermis
    for dx in (-16, 0, 16):
        b.append(path(f"M {206+dx*0.4} 196 q {dx*0.7},-24 {dx},-56", fill="none",
                      stroke="#7c3aed", sw=1.6))
        for k in range(3):
            b.append(circle(206 + dx + (k - 1) * 4, 140 - k * 8 - abs(dx) * 0.1, 1.7,
                            fill="#7c3aed", stroke="none"))
    b.append(latin(206, 118, "free", size=8.5, fill="#6d28d9", anchor="middle"))
    nerve(b, [(206, 196), (218, 300), (250, 400)], color="#7c3aed")

    # --- Merkel disc (basal epidermis, Piezo2, slowly adapting)
    b.append(ellipse(258, 152, 13, 8, fill="#fbbf24", stroke="#b45309", sw=1.2))
    b.append(latin(258, 176, "Merkel", size=8.5, fill="#92400e", anchor="middle"))
    nerve(b, [(258, 160), (262, 300), (270, 400)])

    # --- Meissner corpuscle (dermal papilla, rapid adapting, flutter)
    b.append(rect(308, 150, 26, 6, fill="#f9a8d4", stroke="#be185d", sw=1.0, rx=3))
    for k in range(3):
        b.append(ellipse(321, 160 + k * 9, 15, 5.5, fill="none", stroke="#be185d", sw=1.1))
    b.append(latin(321, 200, "Meissner", size=8.5, fill="#9d174d", anchor="middle"))
    nerve(b, [(321, 186), (316, 300), (300, 400)])

    # --- Pacinian corpuscle (deep, high-frequency vibration)
    for r in (26, 20, 14, 8):
        b.append(ellipse(392, 360, r, r * 0.8, fill="none" if r > 8 else "#fecaca",
                         stroke="#b91c1c", sw=1.2))
    b.append(latin(392, 400, "Pacinian", size=8.5, fill="#991b1b", anchor="middle"))
    nerve(b, [(366, 360), (330, 400)], color="#b91c1c")

    # --- Ruffini ending (stretch, slowly adapting)
    b.append(ellipse(486, 252, 26, 12, fill="#fca5a5", stroke="#b91c1c", sw=1.2))
    for k in range(4):
        b.append(line(464 + k * 4, 252, 508 - k * 4, 252, stroke="#b91c1c", sw=0.8))
    b.append(latin(486, 222, "Ruffini", size=8.5, fill="#991b1b", anchor="middle"))
    nerve(b, [(486, 264), (400, 400)])

    # --- hair-follicle receptor (GLO) : spiral around the follicle
    for k in range(5):
        b.append(path(f"M {110+k*3} {196+k*16} q 34,-4 40,10", fill="none", stroke="#ca8a04",
                      sw=1.4, opacity=0.9))
    # nerve trunk leaving the skin
    nerve(b, [(250, 404), (330, 424), (430, 438), (556, 446)], color="#f97316", sw=4.5)
    b.append(txt(548, 462, "تنهٔ عصب حسی", size=10, fill="#9a3412", anchor="end"))


def acuity_card(b):
    x0, y0, w, h = 570, 24, 314, 176
    b.append(rect(x0, y0, w, h, fill="#f9fbfc", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x0 + w - 12, y0 + 24, "دقت مکانی: آزمون دو نقطه (میلی‌متر)", size=11.5,
                 fill=TEAL, anchor="end", weight="700"))
    rows = [("نوک انگشت", 2), ("کف دست", 10), ("ساعد", 35), ("پشت", 45)]
    y = y0 + 48
    for name, mm in rows:
        b.append(txt(x0 + w - 12, y + 4, name, size=10, fill=INK_SOFT, anchor="end"))
        length = 12 + mm * 2.1
        b.append(rect(x0 + 96, y - 5, length, 12, fill="#ccfbf1", stroke=TEAL, sw=0.9, rx=3))
        b.append(txt(x0 + 96 + length + 7, y + 5, fa(mm), size=9.5, fill=TEAL,
                     anchor="end", weight="700"))
        y += 30


def speed_card(b):
    x0, y0, w, h = 570, 212, 314, 150
    b.append(rect(x0, y0, w, h, fill="#f9fbfc", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x0 + w - 12, y0 + 24, "سرعت هدایت فیبر (متر بر ثانیه)", size=11.5,
                 fill=ROSE, anchor="end", weight="700"))
    rows = [("Aβ", "30 - 70", 70), ("Aδ", "5 - 30", 30), ("C", "0.5 - 2", 4)]
    y = y0 + 50
    for name, val, v in rows:
        b.append(txt(x0 + 44, y + 4, name, size=10.5, fill=INK, anchor="middle", weight="700"))
        b.append(rect(x0 + 66, y - 5, max(6, v * 2.3), 12,
                      fill=ROSE_L if name == "C" else "#fbcfe8", stroke=ROSE, sw=0.9, rx=3))
        b.append(latin(x0 + 74 + max(6, v * 2.3), y + 4, val, size=9, fill=ROSE,
                       anchor="start", style="normal"))
        y += 32


def tuning_card(b):
    x0, y0, w, h = 570, 376, 314, 140
    b.append(rect(x0, y0, w, h, fill="#f9fbfc", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x0 + w - 12, y0 + 24, "پنجرهٔ بسامدی گیرنده‌ها (هرتز)", size=11.5,
                 fill=AMBER, anchor="end", weight="700"))
    ax0, ax1, ay = x0 + 16, x0 + w - 16, y0 + 112

    def X(f):
        import math
        return ax0 + (math.log10(f) + 1) / 4 * (ax1 - ax0)

    b.append(line(ax0, ay, ax1, ay, stroke=INK_SOFT, sw=1.2))
    for f, lab in [(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")]:
        b.append(line(X(f), ay - 4, X(f), ay + 4, stroke=INK_SOFT, sw=1.0))
        b.append(latin(X(f), ay + 16, lab, size=8.5, fill=INK_SOFT, anchor="middle"))
    bands = [("Merkel", 0.4, 3, TEAL, -58), ("Meissner", 5, 50, ROSE, -38),
             ("Pacinian", 150, 400, "#b91c1c", -18)]
    for name, f1, f2, color, dy in bands:
        b.append(rect(X(f1), ay + dy, X(f2) - X(f1), 12, fill="none", stroke=color, sw=1.4,
                      rx=6))
        b.append(latin(X((f1 + f2) / 2), ay + dy - 5, name, size=8, fill=color,
                       anchor="middle"))

    b.append(ellipse(60, 226, 11, 9, fill="#fef3c7", stroke="#b45309", sw=1.1))
    # eccrine sweat gland (coiled) + duct
    b.append(path("M 502 156 q -6,60 -10,110", fill="none", stroke="#38bdf8", sw=5,
                  opacity=0.85))
    for k in range(4):
        b.append(ellipse(494, 286 + k * 9, 14 - k, 6, fill="none", stroke="#38bdf8", sw=2.2))
    b.append(path("M 494 320 q -10,14 -4,26", fill="none", stroke="#38bdf8", sw=2.6))



def key_strip(b, items, x0, y0, x1, y1, cols=2):
    b.append(rect(x0, y0, x1 - x0, y1 - y0, fill="#ffffff", stroke=LINE, sw=1.1, rx=10))
    b.append(txt(x1 - 14, y0 + 24, "راهنمای شماره‌ها", size=12, fill=ROSE, anchor="end",
                 weight="700"))
    b.append(line(x0 + 14, y0 + 32, x1 - 14, y0 + 32, stroke=ROSE_L, sw=1.0))
    per = (len(items) + cols - 1) // cols
    colw = (x1 - x0 - 28) / cols
    for i, (n, text) in enumerate(items):
        c, r = i // per, i % per
        bx = x1 - 14 - c * colw
        by = y0 + 58 + r * 26
        b.append(badge(n, bx - 12, by - 5, r=10.5, fill=ROSE, size=11))
        b.append(txt(bx - 28, by, text, size=10.8, fill=INK, anchor="end"))


def plate():
    b = []
    b.append(txt(16, 30, "شکل ۲ — گیرنده‌های حسی پوست", size=15, fill=INK, anchor="start",
                 weight="700"))
    b.append(txt(884, 30, "هر گیرنده یک «خط برچسب‌دار» به مغز می‌فرستد", size=11,
                 fill=INK_SOFT, anchor="end"))
    skin_block(b)
    hair_and_glands(b)
    receptors(b)
    acuity_card(b)
    speed_card(b)
    tuning_card(b)

    on_plate = [
        (1, (44, 120), (74, 126)),
        (2, (508, 420), (534, 442)),
        (3, (150, 150), (196, 138)),
        (4, (300, 196), (268, 158)),
        (5, (350, 148), (330, 160)),
        (6, (392, 316), (392, 336)),
        (7, (486, 292), (486, 266)),
        (8, (76, 268), (116, 214)),
    ]
    for n, (bx, by), (tx, ty) in on_plate:
        b.append(line(bx, by, tx, ty, stroke=ROSE, sw=1.1, dash="3 3", opacity=0.9))
        b.append(circle(tx, ty, 3.0, fill=ROSE, stroke="#ffffff", sw=1.0))
        b.append(badge(n, bx, by, r=11.5, fill=ROSE, size=12))

    items = [
        (1, "روپوست: لایهٔ سدّی، بدون رگ"),
        (2, "تنهٔ عصب حسی و فیبرهای آوران"),
        (3, "پایانهٔ آزاد: درد و دما"),
        (4, "دیسک مرکل: فشار پایدار و لبه"),
        (5, "جسم مایسنر: لرزش ۵ تا ۵۰ هرتز"),
        (6, "جسم پاکینی: ارتعاش ۲۰۰ تا ۳۰۰ هرتز"),
        (7, "پایانهٔ رافینی: کشش پوست"),
        (8, "فولیکول مو و ماهیچهٔ راست‌کننده"),
    ]
    key_strip(b, items, 20, 540, 884, 684, cols=2)
    return svg(W, H, "".join(b))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "figs", "fig3.svg")
    save(out, plate())
    print("wrote", out)
