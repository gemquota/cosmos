# Series 3: Semantic Relationships

**x = 4 rounds · y = 2 open-ended per round · z = 4 choices per open-ended**

Maps direct, hierarchical, causal, and dynamic connections between entities identified in Series 2.

Context from Series 2: entities=`{entity_list}`, attributes=`{entity_attributes}`, categories=`{entity_categories}`

---

## Round 1: Direct Associations

### Open-Ended 3.1.1
**What direct associations exist between entities? Which entities reference, point to, or are linked to which others?**

Write freely. For each entity pair, describe if and how they connect.

**After answering, choose one:**
- a) Sparse — fewer associations than entities; most entities are isolated
- b) Moderate — roughly one association per entity on average
- c) Dense — entities form a richly connected web
- d) Clustered — dense connections within groups, sparse between groups

---

### Open-Ended 3.1.2
**What is the nature or type of each association? Is it a use, creation, ownership, or communication link?**

Write freely. Name each link type and what it means.

**After answering, choose one:**
- a) Single type — all associations are of the same nature
- b) 2–3 distinct relationship types (e.g., owns, produces, references)
- c) 4–7 distinct relationship types covering different interaction modes
- d) 8+ relationship types — rich relational vocabulary needed

---

## Round 2: Hierarchical and Containment Relationships

### Open-Ended 3.2.1
**What parent-child, containment, or hierarchical relationships exist? Which entities are within, belong to, or are part of others?**

Write freely. Draw the nesting structure if helpful.

**After answering, choose one:**
- a) No hierarchy — all entities are peers with no containment structure
- b) Shallow hierarchy (1–2 levels) — simple containment chains
- c) Deep hierarchy (3+ levels) — multi-level nesting
- d) DAG structured — entities form a directed acyclic graph with multiple parents

---

### Open-Ended 3.2.2
**What inheritance, specialization, or generalization relationships exist? Which entities are kinds of other entities?**

Write freely. Consider `is-a` relationships and type-subtype patterns.

**After answering, choose one:**
- a) No inheritance — each entity is unique in its type
- b) Simple inheritance — a few parent types with child specializations
- c) Polymorphic hierarchy — entities can serve as multiple types simultaneously
- d) Trait-based — entities pick capabilities from a shared set of traits

---

## Round 3: Causal and Dynamic Relationships

### Open-Ended 3.3.1
**What causal, temporal, or triggering relationships exist? Which entities cause changes in, or are triggered by, others?**

Write freely. Describe cause-effect chains and temporal ordering.

**After answering, choose one:**
- a) No causal links — entities change independently
- b) Direct causation — entity A creates or changes entity B in a predictable chain
- c) Event-driven — state changes propagate as events through the network
- d) Feedback loops — entities can influence each other in circular patterns

---

### Open-Ended 3.3.2
**What dependency chains, prerequisites, or ordering constraints exist? Must some entities exist before others can be created or used?**

Write freely. Map the prerequisite relationships between entities.

**After answering, choose one:**
- a) No ordering constraints — entities are independent
- b) Simple chain — a linear sequence of prerequisites
- c) Branching dependencies — a DAG of ordered entity relationships
- d) Cyclic dependencies — entities depend on each other (requires careful management)

---

## Round 4: Composition and Constraints

### Open-Ended 3.4.1
**What rules govern how relationships can change? Can associations be created, deleted, or modified at any time, or are there restrictions?**

Write freely. Consider lifecycle constraints on relationship mutability.

**After answering, choose one:**
- a) Freely mutable — relationships can change at any time with no restrictions
- b) State-gated — relationships can only change when entities are in certain states
- c) Immutable after creation — relationships are set once and cannot change
- d) Versioned — relationship changes create new versions rather than modifying in place

---

### Open-Ended 3.4.2
**How do relationships compose or chain across entities? Can indirect relationships be inferred from direct ones?**

Write freely. Consider transitivity, composition rules, and inference patterns.

**After answering, choose one:**
- a) No composition — only direct relationships matter
- b) Transitive — some relationship types imply transitive chains
- c) Composable — relationships can be combined according to specific rules
- d) Weighted/typed composition — chains have strength or type that affects meaning
