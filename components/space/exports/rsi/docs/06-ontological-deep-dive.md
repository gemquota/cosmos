# 06 — Ontological Deep Dive: Entity Spaces, State Topology, and Existential Commitments of RSI

> **Analytical Lens:** Ontological (Tier 2 — Exhaustive)
> **Supersedes:** 01-ontological-taxonomy.md (extends with formal analysis)
> **Source Artifacts:** All 67 SPACE artifacts + 67 open-ended answers
> **Derivation Depth:** Full artifact cross-referencing

---

## 1. The Ontological Commitment of RSI

RSI makes a fundamental ontological commitment: **improvement is additive, never destructive**. Nothing in the system is deleted — only deprecated, superseded, or versioned. This is not merely a data retention policy; it is a claim about the nature of recursive improvement itself.

### 1.1 The Additivity Principle

Every entity that enters the system persists indefinitely. This creates an **ontological layering** where the current state of the system is the sum of all its history. The system literally is its past.

**Implication:** The system cannot be understood from a snapshot alone. To comprehend RSI, you must comprehend its trajectory — the path through modification-space, not just the current position.

### 1.2 The Boundedness Principle

The system operates within defined systemic boundaries. The scope is narrow and well-defined. This bounding is itself an ontological statement: **self-improvement requires self-definition**. The system must know where it ends to improve itself safely.

### 1.3 The Core-Peripheral Distinction

All 8 entities are classified as **core** — there is no peripheral surface area. This is unusual for a system of this complexity. Most domains have support entities, utility classes, or incidental objects. RSI does not. Every entity is load-bearing. Removing any one collapses a fundamental aspect of recursive self-improvement.

**Taxonomic consequence:** The domain admits no "nice to have" entities. Each must justify its existence against the eight-entity minimum.

---

## 2. Entity Ontology — Exhaustive Analysis

### 2.1 Entity Census (8 Entities)

| # | Entity | Existential Role | Ontological Category | Persistence |
|---|--------|-----------------|---------------------|-------------|
| 1 | **ImprovementLoop** | The process-substance of recursion | Process | Ephemeral (per-session) |
| 2 | **Evaluator** | The judgment-capacity | Agent | Persistent |
| 3 | **Modifier** | The change-capacity | Agent | Persistent |
| 4 | **Artifact** | The object-of-improvement | Object | Persistent, versioned |
| 5 | **EvaluationCriteria** | The standard-of-judgment | Abstract | Persistent, human-controlled |
| 6 | **SafetyGuard** | The constraint-enforcement | Agent | Persistent, immutable core |
| 7 | **History** | The memory-substance | Repository | Persistent, append-only |
| 8 | **ConvergenceDetector** | The termination-intelligence | Agent | Persistent |

### 2.2 Entity State Spaces

Each entity occupies a state space — the set of all possible configurations it can be in.

#### ImprovementLoop State Space

```
States: { Initialized, Running, Paused, Converged, Terminated, Error }
Transitions:
  Initialized → Running        (loop.start())
  Running → Paused             (human干预 or resource exhaustion)
  Running → Converged          (convergence detected)
  Running → Terminated         (max cycles reached)
  Running → Error              (unrecoverable failure)
  Paused → Running             (human resume)
  Paused → Terminated          (human abort)
  Error → Initialized          (manual restart)
  
Invariant: ConvergenceDetector must be consulted before any Running → Converged transition.
```

#### Evaluator State Space

```
States: { Idle, Evaluating, Scoring, Reporting, SelfImproving }
Transitions:
  Idle → Evaluating            (artifact submitted)
  Evaluating → Scoring         (analysis complete)
  Scoring → Reporting          (scores computed)
  Reporting → Idle             (results delivered)
  Idle → SelfImproving         (evaluator's own improvement triggered)
  SelfImproving → Idle         (self-improvement validated)
  
Invariant: SelfImproving state requires 3x validation cycles and human approval for safety-impacting changes.
```

#### Modifier State Space

```
States: { Idle, Analyzing, Proposing, SelfModifying, AwaitingApproval }
Transitions:
  Idle → Analyzing             (improvement request received)
  Analyzing → Proposing        (hypothesis formed)
  Proposing → Idle             (proposal submitted for safety review)
  Idle → SelfModifying         (self-improvement triggered)
  SelfModifying → AwaitingApproval  (self-change requires human approval)
  AwaitingApproval → Idle      (approved or rejected)
  
Invariant: SelfModifying state has depth limit of 3 levels. Exceeding this halts all modification.
```

#### Artifact State Space

