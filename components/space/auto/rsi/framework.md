# SPACE Framework — Complete Question Set

> Superb Prompt Automatic Creation Engine v2.0.0
> 7 Series · 25 Rounds · 67 Questions · 201 Multi-Choice Follow-ups

---

## Series 1: Conceptual Depth

*Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.*

### Round 1: Domain and Audience

**Q 1.1.1** — What is the primary domain or field this prompt or project addresses? Describe its scope, core concerns, and any relevant sub-disciplines.

Follow-up choices:
- **1.1.1.a** — A single well-established domain (e.g., machine learning, civil engineering)
- **1.1.1.b** — An interdisciplinary space spanning 2-3 domains
- **1.1.1.c** — An emerging or niche area with evolving terminology

**Q 1.1.2** — Who is the intended audience for the generated output? What is their baseline familiarity with this domain?

Follow-up choices:
- **1.1.2.a** — Experts / researchers — people who work in this domain daily
- **1.1.2.b** — Practitioners / professionals — experienced but may need refreshers
- **1.1.2.c** — Learners / general audience — minimal assumed knowledge

### Round 2: Assumptions and Abstraction

**Q 1.2.1** — What foundational concepts, theorems, or prior art can the output take for granted? What must be explained from scratch?

Follow-up choices:
- **1.2.1.a** — Full prerequisites assumed — dive straight into advanced material
- **1.2.1.b** — Core fundamentals assumed; edge cases and advanced topics explained
- **1.2.1.c** — First-principles treatment — no prior knowledge assumed

**Q 1.2.2** — At what level of abstraction should the output operate? Should it be concrete and example-driven, or formal and general?

Follow-up choices:
- **1.2.2.a** — Concrete — specific examples, code snippets, case studies
- **1.2.2.b** — Mixed — conceptual frameworks illustrated with examples
- **1.2.2.c** — Formal — definitions, proofs, mathematical notation, first-order logic

### Round 3: Terminology and Scaffolding

**Q 1.3.1** — What vocabulary, jargon, or notation should be used or deliberately avoided? Are there established standards the output should follow?

Follow-up choices:
- **1.3.1.a** — Standard industry terminology — use common terms precisely
- **1.3.1.b** — Plain accessible language — minimize jargon; explain what is used
- **1.3.1.c** — Formal academic register — precise definitions, technical notation

**Q 1.3.2** — How should complexity be distributed across the output? Should it start simple and deepen, or maintain a consistent level throughout?

Follow-up choices:
- **1.3.2.a** — Progressive — scaffold from simple foundations to advanced topics
- **1.3.2.b** — Flat — consistent complexity level throughout
- **1.3.2.c** — Overview-first — high-level summary then independent deep dives

## Series 2: Ontological Characteristics

*Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.*

### Round 1: Entity Discovery

**Q 2.1.1** — What are the primary entities, objects, concepts, or actors that exist in this domain? List them with brief descriptions.

Follow-up choices:
- **2.1.1.a** — Fewer than 5 core entities — the domain is compact and well-bounded
- **2.1.1.b** — 5–10 entities — moderate complexity with clear boundaries
- **2.1.1.c** — 10–20 entities — rich domain with distinct sub-areas
- **2.1.1.d** — 20+ entities — large domain requiring hierarchical organization
- **2.1.1.e** — Uncertain — exploration may reveal entities not yet known

**Q 2.1.2** — What attributes, properties, or state define each entity? How do entities differ from one another?

Follow-up choices:
- **2.1.2.a** — 1–2 key attributes per entity — simple identifiers suffice
- **2.1.2.b** — 3–5 attributes per entity — moderate descriptive richness
- **2.1.2.c** — 6–10 attributes per entity — detailed characterization
- **2.1.2.d** — 10+ attributes per entity — comprehensive with optional fields
- **2.1.2.e** — Highly variable — attributes differ significantly across entities

**Q 2.1.3** — What natural categories, types, or groupings organize these entities? Are there clear taxonomies or classification schemes?

