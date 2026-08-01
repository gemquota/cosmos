"""Round 4 — experimental dynamics diagrams.

Every animation encodes real system behaviour:
  B-11 pulse period == loop cadence (L1 seconds / RRP minutes / L3 hours)
  A-11 sweep       == RRP dispatch order (25 rounds across 7 series)
  E-10 trajectories == observed maturation flows (spec -> impl -> memory)
No decorative motion. Each diagram carries a legend line stating what moves and why.
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
            f'COSMOS — Architecture Diagrams • Round 4 · experimental dynamics</text>\n</svg>')


def anim_ring(cx, cy, dur, color, rmax=88, w=2.2, start=12):
    """expanding pulse ring — one full expansion == one real loop iteration"""
    return (f'<circle cx="{cx}" cy="{cy}" r="{start}" fill="none" stroke="{color}" stroke-width="{w}">'
            f'<animate attributeName="r" values="{start};{rmax}" dur="{dur}" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0.85;0" dur="{dur}" repeatCount="indefinite"/>'
            f'</circle>')


def travel_dot(x1, x2, y, dur, color, begin, r=5):
    """event shuttle — a bright dot that rides one pulse across the rail"""
    return (f'<circle cx="{x1}" cy="{y}" r="{r}" fill="{color}" opacity="0">'
            f'<animate attributeName="cx" values="{x1};{x2}" dur="{dur}" begin="{begin}" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;0" dur="{dur}" begin="{begin}" repeatCount="indefinite"/>'
            f'</circle>')


# ── B-11 · The Pulse Field (cadence-encoded animation) ────────────────
LANES = [
    ("L1 · ACTION LOOP", "RSIS3 — tool call → observe → retry", RSIS, "1s", "≈ 1–2 s real",
     ["tool call", "observe", "retry", "result", "pulse"], "→ rack · dashboard-data.json"),
    ("RRP · IDEATION ROUND", "SPACE — probe → answer → artifact", SPACE, "12s", "≈ 1 min real",
     ["probe", "answer", "artifact", "validate", "export"], "→ artifacts · 6 formats"),
    ("L3 · CONSOLIDATION", "MYKB — merge → evolve → write memory", MYKB, "60s", "≈ 1 hr real",
     ["merge", "evolve", "consolidate", "KG write", "index"], "→ wiki · 2,360+ pages"),
]


def pulse_field():
    s = [open_doc("THE PULSE FIELD — CADENCE IS THE DATA",
                  "Three loops, three real rhythms: each ring below takes exactly one loop iteration to expand — L1 seconds, RRP minutes, L3 hours")]
    # y-axis (loop depth)
    ax_y = 340
    s.append(f'<line x1="70" y1="452" x2="70" y2="130" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(f'<text x="58" y="{ax_y}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="10.5" font-weight="700" transform="rotate(-90 58 {ax_y})">LOOP DEPTH — FASTER ↑ · SLOWER ↓</text>')
    s.append(label(96, 116, "L1 (seconds) — shallowest, hottest", 9, TEXT4))
    s.append(label(96, 236, "RRP (minutes) — mid-depth, 25 rounds", 9, TEXT4))
    s.append(label(96, 356, "L3 (hours) — deepest, rarest", 9, TEXT4))

    lane_y = [120, 240, 360]
    for (name, sub, c, dur, real, evs, sink), ly in zip(LANES, lane_y):
        cy = ly + 46
        s.append(f'<rect x="96" y="{ly}" width="816" height="92" rx="14" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1"/>')
        s.append(f'<rect x="96" y="{ly}" width="816" height="20" rx="14" fill="{c}" opacity=".12"/>')
        s.append(f'<rect x="96" y="{ly+8}" width="816" height="12" fill="{c}" opacity=".10"/>')
        s.append(f'<text x="112" y="{ly+33}" fill="{c}" font-family="{FONT}" font-size="12" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="112" y="{ly+47}" fill="{TEXT3}" font-family="{FONT}" font-size="8.5">{esc(sub)}</text>')
        # source orb + echoes + animated ring
        s.append(f'<circle cx="150" cy="{cy}" r="16" fill="{c}" opacity=".9" stroke="#0b1120" stroke-width="2"/>')
        s.append(f'<circle cx="150" cy="{cy}" r="16" fill="none" stroke="{c}" stroke-width="1" opacity=".5"/>')
        for er in (30, 46, 64):
            s.append(f'<circle cx="150" cy="{cy}" r="{er}" fill="none" stroke="{c}" stroke-width="1" stroke-dasharray="2,5" opacity=".28"/>')
        s.append(anim_ring(150, cy, dur, c, rmax=150))
        # cadence chip
        s.append(f'<rect x="812" y="{cy-11}" width="84" height="22" rx="11" fill="{c}" opacity=".15"/>')
        s.append(f'<text x="854" y="{cy+4}" text-anchor="middle" fill="{c}" font-family="{MONO}" font-size="9.5" font-weight="700">T = {dur}</text>')
        s.append(f'<text x="812" y="{cy+24}" text-anchor="start" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(real)}</text>')
        # event rail: static ticks + labels + travelling shuttles
        rail_x = [300, 402, 504, 606, 708]
        for i, (rx, ev) in enumerate(zip(rail_x, evs)):
            s.append(f'<circle cx="{rx}" cy="{cy}" r="4" fill="{c}" opacity=".22"/>')
            s.append(f'<text x="{rx}" y="{cy+20}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(ev)}</text>')
            s.append(travel_dot(170, 760, cy, dur, "#ffffff", f"{i * float(dur.rstrip('s')) / 5:.2f}s"))
        # sink
        s.append(f'<text x="800" y="{cy-16}" text-anchor="end" fill="{TEXT3}" font-family="{FONT}" font-size="8">{esc(sink)}</text>')

    # time rail
    s.append(f'<line x1="120" y1="496" x2="880" y2="496" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)"/>')
    s.append(label(500, 486, "X = TIME", 10, TEXT2, font=MONO))
    s.append(label(500, 518, "each pulse emits one event — the white shuttle is that event flowing right toward the rack, the spec exports, the wiki", 9.5, TEXT4))

    # legend — what the animation means
    s.append(panel(96, 556, 816, 128, EXT, "WHAT THE ANIMATION MEANS — AND WHY THESE THREE RINGS MOVE",
                   [(EXT, 10.5, "PERIOD = CADENCE — the ring's expansion time IS the loop's real firing interval (1s / 12s / 60s, time-compressed)."),
                    (TEXT2, 9.5, "L1 rings every ~1–2s of real runtime · RRP every ~1 min · L3 every ~1 hr — deeper loops fire slower."),
                    (TEXT2, 9.5, "SHUTTLE = the event that pulse emits: L1 writes a rack pulse, RRP writes an artifact, L3 writes consolidated memory."),
                    (TEXT2, 9.5, "Nothing else moves. If a ring were decorative, this diagram would be a screensaver — it isn't.")],
                   header_h=30, pad=14, line_h=19))
    # cadence table
    rows = [(RSIS, "L1 · ACTION", "≈ 1–2 s / tool-call round", "hundreds per session", "rack/pulses JSONL → dashboard-data.json"),
            (SPACE, "RRP · IDEATION", "≈ 1 min / probe round", "25 rounds per spec", "artifacts → 6 export formats"),
            (MYKB, "L3 · CONSOLIDATION", "≈ 1 hr / consolidation", "per session end", "wiki + KG writes · 2,360+ pages")]
    s.append(f'<text x="96" y="724" fill="{TEXT3}" font-family="{FONT}" font-size="10" font-weight="700">CADENCE REGISTER — REAL TIMINGS, NOT DECORATION</text>')
    for i, (c, name, cad, freq, out) in enumerate(rows):
        cx0 = 96 + i * 280
        s.append(f'<rect x="{cx0}" y="736" width="256" height="92" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>')
        s.append(f'<circle cx="{cx0+20}" cy="{756}" r="6" fill="{c}"/>')
        s.append(f'<text x="{cx0+34}" y="{760}" fill="{c}" font-family="{MONO}" font-size="10" font-weight="700">{esc(name)}</text>')
        for j, (txt, col) in enumerate([(cad, TEXT2), (freq, TEXT3), (out, TEXT3)]):
            s.append(f'<text x="{cx0+16}" y="{782+j*18}" fill="{col}" font-family="{FONT}" font-size="8.5">{esc(txt)}</text>')
    s.append(close_doc("cadence is not a styling choice — it is the system's heartbeat, drawn at its actual rate"))
    return "\n".join(s)


# ── A-11 · The Probe Constellation (dispatch wave animation) ───────────
SERIES = [
    (1, "Conceptual Depth", 3, 6, "#fbbf24"),
    (2, "Ontological Characteristics", 5, 15, "#f59e0b"),
    (3, "Semantic Relationships", 4, 8, "#f97316"),
    (4, "Procedural Breadth", 3, 6, "#fb923c"),
    (5, "Technical Specifications", 4, 20, "#d97706"),
    (6, "Development Methodologies", 3, 6, "#fcd34d"),
    (7, "Operational / Functional", 3, 6, "#ea580c"),
]
CX, CY = 500, 560
R_ORB = 250
R_CL = 296


def probe_constellation():
    s = [open_doc("THE PROBE CONSTELLATION — RRP DISPATCH SEQUENCE",
                  "326 probes · 7 series · 25 rounds — the cursor sweeps the constellation once per full elicitation session")]
    # orbit + round ticks (25 rounds → one full turn)
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R_ORB}" fill="none" stroke="{BORDER2}" stroke-width="1" stroke-dasharray="2,6" opacity=".6"/>')
    for k in range(25):
        a = math.radians(k * 14.4)
        x1 = CX + (R_ORB - 7) * math.sin(a); y1 = CY - (R_ORB - 7) * math.cos(a)
        x2 = CX + (R_ORB + 7) * math.sin(a); y2 = CY - (R_ORB + 7) * math.cos(a)
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{TEXT4}" stroke-width="1.4"/>')
        if k % 5 == 0:
            lx = CX + (R_ORB - 24) * math.sin(a); ly = CY - (R_ORB - 24) * math.cos(a)
            s.append(f'<text x="{lx:.0f}" y="{ly+3:.0f}" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="8.5" font-weight="700">{k+1}</text>')
    # dispatched wedge (rounds 1–5 at load) + cursor
    a1, a2 = math.radians(0), math.radians(72)
    wx = CX + R_ORB * math.sin(a2); wy = CY - R_ORB * math.cos(a2)
    s.append(f'<path d="M{CX},{CY} L{CX},{CY-R_ORB} A{R_ORB},{R_ORB} 0 0 1 {wx:.1f},{wy:.1f} Z" fill="{SPACE}" opacity=".07"/>')
    s.append(f'<g><line x1="{CX}" y1="{CY}" x2="{CX}" y2="{CY-R_ORB}" stroke="{SPACE}" stroke-width="2" opacity=".55">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="25s" repeatCount="indefinite"/>'
             f'</line><circle cx="{CX}" cy="{CY-R_ORB}" r="5" fill="{SPACE}">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="25s" repeatCount="indefinite"/>'
             f'</circle></g>'
             f'<text x="{CX+150}" y="{CY-R_ORB-14}" text-anchor="middle" fill="{SPACE}" font-family="{MONO}" font-size="8.5" font-weight="700">ROUND {k+1}</text>')
    # center engine
    s.append(f'<circle cx="{CX}" cy="{CY}" r="26" fill="{SPACE}" opacity=".9" stroke="#0b1120" stroke-width="2"/>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="34" fill="none" stroke="{SPACE}" stroke-width="1" opacity=".5"/>')
    s.append(f'<circle cx="{CX}" cy="{CY}" r="48" fill="none" stroke="{SPACE}" stroke-width="1" stroke-dasharray="2,5" opacity=".3"/>')
    s.append(f'<text x="{CX}" y="{CY+4}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="10" font-weight="800">SPACE</text>')
    s.append(f'<text x="{CX}" y="{CY+68}" text-anchor="middle" fill="{SPACE}" font-family="{FONT}" font-size="10.5" font-weight="700">RRP ENGINE</text>')
    s.append(f'<text x="{CX}" y="{CY+82}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8.5">1 turn = 25 rounds = 1 spec</text>')

    # series clusters — dots sized by open-ended share, twinkling in dispatch order
    rnd = random.Random("rrp-326")
    pos = {}
    for idx, (sid, name, rounds, oe, c) in enumerate(SERIES):
        a = math.radians(idx * (360 / 7))
        cx = CX + R_CL * math.sin(a); cy = CY - R_CL * math.cos(a)
        pos[sid] = (cx, cy)
        r_cl = 16 + oe * 1.15
        n = 5 + oe  # sampled probes (visible count)
        for _ in range(n):
            rr = r_cl * math.sqrt(rnd.random()) + 3
            aa = rnd.uniform(0, 2 * math.pi)
            px = cx + rr * math.cos(aa); py = cy + rr * math.sin(aa)
            t = (idx * (360 / 7) + rnd.uniform(-10, 10)) / 360 * 25
            s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="2.6" fill="{c}">'
                     f'<animate attributeName="fill-opacity" values=".18;1;.18" dur="25s" begin="-{t:.2f}s" repeatCount="indefinite"/>'
                     f'</circle>')
        # series label
        below = idx in (3, 4)
        ly = cy + (r_cl + 34 if below else -r_cl - 12)
        s.append(f'<text x="{cx:.0f}" y="{ly:.0f}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="10.5" font-weight="800">S{sid} · {esc(name)}</text>')
        s.append(f'<text x="{cx:.0f}" y="{ly+14:.0f}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8">{rounds} rounds · {oe} open-ended</text>')

    # dependency chain S1→S2→…→S7 (clockwise)
    for idx in range(6):
        (x1, y1), (x2, y2) = pos[idx + 1], pos[idx + 2]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        s.append(arrow(mx, my, x2, y2, TEXT4, marker="arwG", width=1.4, dashed=True, opacity=.7))
        s.append(f'<text x="{mx+8}" y="{my-8}" fill="{TEXT4}" font-family="{MONO}" font-size="7.5">depends_on</text>')

    # legend
    s.append(panel(96, 920, 816, 108, SPACE, "WHAT THE MOTION MEANS — THE PROTOCOL, ANIMATED",
                   [(SPACE, 10.5, "THE SWEEP = DISPATCH ORDER — the cursor advances one round per 14.4°; probes brighten exactly when the protocol reaches them."),
                    (TEXT2, 9.5, "One full turn = all 25 rounds = one elicitation session. The static wedge shows rounds already dispatched at load (1–5)."),
                    (TEXT2, 9.5, "Dashed arrows = the series dependency graph — S2 can't fire before S1, and so on around the constellation."),
                    (TEXT2, 9.5, "Star size & density = probe share (open-ended count per series: 6 · 15 · 8 · 6 · 20 · 6 · 6).")],
                   header_h=30, pad=14, line_h=19))
    # dispatch contract panel
    chain = "S1(3) → S2(5) → S3(4) → S4(3) → S5(4) → S6(3) → S7(3)"
    s.append(panel(96, 1056, 816, 92, EXT, "THE DISPATCH CONTRACT",
                   [(EXT, 10.5, f"{chain} = 25 rounds · 67 open-ended + 259 choice = 326 probes → artifacts → 6 export formats"),
                    (TEXT2, 9.5, "Series 5 (Technical Specifications) carries the heaviest probe load — implementation constraints dominate the elicitation."),
                    (TEXT2, 9.5, "Artifacts accumulate across rounds; exports render the completed session in every format below.")],
                   header_h=28, pad=14, line_h=20))
    # export formats
    fmts = ["JSON", "YAML", "Markdown", "HTML", "System Prompt", "TXT"]
    for i, f in enumerate(fmts):
        fx = 96 + i * 138 + 60
        s.append(f'<rect x="{fx-46}" y="1176" width="92" height="26" rx="13" fill="{SPACE}" opacity=".13"/>')
        s.append(f'<text x="{fx}" y="{1193}" text-anchor="middle" fill="{SPACE}" font-family="{MONO}" font-size="9" font-weight="700">{esc(f)}</text>')
    s.append(label(500, 1224, "6 EXPORT FORMATS — the constellation's output layer", 9.5, TEXT4))
    s.append(close_doc("the order of questions is not arbitrary — it is a dependency-respecting wave, and you are watching it fire"))
    return "\n".join(s)


# ── E-10 · The Attractor Basins (phase-space simulation) ───────────────
ATTR = [
    ("SPACE · IDEATION", SPACE, 500, 235, ["probe answers", "artifacts", "spec drafts"], "RRP sessions pull theory into shape"),
    ("RSIS3 · EXECUTION", RSIS, 300, 585, ["candidates", "pulses", "lessons"], "the evaluator gate pulls work in"),
    ("MYKB · MEMORY", MYKB, 700, 585, ["captures", "index builds", "KG edges"], "persistence pulls everything durable"),
    ("DASH · TELEMETRY", DASH, 500, 885, ["dashboard-data.json", "extrapolations", "success-rate"], "every pulse ends in a view"),
]
BASIN_DEFS = """<defs>
  <radialGradient id="basinS" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#fde68a" stop-opacity=".55"/><stop offset="60%" stop-color="#f59e0b" stop-opacity=".18"/><stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/></radialGradient>
  <radialGradient id="basinR" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#c7d2fe" stop-opacity=".55"/><stop offset="60%" stop-color="#818cf8" stop-opacity=".18"/><stop offset="100%" stop-color="#818cf8" stop-opacity="0"/></radialGradient>
  <radialGradient id="basinM" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#a5f3fc" stop-opacity=".55"/><stop offset="60%" stop-color="#22d3ee" stop-opacity=".18"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
  <radialGradient id="basinD" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#a7f3d0" stop-opacity=".55"/><stop offset="60%" stop-color="#10b981" stop-opacity=".18"/><stop offset="100%" stop-color="#10b981" stop-opacity="0"/></radialGradient>
