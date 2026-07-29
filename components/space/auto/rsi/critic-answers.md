# SPACE RSI — Critic Answers

> All 67 critic-perspective answers extracted from the variant viewer

---

## Q 1.1.1 — Domain and Audience

**Series 1** · What is the primary domain or field this prompt or project addresses? Describe its scope, core concerns, and any relevant sub-disciplines.

The domain classification is somewhat inflated. SPACE is fundamentally a structured questionnaire with artifact extraction and template-based export — calling it 'specification engineering' overstates the formal rigor. The 326 probes are pre-authored, not generated, so the 'automatic creation engine' moniker is misleading; it's more of a 'guided specification elicitation engine.' A skeptic would note that the LLM integration layer (src/llm/) adds significant complexity but unclear value — if the probes are well-designed, human answers should be sufficient without LLM refinement. The dependency graph between series, while elegant architecturally, creates a rigid workflow that may frustrate users who want to jump to specific sections. The sub-disciplines claimed (ontological modeling, JAD facilitation) are loosely borrowed; the system doesn't actually implement OWL-style reasoning or JAD's multi-stakeholder facilitation. The real risk is that the domain is too niche: developers who need specs usually just write them, and those who don't won't be motivated by a 326-question questionnaire regardless of how well-structured it is.

---

## Q 1.1.2 — Domain and Audience

**Series 1** · Who is the intended audience for the generated output? What is their baseline familiarity with this domain?

The audience definition is too broad and internally contradictory. A 'TypeScript developer building LLM-powered applications' is a very specific persona — these are early adopters building with OpenAI/Anthropic APIs, not the mainstream developer population. Assuming they understand 'npm ecosystems and basic AI/ML concepts' may alienate the larger market of developers who build traditional CRUD apps and could benefit from structured specs. The claim that 'technical writers need structured input for generating documentation pipelines' is aspirational; most technical writers use Markdown in Git repos and would not adopt a 326-question tool for documentation. The framework's explanatory approach ('explains these concepts progressively through Series 1') assumes users will complete all 326 questions, but completion rates for long structured inputs are typically below 15%. The real audience is likely much narrower: technically sophisticated developers who are already bought into structured specification methodologies (like Behavior-Driven Development practitioners) and are looking for a more comprehensive framework. Marketing to a broader audience risks disappointing users who expect a simpler tool.

---

## Q 1.2.1 — Assumptions and Abstraction

**Series 1** · What foundational concepts, theorems, or prior art can the output take for granted? What must be explained from scratch?

The assumption that users understand 'CLI tool usage, npm, and TypeScript basics' is already a significant filter that excludes most software professionals. The real issue is that the 'foundational concepts' SPACE requires aren't just technical — they include an entire methodology (structured elicitation, progressive deepening, artifact dictionaries) that has no mainstream precedent. This means SPACE is simultaneously trying to introduce a new methodology AND build tooling for it, which is a much harder go-to-market challenge than building tooling for an established methodology. The JAD reference is problematic: Joint Application Development was popular in the 1990s enterprise space and is largely forgotten. Referencing it adds no value for the target audience. The OWL-style ontology claim should be dropped entirely — the system does simple key-value artifact extraction, not formal ontological reasoning. Being honest about what the system does (structured questioning with artifact extraction and multi-format export) is more compelling than dressing it up with academic terminology. The assumption that 'the artifact dictionary becomes a living knowledge base' is only true if users return to the tool repeatedly, which assumes a retention mechanism that doesn't exist in the current design.

---

## Q 1.2.2 — Assumptions and Abstraction

**Series 1** · At what level of abstraction should the output operate? Should it be concrete and example-driven, or formal and general?

The mixed abstraction approach risks incoherence. If the document starts abstract and shifts to concrete without clear signposting, readers will be disoriented. The claim that it 'grounds each concept with concrete examples from the actual codebase' assumes the codebase is stable enough to reference — in an active development phase, code examples rot quickly. A more robust approach would be to keep the specification abstract and provide a separate 'implementation guide' with code examples that can be updated independently. The progressive deepening described ('Series 1 establishes grounding, Series 2-3 builds entities, Series 4-7 specifies details') sounds elegant but may not survive contact with real users who want to skip ahead. The abstraction level assumption also fails for the web audience: web users expect instant visual feedback, not progressive methodology revelation. The biggest flaw is assuming that one document format can serve both the architect (who wants diagrams) and the practitioner (who wants code). These are different documents for different audiences, and trying to serve both dilutes both.

---

## Q 1.3.1 — Terminology and Scaffolding

**Series 1** · What vocabulary, jargon, or notation should be used or deliberately avoided? Are there established standards the output should follow?

The terminology enforcement is inconsistent across the existing codebase. The CLI in src/cli/tui.ts uses 'Question' in user-facing text, while the artifact system refers to 'probes.' The web UI (web/) likely has its own terminology choices. This inconsistency will confuse users who see different terms for the same concept across interfaces. The snake_case convention for artifact keys ('entity_list', 'domain_scope') is developer-friendly but not user-friendly — the web UI should present these as human-readable labels ('Entity List', 'Domain Scope') while maintaining the snake_case keys internally. The biggest vocabulary problem is 'session' — in web development, 'session' universally means 'user authentication state,' so using it for 'a run through the questionnaire' will cause confusion. A better term would be 'survey run' or 'spec run.' The deliberate avoidance of 'template' is undermined by the framework itself using context_template as a field name. The claim that terminology follows 'JSON Schema patterns' is aspirational — the framework JSON files use a custom format that doesn't conform to JSON Schema's vocabulary.

---

## Q 1.3.2 — Terminology and Scaffolding

**Series 1** · How should complexity be distributed across the output? Should it start simple and deepen, or maintain a consistent level throughout?

The progressive scaffolding assumption breaks down in practice because SPACE's 326 questions are front-loaded with methodology questions (Series 1: Domain & Audience, Assumptions & Abstraction) that most practitioners will find tedious. The 'simple to deep' progression assumes users are learning the methodology as they answer, but most developers just want to describe their project and get a spec — they don't want to first articulate their 'primary domain,' 'intended audience,' and 'foundational concepts.' A better approach would be to invert the progression: start with the concrete (what are you building? what entities does it have? how do they relate?) and derive the abstract (what domain is this? who is the audience?) as downstream inferences. The claim that 'each series' output should be independently useful' is aspirational — a specification that only covers domain/audience and entity discovery (Series 1-2) is not useful as a development spec. The complexity distribution also fails for the web UI: web users expect visual feedback (charts, progress bars, entity diagrams) which adds implementation complexity that the CLI doesn't face. The progressive model is a content architecture decision being presented as a UX decision, and these serve different masters.

---

## Q 2.1.1 — Entity Discovery

**Series 2** · What are the primary entities, objects, concepts, or actors that exist in this domain? List them with brief descriptions.

The entity list has gaps. There's no 'User' or 'Respondent' entity — the system assumes a single user per session, but real-world use cases involve multiple stakeholders answering different questions. The 'Choice' entity (MultiChoice) conflates two different things: pre-authored follow-up choices (part of the framework definition) and user selections (part of the answer). The src/types/index.ts uses 'MultiChoice' for the definition side and 'multi_choice_id' in AnswerEntry for the selection, which is correct but the naming creates confusion. More critically, there's no 'Version' entity — when the framework is updated (new probes added, existing ones modified), there's no mechanism to track which version of the framework a session was created against, despite framework_version appearing as a string field. The entity model also lacks a 'Tag' or 'Label' entity for categorizing artifacts, which will be needed for the export layer to group related artifacts. The DependencyGraph being separate from the Framework entity is an architectural smell — it should be embedded within the Framework definition.

---

## Q 2.1.2 — Entity Discovery

**Series 2** · What attributes, properties, or state define each entity? How do entities differ from one another?

The ArtifactValue.value typed as 'any' is a significant type safety violation. While it provides flexibility, it means the artifact dictionary cannot be validated at compile time — a typo in a key like 'entity_lsit' instead of 'entity_list' won't be caught until runtime. A better approach would be a typed artifact registry where each known artifact key has a defined value type. The quality_score on AnswerEntry (0.0-1.0) is dangerously vague — what does a 0.7 quality score mean? Without dimension-specific scoring (the QualityResult interface in types/index.ts has completeness/specificity/consistency/actionability but this isn't used on AnswerEntry), the single score is meaningless. The edit_count attribute suggests a 'mutable answers' model, but the dependency graph assumes answers are stable once submitted — if a user edits a Series 1 answer after completing Series 3, downstream artifacts may become inconsistent. The framework_version field is a string with no schema — there's no mechanism to compare versions or detect incompatibilities. The ProgressState.completed_rounds being stored as string[] means progress tracking requires array scanning rather than a more efficient set or bitmap.

---

## Q 2.1.3 — Entity Discovery

**Series 2** · What natural categories, types, or groupings organize these entities? Are there clear taxonomies or classification schemes?

The three-category classification is neat but misses important cross-cutting concerns. The LLM integration layer (src/llm/) doesn't fit cleanly into any category — it operates on Runtime entities (Answers) using Structural entity context (Questions) to produce enhanced Runtime entities (refined Answers, extracted Artifacts). The Intelligence layer (src/intelligence/) similarly spans categories, reading Runtime entities and producing meta-information about them. The event system (SpaceEvent types in types/index.ts) is an orthogonal concern that cuts across all three categories. This categorization also creates a misleading implication that the layers are strictly sequential (define → run → export), when in reality the system supports iterative workflows where users run a session, export a partial spec, refine answers, and re-export. The 'distinct persistence strategies' claim (JSON files for Structural, SQLite for Runtime, on-demand for Output) is incorrect — the framework JSON files are actually compiled into the source code at build time, not loaded dynamically. This means customizing the framework requires rebuilding the tool, which undermines the 'framework authoring' product opportunity.

---

## Q 2.2.1 — Classification and Core vs. Peripheral

**Series 2** · Of the entities listed, which are absolutely essential (core) and which are optional, derivative, or contextual (peripheral)?

The 5-entity core is debatable. The Engine is not an entity — it's a service/controller that operates on entities. Including it in the 'core entity' list conflates the entity model with the service layer, which is an architectural smell. The true core entities are Framework, Session, Question, and Artifact. Engine, Series, Round, and Choice are structural or behavioral concerns, not entities. This misclassification could lead to poor design decisions, like giving Engine persistent state (it shouldn't — it's stateless and operates on SessionState). The claim that 'the system could function with a flat list of questions' understates the importance of the Series/Round structure — without it, the dependency graph cannot function, which means artifacts cannot be consumed by downstream questions. The Series/Round hierarchy is not peripheral; it's essential for the progressive specification methodology that defines SPACE. The peripheral classification of Project is also wrong — multi-session support (Project) is essential for any real-world usage where the first attempt is rarely the final specification.

---

## Q 2.2.2 — Classification and Core vs. Peripheral

**Series 2** · At what level of granularity should entities be modeled? Should fine distinctions be separate entities or attributes of coarser ones?

