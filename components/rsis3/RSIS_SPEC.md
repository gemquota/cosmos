# RSIS — Recursive Self-Improvement System

## Implementation Specification

*Generated via RRP — 11 locked decisions, 0 contradictions, full topic coverage*

---

## 1. System Architecture

### 1.1 Loop Stack (nine-level hierarchy)

```
┌──────────────────────────────────────────────────────────────┐
│                    L3 — Evolution Loop                        │
│  Frequency: hours/days  │  Trigger: cross-session interval   │
│──────────────────────────────────────────────────────────────│
│  - Consolidate memory into knowledge graph                   │
│  - Derive meta-strategies from session history               │
│  - Prune redundant code paths (redundancy refinement)        │
│  - Evolve L2 improvement heuristics                          │
│  - Report cross-session trends                               │
└───────────────────────────┬──────────────────────────────────┘
                            │ promotes
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    L2 — Improvement Loop                      │
│  Frequency: per-session  │  Trigger: session start / detect  │
│──────────────────────────────────────────────────────────────│
│  - Generate code changes (new features, refactors, fixes)    │
│  - Tune prompts / tool selection preferences                 │
│  - Modify architecture within scope                          │
│  - Submit to immutable AI evaluator                          │
│  - On approval: apply, checkpoint, update knowledge graph    │
│  - On rejection: discard, log failure pattern                │
└───────────────────────────┬──────────────────────────────────┘
                            │ spawns
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    L1 — Action Loop                           │
│  Frequency: per-task    │  Trigger: user request / event     │
│──────────────────────────────────────────────────────────────│
│  - Plan → execute tool calls → observe → retry/adapt        │
│  - Collect workspace telemetry                               │
│  - Checkpoint before destructive operations                  │
│  - Fallback: revert to last checkpoint + log                 │
└──────────────────────────────────────────────────────────────┘
```

The RSIS engine was conceived as **nine nested loops**. Three are fully
implemented (`loop_l1.py` … `loop_l3.py`); L4 (`loop_l4.py`, Optimizer),
L5 (`loop_l5.py`, Evolution), L6 (`loop_l6.py`, Identity) and L7
(`loop_l7.py`, Meta-Cog) are implemented as bounded, evaluator-gated
cycles; L8–L9 are hypothetical.

**Tuning ownership follows a +3 diagonal: loop k+3 tunes loop k.**
L4→L1, L5→L2, L6→L3, L7→L4, L8→L5, L9→L6. Each loop tunes exactly one
target, so no two loops ever write the same parameter key. L7–L9 are
themselves untuned (no L10+), making the top three fixed points — the
unbounded-recursion guard. This yields a modification depth of exactly
three meta-levels: core (L1–L3) → tuners (L4–L6) → meta-tuners (L7–L9),
which matches the max-3-self-modification depth limit in the SPACE
recursive-depth analysis.

**L1 and L2 tune nothing.** They are pure consumers of tuned params
(L4→L1, L5→L2) and never write a parameter key. Their intra-cycle
adaptation — L1 retry/adapt, L2 candidate refinement after evaluator
rejection — is self-adaptation inside a task, not cross-loop tuning.
L2 *spawns* L1 action loops (instantiation), which is also not tuning.

**L0 is the substrate, not a loop.** It is the workspace/artifact layer
(files, config, `.rsis` state) that the loops mutate. Nothing parameterizes
it; L1–L3 mutate it directly (tool calls, code application, memory
consolidation). The diagonal therefore terminates at L1:
L9 → L6 → L3 → substrate, with L3's consolidation/pruning as the loop that
most directly curates the substrate.

| Loop | Name | Status | Responsibility |
|------|------|--------|----------------|
| L0 | Substrate | n/a (not a loop) | The artifact/workspace layer loops mutate — files, config, `.rsis` state |
| L1 | Execution | implemented | Per-task action loop: plan → tool calls → observe → retry |
| L2 | Planning / Improvement | implemented | Per-session improvement candidates, immutable-evaluator gate |
| L3 | Self-Direction / Evolution | implemented | Cross-session memory consolidation, strategy derivation, pruning |
| L4 | Optimizer | implemented | Fast-feedback tuning of **L1 execution params** from outcomes |
| L5 | Evolution | implemented | Population-based evolution of **L2 improvement params** + focus |
| L6 | Identity | implemented | Tunes **L3 evolution params** (plateau timeout) |
| L7 | Meta-Cog | implemented | Tunes **L4 optimizer params** (window / thresholds) |
| L8 | Meta-Meta | hypothetical | Tunes **L5 strategy params** (population / mutation) |
| L9 | MMM | hypothetical | Tunes **L6 identity params** (the recursion guard) |

