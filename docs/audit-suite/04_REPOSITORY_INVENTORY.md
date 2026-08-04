# 04 — Repository Inventory

**Doc ID:** COSMOS-AUDIT-04 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [05 File-by-File Audit](05_FILE_BY_FILE_AUDIT.md) · [06 Module-by-Module Audit](06_MODULE_BY_MODULE_AUDIT.md) · [35 Appendices](35_APPENDICES.md)

---

## 1. Totals by Extension

| Ext | Files | Total lines |
|-----|------|-------------|
| md | 7,044 | 542,416 |
| json | 95 | 172,794 |
| npy | 2 | 151,680 |
| log | 2 | 106,034 |
| py | 90 | 21,659 |
| html | 26 | 14,488 |
| svg | 95 | 10,851 |
| png | 4 | 9,187 |
| ts | 77 | 9,024 |
| txt | 17 | 7,483 |
| jsonl | 17 | 6,266 |
| yaml | 4 | 3,787 |
| mjs | 11 | 2,433 |
| markdown | 1 | 1,189 |
| zip | 2 | 488 |
| js | 4 | 484 |
| (none) | 15 | 389 |
| sh | 6 | 317 |
| yml | 3 | 101 |
| css | 1 | 48 |
| tag | 1 | 4 |
| pid | 2 | 2 |
| **Total** | **7,519** | **1,061,124** |

## 2. Code Surface by Area (py+ts+mjs+js+sh+html+css)

| Area | Files | LOC |
|------|-------|-----|

## 3. Python Files (all 90, by LOC)