Follow-up choices:
- **2.1.3.a** — A single flat list — no meaningful sub-groupings
- **2.1.3.b** — 2–3 broad categories partitioning the entities
- **2.1.3.c** — A shallow hierarchy (2 levels deep) of types and subtypes
- **2.1.3.d** — A deep hierarchy (3+ levels) with inheritance
- **2.1.3.e** — Multiple overlapping classification axes (e.g., by function and by scale)

### Round 2: Classification and Core vs. Peripheral

**Q 2.2.1** — Of the entities listed, which are absolutely essential (core) and which are optional, derivative, or contextual (peripheral)?

Follow-up choices:
- **2.2.1.a** — Most entities are core — the domain has little extraneous surface area
- **2.2.1.b** — Roughly equal split between core and peripheral entities
- **2.2.1.c** — A small core (~20%) with a large periphery of optional or derived entities
- **2.2.1.d** — Core/peripheral depends on use case — context-dependent classification
- **2.2.1.e** — Entities exist on a spectrum of centrality — no sharp core/peripheral boundary

**Q 2.2.2** — At what level of granularity should entities be modeled? Should fine distinctions be separate entities or attributes of coarser ones?

Follow-up choices:
- **2.2.2.a** — Coarse-grained — entities are broad; most variation is captured via attributes
- **2.2.2.b** — Moderate — key specializations become distinct entities
- **2.2.2.c** — Fine-grained — every meaningful distinction yields a separate entity
- **2.2.2.d** — Mixed — core domains are fine-grained; peripheral domains are coarse
- **2.2.2.e** — Undecided — granularity should emerge from relationship analysis

**Q 2.2.3** — How do entities relate to each other in terms of sharing, inheriting, or differentiating attributes?

Follow-up choices:
- **2.2.3.a** — Mostly independent — entities share few attributes beyond common identifiers
- **2.2.3.b** — Shared attributes grouped by category — entities in same category share a profile
- **2.2.3.c** — Inheritance hierarchy — subtypes inherit and extend parent attributes
- **2.2.3.d** — Mixin / trait composition — entities compose attribute sets from multiple sources
- **2.2.3.e** — Dynamic — attribute sharing depends on entity state or context

### Round 3: Boundaries and Lifecycles

**Q 2.3.1** — What are the systemic boundaries of this domain? What is explicitly in scope vs. out of scope?

Follow-up choices:
- **2.3.1.a** — Tightly bounded — scope is narrow and well-defined
- **2.3.1.b** — Moderately bounded — clear core with some fuzzy edges
- **2.3.1.c** — Loosely bounded — domain bleeds into adjacent areas
- **2.3.1.d** — Bounded by role/perspective — different stakeholders draw different boundaries
- **2.3.1.e** — Boundaries are discovered — scoping is itself a goal of the process

**Q 2.3.2** — What external entities, systems, or actors interact with this domain but are not part of it?

Follow-up choices:
- **2.3.2.a** — No external interactions — fully self-contained domain
- **2.3.2.b** — 1–3 external actors (users, upstream data sources, downstream consumers)
- **2.3.2.c** — 4–7 external actors with distinct interaction patterns
- **2.3.2.d** — 8+ external actors — the domain is a hub in a larger ecosystem
- **2.3.2.e** — External actors are themselves complex systems requiring partial modeling

**Q 2.3.3** — What is the lifecycle of each entity? How are they created, modified, combined, retired?

Follow-up choices:
- **2.3.3.a** — Simple lifecycle — create, read, update, delete (CRUD)
- **2.3.3.b** — Stateful lifecycle — entities pass through defined states with transition rules
- **2.3.3.c** — Versioned lifecycle — entities have history, revisions, or snapshots
- **2.3.3.d** — Composite lifecycle — entities are assembled/disassembled from sub-entities
- **2.3.3.e** — Evolving lifecycle — entities change type or role over time

### Round 4: Refinement and Constraints

