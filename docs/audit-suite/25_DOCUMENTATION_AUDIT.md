# 25 — Documentation Audit

**Doc ID:** COSMOS-AUDIT-25 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [01 Repository Overview](01_REPOSITORY_OVERVIEW.md) · [04 Repository Inventory](04_REPOSITORY_INVENTORY.md) · [35 Appendices](35_APPENDICES.md)

---

## 1. Documentation Inventory (Observed)

| Doc | Location | Coverage |
|---|---|---|
| Agent instructions | root `AGENTS.md` | architecture, components, invariants, L3 consolidation practice, deployment |
| AO integration review | `docs/ao-cosmos-comprehensive-review.md` | 336-line COSMOS × AO analysis + D1–D5 roadmap |
| Assessment status | `docs/ao-assessment.md` | phase tracking |
| This audit suite | `docs/audit-suite/` (36 docs) | full-system audit |
| Wiki (MyKB) | `components/mykb/wiki/` (6,855 docs) | content knowledge base |
| Operational docs | `components/mykb/ops/` (43 tracked files) | curation, prompts, reports, plans |
| Dashboard | `components/rsis3/dashboard/` | self-describing UI tabs |
| Usage practices | `components/rsis3/docs/usage-practices.md` | workspace/loop hygiene |
| MyKB self-docs | `mykb-code.md`, `mykb-content.md` | code/content orientation |

## 2. Coverage Gaps

| Gap | Severity |
|---|---|
| No generated API reference for `rsis.*` modules (docstrings exist, no docs build) | Med |
| No configuration reference (all `RSIS_*` env vars in one place) — see [21](21_CONFIGURATION_ANALYSIS.md) | Med |
| No architecture diagram beyond the ASCII block in AGENTS.md | Low |
| No CHANGELOG; behavior changes are inferred from commit messages | Low |
| Deploy procedure is implicit (gh-pages sync commits) — see [31](31_DEPLOYMENT_AUDIT.md) | Med |
| Dashboard embedding contracts (OKF graph, meta-viewer) partially documented in AGENTS.md | Low |

## 3. Consistency Findings

- AGENTS.md correctly describes the unified-dashboard invariant; no standalone dashboards
  have been added since. [O]
- The wiki's own frontmatter schema (type taxonomy) is documented only implicitly through
  `mykb-content.md` + curation reports; a formal schema doc would help the reclassification
  passes that recur weekly. [I, Med]
- Docs cross-link well within the audit suite; links were verified by reference extraction. [O]

## 4. Recommendations

1. Add `docs/configuration-reference.md` generated from `config.py` (ties to [21](21_CONFIGURATION_ANALYSIS.md)).
2. Add a `CHANGELOG.md` with per-phase entries (Phases A–C, D1, D2 are already committed
   history — transcribe into the changelog).
3. Document the frontmatter type taxonomy (concept/entity/pulse/synthesis/…) with the
   canonical list and migration notes.
4. Add a `docs/architecture.md` rendered from AGENTS.md's ASCII diagram with module contracts.
