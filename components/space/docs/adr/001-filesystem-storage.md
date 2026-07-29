# ADR 001: Filesystem-Based Storage

## Status

Accepted

## Date

2024-01-01

## Context

SPACE needs to persist session state (answers, artifacts, progress) between CLI invocations. Options include:
1. JSON files on filesystem
2. SQLite database
3. In-memory only (no persistence)
4. Cloud storage (S3, etc.)

## Decision

Use JSON files on the local filesystem as the primary storage mechanism. The SQLite adapter exists as an alternative but is not the default.

## Consequences

### Positive
- Simple implementation with no external dependencies
- Human-readable and debuggable (JSON files can be inspected with any editor)
- Version-control friendly (git trackable)
- Offline-first (no network required)
- Atomic writes via rename pattern

### Negative
- No query capabilities (must load entire file to search)
- Concurrent access not supported (single-user tool)
- No built-in backup/replication
- Filesystem permissions are the only access control

### Risks
- Data loss if filesystem is corrupted
- No transaction support (partial writes possible on crash)

## Alternatives Considered

### SQLite
- Better query support, but adds complexity (WASM dependency, ~1MB)
- Not needed for the current single-user use case
- Available as optional adapter for future scaling

### In-Memory Only
- Faster, but no persistence
- Not acceptable for a tool that may take hours to complete

## References

- `src/storage/filesystem.ts` — Primary implementation
- `src/storage/sqlite.ts` — Optional SQLite adapter
- `src/storage/types.ts` — StorageProvider interface
