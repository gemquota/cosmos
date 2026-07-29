import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const BASE = join(__dirname, '..', 'auto', 'rsi');
const ANSWERS_DIR = join(BASE, 'answers');
mkdirSync(ANSWERS_DIR, { recursive: true });

const SERIES_FILES = [
  '01-conceptual-depth.json',
  '02-ontological-characteristics.json',
  '03-semantic-relationships.json',
  '04-procedural-breadth.json',
  '05-technical-specifications.json',
  '06-development-methodologies.json',
  '07-operational-functional.json',
];

const SERIES_NAMES = [
const SERIES_DESCRIPTIONS = [
  "Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.",
  "Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.",
  "Maps associations, dependencies, hierarchies, and causal chains between entities.",
  "Defines the workflows, procedures, decision points, and error handling for the system.",
  "Specifies hardware, software, performance, security, integrations, and deployment requirements.",
  "Establishes development methodology, team structure, quality practices, and communication patterns.",
  "Covers deployment, operations, monitoring, maintenance, and long-term stewardship.",
];
  'Conceptual Depth', 'Ontological Characteristics', 'Semantic Relationships',
const SERIES_DESCRIPTIONS = [
  "Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.",
  "Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.",
  "Maps associations, dependencies, hierarchies, and causal chains between entities.",
  "Defines the workflows, procedures, decision points, and error handling for the system.",
  "Specifies hardware, software, performance, security, integrations, and deployment requirements.",
  "Establishes development methodology, team structure, quality practices, and communication patterns.",
  "Covers deployment, operations, monitoring, maintenance, and long-term stewardship.",
];
  'Procedural Breadth', 'Technical Specifications', 'Development Methodologies',
const SERIES_DESCRIPTIONS = [
  "Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.",
  "Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.",
  "Maps associations, dependencies, hierarchies, and causal chains between entities.",
  "Defines the workflows, procedures, decision points, and error handling for the system.",
  "Specifies hardware, software, performance, security, integrations, and deployment requirements.",
  "Establishes development methodology, team structure, quality practices, and communication patterns.",
  "Covers deployment, operations, monitoring, maintenance, and long-term stewardship.",
];
  'Operational / Functional',
const SERIES_DESCRIPTIONS = [
  "Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.",
  "Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.",
  "Maps associations, dependencies, hierarchies, and causal chains between entities.",
  "Defines the workflows, procedures, decision points, and error handling for the system.",
  "Specifies hardware, software, performance, security, integrations, and deployment requirements.",
  "Establishes development methodology, team structure, quality practices, and communication patterns.",
  "Covers deployment, operations, monitoring, maintenance, and long-term stewardship.",
];
];
const SERIES_DESCRIPTIONS = [
  "Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.",
  "Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.",
  "Maps associations, dependencies, hierarchies, and causal chains between entities.",
  "Defines the workflows, procedures, decision points, and error handling for the system.",
  "Specifies hardware, software, performance, security, integrations, and deployment requirements.",
  "Establishes development methodology, team structure, quality practices, and communication patterns.",
  "Covers deployment, operations, monitoring, maintenance, and long-term stewardship.",
];

// Comprehensive answers keyed by question ID
const A = {};

// ═══ SERIES 1: CONCEPTUAL DEPTH ═══
A['1.1.1'] = `SPACE (Superb Prompt Automatic Creation Engine) is a programmable specification engine that transforms structured elicitation probes into development specifications. It operates at the intersection of prompt engineering, software specification, and developer tooling.

The primary domain is software specification engineering augmented by LLM capabilities. Core concerns include: (1) Structured elicitation — systematically extracting domain knowledge from humans through a 326-probe questionnaire organized into 7 progressive series with 25 rounds. (2) Dependency-aware routing — ensuring questions are asked in an order that respects logical prerequisites, where later questions can reference artifacts from earlier ones. (3) Artifact extraction — automatically identifying and cataloging key design decisions, entity definitions, and architectural choices from free-text answers. (4) Multi-format export — generating specification documents in JSON, Markdown, YAML, HTML, and LLM-consumable prompt formats.

Sub-disciplines encompassed: structured prompt engineering, dependency graph traversal, artifact mapping, specification generation, and progressive deepening methodologies. The system draws from elicitation techniques used in requirements engineering (specifically the JAD — Joint Application Development — facilitation model), ontological modeling from knowledge representation (OWL-style entity classification), and the progressive disclosure pattern from UX design. The domain also intersects with formal methods (the framework produces structured, machine-readable specifications) and knowledge management (the artifact dictionary becomes a living knowledge base for the project).`;

A['1.1.2'] = `The primary audience is software developers and technical leads building LLM-powered applications or complex systems who need structured specifications. These are practitioners who understand TypeScript/Node.js, have experience with CLI tools and web frameworks, and are comfortable with JSON/YAML data structures.

Secondary audiences: (1) Product managers who need to formalize requirements for AI-assisted development — they provide domain context but expect the framework to structure it. (2) Architects designing systems that integrate multiple LLM providers — they need the framework to capture cross-cutting concerns like provider fallback, cost budgets, and latency targets. (3) Open-source maintainers who want to document their projects systematically — the framework produces a comprehensive specification that doubles as project documentation. (4) Technical writers who need structured input for generating documentation — the exported specifications feed directly into documentation pipelines.

Baseline familiarity: respondents understand REST APIs, npm ecosystems, and basic AI/ML concepts. They have likely used at least one LLM API (OpenAI, Anthropic, Google Gemini, Mistral, or Ollama) and understand the difference between system prompts, user prompts, and completion endpoints. They may not be familiar with ontological modeling or dependency graph theory, so the framework explains these concepts progressively through Series 1. The audience profile directly informs the verbosity level (moderate), abstraction level (mixed concrete/formal), and terminology choices (industry standard with definitions for novel terms) across the entire framework.`;

A['1.2.1'] = `Assumed knowledge that the output can take for granted: CLI tool usage (npm install, git clone, running scripts), Node.js/TypeScript basics (import/export, async/await, type annotations, interfaces), JSON/YAML parsing and structure, REST API concepts (endpoints, request/response, status codes), prompt engineering fundamentals (system prompts, few-shot prompting, temperature, top_p), and basic software architecture patterns (MVC, event-driven, plugin systems, dependency injection).

Must be explained from scratch: (1) The specific 7-series progressive elicitation methodology — how questions build on each other across series in a dependency graph. (2) The dependency chain between series — why Series 2 (Ontological Characteristics) cannot start until Series 1 (Conceptual Depth) provides domain and audience context, and why Series 7 (Operational/Functional) depends on both Series 5 and 6. (3) How artifacts accumulate — each answer contributes extracted data (entity lists, relationship graphs, procedure steps, tech stack decisions) that downstream series consume via the artifact dictionary. (4) The 326-probe structure — 67 open-ended questions, each with 3-5 multi-choice follow-ups that classify and clarify the answer, totaling 201+ follow-up choices. (5) How the framework produces a coherent specification from apparently disconnected questions through the artifact dependency graph. (6) The StorageProvider abstraction — how sessions persist via filesystem or SQLite. (7) The LLM provider factory — how multiple AI backends (OpenAI, Anthropic, Gemini, Mistral, Ollama) are abstracted behind a unified interface.`;

A['1.2.2'] = `Mixed approach — present the SPACE architecture with clear structural diagrams showing the series dependency graph and question flow, then ground each concept with concrete examples from the actual codebase.

For the structural layer: use dependency graphs (Series 1 feeds Series 2, which feeds Series 3; Series 2+3 feed Series 4; Series 1+4 feed Series 5; Series 4+5 feed Series 6; Series 5+6 feed Series 7) to show the progressive narrowing. Show how each series consumes artifacts from previous series via the artifact dictionary. Show the series/round/question hierarchy with the z_multi_choice_per_open parameter controlling follow-up depth.

For the concrete layer: show actual TypeScript code snippets from the engine (question-router.ts showing dependency resolution, session-manager.ts showing state transitions, artifact-mapping.ts showing extraction patterns), real JSON examples of session state (with question answers, artifact dictionaries, and completion flags), and actual output from the export pipeline (JSON spec, Markdown doc, YAML config, HTML report, LLM prompt). The abstraction level balances formal definitions (the StorageProvider interface, the LLMProvider interface, the SpaceConfig type) with illustrative examples (actual terminal output from "space run", actual JSON artifact entries).`;

A['1.3.1'] = `Standard software engineering terminology used consistently throughout: session (a user interaction instance with a unique UUID), artifact (extracted structured data from answers, stored in the artifact dictionary), framework (the 326-probe question set defined in JSON), series (a themed group of rounds, 7 total), round (a batch of 2-5 related open-ended questions), probe (a single elicitation question — open-ended or multi-choice follow-up), dependency (a series that must complete before another can start).

Industry terms used precisely: dependency injection (for the StorageProvider pattern allowing filesystem or SQLite backends), factory pattern (for LLM provider creation via createLLMProvider()), event emitter (for lifecycle hooks in the session manager), command pattern (for CLI commands in src/cli/commands/), strategy pattern (for export format selection), adapter pattern (for the StorageProvider implementations).

Terms deliberately avoided: "AI" or "intelligent" for the engine (it routes and extracts deterministically, not "understands"), "user" for the respondent (use "respondent" or "answerer" to distinguish from system operators), "generate" for the export (use "compile" or "render" to distinguish from LLM generation), "smart" for any feature (avoid marketing language in technical specifications), "revolutionary" or "groundbreaking" for the methodology (it's a practical engineering tool, not a research paper).

Notation conventions: question IDs use dot notation (e.g., "2.3.1" = Series 2, Round 3, Question 1). Artifact keys use snake_case (e.g., "entity_list", "relationship_graph"). File paths use forward slashes. Code references use backtick formatting.`;

