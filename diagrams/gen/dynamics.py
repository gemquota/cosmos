"""Round 5 — dynamical-systems portraits (the phase-space expansion).

Extends the attractor-basin genre into a full dynamical family. Every
animation encodes real system behaviour:
  B-12 field arrows  == resultant basin pull at every sampled state
  A-12 comet descent == one artifact rolling down the maturation gradient
  A-13 lambda cursor == integration depth; each bifurcation = a subsystem joining
  E-11 ring rotation == loop cadence (1s / 12s / 60s, time-compressed)
  E-12 trajectories  == repeated sessions converging on the same attractor
No decorative motion. Each diagram carries a legend line stating what moves.
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
            f'COSMOS — Architecture Diagrams • Round 5 · dynamical portraits</text>\n</svg>')


# ── B-12 · The Flow Field (continuous vector portrait) ────────────────
FIELD = [
    ("SPACE", "RRP ideation · 326 probes", SPACE, 250, 330, 0.85),
    ("RSIS3", "engine · evaluator gate", RSIS, 750, 330, 1.0),
    ("MYKB", "memory · daemon :8765", MYKB, 500, 810, 0.72),
    ("DASH", "telemetry sink", DASH, 830, 770, 0.45),
]
MARK = {SPACE: "arwS", RSIS: "arwR", MYKB: "arwM", DASH: "arwD"}


def flow_field():
    xs = list(range(150, 856, 44))
    ys = list(range(200, 881, 44))
    s = [open_doc("THE FLOW FIELD — A VECTOR PORTRAIT",
                  f"{len(xs) * len(ys)} sampled states — each arrow is the resultant pull toward the loop that would consume an artifact born there")]
    # axes
    s.append(f'<line x1="120" y1="945" x2="880" y2="945" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(label(500, 974, "X — THEORY ←———→ EXECUTION", 10, TEXT3, font=MONO))
    s.append(f'<line x1="120" y1="160" x2="120" y2="945" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(f'<text x="96" y="545" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700" transform="rotate(-90 96 545)">Y — SHORT-TERM ↑ · LONG-TERM ↓</text>')
    # field arrows
    for x in xs:
        for y in ys:
            if any(math.hypot(x - ax, y - ay) < 36 for _, _, _, ax, ay, _ in FIELD):
                continue
            vx = vy = 0.0
            dom = None
            dmax = -1.0
            for _, _, c, ax, ay, st in FIELD:
                dx, dy = ax - x, ay - y
                d = math.hypot(dx, dy) + 1e-6
                f = st / ((d / 200.0) ** 2 + 0.35)
                vx += (dx / d) * f
                vy += (dy / d) * f
                if f > dmax:
                    dmax, dom = f, c
            m = math.hypot(vx, vy) + 1e-9
            L = min(26.0, 5 + m * 13.0)
            ex, ey = x + vx / m * L, y + vy / m * L
            s.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{ex:.0f}" y2="{ey:.0f}" stroke="{dom}" stroke-width="1.5" opacity=".5" marker-end="url(#{MARK[dom]})"/>')
    # orbs + artifact chips
    chips = {
        SPACE: "probe answers · spec drafts",
        RSIS: "candidates · pulses · lessons",
        MYKB: "captures · KG edges · index builds",
        DASH: "dashboard-data.json",
    }
    for name, tag, c, x, y, _ in FIELD:
        s.append(f'<circle cx="{x}" cy="{y}" r="20" fill="{c}" opacity=".92" stroke="#0b1120" stroke-width="2"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="30" fill="none" stroke="{c}" stroke-width="1" opacity=".5"/>')
        s.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="9" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y-26}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="10.5" font-weight="800">{esc(tag)}</text>')
        s.append(f'<text x="{x}" y="{y+42}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(chips[c])}</text>')
    # real pipeline flows + comets
    flows = [
        ("M 310,340 C 420,295 590,295 700,340", SPACE, "10s", "spec → implementation · evaluator gate", 505, 304),
        ("M 720,380 C 770,560 630,700 530,780", RSIS, "14s", "lessons → consolidation", 681, 606),
        ("M 470,780 C 370,650 450,490 680,370", MYKB, "9s", "context retrieval · :8765", 451, 560),
        ("M 768,370 C 800,480 812,630 822,740", RSIS, "5s", "pulses → dashboard-data.json", 803, 544),
        ("M 812,728 C 780,680 700,630 480,460", DASH, "7s", "dashboard → launch SPACE web UI", 655, 700),
    ]
    for path, c, dur, name, lx, ly in flows:
        s.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="7,5" opacity=".65" marker-end="url(#{MARK[c]})"/>')
        s.append(f'<circle r="5" fill="#fff"><animateMotion dur="{dur}" repeatCount="indefinite" path="{path}"/></circle>')
        s.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="8.5" font-weight="700">{esc(name)}</text>')
    # legend
    s.append(panel(96, 1000, 816, 200, EXT, "READING THE VECTOR FIELD",
                   [(EXT, 10.5, "ARROW = the resultant pull at that state — direction is the basin that wins, length is pull strength."),
                    (TEXT2, 9.5, "COLOUR = dominant basin — amber SPACE ideation · indigo RSIS3 execution · cyan MYKB memory · green DASH telemetry."),
                    (TEXT2, 9.5, "COMET = a real artifact in transit along the named route (spec → implementation · lessons → consolidation · retrieval :8765 · dashboard → launch SPACE web UI)."),
                    (TEXT2, 9.5, "Between the four orbs the field is contested — that contested band is the separatrix, where the evaluator gate decides."),
                    (TEXT2, 9.5, "This is the same basin geometry as the attractor portrait, drawn as a continuous field instead of a simulation.")],
                   header_h=30, pad=14, line_h=18))
    s.append(close_doc("a phase portrait without the trajectories — every possible artifact state, and the direction it is being pulled"))
    return "\n".join(s)


# ── A-12 · The Energy Landscape (maturation as a potential field) ──────
def alt_color(a):
    def lerp_hex(h1, h2, t):
        c1 = [int(h1[i:i + 2], 16) for i in (1, 3, 5)]
        c2 = [int(h2[i:i + 2], 16) for i in (1, 3, 5)]
        return "#" + "".join(f"{round(c1[i] + (c2[i] - c1[i]) * t):02x}" for i in range(3))
    if a >= 50:
        return lerp_hex("#fbbf24", "#f97316", (85 - a) / 35.0)
    return lerp_hex("#f97316", "#22d3ee", (50 - a) / 36.0)


WELLS12 = [
    ("SPACE · IDEATION", SPACE, 270, 300, 85, 62, "theory — cheap to draft, unstable", "landS"),
    ("RSIS3 · EXECUTION", RSIS, 740, 300, 22, 58, "implementation — deep, gated", "landR"),
    ("MYKB · MEMORY", MYKB, 500, 840, 14, 88, "consolidation — deepest, widest", "landM"),
]
GATES12 = [
    ("EVALUATOR GATE · barrier 55", 505, 300, "candidates must pass the gate to leave ideation"),
    ("CONSOLIDATION GATE · barrier 42", 620, 590, "lessons must pass to become memory"),
]


def energy_landscape():
    s = [open_doc("THE ENERGY LANDSCAPE — MATURATION AS A POTENTIAL FIELD",
                  "elevation = maturity cost · an artifact rolls downhill from cheap theory toward stable memory")]
    s.insert(1, """<defs>
  <radialGradient id="landS" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#fde68a" stop-opacity=".5"/><stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/></radialGradient>
  <radialGradient id="landR" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#c7d2fe" stop-opacity=".5"/><stop offset="100%" stop-color="#818cf8" stop-opacity="0"/></radialGradient>
  <radialGradient id="landM" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#a5f3fc" stop-opacity=".5"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
