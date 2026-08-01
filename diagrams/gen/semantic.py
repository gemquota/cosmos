"""Semantic ontology diagrams — components and modules mapped onto
semantic/ontological spectra as overlapping sets.

  Basic    — the component ontology Venn · the system ontology field
  Advanced — MyKB ontology Venn · SPACE framework ontology
  Expert   — ontological spheres (3D) · evolution over time (4D)
"""
import math
from design import *


W, H = 1000, 1320
FOOT_Y = 1300


def open_doc(title, subtitle):
    return svg_start(W, H, title, subtitle)


def close_doc():
    return f'<text x="{W/2}" y="{FOOT_Y}" text-anchor="middle" fill="#334155" font-family="{FONT}" font-size="9.5">COSMOS — Architecture Diagrams • Generated from source analysis</text>\n</svg>'


def screen_hex(c1, c2):
    """screen blend of two hex colours"""
    def ch(h):
        return int(h[1:3], 16) / 255, int(h[3:5], 16) / 255, int(h[5:7], 16) / 255
    a, b = ch(c1), ch(c2)
    out = [min(255, round((1 - (1 - x) * (1 - y)) * 255)) for x, y in zip(a, b)]
    return "#" + "".join(f"{v:02x}" for v in out)


def vcircle(cx, cy, r, color, opacity=0.5, stroke_w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" fill-opacity="{opacity}" '
            f'stroke="{color}" stroke-width="{stroke_w}" style="mix-blend-mode:screen"{d}/>')


