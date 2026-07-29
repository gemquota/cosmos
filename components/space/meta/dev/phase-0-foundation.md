# Phase 0: Foundation — Development Guide

**Spec References:** `specs/01-data-schema.md`, `specs/02-architecture.md`
**Prerequisites:** None
**Estimated Effort:** 2–3 weeks
**Sprint Count:** 2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Establish the canonical data model, fix all known bugs from the audit, remove data duplication, implement template variable interpolation, create the CLI entry point, and set up project scaffolding conventions. This phase creates the foundation every subsequent phase builds on.

---

## Task List

### Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 0.T1 | Define Schema v2 TypeScript types | 01 §4 | M | — | All types compile; JSDoc complete |
| 0.T2 | Write JSON Schema validator for framework files | 01 §5 | M | 0.T1 | Validates all 7 original JSON files |
| 0.T3 | Implement v1 → v2 migration function | 01 §5.1 | L | 0.T1, 0.T2 | Round-trip v1→v2→v1 produces equivalent data |
| 0.T4 | Consolidate data files (remove duplication) | — | S | — | Single copy of each JSON; all imports updated |
| 0.T5 | Fix consolidate-spec.sh broken JSON merging | 03 §3 | M | — | Script produces valid JSON from answer directories |
| 0.T6 | Implement template variable interpolation | 02 §3 | M | 0.T1 | MD context variables resolve against artifact dictionary |
| 0.T7 | Create SPACE configuration system | 02 §4.4 | M | 0.T1 | Config loads from file/env/defaults with precedence |
| 0.T8 | Scaffold CLI with commander.js | 04 §3.1 | M | 0.T7 | `space --help` shows all commands |
| 0.T9 | Implement `space init` command | 04 §3.1 | M | 0.T8 | Creates valid project directory structure |
| 0.T10 | Implement `space framework` inspection command | 04 §3.1 | S | 0.T8 | Shows framework stats and series info |
| 0.T11 | Set up Vitest test infrastructure | — | S | — | `npm test` runs and passes |
| 0.T12 | Set up TypeScript build pipeline | — | M | — | `npm run build` produces dist/ with types |

### Task Details

#### 0.T1: Define Schema v2 TypeScript Types

**What:**
Create `src/types/` directory with all TypeScript interfaces matching `specs/01-data-schema.md` §5. Includes `FrameworkDefinition`, `SeriesDefinition`, `RoundDefinition`, `OpenEndedQuestion`, `MultiChoice`, `SessionState`, `AnswerEntry`, `ArtifactDictionary`, `Project`, and all sub-types.

**Files:**
- `src/types/framework.ts` — Framework definition types
- `src/types/session.ts` — Session state types
- `src/types/project.ts` — Project types
- `src/types/events.ts` — Event types
- `src/types/index.ts` — Re-exports all types

