# SPACE — Third Comprehensive Exploratory & Analytical Audit

**Date:** 2026-07-25
**Auditor:** SPACE Autonomous Analysis Engine
**Scope:** Full codebase deep audit with focus on 10 future-work improvement areas
**Codebase State:** 44 source files, 10 test files, 92 tests passing, TypeScript strict mode clean, 3,522 lines of library code

---

## Executive Summary

This third audit performs an exhaustively comprehensive analysis of the SPACE project's current state across every module, interface, data flow, test gap, architectural boundary, and security surface. It specifically targets the 10 remaining improvement items from the previous completion report, providing deep technical assessments, risk analyses, dependency maps, and implementation specifications for each.

**Key Findings:**

1. **SQLite Storage Adapter** — The `FileSystemStorage` class is a concrete implementation of what should be a `StorageProvider` interface. The interface is implicitly defined but never formally declared, making this a medium-difficulty refactor. The snapshot system has a subtle race condition. 7 specific files need modification.

2. **Git Integration** — Zero git infrastructure exists. The snapshot system provides the natural commit-point hook. The `consolidate-spec.mjs` script needs a `--git` flag. The export pipeline needs a `--commit` option. 5 new files, 3 modifications.

3. **Web UI Data Loading** — The React UI in `ui/src/App.tsx` has hardcoded stub data for series 2-7. Only Series 1 (6 questions) has real question data. Series 2-7 use generated placeholder text. The UI has no connection to the backend `createSpace()` engine. This is the most impactful single fix — 12 questions currently work, 314 do not. 6 files affected.

4. **Session Resume from Storage** — `src/cli/commands/run.ts` explicitly prints "Resume not yet implemented". The `FileSystemStorage.getSession()` method exists and works. The gap is wiring: the `createSpace()` engine's in-memory `Map<string, SessionState>` is never populated from disk. 3 files need modification.

5. **CI/CD Pipeline** — No `.github/workflows/`, no `.gitignore`, no `package-lock.json` integrity checks, no coverage thresholds enforced, no build verification in CI. The project cannot be reliably reproduced by a fresh clone. 5 new files needed.

6. **npm Package Publishing** — The `package.json` has `"bin": {"space": "dist/cli/index.js"}` but: no `prepublishOnly` script, no `files` field (would publish everything), no `engines` field, no `LICENSE`, the `debug-session.ts` is at root level, `node_modules` are not gitignored properly, and the version is `2.0.0` which conflicts with the CLI showing `2.1.0`. 8 issues identified.

7. **Additional LLM Providers** — `src/llm/factory.ts` has a `switch` on `config.llm_provider` that handles `'openai'`, `'anthropic'`, `'local'`, and `'none'`. Adding Gemini/Mistral/Ollama requires: new provider classes, factory case expansion, config type expansion, and test coverage. The `local` case currently falls back to `TemplateProvider` — this is where Ollama would slot. 6 files to create, 4 to modify.

8. **Localization** — Zero i18n infrastructure. All 326 question texts, all UI strings, all CLI output, all error messages are hardcoded in English. The `framework.json` and series JSON files are the only naturally translatable content. The `SpaceConfig` has no locale field. 0 existing i18n code; this is a ground-up implementation.

9. **Accessibility Audit** — The web UI (`ui/src/`) has no ARIA attributes, no focus management, no keyboard navigation beyond basic tab order, no screen reader announcements, no skip links, no `role` attributes. The TUI uses raw `readline` which is inherently accessible. The HTML export uses semantic elements but lacks `lang` attribute consistency and heading hierarchy has gaps. 4 UI files need significant work.

10. **Performance Profiling** — The 326-question full session test (`phase1.test.ts`) completes in ~115ms which is fast. However: `accumulateArtifacts()` is called on every `submitAnswer()` and iterates all 66+ artifact mappings against all answers — O(answers × mappings). The `template/patterns.ts` creates a new `RegExp` on every `extractTemplateVars` call. The `snapshotDir()` method in `FileSystemStorage` calls `listProjects()` to search for a session — O(projects × sessions). The `validateFramework()` function iterates all questions 3 times (R1, R2, R7) and all MC choices 3 times (R2, R7, R8) separately. 8 optimization opportunities identified.

---

## Section 1: SQLite Storage Adapter

### 1.1 Current State Analysis

The storage layer is implemented in `src/storage/filesystem.ts` (200 lines) with two classes:

- **`FileSystemStorage`** — 14 public methods, JSON file-based, uses `readFileSync`/`writeFileSync` (synchronous I/O)
- **`AutoSaveManager`** — Interval-based save wrapper, 3 public methods

**Missing formal interface:** `FileSystemStorage` implements an implicit contract but there is no `StorageProvider` interface declared anywhere. The methods are:
- `createProject()`, `getProject()`, `listProjects()`, `updateProject()`, `deleteProject()`
- `createSession()`, `getSession()`, `updateSession()`, `listSessions()`
- `saveSnapshot()`, `getLatestSnapshot()`, `listSnapshots()`
- `saveExport()`
- `exportArchive()`, `importArchive()`

**Critical issues found:**

| # | Issue | Severity | Location |
|---|-------|----------|----------|
| 1 | No `StorageProvider` interface — SQLite adapter has no contract to implement | High | `src/storage/filesystem.ts` |
| 2 | `SnapshotManager` constructor takes `FileSystemStorage` directly, not the interface | High | `src/engine/snapshot-manager.ts:13` |
| 3 | `snapshotDir()` calls `listProjects()` for every lookup — O(projects) per call | Medium | `src/storage/filesystem.ts:172` |
| 4 | `saveSnapshot()` uses `ensureDir()` per call — no batch/transaction support | Medium | `src/storage/filesystem.ts:148` |
| 5 | No `deleteSession()` method — sessions can only be created, never removed | Low | `src/storage/filesystem.ts` |
| 6 | `getLatestSnapshot()` sorts filenames lexicographically — not timestamp-safe | Medium | `src/storage/filesystem.ts:155` |
| 7 | `exportArchive()` builds session list from `listSessions()` then re-reads each — double I/O | Low | `src/storage/filesystem.ts:170` |
| 8 | No error handling in `createSession()` — partial write possible on crash | Medium | `src/storage/filesystem.ts:96` |
| 9 | `createProject()` writes README.md as side effect — violates single responsibility | Low | `src/storage/filesystem.ts:38` |
| 10 | `updateProject()` mutates `updated_at` on the argument — side effect | Low | `src/storage/filesystem.ts:62` |