A['1.3.2'] = `Progressive scaffolding — start with the simple concept of asking structured questions to produce specifications, then layer in complexity one dimension at a time:

Layer 1 (Series 1): Question asking — the basic loop of presenting questions and recording answers. Establish domain, audience, vocabulary, and abstraction level. This is the simplest concept and requires no prerequisite knowledge.

Layer 2 (Series 2): Entity discovery — identify the primary entities, attributes, categories, and boundaries of the domain. Introduce the concept of ontological modeling (but call it "entity mapping" for accessibility). Show how free-text answers are parsed for entity mentions.

Layer 3 (Series 3): Relationship mapping — connect entities with associations, hierarchies, causal chains, and dependencies. Introduce graph theory concepts (nodes, edges, directed graphs) through concrete examples.

Layer 4 (Series 4): Procedural scoping — define workflows, decision points, error handling, and step granularity. Connect procedures to entities (procedures operate on entities) and relationships (procedures traverse relationships).

Layer 5 (Series 5): Technical specifications — hardware, software, performance, security, integrations, and timeline. This is the most concrete layer and grounds all previous abstract concepts in specific technology choices.

Layer 6 (Series 6): Development methodology — team process, quality practices, communication patterns. Connects technical specifications to human organization.

Layer 7 (Series 7): Operational preferences — deployment, monitoring, maintenance, stewardship. The final layer that ensures the specification is actionable.

Each layer builds on all previous layers. The complexity distribution is deliberately front-loaded: Series 1-2 introduce the most new concepts, Series 3-4 apply them, Series 5-7 ground them in specifics. This matches the progressive disclosure pattern where users learn the framework by doing, not by reading documentation.`;

// ═══ SERIES 2: ONTOLOGICAL CHARACTERISTICS ═══
A['2.1.1'] = `Core entities identified through systematic domain analysis of the SPACE system:

1. Framework — The 326-probe question set. Contains 7 series, each with multiple rounds, each round with 2-5 open-ended questions, each question with 3-5 multi-choice follow-ups. Defined in JSON files under prompt-framework/json/. Immutable after creation; the framework is the reference specification.

2. Series — A themed group of rounds within the framework. 7 series total: Conceptual Depth, Ontological Characteristics, Semantic Relationships, Procedural Breadth, Technical Specifications, Development Methodologies, Operational/Functional. Each series has dependencies (other series that must complete first), consumes (artifacts it needs), and provides (artifacts it produces).

3. Round — A batch of related open-ended questions within a series. Each round has a focus area (e.g., "Entity Discovery", "System Boundaries") and contains 2-5 questions that share thematic coherence.

4. Question — A single elicitation probe. Two types: open-ended (free text response) and multi-choice follow-up (classify the open-ended answer). Each question has a unique ID (e.g., "2.3.1"), text (the question prompt), and follow_up_choices (2-5 options).

5. Answer — A respondent's response to a question. Contains the open-ended text (the free response) and the chosen follow-up option (the classification). Answers are stored in session state.

6. Artifact — Structured data extracted from answers. Created by the artifact mapping system which parses free-text answers for entity mentions, architectural decisions, technology choices, and constraints. Artifacts accumulate across series and are consumed by downstream series.

7. Session — A complete interaction instance. Has a UUID, project association, current question pointer, answer history, artifact dictionary, and completion status. Sessions can be resumed from storage.

8. Project — A named workspace. Contains sessions, exports, and configuration. Stored in ~/.space/projects/<name>/.

9. Export — A compiled specification document. Multiple formats: JSON, Markdown, YAML, HTML, LLM prompt. Generated on-demand from session state and artifact dictionary.

10. Engine — The orchestration layer. Manages question routing, answer validation, artifact extraction, and session lifecycle. The core runtime that ties everything together.`;

A['2.1.2'] = `Entity attributes with types and constraints:

Framework: id (number, 1-7 range), name (string, 3-50 chars), description (string, 50-200 chars), x_rounds (number), y_open_ended_per_round (number), z_multi_choice_per_open (number), depends_on (number[]), provides (string[]), consumes (string[]).

Series: id (number, 1-7), name (string), description (string), rounds (Round[]), deps (number[]). Attributes differ from Framework because Series is the runtime representation while Framework is the definition format.

Round: round (number, 1-based within series), focus (string, 2-20 words), questions (Question[]).

Question: id (string, dot notation e.g., "2.3.1"), text (string, 10-200 chars), follow_up_choices (Choice[]), type ("open_ended" | "multi_choice_follow_up").

Answer: question_id (string, FK to Question), open_ended (string, 10-5000 chars), choice_id (string, FK to Choice), timestamp (ISO 8601).

Artifact: key (string, snake_case), value (any — string, number, array, object), source_question_id (string, FK), series_origin (number), confidence (number, 0-1).

Session: id (UUID string), project_id (string, FK), current_question_id (string | null), answers (Answer[]), artifacts (Record<string, any>), status ("active" | "completed" | "paused"), created_at (ISO 8601), updated_at (ISO 8601).

Project: name (string, kebab-case), description (string), created_at (ISO 8601), sessions (Session[]), exports (Export[]).

Export: session_id (string, FK), format ("json" | "markdown" | "yaml" | "html" | "llm_prompt"), content (string), filename (string), generated_at (ISO 8601).

Engine: config (SpaceConfig), storage (StorageProvider), llm (LLMProvider | null), state (SessionState).`;

A['2.1.3'] = `Three natural categories emerge from functional analysis:

Category 1 — Structural Entities (define the system's shape): Framework, Series, Round, Question. These are the static definition entities that don't change during a session. They define WHAT gets asked and in what order. The dependency graph lives here — Series dependencies create a directed acyclic graph (DAG) that determines execution order.

Category 2 — Runtime Entities (capture the session's state): Session, Answer, Artifact. These are the dynamic entities that change as the session progresses. They capture WHAT was answered and what was extracted. The artifact dictionary is the central data structure here — it accumulates across all series.

Category 3 — Output Entities (produce the deliverables): Project, Export, Engine. These are the container and delivery entities. Projects hold sessions, Exports hold compiled specifications, and the Engine orchestrates everything.

The categories map to architectural layers: structural → data model (JSON schema definitions), runtime → engine layer (session management, artifact extraction), output → export layer (format compilation, file I/O). The dependency graph creates cross-category relationships where structural entities (Series) consume output entities (Artifacts) from other structural entities — this is the key insight that makes the framework self-referential.

The category boundaries are clean: no entity belongs to multiple categories. This separation enables independent testing (structural entities can be validated without runtime entities) and independent evolution (adding a new export format doesn't affect structural entities).`;

A['2.2.1'] = `Core entities (system cannot function without): Framework, Session, Question, Artifact, Engine. These five entities are the minimal viable set — without any one of them, the system cannot ask questions, record answers, or produce output.

Framework defines what to ask. Question defines individual probes. Session captures the interaction. Artifact extracts structured data. Engine orchestrates the flow.

Peripheral entities (system works but is limited without): Series, Round, Answer, Project, Export.

Series and Round are organizational — they group Questions but the system could theoretically work with a flat list of Questions. Answer is the data record of a Question response — without it, the system would lose history, but the extraction could theoretically happen in real-time. Project is a container — without it, sessions would be unorganized but still functional. Export is a deliverable — without it, the system produces artifacts but no compiled specifications.

The core/peripheral split is important for implementation: core entities get first-class type definitions, comprehensive validation, and priority error handling. Peripheral entities get simpler types and can tolerate graceful degradation (e.g., if Export generation fails, the session data is still preserved).

Context-dependent classification: The Engine becomes peripheral if the system is used as a pure data model (just defining the framework without running it). The Project becomes core if multi-project management is a requirement (which it currently is). This context-dependency is why the entity model includes both perspectives.`;

A['2.2.2'] = `Moderate granularity — key specializations become distinct entities, but trivial variations are collapsed.

Example of appropriate splitting: Session and Answer are separate entities even though Answers live inside Sessions, because Answers have their own lifecycle (they can be edited, skipped, or marked as invalid) and their own relationships (each Answer links to exactly one Question and contributes to specific Artifacts).

Example of appropriate merging: Round and Focus are NOT separate entities. The "focus" is just a string attribute of Round. Splitting them would add complexity without enabling new behaviors.

Example of progressive refinement: The initial model had separate "OpenEndedAnswer" and "MultiChoiceAnswer" entities. These were merged into a single "Answer" entity with a choice_id attribute that may be null (for open-ended only) or populated (for follow-up classification). The split wasn't adding value because both types share the same lifecycle and storage.

Granularity decision criteria: An entity should be separate if it (a) has a distinct lifecycle, (b) participates in unique relationships, (c) has attributes not shared with the candidate parent, or (d) is independently addressable (has its own ID). Question passes all four tests. Round passes tests (a) and (d) but not (b) and (c) — yet it's still separate because it provides essential organizational structure.

The balance: 10 entity types total. Fine enough to capture all meaningful distinctions in the system. Coarse enough to keep the type system manageable. Each entity has 5-15 attributes. The total attribute count across all entities is approximately 80, which is within the cognitive load limit for a single developer.`;

A['2.2.3'] = `Shared attributes grouped by functional category:

Universal attributes (shared by most entities): id (unique identifier), created_at (timestamp), updated_at (timestamp). These are present on Session, Answer, Artifact, Project, and Export. Question and Framework use id but not timestamps (they're static definitions).

Structural attributes (shared by definition entities): name, description, text. Framework has name+description. Series has name+description. Round has focus. Question has text. These are all human-readable strings that describe the entity's purpose.

Relational attributes (shared by entities that reference others): The FK pattern appears on Session (project_id → Project), Answer (question_id → Question), Artifact (source_question_id → Question), Export (session_id → Session). The consistency of this pattern (always string FKs, always referencing by ID) simplifies the storage layer.

Content attributes (unique to each entity): Framework has depends_on/provides/consumes arrays. Session has answers/artifacts dictionaries. Answer has open_ended/choice_id. Artifact has key/value/confidence. These are the distinguishing attributes that make each entity type necessary.

The dependency graph between Series creates a cross-cutting concern: Series entities have both structural attributes (name, description, rounds) and dependency attributes (deps, consumes, provides). The consumes/provides arrays use string keys that must match artifact dictionary keys — this implicit contract is enforced at runtime by the question router, not at compile time. A type-safe artifact key type could improve this.`;

A['2.3.1'] = `Tightly bounded — scope is narrow and well-defined.

The system boundary encompasses: the CLI interface (src/cli/), the core engine (src/engine/), the storage layer (src/storage/), the LLM integration (src/llm/), the export pipeline (src/export/), the web UI (web/), and the test suite (tests/).

Outside the boundary: external LLM APIs (OpenAI, Anthropic, Gemini, Mistral), the user's filesystem (projects directory), and the npm registry (for distribution). The system interacts with these through well-defined interfaces (HTTP for LLM APIs, filesystem API for storage, npm CLI for distribution).

The boundary is enforced by: the StorageProvider interface (abstracts filesystem access), the LLMProvider interface (abstracts API calls), and the SpaceConfig type (defines all configurable parameters). No entity inside the boundary reaches outside except through these interfaces.

The tight boundary is a design strength: it makes the system predictable (limited external dependencies), testable (all interfaces can be mocked), and composable (users can integrate SPACE into larger workflows by calling createSpace() programmatically). The system can run fully offline (LLM integration is optional) and has no runtime dependencies beyond Node.js.`;

