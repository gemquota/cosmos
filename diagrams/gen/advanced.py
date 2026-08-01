"""Advanced tier diagrams — deeper technical views."""
from design import *

# ── 1. RSIS3 Three-Loop Detail ────────────────────────────────────────
def rsis3_loops():
    w, h = 1400, 900
    s = [svg_start(w, h, "RSIS3 — THREE-LOOP ARCHITECTURE",
        "L1 acts • L2 improves (evaluator-gated) • L3 evolves — with budgets, telemetry, and recovery")]

    loops = [
        (110, 130, RSIS, "L3 — Cross-Session Evolution", "hours / days", [
            (TEXT2, 10.5, "Memory consolidation: git → knowledge graph → vector embeddings"),
            (TEXT2, 10.5, "Strategy & meta-parameter evolution"),
            (TEXT2, 10.5, "Redundancy refinement + pruning"),
            (TEXT2, 10.5, "L2 heuristic evolution from session history"),
            (TEXT4, 9.5, "Plateau: 20 sessions or 24h timeout (L3Config)"),
        ]),
        (110, 390, MYKB, "L2 — Per-Session Improvement", "minutes", [
            (TEXT2, 10.5, "Code generation & architecture modification"),
            (TEXT2, 10.5, "Prompt/tool tuning"),
            (TEXT2, 10.5, "IMMUTABLE AI evaluator gates every candidate"),
            (TEXT4, 9.5, "Max 5 attempts / 30min session (L2Config)"),
        ]),
        (110, 650, SPACE, "L1 — Per-Task Action Loop", "seconds", [
            (TEXT2, 10.5, "Tool calls, observations, retries"),
            (TEXT2, 10.5, "Immediate feedback + checkpoint before mutation"),
            (TEXT4, 9.5, "Max 10 tool calls / step, 120s timeout, 3 retries (L1Config)"),
        ]),
    ]
    for x, y, accent, title, ts, rows in loops:
        s.append(panel(x, y, 900, 200, accent, title, rows, header_h=34, line_h=26))
        s.append(label(x + 900 + 60, y + 24, ts, 11, TEXT3, italic=True))
        s.append(label(x + 900 + 60, y + 46, "timescale", 8.5, TEXT4, italic=True))

    # Feedback arrows
    s.append(arrow(1010, 330, 1010, 388, RSIS, "arwR", 2.5, opacity=0.6))
    s.append(arrow(1010, 590, 1010, 648, MYKB, "arwM", 2.5, opacity=0.6))
    s.append(arrow(1100, 850, 1100, 170, GRAY, "arwG", 1.5, dashed=True, curve=(1150, 850, 1150, 170)))
    s.append(label(1130, 520, "feedback propagates upward", 9.5, TEXT4, italic=True))

    # Right column: support systems
    s.append(panel(1160, 130, 220, 200, EXT, "GOVERNANCE", [
        (TEXT2, 10, "Budgets & deadlines"),
        (TEXT2, 10, "Resource enforcer"),
        (TEXT2, 10, "Recovery manager"),
        (TEXT2, 10, "Checkpoint rollback"),
        (TEXT4, 9, "Triple recovery: checkpoint → HITL → fallback"),
    ], header_h=34, line_h=24))
    s.append(panel(1160, 390, 220, 200, DASH, "TELEMETRY", [
        (TEXT2, 10, "TelemetryCollector"),
        (TEXT2, 10, "JSONL event buffer"),
        (TEXT2, 10, "TelemetryExtrapolator"),
        (TEXT2, 10, "Velocity reports"),
        (TEXT4, 9, "Feeds L3 trend detection"),
    ], header_h=34, line_h=24))
    s.append(panel(1160, 650, 220, 200, SPACE, "MEMORY", [
        (TEXT2, 10, "KnowledgeGraph"),
        (TEXT2, 10, "VectorStore"),
        (TEXT2, 10, "MemoryManager"),
        (TEXT4, 9, ".rsis/knowledge_graph.json"),
        (TEXT4, 9, ".rsis/vectors/"),
    ], header_h=34, line_h=24))

    s.append(svg_end(w))
    return "\n".join(s)

