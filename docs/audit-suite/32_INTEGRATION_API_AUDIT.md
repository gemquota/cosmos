# 32 — Integration & API Audit

**Doc ID:** COSMOS-AUDIT-32 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [02 Architecture](02_ARCHITECTURE_ANALYSIS.md) · [03 System Spec](03_SYSTEM_ARCHITECTURE_SPECIFICATION.md) · [33 Engineering Spec](33_ENGINEERING_SPECIFICATION.md)

---

## 1. Component Boundaries (Observed)

| Component | Layer | Interface |
|---|---|---|
| RSIS3 | cognitive engine (Python) | CLI (`python -m rsis …`), JSON snapshots |
| MyKB | memory (Python + markdown) | wiki files, `files.json`/`graph.json`, daemon HTTP |
| SPACE | ideation (TS) | web UI + `meta-viewer.html`, export formats |
| Unified dashboard | shell | embeds MyKB + SPACE + telemetry in one page |

## 2. HTTP / Data Contracts

| Endpoint / artifact | Producer | Consumer |
|---|---|---|
| `files.json` | `build_files_index.py` / `gen-static-data.py` | wiki browser (plain or enriched format) |
| `graph.json` | `build_graph.py` | `okf-graph.html` |
| `ecosystem.json` | `gen-static-data.py` | dashboard Overview |
| `loops.json` | `gen-static-data.py` | dashboard Loops tab |
| `api/stats` | wiki daemon | dashboard MyKB tab |
| `api/v2/search/hybrid` | wiki daemon | search build UI |
| `api/v2/health/lint`, `api/v2/search/build` | wiki daemon | Actions tab |
| `api/v2/graph/topology` | wiki daemon | graph subgraph queries |
| `rack/pulses/*.json` | RSIS loops | dashboard telemetry |

## 3. AO Integration Surface (Phase D roadmap)

- D1: `error_classifier` + retry budgets wired into L1/pipeline/L2. [O]
- D2: `EventBus` + priority pools + `SharedMemoryManager` wired into L2 parallel path. [O]
- D3–D5 (planned): context_manager GC, sqlite-vec in MyKB search, `github_tool`
  (risk=CRITICAL + HITL), intercom endpoint, AO test assertions as pytest. [O]
- Port rule (from `docs/ao-cosmos-comprehensive-review.md`): **selective port only**; never
  merge AO as a component. [O]

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| I-1 | Daemon endpoints are unversioned beyond the `v2` prefix in some paths (inconsistent) | Low |
| I-2 | Data contracts (files.json formats) are documented in code comments only | Med |
| I-3 | Dashboard embeds MyKB/SPACE via iframes/links — no cross-frame messaging contract yet | Low |
| I-4 | No intercom between RSIS3 loops and the wiki daemon (D4 candidate) | Med |
| I-5 | The `enriched` files.json format (with type/title/tags) is only used when present; the
  deployed snapshot ships the plain format, so Type-grouping in the browser degrades to
  path-derived groups | Med |

## 5. Recommendations

1. Publish a contracts doc (`docs/integration-contracts.md`) capturing files.json formats,
   graph.json schema, pulse schema, and daemon endpoints.
2. Ship the enriched files.json format so Type grouping is driven by frontmatter types.
3. Add an intercom endpoint (D4) exposing pulse/telemetry to the wiki daemon.
4. Version daemon endpoints consistently (`api/v2/...` everywhere).