| LOC | Imports | Functions | Classes | Path |
|-----|---------|-----------|---------|------|
| 745 | 29 | 20 | 0 | `./components/rsis3/rsis/main.py` |
| 706 | 8 | 39 | 8 | `./components/rsis3/rack/rrp_engine.py` |
| 694 | 6 | 11 | 0 | `./components/mykb/.wiki-daemon/build_stats.py` |
| 600 | 4 | 8 | 0 | `./diagrams/gen/omega_nested.py` |
| 592 | 1 | 13 | 0 | `./diagrams/gen/round6_advanced.py` |
| 576 | 12 | 20 | 1 | `./components/mykb/.wiki-daemon/search_fusion.py` |
| 567 | 10 | 28 | 7 | `./components/rsis3/rsis/priority_pool.py` |
| 551 | 4 | 6 | 0 | `./components/mykb/.wiki-daemon/enrich_links.py` |
| 525 | 1 | 13 | 0 | `./diagrams/gen/round6_expert.py` |
| 525 | 2 | 12 | 0 | `./diagrams/gen/expert_plus.py` |
| 500 | 1 | 12 | 0 | `./diagrams/gen/round6_basic.py` |
| 497 | 3 | 2 | 0 | `./diagrams/gen/omega.py` |
| 496 | 6 | 7 | 1 | `./components/rsis3/rack/rrp_conversation.py` |
| 483 | 3 | 15 | 0 | `./diagrams/gen/dynamics.py` |
| 425 | 3 | 14 | 0 | `./diagrams/gen/semantic.py` |
| 407 | 18 | 11 | 3 | `./components/rsis3/rsis/loop_l2.py` |
| 390 | 12 | 26 | 4 | `./components/rsis3/rsis/telemetry.py` |
| 388 | 6 | 4 | 14 | `./components/rsis3/rsis/config.py` |
| 386 | 11 | 5 | 2 | `./components/mykb/server.py` |
| 386 | 1 | 3 | 0 | `./diagrams/gen/_index_update.py` |
| 379 | 1 | 6 | 0 | `./diagrams/gen/conceptual.py` |
| 354 | 1 | 5 | 0 | `./diagrams/gen/advanced.py` |
| 351 | 15 | 13 | 2 | `./components/rsis3/rsis/tools/sandbox.py` |
| 346 | 10 | 28 | 4 | `./components/rsis3/rsis/memory.py` |
| 332 | 1 | 4 | 0 | `./diagrams/gen/expert.py` |
| 323 | 16 | 2 | 0 | `./components/rsis3/rack/run_rrp_pulse.py` |
| 319 | 9 | 13 | 3 | `./components/rsis3/rsis/pipeline.py` |
| 307 | 6 | 30 | 0 | `./components/rsis3/tests/test_priority_pool.py` |
| 305 | 3 | 7 | 0 | `./diagrams/gen/experimental.py` |
| 297 | 13 | 9 | 2 | `./components/rsis3/rsis/loop_l5.py` |
| 288 | 2 | 5 | 0 | `./diagrams/gen/basic.py` |
| 279 | 9 | 12 | 3 | `./components/rsis3/rsis/tools/hitl.py` |
| 272 | 3 | 7 | 0 | `./diagrams/gen/abstract.py` |
| 256 | 12 | 6 | 2 | `./components/rsis3/rsis/loop_l3.py` |
| 253 | 10 | 5 | 3 | `./components/rsis3/rsis/loop_l1.py` |
| 245 | 7 | 9 | 1 | `./components/rsis3/rsis/extrapolation.py` |
| 242 | 11 | 7 | 2 | `./components/rsis3/rsis/loop_l8.py` |
| 237 | 11 | 8 | 2 | `./components/rsis3/rsis/loop_l4.py` |
| 234 | 7 | 10 | 1 | `./components/rsis3/rsis/practices.py` |
| 233 | 12 | 7 | 2 | `./components/rsis3/rsis/loop_l9.py` |
| 232 | 5 | 7 | 0 | `./components/mykb/build-export.py` |
| 227 | 12 | 7 | 2 | `./components/rsis3/rsis/loop_l7.py` |
| 213 | 7 | 7 | 3 | `./components/rsis3/rsis/scheduler.py` |
| 208 | 6 | 6 | 0 | `./gen-static-data.py` |
| 205 | 13 | 6 | 2 | `./components/rsis3/rsis/loop_l6.py` |
| 204 | 10 | 14 | 3 | `./components/rsis3/rsis/resource_monitor.py` |
| 203 | 5 | 4 | 0 | `./components/mykb/.wiki-daemon/kb_linter.py` |
| 202 | 11 | 10 | 2 | `./components/rsis3/rsis/tools/manager.py` |
| 198 | 6 | 8 | 0 | `./components/mykb/.wiki-daemon/temporal_engine.py` |
| 198 | 13 | 13 | 3 | `./components/rsis3/rsis/recovery.py` |
| 188 | 0 | 0 | 0 | `./components/space/_update_viewer.py` |
| 156 | 2 | 12 | 0 | `./diagrams/gen/round6.py` |
| 143 | 6 | 9 | 3 | `./components/rsis3/rsis/shared_memory.py` |
| 142 | 4 | 3 | 0 | `./components/mykb/build-tree.py` |
| 142 | 4 | 5 | 0 | `./ops/reports/adversarial-reviews/check_slice.py` |
| 130 | 11 | 5 | 2 | `./components/rsis3/rsis/evaluator.py` |
| 127 | 0 | 13 | 0 | `./diagrams/gen/design.py` |
| 125 | 5 | 4 | 0 | `./components/mykb/.wiki-daemon/build_stub_audit.py` |
| 124 | 5 | 4 | 0 | `./components/mykb/.wiki-daemon/build_graph.py` |
| 119 | 7 | 10 | 1 | `./components/rsis3/rsis/checkpoint.py` |
| 117 | 4 | 3 | 0 | `./diagrams/gen/_rebuild_index.py` |
| 115 | 3 | 5 | 4 | `./components/rsis3/rsis/tools/workspace_tools.py` |
| 105 | 5 | 9 | 2 | `./components/rsis3/rsis/timeout.py` |
| 103 | 5 | 4 | 0 | `./components/mykb/.wiki-daemon/build_stub_index.py` |
| 103 | 4 | 4 | 0 | `./components/rsis3/evaluator/evaluator.py` |
| 102 | 3 | 13 | 2 | `./components/rsis3/tests/test_loop_l1_retry.py` |
| 98 | 1 | 11 | 0 | `./components/rsis3/tests/test_pipeline_retry.py` |
| 95 | 9 | 7 | 0 | `./components/rsis3/rsis/dashboard/app.py` |
| 91 | 2 | 8 | 0 | `./components/rsis3/tests/test_shared_memory.py` |
| 89 | 5 | 8 | 1 | `./components/rsis3/rsis/event_bus.py` |
| 89 | 3 | 8 | 0 | `./components/rsis3/tests/test_event_bus.py` |
| 82 | 8 | 1 | 0 | `./components/rsis3/rsis/tools/__init__.py` |
| 67 | 3 | 1 | 0 | `./components/mykb/.wiki-daemon/link_check.py` |
| 67 | 4 | 2 | 0 | `./components/mykb/.wiki-daemon/build_index_pages.py` |
| 67 | 3 | 3 | 1 | `./components/rsis3/rsis/error_classifier.py` |
| 58 | 1 | 10 | 3 | `./components/rsis3/tests/test_error_classifier.py` |
| 54 | 4 | 1 | 0 | `./components/mykb/hooks/post-tool-use.py` |
| 51 | 6 | 2 | 1 | `./components/mykb/wiki/server.py` |
| 51 | 6 | 2 | 1 | `./components/space/docs-server.py` |
| 50 | 3 | 0 | 0 | `./components/mykb/build-index.py` |
| 46 | 4 | 2 | 3 | `./components/rsis3/rsis/tools/base.py` |
| 46 | 16 | 1 | 0 | `./diagrams/gen/generate.py` |
| 33 | 4 | 1 | 0 | `./components/mykb/hooks/session-stop.py` |
| 31 | 3 | 0 | 0 | `./components/mykb/.wiki-daemon/build_files_index.py` |
| 29 | 4 | 4 | 1 | `./components/rsis3/rack/server.py` |
| 27 | 4 | 1 | 0 | `./components/rsis3/ops/check_practices.py` |
| 5 | 0 | 0 | 0 | `./components/rsis3/rsis/__init__.py` |
| 5 | 2 | 0 | 0 | `./components/rsis3/rsis/__main__.py` |
| 5 | 2 | 0 | 0 | `./components/rsis3/tests/conftest.py` |
| 1 | 0 | 0 | 0 | `./components/rsis3/rsis/dashboard/__init__.py` |

