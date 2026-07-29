# Series 2: Ontological Characteristics

**x = 5 rounds · y = 3 open-ended per round · z = 5 choices per open-ended**

Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain. This is the heaviest series in the framework — careful work here pays off downstream.

Context from Series 1: domain=`{domain}`, audience_level=`{audience_level}`, terminology=`{terminology_preferences}`

---

## Round 1: Entity Discovery

### Open-Ended 2.1.1
**What are the primary entities, objects, concepts, or actors that exist in this domain? List them with brief descriptions.**

Write freely. Be exhaustive — you can refine later. Consider both tangible and abstract entities.

**After answering, choose one:**
- a) Fewer than 5 core entities — the domain is compact and well-bounded
- b) 5–10 entities — moderate complexity with clear boundaries
- c) 10–20 entities — rich domain with distinct sub-areas
- d) 20+ entities — large domain requiring hierarchical organization
- e) Uncertain — exploration may reveal entities not yet known

---

### Open-Ended 2.1.2
**What attributes, properties, or state define each entity? How do entities differ from one another?**

Write freely. For each entity from 2.1.1, list the attributes that characterize it.

**After answering, choose one:**
- a) 1–2 key attributes per entity — simple identifiers suffice
- b) 3–5 attributes per entity — moderate descriptive richness
- c) 6–10 attributes per entity — detailed characterization
- d) 10+ attributes per entity — comprehensive with optional fields
- e) Highly variable — attributes differ significantly across entities

---

### Open-Ended 2.1.3
**What natural categories, types, or groupings organize these entities? Are there clear taxonomies or classification schemes?**

Write freely. Look for patterns, families, or dimensions along which entities cluster.

**After answering, choose one:**
- a) A single flat list — no meaningful sub-groupings
- b) 2–3 broad categories partitioning the entities
- c) A shallow hierarchy (2 levels deep) of types and subtypes
- d) A deep hierarchy (3+ levels) with inheritance
- e) Multiple overlapping classification axes (e.g., by function and by scale)

---

## Round 2: Classification and Core vs. Peripheral

### Open-Ended 2.2.1
**Of the entities listed, which are absolutely essential (core) and which are optional, derivative, or contextual (peripheral)?**

Write freely. Consider what the system cannot function without.

**After answering, choose one:**
- a) Most entities are core — the domain has little extraneous surface area
- b) Roughly equal split between core and peripheral entities
- c) A small core (~20%) with a large periphery of optional or derived entities
- d) Core/peripheral depends on use case — context-dependent classification
- e) Entities exist on a spectrum of centrality — no sharp core/peripheral boundary

---

### Open-Ended 2.2.2
**At what level of granularity should entities be modeled? Should fine distinctions be separate entities or attributes of coarser ones?**

Write freely. Consider the tradeoff between precision and complexity.

**After answering, choose one:**
- a) Coarse-grained — entities are broad; most variation is captured via attributes
- b) Moderate — key specializations become distinct entities
- c) Fine-grained — every meaningful distinction yields a separate entity
- d) Mixed — core domains are fine-grained; peripheral domains are coarse
- e) Undecided — granularity should emerge from relationship analysis

---

### Open-Ended 2.2.3
**How do entities relate to each other in terms of sharing, inheriting, or differentiating attributes?**

Write freely. Look for where attribute definitions overlap or diverge.

**After answering, choose one:**
- a) Mostly independent — entities share few attributes beyond common identifiers
- b) Shared attributes grouped by category — entities in same category share a profile
- c) Inheritance hierarchy — subtypes inherit and extend parent attributes
- d) Mixin / trait composition — entities compose attribute sets from multiple sources
- e) Dynamic — attribute sharing depends on entity state or context

---

## Round 3: Boundaries and Lifecycles

### Open-Ended 2.3.1
**What are the systemic boundaries of this domain? What is explicitly in scope vs. out of scope?**

Write freely. Define the edges — what is this model responsible for, and what does it delegate elsewhere?

**After answering, choose one:**
- a) Tightly bounded — scope is narrow and well-defined
- b) Moderately bounded — clear core with some fuzzy edges
- c) Loosely bounded — domain bleeds into adjacent areas
- d) Bounded by role/perspective — different stakeholders draw different boundaries
- e) Boundaries are discovered — scoping is itself a goal of the process