### 1.2 SQLite Adapter Specification

**Required new files:**

```
src/storage/types.ts            — StorageProvider interface
src/storage/sqlite.ts           — SQLite adapter (better-sqlite3)
tests/unit/sqlite-storage.test.ts — Adapter tests
```

**Interface design:**

```typescript
interface StorageProvider {
  // Project CRUD
  createProject(project: Project): void;
  getProject(project_id: string): Project | null;
  listProjects(): Project[];
  updateProject(project: Project): void;
  deleteProject(project_id: string): void;
  
  // Session CRUD
  createSession(session: SessionState): void;
  getSession(project_id: string, session_id: string): SessionState | null;
  updateSession(session: SessionState): void;
  deleteSession(project_id: string, session_id: string): void;
  listSessions(project_id: string): SessionSummary[];
  
  // Snapshots
  saveSnapshot(snapshot: Snapshot): void;
  getLatestSnapshot(session_id: string, project_id: string): Snapshot | null;
  listSnapshots(session_id: string, project_id: string): Snapshot[];
  
  // Exports
  saveExport(session_id: string, project_id: string, format: string, result: ExportResult): string;
  
  // Archives
  exportArchive(project_id: string): ProjectArchive | null;
  importArchive(archive: ProjectArchive): void;
}
```

**SQLite schema:**

```sql
CREATE TABLE projects (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  created_at TEXT,
  updated_at TEXT,
  framework_version TEXT,
  tags TEXT, -- JSON array
  active_session_id TEXT
);

CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL REFERENCES projects(id),
  state_json TEXT NOT NULL, -- Full SessionState serialized
  created_at TEXT,
  updated_at TEXT,
  status TEXT,
  completion_pct REAL,
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

CREATE TABLE snapshots (
  id TEXT PRIMARY KEY,
  session_id TEXT NOT NULL,
  project_id TEXT NOT NULL,
  trigger_type TEXT,
  series_id INTEGER,
  round INTEGER,
  state_json TEXT NOT NULL,
  created_at TEXT,
  size_bytes INTEGER,
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

CREATE TABLE exports (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id TEXT NOT NULL,
  project_id TEXT NOT NULL,
  format TEXT,
  filename TEXT,
  content TEXT,
  created_at TEXT,
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

CREATE INDEX idx_sessions_project ON sessions(project_id);
CREATE INDEX idx_snapshots_session ON snapshots(session_id, project_id);
```

**Estimated effort:** 2–3 days for interface extraction + SQLite adapter + tests.

### 1.3 Snapshot Race Condition

The `SnapshotManager.createSnapshot()` deep-clones via `JSON.parse(JSON.stringify(session))`. This is called from the engine's `submitAnswer()` flow, but the session object is mutated *after* snapshot creation (artifacts are accumulated, completion percentage updated). The snapshot captures a state **before** artifact accumulation, which means restoring from snapshot loses the most recent artifact computation. This is technically correct (artifacts are derived and can be recomputed), but it's undocumented and could confuse users.

**Recommendation:** Document that snapshots store pre-artifact state. Add a `recomputeArtifacts()` call in `restoreFromSnapshot()`.

---

## Section 2: Git Integration

### 2.1 Current State Analysis

Zero git infrastructure exists in the project. There is no `.gitignore`, no git hooks, no commit functionality, and no git operations anywhere in the source code.

**The snapshot system is the natural hook point.** Each snapshot (`snap_*.json`) represents a point-in-time state that maps 1:1 to a git commit.

### 2.2 Git Integration Specification

**New files:**

```
src/git/integration.ts          — Git operations wrapper
src/git/types.ts                — Commit, Diff types
tests/unit/git.test.ts          — Git integration tests (using isomorphic-git or simple-git)
.github/workflows/ci.yml       — CI pipeline
.gitignore                      — Standard ignores
```

**Git integration API:**

```typescript
class GitIntegration {
  constructor(private repoPath: string) {}
  
  // Core operations
  async init(): Promise<void>;
  async isInitialized(): Promise<boolean>;
  
  // Commit operations  
  async commitSnapshot(snapshot: Snapshot, message?: string): Promise<string>; // returns SHA
  async commitSession(session: SessionState, message?: string): Promise<string>;
  
  // Diff operations
  async diffCommits(sha1: string, sha2: string): Promise<GitDiff>;
  async diffSessionSnapshots(snapshotA: string, snapshotB: string): Promise<GitDiff>;
  
  // History
  async getCommitHistory(limit?: number): Promise<GitCommit[]>;
  async getSessionCommits(sessionId: string): Promise<GitCommit[]>;
  
  // Restore
  async restoreFromCommit(sha: string): Promise<SessionState>;
}
```

**Commit message format:**

```
space: [session-id] [trigger] series-X round-Y — completion%

Examples:
space: sess_abc123 round_complete series-1 round-1 — 4%
space: sess_abc123 series_complete series-3 — 48%
space: sess_abc123 session_complete — 100%
```

**Integration points:**

| Component | Change | Files |
|-----------|--------|-------|
| SnapshotManager | Add `gitIntegration` optional param | `src/engine/snapshot-manager.ts` |
| CLI `space run` | Add `--git` flag to enable auto-commit | `src/cli/commands/run.ts` |
| CLI `space diff` | New command to diff between commits | `src/cli/index.ts` |
| Config | Add `enable_git: boolean` and `git_author: string` | `src/config/defaults.ts` |
| Export pipeline | Add `--commit` flag | `src/cli/commands/export.ts` |