The 'moderate granularity' answer is a hedge that avoids committing to a clear position. The reality is that the current implementation has inconsistent granularity: FrameworkDefinition embeds Series/Round/Question/Choice as a deep hierarchy, but SessionState embeds Answers as a flat Record<string, AnswerEntry>. This inconsistency means framework questions can be navigated hierarchically (series → round → question), but answers cannot (you query by question_id, not by series/round/question path). The ArtifactDictionary is a flat Record<string, ArtifactValue> that conflates entity types — 'entity_list' (an array of entity names) and 'domain_scope' (a string description) have completely different value types but share the same dictionary. The 'four-entity-test' described in the existing answer (distinct lifecycle, unique relationships, different attributes, independent query) is too strict — it would keep Question and Choice as the same entity since they share the same lifecycle and can't be queried independently. The granularity problem is that SPACE's model tries to serve both a static definition (framework) and a dynamic execution (session) with overlapping but non-identical entity sets, creating confusion about where boundaries should be drawn.

---

## Q 2.2.3 — Classification and Core vs. Peripheral

**Series 2** · How do entities relate to each other in terms of sharing, inheriting, or differentiating attributes?

The entity relationship model has a significant flaw: it assumes a single framework version per project, but the relationship between Session.framework_version and FrameworkDefinition is implicit (matched by string comparison) rather than explicit (foreign key with constraint). If a framework is updated and a session was created with the old version, there's no mechanism to detect or handle the mismatch. The ArtifactValue derived_from field (string[]) claims to track multi-hop derivation chains, but the artifact extraction in src/data/artifact-mapping.ts doesn't populate this field — it's aspirational, not implemented. The shared attributes (id, created_at, updated_at) are defined inconsistently: SessionMeta has them, but ArtifactValue does not (it has source_question_id and last_updated but no id or created_at). This inconsistency means artifacts cannot be individually tracked, versioned, or deleted. The EAV pattern for ArtifactDictionary is a known anti-pattern that sacrifices query performance and type safety for flexibility — a typed artifact registry would be more maintainable.

---

## Q 2.3.1 — Boundaries and Lifecycles

**Series 2** · What are the systemic boundaries of this domain? What is explicitly in scope vs. out of scope?

The boundary definitions are aspirational rather than enforced. The web/ directory contains a server.mjs that serves a React frontend — this is technically a web server, contradicting the 'no HTTP API' claim. The integration/ directory exists but is apparently empty or experimental, suggesting the boundary is porous. More critically, the system's boundaries don't address data privacy: SPACE collects detailed project specifications that may contain proprietary information, but there's no encryption at rest, no access control, and no data retention policy. The 'out of scope' list excludes team collaboration, but the Project entity (src/types/index.ts) explicitly supports multiple sessions — this is team collaboration at the data model level. The narrow scope claim also ignores the LLM integration: by sending answers to external LLM providers (OpenAI, Anthropic, etc.), SPACE is de facto sharing project information with third parties, which is a significant scope expansion that isn't acknowledged. The boundary between 'SPACE' and 'the framework JSON files' is also unclear — are the 326 probes part of the tool or part of the methodology? This distinction matters for licensing and customization.

---

## Q 2.3.2 — Boundaries and Lifecycles

**Series 2** · What external entities, systems, or actors interact with this domain but are not part of it?

The external actor model underserves the most critical external actor: the downstream consumer of SPACE's output. The specification generated by SPACE is consumed by developers, project managers, and AI coding tools — but there's no formal interface for these consumers. The ExportResult type (content, filename, mime_type, size_bytes) is too generic to be useful as an integration contract. A real integration would require a structured specification schema (JSON Schema, OpenAPI-style) that downstream tools can validate against. The LLM provider abstraction is also weaker than claimed — the null-provider and template-provider are test doubles, not production fallbacks. If the real LLM provider fails, the system's artifact extraction quality drops significantly. The Storage Backend abstraction is unnecessary complexity for a CLI tool — SQLite is sufficient and the filesystem backend adds maintenance burden without clear user value. The most concerning external actor gap is the lack of a webhook or event system for triggering downstream workflows when a specification is completed.

---

## Q 2.3.3 — Boundaries and Lifecycles

**Series 2** · What is the lifecycle of each entity? How are they created, modified, combined, retired?

The lifecycle model has gaps. The Session lifecycle allows 'abandoned' as a terminal state, but there's no mechanism to 'resume' an abandoned session — the status field doesn't include a 'resumed' state. In practice, users will want to abandon and later resume sessions, which requires either a new state ('paused') or a convention (abandoned sessions can be resumed by setting status back to in_progress). The Artifact lifecycle claims 'refined' as a state, but ArtifactValue has no status field — refinement is tracked implicitly by the confidence score and last_updated timestamp. This means you can't query 'all finalized artifacts' without inferring the state from other fields. The Snapshot lifecycle being immutable is correct for data integrity but problematic for storage — if a user creates many snapshots (every question), the storage grows unboundedly with no garbage collection mechanism. The export lifecycle being 'delivered' doesn't account for the case where the user requests an export but doesn't have write permissions to the output directory — the ExportResult is generated but never persisted, creating a ghost export.

---

## Q 2.4.1 — Refinement and Constraints

**Series 2** · Are there entities that are missing from the model so far? What gaps exist in the current entity list?

The claim that 'no major entity gaps exist' is premature. The most significant missing entity is the 'Template' — a reusable specification template that users can start from instead of answering all 326 questions. The existing system forces every user through the same exhaustive process, which is why completion rates will be low. A Template entity would allow sharing 'starter specifications' that pre-fill common answers, drastically reducing friction. The second missing entity is 'Metric' — there's no way to define custom quality metrics beyond the fixed four dimensions (completeness, specificity, consistency, actionability). Different domains need different quality criteria. The third gap is the lack of a 'Constraint' entity — business rules and invariants are discussed in the answers but not modeled as first-class objects that can be validated, versioned, and exported. The 'no gaps' assessment reflects the current narrow scope (single-user CLI tool) but fails to anticipate the natural expansion to collaborative, customizable, and extensible use cases.

---

## Q 2.4.2 — Refinement and Constraints

**Series 2** · Which entities should be merged, split, or reclassified? Are there boundary cases where entity distinctions break down?

The entity boundary verification is circular — it validates that current boundaries are consistent with current usage, but doesn't test whether better boundaries exist. The Round entity is the weakest link: it's primarily a grouping mechanism for questions within a series, with the 'focus' attribute as its only unique property. The focus string could be a field on Question instead, eliminating the Round entity entirely. This would simplify the hierarchy from 5 levels (Framework → Series → Round → Question → Choice) to 4 levels (Framework → Series → Question → Choice). The 'focus' grouping could be achieved through question tags or metadata rather than a structural entity. The cost of removing Round would be minimal (update framework JSON structure, update loaders) but the benefit is a simpler mental model. Similarly, the 'depends_on' field on SeriesDefinition duplicates information that could be derived from the DependencyGraph — having both creates a consistency risk where the two representations diverge.

---

## Q 2.4.3 — Refinement and Constraints

**Series 2** · What constraints, invariants, or business rules apply to entity instances? What must always be true?

The constraint system has weaknesses. The structural constraints (exactly 7 series, 3-5 rounds) are enforced by convention, not by code — if someone manually edits the framework JSON to add an 8th series, the system may partially work or fail unpredictably. The runtime dependency constraint is too rigid: it prevents users from answering later questions even when they have the knowledge, forcing them through the full progression. A better approach would be to allow 'preview mode' where users can see and partially answer any question, with a 'validation mode' that checks completeness before export. The data integrity constraints are incomplete: there's no validation that ArtifactValue.confidence is between 0 and 1, no validation that AnswerEntry.quality_score matches the QualityResult dimensions, and no validation that the artifact dictionary keys follow a naming convention. The 'export must have all required artifacts' constraint is enforced by src/export/ but the error message is unclear — users need to know exactly which artifacts are missing and which questions produce them.

---

## Q 2.5.1 — Validation and Composition

**Series 2** · What edge cases, exceptions, or degenerate cases could break the entity model? How should they be handled?

The edge case analysis is incomplete. The most critical missing edge case is 'answer quality degradation' — what happens when a user gives intentionally bad or nonsensical answers? The artifact extraction will produce garbage artifacts, the quality scorer will flag them, but the system doesn't have a mechanism to block low-quality answers or force refinement. Another missing edge case: 'framework update during active session' — if the framework JSON is updated while a session is in progress, the session may reference questions that no longer exist. The concurrent access model ('single-writer') is described but not enforced — there's no file locking implementation in the codebase, just the assumption that users won't run two CLI instances simultaneously. The LLM fallback to 'template-provider' is a poor fallback because the template provider produces generic, unhelpful artifacts — a better fallback would be to skip artifact extraction for that question and flag it for manual review. The snapshot restoration claim is aspirational — the snapshot-manager creates snapshots but there's no UI or CLI command to restore from a snapshot.

---

## Q 2.5.2 — Validation and Composition

**Series 2** · How do entities compose or aggregate into larger structures? Can entities contain or be composed of other entities?

The strict containment hierarchy is overly rigid for a tool that aims to be flexible. Real-world projects don't always fit neatly into 7 predefined series — some projects need more domain questions and fewer technical questions. The containment hierarchy prevents users from reordering, merging, or skipping series. The cross-cutting dependency relationships are described but the DependencyGraph in src/types/index.ts uses a separate node/edge structure that duplicates information already encoded in the series' depends_on, consumes, and provides fields. This duplication creates a consistency risk — if the depends_on array and the DependencyGraph edges disagree, the system may behave unpredictably. The artifact dictionary being flat is a limitation — as the number of artifacts grows (potentially 100+), the flat structure becomes unwieldy. A hierarchical artifact organization (grouping artifacts by series or by entity type) would improve navigability. The aggregate root pattern assumes the entire project is loaded at once, which won't scale for projects with many sessions.

---

## Q 2.5.3 — Validation and Composition

**Series 2** · What are the cardinality and multiplicity relationships between entity types? Can an entity have zero, one, or many of another?

The cardinality model has issues that will surface as the product matures. The fixed 1:7 series cardinality is the most problematic — it assumes every project needs all 7 series, but many projects will only need 3-4. The system should support variable series counts, which means the '7' should be a derived value from the framework definition, not a hardcoded constant. The 0..326 Session→Answer cardinality is technically correct but misleading — it implies all 326 answers are equally required, when in practice some questions are conditional or optional. The dependency graph's many-to-many cardinality creates O(N²) worst-case complexity for topological sorting, though with only 7 series this is negligible. The most concerning cardinality issue is Artifact→Question: the many-to-one claim is incorrect for derived artifacts that are synthesized from multiple questions. The ArtifactValue type supports derived_from: string[] which implies many-to-many, contradicting the stated many-to-one. This inconsistency between the stated model and the actual implementation creates confusion for anyone trying to reason about the data model.

---

## Q 3.1.1 — Direct Associations

**Series 3** · What direct associations exist between entities? Which entities reference, point to, or are linked to which others?

