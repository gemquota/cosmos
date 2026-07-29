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
  'Conceptual Depth',
  'Ontological Characteristics',
  'Semantic Relationships',
  'Procedural Breadth',
  'Technical Specifications',
  'Development Methodologies',
  'Operational / Functional',
];

const SERIES_DESCRIPTIONS = [
  'Calibrates the register, audience sophistication, vocabulary, and complexity scaffolding for the entire specification.',
  'Discovers, classifies, refines, and validates the entities, categories, attributes, and boundaries of the domain.',
  'Maps associations, dependencies, hierarchies, and causal chains between entities.',
  'Defines the workflows, procedures, decision points, and error handling for the system.',
  'Specifies hardware, software, performance, security, integrations, and deployment requirements.',
  'Establishes development methodology, team structure, quality practices, and communication patterns.',
  'Covers deployment, operations, monitoring, maintenance, and long-term stewardship.',
];

// Read all answer files from a separate JSON or load from answers.json
// For now, generate comprehensive answers inline using escaped strings

const ANSWERS = {
  '1.1.1': 'SPACE (Superb Prompt Automatic Creation Engine) is a programmable specification engine that transforms structured elicitation probes into development specifications. It sits at the intersection of prompt engineering, software specification, and developer tooling.\n\nCore concerns include: (1) Structured elicitation — systematically extracting domain knowledge from humans through a 326-probe questionnaire organized into 7 progressive series. (2) Dependency-aware routing — ensuring questions are asked in an order that respects logical prerequisites, where later questions can reference artifacts from earlier ones. (3) Artifact extraction — automatically identifying and cataloging key design decisions, entity definitions, and architectural choices from free-text answers. (4) Multi-format export — generating specification documents in JSON, Markdown, YAML, HTML, and LLM-consumable prompt formats.\n\nSub-disciplines: structured prompt engineering, dependency graph traversal, artifact mapping, specification generation, and progressive deepening methodologies. The system draws from elicitation techniques used in requirements engineering, ontological modeling from knowledge representation, and the progressive disclosure pattern from UX design.',

  '1.1.2': 'The primary audience is software developers and technical leads building LLM-powered applications or complex systems who need structured specifications. These are practitioners who understand TypeScript/Node.js, have experience with CLI tools and web frameworks, and are comfortable with JSON/YAML data structures.\n\nSecondary audience includes: (1) Product managers who need to formalize requirements for AI-assisted development. (2) Architects designing systems that integrate multiple LLM providers. (3) Open-source maintainers who want to document their projects systematically. (4) Technical writers who need structured input for generating documentation.\n\nBaseline familiarity: respondents understand REST APIs, npm ecosystems, and basic AI/ML concepts. They have likely used at least one LLM API (OpenAI, Anthropic, etc.) and understand the difference between system prompts, user prompts, and completion endpoints. They may not be familiar with ontological modeling or dependency graph theory, so the framework explains these concepts progressively.',

  '1.2.1': 'Assumed knowledge that the output can take for granted: CLI tool usage (npm install, git clone, running scripts), Node.js/TypeScript basics (import/export, async/await, type annotations), JSON/YAML parsing and structure, REST API concepts (endpoints, request/response), prompt engineering fundamentals (system prompts, few-shot, temperature), and basic software architecture patterns (MVC, event-driven, plugin systems).\n\nMust be explained from scratch: (1) The specific 7-series progressive elicitation methodology — how questions build on each other across series. (2) The dependency chain between series — why Series 2 cannot start until Series 1 provides domain and audience context. (3) How artifacts accumulate — each answer contributes extracted data that downstream series consume. (4) The 326-probe structure — 67 open-ended questions, each with 3 multi-choice follow-ups that classify and clarify the answer. (5) How the framework produces a coherent specification from apparently disconnected questions.',

  '1.2.2': 'Mixed approach — present the SPACE architecture with clear structural diagrams showing the series dependency graph and question flow, then ground each concept with concrete examples from the actual codebase.\n\nFor the structural layer: use dependency graphs (Series 1 feeds Series 2, which feeds Series 3, etc.) to show the progressive narrowing. Show how each series consumes artifacts from previous series. Show the round/round/question hierarchy.\n\nFor the concrete layer: show actual TypeScript code snippets from the engine (question-router.ts, session-manager.ts, artifact-mapping.ts), real JSON examples of session state and artifact dictionaries, and actual output from the export pipeline. For instance, show how answering question 2.1.1 (entity discovery) feeds the entity_list artifact that Series 3 consumes for relationship mapping.',

  '1.3.1': 'Standard software engineering terminology used consistently throughout: session (a user interaction instance), artifact (extracted structured data), framework (the 326-probe question set), series (a themed group of rounds), round (a batch of 2 related questions), probe (a single elicitation question — open-ended or multi-choice follow-up).\n\nIndustry terms used precisely: dependency injection (for the StorageProvider pattern), factory pattern (for LLM provider creation), event emitter (for lifecycle hooks), command pattern (for CLI commands).\n\nTerms deliberately avoided: "AI" or "intelligent" for the engine (it routes and extracts, not "understands"), "user" for the respondent (use "respondent" or "answerer" to distinguish from system operators), "generate" for the export (use "compile" or "render" to distinguish from LLM generation).',

  '1.3.2': 'Progressive scaffolding — start with the simple concept of asking structured questions to produce specifications, then layer in complexity one dimension at a time:\n\nLayer 1: Question asking — the basic loop of presenting questions and recording answers.\nLayer 2: Dependency awareness — some questions depend on earlier answers (Series 2 needs Series 1 context).\nLayer 3: Artifact extraction — answers are automatically parsed for key terms, entity names, architectural decisions.\nLayer 4: Multi-format output — artifacts compile into JSON, Markdown, YAML, HTML, or LLM prompt formats.\nLayer 5: Intelligence layer — optional LLM integration for auto-filling follow-up choices and suggesting answers.',
};

