# 28 — Technical Debt Register

**Doc ID:** COSMOS-AUDIT-28 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [05 File-by-File](05_FILE_BY_FILE_AUDIT.md) · [07 Function-by-Function](07_FUNCTION_BY_FUNCTION_AUDIT.md) · [11 Dependency Analysis](11_DEPENDENCY_ANALYSIS.md)

---

## 1. Register

| ID | Item | Severity | Area | Cost / Risk | Mitigation |
|---|---|---|---|---|---|
| TD-1 | No CI pipeline (regressions surface manually) | High | process | D1 retry-spin bug shipped before tests existed | GH Actions (see [22](22_BUILD_CI_ANALYSIS.md)) |
| TD-2 | `numpy`/`networkx` imported but commented out of requirements | High | deps | import crash on clean env | pin + uncomment (see [24](24_DEPENDENCY_AUDIT.md)) |
| TD-3 | Pulse/state JSON non-atomic writes | Med | core | torn reads, data loss on crash | atomic writer helper |
| TD-4 | Thread-per-connection HTTP servers, no limits | Med | infra | resource exhaustion | connection cap / asyncio server |
| TD-5 | Sandbox vs plain tool routers duplicated | Med | core | guard drift (D1 fixed one instance) | unified executor wrapper |
| TD-6 | `index.html` ~3k-line monolith (ES5) | Med | UI | hard to test, risky edits | split into modules |
| TD-7 | Weekly frontmatter reclassification passes | Med | data | taxonomy churn, mixed quoting | canonical schema + single writer |
| TD-8 | No lint/format/type gates | Med | process | style drift across 3 components | ruff + CI |
| TD-9 | Unversioned deps; no lockfile | Low | deps | reproducibility | pyproject + pins |
| TD-10 | Manual gh-pages deploy (stale-deploy incidents) | Med | ops | live site lags main | CI deploy or sync script |
| TD-11 | No CHANGELOG | Low | docs | history opaque | transcribe phase commits |
| TD-12 | Evaluator subprocess path hardcoded via config default | Med | core | SPOF, brittle | fallback engine (see [20](20_RESILIENCE_ANALYSIS.md)) |
| TD-13 | Scratch artifacts committed (`.rsis/*.tmp`, ops slices) | Low | hygiene | repo bloat | gitignore + cleanup |
| TD-14 | TS audit census misclassifies `for`/`if` as functions | Low | tooling | skewed metrics | fix extractor |

## 2. Top-Priority Paydown Order

1. **TD-2** (dependency mismatch — breaks clean installs)
2. **TD-1** (CI — prevents regressions)
3. **TD-3** (atomic writes — data integrity)
4. **TD-5** (router unification — correctness drift)
5. **TD-10** (deploy automation — live-site correctness, just caused a user-visible regression)
