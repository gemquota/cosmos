"""Round 3 — abstract ontology diagrams.

The discrete Venns become continuous: a density terrain (B-10), a projected
high-dimensional embedding space (A-10), and a categorical lattice of
artifacts and morphisms (E-09).
"""
import math, random
from design import *

W, H = 1000, 1320


def open_doc(title, subtitle):
    return svg_start(W, H, title, subtitle)


def close_doc(note):
    return (f'<text x="{W/2}" y="1278" text-anchor="middle" fill="{TEXT4}" '
            f'font-family="{FONT}" font-size="9.5" font-style="italic">{esc(note)}</text>\n'
            f'<text x="{W/2}" y="1300" text-anchor="middle" fill="#334155" font-family="{FONT}" font-size="9.5">'
            f'COSMOS — Architecture Diagrams • Round 3 · abstract ontology</text>\n</svg>')


def axis_frame(x0, x1, y_top, y_bot, x_left, x_right, y_bottom_label, y_top_label, xticks=None, yticks=None):
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


# ── B-10 · The Ontology Terrain (continuous semantic field) ───────────
def ontology_terrain():
    s = [open_doc("THE ONTOLOGY TERRAIN — A CONTINUOUS FIELD",
                  "The B-08 Venn, made continuous — components are density hills on shared semantic terrain, not circles with borders")]
    hills = '''<defs>
      <radialGradient id="hillR" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#c7d2fe" stop-opacity=".8"/><stop offset="55%" stop-color="#818cf8" stop-opacity=".38"/><stop offset="100%" stop-color="#818cf8" stop-opacity="0"/></radialGradient>
      <radialGradient id="hillM" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#a5f3fc" stop-opacity=".8"/><stop offset="55%" stop-color="#22d3ee" stop-opacity=".38"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
      <radialGradient id="hillS" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#fde68a" stop-opacity=".8"/><stop offset="55%" stop-color="#f59e0b" stop-opacity=".38"/><stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/></radialGradient>
    </defs>'''
    s.insert(1, hills)
    x0, x1, y_top, y_bot = 180, 820, 200, 1050
    s.append(axis_frame(x0, x1, y_top, y_bot, "REAL-TIME · seconds", "LONG-TERM · months", "EXECUTION", "THEORY",
                        xticks=[(280, "sec"), (460, "min"), (640, "hr"), (800, "days+")],
                        yticks=[(330, "strategy"), (500, "ideation"), (680, "action"), (860, "tool calls")]))
    s.append(label(275, 1030, "ACTION plane", 9, TEXT4, italic=True))
    s.append(label(720, 1030, "MEMORY plane", 9, TEXT4, italic=True))
    s.append(label(275, 228, "IDEATION plane", 9, TEXT4, italic=True))
    s.append(label(720, 228, "STRATEGY plane", 9, TEXT4, italic=True))

    hills3 = [("hillS", 450, 310, 250, SPACE, "SPACE · IDEATION", "69k LOC · 326 probes"),
              ("hillR", 280, 500, 260, RSIS, "RSIS3 · CORE ENGINE", "67k LOC · L1→L3"),
              ("hillM", 660, 560, 285, MYKB, "MYKB · MEMORY", "103k LOC · 2,360+ pages")]
    for gid, cx, cy, r, c, name, sub in hills3:
        s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.86}" fill="url(#{gid})" style="mix-blend-mode:screen"/>')
        for f in (0.52, 0.8):
            s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*f:.0f}" ry="{r*0.86*f:.0f}" fill="none" stroke="{c}" stroke-width="1" stroke-dasharray="4,7" opacity=".55"/>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{c}"/>')
        s.append(f'<text x="{cx}" y="{cy-16}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="13.5" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{cx}" y="{cy+2}" text-anchor="middle" fill="{TEXT2}" font-family="{FONT}" font-size="9">{esc(sub)}</text>')

    # modules sampled from the field (12 real modules at semantic coordinates)
    mods = [("evaluator", RSIS, 420, 800), ("L2 improvement", RSIS, 560, 640), ("L3 evolution", RSIS, 720, 300),
            ("rack pulses", DASH, 335, 950), ("TF-IDF index", MYKB, 470, 690), ("knowledge graph", MYKB, 620, 520),
            ("temporal engine", MYKB, 650, 340), ("session hooks", MYKB, 560, 500), ("RRP probes", SPACE, 350, 330),
            ("spec exports", SPACE, 450, 420), ("LLM providers", SPACE, 290, 540), ("prompt framework", SPACE, 380, 220)]
    for name, c, x, y in mods:
        s.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>')
        s.append(f'<text x="{x}" y="{y-8}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="7.5">{esc(name)}</text>')

    # overlap hotspots (explicit additive blends — render-safe)
    s.append(pill_b(453, 430, "RSIS3 × SPACE", screen_hex(RSIS, SPACE)))
    s.append(pill_b(560, 545, "RSIS3 × MYKB", screen_hex(RSIS, MYKB)))
    s.append(pill_b(600, 380, "MYKB × SPACE", screen_hex(SPACE, MYKB)))
    s.append(pill_b(455, 660, "THE COSMOS MIND", "#e2e8f0"))

    # legend
    s.append(f'<text x="80" y="1150" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">HOW TO READ THE TERRAIN</text>')
    for i, (c, t) in enumerate([
        ("#67e8f9", "HEIGHT = semantic load — brightest where a component is most itself"),
        ("#fbbf24", "CONTOURS = equipotential lines — equal semantic density"),
        ("#f472b6", "ADDITIVE BLEND = shared meaning — overlaps glow brighter, hues mix"),
        ("#94a3b8", "DOTS = modules — a module is a peak on the terrain, not a circle edge")]):
        s.append(f'<circle cx="90" cy="{1174+i*24}" r="7" fill="{c}" fill-opacity=".8"/>')
        s.append(f'<text x="106" y="{1178+i*24}" fill="{TEXT2}" font-family="{FONT}" font-size="9.5">{esc(t)}</text>')
    s.append(pill_b(500, 1000, "DISCRETE → CONTINUOUS", "#e2e8f0", sub="the Venn round was a map with borders — this round is the field the borders abstract away", dy=980))
    s.append(close_doc("sets are an approximation of a continuous space — the terrain is the ontology, the circles were just its census"))
    return "\n".join(s)