```
States: { Draft, Evaluated, ModificationProposed, SafetyReviewed, 
          Applied, ReEvaluated, Regressed, Archived, Deprecated }
Transitions:
  Draft → Evaluated            (first evaluation)
  Evaluated → ModificationProposed  (modifier proposes change)
  ModificationProposed → SafetyReviewed  (safety guard reviews)
  SafetyReviewed → Applied     (approved and applied)
  SafetyReviewed → Evaluated   (rejected, stays at current version)
  Applied → ReEvaluated        (post-modification scoring)
  ReEvaluated → Evaluated      (accepted, new baseline)
  ReEvaluated → Regressed      (regression detected)
  Regressed → Evaluated        (automatic rollback)
  Any → Archived               (end of improvement session)
  Any → Deprecated             (superseded by better version)
  
Invariant: Regressed → Evaluated rollback must complete within 100ms.
```

#### SafetyGuard State Space

```
States: { Active, Blocking, Learning, Override }
Transitions:
  Active → Blocking            (dangerous modification detected)
  Blocking → Active            (modification rejected, return to monitoring)
  Active → Learning            (new pattern incorporated from history)
  Learning → Active            (pattern validated)
  Active → Override            (human emergency override)
  Override → Active            (override lifted)
  
Invariant: Override state requires human authentication and is logged.
```

#### History State Space

```
States: { Accepting, Querying, Compacting }
Transitions:
  Accepting → Querying         (read request received)
  Querying → Accepting         (read complete)
  Accepting → Compacting       (periodic maintenance)
  Compacting → Accepting       (compaction complete)
  
Invariant: History is append-only in Accepting state. No deletion, no modification.
```

#### ConvergenceDetector State Space

```
States: { Monitoring, Predicting, Deciding, Reported }
Transitions:
  Monitoring → Predicting      (velocity data collected)
  Predicting → Deciding        (prediction complete)
  Deciding → Reported          (convergence verdict issued)
  Reported → Monitoring        (new cycle begins)
  
Invariant: Deciding state must consider minimum window of 10 cycles before declaring convergence.
```

#### EvaluationCriteria State Space

```
States: { Active, UnderReview, Locked }
Transitions:
  Active → UnderReview         (human proposes change)
  UnderReview → Active         (change approved)
  UnderReview → Locked         (change rejected, criteria frozen)
  Locked → Active              (human unlocks for revision)
  
Invariant: No entity other than human operators can modify EvaluationCriteria. The RSI loop itself cannot alter its objective function.
```

### 2.3 Entity Cardinality Map

| Relationship | Cardinality | Multiplicity | Notes |
|-------------|:-----------:|:------------:|-------|
| ImprovementLoop → Evaluator | 1:1 | Exactly one | Each loop has one evaluator |
| ImprovementLoop → Modifier | 1:1 | Exactly one | Each loop has one modifier |
| ImprovementLoop → SafetyGuard | 1:1 | Exactly one | Each loop has one safety guard |
| ImprovementLoop → ConvergenceDetector | 1:1 | Exactly one | Each loop has one convergence detector |
| ImprovementLoop → Artifact | 1:N | Zero or more | Loop improves artifacts iteratively |
| ImprovementLoop → History | 1:1 | Exactly one | Each loop has one history |
| Evaluator → EvaluationCriteria | N:1 | Many-to-one | Multiple evaluators share criteria |
| Evaluator → Artifact | N:M | Many-to-many | Evaluators score many artifacts |
| Modifier → Artifact | 1:N | One-to-many | Modifier produces artifact versions |
| SafetyGuard → ModificationProposal | 1:N | One-to-many | Guard reviews many proposals |
| Artifact → Artifact | 1:N (tree) | Parent-child | Version chain forms a tree |
| History → ModificationRecord | 1:N | One-to-many | History contains records |
| Human → EvaluationCriteria | 1:N | One-to-many | Humans define criteria |
| Human → ImprovementLoop | 1:N | One-to-many | Humans start/stop loops |

### 2.4 Entity Composition Tree (Extended)

