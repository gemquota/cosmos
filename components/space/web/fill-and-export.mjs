import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { createSpace } from '../dist/engine/core.js';
import { exportSession } from '../dist/export/index.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_NAME = 'space-complete';

// ── All 67 answers about SPACE ──
const A = {
  // ═══ SERIES 1: Conceptual Depth (6) ═══
  '1.1.1': ['SPACE (Superb Prompt Automatic Creation Engine) is a programmable specification engine that transforms structured elicitation probes into development specifications. It sits at the intersection of prompt engineering, software specification, and developer tooling. Core concerns: transforming vague project ideas into concrete specs through progressive deepening across ontological, semantic, procedural, technical, and operational dimensions. Sub-disciplines include structured elicitation, dependency-aware question routing, artifact extraction, and multi-format export.', '1.1.1.b'],
  '1.1.2': ['The primary audience is software developers and technical leads building LLM-powered applications or complex systems who need structured specifications. Secondary audience includes product managers and architects who need to formalize requirements. They understand TypeScript/Node.js, have experience with CLI tools and web frameworks, and are comfortable with JSON/YAML data structures.', '1.1.2.a'],
  '1.2.1': ['Assumed: understanding of CLI tools, npm/Node.js ecosystem, basic TypeScript, JSON/YAML formats, REST API concepts, and prompt engineering basics. Must explain from scratch: the specific 7-series progressive elicitation methodology, how dependency chains between series work, how artifacts accumulate across rounds, and how the 326 probes produce a coherent specification.', '1.2.1.b'],
  '1.2.2': ['Mixed approach — present the framework architecture with clear diagrams showing the series dependency graph and question flow, then ground each concept with concrete code examples from the TypeScript engine. For instance, show how a question flows through the router, gets answered, produces an artifact, and feeds into downstream series.', '1.2.2.b'],
  '1.3.1': ['Use standard software engineering terminology (session, artifact, framework, series, round) consistently. Avoid anthropomorphizing the tool — it "elicits" and "generates" rather than "understands." Use SPACE-specific terms with definitions: probe (a single elicitation question), artifact (extracted data from answers), series (a themed group of rounds), round (a batch of related questions within a series).', '1.3.1.a'],
  '1.3.2': ['Progressive — start with the simple concept of asking questions to generate specs, then layer in the dependency system, artifact accumulation, multi-format export, and finally the intelligence layer (analytics, contradiction detection, recommendations). Each layer builds on the previous.', '1.3.2.b'],

  // ═══ SERIES 2: Ontological Characteristics (15) ═══
  '2.1.1': ['Core entities: Framework (the 326-probe question set with dependency graph), Session (a user interaction instance tracking progress and answers), Project (a named container for sessions), Artifact (extracted structured data from answers), Series (a themed group of 3-5 rounds), Round (a batch of 2 open-ended questions with multi-choice follow-ups), Question (an open-ended probe with clarifying follow-ups), Export (generated specification documents in various formats), User (the human answering questions), Engine (the orchestration layer managing question routing and state).', '2.1.1.b'],
  '2.1.2': ['Each entity has 3-5 key attributes. Framework: version, total_series, total_rounds, dependency_graph. Session: id, project_id, status, answers map, progress state, artifacts dict. Project: id, name, description, created_at, sessions list. Artifact: value, source_question_id, confidence, derived_from. Series: id, name, depends_on, provides, rounds. Question: id, text, follow_up_choices. Export: content, filename, mime_type.', '2.1.2.b'],
  '2.1.3': ['Three broad categories: (1) Structural entities (Framework, Series, Round, Question) define the probe taxonomy. (2) Runtime entities (Session, Engine, User) manage execution. (3) Output entities (Artifact, Export) represent derived data. These map naturally to the architecture — structural defines what gets asked, runtime manages asking, output captures results.', '2.1.3.b'],
  '2.2.1': ['Core: Framework, Session, Question, Artifact, Engine. Peripheral: Project (convenience wrapper), User (implicit), Export (derived from Session + Artifacts). The system could function with just Framework + Session + Engine + Questions, but Projects provide organization and Exports provide delivery.', '2.2.1.b'],
  '2.2.2': ['Moderate granularity — key specializations become distinct entities. Questions are fine-grained (each of 326 is unique), but Rounds and Series are moderate groupings. Artifacts are fine-grained per-question but aggregate into a dictionary. This balance keeps the entity count manageable while preserving the granularity needed for the 326-probe structure.', '2.2.2.b'],
  '2.2.3': ['Shared attributes grouped by category — entities in same category share a profile. All runtime entities share a lifecycle pattern (create → active → complete). All structural entities share a naming convention (dot-separated IDs like 2.3.1). Artifacts share a common interface (value + metadata) but their content varies by source series.', '2.2.3.b'],
  '2.3.1': ['Tightly bounded — scope is narrow and well-defined. SPACE generates specifications; it does not implement them, deploy them, or manage projects after generation. The boundary is: input = user answers to 326 probes, output = structured specification documents. Everything inside this boundary is in scope; everything outside is explicitly out.', '2.3.1.a'],
  '2.3.2': ['3 external actors: (1) The human user answering questions — provides the domain knowledge. (2) The LLM (optional) — can auto-answer or refine questions, but the system works without it. (3) The file system / browser storage — persists sessions and exports. The system is deliberately designed to work without external services.', '2.3.2.b'],
  '2.3.3': ['Stateful lifecycle with versioned artifacts. Sessions: created → in_progress → completed. Questions within sessions: locked → available → answered. Artifacts: extracted → accumulated → exported. The system also supports snapshot/resume, so sessions can be paused and resumed with full state preservation.', '2.3.3.b'],
  '2.4.1': ['No major gaps — the entity set is comprehensive for the current scope. One potential addition: a "Configuration" entity to formalize runtime settings (LLM provider, export formats, quality thresholds). Currently these are embedded in the Engine config rather than being first-class entities.', '2.4.1.a'],
  '2.4.2': ['No merges or splits needed. The entity boundaries are clean. One reclassification candidate: "User" could be split into "Respondent" (answers questions) and "Consumer" (reads exports), but this adds complexity without benefit at current scale.', '2.4.2.a'],
  '2.4.3': ['Key constraints: (1) Framework is immutable after loading — no runtime modifications to the question set. (2) Session answers are append-only during active session — editing allowed before completion, not after. (3) Artifacts are derived, not stored — recomputed from answers on every access. (4) Series dependencies are strict — cannot answer Series N before all dependencies are complete.', '2.4.3.b'],
  '2.5.1': ['Edge cases: (1) Empty project with no sessions — handled gracefully with "no sessions" message. (2) Corrupted session JSON — validation on load, fallback to fresh session. (3) Missing framework files — fallback to bundled defaults. (4) Concurrent sessions in same project — allowed but not coordinated. (5) Very long answers (>10KB) — accepted but may slow export generation.', '2.5.1.b'],
  '2.5.2': ['Entities compose hierarchically: Framework contains Series contains Rounds contains Questions. Sessions contain Answers (keyed by question ID) and Artifacts (keyed by artifact name). Projects contain Sessions. Exports compose from Session + Artifacts + Framework. The dependency graph creates cross-series composition where later Series consume Artifacts from earlier Series.', '2.5.2.b'],
  '2.5.3': ['Cardinality: Framework 1:N Series, Series 1:N Rounds, Round 1:N Questions (always 2). Project 1:N Sessions. Session N:M Questions (via answers map). Session 1:N Artifacts. Session 1:N Exports. Series N:M Series (via dependency graph). The dominant pattern is one-to-many containment with the answers map as the many-to-many junction.', '2.5.3.b'],

  // ═══ SERIES 3: Semantic Relationships (8) ═══
  '3.1.1': ['Primary associations: Framework CONTAINS Series (1:many), Series CONTAINS Rounds (1:many), Round CONTAINS Questions (1:many), Session ANSWERS Questions (many:many via answers map), Session EXTRACTS Artifacts (1:many), Project OWNS Sessions (1:many), Engine ORCHESTRATES Sessions (1:many), Export PRODUCES_FROM Session+Artifacts (many:1). The dependency graph defines which Series consumes artifacts from which other Series.', '3.1.1.b'],
  '3.1.2': ['Composition dominates — most relationships are whole-part (Framework contains Series contains Rounds contains Questions). The exception is the dependency graph between Series, which is a directed acyclic graph of artifact consumption. The answers map in Session is an association table linking Questions to user responses.', '3.1.2.b'],
  '3.2.1': ['Hierarchical containment with a flat dependency layer. The structural hierarchy is: Framework → Series → Round → Question. This is strict containment. The dependency graph is flat — Series reference each other by ID, not by nesting. Artifacts float across this hierarchy, extracted from Questions but consumed by downstream Series.', '3.2.1.a'],
  '3.2.2': ['Composition primarily — Artifacts are composed into the Session state, not inherited. The exception is the Export hierarchy: JSON, Markdown, YAML, HTML, and Prompt exports all share a common interface (content + filename + mime_type) but implement different serialization strategies. This is strategy pattern, not inheritance.', '3.2.2.a'],
  '3.3.1': ['Sequential causation with parallel-reads. Answering Question 1.1.1 causes its artifact to become available to downstream Series. However, within a Round, both Questions can be answered in any order. The dependency graph is a DAG — answering earlier Series enables later Series, but there are no cycles.', '3.3.1.a'],
  '3.3.2': ['The dependency chains form a DAG with 7 nodes (Series) and approximately 10 edges. The critical path runs: Series 1 → Series 2 → Series 3 → Series 4 → Series 5 → Series 6 → Series 7. Branching occurs where Series 5 depends on both Series 1 and Series 4, creating a merge point.', '3.3.2.b'],
  '3.4.1': ['Mostly immutable — once an answer is recorded, it is never modified (only appended to). The exception is the "edit" capability where users can revise answers before session completion. Artifacts are recomputed from answers, so editing an answer automatically updates its artifact. Session status transitions are one-way (created → in_progress → completed).', '3.4.1.b'],
  '3.4.2': ['Two junction entities mediate the primary relationships: (1) The answers map in Session — a dictionary linking question_id to AnswerEntry, carrying the open-ended text, multi-choice selection, timestamps, and quality scores. (2) The artifacts dictionary — linking artifact keys to ArtifactValue objects with source provenance and confidence scores.', '3.4.2.b'],

  // ═══ SERIES 4: Procedural Breadth (6) ═══
  '4.1.1': ['The primary procedure is the elicitation session: user creates project → starts session → answers questions series by series → system routes questions respecting dependencies → extracts artifacts from answers → generates exports. Secondary procedures include: session save/resume, artifact accumulation, progress tracking, and export generation.', '4.1.1.a'],
  '4.1.2': ['The session procedure has 5 major phases: (1) Initialization — create project, load framework, validate structure. (2) Elicitation — answer 67 open-ended questions across 25 rounds, each with 3 multi-choice follow-ups. (3) Extraction — accumulate 66 artifacts from answers via mapping registry. (4) Validation — check for contradictions, completeness gaps, quality issues. (5) Export — generate specification documents in multiple formats.', '4.1.2.b'],
  '4.2.1': ['The elicitation flow has 8-10 steps per question: router selects next question → displays question text and follow-up choices → user types open-ended answer → user selects classification → system validates answer → system records answer → system extracts artifacts → system checks round completion → system checks series completion → system advances to next question.', '4.2.1.b'],
  '4.2.2': ['Each step has 2-3 sub-actions. For example, "display question" involves: checking dependency gates are met, formatting the question with series context and round focus, showing the progress bar and series indicator. "Submit answer" involves: validating non-empty text, recording timestamp, updating answers map, recomputing artifacts, checking if round is complete.', '4.2.2.a'],
  '4.3.1': ['Three decision points: (1) Question routing — which question to show next, governed by the dependency graph and completion state. (2) Answer validation — whether the answer meets quality thresholds (non-empty text, valid choice selection). (3) Completion detection — whether a round, series, or session is complete based on all questions answered.', '4.3.1.a'],
  '4.3.2': ['The main branching path is: if dependencies met → show question, else → skip to next available. Secondary branch: if answer valid → record and advance, else → re-prompt. Tertiary branch: if round complete → check series, if series complete → check session, if session complete → generate exports.', '4.3.2.b'],

  // ═══ SERIES 5: Technical Specifications (20) ═══
  '5.1.1': ['TypeScript/Node.js for the engine, CLI, and storage. Python for the web server backend. Single HTML file with Tailwind CSS for the web UI. The engine uses no external runtime dependencies beyond Node.js built-ins — the entire CLI compiles to a single executable via npm link.', '5.1.1.b'],
  '5.1.2': ['Minimum: Node.js 18+, 512MB RAM, 100MB disk. Recommended: Node.js 20+, 2GB RAM, 1GB disk. The system is lightweight — the entire codebase is ~3500 lines of TypeScript. The web UI is a single 36KB HTML file. Storage grows linearly with sessions (~10KB per session).', '5.1.2.a'],
  '5.1.3': ['Offline-first — the core system requires zero network access. LLM integration is optional and requires internet for API calls. The web UI is served locally. No bandwidth or latency requirements for core functionality. The system is designed for developers working on their local machine.', '5.1.3.a'],
  '5.1.4': ['JSON files on the local filesystem — one .space.json per project, one state.json per session, export files in the exports directory. SQLite adapter exists for future scaling but is not currently integrated. No databases, object storage, or caching infrastructure needed.', '5.1.4.a'],
  '5.1.5': ['Local development only — no cloud, no on-premise servers, no hybrid. The system runs on the developers machine. The web server binds to localhost. The CLI is installed globally via npm. No containerization, no orchestration, no deployment pipeline for the tool itself.', '5.1.5.a'],
  '5.2.1': ['TypeScript for all business logic (engine, CLI, LLM providers, export). Python for the lightweight web server. Single HTML file with Tailwind CSS via CDN for the web UI. No frontend build step — the HTML file is served directly. The TypeScript compiles to ES2022 JavaScript.', '5.2.1.b'],
  '5.2.2': ['Cross-platform — runs on macOS, Linux, and Windows. Tested on Node.js 18, 20, and 22. The CLI uses platform-independent path handling. The web UI works in any modern browser (Chrome, Firefox, Safari, Edge). No platform-specific code.', '5.2.2.b'],
  '5.2.3': ['Runtime dependencies: commander (CLI framework), chalk (terminal colors), inquirer (interactive prompts), ora (spinners), js-yaml (YAML), sql.js (SQLite). Dev dependencies: vitest (testing), tsx (dev runner), typescript (compiler). LLM providers: openai, anthropic SDKs (optional). No databases, no message queues, no external services required.', '5.2.3.a'],
  '5.2.4': ['Semantic versioning (currently v2.1.0). The framework JSON format is versioned separately (v1 → v2 migration built in). Backward compatibility maintained — old session files load in new versions. Breaking changes require a major version bump.', '5.2.4.a'],
  '5.2.5': ['npm for package management and distribution. TypeScript compiler (tsc) for build. Vitest for testing. No CI/CD pipeline configured yet — builds are manual. The prepublishOnly hook runs build + test before npm publish. No Docker, no Kubernetes, no cloud deployment.', '5.2.5.a'],
  '5.3.1': ['Single-user interactive tool — no throughput requirements. Session creation: <100ms. Question routing: <10ms. Answer submission: <50ms. Artifact extraction: <20ms. Export generation: <500ms. All operations complete in under a second. No concurrency requirements — the system handles one user at a time.', '5.3.1.a'],
  '5.3.2': ['Current scale: 326 questions, ~66 artifacts per session, ~10KB per session state file. A single project might have 5-10 sessions. Total storage per project: ~500KB. The system is designed for hundreds of projects, not millions. No archival strategy needed at current scale.', '5.3.2.a'],
  '5.3.3': ['Not applicable — this is a local development tool, not a production service. No SLA, no uptime requirement. The system works offline and completes all operations in under a second. Data durability is handled by file system + optional git versioning.', '5.3.3.a'],
  '5.3.4': ['Single-process, single-user architecture. No horizontal scaling needed. Vertical scaling is irrelevant — the system is lightweight. The web server handles one request at a time, which is fine for a development tool. No load balancing, no caching, no CDN.', '5.3.4.a'],
  '5.3.5': ['No specific security requirements beyond standard development tool practices. API keys for LLM providers are stored in environment variables. Session data is local JSON files — no encryption needed for a development tool. No authentication, no authorization, no audit logging.', '5.3.5.a'],
  '5.4.1': ['5 LLM providers via unified interface: OpenAI (GPT-4), Anthropic (Claude), Google Gemini, Mistral, Ollama (local). Each implements the same LLMProvider interface. File system for storage. npm for distribution. The system works without any LLM — the template provider generates deterministic responses for offline use.', '5.4.1.b'],
  '5.4.2': ['File system API for session persistence (JSON read/write). LLM providers use their native REST APIs via SDK packages. The web server uses HTTP REST endpoints. No gRPC, no WebSocket, no message queues. All communication is synchronous and simple.', '5.4.2.a'],
  '5.4.3': ['Phase 1 (done): Core engine + CLI. Phase 2 (done): Web UI. Phase 3 (done): LLM providers. Phase 4 (done): Export pipeline. Phase 5 (done): Persistence + snapshots. Phase 6 (done): Intelligence layer. Phase 7 (current): npm publishing + documentation. The system has been developed incrementally over ~4 weeks.', '5.4.3.b'],
  '5.4.4': ['Test-driven development with 142 tests across 13 test files. Each phase has its own test file. Integration tests for full session flows. Snapshot tests for export formatters. No staging environment needed for a local tool. Manual testing for the web UI.', '5.4.4.b'],
  '5.4.5': ['npm package with README, LICENSE, and TypeScript declarations. CLI help text for every command. Inline JSDoc for all public APIs. Meta directory with specs, dev plans, and audit reports. The web UI is self-documenting — the dashboard shows the framework structure.', '5.4.5.b'],

  // ═══ SERIES 6: Development Methodologies (6) ═══
  '6.1.1': ['Iterative development in 7 phases, each adding a distinct capability layer. Phase 0: Foundation (schema, loader, CLI). Phase 1: Execution engine (session lifecycle, routing). Phase 2: LLM integration (providers, refinement). Phase 3: Export pipeline (6 formats). Phase 4: Interactive UI (web + terminal). Phase 5: Persistence (filesystem, snapshots). Phase 6: Intelligence (analytics, contradictions). Each phase is independently testable.', '6.1.1.b'],
  '6.1.2': ['Solo developer — one person handles all roles (architecture, implementation, testing, documentation). The project is small enough (~3500 LOC) for one person to maintain full context. No team coordination overhead. Decisions are fast and informal.', '6.1.2.a'],
  '6.2.1': ['TypeScript strict mode for all source code. Every function has clear input/output types. 142 tests across 13 test files. Snapshot tests for export formatters. Integration tests for full session flows. No code review process (solo developer). No linter configured yet — TypeScript compiler catches type errors.', '6.2.1.b'],
  '6.2.2': ['Boy scout rule — leave code cleaner than you found it. Refactor when adding new features if existing code makes the feature harder. No dedicated refactoring phases. Technical debt is tracked informally. The main debt: web UI lacks automated tests, SQLite adapter not integrated.', '6.2.2.a'],
  '6.3.1': ['Solo developer, so communication is self-documentation. Architecture decisions recorded in meta/specs/ as markdown. Code is the primary documentation — TypeScript types are self-describing. README files explain usage. No meetings, no Slack, no formal communication channels.', '6.3.1.a'],
  '6.3.2': ['BDFL — one person makes all decisions. No RFC process, no ADR reviews. Architecture decisions are made quickly and documented after implementation. The framework JSON format is the single source of truth for the question taxonomy. Changes to the framework require updating both the JSON files and the TypeScript types.', '6.3.2.a'],

  // ═══ SERIES 7: Operational / Functional (6) ═══
  '7.1.1': ['npm publish for distribution — the package is published to the public npm registry as space-cli. Users install globally with npm install -g space-cli and access the space command. The web UI is bundled but not separately distributed — users clone the repo and run the server locally.', '7.1.1.b'],
  '7.1.2': ['npm for distribution, GitHub for source. No Docker images — the system is a Node.js CLI tool that runs anywhere Node.js runs. The web UI is zero-dependency (single HTML file + Python server). No cloud deployment, no container registry, no package manager beyond npm.', '7.1.2.b'],
  '7.2.1': ['Not applicable — this is a development tool, not a production service. No logging infrastructure, no monitoring, no alerting. The closest thing to observability is the session progress tracking and artifact quality scores, which help users understand their specification completeness.', '7.2.1.a'],
  '7.2.2': ['Configuration via CLI flags and environment variables. No feature flags, no runtime configuration, no remote config. The framework JSON is the primary configuration — it defines the question taxonomy. LLM provider settings are environment variables (API keys). The system is designed for simplicity — minimal configuration.', '7.2.2.a'],
  '7.3.1': ['Solo developer handles everything — no maintenance team, no support process. Issues tracked via GitHub. No SLA, no response time requirements. The system is open source and self-service. Updates are released as npm package versions with changelogs.', '7.3.1.a'],
  '7.3.2': ['The system is actively developed and maintained by the original author. Updates are released as npm package versions. Breaking changes are avoided through semantic versioning. The framework format is versioned separately from the engine code. Long-term: the system becomes a stable tool with occasional feature additions.', '7.3.2.b'],
};