def pill(x, y, lines, anchor="middle", pad=9, line_h=14):
    """dark rounded label box centered at (x,y); lines: (text, size, color)"""
    widths = []
    total_h = pad * 2 + (len(lines) - 1) * line_h
    for t, s, _ in lines:
        widths.append(len(t) * s * 0.56)
    bw = max(widths) + pad * 2
    x0 = x - bw / 2 if anchor == "middle" else x
    y0 = y - total_h / 2 if anchor == "middle" else y
    out = [f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{bw:.0f}" height="{total_h}" rx="8" fill="#0b1120" opacity=".78"/>']
    ty = y0 + pad + 4.5
    for t, s, c in lines:
        out.append(f'<text x="{x0 + bw/2:.0f}" y="{ty:.0f}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="{s}" font-weight="600">{esc(t)}</text>')
        ty += line_h
    return "\n".join(out)


def axis_frame(x0, x1, y_top, y_bot, x_left, x_right, y_bottom_label, y_top_label, xticks=None, yticks=None):
    """horizontal + vertical semantic axes. x_left/right labels sit under the X axis;
    y labels are rotated along the Y axis. returns svg chunk."""
    out = [
        f'<line x1="{x0}" y1="{y_bot}" x2="{x1}" y2="{y_bot}" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)" opacity=".9"/>',
        f'<line x1="{x0}" y1="{y_bot}" x2="{x0}" y2="{y_top}" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)" opacity=".9"/>',
        f'<text x="{x1}" y="{y_bot+22}" text-anchor="end" fill="{TEXT2}" font-family="{FONT}" font-size="11.5" font-weight="700">{esc(x_right)}</text>',
        f'<text x="{x0}" y="{y_bot+22}" text-anchor="start" fill="{TEXT2}" font-family="{FONT}" font-size="11.5" font-weight="700">{esc(x_left)}</text>',
        f'<text x="{x0-26}" y="{(y_top+y_bot)/2}" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="11.5" font-weight="700" transform="rotate(-90 {x0-26} {(y_top+y_bot)/2})">{esc(y_bottom_label)} ⇄ {esc(y_top_label)}</text>',
    ]
    for tx, tl in (xticks or []):
        out.append(f'<line x1="{tx}" y1="{y_bot-5}" x2="{tx}" y2="{y_bot+5}" stroke="{BORDER2}" stroke-width="1"/>')
        out.append(f'<text x="{tx}" y="{y_bot+14}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="9">{esc(tl)}</text>')
    for ty, tl in (yticks or []):
        out.append(f'<line x1="{x0-5}" y1="{ty}" x2="{x0+5}" y2="{ty}" stroke="{BORDER2}" stroke-width="1"/>')
        out.append(f'<text x="{x0-12}" y="{ty+3}" text-anchor="end" fill="{TEXT4}" font-family="{FONT}" font-size="9">{esc(tl)}</text>')
    return "\n".join(out)


def size_legend(x, y, items, title="RADIUS ∝ √LOC"):
    """items: (radius, color, label)"""
    out = [f'<text x="{x}" y="{y}" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">{esc(title)}</text>']
    ty = y + 18
    for r, c, l in items:
        out.append(f'<circle cx="{x + max(r, 14)}" cy="{ty}" r="{max(r, 14)}" fill="{c}" fill-opacity=".45" stroke="{c}" stroke-width="1.4"/>')
        out.append(f'<text x="{x + max(r, 14) * 2 + 16}" y="{ty + 4}" fill="{TEXT2}" font-family="{FONT}" font-size="10">{esc(l)}</text>')
        ty += 40
    return "\n".join(out)


# ── B-08: The Component Ontology Venn ─────────────────────────────────
def component_ontology():
    s = [open_doc("THE COMPONENT ONTOLOGY VENN",
                  "Three components as overlapping sets in semantic space — position, radius, and hue encode ontological spectra")]
    x0, x1, y_top, y_bot = 180, 820, 200, 1050
    s.append(axis_frame(x0, x1, y_top, y_bot, "REAL-TIME · seconds", "LONG-TERM · months", "EXECUTION", "THEORY",
                        xticks=[(280, "sec"), (460, "min"), (640, "hr"), (800, "days+")],
                        yticks=[(330, "strategy"), (500, "ideation"), (680, "action"), (860, "tool calls")]))
    # quadrant hints
    s.append(label(275, 1030, "ACTION plane", 9, TEXT4, italic=True))
    s.append(label(720, 1030, "MEMORY plane", 9, TEXT4, italic=True))
    s.append(label(275, 228, "IDEATION plane", 9, TEXT4, italic=True))
    s.append(label(720, 228, "STRATEGY plane", 9, TEXT4, italic=True))

    # circles (x, y, r): radius ≈ sqrt(LOC)/1.35 — 67k / 103k / 69k
    rsis = (280, 500, 195, RSIS, "RSIS3 · CORE ENGINE", "67k LOC · L1→L3 loops · evaluator · telemetry")
    space = (450, 310, 185, SPACE, "SPACE · IDEATION", "69k LOC · 326 probes · 7 series · 6 exports")
    mykb = (660, 560, 240, MYKB, "MYKB · MEMORY", "103k LOC · 2,360+ pages · graph · temporal engine")
    s.append(vcircle(mykb[0], mykb[1], mykb[2], mykb[3], opacity=0.5))
    s.append(vcircle(space[0], space[1], space[2], space[3], opacity=0.5))
    s.append(vcircle(rsis[0], rsis[1], rsis[2], rsis[3], opacity=0.5))
    for cx, cy, r, c, name, sub in (rsis, space, mykb):
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="2.4"/>')
        s.append(f'<text x="{cx}" y="{cy-10}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="14" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{cx}" y="{cy+10}" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="9.5">{esc(sub)}</text>')

    # overlap labels — real semantic relations
    s.append(pill(367, 402, [("RRP → L2", 11, SPACE), ("ideation feeds", 9, TEXT2), ("improvement cycles", 9, TEXT2)]))
    s.append(pill(450, 527, [("L3 CONSOLIDATION", 11, RSIS), ("lessons → memory", 9, TEXT2), ("git → graph → vectors", 9, TEXT2)]))
    s.append(pill(541, 419, [("SPEC CAPTURE", 11, MYKB), ("exports + session hooks", 9, TEXT2), ("stored in the wiki", 9, TEXT2)]))
    s.append(pill(455, 455, [("THE COSMOS MIND", 11.5, "#e2e8f0"), ("recursive self-improvement", 9, TEXT3)], pad=11))

    s.append(size_legend(60, 1180, [(195, RSIS, "RSIS3 · 67k LOC"), (238, MYKB, "MyKB · 103k LOC"), (192, SPACE, "SPACE · 69k LOC")]))
    # blend legend
    s.append(f'<text x="{W-60}" y="1180" text-anchor="end" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">OVERLAP = SHARED SEMANTIC TERRITORY</text>')
    blends = [("RSIS3 × SPACE", screen_hex(RSIS, SPACE)), ("RSIS3 × MyKB", screen_hex(RSIS, MYKB)),
              ("SPACE × MyKB", screen_hex(SPACE, MYKB)), ("all three", screen_hex(screen_hex(RSIS, MYKB), SPACE))]
    by = 1202
    for t, c in blends:
        s.append(f'<circle cx="{W-60}" cy="{by}" r="7" fill="{c}" fill-opacity=".9"/>')
        s.append(f'<text x="{W-74}" y="{by+3.5}" text-anchor="end" fill="{TEXT2}" font-family="{FONT}" font-size="9.5">{esc(t)}</text>')
        by += 26
    s.append(label(500, 1260, "colour = component identity · position = semantic spectra · size = footprint · blends = shared meaning", 9.5, TEXT4, italic=True))
    s.append(close_doc())
    return "\n".join(s)


# ── B-09: The System Ontology Field ───────────────────────────────────
def system_spectrum():
    s = [open_doc("THE SYSTEM ONTOLOGY FIELD",
                  "Every module mapped onto two spectra — certainty (observed ⇄ hypothesized) and scope (per-task ⇄ cross-session)")]
    x0, x1, y_top, y_bot = 170, 830, 180, 1060
    s.append(axis_frame(x0, x1, y_top, y_bot, "OBSERVED · facts", "HYPOTHESIZED · possibilities", "PER-TASK", "CROSS-SESSION",
                        xticks=[(335, "measured"), (665, "inferred")],
                        yticks=[(400, "session+"), (640, "task"), (880, "real-time")]))
    # quadrant labels
    s.append(label(275, 1038, "EXECUTION · observed facts", 9.5, TEXT4, italic=True))
    s.append(label(725, 1038, "GENERATION · candidate actions", 9.5, TEXT4, italic=True))
    s.append(label(275, 206, "MEMORY · accumulated knowledge", 9.5, TEXT4, italic=True))
    s.append(label(725, 206, "EVOLUTION · strategy & theory", 9.5, TEXT4, italic=True))
    s.append(f'<line x1="500" y1="{y_top}" x2="500" y2="{y_bot}" stroke="{BORDER}" stroke-width="1" stroke-dasharray="3,6"/>')
    s.append(f'<line x1="{x0}" y1="620" x2="{x1}" y2="620" stroke="{BORDER}" stroke-width="1" stroke-dasharray="3,6"/>')

    # trajectories first (under nodes)
    s.append(f'<path d="M 260 900 C 380 800, 480 720, 560 640" fill="none" stroke="{RSIS}" stroke-width="2" stroke-dasharray="5,5" opacity=".7" marker-end="url(#arwR)"/>')
    s.append(f'<path d="M 560 640 C 630 500, 680 400, 720 300" fill="none" stroke="{RSIS}" stroke-width="2" stroke-dasharray="5,5" opacity=".7" marker-end="url(#arwR)"/>')
    s.append(f'<path d="M 350 330 C 400 380, 430 400, 450 420" fill="none" stroke="{SPACE}" stroke-width="2" stroke-dasharray="4,6" opacity=".7" marker-end="url(#arwS)"/>')
    s.append(f'<path d="M 450 420 C 500 450, 530 470, 560 500" fill="none" stroke="{SPACE}" stroke-width="2" stroke-dasharray="4,6" opacity=".7" marker-end="url(#arwS)"/>')

    # nodes: (name, color, x, y, r)
    nodes = [
        ("L1 action loop", RSIS, 260, 900, 30),
        ("telemetry", DASH, 230, 760, 22),
        ("rack pulses", RSIS, 335, 950, 17),
        ("evaluator", RSIS, 420, 800, 26),
        ("L2 improvement", RSIS, 560, 640, 34),
        ("L3 evolution", RSIS, 720, 300, 38),
        ("wiki corpus", MYKB, 700, 430, 44),
        ("knowledge graph", MYKB, 620, 520, 32),
        ("TF-IDF index", MYKB, 470, 690, 26),
        ("temporal engine", MYKB, 650, 340, 24),
        ("session hooks", MYKB, 560, 500, 20),
        ("RRP probes", SPACE, 350, 330, 34),
        ("spec exports", SPACE, 450, 420, 26),
        ("LLM providers", SPACE, 290, 540, 22),
        ("prompt framework", SPACE, 380, 220, 30),
    ]
    for name, c, x, y, r in nodes:
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" fill-opacity=".28" stroke="{c}" stroke-width="2" filter="url(#shadow)"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>')
        s.append(f'<text x="{x}" y="{y - r - 7}" text-anchor="middle" fill="{TEXT}" font-family="{FONT}" font-size="10" font-weight="600">{esc(name)}</text>')

    s.append(pill(655, 430, [("IMPROVEMENT TRAJECTORY", 9.5, RSIS), ("L1 → L2 → L3 · facts become strategy", 8.5, TEXT3)]))
    s.append(pill(428, 372, [("IDEATION → MEMORY", 9.5, SPACE), ("probes → specs → hooks", 8.5, TEXT3)]))

    # legend
    lx, ly = 60, 1180
    s.append(f'<text x="{lx}" y="{ly}" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">HUE = COMPONENT</text>')
    for i, (c, t) in enumerate([(RSIS, "RSIS3 — engine"), (MYKB, "MyKB — memory"), (SPACE, "SPACE — ideation"), (DASH, "data / telemetry")]):
        yy = ly + 22 + i * 24
        s.append(f'<circle cx="{lx+9}" cy="{yy}" r="8" fill="{c}" fill-opacity=".8"/>')
        s.append(f'<text x="{lx+26}" y="{yy+3.5}" fill="{TEXT2}" font-family="{FONT}" font-size="10">{esc(t)}</text>')
    s.append(label(950, 1180, "radius ∝ footprint", 10, TEXT3, anchor="end", font=MONO))
    s.append(label(950, 1198, "files · LOC · pages", 9.5, TEXT4, anchor="end"))
    s.append(label(500, 1260, "each module occupies a semantic coordinate — the field IS the ontology, relationships are distance and overlap", 9.5, TEXT4, italic=True))
    s.append(close_doc())
    return "\n".join(s)


# ── A-08: MyKB Ontology Venn ──────────────────────────────────────────
def mykb_ontology():
    s = [open_doc("MYKB ONTOLOGY VENN",
                  "The memory substrate decomposed — episodic ⇄ semantic on X, implicit ⇄ explicit on Y, size ∝ storage footprint")]
    x0, x1, y_top, y_bot = 170, 830, 190, 1030
    s.append(axis_frame(x0, x1, y_top, y_bot, "EPISODIC · events & notes", "SEMANTIC · concepts & invariants", "IMPLICIT · raw", "EXPLICIT · linked",
                        xticks=[(290, "daily notes"), (500, "processed"), (710, "curated")],
                        yticks=[(300, "graph"), (550, "indexed"), (800, "buffers")]))
    # sets — all in the MyKB cyan family; lightness = explicitness
    sets = [
        ("daily + raw", 300, 780, 150, "#67e8f9", 0.42),
        ("temporal engine", 340, 520, 150, "#38bdf8", 0.42),
        ("TF-IDF index", 470, 560, 120, "#0ea5e9", 0.42),
        ("knowledge graph", 720, 420, 155, "#06b6d4", 0.45),
        ("hooks + ops", 560, 780, 110, "#0e7490", 0.45),
        ("wiki corpus", 640, 640, 215, "#22d3ee", 0.45),
    ]
    for name, cx, cy, r, c, op in sets:
        s.append(vcircle(cx, cy, r, c, opacity=op))
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="2"/>')
        s.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="11.5" font-weight="800">{esc(name.upper())}</text>')
    s.append(label(640, 660, "2,360+ pages · 48 domains", 9, TEXT2, italic=True))
    s.append(label(300, 800, "session logs · inbox", 9, TEXT2, italic=True))
    s.append(label(720, 440, "entities + edges", 9, TEXT2, italic=True))
    s.append(label(470, 580, "search surface", 9, TEXT2, italic=True))
    s.append(label(340, 540, "snapshots", 9, TEXT2, italic=True))

    s.append(pill(686, 512, [("ENTITY LINKS", 10.5, "#67e8f9"), ("48 domains · edges", 8.5, TEXT2)]))
    s.append(pill(531, 589, [("RETRIEVAL SURFACE", 10.5, "#7dd3fc"), ("queries hit pages + notes", 8.5, TEXT2)]))
    s.append(pill(440, 723, [("DAILY → WIKI", 10.5, "#67e8f9"), ("promotion pipeline", 8.5, TEXT2)]))
    s.append(pill(321, 643, [("TIME-TRAVEL", 10.5, "#38bdf8"), ("temporal snapshots", 8.5, TEXT2)]))
    s.append(pill(463, 569, [("TIME-TRAVEL RETRIEVAL", 10.5, "#e0f2fe"), ("3-way overlap", 8.5, TEXT3)]))
    s.append(pill(587, 733, [("SESSION CAPTURE", 10.5, "#0e7490"), ("hooks → wiki", 8.5, TEXT2)]))

    # legend: explicitness scale
    s.append(f'<text x="80" y="1160" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">LIGHTNESS = EXPLICITNESS (one cyan family = one substrate)</text>')
    for i, (c, t) in enumerate([("#67e8f9", "episodic / raw"), ("#22d3ee", "processed wiki"), ("#06b6d4", "semantic graph"), ("#0e7490", "procedural hooks")]):
        s.append(f'<rect x="80" y="{1180 + i*22}" width="16" height="12" rx="3" fill="{c}"/>')
        s.append(f'<text x="106" y="{1190 + i*22}" fill="{TEXT2}" font-family="{FONT}" font-size="9.5">{esc(t)}</text>')
    s.append(label(920, 1160, "radius ∝ storage", 10, TEXT3, anchor="end"))
    s.append(label(500, 1270, "one substrate, many surfaces — every overlap is a retrieval or capture path, not a boundary", 9.5, TEXT4, italic=True))
    s.append(close_doc())
    return "\n".join(s)


# ── A-09: SPACE Framework Ontology ────────────────────────────────────
def space_ontology():
    s = [open_doc("SPACE FRAMEWORK ONTOLOGY",
                  "The 7 RRP series mapped onto What ⇄ How and Concrete ⇄ Abstract — 326 probes distributed across the field")]
    x0, x1, y_top, y_bot = 170, 830, 190, 1030
    s.append(axis_frame(x0, x1, y_top, y_bot, "WHAT · description", "HOW · procedure", "CONCRETE", "ABSTRACT",
                        xticks=[(290, "identity"), (500, "meaning"), (710, "workflow")],
                        yticks=[(330, "specs"), (560, "methods"), (800, "operations")]))
    s.append(label(275, 1012, "DOMAIN of the artifact", 9, TEXT4, italic=True))
    s.append(label(725, 1012, "DOMAIN of the process", 9, TEXT4, italic=True))

    series = [
        ("CONCEPTUAL DEPTH", 300, 330, 120, "#f59e0b", "why · depth"),
        ("ONTOLOGY", 450, 400, 115, "#fbbf24", "what exists"),
        ("SEMANTICS", 580, 330, 110, "#f59e0b", "what it means"),
        ("TECHNICAL SPECS", 400, 700, 120, "#f59e0b", "what it must do"),
        ("PROCEDURES", 620, 760, 115, "#d97706", "how to do it"),
        ("METHODOLOGY", 720, 560, 105, "#fbbf24", "how to think"),
        ("OPERATIONS", 500, 840, 105, "#b45309", "how to run it"),
    ]
    for name, cx, cy, r, c, sub in series:
        s.append(vcircle(cx, cy, r, c, opacity=0.42))
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="2"/>')
        s.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="10" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8.5">{esc(sub)}</text>')
        # probe dots per series
        import random
        rnd = random.Random(f"space-{name}")
        for _ in range(5):
            a = rnd.uniform(0, 2 * math.pi)
            rr = rnd.uniform(0, r * 0.72)
            s.append(f'<circle cx="{cx + rr*math.cos(a):.0f}" cy="{cy + rr*math.sin(a):.0f}" r="2.2" fill="{c}" fill-opacity=".75"/>')

    s.append(pill(516, 364, [("MEANING & IDENTITY", 10.5, "#fde68a"), ("ontology × semantics", 8.5, TEXT2)]))
    s.append(pill(377, 366, [("DEPTH OF BEING", 10.5, "#fcd34d"), ("conceptual × ontology", 8.5, TEXT2)]))
    s.append(pill(672, 656, [("REPEATABLE WORKFLOWS", 10.5, "#fbbf24"), ("method × procedure", 8.5, TEXT2)]))
    s.append(pill(512, 730, [("IMPLEMENTATION CONTRACTS", 10.5, "#fde68a"), ("specs × procedures", 8.5, TEXT2)]))
    s.append(pill(557, 802, [("RUNBOOKS & DEPLOYS", 10.5, "#d97706"), ("operations × procedures", 8.5, TEXT2)]))

    s.append(f'<text x="80" y="1160" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">THE 7 SERIES (radius ∝ question share, est.)</text>')
    for i, (name, cx, cy, r, c, sub) in enumerate(series):
        yy = 1182 + i * 18
        s.append(f'<circle cx="90" cy="{yy}" r="6" fill="{c}" fill-opacity=".9"/>')
        s.append(f'<text x="106" y="{yy+3.5}" fill="{TEXT2}" font-family="{FONT}" font-size="9">{esc(name.lower())}</text>')
    s.append(f'<text x="920" y="1160" text-anchor="end" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">326 PROBES</text>')
    s.append(label(920, 1178, "dots sampled · density ∝ share", 9, TEXT4, anchor="end"))
    s.append(label(920, 1196, "6 export formats", 9, TEXT4, anchor="end"))
    s.append(label(500, 1275, "the framework is a space, not a list — questions live where their series overlap", 9.5, TEXT4, italic=True))
    s.append(close_doc())
    return "\n".join(s)


# ── E-07: Ontological Spheres (3D) ────────────────────────────────────
def ontology_spheres():
    s = [open_doc("ONTOLOGICAL SPHERES — 3D",
                  "The ontology map lifted into depth — hue = component, radius ∝ √LOC, floor = the two spectra, height = explicitness")]
    # perspective floor
    vp = (500, 620)
    s.append(f'<line x1="120" y1="1220" x2="{vp[0]}" y2="{vp[1]}" stroke="{BORDER}" stroke-width="1" opacity=".55"/>')
    s.append(f'<line x1="880" y1="1220" x2="{vp[0]}" y2="{vp[1]}" stroke="{BORDER}" stroke-width="1" opacity=".55"/>')
    for x in range(220, 801, 60):
        s.append(f'<line x1="{x}" y1="1240" x2="{vp[0]}" y2="{vp[1]}" stroke="{BORDER}" stroke-width=".7" opacity=".35"/>')
    for yy in (700, 800, 900, 1000, 1100, 1200):
        w = (yy - 620) / 600 * 780
        s.append(f'<line x1="{vp[0]-w}" y1="{yy}" x2="{vp[0]+w}" y2="{yy}" stroke="{BORDER}" stroke-width=".8" opacity=".5"/>')
    # floor axes
    s.append(f'<line x1="160" y1="1180" x2="840" y2="1120" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)"/>')
    s.append(f'<line x1="820" y1="1080" x2="760" y2="1230" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)"/>')
    s.append(label(852, 1112, "REAL-TIME → LONG-TERM", 10.5, TEXT2, anchor="start"))
    s.append(label(848, 1238, "EXECUTION → THEORY", 10.5, TEXT2, anchor="start"))

    defs = f'''<defs>
      <radialGradient id="sphR" cx="35%" cy="30%" r="75%"><stop offset="0%" stop-color="#c7d2fe"/><stop offset="45%" stop-color="#818cf8"/><stop offset="100%" stop-color="#3730a3"/></radialGradient>
      <radialGradient id="sphM" cx="35%" cy="30%" r="75%"><stop offset="0%" stop-color="#a5f3fc"/><stop offset="45%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#0e7490"/></radialGradient>
      <radialGradient id="sphS" cx="35%" cy="30%" r="75%"><stop offset="0%" stop-color="#fde68a"/><stop offset="45%" stop-color="#f59e0b"/><stop offset="100%" stop-color="#92400e"/></radialGradient>
    </defs>'''
    s.insert(1, defs)

    spheres = [
        ("RSIS3", 330, 900, 165, "sphR", RSIS, "execution · 67k LOC", 500),
        ("MYKB", 700, 950, 205, "sphM", MYKB, "persistence · 103k LOC", 820),
        ("SPACE", 500, 690, 170, "sphS", SPACE, "theory · 69k LOC", 700),
    ]
    # shadows first
    for name, cx, cy, r, gid, c, sub, z in spheres:
        s.append(f'<ellipse cx="{cx+18}" cy="{cy+ r*0.28 + 18}" rx="{r*1.02:.0f}" ry="{r*0.16:.0f}" fill="#000" opacity=".5"/>')
    for name, cx, cy, r, gid, c, sub, z in spheres:
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{gid})"/>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="1.6" opacity=".7"/>')
        s.append(f'<text x="{cx}" y="{cy - r - 12}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="13" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{cx}" y="{cy + r + 18}" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="9.5">{esc(sub)}</text>')

    # z-axis (explicitness) on the right
    zx = 910
    s.append(f'<line x1="{zx}" y1="1240" x2="{zx}" y2="300" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)"/>')
    s.append(f'<text x="{zx}" y="292" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="10.5" font-weight="700">EXPLICIT</text>')
    s.append(f'<text x="{zx}" y="1252" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="10.5" font-weight="700">IMPLICIT</text>')
    for name, cx, cy, r, gid, c, sub, z in spheres:
        s.append(f'<line x1="{cx}" y1="{z}" x2="{zx}" y2="{z}" stroke="{c}" stroke-width="1" stroke-dasharray="3,5" opacity=".75"/>')
        s.append(f'<circle cx="{zx}" cy="{z}" r="3.5" fill="{c}"/>')
        s.append(f'<text x="{zx-8}" y="{z+3.5}" text-anchor="end" fill="{TEXT3}" font-family="{MONO}" font-size="8.5">z={z}</text>')

    # blended overlap halos
    halos = [
        (415, 770, 78, 46, screen_hex(RSIS, SPACE), "ideation × action", "RRP feeds L2"),
        (515, 905, 86, 50, screen_hex(RSIS, MYKB), "consolidation", "L3 → memory"),
        (600, 830, 80, 46, screen_hex(SPACE, MYKB), "spec capture", "exports → wiki"),
    ]
    for hx, hy, hw, hh, c, t, sub in halos:
        s.append(f'<ellipse cx="{hx}" cy="{hy}" rx="{hw}" ry="{hh}" fill="{c}" fill-opacity=".55" style="mix-blend-mode:screen"/>')
        s.append(f'<text x="{hx}" y="{hy-4}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="9" font-weight="800">{esc(t)}</text>')
        s.append(f'<text x="{hx}" y="{hy+9}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="7.5">{esc(sub)}</text>')

    s.append(label(500, 1270, "depth illusion: radial light = surface, elliptical shadow = floor contact · halos = blended semantic territory", 9.5, TEXT4, italic=True))
    s.append(close_doc())
    return "\n".join(s)


# ── E-08: 4D — Evolution over Time ────────────────────────────────────
def time_evolution():
    s = [open_doc("THE 4D ONTOLOGY — EVOLUTION OVER TIME",
                  "Same semantic space, fourth axis = time — watch the components converge on shared territory while memory grows")]
    x0, x1, y_top, y_bot = 180, 820, 130, 640
    s.append(axis_frame(x0, x1, y_top, y_bot, "REAL-TIME", "LONG-TERM", "EXECUTION", "THEORY"))

    # states per time: (cx, cy, r) for rsis / space / mykb
    states = [
        ((240, 620, 150), (520, 320, 140), (760, 700, 170)),
        ((280, 560, 175), (470, 330, 160), (700, 620, 205)),
        ((300, 510, 195), (450, 310, 185), (660, 560, 240)),
    ]
    circles = [
        ("rsis", RSIS, [st[0] for st in states]),
        ("space", SPACE, [st[1] for st in states]),
        ("mykb", MYKB, [st[2] for st in states]),
    ]
    for name, c, pts in circles:
        vals_cx = ";".join(str(p[0]) for p in pts)
        vals_cy = ";".join(str(p[1]) for p in pts)
        vals_r = ";".join(str(p[2]) for p in pts)
        s.append(f'<circle fill="{c}" fill-opacity=".5" stroke="{c}" stroke-width="2" style="mix-blend-mode:screen">'
                 f'<animate attributeName="cx" values="{vals_cx}" dur="10s" repeatCount="indefinite"/>'
                 f'<animate attributeName="cy" values="{vals_cy}" dur="10s" repeatCount="indefinite"/>'
                 f'<animate attributeName="r" values="{vals_r}" dur="10s" repeatCount="indefinite"/></circle>')
        s.append(f'<text x="{pts[0][0]}" y="{pts[0][1]-12}" fill="{c}" font-family="{FONT}" font-size="11" font-weight="800">{esc(name.upper())}</text>')

    s.append(label(500, 700, "animated: circles drift from launch to consolidation — press play is not needed, the SVG animates in the browser", 9.5, TEXT4, italic=True))

    # frames strip
    fy0, fy1 = 760, 940
    frames = [
        ("T0 · LAUNCH", "separate & small", ((252, 880, 44), (440, 800, 40), (620, 880, 52))),
        ("T1 · INTEGRATION", "first overlaps", ((262, 852, 52), (420, 802, 46), (592, 852, 62))),
        ("T2 · CONSOLIDATION", "shared territory", ((272, 828, 58), (404, 806, 54), (568, 828, 72))),
        ("T3 · CONVERGENCE", "blended mind", ((282, 806, 64), (390, 810, 60), (546, 806, 80))),
    ]
    panel_w, gap = 212, 16
    for i, (t, cap, (pr, ps, pm)) in enumerate(frames):
        px = 34 + i * (panel_w + gap)
        s.append(f'<rect x="{px}" y="{fy0}" width="{panel_w}" height="{fy1-fy0}" rx="10" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1"/>')
        s.append(f'<text x="{px + panel_w/2}" y="{fy0+20}" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="10" font-weight="700">{esc(t)}</text>')
        s.append(f'<text x="{px + panel_w/2}" y="{fy0+34}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="8.5">{esc(cap)}</text>')
        scale = 0.26
        for (cx, cy, r), c in ((pr, RSIS), (ps, SPACE), (pm, MYKB)):
            s.append(f'<circle cx="{px + 30 + cx*scale:.0f}" cy="{fy0 + 110 - cy*scale:.0f}" r="{r*scale:.0f}" fill="{c}" fill-opacity=".5" stroke="{c}" stroke-width="1.4" style="mix-blend-mode:screen"/>')
    # time axis
    ty = 1000
    s.append(f'<line x1="150" y1="{ty}" x2="850" y2="{ty}" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)"/>')
    for i, (t, _, _) in enumerate(frames):
        x = 160 + i * (panel_w + gap) + panel_w / 2 - 14
        s.append(f'<text x="{x:.0f}" y="{ty+18}" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5">{esc(t.split(" ")[0])}</text>')
    s.append(f'<text x="858" y="{ty-8}" text-anchor="end" fill="{TEXT2}" font-family="{FONT}" font-size="10.5" font-weight="700">TIME — the 4th axis</text>')
    s.append(pill(500, 1090, [("WHAT CHANGES", 10, "#e2e8f0"), ("memory grows fastest · overlap increases · hues blend as cycles compound", 8.5, TEXT3)], pad=10))
    s.append(label(500, 1260, "a static frame is one slice of the ontology — the system only fully exists across time", 9.5, TEXT4, italic=True))
    s.append(close_doc())
    return "\n".join(s)


SEMANTIC = {
    "basic-08-component-ontology.svg": component_ontology,
    "basic-09-system-spectrum.svg": system_spectrum,
    "advanced-08-mykb-ontology.svg": mykb_ontology,
    "advanced-09-space-ontology.svg": space_ontology,
    "expert-07-ontology-spheres.svg": ontology_spheres,
    "expert-08-time-evolution.svg": time_evolution,
}
