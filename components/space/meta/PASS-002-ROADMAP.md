# SPACE — Improvement Roadmap & Development Plan

**Project:** Superb Prompt Automatic Creation Engine (SPACE)
**Based on:** Structured Prompt Creation Framework audit (`meta/PASS-001-AUDIT.md`)
**Created:** 2026-07-25
**Version:** 1.0.0

---

## Vision

SPACE transforms a manually-operated, browser-only prompt elicitation framework into a **programmable, LLM-augmented, multi-format specification engine**. The original framework's 326-probe methodology becomes the knowledge backbone; SPACE builds the intelligence, automation, and output layers around it.

---

## Strategic Principles

1. **Data-first:** The 7-series JSON specs and dependency DAG are the canonical knowledge base — everything else is built to serve them
2. **API-native:** Every capability is exposed as a programmatic interface; the UI is one consumer among many
3. **LLM-in-the-loop:** Questions are dynamically refined using accumulated context, not read statically from files
4. **Incremental delivery:** Each phase produces a shippable artifact; no "big bang" integration
5. **Backward compatible:** The original JSON schema remains valid — SPACE extends, never breaks

---

## Phase Overview

| Phase | Name | Duration | Core Deliverable | Dependencies |
|:-----:|------|:--------:|------------------|:------------:|
| 0 | Foundation | 2–3 weeks | Schema v2, engine core, CLI | — |
| 1 | Execution Engine | 3–4 weeks | Programmatic run orchestration | Phase 0 |
| 2 | LLM Integration | 3–4 weeks | Dynamic question refinement + synthesis | Phase 1 |
| 3 | Export Pipeline | 2–3 weeks | Multi-format output generation | Phase 1 |
| 4 | Interactive UI | 3–4 weeks | Web + terminal UIs | Phase 1 |
| 5 | Persistence & Projects | 2–3 weeks | Multi-session, multi-project storage | Phase 1 |
| 6 | Intelligence Layer | 3–4 weeks | Coherence scoring, adaptive routing, analytics | Phase 2 |

**Total estimated timeline:** 18–25 weeks (4.5–6 months) for a single developer

---

## Phase 0: Foundation

**Goal:** Establish the canonical data model, fix all known issues, and create a CLI entry point.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 0.1 | Schema v2 specification | `specs/01-data-schema.md` | P0 |
| 0.2 | Fix `consolidate-spec.sh` broken JSON merging | `specs/03-export-pipeline.md` | P0 |
| 0.3 | Remove 48KB data duplication | — | P0 |
| 0.4 | Implement template variable interpolation for MD specs | `specs/02-architecture.md` §3 | P0 |
| 0.5 | CLI entry point (`space init`, `space run`, `space export`) | `specs/04-api-design.md` | P1 |
| 0.6 | Project scaffolding and directory conventions | `specs/02-architecture.md` §2 | P1 |

### Acceptance Criteria

- [ ] Schema v2 is backward-compatible with v1 JSON format
- [ ] All 326 questions parseable programmatically with unique IDs
- [ ] Dependency DAG is traversable with topological sort
- [ ] `space init my-project` creates a valid project structure
- [ ] No data files exist in two locations
- [ ] MD context variables resolve against accumulated artifact dictionary

### Task Decomposition

See `dev/phase-0-foundation.md` for atomic task breakdown.

---

## Phase 1: Execution Engine

**Goal:** Build the core run-time that orchestrates series/round/question flow programmatically.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 1.1 | Session manager (create, resume, pause) | `specs/05-execution-engine.md` §2 | P0 |
| 1.2 | Series/round/question state machine | `specs/05-execution-engine.md` §3 | P0 |
| 1.3 | Artifact accumulation pipeline | `specs/05-execution-engine.md` §4 | P0 |
| 1.4 | Dependency resolver (which series can run next) | `specs/05-execution-engine.md` §5 | P0 |
| 1.5 | Answer validation layer | `specs/05-execution-engine.md` §6 | P1 |
| 1.6 | Progress tracking and metrics | `specs/05-execution-engine.md` §7 | P2 |

### Acceptance Criteria

- [ ] Can execute a full 25-round session programmatically
- [ ] State is resumable after interruption
- [ ] Dependency constraints are enforced (no out-of-order series)
- [ ] Artifact dictionary grows correctly after each completed round
- [ ] Answer validation catches incomplete or malformed responses

### Task Decomposition

See `dev/phase-1-execution-engine.md` for atomic task breakdown.

---

## Phase 2: LLM Integration

