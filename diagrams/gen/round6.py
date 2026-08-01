"""Round 6 shared helpers — portrait 1000x1320, mobile-first, viewBox-only.

Every diagram is a vertical composition: header band (0-76), body
(100-1000), legend (>=1080), footer notes (1278/1300). Animations are
only used where they encode a real cadence or flow, and each animated
diagram's legend states what the motion means.
"""
import math
from design import *

W, H = 1000, 1320


def doc(title, subtitle):
    return svg_start(W, H, title, subtitle)


def end(note):
    return (f'<text x="{W/2}" y="1278" text-anchor="middle" fill="{TEXT4}" '
            f'font-family="{FONT}" font-size="9.5" font-style="italic">{esc(note)}</text>\n'
            f'<text x="{W/2}" y="1300" text-anchor="middle" fill="#334155" font-family="{FONT}" font-size="9.5">'
            f'COSMOS — Architecture Diagrams • Round 6 · the doubling pass</text>\n</svg>')


def sect(x, y, w, accent, title, sub=None, h=42):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{accent}" opacity=".14" stroke="{accent}" stroke-width="1" stroke-opacity=".35"/>',
         f'<text x="{x+16}" y="{y+h/2+4}" fill="{accent}" font-family="{FONT}" font-size="12.5" font-weight="700">{esc(title)}</text>']
    if sub:
        s.append(f'<text x="{x+w-16}" y="{y+h/2+4}" text-anchor="end" fill="{TEXT4}" font-family="{FONT}" font-size="9">{esc(sub)}</text>')
    return "\n".join(s)


def legend(rows, title="READING THIS DIAGRAM", x=60, w=880, accent=EXT, line_h=17, pad=12):
    h = 30 + pad + line_h * len(rows)
    y = 1264 - h
    return panel(x, y, w, h, accent, title, rows, header_h=28, pad=pad, line_h=line_h)