**Q 2.4.1** — Are there entities that are missing from the model so far? What gaps exist in the current entity list?

Follow-up choices:
- **2.4.1.a** — No gaps — the current entity list is comprehensive
- **2.4.1.b** — Minor gaps — 1–2 entities that were initially overlooked
- **2.4.1.c** — Moderate gaps — several entities uncovered during analysis
- **2.4.1.d** — Uncertain — the entity list needs validation against real-world instances
- **2.4.1.e** — Incremental — entities will be added as the domain is explored further

**Q 2.4.2** — Which entities should be merged, split, or reclassified? Are there boundary cases where entity distinctions break down?

Follow-up choices:
- **2.4.2.a** — No changes needed — current classification is sound
- **2.4.2.b** — 1–2 entities need merging or splitting
- **2.4.2.c** — Several entities could be refined, but classification is directionally correct
- **2.4.2.d** — Significant restructuring needed — initial classification was exploratory
- **2.4.2.e** — Ongoing — classification will stabilize as boundary cases are examined

**Q 2.4.3** — What constraints, invariants, or business rules apply to entity instances? What must always be true?

Follow-up choices:
- **2.4.3.a** — Minimal constraints — entities have few invariants beyond uniqueness
- **2.4.3.b** — Moderate constraints — several required fields and validity rules
- **2.4.3.c** — Strict constraints — entities must satisfy complex invariants at all times
- **2.4.3.d** — Context-dependent — constraints vary by entity state or relationship
- **2.4.3.e** — Evolving — constraints will be discovered through usage patterns

### Round 5: Validation and Composition

**Q 2.5.1** — What edge cases, exceptions, or degenerate cases could break the entity model? How should they be handled?

Follow-up choices:
- **2.5.1.a** — Few edge cases — the model is robust to real-world variation
- **2.5.1.b** — Known edge cases — they are well-understood and can be handled explicitly
- **2.5.1.c** — Many edge cases — the model needs to be flexible to accommodate them
- **2.5.1.d** — Edge cases are domain-specific — they vary by deployment or context
- **2.5.1.e** — Edge cases will emerge — the model should accommodate undefined unknowns

**Q 2.5.2** — How do entities compose or aggregate into larger structures? Can entities contain or be composed of other entities?

Follow-up choices:
- **2.5.2.a** — Flat — entities do not compose; all entities are atomic
- **2.5.2.b** — Containment — some entities serve as containers for others (1-level deep)
- **2.5.2.c** — Nested composition — entities form trees or recursive structures
- **2.5.2.d** — Cross-cutting aggregation — entities participate in multiple overlapping groups
- **2.5.2.e** — Dynamic composition — composition structure depends on entity state or context

**Q 2.5.3** — What are the cardinality and multiplicity relationships between entity types? Can an entity have zero, one, or many of another?

Follow-up choices:
- **2.5.3.a** — Mostly one-to-one — entities pair uniquely
- **2.5.3.b** — One-to-many — common pattern with one parent referencing multiple children
- **2.5.3.c** — Many-to-many — entities have complex cross-referencing patterns
- **2.5.3.d** — Mixed — cardinalities vary significantly across entity pairs
- **2.5.3.e** — Conditional — cardinalities depend on entity state or relationship type

## Series 3: Semantic Relationships

*Maps associations, dependencies, hierarchies, and causal chains between entities.*

### Round 1: Direct Associations

**Q 3.1.1** — What direct associations exist between entities? Which entities reference, point to, or are linked to which others?

Follow-up choices:
- **3.1.1.a** — Sparse — fewer associations than entities; most entities are isolated
- **3.1.1.b** — Moderate — roughly one association per entity on average
- **3.1.1.c** — Dense — entities form a richly connected web
- **3.1.1.d** — Clustered — dense connections within groups, sparse between groups

**Q 3.1.2** — What is the nature or type of each association? Is it a use, creation, ownership, or communication link?