**Goal:** Use language models to dynamically refine questions, synthesize answers, and produce polished specifications.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 2.1 | Context-aware question refinement | `specs/06-llm-integration.md` §2 | P0 |
| 2.2 | Answer synthesis engine | `specs/06-llm-integration.md` §3 | P0 |
| 2.3 | Final specification generator | `specs/06-llm-integration.md` §4 | P0 |
| 2.4 | Quality scoring and coherence checking | `specs/06-llm-integration.md` §5 | P1 |
| 2.5 | Adaptive question generation (beyond the 326 fixed probes) | `specs/06-llm-integration.md` §6 | P2 |

### Acceptance Criteria

- [ ] Questions reference prior answers in their wording
- [ ] Generated specification is coherent and readable
- [ ] Quality score identifies weak/contradictory areas
- [ ] Adaptive questions can be triggered when gaps are detected

### Task Decomposition

See `dev/phase-2-llm-integration.md` for atomic task breakdown.

---

## Phase 3: Export Pipeline

**Goal:** Generate production-ready specification documents in multiple formats from completed sessions.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 3.1 | JSON export (v2 format with metadata) | `specs/03-export-pipeline.md` §2 | P0 |
| 3.2 | Markdown specification document | `specs/03-export-pipeline.md` §3 | P0 |
| 3.3 | YAML export | `specs/03-export-pipeline.md` §4 | P1 |
| 3.4 | Prompt template export (for LLM consumption) | `specs/03-export-pipeline.md` §5 | P1 |
| 3.5 | HTML/PDF export | `specs/03-export-pipeline.md` §6 | P2 |
| 3.6 | Diff/comparison between sessions | `specs/03-export-pipeline.md` §7 | P2 |

### Acceptance Criteria

- [ ] All formats produce valid, parseable output
- [ ] Markdown export includes table of contents and section numbering
- [ ] Prompt template export produces a single copy-paste-ready system prompt
- [ ] Two sessions can be compared to show specification drift

### Task Decomposition

See `dev/phase-3-export-pipeline.md` for atomic task breakdown.

---

## Phase 4: Interactive UI

**Goal:** Replace the original React frontend with a modern, feature-complete interface.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 4.1 | Web UI (React/Next.js or similar) | `specs/07-ui-design.md` §2 | P0 |
| 4.2 | Terminal UI (TUI) for headless environments | `specs/07-ui-design.md` §3 | P1 |
| 4.3 | Real-time progress dashboard | `specs/07-ui-design.md` §4 | P2 |
| 4.4 | Session management UI (list, resume, delete) | `specs/07-ui-design.md` §5 | P1 |
| 4.5 | Inline LLM chat for question answering | `specs/07-ui-design.md` §6 | P2 |

### Acceptance Criteria

- [ ] Web UI supports all 326 probes with full navigation
- [ ] TUI works in terminal-only environments
- [ ] Progress is saved automatically and survives refresh
- [ ] Sessions can be listed and resumed from the UI

### Task Decomposition

See `dev/phase-4-interactive-ui.md` for atomic task breakdown.

---

## Phase 5: Persistence & Projects

**Goal:** Support multi-session, multi-project storage with versioning and history.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 5.1 | File-system project storage | `specs/08-persistence.md` §2 | P0 |
| 5.2 | SQLite session database | `specs/08-persistence.md` §3 | P1 |
| 5.3 | Session versioning (snapshots) | `specs/08-persistence.md` §4 | P2 |
| 5.4 | Import/export of project archives | `specs/08-persistence.md` §5 | P1 |
| 5.5 | Git integration for spec versioning | `specs/08-persistence.md` §6 | P2 |

### Acceptance Criteria

- [ ] Projects are stored as self-contained directories
- [ ] Session history shows all previous runs
- [ ] Snapshots can be restored to any prior state
- [ ] Projects can be exported as portable archives

### Task Decomposition

See `dev/phase-5-persistence.md` for atomic task breakdown.

---

## Phase 6: Intelligence Layer

**Goal:** Add analytics, adaptive routing, and quality intelligence on top of the core engine.

### Deliverables

| # | Deliverable | Spec Reference | Priority |
|---|-------------|----------------|:--------:|
| 6.1 | Cross-session analytics and insights | `specs/09-intelligence.md` §2 | P1 |
| 6.2 | Adaptive question routing (skip irrelevant probes) | `specs/09-intelligence.md` §3 | P2 |
| 6.3 | Specification completeness scoring | `specs/09-intelligence.md` §4 | P1 |
| 6.4 | Contradiction detection | `specs/09-intelligence.md` §5 | P2 |
| 6.5 | Recommendation engine ("you might also consider...") | `specs/09-intelligence.md` §6 | P2 |

