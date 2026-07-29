# 07 — Semantic Relationship Matrix: Complete Association Catalog of the RSI Domain

> **Analytical Lens:** Semantic (Tier 2 — Exhaustive)
> **Supersedes:** 02-semantic-topology.md (extends with formal semantics)
> **Source Artifacts:** All 67 SPACE artifacts + 67 open-ended answers
> **Derivation Depth:** Full artifact cross-referencing

---

## 1. The Semantic Field — Extended Analysis

The RSI domain's semantic structure is defined by **sparse but deep associations**. The prior analysis established this at a high level. This document exhaustively catalogs every association, its formal semantics, safety implications, and temporal behavior.

### 1.1 Semantic Density Quantification

From the 8 core entities, the maximum possible directed associations are 8 × 7 = 56. The actual count is approximately 18 distinct directed associations, yielding a **semantic density of 32%**. This is low for a domain of this complexity and is by design — loose coupling enables independent improvement.

### 1.2 Association Classification Taxonomy

Every association in the RSI domain falls into one of five semantic classes:

| Class | Definition | Count | Safety Impact |
|-------|-----------|:-----:|:-------------:|
| **Generative** | One entity creates another | 5 | Medium |
| **Evaluative** | One entity assesses another | 4 | Low-Medium |
| **Regulatory** | One entity constrains another | 3 | Critical |
| **Observational** | One entity reads another | 3 | Low |
| **Orchestral** | One entity coordinates others | 3 | Medium |

---

## 2. Complete Association Catalog

### 2.1 Generative Associations

These associations describe entity creation — one entity produces or transforms another.

#### G1: Modifier → Artifact (proposes)

```
Source: Modifier
Target: Artifact (new version)
Verb: "proposes"
Semantics: The Modifier analyzes the current Artifact state and generates a ModificationProposal 
           containing a diff, predicted impact, and rationale.
Preconditions: 
  - Modifier.state ∈ {Analyzing, Proposing}
  - Artifact.state ∈ {Evaluated}
  - SafetyGuard.state ∈ {Active}
Effects:
  - Artifact.state → ModificationProposed
  - History.append(ModificationRecord)
  - SafetyGuard receives proposal for review
Safety Level: Medium — proposals are not applied until safety review passes
Temporal: Synchronous — proposal generation blocks until complete
Cardinality: 1 Modifier → 1 Proposal → 0..1 Artifact
```

#### G2: Modifier → Artifact (applies)

```
Source: Modifier
Target: Artifact (existing)
Verb: "applies"
Semantics: The Modifier applies an approved ModificationProposal to the Artifact, 
           creating a new version in the version chain.
Preconditions:
  - ModificationProposal.state = Approved
  - SafetyGuard.state = Active
Effects:
  - Artifact.version_chain.append(newVersion)
  - Artifact.state → Applied
  - Artifact.performance_delta = null (awaiting re-evaluation)
Safety Level: High — applied modifications affect system behavior
Temporal: Synchronous — application is atomic (succeeds or rolls back)
Cardinality: 1 Modifier → 1 Artifact → 1 new Version
```

#### G3: Evaluator → EvaluationResult (produces)

```
Source: Evaluator
Target: EvaluationResult (new)
Verb: "produces"
Semantics: The Evaluator scores an Artifact across multiple dimensions, producing 
           a structured EvaluationResult with scores, confidence intervals, and metadata.
Preconditions:
  - Evaluator.state ∈ {Evaluating, Scoring}
  - Artifact.state ∈ {Evaluated, ReEvaluated}
Effects:
  - EvaluationResult created with dimension scores
  - Evaluator.state → Reporting
  - History.append(EvaluationRecord)
Safety Level: Low — evaluation is read-only assessment
Temporal: Asynchronous — evaluation may take seconds to minutes (LLM-dependent)
Cardinality: 1 Evaluator → 1 EvaluationResult → 1 Artifact
```

#### G4: ConvergenceDetector → TerminationDecision (produces)

```
Source: ConvergenceDetector
Target: TerminationDecision (new)
Verb: "produces"
Semantics: After analyzing improvement velocity, trajectory, and diminishing returns, 
           the ConvergenceDetector produces a verdict: continue, converge, or escalate.
Preconditions:
  - ConvergenceDetector.state ∈ {Deciding}
  - window_size observations collected
Effects:
  - TerminationDecision created
  - If verdict = 'converge': ImprovementLoop.state → Converged
  - If verdict = 'continue': ImprovementLoop continues
  - If verdict = 'escalate': HumanOperator notified
Safety Level: Medium — termination decisions affect system behavior
Temporal: Synchronous — decision blocks loop progression
Cardinality: 1 ConvergenceDetector → 1 TerminationDecision → 1 ImprovementLoop
```

#### G5: History → ModificationRecord (records)

