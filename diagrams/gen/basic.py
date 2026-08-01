"""Basic tier diagrams — high-level conceptual views."""
from design import *

# ── 1. System Overview ─────────────────────────────────────────────────
def system_overview():
    w, h = 1200, 800
    s = [svg_start(w, h, "COSMOS — SYSTEM OVERVIEW",
        "Cognitive Orchestration System for Meta-cognitive Orchestration & Synthesis")]
    # Ecosystem band
    s.append(f'<rect x="80" y="100" width="1040" height="46" rx="10" fill="{PANEL}" stroke="{BORDER2}"/>')
    s.append(label(600, 120, "🌌 COSMOS — one ecosystem, three components, one goal: recursive self-improvement", 12, TEXT2))
    s.append(label(600, 138, "Hub-and-spoke architecture  •  Shared filesystem  •  GitHub Pages + local servers", 10, TEXT4))

    # Three component cards
    cards = [
        (180, RSIS, "🔄", "RSIS3", "Core Cognitive Engine", "Python", [
            ("Three-loop recursive self-improvement", 10.5),
            ("L1: per-task action loop (seconds)", 10),
            ("L2: per-session improvement (minutes)", 10),
            ("L3: cross-session evolution (hours/days)", 10),
            ("IMMUTABLE AI evaluator gates changes", 10),
            ("112 files • 67k LOC", 10),
        ]),
        (510, MYKB, "🧠", "MyKB", "Long-Term Memory", "Python + Markdown", [
            ("Obsidian wiki — 2,360+ markdown pages", 10.5),
            ("TF-IDF search over 48 knowledge domains", 10),
            ("Temporal engine: time-travel snapshots", 10),
            ("Knowledge graph + session capture hooks", 10),
            ("2,436 files • 58MB", 10),
        ]),
        (840, SPACE, "✧", "SPACE", "RRP Ideation Engine", "TypeScript", [
            ("Structured prompt/spec generation", 10.5),
            ("326-probe framework across 7 series", 10),
            ("7 LLM providers integrated", 10),
            ("6 export formats (JSON/MD/YAML/HTML…)  ", 10),
            ("150 tests • 14 suites", 10),
        ]),
    ]
    for cx, accent, icon, name, role, lang, facts in cards:
        s.append(box(cx, 170, 330, 210, accent, f"{icon} {name}", f"{role} — {lang}"))
        fy = 170 + 40 + 34
        for text, size in facts:
            s.append(label(cx + 165, fy, text, size, TEXT3))
            fy += 22

    # Connections between cards
    s.append(arrow(510, 275, 675, 275, RSIS, "arwR", 2, opacity=0.5))
    s.append(arrow(840, 275, 1005, 275, MYKB, "arwM", 2, opacity=0.5))
    s.append(label(600, 265, "memory I/O", 9, TEXT4, italic=True))
    s.append(label(930, 265, "specs flow", 9, TEXT4, italic=True))

    # How they work together
    s.append(panel(80, 420, 1040, 180, DASH, "HOW THEY WORK TOGETHER", [
        (TEXT2, 11, "1.  SPACE ideates — RRP sessions produce structured specifications (326 probes, 7 series)"),
        (TEXT2, 11, "2.  MyKB stores — specs and session artifacts persist as wiki pages and knowledge graph entries"),
        (TEXT2, 11, "3.  RSIS3 executes — L1 acts, L2 improves (evaluator-gated), L3 evolves strategies across sessions"),
        (TEXT2, 11, "4.  MyKB consolidates — results written back to the knowledge graph for the next cycle"),
        (TEXT4, 10, "The cycle repeats: ideation → storage → execution → consolidation → better ideation"),
    ], header_h=34, line_h=26))

    # Facts strip
    s.append(panel(80, 620, 1040, 120, EXT, "KEY NUMBERS", [
        (TEXT2, 11, "2,881 total files   •   ~239k LOC   •   ~70MB   •   235 directories"),
        (TEXT2, 11, "2 git repos (cosmos + hub)   •   2 GitHub Pages deployments"),
        (TEXT4, 10, "Ports: 9000 Dashboard  •  8765 MyKB  •  8888/8899 SPACE  •  8080 RSIS3 (static by default)"),
    ], header_h=34, line_h=30))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 2. Layer Architecture ─────────────────────────────────────────────