## 4. TypeScript Files (all 77, by LOC)

| LOC | Funcs/Methods | Classes | Interfaces | Path |
|-----|---------------|---------|------------|------|
| 659 | 41 | 1 | 2 | `components/space/src/data/artifact-extractor.ts` |
| 533 | 4 | 0 | 1 | `components/space/src/data/artifact-mapping.ts` |
| 377 | 17 | 0 | 1 | `components/space/src/engine/core.ts` |
| 340 | 0 | 0 | 30 | `components/space/src/types/index.ts` |
| 311 | 5 | 0 | 0 | `components/space/src/cli/index.ts` |
| 305 | 5 | 1 | 0 | `components/space/scripts/run-rsi.ts` |
| 270 | 23 | 1 | 0 | `components/space/src/storage/sqlite.ts` |
| 270 | 0 | 0 | 0 | `components/space/tests/unit/phase5.test.ts` |
| 237 | 3 | 0 | 0 | `components/space/tests/unit/sqlite-storage.test.ts` |
| 236 | 9 | 0 | 0 | `components/space/src/data/framework-loader.ts` |
| 224 | 2 | 0 | 0 | `components/space/src/intelligence/contradiction-detector.ts` |
| 222 | 28 | 2 | 0 | `components/space/src/storage/filesystem.ts` |
| 219 | 1 | 0 | 0 | `components/space/tests/unit/phase1.test.ts` |
| 204 | 23 | 1 | 3 | `components/space/src/integration/git.ts` |
| 191 | 6 | 0 | 3 | `components/space/src/config/validation.ts` |
| 186 | 7 | 0 | 0 | `components/space/src/cli/tui.ts` |
| 166 | 6 | 0 | 0 | `components/space/src/engine/question-router.ts` |
| 154 | 1 | 0 | 0 | `components/space/tests/unit/phase6.test.ts` |
| 144 | 0 | 0 | 0 | `components/space/tests/unit/snapshot.test.ts` |
| 142 | 0 | 0 | 0 | `components/space/tests/unit/template.test.ts` |
| 141 | 0 | 0 | 0 | `components/space/tests/unit/phase2.test.ts` |
| 138 | 6 | 0 | 0 | `components/space/src/data/artifact-keys.ts` |
| 130 | 9 | 1 | 2 | `components/space/src/data/artifact-tracker.ts` |
| 130 | 0 | 0 | 0 | `components/space/tests/unit/llm-providers.test.ts` |
| 125 | 14 | 0 | 0 | `components/space/src/engine/session-manager.ts` |
| 123 | 0 | 0 | 0 | `components/space/tests/unit/git-integration.test.ts` |
| 118 | 3 | 0 | 1 | `components/space/src/intelligence/adaptive-router.ts` |
| 117 | 7 | 0 | 2 | `components/space/src/export/index.ts` |
| 111 | 2 | 0 | 0 | `components/space/tests/unit/phase3.test.ts` |
| 104 | 3 | 0 | 0 | `components/space/src/export/formatters/markdown-exporter.ts` |
| 99 | 4 | 0 | 0 | `components/space/src/export/formatters/html-exporter.ts` |
| 96 | 0 | 0 | 0 | `components/space/tests/unit/phase0.test.ts` |
| 88 | 3 | 0 | 0 | `components/space/src/intelligence/recommendations.ts` |
| 83 | 4 | 0 | 0 | `components/space/src/export/formatters/diff-exporter.ts` |
| 81 | 4 | 0 | 0 | `components/space/src/engine/dependency-resolver.ts` |
| 80 | 7 | 1 | 0 | `components/space/src/engine/snapshot-manager.ts` |
| 80 | 7 | 0 | 0 | `components/space/src/i18n/index.ts` |
| 78 | 1 | 0 | 0 | `components/space/src/intelligence/completeness-scorer.ts` |
| 74 | 3 | 0 | 1 | `components/space/src/intelligence/analytics.ts` |
| 74 | 9 | 1 | 0 | `components/space/src/llm/providers/template-provider.ts` |
| 73 | 0 | 0 | 0 | `components/space/tests/unit/consolidate.test.ts` |
| 70 | 1 | 0 | 0 | `components/space/tests/unit/phase4.test.ts` |
| 66 | 0 | 0 | 0 | `components/space/src/i18n/locales/en.ts` |
| 65 | 0 | 0 | 0 | `components/space/src/i18n/locales/es.ts` |
| 65 | 0 | 0 | 0 | `components/space/src/i18n/locales/fr.ts` |
| 65 | 5 | 1 | 0 | `components/space/src/llm/quality-scorer.ts` |
| 64 | 7 | 0 | 0 | `components/space/src/template/resolver.ts` |
| 63 | 1 | 0 | 0 | `components/space/src/engine/progress.ts` |
| 62 | 0 | 0 | 2 | `components/space/src/i18n/types.ts` |
| 62 | 0 | 0 | 0 | `components/space/tests/unit/cli.test.ts` |
| 59 | 2 | 0 | 0 | `components/space/src/export/formatters/json-exporter.ts` |
| 57 | 2 | 0 | 0 | `components/space/src/export/formatters/prompt-exporter.ts` |
| 56 | 3 | 1 | 0 | `components/space/src/llm/providers/ollama-provider.ts` |
| 52 | 3 | 1 | 0 | `components/space/src/llm/providers/openai-provider.ts` |
| 51 | 3 | 1 | 0 | `components/space/src/llm/providers/mistral-provider.ts` |
| 50 | 3 | 0 | 0 | `components/space/src/cli/commands/run.ts` |
| 50 | 3 | 1 | 0 | `components/space/src/llm/providers/anthropic-provider.ts` |
| 49 | 3 | 1 | 0 | `components/space/src/llm/providers/gemini-provider.ts` |
| 49 | 3 | 1 | 0 | `components/space/src/llm/question-refiner.ts` |
| 45 | 4 | 0 | 0 | `components/space/src/cli/commands/export.ts` |
| 43 | 3 | 0 | 0 | `components/space/src/engine/validator.ts` |
| 43 | 2 | 1 | 0 | `components/space/src/llm/artifact-synthesizer.ts` |
| 39 | 2 | 0 | 0 | `components/space/src/export/formatters/yaml-exporter.ts` |
| 38 | 3 | 0 | 0 | `components/space/src/llm/factory.ts` |
| 37 | 0 | 0 | 1 | `components/space/src/config/defaults.ts` |
| 37 | 1 | 0 | 1 | `components/space/src/intelligence/index.ts` |
| 37 | 3 | 1 | 0 | `components/space/src/llm/spec-generator.ts` |
| 30 | 16 | 0 | 1 | `components/space/src/storage/types.ts` |
| 27 | 3 | 0 | 0 | `components/space/src/template/patterns.ts` |
| 24 | 0 | 0 | 0 | `components/space/src/index.ts` |
| 21 | 2 | 0 | 3 | `components/space/src/llm/types.ts` |
| 21 | 5 | 0 | 0 | `components/space/src/sql.js.d.ts` |
| 21 | 0 | 0 | 0 | `components/space/vitest.config.ts` |
| 19 | 2 | 1 | 0 | `components/space/src/llm/providers/null-provider.ts` |
| 14 | 2 | 0 | 0 | `components/space/debug-session.ts` |
| 14 | 0 | 0 | 0 | `components/space/src/llm/index.ts` |
| 3 | 0 | 0 | 0 | `components/space/src/template/index.ts` |

