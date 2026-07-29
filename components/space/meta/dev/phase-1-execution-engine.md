# Phase 1: Execution Engine — Development Guide

**Spec References:** `specs/05-execution-engine.md`, `specs/02-architecture.md`
**Prerequisites:** Phase 0 complete
**Estimated Effort:** 3–4 weeks
**Sprint Count:** 2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Build the core run-time engine that orchestrates the entire elicitation flow — session lifecycle, question routing, artifact accumulation, dependency resolution, answer validation, and progress tracking. This is the programmable brain of SPACE.

---

## Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 1.T1 | Session manager (create, resume, pause, complete) | 05 §3.1 | L | 0.T1 | All lifecycle transitions work; state persists |
| 1.T2 | Series state machine (lock/available/in_progress/complete) | 05 §3.2 | M | 0.T1 | Series gate correctly based on dependencies |
| 1.T3 | Round state machine with auto-transitions | 05 §3.3 | M | 1.T2 | Rounds advance on answer submission |
| 1.T4 | Question router (find next unanswered question) | 05 §3.4 | L | 1.T2, 1.T3 | Always returns correct next question |
| 1.T5 | Artifact accumulation pipeline | 05 §3.5 | L | 0.T1, 1.T3 | Artifacts populate correctly per mapping table |
| 1.T6 | Answer validation layer | 05 §3.6 | M | 0.T1 | Rejects invalid answers; warns on weak ones |
| 1.T7 | Progress tracking and metrics | 05 §3.7 | M | 1.T1 | Accurate completion_pct and timing |
| 1.T8 | Auto-save and snapshot system | 05 §3.8 | M | 1.T1 | State saved after each answer; recovery works |
| 1.T9 | Dependency resolver (next available series) | 05 §3.2 | M | 1.T2 | Correct series available after dependencies met |
| 1.T10 | Integration tests for full session flow | — | L | 1.T1–1.T9 | 326-question session completes programmatically |
| 1.T11 | `space run` CLI command (interactive mode) | 04 §3.1 | M | 1.T4, 1.T6 | Interactive question/answer loop in terminal |

---

## Task Details

#### 1.T1: Session Manager

**What:**
Implement `SessionManager` class with `create`, `resume`, `pause`, `complete` methods. Each method transitions session state and persists to disk.

**Files:**
- `src/engine/session-manager.ts`
- `tests/engine/session-manager.test.ts`

**Done When:**
- [ ] `createSession()` returns new SessionState with unique ID
- [ ] `resumeSession()` loads from disk and restores state
- [ ] `pauseSession()` persists current state
- [ ] `completeSession()` marks status='completed' and persists
- [ ] All transitions validated (can't complete a paused session, etc.)

---

#### 1.T2: Series State Machine

**What:**
Implement series state transitions with strict dependency gating. Fixes audit issue #6 (original only checked last round).

**Files:**
- `src/engine/series-state.ts`
- `tests/engine/series-state.test.ts`

**Done When:**
- [ ] Series 1 always available (no dependencies)
- [ ] Series 2 locked until all 3 rounds of Series 1 complete
- [ ] Series 4 locked until Series 2 AND 3 both complete
- [ ] `getNextAvailableSeries()` returns correct series
- [ ] All 7 series unlock in correct order

---

#### 1.T5: Artifact Accumulation Pipeline

**What:**
Implement the artifact extraction logic per the mapping table in spec `05-execution-engine.md` §3.5. After each round completes, extract answer values and populate the artifact dictionary.

**Files:**
- `src/engine/artifact-builder.ts`
- `src/engine/artifact-mapping.ts` — Mapping registry
- `tests/engine/artifact-builder.test.ts`

**Done When:**
- [ ] All 28 artifact keys are mapped to source questions
- [ ] `computeArtifacts()` populates correct values from mock answers
- [ ] Dependencies between artifacts honored (entity_list before entity_attributes)
- [ ] Confidence scores calculated correctly

---

#### 1.T10: Full Session Integration Test

**What:**
End-to-end test that creates a session, answers all 326 questions programmatically, verifies artifact accumulation, and exports results.

**Files:**
- `tests/integration/full-session.test.ts`

**Implementation Notes:**
- Use mock answer generator (random valid choices + short text)
- Verify: all 25 rounds complete, all 7 series complete, session status = 'completed'
- Verify: artifact dictionary has all 28 keys
- Verify: export produces valid JSON

**Done When:**
- [ ] Test runs in <2 seconds (no LLM, no disk I/O beyond necessary)
- [ ] All assertions pass
- [ ] No memory leaks (process exits cleanly)

---

## Testing

- Unit tests for each module (T1–T9)
- Integration test for full session flow (T10)
- Edge case tests: empty session, all skipped, resume mid-session

## Risks

- Artifact mapping complexity — the mapping table has 28 entries with dependencies; thorough testing required
- State serialization format must be forward-compatible — use versioned snapshots
