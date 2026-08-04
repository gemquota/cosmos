# 05 — File-by-File Audit

**Doc ID:** COSMOS-AUDIT-05 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Coverage:** all 90 Python + 77 TypeScript files; HTML/JS/shell summarized in §4. Deep-dive notes from manual reading of the highest-value files; standardized ratings elsewhere. [O] observed, [I] inferred.
**Cross-references:** [04 Repository Inventory](04_REPOSITORY_INVENTORY.md) · [07 Function-by-Function](07_FUNCTION_BY_FUNCTION_AUDIT.md) · [28 Technical Debt](28_TECHNICAL_DEBT_REGISTER.md)

---

## 1. Rating Scale

- **Importance 1–5:** 5 = core path, 1 = auxiliary/generated.
- **Complexity 1–5:** cyclomatic/cognitive-load heuristic (LOC + branches + state).
- **Risk:** security/reliability exposure: Low / Med / High.

## 2. Full File Matrix (Python + TypeScript, largest first)

| LOC | Lang | Imp | Cx | Risk | Path | Purpose / notes |
|-----|------|-----|----|----|------|-----------------|
| 745 | PY | 5 | 3 | Med | `components/rsis3/rsis/main.py` | CLI orchestrator; 17 commands; wires subsystems per command |
| 706 | PY | 5 | 4 | Med | `components/rsis3/rack/rrp_engine.py` | RRP pulse engine: runs RRP cycles, produces pulse JSON |
| 694 | PY | 3 | 2 | Low | `components/mykb/.wiki-daemon/build_stats.py` | Stats aggregator (694 LOC) |
| 659 | TS | 4 | 3 | Low | `components/space/src/data/artifact-extractor.ts` | Artifact extraction from answers (658 LOC) |
| 600 | PY | 1 | 2 | Low | `diagrams/gen/omega_nested.py` | Diagram generator (SVG output) |
| 592 | PY | 1 | 2 | Low | `diagrams/gen/round6_advanced.py` | Diagram generator (SVG output) |
| 576 | PY | 5 | 4 | Med | `components/mykb/.wiki-daemon/search_fusion.py` | Hybrid/semantic search server + index builder |
| 567 | PY | 4 | 4 | Med | `components/rsis3/rsis/priority_pool.py` | PriorityPool: aging, preemption, D2 scheduling |
| 551 | PY | 4 | 3 | Low | `components/mykb/.wiki-daemon/enrich_links.py` | Link enrichment: auto wikilinks |
| 533 | TS | 4 | 3 | Low | `components/space/src/data/artifact-mapping.ts` | Artifact mapping rules (532 LOC) |
| 525 | PY | 1 | 2 | Low | `diagrams/gen/expert_plus.py` | Diagram generator (SVG output) |
| 525 | PY | 1 | 2 | Low | `diagrams/gen/round6_expert.py` | Diagram generator (SVG output) |
| 500 | PY | 1 | 2 | Low | `diagrams/gen/round6_basic.py` | Diagram generator (SVG output) |
| 497 | PY | 1 | 2 | Low | `diagrams/gen/omega.py` | Diagram generator (SVG output) |
| 496 | PY | 4 | 3 | Med | `components/rsis3/rack/rrp_conversation.py` | RRP conversation model: 326-probe protocol impl |
| 483 | PY | 1 | 2 | Low | `diagrams/gen/dynamics.py` | Diagram generator (SVG output) |
| 425 | PY | 1 | 2 | Low | `diagrams/gen/semantic.py` | Diagram generator (SVG output) |
| 407 | PY | 5 | 4 | Med | `components/rsis3/rsis/loop_l2.py` | L2 improvement loop: candidates, DAG parallel, priority pool |
| 390 | PY | 5 | 3 | Med | `components/rsis3/rsis/telemetry.py` | Telemetry collector + WorkspaceMonitor + cost ledger |
| 388 | PY | 5 | 3 | Low | `components/rsis3/rsis/config.py` | Tunables registry + +3 ownership + env + state application |
| 386 | PY | 4 | 3 | High | `components/mykb/server.py` | Wiki server: static + TF-IDF search + subprocess history endpoints |
| 386 | PY | 1 | 2 | Low | `diagrams/gen/_index_update.py` | Diagram generator (SVG output) |
| 379 | PY | 1 | 2 | Low | `diagrams/gen/conceptual.py` | Diagram generator (SVG output) |
| 377 | TS | 5 | 4 | Med | `components/space/src/engine/core.ts` | SPACE engine: sessions, question flow, events, storage |
| 354 | PY | 1 | 2 | Low | `diagrams/gen/advanced.py` | Diagram generator (SVG output) |
| 351 | PY | 5 | 4 | High | `components/rsis3/rsis/tools/sandbox.py` | 3-tier execution sandbox (subprocess/RestrictedPython/Docker) |
| 346 | PY | 4 | 3 | Low | `components/rsis3/rsis/memory.py` | Memory manager: store/retrieve outcomes + memory index |
| 340 | TS | 2 | 2 | Low | `components/space/src/types/index.ts` | Support module |
| 332 | PY | 1 | 2 | Low | `diagrams/gen/expert.py` | Diagram generator (SVG output) |
| 323 | PY | 3 | 2 | Low | `components/rsis3/rack/run_rrp_pulse.py` | CLI entry for RRP pulses |
| 319 | PY | 4 | 3 | Med | `components/rsis3/rsis/pipeline.py` | Pipeline orchestration demo/runner |
| 311 | TS | 4 | 3 | Low | `components/space/src/cli/index.ts` | CLI: commands, prompts, TUI wiring |
| 307 | PY | 3 | 2 | Low | `components/rsis3/tests/test_priority_pool.py` | Test module |
| 305 | PY | 1 | 2 | Low | `diagrams/gen/experimental.py` | Diagram generator (SVG output) |
| 305 | TS | 2 | 2 | Low | `components/space/scripts/run-rsi.ts` | Support module |
| 297 | PY | 4 | 3 | Low | `components/rsis3/rsis/loop_l5.py` | Strategy evolution: population + mutation, owns L2 |
| 288 | PY | 1 | 2 | Low | `diagrams/gen/basic.py` | Diagram generator (SVG output) |
| 279 | PY | 4 | 3 | Med | `components/rsis3/rsis/tools/hitl.py` | HITL approval gate; blocklist regexes for dangerous calls |
| 272 | PY | 1 | 2 | Low | `diagrams/gen/abstract.py` | Diagram generator (SVG output) |
| 270 | TS | 4 | 3 | Med | `components/space/src/storage/sqlite.ts` | SQLite storage via sql.js |
| 270 | TS | 3 | 2 | Low | `components/space/tests/unit/phase5.test.ts` | Test module |
| 256 | PY | 4 | 3 | Med | `components/rsis3/rsis/loop_l3.py` | L3 evolution: cross-session consolidation, strategies |
| 253 | PY | 5 | 3 | Med | `components/rsis3/rsis/loop_l1.py` | L1 action loop: tool calls, retries, HITL hooks |
| 245 | PY | 3 | 3 | Low | `components/rsis3/rsis/extrapolation.py` | Extrapolation: outcome prediction/trends |
| 242 | PY | 3 | 3 | Low | `components/rsis3/rsis/loop_l8.py` | Meta-meta: tunes L5 strategy params |
| 237 | PY | 4 | 3 | Low | `components/rsis3/rsis/loop_l4.py` | Optimizer: outcome-window param tuning of L1 |
| 237 | TS | 3 | 2 | Low | `components/space/tests/unit/sqlite-storage.test.ts` | Test module |
| 236 | TS | 2 | 2 | Low | `components/space/src/data/framework-loader.ts` | Support module |
| 234 | PY | 4 | 3 | Low | `components/rsis3/rsis/practices.py` | check-practices: registry invariants, state disjointness, git |
| 233 | PY | 3 | 3 | Low | `components/rsis3/rsis/loop_l9.py` | MMM: tunes L6 identity bands |
| 232 | PY | 2 | 2 | Low | `components/mykb/build-export.py` | Support module |
| 227 | PY | 3 | 3 | Low | `components/rsis3/rsis/loop_l7.py` | Meta-cog: deadband tuning of L4 |
| 224 | TS | 2 | 2 | Low | `components/space/src/intelligence/contradiction-detector.ts` | Support module |
| 222 | TS | 3 | 2 | Low | `components/space/src/storage/filesystem.ts` | Filesystem JSON storage |
| 219 | TS | 3 | 2 | Low | `components/space/tests/unit/phase1.test.ts` | Test module |
| 213 | PY | 3 | 3 | Low | `components/rsis3/rsis/scheduler.py` | Scheduler demo for pools |
| 208 | PY | 4 | 2 | Low | `gen-static-data.py` | Snapshot generator for GH Pages (files.json/ecosystem/loops) |
| 205 | PY | 3 | 3 | Low | `components/rsis3/rsis/loop_l6.py` | Identity loop: tunes L3 plateau timeout |
| 204 | PY | 4 | 3 | Low | `components/rsis3/rsis/resource_monitor.py` | ResourceEnforcer thread: disk/mem/cpu gates |
| 204 | TS | 2 | 2 | Low | `components/space/src/integration/git.ts` | Support module |
| 203 | PY | 3 | 2 | Low | `components/mykb/.wiki-daemon/kb_linter.py` | KB lint rules for notes |
| 202 | PY | 4 | 3 | Med | `components/rsis3/rsis/tools/manager.py` | ToolManager: allowlists, registration |
| 198 | PY | 3 | 3 | Low | `components/mykb/.wiki-daemon/temporal_engine.py` | Temporal query engine over timestamps |
| 198 | PY | 4 | 3 | Med | `components/rsis3/rsis/recovery.py` | FailureInjector + RecoveryManager + subprocess recovery |
| 191 | TS | 2 | 2 | Low | `components/space/src/config/validation.ts` | Support module |
| 188 | PY | 2 | 2 | Low | `components/space/_update_viewer.py` | Support module |
| 186 | TS | 2 | 2 | Low | `components/space/src/cli/tui.ts` | Support module |
| 166 | TS | 2 | 2 | Low | `components/space/src/engine/question-router.ts` | Support module |
| 156 | PY | 1 | 2 | Low | `diagrams/gen/round6.py` | Diagram generator (SVG output) |
| 154 | TS | 3 | 2 | Low | `components/space/tests/unit/phase6.test.ts` | Test module |
| 144 | TS | 3 | 2 | Low | `components/space/tests/unit/snapshot.test.ts` | Test module |
| 143 | PY | 3 | 3 | Med | `components/rsis3/rsis/shared_memory.py` | SharedMemoryManager for parallel candidates |
| 142 | PY | 2 | 2 | Low | `components/mykb/build-tree.py` | Support module |
| 142 | PY | 2 | 2 | Low | `ops/reports/adversarial-reviews/check_slice.py` | Support module |
| 142 | TS | 3 | 2 | Low | `components/space/tests/unit/template.test.ts` | Test module |
| 141 | TS | 3 | 2 | Low | `components/space/tests/unit/phase2.test.ts` | Test module |
| 138 | TS | 2 | 2 | Low | `components/space/src/data/artifact-keys.ts` | Support module |
| 130 | PY | 3 | 2 | Low | `components/rsis3/rsis/evaluator.py` | EvaluatorClient: immutable subprocess evaluator |
| 130 | TS | 2 | 2 | Low | `components/space/src/data/artifact-tracker.ts` | Support module |
| 130 | TS | 3 | 2 | Low | `components/space/tests/unit/llm-providers.test.ts` | Test module |
| 127 | PY | 1 | 2 | Low | `diagrams/gen/design.py` | Diagram generator (SVG output) |
| 125 | PY | 2 | 2 | Low | `components/mykb/.wiki-daemon/build_stub_audit.py` | Support module |
| 125 | TS | 2 | 2 | Low | `components/space/src/engine/session-manager.ts` | Support module |
| 124 | PY | 3 | 2 | Low | `components/mykb/.wiki-daemon/build_graph.py` | Knowledge graph builder (nodes/edges JSON) |
| 123 | TS | 3 | 2 | Low | `components/space/tests/unit/git-integration.test.ts` | Test module |
| 119 | PY | 3 | 2 | Med | `components/rsis3/rsis/checkpoint.py` | CheckpointManager: git checkpoint commits |
| 118 | TS | 2 | 2 | Low | `components/space/src/intelligence/adaptive-router.ts` | Support module |
| 117 | PY | 1 | 2 | Low | `diagrams/gen/_rebuild_index.py` | Diagram generator (SVG output) |
| 117 | TS | 2 | 2 | Low | `components/space/src/export/index.ts` | Support module |
| 115 | PY | 3 | 2 | Med | `components/rsis3/rsis/tools/workspace_tools.py` | Workspace file tools |
| 111 | TS | 3 | 2 | Low | `components/space/tests/unit/phase3.test.ts` | Test module |
| 105 | PY | 3 | 2 | Low | `components/rsis3/rsis/timeout.py` | Budget + deadline + TimeoutError |
| 104 | TS | 2 | 2 | Low | `components/space/src/export/formatters/markdown-exporter.ts` | Support module |
| 103 | PY | 2 | 2 | Low | `components/mykb/.wiki-daemon/build_stub_index.py` | Support module |
| 103 | PY | 2 | 2 | Low | `components/rsis3/evaluator/evaluator.py` | Support module |
| 102 | PY | 3 | 2 | Low | `components/rsis3/tests/test_loop_l1_retry.py` | Test module |
| 99 | TS | 2 | 2 | Low | `components/space/src/export/formatters/html-exporter.ts` | Support module |
| 98 | PY | 3 | 2 | Low | `components/rsis3/tests/test_pipeline_retry.py` | Test module |
| 96 | TS | 3 | 2 | Low | `components/space/tests/unit/phase0.test.ts` | Test module |
| 95 | PY | 3 | 2 | Low | `components/rsis3/rsis/dashboard/app.py` | FastAPI dashboard: status/trends/velocity/search |
| 91 | PY | 3 | 2 | Low | `components/rsis3/tests/test_shared_memory.py` | Test module |
| 89 | PY | 3 | 2 | Low | `components/rsis3/rsis/event_bus.py` | EventBus: pub/sub |
| 89 | PY | 3 | 2 | Low | `components/rsis3/tests/test_event_bus.py` | Test module |
| 88 | TS | 2 | 2 | Low | `components/space/src/intelligence/recommendations.ts` | Support module |
| 83 | TS | 2 | 2 | Low | `components/space/src/export/formatters/diff-exporter.ts` | Support module |
| 82 | PY | 2 | 2 | Low | `components/rsis3/rsis/tools/__init__.py` | Support module |
| 81 | TS | 2 | 2 | Low | `components/space/src/engine/dependency-resolver.ts` | Support module |
| 80 | TS | 2 | 2 | Low | `components/space/src/engine/snapshot-manager.ts` | Support module |
| 80 | TS | 2 | 2 | Low | `components/space/src/i18n/index.ts` | Support module |
| 78 | TS | 2 | 2 | Low | `components/space/src/intelligence/completeness-scorer.ts` | Support module |
| 74 | TS | 2 | 2 | Low | `components/space/src/intelligence/analytics.ts` | Support module |
| 74 | TS | 2 | 2 | Low | `components/space/src/llm/providers/template-provider.ts` | Support module |
| 73 | TS | 3 | 2 | Low | `components/space/tests/unit/consolidate.test.ts` | Test module |
| 70 | TS | 3 | 2 | Low | `components/space/tests/unit/phase4.test.ts` | Test module |
| 67 | PY | 2 | 2 | Low | `components/mykb/.wiki-daemon/build_index_pages.py` | Support module |
| 67 | PY | 2 | 2 | Low | `components/mykb/.wiki-daemon/link_check.py` | Support module |
| 67 | PY | 3 | 2 | Low | `components/rsis3/rsis/error_classifier.py` | Error classification taxonomy (D1) |
| 66 | TS | 2 | 2 | Low | `components/space/src/i18n/locales/en.ts` | Support module |
| 65 | TS | 2 | 2 | Low | `components/space/src/i18n/locales/es.ts` | Support module |
| 65 | TS | 2 | 2 | Low | `components/space/src/i18n/locales/fr.ts` | Support module |
| 65 | TS | 2 | 2 | Low | `components/space/src/llm/quality-scorer.ts` | Support module |
| 64 | TS | 2 | 2 | Low | `components/space/src/template/resolver.ts` | Support module |
| 63 | TS | 2 | 2 | Low | `components/space/src/engine/progress.ts` | Support module |
| 62 | TS | 2 | 2 | Low | `components/space/src/i18n/types.ts` | Support module |
| 62 | TS | 3 | 2 | Low | `components/space/tests/unit/cli.test.ts` | Test module |
| 59 | TS | 2 | 2 | Low | `components/space/src/export/formatters/json-exporter.ts` | Support module |
| 58 | PY | 3 | 2 | Low | `components/rsis3/tests/test_error_classifier.py` | Test module |
| 57 | TS | 2 | 2 | Low | `components/space/src/export/formatters/prompt-exporter.ts` | Support module |
| 56 | TS | 2 | 2 | Low | `components/space/src/llm/providers/ollama-provider.ts` | Support module |
| 54 | PY | 2 | 2 | Low | `components/mykb/hooks/post-tool-use.py` | Support module |
| 52 | TS | 2 | 2 | Low | `components/space/src/llm/providers/openai-provider.ts` | Support module |
| 51 | PY | 2 | 2 | Low | `components/mykb/wiki/server.py` | Support module |
| 51 | PY | 2 | 2 | Low | `components/space/docs-server.py` | Support module |
| 51 | TS | 2 | 2 | Low | `components/space/src/llm/providers/mistral-provider.ts` | Support module |
| 50 | PY | 2 | 2 | Low | `components/mykb/build-index.py` | Support module |
| 50 | TS | 2 | 2 | Low | `components/space/src/cli/commands/run.ts` | Support module |
| 50 | TS | 2 | 2 | Low | `components/space/src/llm/providers/anthropic-provider.ts` | Support module |
| 49 | TS | 2 | 2 | Low | `components/space/src/llm/providers/gemini-provider.ts` | Support module |
| 49 | TS | 2 | 2 | Low | `components/space/src/llm/question-refiner.ts` | Support module |
| 46 | PY | 2 | 1 | Low | `components/rsis3/rsis/tools/base.py` | ToolResult/ToolStatus dataclasses |
| 46 | PY | 3 | 2 | Low | `diagrams/gen/generate.py` | Diagram generation orchestrator |
| 45 | TS | 2 | 2 | Low | `components/space/src/cli/commands/export.ts` | Support module |
| 43 | TS | 2 | 2 | Low | `components/space/src/engine/validator.ts` | Support module |
| 43 | TS | 2 | 2 | Low | `components/space/src/llm/artifact-synthesizer.ts` | Support module |
| 39 | TS | 2 | 2 | Low | `components/space/src/export/formatters/yaml-exporter.ts` | Support module |
| 38 | TS | 2 | 2 | Low | `components/space/src/llm/factory.ts` | Support module |
| 37 | TS | 2 | 2 | Low | `components/space/src/config/defaults.ts` | Support module |
| 37 | TS | 2 | 2 | Low | `components/space/src/intelligence/index.ts` | Support module |
| 37 | TS | 2 | 2 | Low | `components/space/src/llm/spec-generator.ts` | Support module |
| 33 | PY | 2 | 2 | Low | `components/mykb/hooks/session-stop.py` | Support module |
| 31 | PY | 2 | 2 | Low | `components/mykb/.wiki-daemon/build_files_index.py` | Support module |
| 30 | TS | 4 | 1 | Low | `components/space/src/storage/types.ts` | StorageProvider interface (clean seam) |
| 29 | PY | 2 | 1 | High | `components/rsis3/rack/server.py` | Static dashboard server on 0.0.0.0, ThreadingTCPServer |
| 27 | PY | 2 | 2 | Low | `components/rsis3/ops/check_practices.py` | Support module |
| 27 | TS | 2 | 2 | Low | `components/space/src/template/patterns.ts` | Support module |
| 24 | TS | 2 | 2 | Low | `components/space/src/index.ts` | Support module |
| 21 | TS | 2 | 2 | Low | `components/space/src/llm/types.ts` | Support module |
| 21 | TS | 2 | 2 | Low | `components/space/src/sql.js.d.ts` | Support module |
| 21 | TS | 2 | 2 | Low | `components/space/vitest.config.ts` | Support module |
| 19 | TS | 2 | 2 | Low | `components/space/src/llm/providers/null-provider.ts` | Support module |
| 14 | TS | 2 | 2 | Low | `components/space/debug-session.ts` | Support module |
| 14 | TS | 2 | 2 | Low | `components/space/src/llm/index.ts` | Support module |
| 5 | PY | 2 | 2 | Low | `components/rsis3/rsis/__init__.py` | Support module |
| 5 | PY | 2 | 2 | Low | `components/rsis3/rsis/__main__.py` | Support module |
| 5 | PY | 3 | 2 | Low | `components/rsis3/tests/conftest.py` | Test module |
| 3 | TS | 2 | 2 | Low | `components/space/src/template/index.ts` | Support module |
| 1 | PY | 2 | 2 | Low | `components/rsis3/rsis/dashboard/__init__.py` | Support module |