def pill_b(x, y, text, color, sub=None, dy=None):
    """small dark label pill (reused across round-3 diagrams)"""
    w = max(150, 16 + len(text) * 7.6)
    lines = [f'<rect x="{x-w/2}" y="{y-14}" width="{w}" height="28" rx="8" fill="#0b1120" opacity=".78"/>',
             f'<text x="{x}" y="{y+2}" text-anchor="middle" fill="{color}" font-family="{FONT}" font-size="10" font-weight="700">{esc(text)}</text>']
    if sub:
        lines.append(f'<rect x="{x-w/2}" y="{y+16}" width="{w}" height="24" rx="8" fill="#0b1120" opacity=".78"/>')
        lines.append(f'<text x="{x}" y="{y+30}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8" font-style="italic">{esc(sub)}</text>')
    return "\n".join(lines)


# ── A-10 · The Embedding Space (2,360+ pages → 2D) ────────────────────
DOMAINS = ["agent-systems", "ai-ml", "api-protocols", "cloud-infra", "concepts", "data-storage",
           "decisions", "dev-tools", "development", "entities", "frontend", "infrastructure",
           "js-ts-ecosystem", "llm-agents", "memory", "meta-learning", "ml-frameworks",
           "mobile-platform", "prompt-engineering", "security-auth", "shell-environment",
           "software-engineering", "syntheses", "testing", "topics", "web-platforms"]
LABEL_DOMAINS = {"agent-systems": (1, 0), "ai-ml": (6, 2), "api-protocols": (0, 4), "cloud-infra": (3, 5),
                 "concepts": (2, 2), "data-storage": (5, 3), "llm-agents": (4, 0), "memory": (7, 1),
                 "meta-learning": (6, 4), "prompt-engineering": (3, 0), "security-auth": (1, 3),
                 "testing": (5, 5), "web-platforms": (7, 3), "software-engineering": (2, 4)}


