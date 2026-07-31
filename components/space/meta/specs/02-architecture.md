# 2: System Architecture Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `01-data-schema.md`

---

## 1. Purpose

Defines the overall system architecture for SPACE — how components communicate, what each layer is responsible for, and how the system scales from CLI tool to multi-user service.

## 2. Scope

- Layered architecture and component responsibilities
- Module boundaries and dependency direction
- Configuration and dependency injection
- Template interpolation for MD specs

Out of scope: API wire format (see `04-api-design.md`), persistence internals (see `08-persistence.md`).

## 3. Background / Context

The original framework is a monolithic React app with data hardcoded in JSON imports. SPACE decomposes this into layered modules with clean interfaces between them.

### 3.1 Template Variable Interpolation (Audit Fix #4, #8)

The original MD files contain unresolved template variables:

```markdown
Context from Series 1: domain=`{domain}`, audience_level=`{audience_level}`
```

SPACE implements a **context injection pipeline** that resolves these at generation time:

```
Artifacts: { domain: "machine learning", audience_level: "practitioners" }
    ↓
Template: "Context from Series 1: domain=`{domain}`, audience_level=`{audience_level}`"
    ↓
Resolved: "Context from Series 1: domain=`machine learning`, audience_level=`practitioners`"
```

---

## 4. Design

### 4.1 Layered Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │
│  │  Web UI  │  │  TUI     │  │  CLI (command-line)  │   │
│  └────┬─────┘  └────┬─────┘  └──────────┬───────────┘   │
│       │              │                    │                │
├───────┴──────────────┴────────────────────┴───────────────┤
│                     API LAYER                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  Core API (programmatic interface)                   │ │
│  │  - init, run, resume, export, status, list, delete   │ │
│  └──────────────────────┬───────────────────────────────┘ │
├─────────────────────────┴─────────────────────────────────┤
│                   ENGINE LAYER                            │
│  ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌───────────┐ │
│  │ Session  │ │ Dependency │ │ Artifact │ │ Validator │ │
│  │ Manager  │ │ Resolver   │ │ Builder  │ │           │ │
│  └──────────┘ └────────────┘ └──────────┘ └───────────┘ │
│  ┌──────────┐ ┌────────────┐ ┌──────────┐               │
│  │ Question │ │ LLM Engine │ │ Synth    │               │
│  │ Router   │ │            │ │ Engine   │               │
│  └──────────┘ └────────────┘ └──────────┘               │
├──────────────────────────────────────────────────────────┤
│                    DATA LAYER                             │
│  ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌───────────┐ │
│  │ Schema   │ │ Template   │ │ Storage  │ │ Export    │ │
│  │ Loader   │ │ Resolver   │ │ Provider │ │ Pipeline  │ │
│  └──────────┘ └────────────┘ └──────────┘ └───────────┘ │
└──────────────────────────────────────────────────────────┘
```

### 4.2 Module Map

| Module | Layer | Responsibility | Key Types |
|--------|:-----:|----------------|-----------|
| `schema-loader` | Data | Parse + validate framework JSON, migrate v1→v2 | `FrameworkDefinition` |
| `template-resolver` | Data | Resolve `{artifact}` placeholders in text | — |
| `storage-provider` | Data | Read/write projects, sessions, snapshots | `Project`, `SessionState` |
| `export-pipeline` | Data | Generate output in multiple formats | — |
| `session-manager` | Engine | Create, resume, pause, complete sessions | `SessionState` |
| `dependency-resolver` | Engine | Compute available series from DAG | `DependencyGraph` |
| `artifact-builder` | Engine | Accumulate answers into artifact dictionary | `ArtifactDictionary` |
| `validator` | Engine | Check answer completeness and quality | — |
| `question-router` | Engine | Determine next question, handle adaptive flow | — |
| `llm-engine` | Engine | LLM calls for refinement and synthesis | — |
| `synth-engine` | Engine | Assemble final specification from artifacts | — |
| `core-api` | API | Public programmatic interface | — |
| `web-ui` | Presentation | React-based browser interface | — |
| `tui` | Presentation | Terminal-based interface | — |
| `cli` | Presentation | Command-line entry points | — |

### 4.3 Dependency Direction

```
cli / web-ui / tui  →  core-api  →  engine-layer  →  data-layer
```

- Presentation depends on API, never on Engine or Data directly
- Engine depends on Data, never on Presentation
- Data depends on nothing (leaf modules)
- All inter-module communication uses interfaces, not concrete types

### 4.4 Configuration

```typescript
interface SpaceConfig {
  // Paths
  projects_dir: string;            // default: ~/.space/projects/
  framework_dir: string;           // default: bundled framework JSON
  