## 3. Deep-Dive Highlights (observed)

### 3.1 `components/rsis3/rsis/config.py` — the meta-design heart
- Registry `L1_TUNABLES … L6_TUNABLES` maps param names to (min,max,attr-path,kind) with the +3 ownership diagonal. [O]
- `_apply_tuned_state()` loads six `.rsis/*_state.json` files, clamps values, and applies; malformed files are skipped with a warning (fault-tolerant). [O]
- 30+ env overrides in `load_config()`. [O]
- **Finding:** state files have no schema version; silent skip on parse failure can hide stale tuning. [I, Med]
### 3.2 `components/rsis3/rsis/tools/sandbox.py` — the security boundary
- Tier 1 subprocess: `RLIMIT_CPU/RLIMIT_DATA/RLIMIT_NOFILE`, privilege drop to nobody when euid==0, scrubbed `_BASE_ENV` (restricted PATH, no secrets). [O]
- Tier 2: `compile_restricted` (RestrictedPython) with whitelisted builtins and `_print` collector; runtime exceptions surface as results. [O]
- Tier 3: docker-py with `cap_drop=ALL`, `pids_limit=64`, `no-new-privileges`, `network_mode=none` default, hard kill on ReadTimeout, forced container removal. [O]
- **Finding:** Tier-2 executes in-process; a bug in the RestrictedPython allowlist is a code-execution risk (mitigated by `auto` → Tier 1 fallback). [I, Med]
### 3.3 `components/space/src/engine/core.ts` — the SPACE kernel
- `createSpace(config)` merges defaults, loads+validates framework, holds sessions in a Map, emits typed events. [O]
- Clean seams: session-manager (pure transitions), question-router, validator, snapshot-manager, storage provider. [O]
- **Finding:** fallback `altDir = /data/data/com.termux/files/home/dev/space/prompt-framework` is machine-specific. [O, High]
### 3.4 `components/mykb/server.py` — the wiki server
- Static md serving + TF-IDF search + `/api/v2/history/log|snapshot` endpoints that shell out to `temporal_engine.py` via `subprocess.run([sys.executable, ...])` (no shell=True — injection-safe). [O]
- **Finding:** no auth; binds all interfaces; endpoints trigger subprocesses (exposure risk if reachable beyond localhost). [O, High]