A['2.3.2'] = `Three external actors with distinct interaction patterns:

1. Human Respondent — Primary actor. Interacts via CLI (terminal prompts) or Web UI (browser forms). Provides free-text answers to open-ended questions and selections from multi-choice follow-ups. The respondent's primary interaction loop: read question → formulate answer → type response → select classification → proceed to next question. The system must be responsive to this loop — no unnecessary friction, clear progress indication, ability to skip and return.

2. LLM API (Optional) — Secondary actor. Called when auto-fill is requested or when the respondent wants AI-assisted answer formulation. Interaction pattern: send question context + respondent's partial answer → receive suggested completion. The LLM is a tool, not a co-author — the respondent always has final say. Fallback: if LLM is unavailable, the system works identically without it.

3. File System / Browser Storage — Persistence actor. Sessions are saved as JSON files on disk (CLI) or in browser localStorage/IndexedDB (Web UI). The storage layer handles serialization, compression (for large sessions), and atomic writes (to prevent corruption). The system reads from storage on startup (resume session) and writes after each answer (checkpoint). No network storage, no cloud sync — purely local persistence.

No other actors interact with the system. There is no authentication, no multi-user support, no API server (the web UI serves static files + local REST API). The three-actor model keeps the system simple, secure, and offline-capable.`;

A['2.3.3'] = `Stateful lifecycle with well-defined transitions:

Session lifecycle: created → active → paused/completed. Created when "space init" or "space run" is invoked. Active while questions are being answered. Paused when the user exits (auto-saved). Completed when all questions are answered or skipped. Can be resumed from paused state.

Question lifecycle: presented → answered/skipped. Presented when the question router selects it (based on dependency resolution). Answered when the respondent provides both open-ended text and follow-up selection. Skipped when the respondent explicitly skips (with optional reason). Questions can be re-answered (overwriting previous answer).

Artifact lifecycle: extracted → refined → finalized. Extracted when an answer is processed (pattern matching, keyword detection). Refined when subsequent answers provide additional context. Finalized when the series completes (no more extraction possible for this artifact key).

Export lifecycle: not_generated → generated → stale. Generated on-demand when the user requests export. Stale when new answers have been recorded since the last export. Regeneration overwrites the stale export.

Entity lifecycle summary: Framework and Series are immutable (defined once, never change). Rounds and Questions are immutable (fixed in the framework JSON). Sessions are mutable (answers accumulate). Artifacts are mutable (refined across series). Exports are computed (regenerated from current state). The lifecycle model ensures data integrity: immutable entities provide a stable reference, mutable entities track progress, computed entities reflect current state.`;

A['2.4.1'] = `No major entity gaps identified. The entity set is comprehensive for the current scope.

Potential minor gaps: (1) A "User" or "Respondent" entity could track who is answering — currently implicit in the Session. This would matter for multi-user scenarios but is explicitly out of scope. (2) A "Template" entity could define reusable framework configurations — currently each framework is hardcoded in JSON files. This would enable user-defined frameworks but adds significant complexity. (3) A "History" or "AuditLog" entity could track all changes — currently the Session's answers array serves this purpose but doesn't capture edit history or undo operations.

The entity set is deliberately minimal — each entity must justify its existence against the current feature set. Adding entities without corresponding behaviors creates dead weight that complicates the type system, storage layer, and test suite. The current 10-entity model covers all implemented features with no entity serving a purely decorative purpose.

Future entity candidates: "User" (multi-user support), "Template" (custom frameworks), "Webhook" (event notification), "Metric" (usage analytics), "Plugin" (extension system). None of these are needed for the current feature set. The entity model should evolve only when new features require it, not speculatively.`;

A['2.4.2'] = `No merges or splits needed. The entity boundaries are clean and well-motivated.

Verification: Each entity passes the four-entity-test: (1) distinct lifecycle — yes for all 10 entities. (2) unique relationships — yes (no two entities have identical relationship patterns). (3) non-shared attributes — yes (each entity has at least 2 attributes not shared with any other entity). (4) independent addressability — yes (each entity has a unique ID).

The current 10-entity model is stable and should not change without significant new requirements. Entity changes are expensive: they cascade through the type system, storage schema, API contracts, test suite, and documentation. The cost-benefit ratio only favors changes when new features demand it.

One observation: the Answer entity currently stores both the open-ended text and the follow-up choice. An alternative design would split these into OpenEndedResponse and FollowUpResponse entities. This was considered and rejected because: (a) every question has both an open-ended and follow-up component (they're always co-created), (b) splitting adds a join requirement for any query that needs both, and (c) the lifecycle is identical (both created/updated together). The current unified Answer entity is the right design.`;

A['2.4.3'] = `Key constraints and invariants:

1. Framework Immutability — A Framework cannot be modified after creation. The JSON files are read-only at runtime. This ensures consistent question delivery across sessions.

2. Session Uniqueness — Each Session has a UUID that is unique across all projects. Generated via crypto.randomUUID(). No two sessions can share an ID.

3. Question ID Format — Question IDs follow the pattern "S.R.Q" where S=series (1-7), R=round (1-5), Q=question (1-5). This format is validated on load.

4. Dependency Ordering — A series cannot start until all its dependency series have completed at least one round. Enforced by the question router's dependency resolution algorithm.

5. Artifact Key Uniqueness — Each artifact key is unique within a session's artifact dictionary. Overwriting an existing key is allowed (refinement) but logged.

6. Answer Completeness — A question is considered "answered" only when both the open-ended text AND the follow-up choice are provided. Partial answers are stored but don't count toward completion.

7. Export Atomicity — Export generation is atomic — either all requested formats succeed or the operation fails cleanly. No partial exports are left on disk.

8. Storage Consistency — After each answer, the session state is written to disk atomically (write to temp file, then rename). This prevents corruption if the process is interrupted.`;

A['2.5.1'] = `Edge cases and their handling:

1. Empty Session — User starts a session and immediately exits without answering any questions. Handling: session is saved with zero answers, zero artifacts, status "paused". Can be resumed or abandoned.

2. Duplicate Answers — User re-answers a question that was already answered. Handling: the new answer overwrites the old one. The artifact dictionary is re-extracted from the new answer. The old answer is lost (no version history in current implementation).

3. Very Long Answers — User provides an answer exceeding 5000 characters. Handling: the answer is stored in full. No truncation. The artifact extraction may be slower due to parsing but remains functional.

4. Invalid Follow-up Selection — User selects a follow-up choice that doesn't exist in the question's choices array. Handling: validation rejects the selection, returns an error, and re-presents the question.

5. Corrupted Session File — The session JSON file is manually edited or corrupted. Handling: the StorageProvider catches the parse error, logs a warning, and offers to start a new session. No crash.

6. Missing Framework Files — The prompt-framework JSON files are deleted or moved. Handling: the engine fails to load the framework and exits with a clear error message. No partial operation.

7. Concurrent Access — Two processes try to write to the same session file. Handling: not currently handled (single-user system). The last writer wins. This is acceptable for the current scope.

8. All Questions Skipped — If every question is skipped, the session completes with empty artifacts. The export produces a valid but empty specification. This is a valid edge case (user explored the framework without committing to answers).`;

A['2.5.2'] = `Entity composition forms a clear hierarchy:

Level 0: Framework (root container)
  Level 1: Series (Framework contains 7 Series)
    Level 2: Round (Series contains 3-5 Rounds)
      Level 3: Question (Round contains 2-5 Questions)
        Level 4: Choice (Question contains 3-5 Choices)

This is a strict containment hierarchy — each entity belongs to exactly one parent at each level. No entity participates in multiple containments at the same level.

Cross-cutting relationships exist outside the containment hierarchy:
- Session contains Answers (1:many, Session is the aggregate root)
- Session contains Artifact dictionary (1:1, the dictionary is a value object)
- Answer references Question (many:1, FK relationship)
- Artifact references Question (many:1, FK relationship for source tracking)
- Export references Session (many:1, FK relationship)
- Project contains Sessions (1:many, Project is an aggregate root)

The dependency graph creates cross-series composition where later Series consume Artifacts produced by earlier Series. For example, Series 3 (Semantic Relationships) consumes the entity_list artifact produced by Series 2 (Ontological Characteristics). This is not containment but dependency — Series 3 doesn't own the entity_list, it reads from it.

The aggregate roots are Framework (for the question structure) and Project (for the session data). All other entities are reachable through these roots. This simplifies storage: saving a Project saves all its Sessions, which save all their Answers and Artifacts. Loading a Framework loads all its Series, which load all their Rounds, which load all their Questions.`;

A['2.5.3'] = `Cardinality and multiplicity relationships:

Framework → Series: 1:7 (exactly 7 series per framework, hardcoded)
Framework → depends_on: 1:0..5 (a series depends on 0-5 other series)
Series → Round: 1:3..5 (3-5 rounds per series)
Round → Question: 1:2..5 (2-5 questions per round)
Question → Choice: 1:3..5 (3-5 follow-up choices per question)
Session → Answer: 1:0..326 (0 to all questions answered)
Session → Artifact: 1:0..~100 (0 to many extracted artifacts)
Answer → Question: many:1 (each answer references exactly one question)
Artifact → Question: many:1 (each artifact traces to one source question)
Project → Session: 1:0..N (0 to many sessions per project)
Export → Session: many:1 (multiple export formats per session)

The dominant pattern is one-to-many containment (Framework→Series→Round→Question). The exceptions are the many-to-one reference patterns (Answer→Question, Artifact→Question) which represent the runtime data flow from questions to answers to artifacts.

Notable: the Framework→depends_on relationship is many-to-many (a series can depend on multiple other series, and a series can be depended upon by multiple other series). This creates the DAG that governs question ordering.

Optional relationships: Session→Answer is optional (session can exist with zero answers). Session→Artifact is optional (no artifacts extracted yet). Export→Session is required (every export must reference a session).

The cardinality constraints are enforced at different layers: structural constraints (Framework→Series count) are hardcoded in the framework definition. Runtime constraints (Session→Answer count) are enforced by the question router. Storage constraints (FK validity) are enforced by the StorageProvider implementation.`;

