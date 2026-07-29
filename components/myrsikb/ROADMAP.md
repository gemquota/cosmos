# Triad Audit Resolution Roadmap

Addresses every issue from the comparative audits:
[ACE Pros](https://gist.github.com/...ace-audit) and
[Triad Cons](https://gist.github.com/...triad-audit).

---

## ✅ Resolved Already

| Issue | Audit | Fix |
|-------|-------|-----|
| `sys.path.insert` in 4 bridge modules | Triad/mykb con | Replaced with `importlib`-based `mykb_loader.py` — no global path mutation |

---

## 1. Search Infrastructure Sprawl (mykb)

**Problem:** 3 parallel search stacks (JS daemon, Python vdb, Python retriever), 10+ index files, overlapping formats.

### Implementation: Consolidate to Python stack, retire JS

**Decision:** The Python stack (`retriever.py` + `embedder.py` + `vectordb.py`) is what `myrsikb` uses. The JS stack (`daemon.js`, `extract.js`, `store.js`, `link-graph.js`) is unmaintained and unused.

**Actions:**

- [ ] Move JS files to `.wiki-daemon/archive/js-search/` with a deprecation notice
- [ ] Remove duplicate `search_chunks.json` + `search_index.json` + `search_meta.json` (JS-produced, superseded by `vdb.npz` + `vdb_tfidf.json`)
- [ ] Add `FORMAT.md` to `.wiki-daemon/` documenting the canonical index schema
- [ ] Add staleness check to `graph_engine.py`: compare graph timestamp vs newest entity/session mtime

### Format Canonicalization

| File | Format | Produced By | Status |
|------|--------|-------------|--------|
| `vdb.npz` | compressed numpy | `vectordb.py` | **Canonical** |
| `vdb_tfidf.json` | JSON | `embedder.py` | **Canonical** |
| `graph.json` | JSON | `graph_engine.py` | **Canonical** |
| `backlinks.json` | JSON | `backlinks.py` | **Canonical** |
| `timeline.json` | JSON | `temporal_engine.py` | **Canonical** |
| `search_chunks.json` | JSON | JS daemon | **Retire** → archive |
| `search_index.json` | JSON | JS daemon | **Retire** → archive |
| `search_meta.json` | JSON | JS daemon | **Retire** → archive |
| `search_vectors.npy` | numpy | JS daemon | **Retire** → archive |
| `vdb.json` | JSON | legacy vdb | **Retire** (superseded by `vdb.npz`) |

---

## 2. Causal Event Tracing (ACE Pro)

**Problem:** ACE has Lamport clocks + SHA-256 hash chains. RSIS3's pulse cycles are timestamped but have no causal linking — two cycles cannot be proven to be in sequence.

### Implementation: Lightweight causal chain on pulse cycles

- [ ] Each `pulse_id` already increments sequentially. Add a `causal_parent` field (previous `pulse_id`) and `cycle_hash = sha256(f"{prev_hash}:{pulse_id}:{goal}")` to cycle records
- [ ] Store in SQLite `cycles` table as new column `causal_hash TEXT`
- [ ] The cycle hash chain enables deterministic replay verification (ACE-style)

**Status:** The `cycles` table exists. Adding `causal_hash` and `parent_id` columns is a single migration.

---

## 3. Genesis Hash Identity (ACE Pro)

**Problem:** ACE's identity is a Genesis Hash anchored to the first event. RSIS3's identity is a JSON file with mutable layer scores — no cryptographic anchor.

### Implementation: Anchor identity to a genesis hash

- [ ] On first `SelfModel` init, generate `genesis_hash = sha256(f"{hostname}:{timestamp}:{version}")` stored in both `self_model.json` and a `.genesis_hash` file
- [ ] Every snapshot includes the genesis hash
- [ ] On load, compare stored genesis hash against `.genesis_hash`. Mismatch → crisis trigger
- [ ] This gives RSIS3 the same "Ship of Theseus" identity as ACE

**Status:** `SelfModel` already has `version`, `snapshot_count`, and `_save()`. Adding genesis hash is ~30 lines.

---

## 4. Temporal Horizon (ACE Pro)

**Problem:** ACE enforces a 4-hour temporal horizon — any goal exceeding 4 hours triggers Sovereign Panic. RSIS3 has no time bound on pulse cycles.

### Implementation: Configurable cycle time limit

- [ ] Add `max_cycle_duration` to pulse config (default: 4 hours)
- [ ] In `pulse_engine.py`, track cycle start time. If elapsed > max, auto-mark as HOLD with reason "temporal horizon exceeded"
- [ ] `RecoveryManager` already handles git rollback — wire the temporal horizon into rollback triggers

**Status:** ~40 lines in `pulse_engine.py` + config.

---

## 5. Dual KG Resolution

**Problem:** Two independent knowledge graphs — `LocalKnowledgeGraph` (SQLite, used by dashboard) and `memory_bridge.KnowledgeGraph` (mykb-backed, used by pulse engine). No sync between them.

### Options

| Option | Effort | Risk | 
|--------|--------|------|
| **A.** Replace dashboard KG with mykb-backed version | Medium | Dashboard read-only KG queries → can switch seamlessly |
| **B.** Sync both KGs via write bridge | Medium | Every write goes to both |
| **C.** Keep dual KG, add staleness warning | Low | Dashboard shows "last synced" timestamp |

**Recommendation: Option A** — the dashboard's KG endpoints (`/api/kg/*`) already delegate to `get_kb()` which returns `LocalKnowledgeGraph`. Replace that with the mykb-backed version. The SQLite tables remain for `rebirth/engine.py` archival but are no longer the primary query path.

---

## 6. Pulse Engine Automation

**Problem:** `pulse_engine.py` is interactive — `input()` for every phase. Cannot run headless.

### Implementation: Auto-evaluation mode

- [ ] Add `--auto` flag to `pulse_engine.py` that skips `input()` prompts
- [ ] Auto-mode generates evaluation phases from telemetry:
  - `goal_analysis` → from `GoalGenerator` output
  - `constraint_extraction` → from RRP state machine  
  - `ambiguity_assessment` → from last evaluation's ambiguity vector
  - `evaluation` → from test results (PASS if tests pass, HOLD otherwise)
- [ ] Existing `--phases phases.json` batch mode already works for non-interactive
- [ ] Add `PulseScheduler` support: `--auto --scheduled` runs the full cycle without any input

**Status:** Batch mode exists (`--phases`). Need to add phase auto-generation from telemetry.

---

## 7. Integration Tests

**Problem:** Zero tests exercise the RSIS3→myrsikb→mykb pathway.

### Implementation: Add integration test

- [ ] Create `rsis3/tests/test_memory_bridge.py`
- [ ] Test: `MemoryClient.store_identity_snapshot()` → verify wiki file created
- [ ] Test: `MemoryClient.store_pulse_memory()` → verify wiki/pulses/ entry
- [ ] Test: `KnowledgeGraph.create_node()` → verify mykb entity created
- [ ] Test: `MemoryClient.search()` → verify vector index returns results
- [ ] Each test creates a temp wiki, runs the bridge operation, asserts file exists + content correct, then cleans up

**Status:** ~150 lines of tests.

---

## 8. Versioning

**Problem:** RSIS3 v0.1.0, mykb unversioned, myrsikb unversioned — no coordination.

### Implementation: Version manifest

- [ ] Add `VERSION` file to each project root
- [ ] Add `myrsikb/version.py` with `__version__`, `__rsis3_version__`, `__mykb_version__` compatibility pins
- [ ] `MemoryClient.__init__` checks version compatibility on init (warning, not blocking)

**Status:** Trivial — 3 files, ~15 lines each.

---

## 9. mykb Rollback

**Problem:** RSIS3 can git-rollback its code. mykb wiki changes are irreversible.

### Implementation: Git-based wiki

- [ ] `mykb/wiki/` should be a git repository
- [ ] Add `hooks/pre-commit.py` that runs `kb_linter.py` on staged files
- [ ] `gap_detector.py` and other daemon scripts auto-commit after writes
- [ ] Rollback: `git revert` on a wiki page

**Status:** The wiki is NOT currently a git repo (2,385 files, unversioned). Making it one is a one-time `git init && git add && git commit`.

---

## 10. Pre-commit Validation for mykb

**Problem:** OKF conformance (YAML frontmatter, valid types, non-empty titles) is enforced only when `kb_linter.py` is explicitly run.

### Implementation: Git pre-commit hook

- [ ] Install `.wiki-daemon/kb_linter.py` as a pre-commit hook in the wiki repo
- [ ] Reject commits where frontmatter is malformed, required fields are missing, or tags are invalid
- [ ] Add `--fix` mode that auto-corrects common violations

**Status:** `kb_linter.py` exists. Needs hook integration + `--fix` mode.

---

## 11. Dual-Layer Metacognition (ACE Pro)

**Problem:** ACE has a "Subconscious Drawer" — debounced telemetry stream separate from conscious reasoning. RSIS3 has only conscious pulse cycles.

### Implementation: Pulse telemetry stream with debounce

- [ ] The `pulse_engine.py` integration in `myrsikb` already stores pulse memories
- [ ] Add a lightweight telemetry poller (separate thread) that writes status observations to a `wiki/telemetry/` stream
- [ ] Dashboard gains a "/subconscious" drawer that shows raw telemetry at reduced frequency (>100 events/min → debounce to 2Hz)
- [ ] This is what the `knowledge_weekly()` dashboard endpoint already approximates

**Status:** Foundation exists (pulse memory + dashboard). Needs the streaming + debounce layer.

---

## 12. Write-Enabled Dashboard API

**Problem:** Dashboard API is read-only for most resources — 12+ GET endpoints, no POST/PUT/DELETE for creation.

### Implementation: Add write endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/pulse/start` | POST | Kick off a pulse cycle |
| `/api/goals` | POST | Create a goal |
| `/api/goals/{id}` | PUT | Update goal status |
| `/api/identity/narrative` | PUT | Set narrative |
| `/api/kg/nodes` | POST | Create KG node |
| `/api/kg/edges` | POST | Create KG edge |

**Status:** Some exist (`/api/identity/narrative`, `/api/kg/nodes` via batch). Need the goal + pulse endpoints.

---

## 13. RRP State Machine — Wire or Prune

**Problem:** 2,025 lines of RRP state machine with capabilities no runtime calls (fork/merge, checkpoint, question quality indices, topic coverage bitmasks).

### Wire (recommended)

- [ ] `pulse_engine.py` auto-mode uses `RRPEngine` for constraint extraction and ambiguity vector calculation instead of interactive prompts
- [ ] `cli.py` exposes fork/merge/checkpoint commands
- [ ] Dashboard adds RRP session fork/merge UI

### Or Prune

- [ ] Remove functions not referenced by any call site
- [ ] Document the removed capabilities in ARCHITECTURE.md in case they're needed later

**Status:** The audit found specific uncalled capabilities. Either path is ~1 day of focused work.

---

## Priority Matrix

| Item | Impact | Effort | Do First |
|------|--------|--------|----------|
| ✅ sys.path.insert fix | High | 1h | ✅ Done |
| Genesis hash | Medium | 30min | After consolidation |
| Search consolidation | High | 1h | **Now** |
| Integration tests | High | 2h | Next |
| Temporal horizon | Medium | 1h | Next |
| Version manifest | Low | 30min | Whenever |
| Pulse engine auto-mode | High | 4h | Phase 2 |
| mykb git rollback | Medium | 1h | Phase 2 |
| Pre-commit hook | Medium | 2h | Phase 2 |
| Dual KG resolution | Medium | 3h | Phase 2 |
| Dashboard write API | Medium | 4h | Phase 3 |
| Dual-layer metacognition | Low | 4h | Phase 3 |
| RRP wire/prune | Medium | 8h | Phase 3 |

---

## Summary: ACE Pros Triad Gets

| ACE Feature | Triad Equivalent | Status |
|-------------|------------------|--------|
| Causal event system | Pulse cycle chain + causal_hash | Planned |
| Genesis Hash identity | Genesis anchor on SelfModel | **Implementing** |
| Temporal horizon | Cycle time limit + auto-HOLD | Planned |
| Swarm economy | Not applicable (single-agent architecture) | Won't do |
| Glyph visual logic | Not applicable | Won't do |
| AUSP FastAPI server | Dashboard API with write endpoints | Phase 3 |

## Summary: Triad Cons Removed

| Con | Resolution | Status |
|-----|-----------|--------|
| `sys.path.insert` | `mykb_loader.py` (importlib) | ✅ Done |
| Search infrastructure sprawl | Archive JS stack, canonicalize | **Implementing** |
| No integration tests | `test_memory_bridge.py` | Planned |
| No versioning | `VERSION` + `version.py` | Planned |
| No mykb rollback | Git wiki + pre-commit hook | Planned |
| Partial automation | `--auto` mode for pulse engine | Phase 2 |
| Dead code / over-engineering | RRP wire-or-prune audit | Phase 3 |
| Dual KG | Option A: mykb-backed dashboard | Phase 2 |
| Read-only API | Write endpoints | Phase 3 |
