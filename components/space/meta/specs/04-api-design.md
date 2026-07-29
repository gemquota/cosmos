# 4: API Design Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `01-data-schema.md`, `02-architecture.md`

---

## 1. Purpose

Defines the CLI commands, programmatic API, and (future) HTTP endpoints for SPACE. Every capability is accessible via at least two interfaces: CLI for humans, API for programs.

## 2. Scope

- CLI command structure and behavior
- Programmatic TypeScript/JavaScript API
- HTTP REST API (Phase 5+ only)
- Configuration management
- Error handling conventions

---

## 3. Design

### 3.1 CLI Commands

```
space <command> [options]

Commands:
  init <name>        Create a new project
  list               List all projects
  run <project>      Start or resume a session
  status [project]   Show session status and progress
  export <project>   Export session to file(s)
  diff <a> <b>       Compare two sessions
  config             Manage SPACE configuration
  framework          Inspect the framework definition
  version            Show SPACE version

Global Options:
  --format, -f       Output format (json, md, yaml, prompt)
  --output, -o       Output directory or file
  --session, -s      Target specific session ID
  --verbose, -v      Enable verbose logging
  --quiet, -q        Suppress non-error output
  --help, -h         Show help
  --version, -V      Show version
```

#### Command Details

**`space init <name>`**
```
Creates a new project directory structure.

$ space init my-project
✓ Created project: my-project
  Location: ~/.space/projects/my-project/
  Framework: v2.0.0 (7 series, 326 probes)
  
  Next: space run my-project
```

File structure created:
```
~/.space/projects/my-project/
├── .space.json           # Project metadata
├── sessions/
│   └── <session-id>/     # Created on first run
│       ├── state.json    # Session state
│       ├── artifacts.json
│       └── snapshots/    # Auto-save checkpoints
├── exports/              # Generated exports
└── README.md             # Project description
```

**`space run <project>`**
```
Starts or resumes a session. Enters interactive question mode.

$ space run my-project
Starting session for "my-project"...

═══ Series 1: Conceptual Depth ═══ Round 1 of 3 ═══

Q 1.1.1 — What is the primary domain or field this project addresses?
  Write freely. Consider the landscape, key communities, and where boundaries lie.

> [type your answer, or press Enter to skip]

a) A single well-established domain
b) An interdisciplinary space spanning 2–3 domains  
c) An emerging or niche area with evolving terminology

Select (a/b/c): _

$ space run my-project --auto    # Non-interactive mode (LLM answers from prompt)
$ space run my-project --resume  # Resume from last question
```

**`space export <project>`**
```
$ space export my-project -f json -o ./output/
✓ Exported JSON: ./output/prompt-framework-specification.json (12.3 KB)

$ space export my-project -f md,prompt -o ./output/
✓ Exported Markdown: ./output/specification.md (28.7 KB)
✓ Exported Prompt: ./output/system-prompt.txt (4.1 KB)

$ space export my-project --session <id> -f json
✓ Exported session <id> to JSON
```

**`space diff <project-a> <project-b>`**
```
$ space diff project-alpha project-beta
Specification Diff: alpha → beta

Changed: 12 answers
Added: 3 answers (only in beta)
Removed: 1 answer (only in alpha)

Run with -f md for full diff report.
```

**`space config`**
```
$ space config
SPACE Configuration (~/.space/config.json)

  projects_dir:    ~/.space/projects/
  llm_provider:    openai
  llm_model:       gpt-4o
  auto_save:       true (10s interval)
  adaptive:        true
  quality_scoring: true

$ space config set llm_model gpt-4o-mini
✓ Updated llm_model: gpt-4o → gpt-4o-mini

$ space config get llm_provider
openai
```

### 3.2 Programmatic API