// ═══ SERIES 3: SEMANTIC RELATIONSHIPS ═══
A['3.1.1'] = `Direct associations between entities:

Framework → Series: containment (Framework "has" Series). Bidirectional: Series knows its parent Framework.
Series → Round: containment (Series "has" Rounds). Bidirectional.
Round → Question: containment (Round "has" Questions). Bidirectional.
Question → Choice: containment (Question "has" Choices). Unidirectional (Choices don't reference back).

Session → Answer: composition (Session "produces" Answers). Session owns Answers; Answers don't exist without Session.
Session → Artifact: composition (Session "extracts" Artifacts). Artifact dictionary is part of Session state.
Answer → Question: reference (Answer "responds to" Question). Weak reference — Answers can exist without their source Question (if framework changes).
Artifact → Question: reference (Artifact "derived from" Question). Traces provenance.
Export → Session: reference (Export "compiled from" Session). Weak reference.
Project → Session: composition (Project "contains" Sessions).

Association density: Moderate — 12 distinct associations across 10 entities. Most entities participate in 2-3 associations. The densest entity is Session (6 associations: contains Answers, contains Artifacts, belongs to Project, referenced by Exports, references current Question, tracks status).`;

A['3.1.2'] = `Association types and their semantics:

1. CONTAINS — Parent-to-child structural containment. Framework contains Series. Series contains Rounds. Round contains Questions. Question contains Choices. These are strong ownership relationships — deleting the parent deletes all children. Implementation: parent holds array of children.

2. REFERENCES — Weak linking between entities. Answer references Question (by question_id FK). Artifact references Question (by source_question_id FK). Export references Session (by session_id FK). These are weak relationships — deleting the referenced entity doesn't delete the referencing entity (but may leave orphaned references). Implementation: entity holds ID string of referenced entity.

3. PRODUCES — Creation relationship. Session produces Answers. Session produces Artifacts. These are stronger than references because the producing entity owns the created entity. Implementation: Session holds arrays/dictionaries of created entities.

4. CONSUMES — Data flow relationship. Series consumes Artifacts from previous Series. This is the most interesting association type because it creates the dependency graph. Implementation: Series defines "consumes" array of artifact keys; the question router checks that these artifacts exist before starting the series.

5. DEPENDS_ON — Ordering constraint between Series. Series A depends on Series B means A cannot start until B has completed. This is a weaker relationship than CONSUMES — it's about ordering, not data flow. Implementation: Series defines "deps" array of Series IDs.`;

A['3.2.1'] = `Hierarchy and containment structure:

The primary hierarchy is the Framework structure:
Framework (root)
  └── Series (7 children)
        └── Round (3-5 children per Series)
              └── Question (2-5 children per Round)
                    └── Choice (3-5 children per Question)

This is a strict tree hierarchy — no entity has multiple parents at the same level. Maximum depth: 4 levels (Framework → Series → Round → Question → Choice). Average branching factor: Series=7, Round=3.5, Question=3.5, Choice=3.5.

The runtime hierarchy is the Project structure:
Project (root)
  └── Session (0..N children)
        ├── Answer (0..326 children)
        ├── Artifact (0..~100 key-value pairs)
        └── Export (0..5 children)

The two hierarchies intersect at the Session level: a Session is both part of a Project hierarchy AND linked to a Framework hierarchy (through its current question pointer and answer references). This intersection is managed by the Engine, which translates between the static Framework hierarchy and the dynamic Session state.`;

A['3.2.2'] = `Inheritance and specialization:

The entity model uses composition over inheritance. No entity inherits from another entity.

Why no inheritance: The 10 entities are distinct types with different attributes and behaviors. There is no "base entity" that others extend. Each entity has its own type definition in src/types/index.ts. The closest thing to inheritance is the StorageProvider interface — FileSystemStorage and SQLiteStorage both implement the same interface, but this is interface implementation, not entity inheritance.

Alternative considered: A "BaseEntity" abstract class with id, created_at, updated_at. Rejected because: (a) not all entities need timestamps (Framework, Series, Round, Question are static), (b) the id types differ (number for Framework/Series, string for Session/Answer/Artifact), (c) it would force uniform structure on heterogeneous entities.

Trait-based approach: Instead of inheritance, the system uses traits (behaviors) that entities opt into: "storable" (can be persisted), "extractable" (can have data extracted from it), "exportable" (can be compiled into output). These are not formal type system constructs but implementation patterns — a storable entity has a corresponding StorageProvider method, an extractable entity has an artifact extraction handler, an exportable entity has a format compiler.`;

A['3.3.1'] = `Causal and temporal relationships:

Direct causation chains:
1. User answers Question → Answer is created → Artifact extraction runs → Artifact dictionary is updated. This is a synchronous chain — each step triggers the next immediately.

2. All Questions in a Round are answered → Round is marked complete → Next Round is enabled (if within same series). This is a sequential chain — rounds within a series execute in order.

3. All Rounds in a Series are answered → Series is marked complete → Dependent Series are enabled. This triggers the dependency resolution for downstream series.

4. User requests Export → Export generation reads Session state + Artifact dictionary → Compiled document is written to disk. This is a demand-driven chain — exports happen only when requested.

Event-driven propagation: The Engine emits events at each transition point: question:presented, answer:submitted, artifact:extracted, round:completed, series:completed, session:completed. These events could be used for logging, analytics, or external integrations (though currently they're only used internally).

No feedback loops: The causal chains are strictly forward-moving. Answers don't cause questions to change (the framework is immutable). Artifacts don't cause earlier answers to change (extraction is one-way). This simplicity prevents infinite loops and makes the system predictable.`;

A['3.3.2'] = `Dependency chains and ordering constraints:

Series dependency graph (DAG):
- Series 1: no dependencies (can start immediately)
- Series 2: depends on [1] (must wait for Series 1)
- Series 3: depends on [2] (must wait for Series 2)
- Series 4: depends on [2, 3] (must wait for both)
- Series 5: depends on [1, 4] (must wait for both)
- Series 6: depends on [4, 5] (must wait for both)
- Series 7: depends on [5, 6] (must wait for both)

This creates a diamond-shaped DAG with Series 1 at the root and Series 7 at the leaf. The critical path is 1→2→3→4→5→6→7 (7 steps).

Within each series, rounds execute sequentially (Round 1 before Round 2, etc.). Within each round, questions can execute in any order (no inter-question dependencies within a round).

The dependency resolution algorithm: When the Engine needs the next question, it (1) identifies the first incomplete series whose dependencies are all met, (2) finds the first incomplete round in that series, (3) selects the first unanswered question in that round. If no series has all dependencies met (e.g., all remaining series are blocked), the session is complete.

Practical implication: A user who answers all of Series 1 can immediately jump to Series 2 (once Series 1 completes). They cannot skip to Series 3 without completing Series 2. This enforced ordering ensures that each series has the context it needs from predecessor series.`;

A['3.4.1'] = `Rules governing relationship changes:

Framework relationships (Series→Round→Question→Choice): Immutable. These are defined in JSON files and never change at runtime. The framework is a read-only reference.

Session relationships: Mutable with constraints.
- Session→Answer: Answers can be added (new questions answered) or updated (re-answering a question). Cannot be deleted (skipping is recorded as a "skipped" answer, not deletion).
- Session→Artifact: Artifacts can be added (new extraction) or updated (refined extraction). Cannot be deleted (artifacts are append-only with overwrite semantics).
- Session→Project: Immutable after creation. A session belongs to one project forever.

Export relationships: Regenerated, not modified. When an export is stale (new answers since last export), it's regenerated from scratch, not incrementally updated. The old export is overwritten.

Answer→Question: Immutable. Once an answer is linked to a question, the link doesn't change. If the framework changes (which it doesn't), orphaned answers would reference non-existent questions — this is handled by the "missing question" edge case (answer preserved but marked as orphaned).

The immutability of framework relationships is a key design decision: it ensures deterministic behavior. The Engine always sees the same framework structure, regardless of when it was loaded or how many sessions have been created. This eliminates an entire class of bugs related to framework evolution.`;

A['3.4.2'] = `Relationship composition and chaining:

Direct relationships: Framework→Series, Series→Round, Round→Question, Question→Choice. These are the only relationships defined in the framework JSON.

Indirect relationships (derived from direct):
- Framework→Question: derived through Series and Round. The path is Framework→Series→Round→Question. This path is used for question numbering (the full ID encodes the path: "2.3.1" means Series 2, Round 3, Question 1).
- Framework→Choice: derived through Series, Round, and Question. Used for answer validation (a choice must belong to the correct question).
- Session→Question: derived through the current_question_id pointer. The session tracks which question it's currently on, creating an implicit relationship.

Transitive chains: The dependency graph creates transitive chains. If Series 4 depends on Series 2 and 3, and Series 3 depends on Series 2, then Series 4 transitively depends on Series 2 through two paths (direct and through Series 3). The dependency resolution algorithm handles this correctly — it checks direct dependencies, not transitive ones, because the transitive dependencies are already satisfied by the direct ones.

Composable relationships: The artifact consumption pattern composes relationships across series. Series 3 consumes entity_list (produced by Series 2), and Series 4 consumes entity_list + relationship_graph (produced by Series 2 + 3). The composition is additive — later series consume artifacts from all predecessor series.

Weighted composition: Not applicable in the current system. All relationships are binary (exists/doesn't exist) with no weights or strengths. This is appropriate for a specification tool — there's no concept of "weakly related" or "strongly associated" in the question framework.`;

// ═══ SERIES 4: PROCEDURAL BREADTH ═══
A['4.1.1'] = `Overall procedure scope: End-to-end specification generation spanning 7 phases (one per series).

Start state: User has a project idea or system to specify. No prior documentation, no existing specification, no code. Just a concept in their head.

End state: A comprehensive, multi-format specification document that captures domain context, entities, relationships, procedures, technical requirements, methodology, and operational preferences. The specification is machine-readable (JSON/YAML), human-readable (Markdown/HTML), and LLM-consumable (prompt format).

The procedure is moderate in scope — it's not a single atomic task (too narrow) and not a multi-phase program (too broad). It's an interactive elicitation session that takes 1-4 hours depending on depth of answers and number of questions answered.

Sub-processes: (1) Project initialization — create project directory, load framework, configure LLM provider. (2) Interactive question flow — present questions, collect answers, extract artifacts. (3) Artifact accumulation — build the artifact dictionary across all series. (4) Export compilation — generate specification documents in requested formats. (5) Session management — save, resume, abandon sessions.

The procedure is interactive (requires human input at each step) but structured (the framework determines the question order). The human provides domain knowledge; the system provides structure and extraction.`;

