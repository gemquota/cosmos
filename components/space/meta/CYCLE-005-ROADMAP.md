# SPACE — Cycle 005 Improvement Roadmap

**Date:** 2026-08-06
**Based on:** `meta/CYCLE-005-AUDIT.md`
**Status:** In progress

---

## Overview

Cycle 005 (Pass 005) hardens the hosting layer that carries SPACE in the
Cosmos dashboard: test the web server, fix its dead code, populate the
static fallback, retarget sentry watches, pay down lint/format debt, and
sync versioning/docs with the hosted reality.

## Improvement Items

| # | Item | Area | Effort | Priority |
|:-:|------|------|:-----:|:--------:|
| 1 | Refactor `web/server.mjs` → `createApp({ projectsDir })` factory, main-module listen, remove `matchRoute`/`req_method`/unused `storage` | Web | S | 🔴 Critical |
| 2 | Add `tests/unit/web-server.test.ts` (12+ tests: preflight, projects CRUD, framework, static, 404) | Testing | M | 🔴 Critical |
| 3 | Add `scripts/sync-static-data.mjs` + populate `web/projects.json` | Web | S | 🔴 High |
| 4 | Retarget `watches.json` mykb entries to cosmos `components/mykb` | Infra | S | 🔴 High |
| 5 | Fix lint warnings (74 → <25) and run Prettier | Quality | M | 🟡 Medium |
| 6 | Bump version to 2.2.0 + CHANGELOG + README hosting section | Docs | S | 🟡 Medium |
| 7 | Register Pass 005 in meta-viewer + update overview/status docs | Docs | S | 🟡 Medium |

## Execution Order

All items executed consecutively with verification after each. Verification
gates: `npm test` green, `npm run typecheck` clean, `npm run lint` warnings
<25, `npm run format:check` clean.
