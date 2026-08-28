# COSMOS — Adversarial Verification & Evidence Audit

*Independent verification of claims from the initial reconnaissance report.*
*Evidence gathered from direct code inspection, test execution, and runtime state examination.*
*No code changes made.*

---

## 1. System Model Verification

### Claim: "COSMOS is a 9-loop recursive self-improvement system"
**VERDICT: PARTIALLY VERIFIED**

Evidence: All 9 loops (L1–L9) exist as implemented Python modules with concrete `run_cycle()` methods. The CLI dispatches to each. However:

- **L1–L3** have real, exercised code paths (tested, with runtime state artifacts).
- **L4–L5** have real tuning logic (tested in isolation).
- **L6–L9** have real signal detection and parameter clamping logic (tested in isolation).
- **None of L4–L9 have been run in production.** The `.rsis/` directory is empty. No `optimizer_state.json`, `strategies.json`, `identity_state.json`, `metacog_state.json`, `metameta_state.json`, or `mmm_state.json` files exist. The loops are implemented but never executed end-to-end.

### Claim: "+3 diagonal architecture is the key insight"
**VERDICT: VERIFIED (structurally)**

The code explicitly declares this. `config.py` defines `L1_TUNABLES`, `L2_TUNABLES`, `L3_TUNABLES`, `L4_TUNABLES`, `L5_TUNABLES`, `L6_TUNABLES` with ownership comments. Each higher loop imports its target's tunables:
- L4 imports `L1_TUNABLES` (line `from rsis.config import CONFIG, L1_TUNABLES`)
- L5 imports `L2_TUNABLES`
- L6 imports `L3_TUNABLES`
- L7 imports `L4_TUNABLES`
- L8 imports `L5_TUNABLES`
- L9 imports `L6_TUNABLES`

**However:** The diagonal is incomplete in practice. L1 only exposes 2 tunables (`max_retries`, `max_tool_calls`), L2 exposes 1 (`max_attempts`), L3 exposes 1 (`plateau_timeout_s`). The higher loops tune a very small parameter space.

### Claim: "The evaluator is immutable and authoritative"
**VERDICT: PARTIALLY VERIFIED — see Section 4**

### Claim: "L3 writes synthesis notes to MyKB"
**VERDICT: VERIFIED**

`loop_l3.py` `_write_mykb_consolidation()` writes OKF synthesis notes to `components/mykb/wiki/syntheses/` and appends to `log.md`. This is real, tested code.

---

## 2. Actual Execution Paths

### `run` command
```
cmd_run() → _init_subsystems() → L2ImprovementLoop.run_session(goal) → 
  _generate_candidate() → evaluator.evaluate() → _apply_improvement()
→ L1ActionLoop.execute(goal) → _plan_next_action() → _execute_tool()
```

**Critical finding:** L2's `_generate_candidate()` is **deterministic** by default. It either:
1. Parses a target from the goal regex (`Implement <Name> in <path>`)
2. Runs `StubDetector.scan_by_priority()` to find missing modules
3. Returns `None` if no target exists

The LLM path (`_llm_generator()`) requires `RSIS_L2_LLM_GENERATOR` env var pointing to a module with `generate_candidate`. **This is never set by default.** The system cannot generate genuine code improvements without external LLM wiring.

**The evaluator gate:** Every candidate (deterministic or LLM-generated) is sent to `evaluator/evaluator.py` via subprocess. The evaluator performs:
1. Path safety check (no absolute paths, no `..` escapes)
2. Syntax compilation (`compile()`)
3. AST safety scan (unsafe calls like `eval`, `exec`, `os.system`)
4. Style heuristics (line length, trailing whitespace, TODO markers)
5. Efficiency heuristics (no-op functions, catch-all signatures)
6. Regression check (removes existing code → FAIL)
7. Optional LLM refinement (requires `RSIS_EVALUATOR_API_KEY`)

**Hard gates fail closed:** syntax errors, unsafe patterns, and code removal always produce FAIL. The LLM cannot overturn a deterministic FAIL.

**But:** The deterministic gate passes trivial scaffolds. A `def helper(): return None` scaffold scores perfectly. The evaluator rewards compilable, safe, non-regressive code — which is a low bar.

### `evolve` command (L3)
```
cmd_evolve() → L3EvolutionLoop.run_cycle() →
  _detect_trends() → _consolidate_memory() → _evolve_strategies() → 
  _refine_redundancies() → memory.save() → _write_mykb_consolidation()
```

