# 01 — Ontological Taxonomy: What Exists in the RSI Domain

> **Analytical Lens:** Ontological — mapping the being-structure of the system
> **Source Artifacts:** entity_list, entity_attributes, entity_categories, entity_core_peripheral, entity_granularity, entity_attribute_sharing, entity_gaps, entity_reclassification, entity_constraints, entity_lifecycles, entity_composition, entity_cardinality, systemic_boundaries, external_actors, edge_cases

---

## 1. The Domain as Ontological Field

RSI occupies a bounded ontological field at the intersection of meta-learning, optimization theory, and AI alignment. The domain is **tightly bounded** — scope is narrow and well-defined, with little extraneous surface area. This compactness is itself a design property: the system must understand itself precisely to improve itself safely.

**Domain statement:** Building systems that analyze their own performance, identify weaknesses, and autonomously modify their strategies, prompts, architectures, or training data to achieve progressively better outcomes.

**Core sub-disciplines:**
- Self-modifying code
- Evolutionary algorithms
- Automated prompt engineering
- Self-play
- Constitutional AI
- Recursive reward modeling

---

## 2. Entity Census

### 2.1 The Eight Fundamental Entities

The RSI domain contains eight entities. Every entity is **core** — the domain has little extraneous surface area. This is not accidental: each entity exists because removing it would collapse a fundamental aspect of recursive self-improvement.

| Entity | Ontological Role | Defined By |
|--------|-----------------|------------|
| **ImprovementLoop** | The recursive cycle itself — the process that binds all others | The act of recursion |
| **Evaluator** | Scores performance; the system's capacity for self-judgment | scoring_function, confidence_threshold, evaluation_depth |
| **Modifier** | Generates improvements; the system's capacity for self-change | modification_type, granularity, safety_level |
| **Artifact** | The thing being improved — prompts, code, configs, strategies | version_chain, parent_id, diff_summary, performance_delta |
| **EvaluationCriteria** | What "better" means — the objective function externalized | Weighted sub-criteria |
| **SafetyGuard** | Prevents dangerous modifications — the system's immune system | Static rules + dynamic learning |
| **History** | Log of all modifications and their effects — the system's memory | Linked list of ModificationRecords |
| **ConvergenceDetector** | Determines when further recursion yields diminishing returns | Improvement velocity prediction |

### 2.2 Entity Attributes (Typed Properties)

Each entity carries typed properties with constraints:

```
Evaluator
  ├── scoring_function: Callable<(Artifact) → number>
  ├── confidence_threshold: float [0, 1]
  └── evaluation_depth: int — how many future states it considers

Modifier
  ├── modification_type: 'prompt' | 'code' | 'strategy' | 'config'
  ├── granularity: 'fine' | 'coarse'
  └── safety_level: What changes are permitted

Artifact
  ├── version_chain: LinkedList<ArtifactVersion>
  ├── parent_id: ArtifactId | null
  ├── diff_summary: string
  └── performance_delta: float

SafetyGuard (split into two entities)
  ├── StaticGuard — hardcoded rules, never violated
  └── DynamicGuard — learns from history what caused degradation

ConvergenceDetector
  ├── improvement_velocity: float — rate of change per cycle
  ├── improvement_trajectory: 'accelerating' | 'decelerating' | 'plateaued'
  └── convergence_threshold: float — when to stop
```

### 2.3 Attribute Sharing Model

Shared attributes are grouped by category. Entities in the same category share a profile. The categorization is by **functional role in the improvement loop**:

```
┌─────────────────────────────────────────────────┐
│  CONTROLLER ENTITIES                            │
│  Evaluator, SafetyGuard, ConvergenceDetector    │
│  Shared: scoring/judging capability, confidence │
├─────────────────────────────────────────────────┤
│  WORKER ENTITIES                                │
│  Modifier, Artifact                             │
│  Shared: modification capability, versioning    │
├─────────────────────────────────────────────────┤
│  INFRASTRUCTURE ENTITIES                        │
│  History, EvaluationCriteria                    │
│  Shared: persistence, querying, versioning      │
└─────────────────────────────────────────────────┘
```

---

## 3. Granularity and Boundaries

### 3.1 Granularity: Fine-Grained

