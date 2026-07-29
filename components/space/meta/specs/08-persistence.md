# 8: Persistence Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `01-data-schema.md`

---

## 1. Purpose

Defines how SPACE stores projects, sessions, artifacts, and snapshots. Replaces the original localStorage-only approach with a durable, multi-session, multi-project storage system.

## 2. Scope

- File-system project layout
- SQLite session database (optional)
- Session versioning and snapshots
- Import/export of project archives
- Git integration for spec versioning

---

## 3. Design

### 3.1 Directory Layout

```
~/.space/
├── config.json                   # SPACE configuration
├── framework/                    # Framework definition (read-only)
│   ├── framework-v2.json
│   ├── series/
│   │   ├── 01-conceptual-depth.json
│   │   ├── 02-ontological-characteristics.json
│   │   └── ... (7 files)
│   └── prompts/                  # LLM prompt templates
│       ├── question-refinement/
│       ├── artifact-synthesis/
│       └── specification-generation/
├── projects/                     # All projects
│   ├── <project-id>/
│   │   ├── .space.json           # Project metadata
│   │   ├── README.md             # Project description
│   │   ├── sessions/
│   │   │   ├── <session-id>/
│   │   │   │   ├── state.json    # Full session state
│   │   │   │   ├── artifacts.json
│   │   │   │   └── snapshots/
│   │   │   │       ├── round-1-1.json
│   │   │   │       ├── round-1-2.json
│   │   │   │       └── ...
│   │   │   └── <session-id>/     # Additional sessions
│   │   └── exports/
│   │       ├── v1/               # Timestamped export directories
│   │       │   ├── specification.json
│   │       │   ├── specification.md
│   │       │   └── system-prompt.txt
│   │       └── latest/           # Symlink to most recent export
│   └── <project-id>/
│       └── ...
└── db/
    └── space.db                  # Optional SQLite database
```

### 3.2 Project Metadata

```json
{
  "id": "proj_abc123",
  "name": "My Recommendation Engine",
  "description": "A collaborative filtering system for...",
  "created_at": "2026-07-25T12:00:00Z",
  "updated_at": "2026-07-25T15:30:00Z",
  "framework_version": "2.0.0",
  "tags": ["ml", "recommendation", "production"],
  "active_session_id": "sess_xyz789",
  "sessions": [
    {
      "id": "sess_xyz789",
      "status": "in_progress",
      "completion_pct": 45,
      "created_at": "2026-07-25T12:00:00Z",
      "updated_at": "2026-07-25T14:22:00Z"
    }
  ]
}
```

### 3.3 Snapshot System

Snapshots are taken at these points:
1. **Round completion** — after all questions in a round are answered
2. **Series completion** — after all rounds in a series are done
3. **Manual** — user triggers save

```typescript
interface Snapshot {
  id: string;
  session_id: string;
  created_at: string;
  trigger: 'round_complete' | 'series_complete' | 'manual' | 'auto';
  series_id: number;
  round: number;
  state: SessionState;               // full state at snapshot point
  size_bytes: number;
}
```

**Recovery flow:**
1. On session resume, load `state.json`
2. Validate JSON schema conformance
3. If invalid, find latest valid snapshot in `snapshots/`
4. Restore from snapshot, warn user about lost progress
5. Save recovered state as new `state.json`

### 3.4 SQLite Database (Optional)

For advanced use cases (analytics, cross-project queries):

