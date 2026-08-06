# Changelog

## [2.2.0] - 2026-08-06

### Added
- RSI Cycle 005: hosting-layer hardening
  - `web/server.mjs` refactored into an exported `createApp({ projectsDir, port })`
    factory — testable against an isolated projects dir, listens only as main;
    dead `matchRoute`, `req_method` global, and unused storage removed
  - `tests/unit/web-server.test.ts`: 7 tests covering CORS preflight, projects
    CRUD, framework endpoints, static SPA, and 404s (157 total, 15 suites)
  - `scripts/sync-static-data.mjs` populates `web/projects.json` so the static
    SPA fallback lists real projects when the API server is unreachable
  - CORS preflight handler for dashboard embeds (204 + allow headers)

### Fixed
- Project creation from the Cosmos dashboard embed (API fallback now only
  serves GETs; mutations report failures instead of silently no-oping)
- Sentry watch paths for mykb Dashboard/Graph retargeted to cosmos-local
  `components/mykb`

### Quality
- ESLint warnings 74 → 24 (unused imports/args, catch bindings, non-null
  assertions, typed JSON shapes, i18n `unknown` walk)
- Prettier-clean across `src/` and `tests/`; typecheck stays clean

## [2.1.0] - 2026-07-29

### Added
- RSI Cycle 003: 10 improvements implemented
  - ArtifactTracker wired into engine core with staleness detection
  - Config validation at CLI startup (`assertValidConfig`)
  - `space config` CLI command (list, get, set)
  - `space serve` web UI server command
  - SnapshotManager auto-snapshots on round/series completion
  - i18n infrastructure (en, es, fr locales with `t()` function)
  - Git auto-commit on `space run --git`
  - Staleness markers in all 6 export formats
  - Adaptive router with 5 real routing rules
  - Session resume framework version check
- Meta document viewer SPA (`meta-viewer.html`)
- New test file: `git-integration.test.ts` (13 tests)
- New test file: `sqlite-storage.test.ts` (17 tests)
- LLM providers: Gemini, Mistral, Ollama

### Fixed
- Session resume from disk storage
- Web UI data loading for all 7 series (326 questions)
- Snapshot `project_id` field for direct path lookup
- npm package metadata (files, engines, types, license)
- CI/CD pipeline (GitHub Actions matrix build)
- Performance: O(projects) scan removed from snapshotDir
- Accessibility: ARIA labels, skip link, focus indicators, reduced motion

## [2.0.0] - 2026-07-25

### Added
- RSI Cycle 002: All 7 roadmap phases implemented
  - Phase 0: Foundation (types, framework loader, CLI)
  - Phase 1: Execution Engine (session manager, state machine)
  - Phase 2: LLM Integration (OpenAI, Anthropic, Template providers)
  - Phase 3: Export Pipeline (JSON, Markdown, YAML, Prompt, HTML, Diff)
  - Phase 4: Interactive UI (React 18 + Vite web app, TUI)
  - Phase 5: Persistence (FileSystemStorage, snapshots, archives)
  - Phase 6: Intelligence (analytics, completeness, contradictions)
- Complete CLI with init, run, export, list, framework, status commands
- Template variable interpolation system
- 92 automated tests across 10 test files

## [1.0.0] - 2026-07-21

### Added
- Initial prompt-framework extraction and audit
- Framework definition: 7 series, 25 rounds, 326 probes
- React web app from original prompt-framework project
- 20 tests for core engine functionality