def layer_architecture():
    w, h = 1200, 800
    s = [svg_start(w, h, "LAYERED ARCHITECTURE",
        "Presentation → Service → Data — what runs where and on which ports")]
    layers = [
        (100, 140, 1000, 170, RSIS, "PRESENTATION LAYER", "User-facing interfaces", [
            (TEXT2, 10.5, "COSMOS Dashboard (port 9000) — SPA with 6 component cards, status badges, meta viewer"),
            (TEXT2, 10.5, "RSIS3 Telemetry Dashboard — Chart.js + Tailwind, 20-pulse view"),
            (TEXT2, 10.5, "SPACE Web UI (port 8888) + Meta Viewer (port 8899) — React 18 + Vite"),
            (TEXT2, 10.5, "Hub Dashboard — all non-COSMOS projects (GitHub Pages)"),
        ]),
    ]
    for x, y, pw, ph, accent, title, sub, rows in layers:
        s.append(panel(x, y, pw, ph, accent, title, rows, header_h=36, pad=18, line_h=24))
        s.append(label(x + pw/2, y + 20, sub, 10, TEXT4))
    s.append(arrow(600, 310, 600, 350, GRAY, "arwG", 2, opacity=0.6))

    services = [
        (100, RSIS, "🔄 RSIS3 — Core Engine", "port 8080 (or static)", [
            "L1/L2/L3 recursive loops",
            "EvaluatorClient → immutable evaluator",
            "MemoryManager: KG + vectors",
            "TelemetryCollector + extrapolator",
        ]),
        (450, MYKB, "🧠 MyKB — Memory", "port 8765 (server.py)", [
            "HTTP server + search API",
            "TF-IDF search engine",
            "Temporal engine (git-based)",
            "Knowledge graph + linter",
        ]),
        (800, SPACE, "✧ SPACE — Ideation", "ports 8888 / 8899", [
            "RRP session engine",
            "7 LLM providers",
            "6 export formatters",
            "SQLite + filesystem storage",
        ]),
    ]
    for cx, accent, title, sub, facts in services:
        s.append(box(cx, 355, 300, 170, accent, title, sub, title_size=12.5, header_h=38))
        fy = 355 + 38 + 26
        for f in facts:
            s.append(label(cx + 150, fy, f, 9.5, TEXT3))
            fy += 20
    s.append(arrow(600, 525, 600, 560, GRAY, "arwG", 2, opacity=0.6))

    s.append(panel(100, 565, 1000, 150, DASH, "DATA LAYER — Persistent Storage", [
        (TEXT2, 10.5, "components/rsis3/  →  .rsis/knowledge_graph.json  •  .rsis/vectors/  •  .rsis/telemetry/*.jsonl"),
        (TEXT2, 10.5, "components/mykb/   →  wiki/ (2,360+ pages)  •  .wiki-daemon/ (search_index.json, graph.json)"),
        (TEXT2, 10.5, "components/space/  →  exports/ (specs in 6 formats)  •  prompt-framework/ (326 probes)"),
        (TEXT4, 9.5, "All three components read/write the shared filesystem — git-tracked for temporal recovery"),
    ], header_h=34, line_h=24))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 3. Component Relationships (simple) ───────────────────────────────
