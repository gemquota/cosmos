"""Expert tier diagrams — code-level pipelines and internals."""
from design import *

# ── 1. Evaluator Pipeline ─────────────────────────────────────────────
def evaluator_pipeline():
    w, h = 1600, 1000
    s = [svg_start(w, h, "RSIS3 — EVALUATOR PIPELINE",
        "How improvements get validated: L2 candidate → immutable evaluator → PASS/FAIL gate")]

    # Step 1: candidate
    s.append(panel(110, 130, 300, 150, RSIS, "L2ImprovementLoop", [
        (TEXT2, 10, "_generate_candidate(goal)"),
        (TEXT2, 10, "→ ImprovementCandidate"),
        (TEXT2, 10, "  description, target_files,"),
        (TEXT2, 10, "  diff_or_code, rationale"),
        (TEXT4, 9, "max 5 attempts per session"),
    ], header_h=32, line_h=20))
    s.append(arrow(410, 205, 448, 205, RSIS, "arwR", 2.5, opacity=0.8))

    # Step 2: integrity
    s.append(panel(450, 130, 300, 150, MYKB, "EvaluatorClient", [
        (TEXT2, 10, "verify_integrity()"),
        (TEXT2, 10, "→ SHA-256 digest of"),
        (TEXT2, 10, "  evaluator/evaluator.py"),
        (TEXT2, 10, "startup_digest_verify=True"),
        (TEXT4, 9, "read_only_mount=True"),
    ], header_h=32, line_h=20))
    s.append(arrow(750, 205, 788, 205, MYKB, "arwM", 2.5, opacity=0.8))

    # Step 3: subprocess
    s.append(panel(790, 130, 320, 150, SPACE, "subprocess.run()", [
        (TEXT2, 10, "[sys.executable, evaluator.py]"),
        (TEXT2, 10, "input=json.dumps(candidate)"),
        (TEXT2, 10, "capture_output, timeout=60s"),
        (TEXT2, 10, "evaluator runs in isolation"),
        (TEXT4, 9, "never in scope for self-improvement"),
    ], header_h=32, line_h=20))
    s.append(arrow(1110, 205, 1148, 205, SPACE, "arwS", 2.5, opacity=0.8))

    # Step 4: evaluator box (large)
    s.append(panel(1150, 130, 340, 260, EXT, "evaluator/evaluator.py — IMMUTABLE", [
        (TEXT2, 10, "Standalone read-only process"),
        (TEXT2, 10, "Reads candidate from stdin"),
        (TEXT2, 10, "Scores 5 dimensions:"),
        (TEXT4, 9, "  correctness, safety, efficiency,"),
        (TEXT4, 9, "  style, regression"),
        (TEXT2, 10, "Returns JSON decision"),
        (TEXT4, 9, "Prompt: evaluator/prompt.txt"),
        (TEXT4, 9, "--verify <sha256> at startup"),
    ], header_h=32, line_h=20))

    # Result
    s.append(panel(110, 420, 480, 130, DASH, "EvalResult (dataclass)", [
        (TEXT2, 10, "decision: \"PASS\" | \"FAIL\""),
        (TEXT2, 10, "scores: dict — 5 dimensions"),
        (TEXT2, 10, "rationale + suggestions"),
        (TEXT2, 10, "passed → decision == \"PASS\""),
        (TEXT2, 10, "score_avg → mean of scores"),
    ], header_h=32, line_h=20))

    # Branch: PASS / FAIL
    s.append(arrow(630, 555, 620, 610, DASH, "arwD", 2.5, opacity=0.8))
    s.append(panel(420, 615, 380, 140, DASH, "PASS — apply improvement", [
        (TEXT2, 10, "_apply_improvement(candidate)"),
        (TEXT2, 10, "checkpoint before mutation"),
        (TEXT2, 10, "memory.record_improvement()"),
        (TEXT2, 10, "→ KG + vector store"),
    ], header_h=32, line_h=20))

    s.append(arrow(1100, 555, 1140, 610, EXT, "arwH", 2.5, opacity=0.8))
    s.append(panel(940, 615, 380, 140, EXT, "FAIL — discard + recover", [
        (TEXT2, 10, "discard candidate"),
        (TEXT2, 10, "log failure pattern"),
        (TEXT2, 10, "recovery.record_failure()"),
        (TEXT2, 10, "retry or escalate to L3"),
    ], header_h=32, line_h=20))

    # Loop back
    s.append(arrow(800, 755, 800, 330, GRAY, "arwG", 2, dashed=True, curve=(880, 755, 880, 330)))
    s.append(label(900, 560, "next attempt (up to 5)", 9.5, TEXT4, italic=True))

    # Timeout/error paths
    s.append(panel(110, 620, 260, 130, EXT, "Failure modes", [
        (TEXT2, 10, "TimeoutExpired → FAIL"),
        (TEXT2, 10, "process error → FAIL"),
        (TEXT2, 10, "non-zero exit → FAIL"),
        (TEXT4, 9, "rationale records the cause"),
    ], header_h=32, line_h=20))
    s.append(arrow(310, 555, 300, 618, EXT, "arwH", 2, opacity=0.5))

    # Bottom summary
    s.append(panel(110, 790, 1380, 110, MYKB, "WHY IMMUTABLE", [
        (TEXT2, 10.5, "The evaluator is the only component never modified by the system — it is the trust anchor for self-improvement."),
        (TEXT2, 10.5, "SHA-256 digest verification at startup detects any tampering before a single candidate is judged."),
        (TEXT4, 9.5, "L2 generates → evaluator judges → L1 executes approved changes → L3 consolidates what was learned"),
    ], header_h=34, line_h=26))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 2. Telemetry & Extrapolation ──────────────────────────────────────