// ── Load framework and create session ──
const space = createSpace();
const session = space.startSession(PROJECT_NAME);

console.log(`Session: ${session.session.id}`);
console.log(`Questions to answer: ${Object.keys(A).length}`);

// ── Answer all questions ──
let answered = 0;
let failed = [];
for (const [qid, [text, choice]] of Object.entries(A)) {
  const result = space.submitAnswer(session.session.id, qid, text, choice);
  if (result.accepted) {
    answered++;
    if (result.round_completed) process.stdout.write('.');
    if (result.series_completed) process.stdout.write(` [S${qid.split('.')[0]}✓]`);
  } else {
    failed.push(qid);
    console.error(`\nFAILED: ${qid}`);
  }
}

console.log(`\n\nAnswered: ${answered}/67 questions`);
if (failed.length) console.log(`Failed: ${failed.join(', ')}`);

// ── Get final state ──
const progress = space.getProgress(session.session.id);
const artifacts = space.getArtifacts(session.session.id);
console.log(`Completion: ${progress?.overall?.completion_pct || 0}%`);
console.log(`Artifacts: ${Object.keys(artifacts).length}`);

// ── Save session ──
const sessionJson = space.saveSession(session.session.id);
const exportDir = join(dirname(__dirname), 'exports', PROJECT_NAME);
mkdirSync(exportDir, { recursive: true });
writeFileSync(join(exportDir, 'session.json'), sessionJson);
console.log(`\nSession saved: exports/${PROJECT_NAME}/session.json`);

// ── Generate exports ──
const sessionState = JSON.parse(sessionJson);
const formats = ['json', 'markdown', 'yaml', 'html', 'prompt'];

console.log('\nGenerating exports...');
for (const format of formats) {
  const result = exportSession(sessionState, artifacts, space.framework, format, PROJECT_NAME);
  const filePath = join(exportDir, result.filename);
  writeFileSync(filePath, result.content);
  console.log(`  ${format}: ${result.filename} (${(result.content.length / 1024).toFixed(1)} KB)`);
}

console.log(`\nAll exports saved to exports/${PROJECT_NAME}/`);