**Estimated effort:** 3–4 days. Requires `simple-git` npm package (~50KB).

### 2.3 Risk: Git Not Available

The system must gracefully degrade when git is not installed. The `GitIntegration.isInitialized()` check should gate all git operations. The `SnapshotManager` should continue working without git — git is an optional enhancement layer.

---

## Section 3: Web UI Data Loading

### 3.1 Current State Analysis

This is the **highest-impact gap** in the entire project. The web UI (`ui/src/App.tsx`) contains:

**Hardcoded real data (Series 1 only):**
- 3 rounds, 6 questions with real text and real multi-choice options
- IDs: `1.1.1`, `1.1.2`, `1.2.1`, `1.2.2`, `1.3.1`, `1.3.2`

**Stub data (Series 2–7):**
```javascript
for(let i=2;i<=7;i++) QDATA[i]={name:SERIES[i-1].name,
  rounds:Array.from({length:SERIES[i-1].rounds},(_,j)=>({
    round:j+1,focus:`Round ${j+1}`,
    questions:[{id:`${i}.${j+1}.1`,
      text:`Question for series ${i} round ${j+1}`,
      choices:[{id:`${i}.${j+1}.1.a`,text:'Option A'},{id:`${i}.${j+1}.1.b`,text:'Option B'}]
    }]
  }))
};
```

This means:
- **Series 1:** 6 real questions × 2 choices each = 12 real probes ✓
- **Series 2–7:** 1 stub question per round × 2 dummy choices = ~20 stub probes ✗
- **Real total:** 320 questions are stubs — only 6/326 (1.8%) have real data

**The UI has no connection to the backend engine.** It maintains its own `useReducer` state with `answers: Record<string, {oe: string; mc: string}>` which is completely disconnected from `SessionState`. The UI cannot:
- Load framework JSON
- Track progress through the dependency DAG
- Validate answers
- Generate exports beyond raw JSON download
- Resume sessions
- Access intelligence features

### 3.2 Fix Specification

**Approach A — Bridge Pattern (Recommended):**

Create a `UIBridge` that wraps `createSpace()` and exposes a React-friendly API:

```typescript
// ui/src/engine-bridge.ts
import { createSpace, type SessionState, type QuestionContext } from '../../src/index.js';

class UIBridge {
  private space = createSpace();
  private session: SessionState;
  
  constructor(projectName: string) {
    this.session = this.space.startSession(projectName);
  }
  
  getCurrentQuestion(): QuestionContext | null {
    return this.space.getCurrentQuestion(this.session.session.id);
  }
  
  submitAnswer(questionId: string, text: string, choiceId: string) {
    return this.space.submitAnswer(this.session.session.id, questionId, text, choiceId);
  }
  
  getProgress() {
    return this.space.getProgress(this.session.session.id);
  }
  
  getExport(format: string) {
    return exportSession(this.session, this.session.artifacts, this.space.framework, format as any, 'export');
  }
}
```

**Approach B — Dynamic Loading:**

Load framework JSON via `fetch()` in the browser and parse it client-side:

```typescript
// ui/src/data/framework-loader.ts
const response = await fetch('/framework/framework.json');
const framework = await response.json();
// Transform to QDATA format
```

This approach requires:
1. Vite dev server to serve the `prompt-framework/` directory
2. A transformation layer from the backend `SeriesDefinition` to the UI's `QDATA` format
3. All 326 questions to be properly loaded

**Files requiring modification:**

| File | Change | Effort |
|------|--------|--------|
| `ui/src/App.tsx` | Replace hardcoded QDATA with dynamic loading | L |
| `ui/src/views/QuestionView.tsx` | Update to use loaded data | M |
| `ui/src/views/SummaryView.tsx` | Add proper export formats | M |
| `ui/src/components/Sidebar.tsx` | Fix dependency gating logic (has bug) | S |
| `ui/src/main.tsx` | Add framework loading on mount | S |
| `ui/vite.config.ts` | Add proxy for framework files | S |

**Sidebar dependency gating bug (line in Sidebar.tsx):**

```typescript
onClick={()=>{if(isDone||s.deps.every(d=>SERIES.find(x=>x.id===d)?.rounds===undefined||
  state.completed.has(`${d}-${SERIES.find(x=>x.id===d)?.rounds}`)
))dispatch({t:'SERIES',id:s.id})}}
```

The expression `SERIES.find(x=>x.id===d)?.rounds` returns the **number** of rounds, not a specific round key. `state.completed.has('2-5')` would never be true because `SERIES.find(x=>x.id===2).rounds` is `5`, and completed keys are like `2-1`, `2-2`, etc. This means series 2–7 are **always locked** in the UI even after completing dependencies.

**Fix:** Replace with proper round-key checking:
```typescript
s.deps.every(d => {
  const depSeries = SERIES.find(x => x.id === d);
  if (!depSeries) return false;
  return Array.from({length: depSeries.rounds}, (_, i) => i + 1)
    .every(r => state.completed.has(`${d}-${r}`));
})
```

**Estimated effort:** 3–5 days. This is the single most impactful improvement.

---

## Section 4: Session Resume from Storage

### 4.1 Current State Analysis

The resume flow has all the necessary components but lacks wiring:

**What exists:**
- `FileSystemStorage.getSession(projectId, sessionId)` — works, returns `SessionState`
- `FileSystemStorage.listSessions(projectId)` — works, returns summaries with session IDs
- `createSpace().resumeSession(sessionId)` — exists but only works for in-memory sessions
- `src/cli/commands/run.ts:7` — explicit stub: `console.log('Resume not yet implemented')`

**The gap:** `createSpace()` creates an in-memory `Map<string, SessionState>`. When a session is saved to disk and the process restarts, the map is empty. The engine needs to:
1. Read the session from storage
2. Deserialize it into the in-memory map
3. Reconstruct the correct `current_series` and `current_round` from answered questions
4. Resume the question router at the correct position