L3 reads from `TelemetryExtrapolator` (parses `.rsis/telemetry/*.jsonl`), writes to KG and MyKB. **No evaluator gate for L3 itself.** L3 is the only core loop that modifies the knowledge graph without evaluator approval.

### `optimize` command (L4)
```
cmd_optimize() → OptimizerLoop.run_cycle() →
  aggregate_outcomes(memory.kg) → _propose_deltas() → 
  evaluator.evaluate(deltas) → _apply() → _save_state()
```

L4 reads KG insights, proposes bounded deltas to L1 tunables, gates through evaluator, persists to `.rsis/optimizer_state.json`. **The evaluator receives JSON deltas, not Python code.** The evaluator's `_is_data_candidate()` recognizes JSON payloads and applies shape + destructive-string checks only (no syntax/safety/AST checks).

### `strategies` command (L5)
```
cmd_strategies() → EvolutionLoop.run_cycle() →
  _seed_from_l3() → _score() → _mutate()/_recombine() →
  evaluator.evaluate() → _save_state()
```

Population-based evolutionary strategy. Fitness is a blend of KG outcome success_rate and avg_score. Mutations adjust `l2_attempts`, `budget_factor`, `focus`. **Gated through evaluator (JSON data path).**

### `identity` command (L6)
```
cmd_identity() → IdentityLoop.run_cycle() →
  aggregate_outcomes() → detect_regression_trends() → _signal() →
  evaluator.evaluate() → _save_state()
```

Reads KG outcomes and regression trends. Signal: "shrink" (regressions or low success) → decrease L3 plateau timeout; "grow" (high success) → increase. **Gated through evaluator.**

### `metacog` (L7), `metameta` (L8), `mmm` (L9)
All follow the same pattern: read lower-loop state, detect signal (oscillation/stall), propose parameter deltas, gate through evaluator, persist.

**Key observation:** L7–L9's signal detection reads *history* from state files of the loop they tune. L7 reads `optimizer_state.json` (L4), L8 reads `strategies.json` (L5), L9 reads `identity_state.json` (L6). These state files are empty because the target loops have never run.

### `cycle-daemon`
```
cmd_cycle_daemon() → run_forever() →
  CycleLock.acquire() → run_one_cycle() → launch.run_batch() →
  (each loop as subprocess) → maybe_auto_retune() → _commit_cycle()
```

The daemon uses an fcntl lockfile for mutual exclusion. It runs the full L1–L9 batch, optionally commits artifacts, and auto-retunes from convergence proposals.

---

## 3. +3 Diagonal Invariant Verification

### Formal Invariant Table

| Tuning Loop | Target Loop | Tunables Owned | Bounds | Source File | Evaluator-Gated | State File | Never Run |
|-------------|------------|----------------|--------|-------------|-----------------|------------|-----------|
| L4 | L1 | `max_retries` [1,8], `max_tool_calls` [5,25] | config.py L1_TUNABLES | Yes (JSON) | `.rsis/optimizer_state.json` | Yes |
| L5 | L2 | `max_attempts` [2,10] | config.py L2_TUNABLES | Yes (JSON) | `.rsis/strategies.json` | Yes |
| L6 | L3 | `plateau_timeout_s` [3600,172800] | config.py L3_TUNABLES | Yes (JSON) | `.rsis/identity_state.json` | Yes |
| L7 | L4 | `outcome_window` [5,50], `min_outcomes` [2,20], `target_success_low` [0.3,0.7], `target_success_high` [0.7,0.95] | config.py L4_TUNABLES | Yes (JSON) | `.rsis/metacog_state.json` | Yes |
| L8 | L5 | `mutation_rate` [0.05,0.6], `population_size` [4,16] | config.py L5_TUNABLES | Yes (JSON) | `.rsis/metameta_state.json` | Yes |
| L9 | L6 | `shrink_below` [0.2,0.6], `grow_above` [0.6,0.95] | config.py L6_TUNABLES | Yes (JSON) | `.rsis/mmm_state.json` | Yes |

**Mutation path for L4 → L1:**
1. Tunables declared: `L1_TUNABLES` dict in `config.py`
2. Bounds declared: min/max tuples in the same dict
3. Proposed values: `_propose_deltas()` in `loop_l4.py` adjusts by step size toward success target band
4. Validated: Clamped to `[lo, hi]` in `_propose_deltas()` and again at apply
5. Evaluator-gated: `evaluator.evaluate()` subprocess — JSON data path (shape + destructive-string checks)
6. Persisted: `_save_state()` writes `.rsis/optimizer_state.json`
7. Loaded at startup: `_apply_tuned_state()` in `config.py` reads all state files and applies clamped values
8. Runtime effect: Direct `setattr()` on `CONFIG.l1.*` after apply