def telemetry_pipeline():
    w, h = 1600, 1000
    s = [svg_start(w, h, "RSIS3 — TELEMETRY & EXTRAPOLATION",
        "From raw events to strategic insight: how L3 learns from every session")]

    # Event sources
    s.append(panel(110, 130, 380, 140, RSIS, "EVENT SOURCES", [
        (TEXT2, 10, "L1ActionLoop — l1_start, l1_complete"),
        (TEXT2, 10, "L2ImprovementLoop — session events"),
        (TEXT2, 10, "L3EvolutionLoop — cycle events"),
        (TEXT2, 10, "WorkspaceMonitor — file activity"),
    ], header_h=32, line_h=22))

    # TelemetryEvent
    s.append(panel(560, 130, 330, 140, MYKB, "TelemetryEvent", [
        (TEXT2, 10, "event_type, path, delta"),
        (TEXT2, 10, "duration_ms, metadata"),
        (TEXT2, 10, "timestamp (UTC ISO)"),
        (TEXT4, 9, "to_dict() flattens metadata"),
    ], header_h=32, line_h=22))
    s.append(arrow(490, 200, 558, 200, RSIS, "arwR", 2.5, opacity=0.7))

    # Collector
    s.append(panel(960, 130, 340, 140, MYKB, "TelemetryCollector", [
        (TEXT2, 10, "record(event) → buffer"),
        (TEXT2, 10, "flush() every 5s (threaded)"),
        (TEXT2, 10, "_session_id = uuid4()"),
        (TEXT2, 10, "start()/stop() lifecycle"),
    ], header_h=32, line_h=22))
    s.append(arrow(890, 200, 958, 200, MYKB, "arwM", 2.5, opacity=0.7))

    # JSONL storage
    s.append(panel(110, 350, 1180, 90, EXT, ".rsis/telemetry/*.jsonl", [
        (TEXT2, 10, "one JSON event per line • session-scoped filenames (uuid_timestamp.jsonl) • append-only"),
        (TEXT4, 9, "persists across processes → the raw material for L3 analysis"),
    ], header_h=32, line_h=24))

    s.append(arrow(1130, 270, 700, 348, EXT, "arwH", 2.5, curve=(1000, 300, 900, 310)))
    s.append(arrow(700, 348, 500, 350, EXT, "arwH", 2, opacity=0.4))

    # Extrapolator
    s.append(panel(110, 500, 420, 230, RSIS, "TelemetryExtrapolator", [
        (TEXT2, 10, "load_events(force=False)"),
        (TEXT2, 10, "get_sessions()"),
        (TEXT2, 10, "_build_session(events)"),
        (TEXT2, 10, "_cache for repeated reads"),
        (TEXT4, 9, "analyses across ALL sessions"),
    ], header_h=32, line_h=22))

    # Outputs
    outs = [
        (580, 500, "predict_optimal_iterations()", "optimal L2 budget\nfrom eval curves", DASH),
        (860, 500, "detect_regression_trends()", "performance regression\nbefore thresholds", DASH),
        (1140, 500, "find_redundancy_candidates()", "code areas needing\npruning", DASH),
    ]
    for x, y, title, sub, accent in outs:
        s.append(panel(x, y, 260, 100, accent, title, [
            (TEXT2, 9.5, two_line(sub)[0]), (TEXT3, 9.5, two_line(sub)[1]),
        ], header_h=30, line_h=18, title_size=10))
        s.append(arrow(x - 60, 550, x - 18, 550, RSIS, "arwR", 2, opacity=0.6))

    s.append(panel(580, 640, 820, 90, SPACE, "generate_velocity_report()", [
        (TEXT2, 10, "cross-session improvement velocity → used in L3 reports and strategy evolution"),
        (TEXT4, 9, "statistics module: means, trends, deltas across session groups"),
    ], header_h=32, line_h=24))

    # L3 consumption
    s.append(panel(110, 790, 1380, 110, MYKB, "CONSUMED BY L3EvolutionLoop", [
        (TEXT2, 10.5, "_detect_trends() → _consolidate_memory() → _evolve_strategies() → _refine_redundancies()"),
        (TEXT2, 10.5, "Insights land in the knowledge graph → next session's retrieval context"),
        (TEXT4, 9.5, "The loop closes: L1/L2 produce telemetry → L3 turns it into better L1/L2 behavior"),
    ], header_h=34, line_h=26))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 3. SPACE LLM Provider Architecture ────────────────────────────────