The '12 associations across 10 entities' framing understates the coupling problem. Session is the most connected entity with 6 associations, which makes it a change-magnet — modifying anything about Session state (adding a new artifact type, changing export format) ripples across at least 6 call sites. This violates the single-responsibility principle at the architectural level: Session currently owns answer storage, artifact extraction, project membership, export compilation, question tracking, and status management. A more robust design would extract at least two of these responsibilities: artifact extraction into an ArtifactExtractor service and export compilation into an ExportCompiler. The bidirectional containment in the Framework hierarchy (both parent and child hold references) creates a maintenance burden — when deserializing from JSON in `src/data/framework-loader.ts`, both directions must be reconstructed, and if only one direction is built, the other is silently stale. The unidirectional Question → Choice association is inconsistent with the rest: if the system ever needs to find which Questions reference a Choice (e.g., for validation of custom follow-up selections), it would require a linear scan. More critically, there's no association between Framework and Session at all — a Session doesn't formally know which Framework it was created from, which means resuming a session after a Framework update is inherently unsafe (the question IDs might still exist but their positions or meanings may have changed).

---

## Q 3.1.2 — Direct Associations

**Series 3** · What is the nature or type of each association? Is it a use, creation, ownership, or communication link?

The five-type taxonomy is clean but has a significant gap: there's no MUTATES relationship type. When a user goes back and changes an answer (which the system supports via overwriting), that change can invalidate artifacts produced downstream. But there's no formal mechanism to propagate mutations through the CONSUMES chain. If a user changes their answer to Question 5 in Series 1, the artifact produced from that answer changes, and the artifacts produced by Series 3 (which consumed Series 1 artifacts) may now be inconsistent with the original answers. The system handles this by silently overwriting, but there's no dirty-flagging or staleness detection. The DEPENDS_ON type is also under-specified: the answer says it's 'about ordering, not data flow,' but in practice the dependency resolver in `src/engine/dependency-resolver.ts` treats DEPENDS_ON and CONSUMES identically — both just add edges to the execution graph. This means there's no way to express 'Series B must run after Series A' without also implying 'Series B may need Series A's artifacts.' A more honest design would merge them into a single type or clearly separate their implementations. The CONTAINS implementation claim ('deleting the parent deletes all children') is aspirational — looking at the actual filesystem storage in `src/storage/filesystem.ts`, there's no cascade delete logic. If you delete a Session file, the Answer objects within it are gone only because they were serialized together, not because of any active cascade mechanism.

---

## Q 3.2.1 — Hierarchical and Containment Relationships

**Series 3** · What parent-child, containment, or hierarchical relationships exist? Which entities are within, belong to, or are part of others?

The 'two independent hierarchies' description glosses over a coupling point that's not well-managed: Session tracks `currentQuestionId` as a string reference into the Framework tree, but there's no schema validation that this ID maps to a valid path in the current Framework version. If the framework.json is updated (renumbering questions, adding Series 8), a resumed session could have a stale `currentQuestionId` that points to a non-existent question. The `question-router.ts` presumably handles this, but the answer doesn't specify whether it fails gracefully or crashes. The depth-4 maximum is also a constraint that could become problematic: if SPACE adds a 'sub-question' concept (e.g., follow-up probes that branch into their own mini-trees), the depth would increase to 5, and the CLI navigation would need restructuring. The claim that 'no entity has multiple parents at the same level' is true for the Framework hierarchy but potentially false for the runtime hierarchy — if a future feature allows an Answer to belong to multiple Sessions (e.g., shared answers between related projects), the Session → Answer relationship would become a DAG, not a tree. The branching factor of 3.5 is described as 'average,' but the variance is likely high — some Rounds have 2 questions while others have 5, which means progress tracking feels uneven. A user completing a 2-question Round feels like they made no progress, while completing a 5-question Round feels like a slog. The progress bar in `src/engine/progress.ts` should account for this by weighting progress by question count, not just round count.

---

## Q 3.2.2 — Hierarchical and Containment Relationships

**Series 3** · What inheritance, specialization, or generalization relationships exist? Which entities are kinds of other entities?

The absence of inheritance is presented as a clean design choice, but it introduces a practical problem: code duplication across entity types. Series, Round, and Question all have similar properties (id, name, description, optional metadata) but each declares them independently. When you add a new property like `createdAt: Date` to all entities, you have to modify 10 interfaces instead of one base class. The mixin approach mentioned as a solution is not visible in the actual codebase — `src/types/index.ts` shows standalone interfaces with no shared base. This suggests the 'shared traits via mixins' claim is aspirational, not implemented. The artifact type hierarchy being 'informal' is also a weakness: if artifact keys are just strings with no schema enforcement, a typo in a framework JSON (`'entites'` instead of `'entities'`) would silently produce an invalid artifact that downstream Series would fail to consume at runtime rather than at load time. A more robust design would define artifact keys as an enum or a Zod schema in `src/data/artifact-mapping.ts` and validate them during framework loading. The 'extensible without code changes' claim also breaks down for complex customizations — if a user wants to add a custom Series that calls an external API, they can't do it with JSON configuration alone; they need to write TypeScript. The architecture doesn't cleanly separate 'configuration-level extensibility' from 'code-level extensibility,' which means the boundary is ambiguous and users will discover it at the worst possible time (mid-implementation).

---

## Q 3.3.1 — Causal and Dynamic Relationships

**Series 3** · What causal, temporal, or triggering relationships exist? Which entities cause changes in, or are triggered by, others?

The claim that 'no artifact flows backward' is architecturally clean but practically problematic. Real specification processes are iterative — users often realize mid-session that their initial answers were wrong or incomplete. When a user changes an answer in Series 1, all artifacts produced by Series 1 change, and all artifacts produced by downstream Series that consumed those artifacts are now stale. The system doesn't detect or handle this staleness. The 're-answer and overwrite' approach means the Session's artifact dictionary silently changes, but any Exports generated before the change are now outdated. There's no 'staleness indicator' showing which parts of the specification are based on old data. The monotonic growth claim is also slightly misleading: while the artifact dictionary grows in terms of key count, individual artifact values can change (when answers are re-answered), so the 'snapshot captures the complete state' claim is only true for the moment it was taken. A more honest design would track artifact versions (hash or timestamp) and expose a 'specification version' that changes whenever any upstream artifact changes. The snapshot system in `src/engine/snapshot-manager.ts` could support this by storing artifact hashes alongside values, enabling efficient staleness detection without re-comparing entire artifacts. The absence of backward causation also means the system can't implement 'what-if' analysis ('what if I changed my answer to Question 5?') without re-running the entire downstream chain, which limits the tool's exploratory value.

---

## Q 3.3.2 — Causal and Dynamic Relationships

**Series 3** · What dependency chains, prerequisites, or ordering constraints exist? Must some entities exist before others can be created or used?

The dependency chain creates a significant UX problem: the user is forced to answer Series 1 questions (abstract vision questions) before they can get to the questions they actually care about (implementation details in Series 5-7). This is a common complaint with progressive disclosure tools — users feel 'trapped' in early stages. The prerequisite enforcement in `dependency-resolver.ts` is strict: if `canStartSeries()` returns false, the Series is completely inaccessible. A more flexible design would allow 'partial entry' where users can see Series 5 questions but can't submit them until prerequisites are met — this creates anticipation and lets users see where the journey is going. The linear execution order (Series 1 → 2 → 3 → ...) is also an oversimplification. In reality, the dependency graph for SPACE's 7 Series is close to linear, but it could be more parallel: Series 5 (Infrastructure) and Series 6 (Team) could potentially run in parallel since they depend on different upstream Series. The current implementation doesn't exploit this parallelism, which is fine for a CLI tool but would be a bottleneck for a web-based multi-user version. The prerequisite validation doesn't handle 'partial artifact availability' — if Series 3's `consumes` array lists ['entities', 'relationships'] but only 'entities' is available (because Series 2 produced it but relationships are from Series 3 itself, which hasn't run yet), the entire Series is blocked rather than allowing partial progress. A more nuanced design would allow partial artifact consumption with warnings.

---

## Q 3.4.1 — Composition and Constraints

**Series 3** · What rules govern how relationships can change? Can associations be created, deleted, or modified at any time, or are there restrictions?