**Critical finding: Evaluator validation for JSON data candidates is weak.** When the evaluator receives JSON (L4–L9 tuning deltas), it only checks:
- Valid JSON structure
- No destructive shell strings in values
- The rest is a shape check

It does NOT validate that the proposed value is within bounds (the loop does that itself), nor that the value would produce sensible behavior. **The evaluator cannot reject a parameter change that would degrade system performance.**

**Invalid value reachability:** A value outside bounds cannot reach execution because `_apply()` clamps with `max(lo, min(hi, ...))` and `_apply_tuned_state()` also clamps on startup. This is a defense-in-depth, but the evaluator is not the mechanism that enforces it.

---

## 4. Evaluator Gate Audit

### What the evaluator actually evaluates
- **Python code candidates (L2):** Syntax, AST safety (unsafe calls, subprocess patterns), style heuristics, regression heuristics, path safety
- **JSON data candidates (L4–L9):** Shape validation, destructive string detection
- **Optional LLM refinement:** Requires API key; overlays additional scoring but cannot overturn hard FAILs

### Can the evaluator itself be modified?
**The evaluator file (`evaluator/evaluator.py`) is not in the L2 improvement target set.** L2's `_resolve_target()` uses `StubDetector` which scans for `missing_module` — the evaluator is a complete, existing file. L2's deterministic generator only creates *new* files for missing modules. **However:** There is no structural protection preventing L2 from targeting `evaluator/evaluator.py` if a goal explicitly names it. The checkpoint-before-mutation invariant would allow rollback, but the evaluator subprocess would run the modified code for one evaluation cycle.

**The evaluator reads its own source file on startup for `self_verify()` (SHA-256 digest check), but this is opt-in** (`--verify` flag). It is NOT called during normal evaluation. The `CONFIG.evaluator.startup_digest_verify` flag exists but the `EvaluatorClient.verify_integrity()` method is never called automatically.

### Does it test semantic correctness?
**No.** It tests structural properties: compilability, absence of dangerous patterns, basic style heuristics. A scaffolded `def helper(): return None` passes all gates. The evaluator cannot distinguish between a trivial no-op and a meaningful improvement.

### Can scaffolded candidates pass?
**Yes, trivially.** The deterministic generator produces:
```python
"""Module scaffold generated by the RSIS L2 improvement loop."""
def symbol(*args, **kwargs):
    """symbol — production implementation."""
    return None
```
This compiles, has no unsafe patterns, has no style issues, and doesn't remove any existing code. It passes the evaluator with perfect scores.

### Fail closed or open?
**Fail closed for hard gates.** Syntax errors, unsafe patterns, and code removal always FAIL. **Fail open for quality assessment.** Trivial scaffolds pass. The evaluator is a safety gate, not a quality gate.

### What prevents optimizing toward satisfying the evaluator?
**Nothing structural.** The L2 deterministic generator inherently optimizes for "compilable, safe, non-regressive" because that's all it produces. The evaluator rewards exactly that. This is a local optimum trap: the system will generate trivial scaffolds that satisfy the evaluator indefinitely, never producing meaningful improvements.

The evaluator's `_style_check()` penalizes `pass`, `...`, `NotImplementedError`, and TODO markers, but the scaffold generator avoids these. The `_efficiency_check()` penalizes no-op functions, but the generator's functions have docstrings (which count as non-trivial body statements).

---

## 5. LLM Dependence — The Central Finding

### Is an LLM configured?
**No.** In the default configuration:
- `RSIS_L2_LLM_GENERATOR` is not set → L2 uses deterministic scaffolding
- `RSIS_EVALUATOR_API_KEY` / `OPENAI_API_KEY` are not set → evaluator runs deterministic-only
- No other LLM provider is wired

### What percentage of candidate generation depends on LLM?
**0% in default configuration.** 100% of L2 candidate generation is deterministic scaffolding.

### What happens when the LLM is unavailable?
**The system works identically.** The LLM is a pure optional enhancement. All paths degrade gracefully to deterministic behavior.

### Does the system silently fall back to deterministic scaffolding?
**Yes.** `_llm_generator()` returns `None` when `RSIS_L2_LLM_GENERATOR` is not set, and `_generate_candidate()` falls through to `_resolve_target()` → `_scaffold_module()`.

