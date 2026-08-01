"""Round 6 Expert+ tier — cross-cutting and systems-theoretic (X+-01…X+-12).

Portrait 1000x1320. These diagrams read across all four runtimes at once:
causality, entropy fields, resilience, time-scale separation, feedback
topology, dependency lattices, resource flows, stability, phylogeny,
constraint hypergraphs — every claim traceable to the spec facts.
"""
import math
from round6 import *


# ── X+-01 · The Causality Graph ───────────────────────────────────────
def causality_graph():
    s = [doc("THE CAUSALITY GRAPH — WHAT CAUSES WHAT, WITH LAG",
             "Nine events, ten causal edges, four loops — the ecosystem as a directed graph of consequences")]
    nodes = [
        ("SPEC", 200, 210, SPACE), ("CANDIDATE", 460, 190, RSIS), ("VERDICT", 740, 190, EXT),
        ("PULSE", 620, 330, DASH), ("LESSON", 300, 340, MYKB), ("KG EDGE", 130, 440, MYKB),
        ("RETRIEVAL", 420, 480, MYKB), ("STRATEGY", 760, 480, RSIS), ("DASHBOARD", 850, 340, DASH),
    ]
    edges = [
        ("SPEC", "CANDIDATE", "L2 consumes", RSIS),
        ("CANDIDATE", "VERDICT", "spawn · 60s", EXT),
        ("VERDICT", "PULSE", "recorded", DASH),
        ("VERDICT", "STRATEGY", "fail → retry path", RSIS),
        ("PULSE", "DASHBOARD", "JSONL → snapshot", DASH),
        ("PULSE", "STRATEGY", "trends feed L3", RSIS),
        ("LESSON", "KG EDGE", "L3 consolidates", MYKB),
        ("KG EDGE", "RETRIEVAL", "indexed · :8765", MYKB),
        ("RETRIEVAL", "SPEC", "context seeds ideation", SPACE),
        ("STRATEGY", "CANDIDATE", "next session's goals", RSIS),
        ("DASHBOARD", "SPEC", "human reads → writes", SPACE),
    ]
    for name, x, y, c in nodes:
        s.append(f'<circle cx="{x}" cy="{y}" r="30" fill="{c}" opacity=".16" stroke="{c}" stroke-width="1.8"/>')
        s.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle" fill="{c}" font-family="{FONT}" font-size="8.5" font-weight="800">{esc(name)}</text>')
    for a, b, tag, c in edges:
        ax, ay = next((x, y) for n, x, y, cc in nodes if n == a)
        bx, by = next((x, y) for n, x, y, cc in nodes if n == b)
        s.append(f'<path d="M {ax} {ay} Q {(ax+bx)/2} {(ay+by)/2 - 34} {bx} {by}" fill="none" stroke="{c}" stroke-width="1.6" opacity=".75" marker-end="url(#arwG)"/>')
        s.append(label((ax + bx) / 2, (ay + by) / 2 - 40, tag, 7, TEXT4))
    # loop badges
    s.append(panel(60, 560, 880, 130, EXT, "THE FOUR LOOPS THE GRAPH CONTAINS", [
        (TEXT2, 10.5, "IMPROVEMENT — SPEC → CANDIDATE → VERDICT → STRATEGY → CANDIDATE (the gate in the middle)"),
        (TEXT2, 10.5, "MEMORY — LESSON → KG EDGE → RETRIEVAL → SPEC (consolidation + retrieval)"),
        (TEXT2, 10.5, "TELEMETRY — PULSE → DASHBOARD → SPEC (human in the loop) and PULSE → STRATEGY (no human)"),
        (TEXT4, 9.5, "Every loop is a cycle in the graph — causality is what makes the architecture recursive."),
    ], header_h=32, line_h=23))
    s.append(panel(60, 720, 880, 100, DASH, "EDGE LAGS ARE THE CADENCES", [
        (TEXT2, 10.5, "VERDICT → PULSE is ~instant; LESSON → KG EDGE is the L3 cycle; RETRIEVAL → SPEC is on-demand."),
        (TEXT2, 9.5, "The B-21 roster lists the periods; this graph shows which edges they belong to."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "NODE COLOUR = owning component; EDGE COLOUR = the component that performs the causation."),
        (TEXT2, 9.5, "READ AN EDGE AS 'A causes B after some lag' — the lag is labelled (spawn, L3 cycle, JSONL flush, on-demand)."),
        (TEXT2, 9.5, "THE FOUR LOOPS are the system's recursive heart — every diagram in this viewer sits inside one of them."),
    ], title="READING THE GRAPH"))
    s.append(end("causality, not topology, is the architecture — the graph says what makes what happen"))
    return "\n".join(s)