### Acceptance Criteria

- [ ] Analytics dashboard shows completion patterns and time-per-series
- [ ] Adaptive routing can skip probes that don't apply based on context
- [ ] Completeness score is actionable (identifies specific gaps)
- [ ] Contradictions between answers are flagged with suggestions

### Task Decomposition

See `dev/phase-6-intelligence.md` for atomic task breakdown.

---

## Cross-Cutting Concerns

### Testing Strategy

| Layer | Tools | Coverage Target |
|-------|-------|:---------------:|
| Unit (schema validation) | JSON Schema + custom validators | 100% of data files |
| Unit (engine logic) | Jest/Vitest | 90%+ for state machine, DAG |
| Integration (API) | Supertest or similar | All endpoints |
| E2E (UI) | Playwright or similar | Critical user paths |
| LLM (synthesis quality) | Human eval + automated scoring | All output formats |

### Documentation Standards

- All specs use the template in `specs/README.md`
- All dev docs use the template in `dev/README.md`
- API endpoints documented with request/response examples
- Every public function has JSDoc/docstring

### Technology Decisions (Recommended)

| Concern | Recommendation | Rationale |
|---------|---------------|-----------|
| Language | TypeScript | Type safety for schema-heavy work; ecosystem |
| Runtime | Node.js (+ optional Bun) | Vite compatibility; npm ecosystem |
| Web UI | React 18 + Vite | Inherit existing patterns from original app |
| TUI | Ink (React for CLI) or Blessed | Rich terminal UI with component model |
| Storage | SQLite via better-sqlite3 | Embedded, zero-config, fast |
| LLM | OpenAI API + provider abstraction | Flexibility to swap models |
| Testing | Vitest + Playwright | Fast, modern, Vite-compatible |
| Build | Vite for web, tsc for lib | Matches existing setup |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|:----------:|:------:|------------|
| LLM synthesis quality insufficient | Medium | High | Fallback to template-based generation; human-in-the-loop |
| Scope creep across phases | High | Medium | Strict phase gates; MVP-first within each phase |
| Schema v2 breaks existing sessions | Low | High | Migration tool in Phase 0; backward compat mode |
| TUI complexity underestimated | Medium | Low | Ship web UI first; TUI is stretch goal |
| Testing coverage gaps | Medium | Medium | CI-enforced coverage thresholds |

---

## Document Index

| Document | Location | Description |
|----------|----------|-------------|
| Audit Report | `meta/PASS-001-AUDIT.md` | Original framework analysis |
| **This Roadmap** | `meta/PASS-002-ROADMAP.md` | Master improvement plan |
| Architecture Spec | `meta/specs/01-data-schema.md` | Data model and schema |
| Architecture Spec | `meta/specs/02-architecture.md` | System architecture |
| API Design | `meta/specs/04-api-design.md` | CLI and API interfaces |
| Export Pipeline | `meta/specs/03-export-pipeline.md` | Multi-format output |
| Execution Engine | `meta/specs/05-execution-engine.md` | Core run-time logic |
| LLM Integration | `meta/specs/06-llm-integration.md` | Language model features |
| UI Design | `meta/specs/07-ui-design.md` | Web and terminal UIs |
| Persistence | `meta/specs/08-persistence.md` | Storage and projects |
| Intelligence Layer | `meta/specs/09-intelligence.md` | Analytics and adaptation |
| Phase 0 Dev Guide | `meta/dev/phase-0-foundation.md` | Foundation tasks |
| Phase 1 Dev Guide | `meta/dev/phase-1-execution-engine.md` | Engine tasks |
| Phase 2 Dev Guide | `meta/dev/phase-2-llm-integration.md` | LLM tasks |
| Phase 3 Dev Guide | `meta/dev/phase-3-export-pipeline.md` | Export tasks |
| Phase 4 Dev Guide | `meta/dev/phase-4-interactive-ui.md` | UI tasks |
| Phase 5 Dev Guide | `meta/dev/phase-5-persistence.md` | Persistence tasks |
| Phase 6 Dev Guide | `meta/dev/phase-6-intelligence.md` | Intelligence tasks |
| Spec Template | `meta/specs/README.md` | Specification document template |
| Dev Doc Template | `meta/dev/README.md` | Development document template |