The 'append-only/replace-only' mutation model is simpler than it should be, but the implementation has gaps. The claim that Framework entities are 'immutable at runtime' is enforced by convention (the Engine doesn't modify them) rather than by TypeScript's `readonly` modifier — if the codebase doesn't use `Readonly<Framework>` consistently, accidental mutation is possible. The replace-only model for Answers has a subtle problem: re-answering a question produces new artifacts, but the old artifacts aren't tracked. If a user re-answers Question 5 in Series 1, the artifact dictionary is updated, but there's no record of what the previous artifact value was. This makes debugging specification changes difficult — you can't answer 'why did this part of the specification change?' without manually comparing old and new artifact values. The Export write-once model also has a practical issue: re-exporting overwrites all output files, even for formats that didn't change. If a user exported to Markdown and YAML, then re-answered a question and re-exported, both files are rewritten even though the YAML output might be identical. A more efficient design would diff the new output against the existing file and only write if changed. The 'no explicit deletion' claim is technically true but misleading — setting an answer to an empty object is functionally equivalent to deletion, which means the system does support deletion, it just does it in a roundabout way that preserves the answer ID. This creates a data quality issue: empty answers are indistinguishable from unanswered questions in some code paths, leading to potential confusion in progress tracking.

---

## Q 3.4.2 — Composition and Constraints

**Series 3** · How do relationships compose or chain across entities? Can indirect relationships be inferred from direct ones?

The 'traversable from any entity' claim is overstated. In practice, traversal requires knowing the starting entity's type and following a specific code path — there's no generic 'graph traversal' API. The provenance chain described (Export → Session → Answer → Question) works, but it's implemented differently in each exporter. The Markdown exporter includes provenance annotations, but the JSON exporter in `src/export/formatters/json-exporter.ts` doesn't — it outputs the raw artifact data without source references. This inconsistency means provenance tracking only works for some export formats. The lazy resolution approach has a performance problem that the answer glosses over: when generating a full specification, the exporter needs to resolve the provenance for every artifact, which means iterating over all Answers for each artifact's source question. For 326 Questions and ~100 artifacts, this is 32,600 potential lookups — small by modern standards, but it's O(n×m) where n is artifacts and m is questions, not the O(n) claimed. The 'Choice doesn't have parentQuestionId' limitation is more serious than acknowledged — it means you can't implement a 'why was I asked this question?' feature that traces from a follow-up choice back to its parent question without scanning the entire Framework tree. The relationship graph computation in `dependency-resolver.ts` being rebuilt on resume is a real performance issue for large frameworks — if a user has completed 5 of 7 Series and resumes, the resolver recomputes the entire graph even though only the last 2 Series matter. A more efficient approach would be to cache the graph in the Session snapshot and only recompute for unstarted Series.

---

## Q 4.1.1 — Scope and Step Count

**Series 4** · What is the overall scope of the procedure or workflow? What does it start from and what is its end state?

The scope definition has a significant gap: it doesn't address what happens when the user provides poor-quality answers. The procedure accepts any text input for open-ended questions without validation, which means a user who rushes through the questions will produce a garbage-in-garbage-out specification. The scope should include a quality gate — a step after each Series that evaluates artifact quality and warns the user if answers are too short, too vague, or contradictory. The current design treats all answers as equally valid, which is a failure mode for a specification tool. The procedure scope also doesn't address the 'what next?' problem: after the specification is exported, what does the user do with it? The procedure ends with files on disk, but there's no integration with project management tools, no import into IDEs, no generation of code scaffolds. This is an intentional scope limitation, but it creates a 'dead end' UX where the user has a beautiful specification but no clear path to implementation. The resume feature, while essential, introduces a scope creep risk: if the user resumes a session weeks later, they may have forgotten the context of their earlier answers. The procedure should include a 'recap' step that shows the user a summary of previous answers before presenting new questions. The atomic file write claim for session persistence is good, but the procedure doesn't handle the case where the disk is full — `fs.writeFileSync()` will throw, and the SIGINT handler will crash without saving. A more robust scope would include disk space validation at session creation.

---

## Q 4.1.2 — Scope and Step Count

**Series 4** · How many distinct steps, stages, or phases should the procedure contain? What is the natural breakdown?

The 8-stage decomposition is clean but has a significant UX problem: the stages are not equally sized. Series 1 (Vision) has ~15 Questions and takes 15-20 minutes. Series 7 (Deployment) also has ~15 Questions. But Series 3 (Relationships) has ~50 Questions and takes 45-60 minutes. The stage count of 8 doesn't reflect this imbalance — the progress display shows 'Series 3 of 7' which suggests 43% completion, but the actual effort remaining is much higher because Series 3 is the longest. A more honest progress model would weight stages by Question count, not by Series count. The claim that 'each stage produces distinct, independently valuable artifacts' is aspirational — Series 1 produces 'vision' artifacts, but these are too abstract to be useful without the downstream artifacts. You can't review Series 1 output in isolation and get value from it. The 'natural pause points' between Series are also not as natural as claimed — the user is in a flow state after completing 10 Questions in Series 2, and stopping at a Series boundary requires conscious effort. The implementation's stage count being 'determined by the Framework's Series count' is a flexibility that could backfire: a malicious or malformed framework.json could define 100 Series, creating a 10-hour procedure. The Engine should enforce a maximum Series count (e.g., 12) to prevent abuse. The three-level progress display (Series/Round/Question) is informative but overwhelming — showing all three levels simultaneously creates visual noise. A better UX would show only the current level (Question progress within a Round) and expand to show Series progress only when requested.

---

## Q 4.2.1 — Decision Points and Inputs/Outputs

**Series 4** · Where are the key decision points, branches, or conditional paths? At which steps must a choice be made that affects the rest of the flow?

The 'mostly static' 326 Questions is a significant limitation that the answer acknowledges but doesn't fully address. Without conditional branching, a solo developer building a CLI tool answers the same questions as a 10-person team building a microservices platform. The 60% of Questions about team composition, deployment infrastructure, and communication patterns are irrelevant to the solo developer, but they must still answer them (or skip with empty answers). This creates a poor UX for a large segment of the target audience. The 'soft branching' via artifact context is not a real substitute for conditional branching — the same Questions are shown, just with different artifact context. A user doesn't benefit from seeing a Question about 'team communication patterns' even if the artifact context shows their solo-project artifacts. The condition evaluation system mentioned (`question.condition`) is not well-specified: the answer says it supports 'simple predicates like `artifactExists('entities')`' but doesn't address complex conditions ('show this Question if the user selected 'web application' AND the project has more than 10 entities'). The validation decision points also have a gap: the system validates follow-up choices but doesn't validate open-ended answer quality. A user can submit a single-character answer to any Question, and the artifact extraction will produce a low-quality artifact that propagates through the entire pipeline. The Engine should include a quality threshold: if an open-ended answer is below N characters, warn the user and suggest expanding it. The deterministic navigation (always advance, never skip based on answers) is a safety feature (ensures all Questions are asked) but also a rigidity (can't adapt to user needs). The trade-off favors safety for v1 but should be revisited for v2.

---

## Q 4.2.2 — Decision Points and Inputs/Outputs

**Series 4** · What are the expected inputs and outputs at each stage? What data or artifacts flow between steps?

The I/O contracts are described at a high level, but the actual implementation has significant gaps. The `consumes` and `produces` arrays in the framework JSON are string keys, not typed schemas — there's no compile-time or runtime enforcement that the artifact produced by Series 3 actually matches the schema expected by Series 4. The `validateArtifacts()` function checks key presence, not schema conformance, which means a malformed artifact (e.g., `entities` containing a string instead of an array) would silently propagate through the pipeline. The LLM-assisted extraction in `src/llm/artifact-synthesizer.ts` is a black box — the answer says it 'sends the answer text and schema to the LLM,' but there's no specification of what happens when the LLM returns an artifact that doesn't match the schema. Does the synthesizer retry? Reject? Coerce? The null provider's 'simple heuristics' are also problematic — keyword matching and length thresholds produce low-quality artifacts that don't improve downstream processing. The monotonic growth claim is misleading: while keys are added, values can change (when answers are re-answered), so the artifact dictionary is not truly monotonic — it's 'eventually monotonic' if users don't go back and change answers. The cross-stage reference capability is a nice feature but creates a maintenance burden: if the artifact schema changes (e.g., `entities` gains a new required field), all exporters that reference the `entities` artifact must be updated. The claim that 'Series 7 can reference Series 1 vision statements' is accurate but creates a tight coupling between the earliest and latest stages — if the vision changes (re-answered), the deployment artifacts might be inconsistent with the new vision, and the system doesn't detect this.

---

## Q 4.3.1 — Error Handling and Granularity

**Series 4** · What fallback paths, error handling, or recovery procedures should be included for when things go wrong?

The three-tier error handling is conceptually sound but has practical weaknesses. Level 1's 'empty answer → allow' policy is problematic: the answer says 'some questions may not need text if the follow-up is sufficient,' but the system doesn't distinguish between 'intentionally empty' and 'accidentally skipped.' A user who accidentally presses Enter without typing will get an empty answer that's indistinguishable from a deliberate skip. The artifact extraction pipeline will then process this empty answer, potentially producing meaningless artifacts. A better design would require explicit 'skip this question' confirmation for empty answers. Level 2's 'one retry then abort' for storage failures is too aggressive — transient filesystem issues (permission denied due to antivirus, disk temporarily full) are common on Windows and should get more retries with backoff. The 'continue with empty artifact for missing dependency' fallback is dangerous: downstream Series that consume the empty artifact will produce garbage outputs, but the system doesn't warn the user that the specification quality has degraded. Level 3's emergency snapshot is a good idea but the implementation has a race condition: if the crash happens during a `writeFileSync()` call, the emergency snapshot might overwrite partially-written session data. The snapshot should write to a different file path than the main session file. The absence of rollback is acknowledged as a simplification, but the 're-answer by overwriting' approach has a subtle problem: the artifact dictionary is updated, but any previously generated Exports are not. The user might re-answer a question, see the new artifacts, but forget to re-export — their Export files on disk are now stale. The system should auto-invalidate Exports when artifacts change.

---

## Q 4.3.2 — Error Handling and Granularity

**Series 4** · How granular should each procedural step be? Should steps be coarse (several actions) or fine (one action per step)?

The mixed granularity model is described as reflecting 'frequency and criticality,' but the actual granularity split is inconsistent. The answer claims `askQuestion()` is fine-grained, but it actually contains four sub-operations (display, read, validate, save) that each have independent error handling. This makes it a coarse-grained operation, not a fine-grained one. A truly fine-grained design would split these into separate methods: `displayQuestion()`, `readInput()`, `validateAnswer()`, `persistAnswer()` — each independently callable and testable. The current design couples display and input, which means you can't test validation without mocking the TUI. The coarse-grained operations also have inconsistent granularity: `completeRound()` processes all Questions in a Round, but `processSeries()` processes all Rounds in a Series AND extracts artifacts AND validates output. The artifact extraction and validation are separate concerns that should be separate methods, not bundled into `processSeries()`. The error handling granularity claim is also imprecise: 'fine-grained steps get immediate feedback' is true for validation errors, but storage errors within `askQuestion()` get the same 'retry once then abort' treatment as storage errors in `exportSession()`. The granularity doesn't actually affect error handling strategy — the same retry logic is used everywhere. The practical impact of inconsistent granularity is maintenance difficulty: when you change the error handling for storage writes, you have to update it in every method that calls `writeFileSync()`, and the lack of a centralized error handler means these updates are scattered across the codebase. A more maintainable design would use a middleware pattern: wrap all I/O operations in a common error handler that implements the retry/abort policy consistently.

---

## Q 5.1.1 — Hardware and Infrastructure

**Series 5** · What hardware platforms or architectures must be supported? (CPU, GPU, mobile, embedded, etc.)

The platform-agnostic claim deserves scrutiny. While the core engine is genuinely platform-neutral, the codebase contains several assumptions that could break under specific conditions. The StorageProvider's atomic write pattern (write to .tmp, then rename) behaves differently on Windows when the target file is open by another process — Node.js will throw EBUSY on Windows but succeed silently on Linux. The error handling in filesystem.ts should account for this, and if it doesn't, data loss is possible on Windows under concurrent access.

The claim that 'no platform-specific code exists' is slightly misleading. The path module abstracts separators, but the .space.json project directory structure is created under the user's home directory. On Linux, ~/.space/ works predictably. On Windows, the home directory path varies based on environment variables (USERPROFILE vs. HOME), and WSL2 introduces a second home directory. If a user has SPACE installed both natively on Windows and inside WSL2, they could inadvertently create conflicting project directories.

The ES2022 target is appropriate for today but the architecture implicitly assumes Node.js 18+ will remain the baseline indefinitely. Node.js 18 reached end-of-life in April 2025, which means the minimum version constraint needs bumping. This is a minor maintenance burden but should be tracked.

The exclusion of GPU targets is reasonable now, but if SPACE ever adds local LLM inference (via llama.cpp or ONNX Runtime), GPU support would become necessary. The current architecture would make that integration awkward since there's no abstraction for compute backends. This is acceptable for now but represents potential architectural debt if the product direction shifts toward local AI.

---

## Q 5.1.2 — Hardware and Infrastructure

**Series 5** · What are the minimum and recommended hardware specs? (RAM, storage, compute, network)

The hardware specification has a significant gap: it describes what the system needs but not what happens when those needs aren't met. If a user runs SPACE alongside a memory-hungry IDE and Docker on a 4GB laptop, Node.js may hit memory pressure and the OS will start swapping. The system does not monitor its own memory usage or warn when approaching limits. A session with 67 answers loaded into memory plus the web UI plus the LLM API connection state could theoretically exceed the 256MB minimum under memory pressure.

The storage growth model assumes uniform answer lengths, which is unrealistic. The open-ended elicitation probes in SPACE can produce answers ranging from a single word to several paragraphs of detailed specification text. A power user writing verbose answers (2-5KB each) could see per-session sizes of 200-335KB rather than the 10KB estimate. Over 100 sessions, that is 20-33MB per project — still manageable, but the order-of-magnitude discrepancy suggests the growth model needs recalibration with real usage data.

The claim that 'a Raspberry Pi 4 handles the workload comfortably' is unverified and potentially misleading. While the Node.js runtime is available on ARM, the SQLite WASM adapter's performance on low-end ARM processors (especially Pi 4's Cortex-A72) hasn't been benchmarked. The WASM compilation overhead for sql.js initialization could take 200-500ms on a Pi 4, which would be noticeable.

The 'human typing speed is the bottleneck' argument, while largely true, masks a real performance issue: the LLM API call latency. When using auto-fill with GPT-4 or Claude, response times are 2-15 seconds. The system's architecture doesn't currently support speculative execution (pre-loading the next question while the LLM generates an answer), which means the user experiences the full round-trip latency on every AI-assisted question. This is a genuine UX bottleneck that hardware specs don't capture.

---

## Q 5.1.3 — Hardware and Infrastructure

**Series 5** · What bandwidth, latency, or networking requirements exist? Is offline operation needed?

The offline-first claim has a gap between design intent and implementation reality. The web UI loads Tailwind CSS and Inter font from external CDNs. Without network access, the page renders with unstyled content — raw HTML without layout, typography, or responsive behavior. While the core functionality (answer recording via API) works, the user experience degrades to near-unusable. Calling this 'offline-first' is generous; it is more accurately 'offline-functional but offline-ugly.'

The local-only web server binding to localhost is correctly implemented, but the documentation should explicitly warn against port forwarding or tunneling (e.g., ngrok, cloudflared) to expose the server publicly. The REST API has no authentication — any request to localhost:8888 can read and modify all project data. In a shared development environment, this is a real security risk.

The network latency requirement analysis is incomplete. The existing answer mentions LLM API latency (2-15 seconds) but doesn't address what happens during partial network connectivity. If the network is flaky (common on trains, in rural areas, on overloaded WiFi), the LLM request might time out after 30 seconds, leaving the user waiting. The system should implement aggressive timeouts (5-10 seconds) with immediate fallback to manual input, rather than letting the user wait for a timeout.

The claim that 'every feature has an offline fallback' needs verification for all 11 modules in src/intelligence/. The completeness-scorer and contradiction-detector appear to work purely on local session data, but the adaptive-router and recommendations might assume LLM availability. If they don't gracefully handle a missing LLM provider, they could throw unhandled exceptions in offline mode.

A more honest framing: 'SPACE works offline for all core elicitation features. AI-powered analysis and quality scoring require an internet connection.' This sets accurate expectations without overselling the offline capability.

---

## Q 5.1.4 — Hardware and Infrastructure

**Series 5** · What storage infrastructure is needed? (databases, object storage, caching, file systems)

The storage architecture has several under-examined weaknesses. The atomic write pattern (write .tmp, rename) fails silently on some filesystems. On FAT32 (still used on USB drives and some SD cards), rename is not atomic — it's a copy-then-delete operation. If the USB drive is removed during the copy, data loss occurs. The existing answer mentions USB drive transfer as a use case, which makes this a real concern.

The JSON format choice has scaling limitations that aren't discussed. As session files grow (long answers, many follow-ups), parsing a 100KB+ JSON file on every access becomes wasteful. The current architecture parses the entire state.json on every getSession() call. For a session with 326 answers averaging 1KB each, that's 326KB of JSON parsed on every navigation action. A streaming parser or a more granular storage format (e.g., individual answer files) would reduce this overhead.

The SQLite adapter exists but isn't integrated into the main flow. This creates a maintenance risk: the adapter's interface contract could drift from what the filesystem adapter actually implements. Without a shared test suite that runs against both adapters, interface drift will accumulate silently. The 17 tests for SQLite and the filesystem tests likely don't cover the same edge cases.

The exports directory uses a flat structure with format-prefixed filenames. This works for small numbers of exports but doesn't scale. If a user generates 50 exports across different versions, the directory listing becomes unwieldy. A chronological directory structure (exports/2024-01/ or exports/v3/) would be more maintainable.

The biggest gap: there's no backup or recovery mechanism. If ~/.space/ is accidentally deleted (rm -rf ~/.space), all projects and sessions are gone. The system should either support automatic backups to a secondary location or implement an archive/export-all feature that creates a single portable backup file.

---

## Q 5.1.5 — Hardware and Infrastructure

**Series 5** · What cloud, on-premise, or hybrid infrastructure is targeted? Are there compliance or sovereignty requirements?

The 'local development only' claim needs qualification. While the core system is indeed local-only, the LLM integration creates an implicit cloud dependency. When a user configures an OpenAI or Anthropic API key, their elicitation data (answers, project details, technical decisions) is transmitted to a cloud service. The architecture doesn't distinguish between 'local-only' and 'local-but-sends-data-to-LLM-cloud,' which could mislead security-conscious users.

The absence of cloud infrastructure creates real collaboration challenges that the existing answer glosses over. The archive export/import workflow is manual, lossy (no merge strategy for concurrent edits), and doesn't support real-time collaboration. For teams of 2-3 developers, this might be acceptable. For larger teams, it's a dealbreaker. The product positioning should be honest: 'SPACE is a solo developer tool with basic team export features' rather than implying it supports team workflows.

The Docker container mention creates ambiguity about the infrastructure model. If SPACE runs in Docker, it can be deployed to AWS ECS, Kubernetes, or any cloud platform. This means SPACE is simultaneously 'local-only' and 'cloud-deployable.' The architecture doesn't address this contradiction. If cloud deployment is intentionally supported, it needs its own documentation, security model, and scaling guidance. If it's not supported, Docker usage should be documented as a development convenience, not a deployment target.

The compliance analysis is premature. Even though SPACE doesn't currently collect PII, the elicitation data it captures (team size, technology choices, budget constraints, project timelines) could be considered sensitive business information. If a developer uses SPACE on a corporate machine and the LLM API transmits this data, the organization's legal team might have concerns. The architecture should provide a clear data flow diagram showing exactly what leaves the machine and when.

The biggest architectural gap is the lack of a server mode. Many developer tools (Jupyter, Storybook, Postman) offer both local and server deployments. SPACE's architecture could support a server mode with minimal changes (add authentication to server.mjs, bind to 0.0.0.0), but this hasn't been designed. If team features become a priority, retrofitting authentication and multi-user support onto the current architecture will be significantly harder than designing it upfront.

---

## Q 5.2.1 — Software Stack and Dependencies

**Series 5** · What programming languages, runtimes, or frameworks are required or preferred?

The single-language approach has a blind spot: the web UI's vanilla JavaScript doesn't get any of TypeScript's benefits. The index.html file contains inline JavaScript that isn't type-checked, linted, or tested by the TypeScript compiler or vitest. This means the frontend code is effectively untyped — a runtime error in the UI (misspelled property access, wrong function signature, missing null check) won't be caught until a user encounters it.

The vanilla JS frontend choice is defensible for a simple SPA but creates problems at the boundary of complexity. If SPACE adds features like drag-and-drop question reordering, real-time progress visualization, or rich text editing for answers, the vanilla JS approach will require manual DOM manipulation that becomes increasingly difficult to maintain. The 'UI complexity is bounded' assumption may not hold as the product evolves.

The ESM-only choice creates a practical limitation: the CLI can't be used in CommonJS projects without ESM compatibility wrappers. While this affects few users, it's worth noting that many legacy Node.js projects still use CommonJS. The package.json's 'type: module' means require('space-cli') fails in CommonJS contexts — only dynamic import() works.

The TypeScript strict mode is well-configured but doesn't cover all potential issues. The codebase likely uses 'any' types in places where the type system can't express the data flow (particularly around the LLM API responses, which have loosely-typed JSON structures). The LLM types in src/llm/types.ts should be audited for 'any' usage — each 'any' is a potential runtime error that TypeScript chose not to catch.

The build pipeline (tsc to dist/) is simple but lacks optimization. There's no dead code elimination, no tree-shaking, no minification. The roughly 500KB output could likely be reduced to 200KB with a bundler. For an npm package, this matters because users download and install the entire dist/ directory. For a CLI tool used locally, the overhead is negligible, but it's worth noting as a potential optimization.

---

## Q 5.2.2 — Software Stack and Dependencies

**Series 5** · What operating systems and environments must be supported?

The OS support analysis has a significant blind spot: Windows Subsystem for Linux (WSL2). The existing answer recommends WSL2 for Windows users, but WSL2 creates a hybrid environment where Node.js runs in a Linux VM but the filesystem is shared between Windows and WSL. This creates subtle issues:

1. Performance: File I/O between Windows and WSL2 is 10-50x slower than native I/O. If ~/.space/ is on the Windows filesystem (accessed from WSL), session reads/writes will be noticeably slow.
2. Permissions: WSL2 Linux permissions don't map to Windows ACLs. A file created in WSL may not be accessible from Windows Explorer and vice versa.
3. Path confusion: /mnt/c/Users/... (Windows paths in WSL) versus C:\Users\... (WSL paths in Windows) create opportunities for path-related bugs.

The testing strategy (Linux CI + manual macOS/Windows) has a coverage gap. The manual testing is likely sporadic and unstructured — there's no test matrix, no bug tracking for platform-specific issues, and no regression testing across OS versions. A more robust approach would add at least basic CI testing on macOS and Windows, even if it runs less frequently than Linux.

The 'no platform-specific code' claim is aspirational. The codebase likely has implicit platform assumptions: the home directory structure (~/.space/) assumes a Unix-like hierarchy. On Windows, the equivalent would be %USERPROFILE%\.space\. While os.homedir() handles this, the documentation and examples in the CLI output may show Unix paths (~/) that confuse Windows users.

The OS support tiers (Linux primary, macOS secondary, Windows tertiary) create an implicit quality hierarchy. Users on secondary and tertiary platforms will experience more bugs, slower fixes, and less documentation. This should be communicated honestly rather than marketing 'cross-platform support' without qualification. A better framing: 'Fully supported on Linux. Tested on macOS and Windows. Community contributions welcome for platform-specific fixes.'

---

## Q 5.2.3 — Software Stack and Dependencies

**Series 5** · What existing libraries, services, APIs, or third-party dependencies should be used or avoided?

The minimal dependency approach has several under-examined downsides. The manual HTTP routing in web/server.mjs likely lacks features that frameworks provide for free: request body parsing, CORS handling, content-type negotiation, rate limiting, request validation, and error handling middleware. If the REST API grows in complexity, the manual approach will accumulate technical debt as these features are implemented ad-hoc.

The 'native array methods suffice' claim is partially true but misses cases where library implementations are significantly more efficient. For example, lodash's debounce and throttle functions handle edge cases (leading/trailing edge, cancel, flush) that a naive reimplementation would miss. If SPACE needs debounced search or throttled API calls, rolling a custom implementation risks subtle bugs.

The vitest-only testing strategy lacks integration and end-to-end testing. Unit tests verify individual functions, but they don't verify that the CLI commands work end-to-end, that the web UI interacts correctly with the API, or that the LLM integration handles network failures gracefully. The test suite's 112+ tests are likely all unit tests — there's no mention of integration tests, E2E tests, or smoke tests.

The zero-dependency claim for the CLI tool is technically accurate but slightly misleading. The CLI depends on sql.js for the SQLite adapter, which pulls in a 1MB WASM binary. The sql.js package itself may have minimal dependencies, but the WASM blob is a significant payload. For a tool that claims to be lightweight, a 1MB WASM file is noteworthy.

The supply chain security argument is strong but incomplete. While zero npm dependencies reduces one attack vector, the codebase still depends on the Node.js runtime itself. A vulnerability in Node.js (e.g., the recent HTTP/2 rapid reset vulnerability) affects SPACE regardless of its dependency count. The defense-in-depth approach should include: (1) minimal dependencies, (2) regular Node.js version updates, (3) npm audit in CI, and (4) code review for all changes.

The CDN dependencies (Tailwind, Inter font) create a subtle availability issue. If jsDelivr or Google Fonts goes down (both have had outages), the web UI renders unstyled. For a tool that claims to be offline-first, this is an embarrassing gap that should be fixed by vendoring these assets locally.

---

## Q 5.2.4 — Software Stack and Dependencies

**Series 5** · What versioning, compatibility, or upgrade policies govern the software stack?

The existing answer about browser support doesn't address the question about versioning and upgrade policies. This is a significant gap. The actual versioning concerns for SPACE's software stack are:

1. Node.js version drift: The engines field says '>=18' but doesn't specify what features from Node.js 18 are required. If SPACE only uses APIs available since Node.js 16, the minimum version constraint is unnecessarily restrictive. Conversely, if a future feature requires a Node.js 22 API, the minimum version needs bumping with clear communication.

2. TypeScript version risk: TypeScript has historically introduced breaking changes in minor versions (e.g., TypeScript 5.0 changed some type inference behavior). Using ^5.0.0 means a TypeScript update could break SPACE's compilation. The CI should test against the latest TypeScript version and fail fast on type errors.

3. The sql.js WASM version is a hidden compatibility risk. WASM binaries from different sql.js versions may not be interchangeable. If a user has sql.js 1.10 cached and the new SPACE version requires 1.11, the npm install might silently use the cached version. The lock file mitigates this but only for fresh installs.

4. No dependency update automation is configured (no Dependabot, Renovate, or npm audit). Security vulnerabilities in dependencies won't be flagged automatically. For a tool that handles technical specifications (potentially sensitive project data), this is a security gap.

5. The absence of a defined deprecation policy means users have no warning before features are removed. If a storage format change requires session file migration, users need advance notice. The architecture should include a version field in session state.json and a migration path for format upgrades.

6. The frontend CDN dependencies (Tailwind, Inter) use no version pinning. A breaking change in Tailwind's CDN distribution could break the web UI without any code change in SPACE. This is an uncontrolled variable in the deployment pipeline.

---

## Q 5.2.5 — Software Stack and Dependencies

**Series 5** · What build systems, CI/CD platforms, and packaging formats are required?

The build system has several unaddressed concerns. The 'no CI/CD pipeline configured yet' admission is a significant gap for any project published to npm. Without automated testing on every push, bugs can be introduced and published without detection. The prepublishOnly hook catches some issues, but it only runs on the maintainer's machine — if the maintainer's environment differs from the CI environment (different Node.js version, different OS, different dependency cache), the hook provides false confidence.

The test suite has 112+ tests but no coverage reporting configured. Without knowing what percentage of the codebase is tested, it's impossible to assess test quality. A test suite with 112 tests covering 30% of the code provides less confidence than 50 tests covering 80%. Coverage reporting (vitest --coverage) should be added to identify untested code paths.

The frontend build approach (zero build) is elegant but creates a maintenance problem: the index.html file mixes HTML, CSS (via CDN), and JavaScript in a single file. As the UI grows, this file will become unwieldy. At 500+ lines of inline JavaScript, the lack of module boundaries, linting, and type checking will accumulate technical debt. The 'no build step' advantage becomes a liability when the file exceeds what a single developer can hold in their head.

The package distribution has a subtle issue: the prompt-framework/ directory is included in the npm package. This means framework updates require an npm publish cycle. If framework JSON files change frequently, the release cadence should accommodate this. Currently, there's no mechanism to update framework files independently of the CLI code.

The absence of automated linting is a quality gap. Without ESLint or a similar tool, code style inconsistencies accumulate over time. The 'no CI/CD' situation means there's no automated check for: unused imports, inconsistent naming, potential null references, or performance anti-patterns. These issues are caught by linters, not by the TypeScript compiler alone.

The release process lacks several standard practices: (1) no CHANGELOG.md for tracking changes across versions, (2) no git tagging to mark releases, (3) no GitHub Releases with release notes, (4) no npm dist-tags for pre-release versions (alpha, beta, rc). For a developer tool competing in a mature market, these are expected conventions that build trust.

---

## Q 5.3.1 — Performance and Scalability

**Series 5** · What are the throughput, latency, and concurrency requirements? (requests/sec, response time, simultaneous users)

The single-user, single-session assumption is baked deep into `createSpace()` — it returns a closure over a single `Map<string, SessionState>` with no isolation. If `web/server.mjs` receives two concurrent POST requests to the same session endpoint, the second read will see stale data from the first write (classic read-modify-write race). The `FileSystemStorage` uses synchronous file I/O, which is correct for the single-user CLI but creates an architectural mismatch with the async web server — `writeFileSync` blocks the entire Node event loop during disk writes. This won't matter at current scale, but it's a latent correctness issue: if two export requests arrive simultaneously, both block on sequential `writeFileSync` calls in `exportToFiles()`. The `auto_save_interval_ms` timer in `core.ts` fires independently of the web request cycle — there's no guarantee that an auto-save won't race with a concurrent HTTP request modifying the same session. The dependency graph is small (7 nodes, ~10 edges) making traversal negligible, but the `getCurrentQuestion` function in `question-router.ts` does a linear scan of `round.open_ended` to find unanswered questions — technically O(n) per round, not O(1) lookup. This is fine at 67 questions but represents a design choice that assumes small datasets. The real risk isn't performance — it's that nobody has defined the concurrency contract. What happens if the CLI and web server run against the same `projects_dir`? The `FileSystemStorage` provides no file locking.

---

## Q 5.3.2 — Performance and Scalability

**Series 5** · What data volume and growth rate is expected? (storage size, records, throughput)

The 'trivially small' data profile masks a real issue: there's no data lifecycle management at all. `FileSystemStorage.deleteSession()` exists but is never called automatically. Snapshots accumulate without bound — the `saveSnapshot()` method in `snapshot-manager.ts` creates a new snapshot file on every trigger with no deduplication and no pruning. If a user completes 5 series × 3 rounds × 2 (round + series snapshots) = 30 snapshots per session, each at 72KB, that's 2.1MB of snapshot data per session. Over 100 sessions, that's 210MB of snapshot-only data — still manageable, but it's 10x the session state itself. The `pretty-printed JSON.stringify` doubles on-disk size compared to minified JSON — an unnecessary overhead for files that are only read by the application, never by humans. The `ProjectArchive` type in `types/index.ts` bundles sessions and exports together, creating potential for data duplication if archives are exported alongside source sessions. The `SQLiteStorage` adapter (`src/storage/sqlite.ts`) provides better query performance for cross-session analytics but isn't the default, creating a fragmented storage story. The `exportToFiles()` function writes to `output_dir` with no cleanup — repeated exports accumulate files. There's no `.gitignore` awareness: exported files in the project directory would pollute repositories. Growth projections assume ideal usage; in practice, users will create abandoned sessions, duplicate projects, and accumulate exports that they never clean up.

---

## Q 5.3.3 — Performance and Scalability

**Series 5** · What availability, uptime, and disaster recovery targets are required?

The 'best-effort' label is honest but understates real risks. The `FileSystemStorage` uses `writeFileSync` without explicit `fsync` — data is written to the OS page cache but may not be on disk for up to 30 seconds on Linux (controlled by `dirty_expire_centisecs`). A power loss within this window loses the most recent auto-save. The snapshot system mitigates this: snapshots are written after round/series completion, not on every answer, so a crash between auto-saves loses at most one round of progress. However, `writeFileSync` on a file that already exists is NOT atomic — if the process crashes during the write, the file may be partially written (corrupted). The `readFileSync` in `getSession()` would then fail with a JSON parse error. There's no recovery mechanism for corrupted session files — no backup rotation, no checksum validation, no fallback to the previous snapshot. The `ProjectArchive` export is the only portable backup, but it's opt-in and manual. The snapshot files duplicate the full session state (no incremental snapshots), so a corrupted snapshot doesn't help recover from a corrupted session file — you'd need an earlier snapshot. The `SQLiteStorage` adapter fixes the atomicity issue with WAL mode but isn't the default, creating a reliability gap. The `abandoned` status exists but is never automatically set — interrupted sessions appear as `in_progress` indefinitely, with no automated cleanup or user notification.

---

## Q 5.3.4 — Performance and Scalability

**Series 5** · What scalability model is required? (vertical, horizontal, elastic, serverless)

The vertical scaling assumption creates a single point of failure that nobody addresses directly. If the Node.js process crashes, all in-memory sessions are lost (mitigated by snapshots, but snapshots only capture completed rounds, not in-progress answers). The `FileSystemStorage` synchronous I/O model is correct for single-user but creates a hard ceiling: the web server can't handle concurrent requests efficiently because each request blocks on disk reads. The `createServer` callback in `web/server.mjs` is async, but the underlying storage calls are sync — this creates a mismatch where the event loop appears free but is actually blocked during file operations. The `execSync` in `GitIntegration.run()` is particularly concerning: it blocks the entire event loop for up to 10 seconds per git operation. If auto-commit is triggered during a web request, the request will hang. There's no process isolation between the CLI and web server when they share the same `projects_dir` — two processes writing to the same session file will corrupt it. The `SQLiteStorage` adapter adds better concurrency control (WAL mode allows concurrent reads) but still assumes a single process. The real scaling concern isn't throughput — it's the absence of any documentation or enforcement of single-process access constraints. Users might accidentally run both CLI and web server simultaneously against the same data directory.

---

## Q 5.3.5 — Performance and Scalability

**Series 5** · What security and compliance standards must be met? (auth, encryption, audit, regulations)

The security model has several unaddressed risks that become real as the tool matures. (1) Stored XSS via exported HTML: `html-exporter.ts` renders answer text into HTML without sanitization. If a user writes `<script>alert(1)</script>` as an answer and exports to HTML, the resulting file executes arbitrary JavaScript when opened. This is a real vulnerability if exported specs are shared with non-technical stakeholders. (2) API key storage: `SpaceConfig.llm_api_key` is passed in memory and potentially persisted in config files with no encryption. The `createProvider()` factory in `src/llm/factory.ts` creates a new provider instance per session, but the key lives in the config object which persists for the process lifetime. (3) The web server's CORS policy (`Access-Control-Allow-Origin: *`) allows any website to make requests to the local server. If a user has the SPACE web server running and visits a malicious site, that site can read their session data via fetch requests to `localhost:8888`. This is a classic localhost CSRF/exfiltration attack. (4) `GitIntegration` commits specification data with no `.gitignore` awareness — users might accidentally push API keys or sensitive text embedded in their specification answers to public repositories. (5) No audit trail: the `SpaceEvent` system provides hooks but ships with no logging implementation. For a tool used in regulated environments, the absence of access logging and change history (beyond git) is a compliance gap. (6) The `FileSystemStorage` stores data as plaintext — no encryption at rest means any process with filesystem access can read specification data. For a local tool, this is acceptable, but it's worth documenting as a limitation.

---

## Q 5.4.1 — Integration and Timeline

**Series 5** · What external systems, APIs, or services must this system integrate with?

The integration model has structural weaknesses that become apparent at scale. (1) The `GitIntegration` class uses `execSync` which blocks the event loop for up to 10 seconds — if auto-commit triggers during a web request, the request hangs. The class is also not behind an interface, making it impossible to mock in tests or swap for a Git library (like `simple-git` or `isomorphic-git`). (2) LLM provider fallback is silent: if `llm_api_key` is missing, `createProvider()` returns a `TemplateProvider` without any user notification — the user might think auto-fill is working when it's actually returning static templates. (3) The web server (`web/server.mjs`) has no streaming support — LLM responses that take 5 seconds produce no intermediate feedback. The `fetch()` calls in `web/index.html` block until the full response arrives. (4) The `StorageProvider` interface defines 15 methods but no event hooks — adding a new storage backend that needs to trigger side effects (e.g., webhooks, notifications) requires wrapping the entire interface. (5) The export system (`src/export/index.ts`) is synchronous — `exportToFiles()` blocks on `writeFileSync` for each format. For the web server path, large HTML exports would block the event loop. (6) No integration tests for LLM providers — the `isAvailable()` method is the only health check, and it's never called automatically. A misconfigured API key produces a runtime error during session processing, not during initialization. (7) The `package.json` lists `'lint': 'echo no linter configured'` — the tool ships with no code quality gate for integrations.

---

## Q 5.4.2 — Integration and Timeline

**Series 5** · What integration protocols, data formats, or standards must be supported?

The protocol landscape is simple but has gaps that limit extensibility. (1) The REST API in `web/server.mjs` has no formal schema — no OpenAPI, no JSON Schema, no TypeScript types for request/response contracts. Changes to the API require reading the source code; there's no way to generate a client, validate requests, or detect breaking changes. The manual `matchRoute` function with regex-free string splitting is fragile and won't handle edge cases (double slashes, query parameters, encoded characters). (2) No protocol versioning — the `/api/` endpoints have no version prefix (`/api/v1/`). Any API change is a breaking change for existing web UI consumers. (3) LLM providers use different protocol flavors despite superficial similarities: Anthropic uses `system` as a top-level parameter, OpenAI puts it in the `messages` array, Gemini uses `contents` with role-based formatting. The adapter pattern in `src/llm/providers/` handles this but doesn't abstract the protocol differences — each adapter is a bespoke translation layer. (4) No streaming for LLM responses — the `CompletionResult` type in `src/llm/types.ts` returns a complete `text` string, not a stream. Users wait for the full response (1-5 seconds) with no incremental feedback. (5) The web server has no request body size limit — a malicious POST with a multi-megabyte body could exhaust memory. (6) Export formats use `JSON.stringify` for YAML compatibility checks but don't actually validate YAML output — the `yaml-exporter.ts` may produce invalid YAML for strings with special characters. (7) No content negotiation: the web server always returns JSON regardless of the `Accept` header.

---

## Q 5.4.3 — Integration and Timeline

**Series 5** · What is the expected timeline, milestones, and delivery cadence?

The timeline assessment reveals several process gaps. (1) No test coverage: the `tests/` directory contains `integration/` and `unit/` subdirectories but the actual test content wasn't inspected — the `package.json` script `'test': 'vitest run'` suggests tests exist but their coverage is unknown. For a tool that generates technical specifications, the absence of verified test coverage is concerning. (2) No CI/CD: no `.github/workflows/`, no `.gitlab-ci.yml`, no build automation visible in the codebase. The `prepublishOnly` script (`'npm run build && npm test'`) runs locally but there's no remote verification. (3) Version 2.1.0 suggests two major versions have shipped, but there's no CHANGELOG, no git tags, no release notes. This makes it impossible to assess the maturity of specific features or understand what changed between versions. (4) The `web/server.mjs` is a single-file server with no framework — this is fine for prototyping but doesn't scale to feature additions. Adding authentication, streaming, or WebSocket support would require a complete rewrite. (5) The `auto/rsi/` automation layer is generating this specification, which means we're in a bootstrap scenario: SPACE is being used to spec itself. This recursive process can produce spec drift if the tool changes while generating its own specification. (6) The `lint` script is `echo 'no linter configured'` — no code quality gate exists. (7) No migration strategy for `SessionState` schema changes across versions — the `framework_version` field exists but there's no migration logic for session files written by older versions.

---

## Q 5.4.4 — Integration and Timeline

**Series 5** · What testing, staging, and rollout strategy is required?

The testing and deployment gaps are significant for a tool at v2.1.0. (1) The `tests/` directory structure exists but actual test content is unknown — if tests are skeletal or incomplete, the `vitest run` command may pass trivially or skip entirely. No test coverage reporting is configured. (2) No CI/CD pipeline means there's no automated verification that code changes don't break existing functionality. The `prepublishOnly` script is a local gate only — it can be bypassed with `npm publish --ignore-scripts`. (3) The `tsc` build produces no bundled output — the `dist/` directory contains individual `.js` files with relative imports, requiring consumers to have all files present. This is fragile for npm publishing if the `files` field in `package.json` misses a file. (4) The `web/server.mjs` imports from `../dist/` — it's tightly coupled to the build output structure. Any change to the `tsconfig.json` paths would break the web server. (5) No staging environment for testing the web server against real data — developers test locally against their own projects. (6) No rollback mechanism — if a published version has a bug, the only recourse is publishing a new version. No npm `deprecate` automation. (7) The `DEFAULT_CONFIG` in `src/config/defaults.ts` uses `homedir()` for paths — this means the tool behaves differently on different operating systems, but there's no platform-specific testing visible. (8) No load testing or performance benchmarking — the performance characteristics discussed in questions 5.3.1-5.3.4 are assumed, not verified.

---

## Q 5.4.5 — Integration and Timeline

**Series 5** · What documentation, training, or knowledge transfer outputs are expected alongside the system?

The documentation gaps are a serious risk for adoption and maintenance. (1) No architecture decision records (ADRs): the codebase makes significant design choices (immutable sessions, 7-series dependency graph, filesystem-first storage, raw HTTP web server) that are undocumented. Without ADRs, future contributors will repeat the analysis that led to these choices. (2) The `README.md` exists but is likely minimal — it needs to be the single source of truth for installation, usage, and troubleshooting. (3) No inline documentation: exported functions in `question-router.ts`, `session-manager.ts`, `snapshot-manager.ts` lack JSDoc comments. The `exportSession()` function in `src/export/index.ts` is a critical public API with no documentation of its `ExportOptions` parameter. (4) No versioning documentation: the `framework_version` field in `SessionMeta` suggests versioned framework definitions, but there's no migration guide for moving sessions between versions. (5) The `auto/rsi/` automation layer (which is generating this specification) is itself undocumented — its scripts (`generate-rsi-docs.mjs`, `gen-answers.mjs`, `fill-and-export.mjs`) have no README explaining their purpose or invocation. (6) The `src/template/` module (`patterns.ts`, `resolver.ts`) appears to handle template resolution but its purpose, input/output contract, and usage context are unclear from the code alone. (7) No troubleshooting guide for common issues: corrupted session files, LLM API failures, Git conflicts, filesystem permission errors. (8) The recursive nature of SPACE spec'ing itself (this specification is being generated by SPACE) means documentation quality directly affects specification quality — poor documentation produces poor specifications.

---

## Q 6.1.1 — Process and Cadence

**Series 6** · What development process or methodology best fits this project? How should work be planned and tracked?

The 'no formal process' approach is fragile in several ways. First, without CI/CD, the test suite only runs when the developer manually executes 'npm test' — there's nothing preventing a broken commit from reaching npm. The build artifact (dist/) isn't verified on every push. Second, the lack of linting (package.json has 'lint': 'echo no linter configured') means code style drift is undetectable. Third, without branch protection or PR requirements, a single force-push could destroy history. The phase-based development described (Core engine → Framework data → Web UI → Storage+LLM → Docs) isn't actually documented anywhere — it's reconstructed from git log. Future contributors can't understand the rationale behind architectural choices without reading commit messages or asking the original developer. The GitIntegration class in src/integration/git.ts auto-commits with '[space]' prefix, which is useful but doesn't establish conventional commits, making automated changelog generation impossible. The claim that 'no phase was blocked by incomplete work from earlier phases' is aspirational — in practice, the framework-loader.ts dependency means framework data MUST exist before the engine can run. A formal process would have identified this critical path earlier.

---

## Q 6.1.2 — Process and Cadence

**Series 6** · What is the expected team size, composition, and structure?

The 'solo developer works because the codebase is small' argument conflates correlation with causation. The real question is whether solo development produces better or worse software than a small team. In SPACE's case, the lack of code review means type-safety issues like ArtifactValue.value being typed as 'any' in src/types/index.ts went unnoticed. The FileSystemStorage in src/storage/filesystem.ts uses synchronous fs operations (readFileSync, writeFileSync) which block the Node.js event loop — a second developer would likely have flagged this. The SQLiteStorage in src/storage/sqlite.ts writes the entire database to disk on every mutation (this.persist() after every operation) — this is O(n) where n is database size and would cause performance degradation as data grows. A team member with database experience would catch this immediately. The GitIntegration class in src/integration/git.ts uses execSync with a 10-second timeout — if git operations take longer (large repos), this silently fails and returns empty strings. The 'all roles combined' model means the developer is simultaneously architect, implementer, and tester — but testing your own code has well-documented blind spots. At minimum, a peer review process (even asynchronous, via GitHub PRs) would catch architectural issues before they become technical debt.

---

## Q 6.2.1 — Quality and Review Practices

**Series 6** · What code review, testing, and quality assurance practices should be followed?

Several quality gaps exist that undermine the stated practices. First, 'no linting violations' is a false claim — ESLint isn't configured, so there are literally no violations because rules aren't enforced. The package.json confirms: 'lint': 'echo no linter configured'. Second, the test suite tests public APIs but has blind spots: the template system (src/template/), the artifact mapping logic (src/data/artifact-mapping.ts), and the dependency resolver (src/engine/dependency-resolver.ts) may have insufficient coverage — there's no coverage report generated. Third, there are no negative tests for edge cases: what happens when the framework JSON is malformed? What if storage disk is full? What if two sessions write to the same project simultaneously? The SQLiteStorage's this.persist() call after every mutation means a crash mid-write could corrupt the database — there's no WAL mode or transaction support. Fourth, 'No console.log in production code' is unverifiable without ESLint's no-console rule. Fifth, the test suite doesn't test error paths: what does createProvider() return when given an invalid llm_provider value? The switch in src/llm/factory.ts falls through to NullProvider, which silently succeeds — a test should verify this behavior is intentional. The test-to-code ratio suggests adequate coverage, but without coverage metrics, it's impossible to verify.

---

## Q 6.2.2 — Quality and Review Practices

**Series 6** · How should the team handle technical debt, refactoring, and code quality?

The 'opportunistic — clean as you go' approach has failed to address several significant issues. The codebase has grown organically without a single refactoring pass, and the debt is accumulating: (1) The Engine class in src/engine/core.ts is a monolith that handles session lifecycle, question routing, progress tracking, event emission, and serialization — this violates Single Responsibility Principle and makes the module hard to test in isolation. (2) The StorageProvider implementations (FileSystemStorage, SQLiteStorage) duplicate the ensureDir() utility function — this is DRY violation that suggests the code was copied between files. (3) The GitIntegration class in src/integration/git.ts uses execSync everywhere, making it impossible to use in an async context — if the web server ever needs git operations, this class must be rewritten. (4) The export system has no validation — exportSession() in src/export/index.ts trusts that the SessionState is complete and valid, which means exporting an incomplete session produces a corrupted spec without warning. (5) There's no migration path for framework version upgrades — if the framework JSON schema changes, existing sessions become unreadable. The 'debt prevention' strategy (TypeScript strict mode, comprehensive tests) is necessary but insufficient. Without static analysis (ESLint, complexity checks, dependency analysis), structural debt accumulates invisibly. The honest assessment: the codebase is in decent shape for its age, but the lack of any formal debt tracking means issues are only discovered when they cause pain.

---

## Q 6.3.1 — Communication and Collaboration

**Series 6** · How should the team communicate, share knowledge, and manage decisions?

The knowledge management approach has critical gaps that will bite as the project grows. First, there are zero architecture decision records — why was SQLiteStorage added alongside FileSystemStorage? When was it introduced and what triggered the need? Without ADRs, this context is lost. Second, the codebase lacks a CONTRIBUTING.md, so external contributors don't know coding standards, test requirements, or the PR process. Third, there's no changelog — npm version bumps happen but release notes don't exist. The README.md is minimal and doesn't document the architecture, the 326-probe framework structure, or the StorageProvider/LLMProvider extension points. Fourth, knowledge about the framework's probe taxonomy lives only in the JSON files — there's no human-readable explanation of why probes are ordered as they are or what each series accomplishes. The 'documentation as communication' claim is aspirational — the type definitions document the WHAT but not the WHY. The test files document behavior but not design intent. The most significant knowledge gap: there's no documented migration path for framework version upgrades. If the framework schema changes from v2.0.0 to v3.0.0, there's no tooling or documentation to help users migrate their sessions. This is a critical oversight for long-term stewardship.

---

## Q 6.3.2 — Communication and Collaboration

**Series 6** · What is the decision-making and escalation process? How are architectural choices made?

The BDFL model has produced several decisions that lack justification and may not survive scrutiny. (1) The 'no React for the web UI' decision — stated as 'single HTML file is simpler' — ignores the fact that a 326-probe elicitation flow needs complex state management that vanilla JS handles poorly. The web UI is likely a maintenance burden that grows with each new feature. (2) The 'no database' decision — 'JSON files are simpler' — is contradicted by the fact that SQLiteStorage exists in src/storage/sqlite.ts, meaning a database WAS added. The decision was reversed without documented rationale. (3) The 'no ESLint' decision — justified as 'type checking serves this purpose' — is wrong: TypeScript catches type errors, not style violations, unused imports, or inconsistent naming. (4) The decision to use execSync in GitIntegration (src/integration/git.ts) blocks the event loop and fails silently on timeout — this was chosen for simplicity but creates reliability issues. (5) The event system in core.ts uses string-based event names with no type safety — 'session:created', 'answer:submitted' are magic strings that can be misspelled without detection. The broader critique: most decisions are made for developer convenience rather than user benefit. The architecture should optimize for the user's experience (reliable CLI, fast exports, accurate specs) rather than the developer's comfort (synchronous APIs, minimal abstractions, no linting).

---

## Q 7.1.1 — Deployment and Delivery

**Series 7** · How should the system be deployed, released, and updated in production?

The deployment strategy has several fragilities. (1) The prepublishOnly script runs build+test, but doesn't verify the binary works — 'npm pack' followed by 'npm install -g ./space-cli-*.tgz' should be part of the release checklist. (2) The VERSION constant in src/cli/index.ts is hardcoded as '2.1.0' — if the developer forgets to update it, the CLI reports the wrong version. This should be injected at build time from package.json. (3) There's no CI/CD pipeline — publishing requires manual npm publish, which means: (a) a developer must have npm credentials, (b) there's no automated testing on the publish artifact, (c) there's no rollback mechanism. (4) The web UI deployment (git clone + node web/server.mjs) has no process management — if the server crashes, it stays down until manually restarted. PM2 or systemd should be recommended. (5) The dual distribution model (CLI via npm, web via git) means users might run different versions of the CLI and web UI, leading to schema incompatibilities. (6) npm doesn't support atomic deployments — a failed publish can leave the registry in an inconsistent state. (7) There's no .npmignore file — the 'files' field in package.json limits what's published, but typos could leak sensitive files. The deployment strategy needs a formal checklist and automation before the project gains external users.

---

## Q 7.1.2 — Deployment and Delivery

**Series 7** · What environment and release management strategy should be used?

The environment management is inadequate for anything beyond personal use. (1) No environment separation: dev and prod share ~/.space/projects/, meaning a test run could overwrite a user's real session data. The FileSystemStorage in src/storage/filesystem.ts creates directories in the constructor — running tests that create FileSystemStorage instances writes to the user's actual projects directory. (2) No database migrations: the SQLiteStorage schema (defined in SCHEMA_SQL in src/storage/sqlite.ts) has no version tracking — if the schema changes between versions, existing databases become unreadable. (3) No configuration validation: SpaceConfig accepts any string for llm_provider, but only specific values are valid — an invalid value silently falls through to NullProvider in src/llm/factory.ts. This should fail loudly. (4) The web server has no CORS configuration, no rate limiting, no authentication — it's unsuitable for any environment beyond localhost. (5) No .env file support — the Twelve-Factor App methodology recommends .env files for local development, but SPACE only reads from process.env. (6) The default directory ~/.space/projects/ doesn't differentiate between environments, making backup/restore error-prone. (7) Framework version compatibility is checked at load time (validateFramework in src/data/framework-loader.ts) but not at session resume — a session created with framework v1.0.0 could be resumed with framework v2.0.0 without warning. These gaps are acceptable for a v2.1.0 solo project but must be addressed before public launch.

---

## Q 7.2.1 — Runtime Behavior and Observability

**Series 7** · What logging, monitoring, alerting, and observability infrastructure is needed?

The observability story is the weakest aspect of SPACE's architecture. (1) Zero structured logging means debugging production issues is impossible — there's no log file, no log aggregation, no way to reconstruct what happened. (2) The Engine's event system is not typed — event names are strings, so a typo in 'session:created' vs 'session:creatd' would silently fail. (3) The GitIntegration class (src/integration/git.ts) swallows ALL errors — the run() method catches exceptions and returns empty string, making git failures invisible. This is particularly dangerous for auto-commit: if git commit fails, the user loses version history without knowing. (4) The LLM providers in src/llm/providers/*.ts have inconsistent error handling — OpenAIProvider and AnthropicProvider throw on failure, but the caller in core.ts may not catch these, causing unhandled rejections. (5) The web server has no request ID tracking, no response time logging, no error rate monitoring. (6) FileSystemStorage uses sync I/O, so a slow disk operation blocks the entire process with no visibility into what's slow. (7) There's no audit trail for data modifications — if a session is corrupted, there's no way to determine what changed or when. The event system is a good foundation, but it's underutilized. Without structured logging, SPACE is flying blind in any environment beyond local development.

---

## Q 7.2.2 — Runtime Behavior and Observability

**Series 7** · What configuration and feature management approach should be used at runtime?

The configuration approach has several blind spots. (1) No configuration validation: SpaceConfig accepts any value for llm_provider, but only 'openai' | 'anthropic' | 'gemini' | 'mistral' | 'ollama' | 'local' | 'none' are valid. An invalid value silently falls through to NullProvider in src/llm/factory.ts — the user thinks LLM is configured but it isn't. This should throw an error at startup. (2) No environment variable mapping: despite the design implication, SpaceConfig doesn't actually read from process.env — the createSpace() function only accepts a Partial<SpaceConfig> parameter. Users must pass config programmatically or via CLI arguments. Environment variables are NOT wired up. (3) No configuration discovery: there's no 'space config --list' command, no documentation of available variables, no config validation command. (4) The enable_adaptive_questions flag is read by the intelligence layer but there's no feedback mechanism — users can't tell if adaptive routing is active during a session. (5) The LLM configuration has no connection testing — if SPACE_LLM_API_KEY is invalid, the error only surfaces during a session, not at startup. (6) No configuration export — users can't share their configuration with teammates or backup their settings. (7) The default export format is 'markdown' but there's no way to change this globally without an environment variable that isn't documented. The configuration system works for the developer who built it but is opaque to everyone else.

---

## Q 7.3.1 — Maintenance and Evolution

**Series 7** · What maintenance schedule, upgrade policy, and lifecycle management is expected?

The maintenance plan has significant gaps that will cause problems as the project matures. (1) No automated dependency updates — Dependabot or Renovate should be configured to create PRs for outdated dependencies. Without this, the project will accumulate outdated packages with known vulnerabilities. (2) No security scanning — 'npm audit' is manual, not automated. A GitHub Action should run on every push and block merges on high-severity vulnerabilities. (3) No Node.js version testing matrix — the engines field says >=18 but there's no CI to verify actual compatibility with Node 18, 20, and 22. (4) No framework migration strategy — the framework JSON schema could change between versions, but there's no migration tool or compatibility layer. Existing sessions from v2.0.0 would break with a v3.0.0 schema change. (5) The SQLiteStorage has no backup strategy — a corrupted database file means all session data is lost. (6) No end-of-life policy — what happens if the developer stops maintaining the project? The MIT license allows forks, but without documentation on the architecture and extension points, forking is difficult. (7) The minimal dependency strategy is a double-edged sword — sql.js (SQLite compiled to WASM) is a complex dependency that could have its own breaking changes, and the project has no plan for handling this. Maintenance should include a 'bus factor' assessment: if the developer is unavailable for 6 months, what breaks? The answer: everything, because there's no CI, no documentation, no contributor guide.

---

## Q 7.3.2 — Maintenance and Evolution

**Series 7** · What is the long-term stewardship plan? Who owns the system after initial delivery?

The stewardship plan has a critical vulnerability: bus factor of one. If the original developer becomes unavailable, the project has: (1) No documented architecture beyond code comments, (2) No contributor guide, (3) No governance model, (4) No release automation, (5) No issue triage process. The 'any competent TypeScript developer could take over' claim is dangerously optimistic — the codebase has undocumented design decisions (why SQLite over Postgres? why sync I/O? why no ESLint?), implicit assumptions (the framework JSON format, the artifact dictionary schema), and tribal knowledge (which tests are important, which modules are fragile) that would take weeks to transfer. The succession plan should include: (1) Architecture documentation (ADRs for major decisions), (2) A 'runbook' for common maintenance tasks, (3) A designated successor with repository write access and deployment credentials, (4) Automated CI/CD so maintenance can continue without the original developer's local environment. The open-source aspiration (MIT license, community contributions welcome) conflicts with the reality (no CONTRIBUTING.md, no issue templates, no PR review process). The project is technically open-source but practically closed — only the original developer can effectively contribute. Long-term stewardship requires either: (a) investing in community infrastructure now, or (b) honestly positioning the project as 'maintained by [name]' with no community expectations. The worst outcome is promising community governance without delivering it.

---