def llm_providers():
    w, h = 1600, 1000
    s = [svg_start(w, h, "SPACE — LLM PROVIDER ARCHITECTURE",
        "Factory pattern: one interface, 7 providers, multiple consumers")]

    # Config
    s.append(panel(110, 130, 300, 150, SPACE, "SpaceConfig", [
        (TEXT2, 10, "llm.provider = name"),
        (TEXT2, 10, "llm.api_key / model"),
        (TEXT2, 10, "configFromEnv() at startup"),
        (TEXT4, 9, "assertValidConfig() gates"),
    ], header_h=32, line_h=22))
    s.append(arrow(410, 205, 448, 205, SPACE, "arwS", 2.5, opacity=0.8))

    # Factory
    s.append(panel(450, 130, 300, 150, SPACE, "createProvider(config)", [
        (TEXT2, 10, "factory.ts — switch on"),
        (TEXT2, 10, "config.llm.provider name"),
        (TEXT2, 10, "returns LLMProvider"),
        (TEXT4, 9, "createTemplateProvider()"),
    ], header_h=32, line_h=22))
    s.append(arrow(750, 205, 800, 205, SPACE, "arwS", 2.5, opacity=0.8))

    # 7 providers grid
    providers = [
        (810, 130, "openai-provider", "GPT-4o / 4o-mini"),
        (1030, 130, "anthropic-provider", "Claude"),
        (1250, 130, "gemini-provider", "Google Gemini"),
        (810, 250, "mistral-provider", "Mistral AI"),
        (1030, 250, "ollama-provider", "Local models"),
        (1250, 250, "null-provider", "No-op (tests)"),
        (1030, 370, "template-provider", "Static templates"),
    ]
    for x, y, name, desc in providers:
        s.append(panel(x, y, 200, 90, SPACE, name, [
            (TEXT2, 9.5, desc),
        ], header_h=28, line_h=18, title_size=10))

    # Interface
    s.append(panel(810, 500, 640, 120, MYKB, "LLMProvider interface", [
        (TEXT2, 10, "complete(params: CompletionParams) → Promise<CompletionResult>"),
        (TEXT2, 10, "CompletionParams: prompt, model?, temperature?, maxTokens?"),
        (TEXT2, 10, "CompletionResult: text, usage?, meta?"),
        (TEXT4, 9, "Every provider implements the same contract — swappable via config"),
    ], header_h=32, line_h=22))

    # Consumers
    s.append(label(110, 500, "⬇ CONSUMERS", 11, DASH))
    consumers = [
        (110, 530, "question-refiner", "rewrites/refines questions"),
        (110, 650, "spec-generator", "builds final specification"),
        (110, 770, "artifact-synthesizer", "summarizes artifacts"),
    ]
    for x, y, name, desc in consumers:
        s.append(panel(x, y, 300, 90, DASH, name, [
            (TEXT2, 9.5, desc),
        ], header_h=28, line_h=18, title_size=10.5))
    s.append(panel(450, 530, 300, 330, EXT, "quality-scorer", [
        (TEXT2, 10, "grades response quality"),
        (TEXT2, 10, "feeds adaptive-router"),
        (TEXT2, 10, "skip questions when"),
        (TEXT2, 10, "  quality is sufficient"),
        (TEXT2, 10, "→ shouldSkipQuestion()"),
        (TEXT4, 9, "i18n: en, es, fr"),
    ], header_h=32, line_h=22))

    s.append(arrow(810, 560, 780, 560, MYKB, "arwM", 2.5, opacity=0.7))
    s.append(arrow(810, 560, 770, 560, GRAY, "arwG", 2, opacity=0.3))

    # Output
    s.append(panel(810, 680, 640, 100, DASH, "CompletionResult flows to", [
        (TEXT2, 10, "SessionState answers (setAnswer) → artifact tracker"),
        (TEXT2, 10, "Intelligence layer (metrics, completeness, contradictions)"),
        (TEXT4, 9, "Final spec generated by spec-generator → exportSession()"),
    ], header_h=32, line_h=22))

    s.append(svg_end(w))
    return "\n".join(s)

