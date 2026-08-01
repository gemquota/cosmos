"""Round 6 Basic tier — the ecosystem, doubled (B-13…B-24).

All portrait 1000x1320. Grounded in the real spec: ports, cadences,
formats, evaluator contract, embed relationships, hub URLs, wiki counts.
"""
from round6 import *


# ── B-13 · The Artifact Lifecycle ─────────────────────────────────────
def artifact_lifecycle():
    s = [doc("THE ARTIFACT LIFECYCLE — FIVE STATES, ONE LOOP",
             "An idea born in SPACE becomes a candidate, a pulse, a lesson, and finally a knowledge-graph edge")]
    cx, cy = 500, 560
    items = [
        ("IDEA", SPACE, "326 probes · 7 series"),
        ("CANDIDATE", RSIS, "L2 diff/code · gated"),
        ("PULSE", DASH, "L1 telemetry · JSONL"),
        ("LESSON", MYKB, "session capture hook"),
        ("KG EDGE", "#67e8f9", "graph.json · retrievable"),
    ]
    s.append(ring(cx, cy, 235, 330, items, start=90, label_r=282))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="205" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1.4"/>')
    owners = [(400, 470, SPACE, "SPACE", "ideation"), (600, 470, RSIS, "RSIS3", "execution"),
              (500, 660, MYKB, "MYKB", "consolidation")]
    for ox, oy, c, name, tag in owners:
        s.append(f'<circle cx="{ox}" cy="{oy}" r="30" fill="{c}" opacity=".92" stroke="#0b1120" stroke-width="2"/>')
        s.append(f'<text x="{ox}" y="{oy+4}" text-anchor="middle" fill="#0b1120" font-family="{FONT}" font-size="8.5" font-weight="800">{esc(name)}</text>')
        s.append(label(ox, oy + 50, tag, 8, TEXT4))
    s.append(arrow(430, 470, 570, 470, RSIS, "arwR", 2, opacity=0.55))
    s.append(arrow(560, 520, 530, 610, MYKB, "arwM", 2, opacity=0.55))
    s.append(arrow(450, 630, 420, 540, SPACE, "arwS", 2, opacity=0.55, dashed=True))
    s.append(label(500, 700, "retrieval · :8765 returns memory to ideation", 8.5, TEXT4))
    s.append('<circle r="5.5" fill="#ffffff" stroke="#0b1120" stroke-width="1">'
             f'<animateMotion dur="14s" repeatCount="indefinite" path="M {cx} {cy-185} A 185 185 0 1 1 {cx-0.1} {cy-185} Z"/></circle>')
    gx, gy = polar(cx, cy, 185, 234)
    s.append(f'<path d="M {gx} {gy-10} L {gx+10} {gy} L {gx} {gy+10} L {gx-10} {gy} Z" fill="#0b1120" stroke="{EXT}" stroke-width="1.8"/>')
    s.append(label(gx, gy - 22, "EVALUATOR", 8, EXT, font=MONO))
    s.append(label(gx, gy + 30, "SHA-256 · 60s · ≤5/session", 7.5, TEXT4))
    lx, ly = polar(cx, cy, 150, 343)
    ix, iy = polar(cx, cy, 150, 126)
    s.append(f'<path d="M {lx:.1f} {ly:.1f} A 150 150 0 0 1 {ix:.1f} {iy:.1f}" fill="none" stroke="{MYKB}" stroke-width="1.8" stroke-dasharray="6,5" opacity=".8" marker-end="url(#arwM)"/>')
    s.append(label(500, 318, "maturation cascade — one artifact, five states", 9, TEXT3, italic=True))
    s.append(chiprow(110, 955, [("12:1 pulses per RRP round", SPACE), ("25:1 rounds per spec", RSIS),
                                ("evaluator ≤5 candidates/session", EXT), ("KG edges retrievable via :8765", MYKB)], gap=16, size=8.5))
    s.append(legend([
        (EXT, 10.5, "COMET = one artifact circulating the lifecycle — one lap is one idea matured end-to-end; motion encodes the pipeline."),
        (TEXT2, 9.5, "RING SEGMENTS = the five states, clockwise: IDEA (SPACE) → CANDIDATE (RSIS3) → PULSE (telemetry) → LESSON → KG EDGE (MyKB)."),
        (TEXT2, 9.5, "DIAMOND = the evaluator gate between candidate and pulse: SHA-256-verified, 60s subprocess, ≤5 candidates per session."),
        (TEXT2, 9.5, "DASHED INNER ARC = the return path — retrieval (:8765) pulls consolidated memory back into the next idea."),
        (TEXT2, 9.5, "STATE COLOURS follow the component palette: amber ideation · indigo execution · green telemetry · cyan memory."),
    ], title="READING THE LIFECYCLE"))
    s.append(end("the system's throughput is simply this ring's rotation rate — ideas that survive the gate become retrievable memory"))
    return "\n".join(s)


