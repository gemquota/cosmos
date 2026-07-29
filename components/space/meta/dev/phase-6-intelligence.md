# Phase 6: Intelligence Layer — Development Guide

**Spec References:** `specs/09-intelligence.md`
**Prerequisites:** Phase 2 complete
**Estimated Effort:** 3–4 weeks
**Sprint Count:** 2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Add analytics, adaptive routing, quality intelligence, contradiction detection, and recommendation capabilities on top of the core engine. This is what makes SPACE "superb" — not just a questionnaire, but an intelligent specification collaborator.

---

## Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 6.T1 | Session metrics collector | 09 §3.1 | M | 1.T1 | Timing and quality metrics computed |
| 6.T2 | Cross-project analytics | 09 §3.1 | M | 6.T1 | Insights aggregated across sessions |
| 6.T3 | Completeness scorer (7 dimensions) | 09 §3.3 | L | 1.T5 | Score 0-100 with dimension breakdown |
| 6.T4 | Contradiction detector | 09 §3.4 | L | 2.T5 | Detects direct, implied, temporal contradictions |
| 6.T5 | Adaptive question router | 09 §3.2 | L | 1.T4, 2.T5 | Skips irrelevant questions with reason |
| 6.T6 | Recommendation engine | 09 §3.5 | M | 6.T3, 6.T4 | Generates actionable recommendations |
| 6.T7 | Intelligence report generator | 09 §4 | M | 6.T1–6.T6 | Combines all into single report |
| 6.T8 | Dashboard analytics widgets | 07 §3.1 | M | 6.T1, 4.T2 | Charts and stats in dashboard |
| 6.T9 | Completeness indicator in UI | 07 §3.2 | S | 6.T3, 4.T3 | Visual score shown during questions |
| 6.T10 | Integration tests for intelligence | — | M | 6.T1–6.T7 | All intelligence features tested |

---

## Task Details

#### 6.T3: Completeness Scorer

**What:**
Implement the 7-dimension completeness scoring system per spec `09-intelligence.md` §3.3.

**Files:**
- `src/intelligence/completeness-scorer.ts`
- `src/intelligence/dimensions.ts` — Dimension definitions
- `tests/intelligence/completeness-scorer.test.ts`

**Implementation Notes:**
- Each dimension checks for required artifacts and their confidence scores
- Weighted average across dimensions
- Readiness levels: draft (<40%), review (40-80%), ready (>80%)
- Missing artifacts = 0 score for that dimension; present but low confidence = reduced score

**Done When:**
- [ ] All 7 dimensions implemented with correct weights
- [ ] Full session scores 90-100
- [ ] Empty session scores 0
- [ ] Partial session scores proportionally
- [ ] Readiness levels assigned correctly

---

#### 6.T4: Contradiction Detector

**What:**
Detect contradictions between answers — direct conflicts, implied inconsistencies, and temporal contradictions.

**Files:**
- `src/intelligence/contradiction-detector.ts`
- `src/intelligence/rules/` — Individual contradiction rules
- `tests/intelligence/contradiction-detector.test.ts`

**Contradiction rule examples:**
| Rule | Type | Logic |
|------|------|-------|
| Domain vs entities | Implied | Single domain chosen but entities span multiple |
| Team vs methodology | Direct | Solo team + Scrum methodology |
| Performance vs hardware | Implied | Enterprise hardware + minimal traffic |
| Scale vs deployment | Direct | Internet-scale + single-server |

**Done When:**
- [ ] At least 10 contradiction rules implemented
- [ ] All rules tested with synthetic contradictions
- [ ] False positive rate <5% on clean sessions
- [ ] Each contradiction includes resolution suggestion

---

#### 6.T5: Adaptive Question Router

**What:**
Override the default sequential question flow with intelligent routing that can skip, reorder, or generate additional questions.

**Files:**
- `src/intelligence/adaptive-router.ts`
- `src/intelligence/skip-rules.ts` — Skip heuristics
- `tests/intelligence/adaptive-router.test.ts`

**Implementation Notes:**
- Skip rules check artifacts before each question
- If a question is skipped, it's marked as "skipped" (not unanswered)
- Adaptive probes are added to the queue when gaps detected
- User can toggle adaptive mode on/off

**Done When:**
- [ ] Simple domains skip deep ontological rounds
- [ ] Vague answers trigger clarification questions
- [ ] All skip decisions logged with reasons
- [ ] Adaptive mode can be disabled (falls back to sequential)

---

## Testing

- Analytics: mock sessions with known timing → verify metrics
- Completeness: known-complete session scores high; empty scores 0
- Contradictions: synthetic contradictions detected; clean sessions pass
- Adaptive routing: verify correct skip/continue decisions
- Intelligence report: all components integrated correctly

## Risks

- Contradiction detection false positives — start with conservative rules
- Adaptive routing may confuse users — always explain why a question was skipped
- Intelligence layer adds latency — run synchronously only for scoring; analytics can be async