</defs>"""


def attractor_basins():
    s = [open_doc("THE ATTRACTOR BASINS — A PHASE-SPACE PORTRAIT",
                  "Artifacts are states; loops are attractors. Every dot below traces a real maturation path toward the loop that consumes it")]
    s.insert(1, BASIN_DEFS)
    gid = {"SPACE": "basinS", "RSIS3": "basinR", "MYKB": "basinM", "DASH": "basinD"}
    for name, c, x, y, arts, tag in ATTR:
        s.append(f'<ellipse cx="{x}" cy="{y}" rx="265" ry="240" fill="url(#{gid[name.split()[0]]})" style="mix-blend-mode:screen"/>')

    # separatrix manifold — the diamond of balanced pull between attractors
    seps = [(400, 410), (400, 735), (600, 735), (600, 410)]
    spath = "M " + " L ".join(f"{a},{b}" for a, b in seps) + " Z"
    s.append(f'<path d="{spath}" fill="none" stroke="{TEXT4}" stroke-width="1.4" stroke-dasharray="5,6" opacity=".55"/>')
    s.append(label(500, 585, "SEPARATRIX — the boundary where pull is balanced", 8.5, TEXT4, italic=True))

    # attractors + wells
    for name, c, x, y, arts, tag in ATTR:
        s.append(f'<circle cx="{x}" cy="{y}" r="22" fill="{c}" opacity=".92" stroke="#0b1120" stroke-width="2"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="34" fill="none" stroke="{c}" stroke-width="1" opacity=".5"/>')
        s.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="9" font-weight="800">{esc(name.split()[0])}</text>')
        s.append(f'<text x="{x}" y="{y-40}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="11.5" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y-26}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8.5" font-style="italic">{esc(tag)}</text>')

    # trajectories — closed loops (motion = continuous circulation into the attractor)
    loops = [
        # (path, color, dur, label)
        (f"M 640,300 C 620,330 560,300 520,290 C 480,280 470,240 500,235 C 540,230 600,260 640,300 Z", SPACE, "9s", "spec drafts"),
        (f"M 180,560 C 230,540 240,470 260,470 C 280,470 320,540 300,585 C 290,620 200,600 180,560 Z", RSIS, "6s", "pulses"),
        (f"M 780,560 C 730,540 720,470 700,470 C 680,470 660,540 700,585 C 710,620 800,600 780,560 Z", RSIS, "7s", "lessons"),
        (f"M 420,300 C 450,330 520,310 560,300 C 580,290 560,240 500,235 C 460,230 400,270 420,300 Z", MYKB, "8s", "captures"),
        (f"M 640,800 C 620,770 560,790 520,800 C 480,810 480,860 500,885 C 540,900 600,870 640,800 Z", MYKB, "10s", "KG edges"),
        (f"M 760,700 C 720,720 700,640 690,620 C 680,600 600,620 700,585 C 730,575 780,660 760,700 Z", DASH, "5s", "dashboard-data"),
        (f"M 240,700 C 280,720 300,640 310,620 C 320,600 400,620 300,585 C 270,575 220,660 240,700 Z", DASH, "6s", "extrapolations"),
    ]
    for path, c, dur, name in loops:
        s.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="1.2" stroke-dasharray="2,4" opacity=".35"/>')
        s.append(f'<circle r="4.5" fill="{c}"><animateMotion dur="{dur}" repeatCount="indefinite" path="{path}"/></circle>')
        s.append(f'<circle r="8" fill="none" stroke="{c}" stroke-width="1" opacity=".5"><animateMotion dur="{dur}" repeatCount="indefinite" path="{path}"/></circle>')
        # label the loop near its start
        sx = path.split("M ")[1].split(",")[0]
        sy = path.split(",")[1].split(" ")[0]
        s.append(f'<text x="{float(sx)+8:.0f}" y="{float(sy)+14:.0f}" fill="{TEXT3}" font-family="{FONT}" font-size="7.5">{esc(name)}</text>')

    # cross-basin maturation flow (open paths, one shipment per cycle)
    flows = [
        (f"M 640,200 C 500,150 400,300 330,430", SPACE, "10s", "spec → implementation", "SPACE→RSIS3"),
        (f"M 330,640 C 430,760 560,740 660,640", RSIS, "14s", "lessons → consolidation", "RSIS3→MYKB"),
        (f"M 660,530 C 560,430 460,430 360,530", MYKB, "8s", "context retrieval :8765", "MYKB→RSIS3"),
    ]
    for path, c, dur, name, tag in flows:
        x1, y1 = path[2:].split(" ")[0].split(",")
        x2, y2 = path.rsplit(" ", 1)[1].split(",")
        s.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="7,5" opacity=".7" marker-end="{f"url(#arw{'S' if c==SPACE else 'R' if c==RSIS else 'M'})"}"/>')
        s.append(f'<circle r="5" fill="#fff"><animateMotion dur="{dur}" repeatCount="indefinite" path="{path}"/></circle>')
        s.append(f'<text x="{(float(x1)+float(x2))/2:.0f}" y="{(float(y1)+float(y2))/2:.0f}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="8.5" font-weight="700">{esc(name)}</text>')

    # velocity scale + legend
    s.append(panel(96, 1000, 816, 120, EXT, "READING THE PHASE PORTRAIT",
                   [(EXT, 10.5, "BASIN = the loop that dominates a region · SEPARATRIX = the unstable ridge where pull is balanced, so states wander."),
                    (TEXT2, 9.5, "COMET SPEED = maturation rate — pulses reach DASH in ~5s (seconds of real time), consolidation takes 14s (hours)."),
                    (TEXT2, 9.5, "DASHED CROSS-FLOWS = the one-way maturation pipeline: SPACE spec → RSIS3 implementation → MYKB consolidation, with retrieval back."),
                    (TEXT2, 9.5, "Each closed loop is one artifact class circulating into its home loop — motion is the system doing its job.")],
                   header_h=30, pad=14, line_h=19))
    s.append(close_doc("phase space asks one question of every artifact: which loop wins? — and the answer is visible as motion"))
    return "\n".join(s)


EXPERIMENTAL = {
    "basic-11-pulse-field.svg": pulse_field,
    "advanced-11-probe-constellation.svg": probe_constellation,
    "expert-10-attractor-basins.svg": attractor_basins,
}
