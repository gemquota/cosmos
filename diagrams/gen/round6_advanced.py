"""Round 6 Advanced tier — how each component works, doubled (A-14…A-26).

Portrait 1000x1320. Content follows the real code: 326 probes / 7 series
names, TF-IDF retrieval, SHA-256 evaluator, capture hooks, JSONL pulses,
7 LLM providers, 6 export formats.
"""
from round6 import *

SERIES7 = [
    ("S1 · CONCEPTUAL DEPTH", 3, 6),
    ("S2 · ONTOLOGICAL CHARACTERISTICS", 5, 15),
    ("S3 · SEMANTIC RELATIONSHIPS", 4, 8),
    ("S4 · PROCEDURAL BREADTH", 3, 6),
    ("S5 · TECHNICAL SPECIFICATIONS", 4, 20),
    ("S6 · DEVELOPMENT METHODOLOGIES", 3, 6),
    ("S7 · OPERATIONAL / FUNCTIONAL", 3, 6),
]


# ── A-14 · The Probe Cascade ──────────────────────────────────────────
def probe_cascade():
    s = [doc("THE PROBE CASCADE — 326 QUESTIONS BECOME ONE SPEC",
             "Seven series fan in, answers merge, one structured spec comes out")]
    s.append(label(500, 108, "seven series, 25 rounds, 326 probes — the input surface of every RRP session", 9.5, TEXT3, italic=True))
    y = 136
    for name, lo, hi in SERIES7:
        s.append(panel(60, y, 560, 74, SPACE, name, [
            (TEXT2, 9.5, f"probes per session: {lo} → {hi} · open-ended share varies by series"),
        ], header_h=30, pad=12, line_h=20))
        s.append(f'<rect x="640" y="{y+14}" width="{hi*8}" height="18" rx="4" fill="{SPACE}" opacity=".75"/>')
        s.append(f'<rect x="640" y="{y+14}" width="{lo*8}" height="18" rx="4" fill="#fde68a" opacity=".95"/>')
        s.append(label(640 + hi * 8 + 12, y + 27, f"{lo}–{hi}", 8.5, TEXT2, anchor="start", font=MONO))
        s.append(label(640 + hi * 8 + 12, y + 44, "per session", 7.5, TEXT4, anchor="start"))
        s.append(arrow(620, y + 40, 660, y + 40, GRAY, "arwG", 1.5, opacity=0.5))
        y += 96
    # merge into answers
    s.append(arrow(500, y - 56, 500, y - 34, SPACE, "arwS", 2.5, opacity=0.8))
    s.append(panel(170, y, 660, 110, SPACE, "25 ROUNDS OF PROBE-ANSWER-REFLECT", [
        (TEXT2, 10.5, "Each round dispatches one probe per active series · answers are kept, ranked, and re-asked when contradictory"),
        (TEXT2, 10.5, "The cursor sweeps the constellation in dispatch order (A-11) — the cascade is that sweep, unrolled"),
    ], header_h=30, line_h=24))
    s.append(arrow(500, y + 110, 500, y + 132, SPACE, "arwS", 2.5, opacity=0.8))
    y += 148
    # output fan
    s.append(sect(60, y, 880, DASH, "THE SPEC EMERGES", "6 export formats"))
    s.append(panel(170, y + 56, 660, 96, DASH, "STRUCTURED SPEC DRAFT", [
        (TEXT2, 10.5, "one artifact, six renderings — MD / JSON / YAML / HTML / XML / TXT"),
        (TEXT4, 9.5, "consumed by RSIS3 L2 as the seed of improvement candidates"),
    ], header_h=30, line_h=24))
    s.append(panel(60, y + 180, 880, 70, EXT, "THE 25 : 1 RATIO", [
        (TEXT2, 10.5, "25 rounds refine one spec — the cascade's output is the most edited artifact in the ecosystem."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "BAR = probe volume per series per session (pale = minimum, amber = maximum) — Technical Specs opens the widest funnel (4→20)."),
        (TEXT2, 9.5, "COLOUR = SPACE amber for the input cascade, DASH green for the spec product, pink for the ratio callout."),
        (TEXT2, 9.5, "READ DOWNWARD as time: seven parallel streams converge once per round, and 25 rounds converge into one spec."),
        (TEXT2, 9.5, "Series order follows the dependency chain S1 → S7 from the probe constellation (A-11)."),
    ], title="READING THE CASCADE"))
    s.append(end("the framework is a funnel: 326 questions in, one spec out — the ecosystem's ideation surface"))
    return "\n".join(s)


