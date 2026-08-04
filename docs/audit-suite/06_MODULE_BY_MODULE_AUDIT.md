# 06 — Module-by-Module Audit

**Doc ID:** COSMOS-AUDIT-06 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [05 File-by-File Audit](05_FILE_BY_FILE_AUDIT.md) · [11 Dependency Analysis](11_DEPENDENCY_ANALYSIS.md) · [27 Code Quality Scorecard](27_CODE_QUALITY_SCORECARD.md)

---

## 1. Module Map

| Module | Files | LOC (code) | Layer | Owns |
|---|---|---|---|---|
| `components/rsis3/rsis/` | 29 py | ~8,600 | Engine core | loops, subsystems, tools, config |
| `components/rsis3/rack/` | 4 py + dashboard | ~1,600 | RRP pulses + dashboard server | pulse JSON, dashboard |
| `components/rsis3/evaluator/` | 1 py | 103 | Evaluator subprocess | evaluator |
| `components/rsis3/tests/` | 7 py | ~750 | Tests | — |
| `components/mykb/` (visible) | 7 py + 5 html | ~1,030 | Wiki server + build scripts | wiki, files.json, graph.json |
| `components/mykb/.wiki-daemon/` | 10 py | ~2,740 | Index/search/graph/lint daemons | search_*.json/npy, graph.json |
| `components/mykb/.obsidian/` | 2 json | — | Obsidian config | editor settings |
| `components/mykb/wiki/` | 5,397 md | ~68k | Content corpus | knowledge |
| `components/space/src/` | 58 ts | ~7,130 | SPACE engine/CLI/storage/LLM | sessions, exports |
| `components/space/tests/` | 15 ts | ~1,970 | Vitest suites | — |
| `components/space/web/` | 6 mjs + html | ~2,300 | Web UI + REST server | HTTP API |
| `components/space/scripts/` | 4 ts/mjs | ~570 | Run/consolidate tooling | generated specs |
| `diagrams/gen/` | 26 py | 6,909 | SVG generators | diagrams/*.svg |
| root glue | cli/cosmos, start.sh, gen-static-data.py, package.json, index.html, 404.html | ~600 | Orchestration | deployment |
| `infra/heartbeat/` | 2 | 150 | Process supervision | watches.json |
| `ops/reports/` | md + py | ~600 | Adversarial review artifacts | review docs |

## 2. RSIS3 — `rsis/` Package

**Quality: High for concept, Medium for seams.** Modules are cohesive single-responsibility units with
docstrings and consistent naming. Primary coupling issues [I, Med]:

- `loop_l*.py` construct subsystem dependencies inline rather than receiving them (except via CLI), making
  unit isolation harder; tests compensate by testing subsystems directly.
- `telemetry.py` (390 LOC, 26 funcs) mixes collection, workspace monitoring, and the cost ledger — three
  responsibilities in one module.
- `memory.py` (346 LOC, 28 funcs) mixes persistence, TF-IDF-ish scoring, and session capture.

**Module-level risks:** `priority_pool.py` (567 LOC) is the densest logic module; it has 307 LOC of tests —
good sign. `practices.py` shells out to git for invariants — acceptable but slow on big repos [O].

## 3. RSIS3 — `rack/` (RRP Pulse Layer)

`rrp_engine.py` (706 LOC) implements the pulse protocol and writes `rack/pulses/*.json`. `run_rrp_pulse.py`
is the CLI. `server.py` is a 29-line static server with **0.0.0.0 bind and no cache-control on most
assets** [O]. The pulse JSON contract (goal, steps, outcomes, cd categories) is consumed by
`gen-static-data.py` and the dashboard.

## 4. MyKB — Server + `.wiki-daemon/`

- `server.py`: single-file server doing static file serving, TF-IDF search, and history endpoints.
  Subprocess calls use argument lists (no shell interpolation) — safe pattern [O]. TF-IDF scoring is
  naive (`doc_words.count(w)/len` × idf) — O(Q·D) per query; fine at 5.4k docs, will degrade with corpus
  growth [I, Med].
- `.wiki-daemon/search_fusion.py` (576 LOC): hybrid (BM25-ish + semantic) search with `search_sem.npy` /
  `search_vectors.npy` vector files; serves `/api/v2/search/{hybrid,stats,semantic}`; HTTPServer on all
  interfaces [O].
- `.wiki-daemon/build_stats.py` (694 LOC): the largest MyKB module; stats aggregation with
  `try/except: pass` blocks that swallow errors (e.g., tag parsing) [O].
- Hooks (`hooks/post-tool-use.py`, `session-stop.py`) bridge agent sessions → wiki log entries.

**Module-level risk:** zero tests across the whole daemon set [O].

## 5. SPACE — `src/`

Textbook modularity [O]: `engine/` (orchestration), `data/` (framework/artifacts), `intelligence/`
(scoring/contradictions), `llm/` (providers), `storage/` (providers), `export/formatters/` (6 formats),
`config/`, `cli/`, `i18n/`, `template/`, `types/`. Two findings:

- `data/artifact-extractor.ts` (658 LOC) and `artifact-mapping.ts` (532 LOC) are the biggest modules and
  contain dense rule tables — prime candidates for data-driven config instead of code [I, Med].
- `intelligence/adaptive-router.ts` overlaps with `engine/question-router.ts` conceptually — two routing
  mechanisms with unclear precedence [I, Med].

## 6. Diagrams Generators

26 scripts, each producing a family of SVGs; `generate.py` orchestrates. Code quality is consistent with
the rest (docstrings, named functions) but **untested** and **unpinned to an SVG schema** — regenerating
any single generator can rewrite hundreds of files [O]. The `round6_*` and `omega_*` families are the
largest (500–600 LOC each).

## 7. Root Glue & Infra

| Module | Verdict | Evidence |
|---|---|---|
| `cli/cosmos` | **Fix needed** — dead `rsisb`, status bug | `COMPONENT_DIR[rsisb]`; `cmd_status` only pgrep's space |
| `start.sh` | **Fix needed** — binds 0.0.0.0; `fuser -k` is destructive on shared hosts | [O] |
| `gen-static-data.py` | Good — `--check` drift guard exists | [O] |
| `infra/heartbeat` | **Broken watch** — `serve-dashboard.mjs` doesn't exist; cwd hardcoded | [O] |
| root `package.json` | **Broken** — `cd dashboard` target absent | [O] |

## 8. Module Cohesion & Coupling Ratings

| Module | Cohesion | Coupling (internal) | Coupling (external) | Notes |
|---|---|---|---|---|
| rsis core | High | Med | Low (stdlib) | subsystem interfaces missing |
| rack | Med | Med | Med (dashboard-data) | server security |
| mykb server | Med | Med | Low | subprocess to own daemons |
| wiki-daemon | High | Med | Low | untested |
| space src | High | Low | Med (sql.js, providers) | best-in-repo seams |
| diagrams gen | Med | Low | None | untested |
| root glue | Low | High (bash strings) | Med | drift-prone |

---
*End of document 06. Next: [07 Function-by-Function Audit](07_FUNCTION_BY_FUNCTION_AUDIT.md).*