### Is historical evidence of genuine LLM-generated modifications available?
**No.** The `.rsis/` directory is empty. No runtime artifacts exist. The `rack/attestations/` JSONL files are attestations of development phases, not LLM-generated improvements.

### Conclusion on RSI capability
**The system's RSI capability is ASPIRATIONAL.** The architecture for self-improvement is fully implemented — the loops, the evaluator gate, the checkpoint/rollback, the parameter tuning — but the actual improvement mechanism (LLM-generated code modifications) is not wired. Without an LLM, the system can only:
1. Scaffold trivial placeholder modules (deterministic L2)
2. Tune its own numeric parameters (L4–L9)
3. Detect regressions and adjust timing (L6–L9)

The parameter tuning (L4–L9) is real RSI in a narrow sense: the system can adjust its own numeric configuration based on observed outcomes. But it cannot modify its own code, fix bugs, add features, or make architectural changes without an LLM.

---

## 6. High-Severity Finding Verification

### P1: KG Write Amplification
**VERIFIED → PARTIALLY MITIGATED**

The previous session added a `_dirty` flag to `KnowledgeGraph`. Now `add_node`/`add_edge` mark dirty but don't persist. `save()` writes only when dirty. However, `MemoryManager.record_improvement()` still calls `self.save()` after every single improvement recording (line: `self.save()` at end of `record_improvement()`). This means the dirty flag is circumvented when `record_improvement` is called — each improvement triggers a full KG + vector store save.

**Measurement:** `.rsis/` is empty — no runtime data to measure. Unmeasured.

### P2: Silent Corrupted-State Fallback
**VERIFIED**

`_apply_tuned_state()` in `config.py` catches all exceptions when reading state files and falls back to defaults with `logger.warning()`. If a state file is corrupted (truncated JSON, wrong schema), the system silently uses defaults and continues. This is documented behavior but could mask configuration drift.

### P3: preexec_fn + Threading Safety
**PARTIALLY MITIGATED**

The previous session added `os.setsid()` with `os.setpgrp()` fallback. The `os.setsid()` call is safe in threaded programs (creates a new session, not a new process group). However, the fundamental issue remains: `preexec_fn` runs in the forked child process after `fork()` but before `exec()`, and in a threaded program the fork only copies the calling thread. Other threads' state is undefined in the child. The `os.setsid()` call itself is thread-safe, but the `preexec_fn` pattern in threaded programs is inherently fragile.

**Impact:** Low in practice because the sandbox subprocess is short-lived and doesn't interact with parent threads.

### P4: Scope Expansion / Untested Subsystems
**VERIFIED**

Phase manifest confirms:
- Phases 0–6 (core): tested
- Phases 7–15 (extended): some tested (validate, seasons, convergence, budgets, federation, forecast), some not (verify server, anomalies, policy)
- Phases 16–27 (epoch 1): aspirational, no tests, no integration

The `rack/` directory has 38 subdirectories for various subsystems (approvals, attestation, bridge, capacity, codesign, crisis, diplomacy, etc.). Most contain template/config files but no evidence of runtime use.

### P5: +3 Diagonal Cascading Instability
**CANNOT BE ASSESSED — no runtime data**

The tuning chains (L9 → L8 → L7 → L6 → L5 → L4 → L3 → L2 → L1) have never been executed. Cascading instability is theoretically possible if upper loops converge on extreme parameter values, but the bounded clamping in `_apply_tuned_state()` and `_apply()` methods provides defense. Without runtime data, this remains a theoretical risk.

### P6: Evaluator Weakness for JSON Data Candidates
**NEWLY DISCOVERED**

When L4–L9 submit JSON deltas through the evaluator, the `_is_data_candidate()` path applies minimal validation: destructive string detection and basic JSON parsing. The evaluator cannot assess whether a parameter change is *wise* — only whether it's *safe* (no shell injection). The actual value validation is the `[lo, hi]` clamping in the loop code itself.

### P7: Concurrent State-File Mutation
**NEWLY DISCOVERED**

No file-level locking exists for:
- `.rsis/optimizer_state.json` (L4 reads, L7 reads)
- `.rsis/strategies.json` (L5 reads/writes, L8 reads)
- `.rsis/identity_state.json` (L6 reads/writes, L9 reads)
- `.rsis/knowledge_graph.json` (L3 writes, L4 reads via KG)
- `.rsis/costs.jsonl` (append-only, multiple writers)

The cycle daemon uses a lockfile to prevent parallel full-cycle runs. But individual commands (`optimize`, `strategies`, etc.) have no locking. Running `optimize` in two terminals simultaneously would race on `optimizer_state.json`.

