# COSMOS — Project Description and Architecture

## Executive Summary

COSMOS is a research-oriented Python system for recursive self-improvement, supported by three integrated components:

- **RSIS3** — the core recursive self-improvement engine
- **MyKB** — persistent Markdown-based knowledge and memory storage
- **SPACE** — structured ideation and recursive prompt-refinement tooling

A unified static dashboard visualizes telemetry, loops, memory, graphs, and specifications.

The central architecture contains nine loops, L1–L9, with a **+3 diagonal** tuning relationship:

```text
L4 → L1
L5 → L2
L6 → L3
L7 → L4
L8 → L5
L9 → L6
```

The most accurate operational characterization is:

> COSMOS is a partially operational recursive-adaptation and self-improvement framework. Parameter tuning, strategy evolution, memory consolidation, safety evaluation, and persistence mechanisms execute. Code-level self-improvement remains immature because default candidate generation is deterministic scaffolding, existing-file mutation is restricted, behavioral evaluation is weak, and LLM generation is optional rather than active by default.

---

## Repository Structure

```text
.
├── components/
│   ├── rsis3/
│   │   ├── rsis/
│   │   ├── evaluator/
│   │   ├── tests/
│   │   ├── cli/
│   │   ├── dashboard/
│   │   ├── rack/
│   │   └── telemetry-dashboard/
│   ├── mykb/
│   │   ├── wiki/
│   │   ├── .wiki-daemon/
│   │   ├── server.py
│   │   └── browser and graph artifacts
│   └── space/
│       ├── web/
│       ├── specs/
│       ├── meta-viewer.html
│       └── TypeScript tooling
├── dashboard/
├── contracts/
├── diagrams/
├── docs/
├── infra/
├── README.md
├── ARCHITECTURE.md
├── COSMOS-SPEC.md
├── CODEBASE.md
├── ROADMAP.md
└── index.html
```

The root `index.html` redirects to the unified dashboard.

---

## RSIS3 Core Engine

RSIS3 is the primary cognitive and orchestration engine. It is implemented in Python and exposed through:

```text
components/rsis3/cli/cosmos
```

which invokes:

```bash
python -m rsis
```

Its responsibilities include loop execution, candidate generation, evaluation, persistence, telemetry, checkpointing, recovery, scheduling, tool execution, self-assessment, and meta-optimization.

### L1 — Action Loop

`L1ActionLoop` executes tasks using registered tools.

```text
Task
  → keyword-based planning
  → tool selection
  → tool execution
  → retry or completion
  → telemetry
```

It returns an `L1Result` containing success, steps, tool calls, errors, and final output.

The default planner is keyword-based rather than LLM-based. If no tool name matches the task, L1 marks the task complete. Available tools may include file listing, file reading, file writing, and code execution.

Configuration:

```python
max_tool_calls_per_step
step_timeout_s
max_retries
```

### L2 — Improvement Loop

`L2ImprovementLoop` generates candidate improvements, sends them through the evaluator, and applies approved candidates.

```text
Goal
  → candidate generation
  → candidate persistence
  → checkpoint
  → evaluator
  → acceptance/rejection
  → application
  → checkpoint
  → memory recording
```

By default, candidate generation is deterministic:

1. Parse goals such as `Implement Watcher in rsis/watcher.py`
2. Search for missing modules using `StubDetector`
3. Generate a compilable scaffold
4. Apply it only when the target does not already exist

The optional LLM generator is selected by:

```text
RSIS_L2_LLM_GENERATOR
```

The configured module must expose `generate_candidate`.

A major limitation is that `_apply_improvement()` skips existing files. Deterministic L2 can create new files but cannot modify existing implementations, fix existing bugs, or perform refactoring.

L2 also contains an optional parallel mode using priority workers, an event bus, shared memory, fan-out/fan-in scheduling, and retry controls.

### L3 — Cross-Session Evolution

`L3EvolutionLoop` consolidates recent telemetry and memory into durable knowledge.

```text
Telemetry
  → trend detection
  → memory consolidation
  → strategy derivation
  → redundancy analysis
  → KG/vector persistence
  → MyKB synthesis
```

L3 creates insight nodes from recent sessions, derives budget or regression-focused strategies, flags redundancy candidates, saves memory, and writes synthesis notes to MyKB.

It writes to:

```text
components/mykb/wiki/syntheses/
components/mykb/log.md
```

### L4 — Meta-Parameter Optimizer

`OptimizerLoop` tunes L1 parameters from recorded outcomes.

Tunable parameters include:

```text
l1.max_retries
l1.max_tool_calls
```

Workflow:

```text
KG outcomes
  → success/score aggregation
  → bounded delta proposal
  → checkpoint
  → evaluator
  → runtime CONFIG update
  → optimizer state persistence
```

State file:

```text
.rsis/optimizer_state.json
```

### L5 — Strategy Evolution

`EvolutionLoop` maintains and evolves a population of strategies intended to influence L2.

State file:

```text
.rsis/strategies.json
```

A strategy may contain:

```json
{
  "id": "strategy-1",
  "params": {
    "l2_attempts": 5,
    "budget_factor": 1.0,
    "focus": "general"
  },
  "fitness": 0.0,
  "evals": 0
}
```

Workflow:

```text
Load population
  → seed from L3
  → aggregate outcomes
  → score variants
  → select elites
  → mutate/recombine
  → evaluator
  → persist generation
```

L5 executes as a population-evolution component. However, the ordinary L2 candidate-generation path does not demonstrably load or select from `strategies.json`, so causal L5 → L2 influence remains unproven.

### L6 — Identity Loop

`IdentityLoop` tunes the L3 plateau timeout:

```text
l3.plateau_timeout_s
```

It responds to regression and success-rate signals, proposes bounded changes, gates them through the evaluator, persists state, and mirrors accepted changes into runtime configuration.

State file:

```text
.rsis/identity_state.json
```

### L7 — Meta-Cognitive Loop

`MetaCogLoop` tunes L4 success-band parameters:

```text
l4.outcome_window
l4.min_outcomes
l4.target_success_low
l4.target_success_high
```

It widens the band under oscillation and narrows it under stall conditions.

State file:

```text
.rsis/metacog_state.json
```

### L8 — Meta-Meta Loop

`MetaMetaLoop` tunes L5 exploration parameters:

```text
l5.mutation_rate
l5.population_size
```

It increases mutation under stagnation and reduces population under volatility.

State file:

```text
.rsis/metameta_state.json
```

### L9 — Meta-Meta-Meta Loop

`MMMLoop` tunes L6 sensitivity thresholds:

```text
l6.shrink_below
l6.grow_above
```

It widens the band during oscillation and narrows it during stall with low success.

State file:

```text
.rsis/mmm_state.json
```

---

## +3 Diagonal

The formal relationships are:

| Tuner | Target | Parameters |
|---|---|---|
| L4 | L1 | `l1.max_retries`, `l1.max_tool_calls` |
| L5 | L2 | `l2.max_attempts` through strategy variants |
| L6 | L3 | `l3.plateau_timeout_s` |
| L7 | L4 | outcome window and success band |
| L8 | L5 | mutation rate and population size |
| L9 | L6 | shrink/grow thresholds |

The general state transition is:

```text
Higher loop
  → read lower-loop evidence
  → propose bounded change
  → evaluator
  → write own state file
  → lower-loop configuration loads it later
```

The architecture is implemented. Sustained causal effectiveness remains unproven.

---

## Evaluator

The evaluator is located at:

```text
components/rsis3/evaluator/evaluator.py
```

It runs as a separate subprocess and accepts JSON candidate descriptions.

### Checks

- Target path safety
- Python compilation
- AST safety scans
- Destructive command detection
- Style heuristics
- Efficiency heuristics
- Unified-diff regression checks
- Optional LLM refinement

The evaluator rejects patterns such as:

- `eval`
- `exec`
- unsafe subprocess usage
- destructive filesystem operations
- unsafe pickle operations
- path traversal
- writes outside the workspace

For JSON parameter candidates, Python syntax and AST checks are skipped. The evaluator mostly verifies valid JSON and destructive-string absence.

### Important limitation

The evaluator does not reliably measure:

- Semantic correctness
- Task completion
- Behavioral improvement
- Novelty
- Actual regression safety
- User-value improvement

Adversarial candidates demonstrated that:

- A clean module passes
- Unsafe code fails
- A trivial scaffold passes with an efficiency warning
- A JSON parameter delta passes
- A comment-only change passes with perfect scores
- A semantically wrong implementation passes with perfect scores
- An empty diff fails

The evaluator is therefore best described as a structural safety gate rather than a complete quality or optimization objective.

---

## MyKB

MyKB provides durable knowledge storage using Markdown files with frontmatter.

Capabilities include:

- Synthesis notes
- Session records
- Search
- Wiki browsing
- Knowledge-graph generation
- Graph visualization
- Log management
- HTTP API access

RSIS3 L3 writes durable synthesis notes and log entries. MyKB can supply context to future goals when `from-mykb` is explicitly requested.

This proves a data path from MyKB to goal text, but not that the retrieved context improves behavior.

---

## SPACE

SPACE provides structured ideation and recursive prompt refinement.

It includes:

- A multi-series probe framework
- Prompt specification artifacts
- Recursive refinement workflows
- Web browsing and filtering
- A metadata/spec viewer

RSIS3 can request goals from SPACE artifacts through `from-space` mode. SPACE supplies structured goal material; it does not independently prove better candidate quality or task outcomes.

---

## Persistence and State

Important RSIS3 state includes:

```text
.rsis/optimizer_state.json
.rsis/strategies.json
.rsis/identity_state.json
.rsis/metacog_state.json
.rsis/metameta_state.json
.rsis/mmm_state.json
.rsis/knowledge_graph.json
.rsis/vectors/index.json
.rsis/costs.jsonl
.rsis/candidates.jsonl
.rsis/telemetry/*.jsonl
.rsis/audit.jsonl
.rsis/hitl.jsonl
```