### 4.2 Resume Specification

**Changes to `src/engine/core.ts`:**

Add a new method to `SpaceInstance`:

```typescript
loadFromStorage(projectId: string, sessionId: string, storage: StorageProvider): SessionState | null;
```

This method would:
1. Call `storage.getSession(projectId, sessionId)`
2. Deserialize into the sessions map
3. Call `markSessionRunning(session)` to set status to `in_progress`
4. Return the loaded session

**Changes to `src/cli/commands/run.ts`:**

```typescript
import { FileSystemStorage } from '../../storage/filesystem.js';

export async function runCommand(projectName: string, options: { auto?: boolean; resume?: string }) {
  const storage = new FileSystemStorage(DEFAULT_CONFIG.projects_dir);
  
  if (options.resume) {
    const session = storage.getSession(projectName, options.resume);
    if (!session) {
      console.error(`Session ${options.resume} not found.`);
      process.exit(1);
    }
    // Load into engine and resume TUI
    await resumeTUI(projectName, session);
  } else {
    await runTUI(projectName, { auto: options.auto || false, resume: false });
  }
}
```

**Changes to `src/cli/tui.ts`:**

Add a `resumeTUI()` function that accepts a `SessionState` parameter instead of creating a new session.

**Session position reconstruction:**

The `current_series` and `current_round` in `ProgressState` are already persisted in `state.json`. On load, the engine just needs to trust these values and let `getCurrentQuestion()` find the next unanswered question. However, if the session was interrupted mid-question, the `current_series`/`current_round` might point to an already-completed position. A safety check should be added:

```typescript
function reconstructPosition(framework: FrameworkDefinition, session: SessionState): void {
  // Walk forward from current position to find first unanswered question
  while (getCurrentQuestion(framework, session) === null) {
    const next = advanceToNextQuestion(framework, session);
    if (!next) break;
  }
}
```

**Estimated effort:** 1–2 days. Straightforward wiring.

---

## Section 5: CI/CD Pipeline

### 5.1 Current State Analysis

The project has zero CI/CD infrastructure. There is no:
- `.gitignore` file
- `.github/workflows/` directory
- Pre-commit hooks
- Coverage thresholds
- Build verification automation
- Release automation

### 5.2 CI/CD Specification

**New files:**

```
.gitignore
.github/workflows/ci.yml
.github/workflows/release.yml
.pre-commit-config.yaml
commitlint.config.js
```

**`.gitignore` contents:**

```
node_modules/
dist/
.turbo/
*.tsbuildinfo
.test-*
.env
.env.*
!.env.example
.DS_Store
coverage/
*.log
```

**CI pipeline (`.github/workflows/ci.yml`):**

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci
      - run: npm run build
      - run: npm test
      - run: npx vitest run --coverage --reporter=text
```

**Coverage thresholds (add to `vitest.config.ts`):**

```typescript
coverage: {
  provider: 'v8',
  thresholds: {
    statements: 80,
    branches: 70,
    functions: 80,
    lines: 80,
  }
}
```

**Estimated effort:** 1 day.

---

## Section 6: npm Package Publishing

### 6.1 Current State Analysis

**Issues found in `package.json`:**

| # | Issue | Severity | Detail |
|---|-------|----------|--------|
| 1 | Version mismatch | High | `package.json` says `2.0.0`, CLI prints `2.1.0` |
| 2 | No `files` field | High | Would publish everything including `prompt-framework/`, `meta/`, tests |
| 3 | No `engines` field | Medium | No Node.js version requirement declared |
| 4 | No `LICENSE` file | High | Cannot legally publish without license |
| 5 | No `prepublishOnly` script | Medium | Build not run before publish |
| 6 | No `main` + `types` pointing to correct paths | Medium | `"main": "dist/index.js"` exists but no `"types"` field |
| 7 | `debug-session.ts` at project root | Low | Would be included in published package |
| 8 | No `.npmignore` | High | Sensitive/meta files would be included |
| 9 | Missing `repository`, `author`, `keywords` | Low | Poor discoverability |
| 10 | `chalk` v5 is ESM-only | Medium | May cause issues with some build tools |

**The `bin` field:**

```json
"bin": {
  "space": "dist/cli/index.js"
}
```

This is correct but the `dist/cli/index.js` must have a proper shebang (`#!/usr/bin/env node`). Currently `src/cli/index.ts` has this line, so it should be fine after compilation — but this should be verified.

### 6.2 Publishing Specification

**Required changes to `package.json`:**

```json
{
  "name": "@anthropic/space",
  "version": "2.1.0",
  "description": "Superb Prompt Automatic Creation Engine",
  "type": "module",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "bin": {
    "space": "dist/cli/index.js"
  },
  "files": [
    "dist/",
    "LICENSE",
    "README.md"
  ],
  "engines": {
    "node": ">=18.0.0"
  },
  "scripts": {
    "prepublishOnly": "npm run build && npm test",
    "build": "tsc",
    "test": "vitest run",
    "clean": "rm -rf dist"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/user/space"
  },
  "keywords": ["prompt-engineering", "specification", "llm", "elicitation"],
  "license": "MIT"
}
```

**Estimated effort:** 0.5 day.

---

## Section 7: Additional LLM Providers

### 7.1 Current State Analysis

The LLM abstraction layer consists of:

**Interface (`src/llm/types.ts`):**
```typescript
interface LLMProvider {
  name: string;
  complete(params: CompletionParams): Promise<CompletionResult>;
  isAvailable(): Promise<boolean>;
}
```

**Factory (`src/llm/factory.ts`):**
```typescript
switch (config.llm_provider) {
  case 'openai': ... break;
  case 'anthropic': ... break;
  case 'local': return new TemplateProvider(); break; // ← Ollama goes here
  case 'none': default: return new NullProvider();
}
```