def embedding_space():
    s = [open_doc("THE EMBEDDING SPACE — 2,360+ PAGES PROJECTED",
                  "TF-IDF vectors of the wiki corpus dropped into 2D — distance = semantic similarity, clusters = the 48 domains")]
    x0, x1, y_top, y_bot = 130, 870, 180, 1020
    s.append(f'<rect x="{x0}" y="{y_top}" width="{x1-x0}" height="{y_bot-y_top}" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>')
    s.append(label(500, 1040, "PC1 · PC2 — arbitrary projection axes · distance ≈ semantic similarity (TF-IDF + cosine)", 9.5, TEXT4, italic=True))

    rnd = random.Random("embed-2360")
    # 8×6 distorted grid → 48 cluster centres
    centres = []
    for i in range(48):
        gx, gy = i % 8, i // 8
        cx = x0 + 42 + gx * ((x1 - x0 - 84) / 7) + rnd.uniform(-12, 12)
        cy = y_top + 40 + gy * ((y_bot - y_top - 80) / 5) + rnd.uniform(-12, 12)
        pages = int(280 * (0.4 + rnd.random() ** 2))  # 5–280 pages, skew small
        centres.append((cx, cy, pages))
    shades = ["#67e8f9", "#22d3ee", "#06b6d4", "#0891b2"]
    for cx, cy, pages in centres:
        sh = shades[min(3, int(math.log2(pages + 1) / 2))]
        n = min(6, 2 + int(pages / 60))
        for _ in range(n):
            a = rnd.uniform(0, 2 * math.pi)
            rr = rnd.uniform(2, 9 + pages / 60)
            s.append(f'<circle cx="{cx + rr*math.cos(a):.0f}" cy="{cy + rr*math.sin(a):.0f}" r="2.1" fill="{sh}" opacity=".8"/>')
        s.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="1.6" fill="#e0f2fe" opacity=".9"/>')

    # label a selection of real domains
    for i, name in enumerate(DOMAINS[:26]):
        gx, gy = i % 8, i // 8
        cx = x0 + 42 + gx * ((x1 - x0 - 84) / 7)
        cy = y_top + 40 + gy * ((y_bot - y_top - 80) / 5)
        if name in LABEL_DOMAINS:
            lx, ly = LABEL_DOMAINS[name]
            tx = cx + (lx - 3.5) * 14
            ty = cy + (ly - 2.5) * 13
            s.append(f'<text x="{tx:.0f}" y="{ty:.0f}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="7.5">{esc(name)}</text>')

    # component anchors
    anchors = [("RSIS3 · lessons & pulses", RSIS, 240, 300), ("SPACE · RRP specs", SPACE, 720, 420),
               ("DASH · telemetry views", DASH, 660, 900), ("wiki corpus core", MYKB, 500, 620)]
    for name, c, x, y in anchors:
        s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" stroke="#0b1120" stroke-width="2"/>')
        s.append(f'<text x="{x}" y="{y+24}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="9.5" font-weight="700">{esc(name)}</text>')

    # query + RRF retrieval
    qx, qy = 360, 760
    s.append(f'<circle cx="{qx}" cy="{qy}" r="12" fill="none" stroke="{DASH}" stroke-width="1.6" stroke-dasharray="2,4"/>')
    s.append(f'<circle cx="{qx}" cy="{qy}" r="46" fill="none" stroke="{DASH}" stroke-width="1.4" stroke-dasharray="2,4" opacity=".8"/>')
    s.append(f'<circle cx="{qx}" cy="{qy}" r="92" fill="none" stroke="{DASH}" stroke-width="1.2" stroke-dasharray="2,4" opacity=".5"/>')
    s.append(f'<circle cx="{qx}" cy="{qy}" r="5" fill="{DASH}"/>')
    s.append(f'<text x="{qx}" y="{qy-20}" text-anchor="middle" fill="{DASH}" font-family="{FONT}" font-size="9" font-weight="700">QUERY</text>')
    s.append(f'<text x="{qx}" y="{qy+124}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8.5">RRF top-10 · top-50 · top-200</text>')
    s.append(arrow(qx + 92, qy - 40, 560, 700, DASH, marker="arwD", width=1.8, dashed=True))

    # index panel
    s.append(panel(120, 1080, 760, 74, DASH, "INDEXED BY TF-IDF · RANKED BY RRF · SERVED :8765",
                   [(TEXT2, 9.5, "2,360+ markdown pages · 48 domains → term vectors → cosine neighbourhoods · hybrid fusion ranks the hits")],
                   header_h=26, pad=12))
    s.append(close_doc("high-dimensional meaning, flattened to two axes you can see — every module and every memory lands somewhere on this map"))
    return "\n".join(s)