# ── 2. MyKB Search Pipeline ───────────────────────────────────────────
def mykb_search():
    w, h = 1400, 900
    s = [svg_start(w, h, "MyKB — SEARCH PIPELINE",
        "From 2,360+ markdown pages to ranked results: indexing path (top) and query path (bottom)")]

    # Index path
    s.append(label(130, 120, "⬇ INDEX BUILD (offline)", 11, MYKB))
    steps = [
        (110, 140, "wiki/", "2,360+ .md pages\n48 domains", MYKB),
        (300, 140, "chunk_markdown()", "split by headers\n+ code signatures", MYKB),
        (490, 140, "tokenize()", "word tokens\nfor scoring", MYKB),
        (680, 140, "build_indices()", "TF-IDF vectors\nterm-doc matrix", MYKB),
        (870, 140, "save_index()", "search_index.json\nidf + paths", MYKB),
    ]
    for x, y, title, sub, accent in steps:
        s.append(panel(x, y, 170, 95, accent, title, [
            (TEXT2, 9, two_line(sub)[0]), (TEXT3, 9, two_line(sub)[1]),
        ], header_h=28, line_h=16, title_size=10.5))
        if x < 1000:
            s.append(arrow(x + 170, y + 47, x + 198, y + 47, MYKB, "arwM", 2, opacity=0.6))

    # Query path
    s.append(label(130, 300, "⬇ QUERY (online, port 8765)", 11, SPACE))
    qsteps = [
        (110, 320, "GET /api/v2/search/hybrid?q=", "user query from UI / RSIS3", SPACE),
        (350, 320, "search_query()", "TF-IDF cosine scores\nover chunks", SPACE),
        (590, 320, "rrf_fusion()", "dense + sparse\nreciprocal rank fusion", SPACE),
        (830, 320, "result ranking", "score → top_n=30\npath + title", SPACE),
        (1070, 320, "Response", "JSON to caller\nwiki pages openable", DASH),
    ]
    for x, y, title, sub, accent in qsteps:
        s.append(panel(x, y, 210, 95, accent, title, [
            (TEXT2, 9, two_line(sub)[0]), (TEXT3, 9, two_line(sub)[1]),
        ], header_h=28, line_h=16, title_size=10))
        if x < 1200:
            s.append(arrow(x + 210, y + 47, x + 238, y + 47, SPACE, "arwS", 2, opacity=0.6))

    # Detail: scoring formula
    s.append(panel(110, 460, 610, 130, MYKB, "SCORING — TF-IDF", [
        (TEXT2, 10, "score(doc) = Σ  tf(w, doc) × idf(w)", MONO),
        (TEXT2, 10, "tf  = word count in doc / total words", MONO),
        (TEXT2, 10, "idf = inverse document frequency across wiki", MONO),
        (TEXT4, 9, "Implemented in server.py search_query() + search_fusion.py"),
    ], header_h=34, line_h=24))

    # Detail: RRF fusion
    s.append(panel(750, 460, 540, 130, SPACE, "HYBRID FUSION — RRF", [
        (TEXT2, 10, "rrf_fusion(dense, sparse, k=60, top_n=30)", MONO),
        (TEXT2, 10, "score = Σ 1 / (k + rank_i)  across result sets", MONO),
        (TEXT2, 10, "combines semantic + lexical rankings", MONO),
        (TEXT4, 9, "Dense path: vector similarity • Sparse path: TF-IDF"),
    ], header_h=34, line_h=24))

    # Consumers
    s.append(label(130, 630, "⬇ WHO CONSUMES SEARCH", 11, DASH))
    consumers = [
        (110, 650, "RSIS3 MemoryManager", "get_relevant_patterns(goal)\nfeeds L2 improvement context", RSIS),
        (460, 650, "Wiki UI", "okf-graph.html search box\ninteractive exploration", MYKB),
        (810, 650, "Temporal engine", "history + snapshots\nsnapshot at timestamp", DASH),
    ]
    for x, y, title, sub, accent in consumers:
        s.append(panel(x, y, 300, 85, accent, title, [
            (TEXT2, 9, two_line(sub)[0]), (TEXT3, 9, two_line(sub)[1]),
        ], header_h=28, line_h=16, title_size=10.5))

    s.append(panel(110, 770, 1180, 70, EXT, "STORAGE", [
        (TEXT2, 10, ".wiki-daemon/search_index.json  •  .wiki-daemon/graph.json  •  wiki/ (source of truth)"),
        (TEXT4, 9, "Index rebuilt via POST /api/v2/search/build — incremental chunking keeps it fresh"),
    ], header_h=32, line_h=20))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 3. SPACE Session Lifecycle ────────────────────────────────────────