## 5. HTML / JS / Shell Files

| LOC | Ext | Path |
|-----|-----|------|

## 6. Wiki Content Distribution (markdown)

| Area | Files | Lines |
|------|-------|-------|
| mykb-nonwiki/mykb-content.md | 1 | 169,948 |
| mykb-nonwiki/raw | 1,420 | 116,915 |
| space-docs | 142 | 21,640 |
| wiki/concepts | 636 | 20,533 |
| wiki/(root) | 4 | 17,322 |
| wiki/data-storage | 470 | 15,956 |
| mykb-nonwiki/mykb-code.md | 1 | 12,908 |
| mykb-nonwiki/ops | 19 | 11,431 |
| wiki/frontend | 277 | 10,979 |
| wiki/security-auth | 266 | 10,882 |
| wiki/api-services | 243 | 10,047 |
| wiki/api-protocols | 280 | 9,264 |
| wiki/devops-infra | 241 | 7,354 |
| wiki/infrastructure | 219 | 6,543 |
| wiki/ai-ml | 191 | 6,145 |
| wiki/agent-systems | 187 | 6,127 |
| wiki/memory | 179 | 5,748 |
| wiki/os-shell | 179 | 5,559 |
| wiki/meta-learning | 166 | 5,462 |
| wiki/web-platforms | 162 | 5,311 |
| wiki/software-engineering | 167 | 5,253 |
| wiki/testing | 149 | 4,852 |
| wiki/shell-environment | 104 | 4,364 |
| wiki/cloud-infra | 140 | 4,287 |
| wiki/dev-tools | 133 | 4,237 |
| wiki/frontend-frameworks | 112 | 3,911 |
| ops | 13 | 3,355 |
| wiki/prompt-engineering | 90 | 3,099 |
| wiki/tooling | 97 | 2,912 |
| wiki/llm-agents | 78 | 2,696 |
| wiki/ml-frameworks | 83 | 2,556 |
| wiki/compositions | 73 | 2,231 |
| wiki/syntheses | 51 | 2,178 |
| wiki/development | 54 | 2,163 |
| docs | 8 | 2,047 |
| wiki/android-core | 62 | 1,858 |
| wiki/communities | 55 | 1,680 |
| other | 12 | 1,579 |
| wiki/mobile-platform | 50 | 1,549 |
| mykb-nonwiki/.okf-skill | 12 | 1,458 |
| wiki/security | 39 | 1,338 |
| wiki/identity | 36 | 1,114 |
| wiki/decisions | 34 | 1,060 |
| wiki/questions | 24 | 939 |
| wiki/js-ts-ecosystem | 26 | 787 |
| mykb-nonwiki/log.md | 1 | 551 |
| wiki/pulses | 13 | 402 |
| wiki/entities | 9 | 359 |
| mykb-nonwiki/COMPREHENSIVE_AUDIT.md | 1 | 348 |
| mykb-nonwiki/templates | 11 | 273 |
| mykb-nonwiki/AGENTS.md | 1 | 171 |
| wiki/episodes | 5 | 155 |
| wiki/projects | 2 | 93 |
| wiki/sources | 2 | 79 |
| wiki/ops | 2 | 72 |
| wiki/reflections | 2 | 69 |
| wiki/plans | 2 | 55 |
| wiki/experiments | 2 | 53 |
| mykb-nonwiki/README.md | 1 | 45 |
| mykb-nonwiki/Home.md | 1 | 43 |
| mykb-nonwiki/.wiki-daemon | 1 | 33 |
| mykb-nonwiki/index.md | 1 | 16 |
| wiki/daily | 1 | 12 |
| mykb-nonwiki/daily | 1 | 10 |

## 7. Data & Generated Artifacts (json/jsonl)

| Area | Files |
|------|-------|
| space | 41 |
| rsis3 | 40 |
| mykb-nonwiki | 24 |
| other | 6 |
| mykb/wiki | 1 |

## 8. Diagrams

- Generated SVG assets under `diagrams/`: 95
- Generator scripts under `diagrams/gen/`: 19
- Bitmap snapshots (PNG): 4

## 9. Notes on Completeness

- Counts exclude `.git/`, `.shots/`, `.cosmos-pids/`, `.rsirrp/`, `node_modules/`, `dist/` and `.tmp` scratch files. [O]
- Runtime-only files that are git-ignored (`__pycache__`, `*.log`) are excluded; `sentry.log` (5.5 MB) exists in the working tree. [O]
- The full per-file matrix (7,517 rows: path, ext, LOC, component) is reproducible with `find . -type f | xargs wc -l`; AST datasets `data/audit_py.json` and `data/audit_ts.json` accompany this suite. [O]

---
*End of document 04. Next: [05 File-by-File Audit](05_FILE_BY_FILE_AUDIT.md).*