#!/usr/bin/env python3
"""One-off surgery script: add Round 6 cards + Expert+ / X++ tabs to index.html."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(os.path.dirname(HERE), "index.html")

C = {  # palette keys -> CSS var names
    "rsis": "var(--rsis)", "mykb": "var(--mykb)", "space": "var(--space)",
    "dash": "var(--dash)", "ext": "#f472b6", "cyan": "#67e8f9", "ind": "#a5b4fc",
}

# (num, title, desc, tags, [(color_key, label)], file)
BASIC_CARDS = [
    ("B-13", "The Artifact Lifecycle &mdash; Five States, One Loop",
     "A ring of the five artifact states &mdash; IDEA (SPACE) &rarr; CANDIDATE (RSIS3) &rarr; PULSE (telemetry) &rarr; LESSON &rarr; KG EDGE (MyKB) &mdash; with the evaluator gate diamond between candidate and pulse, the retrieval return arc (:8765), and a white comet that is one artifact circulating the lifecycle: one lap = one idea matured end-to-end.",
     ["Ring lifecycle", "Evaluator gate", "Comet = pipeline", "12:1 · 25:1"],
     [("space", "IDEA"), ("rsis", "CANDIDATE"), ("dash", "PULSE"), ("mykb", "LESSON · KG")],
     "basic-13-artifact-lifecycle.svg"),
    ("B-14", "The Ownership Matrix &mdash; Who Runs What",
     "Six code modules (rsis3 core, rack/pulses, mykb, space, dashboard, evaluator) &times; four runtimes, with OWN / EMBED / READ / WRITE / SERVE / FEED / SPAWN cells. The diagonal is the trunk; the dashboard is the only module embedding all three others; the evaluator is spawned, never imported.",
     ["Module × runtime", "OWN/EMBED/SPAWN", "Port clash :8765", "Dashboard embeds all"],
     [("rsis", "OWN · RSIS3"), ("mykb", "SERVE · MyKB"), ("space", "FEED · SPACE"), ("ext", "SPAWN · evaluator")],
     "basic-14-ownership-matrix.svg"),
    ("B-15", "The Three Jobs &mdash; One Per Loop",
     "L1 the doer (~1s), L2 the improver (~12s RRP rounds), L3 the evolver (~60s) &mdash; one job per loop with real budgets (10 calls/step, 120s, 3 retries; 25 rounds/spec, &le;5 evals) and the nesting rail L3 &sup; L2 &sup; L1.",
     ["L1/L2/L3", "Budgets", "Nested scope", "12:1 · 25:1"],
     [("rsis", "L1 · ~1s"), ("space", "L2 · ~12s"), ("mykb", "L3 · ~60s"), ("ext", "Budgets")],
     "basic-15-three-jobs.svg"),
    ("B-16", "The Data Product Map &mdash; Everything the System Produces",
     "The eight artifacts that flow between components &mdash; probe answers, spec drafts, improvement candidates, eval verdicts, pulses, lessons, KG edges, dashboard-data.json &mdash; each with producer, consumer, and format contract. JSON is the machine spine, Markdown the human spine.",
     ["8 artifacts", "Producer → consumer", "Format contracts", "JSON/MD spine"],
     [("space", "SPACE products"), ("rsis", "RSIS3 products"), ("mykb", "MyKB products"), ("dash", "Dashboard products")],
     "basic-16-data-product-map.svg"),
    ("B-17", "The Six Handoffs &mdash; The System's Real Interfaces",
     "Six directional contracts between the four runtimes: spec drafts, candidate JSON (the spawn), pulses, retrieval :8765, session capture, and dashboard &rarr; SPACE launch &mdash; with payload and cadence on each card. Zero shared objects: files and ports only.",
     ["6 interfaces", "Ports & payloads", "Spawn vs launch", "Zero shared objects"],
     [("space", "SPACE → RSIS3"), ("ext", "RSIS3 → evaluator"), ("mykb", "MyKB ⇄ RSIS3"), ("dash", "Dashboard ⇄")],
     "basic-17-six-handoffs.svg"),
    ("B-18", "The Repo Map &mdash; Where Everything Lives",
     "The monorepo tree: cosmos/ root redirect, the three component trees with their real contents (rack/pulses, immutable evaluator, wiki corpus, daemon, web UI, prompt framework), file and LOC counts, and why the shared git-tracked filesystem matters.",
     ["Filesystem tree", "112 files · 67k LOC", "2,360+ wiki pages", "150 tests"],
     [("rsis", "rsis3/"), ("mykb", "mykb/"), ("space", "space/"), ("dash", "shared FS")],
     "basic-18-repo-map.svg"),
    ("B-19", "The Runtime Map &mdash; What Runs, Where, On Which Port",
     "GitHub Pages (cosmos/ + hub/) in the cloud and the four local servers &mdash; dashboard :9000, MyKB daemon :8765 (the only always-on server), SPACE :8888/:8899, RSIS3 :8080 &mdash; plus the documented port conflict where the rack and the daemon both claim :8765.",
     ["GitHub Pages", ":9000 · :8765 · :8888/8899", "Port conflict", "Only daemon always-on"],
     [("dash", "Cloud · Pages"), ("mykb", ":8765 daemon"), ("space", ":8888/:8899"), ("rsis", ":8080 static")],
     "basic-19-runtime-map.svg"),
    ("B-20", "The Improvement Stack &mdash; One Idea Becomes Memory",
     "Six rungs &mdash; idea &rarr; spec &rarr; candidate &rarr; pulse &rarr; lesson &rarr; memory &mdash; with the evaluator gate between candidate and pulse and the retrieval return arc (:8765) feeding memory back into the next idea. A stack with a return elevator.",
     ["6 rungs", "Maturation", "Evaluator gate", "Return arc :8765"],
     [("space", "Idea · spec"), ("rsis", "Candidate"), ("dash", "Pulse"), ("mykb", "Lesson · memory")],
     "basic-20-improvement-stack.svg"),
    ("B-21", "The Loop Roster &mdash; All Six Rhythms",
     "Every periodic process &mdash; L1 ~1s, RRP ~12s, L3 ~60s, retrieval on-demand, evaluator &le;5/session, telemetry ~1s &mdash; with triggers, plus the two phase-locking ratios 12:1 (pulses per round) and 25:1 (rounds per spec).",
     ["6 rhythms", "12:1 · 25:1", "Phase lock", "Event-driven exceptions"],
     [("rsis", "L1 · 1s"), ("space", "RRP · 12s"), ("mykb", "L3 · 60s"), ("dash", "telemetry")],
     "basic-21-loop-roster.svg"),
    ("B-22", "The Read/Write Ledger &mdash; Who Touches Which Store",
     "Six persistent stores (wiki corpus, TF-IDF index, KG edges, spec store, pulses, dashboard-data.json) &times; four components with R / W / RW / BUILD cells &mdash; the dual of the ownership matrix: B-14 asks who runs the code, this asks who touches the data.",
     ["Store × component", "R/W/RW", "Derived vs owned", "Git-tracked stores"],
     [("rsis", "RSIS3 reads"), ("mykb", "MyKB owns"), ("space", "SPACE writes"), ("dash", "Dashboard reads")],
     "basic-22-read-write-ledger.svg"),
    ("B-23", "The Session Journey &mdash; One Session, Nine Events",
     "The real order of operations from cold start to consolidated memory &mdash; start, L1 runs, retrieval, candidate, eval gate, pulse, capture, consolidate, next &mdash; with the three capture points and the gate as the only step that can send the session backward.",
     ["Event timeline", "Capture points", "Eval gate", "Timing budget"],
     [("rsis", "engine steps"), ("mykb", "memory steps"), ("dash", "pulse"), ("ext", "gate")],
     "basic-23-session-journey.svg"),
    ("B-24", "The Integration Timeline &mdash; λ1 Engine to λ4 Ecosystem",
     "Four integration stages &mdash; engine only, +memory, +ideation, full ecosystem &mdash; each a strict superset of the last and each a bifurcation in the A-13 portrait. &lambda;&#8324; is the system deployed today.",
     ["λ₁ → λ₄", "Strict supersets", "Bifurcations", "Links to A-13"],
     [("rsis", "λ₁ engine"), ("mykb", "λ₂ +memory"), ("space", "λ₃ +ideation"), ("dash", "λ₄ ecosystem")],
     "basic-24-integration-timeline.svg"),
]

ADVANCED_CARDS = [
    ("A-14", "The Probe Cascade &mdash; 326 Questions Become One Spec",
     "The seven series (Conceptual Depth &rarr; Operational/Functional) with their per-session probe ranges (3&ndash;6 up to 4&ndash;20), merging through 25 rounds of probe-answer-reflect into one spec draft in six export formats. The framework is a funnel.",
     ["7 series", "Probe ranges", "25 rounds", "6 exports"],
     [("space", "S1–S7 cascade"), ("dash", "spec product"), ("ext", "25:1 ratio")],
     "advanced-14-probe-cascade.svg"),
    ("A-15", "The Retrieval Path &mdash; From Question to Context",
     "One L1 query through five stages inside MyKB &mdash; query, tokenize, TF-IDF score, rank, return &mdash; over HTTP :8765, with why retrieval is the hot path and the read-only contract that keeps the corpus safe.",
     ["TF-IDF pipeline", ":8765", "Ranked window", "Hot path"],
     [("rsis", "L1 asks"), ("mykb", "daemon scores"), ("dash", "returns ranked")],
     "advanced-15-retrieval-path.svg"),
    ("A-16", "The Evaluator's Day &mdash; One Verdict, End to End",
     "Candidate JSON &rarr; SHA-256 integrity check &rarr; isolated subprocess (60s cap) &rarr; five scoring dimensions &rarr; verdict on stdout &rarr; apply or retry (&le;5/session). The only code path RSIS3 may not rewrite.",
     ["SHA-256", "Subprocess isolation", "5 dimensions", "≤5/session"],
     [("rsis", "L2 owns candidate"), ("ext", "immutable judge"), ("mykb", "scoring model")],
     "advanced-16-evaluator-day.svg"),
    ("A-17", "The Memory Write Path &mdash; How a Session Becomes Knowledge",
     "The three capture hooks (retrieval log, eval verdict, session transcript) feeding the L3 consolidation pipeline &mdash; normalize, write wiki page + KG edge, git snapshot, index rebuild. The only way the corpus grows.",
     ["3 capture hooks", "L3 consolidation", "Git snapshot", "Index rebuild"],
     [("mykb", "capture hooks"), ("rsis", "L3 stages"), ("dash", "index rebuild")],
     "advanced-17-memory-write-path.svg"),
    ("A-18", "The Pulse Anatomy &mdash; One Telemetry Event, Dissected",
     "The six-field JSON payload of a single pulse (timestamp, loop, step, tool, outcome, duration, retries), the append-only JSONL buffer, and the path to dashboard-data.json, Chart.js, and the extrapolator. Pulses are observability, not memory.",
     ["JSON payload", "JSONL buffer", "Append-only", "Extrapolator"],
     [("dash", "pulse path"), ("rsis", "emitters"), ("ext", "forecast")],
     "advanced-18-pulse-anatomy.svg"),
    ("A-19", "The Spec Journey &mdash; Inside One RRP Session",
     "space init &rarr; 25 rounds across 7 series &rarr; 7-provider dispatch &rarr; draft &rarr; six export formats &mdash; with the two consumers (RSIS3 L2 imports, MyKB archives) and why SPACE stays isolated behind exports.",
     ["RRP session", "7 providers", "6 formats", "Two consumers"],
     [("space", "session stages"), ("rsis", "L2 consumes"), ("mykb", "archive")],
     "advanced-19-spec-journey.svg"),
    ("A-20", "The Telemetry Graph &mdash; From Loop to Chart",
     "Four collectors (L1/L2/L3/SPACE) &rarr; one JSONL buffer &rarr; dashboard-data.json &rarr; Chart.js views, plus the extrapolator whose forecasts feed L3 strategy. The graph closes on itself: forecasts change strategies, strategies change pulses.",
     ["4 collectors", "One sink", "Forecast → strategy", "Closed loop"],
     [("rsis", "collectors"), ("dash", "pipeline"), ("ext", "extrapolator")],
     "advanced-20-telemetry-graph.svg"),
    ("A-21", "The Module Topology &mdash; Each Component From the Inside",
     "Three component graphs of real modules and edges &mdash; RSIS3's loops/evaluator/memory/telemetry structure, MyKB's daemon/search/temporal/KG structure, SPACE's RRP/provider/export structure &mdash; flat by design; depth lives in the loops, not the module tree.",
     ["3 module graphs", "27 nodes", "Flat module tree", "Spawn boundary"],
     [("rsis", "RSIS3 graph"), ("mykb", "MyKB graph"), ("space", "SPACE graph"), ("ext", "spawn edge")],
     "advanced-21-module-topology.svg"),
    ("A-22", "The Failure Cascade &mdash; What Degrades, What Survives",
     "Six dependencies with failure modes, degraded modes, and recoveries &mdash; daemon down, evaluator timeout, SPACE UI down, dashboard down, provider outage, wiki corruption &mdash; plus the resilience ladder: degrade gracefully &rarr; retry &rarr; restore from snapshot.",
     ["Failure modes", "Degraded modes", "Recovery ladder", "Nothing fatal"],
     [("ext", "trust boundary"), ("space", "SPACE deps"), ("dash", "dashboard"), ("mykb", "memory deps")],
     "advanced-22-failure-cascade.svg"),
    ("A-23", "The Time Horizon Map &mdash; Two Spectra, All Six Rhythms",
     "Operation cadence (fast &rarr; slow) and memory persistence (ephemeral &rarr; permanent) as two spectra with every artifact positioned &mdash; revealing the anti-diagonal rule: fast things make ephemeral things; retrieval sits at the join.",
     ["2 spectra", "Cadence vs persistence", "Anti-diagonal rule", "Retrieval at the join"],
     [("rsis", "cadence"), ("mykb", "persistence"), ("dash", "ephemeral"), ("space", "middle")],
     "advanced-23-time-horizon-map.svg"),
    ("A-24", "The Semantic Overlap Volume &mdash; Ontology in 4D",
     "Three spheres (SPACE, RSIS3, MyKB) on the theory&harr;execution and short-term&harr;long-term axes &mdash; size = footprint, colour = component, and where they overlap the colours blend into the real interfaces (spec &rarr; candidate, lessons &rarr; memory, retrieval &rarr; ideation). The pulsing &lambda; ring is time, the 4th axis.",
     ["4D spheres", "Blended overlaps", "Footprint ∝ size", "λ morph"],
     [("space", "SPACE · ideation"), ("rsis", "RSIS3 · execution"), ("mykb", "MYKB · memory"), ("ext", "λ · time")],
     "advanced-24-semantic-overlap-volume.svg"),
    ("A-25", "The Interface Contract Table &mdash; The Fine Print",
     "Six interfaces with transport, payload, error mode, and cadence &mdash; the spec-level detail beneath B-17's cards &mdash; including the only bidirectional pair: candidate JSON in and verdict JSON out over one subprocess.",
     ["Transport · payload", "Error modes", "Cadence", "Bidirectional pair"],
     [("space", "SPACE sender"), ("rsis", "RSIS3 sender"), ("mykb", "MyKB sender"), ("ext", "spawn pair")],
     "advanced-25-interface-contracts.svg"),
    ("A-26", "The Component State Machine &mdash; Three Engines, Three Lives",
     "RSIS3's four states (idle &rarr; acting &rarr; improving &rarr; consolidating), MyKB's three (serving &rarr; indexing &rarr; capturing), SPACE's three (composing &rarr; running &rarr; exporting) &mdash; every transition labelled with the real trigger that fires it.",
     ["3 state machines", "Real triggers", "Loop shapes", "Depth in the engine"],
     [("rsis", "RSIS3 machine"), ("mykb", "MyKB machine"), ("space", "SPACE machine")],
     "advanced-26-component-state-machine.svg"),
]

EXPERT_CARDS = [
    ("E-13", "The Information Flow &mdash; Entropy Along the Lifecycle",
     "Entropy (uncertainty before reading) as a curve across the artifact lifecycle &mdash; idea &rarr; spec &rarr; candidate &rarr; gate &rarr; pulse &rarr; lesson &rarr; KG edge &mdash; with the evaluator as the only point that can raise entropy. The 25:1 ratio is entropy in disguise.",
     ["Entropy curve", "25:1 as entropy", "Gate raises entropy", "Information spent"],
     [("space", "high entropy"), ("rsis", "mid entropy"), ("mykb", "low entropy"), ("ext", "the gate")],
     "expert-13-information-flow.svg"),
    ("E-14", "The Invariant Ledger &mdash; What Never Changes",
     "Eight constants &mdash; evaluator immutability, 326 probes / 7 series, 6 formats, 7 providers, the 12:1 and 25:1 ratios, wiki as source of truth, one dashboard, the port map &mdash; each with its enforcement mechanism and its failure clause.",
     ["8 invariants", "Enforcement", "Failure clauses", "Tiebreaker"],
     [("ext", "trust invariant"), ("space", "framework invariants"), ("mykb", "memory invariant"), ("dash", "dashboard invariant")],
     "expert-14-invariant-ledger.svg"),
    ("E-15", "The Fault Tree &mdash; How the System Breaks, Top-Down",
     "The failure cascade as logic: one top event, five branches, OR-gated leaves &mdash; including the one designed-in leaf (the :8765 port clash) that has no external cause. Two levels deep means every failure is one hop from the dashboard.",
     ["Fault tree", "OR gates", "2 levels deep", "Designed-in leaf"],
     [("mykb", "daemon branch"), ("ext", "evaluator branch"), ("space", "provider branch"), ("dash", "port clash")],
     "expert-15-fault-tree.svg"),
    ("E-16", "The Self-Reference Map &mdash; The System Improving Itself",
     "Four levels of recursion &mdash; objects, the engine improving its own code, the meta-loop improving the improver, and the RRP specifying RRP &mdash; with the one forbidden edge: the evaluator may never be rewritten by the system. Recursion is capped exactly at the judge.",
     ["4 recursion levels", "Forbidden edge", "Evaluator boundary", "Well-founded"],
     [("space", "L0 objects"), ("rsis", "L1 engine"), ("mykb", "L2 meta-loop"), ("ext", "L3 + forbidden")],
     "expert-16-self-reference-map.svg"),
    ("E-17", "The Observability Stack &mdash; The System Watching Itself",
     "Emit &rarr; buffer &rarr; snapshot &rarr; render &rarr; read &rarr; decide &rarr; return, with every stage's format named (JSONL &rarr; disk &rarr; JSON &rarr; HTML &rarr; eyes &rarr; spec &rarr; loop) and the closing arc that turns telemetry into the next spec. Two readers: the human and L3.",
     ["7 stages", "Format transitions", "Two readers", "Closed loop"],
     [("rsis", "emit"), ("dash", "buffer·render"), ("ext", "read"), ("space", "decide")],
     "expert-17-observability-stack.svg"),
    ("E-18", "The Thermodynamic Clock &mdash; Cost and Order Around the Loop",
     "The cost/order cycle &mdash; cheap chaos in ideation, the evaluator as energy barrier, work in execution, expensive order in consolidation &mdash; with a comet circling as one artifact's thermodynamic journey. The energy landscape (A-12) as a closed path.",
     ["Entropy ↔ cost", "Barrier", "Comet = gradient", "Closed path"],
     [("space", "ideation · T↑"), ("ext", "barrier · ΔG"), ("rsis", "execution · W"), ("mykb", "memory · T↓")],
     "expert-18-thermodynamic-clock.svg"),
    ("E-19", "The Complexity Budget &mdash; Where the Weight Lives",
     "Three dimensions drawn to scale &mdash; ~239k LOC across the components, 2,881 files (the wiki corpus dominating), and the six cross-component interfaces &mdash; arguing the real tax is coupling, not line count. Six contracts carry the entire ecosystem.",
     ["239k LOC", "2,881 files", "6 interfaces", "To scale"],
     [("rsis", "RSIS3 · 67k"), ("space", "SPACE · 69k"), ("mykb", "corpus · 2,360"), ("dash", "interface bar")],
     "expert-19-complexity-budget.svg"),
    ("E-20", "The Coupling Matrix &mdash; Who Depends on Whom",
     "A directed dependency heatmap over six modules plus fan-in/fan-out bars &mdash; rsis3 core is the hub (highest in and out), the dashboard is a pure consumer, and the evaluator depends on nothing and is depended on by nothing but the spawn.",
     ["Heatmap", "Fan-in/fan-out", "Hub = rsis3", "Isolated evaluator"],
     [("rsis", "fan-out"), ("mykb", "fan-in"), ("ext", "hot cells")],
     "expert-20-coupling-matrix.svg"),
    ("E-21", "The Protocol Stack &mdash; The RRP, Layer by Layer",
     "The seven RRP layers from probe (326 atoms) to consumption (L2 imports the spec), with the ratios between layers (12:1, 25:1, one spec &rarr; six renderings). The stack narrows because each layer is a purposeful compression.",
     ["7 layers", "Layer ratios", "Narrowing stack", "Lossy compression"],
     [("mykb", "L1 probes"), ("space", "L2–L5 session"), ("dash", "L6 exports"), ("rsis", "L7 consumption")],
     "expert-21-protocol-stack.svg"),
    ("E-22", "The Latency Budget &mdash; Where the Time Goes",
     "Every bounded stage with its cap and typical time &mdash; L1 step 120s, telemetry ~1s, RRP round 12s, retrieval ~8&ndash;15s, evaluation 60s, consolidation 60s &mdash; with the three surprises: evaluation owns the critical path, retrieval taxes L1, and consolidation is async.",
     ["Caps vs typical", "Eval owns the path", "Async consolidation", "~4-min bound"],
     [("rsis", "L1 cap 120s"), ("ext", "eval 60s"), ("mykb", "consolidation"), ("dash", "telemetry")],
     "expert-22-latency-budget.svg"),
    ("E-23", "The Evolution Ladder &mdash; Climbing λ With Gates",
     "The &lambda; stages as rungs, each gate a measured proof &mdash; retrieval must round-trip, specs must pass the evaluator, embeds must render. Failing a gate holds the ladder; it does not roll it back.",
     ["λ₁ → λ₄", "Gate proofs", "Measured capabilities", "Holds not rolls back"],
     [("rsis", "λ₁ engine"), ("mykb", "λ₂ memory"), ("space", "λ₃ ideation"), ("dash", "λ₄ ecosystem")],
     "expert-23-evolution-ladder.svg"),
    ("E-24", "The Conservation Laws &mdash; What the System Cannot Lose",
     "Six conserved quantities &mdash; artifact lineage, budget conservation, source-of-truth, append-only telemetry, evaluator constancy, temporal continuity &mdash; each with a testable violation clause. If all six hold, every diagram in this viewer still describes the system.",
     ["6 laws", "Violation clauses", "Testable", "Deepest invariant"],
     [("space", "lineage"), ("rsis", "budgets"), ("mykb", "truth + time"), ("ext", "evaluator")],
     "expert-24-conservation-laws.svg"),
]

PLUS_CARDS = [
    ("X+-01", "The Causality Graph &mdash; What Causes What, With Lag",
     "Nine events and ten causal edges with their lags, containing the four loops &mdash; improvement, memory, telemetry, outer. Causality, not topology, is the architecture: the graph says what makes what happen.",
     ["9 events", "4 loops", "Edge lags", "Recursive heart"],
     [("space", "spec ⇄ retrieval"), ("rsis", "candidate · strategy"), ("ext", "verdict"), ("dash", "pulse")],
     "expert-plus-01-causality-graph.svg"),
    ("X+-02", "The Entropy Field &mdash; Uncertainty Across the Whole Plane",
     "The E-13 curve promoted to a 2D field over theory&harr;execution &times; short-term&harr;long-term &mdash; a high-entropy ideation zone, a low-entropy memory basin, artifact dots where they live, and a comet rolling down the gradient from probe answer to KG edge.",
     ["2D field", "Contours", "Comet = maturation", "Zones = basins"],
     [("space", "high entropy"), ("rsis", "mid entropy"), ("mykb", "low entropy"), ("ext", "comet")],
     "expert-plus-02-entropy-field.svg"),
    ("X+-03", "The Resilience Spectrum &mdash; What Survives, What Degrades",
     "Six dependencies ranked brittle &rarr; resilient &mdash; the port clash and evaluator at the brittle end, the SPACE UI at the resilient end &mdash; with the degrade &rarr; retry &rarr; restore ladder and the one dependency (the wiki) that cannot degrade because everything depends on it.",
     ["Brittle → resilient", "Recovery ladder", "Wiki cannot degrade", "Trust-boundary cost"],
     [("ext", "brittle end"), ("space", "mid"), ("mykb", "restore path"), ("dash", "resilient end")],
     "expert-plus-03-resilience-spectrum.svg"),
    ("X+-04", "The Time-Scale Separation &mdash; Four Clocks, One Log Axis",
     "L1 (~1s), RRP (~12s), L3 (~60s), and cross-session (~1hr) drawn as wave trains on one shared axis &mdash; the order-of-magnitude separation is the adiabatic assumption that makes the recursion composable: fast loops see slow ones as frozen.",
     ["4 clocks", "Log axis", "Adiabatic", "Separation not synchrony"],
     [("rsis", "L1 · 1s"), ("space", "RRP · 12s"), ("mykb", "L3 · 60s"), ("dash", "session · 1hr")],
     "expert-plus-04-time-scale-separation.svg"),
    ("X+-05", "The Semantic Hyperplane &mdash; Ontology as Terrain, Projected",
     "The two semantic axes in isometric projection with elevation = footprint density &mdash; the three components as massifs whose overlapping skirts show shared semantic ground. The venn diagram with altitude.",
     ["Isometric", "Elevation = density", "3 massifs", "Terrain"],
     [("space", "theory massif"), ("rsis", "execution massif"), ("mykb", "memory massif")],
     "expert-plus-05-semantic-hyperplane.svg"),
    ("X+-06", "The Feedback Topology &mdash; Four Loops, Two Signs, One System",
     "The improvement loop (negative &mdash; the evaluator brake), the memory loop (positive &mdash; compounding), the telemetry loop (neutral), and the outer loop (positive &mdash; the flywheel). Latency is the gain: slow loops damp themselves by being slow.",
     ["Loop signs", "− brake + engine", "Latency = gain", "Emergent stability"],
     [("ext", "− improvement"), ("mykb", "+ memory"), ("dash", "0 telemetry"), ("rsis", "+ outer")],
     "expert-plus-06-feedback-topology.svg"),
    ("X+-07", "The Dependency Lattice &mdash; The Partial Order of Artifacts",
     "A Hasse diagram of production rules &mdash; space init and probes at the bottom, retrieval at the top &mdash; forbidding skipped ancestors: no candidate without a spec, no KG edge without a lesson. The conservation laws are its enforcement.",
     ["Hasse diagram", "Partial order", "Forbidden skips", "7 ranks"],
     [("space", "probe · spec"), ("rsis", "candidate"), ("ext", "verdict"), ("mykb", "KG · retrieval")],
     "expert-plus-07-dependency-lattice.svg"),
    ("X+-08", "The Resource Flow &mdash; Tokens, Time, Disk, CPU",
     "Four currencies with their sources and sinks &mdash; tokens via 7 providers, time through loop budgets, disk into the wiki/JSONL/index, CPU in the isolated evaluator spawn &mdash; with budget caps as the exchange rates and pulses as nearly free.",
     ["4 currencies", "Sources → sinks", "Budget = exchange rate", "Economy"],
     [("space", "tokens"), ("rsis", "time"), ("mykb", "disk"), ("ext", "cpu")],
     "expert-plus-08-resource-flow.svg"),
    ("X+-09", "The Meta-Stability Map &mdash; Every Loop's Stability Regime",
     "A period &times; damping phase plane with three regimes &mdash; damped fast loops, the RRP's limit cycle, quasi-static L3 &mdash; and the evaluator as a burst, not a clock: the brake from the feedback topology, drawn in phase space.",
     ["Phase plane", "3 regimes", "Limit cycle", "Burst node"],
     [("dash", "damped zone"), ("space", "limit cycle"), ("mykb", "quasi-static"), ("ext", "burst")],
     "expert-plus-09-meta-stability-map.svg"),
    ("X+-10", "The Origin Phylogeny &mdash; Where Everything Came From",
     "Artifact ancestry, not git history: the RRP origin branching into the spec engine, the improvement loop, and the wiki corpus &mdash; all three lines converging in the dashboard, the ecosystem's single integration node.",
     ["Ancestry tree", "RRP origin", "3 lineages", "Merge at dashboard"],
     [("space", "spec lineage"), ("rsis", "engine lineage"), ("mykb", "memory lineage"), ("dash", "merge")],
     "expert-plus-10-origin-phylogeny.svg"),
    ("X+-11", "The Constraint Hypergraph &mdash; Constraints as Bubbles Over Artifacts",
     "Six multi-way constraints &mdash; eval budget, format contract, append-only telemetry, git temporal, single dashboard &mdash; drawn as bubbles enclosing the artifact sets they bind. Constraints are shapes, not lines: rules bind sets, not pairs.",
     ["Hyperedges", "Multi-way rules", "Wiki bubble largest", "Invariants' geometry"],
     [("ext", "eval budget"), ("space", "format contract"), ("mykb", "temporal"), ("dash", "append-only")],
     "expert-plus-11-constraint-hypergraph.svg"),
    ("X+-12", "The Ω Overview &mdash; The Whole System on One Plane",
     "The capstone: four runtimes, nine artifact families, and the six handoffs on the two semantic axes &mdash; every other diagram in this viewer is a zoom into this plane. The static sibling of the interactive X++ graph.",
     ["Capstone", "4 + 9 + 6", "Static sibling", "One view"],
     [("space", "SPACE basin"), ("rsis", "RSIS3 basin"), ("mykb", "MYKB basin"), ("dash", "DASH basin")],
     "expert-plus-12-omega-overview.svg"),
]

OMEGA_CARD = ("Ω", "The Interactive Omega Graph",
    "The whole ecosystem as one interactive graph &mdash; 27 module/artifact nodes on two semantic spectra (X = theory&harr;execution, Y = short-term&harr;long-term), node size = footprint, node colour = component, edges = the six handoffs plus internal paths. Hover or tap a node to highlight its neighbourhood and pin a detail readout; drag the &lambda; slider &mdash; the 4th axis &mdash; to morph the system from &lambda;&#8321; (engine only) to &lambda;&#8324; (deployed ecosystem): memory grows, the dashboard fades in.",
    ["Interactive", "27 nodes", "λ slider = 4th axis", "Touch-first"],
    [("space", "SPACE · ideation"), ("rsis", "RSIS3 · execution"), ("mykb", "MYKB · memory"), ("dash", "DASH · telemetry")],
    "x-plus-plus-omega.html")


def card(num, title, desc, tags, legend, file):
    is_html = file.endswith(".html")
    frame = (f'<div class="diagram-frame"><iframe src="{file}" title="{title}" loading="lazy" '
             f'style="width:100%;height:min(92vh,1200px);border:0;border-radius:6px;background:var(--surface2)"></iframe></div>'
             if is_html else
             f'<div class="diagram-frame"><img src="{file}" alt="{title}" loading="lazy"></div>')
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    leg_html = "".join(f'<span><i style="background:{C[k]}"></i> {v}</span>' for k, v in legend)
    btn = f'<a class="download-btn" href="{file}" download>{"⬇ HTML" if is_html else "⬇ SVG"}</a>'
    return f"""    <article class="diagram-card">
      {frame}
      <div class="diagram-meta">
        <div class="card-head"><h3>{title}</h3><span class="card-num">{num}</span></div>
        <p class="card-desc">{desc}</p>
        <div class="tags">
          {tags_html}
        </div>
        <div class="card-foot">
          <div class="mini-legend">
            {leg_html}
          </div>
          {btn}
        </div>
      </div>
    </article>"""


def section(name, heading, sub, cards, extra=""):
    inner = "".join(card(*c) for c in cards)
    return f"""
  <!-- ═══ {name} ═══ -->
  <section class="tab-panel" data-panel="{name.lower()}" id="{name.lower()}" role="tabpanel" hidden>
    <div class="panel-head">
      <h2>{heading}</h2>
      <p>{sub}</p>
    </div>
{extra}
{inner}
  </section>"""


def main():
    src = open(HTML).read()

    # 1 · header
    src = src.replace(
        "RSIS3 core engine &middot; MyKB memory &middot; SPACE ideation — 37 new diagrams in three tiers",
        "RSIS3 core engine &middot; MyKB memory &middot; SPACE ideation — 87 diagrams in five tiers + an interactive &Omega; graph")
    src = src.replace(
        '<span class="badge">Basic &middot; Advanced &middot; Expert &middot; Mobile-first SVG</span>',
        '<span class="badge">Basic &middot; Advanced &middot; Expert &middot; Expert+ &middot; X++ &middot; Mobile-first SVG</span>')

    # 2 · tab buttons
    old_nav = '''<button class="tab-btn" data-tab="expert" role="tab" aria-selected="false">Expert <span class="count">12</span></button>'''
    new_nav = old_nav + '''
  <button class="tab-btn" data-tab="expert-plus" role="tab" aria-selected="false">Expert+ <span class="count">12</span></button>
  <button class="tab-btn" data-tab="x-plus-plus" role="tab" aria-selected="false">X++ <span class="count">1</span></button>'''
    assert old_nav in src
    src = src.replace(old_nav, new_nav)
    # update counts on existing buttons
    src = src.replace('>Basic <span class="count">12</span>', '>Basic <span class="count">24</span>')
    src = src.replace('>Advanced <span class="count">13</span>', '>Advanced <span class="count">26</span>')
    src = src.replace('>Expert <span class="count">12</span>', '>Expert <span class="count">24</span>')

    # 3 · new panels before the content wrapper closes
    xplus_extra = '''
    <div class="diagram-frame" style="margin:0 0 22px;padding:6px;">
      <iframe src="x-plus-plus-omega.html" title="Interactive omega graph" loading="lazy"
        style="width:100%;height:min(94vh,1250px);border:0;border-radius:6px;background:var(--surface2);display:block"></iframe>
    </div>
    <p style="color:var(--text3);font-size:11px;margin:-8px 4px 18px;line-height:1.7">
      The single interactive &Omega; graph — one self-contained HTML file, no build step. Hover/tap nodes to pin their readout,
      drag the &lambda; slider to travel &lambda;&#8321; &rarr; &lambda;&#8324;. The same picture is also available as a static SVG in
      Expert+ (X+-12) and as the downloadable HTML below.
    </p>'''
    plus_section = section("EXPERT-PLUS", "Expert+ — cross-cutting systems views",
                           "Diagrams that read across all four runtimes at once: causality, entropy fields, resilience, time-scale separation, feedback topology, dependency lattices, resource flows, stability, phylogeny, and constraint hypergraphs.",
                           PLUS_CARDS)
    xplus_section = section("X++", "X++ — the interactive omega graph",
                            "One graph of the whole ecosystem, interactive: 27 real module/artifact nodes on two semantic spectra, size = footprint, colour = component, edges = the six handoffs — with a &lambda; slider as the 4th axis.",
                            [OMEGA_CARD], extra=xplus_extra)

    marker = "  </section>\n\n</div>"
    assert marker in src
    src = src.replace(marker, "  </section>\n" + plus_section + "\n" + xplus_section + "\n</div>", 1)

    # 4 · JS tab names
    old_js = "var NAMES = ['basic', 'advanced', 'expert'];"
    assert old_js in src
    src = src.replace(old_js, "var NAMES = ['basic', 'advanced', 'expert', 'expert-plus', 'x-plus-plus'];")
    old_cmt = "// Deep-link: #basic / #advanced / #expert"
    src = src.replace(old_cmt, "// Deep-link: #basic / #advanced / #expert / #expert-plus / #x-plus-plus")

    open(HTML, "w").write(src)
    n = len(BASIC_CARDS) + len(ADVANCED_CARDS) + len(EXPERT_CARDS) + len(PLUS_CARDS) + 1
    print(f"index.html updated — {n} new cards, 5 tabs")


if __name__ == "__main__":
    main()
