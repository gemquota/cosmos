# 10 — Data Flow Analysis

**Doc ID:** COSMOS-AUDIT-10 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [12 Data Model](12_DATA_MODEL_ANALYSIS.md) · [13 Algorithm](13_ALGORITHM_ANALYSIS.md) · [18 Security](18_SECURITY_AUDIT.md)

---

## 1. Primary Data Paths

### 1.1 Agent Pulse (RSIS3)
```
goal + workspace state
  → L1 action loop (tools → sandbox → evaluator)
  → outcome (pass/fail/held) + cd categories
  → ledger.record → telemetry (rack/pulses/*.json)
  → dashboard-data.json (gen-static-data.py) → dashboard
  → completed pulses → L2 improvement → L3 consolidation → memory
```

### 1.2 MyKB Index/Search
```
wiki/*.md (frontmatter + body)
  → build_graph.py → graph.json (nodes/edges)
  → enrich_links.py → auto [[wikilinks]]
  → search_fusion.py build-index → search_index.json + search_vectors.npy/search_sem.npy
  → server.py search_query / /api/v2/search/*  (serve-time)
  → hooks (post-tool-use / session-stop) → log.md + syntheses
```

### 1.3 SPACE Session
```
createSpace(config) → framework (JSON) → sessions(Map)
  → startSession → question-router → submitAnswer → validator → artifact-tracker
  → storage (FileSystem/SQLite) + snapshots (snapshot-manager)
  → export (json/md/yaml/html/prompt/diff) → files
```

### 1.4 RRP Pulse
```
rrp_engine.run_pulse → rrp_conversation (326-probe) → pulse-NNN.json
  → rack/pulses → dashboard-data.json
```

## 2. Data Ownership Matrix (observed)

| Data | Producer | Consumer | Storage | Version? |
|---|---|---|---|---|
| pulse JSON | rrp_engine / L1 | dashboard, gen-static | rack/pulses | no |
| tunables state | L4..L9 | config._apply_tuned_state | .rsis/*.json | no |
| telemetry ledger | L1..L3 | dashboard, extrapolation | telemetry dir | no |
| audit/HITL events | tool layer | ops review | .rsis/*.jsonl | no |
| wiki notes | hooks/agents | search, graph, dashboard | mykb/wiki/*.md | git |
| search vectors | search_fusion | server, hybrid search | .wiki-daemon/*.npy | generated |
| SPACE sessions | engine | exports, web UI | ~/.space/** or sql.js | framework_version only |

## 3. Transformation Pipeline Characteristics

- **Pure transforms:** artifact extraction (answer text → dictionary), exporters (session → 6 formats),
  TF-IDF scoring — all side-effect-free given inputs. [O]
- **Impure/stateful:** ledger writes, checkpoint git commits, subprocess executions, search index writes.
- **Lossy points:** dashboard-data.json aggregates drop per-step detail; title extraction reads only the
  first 300 bytes of each doc [O].

## 4. Memory Ownership & Lifetime

- **Process-local:** sessions live in a `Map` in SPACE process; cleared on restart (only persisted via
  storage). RSIS3 telemetry/ledger swap on `stop()`.
- **File lifetime:** generated artifacts persist; `gen-static-data.py` regenerates on demand; no TTL.
- **Leak risk (inferred):** in SPACE, uploaded/serially-added artifacts kept in `artifactTracker` for
  process lifetime. In RSIS3, `MemoryManager` accumulates outcome records unboundedly (no eviction). [I, Med]

## 5. Validation & Integrity Points

- SPACE validates framework (`validateFramework`) and answers (`validateAnswer`) before mutation. [O]
- RSIS3 clamps tuned params to registry bounds. [O]
- MyKB `kb_linter.py` + `link_check.py` can validate wiki integrity, but are not wired into the serving
  path. [O]
- **Gap:** no cross-file validation that dashboard-data.json matches live telemetry (regeneration only on
  manual run). [O, Med]

## 6. Findings

- **D1** — Artifact/Session serialization lacks a schema version (only `framework_version`), risking
  silent forward-breakage of saved sessions. [O, High]
- **D2** — No data pipeline observability: no lineage/audit of which generator wrote which artifact. [I, Med]
- **D3** — Search vectors are binary NumPy; no checksum/version — stale npy can silently mismatch JSON
  index. [I, Low]

---
*End of document 10. Next: [11 Dependency Analysis](11_DEPENDENCY_ANALYSIS.md).*
