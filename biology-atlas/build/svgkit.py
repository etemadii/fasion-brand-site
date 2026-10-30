# -*- coding: utf-8 -*-
"""svgkit — tiny helper kit for the annotated SVG plates of the Senses Atlas.

Everything is plain string building: each plate script imports this module,
composes a body string, and calls svg() to wrap it.
"""

INK      = "#12232e"
INK_SOFT = "#3d5563"
MUTED    = "#7b8f9b"
LINE     = "#c9d5dc"
TEAL     = "#0f766e"
TEAL_L   = "#e4f2ef"
ROSE     = "#be185d"
ROSE_L   = "#fce7f3"
AMBER    = "#b45309"
AMBER_L  = "#fdf3e3"
BLUE     = "#1d4ed8"
BLUE_L   = "#e8eefe"
GREEN    = "#15803d"
PAPER    = "#ffffff"

FA = "۰۱۲۳۴۵۶۷۸۹"

# The plates are drawn on a 900-unit canvas that is printed at ≈584 px (154 mm).
# Everything below 11 units would drop under ~7 pt on paper, so it is scaled up.
MIN_READ = 10.5
MIN_SCALE = 1.15


def fa(n):
    """Latin number -> Persian digits (keeps separators)."""
    return "".join(FA[int(c)] if c.isdigit() else c for c in str(n))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=15, fill=INK, anchor="middle", weight="400",
        family="Noto Sans Arabic", opacity=1.0, extra=""):
    if size < MIN_READ:
        size = size * MIN_SCALE
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'font-family="{family}" font-weight="{weight}" text-anchor="{anchor}" '
            f'opacity="{opacity}" {extra}>{esc(s)}</text>')


def latin(x, y, s, size=13, fill=INK_SOFT, anchor="middle", weight="400", style="italic"):
    """Latin / numeric snippet that must stay LTR (units, gene names, Hz...)."""
    if size < MIN_READ:
        size = size * MIN_SCALE
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'font-family="DejaVu Sans" font-weight="{weight}" text-anchor="{anchor}" '
            f'font-style="{style}" direction="ltr">{esc(s)}</text>')


def rect(x, y, w, h, fill="none", stroke=LINE, sw=1.2, rx=0, opacity=1.0, extra=""):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}" {extra}/>')


def line(x1, y1, x2, y2, stroke=INK, sw=1.2, dash=None, cap="round", opacity=1.0, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d} '
            f'opacity="{opacity}" {extra}/>')


def path(d, fill="none", stroke=INK, sw=1.2, dash=None, opacity=1.0, extra=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round"{da} opacity="{opacity}" {extra}/>')


def circle(cx, cy, r, fill="none", stroke=INK, sw=1.2, opacity=1.0, extra=""):
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}" {extra}/>')


def ellipse(cx, cy, rx, ry, fill="none", stroke=INK, sw=1.2, opacity=1.0, extra="",
            dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{d} {extra}/>')


def poly(points, fill="none", stroke=INK, sw=1.2, opacity=1.0, extra=""):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return (f'<polyline points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round" opacity="{opacity}" {extra}/>')


def polygon(points, fill="none", stroke=INK, sw=1.2, opacity=1.0, extra=""):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return (f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" opacity="{opacity}" {extra}/>')


def group(body, extra=""):
    return f"<g {extra}>{body}</g>"


# --------------------------------------------------------------------------
# annotation layer: numbered pins (like a real anatomical plate)
# --------------------------------------------------------------------------

def badge(n, x, y, r=12.5, fill=ROSE, color="#ffffff", size=14):
    """Numbered callout disc."""
    return (circle(x, y, r, fill=fill, stroke="#ffffff", sw=1.8)
            + txt(x, y + size * 0.36, fa(n), size=size, fill=color, weight="700"))


def pin(n, ax, ay, tx, ty, label, anchor="end", color=ROSE, tx_pad=10,
        size=14.5, label_fill=INK, dash="3 3"):
    """A numbered disc at (ax,ay), a leader to target (tx,ty), and the label text.

    anchor='end'  -> label sits left of the disc
    anchor='start'-> label sits right of the disc
    """
    out = []
    out.append(line(ax, ay, tx, ty, stroke=color, sw=1.15, dash=dash, opacity=0.85))
    out.append(circle(tx, ty, 3.4, fill=color, stroke="#ffffff", sw=1.2))
    out.append(badge(n, ax, ay, fill=color))
    lx = ax - tx_pad if anchor == "end" else ax + tx_pad
    out.append(txt(lx, ay + size * 0.36, label, size=size, fill=label_fill, anchor=anchor))
    return "".join(out)


def tag(x, y, w, h, text, fill=TEAL_L, stroke=TEAL, color=TEAL, size=13.5, weight="600", rx=6):
    return (rect(x, y, w, h, fill=fill, stroke=stroke, sw=1.1, rx=rx)
            + txt(x + w / 2, y + h / 2 + size * 0.36, text, size=size, fill=color,
                  weight=weight))


def arrow(x1, y1, x2, y2, color=ROSE, sw=2.0, dash=None, head="url(#ah)"):
    return line(x1, y1, x2, y2, stroke=color, sw=sw, dash=dash,
                extra=f'marker-end="{head}"')


def cpath_arrow(d, color=ROSE, sw=2.0, dash=None, head="url(#ah)"):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round"{da} marker-end="{head}"/>')


def defs(extra=""):
    return f"""<defs>
  <marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6"
          orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker>
  <marker id="ahT" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6"
          orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{TEAL}"/></marker>
  <marker id="ahB" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6"
          orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>
  <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
    <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0b1b22" flood-opacity="0.28"/>
  </filter>
  <filter id="soft2" x="-30%" y="-30%" width="160%" height="160%">
    <feDropShadow dx="0" dy="1.5" stdDeviation="1.6" flood-color="#0b1b22" flood-opacity="0.22"/>
  </filter>
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="7" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="a"><feFuncA type="linear" slope="0.22"/></feComponentTransfer>
    <feComposite in="a" in2="SourceGraphic" operator="in" result="ga"/>
    <feBlend in="SourceGraphic" in2="ga" mode="multiply"/>
  </filter>
  {extra}
</defs>"""


def svg(w, h, body, extra_defs="", bg=PAPER, cls="plate"):
    # direction="ltr" keeps text-anchor semantics independent of the page dir=rtl,
    # so the plates look identical in the atlas and in isolation.
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="100%" '
            f'preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" '
            f'direction="ltr" role="img">\n{defs(extra_defs)}\n'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>\n{body}\n</svg>\n')


def save(path, content):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return path

