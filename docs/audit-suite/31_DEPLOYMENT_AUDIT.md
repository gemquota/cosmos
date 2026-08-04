# 31 — Deployment & Release Audit

**Doc ID:** COSMOS-AUDIT-31 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [22 Build & CI](22_BUILD_CI_ANALYSIS.md) · [25 Documentation](25_DOCUMENTATION_AUDIT.md) · [29 Risk Register](29_RISK_REGISTER.md)

---

## 1. Deployment Topology (Observed)

- **GitHub Pages** serves the site; the `gh-pages` branch mirrors the `main` tree. [O]
- Deploy commits follow the pattern `Deploy: <summary> (main <sha>)` and are created
  manually (orphan history rooted at `Initial gh-pages`). [O]
- `.nojekyll` + `404.html` shim support deep links; `/mykb/` short-link redirects were added
  in a recent deploy. [O]
- Landing `index.html` redirects to the unified dashboard; `docs/ao-assessment.md` tracks
  phase status. [O]
- `components/rsis3/vercel-deploy/index.html` exists as a Vercel-oriented shell. [O]

## 2. Release Flow (Observed)

```
main (feature commits)  →  (manual) sync tree into gh-pages  →  push gh-pages  →  live
```

- No CI, no staging environment, no release notes/changelog. [O]
- **Incident (this audit):** the wiki redesign + type reclassification (main `642817a3`,
  `5579e1f9`) were never deployed; `origin/main`/`gh-pages` stayed at `c1ff5c8`, so the
  live wiki showed the pre-redesign UI (`Select a document`, no Content/Meta toggle).
  Users observed this as "the wiki has regressed". [O]

## 3. Findings

| # | Finding | Severity |
|---|---|---|
| DP-1 | Deploy is manual and untracked → live site can lag main indefinitely | High |
| DP-2 | No way to verify a deploy (no smoke check of live URLs) | Med |
| DP-3 | gh-pages mirror can drift from main (partial sync risk) | Med |
| DP-4 | No rollback procedure documented beyond reverting commits | Med |
| DP-5 | Multiple deploy targets (GH Pages + vercel-deploy shell) without a single source of truth | Low |

## 4. Recommendations

1. Script the deploy: `scripts/deploy.sh` that (a) verifies `gen-static-data.py --check`,
   (b) runs the test suite, (c) syncs the tree into `gh-pages`, (d) pushes with the
   standard `Deploy: … (main <sha>)` message.
2. Add a GH Actions workflow to run the deploy on `main` push (or a `deploy` dispatch).
3. Add a post-deploy smoke check (curl the live `/components/mykb/index.html` and assert the
   `meta-seg`/`home-metrics` markers — exactly the signals that caught this regression).
4. Document the rollback path (redeploy previous `main` sha).