**Implementation Notes:**
- Use `readonly` modifiers on definition types (they're immutable)
- Use branded types for IDs where possible (`type SessionId = string & { __brand: 'SessionId' }`)
- Export all types; no default exports

**Done When:**
- [ ] All types compile with strict TypeScript settings
- [ ] Every interface has JSDoc describing its purpose
- [ ] All fields have inline comments for non-obvious semantics

---

#### 0.T2: Write JSON Schema Validator for Framework Files

**What:**
Create JSON Schema definitions that validate the original framework data files. Use these to validate both v1 (original) and v2 (migrated) formats.

**Files:**
- `src/schemas/framework-v1.schema.json` — v1 validation
- `src/schemas/framework-v2.schema.json` — v2 validation
- `src/schemas/series-v1.schema.json` — per-series v1 validation
- `src/schemas/series-v2.schema.json` — per-series v2 validation
- `src/validator.ts` — Validation function

**Implementation Notes:**
- Use `ajv` for JSON Schema validation
- Validation returns structured errors, not thrown exceptions
- Support strict mode (all rules) and lenient mode (warnings only)

**Done When:**
- [ ] All 7 original JSON files pass v1 schema validation
- [ ] Migrated v2 files pass v2 schema validation
- [ ] Invalid data produces clear error messages with path info
- [ ] Unit tests for each validation rule

---

#### 0.T3: Implement v1 → v2 Migration Function

**What:**
Build a function that reads the original 7 JSON files + `framework.json` and produces a single `framework-v2.json` file conforming to the Schema v2 `FrameworkDefinition` type.

**Files:**
- `src/migration/v1-to-v2.ts` — Migration function
- `src/migration/index.ts` — Migration entry point

**Implementation Notes:**
- Read `framework.json` for metadata and dependency edges
- Read each `json/01-07-*.json` for series definitions
- Merge dependency_chain.edges into DependencyGraph format
- Preserve all original question IDs exactly
- Create `consumes`/`provides` on each series from edge data

**Done When:**
- [ ] Migration produces valid v2 FrameworkDefinition
- [ ] All 326 question IDs preserved
- [ ] Dependency graph matches original framework.json edges
- [ ] Round-trip test: v1 → v2 → re-derive v1-equivalent data

---

#### 0.T4: Consolidate Data Files

**What:**
Remove the 48KB data duplication by keeping only one copy of each series JSON and updating all imports to use the canonical location.

**Files:**
- Delete: `prompt-app/src/data/*.json` (redundant copies)
- Keep: `json/01-07-*.json` (canonical)
- Update: `prompt-app/src/data/loader.js` — import from `../../json/`

**Implementation Notes:**
- Verify byte-for-byte identity before deleting
- Update Vite config if needed to resolve cross-directory imports
- Update `prompt-app/src/data/loader.js` import paths

**Done When:**
- [ ] No duplicate data files exist
- [ ] All imports resolve correctly
- [ ] `npm run build` in prompt-app still works

---

#### 0.T5: Fix consolidate-spec.sh

**What:**
Rewrite the consolidation script to properly merge answer JSON files without producing invalid JSON.

**Files:**
- `consolidate-spec.sh` (rewrite)

**Implementation Notes:**
- Replace naive JSON concatenation with proper `jq` or `python3` merge
- Each `series-answers.json` is a complete JSON object — merge into a parent
- Validate output JSON before writing
- Add error handling for missing directories/files

**Done When:**
- [ ] Script produces valid JSON from well-formed input
- [ ] Script handles missing files gracefully (warns, continues)
- [ ] Script handles malformed JSON gracefully (skips, warns)

---

#### 0.T6: Implement Template Variable Interpolation

**What:**
Build a template resolver that takes a string containing `{artifact_key}` placeholders and an `ArtifactDictionary`, returning the resolved string.

**Files:**
- `src/template/resolver.ts` — Core resolver
- `src/template/patterns.ts` — Regex patterns for template vars
- `tests/template/resolver.test.ts` — Tests

**Implementation Notes:**
- Pattern: `\{([a-z_]+)\}` matches artifact references
- Unresolved variables become `[Not yet determined: {key}]`
- Support nested resolution: artifact value may itself contain templates
- Max recursion depth: 5 (prevent infinite loops)
- Handle the specific context lines from MD files (lines 3-7 of md/02-07)

**Done When:**
- [ ] Resolves known artifact keys to their values
- [ ] Unresolved keys show placeholder with key name
- [ ] Circular references detected and broken
- [ ] All 6 MD context lines resolve correctly with test data

---

#### 0.T7: Create Configuration System

**What:**
Implement a configuration loader that merges settings from three sources with clear precedence: CLI flags > environment variables > config file > defaults.

**Files:**
- `src/config/defaults.ts` — Default values
- `src/config/loader.ts` — Merge logic
- `src/config/schema.ts` — Config validation schema
- `src/config/index.ts` — Public API

**Implementation Notes:**
- Config file location: `~/.space/config.json`
- Environment prefix: `SPACE_` (e.g., `SPACE_LLM_PROVIDER=openai`)
- CLI flags use kebab-case: `--llm-model gpt-4o`
- Config is immutable after load (frozen object)

**Done When:**
- [ ] Defaults work out of the box
- [ ] Config file overrides defaults
- [ ] Env vars override config file
- [ ] CLI flags override everything
- [ ] Invalid config produces clear error messages

---

#### 0.T8–0.T12: CLI Scaffolding and Tooling

**What:**
Set up the CLI framework, project init command, framework inspection, testing infrastructure, and TypeScript build pipeline.

**Files:**
- `src/cli/index.ts` — CLI entry point with commander.js
- `src/cli/commands/init.ts` — `space init`
- `src/cli/commands/framework.ts` — `space framework`
- `src/cli/commands/version.ts` — `space version`
- `vitest.config.ts` — Test configuration
- `tsconfig.json` — TypeScript configuration
- `package.json` — Updated with scripts and dependencies

**Done When:**
- [ ] `npx space --help` shows all commands
- [ ] `npx space init test-project` creates valid directory
- [ ] `npx space framework` shows stats
- [ ] `npm test` runs all tests
- [ ] `npm run build` produces typed output

---

## Dependencies

```
0.T1 ──┬──▶ 0.T2 ──▶ 0.T3
       │
       ├──▶ 0.T6
       ├──▶ 0.T7 ──▶ 0.T8 ──▶ 0.T9
       │                ├──▶ 0.T10
       │                │
0.T4   │                │
0.T5   │                │
0.T11  │                │
0.T12  │                │
```

---

## Testing

- Run `npm test` after each task
- `npm run build` must always pass
- JSON Schema validation test runs on every framework file

## Risks

- Schema v2 design changes may cascade — lock down types in 0.T1 before proceeding
- Template resolver complexity — keep scope limited to simple variable substitution in Phase 0