</defs>""")
    # basin fills
    for name, c, x, y, alt, base, tag, gid in WELLS12:
        s.append(f'<ellipse cx="{x}" cy="{y}" rx="250" ry="200" fill="url(#{gid})" style="mix-blend-mode:screen"/>')
    # contours
    for name, c, x, y, alt, base, tag, gid in WELLS12:
        for i in range(1, 6):
            rx = base * (1 + i * 0.42)
            ry = rx * 0.58
            a = alt + (100 - alt) * i / 5.5
            s.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx:.0f}" ry="{ry:.0f}" fill="none" stroke="{alt_color(a)}" stroke-width="1.2" opacity="{0.85 - 0.1 * i:.2f}"/>')
        out_rx = base * (1 + 5 * 0.42)
        a_out = alt + (100 - alt) * 5 / 5.5
        s.append(f'<text x="{x + out_rx + 6:.0f}" y="{y + 3}" fill="{TEXT4}" font-family="{MONO}" font-size="7.5">alt {a_out:.0f}</text>')
        s.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{c}" opacity=".92" stroke="#0b1120" stroke-width="2"/>')
        s.append(f'<text x="{x}" y="{y + 4}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="8.5" font-weight="800">{esc(name.split()[0])}</text>')
        s.append(f'<text x="{x}" y="{y - 24}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="11" font-weight="800">{esc(name)} · alt {alt}</text>')
        s.append(f'<text x="{x}" y="{y - 10}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8" font-style="italic">{esc(tag)}</text>')
    # saddle gates
    for name, x, y, tag in GATES12:
        s.append(f'<path d="M {x} {y - 9} L {x + 9} {y} L {x} {y + 9} L {x - 9} {y} Z" fill="#0b1120" stroke="{EXT}" stroke-width="1.6"/>')
        s.append(f'<text x="{x}" y="{y - 16}" text-anchor="middle" fill="{EXT}" font-family="{MONO}" font-size="8.5" font-weight="700">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y + 24}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(tag)}</text>')
    # DASH readout
    s.append(f'<circle cx="856" cy="560" r="14" fill="{DASH}" opacity=".92" stroke="#0b1120" stroke-width="2"/>')
    s.append(f'<text x="856" y="564" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="7" font-weight="800">DASH</text>')
    s.append(label(856, 532, "DASH · TELEMETRY", 8.5, DASH))
    # routes + comets
    routes = [
        ("M 300,300 C 400,300 450,300 505,300 C 600,300 680,300 740,300 C 760,430 720,550 620,590 C 570,640 540,760 500,840",
         "#ffffff", "16s", "MATURATION CASCADE", "spec → candidate → pulse → lesson → KG edge", "arwM", 505, 726),
        ("M 520,800 C 620,690 660,540 700,380",
         MYKB, "9s", "retrieval · :8765", "memory feeds the next action", "arwR", 632, 596),
        ("M 770,330 C 820,380 850,470 856,545",
         DASH, "5s", "pulses → dashboard-data.json", "", "arwD", 815, 470),
    ]
    for path, c, dur, name, sub, mark, lx, ly in routes:
        stroke_c = TEXT4 if c == "#ffffff" else c
        s.append(f'<path d="{path}" fill="none" stroke="{stroke_c}" stroke-width="{2.2 if c == "#ffffff" else 1.6}" stroke-dasharray="7,5" opacity=".6" marker-end="url(#{mark})"/>')
        s.append(f'<circle r="{5.5 if c == "#ffffff" else 4.5}" fill="{c}"><animateMotion dur="{dur}" repeatCount="indefinite" path="{path}"/></circle>')
        s.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" fill="{c if c != "#ffffff" else TEXT}" font-family="{FONT}" font-size="8.5" font-weight="700">{esc(name)}</text>')
        if sub:
            s.append(f'<text x="{lx}" y="{ly + 14}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(sub)}</text>')
    # elevation scale
    s.append(f'<defs><linearGradient id="altG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fbbf24"/><stop offset="55%" stop-color="#f97316"/><stop offset="100%" stop-color="#22d3ee"/></linearGradient></defs>')
    s.append(f'<rect x="908" y="300" width="16" height="540" rx="8" fill="url(#altG)" opacity=".85"/>')
    s.append(label(932, 306, "100", 7.5, TEXT3, anchor="start", font=MONO))
    s.append(label(932, 590, "55 · gate", 7.5, TEXT3, anchor="start", font=MONO))
    s.append(label(932, 842, "15", 7.5, TEXT3, anchor="start", font=MONO))
    s.append(f'<text x="932" y="462" text-anchor="middle" fill="{TEXT2}" font-family="{MONO}" font-size="7.5" transform="rotate(-90 932 462)">ELEVATION</text>')
    # legend
    s.append(panel(96, 1000, 816, 200, EXT, "READING THE LANDSCAPE",
                   [(EXT, 10.5, "ELEVATION = maturity cost — theory sits high (cheap to draft), consolidated memory sits low (expensive to reach, stable once there)."),
                    (TEXT2, 9.5, "SADDLES = the gates — an artifact must climb the evaluator barrier (55) to leave ideation, and the consolidation barrier (42) to become memory."),
                    (TEXT2, 9.5, "COMET = one artifact descending the gradient — spec → candidate → pulse → lesson → KG edge. Motion is the maturation cascade."),
                    (TEXT2, 9.5, "Telemetry's success-rate is the height function: as artifacts settle into wells, measured success rises."),
                    (TEXT2, 9.5, "The dashed routes are the real interfaces — retrieval :8765 returns memory to action, pulses reach dashboard-data.json.")],
                   header_h=30, pad=14, line_h=18))
    s.append(close_doc("the system's 'why' as terrain — every artifact rolls downhill toward the basin that stabilises it"))
    return "\n".join(s)


# ── A-13 · The Bifurcation Portrait (structure as λ grows) ────────────
REGIMES = [
    ("ENGINE ONLY", "1 fixed point", ["RSIS3"],
     [("RSIS3", RSIS, 0, 0)], [],
     "L1/L2/L3 fire with no external memory"),
    ("+ MEMORY", "fixed point + cycle", ["RSIS3", "MYKB"],
     [("RSIS3", RSIS, -42, 0), ("MYKB", MYKB, 42, 0)],
     [(0, 1, MYKB)],
     "lessons persist · retrieval :8765 feeds L1"),
    ("+ IDEATION", "3 basins + separatrix", ["SPACE", "RSIS3", "MYKB"],
     [("SPACE", SPACE, 0, -52), ("RSIS3", RSIS, 44, 38), ("MYKB", MYKB, -44, 38)],
     [(0, 1, SPACE), (1, 2, RSIS), (2, 0, MYKB)],
     "RRP specs feed L2 · separatrix appears"),
    ("+ TELEMETRY", "4 basins, closed loop", ["SPACE", "RSIS3", "MYKB", "DASH"],
     [("SPACE", SPACE, 0, -58), ("RSIS3", RSIS, -44, 0), ("MYKB", MYKB, 0, 58), ("DASH", DASH, 44, 0)],
     [(0, 1, SPACE), (1, 2, RSIS), (2, 3, MYKB), (3, 0, DASH)],
     "success-rate telemetry closes the loop"),
]
MS = [186, 378, 570, 762]
NAME2SHORT = {RSIS: "RSIS3", MYKB: "MYKB", SPACE: "SPACE", DASH: "DASH"}


def bifurcation_map():
    s = [open_doc("THE BIFURCATION PORTRAIT — STRUCTURE AS λ GROWS",
                  "λ = integration depth · each milestone is a real subsystem joining — and each joins the portrait as a new attractor")]
    # λ axis + milestones
    s.append(f'<line x1="120" y1="150" x2="880" y2="150" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(label(500, 128, "λ — INTEGRATION DEPTH (control parameter)", 10, TEXT2, font=MONO))
    labels = ["λ₁ · ENGINE", "λ₂ · +MEMORY", "λ₃ · +IDEATION", "λ₄ · +TELEMETRY"]
    for x, nm in zip(MS, labels):
        s.append(f'<line x1="{x}" y1="150" x2="{x}" y2="166" stroke="{TEXT3}" stroke-width="2"/>')
        s.append(label(x, 184, nm, 9.5, TEXT3, font=MONO))
    # λ cursor (animated)
    s.append(f'<line x1="186" y1="120" x2="186" y2="172" stroke="{EXT}" stroke-width="2.5">'
             f'<animate attributeName="x1" values="186;762;186" dur="40s" repeatCount="indefinite"/>'
             f'<animate attributeName="x2" values="186;762;186" dur="40s" repeatCount="indefinite"/></line>')
    s.append(f'<circle r="7" fill="{EXT}" stroke="#0b1120" stroke-width="1.5">'
             f'<animate attributeName="cx" values="186;762;186" dur="40s" repeatCount="indefinite"/></circle>')
    s.append(label(760, 106, "λ(t) — the cursor sweeps the regimes", 8.5, EXT, anchor="end", font=MONO))
    # regime panels
    PX = [96, 288, 480, 672]
    PW, PY, PH = 180, 210, 330
    for (title, topo, _, atts, links, cap), px in zip(REGIMES, PX):
        cx = px + PW / 2
        s.append(f'<rect x="{px}" y="{PY}" width="{PW}" height="{PH}" rx="12" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1"/>')
        s.append(f'<rect x="{px}" y="{PY}" width="{PW}" height="30" rx="12" fill="#334155" opacity=".25"/>')
        s.append(f'<rect x="{px}" y="{PY + 18}" width="{PW}" height="12" fill="#475569" opacity=".2"/>')
        s.append(f'<text x="{cx}" y="{PY + 20}" text-anchor="middle" fill="{TEXT}" font-family="{FONT}" font-size="11" font-weight="800">{esc(title)}</text>')
        s.append(label(cx, PY + 44, topo, 8, TEXT3, font=MONO))
        py = PY + 185
        for i, j, c in links:
            ax, ay = atts[i][2], atts[i][3]
            bx, by = atts[j][2], atts[j][3]
            s.append(f'<line x1="{cx + ax}" y1="{py + ay}" x2="{cx + bx}" y2="{py + by}" stroke="{c}" stroke-width="1.2" stroke-dasharray="3,4" opacity=".55"/>')
        for name, c, dx, dy in atts:
            ax, ay = cx + dx, py + dy
            s.append(f'<circle cx="{ax:.0f}" cy="{ay:.0f}" r="14" fill="{c}" opacity=".92" stroke="#0b1120" stroke-width="1.6"/>')
            s.append(f'<text x="{ax:.0f}" y="{ay + 4:.0f}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="7" font-weight="800">{esc(name)}</text>')
            s.append(f'<g><animateTransform attributeName="transform" type="rotate" from="0 {ax:.0f} {ay:.0f}" to="360 {ax:.0f} {ay:.0f}" dur="3s" repeatCount="indefinite"/>'
                     f'<circle cx="{ax + 22:.0f}" cy="{ay:.0f}" r="3" fill="{c}"/></g>')
        s.append(label(cx, PY + PH - 30, cap, 7.5, TEXT4))
    # bifurcation tree
    base = 880
    trees = [
        ([RSIS], 186),
        ([RSIS, MYKB], 378),
        ([SPACE, RSIS, MYKB], 570),
        ([SPACE, RSIS, MYKB, DASH], 762),
    ]
    s.append(f'<line x1="120" y1="{base}" x2="880" y2="{base}" stroke="{BORDER2}" stroke-width="1.4"/>')
    s.append(label(500, base + 18, "THE BIFURCATION TREE — every subsystem that joins adds an attractor branch", 9.5, TEXT2))
    for cols, xm in trees:
        n = len(cols)
        if n == 1:
            xs = [xm]
        elif n == 2:
            xs = [xm - 30, xm + 30]
        elif n == 3:
            xs = [xm - 46, xm, xm + 46]
        else:
            xs = [xm - 52, xm - 17, xm + 17, xm + 52]
        for x, c in zip(xs, cols):
            s.append(f'<line x1="{x}" y1="{base}" x2="{x}" y2="800" stroke="{c}" stroke-width="2" opacity=".8"/>')
            s.append(f'<circle cx="{x}" cy="794" r="6" fill="{c}" stroke="#0b1120" stroke-width="1.5"/>')
            s.append(f'<text x="{x}" y="782" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="7.5" font-weight="700">{NAME2SHORT[c]}</text>')
    s.append(label(500, 926, "1 FIXED POINT · 2 ATTRACTORS · 3 BASINS + SEPARATRIX · 4 BASINS — structure accumulates with λ", 8.5, TEXT4, font=MONO))
    # legend
    s.append(panel(96, 960, 816, 200, EXT, "READING THE BIFURCATION PORTRAIT",
                   [(EXT, 10.5, "λ = INTEGRATION DEPTH — the control parameter; each milestone is a real subsystem joining the ecosystem."),
                    (TEXT2, 9.5, "EACH BRANCH = one attractor born into the portrait: fixed point → limit cycle → separatrix → four basins."),
                    (TEXT2, 9.5, "λ CURSOR sweeps the timeline; inside every panel the loops keep firing at their real cadences (motion = live loops)."),
                    (TEXT2, 9.5, "Regimes match the repo: RSIS3 core → +MyKB memory → +SPACE ideation → +unified-dashboard telemetry."),
                    (TEXT2, 9.5, "The topology is the point: adding a subsystem does not add a box — it changes the dynamics.")],
                   header_h=30, pad=14, line_h=18))
    s.append(close_doc("bifurcation diagrams answer 'what changes when a new component joins?' — here the answer is the phase portrait itself"))
    return "\n".join(s)


# ── E-11 · The Coupled Oscillators (loop limit cycles, phase-locked) ───
def coupled_oscillators():
    s = [open_doc("THE COUPLED OSCILLATORS — LOOP LIMIT CYCLES",
                  "three loops, three frequencies, one phase relationship · rotation speed IS the real cadence, time-compressed")]
    CX, CY = 500, 470
    rings = [
        (110, RSIS, "L1 · ACTION", "T = 1s", 24, "1s"),
        (185, SPACE, "RRP · IDEATION", "T = 12s", 12, "12s"),
        (260, MYKB, "L3 · CONSOLIDATION", "T = 60s", 6, "60s"),
    ]
    for r, c, name, t, nt, dur in rings:
        s.append(f'<circle cx="{CX}" cy="{CY}" r="{r}" fill="none" stroke="{c}" stroke-width="2" opacity=".9"/>')
        s.append(f'<circle cx="{CX}" cy="{CY}" r="{r + 6}" fill="none" stroke="{c}" stroke-width="1" opacity=".3"/>')
        for k in range(nt):
            a = math.radians(k * 360 / nt)
            x1 = CX + (r - 5) * math.sin(a)
            y1 = CY - (r - 5) * math.cos(a)
            x2 = CX + (r + 5) * math.sin(a)
            y2 = CY - (r + 5) * math.cos(a)
            s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="1" opacity=".4"/>')
        s.append(f'<text x="{CX - r - 12}" y="{CY + 4}" text-anchor="end" fill="{c}" font-family="{FONT}" font-size="10.5" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{CX - r - 12}" y="{CY + 19}" text-anchor="end" fill="{TEXT3}" font-family="{MONO}" font-size="8.5">{esc(t)}</text>')
        s.append(f'<g><animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="{dur}" repeatCount="indefinite"/>'
                 f'<line x1="{CX}" y1="{CY}" x2="{CX}" y2="{CY - r + 14}" stroke="{c}" stroke-width="2" opacity=".55"/>'
                 f'<circle cx="{CX}" cy="{CY - r}" r="5.5" fill="{c}" stroke="#0b1120" stroke-width="1.5"/></g>')
    # hub
    s.append(f'<circle cx="{CX}" cy="{CY}" r="9" fill="#334155" stroke="{BORDER2}" stroke-width="1.5"/>')
    # coupling arcs + comets
    arcs = [
        (147, RSIS, "1.5s", [0, 3, 6, 9], "pulse → round", CY - 147 - 14),
        (222, SPACE, "3s", [0, 12, 24, 36, 48], "round → consolidation", CY - 222 - 14),
        (185, MYKB, "4s", [7, 37], "retrieval → action", CY - 185 - 14),
    ]
    for ar, c, dur, begins, name, ly in arcs:
        x1, x2 = CX - ar, CX + ar
        s.append(f'<path d="M {x1},{CY} A {ar},{ar} 0 0 1 {x2},{CY}" fill="none" stroke="{c}" stroke-width="1.4" stroke-dasharray="4,5" opacity=".5" marker-end="url(#{MARK[c]})"/>')
        for b in begins:
            s.append(f'<circle r="4.5" fill="{c}"><animateMotion dur="{dur}" begin="{b}s" repeatCount="indefinite" path="M {x1},{CY} A {ar},{ar} 0 0 1 {x2},{CY}"/></circle>')
        s.append(label(CX, ly, name, 8, c, font=MONO))
    # coupling ratios
    s.append(panel(772, 250, 188, 150, EXT, "COUPLING RATIOS",
                   [(EXT, 10.5, "12 : 1 — L1 pulses per RRP round"),
                    (SPACE, 10.5, "25 : 1 — RRP rounds per spec"),
                    (MYKB, 10.5, "1 spec → 1 consolidation"),
                    (TEXT2, 9.5, "phase-locked by the protocol, not by chance")],
                   header_h=28, pad=12, line_h=22))
    # phase gauge
    s.append(label(500, 934, "PHASE GAUGE — FREQUENCY LOCK", 10, TEXT2, font=MONO))
    s.append(f'<line x1="200" y1="960" x2="800" y2="960" stroke="{BORDER2}" stroke-width="2"/>')
    for k in range(12):
        x = 200 + k * 50
        s.append(f'<line x1="{x}" y1="952" x2="{x}" y2="968" stroke="{RSIS}" stroke-width="2"/>')
        if k % 3 == 0:
            s.append(f'<text x="{x}" y="986" text-anchor="middle" fill="{TEXT4}" font-family="{MONO}" font-size="7.5">{k + 1}</text>')
    s.append(f'<path d="M 200,978 L 200,988 L 800,988 L 800,978" fill="none" stroke="{SPACE}" stroke-width="1.6"/>')
    s.append(label(500, 1008, "1 RRP ROUND (12s) — 12 L1 PULSES (1s each)", 9.5, SPACE, font=MONO))
    s.append(f'<path d="M 200,1014 L 200,1024 L 800,1024 L 800,1014" fill="none" stroke="{MYKB}" stroke-width="1.6"/>')
    s.append(label(500, 1042, "5 RRP ROUNDS ≈ 1 L3 CONSOLIDATION (60s, compressed)", 9, MYKB, font=MONO))
    # legend
    s.append(panel(96, 1072, 816, 148, EXT, "WHY THE RINGS ROTATE",
                   [(EXT, 10.5, "ROTATION SPEED = the loop's real cadence, time-compressed — L1 1s · RRP 12s · L3 60s (real: 1–2s · ~1 min · ~1 hr)."),
                    (TEXT2, 9.5, "TICKS = one full cycle divided into 24/12/6 equal phase slots — a visual clock, not a protocol claim."),
                    (TEXT2, 9.5, "COMET = an event crossing the loop boundary — a pulse becoming a round, a round becoming consolidation, memory returning as context."),
                    (TEXT2, 9.5, "The hands are the phase of each loop; the ratios (12:1, 25:1) are the orchestration — not decoration.")],
                   header_h=30, pad=14, line_h=18))
    s.append(close_doc("three clocks, phase-locked by the protocol — the ratios are the orchestration"))
    return "\n".join(s)


# ── E-12 · The Trajectory Bundle (sessions converging on an attractor) ─
def lorenz_step(x, y, z, dt=0.004):
    sgm, rho, bet = 10.0, 28.0, 8.0 / 3.0
    dx = sgm * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - bet * z
    return x + dx * dt, y + dy * dt, z + dz * dt


def lorenz_traj(x0, y0, z0, steps, dt=0.004):
    pts = []
    x, y, z = x0, y0, z0
    for _ in range(steps):
        x, y, z = lorenz_step(x, y, z, dt)
        pts.append((x, y, z))
    return pts


ANG_A = 0.8


def proj3(x, y, z):
    ca, sa = math.cos(ANG_A), math.sin(ANG_A)
    z2 = y * sa + z * ca
    return x, z2


def success_ramp(t):
    lo, mid, hi = (244, 114, 182), (129, 140, 248), (16, 185, 129)
    if t < 0.5:
        a, b, u = lo, mid, t / 0.5
    else:
        a, b, u = mid, hi, (t - 0.5) / 0.5
    return "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * u):02x}" for i in range(3))


def trajectory_bundle():
    s = [open_doc("THE TRAJECTORY BUNDLE — SESSIONS CONVERGING",
                  "repeated sessions projected from a 3-state phase space · colour carries the 4th axis — success over time")]
    rnd = random.Random("lorenz-282")
    ref = lorenz_traj(1.0, 1.0, 1.0, 4200)
    sessions = [lorenz_traj(rnd.uniform(-4, 4), rnd.uniform(-4, 4), rnd.uniform(5, 35), 900) for _ in range(7)]
    allp = [proj3(*p) for p in ref] + [proj3(*p) for tr in sessions for p in tr]
    xs = [p[0] for p in allp]
    ys = [p[1] for p in allp]
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    PB = (130, 870, 240, 860)
    sc = min((PB[1] - PB[0]) / max(xmax - xmin, 1e-9), (PB[3] - PB[2]) / max(ymax - ymin, 1e-9))
    ox = (PB[0] + PB[1]) / 2 - (xmin + xmax) / 2 * sc
    oy = (PB[2] + PB[3]) / 2 - (ymin + ymax) / 2 * sc

    def P(x, y, z):
        px, py = proj3(x, y, z)
        return px * sc + ox, py * sc + oy

    pts = [P(*p) for p in ref]
    skel = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts[::3])
    s.append(f'<path d="{skel}" fill="none" stroke="{TEXT4}" stroke-width="0.8" opacity=".14"/>')

    def lobe_center(pred):
        q = [P(*p) for p in ref if pred(p[0])]
        return sum(a for a, _ in q) / len(q), sum(b for _, b in q) / len(q)

    lc_mem = lobe_center(lambda x: x < 0)
    lc_exe = lobe_center(lambda x: x > 0)
    s.append(f'<text x="{lc_mem[0]:.0f}" y="{lc_mem[1] + 18:.0f}" text-anchor="middle" fill="{MYKB}" font-family="{FONT}" font-size="11" font-weight="800">MEMORY LOBE · MYKB</text>')
    s.append(f'<text x="{lc_exe[0]:.0f}" y="{lc_exe[1] + 18:.0f}" text-anchor="middle" fill="{RSIS}" font-family="{FONT}" font-size="11" font-weight="800">EXECUTION LOBE · RSIS3</text>')
    dmax = max(math.hypot(lc_mem[0] - lc_exe[0], lc_mem[1] - lc_exe[1]) / 2, 60)
    for tr in sessions:
        pts2 = [P(*p) for p in tr]
        for i in range(0, len(pts2) - 14, 14):
            seg = pts2[i:i + 15]
            mx = sum(a for a, _ in seg) / len(seg)
            my = sum(b for _, b in seg) / len(seg)
            d = min(math.hypot(mx - lc_mem[0], my - lc_mem[1]), math.hypot(mx - lc_exe[0], my - lc_exe[1]))
            t = max(0.0, min(1.0, 1 - d / dmax))
            path = "M " + " L ".join(f"{a:.1f},{b:.1f}" for a, b in seg)
            s.append(f'<path d="{path}" fill="none" stroke="{success_ramp(0.18 + 0.82 * t)}" stroke-width="1.15" opacity=".85"/>')
    # entry cloud
    for i in range(8):
        x0 = 500 + rnd.uniform(-240, 240)
        tgt = lc_mem if i % 2 == 0 else lc_exe
        x1 = tgt[0] + rnd.uniform(-140, 140)
        y1 = tgt[1] + rnd.uniform(-120, 120)
        s.append(f'<path d="M {x0:.0f},205 C {x0 - 50:.0f},140 {(x0 + x1) / 2:.0f},{(205 + y1) / 2:.0f} {x1:.0f},{y1:.0f}" fill="none" stroke="{SPACE}" stroke-width="1.1" opacity=".4"/>')
    s.append(label(500, 178, "SESSION STARTS — scattered initial conditions, then convergence", 8.5, TEXT4))
    # comets
    main = pts[::4][:420]
    cm = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in main)
    s.append(f'<circle r="5" fill="#fff" stroke="#0b1120" stroke-width="1"><animateMotion dur="22s" repeatCount="indefinite" path="{cm}"/></circle>')
    echo = pts[::4][480:820]
    ce = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in echo)
    s.append(f'<circle r="4" fill="{MYKB}"><animateMotion dur="16s" begin="8s" repeatCount="indefinite" path="{ce}"/></circle>')
    s.append(label(130, 906, "white comet = the live session · cyan echo = retrieval returning memory to action", 8.5, TEXT4, anchor="start"))
    # axis glyph
    s.append(f'<line x1="150" y1="940" x2="230" y2="940" stroke="{RSIS}" stroke-width="2" marker-end="url(#arwR)"/>')
    s.append(label(240, 944, "x · context load", 8.5, RSIS, anchor="start", font=MONO))
    s.append(f'<line x1="150" y1="940" x2="185" y2="900" stroke="{SPACE}" stroke-width="2" marker-end="url(#arwS)"/>')
    s.append(label(196, 898, "y · action frequency", 8.5, SPACE, anchor="start", font=MONO))
    s.append(f'<line x1="150" y1="940" x2="150" y2="885" stroke="{MYKB}" stroke-width="2" marker-end="url(#arwM)"/>')
    s.append(label(150, 872, "z · memory depth", 8.5, MYKB, anchor="middle", font=MONO))
    # legend
    s.append(panel(96, 990, 816, 210, EXT, "READING THE BUNDLE — A STRANGE ATTRACTOR, DRAWN HONESTLY",
                   [(EXT, 10.5, "TRAJECTORY = one session through phase space (context load × action frequency × memory depth), projected to 2D."),
                    (TEXT2, 9.5, "CONVERGENCE = the ecosystem's steady state: scattered starts end up circulating the same two lobes — execution and memory."),
                    (TEXT2, 9.5, "COLOUR = success-rate telemetry along the path — pink segments are transient/contested, green segments are consolidated."),
                    (TEXT2, 9.5, "COMET = the live session tracing the attractor; the echo = retrieval pulling memory back into action."),
                    (TEXT2, 9.5, "TIME IS THE FOURTH AXIS: colour is a time-series along each line — failures fall away, survivors consolidate.")],
                   header_h=30, pad=14, line_h=18))
    s.append(close_doc("deterministic dynamics, never the same session twice — always the same two lobes: execution and memory"))
    return "\n".join(s)


DYNAMICS = {
    "basic-12-flow-field.svg": flow_field,
    "advanced-12-energy-landscape.svg": energy_landscape,
    "advanced-13-bifurcation-map.svg": bifurcation_map,
    "expert-11-coupled-oscillators.svg": coupled_oscillators,
    "expert-12-trajectory-bundle.svg": trajectory_bundle,
}
