# 1: Data Schema Specification

**Status:** Draft
**Version:** 2.0.0
**Created:** 2026-07-25
**Depends On:** Original `framework.json` v1.0.0

---

## 1. Purpose

Defines the canonical data model for SPACE. Every component — engine, UI, export, LLM — reads and writes through these types. Schema v2 extends v1 with session management, artifact tracking, and LLM metadata while maintaining backward compatibility.

## 2. Scope

- Framework definition schema (series, rounds, questions)
- Session state schema (answers, progress, artifacts)
- Project schema (multi-session containers)
- Export format schemas (JSON v2, Markdown, YAML, Prompt)

Out of scope: database storage format, API wire format (see `04-api-design.md`).

## 3. Background / Context

The original framework uses two parallel data representations:
- `framework.json` — master metadata with dependency graph
- `json/01-07-*.json` — per-series question definitions

Schema v2 consolidates these into a single importable format and adds runtime state types.

---

## 4. Design

### 4.1 Schema Layers

```
┌─────────────────────────────────────────────┐
│  Layer 3: Export Schemas                     │
│  (JSON v2, Markdown, YAML, Prompt Template)  │
├─────────────────────────────────────────────┤
│  Layer 2: Session State Schema               │
│  (answers, progress, artifacts, metadata)    │
├─────────────────────────────────────────────┤
│  Layer 1: Framework Definition Schema        │
│  (series, rounds, questions, dependencies)   │
└─────────────────────────────────────────────┘
```

### 4.2 Version Compatibility

| Schema Version | Format | Backward Compat |
|:--------------:|--------|:---------------:|
| v1 | Original `json/*.json` + `framework.json` | — |
| v2 | Unified SPACE format | Reads v1; writes v2 |
| v3 (future) | TBD | Reads v1+v2; writes v3 |

---

## 5. Interfaces

### 5.1 Framework Definition Schema (`FrameworkDefinition`)

```typescript
interface FrameworkDefinition {
  meta: FrameworkMeta;
  dependency_graph: DependencyGraph;
  series: SeriesDefinition[];
}

interface FrameworkMeta {
  name: string;                    // "Structured Prompt Creation Framework"
  version: string;                 // semver
  description: string;
  total_series: number;            // 7
  total_rounds: number;            // 25
  total_open_ended: number;        // 67
  total_multi_choice: number;      // 259
  estimated_completion_minutes: [number, number]; // [min, max]
}

interface DependencyGraph {
  nodes: DependencyNode[];
  edges: DependencyEdge[];
}

interface DependencyNode {
  series_id: number;               // 1-7
  name: string;
  provides: string[];              // artifact keys this series produces
}

interface DependencyEdge {
  from: number;                    // series_id
  to: number;                      // series_id
  artifacts: string[];             // artifact keys transferred
}

interface SeriesDefinition {
  id: number;                      // 1-7
  name: string;
  description: string;
  depends_on: number[];            // prerequisite series IDs
  consumes: string[];              // artifact keys consumed
  provides: string[];              // artifact keys produced
  rounds: RoundDefinition[];
}

interface RoundDefinition {
  round: number;                   // 1-indexed within series
  focus: string;                   // round title
  open_ended: OpenEndedQuestion[];
}

interface OpenEndedQuestion {
  id: string;                      // e.g. "2.1.1" — series.round.question
  text: string;                    // question prompt
  context_template?: string;       // optional template with {artifact} refs
  follow_up_choices: MultiChoice[];
}

interface MultiChoice {
  id: string;                      // e.g. "2.1.1.a"
  text: string;                    // choice description
  weight?: number;                 // optional importance weight (0-1)
}
```

### 5.2 Session State Schema (`SessionState`)

