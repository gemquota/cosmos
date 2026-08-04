# 27 — Code Quality Scorecard

**Doc ID:** COSMOS-AUDIT-27 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [06 Module-by-Module](06_MODULE_BY_MODULE_AUDIT.md) · [14 Static Code Analysis](14_STATIC_CODE_ANALYSIS.md) · [28 Technical Debt](28_TECHNICAL_DEBT_REGISTER.md)

---

## 1. Scorecard (1–10; observed)

| Dimension | RSIS3 core | MyKB viewer | SPACE / dashboards | Notes |
|---|---|---|---|---|
| Structure / cohesion | 8 | 6 | 7 | per-loop modules clean; `index.html` is a 3k-line monolith |
| Readability / naming | 8 | 6 | 7 | clear names, small helpers; JS is var-heavy legacy style |
| Typing / annotations | 7 | 2 | 4 | Python uses modern annotations; JS/TS minimal |
| Error handling | 8 | 5 | 5 | classifier + budgets + recovery; viewer falls back silently |
| Testability | 7 | 3 | 3 | core loops L3–L9 untested; no JS harness (see [26](26_TESTING_AUDIT.md)) |
| Performance awareness | 7 | 6 | 6 | capped renders (MAX_RENDER), DAG caps; eager file list in viewer |
| Documentation | 8 | 6 | 5 | strong AGENTS/audit; thin API/config docs (see [25](25_DOCUMENTATION_AUDIT.md)) |
| Consistency | 7 | 5 | 6 | Python style consistent; JS/TS conventions drift |
| **Overall** | **7.6** | **4.9** | **5.4** | |

## 2. Strengths (Observed)

- Clean separation of the nine loops; config/tunable registries centralize tuning surface.
- Ports (AO) land with tests + config gates; D1/D2 added 49 cases where none existed.
- Invariants are enforced by tooling (`check-practices`, `gen-static-data.py --check`).
- Dataclasses + type annotations throughout the Python core.

## 3. Weaknesses (Observed)

- `components/mykb/index.html` mixes parser, router, renderer, and state in one file
  (~3,000 lines, var-based ES5) — the highest-complexity, lowest-testability artifact.
- No lint/format/type gate in CI (see [22](22_BUILD_CI_ANALYSIS.md)).
- Frontmatter quoting is inconsistent (`type: concept` vs `type: "concept"`), a symptom of
  mixed generators — see [28](28_TECHNICAL_DEBT_REGISTER.md).
- SPACE TS files appear in the census with `for`/`if` misclassified as functions — the
  census tooling itself needs a fix (see [35 Appendices](35_APPENDICES.md)).

## 4. Recommendations

1. Split `index.html` into modules (parser.js, router.js, sidebar.js) or migrate to a
   build step; until then, add a JS unit harness for `parseMarkdown`.
2. Add ruff + CI gate; fix the TS census function-detection bug.
3. Standardize frontmatter quoting via a single writer in `build_files_index.py`.