A['4.1.2'] = `Step breakdown: 5-8 distinct stages with clear waypoints.

Stage 1: Initialize — Create project, load framework, verify environment. (CLI: "space init <name>")
Stage 2: Series 1 (Conceptual Depth) — 6 questions across 3 rounds. Establishes domain, audience, vocabulary. (~15 min)
Stage 3: Series 2 (Ontological Characteristics) — 15 questions across 5 rounds. Discovers entities, attributes, boundaries. (~30 min)
Stage 4: Series 3 (Semantic Relationships) — 8 questions across 4 rounds. Maps associations, hierarchies, causation. (~20 min)
Stage 5: Series 4 (Procedural Breadth) — 6 questions across 3 rounds. Defines workflows, decisions, error handling. (~15 min)
Stage 6: Series 5 (Technical Specifications) — 20 questions across 4 rounds. Captures hardware, software, performance, security. (~40 min)
Stage 7: Series 6 (Development Methodologies) — 6 questions across 3 rounds. Determines process, quality, communication. (~15 min)
Stage 8: Series 7 (Operational/Functional) — 6 questions across 3 rounds. Covers deployment, monitoring, maintenance. (~15 min)

Total: 67 questions. Average 2-3 minutes per question (reading, thinking, typing). Estimated session time: 2-3 hours for thorough answers, 30-45 minutes for quick answers.

Waypoints: Each series completion is a natural checkpoint. The session auto-saves after each answer, so any interruption preserves progress. The "space export" command can be run at any waypoint to generate a partial specification.`;

A['4.2.1'] = `Decision points and branching:

The primary decision point is the follow-up choice after each open-ended question. Every question has 2-5 follow-up options that classify the answer. This classification drives:
1. Artifact extraction — the chosen option determines which artifact keys are populated.
2. Series routing — certain choices enable or disable dependent questions.
3. Export formatting — choices influence the tone, depth, and structure of exported specifications.

No branching in question order: The question sequence is deterministic — it follows the framework definition exactly. There are no "if answer X, skip to question Y" paths. This simplification was a deliberate design decision: the framework is designed to ask all 67 questions regardless of answers. The follow-up choices classify answers but don't alter the question flow.

Why no branching: (1) Branching would make the framework harder to understand and predict. (2) The 326-probe structure is already comprehensive — there's no need to skip questions. (3) Artifact extraction handles the differentiation — the same question can produce different artifacts depending on the follow-up choice.

Edge case: If a user skips all questions in a series, downstream series that depend on artifacts from the skipped series will have empty artifacts. This is handled gracefully — the export will contain placeholder text for missing artifacts.`;

A['4.2.2'] = `Inputs and outputs at each stage:

Stage 1 (Initialize): Input — project name (string), optional config overrides. Output — project directory, loaded framework, initialized session.

Stage 2 (Series 1): Input — user's free-text answers to 6 questions. Output — artifacts: domain, audience_level, terminology_preferences, scaffolding_preference. These are string values derived from follow-up choices.

Stage 3 (Series 2): Input — user's free-text answers + Series 1 artifacts (for context). Output — artifacts: entity_list (array of entity objects), entity_attributes (nested object), entity_categories (category map), entity_hierarchy (tree), entity_constraints (constraint list).

Stage 4 (Series 3): Input — user's answers + Series 1-2 artifacts. Output — artifacts: relationship_graph (adjacency list), hierarchy_structure (tree), dependency_chains (ordered list), composition_rules (rule set).

Stage 5 (Series 4): Input — user's answers + Series 1-3 artifacts. Output — artifacts: procedure_steps (step array), decision_points (decision tree), branching_complexity (complexity score), io_contracts (input/output specs).

Stage 6 (Series 5): Input — user's answers + Series 1,4 artifacts. Output — artifacts: hardware_requirements (specs), software_stack (tech list), performance_targets (targets), integration_contracts (API specs), timeline (milestones).

Stage 7 (Series 6): Input — user's answers + Series 4,5 artifacts. Output — artifacts: development_cadence, quality_practices, team_composition, communication_patterns.

Stage 8 (Series 7): Input — user's answers + Series 5,6 artifacts. Output — artifacts: deployment_strategy, runtime_configuration, monitoring_plan, maintenance_policy.

Data flow: Artifacts flow forward through the dependency graph. No artifact flows backward. The artifact dictionary grows monotonically throughout the session.`;

A['4.3.1'] = `Error handling and recovery:

Level 1 — Question-level errors:
- Invalid follow-up selection → re-prompt with error message and valid options.
- Empty open-ended answer → allow (some questions may not need text if the follow-up is sufficient).
- Answer too long (>10KB) → warn but accept. Large answers slow artifact extraction.

Level 2 — Session-level errors:
- Corrupted session file → offer to start new session or load from last good checkpoint.
- Missing artifact dependency → log warning, continue with empty artifact for the dependent series.
- Storage write failure → retry once, then abort with error message.

Level 3 — System-level errors:
- Framework JSON parse error → abort with clear error message identifying the malformed file.
- LLM API failure → skip auto-fill, continue with manual input. Log the API error.
- Node.js runtime error → process exits with stack trace. Session was auto-saved, so resume works.

No retry-based recovery: The system favors fail-fast over retry. If something is broken (missing framework, corrupted storage), the user should know immediately rather than having the system silently retry and potentially make things worse.

No rollback: The system doesn't implement undo. If a user answers a question incorrectly, they re-answer it (overwriting the previous answer). This is simpler than rollback and sufficient for the use case — specification answers aren't mission-critical data.`;

A['4.3.2'] = `Step granularity: Mixed — core steps are fine; well-established procedures are coarser.

Fine-grained steps (atomic actions):
- Present a single question to the user
- Record a single answer (open-ended + follow-up)
- Extract artifacts from a single answer
- Save session state to disk
- Validate a follow-up selection

Coarse-grained steps (multi-action phases):
- Initialize a project (create directory, load framework, configure LLM, create session)
- Complete a round (present all questions in the round, collect all answers, mark round complete)
- Export a specification (compile all formats, write all files, generate index)

The granularity split reflects the interaction model: fine-grained steps happen frequently (67 questions × multiple operations each) and need to be fast and reliable. Coarse-grained steps happen rarely (once per round/series/export) and can tolerate slight latency.

For error handling, fine-grained steps get immediate feedback (invalid selection → re-prompt). Coarse-grained steps get batch error reporting (export failure → list all failed formats).

The step granularity is implemented in the Engine's method decomposition: askQuestion() is fine-grained, completeRound() is coarse-grained, exportSession() is coarse-grained. Each coarse method calls multiple fine methods internally.`;

// ═══ SERIES 5: TECHNICAL SPECIFICATIONS ═══
A['5.1.1'] = `Hardware platform support:

Primary target: x86-64 desktop/laptop running Node.js 18+. This is the development and primary use case — a developer runs SPACE on their workstation.

Secondary targets: ARM64 (Apple Silicon Macs, Raspberry Pi, cloud instances). The system uses no architecture-specific code, so ARM64 is supported transparently through Node.js cross-compilation.

Explicitly not targeted: Mobile devices (iOS/Android), embedded systems (Arduino, ESP32), GPUs (no compute-intensive operations), real-time systems (no latency guarantees).

Platform-agnostic design: The system uses only Node.js standard APIs (fs, path, crypto, http). No native bindings, no platform-specific code, no conditional compilation. The TypeScript compiler targets ES2022, which is supported on all modern Node.js versions across all architectures.

Container support: The system runs in Docker containers on any architecture. No special Dockerfile needed — a basic Node.js image suffices. The web UI is accessible via port mapping (node web/server.mjs -p 8888).

Architecture independence is a feature: users don't need to think about what platform they're on. The system works identically on Linux, macOS, and Windows (with minor path separator differences handled by the path module).`;

A['5.1.2'] = `Hardware specifications:

Minimum: Node.js 18+, 256MB RAM, 50MB disk space. The CLI tool is lightweight — the entire codebase is ~3500 LOC TypeScript compiled to ~500KB JavaScript. The framework JSON files total ~50KB. Session files are ~10KB each. The minimum specs accommodate any modern computer.

Recommended: Node.js 20 LTS, 1GB RAM, 500MB disk space. The web UI adds browser overhead. The LLM integration adds API call latency (not local compute). 500MB disk accommodates 50+ projects with 10+ sessions each.

High-performance: Not needed. The system is I/O-bound (reading/writing JSON files, making HTTP requests to LLM APIs) not CPU-bound. A Raspberry Pi 4 handles the workload comfortably. The bottleneck is human typing speed, not system processing.

Storage growth model:
- Per question: ~1KB (answer text + follow-up + metadata)
- Per session: ~10KB (67 answers × ~1KB + overhead)
- Per project: ~500KB (10 sessions + exports)
- Per workspace: ~5MB (100 projects)
- Framework: ~50KB (static, shared across all projects)

The storage model is designed for decades of use — even at 1 project/day, a year of usage produces <200MB of data.`;

A['5.1.3'] = `Networking requirements:

Core system: No network required. The CLI tool, framework loading, session management, and local export all work completely offline. The system can be installed via npm (one-time network access) or copied from a USB drive.

Optional network: LLM API calls require internet access. The system gracefully degrades without network — all features work, just without AI-assisted auto-fill. The LLM provider is configured per-project; if not configured, no network calls are made.

Web UI: The web server binds to localhost only. No external network access required. The browser loads the SPA from the local server. No CDN, no external assets (except the Inter font from Google Fonts, which degrades gracefully to system fonts).

Offline-first design: The system was designed for use on airplanes, in air-gapped environments, and in areas with unreliable internet. Every feature has an offline fallback:
- No LLM → manual answer input
- No network → local storage only
- No browser → CLI interface only

The offline-first design is a deliberate architectural choice: it makes the system reliable (no network = no failure), fast (local I/O = instant), and private (no data leaves the machine).`;