L4 and L5 follow the same invariants as the lower loops: checkpoint before
mutation, bounded budgets, immutable evaluator gate, telemetry, and failure
cascades up to the next level. Persisted tuning is injected at startup:
`load_config()` applies the L4 optimizer state and the L5 best strategy to
`CONFIG` before any loop constructs, so L1/L2 consume the tuned values
without extra plumbing.

```
┌──────────────────────────────────────────────────────────────┐
│                L5 — Evolution Loop (strategies)               │
│  Frequency: days  │  Population selection + mutation         │
│  - Seed from L3 KG strategies                                │
│  - Score fitness from outcome telemetry                      │
│  - Elitism + mutate/recombine → next generation              │
│  - Evaluator gate on each generation                         │
└───────────────────────────┬──────────────────────────────────┘
                            │ tunes strategy space
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                L4 — Optimizer Loop (meta-params)             │
│  Frequency: hours  │  Fast-feedback parameter tuning         │
│  - Aggregate recent L1/L2/L3 outcomes                        │
│  - Propose clamped deltas (retries / tool calls)            │
│  - Evaluator gate → checkpoint → persist optimizer state     │
└───────────────────────────┬──────────────────────────────────┘
                            │ promotes
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    L3 — Evolution Loop                        │
│  Frequency: hours/days  │  Trigger: cross-session interval   │
└───────────────────────────┬──────────────────────────────────┘
                            │ promotes
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    L2 — Improvement Loop                      │
└───────────────────────────┬──────────────────────────────────┘
                            │ spawns
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    L1 — Action Loop                           │
└──────────────────────────────────────────────────────────────┘
```

### 1.2 Loop Termination (per LangChain stacked-loop pattern)

| Loop | Termination Signal | Budget | Timeout |
|------|-------------------|--------|---------|
| L1 | Task completion OR max retries exceeded | 10 tool calls per step | 120s |
| L2 | Evaluator approval OR iteration budget exhausted | 5 improvement attempts | 30min |
| L3 | Plateau detection (no gains in N sessions) OR scheduled | 20 sessions | 24h |
| L4 | No deltas proposed OR evaluator rejection OR budget | 1 cycle | 5min |
| L5 | Generation complete OR evaluator rejection OR budget | 1 generation | 10min |
| L6 | No signal OR at bounds OR evaluator rejection OR budget | 1 cycle | 10min |
| L7 | No signal OR deadband gap OR evaluator rejection OR budget | 1 cycle | 10min |

### 1.3 Stacking Semantics

Each loop level **spawns** the level below it and **evaluates** its output before promoting. Failures cascade upward:
- L1 failure → L2 retries with different approach
- L2 failure (evaluator rejection x3) → L3 flags strategy for evolution
- L3 plateau → triggers redundancy refinement
- L3 strategies → seed L5 population
- L4 tuning failure → L5 evolves the strategy space
- L5 plateau (no fitness gain across generations) → L6 would re-evaluate identity

---

### 1.4 Loop Topology: Nested, Parallel, Overlapping

The nine loops are **not one topology**. The conception mixes three, and the
conflicts that matter come from the overlapping ones:

- **Nested** — a loop spawns the level below and promotes its output
  upward. L1 ⊂ L2 ⊂ L3 is the implemented stack; L5 is seeded from L3's KG
  strategies (a one-way nesting edge); L7–L9 nest above L5 as its tuners.
- **Parallel** — loops with disjoint state that can run concurrently. L4
  (writes `.rsis/optimizer_state.json`) and L5 (writes `.rsis/strategies.json`)
  are parallel by design; multiple L1 action loops run in parallel per task.
  L6 (Meta-Cog) would be a parallel observer over the whole stack.
