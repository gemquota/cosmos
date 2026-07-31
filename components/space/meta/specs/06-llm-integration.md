# 6: LLM Integration Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `05-execution-engine.md`

---

## 1. Purpose

Defines how SPACE integrates large language models to dynamically refine questions, synthesize artifacts, score quality, and generate polished specifications. This transforms a static questionnaire into an intelligent elicitation system.

## 2. Scope

- Context-aware question refinement
- Artifact synthesis from answers
- Final specification generation
- Quality scoring and coherence checking
- Adaptive question generation
- LLM provider abstraction

---

## 3. Design

### 3.1 LLM Integration Points

```
┌─────────────────────────────────────────────────────┐
│                  SPACE ENGINE                        │
│                                                      │
│  Question    ──── [1] ──→  LLM  ──→  Refined Q      │
│  Router            context        question text      │
│                                                      │
│  Artifact    ──── [2] ──→  LLM  ──→  Synthesized    │
│  Builder          answers        artifact text       │
│                                                      │
│  Export      ──── [3] ──→  LLM  ──→  Polished       │
│  Pipeline        artifacts       specification      │
│                                                      │
│  Quality     ──── [4] ──→  LLM  ──→  Score +        │
│  Checker         answers +       feedback            │
│                  artifacts                           │
└─────────────────────────────────────────────────────┘
```

### 3.2 Integration [1]: Context-Aware Question Refinement

Original questions are static strings. SPACE enhances them by injecting accumulated context:

**Before (static):**
> "What are the primary entities that exist in this domain?"

**After (context-refined, given `domain="NLP recommendation systems"`, `audience="practitioners"`):**
> "For your NLP recommendation system domain, what are the primary entities (models, data sources, user segments, etc.) that exist? Since you're working at the practitioner level, you can reference specific ML concepts directly."

```typescript
interface QuestionRefiner {
  refine(
    question: OpenEndedQuestion,
    artifacts: ArtifactDictionary,
    series_context: SeriesContext
  ): Promise<RefinedQuestion>;
}

interface RefinedQuestion {
  id: string;                        // original ID preserved
  refined_text: string;              // LLM-enhanced question text
  refined_choices: MultiChoice[];    // possibly enhanced choices
  context_injected: string[];        // which artifacts were used
  confidence: number;                // how much the refinement helped
  original_text: string;             // preserved for reference
}
```

**Refinement strategies:**

| Strategy | When | Model Cost |
|----------|------|:----------:|
| `none` | LLM unavailable or user preference | Zero |
| `template` | Always — deterministic, no LLM | Zero |
| `llm_contextual` | Default — inject artifacts into question text | Low |
| `llm_expand` | Adaptive mode — generate follow-up probes | Medium |

### 3.3 Integration [2]: Artifact Synthesis

After each round completes, the LLM synthesizes a richer artifact from raw answers:

```typescript
interface ArtifactSynthesizer {
  synthesize(
    question: OpenEndedQuestion,
    open_ended_answer: string,
    selected_choice: MultiChoice,
    prior_artifacts: ArtifactDictionary,
    series_context: SeriesContext
  ): Promise<ArtifactValue>;
}
```

**Synthesis prompt template:**

```
You are a specification synthesizer. Given a user's answer to a scoping question,
extract and structure the key information.

Question: {question.text}
Open-ended answer: {answer.open_ended}
Selected choice: {choice.text}
Prior context: {prior_artifacts_summary}

Extract the key decisions and facts. Return a structured summary.
```

### 3.4 Integration [3]: Specification Generation

After all 326 probes are answered (or at any point for partial export), the LLM generates a polished specification:

```typescript
interface SpecificationGenerator {
  generate(
    session: SessionState,
    artifacts: ArtifactDictionary,
    format: 'full' | 'executive_summary' | 'technical_deep_dive'
  ): Promise<GeneratedSpec>;
}

interface GeneratedSpec {
  content: string;
  sections: SpecSection[];
  quality_score: number;
  word_count: number;
  generation_time_ms: number;
  model_used: string;
}
```

**Generation strategy:**
1. Load all artifacts and answers
2. Generate table of contents from series structure
3. For each series, synthesize a narrative section
4. Cross-reference between sections (e.g., "As established in Series 1...")
5. Generate executive summary from all artifacts
6. Score the specification for completeness and coherence

