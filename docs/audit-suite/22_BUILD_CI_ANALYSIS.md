# 22 — Build & CI Analysis

**Doc ID:** COSMOS-AUDIT-22 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [04 Repository Inventory](04_REPOSITORY_INVENTORY.md) · [24 Dependency Audit](24_DEPENDENCY_AUDIT.md) · [31 Deployment](31_DEPLOYMENT_AUDIT.md)

---

## 1. Build Tooling Inventory (Observed)

| Target | Tooling | Artifacts |
|---|---|---|
| MyKB snapshots | `components/mykb/.wiki-daemon/build_files_index.py`, `build_graph.py`, `build_stats.py` | `files.json`, `graph.json`, `stats.html` data |
| Ecosystem data | `gen-static-data.py` (repo root) | `files.json`, `ecosystem.json`, loops data |
| RSIS3 | pure Python (stdlib) | none compiled |
| SPACE / dashboard | self-contained HTML (no build step) | static SPAs |
| Tests | `pytest` (in `components/rsis3/requirements.txt`) | 49 test cases |

## 2. Continuous Integration (Observed)

- **No CI workflows:** `.github/workflows` does not exist. [O]
- No lint config (flake8/ruff/black), no type checking (mypy/pyright), no pre-commit hooks. [O]
- The only automated checks are in-repo: `gen-static-data.py --check`,
  `python -m rsis check-practices`, and the pytest suite. [O]

## 3. Repeatability

- Snapshot generation is deterministic given the wiki tree (build scripts parse frontmatter +
  files). [O]
- Demo commands (`python -m rsis pipeline`, `python -m rsis scheduler`) provide smoke paths. [O]
- **Finding:** there is no lockfile or pinned environment; pytest is unversioned in
  `requirements.txt` (`pytest>=7.0.0`), and the Node side has no manifest at all. [I, Med]

## 4. Findings

| # | Finding | Severity |
|---|---|---|
| B-1 | No CI: regressions (like the D1 retry spin) only surface via manual pytest runs | High |
| B-2 | No lint/format/type gates; style drift across 3 components | Med |
| B-3 | `pytest>=7.0.0` unpinned; reproducibility risk | Low |
| B-4 | Snapshot freshness depends on humans running build scripts (stale `gh-pages` deploy is a live example) | Med |
| B-5 | No benchmark runner for dashboard/performance numbers | Low |

## 5. Recommendations

1. Add a minimal GitHub Actions workflow: `pytest components/rsis3`, `gen-static-data.py --check`,
   and a link-check for `docs/audit-suite` on push to `main`.
2. Add `ruff` config + `pyproject.toml`; run `ruff check` in CI.
3. Pin pytest (and any future deps) to exact versions in `requirements.txt`.
4. Add a `make verify` target chaining: tests → `--check` → `check-practices`.
