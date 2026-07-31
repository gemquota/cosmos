# ADR 004: Artifact Key Validation

## Status

Accepted

## Date

2024-07-28

## Context

Artifact keys are plain strings with no validation. A typo in framework JSON (e.g., "entites" instead of "entities") produces an invalid artifact that downstream series silently fails to consume.

## Decision

Define a known set of artifact keys and validate them during extraction. Provide fuzzy-match suggestions for typos.

## Consequences

### Positive
- Catch typos at extraction time, not at consumption time
- Clear documentation of all valid artifact keys
- Suggestions help users fix mistakes quickly
- Prevents invalid artifacts from polluting the dictionary

### Negative
- Adds a validation step to every extraction
- Known keys must be updated when new artifacts are added
- Slightly increases code complexity

### Risks
- Known keys may become stale as the framework evolves
- False positives if framework uses custom artifact keys

## References

- `src/data/artifact-keys.ts` — Key validation and fuzzy matching
- `src/data/artifact-extractor.ts` — Extraction with validation