# ── B-14 · The Ownership Matrix ───────────────────────────────────────
def ownership_matrix():
    s = [doc("THE OWNERSHIP MATRIX — WHO RUNS WHAT",
             "Six code modules across four runtimes — every cell is a real read / write / spawn / embed relationship")]
    rows = ["rsis3/ core", "rack/pulses/", "mykb/", "space/", "dashboard/", "evaluator/"]
    cols = ["RSIS3", "MYKB", "SPACE", "DASH"]
    cells = [
        (0, 0, "OWN", RSIS), (0, 1, "EMBED", MYKB), (0, 2, "READ", SPACE), (0, 3, "FEED", DASH),
        (1, 0, "WRITE", RSIS), (1, 3, "READ", DASH),
        (2, 1, "OWN", MYKB), (2, 0, "SERVE", RSIS), (2, 3, "EMBED", DASH),
        (3, 2, "OWN", SPACE), (3, 0, "FEED", RSIS), (3, 1, "WRITE", MYKB), (3, 3, "EMBED", DASH),
        (4, 3, "OWN", DASH), (4, 0, "READ", RSIS), (4, 1, "EMBED", MYKB), (4, 2, "EMBED", SPACE),
        (5, 0, "SPAWN", EXT), (5, 1, "—", TEXT4),
    ]
    s.append(matrix(245, 130, rows, cols, cells, cell_w=118, cell_h=34, header_h=36, gutter=165))
    s.append(label(60, 382, "OWN owns the code · EMBED is embedded inside · READ consumes · WRITE produces · SERVE answers requests · FEED streams events · SPAWN launches a subprocess", 8.5, TEXT4, anchor="start"))
    s.append(sect(60, 420, 880, RSIS, "WHAT THE GRID SAYS", "read the diagonal first"))
    s.append(panel(60, 478, 880, 220, RSIS, "THE DIAGONAL IS THE TRUNK", [
        (TEXT2, 10.5, "Each module's OWN cell is its home runtime — everything else is an interface crossing a boundary."),
        (TEXT2, 10.5, "The dashboard is the only module that embeds all three others (wiki browser, KG graph, SPACE web UI, meta viewer)."),
        (TEXT2, 10.5, "evaluator/ is the only module that RSIS3 SPAWNS — never imports — so self-improvement can never rewrite its judge."),
        (TEXT4, 9.5, "Two crossing paths worth remembering: mykb/ SERVE → rsis3/ (retrieval :8765), and space/ FEED → rsis3/ (spec drafts become candidates)."),
    ], header_h=32, line_h=24))
    s.append(panel(60, 730, 880, 150, EXT, "KNOWN CONFLICT THE GRID HIDES", [
        (EXT, 10.5, "rack/pulses and mykb/ both claim port :8765 — the MyKB daemon is the only always-on server, and the rack's pulse server must yield."),
        (TEXT2, 9.5, "The grid shows clean ownership; the runtime map (B-19) shows the one port both modules want."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOUR = the runtime that owns the relationship: indigo RSIS3 · cyan MyKB · amber SPACE · green DASH · pink external."),
        (TEXT2, 9.5, "READ THE ROWS as modules (code on disk); read the columns as runtimes (processes that own a lifecycle)."),
        (TEXT2, 9.5, "A row with many cells is an integration hub (dashboard, space); a row with few is a specialist (evaluator)."),
        (TEXT2, 9.5, "EMBED cells are the dashboard's iframe mounts — the unified dashboard hosts every component in one page."),
    ], title="READING THE MATRIX"))
    s.append(end("ownership is the first question a reviewer asks: who can change this code, and who only reads its output"))
    return "\n".join(s)


# ── B-15 · The Three Jobs ─────────────────────────────────────────────
def three_jobs():
    s = [doc("THE THREE JOBS — ONE PER LOOP",
             "L1 acts, L2 improves, L3 evolves — nested scope, three timescales, three budgets")]
    jobs = [
        (RSIS, "L1 · THE DOER", "per-task action loop", "seconds · ~1s", [
            "tool calls, observations, retries",
            "max 10 tool calls/step · 120s timeout · 3 retries",
            "checkpoint before every mutation",
            "telemetry: pulse every iteration",
        ]),
        (SPACE, "L2 · THE IMPROVER", "per-session RRP rounds", "~12s per round", [
            "code gen · prompt & tool tuning",
            "IMMUTABLE evaluator gates each candidate",
            "25 rounds per spec · ≤5 eval candidates/session",
            "telemetry: candidate + verdict",
        ]),
        (MYKB, "L3 · THE EVOLVER", "cross-session consolidation", "~60s per cycle", [
            "git → knowledge graph → vector embeddings",
            "strategy & meta-parameter evolution",
            "redundancy refinement + pruning",
            "telemetry: consolidation report",
        ]),
    ]
    y = 120
    for accent, name, role, clock, facts in jobs:
        s.append(panel(60, y, 880, 240, accent, f"{name} — {role}", [
            (TEXT2, 10.5, f"CLOCK: {clock}"),
        ] + [(TEXT2, 9.5, f"•  {f}") for f in facts], header_h=34, pad=16, line_h=23))
        y += 280
    s.append(f'<line x1="36" y1="170" x2="36" y2="890" stroke="{BORDER2}" stroke-width="2" marker-start="url(#arwG)" marker-end="url(#arwG)"/>')
    s.append(f'<text x="26" y="530" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9" font-weight="700" transform="rotate(-90 26 530)">NESTED SCOPE — L3 ⊃ L2 ⊃ L1</text>')
    for i, (accent, name, *_rest) in enumerate(jobs):
        s.append(f'<circle cx="36" cy="{185 + i*280}" r="7" fill="{accent}" stroke="#0b1120" stroke-width="1.6"/>')
    s.append(panel(60, 968, 880, 92, EXT, "THE RATIOS THE CLOCKS IMPLY", [
        (TEXT2, 10.5, "12 pulses per RRP round (12:1) · 25 rounds per spec (25:1) · every round, every pulse, every cycle is logged"),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "ONE JOB PER LOOP: L1 never improves, L2 never consolidates, L3 never acts — separation is what makes the recursion safe."),
        (TEXT2, 9.5, "COLOUR = the clock: indigo the action loop, amber the improvement rounds, cyan the consolidation cycle."),
        (TEXT2, 9.5, "NESTING RAIL = scope containment: every L2 round contains ~12 L1 pulses; every L3 cycle contains ~5 RRP rounds."),
        (TEXT2, 9.5, "BUDGETS are the hard walls: 10 calls/step, 120s, 3 retries · 25 rounds/spec, 5 evals · 20 sessions/plateau."),
    ], title="READING THE JOBS"))
    s.append(end("three jobs, three clocks, three budgets — the whole engine is these three panels firing in phase"))
    return "\n".join(s)


