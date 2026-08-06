# SPACE — RSI Cycle-005 Comprehensive Audit Report

**Project:** Superb Prompt Automatic Creation Engine (SPACE)
**Date:** 2026-08-06
**Cycle:** RSI Cycle 005 (Pass 005)
**Codebase:** 60 source files, 14 test files, 150 tests passing
**Build:** TypeScript strict ✓ | ESLint 0 errors (74 warnings) | Prettier 1 file off
**Hosting:** web/server.mjs :8888 · meta-viewer :8899 · embedded in Cosmos dashboard

---

## Executive Summary

Cycle 004 delivered production-readiness tooling. Since then SPACE was
integrated into the Cosmos dashboard as a hosted component: the vanilla
`web/index.html` SPA + `web/server.mjs` Node API, the `meta-viewer.html`
pass viewer, and sentry watches. Pass 005 audits the **hosting layer** that
Cycle 004 never touched (it predates the cosmos integration) plus the
engineering gaps the web UI uncovered — including the project-creation bug
fixed in `3c0eee81` (CORS preflight + API fallback), which shipped because
the web server had zero automated tests.

### Key Metrics

| Metric | Cycle 004 | Cycle 005 Target |
|--------|:---------:|:----------------:|
| Tests passing | 150 | 165+ |
| Web-server tests | 0 | 12+ |
| Lint warnings | 0 | <25 |
| Prettier clean | ✅ | ✅ |
| Static project fallback | empty | populated |
| Watch paths (mykb) | stale | cosmos-local |

---

## Section 1: Web Server — Untested, Unmaintainable

### 1.1 Zero Automated Tests

**Current state:** `web/server.mjs` (396 lines, 15 API routes) has no tests.
The CORS preflight bug and the static-fallback swallowing POSTs were both
found manually after the dashboard embed shipped.

**Required:**
- Refactor `server.mjs` to export a `createApp({ projectsDir })` factory so
  tests run against a temp projects dir and never touch `~/.space/projects`.
- Auto-listen only when run as the main module.
- `tests/unit/web-server.test.ts`: preflight 204 + CORS headers, projects
  CRUD (list/create/duplicate/detail/delete), framework endpoints, static
  index.html, 404s.

### 1.2 Dead Code & Module-State Bugs

**Current state:** `matchRoute()` (defined, never called) and the global
`req_method` variable; `storage = new FileSystemStorage(...)` is created and
never used. The `req_method` global is racy if requests ever interleave.

**Required:** delete `matchRoute`, the global, and unused `storage`; pass
`req.method` explicitly through the request handler.

## Section 2: Static Fallback — Projects.json Empty

**Current state:** `web/projects.json` is 0 bytes. The SPA's static GET
fallback (`STATIC_API['/api/projects']`) therefore yields a JSON parse error
instead of a project list when the server is unreachable (e.g. GitHub Pages).

**Required:** a `scripts/sync-static-data.mjs` generator that dumps the
projects from `~/.space/projects` into `web/projects.json`, plus a populated
file committed so static hosting shows the real projects.

## Section 3: Sentry Watches — Stale mykb Paths

**Current state:** `watches.json` mykb Dashboard/Graph/myrsikb entries point
at `/data/data/com.termux/files/home/dev/codex/mykb` (pre-cosmos locations).
The repo now hosts mykb at `components/mykb` with `server.py` and
`okf-graph.html`.

**Required:** retarget watch entries to the cosmos-local mykb paths.

## Section 4: Lint & Format Debt

**Current state:** 74 ESLint warnings (37 `no-explicit-any`, 35
`no-unused-vars`, 2 `no-non-null-assertion`); `tests/unit/cli.test.ts` is
not Prettier-clean.

**Required:** clear the unused-vars/non-null-assertion warnings, trim the
`any` batch where mechanical, and run Prettier over the tree.

## Section 5: Docs & Versioning Drift

**Current state:** package.json `2.1.0` / CHANGELOG top entry is Cycle 003;
nothing documents the cosmos hosting layer (`web/server.mjs`, CORS, embed
fallback). README describes the legacy `space serve` CLI path only.
`meta-viewer.html`'s DOCUMENTS registry and welcome card hardcode the latest
pass, so each cycle requires a manual edit.

**Required:** bump to `2.2.0`, CHANGELOG Cycle 005 entry, README section on
the hosted web server + dashboard embed, and register Pass 005 in the viewer.

---

## Priority Matrix

| # | Item | Area | Effort | Priority |
|:-:|------|------|:------:|:--------:|
| 1 | Refactor server.mjs for testability | Web | S | 🔴 Critical |
| 2 | web-server.test.ts (12+ tests) | Testing | M | 🔴 Critical |
| 3 | Populate projects.json + sync script | Web | S | 🔴 High |
| 4 | Fix watches.json mykb paths | Infra | S | 🔴 High |
| 5 | Dead-code removal (matchRoute, storage, req_method) | Web | S | 🟡 Medium |
| 6 | Lint warnings 74 → <25 | Quality | M | 🟡 Medium |
| 7 | Prettier format pass | Quality | S | 🟡 Medium |
| 8 | Version 2.2.0 + CHANGELOG + README | Docs | S | 🟡 Medium |
| 9 | Pass 005 viewer registration + cycle docs | Docs | S | 🟡 Medium |

**Total estimated effort:** 2-3 days

---

*Generated: 2026-08-06 | SPACE v2.1.0 — RSI Cycle 005 Audit*