  // LLM
  llm_provider: 'openai' | 'anthropic' | 'local' | 'none';
  llm_model: string;              // e.g. "gpt-4o"
  llm_api_key?: string;           // from env if not set
  llm_temperature?: number;       // default: 0.7
  llm_max_tokens?: number;        // default: 4096
  
  // Engine
  enable_adaptive_questions: boolean;  // default: true
  enable_quality_scoring: boolean;     // default: true
  auto_save_interval_ms: number;       // default: 10000
  
  // Export
  default_export_format: 'json' | 'markdown' | 'yaml' | 'prompt';
  export_include_metadata: boolean;    // default: true
}
```

### 4.5 Event System

Components communicate through a typed event bus for decoupled notifications:

```typescript
type SpaceEvent =
  | { type: 'session:created'; session_id: string }
  | { type: 'session:resumed'; session_id: string }
  | { type: 'answer:submitted'; question_id: string; series_id: number }
  | { type: 'round:completed'; series_id: number; round: number }
  | { type: 'series:completed'; series_id: number }
  | { type: 'session:completed'; session_id: string }
  | { type: 'artifact:updated'; artifact_key: string; value: any }
  | { type: 'export:generated'; format: string; path: string }
  | { type: 'llm:refinement_complete'; question_id: string }
  | { type: 'error'; code: string; message: string };
```

---

## 5. Interfaces

### 5.1 Core API Surface

```typescript
interface SpaceAPI {
  // Project lifecycle
  initProject(name: string, opts?: InitOptions): Promise<Project>;
  listProjects(): Promise<Project[]>;
  deleteProject(project_id: string): Promise<void>;
  
  // Session lifecycle
  startSession(project_id: string): Promise<SessionState>;
  resumeSession(session_id: string): Promise<SessionState>;
  getSessionStatus(session_id: string): Promise<SessionStatus>;
  
  // Question flow
  getCurrentQuestion(session_id: string): Promise<QuestionContext>;
  submitAnswer(session_id: string, question_id: string, answer: AnswerInput): Promise<void>;
  skipQuestion(session_id: string, question_id: string, reason: string): Promise<void>;
  
  // Artifacts & progress
  getArtifacts(session_id: string): Promise<ArtifactDictionary>;
  getProgress(session_id: string): Promise<ProgressState>;
  
  // Export
  exportSession(session_id: string, format: ExportFormat): Promise<ExportResult>;
  
  // Events
  on(event: SpaceEvent['type'], handler: (event: SpaceEvent) => void): Unsubscribe;
}
```

---

## 6. Data Model

Refer to `01-data-schema.md` for all type definitions.

---

## 7. Edge Cases

- **Framework file missing:** Graceful error with instructions to re-download
- **Corrupted session on resume:** Auto-repair from last valid snapshot
- **LLM unavailable:** Degrade to static question mode (original behavior)
- **Concurrent session access:** File-level locking per project; warn on multi-instance

---

## 8. Testing Strategy

- Module integration tests for each layer boundary
- Contract tests for API surface (all methods return expected types)
- Event bus delivers all events to all subscribers
- Configuration loading from file, env vars, and defaults
- Template resolver handles missing, circular, and malformed templates

---

## 9. Open Questions

- Should the event bus support async handlers or only sync?
- Do we need a plugin system for custom question types?
- Future: Should the architecture support remote execution (client-server)?

---

## 10. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