# ── E-09 · The Semantic Lattice (categorical view) ─────────────────────
LEVELS = [("CODE", 240), ("RUNTIME", 470), ("KNOWLEDGE", 700), ("MEANING", 930)]
COLS = [("RSIS3", 250, RSIS), ("MYKB", 500, MYKB), ("SPACE", 750, SPACE)]
NODES = {
    ("CODE", 0): ("3-loop engine", "python · L1/L2/L3"),
    ("CODE", 1): ("wiki + daemon", "python · markdown"),
    ("CODE", 2): ("SPACE engine", "typescript · 10 modules"),
    ("RUNTIME", 0): ("rack daemon", "pulses · evaluator"),
    ("RUNTIME", 1): (".wiki-daemon", ":8765"),
    ("RUNTIME", 2): ("web UI + meta", ":8888 · :8899"),
    ("KNOWLEDGE", 0): ("rack/pulses", "JSONL events"),
    ("KNOWLEDGE", 1): ("wiki + KG", "2,360+ pages · edges"),
    ("KNOWLEDGE", 2): ("spec exports", "6 formats"),
    ("MEANING", 0): ("evaluator invariants", "PASS/FAIL gate"),
    ("MEANING", 1): ("48 domains", "concepts · clusters"),
    ("MEANING", 2): ("7 RRP series", "326 probes · 25 rounds"),
}


