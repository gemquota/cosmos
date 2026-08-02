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
- **Full-loop run**: single telemetry session ran L1–L9 end-to-end — L2
  applied an improvement, L3 consolidated, L4 tuned `l1.*` both directions,
  L5 evolved 6 generations (oscillating fitness), L6 shrink/grow/shrink, L7
  widened L4 deadband, L8 `shrink_population` (8→6), L9 widened L6 band;
  audit: 60 events, all loops start+complete, zero errors; session
  telemetry + 6 state files committed under `components/rsis3/.rsis` and
  `dashboard/loops.json` regenerated to show the run
- **Acquisition + curation pass**: 15 OKF concept notes added to
  `wiki/concepts/` (telemetry, immutable-evaluator, checkpoint-rollback,
  knowledge-graph-memory, vector-memory, memory-hierarchy,
  meta-parameter-tuning, population-based-evolution, fitness-stagnation,
  tuning-oscillation, tuning-ownership-diagonal, recursion-guard,
  inner-outer-loop-learning, deadband-control, learning-to-learn); 24
  hash-named junk entity pages archived via `git mv` to
  `raw/archive/junk-entities-2026-08/`; 2 broken wikilinks fixed in
  `wiki/agent-systems/agent-loop.md`
- **Structural docs**: `ops/conceptual-guide.md` ("mykb for Humans")
  explains the layer model + how to navigate/contribute; linked from
  `README.md`, `Home.md`, `ops/index.md`; new synthesis note
  `wiki/syntheses/mykb-acquisition-curation-and-practices.md`
- **RSIS3 usage practices defined + enforced**:
  `docs/usage-practices.md` + `rsis/practices.py` (17 checks) wired as
  `python -m rsis check-practices` and `ops/check_practices.py`; full-loop
  workspace verifies 17/17 PASS (ownership diagonal, disjoint keys/state
  files, telemetry coverage, checkpoint hygiene); AGENTS.md points at the
  doc + checker

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


## 2026-08-01
- **Ω diagrams** — zoom direction fix: `zoomAt` in `diagrams/gen/omega.py` corrected from
  `vb.w * f` to `vb.w / f` (f>1 zooms in); `x-plus-plus-omega.html`
  regenerated — scroll-up / pinch-out now zoom in
- **Nested-loop graph added**: `diagrams/gen/omega_nested.py` →
  `diagrams/x-plus-plus-nested.html` — full 52-node / 64-link model with the
  L1–L9 stack as nine concentric rings (r1=48…r9=336) at the semantic
  centroid, min-separated bearings, λ1–λ4 visibility, runtime chain arc
  L1→L2→L3, same pan/zoom/touch UI
- **Index wiring**: X++ tab now hosts both graphs (count 1→2, 88 diagrams);
  `_index_update.py` + `_rebuild_index.py` kept in sync
- **Verified**: 0 label overlaps at λ1–λ4, 64/64 edges, all L-nodes on their
  rings; snapshots `diagrams/gen/nested_snap_1/4.{svg,png}` committed
- **New synthesis note**: `wiki/syntheses/nested-loop-graph-and-zoom-fix.md`

## 2026-08-01
- **Wiki stats hub** — stats hub added: `stats.html` + `.wiki-daemon/build_stats.py` — 7 stat
  tiles and 13 charts (word-count thresholds 300+/400+/500+, length histogram,
  longest notes, status/type/area/tag distributions, monthly + last-60-day
  activity, graph-degree and wikilink distributions, length-vs-links scatter),
  embedded JSON, per-chart data tables, graceful Chart.js-less fallback
- **Dashboard wiring**: MyKB tab in `rsis3/dashboard/index.html` gained a
  `📊 Wiki Stats` tab (csb) + `Stats ↗` link + iframe container
- **Snapshot drift fixed**: `files.json` regenerated 2824 → 2825 (was missing
  `wiki/syntheses/nested-loop-graph-and-zoom-fix.md`); `--check` now passes
- **Graph verified**: `build_graph.py` clean (2286 nodes / 13452 edges, 0
  dangling endpoints); current wiki counts: 2,825 md files, 25 notes at 300+,
  14 at 400+, 11 at 500+ words
- **New synthesis note**: `wiki/syntheses/wiki-stats-hub.md`