A['5.1.4'] = `Storage infrastructure:

Primary storage: Local filesystem. JSON files organized in project directories under ~/.space/projects/. No databases required. The current JSON-file approach is sufficient for hundreds of projects with thousands of sessions.

SQLite adapter: Exists at src/storage/sqlite.ts using sql.js (WASM-based SQLite). Implements the StorageProvider interface. 17 tests pass. Not yet integrated into the main flow but available for future use when query performance matters (e.g., searching across thousands of sessions).

No object storage, no caching layers, no CDN. The system is designed for single-user local use — no need for distributed storage.

Storage model:
- Framework: read-only JSON files in prompt-framework/json/
- Projects: ~/.space/projects/<name>/
  - .space.json: project metadata
  - sessions/<uuid>/state.json: session state + answers
  - exports/<format>-specification.<ext>: compiled specifications

Storage growth: ~10KB per session, ~500KB per project (10 sessions), ~5MB for a large workspace (100 projects). Total storage is trivial.

Atomic writes: The StorageProvider writes to a temporary file first, then renames to the target path. This prevents corruption if the process is interrupted mid-write.`;

A['5.1.5'] = `Infrastructure target:

Local development only — no cloud, no on-premise servers, no hybrid deployment.

Deployment model: npm global install (CLI) or git clone + node server (web UI). The system runs on the developer's machine. The web server binds to localhost:8888. No port forwarding, no DNS, no SSL (local only).

No containerization: Docker is not needed for a local CLI tool. The system has no system dependencies beyond Node.js.

No orchestration: No Kubernetes, no Docker Compose, no process managers. The system is a single Node.js process that runs until the user stops it.

Compliance: None required. The system processes no personal data beyond what the user voluntarily enters. No PII is transmitted (LLM API calls send only the user's answers). No analytics, no telemetry, no tracking.

Privacy: The system is inherently private — all data stays on the local machine. LLM API calls are the only network communication, and they're optional and controlled by the user. The user can configure local-only LLM providers (Ollama) for complete air-gapped operation.

Future consideration: If the system evolves to support team features or cloud hosting, the infrastructure would need to change. The StorageProvider abstraction is designed to accommodate this — a future CloudStorage implementation could replace FileSystemStorage without changing the engine logic.`;

A['5.2.1'] = `Programming languages and runtimes:

Primary language: TypeScript (strict mode). All source code in src/ is TypeScript. The type system is used extensively — interfaces for all entities, discriminated unions for state machines, generics for the StorageProvider and LLMProvider abstractions.

Runtime: Node.js 18+ (ESM modules). The package.json specifies "type": "module" and "engines": { "node": ">=18" }. The codebase uses modern JavaScript features: async/await, optional chaining, nullish coalescing, structuredClone.

Build target: ES2022. The tsconfig.json targets ES2022 with module: ESNext and moduleResolution: bundler. Output is ESM (.js files with import/export).

Frontend: Vanilla JavaScript + Tailwind CSS (single-file HTML). No React, no Vue, no framework. The web UI is a single index.html file with inline JavaScript and Tailwind via CDN. This was a deliberate choice to minimize dependencies and build complexity.

Why TypeScript: The type system catches errors at compile time, enables IDE autocompletion, and serves as living documentation. The strict mode configuration (strictNullChecks, noImplicitAny, etc.) prevents entire categories of runtime errors.

Why vanilla JS for frontend: The web UI is a thin wrapper around the REST API. It doesn't need the component model, state management, or build tooling that React/Vue provide. A single HTML file is simpler to maintain, deploy, and understand.`;

A['5.2.2'] = `Operating system support:

Primary: Linux (Ubuntu 20.04+, Fedora 36+, Debian 11+). All development and testing occurs on Linux. The CI/CD pipeline tests on Ubuntu.

Secondary: macOS (12+). Apple Silicon (ARM64) is fully supported via Node.js universal binaries. File system paths use forward slashes (POSIX).

Tertiary: Windows (10+, WSL2 recommended). Native Windows support via Node.js path module (handles backslash/forward slash conversion). The CLI works in PowerShell, CMD, and Git Bash. WSL2 provides a Linux-compatible environment.

No mobile: iOS and Android are not supported. The CLI requires a terminal, and the web UI requires a desktop browser.

Platform-specific code: Minimal. The path module handles path separator differences. The crypto module handles UUID generation. The fs module handles file operations. No platform-specific conditionals in the codebase.

Testing matrix: CI/CD tests on Node.js 18, 20, and 22 across Ubuntu. Manual testing on macOS and Windows. The test suite (112+ tests) covers all core functionality regardless of platform.`;

A['5.2.3'] = `Third-party dependencies:

Core dependencies (in package.json):
- None for the CLI tool — pure Node.js standard library
- sql.js (WASM SQLite) for the SQLite storage adapter
- vitest for testing

Dev dependencies:
- typescript (compiler)
- vitest (test runner)
- @types/node (type definitions)

Frontend dependencies:
- Tailwind CSS (via CDN) for styling
- Inter font (via Google Fonts CDN) for typography

What's NOT used (deliberate exclusions):
- No Express/Koa/Fastify — the web server uses Node.js http module directly
- No React/Vue/Svelte — the frontend is vanilla JS in a single HTML file
- No ORM — storage is direct JSON file I/O
- No bundler (Webpack/Vite/Rollup) — the backend is native ESM, the frontend is a single file
- No Lodash/Underscore — native array methods suffice
- No Mocha/Jest — vitest is faster and has better ESM support

The minimal dependency approach reduces: (1) Supply chain attack surface, (2) Update maintenance burden, (3) Build complexity, (4) New contributor onboarding time. The trade-off is more manual code for things libraries would provide, but the total codebase is small enough (~3500 LOC) that this trade-off is favorable.`;

A['5.2.4'] = `Browser support for the web UI:

Primary: Chrome 90+, Firefox 90+, Edge 90+, Safari 15+. These browsers support ES2022 features, CSS Grid, CSS Custom Properties, and the Fetch API.

No IE11: The web UI uses modern JavaScript features (optional chaining, nullish coalescing, template literals, async/await) that are not transpiled for IE11. IE11 market share is negligible.

No server-side rendering: The web UI is a client-side SPA. The server only serves static files and provides the REST API. All rendering happens in the browser.

Progressive enhancement: The core functionality (question flow, answer recording) works without JavaScript if needed — the server API can be called directly with curl. The web UI adds a graphical interface on top of the API.

Mobile browsers: The UI is responsive (Tailwind responsive utilities) but not optimized for mobile. The question flow works on phones/tablets but the experience is better on desktop. Mobile is not a primary use case — SPACE is a desktop tool.`;

A['5.2.5'] = `Build systems and packaging:

Backend build: TypeScript compiler (tsc). No bundler. The src/ directory is compiled to dist/ with the same directory structure. The build command is "tsc" (aliased to "npm run build"). Output is ESM JavaScript with .js extension and .d.ts declaration files.

Frontend build: None. The web UI is a single HTML file (web/index.html) that loads Tailwind from CDN and contains inline JavaScript. No build step required.

Test runner: Vitest. Fast, ESM-native, TypeScript-aware. Test files are in tests/unit/. The test command is "vitest run" (aliased to "npm test"). Tests import directly from src/ (no pre-compilation needed).

Package distribution: npm publish. The package.json includes:
- name: "space-cli"
- version: "2.0.0"
- bin: { "space": "./dist/cli/index.js" }
- files: ["dist/", "prompt-framework/"]
- engines: { "node": ">=18" }
- prepublishOnly: "npm run build && npm test"

Distribution: npm global install (npm install -g space-cli). The CLI is accessible as the "space" command. The web UI is not distributed via npm — users clone the repo and run node web/server.mjs directly.

No CI/CD pipeline configured yet — builds are manual. The prepublishOnly hook runs build + test before publish. No Docker, no container registry, no deployment platform.`;

A['5.3.1'] = `Performance requirements:

Response time: <100ms for all local operations (question presentation, answer recording, artifact extraction, session save). The system should feel instantaneous — the user should never wait for the system.

LLM latency: 1-5 seconds for auto-fill API calls. This is network-bound and acceptable. The UI shows a loading indicator during LLM calls.

Memory usage: <100MB RSS for the CLI tool. <200MB RSS for the web server. The system processes one session at a time, so memory is proportional to session size, not concurrent users.

Disk I/O: <1MB/s write throughput for session saves. The system writes ~10KB per answer, so even at maximum answer frequency (one every 2 seconds), disk I/O is negligible.

CPU usage: <5% during normal operation. The system is I/O-bound (waiting for user input or LLM API responses), not CPU-bound. Artifact extraction uses string matching (no ML inference locally).

Concurrency: None required. The system handles one user, one session, one request at a time. The web server uses Node.js single-threaded event loop, which is sufficient for the expected load (1-2 concurrent browser tabs).

Scalability ceiling: The question router's dependency graph traversal is O(V+E) where V=7 nodes and E=10 edges — effectively constant time. Artifact extraction is O(n) where n is the answer text length. Session save is O(m) where m is the total session data size. All operations scale linearly with input size and are bounded by the fixed framework structure.`;

A['5.3.2'] = `Data volume and growth:

Current scale: 67 questions × 3-5 follow-up choices = 201-335 total options. 7 series, 25 rounds. The framework is static and small (~50KB JSON).

Session data: ~10KB per completed session (67 answers × ~100 bytes average text + follow-up selections + metadata). With 10 sessions per project, that's ~100KB per project.

Workspace projection: A developer working on 50 projects over 2 years would accumulate ~5MB of session data. This is trivial by any storage standard.

Growth rate: Linear with usage. No exponential growth patterns. No data compounding across sessions. Each session is independent.

Data lifecycle: Sessions are immutable after completion (no editing). Exports are regenerated on demand. No garbage collection needed — all data is useful and small.

If the system were to scale to team use (multiple users, shared projects), data volume would grow by a factor of N (team size). At 10 users × 50 projects × 10 sessions, that's ~50MB — still trivial. The SQLite adapter would become relevant at this scale for query performance across sessions.`;

A['5.3.3'] = `Availability and disaster recovery:

Availability target: Best-effort. No formal SLA. The system is a local development tool, not a production service. Occasional downtime (crash, bug) is acceptable and expected.

Data durability: High. Session data is written to disk after each answer (checkpoint). Crash recovery loses at most one answer (the most recent un-saved answer). The auto-save frequency (after every answer) makes data loss negligible.

Backup strategy: Manual file copy. The entire workspace (~5MB) can be backed up with a single "cp -r ~/.space/projects/ /backup/" command. No database dumps, no snapshot procedures.

Disaster recovery: Copy the backup directory to a new machine. The system has no external dependencies (no database to restore, no service to reconnect). The session files are self-contained JSON — they work on any machine with Node.js.

The simplicity of the storage model (JSON files) makes disaster recovery trivial — just copy the project directory.`;