### 3.5 Integration [4]: Quality Scoring

```typescript
interface QualityScorer {
  scoreAnswer(
    question: OpenEndedQuestion,
    answer: AnswerEntry,
    context: ArtifactDictionary
  ): Promise<QualityResult>;
  
  scoreSession(session: SessionState): Promise<SessionQualityResult>;
}

interface QualityResult {
  score: number;                    // 0-1
  dimensions: {
    completeness: number;           // how thoroughly answered
    specificity: number;            // concrete vs vague
    consistency: number;            // aligned with prior answers
    actionability: number;          // useful for specification building
  };
  suggestions: string[];            // improvement hints
}

interface SessionQualityResult {
  overall_score: number;
  per_series: { series_id: number; score: number }[];
  weak_areas: string[];             // question IDs with low scores
  contradictions: Contradiction[];  // detected conflicts
}
```

### 3.6 Integration [5]: Adaptive Question Generation

Beyond the fixed 326 probes, SPACE can generate additional questions:

```typescript
interface AdaptiveQuestionGenerator {
  analyze(
    session: SessionState,
    artifacts: ArtifactDictionary
  ): Promise<AdaptiveProbe[]>;
}

interface AdaptiveProbe {
  question: OpenEndedQuestion;
  reason: string;                   // why this probe was generated
  priority: 'low' | 'medium' | 'high';
  source_gap: string;               // which artifact is under-defined
}
```

**Triggers for adaptive questions:**
- Artifact has low confidence (<0.5)
- Two answers appear contradictory
- A critical artifact is still null after its series completes
- Domain complexity suggests the fixed question set was insufficient

### 3.7 Provider Abstraction

```typescript
interface LLMProvider {
  name: string;
  
  complete(params: CompletionParams): Promise<CompletionResult>;
  
  isAvailable(): Promise<boolean>;
  getRateLimitInfo(): Promise<RateLimitInfo>;
}

interface CompletionParams {
  system_prompt: string;
  user_prompt: string;
  temperature?: number;             // default from config
  max_tokens?: number;              // default from config
  response_format?: 'text' | 'json';
}

interface CompletionResult {
  text: string;
  tokens_used: { prompt: number; completion: number };
  model: string;
  latency_ms: number;
}

// Built-in providers:
class OpenAIProvider implements LLMProvider { ... }
class AnthropicProvider implements LLMProvider { ... }
class LocalProvider implements LLMProvider { ... }   // Ollama, llama.cpp
class NullProvider implements LLMProvider { ... }    // No-op, for offline mode
```

---

## 5. Interfaces

### 5.1 Prompt Management

Prompts are versioned and stored as templates:

```
prompts/
├── question-refinement/
│   ├── system.md
│   └── user-template.md
├── artifact-synthesis/
│   ├── system.md
│   └── user-template.md
├── specification-generation/
│   ├── system.md
│   ├── section-template.md
│   └── summary-template.md
├── quality-scoring/
│   ├── system.md
│   └── scoring-rubric.md
└── adaptive-probes/
    ├── system.md
    └── gap-analysis-template.md
```

---

## 6. Edge Cases

- **LLM returns malformed JSON:** Retry up to 3 times with temperature reduction; fallback to template
- **Token limit exceeded:** Chunk long contexts; summarize prior artifacts if needed
- **Rate limiting:** Queue and retry with exponential backoff
- **LLM disagrees with user's explicit choice:** User answer always wins; LLM refinement is additive only
- **Offline mode:** All LLM integrations gracefully degrade to template/static behavior

---

## 7. Testing Strategy

- Unit tests for each integration point with mocked LLM responses
- Prompt template rendering tests (no missing variables)
- Quality score consistency: same input → same score (deterministic at temperature=0)
- Integration tests with real LLM API (gated, not in CI)
- A/B test: static questions vs refined questions → measure spec quality

---

## 8. Open Questions

- Should we support multi-model chains (e.g., fast model for scoring, powerful for synthesis)?
- How to handle LLM hallucination in artifact synthesis?
- Should adaptive questions be visible to the user or transparent?
- Cost budget: should SPACE track and limit LLM API costs per session?

---

## 9. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
