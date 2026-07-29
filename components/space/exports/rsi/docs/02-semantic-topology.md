# 02 — Semantic Topology: How Things Relate in the RSI Domain

> **Analytical Lens:** Semantic — the meaning-structure of relationships
> **Source Artifacts:** direct_associations, association_types, hierarchy_structure, inheritance_model, causal_relationships, dependency_chains, relationship_mutability, relationship_composition

---

## 1. The Semantic Field

The RSI domain's semantic structure is defined by **sparse but deep associations** — fewer associations than entities, with most entities connected through transactional verbs rather than static ties. The meaning of each relationship is determined by its verb: "proposes" vs "applies" vs "reverts" carry fundamentally different safety implications.

**Semantic density:** Low. Most entities are isolated in the association graph. The system is modular by design — loose coupling enables independent improvement of each component.

---

## 2. Association Taxonomy

### 2.1 Primary Associations: Transactional

The dominant association type is **transactional** — entities produce, consume, or transform other entities through discrete actions:

```
Modifier ──[proposes]──▶ ModificationProposal
Modifier ──[produces]──▶ Artifact (new version)
Evaluator ──[scores]──▶ Artifact
Evaluator ──[produces]──▶ EvaluationResult
SafetyGuard ──[approves]──▶ ModificationProposal
SafetyGuard ──[rejects]──▶ ModificationProposal
ImprovementLoop ──[executes]──▶ ModificationRecord
History ──[records]──▶ ModificationRecord
ConvergenceDetector ──[evaluates]──▶ History
```

### 2.2 Verb Semantics

The verb taxonomy directly maps to the API design and safety model:

| Verb | Implication | Safety Level |
|------|-------------|:------------:|
| **proposes** | Generates a candidate change (not yet applied) | Low |
| **approves** | Green-lights a proposed change for application | High |
| **rejects** | Blocks a proposed change permanently | Critical |
| **produces** | Creates a new entity (artifact, result, record) | Medium |
| **scores** | Attaches a performance rating (read-only assessment) | Low |
| **records** | Appends to history (immutable, append-only) | None |
| **reverts** | Undoes a previous modification | High |
| **executes** | Runs the improvement loop (orchestration) | Medium |

### 2.3 Hierarchical Associations

The improvement loop **contains** (owns) its sub-entities:

```
ImprovementLoop ──[contains]──▶ Evaluator
ImprovementLoop ──[contains]──▶ Modifier
ImprovementLoop ──[contains]──▶ SafetyGuard
ImprovementLoop ──[contains]──▶ ConvergenceDetector
```

Ownership semantics: if the loop is destroyed, so are its contained entities. This is **composition**, not aggregation.

### 2.4 Peer-to-Peer Associations

Multiple ImprovementLoops can **observe** each other's History for transfer learning:

```
ImprovementLoop_A ──[observes]──▶ History_B
ImprovementLoop_B ──[observes]──▶ History_A
```

This is the only peer-to-peer association in the system. It enables cross-loop learning without tight coupling.

---

## 3. Hierarchy Structure

### 3.1 Tree for Artifact Versioning

Each artifact version has one parent but can have multiple children (branching modifications):

```
Artifact_v1 (original)
  ├── Artifact_v2a (prompt rewrite)
  │     ├── Artifact_v3a (further refinement)
  │     └── Artifact_v3b (alternative approach)
  └── Artifact_v2b (parameter tuning)
        └── Artifact_v3c (combined approach)
```

The **trunk** represents the best-performing lineage. Branches represent exploratory modifications that may or may not be promoted.

### 3.2 DAG for Dependency Tracking

Dependencies form a directed acyclic graph — an artifact may depend on evaluation results from multiple other artifacts:

```
Artifact_C depends on:
  ├── EvaluationResult of Artifact_A
  └── EvaluationResult of Artifact_B
```

This DAG structure means that improving Artifact_A can invalidate assumptions in Artifact_C, triggering re-evaluation.

---

## 4. Inheritance Model

### 4.1 Composition Only

PromptArtifact, ConfigArtifact, and StrategyArtifact do **not** inherit from a common abstract base. Instead, they implement a shared interface but their modification mechanics are fundamentally different:

| Artifact Type | Modification Mechanic | Why No Inheritance |
|--------------|----------------------|-------------------|
| **PromptArtifact** | Text surgery — insert, delete, rewrite spans | Text-specific operations |
| **ConfigArtifact** | Parameter tuning — adjust numeric/string values | Type-specific validation |
| **StrategyArtifact** | Algorithmic redesign — restructure logic flows | Logic-specific analysis |