# ── 4. Full API Map ───────────────────────────────────────────────────
def api_map():
    w, h = 1600, 1000
    s = [svg_start(w, h, "FULL API MAP",
        "Every HTTP endpoint in the ecosystem — who serves it, what it does")]

    # Dashboard
    s.append(panel(110, 120, 420, 190, DASH, "COSMOS DASHBOARD — port 9000 (start.sh)", [
        (TEXT2, 9.5, "GET /                     — SPA dashboard"),
        (TEXT2, 9.5, "GET /components/…         — static files"),
        (TEXT2, 9.5, "GET /dashboard.html       — alt dashboard"),
        (TEXT2, 9.5, "GET /start.sh             — launcher"),
        (TEXT4, 9, "python3 -m http.server 9000 — serves everything"),
    ], header_h=32, line_h=21))

    # RSIS3
    s.append(panel(560, 120, 420, 190, RSIS, "RSIS3 — dashboard (rsis/dashboard/app.py)", [
        (TEXT2, 9.5, "GET /                  — HTML dashboard"),
        (TEXT2, 9.5, "GET /api/status        — system status"),
        (TEXT2, 9.5, "GET /api/trends        — trend data"),
        (TEXT2, 9.5, "GET /api/velocity      — improvement velocity"),
        (TEXT2, 9.5, "GET /health            — health check"),
    ], header_h=32, line_h=21))

    # SPACE
    s.append(panel(1010, 120, 480, 190, SPACE, "SPACE — ports 8888 / 8899", [
        (TEXT2, 9.5, "GET :8888/              — React web UI (serve-ui.mjs)"),
        (TEXT2, 9.5, "GET :8899/              — meta viewer (serve-meta.mjs)"),
        (TEXT2, 9.5, "GET /docs-viewer.html   — documentation browser"),
        (TEXT2, 9.5, "CLI: space run / export — non-HTTP paths"),
        (TEXT4, 9, "requires npm run build in ui/ for web UI"),
    ], header_h=32, line_h=21))

    # MyKB (larger)
    s.append(panel(110, 360, 720, 310, MYKB, "MYKB — port 8765 (server.py)", [
        (TEXT2, 9.5, "GET /                              — wiki pages as HTML"),
        (TEXT2, 9.5, "GET /files.json                     — recursive .md inventory"),
        (TEXT2, 9.5, "GET /graph.json                     — knowledge graph adjacency"),
        (TEXT2, 9.5, "GET /api/file?path=                 — raw markdown content"),
        (TEXT2, 9.5, "GET /api/stats                      — system statistics"),
        (TEXT2, 9.5, "GET /api/v2/search/hybrid?q=        — dense + sparse RRF search"),
        (TEXT2, 9.5, "GET /api/v2/graph/topology          — KG topology export"),
        (TEXT2, 9.5, "GET /api/v2/health/lint             — wiki lint health"),
        (TEXT2, 9.5, "GET /api/v2/history/log/<path>      — file revision log"),
        (TEXT2, 9.5, "GET /api/v2/history/snapshot?path=&ts= — time-travel"),
        (TEXT2, 9.5, "POST /api/v2/search/build           — rebuild search index"),
    ], header_h=32, line_h=22))

    # Heartbeat
    s.append(panel(860, 360, 630, 310, EXT, "SENTRY HEARTBEAT — watches.json", [
        (TEXT2, 9.5, '{ "name": "COSMOS Dashboard", "port": 9000, "path": "/" }'),
        (TEXT2, 9.5, '{ "name": "SPACE Meta Viewer", "port": 8899, "path": "/" }'),
        (TEXT2, 9.5, '{ "name": "SPACE Web UI",      "port": 8888, "path": "/" }'),
        (TEXT4, 9, "Each watch: startCmd, startArgs, cwd for auto-restart"),
        (TEXT4, 9, "sentry.log — centralized, component-prefixed"),
        (TEXT4, 9, "Monitoring is external to components — zero coupling"),
    ], header_h=32, line_h=24))

    # Summary
    s.append(panel(110, 720, 1380, 110, RSIS, "INTEGRATION NOTES", [
        (TEXT2, 10.5, "MyKB is the only component with a dedicated always-on HTTP server — others are static or on-demand."),
        (TEXT2, 10.5, "RSIS3 dashboard API is FastAPI-style (app.py) — status/trends/velocity drive the telemetry UI."),
        (TEXT4, 9.5, "Port conflicts: MyKB server.py shares 8765 with RSIS3 rack server — known technical debt; run one at a time."),
    ], header_h=34, line_h=26))

    s.append(panel(110, 850, 1380, 60, EXT, "", [
        (TEXT2, 10, "Orchestration entry: cosmos CLI → start.sh → ports + heartbeat → dashboard aggregates"),
    ], header_h=28, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)

EXPERT = {
    "expert-01-evaluator-pipeline.svg": evaluator_pipeline,
    "expert-02-telemetry-pipeline.svg": telemetry_pipeline,
    "expert-03-llm-providers.svg": llm_providers,
    "expert-04-api-map.svg": api_map,
}