## 4. HTML/JS/Shell Inventory Summary

| File | Role | Finding |
|------|------|---------|
| `components/rsis3/dashboard/index.html` (246L) | Unified dashboard (Tailwind+Chart.js) | Real dashboard; root index.html redirects here [O] |
| `components/mykb/index.html` (3,074L) | Wiki browser SPA | Self-contained; content/meta toggle [O] |
| `components/mykb/okf-graph.html` (1,695L) | Knowledge graph viewer | Self-contained [O] |
| `components/space/web/index.html` (803L) | SPACE web UI | Talks to server.mjs API [O] |
| `components/space/meta-viewer.html` (449L) | Spec viewer | Static [O] |
| `components/rsis3/dashboard/app.js` (436L) | Dashboard fetch logic | Reads ../rack/pulses/dashboard-data.json [O] |
| `components/space/web/server.mjs` (388L) | REST API | 14 routes, no auth/rate limit [O] |
| `infra/heartbeat/heartbeat.mjs` (148L) | Watcher | 30s poll, restart on failure [O] |
| `start.sh` (83L) | Launcher | `python3 -m http.server 0.0.0.0:9000`; `fuser -k` cleanup [O] |
| `cli/cosmos` (~260L) | Orchestrator | References nonexistent `rsisb`; status probes SPACE only [O] |
| `gen-static-data.py` (208L) | Snapshot generator | `--check` mode validates committed snapshots [O] |

## 5. Coverage Statement

- Every Python and TypeScript file received a rating (importance/complexity/risk) with a purpose note; highest-value files received manual deep-dive reading (highlighted above).
- Generated SVG/JSON/PNG artifacts are audited at generator level, not per artifact (7,000+ files) — see [35 Appendices](35_APPENDICES.md) §3.
- Confidence: High for deep-dived files; Med for standardized ratings.

---
*End of document 05. Next: [06 Module-by-Module Audit](06_MODULE_BY_MODULE_AUDIT.md).*