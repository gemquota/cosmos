# 35 — Appendices

**Doc ID:** COSMOS-AUDIT-35 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [00 Executive Summary](00_EXECUTIVE_SUMMARY.md) · [36 Glossary](36_GLOSSARY.md)

---

## 1. Full Suite Index (36 docs)

| # | Doc | File |
|---|---|---|
| 00 | Executive Summary | `00_EXECUTIVE_SUMMARY.md` |
| 01 | Repository Overview | `01_REPOSITORY_OVERVIEW.md` |
| 02 | Architecture Analysis | `02_ARCHITECTURE_ANALYSIS.md` |
| 03 | System Architecture Specification | `03_SYSTEM_ARCHITECTURE_SPECIFICATION.md` |
| 04 | Repository Inventory | `04_REPOSITORY_INVENTORY.md` |
| 05 | File-by-File Audit | `05_FILE_BY_FILE_AUDIT.md` |
| 06 | Module-by-Module Audit | `06_MODULE_BY_MODULE_AUDIT.md` |
| 07 | Function-by-Function Audit | `07_FUNCTION_BY_FUNCTION_AUDIT.md` |
| 08 | Class-by-Class Audit | `08_CLASS_BY_CLASS_AUDIT.md` |
| 09 | Control Flow Analysis | `09_CONTROL_FLOW_ANALYSIS.md` |
| 10 | Data Flow Analysis | `10_DATA_FLOW_ANALYSIS.md` |
| 11 | Dependency Analysis | `11_DEPENDENCY_ANALYSIS.md` |
| 12 | Data Model Analysis | `12_DATA_MODEL_ANALYSIS.md` |
| 13 | Algorithm Analysis | `13_ALGORITHM_ANALYSIS.md` |
| 14 | Static Code Analysis | `14_STATIC_CODE_ANALYSIS.md` |
| 15 | Performance Audit | `15_PERFORMANCE_AUDIT.md` |
| 16 | Memory Analysis | `16_MEMORY_ANALYSIS.md` |
| 17 | Concurrency Analysis | `17_CONCURRENCY_ANALYSIS.md` |
| 18 | Security Audit | `18_SECURITY_AUDIT.md` |
| 19 | Reliability Analysis | `19_RELIABILITY_ANALYSIS.md` |
| 20 | Resilience & Recovery Analysis | `20_RESILIENCE_ANALYSIS.md` |
| 21 | Configuration Analysis | `21_CONFIGURATION_ANALYSIS.md` |
| 22 | Build & CI Analysis | `22_BUILD_CI_ANALYSIS.md` |
| 23 | Logging & Monitoring Analysis | `23_LOGGING_MONITORING_ANALYSIS.md` |
| 24 | Dependency Audit | `24_DEPENDENCY_AUDIT.md` |
| 25 | Documentation Audit | `25_DOCUMENTATION_AUDIT.md` |
| 26 | Testing & Verification Audit | `26_TESTING_AUDIT.md` |
| 27 | Code Quality Scorecard | `27_CODE_QUALITY_SCORECARD.md` |
| 28 | Technical Debt Register | `28_TECHNICAL_DEBT_REGISTER.md` |
| 29 | Risk Register | `29_RISK_REGISTER.md` |
| 30 | Performance Benchmarks | `30_PERFORMANCE_BENCHMARKS.md` |
| 31 | Deployment & Release Audit | `31_DEPLOYMENT_AUDIT.md` |
| 32 | Integration & API Audit | `32_INTEGRATION_API_AUDIT.md` |
| 33 | Engineering Specification | `33_ENGINEERING_SPECIFICATION.md` |
| 34 | Operational Manual | `34_OPERATIONAL_MANUAL.md` |
| 35 | Appendices (this doc) | `35_APPENDICES.md` |
| 36 | Glossary | `36_GLOSSARY.md` |

## 2. Methodology

- **Census:** `data/audit_py.json` (90 files / 21,659 LOC) and `data/audit_ts.json`
  (77 entries) extracted with an AST-style analyzer; import graphs, functions, classes,
  and interfaces recorded per file.
- **Tagging convention:** `[O]` = observed directly in code/run output · `[I]` = inferred
  from code structure · `[R]` = recommended.
- **Grounding:** numbers (6,855 docs, 35,514 graph edges, 49 tests) captured 2026-08-04 from
  live snapshots and test runs.
- **Known census limitation:** the TS extractor misclassifies `for`/`if` as functions
  (TD-14) — treat TS function counts as approximate.

## 3. Provenance & Tooling

- Builders: `components/mykb/.wiki-daemon/build_files_index.py`, `build_graph.py`,
  `build_stats.py`, root `gen-static-data.py`.
- Test suites: `components/rsis3/tests/` (pytest, 49 cases).
- Sources of truth: `AGENTS.md`, `docs/ao-cosmos-comprehensive-review.md`,
  `docs/ao-assessment.md`.
