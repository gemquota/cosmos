"""Shared design system + helpers for COSMOS diagram generation."""

# ── Palette ────────────────────────────────────────────────────────────
BG      = "#0b1120"
PANEL   = "#0f172a"
BORDER  = "#1e293b"
BORDER2 = "#334155"
TEXT    = "#e2e8f0"
TEXT2   = "#94a3b8"
TEXT3   = "#64748b"
TEXT4   = "#475569"
RSIS    = "#818cf8"   # indigo
MYKB    = "#22d3ee"   # cyan
SPACE   = "#f59e0b"   # amber
DASH    = "#10b981"   # green
EXT     = "#f472b6"   # pink
GRAY    = "#475569"
FONT    = "system-ui,sans-serif"
MONO    = "ui-monospace,Menlo,monospace"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

DEFS = """<defs>
  <radialGradient id="bgGrad" cx="50%" cy="50%" r="75%">
    <stop offset="0%" stop-color="#111827"/><stop offset="100%" stop-color="#0b1120"/>
  </radialGradient>
  <linearGradient id="rGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#818cf8"/><stop offset="100%" stop-color="#6366f1"/></linearGradient>
  <linearGradient id="mGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#06b6d4"/></linearGradient>
  <linearGradient id="sGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#d97706"/></linearGradient>
  <linearGradient id="dGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#10b981"/><stop offset="100%" stop-color="#059669"/></linearGradient>
  <linearGradient id="hGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#f472b6"/><stop offset="100%" stop-color="#ec4899"/></linearGradient>
  <filter id="shadow"><feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#000" flood-opacity=".5"/></filter>
  <marker id="arwR" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 L2,4Z" fill="#818cf8"/></marker>
  <marker id="arwM" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 L2,4Z" fill="#22d3ee"/></marker>
  <marker id="arwS" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 L2,4Z" fill="#f59e0b"/></marker>
  <marker id="arwD" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 L2,4Z" fill="#10b981"/></marker>
  <marker id="arwH" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 L2,4Z" fill="#f472b6"/></marker>
  <marker id="arwG" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 L2,4Z" fill="#475569"/></marker>
</defs>"""

def svg_start(w, h, title, subtitle):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
{DEFS}
<rect width="{w}" height="{h}" fill="url(#bgGrad)"/>
<text x="{w/2}" y="40" text-anchor="middle" fill="{TEXT}" font-family="{FONT}" font-size="24" font-weight="700" letter-spacing="1">{esc(title)}</text>
<text x="{w/2}" y="62" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="12.5">{esc(subtitle)}</text>
<line x1="{w*0.06}" y1="76" x2="{w*0.94}" y2="76" stroke="{BORDER}" stroke-width="1"/>
"""

def svg_end(w, footer="COSMOS — Architecture Diagrams • Generated from source analysis"):
    return f"""<text x="{w/2}" y="{footer_y(w)}" text-anchor="middle" fill="#334155" font-family="{FONT}" font-size="9.5">{esc(footer)}</text>
</svg>"""

def footer_y(w):
    return 930 if w >= 1600 else (890 if w >= 1400 else 840)

def panel(x, y, w, h, accent, title, rows, header_h=32, pad=14, line_h=17, title_size=13, rx=10):
    """rows: list of (color, size, text) or (color, size, text, font)"""
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1" filter="url(#shadow)"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{header_h}" rx="{rx}" fill="{accent}" opacity=".16"/>',
        f'<rect x="{x}" y="{y+header_h-12}" width="{w}" height="12" fill="{accent}" opacity=".12"/>',
        f'<text x="{x+w/2}" y="{y+header_h/2+4.5}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="{title_size}" font-weight="700">{esc(title)}</text>',
    ]
    ty = y + header_h + pad
    for row in rows:
        color, size, text = row[0], row[1], row[2]
        font = row[3] if len(row) > 3 else FONT
        out.append(f'<text x="{x+pad}" y="{ty}" fill="{color}" font-family="{font}" font-size="{size}">{esc(text)}</text>')
        ty += line_h
    return "\n".join(out)

def chip(x, y, text, color, size=10, h=20):
    w = 12 + len(text) * (size * 0.58)
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="{h/2}" fill="{color}" opacity=".13"/>'
            f'<text x="{x + w/2:.0f}" y="{y + h/2 + 3.5}" text-anchor="middle" fill="{color}" font-family="{FONT}" font-size="{size}" font-weight="600">{esc(text)}</text>')

def arrow(x1, y1, x2, y2, color, marker=None, width=2.5, dashed=False, curve=None, opacity=0.85):
    m = f"url(#{marker})" if marker else ""
    dash = ' stroke-dasharray="6,4"' if dashed else ""
    if curve:
        d = f'M {x1} {y1} C {curve[0]} {curve[1]}, {curve[2]} {curve[3]}, {x2} {y2}'
        return f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="none" opacity="{opacity}"{dash} marker-end="{m}"/>'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" opacity="{opacity}"{dash} marker-end="{m}"/>'

def label(x, y, text, size=10, color=TEXT3, anchor="middle", italic=False, font=FONT):
    it = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{color}" font-family="{font}" font-size="{size}"{it}>{esc(text)}</text>'

def box(x, y, w, h, accent, title, subtitle=None, icon=None, title_size=15, stroke_w=2, rx=14, header_h=40):
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{PANEL}" stroke="{accent}" stroke-width="{stroke_w}" filter="url(#shadow)"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{header_h}" rx="{rx}" fill="{accent}" opacity=".18"/>',
        f'<rect x="{x}" y="{y+header_h-12}" width="{w}" height="12" fill="{accent}" opacity=".14"/>',
    ]
    tx = x + w/2
    if icon:
        out.append(f'<circle cx="{x+30}" cy="{y+header_h/2}" r="13" fill="{accent}" opacity=".32"/>')
        out.append(f'<text x="{x+30}" y="{y+header_h/2+5}" text-anchor="middle" fill="{TEXT}" font-size="13">{icon}</text>')
        tx = x + w/2 + 14
    out.append(f'<text x="{tx}" y="{y+header_h/2+5}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="{title_size}" font-weight="700">{esc(title)}</text>')
    if subtitle:
        out.append(f'<text x="{x+w/2}" y="{y+header_h+20}" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="11.5">{esc(subtitle)}</text>')
    return "\n".join(out)

def body_text(x, y, lines, line_h=17, pad=0):
    out = []
    ty = y
    for color, size, text in lines:
        out.append(f'<text x="{x+pad}" y="{ty}" fill="{color}" font-family="{FONT}" font-size="{size}">{esc(text)}</text>')
        ty += line_h
    return "\n".join(out)

def two_line(sub):
    parts = sub.split("\n")
    if len(parts) >= 2:
        return parts[0], parts[1]
    return parts[0], ""

def screen_hex(c1, c2):
    """screen blend of two hex colours → overlap colour"""
    def ch(h):
        return int(h[1:3], 16) / 255, int(h[3:5], 16) / 255, int(h[5:7], 16) / 255
    a, b = ch(c1), ch(c2)
    out = [min(255, round((1 - (1 - x) * (1 - y)) * 255)) for x, y in zip(a, b)]
    return "#" + "".join(f"{v:02x}" for v in out)