# ── A-15 · The Retrieval Path ─────────────────────────────────────────
def retrieval_path():
    s = [doc("THE RETRIEVAL PATH — FROM QUESTION TO CONTEXT",
             "One L1 query, five stages inside MyKB, one ranked context window returned on :8765")]
    stages = [
        ("1 · QUERY", "L1 needs context for the next tool call", RSIS),
        ("2 · TOKENIZE", "lowercase · strip noise · split terms", MYKB),
        ("3 · SCORE", "TF-IDF against the wiki index (48 domains)", MYKB),
        ("4 · RANK", "top-k pages + KG edges nearby", MYKB),
        ("5 · RETURN", "ranked context window → L1, on-demand", RSIS),
    ]
    y = 128
    for i, (name, desc, accent) in enumerate(stages):
        s.append(panel(180, y, 640, 92, accent, name, [(TEXT2, 10, desc)], header_h=30, pad=12, line_h=20))
        if i < 4:
            s.append(arrow(500, y + 92, 500, y + 110, MYKB, "arwM", 2, opacity=0.65))
        y += 122
    s.append(panel(60, y + 6, 880, 120, MYKB, "WHAT THE INDEX KNOWS", [
        (TEXT2, 10.5, "search_index.json — term → postings over the wiki corpus; built by .wiki-daemon, queried over HTTP :8765"),
        (TEXT2, 10.5, "The temporal engine adds time: queries can target a snapshot, not just the latest state of the corpus."),
        (TEXT4, 9.5, "Retrieval is read-only — L1 gets a window, not a lease; the corpus only changes via capture (A-17)."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 800, 880, 100, EXT, "WHY RETRIEVAL IS THE HOT PATH", [
        (TEXT2, 10.5, "It is the only on-demand interface between memory and action — every L1 step that needs context crosses it."),
        (TEXT2, 10.5, "Latency here is L1 latency: a slow daemon slows the action loop, which is why :8765 must be the always-on server."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOUR = who does the stage: indigo when L1 asks/consumes, cyan when the daemon computes."),
        (TEXT2, 9.5, "THE PIPE IS A CONTRACT: query in, ranked window out — both JSON over :8765, both logged for the session record."),
        (TEXT2, 9.5, "RETRIEVAL is deliberately read-only; the mirror write path (capture) is the only way the corpus grows."),
    ], title="READING THE PATH"))
    s.append(end("memory is only useful at the speed of the action loop — this pipe is that speed"))
    return "\n".join(s)


# ── A-16 · The Evaluator's Day ────────────────────────────────────────
def evaluator_day():
    s = [doc("THE EVALUATOR'S DAY — ONE VERDICT, END TO END",
             "From candidate JSON to pass/fail — the only code path RSIS3 may not rewrite")]
    steps = [
        ("1 · CANDIDATE", "L2 drafts diff/code + rationale", RSIS, "JSON, stdin"),
        ("2 · INTEGRITY", "SHA-256 of evaluator.py verified at startup", EXT, "--verify <sha256>"),
        ("3 · SPAWN", "subprocess.run([python, evaluator.py], timeout=60)", EXT, "read-only mount"),
        ("4 · SCORE", "5 dimensions: correctness · safety · efficiency · style · regression", MYKB, "prompt.txt"),
        ("5 · VERDICT", "pass/fail + scores → stdout as JSON", EXT, "stdout"),
        ("6 · APPLY", "pass → apply candidate; fail → L2 retries (≤5/session)", RSIS, "L2 loop"),
    ]
    y = 130
    for i, (name, desc, accent, tag) in enumerate(steps):
        s.append(panel(90, y, 700, 92, accent, name, [
            (TEXT2, 10, desc),
            (TEXT4, 9, f"transport: {tag}"),
        ], header_h=30, pad=12, line_h=20))
        if i < 5:
            s.append(arrow(500, y + 92, 500, y + 110, EXT if i != 4 else RSIS, "arwG", 2, opacity=0.6))
        y += 122
    s.append(panel(60, y + 6, 880, 120, EXT, "THE BOUNDARIES", [
        (TEXT2, 10.5, "The evaluator never imports RSIS3, never touches the repo except read-only, and is never in scope for self-improvement."),
        (TEXT2, 10.5, "Its prompt and code are content-addressed — any drift is caught by the digest check before the spawn."),
        (TEXT4, 9.5, "Budgets: ≤5 candidates per session · 60s per evaluation · verdicts stored with the candidate for audit."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "PINK = the immutable evaluator's steps; indigo = the L2 loop that owns the candidate; cyan = the scoring model."),
        (TEXT2, 9.5, "THE ONLY TWO-STEP LOOP: verdicts flow back to L2, rejected candidates restart at step 1 — the session survives."),
        (TEXT2, 9.5, "Every step is logged — the verdict is part of the artifact's history in MyKB (capture, A-17)."),
    ], title="READING THE DAY"))
    s.append(end("the evaluator is not an oracle — it is a checked subprocess with a contract and a budget"))
    return "\n".join(s)


# ── A-17 · The Memory Write Path ──────────────────────────────────────
def memory_write_path():
    s = [doc("THE MEMORY WRITE PATH — HOW A SESSION BECOMES KNOWLEDGE",
             "Three capture hooks, one consolidation cycle — the only way the corpus grows")]
    s.append(sect(60, 120, 880, MYKB, "CAPTURE HOOKS", "session → durable traces"))
    hooks = [
        (60, 178, "HOOK 1 · RETRIEVAL LOG", "what was asked + what came back", "query record"),
        (60, 268, "HOOK 2 · EVAL VERDICT", "candidate + scores + gate reasoning", "artifact history"),
        (60, 358, "HOOK 3 · SESSION TRANSCRIPT", "tool calls, observations, outcomes", "raw transcript"),
    ]
    for x, y, name, desc, out in hooks:
        s.append(panel(x, y, 880, 74, MYKB, name, [
            (TEXT2, 9.5, f"{desc}  →  {out}"),
        ], header_h=30, pad=12, line_h=20))
    s.append(arrow(500, 432, 500, 458, MYKB, "arwM", 2.5, opacity=0.8))
    s.append(sect(60, 466, 880, RSIS, "L3 CONSOLIDATION", "~60s cycle"))
    cons = [
        (60, 524, "NORMALIZE", "markdown lint · dedupe · link wiki pages"),
        (60, 598, "WRITE", "new wiki page + KG edge in graph.json"),
        (60, 672, "SNAPSHOT", "git commit → temporal engine checkpoint"),
        (60, 746, "REBUILD", "TF-IDF index refresh → retrievable via :8765"),
    ]
    y = 524
    for i, (x, yy, name, desc) in enumerate(cons):
        s.append(panel(x, yy, 880, 58, RSIS if i < 3 else DASH, name, [
            (TEXT2, 9.5, desc),
        ], header_h=28, pad=12, line_h=18))
        if i < 3:
            s.append(arrow(500, yy + 58, 500, yy + 74, GRAY, "arwG", 1.8, opacity=0.6))
    s.append(panel(60, 840, 880, 90, EXT, "THE ORDER IS A LIE — THE TIMING IS REAL", [
        (TEXT2, 10.5, "Hooks 1–3 fire during the session (L1/L2 pace); consolidation runs on the L3 cycle (~60s compressed) after the plateau."),
        (TEXT2, 9.5, "Until L3 runs, the traces exist only as JSONL/transcripts — memory is written in one batch, not continuously."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "CYAN = capture (MyKB hooks); indigo = consolidation stages; green = the index rebuild that makes memory retrievable."),
        (TEXT2, 9.5, "READ DOWNWARD as one pipeline: three hooks feed one batch cycle that ends with retrieval being able to see the new page."),
        (TEXT2, 9.5, "THE SNAPSHOT IS THE SAFETY: every write is a git commit, so the temporal engine can roll any capture back."),
    ], title="READING THE WRITE PATH"))
    s.append(end("memory grows in batches, not streams — capture is cheap, consolidation is the gate"))
    return "\n".join(s)


# ── A-18 · The Pulse Anatomy ──────────────────────────────────────────
def pulse_anatomy():
    s = [doc("THE PULSE ANATOMY — ONE TELEMETRY EVENT, DISSECTED",
             "What a pulse is, who writes it, and how it becomes a dashboard chart")]
    s.append(label(500, 108, "a pulse is the atomic unit of observability — emitted by every loop iteration", 9.5, TEXT3, italic=True))
    # JSON dissected
    s.append(panel(60, 130, 880, 190, DASH, "THE PAYLOAD — what one pulse carries", [
        (TEXT2, 10, '{ "ts": 1753987200, "loop": "L1", "step": "tool_call", "tool": "rg" }'),
        (TEXT2, 10, '{ "outcome": "ok", "duration_ms": 412, "retries": 0 }'),
        (TEXT4, 9, "timestamp · loop · step · tool · outcome · duration · retries — nothing else. Pulses are tiny by design."),
    ], header_h=32, pad=16, line_h=26))
    # path
    s.append(arrow(500, 320, 500, 348, DASH, "arwD", 2.5, opacity=0.8))
    path = [
        ("EMIT", "every loop iteration — L1 tool calls, L2 rounds, L3 cycles", RSIS),
        ("APPEND", "JSONL buffer · rack/pulses/ · append-only", RSIS),
        ("EXTRACT", "rack reads the buffer → dashboard-data.json", DASH),
        ("RENDER", "Chart.js + Tailwind in the dashboard → 20-pulse view", DASH),
        ("EXTRAPOLATE", "TelemetryExtrapolator projects velocity/trends", EXT),
    ]
    y = 356
    for i, (name, desc, accent) in enumerate(path):
        s.append(panel(140, y, 720, 84, accent, name, [(TEXT2, 9.5, desc)], header_h=28, pad=12, line_h=20))
        if i < 4:
            s.append(arrow(500, y + 84, 500, y + 102, DASH, "arwD", 2, opacity=0.6))
        y += 114
    s.append(panel(60, y + 6, 880, 90, EXT, "WHY PULSES ARE NOT MEMORY", [
        (TEXT2, 10.5, "Pulses are observability — high volume, short-lived, append-only. Memory (A-17) is curated, durable, retrievable."),
        (TEXT2, 9.5, "The dashboard reads the latest snapshot; the extrapolator reads the trend; neither rewrites the buffer."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "GREEN = telemetry path (emit → render); pink = the extrapolator that turns history into a forecast."),
        (TEXT2, 9.5, "THE JSON ABOVE IS THE WHOLE CONTRACT — six fields, one line; anything bigger would slow the action loop."),
        (TEXT2, 9.5, "APPEND-ONLY is the integrity model: the buffer is never edited, only consumed — rollback means truncate."),
    ], title="READING THE ANATOMY"))
    s.append(end("observability is a river, not a library — pulses flow past, lessons are kept"))
    return "\n".join(s)


# ── A-19 · The Spec Journey ───────────────────────────────────────────
def spec_journey():
    s = [doc("THE SPEC JOURNEY — INSIDE ONE RRP SESSION",
             "From `space init` to six export formats — the full ideation pipeline")]
    y = 128
    stages = [
        (SPACE, "INIT", "space init — session dir + prompt framework loaded", "t0"),
        (SPACE, "ROUNDS", "25 rounds × probe dispatch across 7 series", "t0 + 25 rounds"),
        (SPACE, "PROVIDERS", "7 LLM providers dispatched per answer (factory pattern)", "per round"),
        (SPACE, "DRAFT", "spec assembled from ranked answers + reflection", "session end"),
        (SPACE, "EXPORT", "6 formats: MD / JSON / YAML / HTML / XML / TXT", "t_end"),
    ]
    for i, (accent, name, desc, tag) in enumerate(stages):
        s.append(panel(110, y, 640, 88, accent, name, [(TEXT2, 9.5, desc)], header_h=30, pad=12, line_h=20))
        s.append(label(790, y + 32, tag, 8.5, TEXT3, anchor="start", font=MONO))
        s.append(label(790, y + 50, "stage", 7.5, TEXT4, anchor="start"))
        if i < 4:
            s.append(arrow(500, y + 88, 500, y + 108, SPACE, "arwS", 2, opacity=0.65))
        y += 120
    s.append(sect(60, y + 2, 880, DASH, "WHERE THE SPECS LAND", "consumers"))
    s.append(panel(60, y + 58, 424, 96, RSIS, "RSIS3 · L2", [
        (TEXT2, 9.5, "imports the canonical spec → drafts improvement candidates"),
    ], header_h=30, line_h=22))
    s.append(panel(516, y + 58, 424, 96, MYKB, "MYKB · ARCHIVE", [
        (TEXT2, 9.5, "keeps exports as wiki-adjacent artifacts for future retrieval"),
    ], header_h=30, line_h=22))
    s.append(panel(60, y + 182, 880, 80, EXT, "THE 7-PROVIDER DISPATCH", [
        (TEXT2, 10.5, "provider = factory product (E-03) — answers are varied by construction, which is what makes 25 rounds converge."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOUR = SPACE amber through the session; green/pink mark where the product is handed to consumers and the audit trail."),
        (TEXT2, 9.5, "STAGE TAGS are real session landmarks — init, rounds, provider dispatch, draft, export."),
        (TEXT2, 9.5, "THE TWO CONSUMERS never touch the session — they only read exports, which keeps SPACE isolated."),
    ], title="READING THE JOURNEY"))
    s.append(end("a spec is what survives the session — everything else in SPACE is process, not product"))
    return "\n".join(s)


# ── A-20 · The Telemetry Graph ────────────────────────────────────────
def telemetry_graph():
    s = [doc("THE TELEMETRY GRAPH — FROM LOOP TO CHART",
             "Four collectors, one buffer, one JSON snapshot, one extrapolator")]
    s.append(label(500, 108, "every loop emits; the rack buffers; the dashboard renders; the extrapolator forecasts", 9.5, TEXT3, italic=True))
    collectors = [
        ("L1 COLLECTOR", "tool calls · observations · retries", RSIS),
        ("L2 COLLECTOR", "candidates · eval verdicts", RSIS),
        ("L3 COLLECTOR", "consolidation reports", RSIS),
        ("SPACE COLLECTOR", "RRP round progress · exports", SPACE),
    ]
    x = 60
    for name, desc, accent in collectors:
        s.append(panel(x, 140, 210, 120, accent, name, [(TEXT2, 8.5, desc)], header_h=28, pad=10, line_h=17))
        s.append(arrow(x + 105, 260, 500, 320, GRAY, "arwG", 1.8, opacity=0.55, curve=(x + 105, 300, 400, 300)))
        x += 226
    s.append(panel(150, 330, 700, 84, DASH, "RACK — JSONL BUFFER", [
        (TEXT2, 9.5, "rack/pulses/ · append-only events · the single sink for all collectors"),
    ], header_h=28, pad=12, line_h=20))
    s.append(arrow(500, 414, 500, 440, DASH, "arwD", 2.5, opacity=0.8))
    s.append(panel(150, 448, 700, 84, DASH, "EXTRACT → DASHBOARD-DATA.JSON", [
        (TEXT2, 9.5, "rack summarizes the buffer into the snapshot config.js reads"),
    ], header_h=28, pad=12, line_h=20))
    s.append(arrow(500, 532, 500, 558, DASH, "arwD", 2.5, opacity=0.8))
    s.append(panel(150, 566, 700, 84, DASH, "CHART.JS VIEWS", [
        (TEXT2, 9.5, "pulses · layers · success rate · 20-pulse window in the dashboard"),
    ], header_h=28, pad=12, line_h=20))
    s.append(panel(60, 700, 880, 110, EXT, "THE EXTRAPOLATOR — HISTORY BECOMES FORECAST", [
        (TEXT2, 10.5, "TelemetryExtrapolator reads the JSONL trend and projects velocity — feeding L3's trend detection."),
        (TEXT2, 10.5, "Forecasts are telemetry, not memory: they inform strategy but are never written to the corpus."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 840, 880, 90, RSIS, "THE LOOP BACK", [
        (TEXT2, 10.5, "L3 consumes the forecast → adjusts strategies → next session emits new pulses — the graph closes on itself."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "GREEN = the telemetry pipeline (emit → buffer → snapshot → render); pink = extrapolation; indigo/amber = collectors."),
        (TEXT2, 9.5, "ONE SINK: every collector converges on the rack's JSONL — that is why dashboard-data.json can summarize the whole system."),
        (TEXT2, 9.5, "THE GRAPH CLOSES: forecasts change strategies, strategies change pulses, pulses change forecasts."),
    ], title="READING THE GRAPH"))
    s.append(end("telemetry is the system watching itself — four collectors, one buffer, one truth"))
    return "\n".join(s)


# ── A-21 · The Module Topology ────────────────────────────────────────
def module_topology():
    s = [doc("THE MODULE TOPOLOGY — EACH COMPONENT FROM THE INSIDE",
             "Three component graphs — the modules that exist and the edges that connect them")]
    sections = [
        (RSIS, "RSIS3 — CORE ENGINE", [
            ("L1 · action loop", 220, 200), ("L2 · improvement", 420, 160), ("L3 · evolution", 620, 200),
            ("evaluator client", 300, 330), ("memory manager", 500, 330), ("telemetry", 700, 330),
            ("rack · pulses", 220, 470), ("evaluator (spawn)", 500, 470), ("recovery", 700, 470),
        ], [
            ("L1 · action loop", "L2 · improvement", RSIS), ("L2 · improvement", "L3 · evolution", RSIS),
            ("L2 · improvement", "evaluator client", RSIS), ("evaluator client", "evaluator (spawn)", EXT),
            ("L3 · evolution", "memory manager", RSIS), ("L1 · action loop", "rack · pulses", DASH),
            ("L2 · improvement", "telemetry", DASH), ("L3 · evolution", "telemetry", DASH),
        ]),
        (MYKB, "MYKB — MEMORY", [
            ("daemon · :8765", 220, 200), ("TF-IDF search", 420, 160), ("temporal engine", 620, 200),
            ("wiki corpus", 300, 330), ("knowledge graph", 500, 330), ("capture hooks", 700, 330),
            ("search index", 220, 470), ("linter", 500, 470), ("git snapshots", 700, 470),
        ], [
            ("daemon · :8765", "TF-IDF search", MYKB), ("daemon · :8765", "temporal engine", MYKB),
            ("TF-IDF search", "search index", MYKB), ("wiki corpus", "TF-IDF search", MYKB),
            ("capture hooks", "wiki corpus", MYKB), ("capture hooks", "knowledge graph", MYKB),
            ("temporal engine", "git snapshots", MYKB), ("wiki corpus", "linter", MYKB),
        ]),
        (SPACE, "SPACE — IDEATION", [
            ("RRP engine", 220, 200), ("probe framework · 326", 420, 160), ("provider factory · 7", 620, 200),
            ("web UI · :8888", 300, 330), ("meta viewer · :8899", 500, 330), ("exports · 6 formats", 700, 330),
            ("session store", 220, 470), ("sqlite", 500, 470), ("tests · 150", 700, 470),
        ], [
            ("RRP engine", "probe framework · 326", SPACE), ("RRP engine", "provider factory · 7", SPACE),
            ("probe framework · 326", "exports · 6 formats", SPACE), ("provider factory · 7", "exports · 6 formats", SPACE),
            ("RRP engine", "web UI · :8888", SPACE), ("RRP engine", "session store", SPACE),
            ("session store", "sqlite", SPACE), ("exports · 6 formats", "meta viewer · :8899", SPACE),
        ]),
    ]
    y = 130
    for accent, title, nodes, edges in sections:
        s.append(sect(60, y, 880, accent, title, "module graph"))
        y += 56
        for name, nx, ny in nodes:
            s.append(f'<circle cx="{nx}" cy="{ny}" r="26" fill="{accent}" opacity=".14" stroke="{accent}" stroke-width="1.4"/>')
            s.append(f'<text x="{nx}" y="{ny}" text-anchor="middle" dominant-baseline="middle" fill="{TEXT}" font-family="{FONT}" font-size="7.8" font-weight="700">{esc(name)}</text>')
        for a, b, c in edges:
            ax = next(nx for n, nx, ny in nodes if n == a)
            ay = next(ny for n, nx, ny in nodes if n == a)
            bx = next(nx for n, nx, ny in nodes if n == b)
            by = next(ny for n, nx, ny in nodes if n == b)
            s.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{c}" stroke-width="1.3" opacity=".5"/>')
        y += 360
    s.append(legend([
        (EXT, 10.5, "NODE = a real module (file/package); EDGE = a real import or data path — the graph is the component's code structure."),
        (TEXT2, 9.5, "SPAWNED = evaluator is reached by subprocess, not import — the only edge drawn pink because it crosses the trust boundary."),
        (TEXT2, 9.5, "Each graph is small (≤9 nodes) — the components are deliberately flat; depth lives in the loops, not the module tree."),
    ], title="READING THE TOPOLOGY"))
    s.append(end("three graphs, twenty-seven modules — the whole codebase's shape on one page"))
    return "\n".join(s)


# ── A-22 · The Failure Cascade ────────────────────────────────────────
def failure_cascade():
    s = [doc("THE FAILURE CASCADE — WHAT DEGRADES, WHAT SURVIVES",
             "Four dependencies, their failure modes, and the degraded modes the system was built for")]
    rows = [
        ("MYKB DAEMON :8765", "retrieval returns nothing", "L1 runs context-free · capture deferred", "daemon restart · buffer replays", EXT),
        ("EVALUATOR TIMEOUT", "candidate gets no verdict", "L2 treats as fail · retries (≤5)", "next candidate · session continues", EXT),
        ("SPACE WEB UI DOWN", "no new RRP sessions", "L2 drafts from stale specs · exports intact", "restart :8888 · session resumes", SPACE),
        ("DASHBOARD DOWN", "no live charts", "pulses keep buffering in JSONL", "reload — snapshot is re-read", DASH),
        ("LLM PROVIDER OUTAGE", "probe answers fail", "RRP retries provider · falls back to another of 7", "provider factory failover (E-03)", SPACE),
        ("WIKI CORRUPTION", "search returns garbage", "temporal engine restores last snapshot", "git revert · index rebuild", MYKB),
    ]
    s.append(table(60, 130, [210, 220, 230, 220], ["DEPENDENCY", "FAILURE MODE", "DEGRADED MODE", "RECOVERY"],
                  [(r[0], r[1], r[2], (r[3], r[4])) for r in rows],
                  row_h=64, header_h=38, mono_cols=(0,)))
    s.append(panel(60, 620, 880, 130, EXT, "WHAT THE TABLE IS REALLY SAYING", [
        (TEXT2, 10.5, "No single failure is fatal: every dependency has a degraded mode, and every degraded mode has a recovery."),
        (TEXT2, 10.5, "The two hardest are evaluator and daemon — one is a trust boundary, the other is the only always-on server."),
        (TEXT4, 9.5, "The port clash (:8765) is the one failure that can happen even when nothing else breaks."),
    ], header_h=32, line_h=26))
    s.append(panel(60, 780, 880, 110, DASH, "THE RESILIENCE LADDER", [
        (TEXT2, 10.5, "1 · degrade gracefully (context-free L1)  →  2 · retry (evaluator, provider)  →  3 · restore (temporal snapshots)"),
        (TEXT2, 10.5, "Checkpoint → HITL → fallback: RSIS3's triple recovery is the same ladder, applied to sessions instead of services."),
    ], header_h=32, line_h=26))
    s.append(legend([
        (EXT, 10.5, "COLOUR = the component whose failure is described — pink for trust/external, amber SPACE, green dashboard, cyan MyKB."),
        (TEXT2, 9.5, "READ ACROSS = one dependency's whole story: mode → symptom → degraded behaviour → recovery path."),
        (TEXT2, 9.5, "DEGRADED MODES are design decisions, not accidents — the system is built to keep acting without memory."),
    ], title="READING THE CASCADE"))
    s.append(end("the failure table is the architecture's honesty document — everything can break, nothing is fatal"))
    return "\n".join(s)


# ── A-23 · The Time Horizon Map ───────────────────────────────────────
def time_horizon_map():
    s = [doc("THE TIME HORIZON MAP — TWO SPECTRA, ALL SIX RHYTHMS",
             "Operation cadence and memory persistence — the system's two clocks laid out")]
    s.append(label(500, 108, "X axis = how often something runs · Y axis = how long what it makes survives", 9.5, TEXT3, italic=True))
    # spectrum 1 — operation cadence
    s.append(sect(60, 136, 880, RSIS, "SPECTRUM 1 · OPERATION CADENCE", "log time"))
    s.append(f'<line x1="90" y1="250" x2="910" y2="250" stroke="{BORDER2}" stroke-width="2" marker-end="url(#arwG)"/>')
    s.append(label(500, 278, "FAST — seconds ←———→ — hours / days", 9.5, TEXT2, font=MONO))
    ops = [
        ("L1 · ~1s", 160, RSIS), ("TELEMETRY · ~1s", 300, DASH), ("RRP ROUND · ~12s", 470, SPACE),
        ("RETRIEVAL · on-demand", 620, MYKB), ("L3 · ~60s", 770, MYKB), ("CROSS-SESSION · hours", 890, RSIS),
    ]
    for name, x, c in ops:
        s.append(f'<circle cx="{x}" cy="250" r="9" fill="{c}" stroke="#0b1120" stroke-width="1.6"/>')
        s.append(label(x, 222, name, 9, c, font=MONO))
    # spectrum 2 — persistence
    s.append(sect(60, 320, 880, MYKB, "SPECTRUM 2 · MEMORY PERSISTENCE", "what survives"))
    s.append(f'<line x1="90" y1="430" x2="910" y2="430" stroke="{BORDER2}" stroke-width="2" marker-end="url(#arwG)"/>')
    s.append(label(500, 458, "EPHEMERAL — volatile ←———→ — PERMANENT · git-tracked", 9.5, TEXT2, font=MONO))
    pers = [
        ("pulse JSONL", 140, DASH), ("eval verdicts", 260, EXT), ("spec drafts", 400, SPACE),
        ("lessons", 530, MYKB), ("KG edges", 680, MYKB), ("wiki corpus", 830, MYKB),
    ]
    for name, x, c in pers:
        s.append(f'<circle cx="{x}" cy="430" r="9" fill="{c}" stroke="#0b1120" stroke-width="1.6"/>')
        s.append(label(x, 402, name, 9, c, font=MONO))
    s.append(panel(60, 500, 880, 170, EXT, "WHAT THE TWO SPECTRA REVEAL", [
        (TEXT2, 10.5, "Fast things make ephemeral things: L1 pulses are the fastest and least durable artifact in the system."),
        (TEXT2, 10.5, "Slow things make permanent things: L3 consolidation is slow precisely because it writes the wiki."),
        (TEXT2, 10.5, "Retrieval sits at the join: it runs on demand (middle of spectrum 1) but serves the most durable store (end of spectrum 2)."),
        (TEXT4, 9.5, "The 12:1 and 25:1 ratios are spectrum-1 facts; the git snapshot is a spectrum-2 fact."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "NODE COLOUR = owning component; X position on each spectrum is the real value, not decorative."),
        (TEXT2, 9.5, "THE DIAGONAL RULE: speed of production and durability of product trade off — the graph is dense along the anti-diagonal."),
        (TEXT2, 9.5, "MEMORY sits right: on-demand latency (fast enough) and permanent storage (durable enough) — the compromise is the point."),
    ], title="READING THE MAP"))
    s.append(end("two spectra are enough to locate every artifact in the ecosystem — speed and survival"))
    return "\n".join(s)


# ── A-24 · The Semantic Overlap Volume ────────────────────────────────
def semantic_overlap_volume():
    s = [doc("THE SEMANTIC OVERLAP VOLUME — ONTOLOGY IN 4D",
             "Three spheres on two semantic axes — size = footprint, colour = component, and time is the 4th axis (λ₁ → λ₄)")]
    s.append(f'<line x1="120" y1="890" x2="880" y2="890" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(label(500, 918, "X — THEORY ←———→ EXECUTION", 10, TEXT3, font=MONO))
    s.append(f'<line x1="120" y1="170" x2="120" y2="880" stroke="{BORDER2}" stroke-width="1.6" marker-end="url(#arwG)" opacity=".9"/>')
    s.append(f'<text x="94" y="530" text-anchor="middle" fill="{TEXT3}" font-family="{MONO}" font-size="9.5" font-weight="700" transform="rotate(-90 94 530)">Y — SHORT-TERM ↑ · LONG-TERM ↓</text>')
    # spheres (centre, radius, colour) — overlaps use screen blend
    spheres = [
        (SPACE, 340, 300, 150),   # theory + short-term (ideation)
        (RSIS, 660, 320, 165),    # execution + short-term (engine)
        (MYKB, 500, 640, 185),    # memory + long-term
    ]
    s.append('<defs>'
             '<radialGradient id="spS" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f59e0b" stop-opacity=".55"/><stop offset="100%" stop-color="#f59e0b" stop-opacity=".05"/></radialGradient>'
             '<radialGradient id="spR" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#818cf8" stop-opacity=".55"/><stop offset="100%" stop-color="#818cf8" stop-opacity=".05"/></radialGradient>'
             '<radialGradient id="spM" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".55"/><stop offset="100%" stop-color="#22d3ee" stop-opacity=".05"/></radialGradient>'
             '</defs>')
    gid = {SPACE: "spS", RSIS: "spR", MYKB: "spM"}
    for c, x, y, r in spheres:
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{gid[c]})" style="mix-blend-mode:screen"/>')
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{c}" stroke-width="1.6" opacity=".8"/>')
    # overlap blend patches (screen_hex)
    pairs = [
        (SPACE, RSIS, screen_hex(SPACE, RSIS), "spec → candidate", 480, 330),
        (RSIS, MYKB, screen_hex(RSIS, MYKB), "lessons → memory", 560, 560),
        (SPACE, MYKB, screen_hex(SPACE, MYKB), "retrieval → ideation", 400, 540),
    ]
    for a, b, blend, tag, lx, ly in pairs:
        c = (blend, blend, blend)
        s.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" fill="{blend}" font-family="{FONT}" font-size="9.5" font-weight="700">{esc(tag)}</text>')
    for c, x, y, r in spheres:
        name = {"#f59e0b": "SPACE", "#818cf8": "RSIS3", "#22d3ee": "MYKB"}[c]
        s.append(f'<text x="{x}" y="{y-8}" text-anchor="middle" fill="{c}" font-family="{FONT}" font-size="14" font-weight="800">{name}</text>')
        s.append(f'<text x="{x}" y="{y+12}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="8">r ∝ footprint</text>')
    # 4th axis — λ morph
    s.append(f'<circle cx="500" cy="740" r="26" fill="none" stroke="{EXT}" stroke-width="1.6" stroke-dasharray="4,4">'
             f'<animate attributeName="r" values="14;26;14" dur="9s" repeatCount="indefinite"/></circle>')
    s.append(label(500, 800, "λ slider — the memory sphere grows with each integration stage (λ₁ → λ₄)", 9, TEXT4))
    s.append(panel(60, 950, 880, 60, EXT, "THE 4D READING", [
        (TEXT2, 10.5, "X + Y place each component in semantic space · r = footprint · colour = component · time = λ morph (the pulsing ring)."),
    ], header_h=30, line_h=24))
    s.append(legend([
        (EXT, 10.5, "OVERLAPS ARE REAL MEANING: blended colour = the interface where two ontologies share semantics (spec, lessons, retrieval)."),
        (TEXT2, 9.5, "PULSING RING = the 4th axis, time: it marks where MYKB sits at λ₂ and expands to where it sits at λ₄ (the A-13 / B-24 ladder)."),
        (TEXT2, 9.5, "SIZE = footprint: RSIS3 67k LOC, MyKB 58MB corpus, SPACE 69k LOC — area encodes weight, not importance."),
        (TEXT2, 9.5, "The three spheres are the same overlap geometry as the ontology venns (B-08/A-08/A-09), promoted to a continuous volume."),
    ], title="READING THE VOLUME"))
    s.append(end("semantics live in the overlaps — the blended regions are where the ecosystem actually does its work"))
    return "\n".join(s)


# ── A-25 · The Interface Contract Table ───────────────────────────────
def interface_contracts():
    s = [doc("THE INTERFACE CONTRACT TABLE — THE FINE PRINT",
             "Six interfaces with transport, payload, error handling and cadence — the spec-level detail")]
    rows = [
        ("SPACE → RSIS3", "filesystem · exports/", "spec draft · 6 formats", "missing draft → L2 stalls", "on-demand", SPACE),
        ("RSIS3 → EVALUATOR", "subprocess · stdin/stdout", "candidate + verdict JSON", "timeout 60s → treated as fail", "≤5/session", EXT),
        ("RSIS3 → DASHBOARD", "JSONL → dashboard-data.json", "pulse events", "buffer survives · no loss", "~1s", DASH),
        ("MYKB → RSIS3", "HTTP :8765", "query + ranked window", "daemon down → context-free L1", "on-demand", MYKB),
        ("RSIS3 → MYKB", "filesystem · wiki + graph", "capture page + KG edge", "write fail → git-safe retry", "post-session", MYKB),
        ("DASHBOARD → SPACE", "browser · link", "open :8888 / :8899", "UI down → link 404", "user-driven", DASH),
    ]
    s.append(table(60, 130, [200, 200, 190, 170, 120], ["INTERFACE", "TRANSPORT", "PAYLOAD", "ERROR MODE", "CADENCE"],
                  [(r[0], r[1], r[2], r[3], (r[4], r[5])) for r in rows],
                  row_h=74, header_h=38, mono_cols=(1,)))
    s.append(panel(60, 640, 880, 130, EXT, "CONTRACT RULES EVERY ENGINEER HERE KNOWS", [
        (TEXT2, 10.5, "1 · Payloads are versioned by directory (exports/, rack/pulses/) — never by ad-hoc schema drift."),
        (TEXT2, 10.5, "2 · Errors are modes, not exceptions — every row above names the degraded behaviour, not a stack trace."),
        (TEXT2, 10.5, "3 · Cadence is part of the contract — on-demand vs ~1s vs post-session changes how clients must buffer."),
    ], header_h=32, line_h=24))
    s.append(panel(60, 800, 880, 90, RSIS, "THE ONLY BIDIRECTIONAL PAIR", [
        (TEXT2, 10.5, "RSIS3 → evaluator → RSIS3: two JSON messages over one subprocess — the contract's tightest loop."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "COLOURED CADENCE CELL = sender palette — the contract is owned by whoever initiates the message."),
        (TEXT2, 9.5, "ERROR MODE column is the contract's most important part: it names the degraded mode from the failure cascade (A-22)."),
        (TEXT2, 9.5, "COMPARE WITH B-17: B-17 shows the six handoffs as cards; this table adds transport and error semantics."),
    ], title="READING THE TABLE"))
    s.append(end("interfaces here are contracts with error modes — the ecosystem is specified, not just sketched"))
    return "\n".join(s)


# ── A-26 · The Component State Machine ────────────────────────────────
def component_state_machine():
    s = [doc("THE COMPONENT STATE MACHINE — THREE ENGINES, THREE LIVES",
             "Every runtime's states, transitions, and the trigger that fires each one")]
    machines = [
        (RSIS, "RSIS3", [
            ("IDLE", "waiting for a task", 300),
            ("ACTING · L1", "tool calls · observations", 130),
            ("IMPROVING · L2", "candidates · eval gate", 470),
            ("CONSOLIDATING · L3", "merge · snapshot · index", 660),
        ], [
            ("IDLE", "ACTING · L1", "task arrives", RSIS),
            ("ACTING · L1", "IMPROVING · L2", "session feedback", SPACE),
            ("IMPROVING · L2", "CONSOLIDATING · L3", "plateau reached", MYKB),
            ("CONSOLIDATING · L3", "IDLE", "cycle complete", DASH),
        ]),
        (MYKB, "MYKB", [
            ("SERVING", "retrieval :8765", 300),
            ("INDEXING", "TF-IDF rebuild", 130),
            ("CAPTURING", "session → wiki + KG", 470),
        ], [
            ("SERVING", "INDEXING", "corpus changed", MYKB),
            ("INDEXING", "SERVING", "index rebuilt", DASH),
            ("SERVING", "CAPTURING", "capture hook fires", RSIS),
            ("CAPTURING", "INDEXING", "pages written", MYKB),
        ]),
        (SPACE, "SPACE", [
            ("COMPOSING", "session dir + framework", 300),
            ("RUNNING", "25 rounds · 7 providers", 130),
            ("EXPORTING", "6 formats · consumers", 470),
        ], [
            ("COMPOSING", "RUNNING", "space init", SPACE),
            ("RUNNING", "EXPORTING", "session ends", DASH),
            ("EXPORTING", "COMPOSING", "next spec", MYKB),
        ]),
    ]
    y = 128
    for accent, name, states, trans in machines:
        s.append(sect(60, y, 880, accent, f"{name} — STATE MACHINE", "states · transitions"))
        y += 52
        for st, desc, sx in states:
            s.append(f'<rect x="{sx}" y="{y}" width="150" height="52" rx="10" fill="{accent}" opacity=".14" stroke="{accent}" stroke-width="1.4"/>')
            s.append(f'<text x="{sx+75}" y="{y+22}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="10" font-weight="700">{esc(st)}</text>')
            s.append(f'<text x="{sx+75}" y="{y+40}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="7.5">{esc(desc)}</text>')
        for a, b, trig, c in trans:
            ax = next(sx for st, desc, sx in states if st == a)
            ay = y + 26
            bx = next(sx for st, desc, sx in states if st == b)
            s.append(f'<path d="M {ax+150} {ay} C {(ax+150+bx)/2} {ay-26}, {(ax+150+bx)/2} {ay-26}, {bx} {ay}" fill="none" stroke="{c}" stroke-width="1.6" opacity=".7" marker-end="url(#arwG)"/>')
            s.append(label((ax + 150 + bx) / 2, ay - 34, trig, 7.5, TEXT4))
        y += 190
    s.append(panel(60, y, 880, 90, EXT, "WHAT THE MACHINES SHARE", [
        (TEXT2, 10.5, "Every transition is triggered by an artifact crossing an interface — the state machines are the interfaces, animated."),
        (TEXT2, 9.5, "RSIS3 is the only machine with four states; MyKB and SPACE are three-state loops — depth lives in the engine."),
    ], header_h=32, line_h=24))
    s.append(legend([
        (EXT, 10.5, "STATE COLOUR = owning component; TRANSITION COLOUR = the component that triggers the move."),
        (TEXT2, 9.5, "READ A MACHINE AS A LOOP: every component returns to a resting state — IDLE / SERVING / COMPOSING."),
        (TEXT2, 9.5, "THE TRIGGER LABELS are real events — task arrives, plateau reached, capture hook fires, space init."),
    ], title="READING THE MACHINES"))
    s.append(end("if you know the trigger, you know the state — the machines are the system's choreography"))
    return "\n".join(s)


ADVANCED6 = {
    "advanced-14-probe-cascade.svg": probe_cascade,
    "advanced-15-retrieval-path.svg": retrieval_path,
    "advanced-16-evaluator-day.svg": evaluator_day,
    "advanced-17-memory-write-path.svg": memory_write_path,
    "advanced-18-pulse-anatomy.svg": pulse_anatomy,
    "advanced-19-spec-journey.svg": spec_journey,
    "advanced-20-telemetry-graph.svg": telemetry_graph,
    "advanced-21-module-topology.svg": module_topology,
    "advanced-22-failure-cascade.svg": failure_cascade,
    "advanced-23-time-horizon-map.svg": time_horizon_map,
    "advanced-24-semantic-overlap-volume.svg": semantic_overlap_volume,
    "advanced-25-interface-contracts.svg": interface_contracts,
    "advanced-26-component-state-machine.svg": component_state_machine,
}