Follow-up choices:
- **3.1.2.a** — Single type — all associations are of the same nature
- **3.1.2.b** — 2–3 distinct relationship types (e.g., owns, produces, references)
- **3.1.2.c** — 4–7 distinct relationship types covering different interaction modes
- **3.1.2.d** — 8+ relationship types — rich relational vocabulary needed

### Round 2: Hierarchical and Containment Relationships

**Q 3.2.1** — What parent-child, containment, or hierarchical relationships exist? Which entities are within, belong to, or are part of others?

Follow-up choices:
- **3.2.1.a** — No hierarchy — all entities are peers with no containment structure
- **3.2.1.b** — Shallow hierarchy (1–2 levels) — simple containment chains
- **3.2.1.c** — Deep hierarchy (3+ levels) — multi-level nesting
- **3.2.1.d** — DAG structured — entities form a directed acyclic graph with multiple parents

**Q 3.2.2** — What inheritance, specialization, or generalization relationships exist? Which entities are kinds of other entities?

Follow-up choices:
- **3.2.2.a** — No inheritance — each entity is unique in its type
- **3.2.2.b** — Simple inheritance — a few parent types with child specializations
- **3.2.2.c** — Polymorphic hierarchy — entities can serve as multiple types simultaneously
- **3.2.2.d** — Trait-based — entities pick capabilities from a shared set of traits

### Round 3: Causal and Dynamic Relationships

**Q 3.3.1** — What causal, temporal, or triggering relationships exist? Which entities cause changes in, or are triggered by, others?

Follow-up choices:
- **3.3.1.a** — No causal links — entities change independently
- **3.3.1.b** — Direct causation — entity A creates or changes entity B in a predictable chain
- **3.3.1.c** — Event-driven — state changes propagate as events through the network
- **3.3.1.d** — Feedback loops — entities can influence each other in circular patterns

**Q 3.3.2** — What dependency chains, prerequisites, or ordering constraints exist? Must some entities exist before others can be created or used?

Follow-up choices:
- **3.3.2.a** — No ordering constraints — entities are independent
- **3.3.2.b** — Simple chain — a linear sequence of prerequisites
- **3.3.2.c** — Branching dependencies — a DAG of ordered entity relationships
- **3.3.2.d** — Cyclic dependencies — entities depend on each other (requires careful management)

### Round 4: Composition and Constraints

**Q 3.4.1** — What rules govern how relationships can change? Can associations be created, deleted, or modified at any time, or are there restrictions?

Follow-up choices:
- **3.4.1.a** — Freely mutable — relationships can change at any time with no restrictions
- **3.4.1.b** — State-gated — relationships can only change when entities are in certain states
- **3.4.1.c** — Immutable after creation — relationships are set once and cannot change
- **3.4.1.d** — Versioned — relationship changes create new versions rather than modifying in place

**Q 3.4.2** — How do relationships compose or chain across entities? Can indirect relationships be inferred from direct ones?

Follow-up choices:
- **3.4.2.a** — No composition — only direct relationships matter
- **3.4.2.b** — Transitive — some relationship types imply transitive chains
- **3.4.2.c** — Composable — relationships can be combined according to specific rules
- **3.4.2.d** — Weighted/typed composition — chains have strength or type that affects meaning

## Series 4: Procedural Breadth

*Defines the workflows, procedures, decision points, and error handling for the system.*

### Round 1: Scope and Step Count

**Q 4.1.1** — What is the overall scope of the procedure or workflow? What does it start from and what is its end state?

Follow-up choices:
- **4.1.1.a** — Narrow — a single well-defined task with clear boundaries
- **4.1.1.b** — Moderate — an end-to-end process with several stages
- **4.1.1.c** — Broad — a multi-phase workflow spanning distinct sub-processes

**Q 4.1.2** — How many distinct steps, stages, or phases should the procedure contain? What is the natural breakdown?

Follow-up choices:
- **4.1.2.a** — 2–4 steps — quick process with few handoffs
- **4.1.2.b** — 5–8 steps — moderate complexity with clear waypoints
- **4.1.2.c** — 9+ steps — comprehensive procedure with fine-grained stages