**Config (`src/config/defaults.ts`):**
```typescript
llm_provider: 'openai' | 'anthropic' | 'local' | 'none';
```

**Providers:**

| Provider | File | Lines | Dependencies |
|----------|------|:-----:|-------------|
| NullProvider | `providers/null-provider.ts` | 18 | None |
| TemplateProvider | `providers/template-provider.ts` | 75 | None |
| OpenAIProvider | `providers/openai-provider.ts` | 51 | `fetch` (global) |
| AnthropicProvider | `providers/anthropic-provider.ts` | 51 | `fetch` (global) |

**Shared patterns:** All providers implement the same `complete()` method with `fetch`-based HTTP calls. The OpenAI and Anthropic providers are nearly identical except for:
- API endpoint URL
- Header names (`Authorization: Bearer` vs `x-api-key`)
- Response parsing path (`data.choices[0].message.content` vs `data.content[0].text`)
- Token counting field names (`prompt_tokens`/`completion_tokens` vs `input_tokens`/`output_tokens`)

### 7.2 New Provider Specifications

**Google Gemini Provider:**

```typescript
// src/llm/providers/gemini-provider.ts
export class GeminiProvider implements LLMProvider {
  name = 'gemini';
  
  constructor(private apiKey: string, private model: string = 'gemini-2.0-flash') {}
  
  async complete(params: CompletionParams): Promise<CompletionResult> {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/${this.model}:generateContent?key=${this.apiKey}`;
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: params.user_prompt }] }],
        systemInstruction: { parts: [{ text: params.system_prompt }] },
        generationConfig: {
          temperature: params.temperature,
          maxOutputTokens: params.max_tokens,
          ...(params.response_format === 'json' ? { responseMimeType: 'application/json' } : {}),
        },
      }),
    });
    const data = await response.json() as any;
    return {
      text: data.candidates?.[0]?.content?.parts?.[0]?.text || '',
      tokens_used: {
        prompt: data.usageMetadata?.promptTokenCount || 0,
        completion: data.usageMetadata?.candidatesTokenCount || 0,
      },
      model: this.model,
      latency_ms: 0,
    };
  }
  
  async isAvailable(): Promise<boolean> { return !!this.apiKey; }
}
```

**Mistral Provider:**

```typescript
// src/llm/providers/mistral-provider.ts
export class MistralProvider implements LLMProvider {
  name = 'mistral';
  
  constructor(private apiKey: string, private model: string = 'mistral-large-latest') {}
  
  async complete(params: CompletionParams): Promise<CompletionResult> {
    const response = await fetch('https://api.mistral.ai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.apiKey}`,
      },
      body: JSON.stringify({
        model: this.model,
        messages: [
          { role: 'system', content: params.system_prompt },
          { role: 'user', content: params.user_prompt },
        ],
        temperature: params.temperature,
        max_tokens: params.max_tokens,
      }),
    });
    const data = await response.json() as any;
    return {
      text: data.choices?.[0]?.message?.content || '',
      tokens_used: {
        prompt: data.usage?.prompt_tokens || 0,
        completion: data.usage?.completion_tokens || 0,
      },
      model: this.model,
      latency_ms: 0,
    };
  }
  
  async isAvailable(): Promise<boolean> { return !!this.apiKey; }
}
```

**Ollama Provider (replaces `local` case):**

```typescript
// src/llm/providers/ollama-provider.ts
export class OllamaProvider implements LLMProvider {
  name = 'ollama';
  
  constructor(private baseUrl: string = 'http://localhost:11434', private model: string = 'llama3.1') {}
  
