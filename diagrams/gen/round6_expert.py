"""Round 6 Expert tier — internals, pipelines, meta, doubled (E-13…E-24).

Portrait 1000x1320. Grounded in real invariants: evaluator SHA-256
immutability, 326 probes / 7 series / 6 formats / 7 providers, 12:1 and
25:1 ratios, budget caps, the single-dashboard rule, git temporal layer.
"""
from round6 import *


# ── E-13 · The Information Flow ───────────────────────────────────────
def information_flow():
    s = [doc("THE INFORMATION FLOW — ENTROPY ALONG THE LIFECYCLE",
             "How uncertain each artifact is before it is read — and where the gate drops entropy")]
    # entropy curve: y = uncertainty, x = lifecycle stage
    pts = [(130, 300), (240, 340), (355, 265), (470, 225), (585, 175), (700, 130), (815, 92), (900, 80)]
    curve = "M " + " L ".join(f"{x},{y}" for x, y in pts)
    s.append(f'<path d="{curve}" fill="none" stroke="{EXT}" stroke-width="2.5" opacity=".85"/>')
    s.append(f'<path d="{curve} L 900 400 L 130 400 Z" fill="{EXT}" opacity=".07"/>')
    # axes
    s.append(f'<line x1="100" y1="420" x2="920" y2="420" stroke="{BORDER2}" stroke-width="1.5" marker-end="url(#arwG)"/>')
    s.append(label(500, 448, "LIFECYCLE — IDEA → SPEC → CANDIDATE → GATE → PULSE → LESSON → KG EDGE", 9.5, TEXT3, font=MONO))
    s.append(f'<line x1="100" y1="80" x2="100" y2="420" stroke="{BORDER2}" stroke-width="1.5" marker-end="url(#arwG)"/>')
    s.append(f'<text x="74" y="250" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700" transform="rotate(-90 74 250)">ENTROPY — UNCERTAINTY BEFORE READING</text>')
    artifacts = [
        ("IDEA", 130, SPACE, "many possible answers"),
        ("SPEC", 240, SPACE, "structure imposed"),
        ("CANDIDATE", 355, RSIS, "one implementation"),
        ("GATE", 470, EXT, "entropy cliff"),
        ("PULSE", 585, DASH, "noisy but cheap"),
        ("LESSON", 700, MYKB, "distilled"),
        ("KG EDGE", 815, MYKB, "minimal uncertainty"),
    ]
    for name, x, c, tag in artifacts:
        y = next(py for px, py in pts if px == x)
        s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" stroke="#0b1120" stroke-width="2"/>')
        s.append(label(x, y - 22, name, 9, c, font=MONO))
        s.append(label(x, y + 22, tag, 7.5, TEXT4))
    # gate annotation
    s.append(f'<line x1="470" y1="225" x2="470" y2="60" stroke="{EXT}" stroke-width="1" stroke-dasharray="4,4" opacity=".6"/>')
    s.append(label(470, 52, "EVALUATOR — entropy is spent here: rejection is information", 8.5, EXT))
    s.append(panel(60, 520, 880, 150, EXT, "WHERE INFORMATION ACTUALLY MOVES", [
        (TEXT2, 10.5, "The cascade loses entropy on purpose: a spec is less surprising than an idea; a KG edge is nearly deterministic."),
        (TEXT2, 10.5, "The gate is the one place entropy can INCREASE — a rejected candidate reopens the idea space for L2's next attempt."),
        (TEXT4, 9.5, "Pulses look low-entropy but are high-volume — their information is in the trend, not the event (the extrapolator's job)."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 700, 880, 130, RSIS, "MEASURED, NOT METAPHORICAL", [
        (TEXT2, 10.5, "Entropy here ≈ the size of the answer space: probes → 326 answers → 1 spec; candidates → ≤5 verdicts → 1 applied diff."),
        (TEXT2, 10.5, "The ratios are entropy numbers in disguise — 25:1 means the spec process spends 24 rounds eliminating alternatives."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "CURVE = uncertainty before each artifact is read; the downward slope is the system's whole reason to exist."),
        (TEXT2, 9.5, "COLOURED DOTS = owning component; the gate is pink because it is the only node that can raise entropy."),
        (TEXT2, 9.5, "THE DASHED LINE = the gate's axis: rejection is not failure, it is measured information spent to guide the next candidate."),
    ], title="READING THE FLOW"))
    s.append(end("the system is an entropy engine — it converts 326 possibilities into one retrievable fact"))
    return "\n".join(s)


# ── E-14 · The Invariant Ledger ───────────────────────────────────────
def invariant_ledger():
    s = [doc("THE INVARIANT LEDGER — WHAT NEVER CHANGES",
             "The constants the whole ecosystem is built around, what enforces each, and what would break it")]
    rows = [
        ("EVALUATOR IMMUTABILITY", "SHA-256 digest · read-only mount", "self-improvement must never rewrite its judge", EXT),
        ("326 PROBES · 7 SERIES", "prompt-framework/ is versioned", "the RRP input surface is fixed by design", SPACE),
        ("6 EXPORT FORMATS", "exports/ formatters", "consumers depend on the format set", SPACE),
        ("7 LLM PROVIDERS", "provider factory", "no single provider is load-bearing", SPACE),
        ("12:1 · 25:1 RATIOS", "loop clocks · dashboard telemetry", "the cadence relationships are measured, not tuned", DASH),
        ("WIKI IS THE SOURCE OF TRUTH", "capture hooks + git", "any writer that bypasses capture corrupts memory", MYKB),
        ("ONE DASHBOARD", "root index.html redirect", "standalone dashboards are not added", DASH),
        ("PORT MAP :9000 :8765 :8888 :8899", "config.js + server bindings", "clients hard-code the contract", MYKB),
    ]
    s.append(table(60, 130, [230, 330, 320], ["INVARIANT", "ENFORCED BY", "WOULD BREAK IF…"],
                  [(r[0], r[1], (r[2], r[3])) for r in rows],
                  row_h=56, header_h=38))
    s.append(panel(60, 620, 880, 130, EXT, "THE POINT OF THE LEDGER", [
        (TEXT2, 10.5, "Invariants are the architecture's axioms — you can change anything else and the system still means the same thing."),
        (TEXT2, 10.5, "Most are enforced by structure (spawn, redirect, factory), not by policy — nobody can violate them by accident."),
        (TEXT4, 9.5, "The wiki-as-truth invariant is the one with teeth: violating it corrupts memory for every future session."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 780, 880, 100, MYKB, "INVARIANTS VS THE DOUBLING PASS", [
        (TEXT2, 10.5, "Every diagram in this viewer is an observation of these constants — the ledger is the theory, the diagrams are the data."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOUR = the component that guarantees the invariant — pink for the trust boundary, amber SPACE, green dashboard, cyan MyKB."),
        (TEXT2, 9.5, "ENFORCED BY is a mechanism, not a wish: digests, factories, redirects, bindings — all visible in the code."),
        (TEXT2, 9.5, "WOULD BREAK IF… is the failure clause — every invariant has one, which is what makes it testable."),
    ], title="READING THE LEDGER"))
    s.append(end("if two diagrams disagree, one of them is wrong — the ledger is the tiebreaker"))
    return "\n".join(s)


# ── E-15 · The Fault Tree ─────────────────────────────────────────────
def fault_tree():
    s = [doc("THE FAULT TREE — HOW THE SYSTEM BREAKS, TOP-DOWN",
             "One top event, five branches, AND/OR logic — the failure cascade (A-22) as a tree")]
    s.append(panel(330, 120, 340, 64, EXT, "TOP EVENT — SYSTEM DEGRADED", [
        (TEXT2, 9.5, "no dependency is fatal, but combinations stack"),
    ], header_h=30, line_h=20))
    s.append(arrow(500, 184, 500, 210, GRAY, "arwG", 2, opacity=0.6))
    s.append(f'<text x="540" y="212" fill="{EXT}" font-family="{MONO}" font-size="8.5" font-weight="700">OR</text>')
    branches = [
        (140, 260, "MYKB DAEMON DOWN", "retrieval fails · :8765", MYKB),
        (330, 260, "EVALUATOR TIMEOUT", "no verdict in 60s", EXT),
        (520, 260, "PROVIDER OUTAGE", "probe answers fail", SPACE),
        (700, 260, "WIKI CORRUPTION", "search returns garbage", MYKB),
        (890, 260, "PORT CLASH :8765", "rack vs daemon bind", DASH),
    ]
    for x, y, name, tag, c in branches:
        s.append(f'<line x1="500" y1="222" x2="{x}" y2="252" stroke="{BORDER2}" stroke-width="1.4"/>')
        s.append(f'<rect x="{x-92}" y="{y}" width="184" height="56" rx="10" fill="{c}" opacity=".14" stroke="{c}" stroke-width="1.4"/>')
        s.append(f'<text x="{x}" y="{y+23}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="9" font-weight="700">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y+41}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="7.5">{esc(tag)}</text>')
    s.append(f'<text x="540" y="352" fill="{EXT}" font-family="{MONO}" font-size="8.5" font-weight="700">AND / OR GATES BELOW</text>')
    leaves = [
        (60, 380, "daemon not started", "misconfig", MYKB, "OR"),
        (60, 440, "port already bound", "rack won", MYKB, "OR"),
        (330, 380, "evaluator hung", "provider latency", EXT, "OR"),
        (330, 440, "candidate too large", "prompt drift", EXT, "OR"),
        (520, 380, "API key invalid", "rate limited", SPACE, "OR"),
        (520, 440, "model deprecated", "factory not refreshed", SPACE, "OR"),
        (700, 380, "capture wrote bad page", "linter missed", MYKB, "OR"),
        (700, 440, "index stale", "rebuild not run", MYKB, "OR"),
        (890, 380, "both servers want it", "documented", DASH, "OR"),
    ]
    for x, y, name, tag, c, gate in leaves:
        s.append(f'<line x1="{x}" y1="316" x2="{x}" y2="372" stroke="{BORDER2}" stroke-width="1.2" stroke-dasharray="3,3"/>')
        s.append(f'<circle cx="{x}" cy="372" r="8" fill="none" stroke="{c}" stroke-width="1.3"/>')
        s.append(f'<text x="{x}" y="{y+16}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="8.5" font-weight="700">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y+32}" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="7">{esc(tag)}</text>')
    s.append(panel(60, 560, 880, 150, EXT, "READING THE LOGIC", [
        (TEXT2, 10.5, "Each leaf is a single cause; each branch is an OR over its leaves — any leaf triggers the branch."),
        (TEXT2, 10.5, "The TOP is OR over branches — but recovery is AND: you need daemon up AND index rebuilt AND cache warm."),
        (TEXT4, 9.5, "Compare the A-22 table: there you read failures across a row; here you read them down the tree's branches."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 740, 880, 90, DASH, "THE ONE INEVITABLE LEAF", [
        (TEXT2, 10.5, "port clash :8765 is the only leaf with no external cause — it is designed in, which is why it has a documented owner."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "BRANCH COLOUR = the component that fails; circle gates = OR junctions (any child cause fires the parent)."),
        (TEXT2, 9.5, "THE TREE IS SHALLOW ON PURPOSE: two levels means every failure is diagnosable from the dashboard in one hop."),
        (TEXT2, 9.5, "This is the failure cascade (A-22) re-encoded as logic — same facts, different grammar."),
    ], title="READING THE TREE"))
    s.append(end("a fault tree is a promise: every failure the system can suffer is named and reachable"))
    return "\n".join(s)


# ── E-16 · The Self-Reference Map ─────────────────────────────────────
def self_reference_map():
    s = [doc("THE SELF-REFERENCE MAP — THE SYSTEM IMPROVING ITSELF",
             "Four levels of recursion, and the one edge that is deliberately forbidden")]
    levels = [
        (SPACE, "LEVEL 0 · OBJECTS", "code + artifacts", "the plain things — files, pages, probes, specs"),
        (RSIS, "LEVEL 1 · THE ENGINE", "RSIS3 improving RSIS3", "L2 drafts diffs to its own code — evaluator-gated"),
        (MYKB, "LEVEL 2 · THE META-LOOP", "improving the improvement", "L3 evolves strategies, budgets, and L2 heuristics"),
        (EXT, "LEVEL 3 · THE SPEC OF THE SPEC", "RRP specifying RRP", "SPACE generates the prompt framework that generates specs"),
    ]
    y = 128
    for accent, name, tag, desc in levels:
        s.append(panel(140, y, 620, 96, accent, name, [
            (accent, 10, tag),
            (TEXT2, 9.5, desc),
        ], header_h=30, pad=12, line_h=21))
        s.append(f'<path d="M 760 {y+48} C 880 {y+48}, 880 {y+170}, 770 {y+170}" fill="none" stroke="{accent}" stroke-width="1.8" opacity=".75" marker-end="url(#arwG)"/>')
        s.append(label(905, y + 100, "self", 8.5, accent, font=MONO))
        y += 210
    s.append(panel(60, y - 40, 880, 110, EXT, "THE FORBIDDEN EDGE", [
        (EXT, 10.5, "NO SELF-EDGE ON THE EVALUATOR: level 1 may change anything except the code that judges it."),
        (TEXT2, 9.5, "That single prohibition is what keeps the recursion well-founded — everything else can chase its own tail."),
    ], header_h=32, line_h=26))
    s.append(panel(60, y + 96, 880, 96, DASH, "WHY FOUR LEVELS AND NOT MORE", [
        (TEXT2, 10.5, "Level 3 is the ceiling: specifying the specifier is as meta as the system goes — there is no level-4 component."),
        (TEXT2, 9.5, "The meta-ladder (E-06) shows the same stack as rungs; this map adds the self-edges and the forbidden one."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "SELF-EDGES = recursion: each level operates on the level below it; the arrow looping back is the self-reference."),
        (TEXT2, 9.5, "COLOUR = the component that owns that level of recursion — ideation, engine, memory, external boundary."),
        (TEXT2, 9.5, "THE FORBIDDEN EDGE is the design's whole safety story: recursion is allowed exactly until it reaches the judge."),
    ], title="READING THE MAP"))
    s.append(end("self-reference is the feature and the risk — the evaluator boundary is where the risk is capped"))
    return "\n".join(s)


# ── E-17 · The Observability Stack ────────────────────────────────────
def observability_stack():
    s = [doc("THE OBSERVABILITY STACK — THE SYSTEM WATCHING ITSELF",
             "From loop event to human decision and back — telemetry as a closed loop")]
    layers = [
        (RSIS, "EMIT", "every loop iteration writes a pulse", "JSONL"),
        (DASH, "BUFFER", "rack/pulses/ · append-only", "disk"),
        (DASH, "SNAPSHOT", "dashboard-data.json · summarized", "JSON"),
        (DASH, "RENDER", "Chart.js · pulses / layers / success rate", "HTML"),
        (EXT, "READ", "a human (or L3) reads the trend", "eyes"),
        (SPACE, "DECIDE", "next spec / next strategy is written", "spec"),
        (MYKB, "RETURN", "session runs · new pulses emitted", "loop"),
    ]
    y = 128
    for i, (accent, name, desc, tag) in enumerate(layers):
        s.append(panel(170, y, 580, 78, accent, name, [(TEXT2, 9.5, desc)], header_h=28, pad=12, line_h=20))
        s.append(label(790, y + 28, tag, 8, TEXT3, anchor="start", font=MONO))
        s.append(label(790, y + 44, "format", 7, TEXT4, anchor="start"))
        if i < 6:
            s.append(arrow(500, y + 78, 500, y + 96, accent, "arwG", 2, opacity=0.6))
        y += 108
    s.append(f'<path d="M 750 128 C 900 128, 900 {y-60}, 760 {y-60}" fill="none" stroke="{EXT}" stroke-width="1.8" stroke-dasharray="6,4" opacity=".8" marker-end="url(#arwH)"/>')
    s.append(label(930, (128 + y - 60) / 2, "closes", 8.5, EXT, font=MONO))
    s.append(panel(60, y + 10, 880, 100, EXT, "THE TWO READERS", [
        (TEXT2, 10.5, "HUMAN — dashboard reader → writes next spec in SPACE;  L3 — trend reader → evolves strategy directly."),
        (TEXT2, 9.5, "Both close the loop; only L3 closes it without a human in the path."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOUR = who does the stage — emit indigo, buffer/snapshot/render green, read pink, decide amber, return cyan."),
        (TEXT2, 9.5, "EVERY STAGE NAMES ITS FORMAT — JSONL → disk → JSON → HTML → eyes → spec → loop: the stack is format transitions."),
        (TEXT2, 9.5, "THE CLOSING ARC = the loop from reading back to emitting — observability is a cycle, not a log."),
    ], title="READING THE STACK"))
    s.append(end("the system watches itself the same way it works — through artifacts, not shared state"))
    return "\n".join(s)


# ── E-18 · The Thermodynamic Clock ────────────────────────────────────
def thermodynamic_clock():
    s = [doc("THE THERMODYNAMIC CLOCK — COST AND ORDER AROUND THE LOOP",
             "Cheap chaos in ideation, expensive order in memory — the gradient the whole system runs on")]
    # cycle: SPACE (high entropy, low cost) -> GATE (barrier) -> RSIS3 (work) -> MYKB (low entropy, high cost)
    cx, cy = 500, 470
    s.append(f'<circle cx="{cx}" cy="{cy}" r="250" fill="none" stroke="{BORDER2}" stroke-width="1.4"/>')
    pos = [(cx, cy - 250, SPACE, "IDEATION", "high entropy · cheap to draft", "T↑"),
           (cx + 250, cy, EXT, "EVALUATOR", "energy barrier · rejection is work", "ΔG"),
           (cx, cy + 250, MYKB, "CONSOLIDATION", "low entropy · expensive to build", "T↓"),
           (cx - 250, cy, RSIS, "EXECUTION", "the work in between", "W")]
    for x, y, c, name, tag, glyph in pos:
        s.append(f'<circle cx="{x}" cy="{y}" r="56" fill="{c}" opacity=".18" stroke="{c}" stroke-width="2"/>')
        s.append(f'<text x="{x}" y="{y-6}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="11.5" font-weight="800">{esc(name)}</text>')
        s.append(f'<text x="{x}" y="{y+14}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="7.5">{esc(tag)}</text>')
        s.append(f'<text x="{x}" y="{y+32}" text-anchor="middle" fill="{TEXT4}" font-family="{MONO}" font-size="8">{glyph}</text>')
    for i in range(4):
        ax, ay = pos[i][0], pos[i][1]
        bx, by = pos[(i + 1) % 4][0], pos[(i + 1) % 4][1]
        s.append(f'<path d="M {ax} {ay} Q {(ax+bx)/2} {(ay+by)/2 - 60} {bx} {by}" fill="none" stroke="{TEXT4}" stroke-width="1.8" opacity=".8" marker-end="url(#arwG)"/>')
    # comet around the cycle
    s.append('<circle r="5.5" fill="#ffffff" stroke="#0b1120" stroke-width="1">'
             f'<animateMotion dur="12s" repeatCount="indefinite" path="M {cx} {cy-250} A 250 250 0 1 1 {cx-0.1} {cy-250} Z"/></circle>')
    s.append(label(500, 780, "comet = one artifact's thermodynamic journey — cheap chaos → barrier → work → expensive order", 9, TEXT4))
    s.append(panel(60, 820, 880, 140, EXT, "THE GRADIENT, STATED HONESTLY", [
        (TEXT2, 10.5, "Cost here is real: tokens for ideation, time for evaluation, git+index work for consolidation."),
        (TEXT2, 10.5, "Order is real too: a spec is more structured than an idea; a KG edge is more structured than a transcript."),
        (TEXT4, 9.5, "The clock is the energy landscape (A-12) drawn as a cycle instead of a terrain — same gradient, closed path."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COMET = one artifact circling: each lap spends entropy (ideation) to buy order (memory) — motion is the gradient."),
        (TEXT2, 9.5, "THE EVALUATOR IS THE BARRIER: energy must be spent to cross it; rejected artifacts bounce back to ideation."),
        (TEXT2, 9.5, "TEMPERATURE LABELS are entropy, not heat: T↑ = many possibilities, T↓ = few — the loop runs downhill overall."),
    ], title="READING THE CLOCK"))
    s.append(end("the whole system is a heat engine for knowledge — it burns possibilities to forge facts"))
    return "\n".join(s)


# ── E-19 · The Complexity Budget ──────────────────────────────────────
def complexity_budget():
    s = [doc("THE COMPLEXITY BUDGET — WHERE THE WEIGHT LIVES",
             "LOC, files, and interfaces — the real tax is the boundary count, not the line count")]
    s.append(label(500, 108, "three size dimensions, one budget: the 6 interfaces are worth more than all 239k LOC", 9.5, TEXT3, italic=True))
    # LOC bar
    s.append(sect(60, 136, 880, RSIS, "DIMENSION 1 · LINES OF CODE", "~239k total"))
    bars = [
        ("RSIS3", 67, RSIS), ("SPACE", 69, SPACE), ("MYKB+", 103, MYKB),
    ]
    bx = 60
    for name, loc, c in bars:
        w = loc * 5.4
        s.append(f'<rect x="{bx}" y="205" width="{w:.0f}" height="34" rx="6" fill="{c}" opacity=".85"/>')
        s.append(f'<text x="{bx + w/2:.0f}" y="226" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="10" font-weight="800">{esc(name)}</text>')
        s.append(label(bx + w / 2, 200, f"~{loc}k LOC", 8, TEXT3))
        bx += w + 18
    s.append(label(60, 268, "0 ──────────────── 239k LOC (total, incl. dashboard, tests, docs)", 8.5, TEXT4, anchor="start", font=MONO))
    # files bar
    s.append(sect(60, 300, 880, MYKB, "DIMENSION 2 · FILES", "2,881 total"))
    files = [
        ("wiki pages", 2360, MYKB), ("rsis3 + space + rest", 521, EXT),
    ]
    bx = 60
    for name, n, c in files:
        w = n * 0.34
        s.append(f'<rect x="{bx}" y="366" width="{w:.0f}" height="34" rx="6" fill="{c}" opacity=".85"/>')
        s.append(f'<text x="{bx + w/2:.0f}" y="387" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="10" font-weight="800">{esc(name)}</text>')
        bx += w + 18
    s.append(label(60, 428, "0 ──────────────── 2,881 files (wiki corpus dominates — and it is data, not logic)", 8.5, TEXT4, anchor="start", font=MONO))
    # interface bar
    s.append(sect(60, 460, 880, DASH, "DIMENSION 3 · INTERFACES — THE REAL BUDGET", "the tax"))
    s.append(f'<rect x="60" y="524" width="{6*72}" height="40" rx="8" fill="{DASH}" opacity=".8"/>')
    for i in range(6):
        s.append(f'<line x1="{132 + i*72}" y1="524" x2="{132 + i*72}" y2="564" stroke="#0b1120" stroke-width="1.5"/>')
        s.append(label(132 + i * 72, 548, f"IF-{i+1}", 8, "#0b1120", font=MONO))
    s.append(label(60, 592, "6 cross-component interfaces — each one a contract with error modes, formats, and cadence (A-25)", 8.5, TEXT4, anchor="start"))
    s.append(panel(60, 640, 880, 160, EXT, "THE BUDGET RULE", [
        (TEXT2, 10.5, "Complexity is not LOC — it is coupling: 239k lines with 6 interfaces is simpler than 50k lines with 30 interfaces."),
        (TEXT2, 10.5, "The system spends its complexity budget on recursion depth (loops, meta) and keeps the module graph flat (A-21)."),
        (TEXT4, 9.5, "Every new interface must repay its cost: it has to cross one of the six existing contracts or justify a seventh."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 830, 880, 90, RSIS, "THE GAUGE", [
        (TEXT2, 10.5, "LOC budget spent: 100% · files budget spent: 100% · interface budget spent: 6/6 — the tax is fully allocated."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "BAR WIDTH = real measured weight (LOC / files / interface count) — this diagram is drawn to scale."),
        (TEXT2, 9.5, "MYKB+ = wiki markdown plus Python tooling: the corpus is 2,360 pages of data, not logic — a different kind of weight."),
        (TEXT2, 9.5, "THE INTERFACE BAR is the budget that matters: six contracts carry the entire ecosystem."),
    ], title="READING THE BUDGET"))
    s.append(end("complexity is a budget you spend on coupling — the system chose six contracts and unlimited recursion"))
    return "\n".join(s)


# ── E-20 · The Coupling Matrix ────────────────────────────────────────
def coupling_matrix():
    s = [doc("THE COUPLING MATRIX — WHO DEPENDS ON WHOM",
             "Six modules, directed dependency counts, fan-in / fan-out — the heatmap of the codebase")]
    mods = ["rsis3 core", "rack", "mykb", "space", "dashboard", "evaluator"]
    # directed edges: (from, to) — from depends on to
    edges = [
        ("rsis3 core", "rack", 1), ("rsis3 core", "evaluator", 1), ("rsis3 core", "mykb", 1),
        ("rack", "rsis3 core", 1), ("dashboard", "rsis3 core", 1), ("dashboard", "mykb", 1),
        ("dashboard", "space", 1), ("mykb", "rsis3 core", 0), ("space", "rsis3 core", 0),
    ]
    heat = {}
    for a, b, w in edges:
        heat[(a, b)] = w
    def hcol(v):
        return ["#0f172a", "#f59e0b", "#f97316", "#ef4444"][min(v, 3)]
    s.append(f'<rect x="220" y="140" width="{5*118}" height="38" rx="8" fill="{EXT}" opacity=".12" stroke="{BORDER2}"/>')
    for c in range(5):
        s.append(label(220 + c * 118 + 59, 164, mods[c + 1], 9, EXT, font=MONO))
    s.append(label(160, 164, "depends on ↓", 8, TEXT3, anchor="middle", font=MONO))
    for r in range(5):
        ry = 178 + r * 44
        s.append(f'<rect x="220" y="{ry}" width="{5*118}" height="44" fill="{PANEL}" stroke="{BORDER2}" stroke-width="0.7"/>')
        s.append(f'<text x="110" y="{ry + 28}" text-anchor="middle" fill="{TEXT2}" font-family="{MONO}" font-size="9">{esc(mods[r])}</text>')
        for c in range(5):
            v = heat.get((mods[r], mods[c + 1]), 0)
            s.append(f'<rect x="{220 + c * 118 + 4}" y="{ry + 4}" width="110" height="36" rx="6" fill="{hcol(v)}" opacity=".85"/>')
            s.append(f'<text x="{220 + c * 118 + 59}" y="{ry + 27}" text-anchor="middle" fill="{TEXT if v else TEXT4}" font-family="{MONO}" font-size="11" font-weight="700">{v if v else "·"}</text>')
    # fan-in / fan-out
    fin = {"rsis3 core": 3, "rack": 1, "mykb": 2, "space": 1, "dashboard": 0, "evaluator": 1}
    fout = {"rsis3 core": 3, "rack": 1, "mykb": 0, "space": 0, "dashboard": 3, "evaluator": 0}
    s.append(sect(60, 470, 880, DASH, "FAN-IN / FAN-OUT — THE REAL READ", "directed counts"))
    fy = 528
    for m in mods:
        s.append(f'<text x="90" y="{fy}" fill="{TEXT2}" font-family="{MONO}" font-size="9">{esc(m)}</text>')
        s.append(f'<rect x="200" y="{fy-12}" width="{fout[m]*70}" height="12" rx="4" fill="{RSIS}" opacity=".8"/>')
        s.append(f'<rect x="430" y="{fy-12}" width="{fin[m]*70}" height="12" rx="4" fill="{MYKB}" opacity=".8"/>')
        s.append(f'<text x="{200 + fout[m]*70 + 8}" y="{fy}" fill="{RSIS}" font-family="{MONO}" font-size="8.5">out {fout[m]}</text>')
        s.append(f'<text x="{430 + fin[m]*70 + 8}" y="{fy}" fill="{MYKB}" font-family="{MONO}" font-size="8.5">in {fin[m]}</text>')
        fy += 30
    s.append(label(60, 762, "indigo bar = fan-out (depends on) · cyan bar = fan-in (depended on)", 8.5, TEXT4, anchor="start"))
    s.append(panel(60, 800, 880, 110, EXT, "WHAT THE HEATMAP SAYS", [
        (TEXT2, 10.5, "rsis3 core is the hub: highest fan-out (needs rack, evaluator, mykb) and highest fan-in (rack, dashboard depend on it)."),
        (TEXT2, 10.5, "dashboard is a pure consumer (fan-in 0) and space/mykb are pure providers at the code level — their coupling is via files."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "HEAT = directed dependency count (0 · 1 · 2 · 3+): amber warm, red hot — rows depend on columns."),
        (TEXT2, 9.5, "ZERO CELLS MATTER: evaluator depends on nothing, and nothing (except the spawn) depends on it — that isolation is the point."),
        (TEXT2, 9.5, "The B-14 ownership matrix was WHO RUNS WHAT; this matrix is WHO IMPORTS WHOM — code coupling, not runtime coupling."),
    ], title="READING THE MATRIX"))
    s.append(end("coupling is where complexity lives — the heatmap shows it is concentrated in exactly one module"))
    return "\n".join(s)


# ── E-21 · The Protocol Stack ─────────────────────────────────────────
def protocol_stack():
    s = [doc("THE PROTOCOL STACK — THE RRP, LAYER BY LAYER",
             "From a single probe to a consumed spec — seven layers with the ratios between them")]
    layers = [
        ("L7 · CONSUMPTION", "RSIS3 L2 imports the canonical spec → candidates", RSIS),
        ("L6 · EXPORT", "6 formats rendered from the canonical draft", DASH),
        ("L5 · SPEC", "one structured artifact per session", SPACE),
        ("L4 · SESSION", "25 rounds × 7 series · 326 probes in play", SPACE),
        ("L3 · ROUND", "probe → answer → reflect · 12s", SPACE),
        ("L2 · SERIES", "7 series with dependency chain S1 → S7", SPACE),
        ("L1 · PROBE", "the atomic question · 326 of them", MYKB),
    ]
    y = 128
    for i, (name, desc, accent) in enumerate(layers):
        w = 760 - i * 26
        s.append(panel(500 - w / 2, y, w, 72, accent, name, [(TEXT2, 9.5, desc)], header_h=28, pad=12, line_h=20))
        if i < 6:
            s.append(arrow(500, y + 72, 500, y + 92, SPACE, "arwS", 2, opacity=0.6))
        y += 102
    s.append(panel(60, y + 4, 880, 100, EXT, "THE RATIOS BETWEEN LAYERS", [
        (TEXT2, 10.5, "L3 → L4: 12 pulses per round (12:1) ·  L4 → L5: 25 rounds per spec (25:1)"),
        (TEXT2, 10.5, "L1 → L2: 326 probes distributed across 7 series ·  L5 → L6: one spec, six renderings"),
    ], header_h=32, line_h=26))
    s.append(panel(60, 850, 880, 90, MYKB, "WHY THE STACK NARROWS", [
        (TEXT2, 10.5, "Each layer is a lossy-but-purposeful compression: probes → answers → ranked answers → spec → format."),
        (TEXT2, 9.5, "The narrowing is the information flow (E-13) drawn as layers instead of a curve."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "STACK WIDTH = the layer's breadth — 326 probes are wide, one canonical spec is narrow."),
        (TEXT2, 9.5, "COLOUR = owning component: probes/rounds/series/spec amber, exports green, consumption indigo, atomic questions cyan."),
        (TEXT2, 9.5, "READ BOTTOM-UP as the protocol: L1 atoms compose into L7 consumption; each arrow is a defined transition."),
    ], title="READING THE STACK"))
    s.append(end("the RRP is not a checklist — it is a protocol with defined layers and measured ratios"))
    return "\n".join(s)


# ── E-22 · The Latency Budget ─────────────────────────────────────────
def latency_budget():
    s = [doc("THE LATENCY BUDGET — WHERE THE TIME GOES",
             "Every bounded stage in the pipeline, its cap, and where latency actually hides")]
    rows = [
        ("L1 STEP", 120, 120, RSIS, "hard cap per tool step · 10 calls max"),
        ("TELEMETRY FLUSH", 1, 1, DASH, "per pulse · ~1s cadence"),
        ("RRP ROUND", 12, 12, SPACE, "per probe round (compressed)"),
        ("RETRIEVAL", 15, 8, MYKB, "on-demand · adds to L1 latency when hit"),
        ("EVALUATION", 60, 60, EXT, "per candidate · the single biggest block"),
        ("CONSOLIDATION", 60, 60, MYKB, "per L3 cycle · runs post-session"),
    ]
    s.append(table(60, 130, [210, 150, 150, 370], ["STAGE", "CAP (s)", "TYPICAL (s)", "WHERE IT HIDES"],
                  [(r[0], (r[1], r[4]), (r[2], r[4]), (r[3], r[4])) for r in rows],
                  row_h=50, header_h=38, mono_cols=(1, 2)))
    s.append(panel(60, 470, 880, 150, EXT, "THE THREE SURPRISES", [
        (EXT, 10.5, "1 · EVALUATION is 60s — half the whole pipeline; it is the price of the trust boundary, paid in wall-clock."),
        (TEXT2, 10.5, "2 · RETRIEVAL is the only on-demand cost inside an L1 step — it turns a 1s loop into a ~9s loop when context is needed."),
        (TEXT2, 10.5, "3 · CONSOLIDATION looks huge (60s) but is async — sessions keep acting while L3 works."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 650, 880, 110, RSIS, "THE BUDGET RULE", [
        (TEXT2, 10.5, "Every stage's cap is a contract (A-25): exceeding it means fail/retry, never silent wait."),
        (TEXT2, 10.5, "Total worst case ≈ 120s (L1) + 60s (eval) + 60s (L3) — the system is built for a 4-minute bound."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "BAR COLOUR = owner; CAP vs TYPICAL are drawn as numbers — where they match, the budget is the bottleneck."),
        (TEXT2, 9.5, "EVALUATION OWNS THE CRITICAL PATH — reducing it would speed every session, which is why its immutability is non-negotiable."),
        (TEXT2, 9.5, "Compare B-21 (cadence) — that was the rhythm; this is the per-stage price of each beat."),
    ], title="READING THE BUDGET"))
    s.append(end("latency is a budget you allocate — this system spends 60 of every ~180 seconds on judgment"))
    return "\n".join(s)


# ── E-23 · The Evolution Ladder ───────────────────────────────────────
def evolution_ladder():
    s = [doc("THE EVOLUTION LADDER — CLIMBING λ WITH GATES",
             "Each rung adds a subsystem, each gate is the proof required before the next climb")]
    rungs = [
        ("λ₁ · ENGINE", "RSIS3 loops fire", RSIS, "act without memory"),
        ("λ₂ · +MEMORY", "MyKB joins", MYKB, "remember everything"),
        ("λ₃ · +IDEATION", "SPACE joins", SPACE, "ideate before acting"),
        ("λ₄ · ECOSYSTEM", "dashboard + hub", DASH, "observe it all"),
    ]
    y = 128
    for i, (name, desc, accent, tag) in enumerate(rungs):
        s.append(panel(220, y, 480, 84, accent, name, [(TEXT2, 9.5, desc)], header_h=30, pad=12, line_h=20))
        s.append(label(740, y + 28, tag, 8.5, TEXT3, anchor="start", font=MONO))
        s.append(label(740, y + 46, "capability", 7.5, TEXT4, anchor="start"))
        if i < 3:
            gx = 460
            gy = y + 84 + 34
            s.append(f'<path d="M {gx} {gy-9} L {gx+9} {gy} L {gx} {gy+9} L {gx-9} {gy} Z" fill="#0b1120" stroke="{EXT}" stroke-width="1.8"/>')
            gates = [
                ("retrieval proven", "lessons round-trip via :8765"),
                ("spec quality proven", "specs pass evaluator > threshold"),
                ("embeds proven", "dashboard renders all three iframes"),
            ]
            s.append(label(gx + 34, gy - 14, gates[i][0], 8, EXT, anchor="start"))
            s.append(label(gx + 34, gy + 2, gates[i][1], 7.5, TEXT4, anchor="start"))
            s.append(arrow(500, gy + 12, 500, y + 84 + 70, GRAY, "arwG", 2, opacity=0.6))
        y += 190
    s.append(panel(60, y - 40, 880, 100, EXT, "WHAT A GATE IS", [
        (TEXT2, 10.5, "Each gate is a measured capability, not a code review: retrieval must round-trip, specs must pass the evaluator, embeds must render."),
        (TEXT2, 9.5, "Failing a gate does not roll back the rung — it holds the ladder until the measurement passes."),
    ], header_h=32, line_h=26))
    s.append(panel(60, y + 84, 880, 80, MYKB, "LINK TO THE OTHER λ DIAGRAMS", [
        (TEXT2, 10.5, "B-24 showed the λ stages as a timeline; A-13 as bifurcations; this ladder adds the gate each climb must clear."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "RUNG COLOUR = the subsystem added at that λ; DIAMONDS = gates with their proof conditions."),
        (TEXT2, 9.5, "READ UPWARD: each rung is a strict superset and each gate is a measurable prerequisite for the next."),
        (TEXT2, 9.5, "The ladder and the timeline (B-24) tell the same story in two grammars — history and requirements."),
    ], title="READING THE LADDER"))
    s.append(end("evolution is not automatic here — each rung must earn its gate, and the gates are measurements"))
    return "\n".join(s)


# ── E-24 · The Conservation Laws ──────────────────────────────────────
def conservation_laws():
    s = [doc("THE CONSERVATION LAWS — WHAT THE SYSTEM CANNOT LOSE",
             "Six quantities that are conserved across every transformation — the physics of the ecosystem")]
    laws = [
        (SPACE, "ARTIFACT LINEAGE", "every candidate has a spec parent · every KG edge has a lesson parent", "a parentless artifact is a bug"),
        (RSIS, "BUDGET CONSERVATION", "10 calls · 120s · 3 retries · ≤5 evals — per session, not per mood", "a spent budget is never restored mid-session"),
        (MYKB, "SOURCE-OF-TRUTH", "wiki is the canonical copy; indexes and graphs are derived", "derived state never overwrites the corpus"),
        (DASH, "TELEMETRY APPEND-ONLY", "the JSONL buffer is never edited, only consumed and truncated", "a rewritten history would break trends"),
        (EXT, "EVALUATOR CONSTANCY", "the judge's digest is the same at every spawn", "a drifted evaluator invalidates every verdict"),
        (MYKB, "TEMPORAL CONTINUITY", "every write is a git commit — the timeline has no gaps", "an un-snapshotted change is invisible to time-travel"),
    ]
    y = 128
    for accent, name, law, violation in laws:
        s.append(panel(60, y, 880, 104, accent, name, [
            (TEXT2, 10, law),
            (TEXT4, 9, f"VIOLATION →  {violation}"),
        ], header_h=30, pad=14, line_h=22))
        y += 138
    s.append(panel(60, y, 880, 90, EXT, "WHY 'CONSERVED' IS THE RIGHT WORD", [
        (TEXT2, 10.5, "These quantities are invariant under the system's normal transformations — improvement changes code, not lineage."),
        (TEXT2, 9.5, "The invariant ledger (E-14) listed WHAT cannot change; this map says what cannot be LOST as things change."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOUR = the component that guards the law — each law is enforced by exactly one owner."),
        (TEXT2, 9.5, "VIOLATION clauses are testable: parentless artifact, overspent budget, rewritten buffer, drifted digest, gap in history."),
        (TEXT2, 9.5, "TOGETHER the six laws define 'the same system': if all six hold, every diagram in this viewer still describes it."),
    ], title="READING THE LAWS"))
    s.append(end("conservation is the deepest invariant — the system can change anything as long as these six quantities survive"))
    return "\n".join(s)


EXPERT6 = {
    "expert-13-information-flow.svg": information_flow,
    "expert-14-invariant-ledger.svg": invariant_ledger,
    "expert-15-fault-tree.svg": fault_tree,
    "expert-16-self-reference-map.svg": self_reference_map,
    "expert-17-observability-stack.svg": observability_stack,
    "expert-18-thermodynamic-clock.svg": thermodynamic_clock,
    "expert-19-complexity-budget.svg": complexity_budget,
    "expert-20-coupling-matrix.svg": coupling_matrix,
    "expert-21-protocol-stack.svg": protocol_stack,
    "expert-22-latency-budget.svg": latency_budget,
    "expert-23-evolution-ladder.svg": evolution_ladder,
    "expert-24-conservation-laws.svg": conservation_laws,
}