```
Source: History
Target: ModificationRecord (new)
Verb: "records"
Semantics: History appends an immutable record of every modification, evaluation, 
           and system event. Records are never modified or deleted.
Preconditions:
  - Any event occurs in the system
Effects:
  - ModificationRecord appended to History
  - Record is hash-chained to previous record (tamper-evident)
Safety Level: None — append-only, no behavioral impact
Temporal: Synchronous — recording is immediate
Cardinality: 1 History → N ModificationRecords
```

### 2.2 Evaluative Associations

These associations describe assessment — one entity judges or measures another.

#### E1: Evaluator → Artifact (scores)

```
Source: Evaluator
Target: Artifact
Verb: "scores"
Semantics: The Evaluator reads the Artifact and produces numeric scores across 
           defined dimensions (accuracy, latency, cost, safety).
Preconditions:
  - Artifact.state ∈ {Evaluated, ReEvaluated}
  - EvaluationCriteria.state = Active
Effects:
  - Artifact receives score set
  - Score delta computed against baseline
  - Feeds into ConvergenceDetector
Safety Level: Low — read-only assessment
Directionality: Bidirectional information flow (Evaluator reads Artifact, produces scores)
```

#### E2: ConvergenceDetector → History (analyzes)

```
Source: ConvergenceDetector
Target: History
Verb: "analyzes"
Semantics: The ConvergenceDetector reads historical improvement records to compute 
           velocity, trajectory, and diminishing returns.
Preconditions:
  - window_size records available in History
Effects:
  - ConvergenceDetector state updated with analysis
  - Feeds into TerminationDecision
Safety Level: Low — read-only analysis
Directionality: One-way (ConvergenceDetector reads, History passive)
```

#### E3: SafetyGuard → ModificationProposal (reviews)

```
Source: SafetyGuard
Target: ModificationProposal
Verb: "reviews"
Semantics: The SafetyGuard evaluates a proposed modification against static rules 
           (StaticGuard) and learned patterns (DynamicGuard) to determine safety.
Preconditions:
  - ModificationProposal.state = Pending
  - SafetyGuard.state ∈ {Active}
Effects:
  - If safe: ModificationProposal.state → Approved
  - If unsafe: ModificationProposal.state → Rejected
  - SafetyGuard records decision in History
Safety Level: Critical — this is the primary safety gate
Directionality: One-way (SafetyGuard reads and judges)
```

#### E4: HumanOperator → EvaluationCriteria (defines)

```
Source: HumanOperator
Target: EvaluationCriteria
Verb: "defines"
Semantics: The human operator sets and modifies the criteria by which artifacts 
           are judged. This is the only entity that can change what "better" means.
Preconditions:
  - HumanOperator authenticated and authorized
Effects:
  - EvaluationCriteria.state → UnderReview
  - After approval: EvaluationCriteria updated
  - If rejected: EvaluationCriteria.state → Locked
Safety Level: Critical — changes the objective function
Directionality: One-way (Human writes, Criteria被动)
```

### 2.3 Regulatory Associations

These associations describe constraint — one entity limits or bounds another.

#### R1: SafetyGuard → Modifier (constrains)

```
Source: SafetyGuard
Target: Modifier
Verb: "constrains"
Semantics: The SafetyGuard limits what modifications the Modifier can propose. 
           Hard rules (StaticGuard) are immutable. Learned patterns (DynamicGuard) 
           evolve based on historical outcomes.
Preconditions:
  - SafetyGuard.state = Active
Effects:
  - Modifier's proposal space is restricted
  - Blocked proposals generate rejection records
  - SafetyGuard may update DynamicGuard patterns
Safety Level: Critical — prevents dangerous self-modification
Temporal: Persistent — constraint is always active
Cardinality: 1 SafetyGuard constrains 1 Modifier (per loop)
```

#### R2: EvaluationCriteria → Evaluator (governs)

```
Source: EvaluationCriteria
Target: Evaluator
Verb: "governs"
Semantics: EvaluationCriteria define the dimensions, weights, and thresholds 
           that the Evaluator uses to score artifacts. The Evaluator cannot 
           change these criteria.
Preconditions:
  - EvaluationCriteria.state = Active
Effects:
  - Evaluator's scoring function is parameterized by criteria
  - Changes to criteria change all subsequent evaluations
Safety Level: Critical — defines the optimization target
Temporal: Immutable within session (T3 invariant)
Cardinality: N Evaluators governed by 1 EvaluationCriteria
```

#### R3: ConvergenceDetector → ImprovementLoop (terminates)

```
Source: ConvergenceDetector
Target: ImprovementLoop
Verb: "terminates"
Semantics: When convergence is detected, the ConvergenceDetector signals the 
           ImprovementLoop to stop. This is the only entity that can end a loop.
Preconditions:
  - ConvergenceDetector.state = Deciding
  - Verdict = 'converge'
Effects:
  - ImprovementLoop.state → Converged
  - Summary report generated
  - Final artifact versions archived
Safety Level: Medium — prevents infinite improvement attempts
Temporal: One-shot per loop (convergence is terminal)
Cardinality: 1 ConvergenceDetector terminates 1 ImprovementLoop
```