```typescript
interface SessionState {
  session: SessionMeta;
  answers: Record<string, AnswerEntry>;
  progress: ProgressState;
  artifacts: ArtifactDictionary;
  llm_metadata?: LLMMetadata;
}

interface SessionMeta {
  id: string;                      // UUID
  project_id: string;              // parent project
  framework_version: string;       // schema version used
  created_at: string;              // ISO 8601
  updated_at: string;
  status: 'created' | 'in_progress' | 'completed' | 'abandoned';
  estimated_completion_pct: number; // 0-100
  total_time_ms: number;           // active time
}

interface AnswerEntry {
  question_id: string;             // e.g. "2.1.1"
  series_id: number;
  round: number;
  open_ended_text: string;
  multi_choice_id?: string;        // selected choice ID
  multi_choice_text?: string;      // resolved choice text
  answered_at: string;             // ISO 8601
  edit_count: number;
  llm_refined?: string;            // LLM-improved version of answer
  quality_score?: number;          // 0-1, computed by intelligence layer
}

interface ProgressState {
  completed_rounds: string[];      // ["1-1", "1-2", "1-3", ...]
  completed_series: number[];      // [1, 2] if all rounds done
  current_series: number | null;
  current_round: number | null;
  last_question_id?: string;       // for resume
  blocked_on?: string[];           // series IDs blocked by dependencies
}

type ArtifactDictionary = Record<string, ArtifactValue>;

interface ArtifactValue {
  value: any;                      // accumulated from answers
  source_question_id: string;      // which question produced this
  source_series_id: number;
  confidence: number;              // 0-1, based on answer quality
  last_updated: string;
  derived_from?: string[];         // upstream artifact keys
}
```

### 5.3 Project Schema (`Project`)

```typescript
interface Project {
  id: string;                      // UUID
  name: string;
  description: string;
  created_at: string;
  updated_at: string;
  framework_version: string;
  sessions: SessionSummary[];
  active_session_id?: string;
  tags: string[];
}

interface SessionSummary {
  session_id: string;
  status: SessionMeta['status'];
  completion_pct: number;
  created_at: string;
  updated_at: string;
}
```

---

## 6. Data Model

### 6.1 Migration: v1 → v2

The migration function converts original framework files:

```
Input (v1):
  framework.json                  → FrameworkDefinition.meta + dependency_graph
  json/01-conceptual-depth.json   → FrameworkDefinition.series[0]
  json/02-*.json                  → FrameworkDefinition.series[1]
  ...                             → ...

Output (v2):
  framework-v2.json               → single FrameworkDefinition file
```

Key transformations:
- `dependency_chain.edges` → `DependencyGraph.edges`
- Individual `series.provides` + `series.consumes` → `DependencyNode.provides` + `DependencyEdge.artifacts`
- `series.rounds[].open_ended[].id` preserved as-is
- `meta.total_open_ended_questions` → `meta.total_open_ended`
- `estimated_completion_time` string → `estimated_completion_minutes` tuple

### 6.2 Validation Rules

| Rule | Description |
|------|-------------|
| R1 | Every `question_id` is unique across all series |
| R2 | Every `multi_choice.id` starts with its parent `question_id` |
| R3 | Dependency graph is acyclic (topological sort exists) |
| R4 | Every series in `depends_on` has a lower ID than the dependent |
| R5 | Every artifact in `consumes` is provided by at least one dependency |
| R6 | `total_rounds` = sum of all `series.rounds.length` |
| R7 | `total_open_ended` = sum of all `round.open_ended.length` |
| R8 | `total_multi_choice` = sum of all `round.open_ended[].follow_up_choices.length` |

---

## 7. Edge Cases

- **v1 files without `consumes`/`provides`:** Infer from `framework.json` dependency_chain.edges
- **Questions added/removed mid-session:** Schema supports partial completion; new questions get `null` answers
- **Corrupted session file:** Checkpoint system saves snapshots; latest valid snapshot wins

---

## 8. Testing Strategy

- JSON Schema validation of all framework definition files
- Round-trip test: v1 → v2 → v1 produces equivalent content
- Session state serialization/deserialization with property-based tests
- Dependency graph cycle detection with fuzz testing

---

## 9. Open Questions

- Should `weight` on MultiChoice be per-choice or per-question?
- Should session state support undo/redo history stack?
- Future: Should schema support conditional questions (skip based on prior answers)?

---

## 10. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
