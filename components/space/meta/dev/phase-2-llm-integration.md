# Phase 2: LLM Integration — Development Guide

**Spec References:** `specs/06-llm-integration.md`
**Prerequisites:** Phase 1 complete
**Estimated Effort:** 3–4 weeks
**Sprint Count:** 2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Integrate language models to dynamically refine questions, synthesize richer artifacts, score answer quality, generate polished specifications, and produce adaptive follow-up probes. This transforms SPACE from a static questionnaire into an intelligent elicitation system.

---

## Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 2.T1 | LLM provider abstraction layer | 06 §3.7 | M | — | OpenAI, Anthropic, Local, Null providers |
| 2.T2 | Prompt template management system | 06 §5.1 | M | — | Templates loaded, rendered, validated |
| 2.T3 | Context-aware question refiner | 06 §3.2 | L | 1.T5, 2.T1, 2.T2 | Questions enhanced with artifact context |
| 2.T4 | Artifact synthesizer | 06 §3.3 | L | 2.T1, 2.T2 | Raw answers → richer artifact text |
| 2.T5 | Quality scorer (answer + session level) | 06 §3.5 | M | 2.T1, 2.T2 | Scores 0-1 with dimension breakdown |
| 2.T6 | Specification generator | 06 §3.4 | XL | 2.T4, 2.T2 | Produces coherent multi-section spec doc |
| 2.T7 | Adaptive question generator | 06 §3.6 | L | 2.T5 | Generates follow-up probes for weak areas |
| 2.T8 | LLM error handling and fallback | 06 §7 | M | 2.T1 | Graceful degradation to template mode |
| 2.T9 | Integration tests with mock LLM | — | M | 2.T1–2.T8 | All integrations tested without real API |
| 2.T10 | Manual QA with real LLM API | — | L | 2.T9 | Specification quality human-approved |

---

## Task Details

#### 2.T1: LLM Provider Abstraction

**What:**
Create `LLMProvider` interface and four implementations: OpenAI (via `openai` npm package), Anthropic (via `@anthropic-ai/sdk`), Local (via `ollama` or `llama.cpp` HTTP), Null (no-op for offline mode).

**Files:**
- `src/llm/types.ts` — Interface definition
- `src/llm/providers/openai.ts`
- `src/llm/providers/anthropic.ts`
- `src/llm/providers/local.ts`
- `src/llm/providers/null.ts`
- `src/llm/factory.ts` — Provider factory from config

**Done When:**
- [ ] Each provider implements `complete()` with correct API calls
- [ ] `NullProvider` returns placeholder text
- [ ] Factory selects provider based on config
- [ ] Rate limit handling with exponential backoff

---

#### 2.T3: Context-Aware Question Refiner

**What:**
Implement the `QuestionRefiner` that takes a static question and accumulated artifacts, then produces a refined version using the LLM.

**Files:**
- `src/llm/refiners/question-refiner.ts`
- `tests/llm/refiners/question-refiner.test.ts`

**Implementation Notes:**
- Load system prompt from `prompts/question-refinement/system.md`
- Render user prompt with question text + artifact summary
- Parse LLM response into `RefinedQuestion` format
- Preserve original question ID and all choice IDs
- If LLM fails, return original question unchanged

**Done When:**
- [ ] Question text incorporates artifact context
- [ ] Choice options preserved (not hallucinated)
- [ ] Original question available as fallback
- [ ] Processing time <2s per question (with good connection)

---

#### 2.T6: Specification Generator

**What:**
The crown jewel — takes all session data and produces a polished, multi-section development specification document.

**Files:**
- `src/llm/generators/spec-generator.ts`
- `src/llm/generators/section-templates/` — Per-series templates
- `src/llm/generators/summary-template.md`
- `tests/llm/generators/spec-generator.test.ts`

**Implementation Notes:**
1. Generate table of contents from series structure
2. For each series, create a section:
   a. Summarize the series' purpose
   b. Narrative synthesis of all answers in that series
   c. Cross-reference to earlier/later series where relevant
   d. Include key decisions and their rationale
3. Generate executive summary from top-level artifacts
4. Score the specification for quality
5. Support partial generation (incomplete sessions)

**Done When:**
- [ ] Generated spec is coherent and readable
- [ ] All answered questions represented
- [ ] Cross-references between sections are correct
- [ ] Unanswered questions noted as gaps
- [ ] Executive summary accurately captures key decisions
- [ ] Output validated as valid Markdown

---

## Testing

- Mock LLM returns deterministic responses for all test scenarios
- Provider factory: each provider tested with mocked HTTP
- Refiner: artifact injection verified, fallback on error verified
- Generator: partial sessions produce partial specs without errors
- Quality scorer: same input → same score (deterministic at temp=0)

## Risks

- LLM hallucination in artifact synthesis — always preserve user's original answer alongside LLM output
- Token limits for long sessions — implement context windowing/chunking
- Cost management — track token usage per session, warn on high usage
