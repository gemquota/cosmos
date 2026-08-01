---
type: "log"
title: "Bundle Log"
---

# Bundle Log

## 2026-07-19
- Gemini session import: 162 sessions from 24 projects, 21,087 cross-links

## 2026-07-20
- **Graph tab**: Fixed re-render bug (removed `data-loaded` guard), added layout caching via `sessionStorage`, added re-render button, improved canvas dimension detection
- **Wikilink navigation**: Added global click interceptor for `.md` links to use SPA-style `navigateTo()` instead of page reloads
- **Wikilink path normalization**: `navigateTo()` now handles `.md` extension consistently
- **Graph Topology API**: Added `GET /api/v2/graph/topology` with optional `?root=&depth=` subgraph filtering
- **Search build API**: Added `GET /api/v2/search/build` to rebuild index on-demand
- **Cross-encoder reranker** (`reranker.py`): Lightweight reranking module with CPU-friendly cross-encoder model support, LRU query cache, TF-IDF fallback when model unavailable, API server mode on port 8860
- **Entity enrichment** (`enrich_entities.py`): 42 entity files enriched with context-aware descriptions using known acronyms (500+) and topic patterns
- **Search index rebuilt**: 2,310 files → 11,491 structure-aware chunks via hybrid search pipeline
- **Linter**: 2,313 files scanned, 13 broken wikilinks detected, 2,213 orphans (expected for auto-generated entity stubs)
- **start.sh**: Added PID management, stale PID cleanup, browser auto-open

## 2026-07-21
- **Deep entity enrichment**: 12 auto-enriched from glossary (Database, Logging, CDN, DNS, IDE, GraphQL, JSON, REST, WebSocket, etc.)
- **User-confirmed enrichments**: 6 entities enriched (Gesture Harmonics, Harmonic Series, GoalQueue, IntentRouter, MemoryManager, PrestigeSystem, Overseer) with user-verified definitions
- **7 Composition pages** created in `wiki/compositions/`: Setup & Installation, Development Workflow, API & Integration, Data & Storage, Security & Authentication, DevOps & Deployment, Programming Languages
- **Dashboard**: Added "Compositions" sidebar tab showing clickable composition list, wired with `navigateTo()` for SPA navigation
- **Semantic analysis report**: `ops/reports/semantic_composition.md` — 15 tag-based groups, 7 instruction sets, targeted questionnaire
- **Entity stats**: 1,701 total, 73+17=90 with real content (5.3%), 1,611 template-only with descriptions
- **Bulk glossary enrichment**: 305 entities auto-enriched from 168-term comprehensive glossary (languages, frameworks, databases, cloud, security, Android, protocols, patterns, AI/agent)
- **Total entities with real content**: ~395 (23%) — up from 90 (5%)
- **Remaining**: 1,300 entities still template-only, categorized into acronyms (207), agent components (63), project names (588), code identifiers (430), concepts (12)
- **Questionnaire**: `ops/reports/entity_questionnaire.md` — organized by category for user review
- **Bulk glossary enrichment**: 305 entities auto-enriched from 168-term comprehensive glossary (languages, frameworks, databases, cloud, security, Android, protocols, patterns, AI/agent)
- **Total entities with real content**: ~395 (23%) — up from 90 (5%)
- **Remaining**: 1,300 entities still template-only, categorized into acronyms (207), agent components (63), project names (588), code identifiers (430), concepts (12)
- **Questionnaire**: `ops/reports/entity_questionnaire.md` — organized by category for user review

- **Agent components & acronyms**: 55 more entities enriched — 64 ACE agent components (Overseer, GoalQueue, MemoryManager, etc.) and common acronyms (AES, AGI, ADSR, ACID, APK, BFS, BOM, BTC, etc.)
- **Total enriched**: ~450 entities (26%) with real content

## 2026-08-01
- **L8/L9 loops implemented**: `loop_l8.py` (Meta-Meta, `python -m rsis
  metameta` — raises `l5.mutation_rate` on strategy stagnation, shrinks
  `l5.population_size` on fitness volatility) and `loop_l9.py` (MMM,
  `python -m rsis mmm` — widens the L6 identity band on oscillation, narrows
  it on stall); L5 now records generation-fitness history; `load_config()`
  injects `.rsis/metameta_state.json` + `.rsis/mmm_state.json` at startup
- **All nine loops implemented**: RSIS_SPEC §1.1/§1.2/§1.4 + README + AGENTS
  updated; `__version__` bumped to 0.4.0
- **Dashboard Loops tab**: `gen-static-data.py` emits
  `dashboard/loops.json` (state + telemetry, never-run defaults); new 🧬
  Loops tab renders the L1–L9 stack with targets, tuned params, signals and
  run counts
- **New synthesis note**: `wiki/syntheses/nine-loop-stack-implementation.md`
- **Verified**: L8 raise_mutation + shrink_population, L9 widen + narrow +
  gap-collapse no-op, fresh-process injection, jsdom Loops tab + MyKB/SPACE
  integration checks

## 2026-07-31
- **L3 consolidation (RSIRRP xxl + 4xl)**: new synthesis note
  `wiki/syntheses/cosmos-dashboard-mykb-integration.md` capturing durable
  patterns — bounded client-side search, repo-relative snapshots + read-only
  `--check`, level-local hide rules, `../` link resolution, iframe lazy-loading,
  verification-first external gates
- **Knowledge graph regenerated** via `.wiki-daemon/build_graph.py` (static +
  daemon copies)
- **L4/L5 loops implemented**: `loop_l4.py` (meta-parameter Optimizer,
  `python -m rsis optimize`) and `loop_l5.py` (strategy Evolution,
  `python -m rsis strategies`) added to RSIS3; spec §1.1 documents the full
  nine-loop hierarchy (L1–L5 implemented, L6–L9 hypothetical); concept note
  `wiki/concepts/nine-loop-hierarchy.md` added
- **Topology + startup wiring**: L4/L5 ownership partition (L4 → L1 params,
  L5 → L2 params) and `load_config()` startup injection documented in
  `RSIS_SPEC.md` §1.4; concept note `wiki/concepts/nine-loop-hierarchy.md`
  extended with nested/parallel/overlapping analysis
- **+3 diagonal**: tuning ownership generalized — loop k+3 tunes loop k
  (L6→L3, L7→L4, L8→L5, L9→L6); top three loops are untuned fixed points
  (spec §1.1/§1.4, concept note updated)
- **L0 + consumer clarification**: L0 defined as the workspace substrate (not
  a loop); L1/L2 documented as pure consumers of tuned params with no tuning
  targets (spec §1.1, concept note updated)
- **L6/L7 loops implemented**: `loop_l6.py` (Identity, `python -m rsis
  identity` — tunes `l3.plateau_timeout_s`) and `loop_l7.py` (Meta-Cog,
  `python -m rsis metacog` — widens/narrows L4 deadband from L4 history);
  spec §1.1/§1.4 now marks L8–L9 as the only hypothetical loops