def semantic_lattice():
    s = [open_doc("THE SEMANTIC LATTICE — A CATEGORICAL VIEW",
                  "Artifacts as objects, data/control flows as morphisms — the structure the system's relations are forced into")]
    # level rails
    for lname, ly in LEVELS:
        s.append(f'<text x="60" y="{ly+4}" text-anchor="end" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700">{esc(lname)}</text>')
        s.append(f'<line x1="76" y1="{ly}" x2="960" y2="{ly}" stroke="{BORDER}" stroke-width="1" stroke-dasharray="2,5" opacity=".6"/>')
    # spines (vertical abstraction axes)
    for cname, cx, c in COLS:
        s.append(f'<line x1="{cx}" y1="{LEVELS[0][1]+34}" x2="{cx}" y2="{LEVELS[3][1]-34}" stroke="{c}" stroke-width="1.2" stroke-dasharray="3,6" opacity=".4"/>')
        s.append(f'<text x="{cx}" y="{LEVELS[0][1]-26}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="13" font-weight="800">{esc(cname)}</text>')
    s.append(f'<line x1="76" y1="{LEVELS[0][1]+34}" x2="76" y2="{LEVELS[3][1]-34}" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)"/>')
    s.append(label(62, (LEVELS[0][1]+LEVELS[3][1])/2, "MORE ABSTRACT", 9, TEXT3, anchor="middle", font=MONO))
    s.append(f'<text x="62" y="{(LEVELS[0][1]+LEVELS[3][1])/2 - 12}" text-anchor="middle" fill="{TEXT4}" font-family="{MONO}" font-size="8.5" transform="rotate(-90 62 {(LEVELS[0][1]+LEVELS[3][1])/2 - 12})">ABSTRACTION</text>')

    # nodes
    for (lname, ly), (cname, cx, c) in [(l, col) for l in LEVELS for col in COLS]:
        name, sub = NODES[(lname, 0 if cname == "RSIS3" else 1 if cname == "MYKB" else 2)]
        x = cx - 78
        s.append(f'<rect x="{x}" y="{ly-30}" width="156" height="60" rx="10" fill="{PANEL}" stroke="{c}" stroke-width="1.4"/>')
        s.append(f'<rect x="{x}" y="{ly-30}" width="156" height="20" rx="10" fill="{c}" opacity=".16"/>')
        s.append(f'<text x="{cx}" y="{ly-14}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="10.5" font-weight="700">{esc(name)}</text>')
        s.append(f'<text x="{cx}" y="{ly+4}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8">{esc(sub)}</text>')

    # horizontal morphisms per level
    rels = [
        (0, "imports specs", "SPACE→RSIS3", SPACE, 0, 2),
        (0, "session hooks", "SPACE→MYKB", MYKB, 2, 1),
        (1, "queries :8765", "RSIS3→MYKB", RSIS, 0, 1),
        (1, "serves UI", "SPACE→web", SPACE, 2, 0),
        (2, "captures", "SPACE→MYKB", MYKB, 2, 1),
        (2, "reads / writes", "RSIS3↔MYKB", RSIS, 0, 1),
        (3, "gates candidates", "RSIS3→SPACE", RSIS, 0, 2),
        (3, "consolidates", "RSIS3→MYKB", RSIS, 0, 1),
    ]
    for ly, rname, rsub, c, a, b in rels:
        y = ly - 42
        xa, xb = COLS[a][1], COLS[b][1]
        dirx = 1 if xb > xa else -1
        s.append(f'<line x1="{xa+84*dirx}" y1="{y}" x2="{xb-84*dirx}" y2="{y}" stroke="{c}" stroke-width="1.6" marker-end="{f"url(#arw{'R' if c==RSIS else 'M' if c==MYKB else 'S'})" if xb>xa else ''}"/>')
        s.append(f'<text x="{(xa+xb)/2}" y="{y-5}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="8.5" font-weight="600">{esc(rname)}</text>')

    # universal constructions
    unis = [
        ("INITIAL OBJECT", "GOALS & CONSTRAINTS", 500, 150, EXT),
        ("TERMINAL OBJECT", "THE IMMUTABLE EVALUATOR — nothing escapes", 250, 900, EXT),
        ("PULLBACK", "SPEC CAPTURE — the overlap that must exist", 625, 660, EXT),
        ("PUSHOUT", "L3 CONSOLIDATION — the merge that must exist", 375, 860, EXT),
    ]
    for t, sub, x, y, c in unis:
        s.append(f'<g transform="translate({x},{y}) rotate(45)"><rect x="-10" y="-10" width="20" height="20" fill="{c}" opacity=".9"/></g>')
        s.append(f'<text x="{x+16}" y="{y-4}" text-anchor="start" fill="{c}" font-family="{FONT}" font-size="9" font-weight="800">{esc(t)}</text>')
        s.append(f'<text x="{x+16}" y="{y+8}" text-anchor="start" fill="{TEXT3}" font-family="{FONT}" font-size="8">{esc(sub)}</text>')

    # glossary
    s.append(panel(120, 1080, 760, 110, EXT, "READING THE LATTICE — CATEGORY THEORY IN PLAIN WORDS",
                   [(EXT, 10, "OBJECT = an artifact · MORPHISM = a data/control flow · both are real, named things in the codebase"),
                    (TEXT2, 9.5, "PULLBACK = the overlap that must exist · PUSHOUT = the merge that must exist"),
                    (TEXT2, 9.5, "TERMINAL = the judge nothing escapes · INITIAL = the goals nothing precedes")],
                   header_h=28, pad=14, line_h=19))
    s.append(close_doc("relations are not decoration — they are structure, and the structure has a shape: a lattice"))
    return "\n".join(s)


ROUND3 = {
    "basic-10-ontology-terrain.svg": ontology_terrain,
    "advanced-10-embedding-space.svg": embedding_space,
    "expert-09-semantic-lattice.svg": semantic_lattice,
}