def space_session():
    w, h = 1400, 900
    s = [svg_start(w, h, "SPACE — SESSION LIFECYCLE",
        "From `space init` to 6 export formats: the RRP session journey")]

    phases = [
        (110, 130, "space init <name>", "scaffolds project\n.space.json + dirs", SPACE),
        (330, 130, "space run <project>", "loads framework\n326 probes • 7 series", SPACE),
        (550, 130, "Session rounds", "25 rounds\nopen → mixed → choice", SPACE),
        (770, 130, "question-router", "getCurrentQuestion()\nadvanceToNextQuestion()", SPACE),
        (990, 130, "LLM providers", "7 providers refine\nand generate answers", SPACE),
        (1210, 130, "artifact tracker", "collects answers\n+ extracted artifacts", SPACE),
    ]
    for x, y, title, sub, accent in phases:
        s.append(panel(x, y, 190, 95, accent, title, [
            (TEXT2, 9, two_line(sub)[0]), (TEXT3, 9, two_line(sub)[1]),
        ], header_h=28, line_h=16, title_size=10))
        if x < 1300:
            s.append(arrow(x + 190, y + 47, x + 218, y + 47, SPACE, "arwS", 2, opacity=0.6))

    # Completion
    s.append(panel(110, 260, 310, 90, DASH, "Session completion", [
        (TEXT2, 9.5, "computeCompletionPct() → 100%"),
        (TEXT2, 9.5, "markSessionCompleted()"),
        (TEXT4, 9, "serializeSession() persists state"),
    ], header_h=30, line_h=20))
    s.append(panel(450, 260, 310, 90, MYKB, "Intelligence layer", [
        (TEXT2, 9.5, "computeSessionMetrics()"),
        (TEXT2, 9.5, "scoreCompleteness()"),
        (TEXT2, 9.5, "detectContradictions()"),
    ], header_h=30, line_h=20))
    s.append(panel(790, 260, 310, 90, EXT, "Quality & recommendations", [
        (TEXT2, 9.5, "quality-scorer grades responses"),
        (TEXT2, 9.5, "generateRecommendations()"),
        (TEXT2, 9.5, "adaptive-router skips stale Qs"),
    ], header_h=30, line_h=20))

    s.append(arrow(420, 305, 448, 305, GRAY, "arwG", 2, opacity=0.5))
    s.append(arrow(760, 305, 788, 305, GRAY, "arwG", 2, opacity=0.5))
    s.append(arrow(1100, 305, 1128, 305, GRAY, "arwG", 2, opacity=0.5))

    # Export
    s.append(label(130, 400, "⬇ EXPORT (space export)", 11, SPACE))
    s.append(panel(110, 420, 1180, 130, SPACE, "exportSession() — 6 FORMATTERS", [
        (TEXT2, 10, "json-exporter    markdown-exporter    yaml-exporter    html-exporter    prompt-exporter    diff-exporter"),
        (TEXT2, 10, "→ specification.md / .json / .yaml / .html → written to exports/"),
        (TEXT4, 9, "exportDiff() produces git-style diffs for change review • staleness metadata attached to exports"),
    ], header_h=32, line_h=24))

    # Consumers
    s.append(label(130, 590, "⬇ WHO CONSUMES THE EXPORTS", 11, DASH))
    consumers = [
        (110, 610, "RSIS3", "spec → improvement goals\nL2 session context", RSIS),
        (520, 610, "MyKB wiki", "specification.md → wiki page\nsession.json → ops/workflows", MYKB),
        (930, 610, "External docs", "HTML specs → GH Pages\ndiff → review/CI", DASH),
    ]
    for x, y, title, sub, accent in consumers:
        s.append(panel(x, y, 340, 85, accent, title, [
            (TEXT2, 9.5, two_line(sub)[0]), (TEXT3, 9.5, two_line(sub)[1]),
        ], header_h=28, line_h=16, title_size=11))

    s.append(panel(110, 730, 1180, 80, EXT, "STORAGE", [
        (TEXT2, 10, "FileSystemStorage (JSON on disk)  +  SQLite backend  +  AutoSaveManager (periodic saves)"),
        (TEXT4, 9, "Session state lives in <project>/sessions/ • exports in <project>/exports/ • .space.json holds project metadata"),
    ], header_h=32, line_h=20))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 4. Memory Hierarchy ───────────────────────────────────────────────