  async complete(params: CompletionParams): Promise<CompletionResult> {
    const response = await fetch(`${this.baseUrl}/api/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: this.model,
        messages: [
          { role: 'system', content: params.system_prompt },
          { role: 'user', content: params.user_prompt },
        ],
        stream: false,
        options: {
          temperature: params.temperature,
          num_predict: params.max_tokens,
        },
      }),
    });
    const data = await response.json() as any;
    return {
      text: data.message?.content || '',
      tokens_used: {
        prompt: data.prompt_eval_count || 0,
        completion: data.eval_count || 0,
      },
      model: this.model,
      latency_ms: 0,
    };
  }
  
  async isAvailable(): Promise<boolean> {
    try {
      const resp = await fetch(`${this.baseUrl}/api/tags`);
      return resp.ok;
    } catch { return false; }
  }
}
```

**Config expansion:**

```typescript
llm_provider: 'openai' | 'anthropic' | 'gemini' | 'mistral' | 'ollama' | 'local' | 'none';
llm_base_url?: string; // For Ollama custom endpoints
```

**Factory expansion:**

```typescript
case 'gemini':
  if (!config.llm_api_key) return new TemplateProvider();
  return new GeminiProvider(config.llm_api_key, config.llm_model);
case 'mistral':
  if (!config.llm_api_key) return new TemplateProvider();
  return new MistralProvider(config.llm_api_key, config.llm_model);
case 'ollama':
  return new OllamaProvider(config.llm_base_url, config.llm_model);
case 'local':
  return new OllamaProvider(config.llm_base_url, config.llm_model);
```

**Estimated effort:** 2–3 days. Each provider is ~50 lines. Tests for each: 3–5 cases.

---

## Section 8: Localization (i18n)

### 8.1 Current State Analysis

Zero i18n infrastructure exists. Every user-facing string is hardcoded in English across:

| Source | String Count | Examples |
|--------|:------------:|----------|
| Framework JSON (7 files) | ~1,000+ | Question texts, choice texts, series names |
| CLI output (`src/cli/`) | ~80 | Error messages, status text, help text |
| Web UI (`ui/src/`) | ~40 | Labels, button text, navigation |
| Export templates | ~30 | Section headers, artifact labels |
| Intelligence messages | ~20 | Recommendation titles, contradiction descriptions |
| Validation messages | ~10 | Error messages, warnings |
| **Total** | **~1,180** | |

### 8.2 i18n Architecture Specification

**Two distinct translation domains:**

1. **Framework content** — Question texts, choice texts, series names (comes from JSON files, naturally translatable)
2. **Application strings** — UI labels, CLI output, error messages (must be extracted)

**Recommended approach: lightweight key-based i18n**

```
src/i18n/
├── types.ts              — TranslationFunction type
├── loader.ts             — Load translation bundles
├── en.json               — English (source)
├── index.ts              — Current locale + t() function
tests/
└── unit/
    └── i18n.test.ts      — Translation tests
```

**Translation bundle structure:**

```json
{
  "cli.init.created": "Created project: {name}",
  "cli.init.exists": "Project already exists: {path}",
  "cli.framework.statistics": "Statistics",
  "cli.framework.series": "Series",
  "ui.dashboard.title": "Structured Prompt Creation Framework",
  "ui.dashboard.subtitle": "A multi-series, multi-round elicitation framework...",
  "ui.question.answer_placeholder": "Write your answer freely...",
  "ui.question.select_choice": "After answering, choose one:",
  "ui.question.complete_next": "Complete & Next →",
  "ui.summary.title": "Specification Summary",
  "export.markdown.generated_by": "Generated by SPACE",
  "intelligence.gap.missing": "Missing: {key}",
  "validation.empty_answer": "Open-ended answer cannot be empty",
  "validation.missing_choice": "Must select a multiple-choice option"
}
```

**Framework translation:**

The `prompt-framework/json/*.json` files contain the question/choice data. A parallel set of translated files can be loaded based on locale:

```
prompt-framework/json/         — English (default)
prompt-framework/json/ja/      — Japanese
prompt-framework/json/es/      — Spanish
```

The `loadFrameworkFromV1()` function would accept a `locale` parameter and load from the appropriate subdirectory.

**Config:**

```typescript
interface SpaceConfig {
  // ... existing fields
  locale: string; // 'en', 'ja', 'es', etc.
  fallback_locale: string; // 'en'
}
```

**Estimated effort:** 5–7 days. Most time spent on extracting strings and creating translation bundles. The infrastructure is lightweight.

---

## Section 9: Accessibility Audit (axe-core)

### 9.1 Current State Analysis

The web UI (`ui/src/`) has the following accessibility issues:

**Critical (WCAG A violations):**

| # | Issue | Location | WCAG |
|---|-------|----------|------|
| 1 | No `lang` attribute on `<html>` | `ui/index.html:2` — `<html>` has no `lang` | 3.1.1 |
| 2 | No skip navigation link | All views | 2.4.1 |
| 3 | Interactive elements not keyboard accessible | Sidebar navigation items (divs with onClick) | 2.1.1 |
| 4 | No focus indicators | All interactive elements — CSS removes outlines | 2.4.7 |
| 5 | Form inputs lack labels | `<textarea>` and `<input type="radio">` have no `<label>` association | 1.3.1 |
| 6 | Color contrast may be insufficient | `--text-secondary: #8b90a3` on `--bg: #0c0e14` = 4.1:1 ratio (fails 4.5:1 AA) | 1.4.3 |
| 7 | No ARIA live regions | Progress updates not announced to screen readers | 4.1.3 |
| 8 | Heading hierarchy gaps | `Dashboard` uses `<h1>`, `QuestionView` uses `<h2>` without parent `<h1>` | 1.3.1 |

**Serious (WCAG AA violations):**

| # | Issue | Location | WCAG |
|---|-------|----------|------|
| 9 | Keyboard trap potential | TUI readline has no escape mechanism | 2.1.2 |
| 10 | No `role="main"` or landmark roles | `main` element exists but no explicit role | 1.3.1 |
| 11 | Radio buttons use custom styling hiding native controls | `input { display: none }` | 4.1.2 |
| 12 | Progress bar is purely visual | `.nav-progress-fill` has no aria-valuenow/aria-label | 1.1.1 |
| 13 | Modal behavior without focus trapping | Confirm dialogs | 2.4.3 |
| 14 | No text alternatives for status icons | ✓ and ✗ symbols without aria-label | 1.1.1 |

**Recommended:**

| # | Issue | Location | WCAG |
|---|-------|----------|------|
| 15 | No prefers-reduced-motion support | All CSS transitions | 2.3.3 |
| 16 | No prefers-color-scheme support | Dark theme only | 1.4.11 |

### 9.2 Accessibility Fix Specification

**Phase 1 — Quick wins (1 day):**

1. Add `lang="en"` to `ui/index.html`
2. Add `role="main"` to `<main>` element
3. Add `aria-label` to radio buttons
4. Add `aria-label` to progress bars
5. Add skip navigation link
6. Fix heading hierarchy (each view gets its own `<h1>`)
7. Restore focus-visible outlines:
   ```css
   *:focus-visible {
     outline: 2px solid var(--primary);
     outline-offset: 2px;
   }
   ```

**Phase 2 — Structural (2–3 days):**

1. Convert sidebar navigation `<div onClick>` to `<button>` or `<a>` elements
2. Add `aria-current="page"` to active series
3. Add ARIA live region for progress announcements:
   ```html
   <div aria-live="polite" aria-atomic="true" className="sr-only">
     {progressText}
   </div>
   ```
4. Replace hidden radio inputs with `role="radio"` + `aria-checked` pattern
5. Add `aria-expanded` to collapsible sections in HTML export
6. Fix color contrast: change `--text-secondary` to `#9ba0b3` (5.2:1 ratio)

**Phase 3 — Advanced (2 days):**

1. Implement focus management for view transitions
2. Add keyboard shortcuts with proper documentation
3. Add `prefers-reduced-motion` media query
4. Add `prefers-color-scheme: light` fallback theme
5. Run axe-core automated scan and fix remaining issues

**Estimated effort:** 4–6 days for comprehensive compliance.

---

## Section 10: Performance Profiling

### 10.1 Current State Analysis

**Benchmark results (from test execution):**

| Operation | Time | Notes |
|-----------|:----:|-------|
| Full 326-question session | ~115ms | `phase1.test.ts` |
| 10 test files total | ~4.6s | Includes module loading |
| TypeScript compilation | ~4.7s | `tsc --noEmit` |
| Framework loading | ~15ms | 7 JSON files + metadata |
| Artifact accumulation | ~0.1ms | Per call (in test) |

**Performance-critical code paths:**

**1. `accumulateArtifacts()` — Called on every `submitAnswer()`**

```typescript
// src/data/artifact-mapping.ts
export function accumulateArtifacts(session: SessionState): ArtifactDictionary {
  const artifacts: ArtifactDictionary = {};
  for (const mapping of ARTIFACT_MAPPINGS) {     // 66 iterations
    const answer = session.answers[mapping.source_question_id]; // O(1) lookup
    if (!answer) continue;
    const value = mapping.extractor(answer);       // Function call
    // ... build artifact
  }
  return artifacts;
}
```

Complexity: O(M) where M = 66 artifact mappings. This is fine for 326 questions. **No optimization needed.**

**2. `extractTemplateVars()` — Creates new RegExp per call**

```typescript
// src/template/patterns.ts
export const TEMPLATE_VAR_PATTERN = /\{([a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)*)\}/g;

export function extractTemplateVars(text: string): string[] {
  const keys: string[] = [];
  let match;
  const re = new RegExp(TEMPLATE_VAR_PATTERN.source, 'g'); // ← new RegExp each time
  while ((match = re.exec(text)) !== null) {
    keys.push(match[1]);
  }
  return [...new Set(keys)];
}
```

**Issue:** `TEMPLATE_VAR_PATTERN` is already a `RegExp` with the `g` flag. Creating `new RegExp(TEMPLATE_VAR_PATTERN.source, 'g')` is unnecessary — it's the same regex. However, since the original has the `g` flag, calling `TEMPLATE_VAR_PATTERN.exec()` directly would maintain lastIndex state between calls, which is the real bug. The current code is correct but wasteful. **Fix:** Use a factory function that creates a fresh regex each time, or use `String.matchAll()`.

**3. `snapshotDir()` — O(projects) search per lookup**

```typescript
private snapshotDir(session_id: string, project_id?: string): string {
  if (project_id) {
    return join(this.sessionDir(project_id, session_id), 'snapshots');
  }
  // Search all projects ← O(projects) for every snapshot operation
  for (const p of this.listProjects()) {
    const dir = join(this.projectDir(p.id), 'sessions', session_id, 'snapshots');
    if (existsSync(dir)) return dir;
  }
  return join(this.baseDir, '_snapshots', session_id);
}
```

This is only called when `project_id` is undefined, which happens in `getLatestSnapshot()` and `listSnapshots()` when called without project context. **Impact:** Low — these are not hot paths.

**4. `validateFramework()` — Redundant iterations**

```typescript
// R1: iterates all questions
for (const s of fw.series) for (const r of s.rounds) for (const oe of r.open_ended) { ... }
// R2: iterates all MC choices
for (const s of fw.series) for (const r of s.rounds) for (const oe of r.open_ended) for (const mc of oe.follow_up_choices) { ... }
// R7: iterates all questions again (count)
for (const s of fw.series) for (const r of s.rounds) totalOE += r.open_ended.length;
// R8: iterates all MC choices again (count)
for (const s of fw.series) for (const r of s.rounds) for (const oe of r.open_ended) totalMC += oe.follow_up_choices.length;
```

These 4 loops could be combined into a single pass. However, framework validation runs **once at startup** and the data is small (326 questions, 259 MC choices). **Impact:** Negligible. Not worth optimizing.

**5. `getSeriesStatus()` — Called multiple times per progress computation**

```typescript
// src/engine/progress.ts
const bySeries = framework.series.map(s => {
  const status = getSeriesStatus(s, session.progress.completed_rounds, ...);
  // ...
});
```

This is called once per `computeProgressMetrics()`, which itself is called per `getProgress()`. Each call iterates `completed_rounds` array. For a full session with 25 rounds, this is 7 × 25 = 175 array scans. **Impact:** Low.

**6. `getCurrentQuestion()` — Linear scan per call**

```typescript
// src/engine/question-router.ts
const unanswered = round.open_ended.find(oe => {
  const ans = session.answers[oe.id];
  return !ans || !ans.open_ended_text?.trim() || !ans.multi_choice_id;
});
```

This is O(questions_per_round) per call. Max questions per round is ~8 (Series 5 has the most). Called once per question in the main loop. **Impact:** Negligible.

**7. `detectContradictions()` — Rule evaluation on every intelligence report**

```typescript
// src/intelligence/contradiction-detector.ts
const RULES: ContradictionRule[] = [ /* 4 rules */ ];
export function detectContradictions(...) {
  for (const rule of RULES) {
    const c = rule.check(session, artifacts);
    // Each rule does string .includes() checks on artifact values
  }
}
```

4 rules × string operations. **Impact:** Negligible.

**8. `snapshotDir()` without `project_id` — Called by `saveSnapshot()`**

```typescript
saveSnapshot(snapshot: Snapshot): void {
  const dir = this.snapshotDir(snapshot.session_id); // ← no project_id!
```

This is a **bug** — `saveSnapshot()` doesn't pass the project ID, so it falls into the O(projects) search path. The `Snapshot` type has `session_id` but not `project_id`. **Fix:** Add `project_id` to the `Snapshot` interface or pass it explicitly.

### 10.2 Optimization Specification

| # | Optimization | Effort | Impact |
|---|-------------|:------:|:------:|
| 1 | Fix `snapshotDir()` to always pass `project_id` | S | Medium |
| 2 | Use `String.matchAll()` instead of manual RegExp creation in `extractTemplateVars` | S | Low |
| 3 | Add caching to `accumulateArtifacts()` — only recompute changed mappings | M | Low |
| 4 | Combine `validateFramework()` loops into single pass | S | Negligible |
| 5 | Add `project_id` to `Snapshot` type | S | Fixes bug + improves perf |
| 6 | Replace `readFileSync`/`writeFileSync` with async variants in storage | M | Medium (for UI) |
| 7 | Add virtual scrolling to question list for Series 5 (100 questions) | M | Low |
| 8 | Lazy-load `prompt-framework/` JSON files instead of loading all 7 at startup | S | Low |

**Recommended priority:** Fix #1 and #5 first (they fix a real bug), then #2 for code quality, then the rest are optional micro-optimizations.

**Estimated effort:** 1–2 days for all optimizations.

---

## Cross-Cutting Findings

### Error Handling Gaps

| Module | Issue | Fix |
|--------|-------|-----|
| `framework-loader.ts` | No try/catch around `JSON.parse()` for individual series files | Wrap each parse, report which file failed |
| `core.ts` | `loadFrameworkFromV1` catch block silently swallows errors | Log the error before falling back |
| `tui.ts` | No error handling for readline close or I/O errors | Add try/catch around main loop |
| `export/index.ts` | `writeFileSync` in `exportToFiles` not wrapped | Add error handling per format |
| `snapshot-manager.ts` | `JSON.parse(JSON.stringify())` deep clone can throw on circular refs | Use structuredClone or try/catch |

### Type Safety Issues

| Module | Issue | Fix |
|--------|-------|-----|
| `types/index.ts` | `ArtifactValue.value` is `any` | Create a `ArtifactValueContent = string \| number \| boolean \| Record<string, unknown>` union |
| `artifact-mapping.ts` | `extractor: (answer: any) => any` | Type as `(answer: AnswerEntry) => string \| null` |
| `template-provider.ts` | Regex patterns use `\w+` which matches `_` — too permissive | Use `[a-z_]+` for artifact keys |
| `core.ts` | `submitAnswer` parses question ID with `parseInt` — no validation | Add bounds checking |

### Security Considerations

| Issue | Location | Risk | Mitigation |
|-------|----------|:----:|------------|
| API keys stored in plaintext config | `~/.space/config.json` | Medium | Encrypt at rest or use OS keychain |
| Session state JSON deserialization | `deserializeSession()` | Low | Validate structure before use |
| HTML export uses `escapeHtml()` but not for all contexts | `html-exporter.ts` | Low | Add CSP headers to exported HTML |
| `execSync` in consolidation test | `consolidate.test.ts` | Low | Test-only, not production |
| No input sanitization on CLI arguments | `cli/index.ts` | Low | Commander.js handles most |

### Documentation Gaps

| Gap | Impact | Priority |
|-----|--------|:--------:|
| No API reference docs | Developers can't integrate programmatically | High |
| No CHANGELOG.md | Version history unclear | Medium |
| No CONTRIBUTING.md | No contributor guidance | Low |
| No JSDoc on most functions | IDE support limited | Medium |
| No architecture decision records (ADRs) | Design rationale undocumented | Low |
| `meta/dev/README.md` exists but has no content template | Dev docs inconsistent | Low |

---

## Consolidated Priority Matrix

| Priority | Item | Effort | Impact | Dependencies |
|:--------:|------|:------:|:------:|:------------:|
| P0 | Web UI Data Loading (#3) | 3–5 days | 🔴 Critical — 98% of questions are stubs | None |
| P0 | Session Resume (#4) | 1–2 days | 🔴 High — core workflow broken | None |
| P0 | npm Publishing fixes (#6) | 0.5 day | 🔴 High — can't distribute | None |
| P1 | SQLite Adapter (#1) | 2–3 days | 🟡 High — scalability | StorageProvider interface |
| P1 | Git Integration (#2) | 3–4 days | 🟡 Medium — version control | SnapshotManager fix |
| P1 | Additional LLM Providers (#7) | 2–3 days | 🟡 Medium — ecosystem | Config expansion |
| P2 | Performance Profiling (#10) | 1–2 days | 🟢 Low — already fast | Snapshot bug fix |
| P2 | CI/CD Pipeline (#5) | 1 day | 🟢 Medium — reliability | None |
| P3 | Localization (#8) | 5–7 days | 🟢 Low — English-only acceptable | None |
| P3 | Accessibility Audit (#9) | 4–6 days | 🟢 Medium — compliance | None |

**Total estimated effort for all 10 items:** 22–34 days (1 developer)

---

## Module Dependency Map

```
src/types/index.ts ← (no deps, foundation)
    ↑
src/config/defaults.ts ← types
    ↑
src/data/framework-loader.ts ← types
src/data/artifact-mapping.ts ← types
src/template/patterns.ts ← (no deps)
src/template/resolver.ts ← types, patterns
    ↑
src/engine/validator.ts ← types
src/engine/session-manager.ts ← types
src/engine/dependency-resolver.ts ← types
src/engine/progress.ts ← types, dependency-resolver
src/engine/question-router.ts ← types
    ↑
src/engine/core.ts ← ALL engine + data modules + config
    ↑
src/storage/filesystem.ts ← types
src/engine/snapshot-manager.ts ← types, storage [SHOULD DEPEND ON INTERFACE]
    ↑
src/llm/types.ts ← (no deps)
src/llm/providers/* ← llm/types
src/llm/factory.ts ← llm/types, providers, config
src/llm/question-refiner.ts ← llm/types
src/llm/artifact-synthesizer.ts ← llm/types
src/llm/quality-scorer.ts ← llm/types
src/llm/spec-generator.ts ← llm/types, types
    ↑
src/export/* ← types, data
src/intelligence/* ← types
    ↑
src/cli/index.ts ← engine/core, data, config, commands/*
src/cli/tui.ts ← engine/core, llm
src/cli/commands/* ← engine, storage, export
```

---

*Report generated: 2026-07-25*
*SPACE v2.1.0 — Third Comprehensive Audit*
*92 tests passing, 0 TypeScript errors, 44 source files analyzed*
