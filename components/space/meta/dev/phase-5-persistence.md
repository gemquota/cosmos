# Phase 5: Persistence & Projects — Development Guide

**Spec References:** `specs/08-persistence.md`
**Prerequisites:** Phase 1 complete
**Estimated Effort:** 2–3 weeks
**Sprint Count:** 1-2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Replace localStorage with a durable, multi-session, multi-project storage system. Support file-system project layout, optional SQLite database, session versioning with snapshots, portable archive import/export, and optional git integration.

---

## Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 5.T1 | Storage provider interface | 08 §5 | M | 0.T1 | Interface compiles; all methods typed |
| 5.T2 | File-system storage implementation | 08 §3.1 | L | 5.T1 | CRUD for projects, sessions, snapshots |
| 5.T3 | Project directory scaffolding | 08 §3.1 | M | 5.T2 | `space init` creates full directory tree |
| 5.T4 | Snapshot system (save/restore/list) | 08 §3.3 | M | 5.T2 | Snapshots at round/series completion |
| 5.T5 | Recovery from corrupted state | 08 §3.3 | M | 5.T4 | Corrupted state.json → restore from snapshot |
| 5.T6 | Archive export (.space-project ZIP) | 08 §3.5 | M | 5.T2 | Portable archive with all data |
| 5.T7 | Archive import | 08 §3.5 | M | 5.T6 | Import archive → valid project |
| 5.T8 | SQLite storage adapter (optional) | 08 §3.4 | L | 5.T1 | Same interface, database-backed |
| 5.T9 | Git integration | 08 §3.6 | L | 5.T2 | Auto-commit on completion; diff between commits |
| 5.T10 | `space list` and `space status` commands | 04 §3.1 | M | 5.T2 | Show projects/sessions from storage |
| 5.T11 | Migration from localStorage (original app) | — | M | 5.T2 | Import old localStorage data into new system |

---

## Task Details

#### 5.T2: File-System Storage

**What:**
Implement `FileSystemStorage` class that reads/writes projects, sessions, and snapshots as JSON files in the directory structure defined by spec `08-persistence.md` §3.1.

**Files:**
- `src/storage/filesystem.ts`
- `src/storage/utils.ts` — File helpers (atomic write, safe read)
- `tests/storage/filesystem.test.ts`

**Implementation Notes:**
- Atomic writes: write to `.tmp` then rename (prevent corruption on crash)
- Directory creation on first write
- JSON pretty-printed for human readability
- File locking via `.lock` files (advisory)
- Use `crypto.randomUUID()` for IDs

**Done When:**
- [ ] Create, read, update, delete for all entity types
- [ ] Atomic writes prevent corruption
- [ ] Concurrent access handled with file locks
- [ ] Handles missing directories gracefully (creates them)

---

#### 5.T9: Git Integration

**What:**
Add git operations for specification versioning within project directories.

**Files:**
- `src/git/init.ts` — Initialize git repo
- `src/git/commit.ts` — Auto-commit
- `src/git/diff.ts` — Spec diff between commits
- `src/git/tag.ts` — Tag releases

**Implementation Notes:**
- Use `simple-git` npm package
- Auto-commit message: "Session completed: [session_id] ([completion_pct]%)"
- Only commit JSON files and exports (not node_modules, etc.)
- `.gitignore` auto-generated on init

**Done When:**
- [ ] `space git init` creates repo with proper .gitignore
- [ ] `space git auto-commit` creates commit with session info
- [ ] `space git diff HEAD~1 HEAD` shows spec changes
- [ ] `space git tag v1.0.0` creates annotated tag

---

## Testing

- File system: create/read/update/delete cycle for all entities
- Atomicity: kill process during write → file not corrupted
- Snapshot recovery: corrupt state.json → verify restore
- Archive round-trip: export → import → compare
- SQLite: same CRUD operations via database adapter

## Risks

- Git dependency (requires git installed) — optional, graceful skip if absent
- Large session files — unlikely but monitor file sizes