## 2026-08-01
- **Pass 2 acquisition** — second acquisition pass — 4 parallel research workers (specs E–H) added **400 articles (100 full + 300 stubs)** across four new clusters:
  - Cloud Infrastructure & DevOps — `wiki/cloud-infra/`, `wiki/infrastructure/`, `wiki/devops-infra/`
  - Software Engineering & Developer Tools — `wiki/software-engineering/`, `wiki/dev-tools/`, `wiki/os-shell/`, `wiki/web-platforms/`
  - Mobile & Client Platforms — `wiki/mobile-platform/`, `wiki/android-core/`, `wiki/frontend-frameworks/`, `wiki/shell-environment/`
  - Identity, Security & Governance — `wiki/identity/`, `wiki/security-auth/`, `wiki/api-services/`
- **Verification**: 168 source URLs verified live (HTTP 200); 14 cross-directory wikilink mismatches fixed; zero broken links across all 400 files; frontmatter + word-count checks green (fulls 150–400w, stubs short)
- **Snapshots regenerated**: `files.json` 2,825 → 3,225; `graph.json` 2,286 nodes / 13,452 edges → 2,687 / 15,820; `okf-graph.html` 3,125 concepts; 15 area index pages refreshed
- **Report**: `ops/reports/curation-2026-08-01.md`
- **Stats hub refresh after Pass 2**: `build_stats.py` re-run over the
  expanded wiki — 2,687 content files, 370,366 words, 14,525 wikilinks;
  thresholds 300+/400+/500+ = 54/14/11 (300+ grew 26 → 54 as expected,
  fulls are capped at 400 words so 400+/500+ unchanged)
- **Snapshot ordering rule captured**: `gen-static-data.py` counts tracked
  files only, so files.json must be regenerated *after* staging an
  acquisition round (synthesis: `wiki/syntheses/acquisition-pass-snapshot-ordering.md`)
- **Deployed**: full-tree mirror to `gh-pages` with Pass-2 content

## 2026-08-02 (Pass 3 — parallel agents)
- **5-agent acquisition pass**: five parallel workers (data-storage,
  api-protocols, testing, frontend, os-shell) each generated **100 unique
  full articles** — 500 total, gated through define → confirm → generate
- **Uniqueness confirmed programmatically**: 500/500 slugs unique (no
  intra/cross-agent dupes), zero collisions with the existing wiki
- **Independent verification**: 500/500 files present, frontmatter valid,
  bodies 150–400 words, 0 broken wikilinks (agents' own checks re-run by
  orchestrator)
- **Wiki size**: 2,688 → 3,188 content files
- **New synthesis note**: `wiki/syntheses/parallel-agent-acquisition.md`
- **Deployed**: full-tree mirror to `gh-pages`

## 2026-08-02 (stats hub v2)
- **Stats hub v2**: `build_stats.py` + `stats.html` extended — article-level
  stats now **exclude `log.md`, `index.md` and all `*/index.md`** (graph
  totals still include them; footer caveat added)
- **Article-level counts after exclusion**: 3,189 → **3,093 files**,
  374,672 words, 16,805 wikilinks; thresholds 300+/400+/500+ =
  **70/8/5** (previously 86/19/16); graph unchanged at 3,189 nodes /
  19,047 edges
- **7 new charts added** (20 canvases total): ECDF (share ≤ N words),
  words by area, word-length buckets by area, status by month, cumulative
  growth, avg words/month, most linked-to; tiles now show
  `excl. log.md / index.md` + content-area counts (8 cards)
- **QA**: headless Chromium — 20 canvases, zero JS errors; fallback
  (tiles/tables) renders without Chart.js
- **Deployed**: full-tree mirror to `gh-pages`

## 2026-08-02 (stats hub v2.1 — overview card)
- **9th overview card added**: `full articles (300+)` with sub-line
  `400+ → 8 · 500+ → 5`, computed dynamically from thresholds data —
  top grid reflows (auto-fit), no layout change needed
- **Regenerated**: `build_stats.py` → `stats.html`; JS syntax check + headless
  render QA green (9 cards, 20 canvases)

## 2026-08-02 (stats hub v2.2 — card tooltips)
- **Overview cards now show info tooltips on tap/click**: each of the 9 cards
  has an explanation; tapping toggles the bubble, tapping a different card
  switches it, tapping elsewhere/scroll/resize closes it