---

### Open-Ended 2.3.2
**What external entities, systems, or actors interact with this domain but are not part of it?**

Write freely. List the things at the boundary that send or receive information.

**After answering, choose one:**
- a) No external interactions — fully self-contained domain
- b) 1–3 external actors (users, upstream data sources, downstream consumers)
- c) 4–7 external actors with distinct interaction patterns
- d) 8+ external actors — the domain is a hub in a larger ecosystem
- e) External actors are themselves complex systems requiring partial modeling

---

### Open-Ended 2.3.3
**What is the lifecycle of each entity? How are they created, modified, combined, retired?**

Write freely. Trace an entity from inception to disposal.

**After answering, choose one:**
- a) Simple lifecycle — create, read, update, delete (CRUD)
- b) Stateful lifecycle — entities pass through defined states with transition rules
- c) Versioned lifecycle — entities have history, revisions, or snapshots
- d) Composite lifecycle — entities are assembled/disassembled from sub-entities
- e) Evolving lifecycle — entities change type or role over time

---

## Round 4: Refinement and Constraints

### Open-Ended 2.4.1
**Are there entities that are missing from the model so far? What gaps exist in the current entity list?**

Write freely. Review the entities from Round 1 with fresh eyes.

**After answering, choose one:**
- a) No gaps — the current entity list is comprehensive
- b) Minor gaps — 1–2 entities that were initially overlooked
- c) Moderate gaps — several entities uncovered during analysis
- d) Uncertain — the entity list needs validation against real-world instances
- e) Incremental — entities will be added as the domain is explored further

---

### Open-Ended 2.4.2
**Which entities should be merged, split, or reclassified? Are there boundary cases where entity distinctions break down?**

Write freely. Look for entities that blur together or that carry dual identities.

**After answering, choose one:**
- a) No changes needed — current classification is sound
- b) 1–2 entities need merging or splitting
- c) Several entities could be refined, but classification is directionally correct
- d) Significant restructuring needed — initial classification was exploratory
- e) Ongoing — classification will stabilize as boundary cases are examined

---

### Open-Ended 2.4.3
**What constraints, invariants, or business rules apply to entity instances? What must always be true?**

Write freely. Consider uniqueness, validity ranges, required relationships, and temporal invariants.

**After answering, choose one:**
- a) Minimal constraints — entities have few invariants beyond uniqueness
- b) Moderate constraints — several required fields and validity rules
- c) Strict constraints — entities must satisfy complex invariants at all times
- d) Context-dependent — constraints vary by entity state or relationship
- e) Evolving — constraints will be discovered through usage patterns

---

## Round 5: Validation and Composition

### Open-Ended 2.5.1
**What edge cases, exceptions, or degenerate cases could break the entity model? How should they be handled?**

Write freely. Stress-test the model — nulls, duplicates, conflicts, missing data.

**After answering, choose one:**
- a) Few edge cases — the model is robust to real-world variation
- b) Known edge cases — they are well-understood and can be handled explicitly
- c) Many edge cases — the model needs to be flexible to accommodate them
- d) Edge cases are domain-specific — they vary by deployment or context
- e) Edge cases will emerge — the model should accommodate undefined unknowns

---

### Open-Ended 2.5.2
**How do entities compose or aggregate into larger structures? Can entities contain or be composed of other entities?**

Write freely. Consider containment, aggregation, and grouping patterns.

**After answering, choose one:**
- a) Flat — entities do not compose; all entities are atomic
- b) Containment — some entities serve as containers for others (1-level deep)
- c) Nested composition — entities form trees or recursive structures
- d) Cross-cutting aggregation — entities participate in multiple overlapping groups
- e) Dynamic composition — composition structure depends on entity state or context

---

### Open-Ended 2.5.3
**What are the cardinality and multiplicity relationships between entity types? Can an entity have zero, one, or many of another?**

Write freely. For each pair of related entities, describe how many of each can be associated.

**After answering, choose one:**
- a) Mostly one-to-one — entities pair uniquely
- b) One-to-many — common pattern with one parent referencing multiple children
- c) Many-to-many — entities have complex cross-referencing patterns
- d) Mixed — cardinalities vary significantly across entity pairs
- e) Conditional — cardinalities depend on entity state or relationship type