The knowledge graph uses atomic temporary-file replacement and dirty tracking. Most loop state files use direct writes and lack explicit schema versioning, migration, and general file locking.

Runtime state is generally local and not necessarily Git-tracked.

---

## Telemetry and Cost Accounting

Telemetry records:

- Loop starts/completions
- Candidate generation
- Evaluator decisions
- Tool calls
- Durations
- Errors
- Worker events
- Shared-memory events
- Resource activity

Telemetry is generally JSONL under `.rsis/telemetry/`.

The cost ledger records calls, token estimates, models, latency, costs, and errors. Evaluator token usage is estimated rather than measured:

```python
in_tokens = max(1, (len(input_json) + 1200) // 4)
out_tokens = 200
```

Consequently, deterministic evaluator execution may create ledger entries that resemble LLM spend.

---

## Checkpointing and Recovery

`CheckpointManager` uses Git to checkpoint before mutation.

Typical sequence:

```text
Ensure repository
  → detect changes
  → stage changes
  → commit checkpoint
  → mutate
  → commit applied result
```

Recovery mechanisms include:

- In-memory restoration
- File-level restoration
- Git rollback
- Failure counters
- Human alert logging

The most clearly available recovery mechanism is Git rollback. Other levels depend on snapshots or backups being created before failure.

---

## Launch and Cycle Daemon

`launch.py` defines the normal loop order:

```text
run
→ evolve
→ optimize
→ strategies
→ identity
→ metacog
→ metameta
→ mmm
```

The default executor starts each command as a Python subprocess.

`ops_daemon.py` provides:

```text
Acquire lock
  → bridge healthcheck
  → launch full batch
  → optional auto-retune
  → optional snapshot regeneration
  → optional commit/push
  → adaptive sleep or backoff
```

The daemon lock prevents parallel daemon invocations. It does not protect arbitrary manually launched loop commands from racing on shared state.

---

## Security

Implemented controls include:

- Candidate path validation
- AST safety scanning
- Destructive command detection
- Evaluator subprocess isolation
- Checkpoint-before-mutation behavior
- Tool allowlists
- Optional HITL approval
- Resource enforcement
- Cost budgets
- Git rollback
- MyKB write-endpoint session authentication

Limitations include:

- Evaluator digest verification is not automatically enforced
- Evaluator source has no hard immutable filesystem boundary
- JSON tuning candidates receive weak semantic validation
- State-file locking is generally absent
- Several writes are non-atomic
- Sandbox behavior depends on backend configuration
- Static safety checks cannot catch every semantic or behavioral problem

---

## Testing

The RSIS3 test suite contains approximately 372 collected tests in the examined environment.

Coverage includes:

- Evaluator behavior
- L1 retries and tools
- L2 candidate generation
- L3 idempotency
- Knowledge graph persistence
- MyKB gateway
- Pipeline scheduling
- Priority workers
- Shared memory
- Timeout behavior
- Self-assessment
- Forecasting
- Convergence
- Budgets
- Policies
- Federation
- Bridge behavior
- Validation

Important gaps remain around:

- Full L1–L9 causal interaction
- Long-running daemon behavior
- Multi-process state races
- L5-to-L2 influence
- L4/L6 causal performance effects
- MyKB-induced performance changes
- Semantic correctness
- Behavioral regression testing
- Sustained convergence
- Real provider-backed LLM behavior

A passing test suite establishes local behavior, not autonomous effectiveness.

---

## Demonstrated Capabilities

Direct execution and inspection demonstrate:

- CLI dispatch
- L2 deterministic candidate generation
- Evaluator subprocess execution
- Safety rejection
- Git checkpoints
- New-file mutation
- Knowledge-graph persistence
- Vector persistence and retrieval
- L3 memory consolidation
- MyKB synthesis writing
- MyKB goal retrieval
- L4 parameter mutation
- L5 population evolution
- L6 parameter mutation
- L7–L9 invocation
- Self-assessment
- Telemetry
- Cost bookkeeping
- Daemon lock/backoff logic
- Worker-pool scheduling
- Shared-memory CAS behavior

These are operational mechanisms. Their ability to produce sustained task-level improvement remains incompletely demonstrated.

---

## Missing or Dormant Capabilities

Not yet demonstrated:

- Meaningful LLM-generated code improvement
- Reliable modification of existing code
- Semantic correctness evaluation
- Behavioral regression testing after mutation
- L5 influence on L2
- L4/L6 causal downstream improvement
- MyKB-driven performance improvement
- Stable long-run +3 convergence
- Autonomous goal evolution
- Production-grade concurrent state management
- Evaluator calibration against real outcomes

---

## Final Characterization

COSMOS is best described as:

> A partially operational recursive self-improvement framework with working parameter adaptation, strategy population evolution, memory consolidation, safety gating, checkpointing, and telemetry, but with an immature code-improvement substrate and unproven causal effectiveness.

It is not merely an architecture, but it is not yet a fully autonomous self-improving agent.

The central unresolved question is:

> Do COSMOS's adaptations cause later system behavior to improve?

That question belongs to controlled capability experiments rather than further reconnaissance.
