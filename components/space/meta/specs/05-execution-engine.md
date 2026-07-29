# 5: Execution Engine Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `01-data-schema.md`, `02-architecture.md`

---

## 1. Purpose

Defines the core run-time engine that orchestrates the entire elicitation flow — from session creation through question routing, answer processing, artifact accumulation, and session completion. This is the heart of SPACE.

## 2. Scope

- Session lifecycle management
- Series/round/question state machine
- Artifact accumulation pipeline
- Dependency resolution and series gating
- Answer validation
- Progress tracking and metrics
- Auto-save and recovery

---

## 3. Design

### 3.1 Session Lifecycle State Machine

```
                    ┌──────────┐
                    │ CREATED  │
                    └────┬─────┘
                         │ start()
                         ▼
                    ┌──────────┐
              ┌─────│ RUNNING  │◄────────┐
              │     └────┬─────┘         │
              │          │               │
         pause()│    resume()        submit_answer()
              │          │               │
              ▼          │               │
        ┌──────────┐     │               │
        │ PAUSED   │─────┘               │
        └──────────┘                     │
              │                          │
         resume()                        │
              │                          │
              └──────────────────────────┘
                         │
                    complete()
                         ▼
                    ┌──────────┐
                    │COMPLETED │
                    └──────────┘
                         │
                    export()
                         ▼
                   [export data]
```

### 3.2 Series State Machine

Each series follows this progression:

```
LOCKED → AVAILABLE → IN_PROGRESS → COMPLETED
  │          │            │              │
  │     deps met?     has answers?   all rounds done?
  │          │            │              │
  └──no──────┘            └──yes────────┘
```