### 2.4 Observational Associations

These associations describe passive information flow — one entity reads another without modification.

#### O1: HumanOperator → ImprovementLoop (monitors)

```
Source: HumanOperator
Target: ImprovementLoop
Verb: "monitors"
Semantics: The human operator observes loop progress via dashboards, logs, 
           and alerts. Monitoring is passive — it does not affect loop behavior.
Preconditions:
  - ImprovementLoop.state = Running
Effects:
  - HumanOperator gains visibility into loop state
  - May trigger intervention if anomalies detected
Safety Level: Low — passive observation
```

#### O2: ImprovementLoop → History (appends to)

```
Source: ImprovementLoop
Target: History
Verb: "appends to"
Semantics: The ImprovementLoop generates records that are appended to History 
           for each cycle's activities.
Preconditions:
  - ImprovementLoop.state = Running
Effects:
  - History grows with each cycle
  - Records are hash-chained
Safety Level: None — append-only
```

#### O3: HumanOperator → History (queries)

```
Source: HumanOperator
Target: History
Verb: "queries"
Semantics: The human operator can query historical records to understand 
           improvement trajectories, identify patterns, and make decisions.
Preconditions:
  - History.count > 0
Effects:
  - HumanOperator gains retrospective insight
  - May inform EvaluationCriteria adjustments
Safety Level: Low — read-only
```

### 2.5 Orchestral Associations

These associations describe coordination — one entity manages the behavior of others.

#### C1: ImprovementLoop → Evaluator (invokes)

```
Source: ImprovementLoop
Target: Evaluator
Verb: "invokes"
Semantics: The ImprovementLoop triggers evaluation at specific points in the 
           improvement cycle (steps 2, 6, 7).
Preconditions:
  - ImprovementLoop.state = Running
Effects:
  - Evaluator.state → Evaluating
  - Evaluation produces scores and deltas
Safety Level: Medium — evaluation drives decisions
```

#### C2: ImprovementLoop → Modifier (invokes)

```
Source: ImprovementLoop
Target: Modifier
Verb: "invokes"
Semantics: The ImprovementLoop triggers modification generation at step 3 
           of the improvement cycle.
Preconditions:
  - ImprovementLoop.state = Running
  - Step 2 (Analyze) complete
Effects:
  - Modifier.state → Analyzing → Proposing
  - ModificationProposal generated
Safety Level: Medium — modification is the core action
```

#### C3: ImprovementLoop → SafetyGuard (consults)

```
Source: ImprovementLoop
Target: SafetyGuard
Verb: "consults"
Semantics: The ImprovementLoop consults the SafetyGuard at step 4 of the 
           improvement cycle before applying any modification.
Preconditions:
  - ModificationProposal.state = Pending
Effects:
  - SafetyGuard reviews proposal
  - Verdict determines next step (apply or reject)
Safety Level: Critical — this consultation is the safety gate
```

---

## 3. Association Properties Matrix

| ID | Source | Target | Verb | Type | Mutability | Safety | Temporal | Transitive |
|----|--------|--------|------|------|:----------:|:------:|:--------:|:----------:|
| G1 | Modifier | Artifact | proposes | Generative | State-gated | Medium | Sync | No |
| G2 | Modifier | Artifact | applies | Generative | State-gated | High | Sync | No |
| G3 | Evaluator | EvalResult | produces | Generative | Immutable | Low | Async | No |
| G4 | ConvDetector | TermDecision | produces | Generative | State-gated | Medium | Sync | No |
| G5 | History | ModRecord | records | Generative | Immutable | None | Sync | No |
| E1 | Evaluator | Artifact | scores | Evaluative | Read-only | Low | Async | No |
| E2 | ConvDetector | History | analyzes | Evaluative | Read-only | Low | Sync | No |
| E3 | SafetyGuard | ModProposal | reviews | Evaluative | State-gated | Critical | Sync | No |
| E4 | HumanOp | EvalCriteria | defines | Evaluative | Human-only | Critical | Async | No |
| R1 | SafetyGuard | Modifier | constrains | Regulatory | State-gated | Critical | Persistent | No |
| R2 | EvalCriteria | Evaluator | governs | Regulatory | Immutable* | Critical | Persistent | Yes |
| R3 | ConvDetector | ImpLoop | terminates | Regulatory | One-shot | Medium | One-shot | No |
| O1 | HumanOp | ImpLoop | monitors | Observational | Passive | Low | Persistent | No |
| O2 | ImpLoop | History | appends | Observational | Append-only | None | Persistent | No |
| O3 | HumanOp | History | queries | Observational | Read-only | Low | Persistent | No |
| C1 | ImpLoop | Evaluator | invokes | Orchestral | State-gated | Medium | On-demand | No |
| C2 | ImpLoop | Modifier | invokes | Orchestral | State-gated | Medium | On-demand | No |
| C3 | ImpLoop | SafetyGuard | consults | Orchestral | State-gated | Critical | On-demand | No |