Every meaningful distinction yields a separate entity. The system does not conflate evaluation with modification, or safety with scoring. This fine granularity is essential for the recursive architecture — each entity must be independently improvable.

**Consequence:** The Modifier can improve itself without affecting the Evaluator. The SafetyGuard can be upgraded without changing the Artifact format. ConvergenceDetector can be tuned independently.

### 3.2 Systemic Boundaries: Tightly Bounded

The RSI system operates within a defined sandbox:
- **Inputs:** Fixed evaluation dataset or benchmark
- **Outputs:** Modified artifacts within version control
- **External calls:** LLM APIs (called but never directly modify training weights)
- **Hard boundary:** The system never autonomously changes which benchmarks it uses

### 3.3 Edge Cases

Few edge cases — the model is robust to real-world variation. The tight bounding of the domain absorbs most variability internally.

---

## 4. Lifecycle Ontology

### 4.1 Versioned Lifecycle

All entities have history, revisions, or snapshots. Nothing is destroyed — only deprecated or superseded. This is the ontological commitment of RSI: **improvement is additive, never destructive**.

### 4.2 Artifact State Machine

Artifacts progress through states:

```
Draft → Evaluated → ModificationProposed → SafetyReviewed → Applied → ReEvaluated
  │                                                               │
  └─── Regressed (if re-evaluation shows regression) ────────────┘
```

**Temporal constraint:** Modifications cannot be older than the current version (no time-travel edits).

### 4.3 Entity Gaps and Reclassification

- **Gaps:** The current entity list is comprehensive. No missing entities identified.
- **Reclassification:** 1–2 entities need splitting — SafetyGuard should become StaticGuard + DynamicGuard. EvaluationCriteria should become an aggregate of multiple sub-criteria with weighted importance.

---

## 5. Composition Structure

### 5.1 Nested Composition

Entities form trees or recursive structures. The ImprovementLoop is the root:

```
ImprovementLoop
  ├── Evaluator (owned)
  │     └── EvaluationCriteria (composed)
  ├── Modifier (owned)
  │     └── Artifact (produces)
  ├── SafetyGuard (owned)
  │     ├── StaticGuard (hardcoded rules)
  │     └── DynamicGuard (learned patterns)
  ├── History (shared infrastructure)
  │     └── ModificationRecord[] (one per cycle)
  └── ConvergenceDetector (owned)
```

### 5.2 Cardinality: One-to-Many

The dominant pattern is one parent referencing multiple children:
- One ImprovementLoop → many Artifacts
- One Evaluator → many EvaluationResults
- One Modifier → many ModificationProposals

Exception: One-to-one for ImprovementLoop ↔ Evaluator and ImprovementLoop ↔ SafetyGuard (each loop has exactly one of each).

---

## 6. External Actor Ontology

Three external actors interact with the system through distinct interfaces:

| Actor | Interaction Pattern | Ontological Role |
|-------|-------------------|------------------|
| **Human operators** | Set EvaluationCriteria, intervene/pause loops | Objective-setter, override authority |
| **LLM APIs** | Power Modifier and Evaluator | Capability substrate |
| **Benchmark datasets** | Provide ground-truth evaluation signals | Reality anchor |

**Critical invariant:** The system cannot autonomously change which benchmarks it uses. This prevents Goodhart's Law from collapsing the evaluation framework.

---

## 7. Taxonomic Summary

The RSI domain is a **compact, fine-grained, tightly-bounded ontological field** with:
- 8 fundamental entities (all core, none peripheral)
- 3 functional categories (Controllers, Workers, Infrastructure)
- Versioned lifecycles (additive, never destructive)
- Nested composition (tree structures, one-to-many cardinality)
- 3 external actors with distinct interaction patterns
- Few edge cases due to tight domain bounding

This ontological compactness is both a feature and a constraint: it makes the system comprehensible and analyzable, but also means that adding new entity types requires careful justification against the existing taxonomy.

---

*Source: SPACE artifacts entity_list, entity_attributes, entity_categories, entity_core_peripheral, entity_granularity, entity_attribute_sharing, entity_gaps, entity_reclassification, entity_constraints, entity_lifecycles, entity_composition, entity_cardinality, systemic_boundaries, external_actors, edge_cases*