A['5.3.4'] = `Scalability model:

Current model: Vertical. The system runs on a single machine, single process, single thread. Scaling means upgrading the machine (more RAM, faster disk) — but the current requirements are so low that scaling is not needed.

Horizontal scaling: Not needed and not supported. The system is single-user. Multiple users would each run their own instance.

Elastic scaling: Not applicable. The system doesn't have variable load — it processes one session at a time, always.

Serverless: Not applicable. The system requires persistent local storage (filesystem), which doesn't fit the serverless model.

The scalability ceiling is high: JSON files can handle millions of entries before performance degrades. The bottleneck would be the question router's dependency graph traversal, which is O(V+E) where V=7 nodes and E=10 edges — effectively constant time.`;

A['5.3.5'] = `Security and compliance:

Authentication: None. The system is single-user, local-only. No login, no passwords, no tokens.

Authorization: None needed. Single user has full access to all features.

Encryption: None for local storage. Data is stored as plaintext JSON files on the user's filesystem. This is appropriate for a local development tool — the user's filesystem permissions provide the access control.

Encryption in transit: TLS for LLM API calls (handled by the HTTP client). The system sends user answers to LLM providers over HTTPS. No sensitive data is transmitted beyond what the user explicitly sends.

Input validation: Follow-up selections are validated against the question's choices array. Answer text is stored as-is (no sanitization needed for local storage). Framework JSON is parsed with JSON.parse (throws on malformed input).

No compliance requirements: The system processes no personal data beyond what the user voluntarily enters. No GDPR, HIPAA, SOC2, or PCI-DSS requirements apply. No analytics, no telemetry, no tracking.

Security posture: Minimal attack surface. No network exposure (except optional LLM API calls). No user input processing beyond text storage. No file upload. No database queries. The system is as secure as a text editor.`;

A['5.4.1'] = `External systems and integrations:

Required integrations: None. The system is fully standalone.

Optional integrations:
1. LLM APIs (OpenAI, Anthropic, Google Gemini, Mistral, Ollama) — for auto-fill feature. Configured per-project via SpaceConfig. Each provider is behind the LLMProvider interface with a factory pattern for selection.

2. Git — for version control of project files. The GitIntegration class (src/integration/git.ts) provides auto-commit, diff, log, branch, and stash operations. Not required for normal operation.

3. npm registry — for package distribution. The system is published as "space-cli" on npm. Users install via "npm install -g space-cli".

No databases, no message queues, no external APIs (beyond optional LLM). The system is deliberately self-contained.`;

A['5.4.2'] = `Integration protocols and data formats:

LLM API: REST/JSON over HTTPS. Each provider (OpenAI, Anthropic, Gemini, Mistral) has a dedicated adapter that translates between the SPACE message format and the provider's API format. Ollama uses a local REST API (http://localhost:11434).

CLI → Engine: TypeScript function calls. The CLI (src/cli/) imports and calls the Engine (src/engine/) directly. No IPC, no HTTP, no serialization.

Web UI → Engine: REST/JSON over HTTP. The web server (web/server.mjs) wraps the Engine in HTTP endpoints. The web UI (web/index.html) calls these endpoints via fetch().

Export formats: JSON, Markdown, YAML, HTML, LLM prompt. Each format is a renderer that takes the session state + artifact dictionary and produces a string. The renderers are in src/export/.

Session persistence: JSON files on the filesystem. The StorageProvider interface abstracts this. The SQLite adapter (src/storage/sqlite.ts) provides an alternative persistence layer.

All formats are text-based. No binary formats. No compression. No encryption.`;

A['5.4.3'] = `Timeline and delivery cadence:

Completed milestones:
- Core engine + CLI (Phase 1): ~2 weeks
- Web UI (Phase 2): ~1 week
- Storage providers (Phase 3): ~1 week
- LLM integration (Phase 4): ~1 week
- Git integration (Phase 5): ~3 days
- Tests + documentation (ongoing): ~1 week total

Current status: v2.0.0 — all core features implemented, 112+ tests passing, ready for npm publish.

Future milestones:
- npm publishing: Ready (package.json configured, prepublishOnly hook set)
- CI/CD pipeline: Planned (GitHub Actions for automated testing)
- LLM auto-fill in web UI: Planned (requires UI framework changes)
- Collaborative sessions: Future (multi-user, shared projects)
- Plugin system: Future (user-defined extensions)

Delivery cadence: Irregular. Features are released when complete, not on a fixed schedule. The system is maintained by a single developer with no external deadlines.

Total: ~5 working days of active development. Each phase produced a working, tested increment. No phase depends on all previous phases being perfect — they build incrementally.`;

A['5.4.4'] = `Testing and rollout strategy:

Testing: Comprehensive unit tests (112+ tests across 11 test files). Tests cover:
- Core engine (67 tests — one per question)
- Template interpolation (16 tests)
- Snapshot lifecycle (6 tests)
- Consolidation (3 tests)
- LLM providers (20 tests)
- SQLite storage (17 tests)
- Git integration (13 tests)

Test execution: "vitest run" — completes in <2 seconds. Tests are deterministic (no external dependencies, no network calls, no file system side effects for most tests).

Rollout: Manual npm publish. No staging environment. The system is tested locally before publish. Users get the latest version via npm update.

Versioning: Semantic versioning (MAJOR.MINOR.PATCH). Breaking changes increment MAJOR. New features increment MINOR. Bug fixes increment PATCH.

Rollback: Users can install a specific version: "npm install -g space-cli@2.0.0". Git users can checkout a specific tag.`;

A['5.4.5'] = `Documentation and knowledge transfer:

README.md: Installation instructions, quick start guide, feature overview. ~200 lines.

CLI help: Built-in help via "space --help" and "space <command> --help". Generated from command definitions in src/cli/.

Framework JSON: The prompt-framework/json/ directory IS the documentation for the question taxonomy. Each JSON file documents one series with full question text, choices, dependencies, and metadata.

Type definitions: src/types/index.ts serves as API documentation. Every interface, type, and enum is documented with comments. TypeScript consumers get autocompletion and type checking as documentation.

Code comments: Minimal inline comments. The code is self-documenting through clear naming and type annotations. Comments explain "why" not "what".

Test suite as documentation: The test files demonstrate expected behavior. Reading tests/src/ gives a comprehensive understanding of how the system works.

API documentation: The web server's REST endpoints are documented in web/server.mjs comments. Each endpoint specifies method, path, request body, and response format.

Knowledge transfer: The system is designed for self-service. A developer can clone the repo, read the README, and be productive in 5 minutes. The framework JSON is the single source of truth for the question taxonomy — understanding it is equivalent to understanding the system.`;

// ═══ SERIES 6: DEVELOPMENT METHODOLOGIES ═══
A['6.1.1'] = `Development methodology: Iterative, phase-based development with test-driven increments.

Process: Build one feature at a time, test it thoroughly, then move to the next. No big design upfront — the architecture emerged from implementation. Each phase produced a working, tested increment.

Phase breakdown:
1. Core engine + CLI (2 days) — question routing, answer recording, session management, CLI interface
2. Framework data + tests (1 day) — all 67 questions, 112+ unit tests
3. Web UI (1 day) — Tailwind SPA with REST API backend
4. Storage + LLM + Git (2 days) — StorageProvider, LLM factory, GitIntegration
5. Documentation + packaging (1 day) — README, types, npm config, CI/CD

Total: ~5 working days. Each phase built on the previous one. No phase was blocked by incomplete work from earlier phases — they were designed to be independently deliverable.

No formal project management tool. Development tracked via git commits with descriptive messages. No Kanban board, no sprint planning, no standups. The solo developer is both the planner and the implementer.`;

A['6.1.2'] = `Team size and composition: Solo developer.

The entire system was built by one person in ~5 working days. All roles are combined: architect, developer, tester, documentation writer, release manager.

Why solo works: (1) The codebase is small (~3500 LOC). (2) The domain is well-understood (the developer IS the target user). (3) The architecture is simple (no distributed systems, no complex state management). (4) The test suite provides safety net for changes.

When to add team members: If the project grows beyond 10,000 LOC, or if multiple features need parallel development, or if the web UI becomes a significant application. Currently, none of these apply.

If the team grows: The recommended first hire would be a frontend developer (the web UI is the most likely area for growth) or a DevOps engineer (CI/CD, npm publishing, release automation). The architecture supports team development through clear module boundaries and comprehensive type definitions.`;

A['6.2.1'] = `Code review and quality practices:

Testing: Test-driven development for core functionality. Every feature has corresponding tests. The test suite (112+ tests) covers all public APIs. Tests run in <2 seconds.

Quality gates:
- TypeScript strict mode — no implicit any, no null bypass, no type assertions unless necessary
- All tests pass before any commit
- No linting violations (eslint not configured — type checking serves this purpose)
- No console.log in production code (test output only)

Code style:
- Consistent naming: camelCase for variables/functions, PascalCase for types/classes, kebab-case for files
- Functional over imperative where possible
- No nested callbacks — async/await throughout
- Early returns over nested ifs
- Types are explicit (no inference where clarity matters)

No formal code review (solo developer). The test suite serves as automated review — if the tests pass, the code is correct. The type system serves as structural review — if it compiles, the types are consistent.

No pair programming. No mob programming. No PR review process. These would add overhead without benefit for a solo-maintained project of this size.`;

A['6.2.2'] = `Technical debt management:

Approach: Opportportunistic — clean as you go, no formal tracking.

Debt prevention: (1) TypeScript strict mode prevents type debt. (2) Comprehensive tests prevent behavioral debt. (3) Small codebase limits structural debt. (4) Clear naming conventions prevent semantic debt.

Debt detection: Code review of own code (rare but occurs). Refactoring triggered by pain points — when adding a feature requires navigating complex code, that code gets simplified first.

Debt priority: High — anything that affects correctness or security. Medium — anything that affects maintainability. Low — anything that affects style or conventions.

Known debt: (1) No ESLint configuration — relies on TypeScript for linting. (2) No Prettier configuration — relies on manual formatting. (3) Some test files have repetitive setup that could be extracted to helpers. (4) The web UI inline JavaScript could be modularized.

Debt payoff: Each refactoring must produce measurable improvement (fewer lines, clearer names, better test coverage, or simpler logic). Refactoring for its own sake is avoided — the YAGNI principle applies.`;