def memory_hierarchy():
    w, h = 1400, 900
    s = [svg_start(w, h, "MEMORY HIERARCHY",
        "Four tiers from ephemeral runtime state to durable, queryable knowledge")]

    tiers = [
        (110, 120, "TIER 0 — Ephemeral Runtime", EXT, [
            (TEXT2, 10, "L1 tool calls & in-loop context"),
            (TEXT2, 10, "TelemetryCollector in-memory buffer"),
            (TEXT2, 10, "Session state (SPACE SessionState)"),
            (TEXT4, 9.5, "Lifetime: seconds — lost on process exit"),
        ], 150),
        (110, 310, "TIER 1 — Session Files (.rsis/)", RSIS, [
            (TEXT2, 10, "knowledge_graph.json — improvement nodes"),
            (TEXT2, 10, "vectors/index.json — semantic embeddings"),
            (TEXT2, 10, "telemetry/*.jsonl — event log"),
            (TEXT2, 10, "checkpoints — git commits for rollback"),
            (TEXT4, 9.5, "Lifetime: sessions — durable on disk, per-component"),
        ], 150),
        (110, 500, "TIER 2 — Wiki Knowledge (mykb/)", MYKB, [
            (TEXT2, 10, "wiki/ — 2,360+ pages across 48 domains"),
            (TEXT2, 10, ".wiki-daemon/ — search_index.json, graph.json"),
            (TEXT2, 10, "daily/ — daily notes, raw/ — inbox"),
            (TEXT2, 10, "templates/ — note templates, hooks/ — capture"),
            (TEXT4, 9.5, "Lifetime: indefinite — git-tracked, time-travel capable"),
        ], 170),
        (110, 710, "TIER 3 — External & Exported", SPACE, [
            (TEXT2, 10, "space/exports/ — specs in 6 formats"),
            (TEXT2, 10, "space/prompt-framework/ — 326 probes"),
            (TEXT2, 10, "GitHub Pages — deployed dashboards"),
            (TEXT4, 9.5, "Lifetime: indefinite — shared with the world"),
        ], 150),
    ]
    for x, y, title, accent, rows, hh in tiers:
        s.append(panel(x, y, 620, hh, accent, title, rows, header_h=34, line_h=22))
        # pyramid arrows on left
        s.append(label(x + 660, y + 30, "fast / volatile", 8.5, TEXT4, italic=True))
        s.append(label(x + 660, y + 44, "▼", 10, TEXT4))
        s.append(label(x + 660, y + hh - 20, "slow / durable", 8.5, TEXT4, italic=True))

    # Right: access patterns
    s.append(panel(800, 120, 500, 170, MYKB, "READS (knowledge in)", [
        (TEXT2, 10, "RSIS3 → MemoryManager.get_relevant_patterns()"),
        (TEXT2, 10, "RSIS3 → MyKB /api/v2/search/hybrid"),
        (TEXT2, 10, "SPACE → wiki context for question routing"),
        (TEXT4, 9.5, "All retrieval is search-or-path based, not raw DB"),
    ], header_h=34, line_h=24))
    s.append(panel(800, 330, 500, 170, RSIS, "WRITES (knowledge out)", [
        (TEXT2, 10, "RSIS3 → .rsis/ knowledge graph + telemetry"),
        (TEXT2, 10, "SPACE → exports/*.md → wiki pages"),
        (TEXT2, 10, "MyKB → daily notes via session capture hooks"),
        (TEXT4, 9.5, "Checkpoint-before-mutation on every write"),
    ], header_h=34, line_h=24))
    s.append(panel(800, 540, 500, 170, DASH, "RETRIEVAL PATHS", [
        (TEXT2, 10, "Hybrid search: TF-IDF + RRF fusion"),
        (TEXT2, 10, "Knowledge graph queries (graph.json)"),
        (TEXT2, 10, "Vector similarity (semantic recall)"),
        (TEXT2, 10, "Temporal snapshots (time travel)"),
    ], header_h=34, line_h=24))
    s.append(panel(800, 750, 500, 110, EXT, "CONSISTENCY", [
        (TEXT2, 10, "Single source of truth: filesystem"),
        (TEXT2, 10, "Indexes are derived (rebuildable)"),
        (TEXT4, 9.5, "git commits enable rollback everywhere"),
    ], header_h=34, line_h=22))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 5. Orchestration & Dashboard ──────────────────────────────────────