**Impact:** Medium. The cycle daemon prevents this in normal operation. Manual parallel execution is the risk.

### P8: Unbounded KG Growth
**PARTIALLY MITIGATED**

L3's `_refine_redundancies()` now caps new flags per cycle with `max_redundancy_flags_per_cycle`. But L3's `_consolidate_memory()` adds one insight node per recent session (up to 5), and `_detect_trends()` adds one node per high-severity regression trend. There is no pruning of old insight nodes. Over many cycles, the KG will grow monotonically.

**Impact:** Low in short term (KG is small), High in long term (unbounded growth → serialization overhead → slow saves).

---

## 7. Performance Quantification

### Runtime State
- `.rsis/` directory: **empty** (no runtime state files)
- `rack/pulses/`: 1 dashboard-data.json, 1 latest.json, 1 pulse-001.json (pre-existing, not generated by runtime)
- `rack/attestations/`: 17 daily JSONL files (346 bytes each), 1 chain.jsonl (2718 bytes) — total 8.9 KB
- Total `.rsis/` state: **0 bytes** (uninitialized)
- Knowledge graph nodes/edges: **0** (fresh)
- Vector store documents: **0** (fresh)

**All performance claims from the reconnaissance are UNMEASURED.** No runtime data exists to profile.

### Theoretical Concerns
- KG serialization: O(nodes + edges) JSON dump. With current zero state, trivial. At 10K nodes, the JSON serialization could take seconds.
- Vector store search: O(documents × dim) matrix multiply. At 10K documents with dim=256, this is ~2.5M floating-point operations — fast on modern hardware.
- Telemetry JSONL growth: Append-only, unbounded. At one pulse every 3 minutes, ~480 pulses/day, ~5 KB/pulse → ~2.4 MB/day.

---

## 8. State Integrity Audit

### State Files Map

| File | Producer | Consumer | Schema | Atomic Write | Corruption Handling | Lock |
|------|----------|----------|--------|-------------|-------------------|------|
| `.rsis/optimizer_state.json` | L4 | L4 (load), L7 (read history), `_apply_tuned_state` | `{params, history, cycle}` | No (direct write) | Log warning, reset to defaults | None |
| `.rsis/strategies.json` | L5 | L5 (load), L8 (read history), `_apply_tuned_state` | `{generation, population, history}` | No (direct write) | Log warning, reseed | None |
| `.rsis/identity_state.json` | L6 | L6 (load), L9 (read history), `_apply_tuned_state` | `{params, history, cycle}` | No (direct write) | Log warning, reset | None |
| `.rsis/metacog_state.json` | L7 | L7 (load) | `{params, history, cycle}` | No (direct write) | Log warning, reset | None |
| `.rsis/metameta_state.json` | L8 | L8 (load) | `{params, history, cycle}` | No (direct write) | Log warning, reset | None |
| `.rsis/mmm_state.json` | L9 | L9 (load) | `{params, history, cycle}` | No (direct write) | Log warning, reset | None |
| `.rsis/knowledge_graph.json` | L3, L1 (via memory) | L4, L5, L6, L7, L9 (via KG queries) | `{nodes, edges}` | **Yes** (tmp+rename) | Log warning, start fresh | None |
| `.rsis/vectors/index.json` | VectorStore | VectorStore | `{documents, embeddings}` | No (direct write) | Log warning | None |
| `.rsis/costs.jsonl` | CostLedger | CostLedger, evaluator | JSONL append | N/A (append) | Truncate recovery | None |
| `.rsis/telemetry/*.jsonl` | TelemetryCollector | TelemetryExtrapolator, SelfAssess | JSONL append | N/A (append) | Truncate recovery | None |

**Critical: State file disjointness is verified.** Each loop has its own state file. No loop writes to another loop's state file directly. The tuning relationship is:
- Higher loop writes to its own state file
- Lower loop reads the higher loop's state at startup via `_apply_tuned_state()`

**But:** The state files lack versioning, schema migration, and backup. A schema change in state format would silently corrupt the tuning chain until the file is reset.

---

## 9. Concurrency Audit

### Concurrency Matrix