```
System (root)
├── ImprovementLoop[1..N]                    — multiple concurrent loops possible
│   ├── Evaluator[1]
│   │   ├── scoring_function: Callable
│   │   ├── confidence_threshold: float
│   │   ├── evaluation_depth: int
│   │   └── EvaluationCriteria[1..N]         — shared across evaluators
│   │       ├── dimension_weights: Map<string, float>
│   │       ├── benchmark_references: string[]
│   │       └── human_overrides: OverrideRecord[]
│   ├── Modifier[1]
│   │   ├── modification_type: enum
│   │   ├── granularity: enum
│   │   ├── safety_level: enum
│   │   └── Artifact[0..N]                   — modified artifacts
│   │       ├── version_chain: LinkedList<Version>
│   │       ├── parent_id: ArtifactId | null
│   │       ├── diff_summary: string
│   │       ├── performance_delta: float
│   │       └── ArtifactType variants:
│   │           ├── PromptArtifact
│   │           ├── ConfigArtifact
│   │           └── StrategyArtifact
│   ├── SafetyGuard[1]
│   │   ├── StaticGuard
│   │   │   └── rule_set: ImmutableRule[]
│   │   └── DynamicGuard
│   │       ├── learned_patterns: Pattern[]
│   │       └── confidence_threshold: float
│   ├── ConvergenceDetector[1]
│   │   ├── improvement_velocity: float
│   │   ├── improvement_trajectory: enum
│   │   ├── convergence_threshold: float
│   │   └── window_size: int
│   └── History[1]
│       └── ModificationRecord[0..N]
│           ├── cycle_id: string
│           ├── artifact_id: string
│           ├── modification_diff: string
│           ├── before_score: float
│           ├── after_score: float
│           ├── safety_verdict: enum
│           └── timestamp: DateTime
└── ExternalActors
    ├── HumanOperator[1..N]
    │   ├── role: 'architect' | 'reviewer' | 'operator'
    │   └── permissions: PermissionSet
    ├── LLMApi[1..N]
    │   ├── provider: enum
    │   ├── model: string
    │   └── rate_limits: RateLimitConfig
    └── BenchmarkDataset[1..N]
        ├── name: string
        ├── version: string
        └── test_cases: TestCase[]
```

---

## 3. Ontological Invariants

These are properties that must hold true in every reachable state of the system. Violating any invariant indicates a system defect.

### 3.1 Structural Invariants

| # | Invariant | Formal Statement | Consequence of Violation |
|---|-----------|-----------------|------------------------|
| I1 | **No orphan artifacts** | ∀ artifact a: ∃ improvement_loop l such that a ∈ l.artifacts | Artifact exists without a loop to evaluate it |
| I2 | **No circular improvement** | The artifact version graph is a DAG | Infinite modification loops |
| I3 | **Safety guard always present** | ∀ improvement_loop l: l.safety_guard ≠ null | Unprotected modifications possible |
| I4 | **History integrity** | ∀ record r in history h: r is append-only | Loss of audit trail |
| I5 | **Criteria immutability** | ∀ session s: s.evaluation_criteria = s.initial_criteria | Objective function drift during optimization |
| I6 | **Single objective authority** | ∃! human-controlled authority for EvaluationCriteria | Multiple conflicting objective functions |
| I7 | **Rollback always possible** | ∀ artifact a with version_chain c: |c| ≥ 1 implies rollback target exists | No recovery from bad modifications |

### 3.2 Behavioral Invariants

| # | Invariant | Formal Statement | Consequence of Violation |
|---|-----------|-----------------|------------------------|
| B1 | **Modification → Evaluation** | Every applied modification triggers a re-evaluation | Unvalidated changes enter production |
| B2 | **Evaluation → Comparison** | Every evaluation produces a score delta against baseline | Cannot determine if improvement occurred |
| B3 | **Regression → Rollback** | Score delta < -threshold implies automatic revert | Degraded artifacts persist |
| B4 | **Convergence → Termination** | Convergence detection implies loop termination | Infinite improvement attempts |
| B5 | **Self-modification → Increased scrutiny** | Self-modifications require 3x validation | Modifier can improve itself unchecked |
| B6 | **Human override → Logging** | Every human override generates an audit record | Loss of accountability |
| B7 | **External boundary → No autonomy** | System cannot modify its own benchmarks | Goodhart's Law collapse |

### 3.3 Temporal Invariants

| # | Invariant | Formal Statement | Consequence of Violation |
|---|-----------|-----------------|------------------------|
| T1 | **Monotonic versioning** | Version numbers are strictly increasing | Version confusion, rollback ambiguity |
| T2 | **Causal ordering** | Cause always precedes effect in History | Temporal paradox in improvement tracking |
| T3 | **Session isolation** | Configuration changes are immutable within a session | Mid-loop configuration drift |
| T4 | **Graceful termination** | Active loops complete before system shutdown | Data loss, incomplete improvements |

---

## 4. Possible Worlds Analysis

The RSI system can be in multiple "possible worlds" — configurations that are internally consistent but mutually exclusive. Understanding these helps predict system behavior under different conditions.

### 4.1 World: Single-Loop Steady State

The simplest world. One ImprovementLoop, one Artifact, iterating until convergence. All safety checks pass. History grows linearly. This is the "happy path."

**Characteristics:** Linear growth, predictable timelines, easy monitoring.

### 4.2 World: Multi-Artifact Concurrent Improvement

Multiple ImprovementLoops running simultaneously, each working on different Artifacts. They share EvaluationCriteria and SafetyGuard rules, but have independent Histories.

**Characteristics:** Bursty resource usage, potential for cross-artifact insights, harder to monitor.

### 4.3 World: Self-Modification Cascade

The Modifier improves its own prompt template, which changes how it generates modifications, which changes how it evaluates its own modifications. The SafetyGuard must detect and contain cascading effects.