- **QA**: JS syntax check green; headless iframe click test passed —
  9 cards, show/toggle/switch all OK

## 2026-08-02 (expansion pass — 500 articles to 300+)
- **10-agent expansion pass**: 10 parallel workers each expanded ~50 short
  articles (50–99 body words) to 300+ words; five agents were re-spawned
  after upstream provider errors mid-run (work persisted; only untouched
  files were re-assigned)
- **Result**: 300+ tier grew **70 → 570** (+500, exactly on target);
  400+ 8 → 17; 500+ unchanged at 5; total words 374,672 → 513,542
  (+138,870); graph 3,189 nodes / 19,047 → 19,571 edges (+524 new links)
- **Verification**: 500/500 files ≥300 body words (frontmatter-stripped),
  valid frontmatter, `status: growing` on all targets; zero *new* broken
  wikilinks vs HEAD (277 pre-existing template links unchanged)
- **Snapshots regenerated**: `build_stats.py`, `build_graph.py`,
  `gen-static-data.py --check` OK (3,729 entries)

## 2026-08-02 (stub curation pass — 735 pointless stubs archived)
- **Reviewed all 3,093 content files**; archived **735 pointless stubs** to
  `raw/archive/junk-entities-2026-08/` (preserving relative paths):
  723 auto-extracted session-entity stubs (template-only bodies, <100 words,
  no prose) + 12 empty `overview.md` category placeholders
- **Criteria**: template-only body (no content beyond the "appears in N
  session(s)" auto-template) AND zero inbound links from any kept file
  (index pages included); 129 referenced stubs were deliberately kept so no
  links break — verified 0 keeper→removed link violations
- **Removed stubs were all <100 words**: 300+/400+/500+ tiers unchanged
  (570/17/5); words 513,542 → 476,046; wikilinks 17,594 → 13,811;
  graph 3,189 → **2,454 nodes**, 19,571 → **15,422 edges**
- **Snapshots regenerated**: build_stats, build_graph, okf render,
  gen-static-data --check OK (2,994 md files)

## 2026-08-02 (broken-link repair pass — 248 dead wikilinks fixed)
- **Post-archive repair**: the 735-stub archive left **248 broken wikilinks**
  in kept files — dead links to archived junk entities, unsupported
  `wiki/*/…` wildcard targets (~300 instances), and stale raw-archive refs
- **Fix**: removed dead entity bullets from index/related lists; converted
  `[[raw/archive/…|label]]` wikilinks to relative markdown links
  (`[label](../../raw/archive/….md)`); dropped wildcard targets the browser
  cannot resolve
- **Verification**: 0 unresolvable wikilinks in the wiki (was 248 at HEAD);
  relative markdown-link targets checked against disk; 300+/400+/500+ tiers
  unchanged at 570/17/5; words 476,046 → 475,777
- **Snapshots regenerated**: build_stats, build_graph, okf render,
  gen-static-data --check OK (3,729 md files)

## 2026-08-02 (link repair pass — 797 dead markdown links fixed)
- **Repointed 777 session links** to `raw/archive/session-artifacts-2026-07/sessions/`
  (all 236 referenced sessions exist in the archive; deep relative paths resolve
  on disk and strip to browser-resolvable `raw/...` paths via files.json)
- **Repointed 3 overview links** to archived `raw/archive/junk-entities-2026-08/`
  category overviews; converted 14 dead cross-domain category links to
  `[[wiki/…/overview|label]]` wikilinks (entity "**Overview:**" bullets and
  overview "Related Categories" lists)
- **Repointed misc**: `data-storage/index.md` CACHE → `entities/cache.md`;
  `cosmos-dashboard-mykb-integration` Wiki Schema → `../../ops/wiki-schema.md`
- **Verification**: 0 broken wikilinks and 0 broken relative markdown links in
  wiki pages (one intentional `[title](path)` syntax example skipped; root
  `log.md`/`index.md` excluded as before); tiers unchanged 570/17/5;
  wikilinks 13,567 → 13,581
- **Snapshots regenerated**: build_stats, build_graph, okf render,
  gen-static-data --check OK (3,729 md files)