**Rationale:** Inheritance would force a common modification interface that is too generic to be useful. Each artifact type needs its own modification grammar.

---

## 5. Causal Relationships

### 5.1 Direct Causation

```
Modifier's prompt template ──[causes]──▶ Changes in all subsequent modifications
```

When the Modifier improves its own prompt template, this directly affects every modification it subsequently proposes. This is a **first-order recursive effect**.

### 5.2 Correlation (Emergent)

```
Multiple small improvements across independent artifacts ──[correlate with]──▶ Sudden jumps in overall performance
```

This is the phenomenon of **emergent capability** — the system suddenly "levels up" after accumulating many small improvements that individually seemed insignificant.

### 5.3 Feedback Loops (Critical)

```
Evaluator's scoring function ──[improved by]──▶ RSI loop
RSI loop ──[produces better evaluations]──▶ Evaluator's scoring function
```

When the Evaluator's scoring function is itself improved by an RSI loop, this creates a **positive feedback loop** that must be carefully bounded. Without bounds, this loop can:
1. Cause the Evaluator to score increasingly favorably (reward hacking)
2. Create a divergence between the Evaluator's scores and actual performance
3. Collapse the evaluation framework entirely

**Mitigation:** The SafetyGuard monitors the Evaluator's own improvement trajectory and flags if evaluation scores diverge from benchmark performance by more than a threshold.

---

## 6. Dependency Chains

### 6.1 Complex Dependency Graphs

Improving the Evaluator may require first improving the benchmark dataset, which requires improving data generation prompts, which requires improving the generation Evaluator. This creates chains of 4-5 dependencies:

```
Improve Evaluator
  └── requires: Improve Benchmark Dataset
        └── requires: Improve Data Generation Prompts
              └── requires: Improve Generation Evaluator
                    └── requires: Improve Base Evaluation Framework
```

### 6.2 Topological Resolution

These dependency chains must be resolved in **topological order** — you cannot improve the Evaluator before improving its inputs. The system detects circular dependencies and flags them as architectural issues requiring human intervention.

---

## 7. Relationship Mutability

### 7.1 Mutable with Versioning

All modifications are tracked in History. Previous versions are never deleted, only deprecated. The system can always roll back to any historical version.

**Rollback semantics:** Rolled-back versions are marked as "regressed" to prevent the Modifier from rediscovering the same failed approach. This is a form of **negative transfer learning** — the system learns what not to do.

### 7.2 Immutability Constraints

Some relationships are immutable:
- **EvaluationCriteria ↔ Human Operator:** Only humans can redefine what "better" means
- **SafetyGuard ↔ Hard Rules:** Static safety rules cannot be modified by the RSI loop
- **Benchmark ↔ External Dataset:** The system cannot autonomously change its benchmarks

---

## 8. Relationship Composition

### 8.1 Junction Entities

Two junction entities mediate the primary relationships:

**ModificationProposal** — junction between Modifier and Artifact:
- Carries the proposed change (diff)
- Carries safety review status (approved/rejected/pending)
- Carries expected impact (predicted score delta)

**EvaluationResult** — junction between Evaluator and Artifact:
- Carries scores (multiple dimensions)
- Carries confidence levels
- Carries evaluation metadata (timestamp, model version, benchmark used)

### 8.2 Semantic Implications of Junctions

Junction entities are **information-rich** — they carry the semantic content that gives meaning to the raw associations. Without ModificationProposal, "Modifier produces Artifact" is meaningless. With it, we know what was proposed, why, and what happened.

---

## 9. Semantic Summary

The RSI domain's semantic structure is:

- **Sparse but deep** — few associations, each carrying significant meaning
- **Verb-driven** — the verb determines the safety and semantic implications
- **Hierarchical for ownership** — composition semantics (destroy parent = destroy children)
- **Tree for versioning** — branching modifications with a best-performing trunk
- **DAG for dependencies** — complex chains resolved topologically
- **Mutable with rollback** — versioned, with negative transfer learning
- **Junction-mediated** — ModificationProposal and EvaluationResult carry the semantic weight

The sparsity of associations is a feature: it means each component can be improved independently, which is the fundamental enabler of recursive self-improvement.

---

*Source: SPACE artifacts direct_associations, association_types, hierarchy_structure, inheritance_model, causal_relationships, dependency_chains, relationship_mutability, relationship_composition*