- **Overlapping** — loops that share state or feedback and therefore need
  arbitration. The overlaps that exist today:
  - *Shared reads*: L3, L4, L5 all read the same outcome telemetry / KG.
    Read-sharing is safe and intended.
  - *Shared config writes*: tuning loops adjust other loops' budgets.
    Resolved by the strict **+3 ownership diagonal** — L4 owns `l1.*`,
    L5 owns `l2.max_attempts`, L6 would own `l3.*`, L7 `l4.*`, L8 `l5.*`,
    L9 `l6.*` (registry in `config.py`). No two loops write the same key.
  - *Seeding*: L5 reads L3's strategy nodes (write→read, one-way, safe).

**Arbitration rules**

| State slice | Owner | Others |
|---|---|---|
| `.rsis/knowledge_graph.json`, vectors | L3 | L4/L5 read-only |
| `.rsis/optimizer_state.json` | L4 | startup loader reads |
| `.rsis/strategies.json` | L5 | startup loader reads |
| `.rsis/identity_state.json` | L6 | startup loader reads |
| `.rsis/metacog_state.json` | L7 | startup loader reads |
| `CONFIG` (runtime) | startup loader writes; L4/L5 mirror in-process | L1/L2 read |

**Concurrency guardrail**: the ownership table gives file-level disjointness,
but two concurrent runs of the *same* loop (e.g., two L5 cycles) would race on
their own state file. Loop execution is therefore serialized by the CLI; a
parallel scheduler must hold a lock per state file before a cycle.

**Deliberate non-overlaps** (documented so they stay that way):
- L0 is the shared substrate, not a tunable loop — no loop owns L0 keys.
- The evaluator is immutable and owned by no loop.
- A loop writes only its +3 target's params (L4→L1, L5→L2, L6→L3, L7→L4,
  L8→L5, L9→L6) and never any other loop's keys.
- L7–L9 are untuned fixed points; adding an L10+ would change the recursion
  guard and requires a spec change.

## 2. Memory Hierarchy

### 2.1 Three-Tier Storage

```
┌──────────────────────────────────────────────────────┐
│                    Vector Store                       │
│  (Semantic Retrieval — Qdrant / Chroma / pgvector)   │
│  - Embedding search over past improvements           │
│  - Similar pattern retrieval for codegen             │
│  - Failure mode similarity matching                  │
└──────────────────────┬───────────────────────────────┘
         queries ▲
┌──────────────────────┴───────────────────────────────┐
│                  Knowledge Graph                       │
│  (Neo4j / in-memory RDF / NetworkX)                  │
│  - Entity: Module, Function, Pattern, Strategy       │
│  - Relations: DEPENDS_ON, IMPROVED_BY, CAUSED_FAILURE│
│  - Derived by L3 consolidation from raw history      │
└──────────────────────┬───────────────────────────────┘
         commits ▲
┌──────────────────────┴───────────────────────────────┐
│                    Git Repository                      │
│  (Code Versioning — libgit2 / git CLI)               │
│  - Full history of every improvement                  │
│  - Rollback to any point via checkpoint tags          │
│  - Branch per experiment, merge on evaluator approval │
└──────────────────────────────────────────────────────┘
```

### 2.2 Write & Query Flow

| Operation | Write Pattern | Query Pattern |
|-----------|--------------|---------------|
| L1 execution | Log to workspace telemetry | Load recent context |
| L2 improvement | Commit code to git → record in KG | Search vectors for similar patterns |
| L3 evolution | Consolidate KG → update vectors | Query all three for synthesis |

### 2.3 Redundancy Refinement

Every Nth L3 cycle (configurable, default N=5):
1. Scan git history for stale/unused branches
2. Prune knowledge graph nodes with zero references
3. Compress vector store (deduplicate near-identical embeddings)
4. Report bloat metrics

---

## 3. Guardrails & Evaluation

### 3.1 Immutable AI Evaluator

```
┌──────────────────────────────────────┐
│          AI Evaluator (Frozen)        │
│                                      │
│  - Separate model instance / API     │
│  - Fixed system prompt (never edited)│
│  - Evaluates: correctness, safety,   │
│    efficiency, style, regression     │
│  - Outputs: PASS / FAIL + rationale  │
│  - No code modification capability   │
└──────────────────────────────────────┘
         ▲ passes candidate to
         │
┌─────────┴────────────────────────────┐
│         L2 Improvement Engine        │
│  (can modify anything except the     │
│   evaluator's prompt, model, or code)│
└──────────────────────────────────────┘
```