### Round 2: Decision Points and Inputs/Outputs

**Q 4.2.1** — Where are the key decision points, branches, or conditional paths? At which steps must a choice be made that affects the rest of the flow?

Follow-up choices:
- **4.2.1.a** — No branching — a single linear path from start to finish
- **4.2.1.b** — Few branches — 1–2 decision points with 2–3 choices each
- **4.2.1.c** — Moderate branching — multiple decision points with varying path counts

**Q 4.2.2** — What are the expected inputs and outputs at each stage? What data or artifacts flow between steps?

Follow-up choices:
- **4.2.2.a** — Simple I/O — each step takes one input and produces one output
- **4.2.2.b** — Multi-I/O — some steps consume or produce multiple items
- **4.2.2.c** — Network I/O — steps pass data through a shared context rather than direct handoffs

### Round 3: Error Handling and Granularity

**Q 4.3.1** — What fallback paths, error handling, or recovery procedures should be included for when things go wrong?

Follow-up choices:
- **4.3.1.a** — Minimal — errors abort the procedure with a clear message
- **4.3.1.b** — Retry-based — failed steps can be retried with backoff
- **4.3.1.c** — Recovery paths — dedicated handling for known failure modes with alternative flows

**Q 4.3.2** — How granular should each procedural step be? Should steps be coarse (several actions) or fine (one action per step)?

Follow-up choices:
- **4.3.2.a** — Coarse — each step is a meaningful phase (2–5 sub-actions per step)
- **4.3.2.b** — Fine — each step is a single atomic action
- **4.3.2.c** — Mixed — core steps are fine; well-established procedures are coarser

## Series 5: Technical Specifications

*Specifies hardware, software, performance, security, integrations, and deployment requirements.*

### Round 1: Hardware and Infrastructure

**Q 5.1.1** — What hardware platforms or architectures must be supported? (CPU, GPU, mobile, embedded, etc.)

Follow-up choices:
- **5.1.1.a** — Single architecture — x86-64 desktop/server only
- **5.1.1.b** — Dual architecture — e.g., x86-64 + ARM
- **5.1.1.c** — Mobile/embedded — ARM, RISC-V, or specialized hardware
- **5.1.1.d** — Platform-agnostic — must run on any reasonably modern hardware

**Q 5.1.2** — What are the minimum and recommended hardware specs? (RAM, storage, compute, network)

Follow-up choices:
- **5.1.2.a** — Minimal — <1GB RAM, <100MB storage, single-core sufficient
- **5.1.2.b** — Standard — 2–8GB RAM, 1–10GB storage, multi-core recommended
- **5.1.2.c** — High-performance — 16–64GB RAM, SSD storage, GPU recommended
- **5.1.2.d** — Enterprise — 128GB+ RAM, distributed storage, multi-GPU clusters

**Q 5.1.3** — What bandwidth, latency, or networking requirements exist? Is offline operation needed?

Follow-up choices:
- **5.1.3.a** — Always-online — requires reliable internet connection
- **5.1.3.b** — Online with offline fallback — core features work disconnected
- **5.1.3.c** — Primarily offline — sync is optional or batch-oriented
- **5.1.3.d** — Edge-deployed — must operate on intermittent or low-bandwidth connections

**Q 5.1.4** — What storage infrastructure is needed? (databases, object storage, caching, file systems)

Follow-up choices:
- **5.1.4.a** — Single database — one relational or document store covers all needs
- **5.1.4.b** — Primary DB + cache — e.g., PostgreSQL with Redis
- **5.1.4.c** — Polyglot persistence — multiple specialized data stores
- **5.1.4.d** — Distributed storage — sharded databases, multi-region replication

**Q 5.1.5** — What cloud, on-premise, or hybrid infrastructure is targeted? Are there compliance or sovereignty requirements?