**Characteristics:** High risk, high reward. Requires strict depth limiting and human oversight.

### 4.4 World: Evaluation Disagreement

Multiple Evaluators produce conflicting scores for the same Artifact. The system must resolve disagreements without a single source of truth.

**Characteristics:** Requires voting or consensus mechanisms. SafetyGuard must block modifications when evaluator confidence is low.

### 4.5 World: Resource Exhaustion

API rate limits, token budgets, or storage capacity constrain the improvement loop. The system must degrade gracefully, prioritizing which improvements to pursue.

**Characteristics:** Queue management, priority scheduling, cost-aware improvement selection.

### 4.6 World: Adversarial Conditions

An external actor attempts to trick the Modifier into producing harmful modifications. The SafetyGuard must detect and block adversarial inputs.

**Characteristics:** Requires input validation, anomaly detection, potentially adversarial robustness testing.

---

## 5. Ontological Gaps and Recommendations

### 5.1 Identified Gaps

| Gap | Description | Impact | Recommendation |
|-----|-------------|--------|----------------|
| **No Entity for "Benchmark"** | Benchmarks are mentioned as external actors but have no internal entity representation | Cannot version or track benchmark changes | Add `Benchmark` entity with versioning |
| **No Entity for "Cost"** | LLM API costs are mentioned but not tracked as first-class entities | Cannot optimize for cost-effectiveness | Add `CostTracker` entity |
| **No Entity for "Configuration"** | Runtime config is mentioned but has no ontological status | Configuration changes are opaque | Add `Configuration` entity with immutability guarantees |
| **SafetyGuard Split Incomplete** | SafetyGuard is described as two sub-entities (Static/Dynamic) but still listed as one | Confusion about lifecycle | Promote StaticGuard and DynamicGuard to top-level entities |
| **EvaluationCriteria Rigidity** | Criteria are described as immutable per session but must evolve over time | System cannot adapt its objectives | Add versioned Criteria evolution with human approval gates |
| **No "Session" Entity** | Improvement sessions are implied but not entity-ified | Cannot track or resume sessions | Add `Session` entity with start/end/resume lifecycle |

### 5.2 Entity Reclassification Proposals

| Current Entity | Proposed Change | Rationale |
|---------------|----------------|-----------|
| SafetyGuard | Split into StaticGuard + DynamicGuard | Different lifecycles, different modification rules |
| EvaluationCriteria | Add sub-entity WeightedDimension | Criteria are aggregates of weighted dimensions |
| Artifact | Add subtype hierarchy (Prompt/Config/Strategy) | Different modification mechanics need formal types |
| History | Add sub-entity AuditTrail | Audit trails have different access patterns than improvement history |

---

## 6. Formal Ontological Model

### 6.1 Entity-Relationship Notation

```
∀x ∈ Entity: x.state ∈ x.stateSpace
∀(x,y) ∈ Relation: x.state × y.state ⊆ allowedTransitions(x,y)
∀ loop ∈ ImprovementLoop: loop.state = Running ⟹ 
  ∃ guard ∈ SafetyGuard: guard.state ∈ {Active, Blocking}
∀ artifact ∈ Artifact: artifact.state = Regressed ⟹ 
  ∃ record ∈ History: record.type = 'rollback'
∀ session ∈ Session: session.criteria = session.initialCriteria  -- immutability
```

### 6.2 System State Definition

The global system state is the Cartesian product of all entity states, constrained by the invariants:

```
SystemState = (IL_state × Eval_state × Mod_state × Art_state × 
               Criteria_state × Safety_state × History_state × Conv_state) 
              ∩ Invariants
```

**Reachability:** Not all combinations are reachable. The invariants prune the state space significantly. For example, `SafetyGuard.state = Override` while `Modifier.state = SelfModifying` without `HumanOperator.state = Authorizing` is unreachable.

---

## 7. Ontological Summary

The RSI domain exhibits:

- **Compact ontology** — 8 core entities, all load-bearing, no peripheral objects
- **Additive persistence** — nothing is deleted, only versioned or deprecated
- **Fine granularity** — every meaningful distinction yields a separate entity
- **Bounded scope** — tight systemic boundaries prevent ontological inflation
- **Formal invariants** — 7 structural + 7 behavioral + 4 temporal invariants
- **6 possible worlds** — ranging from simple steady-state to adversarial conditions
- **6 identified gaps** — entities that should exist but don't yet

The ontology is deliberately minimal. Each entity must justify its existence against the eight-entity minimum. This constraint forces clarity about what truly matters in recursive self-improvement.

---

*Derived from: All 67 SPACE artifacts, all 67 open-ended answers, cross-referenced with 01-ontological-taxonomy.md*
*SPACE — Superb Prompt Automatic Creation Engine v2.1.0*