Enforcement of immutability:
- Evaluator runs in a separate process/container
- Its code is loaded from a read-only filesystem mount
- Configuration is environment-variable driven, not file-driven
- Digest verification at startup (SHA-256 of evaluator binary)

### 3.2 Resource Limits

Despite the "no artificial guardrails" stance, practical bounds must exist to prevent host exhaustion:

| Resource | Limit | Action on Exceed |
|----------|-------|-----------------|
| Disk (git + vector store) | 80% of available | Trigger redundancy refinement |
| Memory (process) | 4GB RSS | Halt L2, fallback to L1 only |
| CPU (improvement process) | N-1 cores | Throttle L3 frequency |
| API calls (evaluator) | 100/min | Exponential backoff |

### 3.3 Recovery Mechanisms

| Failure | Mechanism | Recovery |
|---------|-----------|----------|
| Destructive code change | Git checkpoint rollback | `git checkout` + restart L2 |
| Evaluator unreachable | Degraded mode | Queue improvements, retry |
| Infinite L1 loop | Max iterations + timeout | Kill L1, log, alert |
| Memory corruption | Fallback interpreter | Reset to last valid state |

---

## 4. Workspace Telemetry

### 4.1 Data Collected

- File modification events (inotify / watchman)
- Shell command history (`.bash_history` / `.zsh_history`)
- Editor buffer state (via LSP / extension integration)
- Resource usage (CPU, memory, disk I/O)
- Error rates (stderr capture, exit codes)

### 4.2 Reporting Format

```json
{
  "session_id": "uuid",
  "timestamp": "ISO8601",
  "loop_level": "L1|L2|L3",
  "trigger": "user_request|scheduled|threshold",
  "events": [
    {
      "type": "file_write|command|error|eval",
      "path": "src/main.py",
      "delta": "+42 -12 lines",
      "duration_ms": 1234
    }
  ],
  "metrics": {
    "token_usage": 45000,
    "eval_score": 0.87,
    "iterations": 3
  }
}
```

### 4.3 Extrapolation Engine

Analyzes telemetry across sessions to:
- Predict optimal L2 iteration budget based on past eval curves
- Detect performance regression trends before they hit thresholds
- Suggest which code areas need redundancy refinement
- Generate cross-session improvement velocity reports

---

## 5. Implementation Phases

### Phase 1 — Core Loop Engine (MVP)
- [ ] L1 action loop with tool calling and checkpointing
- [ ] L2 code generation with git commits
- [ ] Immutable evaluator integration (separate process)
- [ ] Basic workspace telemetry collection

### Phase 2 — Memory & Persistence
- [ ] Hierarchical memory (git → knowledge graph → vectors)
- [ ] L3 evolution loop with memory consolidation
- [ ] Similarity search for improvement patterns

### Phase 3 — Autonomy & Refinement
- [ ] Redundancy refinement automation
- [ ] Telemetry-based extrapolation engine
- [ ] Cross-session strategy evolution
- [ ] Web dashboard for reporting

### Phase 4 — Production Hardening
- [ ] Resource limit enforcement
- [ ] Full recovery mechanism testing
- [ ] Performance optimization
- [ ] Security audit (accepting risk)

---

## 6. Technology Stack Recommendations

| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| Agent framework | LangChain (loop stacking) | Confirmed reference architecture |
| Vector store | Chroma (local) | Embedded, no infra needed |
| Knowledge graph | NetworkX + JSON serialization | Lightweight, no DB dependency |
| Version control | libgit2 (via pygit2/gitpython) | Programmatic git ops |
| Evaluator | Separate GPT/Claude API | Read-only, frozen prompt |
| Telemetry | watchdog + psutil | Standard Python libs |
| Reporting | FastAPI + HTMX dashboard | Lightweight web UI |

---

## 7. Key Architectural Invariants

1. **Evaluator is immutable** — never in-scope for self-improvement
2. **Checkpoint before every mutation** — rollback is always possible
3. **Loops terminate** — no unbounded recursion within a level
4. **Failure cascades up** — L1→L2→L3 for adaptive retry
5. **Memory is hierarchical** — git (truth) → KG (insight) → vectors (retrieval)
6. **Risk is accepted** — no artificial scope limits, only practical resource bounds

---

*Specification generated 2026-06-30 via RRP (U2|M1|R5/5|D2)*
*11 decisions locked, 0 contradictions, ambiguity resolved to avg 0.25*