```typescript
import { createSpace } from '@space/core';

const space = createSpace({
  projects_dir: './projects',
  llm_provider: 'openai',
  llm_model: 'gpt-4o',
});

// Create project
const project = await space.initProject('my-app', {
  description: 'A recommendation engine'
});

// Start session
const session = await space.startSession(project.id);

// Get first question
const q = await space.getCurrentQuestion(session.id);
console.log(q.text);  // "What is the primary domain..."
console.log(q.choices); // [{ id: "1.1.1.a", text: "..." }, ...]

// Submit answer
await space.submitAnswer(session.id, '1.1.1', {
  open_ended: 'Machine learning recommendation systems',
  choice_id: '1.1.1.a'
});

// Check artifacts
const artifacts = await space.getArtifacts(session.id);
console.log(artifacts.domain); // { value: "machine learning...", ... }

// Export
const md = await space.exportSession(session.id, 'markdown');
console.log(md.content); // Full markdown specification

// Subscribe to events
const unsub = space.on('series:completed', (event) => {
  console.log(`Series ${event.series_id} done!`);
});
```

### 3.3 HTTP REST API (Phase 5+)

```
Base URL: http://localhost:3847/api/v1

GET    /projects                  List projects
POST   /projects                  Create project
GET    /projects/:id              Get project
DELETE /projects/:id              Delete project

POST   /projects/:id/sessions     Start session
GET    /sessions/:id              Get session state
POST   /sessions/:id/resume       Resume session
GET    /sessions/:id/status       Get status

GET    /sessions/:id/question     Get current question
POST   /sessions/:id/answer       Submit answer
POST   /sessions/:id/skip         Skip question

GET    /sessions/:id/artifacts    Get artifact dictionary
GET    /sessions/:id/progress     Get progress

POST   /sessions/:id/export       Generate export
GET    /sessions/:id/export/:fmt  Download export

WebSocket: ws://localhost:3847/api/v1/sessions/:id/events
  → Real-time event stream
```

---

## 5. Interfaces

### 5.1 Error Handling

All errors follow a structured format:

```typescript
interface SpaceError {
  code: string;           // e.g. "SESSION_NOT_FOUND"
  message: string;        // human-readable
  details?: any;          // additional context
  recovery?: string;      // suggested fix
}

// CLI renders as:
// ✗ Error: Session not found (SESSION_NOT_FOUND)
//   Session abc-123 does not exist in project "my-app"
//   Recovery: Run `space list` to see available sessions
```

Error codes:
| Code | HTTP | Description |
|------|:----:|-------------|
| `FRAMEWORK_NOT_FOUND` | 500 | Framework definition files missing |
| `FRAMEWORK_INVALID` | 500 | Framework JSON validation failed |
| `PROJECT_NOT_FOUND` | 404 | Project directory doesn't exist |
| `PROJECT_EXISTS` | 409 | Project already exists at path |
| `SESSION_NOT_FOUND` | 404 | Session ID not found |
| `SESSION_COMPLETED` | 400 | Session already completed |
| `SESSION_LOCKED` | 409 | Session open in another process |
| `QUESTION_NOT_FOUND` | 404 | Question ID doesn't exist |
| `DEPENDENCY_BLOCKED` | 409 | Series blocked by prerequisite |
| `ANSWER_INVALID` | 400 | Answer doesn't meet validation rules |
| `LLM_UNAVAILABLE` | 503 | LLM provider not reachable |
| `EXPORT_FAILED` | 500 | Export generation failed |
| `STORAGE_ERROR` | 500 | File system or DB error |

---

## 6. Data Model

Refer to `01-data-schema.md` for all request/response types.

---

## 7. Edge Cases

- **`space run` with no existing session:** Auto-creates one
- **`space export` with no answers:** Produces empty template export
- **`space diff` with different framework versions:** Warning + best-effort alignment by question ID
- **`space config` with invalid values:** Rejects with validation error before writing

---

## 8. Testing Strategy

- CLI integration tests for every command (happy path + error paths)
- API contract tests against OpenAPI schema
- Error message formatting tests (code, message, recovery all present)
- Config loading precedence: CLI flags > env vars > config file > defaults

---

## 9. Open Questions

- Should `space run` use readline/TUI library or plain stdin?
- Should HTTP API use REST or tRPC?
- Do we need authentication for the HTTP API?

---

## 10. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