```sql
CREATE TABLE projects (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  created_at TEXT,
  updated_at TEXT,
  framework_version TEXT
);

CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  project_id TEXT REFERENCES projects(id),
  status TEXT,
  completion_pct REAL,
  total_time_ms INTEGER,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE answers (
  session_id TEXT REFERENCES sessions(id),
  question_id TEXT,
  series_id INTEGER,
  round INTEGER,
  open_ended_text TEXT,
  multi_choice_id TEXT,
  answered_at TEXT,
  edit_count INTEGER,
  quality_score REAL,
  PRIMARY KEY (session_id, question_id)
);

CREATE TABLE artifacts (
  session_id TEXT REFERENCES sessions(id),
  key TEXT,
  value TEXT,                           -- JSON-serialized
  source_question_id TEXT,
  confidence REAL,
  updated_at TEXT,
  PRIMARY KEY (session_id, key)
);

CREATE TABLE snapshots (
  id TEXT PRIMARY KEY,
  session_id TEXT REFERENCES sessions(id),
  created_at TEXT,
  trigger TEXT,
  series_id INTEGER,
  round INTEGER,
  state TEXT,                           -- JSON-serialized SessionState
  size_bytes INTEGER
);

CREATE INDEX idx_answers_session ON answers(session_id);
CREATE INDEX idx_answers_series ON answers(series_id, round);
CREATE INDEX idx_snapshots_session ON snapshots(session_id);
```

### 3.5 Import / Export Archives

Projects can be packaged as portable archives:

```typescript
interface ProjectArchive {
  format_version: string;
  exported_at: string;
  project: Project;
  sessions: SessionState[];
  exports?: ExportResult[];
}
```

Archive format: `.space-project` (actually a ZIP containing JSON files)

```
my-project.space-project
├── .space.json
├── sessions/
│   ├── sess_001/state.json
│   ├── sess_001/artifacts.json
│   ├── sess_002/state.json
│   └── ...
└── exports/
    ├── specification.json
    └── specification.md
```

### 3.6 Git Integration

For version-controlled specifications:

```bash
# Initialize git in project
space git init my-project

# Auto-commit on session completion
space git auto-commit my-project --message "Session completed: 100%"

# Show spec diff between commits
space git diff my-project HEAD~1 HEAD

# Tag releases
space git tag my-project v1.0.0
```

Git hooks:
- `pre-commit`: Validate state.json schema
- `post-commit`: Update export/ symlink

---

## 5. Interfaces

```typescript
interface StorageProvider {
  // Projects
  createProject(project: Project): Promise<void>;
  getProject(project_id: string): Promise<Project>;
  listProjects(): Promise<Project[]>;
  updateProject(project: Project): Promise<void>;
  deleteProject(project_id: string): Promise<void>;
  
  // Sessions
  createSession(session: SessionState): Promise<void>;
  getSession(session_id: string): Promise<SessionState>;
  updateSession(session: SessionState): Promise<void>;
  listSessions(project_id: string): Promise<SessionSummary[]>;
  
  // Snapshots
  saveSnapshot(snapshot: Snapshot): Promise<void>;
  getLatestSnapshot(session_id: string): Promise<Snapshot | null>;
  listSnapshots(session_id: string): Promise<Snapshot[]>;
  
  // Exports
  saveExport(session_id: string, format: string, result: ExportResult): Promise<string>;
  getExport(session_id: string, format: string): Promise<ExportResult | null>;
}

// File-system implementation
class FileSystemStorage implements StorageProvider { ... }

// SQLite implementation (optional)
class SQLiteStorage implements StorageProvider { ... }
```

---

## 6. Edge Cases

- **Disk full:** Warn user, stop auto-saving, suggest export and cleanup
- **Concurrent writes:** Advisory file locks per session directory
- **State.json >100MB:** Extremely unlikely given data types; archive old sessions
- **Import from different SPACE version:** Migration layer runs on import

---

## 7. Testing Strategy

- File-system operations: create, read, update, delete for all entity types
- Snapshot recovery: corrupt state.json → verify latest valid snapshot loads
- Archive round-trip: export → import → verify all data intact
- SQLite: same operations via database adapter
- Concurrency: parallel session updates without data corruption

---

## 8. Open Questions

- Should SQLite be the primary storage or an optional add-on?
- How to handle cross-device sync (future)?
- Should archives include the framework definition for self-contained portability?

---

## 9. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
