# 12 — Data Model Analysis

**Doc ID:** COSMOS-AUDIT-12 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [10 Data Flow](10_DATA_FLOW_ANALYSIS.md) · [13 Algorithms](13_ALGORITHM_ANALYSIS.md) · [34 Operations](34_OPERATIONAL_MANUAL.md)

---

## 1. Entity Model (reverse-engineered)

### 1.1 RSIS3
- **Pulse** — one goal-directed session: id, goal, outcomes, steps, cd categories (error_handling,
  type_safety, test_coverage, logging, documentation, security, input_validation, code_quality,
  maintainability, performance) seen in `dashboard-data.json` summary. [O]
- **Outcome** — count / pass / fail / held / encode_attempt, per pulse. [O]
- **TunableParams** — `{name: (min, max, attr, kind)}` registry + live value per loop. [O]
- **StateFile** — `.rsis/{optimizer,strategies,identity,metacog,metameta,mmm}_state.json`. [O]
- **ToolResult** — `{status: OK|TIMEOUT|ERROR, output, metadata: {returncode}}`. [O]
- **LedgerEntry** — cost accounting (cost_log, model, tokens, budget_cap). [O]

### 1.2 MyKB
- **Note** — markdown + YAML frontmatter (type, title, description, tags, timestamp, status). [O]
- **Graph** — `graph.json`: nodes(#entities)+edges(#wikilinks). [O]
- **SearchIndex** — `search_*.json` (idf, paths, docs) + `search_vectors.npy`/`search_sem.npy`. [O]
- **Synthesis** — OKF `synthesis` note under `wiki/syntheses/`. [O]

### 1.3 SPACE
- **FrameworkDefinition** — meta.version, series, questions (choice_id/open_ended). [O]
- **SessionState** — framework_version, answers map question_id→{open_ended, choice_id}, artifacts. [O]
- **QuestionContext** — current question + known data, routed per framework. [O]
- **ArtifactDictionary** — typed artifacts extracted from answers. [O]
- **Snapshot** — serialized session at a point in time. [O]

## 2. Relationship Cardinalities

| Relation | Cardinality |
|---|---|
| Framework → Session | 1:N |
| Session → Answer | 1:N |
| Session → Snapshot | 1:N |
| Pulse → Outcome | 1:N |
| Note → Note (wikilink) | N:M |
| TunableName → Loop owner | 1:1 (registry) |
| Loop(k) → loop(k-1) params owned | 1:1 (+3 diagonal) |

## 3. Serialization

- Python: `json` exclusively for state; `jsonl` for audit/hitl streams; no pickle on disk (only
  in-memory? searched: no pickle.load in repo) [O].
- SPACE: `serializeSession`/`deserializeSession` JSON.stringify; exporter templates. [O]
- MyKB: JSON index, NumPy arrays for vectors. [O]
- **Finding:** no `__version__` field on any state/session JSON — forward-compat unmanaged. [O, High]

## 4. Persistence & Caching

- RSIS3 state persisted to workspace `.rsis/`; telemetry flushed by interval thread. [O]
- MyKB loads search index at server start into memory (`SEARCH_INDEX`) — staleness until restart/index
  rebuild. [O, Med]
- SPACE `sessions` Map is ephemeral; persisted via StorageProvider on save. [O]
- **No cache layer** (Redis/memcache) anywhere; all reads hit filesystem. [O]

## 5. Indexes

| Index | Location | Type |
|---|---|---|
| MyKB TF-IDF | `search_index.json` | sparse term-idf |
| MyKB semantic | `search_vectors.npy`, `search_sem.npy` | dense vectors |
| MyKB file list | `files.json` | path list |
| RRP pulses | `rack/pulses/*.json` + `dashboard-data.json` | array |
| SPACE sessions | filesystem or sql.js table | PK: session_id |

## 6. Validation & Integrity

- Framework validation: `validateFramework` (SPACE) — rejects invalid frameworks at load. [O]
- Answer validation: `validateAnswer`. [O]
- RSIS3 tuned-param clamping to registry bounds. [O]
- **No referential integrity** between pulse JSON and dashboard-data.json aggregates (regenerated
  wholesale). [O, Med]
- **No uniqueness constraint** on session/project ids beyond uuid prefix `proj_`+8 hex. [O, Low]

## 7. Normalization Assessment

- Well-normalized: SPACE types; MyKB notes (typed/tagged); registry (single source of param truth).
- De-normalized by design: dashboard aggregates; search index (rebuilt, not incremental).
- **Normalization debt:** `telemetry.py` mixes raw events + aggregates + cost ledger in one store; a
  better split is raw-event store / derived-aggregates store. [I, Med]

## 8. Findings

- **M1** — Missing schema versions across all state formats (most consequential data-model gap). [O, High]
- **M2** — Binary vector files (`.npy`) have no checksums; rebuild must be deterministic or stale ghosts
  appear. [I, Low]
- **M3** — No data-version migration tooling; renaming a report field (e.g. review passes) requires
  manual backfill. [I, Med]

---
*End of document 12. Next: [13 Algorithm Analysis](13_ALGORITHM_ANALYSIS.md).*