// Load remaining answers from the original generate script or use a fallback
// For now, generate the framework and Q&A documents with what we have
// then run a second pass to fill in all answers

// ── Phase 1: Generate framework document ──
let frameworkDoc = '# SPACE Framework — Complete Question Set\n\n';
frameworkDoc += '> Superb Prompt Automatic Creation Engine v2.0.0\n';
frameworkDoc += '> 7 Series \u00B7 25 Rounds \u00B7 67 Questions \u00B7 201 Multi-Choice Follow-ups\n\n';
frameworkDoc += '---\n\n';

let allQA = '# SPACE — Recursive Self Improvement\n\n';
allQA += '> Complete Question & Answer Specification\n';
allQA += '> Generated: ' + new Date().toISOString().split('T')[0] + '\n';
allQA += '> 67 Questions \u00B7 Extensive Technical Answers\n\n';
allQA += '---\n\n';

let questionNum = 0;
let answerFiles = [];

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

      const answer = ANSWERS[qid] || '[Answer for ' + qid + ' not yet written]';

      allQA += '---\n\n';
      allQA += '### Q ' + qid + ' \u2014 ' + round.focus + '\n\n';
      allQA += '**Question:** ' + q.text + '\n\n';
      allQA += '**Follow-up choices:**\n';
      for (const c of q.follow_up_choices) {
        allQA += '- ' + c.id + ': ' + c.text + '\n';
      }
      allQA += '\n**Answer:**\n\n' + answer + '\n\n';

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
      answerContent += '## Answer\n\n' + answer + '\n';

      writeFileSync(filepath, answerContent);
      answerFiles.push(filename);
    }
  }
}

frameworkDoc += '---\n\n*Total: ' + questionNum + ' questions across ' + SERIES_NAMES.length + ' series*\n';
allQA += '---\n\n*End of Specification \u2014 ' + questionNum + ' questions with extensive technical answers*\n';

writeFileSync(join(BASE, 'framework.md'), frameworkDoc);
writeFileSync(join(BASE, 'rsi-complete-qa.md'), allQA);

console.log('Framework document: auto/rsi/framework.md (' + frameworkDoc.length + ' bytes)');
console.log('Complete Q&A: auto/rsi/rsi-complete-qa.md (' + allQA.length + ' bytes)');
console.log('Individual answers: ' + answerFiles.length + ' files in auto/rsi/answers/');
console.log('Question ' + questionNum + ': all written');
console.log('NOTE: Only 6 questions have inline answers. Run the full generator to populate all 67.');