def polar(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc(cx, cy, r, a0, a1, color, width=2, dashed=False, opacity=0.8, marker=None):
    x0, y0 = polar(cx, cy, r, a0)
    x1, y1 = polar(cx, cy, r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    m = f"url(#{marker})" if marker else ""
    dash = ' stroke-dasharray="6,4"' if dashed else ""
    return (f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}" '
            f'fill="none" stroke="{color}" stroke-width="{width}" opacity="{opacity}"{dash} marker-end="{m}"/>')


def ring(cx, cy, r0, r1, items, start=90, label_r=None, font=10.5):
    """items: (name, color, sub) — one arc segment per item around a ring.
    Arcs are laid out clockwise from 12 o'clock. Segments are separated by
    small gaps; each carries its own colour and a labelled mid-point."""
    out = []
    n = len(items)
    seg = 360.0 / n
    gap = 6.0
    lr = label_r if label_r else (r0 + r1) / 2
    for i, (name, color, sub) in enumerate(items):
        a0 = start + i * seg + gap / 2
        a1 = start + (i + 1) * seg - gap / 2
        out.append(arc(cx, cy, (r0 + r1) / 2, a0, a1, color, width=r1 - r0, opacity=0.5))
        mx, my = polar(cx, cy, lr, (a0 + a1) / 2)
        out.append(f'<text x="{mx}" y="{my+3.5}" text-anchor="middle" fill="{TEXT}" font-family="{FONT}" font-size="{font}" font-weight="700">{esc(name)}</text>')
        if sub:
            sx, sy = polar(cx, cy, r1 + 18, (a0 + a1) / 2)
            out.append(f'<text x="{sx}" y="{sy+3}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(sub)}</text>')
    return "\n".join(out)


def timeline(x0, x1, y, events, rail=BORDER2, size=11, sub_size=8):
    """events: (label, sub, color) laid out left→right on a horizontal rail."""
    out = [f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{rail}" stroke-width="1.5"/>']
    n = len(events)
    gap = (x1 - x0) / (n - 1)
    for i, (lab, sub, color) in enumerate(events):
        cx = x0 + gap * i
        out.append(f'<circle cx="{cx:.0f}" cy="{y}" r="6.5" fill="{color}" stroke="#0b1120" stroke-width="1.5"/>')
        out.append(label(cx, y - 15, lab, size, TEXT2))
        if sub:
            out.append(label(cx, y + 25, sub, sub_size, TEXT4))
    return "\n".join(out)


def matrix(x, y, row_labels, col_labels, cells, cell_w=118, cell_h=32, header_h=34, accent=EXT, gutter=150):
    """cells: (row, col, text, color) — ownership / read-write matrices."""
    out = []
    gx = x - gutter
    tw = gutter + len(col_labels) * cell_w
    out.append(f'<rect x="{gx}" y="{y}" width="{tw}" height="{header_h}" rx="8" fill="{accent}" opacity=".12" stroke="{BORDER2}"/>')
    out.append(f'<text x="{gx + 10}" y="{y + header_h/2 + 4}" fill="{TEXT3}" font-family="{MONO}" font-size="8.5">{esc("module \\ component")}</text>')
    for c, lab in enumerate(col_labels):
        out.append(label(x + c * cell_w + cell_w / 2, y + header_h / 2 + 4, lab, 9.5, accent, font=MONO))
    for r, lab in enumerate(row_labels):
        ry = y + header_h + r * cell_h
        out.append(f'<rect x="{gx}" y="{ry}" width="{tw}" height="{cell_h}" fill="{PANEL}" stroke="{BORDER2}" stroke-width="0.7"/>')
        out.append(f'<text x="{gx + 10}" y="{ry + cell_h/2 + 3.5}" fill="{TEXT2}" font-family="{MONO}" font-size="8.5">{esc(lab)}</text>')
        out.append(f'<line x1="{x}" y1="{ry}" x2="{x}" y2="{ry + cell_h}" stroke="{BORDER2}" stroke-width="0.7"/>')
    for (r, c, text, color) in cells:
        cx = x + c * cell_w + cell_w / 2
        cy = y + header_h + r * cell_h + cell_h / 2
        out.append(f'<text x="{cx}" y="{cy+3.5}" text-anchor="middle" fill="{color}" font-family="{MONO}" font-size="8.5" font-weight="700">{esc(text)}</text>')
    return "\n".join(out)


def table(x, y, col_w, headers, rows, row_h=26, header_h=30, accent=EXT, mono_cols=(), col_colors=None):
    """rows: list of cell-tuples; a cell may be (text, color) or plain str."""
    out = []
    th = header_h
    out.append(f'<rect x="{x}" y="{y}" width="{sum(col_w)}" height="{th}" rx="8" fill="{accent}" opacity=".12" stroke="{BORDER2}"/>')
    cxx = x
    for i, htxt in enumerate(headers):
        out.append(label(cxx + col_w[i] / 2, y + th / 2 + 4, htxt, 9.5, accent, font=MONO))
        cxx += col_w[i]
    for r, row in enumerate(rows):
        ry = y + th + r * row_h
        out.append(f'<rect x="{x}" y="{ry}" width="{sum(col_w)}" height="{row_h}" fill="{PANEL}" stroke="{BORDER2}" stroke-width="0.7"/>')
        cxx = x
        for c, cell in enumerate(row):
            if isinstance(cell, tuple):
                txt, color = cell
            else:
                txt, color = cell, TEXT2
            font = MONO if c in mono_cols else FONT
            weight = ' font-weight="700"' if isinstance(cell, tuple) else ""
            out.append(f'<text x="{cxx+10}" y="{ry+row_h/2+3.5}" fill="{color}" font-family="{font}" font-size="8.5"{weight}>{esc(str(txt))}</text>')
            cxx += col_w[c]
    return "\n".join(out)


def stack(x, y, w, items, gap=46, ch=120):
    """Vertical stack of cards joined by arrows. items: (title, accent, lines)."""
    out = []
    n = len(items)
    for i, (title, accent, lines) in enumerate(items):
        ty = y + i * (ch + gap)
        out.append(panel(x, ty, w, ch, accent, title, lines, header_h=30, pad=12, line_h=19))
        if i < n - 1:
            out.append(arrow(x + w / 2, ty + ch + 4, x + w / 2, ty + ch + gap - 4, accent, "arwG", 2, opacity=0.6))
    return "\n".join(out)


def chiprow(x, y, items, gap=10, size=9.5, h=22):
    """items: (text, color) — a row of pill chips."""
    out = []
    cx = x
    for text, color in items:
        w = 14 + len(text) * (size * 0.58)
        out.append(f'<rect x="{cx}" y="{y}" width="{w:.0f}" height="{h}" rx="{h/2}" fill="{color}" opacity=".13" stroke="{color}" stroke-width="0.6" stroke-opacity=".4"/>')
        out.append(f'<text x="{cx + w/2:.0f}" y="{y + h/2 + 3.5}" text-anchor="middle" fill="{color}" font-family="{MONO}" font-size="{size}" font-weight="600">{esc(text)}</text>')
        cx += w + gap
    return "\n".join(out)