Follow-up choices:
- **5.1.5.a** — Cloud-native — designed for a specific cloud provider
- **5.1.5.b** — Cloud-agnostic — portable across providers
- **5.1.5.c** — On-premise only — deployed in private data centers
- **5.1.5.d** — Hybrid — components span cloud and on-premise with strict compliance

### Round 2: Software Stack and Dependencies

**Q 5.2.1** — What programming languages, runtimes, or frameworks are required or preferred?

Follow-up choices:
- **5.2.1.a** — Single language — one ecosystem covers everything
- **5.2.1.b** — Two languages — e.g., backend + frontend split
- **5.2.1.c** — Polyglot — 3+ languages for specialized components
- **5.2.1.d** — Language-agnostic — choice delegated to implementation team

**Q 5.2.2** — What operating systems and environments must be supported?

Follow-up choices:
- **5.2.2.a** — Linux only
- **5.2.2.b** — Linux + macOS (developer-focused)
- **5.2.2.c** — Cross-platform — Linux, macOS, Windows
- **5.2.2.d** — Containerized — only targets Docker/K8s; host OS is irrelevant

**Q 5.2.3** — What existing libraries, services, APIs, or third-party dependencies should be used or avoided?

Follow-up choices:
- **5.2.3.a** — Minimal dependencies — build from standard library where possible
- **5.2.3.b** — Core curated deps — choose established libraries for major concerns
- **5.2.3.c** — Ecosystem-driven — leverage framework convention over custom code
- **5.2.3.d** — Heavy integration — depend on multiple external services and SaaS

**Q 5.2.4** — What versioning, compatibility, or upgrade policies govern the software stack?

Follow-up choices:
- **5.2.4.a** — Latest-stable — always use current versions, update frequently
- **5.2.4.b** — LTS-only — pinned to long-term support versions
- **5.2.4.c** — Semver-constrained — explicit version ranges with CI verification
- **5.2.4.d** — Locked — dependencies are vendored and updated on a release cycle

**Q 5.2.5** — What build systems, CI/CD platforms, and packaging formats are required?

Follow-up choices:
- **5.2.5.a** — Simple build — single build tool, manual or script-based deployment
- **5.2.5.b** — CI-built — automated builds on push, artifact registry
- **5.2.5.c** — Full CI/CD — automated testing, staging, and production deployment
- **5.2.5.d** — GitOps — infrastructure-as-code with automated promotion pipelines

### Round 3: Performance and Scalability

**Q 5.3.1** — What are the throughput, latency, and concurrency requirements? (requests/sec, response time, simultaneous users)

Follow-up choices:
- **5.3.1.a** — Low traffic — <100 req/s, seconds of latency, single-digit concurrency
- **5.3.1.b** — Moderate traffic — 100–10K req/s, sub-second latency, hundreds concurrent
- **5.3.1.c** — High traffic — 10K–100K req/s, low-latency targets, thousands concurrent
- **5.3.1.d** — Internet scale — 100K+ req/s, strict SLOs, global distribution

**Q 5.3.2** — What data volume and growth rate is expected? (storage size, records, throughput)

Follow-up choices:
- **5.3.2.a** — Small — <10GB data, slow growth, single-node viable
- **5.3.2.b** — Medium — 10GB–1TB, moderate growth, needs partitioning
- **5.3.2.c** — Large — 1TB–100TB, rapid growth, requires distributed architecture
- **5.3.2.d** — Massive — 100TB+, petabyte-scale, data lifecycle management needed

**Q 5.3.3** — What availability, uptime, and disaster recovery targets are required?

Follow-up choices:
- **5.3.3.a** — Best-effort — no formal SLA, occasional downtime acceptable
- **5.3.3.b** — Standard — 99.9% uptime, daily backups, basic DR plan
- **5.3.3.c** — High — 99.99% uptime, multi-region redundancy, automated failover
- **5.3.3.d** — Critical — 99.999%+ uptime, active-active, zero-data-loss DR