**Locking rules (fixes audit issue #6):**
- A series is **LOCKED** if ANY of its `depends_on` series has at least one round incomplete
- A series becomes **AVAILABLE** only when ALL dependency series have ALL rounds completed
- This is stricter than the original app (which only checked the last round)

### 3.3 Round State Machine

```
AVAILABLE → IN_PROGRESS → COMPLETED
     │           │              │
     │     has any answer?   all OEs answered
     │     (auto-transition)  (auto-transition)
```

### 3.4 Question Routing Flow

```
space.run(project)
    │
    ├─ Is session new? → Load framework → Create session → Start
    │
    ├─ Find next question:
    │   ├─ current_series available? → Find next round
    │   │   ├─ current_round incomplete? → Return next unanswered OE
    │   │   └─ current_round complete? → Advance to next round
    │   ├─ current_round complete AND more rounds? → Next round
    │   └─ all rounds complete? → Mark series complete → Next series
    │
    ├─ All series complete? → Mark session complete
    │
    └─ Return QuestionContext to caller
```

### 3.5 Artifact Accumulation

When a round is completed, the engine extracts artifacts from answers:

```typescript
function accumulateArtifacts(
  session: SessionState,
  series_id: number,
  round: number
): ArtifactDictionary {
  const series = framework.series.find(s => s.id === series_id);
  const round_def = series.rounds.find(r => r.round === round);
  
  // For each artifact this series produces:
  for (const artifact_key of series.provides) {
    // Find the question(s) that best map to this artifact
    const mapping = ARTIFACT_MAPPING[artifact_key];
    const answer = session.answers[mapping.question_id];
    
    session.artifacts[artifact_key] = {
      value: mapping.extractor(answer),  // function to pull value from answer
      source_question_id: mapping.question_id,
      source_series_id: series_id,
      confidence: computeConfidence(answer),
      last_updated: new Date().toISOString(),
      derived_from: mapping.dependencies,
    };
  }
  
  return session.artifacts;
}
```

**Artifact Mapping Registry:**

| Artifact Key | Source Question | Extractor | Dependencies |
|-------------|----------------|-----------|:------------:|
| `domain` | 1.1.1 | open_ended text | — |
| `audience_level` | 1.1.2 | choice text | — |
| `terminology_preferences` | 1.3.1 | choice text | — |
| `scaffolding_preference` | 1.3.2 | choice text | — |
| `entity_list` | 2.1.1 | open_ended text (parsed) | — |
| `entity_attributes` | 2.1.2 | open_ended text (parsed) | entity_list |
| `entity_categories` | 2.1.3 | choice text | entity_list |
| `entity_hierarchy` | 2.3.3 | choice text | entity_list |
| `entity_constraints` | 2.4.3 | choice text | entity_list |
| `relationship_graph` | 3.1.1 | open_ended text (parsed) | entity_list |
| `hierarchy_structure` | 3.2.1 | choice text | entity_list |
| `dependency_chains` | 3.3.2 | choice text | entity_list |
| `composition_rules` | 3.4.2 | choice text | entity_list |
| `procedure_steps` | 4.1.2 | choice text | entity_list, relationship_graph |
| `decision_points` | 4.2.1 | open_ended text | procedure_steps |
| `branching_complexity` | 4.2.1 | choice text | procedure_steps |
| `io_contracts` | 4.2.2 | choice text | procedure_steps |
| `hardware_requirements` | 5.1.x | combined | domain |
| `software_stack` | 5.2.x | combined | domain |
| `performance_targets` | 5.3.x | combined | — |
| `integration_contracts` | 5.4.x | combined | — |
| `timeline` | 5.4.3 | choice text | — |
| `development_cadence` | 6.1.1 | choice text | procedure_steps, tech_stack |
| `quality_practices` | 6.2.1 | choice text | — |
| `team_composition` | 6.1.2 | choice text | — |
| `communication_patterns` | 6.3.1 | choice text | — |
| `deployment_strategy` | 7.1.1 | choice text | tech_stack |
| `runtime_configuration` | 7.2.2 | choice text | tech_stack |
| `monitoring_plan` | 7.2.1 | choice text | — |
| `maintenance_policy` | 7.3.1 | choice text | — |

### 3.6 Answer Validation

Answers pass through a validation pipeline before being accepted:

```typescript
interface AnswerValidator {
  validate(answer: AnswerInput, question: OpenEndedQuestion): ValidationResult;
}

class DefaultValidator implements AnswerValidator {
  validate(answer, question) {
    const errors: string[] = [];
    
    // Open-ended: must have text
    if (!answer.open_ended?.trim()) {
      errors.push('Open-ended answer cannot be empty');
    }
    
    // Multi-choice: must select one of the valid choices
    if (!answer.choice_id) {
      errors.push('Must select a multiple-choice option');
    } else if (!question.follow_up_choices.find(c => c.id === answer.choice_id)) {
      errors.push(`Invalid choice ID: ${answer.choice_id}`);
    }
    
    // Length warnings
    if (answer.open_ended && answer.open_ended.length < 20) {
      errors.push('Consider providing more detail (currently <20 chars)');
    }
    
    return { valid: errors.length === 0, errors, warnings: [] };
  }
}
```

### 3.7 Progress Metrics

```typescript
interface ProgressMetrics {
  session_id: string;
  overall: {
    total_questions: number;         // 326
    answered: number;
    completion_pct: number;          // 0-100
  };
  by_series: {
    series_id: number;
    name: string;
    total_rounds: number;
    completed_rounds: number;
    total_questions: number;
    answered: number;
    completion_pct: number;
    status: 'locked' | 'available' | 'in_progress' | 'completed';
  }[];
  timing: {
    started_at: string;
    last_activity_at: string;
    active_time_ms: number;
    estimated_remaining_ms: number;
    avg_time_per_question_ms: number;
  };
}
```

### 3.8 Auto-Save & Recovery

- State is persisted to `state.json` after every answer submission
- Snapshots are created at round completion and series completion
- On resume, engine loads latest valid snapshot
- Recovery checks: JSON validity, schema conformance, circular reference detection

---

## 4. Interfaces

```typescript
class ExecutionEngine {
  // Session management
  createSession(project_id: string): Promise<SessionState>;
  resumeSession(session_id: string): Promise<SessionState>;
  pauseSession(session_id: string): Promise<void>;
  completeSession(session_id: string): Promise<void>;
  
  // Question flow
  getCurrentQuestion(session_id: string): Promise<QuestionContext>;
  submitAnswer(session_id: string, question_id: string, answer: AnswerInput): Promise<SubmitResult>;
  skipQuestion(session_id: string, question_id: string, reason: string): Promise<void>;
  
  // Queries
  getProgress(session_id: string): Promise<ProgressMetrics>;
  getArtifacts(session_id: string): Promise<ArtifactDictionary>;
  getNextSeries(session_id: string): Promise<number | null>;
  isQuestionAnswered(session_id: string, question_id: string): Promise<boolean>;
  
  // Events
  on(event: string, handler: Function): () => void;
}

interface QuestionContext {
  question: OpenEndedQuestion;
  series_id: number;
  series_name: string;
  round: number;
  round_focus: string;
  total_rounds: number;
  context_template?: string;       // interpolated with current artifacts
  artifacts_used: string[];        // which artifacts were injected
}

interface SubmitResult {
  accepted: boolean;
  artifacts_updated: string[];     // which artifacts changed
  round_completed: boolean;        // was this the last question in the round?
  series_completed: boolean;       // was this the last round in the series?
  session_completed: boolean;      // was this the entire session?
  next_question?: QuestionContext;  // convenience: pre-fetched next question
}
```

---

## 5. Edge Cases

- **Session resume with corrupted state:** Load last valid snapshot, warn user
- **All questions in a round skipped:** Round still completes; artifacts get `null` values
- **Dependency cycle introduced by schema error:** Reject framework at load time
- **Answer submitted for locked series:** Reject with `DEPENDENCY_BLOCKED` error
- **Concurrent writes to same session:** File lock with timeout

---

## 6. Testing Strategy

- State machine tests: every valid transition, every invalid transition
- Artifact accumulation: mock answers → verify artifact dictionary
- Dependency resolver: DAG with various lock states
- Auto-save: kill process mid-answer → resume → verify state intact
- Performance: 326-question session completes in <500ms (no LLM)

---

## 7. Open Questions

- Should the engine support parallel question answering (multiple OEs simultaneously)?
- Should skipping produce a "skipped" artifact vs a `null` artifact?
- Future: Should the engine support branching (different question paths based on answers)?

---

## 8. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