def orchestration():
    w, h = 1400, 900
    s = [svg_start(w, h, "ORCHESTRATION & DASHBOARD",
        "How the cosmos CLI, dashboard, and heartbeat keep the ecosystem running")]

    # CLI
    s.append(panel(110, 120, 380, 260, DASH, "cosmos CLI", [
        (TEXT2, 10, "cosmos start all   — all servers"),
        (TEXT2, 10, "cosmos status      — health polls"),
        (TEXT2, 10, "cosmos stop        — kill all"),
        (TEXT2, 10, "cosmos list        — file counts"),
        (TEXT2, 10, "cosmos logs        — sentry.log"),
        (TEXT2, 10, "cosmos build       — TS builds"),
        (TEXT2, 10, "cosmos test        — component tests"),
        (TEXT4, 9, "symlinked to ~/.local/bin/cosmos"),
    ], header_h=34, line_h=22))

    # Dashboard
    s.append(panel(540, 120, 380, 260, MYKB, "Dashboard (port 9000)", [
        (TEXT2, 10, "6 component cards + status"),
        (TEXT2, 10, "global health badge"),
        (TEXT2, 10, "meta document viewer"),
        (TEXT2, 10, "quick links to servers"),
        (TEXT2, 10, "donut + stacked bar charts"),
        (TEXT4, 9, "33KB self-contained SPA (index.html)"),
        (TEXT4, 9, "served by start.sh → python http.server"),
    ], header_h=34, line_h=22))

    # Heartbeat
    s.append(panel(970, 120, 320, 260, EXT, "Sentry Heartbeat", [
        (TEXT2, 10, "watches.json definitions"),
        (TEXT2, 10, "polls ports 9000, 8888, 8899"),
        (TEXT2, 10, "auto-restart on failure"),
        (TEXT2, 10, "centralized sentry.log"),
        (TEXT4, 9, "infra/heartbeat/heartbeat.mjs"),
        (TEXT4, 9, "component-prefixed log lines"),
    ], header_h=34, line_h=22))

    # iframe embeds
    s.append(panel(110, 430, 1180, 120, DASH, "DASHBOARD IFRAME EMBEDS (port 9000)", [
        (TEXT2, 10, "/components/rsis3/dashboard/        → RSIS3 telemetry (Chart.js + Tailwind)"),
        (TEXT2, 10, "http://localhost:8765/              → MyKB wiki (own server)"),
        (TEXT2, 10, "/components/space/web/              → SPACE web UI (React)"),
        (TEXT4, 9, "Each component keeps its own UI — the dashboard aggregates, never duplicates"),
    ], header_h=34, line_h=24))

    # Health check flow
    s.append(label(130, 590, "⬇ HEALTH-CHECK FLOW", 11, EXT))
    hc = [
        (110, 610, "cosmos status", "user or cron", EXT),
        (360, 610, "HTTP GET /", "port 9000", EXT),
        (610, 610, "component fetch()", "localhost:{port}", EXT),
        (860, 610, "ONLINE / OFFLINE", "badge per card", DASH),
        (1110, 610, "heartbeat restart", "if offline", DASH),
    ]
    for x, y, title, sub, accent in hc:
        s.append(panel(x, y, 220, 70, accent, title, [
            (TEXT2, 9.5, sub),
        ], header_h=28, line_h=18, title_size=10.5))
        if x < 1200:
            s.append(arrow(x + 220, y + 35, x + 248, y + 35, EXT, "arwH", 2, opacity=0.6))

    # Ports
    s.append(panel(110, 730, 1180, 90, RSIS, "SERVICE REGISTRY", [
        (TEXT2, 10, "9000  Dashboard/static   8765  MyKB server   8888  SPACE Web UI   8899  SPACE Meta Viewer   8080  RSIS3 (optional)"),
        (TEXT4, 9, "start.sh: frees stale ports, starts main server + MyKB, records PIDs in .cosmos-pids/"),
    ], header_h=32, line_h=22))
    s.append(svg_end(w))
    return "\n".join(s)

ADVANCED = {
    "advanced-01-rsis3-loops.svg": rsis3_loops,
    "advanced-02-mykb-search.svg": mykb_search,
    "advanced-03-space-session.svg": space_session,
    "advanced-04-memory-hierarchy.svg": memory_hierarchy,
    "advanced-05-orchestration.svg": orchestration,
}
