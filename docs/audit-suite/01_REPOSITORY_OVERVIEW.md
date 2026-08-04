# 01 — Repository Overview

**Doc ID:** COSMOS-AUDIT-01 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [00 Executive Summary](00_EXECUTIVE_SUMMARY.md) · [04 Repository Inventory](04_REPOSITORY_INVENTORY.md) · [35 Appendices](35_APPENDICES.md)

---

## 1. Repository Purpose

COSMOS ("**C**ognitive **O**rchestration **S**ystem for **M**eta-cognitive **O**rchestration &
**S**ynthesis") is a local-first research platform for **recursive self-improvement (RSI)** experiments.
It integrates three component projects under `components/`:

- **RSIS3** (`components/rsis3/`) — the core cognitive engine: a Python implementation of a nested
  self-improvement loop stack (L1–L9) that runs "pulses" (goal-directed agent sessions), records
  telemetry, tunes its own parameters, and improves its own code/strategy.
- **MyKB** (`components/mykb/`) — long-term memory: an Obsidian-conventions knowledge base (Open Knowledge
  Format, OKF) with ~5,400 wiki notes, TF-IDF/hybrid/semantic search, a knowledge graph, temporal engine,
  and session-capture hooks that let RSIS3 sessions persist conclusions.
- **SPACE** (`components/space/`) — ideation/spec engine: a TypeScript CLI + web app that drives a
  326-probe, 7-series question framework ("Recursive Refinement Protocol", RRP) to elicit complete
  development specifications, exported to 6 formats, with 7 pluggable LLM providers.

**Primary domain:** meta-cognition tooling / agent self-improvement research.
**Secondary domains:** prompt engineering, specification elicitation, knowledge management, agent
operating systems, LLM cost governance.

**Intended users:** the repository owner; LLM coding agents that operate the repo via `AGENTS.md`;
anyone experimenting with multi-loop self-improvement systems.

## 2. Software Category

| Aspect | Value |
|---|---|
| Category | Research software / personal platform; partially productized (SPACE is an npm package) |
| Architecture style | Hub-and-spoke; layered core; loop-stack (pipeline-of-loops) in RSIS3 |
| Deployment model | Local servers (Python/Node) + static GitHub Pages |
| Packaging | SPACE: npm package (`@gemquota/space`); RSIS3: Python module (`python -m rsis`); MyKB: static site + local server |

## 3. Technology Stack (Observed)

| Layer | Technology | Evidence |
|---|---|---|
| Language (core) | Python 3 (targets ≥3.10; runs on 3.13) | `components/rsis3/rsis/*.py`, `components/rsis3/requirements.txt` |
| Language (SPACE) | TypeScript 5.9 (strict), Node ≥18, ESM | `components/space/package.json`, `tsconfig.json` |
| Language (glue) | Bash, Node ESM (mjs) | `cli/cosmos`, `start.sh`, `infra/heartbeat/heartbeat.mjs` |
| Web UI | Hand-rolled HTML/JS (Chart.js, Tailwind CDN), no build step for dashboards | `components/rsis3/dashboard/index.html` |
| SPACE UI | React-free vanilla web UI (`web/index.html`) + Node server (`web/server.mjs`) | `components/space/web/` |
| Dashboard backend | FastAPI (optional) | `components/rsis3/rsis/dashboard/app.py` |
| Wiki | Obsidian conventions, YAML frontmatter, `[[wikilinks]]` | `components/mykb/wiki/` |
| LLM providers (SPACE) | OpenAI, Anthropic, Gemini, Mistral, Ollama, Template, Null | `components/space/src/llm/providers/` |
| Storage | Filesystem JSON; SQLite via `sql.js` (SPACE); NumPy vector files (MyKB) | `space/src/storage/`, `mykb/.wiki-daemon/*.npy` |
| Testing | pytest (RSIS3), Vitest (SPACE) | `components/rsis3/tests/`, `components/space/tests/` |
| Diagram generation | Python → SVG (hand-built generators) | `diagrams/gen/*.py` → `diagrams/*.svg` |

**Runtime dependencies (minimal):** Python stdlib dominates RSIS3 (argparse, http.server, subprocess,
threading, json, dataclasses); optional `psutil` (resource monitoring) and `pytest` (dev). SPACE uses
`chalk`, `commander`, `inquirer`, `js-yaml`, `ora`, `sql.js`, `uuid`; dev: `typescript`, `vitest`,
`tsx`, `eslint`, `prettier`. See [24 Dependency Audit](24_DEPENDENCY_AUDIT.md).

## 4. Repository Metrics (Observed, 2026-08-04)

| Metric | Value |
|---|---|
| Git commits | 89 |
| First commit | 2026-07-29 (`96e55912 "Initial commit: COSMOS ecosystem"`) |
| Last commit (HEAD) | `7055c457` (rsis3 L1 retry + D1 tests) |
| Authors | 1 (git shortlog empty under current config; commit messages all single-voice) |
| Total tracked files | 7,517 |
| Code LOC | ≈ 48,400 (py 21,659 · ts 9,024 · html 14,483 · mjs 2,433 · js 484 · sh 317) |
| Content LOC (md) | 85,685 across 7,040 files |
| Data LOC (json/jsonl) | ≈ 178,700 |
| Test files | 22 (7 Python in RSIS3 + 15 TS in SPACE) |
| GitHub Pages | https://gemquota.github.io/cosmos/ (redirects to unified dashboard) |

## 5. Repository Maturity

| Dimension | Assessment | Confidence |
|---|---|---|
| Engineering level | Early-stage research prototype; core engine unusually disciplined | High |
| Project age | ≈ 7 days | High |
| Maintainability | Moderate — small surface, but stale docs and generated-data churn | Med |
| Scalability | Low-to-moderate: designed for single host; in-memory indexes | Med |
| Complexity | High conceptual complexity, low code complexity per file | High |
| Production readiness | Low (40/100) — no CI, no auth, no releases | Med |

## 6. Directory Topology (Observed)

```
cosmos/
├── index.html                  # 24-line redirect → components/rsis3/dashboard/index.html
├── 404.html                    # GH Pages deep-link shim (MyKB paths)
├── start.sh                    # Launcher: python http.server :9000 + MyKB server :8765
├── gen-static-data.py          # Regenerates files.json / ecosystem.json / loops.json
├── package.json                # root: scripts reference nonexistent dashboard/ (BROKEN)
├── cli/cosmos                  # Bash orchestrator (space/mykb/rsis3 + dead rsisb)
├── components/
│   ├── rsis3/                  # Python engine (10.5k py LOC) + dashboard + rack (RRP pulses)
│   ├── mykb/                   # OKF wiki (5.4k md) + server.py + .wiki-daemon (2.7k py LOC)
│   └── space/                  # TS package (7.1k src LOC) + web UI + exports
├── diagrams/                   # 95 generated SVG + 26 generators (6.9k py LOC)
├── docs/                       # ARCHITECTURE-SPEC.md, COSMOS-COMPLETE.md, AO reviews
├── infra/heartbeat/            # heartbeat.mjs + watches.json (hardcoded paths, dead startCmd)
├── ops/reports/                # adversarial reviews, check_slice.py
├── mykb/                       # GH Pages snapshot mirrors (graph.html, stats.html, stub-audit.html)
├── .rsis/                      # runtime state (audit.jsonl, hitl.jsonl, temp files)
├── .rsirrp/                    # RRP work archive (sessions, work/)
├── .cosmos-pids/               # pid files + jsdom test scripts
└── .shots/                     # screenshots (excluded from audit)
```

## 7. Build & Run Surface (Observed)

| Entry point | Command | Status |
|---|---|---|
| RSIS3 engine | `python3 -m rsis <cmd>` (from `components/rsis3`) | Works (49 tests pass) |
| RSIS3 dashboard | `python3 rsis/rack/server.py` or FastAPI `app.py` | Serves static + /api |
| MyKB server | `python3 components/mykb/server.py [port]` | Works (8765 default) |
| MyKB search daemon | `python3 .wiki-daemon/search_fusion.py serve` | Serves /api/v2/search/* |
| SPACE CLI | `npm run dev` / `node dist/cli/index.js` | Requires `npm install` (not installed here) |
| SPACE web | `node web/server.mjs` | Requires node_modules |
| Ecosystem | `./start.sh` or `cosmos dashboard` | Works on this host |
| Root npm | `npm run dev/build/preview` | **Broken** — `cd dashboard` fails |

## 8. Versioning & Releases

- SPACE: `@gemquota/space@2.1.0`, MIT, `npm` publish pipeline declared (`prepublishOnly`) but no evidence
  of a published release in this tree.
- RSIS3: `__version__` in `rsis/__init__.py`; no PyPI packaging metadata (no `pyproject.toml`/`setup.py`).
- MyKB: `VERSION` file present.
- Root: `cosmos@0.2.0`, private.
- **No tags found** in `git log`/`git tag` (checked 2026-08-04) [O].

## 9. Historical Context (Inferred from git log)

The commit history shows a deliberate cadence: Phase A (foundation), Phase B (cost ledger + semantic
search), Phase C (Agent OS tool layer port), Phase D (error classifier + retry resilience), plus
continuous MyKB curation passes (stub expansion, adversarial reviews, reclassification) and RSIS
"checkpoint" commits generated by failed tool runs (`rsis-checkpoint: after-tool-failure-run_code`).
The repo is therefore both a codebase *and* a dataset produced by the tooling itself — generated files
are first-class citizens. This dual nature drives many findings in [25 Documentation Audit](25_DOCUMENTATION_AUDIT.md)
and [28 Technical Debt Register](28_TECHNICAL_DEBT_REGISTER.md).

---
*End of document 01. Next: [02 Architecture Analysis](02_ARCHITECTURE_ANALYSIS.md).*