**Q 5.3.4** — What scalability model is required? (vertical, horizontal, elastic, serverless)

Follow-up choices:
- **5.3.4.a** — Vertical — scale up a single node as needed
- **5.3.4.b** — Horizontal — add/remove nodes with load balancer
- **5.3.4.c** — Elastic — auto-scale based on metrics
- **5.3.4.d** — Serverless — event-driven scale managed by platform

**Q 5.3.5** — What security and compliance standards must be met? (auth, encryption, audit, regulations)

Follow-up choices:
- **5.3.5.a** — Basic — password auth, TLS, no formal compliance requirements
- **5.3.5.b** — Standard — OAuth2/MFA, encryption at rest, audit logging
- **5.3.5.c** — Regulated — SOC2, HIPAA, GDPR, or PCI-DSS requirements
- **5.3.5.d** — High-security — air-gapped, FIPS, zero-trust architecture

### Round 4: Integration and Timeline

**Q 5.4.1** — What external systems, APIs, or services must this system integrate with?

Follow-up choices:
- **5.4.1.a** — No integrations — fully standalone system
- **5.4.1.b** — 1–2 integrations — limited surface area for interoperability
- **5.4.1.c** — 3–7 integrations — multiple external touchpoints
- **5.4.1.d** — 8+ integrations — integration-heavy, requiring an API gateway or ESB

**Q 5.4.2** — What integration protocols, data formats, or standards must be supported?

Follow-up choices:
- **5.4.2.a** — REST/JSON only — simple HTTP-based communication
- **5.4.2.b** — REST + events — REST APIs plus message queue or event stream
- **5.4.2.c** — gRPC + protobuf — type-safe, high-performance contracts
- **5.4.2.d** — Multiple protocols — REST, gRPC, GraphQL, file-based, and binary formats

**Q 5.4.3** — What is the expected timeline, milestones, and delivery cadence?

Follow-up choices:
- **5.4.3.a** — Quick — prototype in weeks, production in 1–3 months
- **5.4.3.b** — Standard — phased delivery over 3–9 months
- **5.4.3.c** — Ambitious — 9–18 months with multiple major releases
- **5.4.3.d** — Large program — 18+ months with distinct workstreams

**Q 5.4.4** — What testing, staging, and rollout strategy is required?

Follow-up choices:
- **5.4.4.a** — Basic — dev + production environments, manual testing
- **5.4.4.b** — Standard — dev, staging, production with automated test suite
- **5.4.4.c** — Robust — preview deployments, canary releases, feature flags
- **5.4.4.d** — Enterprise — full deployment matrix, blue-green, chaos engineering

**Q 5.4.5** — What documentation, training, or knowledge transfer outputs are expected alongside the system?

Follow-up choices:
- **5.4.5.a** — Minimal — inline comments and a README
- **5.4.5.b** — Standard — API docs, architecture decision records, setup guide
- **5.4.5.c** — Comprehensive — full technical docs, runbooks, user manuals
- **5.4.5.d** — Certification-level — training materials, compliance documentation, formal specs

## Series 6: Development Methodologies

*Establishes development methodology, team structure, quality practices, and communication patterns.*

### Round 1: Process and Cadence

**Q 6.1.1** — What development process or methodology best fits this project? How should work be planned and tracked?

Follow-up choices:
- **6.1.1.a** — Sprint-based agile (Scrum) — fixed-length iterations with formal ceremonies
- **6.1.1.b** — Continuous flow (Kanban) — pull-based with WIP limits, no fixed iterations
- **6.1.1.c** — Lean/startup — build-measure-learn cycles, just-in-time planning

**Q 6.1.2** — What is the expected team size, composition, and structure?

Follow-up choices:
- **6.1.2.a** — Solo or pair — 1–2 people, all roles combined
- **6.1.2.b** — Small team — 3–6 people with distinct roles (dev, design, PM)
- **6.1.2.c** — Multiple teams — 7+ people across 2+ squads with coordination overhead