# ── B-16 · The Data Product Map ───────────────────────────────────────
def data_product_map():
    s = [doc("THE DATA PRODUCT MAP — EVERYTHING THE SYSTEM PRODUCES",
             "Eight artifacts that actually flow between components — who makes them, who consumes them, what format")]
    rows = [
        ("PROBE ANSWERS", "SPACE · RRP", "SPACE (session state)", "JSON", SPACE),
        ("SPEC DRAFTS", "SPACE · exports/", "RSIS3 · L2 loop", "MD/JSON/YAML/HTML/XML/TXT", SPACE),
        ("IMPROVEMENT CANDIDATES", "RSIS3 · L2", "Evaluator (stdin)", "JSON · SHA-256", RSIS),
        ("EVAL VERDICTS", "Evaluator (immutable)", "RSIS3 · L2 loop", "JSON (stdout)", EXT),
        ("PULSES", "RSIS3 · L1/L3", "Rack → dashboard", "JSONL", DASH),
        ("LESSONS", "RSIS3 · L3", "MyKB · wiki writer", "Markdown", MYKB),
        ("KG EDGES", "MyKB · graph builder", "RSIS3 · retrieval :8765", "graph.json", MYKB),
        ("DASHBOARD-DATA.JSON", "Rack (RSIS3)", "Dashboard · Chart.js", "JSON", DASH),
    ]
    s.append(table(60, 130, [250, 200, 230, 200], ["PRODUCT", "PRODUCER", "CONSUMER", "FORMAT"],
                  [(r[0], r[1], r[2], (r[3], r[4])) for r in rows], row_h=40, header_h=36,
                  mono_cols=(0,)))
    s.append(panel(60, 560, 880, 150, DASH, "FORMAT FAMILIES", [
        (TEXT2, 10.5, "JSON is the machine spine — candidates, verdicts, telemetry, dashboard data all speak it."),
        (TEXT2, 10.5, "Markdown is the human spine — specs, lessons, and wiki pages are readable and diffable."),
        (TEXT4, 9.5, "SPACE exports one spec in six formats; MyKB archives them; RSIS3 consumes the canonical one."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 740, 880, 150, RSIS, "WHO PAYS FOR EACH PRODUCT", [
        (TEXT2, 10.5, "Every producer has exactly one primary consumer — except pulses, which fan out to the rack, the dashboard, and L3 trend detection."),
        (TEXT2, 10.5, "Every consumer is coupled to a format contract: changing a format is an interface change, not a code change."),
        (TEXT4, 9.5, "The only bidirectional pair: candidates (RSIS3 → evaluator) and verdicts (evaluator → RSIS3) — one subprocess, two JSON messages."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COLOURED FORMAT CELLS = producer palette — who owns the schema: SPACE amber, RSIS3 indigo, MyKB cyan, dashboard green, evaluator pink."),
        (TEXT2, 9.5, "READ ACROSS a row as a contract: producer → consumer with a format that neither side may silently change."),
        (TEXT2, 9.5, "The eight rows are the system's entire observable surface — nothing else crosses a component boundary."),
    ], title="READING THE MAP"))
    s.append(end("if a reviewer asks 'what does this system actually emit?', the answer is exactly these eight products"))
    return "\n".join(s)


# ── B-17 · The Six Handoffs ───────────────────────────────────────────
def six_handoffs():
    s = [doc("THE SIX HANDOFFS — THE SYSTEM'S REAL INTERFACES",
             "Six directional contracts between the four runtimes — port, payload, cadence")]
    handoffs = [
        ("SPACE", "RSIS3", SPACE, RSIS, "SPEC DRAFTS", "exports/ on the shared filesystem · MD/JSON", "on-demand after RRP sessions"),
        ("RSIS3", "EVALUATOR", RSIS, EXT, "CANDIDATE JSON", "stdin subprocess · SHA-256 verified", "≤5 per session · 60s cap"),
        ("RSIS3", "DASHBOARD", RSIS, DASH, "PULSES", "rack/pulses → dashboard-data.json · JSONL", "~1s cadence"),
        ("MYKB", "RSIS3", MYKB, RSIS, "RETRIEVAL", "HTTP :8765 · ranked wiki context", "on-demand during L1"),
        ("RSIS3", "MYKB", RSIS, MYKB, "SESSION CAPTURE", "wiki pages + KG edges + snapshots", "post-session · L3"),
        ("DASHBOARD", "SPACE", DASH, SPACE, "LAUNCH", "open web UI (:8888) + meta viewer (:8899)", "on-demand, user-driven"),
    ]
    y = 120
    for i, (fr, to, fc, tc, name, payload, cadence) in enumerate(handoffs):
        col = 60 if i % 2 == 0 else 500
        ry = y + (i // 2) * 250
        s.append(panel(col, ry, 440, 180, fc, f"{fr}  →  {to}", [
            (fc, 10.5, f"PAYLOAD — {name}"),
            (TEXT2, 9.5, payload),
            (TEXT4, 9, f"CADENCE — {cadence}"),
        ], header_h=32, pad=14, line_h=22))
        ax = col + 440 if i % 2 == 0 else col - 56
        dx = 56 if i % 2 == 0 else -56
        s.append(arrow(ax, ry + 90, ax + dx, ry + 90, tc, "arwG", 2, opacity=0.6))
        s.append(label(ax + dx / 2, ry + 78, f"→ {to}", 8.5, tc))
    s.append(panel(60, 885, 880, 120, EXT, "WHAT THE SIX SHARE", [
        (TEXT2, 10.5, "All six are directional and content-addressed: files on disk or JSON over a port — no shared objects, no hidden state."),
        (TEXT2, 10.5, "Two are user-initiated (launch), three are engine-initiated, one is a spawn — the only handoff that runs code is RSIS3 → evaluator."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COLOUR = sender palette; the arrowhead lands in the receiver's colour — read each card as 'sender → receiver'."),
        (TEXT2, 9.5, "THE SPAWN IS SPECIAL: RSIS3 → evaluator runs a verified subprocess, because the judge must never be imported into the judged."),
        (TEXT2, 9.5, "THE LAUNCH IS THE DASH: dashboard → SPACE opens the web UI — the reverse of the telemetry handoff (RSIS3 → dashboard)."),
    ], title="READING THE HANDOFFS"))
    s.append(end("six contracts, zero shared objects — the ecosystem is a graph of files and ports, not a graph of calls"))
    return "\n".join(s)


# ── B-18 · The Repo Map ───────────────────────────────────────────────
def repo_map():
    s = [doc("THE REPO MAP — WHERE EVERYTHING LIVES",
             "One monorepo, three component trees, one dashboard, one redirect")]
    s.append(panel(60, 120, 880, 60, EXT, "cosmos/ — THE MONOREPO ROOT", [
        (TEXT2, 10.5, "index.html → redirects to the unified dashboard · components/ holds the three engines · diagrams/ holds this viewer"),
    ], header_h=32, line_h=22))
    s.append(arrow(500, 180, 500, 210, GRAY, "arwG", 2, opacity=0.6))
    trees = [
        (60, 220, RSIS, "components/rsis3/ — CORE ENGINE", [
            (TEXT2, 10, "dashboard/index.html · the unified hub (port 9000)"),
            (TEXT2, 10, "rack/pulses/ · dashboard-data.json · JSONL buffer"),
            (EXT, 10, "evaluator/evaluator.py · IMMUTABLE · SHA-256 verified"),
            (TEXT2, 10, ".rsis/knowledge_graph.json · .rsis/vectors/ · telemetry/*.jsonl"),
            (TEXT4, 9.5, "112 files · ~67k LOC · Python"),
        ]),
        (60, 520, MYKB, "components/mykb/ — MEMORY", [
            (TEXT2, 10, "wiki/ · 2,360+ markdown pages across 48 domains"),
            (TEXT2, 10, ".wiki-daemon/server.py · search_index.json · graph.json"),
            (TEXT2, 10, "index.html (wiki browser) · okf-graph.html (knowledge graph)"),
            (TEXT2, 10, "git-based temporal snapshots · session capture hooks"),
            (TEXT4, 9.5, "2,436 files · ~58MB · Python + Markdown"),
        ]),
        (60, 820, SPACE, "components/space/ — IDEATION", [
            (TEXT2, 10, "web/index.html · self-contained SPA (port 8888)"),
            (TEXT2, 10, "meta-viewer.html · spec viewer (port 8899)"),
            (TEXT2, 10, "prompt-framework/ · 326 probes · 7 series"),
            (TEXT2, 10, "exports/ · 6 formats · SQLite + filesystem"),
            (TEXT4, 9.5, "150 tests · 14 suites · TypeScript"),
        ]),
    ]
    for x, y, accent, title, rows in trees:
        s.append(panel(x, y, 880, 290, accent, title, rows, header_h=34, pad=16, line_h=26))
    s.append(panel(60, 1130, 880, 100, DASH, "WHY THE SHARED FILESYSTEM MATTERS", [
        (TEXT2, 10.5, "All three engines read/write the same git-tracked tree — temporal recovery, cross-component diffs, and one backup story."),
        (TEXT4, 9.5, "The dashboard lives in rsis3/ but embeds mykb/ and space/ pages — it is the tree's single integration point."),
    ], header_h=32, line_h=24))
    s.append(end("the repo map is the answer to 'where does this live?' — one tree, three engines, one hub"))
    return "\n".join(s)


# ── B-19 · The Runtime Map ────────────────────────────────────────────
def runtime_map():
    s = [doc("THE RUNTIME MAP — WHAT RUNS, WHERE, ON WHICH PORT",
             "GitHub Pages in the cloud · three local servers · one dashboard · one known port conflict")]
    s.append(sect(60, 120, 880, DASH, "CLOUD — GITHUB PAGES", "always on, static"))
    s.append(panel(60, 178, 880, 150, DASH, "github.io — THE STATIC FRONT DOOR", [
        (TEXT2, 10.5, "https://gemquota.github.io/cosmos/ — the cosmos entry point (redirects to the unified dashboard)"),
        (TEXT2, 10.5, "https://gemquota.github.io/hub/ — every non-COSMOS project's dashboard"),
        (TEXT4, 9.5, "Two repos, two Pages deployments, one redirect — the whole cloud surface is static HTML."),
    ], header_h=32, line_h=26))
    s.append(arrow(500, 330, 500, 360, GRAY, "arwG", 2, opacity=0.6))
    s.append(sect(60, 368, 880, RSIS, "LOCAL — THE FOUR SERVERS", "ports are the API"))
    servers = [
        (60, 426, DASH, ":9000", "UNIFIED DASHBOARD", "rsis3/dashboard/index.html · Tailwind + Chart.js", "reads rack/pulses/dashboard-data.json via config.js"),
        (60, 556, MYKB, ":8765", "MYKB DAEMON", ".wiki-daemon/server.py · the only always-on server", "serves search + retrieval to RSIS3, wiki pages to the dashboard"),
        (60, 686, SPACE, ":8888 / :8899", "SPACE WEB UI + META VIEWER", "web/index.html (SPA) + meta-viewer.html", "RRP sessions and spec rendering, user-driven"),
        (60, 816, RSIS, ":8080", "RSIS3 (STATIC BY DEFAULT)", "telemetry + dashboard assets", "static file serving unless the rack binds"),
    ]
    for x, y, accent, port, name, role, note in servers:
        s.append(panel(x, y, 880, 116, accent, f"{name} — {port}", [
            (TEXT2, 10.5, role),
            (TEXT4, 9.5, note),
        ], header_h=32, pad=14, line_h=22))
    s.append(panel(60, 962, 880, 120, EXT, "THE PORT CONFLICT — :8765", [
        (EXT, 10.5, "The MyKB daemon and the RSIS3 rack both want :8765. The daemon is the always-on owner; the rack yields unless it wins the bind."),
        (TEXT2, 9.5, "It is the only resource collision in the ecosystem — and it is a known, documented one, not a discovery."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COLOUR = owning runtime — the same palette as every other diagram: RSIS3 indigo, MyKB cyan, SPACE amber, dashboard green."),
        (TEXT2, 9.5, "CLOUD band is static and read-only; LOCAL band is dynamic — every port above is a contract a client can depend on."),
        (TEXT2, 9.5, "Only one server is always on (:8765); the rest are demand-driven — that asymmetry is why the daemon owns the port."),
    ], title="READING THE RUNTIME MAP"))
    s.append(end("where a thing runs is part of its contract — ports are the ecosystem's addressable surface"))
    return "\n".join(s)


# ── B-20 · The Improvement Stack ──────────────────────────────────────
def improvement_stack():
    s = [doc("THE IMPROVEMENT STACK — ONE IDEA BECOMES MEMORY",
             "Six rungs from ideation to durable memory — the return path is retrieval")]
    rungs = [
        (SPACE, "1 · IDEA", "a probe answer in an RRP session — 326 probes, 7 series"),
        (SPACE, "2 · SPEC", "structured spec draft — exported in 6 formats"),
        (RSIS, "3 · CANDIDATE", "L2 turns the spec into code/diff — evaluator-gated"),
        (DASH, "4 · PULSE", "L1 runs emit telemetry — JSONL, ~1s cadence"),
        (MYKB, "5 · LESSON", "post-session capture — what worked, what didn't"),
        (MYKB, "6 · MEMORY", "KG edge + wiki page — retrievable via :8765"),
    ]
    s.append(stack(170, 120, 660, [(t, a, [(TEXT2, 10.5, d)]) for a, t, d in rungs], gap=34, ch=86))
    s.append(f'<path d="M 830,640 C 920,640 920,300 830,300" fill="none" stroke="{MYKB}" stroke-width="2" stroke-dasharray="7,5" opacity=".85" marker-end="url(#arwM)"/>')
    s.append(label(905, 470, "retrieval · :8765", 9, MYKB))
    s.append(label(905, 486, "memory → next idea", 8, TEXT4))
    s.append(f'<path d="M 500 412 L 512 424 L 500 436 L 488 424 Z" fill="#0b1120" stroke="{EXT}" stroke-width="1.8"/>')
    s.append(label(500, 402, "EVALUATOR GATE", 8, EXT, font=MONO))
    s.append(panel(60, 978, 880, 82, DASH, "THE STACK IN ONE LINE", [
        (TEXT2, 10.5, "idea → spec → candidate → pulse → lesson → memory — every rung is a format change, every arrow is a component handoff."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "UPWARD FLOW = maturation: each rung is produced by the component above's colour — SPACE amber → RSIS3 indigo → DASH green → MyKB cyan."),
        (TEXT2, 9.5, "GATE = between candidate and pulse: the evaluator is the only rung that can send an artifact back down."),
        (TEXT2, 9.5, "RETURN ARC = the stack is a loop: consolidated memory is retrieved (:8765) to seed the next idea."),
        (TEXT2, 9.5, "FOUR COLOURS, SIX RUNGS — the two middle transitions (spec→candidate, pulse→lesson) are RSIS3's two L2/L3 jobs."),
    ], title="READING THE STACK"))
    s.append(end("improvement is not a circle in this system — it is a stack with a return elevator"))
    return "\n".join(s)


# ── B-21 · The Loop Roster ────────────────────────────────────────────
def loop_roster():
    s = [doc("THE LOOP ROSTER — ALL SIX RHYTHMS",
             "Every periodic process, its cadence, its trigger — and the ratios that phase-lock them")]
    rows = [
        ("L1 · ACTION LOOP", "~1s", "per task / tool call", "1 — the base clock", RSIS),
        ("RRP · IDEATION ROUND", "~12s", "per SPACE probe round", "12:1 vs L1", SPACE),
        ("L3 · CONSOLIDATION", "~60s", "per session plateau", "5:1 vs RRP", MYKB),
        ("RETRIEVAL", "on-demand", "L1 asks MyKB :8765", "sporadic", MYKB),
        ("EVALUATOR", "≤5 / session", "L2 candidate generated", "burst · 60s cap", EXT),
        ("TELEMETRY FLUSH", "~1s", "every pulse emitted", "1:1 with L1", DASH),
    ]
    s.append(table(60, 130, [260, 170, 260, 190], ["LOOP", "CADENCE", "TRIGGER", "RATIO"],
                  [(r[0], (r[1], r[4]), r[2], (r[3], r[4])) for r in rows],
                  row_h=46, header_h=38, mono_cols=(1, 3)))
    s.append(sect(60, 470, 880, SPACE, "THE TWO RATIOS THAT PHASE-LOCK THE SYSTEM", "time-compressed"))
    s.append(panel(60, 528, 424, 180, SPACE, "12 : 1 — PULSES PER RRP ROUND", [
        (TEXT2, 10.5, "Twelve L1 pulses fire inside one RRP ideation round."),
        (TEXT2, 10.5, "The engine is executing while SPACE is ideating."),
        (TEXT4, 9.5, "This is the cadence ratio from the coupled-oscillators portrait (E-11)."),
    ], header_h=32, line_h=24))
    s.append(panel(516, 528, 424, 180, RSIS, "25 : 1 — ROUNDS PER SPEC", [
        (TEXT2, 10.5, "Twenty-five RRP rounds refine one spec draft."),
        (TEXT2, 10.5, "The spec is the artifact that survives to become a candidate."),
        (TEXT4, 9.5, "25 rounds × ~12s ≈ the L2 session budget in compressed time."),
    ], header_h=32, line_h=24))
    s.append(panel(60, 736, 880, 140, DASH, "WHAT PHASE-LOCK MEANS HERE", [
        (TEXT2, 10.5, "The loops are not free-running: L1 pulses gate on task boundaries, RRP rounds gate on probe answers, L3 gates on session plateaus."),
        (TEXT2, 10.5, "When the ratios hold, telemetry lines up — 12 pulses per round is visible in dashboard-data.json, not just in theory."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COLOUR = the loop's component: RSIS3 indigo, SPACE amber, MyKB cyan, telemetry green, evaluator pink."),
        (TEXT2, 9.5, "READ CADENCE in compressed diagram time — real seconds are longer; the ratios are the invariant, not the absolute numbers."),
        (TEXT2, 9.5, "RETRIEVAL and EVALUATOR are not periodic — they are event-driven, which is why they break the 1/12/60 ladder."),
    ], title="READING THE ROSTER"))
    s.append(end("six rhythms, two ratios, one ladder — the roster is the system's heartbeat on paper"))
    return "\n".join(s)


# ── B-22 · The Read/Write Ledger ──────────────────────────────────────
def read_write_ledger():
    s = [doc("THE READ/WRITE LEDGER — WHO TOUCHES WHICH STORE",
             "Six persistent stores, four components — every access is a real code path")]
    rows = ["wiki corpus", "TF-IDF index", "KG edges", "spec store", "pulses JSONL", "dashboard-data.json"]
    cols = ["RSIS3", "MYKB", "SPACE", "DASH"]
    cells = [
        (0, 0, "R", DASH), (0, 1, "RW", MYKB), (0, 3, "R", DASH),
        (1, 0, "R", MYKB), (1, 1, "BUILD", MYKB),
        (2, 0, "R", RSIS), (2, 1, "W", MYKB), (2, 3, "R", DASH),
        (3, 0, "R", RSIS), (3, 1, "R", MYKB), (3, 2, "W", SPACE),
        (4, 0, "W", RSIS), (4, 3, "R", DASH),
        (5, 0, "W", RSIS), (5, 3, "R", DASH),
    ]
    s.append(matrix(245, 130, rows, cols, cells, cell_w=118, cell_h=40, header_h=38, gutter=165))
    s.append(label(60, 430, "R = read · W = write · RW = read+write · BUILD = index build · blank = no access", 8.5, TEXT4, anchor="start"))
    s.append(panel(60, 470, 880, 200, MYKB, "THE THREE STORES THAT MATTER", [
        (TEXT2, 10.5, "WIKI CORPUS is the only RW store — MyKB owns it, RSIS3 reads it (retrieval), the dashboard renders it (embed)."),
        (TEXT2, 10.5, "TF-IDF INDEX is derived state: MyKB builds it from the corpus; RSIS3 only queries it. Nobody writes it directly."),
        (TEXT2, 10.5, "PULSES and DASHBOARD-DATA are one pipeline: RSIS3 writes, the dashboard reads — the ledger's simplest row."),
        (TEXT4, 9.5, "The spec store is the odd one: SPACE writes it, but both RSIS3 (consume) and MyKB (archive) read it."),
    ], header_h=32, line_h=24))
    s.append(panel(60, 700, 880, 160, DASH, "THE TEMPORAL LAYER UNDERNEATH", [
        (TEXT2, 10.5, "Every store above is git-tracked — the ledger shows today's access, but time-travel snapshots let any reader restore yesterday's state."),
        (TEXT2, 10.5, "That is why W cells are safe: a bad write is a git revert, not a data loss."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COLOUR of a cell = the runtime that holds the access path — the same four-colour palette as the ownership matrix (B-14)."),
        (TEXT2, 9.5, "B-14 asked WHO RUNS THE CODE; this ledger asks WHO TOUCHES THE DATA — the two matrices are dual views of the same system."),
        (TEXT2, 9.5, "Blank cells are contracts too: the dashboard never writes the corpus; SPACE never touches pulses."),
    ], title="READING THE LEDGER"))
    s.append(end("permission is implicit in the topology — there is no auth layer because there is no cross-write path"))
    return "\n".join(s)


# ── B-23 · The Session Journey ────────────────────────────────────────
def session_journey():
    s = [doc("THE SESSION JOURNEY — ONE SESSION, NINE EVENTS",
             "The real order of operations from cold start to consolidated memory")]
    events = [
        ("START", "RSIS3 boots · L1/L2/L3 armed", RSIS),
        ("L1 RUNS", "tool calls · obs · retries", RSIS),
        ("RETRIEVAL", "MyKB :8765 · ranked context", MYKB),
        ("CANDIDATE", "L2 diff/code drafted", RSIS),
        ("EVAL GATE", "SHA-256 · 60s · verdict", EXT),
        ("PULSE", "JSONL → dashboard-data.json", DASH),
        ("CAPTURE", "session → wiki pages", MYKB),
        ("CONSOLIDATE", "L3 · KG edges + index", MYKB),
        ("NEXT", "retrieval seeds the new session", SPACE),
    ]
    s.append(timeline(90, 910, 300, events, size=8.5, sub_size=7.5))
    s.append(label(500, 385, "one session, left to right — the rail is real time, compressed", 9, TEXT3, italic=True))
    s.append(sect(60, 430, 880, MYKB, "WHERE THE SESSION LEAVES TRACES", "capture hooks"))
    s.append(panel(60, 488, 880, 190, MYKB, "THREE CAPTURE POINTS", [
        (TEXT2, 10.5, "1 · RETRIEVAL is logged — what context the session asked for and got becomes a query record."),
        (TEXT2, 10.5, "2 · EVAL VERDICT is stored with its candidate — the gate's reasoning is part of the artifact's history."),
        (TEXT2, 10.5, "3 · CAPTURE writes the session transcript as wiki pages + KG edges — the durable copy."),
        (TEXT4, 9.5, "Pulses are the only trace that is not memory: telemetry is observability, not knowledge."),
    ], header_h=32, line_h=24))
    s.append(sect(60, 700, 880, EXT, "THE GATE IN THE MIDDLE", "the only rejection point"))
    s.append(panel(60, 758, 880, 160, EXT, "WHAT HAPPENS AT THE EVAL GATE", [
        (TEXT2, 10.5, "Candidate JSON is piped to the immutable evaluator subprocess — SHA-256 verified at startup, read-only mount."),
        (TEXT2, 10.5, "Verdicts (pass/fail + scores) return on stdout; rejected candidates feed the next attempt, up to 5 per session."),
        (TEXT4, 9.5, "If the gate fails the session survives — L2 retries with a better candidate; that retry is itself a recorded pulse."),
    ], header_h=32, line_h=24))
    s.append(panel(60, 950, 880, 70, DASH, "TIMING BUDGET", [
        (TEXT2, 10.5, "L1 ~1s · eval ≤60s · consolidation ~60s — the journey is bounded at every stage by a documented budget."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "RAIL = one session in time; node colour = the runtime doing that step (indigo RSIS3 · cyan MyKB · green telemetry · pink gate)."),
        (TEXT2, 9.5, "THE GATE IS THE ONLY STEP THAT CAN SEND THE SESSION BACKWARD — rejected candidates restart the L2 block."),
        (TEXT2, 9.5, "CAPTURE → CONSOLIDATE is the only pair that is not instant: it is the L3 cycle, running at its own ~60s cadence."),
        (TEXT2, 9.5, "NEXT is SPACE-amber because the journey is a loop — consolidated memory seeds the next idea."),
    ], title="READING THE JOURNEY"))
    s.append(end("a session is a pipeline with one feedback loop — the gate — and one exit: memory"))
    return "\n".join(s)


# ── B-24 · The Integration Timeline ───────────────────────────────────
def integration_timeline():
    s = [doc("THE INTEGRATION TIMELINE — λ1 ENGINE TO λ4 ECOSYSTEM",
             "Four integration stages — each λ is one subsystem joining the constellation")]
    stages = [
        ("λ₁ · ENGINE ONLY", RSIS, "RSIS3 alone", [
            "L1/L2/L3 fire with no external memory",
            "port :8080 static · telemetry local",
            "one fixed point: the loop runs in place",
        ]),
        ("λ₂ · +MEMORY", MYKB, "RSIS3 + MyKB", [
            "lessons persist · retrieval :8765",
            "wiki + KG + temporal snapshots",
            "fixed point becomes a cycle: act → remember",
        ]),
        ("λ₃ · +IDEATION", SPACE, "RSIS3 + MyKB + SPACE", [
            "RRP feeds specs to L2 · 326 probes",
            "evaluator gate between ideation and execution",
            "three basins + separatrix: the contested field",
        ]),
        ("λ₄ · FULL ECOSYSTEM", DASH, "+ dashboard + hub", [
            "unified dashboard embeds all three",
            "GitHub Pages: cosmos/ + hub/",
            "deployed today — the system as shipped",
        ]),
    ]
    y = 130
    for name, accent, who, facts in stages:
        s.append(panel(120, y, 640, 176, accent, name, [
            (accent, 10.5, f"JOINS — {who}"),
        ] + [(TEXT2, 9.5, f"•  {f}") for f in facts], header_h=32, pad=14, line_h=21))
        s.append(label(810, y + 30, "bifurcation", 8.5, TEXT4, anchor="start", font=MONO))
        s.append(label(810, y + 48, "↑ added by λ", 8.5, accent, anchor="start", font=MONO))
        if name != "λ₄ · FULL ECOSYSTEM":
            s.append(arrow(500, y + 176, 500, y + 196, GRAY, "arwG", 2, opacity=0.6))
        y += 216
    s.append(panel(60, 1000, 880, 90, EXT, "LINK TO THE BIFURCATION PORTRAIT (A-13)", [
        (TEXT2, 10.5, "Each λ above is one control-parameter step in the A-13 portrait — λ₄ is the deployed system's position on that diagram."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "STAGE COLOUR = the subsystem that joined at that λ: engine indigo, memory cyan, ideation amber, full ecosystem green."),
        (TEXT2, 9.5, "READ DOWNWARD as history: each stage is a strict superset — λ₄ contains all code from λ₁, plus the new integration layer."),
        (TEXT2, 9.5, "THE BIFURCATION LABELS are the A-13 regimes — every λ is visible there as a change in the phase portrait's topology."),
    ], title="READING THE TIMELINE"))
    s.append(end("the doubling pass ends where the system began — the λ ladder is the answer to 'how did this get here?'"))
    return "\n".join(s)


BASIC6 = {
    "basic-13-artifact-lifecycle.svg": artifact_lifecycle,
    "basic-14-ownership-matrix.svg": ownership_matrix,
    "basic-15-three-jobs.svg": three_jobs,
    "basic-16-data-product-map.svg": data_product_map,
    "basic-17-six-handoffs.svg": six_handoffs,
    "basic-18-repo-map.svg": repo_map,
    "basic-19-runtime-map.svg": runtime_map,
    "basic-20-improvement-stack.svg": improvement_stack,
    "basic-21-loop-roster.svg": loop_roster,
    "basic-22-read-write-ledger.svg": read_write_ledger,
    "basic-23-session-journey.svg": session_journey,
    "basic-24-integration-timeline.svg": integration_timeline,
}