# ── X+-02 · The Entropy Field ─────────────────────────────────────────
def entropy_field():
    s = [doc("THE ENTROPY FIELD — UNCERTAINTY ACROSS THE WHOLE PLANE",
             "The E-13 curve promoted to a 2D field — every point on the semantic plane has an entropy")]
    s.append(f'<line x1="120" y1="870" x2="880" y2="870" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(label(500, 898, "X — THEORY ←———→ EXECUTION", 10, TEXT3, font=MONO))
    s.append(f'<line x1="120" y1="160" x2="120" y2="860" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(f'<text x="94" y="510" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700" transform="rotate(-90 94 510)">Y — SHORT-TERM ↑ · LONG-TERM ↓</text>')
    s.insert(1, '<defs><radialGradient id="efS" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f59e0b" stop-opacity=".55"/><stop offset="100%" stop-color="#f59e0b" stop-opacity=".05"/></radialGradient>'
                '<radialGradient id="efR" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#818cf8" stop-opacity=".55"/><stop offset="100%" stop-color="#818cf8" stop-opacity=".05"/></radialGradient>'
                '<radialGradient id="efM" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".55"/><stop offset="100%" stop-color="#22d3ee" stop-opacity=".05"/></radialGradient></defs>')
    # high-entropy zone (theory + short-term) vs low-entropy zone (memory)
    s.append(f'<ellipse cx="300" cy="300" rx="190" ry="150" fill="url(#efS)" style="mix-blend-mode:screen"/>')
    s.append(f'<ellipse cx="700" cy="320" rx="200" ry="140" fill="url(#efR)" style="mix-blend-mode:screen"/>')
    s.append(f'<ellipse cx="500" cy="660" rx="230" ry="160" fill="url(#efM)" style="mix-blend-mode:screen"/>')
    s.append(label(300, 210, "HIGH ENTROPY — ideation", 9.5, SPACE))
    s.append(label(700, 230, "MID ENTROPY — execution", 9.5, RSIS))
    s.append(label(500, 590, "LOW ENTROPY — memory", 9.5, MYKB))
    # contour lines (equal-entropy rings)
    for cx, cy, r, c in [(300, 300, 90, SPACE), (300, 300, 150, SPACE), (700, 320, 95, RSIS),
                         (700, 320, 155, RSIS), (500, 660, 110, MYKB), (500, 660, 180, MYKB)]:
        s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.72}" fill="none" stroke="{c}" stroke-width="1" opacity=".35" stroke-dasharray="3,5"/>')
    # artifacts as dots
    arts = [(250, 260, SPACE, "probe answers"), (360, 330, SPACE, "spec drafts"), (640, 300, RSIS, "candidates"),
            (700, 380, RSIS, "verdicts"), (760, 420, DASH, "pulses"), (560, 560, MYKB, "lessons"),
            (500, 700, MYKB, "KG edges"), (430, 660, MYKB, "wiki pages")]
    for x, y, c, tag in arts:
        s.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" stroke="#0b1120" stroke-width="1.4"/>')
        s.append(label(x + 14, y + 4, tag, 7.5, TEXT4, anchor="start"))
    # comet descending entropy gradient
    path = "M 250,260 C 340,300 430,400 500,560 C 520,610 510,660 500,700"
    s.append(f'<circle r="5" fill="#fff" stroke="#0b1120" stroke-width="1"><animateMotion dur="11s" repeatCount="indefinite" path="{path}"/></circle>')
    s.append(label(500, 795, "comet = an artifact rolling from high to low entropy — ideation → memory", 9, TEXT4))
    s.append(panel(60, 830, 880, 80, EXT, "FIELD READ", [
        (TEXT2, 10.5, "Entropy falls with execution (X→) and with time (Y↓) — the field's gradient is the system's purpose."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COMET = an artifact descending the entropy gradient (probe answer → KG edge); motion encodes maturation."),
        (TEXT2, 9.5, "ZONES = the three basins from A-24; CONTOURS = equal-entropy rings — the field, not the metaphor."),
        (TEXT2, 9.5, "ARTIFACT DOTS sit where they actually live: drafts top-left, verdicts mid, wiki pages bottom."),
        (TEXT2, 9.5, "This is the E-13 curve expanded across both axes — one dimension became the whole plane."),
    ], title="READING THE FIELD"))
    s.append(end("the whole system is one gradient — every artifact is rolling downhill toward memory"))
    return "\n".join(s)


# ── X+-03 · The Resilience Spectrum ───────────────────────────────────
def resilience_spectrum():
    s = [doc("THE RESILIENCE SPECTRUM — WHAT SURVIVES, WHAT DEGRADES",
             "Every dependency ranked from brittle to resilient, with its degradation ladder")]
    s.append(f'<line x1="90" y1="300" x2="910" y2="300" stroke="{BORDER2}" stroke-width="2.5" marker-end="url(#arwG)"/>')
    s.append(label(500, 335, "BRITTLE ←———→ RESILIENT", 10.5, TEXT2, font=MONO))
    items = [
        (":8765 PORT CLASH", 130, EXT, "documented but inevitable"),
        ("EVALUATOR TIMEOUT", 260, EXT, "fail → retry (≤5)"),
        ("PROVIDER OUTAGE", 400, SPACE, "7-provider failover"),
        ("WIKI CORRUPTION", 530, MYKB, "temporal restore"),
        ("DASHBOARD DOWN", 660, DASH, "buffer keeps flowing"),
        ("SPACE UI DOWN", 800, SPACE, "exports stay intact"),
    ]
    for name, x, c, tag in items:
        s.append(f'<circle cx="{x}" cy="300" r="13" fill="{c}" stroke="#0b1120" stroke-width="2"/>')
        s.append(label(x, 262, name, 8.5, c, font=MONO))
        s.append(label(x, 278, "▾", 7, TEXT4))
        s.append(label(x, 358, tag, 7.5, TEXT4))
    s.append(label(90, 396, "the ladder every item climbs: 1 · degrade gracefully → 2 · retry → 3 · restore from snapshot", 9, TEXT3, anchor="start"))
    s.append(panel(60, 430, 880, 160, EXT, "THE RULE THE SPECTRUM REVEALS", [
        (TEXT2, 10.5, "Resilience correlates with distance from the trust boundary: the evaluator and the port clash are the brittle ends."),
        (TEXT2, 10.5, "Everything with a restore path (wiki, index) sits right; everything with only a retry sits left."),
        (TEXT4, 9.5, "The A-22 table listed modes; this spectrum ranks them — the two views share all six dependencies."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 620, 880, 120, MYKB, "THE ONE THAT CANNOT DEGRADE", [
        (TEXT2, 10.5, "The wiki corpus has no degraded mode — corruption is restored, not tolerated. That is what 'source of truth' means here."),
        (TEXT2, 9.5, "Every other dependency can fail softly; memory cannot, because everything else depends on it."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "POSITION = assessed resilience from the failure modes (A-22); COLOUR = owning component."),
        (TEXT2, 9.5, "THE LADDER below the axis is the recovery grammar: degrade → retry → restore, in that order."),
        (TEXT2, 9.5, "Brittle is not bad — it is cheap: the port clash is the system's one known, documented, accepted weakness."),
    ], title="READING THE SPECTRUM"))
    s.append(end("resilience is a budget too — the system spends it on memory and spends it off the trust boundary"))
    return "\n".join(s)


# ── X+-04 · The Time-Scale Separation ─────────────────────────────────
def time_scale_separation():
    s = [doc("THE TIME-SCALE SEPARATION — FOUR CLOCKS, ONE LOG AXIS",
             "L1 · RRP · L3 · cross-session — separated by orders of magnitude, which is what makes them composable")]
    # log axis with four sine trains
    periods = [
        ("L1 · ACTION", 1, RSIS, "#818cf8"),
        ("RRP · ROUND", 12, SPACE, "#f59e0b"),
        ("L3 · CONSOLIDATION", 60, MYKB, "#22d3ee"),
        ("CROSS-SESSION", 3600, DASH, "#10b981"),
    ]
    y = 150
    for name, T, c, wc in periods:
        s.append(label(90, y + 16, name, 10, c, anchor="start", font=MONO))
        # time axis for this row: 0..3600s compressed
        s.append(f'<line x1="200" y1="{y+22}" x2="880" y2="{y+22}" stroke="{BORDER2}" stroke-width="1"/>')
        pts = []
        for t in range(0, 361, 4):
            v = math.sin(2 * math.pi * t / T) * 14
            pts.append(f"{200 + t * 680 / 360:.1f},{y + 22 - v:.1f}")
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{wc}" stroke-width="1.6" opacity=".9"/>')
        # period marker
        xp = 200 + T * 680 / 360 if T <= 360 else 880
        s.append(f'<line x1="{xp:.0f}" y1="{y+10}" x2="{xp:.0f}" y2="{y+34}" stroke="{wc}" stroke-width="2"/>')
        s.append(label(min(xp + 10, 890), y + 16, f"T={T}s" if T != 3600 else "T≈1hr", 8, c, anchor="start", font=MONO))
        y += 120
    s.append(label(540, y - 26, "← 1 second ───────────────────────────── 1 hour →", 8.5, TEXT3, font=MONO))
    s.append(panel(60, y, 880, 120, EXT, "WHY THE SEPARATION MATTERS", [
        (TEXT2, 10.5, "Each clock is ≥5× slower than the one above — fast loops finish many cycles inside slow ones, so they can be treated as stable."),
        (TEXT2, 10.5, "This is the adiabatic assumption: L1 sees L3 as frozen; L3 sees L1 as averaged. The ratios 12:1 and 5:1 are the separations."),
        (TEXT4, 9.5, "If the clocks converged, the loops would entangle and the recursion would become a single indistinguishable buzz."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "WAVE = one loop's activity over a shared 1-hour window; PERIOD MARK = its real cadence on the log axis."),
        (TEXT2, 9.5, "SEPARATION, NOT SYNCHRONY, is the design: overlapping periods would couple the loops destructively."),
        (TEXT2, 9.5, "The roster (B-21) listed periods; this map draws them to the same scale so the gaps become visible."),
    ], title="READING THE SEPARATION"))
    s.append(end("the system is stable because its clocks are far apart — order-of-magnitude spacing is the real architecture"))
    return "\n".join(s)


# ── X+-05 · The Semantic Hyperplane ───────────────────────────────────
def semantic_hyperplane():
    s = [doc("THE SEMANTIC HYPERPLANE — ONTOLOGY AS TERRAIN, PROJECTED",
             "Two semantic axes in isometric projection — elevation = footprint density, peaks = the three components")]
    # isometric grid
    s.append('<defs><linearGradient id="hpG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#334155" stop-opacity=".0"/><stop offset="100%" stop-color="#22d3ee" stop-opacity=".18"/></linearGradient></defs>')
    grid = []
    for i in range(11):
        x = 120 + i * 72
        grid.append(f'<line x1="{x}" y1="220" x2="{x-180}" y2="760" stroke="{BORDER2}" stroke-width="0.8" opacity=".5"/>')
        grid.append(f'<line x1="{x}" y1="220" x2="{x+180}" y2="760" stroke="{BORDER2}" stroke-width="0.8" opacity=".5"/>')
    s.append("\n".join(grid))
    # peaks (footprint ∝ height)
    peaks = [
        ("SPACE · theory", 300, 360, SPACE, 150, "ideation surface"),
        ("RSIS3 · execution", 700, 360, RSIS, 175, "engine surface"),
        ("MYKB · memory", 500, 640, MYKB, 205, "memory surface"),
    ]
    for name, x, y, c, h, tag in peaks:
        s.append(f'<ellipse cx="{x}" cy="{y}" rx="120" ry="66" fill="{c}" opacity=".35" style="mix-blend-mode:screen"/>')
        s.append(f'<ellipse cx="{x}" cy="{y}" rx="120" ry="66" fill="none" stroke="{c}" stroke-width="1.6" opacity=".8"/>')
        s.append(f'<path d="M {x-120} {y} C {x-60} {y-h}, {x+60} {y-h}, {x+120} {y}" fill="none" stroke="{c}" stroke-width="1.4" opacity=".6"/>')
        s.append(f'<text x="{x}" y="{y-h-14}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="11" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y-h+2}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7.5">{esc(tag)}</text>')
    # axis labels
    s.append(label(180, 780, "X — theory ⇄ execution", 9, TEXT3, font=MONO))
    s.append(label(760, 780, "Y — short-term ⇄ long-term", 9, TEXT3, font=MONO))
    s.append(label(500, 240, "Z (elevation) — footprint density: LOC + pages + probes at that semantic coordinate", 9, TEXT3))
    s.append(panel(60, 830, 880, 90, EXT, "PROJECTION, NOT TRUTH", [
        (TEXT2, 10.5, "Isometric projection loses real depth — but the A-24 spheres keep it. Here the point is the terrain, not the metric."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "ELEVATION = footprint density (LOC + corpus + probes); each component is a massif on the semantic plane."),
        (TEXT2, 9.5, "THE GRID = the two spectra from A-24; overlapping skirts show where two components share semantic ground."),
        (TEXT2, 9.5, "READ THE THREE PEAKS as the ontology terrain (B-10) with component weight drawn as height."),
    ], title="READING THE PLANE"))
    s.append(end("terrain is ontology you can walk — the hyperplane is the venn diagram with altitude"))
    return "\n".join(s)


# ── X+-06 · The Feedback Topology ─────────────────────────────────────
def feedback_topology():
    s = [doc("THE FEEDBACK TOPOLOGY — FOUR LOOPS, TWO SIGNS, ONE SYSTEM",
             "Every loop's sign, gain, and latency — stability is a property of the loop set, not the parts")]
    loops = [
        (SPACE, "IMPROVEMENT LOOP", "L2 → evaluator → L2", "NEGATIVE", "stabilising — the gate rejects, so change is damped", "-"),
        (MYKB, "MEMORY LOOP", "L3 → KG → retrieval → L1", "POSITIVE", "compounding — more memory, better actions, more memory", "+"),
        (DASH, "TELEMETRY LOOP", "pulse → dashboard → strategy", "NEUTRAL", "observational — unless a human acts, it changes nothing", "0"),
        (RSIS, "OUTER LOOP", "spec → candidate → pulse → lesson → KG → retrieval → spec", "POSITIVE", "the flywheel — every cycle should raise success rate", "+"),
    ]
    y = 128
    for accent, name, path, sign, desc, glyph in loops:
        s.append(panel(60, y, 880, 128, accent, f"{name} — {sign} FEEDBACK", [
            (TEXT2, 10.5, f"PATH —  {path}"),
            (TEXT2, 9.5, desc),
        ], header_h=32, pad=14, line_h=24))
        s.append(f'<circle cx="930" cy="{y+36}" r="22" fill="none" stroke="{accent}" stroke-width="2"/>')
        s.append(f'<text x="930" y="{y+42}" text-anchor="middle" fill="{accent}" font-family="{MONO}" font-size="17" font-weight="800">{glyph}</text>')
        y += 158
    s.append(panel(60, y, 880, 110, EXT, "THE SIGN RULE", [
        (EXT, 10.5, "Negative feedback = the evaluator: it exists to oppose change, which is why the system stays stable while improving."),
        (TEXT2, 9.5, "Positive loops are the growth story; the negative loop is the brake — the net sign is the system's character."),
    ], header_h=32, line_h=24))
    s.append(panel(60, y + 130, 880, 80, MYKB, "LATENCY IS THE GAIN", [
        (TEXT2, 10.5, "A loop's effective gain falls as its period rises (X+-04) — slow loops damp themselves by being slow."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "SIGNS = − stabilising · + compounding · 0 observational; the glyph circle repeats the sign."),
        (TEXT2, 9.5, "THE CAUSALITY GRAPH (X+-01) drew the edges; this map labels each cycle's sign and role."),
        (TEXT2, 9.5, "STABILITY IS EMERGENT: no single loop is the system — the set of four, with signs and lags, is."),
    ], title="READING THE TOPOLOGY"))
    s.append(end("feedback is the system's personality — one brake, two engines, one mirror"))
    return "\n".join(s)


# ── X+-07 · The Dependency Lattice ────────────────────────────────────
def dependency_lattice():
    s = [doc("THE DEPENDENCY LATTICE — THE PARTIAL ORDER OF ARTIFACTS",
             "What must exist before what — a Hasse diagram of the ecosystem's production rules")]
    levels = [
        [("SPACE INIT", 200, SPACE), ("PROBE", 500, SPACE), ("CAPTURE HOOK", 800, MYKB)],
        [("ANSWER", 300, SPACE), ("TRANSCRIPT", 640, MYKB)],
        [("SPEC", 470, SPACE), ("LESSON", 780, MYKB)],
        [("CANDIDATE", 240, RSIS), ("KG EDGE", 720, MYKB)],
        [("VERDICT", 380, EXT), ("INDEX", 850, MYKB)],
        [("PULSE", 500, DASH)],
        [("RETRIEVAL", 500, MYKB)],
    ]
    y0 = 120
    for li, level in enumerate(levels):
        yy = y0 + li * 104
        for name, x, c in level:
            s.append(f'<circle cx="{x}" cy="{yy}" r="24" fill="{c}" opacity=".16" stroke="{c}" stroke-width="1.8"/>')
            s.append(f'<text x="{x}" y="{yy}" text-anchor="middle" dominant-baseline="middle" fill="{c}" font-family="{FONT}" font-size="8" font-weight="800">{esc(name)}</text>')
    edges = [
        (0, 0, 1, 0), (0, 1, 1, 0), (0, 1, 2, 0), (0, 2, 1, 1),
        (1, 0, 2, 0), (1, 1, 2, 1), (2, 0, 3, 0), (2, 1, 3, 1),
        (3, 0, 4, 0), (3, 1, 4, 1), (4, 0, 5, 0), (4, 1, 5, 0),
        (5, 0, 6, 0),
    ]
    for a, ai, b, bi in edges:
        ax, ay = levels[a][ai][0], y0 + a * 104
        bx, by = levels[b][bi][0], y0 + b * 104
        s.append(f'<line x1="{ax}" y1="{ay+24}" x2="{bx}" y2="{by-24}" stroke="{BORDER2}" stroke-width="1.4" marker-end="url(#arwG)"/>')
    s.append(label(500, 62, "a lattice reads UPWARD: nothing exists until everything below it exists", 9.5, TEXT3, italic=True))
    s.append(panel(60, 880, 880, 100, EXT, "WHAT THE LATTICE FORBIDS", [
        (TEXT2, 10.5, "No SKIPPING: a candidate without a spec is a violation; a KG edge without a lesson is a violation."),
        (TEXT2, 9.5, "The conservation laws (E-24) are the lattice's enforcement — parentless artifacts are the forbidden nodes."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "NODE COLOUR = owning component; ARROWS = 'is produced from' — the partial order, not a timeline."),
        (TEXT2, 9.5, "LEVELS ARE RANKS: two nodes on the same level are independent — capture hooks and probes never meet."),
        (TEXT2, 9.5, "RETRIEVAL tops the lattice because everything below it exists to make it possible."),
    ], title="READING THE LATTICE"))
    s.append(end("production rules are a partial order — the lattice is the system's grammar of what comes first"))
    return "\n".join(s)


# ── X+-08 · The Resource Flow ─────────────────────────────────────────
def resource_flow():
    s = [doc("THE RESOURCE FLOW — TOKENS, TIME, DISK, CPU",
             "Four currencies the ecosystem spends — where they enter, where they pool, where they sink")]
    currencies = [
        (SPACE, "TOKENS", "7 LLM providers", "SPACE ideation", "the only paid currency", 300),
        (RSIS, "TIME", "loops + budgets", "L1 steps · eval 60s", "wall-clock, capped per stage", 230),
        (MYKB, "DISK", "wiki + JSONL + index", "58MB corpus · 2,436 files", "git-tracked, snapshot-safe", 190),
        (EXT, "CPU", "evaluator spawn", "60s subprocess · read-only", "isolated, never shared", 150),
    ]
    y = 128
    for accent, name, source, sink, note, flow_w in currencies:
        s.append(panel(60, y, 880, 92, accent, name, [
            (TEXT2, 10, f"SOURCE —  {source}     →     SINK —  {sink}"),
            (TEXT4, 9, note),
        ], header_h=30, pad=14, line_h=21))
        s.append(f'<rect x="330" y="{y+62}" width="{flow_w}" height="10" rx="5" fill="{accent}" opacity=".85"/>')
        s.append(label(330 + flow_w + 10, y + 71, "relative weight", 7.5, TEXT4, anchor="start"))
        y += 120
    s.append(panel(60, y, 880, 130, EXT, "WHERE THE CURRENCIES MEET", [
        (TEXT2, 10.5, "TOKENS buy answers; answers cost TIME to evaluate; TIME is spent to write DISK; DISK is verified by CPU at every spawn."),
        (TEXT2, 10.5, "The budget caps (E-22) are the exchange rates: 60s of CPU per verdict, 120s per L1 step, ~58MB of wiki."),
        (TEXT4, 9.5, "Pulses are nearly free (JSONL append); consolidation is the expensive buy — which is why it is batched."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "BAR WIDTH = relative consumption — tokens flow widest, CPU is the narrowest and most guarded."),
        (TEXT2, 9.5, "EVERY CURRENCY HAS A SINK: no resource flows in a circle without being spent — budgets are conservation laws (E-24)."),
        (TEXT2, 9.5, "The four bands are the ecosystem's economy — the dashboard is the one place all four are visible at once."),
    ], title="READING THE FLOW"))
    s.append(end("the system's economy: pay tokens to think, spend time to judge, invest disk to remember, guard CPU to trust"))
    return "\n".join(s)


# ── X+-09 · The Meta-Stability Map ────────────────────────────────────
def meta_stability_map():
    s = [doc("THE META-STABILITY MAP — EVERY LOOP'S STABILITY REGIME",
             "Period × damping phase plane — where each loop sits, and what moves it")]
    s.append(f'<line x1="120" y1="760" x2="880" y2="760" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)"/>')
    s.append(label(500, 790, "PERIOD — FAST ←———→ SLOW", 10, TEXT3, font=MONO))
    s.append(f'<line x1="120" y1="170" x2="120" y2="750" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)"/>')
    s.append(f'<text x="96" y="460" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700" transform="rotate(-90 96 460)">DAMPING — OSCILLATORY ↑ · DAMPED ↓</text>')
    # stability regions
    s.append(f'<path d="M 140 720 L 300 720 L 260 500 L 150 500 Z" fill="{DASH}" opacity=".08"/>')
    s.append(f'<path d="M 330 470 L 600 470 L 560 260 L 340 260 Z" fill="{SPACE}" opacity=".08"/>')
    s.append(f'<path d="M 620 240 L 860 240 L 840 140 L 640 140 Z" fill="{MYKB}" opacity=".08"/>')
    s.append(label(210, 640, "STABLE · damped", 9, DASH))
    s.append(label(460, 380, "LIMIT-CYCLE · oscillatory", 9, SPACE))
    s.append(label(750, 200, "SLOW · quasi-static", 9, MYKB))
    loops = [
        ("L1 · 1s", 200, 620, RSIS), ("TELEMETRY · 1s", 230, 560, DASH),
        ("RRP · 12s", 460, 350, SPACE), ("EVALUATOR · burst", 300, 260, EXT),
        ("RETRIEVAL · on-demand", 520, 520, MYKB), ("L3 · 60s", 760, 190, MYKB),
    ]
    for name, x, y, c in loops:
        s.append(f'<circle cx="{x}" cy="{y}" r="16" fill="{c}" stroke="#0b1120" stroke-width="2"/>')
        s.append(label(x, y + 34, name, 8, c, font=MONO))
    s.append(panel(60, 830, 880, 90, EXT, "THE REGIME READING", [
        (TEXT2, 10.5, "Fast loops sit in the damped zone (stable); the RRP lives in the limit-cycle zone (its 12s period IS the oscillation); L3 is quasi-static."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "ZONES = dynamic regimes on the period × damping plane; NODES = the real loops from the roster (B-21)."),
        (TEXT2, 9.5, "THE EVALUATOR IS THE ODD NODE: short period, high damping — a burst, not a clock; it is the brake from X+-06."),
        (TEXT2, 9.5, "STABILITY IS NOT UNIFORM: the system is stable because fast parts damp and slow parts barely move (X+-04)."),
    ], title="READING THE MAP"))
    s.append(end("each loop has a personality — damped, cycling, or glacial — and the mix is what keeps the recursion sane"))
    return "\n".join(s)


# ── X+-10 · The Origin Phylogeny ──────────────────────────────────────
def origin_phylogeny():
    s = [doc("THE ORIGIN PHYLOGENY — WHERE EVERYTHING CAME FROM",
             "Artifact ancestry, not git history — what in this system derives from what")]
    # tree
    root = (500, 130)
    s.append(f'<circle cx="{root[0]}" cy="{root[1]}" r="30" fill="{EXT}" opacity=".16" stroke="{EXT}" stroke-width="1.8"/>')
    s.append(f'<text x="500" y="134" text-anchor="middle" fill="{EXT}" font-family="{FONT}" font-size="8" font-weight="800">RRP\nORIGIN</text>')
    branch1 = [(500, 220, SPACE, "SPEC ENGINE"), (500, 340, SPACE, "PROBE FRAMEWORK · 326")]
    branch2 = [(620, 220, RSIS, "IMPROVEMENT LOOP"), (620, 340, RSIS, "EVALUATOR · IMMUTABLE"), (760, 460, EXT, "SHA-256 GATE")]
    branch3 = [(380, 220, MYKB, "WIKI CORPUS"), (380, 340, MYKB, "CAPTURE + KG"), (260, 460, MYKB, "TF-IDF · RETRIEVAL :8765")]
    for x, y, c, name in branch1 + branch2 + branch3:
        s.append(f'<circle cx="{x}" cy="{y}" r="30" fill="{c}" opacity=".16" stroke="{c}" stroke-width="1.8"/>')
        s.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle" fill="{c}" font-family="{FONT}" font-size="7.5" font-weight="800">{esc(name)}</text>')
    edges = [
        ((500, 130), (500, 190)), ((500, 130), (620, 190)), ((500, 130), (380, 190)),
        ((500, 220), (500, 310)), ((620, 220), (620, 310)), ((380, 220), (380, 310)),
        ((620, 340), (760, 430)), ((380, 340), (260, 430)),
        ((500, 340), (500, 500)), ((620, 340), (620, 500)), ((380, 340), (380, 500)),
    ]
    for a, b in edges:
        s.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{BORDER2}" stroke-width="1.5" marker-end="url(#arwG)"/>')
    # merged descendants
    merges = [(500, 540, DASH, "DASHBOARD — EMBEDS ALL"), (620, 540, RSIS, "L2/L3 — CONSUMES SPECS"), (380, 540, MYKB, "SERVES RETRIEVAL")]
    for x, y, c, name in merges:
        s.append(f'<rect x="{x-86}" y="{y-22}" width="172" height="44" rx="10" fill="{c}" opacity=".16" stroke="{c}" stroke-width="1.8"/>')
        s.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="8.5" font-weight="800">{esc(name)}</text>')
    s.append(f'<line x1="500" y1="500" x2="500" y2="518" stroke="{BORDER2}" stroke-width="1.5" marker-end="url(#arwG)"/>')
    s.append(f'<line x1="620" y1="500" x2="620" y2="518" stroke="{BORDER2}" stroke-width="1.5" marker-end="url(#arwG)"/>')
    s.append(f'<line x1="380" y1="500" x2="380" y2="518" stroke="{BORDER2}" stroke-width="1.5" marker-end="url(#arwG)"/>')
    s.append(panel(60, 600, 880, 120, EXT, "WHAT THIS IS NOT", [
        (TEXT2, 10.5, "This is artifact ancestry (what derives from what in the current codebase), not a claim about commit history."),
        (TEXT2, 10.5, "The B-24 timeline is the deployment story; this tree is the derivation story — they are different questions."),
        (TEXT4, 9.5, "Honest limit: exact parentage of early commits is not reconstructed here — the tree shows structural descent."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 750, 880, 80, MYKB, "THE MERGE POINT", [
        (TEXT2, 10.5, "All three lines converge in the dashboard — the ecosystem's single integration node (B-18)."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "NODES = artifact families; ARROWS = derived from; the tree reads top-down from the RRP origin."),
        (TEXT2, 9.5, "COLOUR = the component that owns the family today — descent and ownership are independent."),
        (TEXT2, 9.5, "THE THREE MERGED DESCENDANTS are today's runtimes: dashboard, engine consumers, retrieval service."),
    ], title="READING THE TREE"))
    s.append(end("every artifact has an ancestor — the phylogeny is the family tree of the ecosystem's ideas"))
    return "\n".join(s)


# ── X+-11 · The Constraint Hypergraph ─────────────────────────────────
def constraint_hypergraph():
    s = [doc("THE CONSTRAINT HYPERGRAPH — CONSTRAINTS AS BUBBLES OVER ARTIFACTS",
             "Six constraints, each binding several artifacts at once — a graph, but with multi-way edges")]
    nodes = [
        ("SPEC", 300, 220, SPACE), ("CANDIDATE", 470, 240, RSIS), ("VERDICT", 650, 230, EXT),
        ("PULSE", 720, 380, DASH), ("WIKI", 260, 420, MYKB), ("INDEX", 420, 460, MYKB),
        ("KG EDGE", 320, 600, MYKB), ("DASH-DATA", 640, 560, DASH), ("EXPORTS", 520, 620, SPACE),
    ]
    for name, x, y, c in nodes:
        s.append(f'<circle cx="{x}" cy="{y}" r="24" fill="{c}" opacity=".16" stroke="{c}" stroke-width="1.8"/>')
        s.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle" fill="{c}" font-family="{FONT}" font-size="7.5" font-weight="800">{esc(name)}</text>')
    bubbles = [
        (("CANDIDATE", "VERDICT"), 560, 160, EXT, "≤5 / session · 60s cap"),
        (("SPEC", "EXPORTS"), 390, 160, SPACE, "6 format contract"),
        (("PULSE", "DASH-DATA"), 700, 500, DASH, "append-only · ~1s flush"),
        (("WIKI", "INDEX", "KG EDGE"), 330, 520, MYKB, "git temporal · source of truth"),
        (("DASH-DATA", "DASH-DATA"), 640, 560, DASH, "single dashboard rule"),
    ]
    for group, bx, by, c, tag in bubbles:
        xs = [n[1] for n in nodes if n[0] in group]
        ys = [n[2] for n in nodes if n[0] in group]
        n = len(xs)
        cx0 = (min(xs) + max(xs)) / 2
        cy0 = (min(ys) + max(ys)) / 2
        if n == 1:
            rx, ry = 74, 74
        elif n == 2:
            rx, ry = (max(xs) - min(xs)) / 2 + 62, 92
        else:
            rx, ry = 200, 118
        s.append(f'<ellipse cx="{cx0}" cy="{cy0}" rx="{rx}" ry="{ry}" fill="none" stroke="{c}" stroke-width="1.6" stroke-dasharray="5,4" opacity=".85"/>')
        s.append(label(cx0, cy0 + ry - 12, tag, 7.5, c))
    s.append(panel(60, 720, 880, 120, EXT, "WHY HYPEREDGES, NOT ARROWS", [
        (TEXT2, 10.5, "A constraint is not an edge between two things — it binds a SET: the eval budget binds candidate AND verdict together."),
        (TEXT2, 10.5, "The B-22 ledger showed who touches which store; this graph shows which stores a rule touches at once."),
        (TEXT4, 9.5, "Violating any bubble breaks the invariant ledger (E-14) — the hypergraph is the invariants' geometry."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "BUBBLES = constraints (multi-way relations); DOTS = artifacts; an artifact in many bubbles obeys many rules."),
        (TEXT2, 9.5, "DASHED LINES = the boundary is the rule, not a data flow — bubbles enclose, arrows would mislead."),
        (TEXT2, 9.5, "THE WIKI BUBBLE is the largest because memory is the most-constrained store (write path + index + snapshots)."),
    ], title="READING THE HYPERGRAPH"))
    s.append(end("constraints are shapes, not lines — the system's rules are regions that several things must satisfy together"))
    return "\n".join(s)


# ── X+-12 · The Ω Overview ────────────────────────────────────────────
def omega_overview():
    s = [doc("THE Ω OVERVIEW — THE WHOLE SYSTEM ON ONE PLANE",
             "The capstone: every runtime, artifact family, and handoff on the two semantic axes — the static sibling of the X++ graph")]
    s.append(f'<line x1="120" y1="880" x2="880" y2="880" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(label(500, 908, "X — THEORY ←———→ EXECUTION", 10, TEXT3, font=MONO))
    s.append(f'<line x1="120" y1="170" x2="120" y2="870" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(f'<text x="94" y="520" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700" transform="rotate(-90 94 520)">Y — SHORT-TERM ↑ · LONG-TERM ↓</text>')
    # runtime anchors (big) + artifact families (small)
    anchors = [
        ("SPACE", 320, 290, SPACE), ("RSIS3", 680, 310, RSIS), ("MYKB", 500, 660, MYKB), ("DASH", 830, 560, DASH),
    ]
    fams = [
        ("probes", 260, 220, SPACE), ("specs", 380, 250, SPACE), ("candidates", 620, 260, RSIS),
        ("verdicts", 760, 300, EXT), ("pulses", 780, 440, DASH), ("lessons", 420, 540, MYKB),
        ("KG edges", 360, 660, MYKB), ("wiki", 560, 740, MYKB), ("dashboard-data", 810, 620, DASH),
    ]
    for name, x, y, c in anchors:
        s.append(f'<circle cx="{x}" cy="{y}" r="44" fill="{c}" opacity=".2" stroke="{c}" stroke-width="2.4"/>')
        s.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle" fill="{c}" font-family="{FONT}" font-size="12" font-weight="800">{esc(name)}</text>')
    for name, x, y, c in fams:
        s.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{c}" stroke="#0b1120" stroke-width="1.4"/>')
        s.append(label(x, y + 26, name, 7.5, TEXT4))
    # handoff edges
    handoffs = [
        ((320, 290), (680, 310), SPACE, "specs"), ((680, 310), (830, 560), DASH, "pulses"),
        ((500, 660), (680, 310), MYKB, "retrieval"), ((680, 310), (500, 660), MYKB, "capture"),
        ((830, 560), (320, 290), DASH, "launch"),
    ]
    for a, b, c, tag in handoffs:
        s.append(f'<path d="M {a[0]} {a[1]} Q {(a[0]+b[0])/2} {(a[1]+b[1])/2 - 50} {b[0]} {b[1]}" fill="none" stroke="{c}" stroke-width="2" opacity=".75" marker-end="url(#arwG)" stroke-dasharray="7,5"/>')
        s.append(label((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - 56, tag, 8, c))
    s.append(label(500, 70, "the Ω graph, drawn statically — open the X++ tab for the interactive version", 9, TEXT3, italic=True))
    s.append(panel(60, 945, 880, 70, EXT, "KEY NUMBERS AT A GLANCE", [
        (TEXT2, 10.5, "4 runtimes · 6 handoffs · 9 artifact families · 2 spectra · 12:1 & 25:1 ratios · 1 trust boundary"),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "BIG CIRCLES = the four runtimes (r ∝ footprint); SMALL DOTS = artifact families where they live on the spectra."),
        (TEXT2, 9.5, "DASHED ARCS = the six handoffs (B-17) drawn as geometry — every family sits inside its owner's basin."),
        (TEXT2, 9.5, "This is the whole ecosystem in one view: the X++ graph is this picture with hover, click, and a λ time slider."),
    ], title="READING THE Ω"))
    s.append(end("Ω is the last diagram — every other graph in this viewer is a zoom into this one plane"))
    return "\n".join(s)


EXPERT_PLUS = {
    "expert-plus-01-causality-graph.svg": causality_graph,
    "expert-plus-02-entropy-field.svg": entropy_field,
    "expert-plus-03-resilience-spectrum.svg": resilience_spectrum,
    "expert-plus-04-time-scale-separation.svg": time_scale_separation,
    "expert-plus-05-semantic-hyperplane.svg": semantic_hyperplane,
    "expert-plus-06-feedback-topology.svg": feedback_topology,
    "expert-plus-07-dependency-lattice.svg": dependency_lattice,
    "expert-plus-08-resource-flow.svg": resource_flow,
    "expert-plus-09-meta-stability-map.svg": meta_stability_map,
    "expert-plus-10-origin-phylogeny.svg": origin_phylogeny,
    "expert-plus-11-constraint-hypergraph.svg": constraint_hypergraph,
    "expert-plus-12-omega-overview.svg": omega_overview,
}