def relationships_simple():
    w, h = 1200, 800
    s = [svg_start(w, h, "COMPONENT RELATIONSHIPS",
        "Who talks to whom, and what actually flows between them")]
    # Triangle: RSIS3 top, MyKB bottom-left, SPACE bottom-right
    s.append(box(410, 140, 380, 150, RSIS, "🔄 RSIS3", "Core Cognitive Engine", title_size=16))
    s.append(label(600, 330, "executes & improves", 9.5, TEXT4, italic=True))

    s.append(box(110, 520, 380, 150, MYKB, "🧠 MyKB", "Long-Term Memory", title_size=16))
    s.append(label(300, 700, "stores & retrieves", 9.5, TEXT4, italic=True))

    s.append(box(710, 520, 380, 150, SPACE, "✧ SPACE", "RRP Ideation Engine", title_size=16))
    s.append(label(900, 700, "generates specs", 9.5, TEXT4, italic=True))

    # Arrows
    s.append(arrow(600, 292, 380, 518, MYKB, "arwM", 3, curve=(500, 380, 430, 430)))
    s.append(arrow(300, 518, 500, 292, RSIS, "arwR", 3, curve=(370, 430, 440, 380)))
    s.append(arrow(600, 292, 820, 518, SPACE, "arwS", 3, curve=(700, 380, 770, 430)))
    s.append(arrow(900, 518, 700, 292, RSIS, "arwR", 3, curve=(830, 430, 760, 380)))
    s.append(arrow(492, 560, 708, 560, SPACE, "arwS", 2, opacity=0.7))
    s.append(arrow(708, 600, 492, 600, MYKB, "arwM", 2, opacity=0.7))

    # Labels
    s.append(label(430, 380, "knowledge → RSI", 10, MYKB, font=FONT))
    s.append(label(760, 380, "specs → goals", 10, SPACE))
    s.append(label(600, 540, "specs → wiki pages", 9.5, SPACE))
    s.append(label(600, 620, "wiki context → routing", 9.5, MYKB))

    # Summary
    s.append(panel(110, 730, 980, 60, DASH, "", [
        (TEXT2, 10.5, "Shared filesystem at /dev/cosmos/components/ is the integration backbone — all exchanges are file-based or local HTTP"),
    ], header_h=26, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 4. Self-Improvement Cycle ─────────────────────────────────────────
def improvement_cycle():
    w, h = 1200, 800
    s = [svg_start(w, h, "SELF-IMPROVEMENT CYCLE",
        "How the ecosystem recursively improves itself — one full cycle")]
    cx, cy, R = 600, 440, 260
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R+40}" fill="none" stroke="{BORDER}" stroke-width="1" stroke-dasharray="5,8" opacity=".4"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{BORDER2}" stroke-width="1" opacity=".3"/>')
    # Center
    s.append(f'<circle cx="{cx}" cy="{cy}" r="95" fill="{PANEL}" stroke="{DASH}" stroke-width="2" filter="url(#shadow)"/>')
    s.append(label(cx, cy - 8, "♻", 26))
    s.append(label(cx, cy + 26, "Recursive", 11, TEXT2, font=FONT))
    s.append(label(cx, cy + 42, "Improvement", 11, TEXT2, font=FONT))

    # Four stages
    stages = [
        (cx, cy - R - 60, SPACE, "✧ SPACE — Ideate", ["RRP session", "326 probes → spec"], "top"),
        (cx + R + 60, cy, MYKB, "🧠 MyKB — Store", ["spec + artifacts", "→ wiki pages"], "right"),
        (cx, cy + R + 60, RSIS, "🔄 RSIS3 — Execute", ["L1 act → L2 improve", "→ L3 evolve"], "bottom"),
        (cx - R - 60, cy, DASH, "🗄 Consolidate", ["results → knowledge graph", "→ next cycle context"], "left"),
    ]
    import math
    for x, y, accent, title, lines, pos in stages:
        wbox, hbox = 220, 86
        bx, by = x - wbox/2, y - hbox/2
        s.append(panel(bx, by, wbox, hbox, accent, title, [
            (TEXT2, 9.5, lines[0]), (TEXT3, 9.5, lines[1]),
        ], header_h=28, line_h=16, title_size=11.5))
        

    # Circular arrows — clockwise: top (SPACE) → right (MyKB) → bottom (RSIS3) → left (Consolidate)
    ang = [3*math.pi/2, 0, math.pi/2, math.pi]
    markers = ["arwS", "arwM", "arwR", "arwD"]
    r1, r2 = R + 28, R + 88
    for i in range(4):
        a0 = ang[i] + 0.5
        a1 = ang[(i+1) % 4] - 0.5
        x0, y0 = cx + r1*math.cos(a0), cy + r1*math.sin(a0)
        x1, y1 = cx + r1*math.cos(a1), cy + r1*math.sin(a1)
        # arc path (sweep=1 → clockwise in SVG y-down coords)
        large = 0
        sweep = 1
        s.append(f'<path d="M {x0:.0f} {y0:.0f} A {r1} {r1} 0 {large} {sweep} {x1:.0f} {y1:.0f}" '
                 f'fill="none" stroke="{stages[i][1]}" stroke-width="2.5" opacity=".7" marker-end="url(#{markers[i]})"/>')

    # Time context
    s.append(panel(80, 730, 1040, 50, EXT, "", [
        (TEXT2, 10, "Cycle duration: seconds (L1) → minutes (L2) → hours/days (L3) — each loop feeds the next"),
    ], header_h=26, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)

# ── 5. Deployment ─────────────────────────────────────────────────────
def deployment():
    w, h = 1200, 800
    s = [svg_start(w, h, "DEPLOYMENT MODEL",
        "GitHub Pages (production) + local servers (development) + Sentry Heartbeat (monitoring)")]

    # GitHub cloud
    s.append(f'<rect x="80" y="110" width="500" height="330" rx="12" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1.5" stroke-dasharray="7,4"/>')
    s.append(label(330, 132, "☁️ GitHub Cloud", 13, TEXT2, font=FONT))
    s.append(panel(110, 150, 440, 55, EXT, "GitHub Repository", [
        (TEXT2, 10, "gemquota/cosmos — source of truth"),
    ], header_h=28, line_h=18))
    s.append(panel(110, 225, 440, 55, EXT, "CI/CD (planned)", [
        (TEXT2, 10, "GitHub Actions: lint → test → build → deploy"),
    ], header_h=28, line_h=18))
    s.append(panel(110, 300, 210, 110, DASH, "GitHub Pages", [
        (TEXT2, 9.5, "gemquota.github.io/cosmos/"),
        (TEXT3, 9.5, "gemquota.github.io/hub/"),
    ], header_h=28, line_h=20))
    s.append(panel(340, 300, 210, 110, DASH, "Static Assets", [
        (TEXT2, 9.5, "index.html dashboards"),
        (TEXT3, 9.5, "SPAs, charts, docs"),
    ], header_h=28, line_h=20))
    s.append(arrow(330, 285, 330, 298, EXT, "arwH", 2, opacity=0.6))

    # Local env
    s.append(f'<rect x="620" y="110" width="500" height="330" rx="12" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1.5"/>')
    s.append(label(870, 132, "🖥 Local Development", 13, TEXT2, font=FONT))
    s.append(panel(650, 150, 440, 60, DASH, "COSMOS Dashboard Server", [
        (TEXT2, 10, "port 9000 — static serve + SPA"),
    ], header_h=28, line_h=18))
    s.append(panel(650, 230, 140, 90, MYKB, "MyKB", [
        (TEXT2, 9.5, "port 8765"),
        (TEXT3, 9.5, "server.py"),
    ], header_h=28, line_h=20))
    s.append(panel(810, 230, 140, 90, SPACE, "SPACE", [
        (TEXT2, 9.5, "8888/8899"),
        (TEXT3, 9.5, "web + meta"),
    ], header_h=28, line_h=20))
    s.append(panel(970, 230, 120, 90, RSIS, "RSIS3", [
        (TEXT2, 9.5, "static or 8080"),
        (TEXT3, 9.5, "python -m rsis"),
    ], header_h=28, line_h=20))
    s.append(panel(650, 340, 440, 70, EXT, "Sentry Heartbeat", [
        (TEXT2, 9.5, "watches ports 9000, 8888, 8899 — auto-restart on failure"),
        (TEXT3, 9.5, "logs → sentry.log (component-prefixed)"),
    ], header_h=28, line_h=20))

    s.append(arrow(580, 260, 620, 260, GRAY, "arwG", 2, dashed=True, opacity=0.6))
    s.append(label(600, 252, "deploy / git pull", 8.5, TEXT4, italic=True))

    # CLI
    s.append(panel(80, 470, 1040, 110, DASH, "ORCHESTRATOR CLI", [
        (TEXT2, 10.5, "cosmos start all   →   launches dashboard + all component servers"),
        (TEXT2, 10.5, "cosmos status      →   polls HTTP health of every component"),
        (TEXT2, 10.5, "cosmos logs        →   tails sentry.log with component prefixes"),
        (TEXT2, 10.5, "cosmos build/test  →   builds TypeScript / runs component tests"),
    ], header_h=34, line_h=24))

    # Ports strip
    s.append(panel(80, 600, 1040, 110, RSIS, "PORT MAP", [
        (TEXT2, 10.5, "9000  COSMOS Dashboard (static serve of everything)"),
        (TEXT2, 10.5, "8765  MyKB wiki server (server.py)"),
        (TEXT2, 10.5, "8888  SPACE Web UI  •  8899 SPACE Meta Viewer"),
        (TEXT4, 9.5, "8080  RSIS3 (when running via python3 -m rsis; static otherwise)"),
    ], header_h=34, line_h=24))
    s.append(svg_end(w))
    return "\n".join(s)

BASIC = {
    "basic-01-system-overview.svg": system_overview,
    "basic-02-layer-architecture.svg": layer_architecture,
    "basic-03-component-relationships.svg": relationships_simple,
    "basic-04-self-improvement-cycle.svg": improvement_cycle,
    "basic-05-deployment.svg": deployment,
}