A['6.3.1'] = `Communication and knowledge management:

Solo developer: All communication is with self (current and future). The primary communication channel is code comments and documentation.

Documentation as communication:
- README.md: How to install and use the system
- Type definitions: How the system's data model works
- Test files: How the system's behavior is verified
- Framework JSON: How the question taxonomy is structured

No meetings, no Slack, no formal communication channels. The documentation IS the communication — it's written for the future developer (who might be the same person in 6 months).

Knowledge capture: Every design decision is recorded in code (through naming and structure) or in comments (through "why" explanations). The framework JSON is the canonical source for the question taxonomy — understanding it is equivalent to understanding the system's purpose.`;

A['6.3.2'] = `Decision-making process: BDFL (Benevolent Dictator For Life) — one person makes final decisions.

Architectural decisions are made through: (1) Implement the simplest thing that works. (2) If it needs to change later, the type system makes refactoring safe. (3) The test suite ensures changes don't break existing behavior.

Decision examples:
- "Why no React for the web UI?" → Single HTML file is simpler and sufficient for the current scope.
- "Why no database?" → JSON files are simpler and sufficient for the data volume.
- "Why TypeScript strict mode?" → Catches errors at compile time, worth the stricter coding discipline.
- "Why vitest over jest?" → Better ESM support, faster execution.

Escalation: Not applicable — solo developer. If the project attracts contributors, a lightweight RFC process would be appropriate. Architecture Decision Records (ADRs) would be introduced for significant decisions.`;

// ═══ SERIES 7: OPERATIONAL / FUNCTIONAL ═══
A['7.1.1'] = `Deployment and release strategy:

CLI distribution: npm publish to the public registry. Package name: space-cli. Users install globally: "npm install -g space-cli". Updates via "npm update -g space-cli".

Web UI distribution: Git clone. Users clone the repo, run "npm install", then "node web/server.mjs". No separate distribution channel.

Release process:
1. Run full test suite ("npm test")
2. Verify build ("npm run build")
3. Update version in package.json
4. Commit with version tag
5. Run "npm publish"

The prepublishOnly hook runs build + test automatically before publish. If any test fails, publish is blocked.

Rollback: Users can install a specific version: "npm install -g space-cli@2.0.0". Git users can checkout a specific tag.

No canary releases, no staged rollouts, no feature flags for the CLI. The web UI supports feature flags through the SpaceConfig object but this is not exposed to end users.`;

A['7.1.2'] = `Environment and release management:

Environments: Two — development (local) and production (npm/global install).

Development: Clone the repo, run "npm install", use "npx space" or "node dist/cli/index.js". Source maps available. Hot reload not needed (CLI tool).

Production: "npm install -g space-cli". Compiled JavaScript in dist/. No source maps. No debug mode.

Configuration: Environment variables for optional overrides:
- SPACE_PROJECTS_DIR: Custom projects directory (optional, default: ~/.space/projects)
- OPENAI_API_KEY: OpenAI API key (optional, for LLM integration)
- ANTHROPIC_API_KEY: Anthropic API key (optional)
- GEMINI_API_KEY: Google Gemini API key (optional)
- MISTRAL_API_KEY: Mistral API key (optional)

No .env files, no dotenv, no configuration management library. Environment variables are the simplest configuration mechanism and work across all platforms.

No staging environment. The system is tested locally before publish. Users get the latest version directly.`;

A['7.2.1'] = `Logging and monitoring:

Current: Minimal — console output for CLI operations, no structured logging.

CLI output: Question text, answer confirmations, export progress, error messages. All to stdout/stderr. No log levels, no log files.

Web UI: Console.log for API requests and errors. No logging library.

If monitoring were needed (e.g., for a hosted version), the architecture supports it: the Engine emits events (session:created, answer:submitted, etc.) that could be forwarded to a logging system.

No metrics collection. No performance monitoring. No error tracking (Sentry, etc.). No analytics. The system is designed for local use where the developer IS the user and can observe behavior directly.

Health check: The web server responds to GET /api/health with { status: "ok", version: "2.0.0" }. This is sufficient for basic monitoring if needed.`;

A['7.2.2'] = `Configuration management:

Static configuration: SpaceConfig type (src/config/defaults.ts). Defines all configurable parameters with sensible defaults. Loaded from environment variables and command-line arguments.

Runtime configuration: Minimal by design. The system works with zero configuration — just run "space init" and "space run". Configuration is only needed for optional features (LLM providers, custom directories).

Configuration loading order: (1) Built-in defaults, (2) Environment variables override defaults, (3) Command-line arguments override environment variables.

No dynamic configuration: Configuration is loaded once at startup and doesn't change during execution. No hot-reloading, no dynamic configuration. This simplifies the system and prevents configuration drift.

No configuration files: All configuration is via environment variables or CLI arguments. No .env files, no config.json, no YAML config. This eliminates an entire category of configuration management problems (missing files, wrong paths, permission issues).`;

A['7.3.1'] = `Maintenance and lifecycle management:

Maintenance activities:
1. Dependency updates: Periodic (monthly). Run "npm audit", update vulnerable packages. The minimal dependency list makes this quick.
2. Node.js version support: Track Node.js LTS releases. Drop support for EOL versions (currently testing 18, 20, 22).
3. Bug fixes: As reported. The test suite makes regression testing automatic.
4. Feature additions: As needed. The modular architecture allows adding features without modifying existing code.

Upgrade policy: Non-breaking for MINOR and PATCH versions. Breaking changes only in MAJOR versions with migration guide.

Lifecycle: The system is actively maintained. No end-of-life planned. The framework JSON format is stable and unlikely to change significantly.`;

A['7.3.2'] = `Long-term stewardship:

Ownership: Original developer. Single point of responsibility for all decisions, maintenance, and support.

Sustainability: The system is self-contained (~3500 LOC) and has minimal dependencies. It can be maintained by one person indefinitely. No complex infrastructure to manage.

Future evolution:
- Short term (3 months): npm publishing, CI/CD, web UI improvements
- Medium term (6 months): LLM auto-fill, collaborative sessions, plugin system
- Long term (1 year): Team features, cloud hosting option, enterprise edition

Succession planning: The codebase is small enough that any competent TypeScript developer could take over. The architecture is documented, the types are explicit, and the tests provide safety net.

Open source: The system is MIT licensed. Community contributions are welcome but not expected at current scale. The project is designed to be self-sustaining with minimal external input.`;

// ── Generate all documents ──
let frameworkDoc = '# SPACE Framework \u2014 Complete Question Set\n\n';
frameworkDoc += '> Superb Prompt Automatic Creation Engine v2.0.0\n';
frameworkDoc += '> 7 Series \u00B7 25 Rounds \u00B7 67 Questions \u00B7 201 Multi-Choice Follow-ups\n\n';
frameworkDoc += '---\n\n';

let allQA = '# SPACE \u2014 Recursive Self Improvement\n\n';
allQA += '> Complete Question & Answer Specification\n';
allQA += '> Generated: ' + new Date().toISOString().split('T')[0] + '\n';
allQA += '> 67 Questions \u00B7 Extensive Technical Answers\n\n';
allQA += '---\n\n';

let questionNum = 0;
let answeredCount = 0;

for (let si = 0; si < SERIES_FILES.length; si++) {
  const seriesData = JSON.parse(readFileSync(
    join(__dirname, '..', 'prompt-framework', 'json', SERIES_FILES[si]), 'utf-8'
  ));

  const seriesName = SERIES_NAMES[si];
  const seriesDesc = SERIES_DESCRIPTIONS[si];

  frameworkDoc += '## Series ' + (si + 1) + ': ' + seriesName + '\n\n';
  frameworkDoc += '_' + seriesDesc + '_\n\n';

  allQA += '## Series ' + (si + 1) + ': ' + seriesName + '\n\n';
  allQA += '_' + seriesDesc + '_\n\n';

  for (const round of seriesData.rounds) {
    frameworkDoc += '### Round ' + round.round + ': ' + round.focus + '\n\n';
    allQA += '### Round ' + round.round + ': ' + round.focus + '\n\n';

    for (const q of round.open_ended) {
      questionNum++;
      const qid = q.id;

      frameworkDoc += '**Q ' + qid + '** \u2014 ' + q.text + '\n\n';
      frameworkDoc += 'Follow-up choices:\n';
      for (const c of q.follow_up_choices) {
        frameworkDoc += '- **' + c.id + '** \u2014 ' + c.text + '\n';
      }
      frameworkDoc += '\n';

      const answer = A[qid] || null;
      if (answer) answeredCount++;

      const answerText = answer || '[Answer for ' + qid + ' not yet written]';

      allQA += '---\n\n';
      allQA += '### Q ' + qid + ' \u2014 ' + round.focus + '\n\n';
      allQA += '**Question:** ' + q.text + '\n\n';
      allQA += '**Follow-up choices:**\n';
      for (const c of q.follow_up_choices) {
        allQA += '- ' + c.id + ': ' + c.text + '\n';
      }
      allQA += '\n**Answer:**\n\n' + answerText + '\n\n';

      // Write individual answer file
      const safeId = qid.replace(/\./g, '-');
      const filename = safeId + '.md';
      const filepath = join(ANSWERS_DIR, filename);

      let answerContent = '# Q ' + qid + ' \u2014 ' + round.focus + '\n\n';
      answerContent += '**Series:** ' + (si + 1) + ' \u2014 ' + seriesName + '\n\n';
      answerContent += '**Question:** ' + q.text + '\n\n';
      answerContent += '**Follow-up choices:**\n\n';
      for (const c of q.follow_up_choices) {
        answerContent += '- **' + c.id + '** \u2014 ' + c.text + '\n';
      }
      answerContent += '\n---\n\n';
      answerContent += '## Answer\n\n' + answerText + '\n';

      writeFileSync(filepath, answerContent);
    }
  }
}

frameworkDoc += '---\n\n*Total: ' + questionNum + ' questions across ' + SERIES_NAMES.length + ' series*\n';
allQA += '---\n\n*End of Specification \u2014 ' + questionNum + ' questions with extensive technical answers*\n';

writeFileSync(join(BASE, 'framework.md'), frameworkDoc);
writeFileSync(join(BASE, 'rsi-complete-qa.md'), allQA);

console.log('Framework document: auto/rsi/framework.md (' + frameworkDoc.length + ' bytes)');
console.log('Complete Q&A: auto/rsi/rsi-complete-qa.md (' + allQA.length + ' bytes)');
console.log('Individual answers: ' + questionNum + ' files in auto/rsi/answers/');
console.log('Answers populated: ' + answeredCount + '/' + questionNum);
console.log('Generation complete!');