| Resource | Multiple Readers | Multiple Writers | Locking | Atomic Write | Race Risk |
|----------|-----------------|------------------|---------|-------------|-----------|
| `optimizer_state.json` | L4, L7 | L4 only | None | No | Low (sequential in daemon) |
| `strategies.json` | L5, L8 | L5 only | None | No | Low |
| `identity_state.json` | L6, L9 | L6 only | None | No | Low |
| `knowledge_graph.json` | L3, L4, L5, L6 | L3 only | None | **Yes** | Low |
| `vectors/index.json` | VectorStore | VectorStore | None | No | Low |
| `costs.jsonl` | CostLedger | CostLedger | None | Append | Low |
| Git working tree | N/A | CheckpointManager | None | N/A | **Medium** (parallel commands) |
| MyKB files | MyKBGateway | MyKBGateway, L3 | None | No | Low (single daemon) |

**The cycle daemon's `CycleLock` (fcntl) is the primary concurrency control.** It prevents parallel full-cycle runs. Individual commands executed outside the daemon have no locking.

---

## 10. Test Coverage Audit

### Test Suite Summary
- **371 tests pass, 1 skipped, 0 failures** (after previous session's fixes)
- **42 test files**, ~5,473 lines of test code

### What IS tested
- Evaluator gate: comprehensive (319 lines) — syntax, safety, style, regression, path safety, diff handling, data candidates
- L1 retry logic, tool routing, sandbox
- L2 improvement cycle, candidate generation, application
- L3 idempotency, redundancy refinement
- KG robustness (atomic writes, concurrent access, dedup)
- Vector store operations
- Shared memory (CAS, versioning, thread safety)
- Event bus, priority pool, scheduler
- Timeout enforcement (polling watchdog)
- Self-assessment, convergence, forecast, anomaly detection
- Policy, budgets, federation, invariants, seasons
- Users, validation, projects, bridge

### What is NOT tested
- **L4–L9 end-to-end tuning chains** (each loop is tested in isolation, but the full diagonal chain L9→L6→L3→L1 has never been tested)
- **Cross-loop state propagation** (L4 writes state → `_apply_tuned_state` → L1 uses new params)
- **Runtime behavior with actual state files** (all tests use mock/tmp paths)
- **Concurrent command execution** (no multi-process tests)
- **Long-running daemon behavior** (ops_daemon tested for lock/backoff, not for sustained operation)
- **MyKB integration** (gateway tested, but actual MyKB HTTP server not tested in integration)
- **Evaluator digest verification** (`self_verify` tested indirectly but not as a startup gate)

### What dangerous behavior could change undetected?
1. **Evaluator logic degradation** — if `evaluator.py` is modified (e.g., by a future L2 improvement), the test suite uses `importlib.util.spec_from_file_location` to load the exact file, so tests would catch changes. This is good.
2. **Parameter bound violations** — the `_apply()` clamping is tested implicitly through unit tests, but no test verifies that `_apply_tuned_state()` correctly clamps all values on startup.
3. **State file format drift** — no schema validation test ensures state files remain compatible across versions.

---

## 11. Architectural Invariants

| Invariant | Enforcement Mechanism | Test | Failure Consequence |
|-----------|----------------------|------|-------------------|
| Checkpoint before mutation | `CONFIG.checkpoint_before_mutation` flag + `checkpoint()` call in every loop | test_kg_robustness, test_launch | No rollback possible |
| Evaluator immutability | No structural protection; relies on L2 not targeting `evaluator/evaluator.py` | None specific | Modified evaluator could pass unsafe code |
| +3 diagonal tuning bounds | `[lo, hi]` clamping in `_TUNABLES` and `_apply()` | Indirect (unit tests) | Out-of-range parameters |
| State file disjointness | Each loop writes only its own state file | Verified by code inspection | Cross-loop state corruption |
| Atomic KG writes | `tmp` + `os.replace()` | test_kg_robustness | Truncated/corrupted KG |
| Fail-closed evaluator | Hard gates return FAIL on any violation | test_evaluator_gate (comprehensive) | Unsafe code passes |
| Concurrent cycle exclusion | fcntl lockfile in CycleLock | test_ops_daemon | Parallel cycles race |

### Invariants documented but NOT enforced:
1. **Evaluator digest verification** — `startup_digest_verify` flag exists but is never checked automatically. The `EvaluatorClient.verify_integrity()` method exists but is never called.
2. **Budget enforcement** — `Budget` class tracks iterations and time, but the `max_iterations` limit is checked via `budget.tick()` which can be bypassed if the loop doesn't check it.
3. **Cost cap** — `budget_cap_usd` is enforced in `EvaluatorClient.evaluate()` but only for the evaluator call, not for other LLM calls.

---

## 12. Contradiction Audit

### Documentation vs. Implementation

| Claim | Source | Reality | Severity |
|-------|--------|---------|----------|
| "RSIS3 is a recursive self-improvement system" | README, docs | Architecture for RSI is implemented; actual improvement mechanism (LLM) is not wired | HIGH |
| "The evaluator is immutable" | docs, comments | No structural protection; evaluator file can be targeted by L2; digest verification is opt-in | MEDIUM |
| "L4–L9 tune lower-loop parameters" | docs, code comments | Implemented but never executed; no runtime evidence | MEDIUM |
| "Pipeline of 25 named nodes" | completion report | `pipeline.py` is a DAG worker pool, not a 25-node pipeline. The "25 nodes" claim appears to come from an earlier design. | LOW |
| "Three recovery levels" | docs | RecoveryManager exists but Level 1 (in-memory) and Level 2 (file backup) require pre-existing snapshots that are never created. Only Level 3 (git reset) is practically available. | MEDIUM |
| "Consensus system / consent" | memory.py NODE_TYPES | No consent/consensus logic exists in KnowledgeGraph. NODE_TYPES is a static tuple. | LOW |
| "Telemetry writes to rack/telemetry.json" | completion report | Telemetry writes to `.rsis/telemetry/*.jsonl` (JSONL files), not `rack/telemetry.json` | LOW |

### Comments vs. Code

| Comment | Code Reality |
|---------|-------------|
| "evaluator is loaded from a read-only filesystem mount" | Evaluator is loaded from `evaluator/evaluator.py` in the workspace — no read-only mount |
| "Startup digest verify" | `self_verify()` exists but is opt-in via CLI flag, not automatic |
| "read_only_mount: True" in EvaluatorConfig | No code enforces a read-only mount |

---

## 13. Newly Discovered Findings

### ND1: The Deterministic Generator Creates Technical Debt
Every L2 run that finds a missing module creates a trivial scaffold. Over many runs, this produces an accumulation of no-op placeholder files that satisfy the evaluator but provide no value. There is no mechanism to detect or clean up these scaffolds.

### ND2: `_apply_tuned_state()` Applies ALL State Files at Startup
Every time any RSIS command runs, `_apply_tuned_state()` reads and applies state from L4, L5, L6, L7, L8, and L9 state files. This means a corrupted state file affects ALL subsequent commands, not just the affected loop.

### ND3: L3 Has No Evaluator Gate
L3's evolution cycle (adding insight nodes, evolving strategies, pruning redundancies, writing to MyKB) runs without evaluator approval. This is intentional (L3 is a consolidation loop, not a mutation loop), but it means L3 can add arbitrary nodes to the KG and write arbitrary content to MyKB without quality control.

### ND4: Vector Store Saves On Every `add()`
`VectorStore.add()` calls `self.save()` after every document addition. Combined with `MemoryManager.record_improvement()` calling `self.save()` which calls `self.vectors.save()`, each improvement triggers a full vector store serialization.

### ND5: Telemetry Collector Has No Rotation
`TelemetryCollector` appends to `.jsonl` files without rotation or pruning. Over long-running sessions, these files grow without bound.

### ND6: Evaluator Cost Accounting is Fabricated
The evaluator client estimates tokens (`(len(input_json) + 1200) // 4`) and uses a fixed `out_tokens = 200`. These are not real measurements — they're placeholders for cost tracking. The actual evaluator subprocess makes no API calls (deterministic mode), so the cost accounting records phantom LLM spend.

---

## 14. Revised Finding Register

| ID | Original Claim | Verdict | Evidence | Revised Severity | Confidence |
|----|---------------|---------|----------|-----------------|------------|
| P1 | KG write amplification | PARTIALLY MITIGATED | Dirty flag added, but `record_improvement` still saves per-call | Medium | High |
| P2 | Silent corrupted-state fallback | VERIFIED | `_apply_tuned_state` catches all exceptions, logs warning | Medium | High |
| P3 | preexec_fn threading | PARTIALLY MITIGATED | `os.setsid()` added, fundamental pattern unchanged | Low | High |
| P4 | Scope expansion | VERIFIED | 27+ phases, most aspirational, many untested | High | High |
| P5 | +3 cascading instability | UNVERIFIED | No runtime data exists | Medium | Low |
| P6 | Evaluator weakness | VERIFIED (NEW) | JSON data candidates get minimal validation | High | High |
| P7 | Concurrent state mutation | NEWLY DISCOVERED | No file locking on state files | Medium | High |
| P8 | Unbounded KG growth | PARTIALLY MITIGATED | Per-cycle cap on redundancy flags, but insight nodes grow unbounded | Medium | High |
| ND1 | Scaffold accumulation | NEWLY DISCOVERED | Deterministic generator creates no-op files | Medium | High |
| ND2 | Startup state contamination | NEWLY DISCOVERED | All state files applied globally at startup | Medium | Medium |
| ND3 | L3 has no evaluator gate | NEWLY DISCOVERED | L3 writes freely to KG and MyKB | Low | High |
| ND4 | Vector store save-on-add | NEWLY DISCOVERED | Every document addition triggers full serialization | Low | High |
| ND5 | Telemetry unbounded growth | NEWLY DISCOVERED | No rotation or pruning | Low | Medium |
| ND6 | Evaluator cost fabrication | NEWLY DISCOVERED | Phantom token counts recorded as LLM spend | Low | High |

---

## 15. Maturity Assessment

| Dimension | Score (0–5) | Evidence |
|-----------|-------------|----------|
| **Architecture** | 3.5 | Well-designed +3 diagonal, clear separation of concerns, but scope exceeds demonstrated capability |
| **Correctness** | 3.0 | Core loops work correctly in tests; evaluator catches unsafe patterns; but trivial scaffolds pass |
| **Reliability** | 2.5 | Recovery mechanisms exist but Level 1/2 require preconditions never met; only Level 3 (git) is practical |
| **Security** | 3.0 | Evaluator fails closed on hard gates; MyKB now has session auth; but no structural evaluator immutability |
| **Testing** | 3.5 | 371 tests covering core paths; comprehensive evaluator tests; but no cross-loop integration tests |
| **Observability** | 2.5 | Telemetry collection exists; cost ledger exists; but evaluator costs are fabricated, no rotation |
| **Autonomy** | 1.0 | LLM not wired; deterministic scaffolding is trivial; no genuine autonomous improvement |
| **Self-improvement** | 1.0 | Architecture for RSI exists; actual improvement capability is limited to numeric parameter tuning |
| **State integrity** | 2.5 | KG has atomic writes; but state files have no versioning, no locking, corruption falls back silently |
| **Operational readiness** | 2.0 | Cycle daemon works; but no runtime state exists, no monitoring, no alerting |

**Overall: 2.2/5** — The architectural ambition significantly exceeds demonstrated operational capability.

---

## 16. Critical Risks

1. **The system cannot actually improve itself.** Without an LLM, the "self-improvement" is limited to (a) scaffolding trivial placeholder modules and (b) adjusting numeric parameters. This is the single most important fact about the system's current capability.

2. **The evaluator is a safety gate, not a quality gate.** It prevents dangerous code but cannot distinguish meaningful improvements from trivial scaffolds. Any future LLM integration must address this gap.

3. **State files lack structural protections.** No schema versioning, no locking, no backup before write. A corrupted state file silently degrades the tuning chain.

4. **Scope exceeds testing.** 27+ phases with ~40% untested. Aspirational subsystems add complexity without validation.

---

## 17. Highest-Value Improvements (Prioritized)

| Priority | Improvement | Benefit | Complexity | Dependencies |
|----------|------------|---------|------------|-------------|
| **1** | Wire LLM for genuine candidate generation | Unlocks actual self-improvement | High | LLM API key, provider integration |
| **2** | Add evaluator quality scoring (not just safety) | Prevents trivial scaffold optimization | Medium | Design quality metrics, possibly LLM evaluator |
| **3** | Add state file schema versioning + validation | Prevents silent corruption | Low | Schema definition per state file |
| **4** | Add file locking for state files | Prevents concurrent mutation | Low | fcntl or similar |
| **5** | Add telemetry rotation/pruning | Prevents unbounded growth | Low | Retention policy |
| **6** | Test the full +3 diagonal chain end-to-end | Validates the core architectural claim | Medium | Runtime state generation |
| **7** | Enforce evaluator digest verification at startup | Structural immutability guarantee | Low | Checksum storage |

---

## 18. Recommended Next Phase

**Wire an LLM provider and run the full L1–L9 batch for 1 cycle.**

This single action would:
1. Validate the actual RSI capability (or confirm it's aspirational)
2. Generate runtime state files for profiling
3. Exercise the full +3 diagonal tuning chain
4. Expose evaluator quality-assessment weaknesses
5. Produce real telemetry for performance measurement

Without this step, the system remains an architecture without a demonstration.

---

*Audit complete. All findings are based on direct code inspection, test execution, and runtime state examination. No code changes were made.*
