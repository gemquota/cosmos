# 14 — Static Code Analysis

**Doc ID:** COSMOS-AUDIT-14 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [07 Function-by-Function](07_FUNCTION_BY_FUNCTION_AUDIT.md) · [28 Technical Debt](28_TECHNICAL_DEBT_REGISTER.md) · [27 Scorecard](27_CODE_QUALITY_SCORECARD.md)

---

## 1. Cyclomatic Complexity (McCabe proxy) — top 25 modules

| CYC | LOC | Module |
|-----|-----|--------|
| 118 | 551 | `components/mykb/.wiki-daemon/enrich_links.py` |
| 98 | 706 | `components/rsis3/rack/rrp_engine.py` |
| 95 | 496 | `components/rsis3/rack/rrp_conversation.py` |
| 87 | 576 | `components/mykb/.wiki-daemon/search_fusion.py` |
| 86 | 386 | `components/mykb/server.py` |
| 75 | 694 | `components/mykb/.wiki-daemon/build_stats.py` |
| 74 | 745 | `components/rsis3/rsis/main.py` |
| 66 | 567 | `components/rsis3/rsis/priority_pool.py` |
| 53 | 245 | `components/rsis3/rsis/extrapolation.py` |
| 52 | 390 | `components/rsis3/rsis/telemetry.py` |
| 51 | 203 | `components/mykb/.wiki-daemon/kb_linter.py` |
| 46 | 407 | `components/rsis3/rsis/loop_l2.py` |
| 44 | 388 | `components/rsis3/rsis/config.py` |
| 43 | 253 | `components/rsis3/rsis/loop_l1.py` |
| 43 | 319 | `components/rsis3/rsis/pipeline.py` |
| 42 | 232 | `components/mykb/build-export.py` |
| 40 | 346 | `components/rsis3/rsis/memory.py` |
| 40 | 351 | `components/rsis3/rsis/tools/sandbox.py` |
| 38 | 234 | `components/rsis3/rsis/practices.py` |
| 37 | 202 | `components/rsis3/rsis/tools/manager.py` |
| 35 | 242 | `components/rsis3/rsis/loop_l8.py` |
| 34 | 198 | `components/mykb/.wiki-daemon/temporal_engine.py` |
| 33 | 323 | `components/rsis3/rack/run_rrp_pulse.py` |
| 32 | 124 | `components/mykb/.wiki-daemon/build_graph.py` |
| 31 | 233 | `components/rsis3/rsis/loop_l9.py` |

**Interpretation:** <10 simple; 10–20 moderate (review); >20 complex (refactor). Core loops (loop_l2), rrp_engine, search_fusion, priority_pool sit in the 20–40 band. [I, Med]

## 2. Code Smells & Anti-Patterns (evidence-based)

- **Broad exception swallowing** — `try/except: pass` in `mykb/server.py get_system_stats` and `build_stats.py` hide real errors (tag parsing, file reads). [O, High]
- **Import-time side effect** — `CONFIG = load_config()` at import in `config.py`. [O, Med]
- **Magic numbers** — `300`-byte title read (`server.py`), `30s` heartbeat default, 8-hex uuid prefix (`core.ts`), `0.5/0.85` target bands. [O, Med]
- **Dead references** — `rsisb` (`cli/cosmos`), `serve-dashboard.mjs` (`watches.json`), `dashboard/` npm target, `myrsikb/rsiskb` (`COSMOS-SPEC.md`). [O, High]
- **Template duplication** — `loop_l6..l9.py` near-identical structure (copy-paste variation). [I, Med]
- **Long functions** — `cmd_*` methods mix orchestration + policy; >100 LOC. [O, Med]
- **Stringly-typed config kind** — registry `kind` is "int"/"float" strings. [O, Low]
- **Implicit coupling** — telemetry cost ledger shares a module with telemetry; extrapolation reads telemetry dir by convention. [I, Med]
## 3. Dead Code & Unused

- `pytest_cache/` dir present in tree. [O]
- `.cosmos-pids/*.js` and `.rsirrp/work/*` are scratch/archived, on no active path. [O]
- `debug-session.ts`, `docs-server.py`, `_update_viewer.py` — helpers not wired to build/scripts. [O, Med]
## 4. Technical Debt Concentration

- **High:** MyKB daemons (untested, broad excepts); glue layer (dead refs); dashboard regeneration drift.
- **Medium:** RSIS3 loop template duplication; telemetry sprawl; diagrams-gen untested.
- **Low:** SPACE core (well-structured; minor magic numbers).
## 5. Suggested Rewrites (high ROI)

1. Replace bare `pass` with `logger.exception` + metric increment.
2. Extract a `TFSearch` class with precomputed idf/norms + inverted index; drop inline doc reads.
3. Refactor `loop_l6..l9` into one parameterized meta-loop class.
4. Make `CONFIG` a lazy accessor to remove import-time I/O.
5. Centralize loop-state apply/disjointness (partially in practices.py).

---
*End of document 14. Next: [15 Performance Audit](15_PERFORMANCE_AUDIT.md).*