*Immutable within session; changes require human approval across sessions.

---

## 4. Transitive Relationships

Only one transitive relationship exists in the RSI domain:

```
R2: EvaluationCriteria ──[governs]──▶ Evaluator ──[scores]──▶ Artifact

Transitive closure: EvaluationCriteria ──[governs scoring of]──▶ Artifact
```

**Implication:** Changing EvaluationCriteria transitively changes how all Artifacts are scored. This is why criteria changes require human approval — they have cascading effects across the entire system.

### 4.1 Transitive Chain Analysis

```
HumanOperator ──[defines]──▶ EvaluationCriteria ──[governs]──▶ Evaluator ──[scores]──▶ Artifact
     ↑                                                                              │
     └────────────────────── [monitors outcomes] ──────────────────────────────────┘
```

This forms a **causal loop**: Human defines criteria → Evaluator uses criteria to score → Scores inform human about progress → Human adjusts criteria. The loop is broken by the session immutability invariant (T3) — criteria cannot change within a session.

---

## 5. Semantic Conflict Analysis

### 5.1 Potential Conflicts

| Conflict | Entities | Nature | Resolution |
|----------|----------|--------|------------|
| **Score vs Safety** | Evaluator vs SafetyGuard | Evaluator may score a modification positively while SafetyGuard rejects it | SafetyGuard always wins (B3 invariant) |
| **Speed vs Thoroughness** | Modifier vs ConvergenceDetector | Modifier wants more iterations; ConvergenceDetector may terminate early | ConvergenceDetector has authority (R3) |
| **Autonomy vs Control** | Modifier vs HumanOperator | Modifier wants to self-improve; Human wants oversight | Self-modification requires human approval (B5) |
| **History Growth vs Query Performance** | History vs ConvergenceDetector | History grows unbounded; ConvergenceDetector needs fast queries | Indexing and compaction (Operational concern) |
| **Local vs Global Optimization** | Artifact vs ImprovementLoop | Artifact improvement may not align with global system improvement | Loop-level optimization takes precedence |

### 5.2 Conflict Resolution Precedence

```
1. SafetyGuard (highest authority — blocks unsafe actions)
2. EvaluationCriteria (defines the objective — cannot be overridden by system)
3. ConvergenceDetector (terminates loops — prevents infinite recursion)
4. HumanOperator (override authority — can intervene at any point)
5. ImprovementLoop (orchestration — coordinates but does not override)
6. Evaluator (assessment — informs but does not decide)
7. Modifier (action — proposes but does not apply without approval)
8. History (passive — records but does not influence)
```

---

## 6. Semantic Invariants

| # | Invariant | Statement | Rationale |
|---|-----------|-----------|-----------|
| S1 | **No silent modifications** | Every modification produces a record in History | Auditability |
| S2 | **No unreviewed modifications** | Every modification passes through SafetyGuard | Safety |
| S3 | **No orphan evaluations** | Every EvaluationResult references exactly one Artifact | Traceability |
| S4 | **No circular causation** | The causal graph is a DAG | Prevents infinite loops |
| S5 | **Criteria sovereignty** | Only HumanOperator can modify EvaluationCriteria | Alignment |
| S6 | **Safety primacy** | SafetyGuard verdicts cannot be overridden by any entity except HumanOperator override | Safety |
| S7 | **Temporal ordering** | Cause always precedes effect in all Association paths | Consistency |

---

## 7. Semantic Topology Summary

The RSI domain's semantic structure exhibits:

- **18 directed associations** across 5 semantic classes (Generative, Evaluative, Regulatory, Observational, Orchestral)
- **32% semantic density** — deliberately sparse for loose coupling
- **1 transitive relationship** (EvaluationCriteria → Evaluator → Artifact)
- **5 semantic conflicts** with defined resolution precedence
- **7 semantic invariants** ensuring system integrity
- **Safety-critical associations** concentrated in the Regulatory class
- **Temporal patterns** ranging from synchronous (recording) to asynchronous (evaluation)

The sparsity of the semantic network is the fundamental enabler of recursive self-improvement. Each component can be improved independently because associations are narrow and well-defined. The system trades semantic richness for modularity — a deliberate architectural choice.

---

*Derived from: All 67 SPACE artifacts, all 67 open-ended answers, cross-referenced with 02-semantic-topology.md*
*SPACE — Superb Prompt Automatic Creation Engine v2.1.0*