### Round 2: Quality and Review Practices

**Q 6.2.1** — What code review, testing, and quality assurance practices should be followed?

Follow-up choices:
- **6.2.1.a** — Light — ad-hoc reviews, manual testing, minimal automation
- **6.2.1.b** — Standard — mandatory reviews, unit + integration tests, CI gates
- **6.2.1.c** — Rigorous — pair programming, TDD, property-based testing, full automation

**Q 6.2.2** — How should the team handle technical debt, refactoring, and code quality?

Follow-up choices:
- **6.2.2.a** — Opportunistic — clean as you go, no formal tracking
- **6.2.2.b** — Budgeted — allocate X% of each sprint to debt reduction
- **6.2.2.c** — Formal — tracked backlog with dedicated quality improvement cycles

### Round 3: Communication and Collaboration

**Q 6.3.1** — How should the team communicate, share knowledge, and manage decisions?

Follow-up choices:
- **6.3.1.a** — Async-first — written docs, Slack/Teams, minimal meetings
- **6.3.1.b** — Balanced — regular standups, weekly syncs, supplemented by async
- **6.3.1.c** — Sync-heavy — daily standups, frequent pairing, co-located or synchronous remote

**Q 6.3.2** — What is the decision-making and escalation process? How are architectural choices made?

Follow-up choices:
- **6.3.2.a** — BDFL — one person makes final decisions with input
- **6.3.2.b** — Consensus-driven — team agrees, with escalation to lead if deadlocked
- **6.3.2.c** — ADR-based — proposals, reviews, and recorded Architecture Decision Records

## Series 7: Operational / Functional

*Covers deployment, operations, monitoring, maintenance, and long-term stewardship.*

### Round 1: Deployment and Delivery

**Q 7.1.1** — How should the system be deployed, released, and updated in production?

Follow-up choices:
- **7.1.1.a** — Manual deploy — push artifacts, restart services, update on schedule
- **7.1.1.b** — Automated CI/CD — merged to main triggers build + deploy pipeline
- **7.1.1.c** — Progressive delivery — feature flags, canary releases, gradual rollout

**Q 7.1.2** — What environment and release management strategy should be used?

Follow-up choices:
- **7.1.2.a** — Single environment — production only, with local dev
- **7.1.2.b** — Dev / staging / production — standard promotion pipeline
- **7.1.2.c** — Ephemeral environments — per-branch previews, review apps

### Round 2: Runtime Behavior and Observability

**Q 7.2.1** — What logging, monitoring, alerting, and observability infrastructure is needed?

Follow-up choices:
- **7.2.1.a** — Minimal — basic logging to stdout, manual check-ins
- **7.2.1.b** — Standard — structured logging, metrics dashboard, alert on errors
- **7.2.1.c** — Full observability — traces, logs, metrics; SLO monitoring; on-call rotation

**Q 7.2.2** — What configuration and feature management approach should be used at runtime?

Follow-up choices:
- **7.2.2.a** — Static config — environment variables, restart to change
- **7.2.2.b** — Dynamic config — runtime-reloadable config without redeploy
- **7.2.2.c** — Feature flags + config — separate toggle system with gradual rollout

### Round 3: Maintenance and Evolution

**Q 7.3.1** — What maintenance schedule, upgrade policy, and lifecycle management is expected?

Follow-up choices:
- **7.3.1.a** — Firefighting — fix issues as they arise, no scheduled maintenance
- **7.3.1.b** — Regular maintenance — scheduled patch cycles, dependency updates
- **7.3.1.c** — Proactive — automated updates, security scanning, continuous improvement

**Q 7.3.2** — What is the long-term stewardship plan? Who owns the system after initial delivery?

Follow-up choices:
- **7.3.2.a** — Hand-off — delivered to a separate operations team
- **7.3.2.b** — Build-and-run — the same team owns development and operations
- **7.3.2.c** — Community/open-source — external contributions, governance model

---

*Total: 67 questions across 7 series*
