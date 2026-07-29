---
type: "synthesis"
title: "mykb: Personal LLM Wiki — Analysis & Enrichment Theory"
description: "Comprehensive analysis of the mykb personalized knowledge wiki system, its architecture, extraction pipeline, and strategies for active curation."
tags: ["mykb", "synthesis", "theory", "knowledge-graph", "enrichment", "curation", "personal-wiki"]
timestamp: "2026-07-19"
resource: ""
---


## Mykb Analysis

# mykb: Personal LLM Wiki — Analysis & Enrichment Theory

> *A constantly-growing knowledge graph extracted from every Codex agent session, automatically curated and organized into a multi-tier hierarchy.*

## I. What Is mykb?

mykb ("my knowledge base") is a **personalized, auto-extracted knowledge wiki** that captures everything a developer learns while working with AI coding agents. Every session with Codex produces hundreds of data points: technologies referenced, patterns applied, decisions made, errors encountered, and solutions created. Rather than losing this context when the session ends, mykb preserves it as a structured, queryable knowledge graph.

### The Core Insight

> **Every agent interaction is a learning opportunity.** The LLM doesn't just write code — it reveals the developer's technology stack, decision patterns, problem-solving approaches, and evolving preferences. mykb captures and structures this latent knowledge.

### Why Not a Traditional Wiki?

Traditional wikis require manual effort: you stop working, write a note, format it, link it. This doesn't scale. mykb's key innovation is **zero-effort capture**:

1. **Passive extraction**: The LLM wiki daemon hooks into Codex's PostToolUse and Stop events
2. **Automatic structuring**: Session turns are parsed into entities, decisions, facts, and tags
3. **Progressive enrichment**: Curated content overwrites stubs as the knowledge base matures
4. **Continuous curation**: Validation and linting run on a schedule, maintaining quality

## II. Architecture

### Pipeline

```
Agent Session ──► PostToolUse Hook ──► Buffer (.ndjson) ──► Daemon ──► Extraction ──► OKF Concepts
                        │                                                      │
                        ▼                                                      ▼
                   Session Stop                                           Entity, Decision,
                   Signal File                                             Fact Extraction
                                                                                 │
                                                                                 ▼
                                                                        Curation Cycle
                                                                        (validate, lint,
                                                                         reclassify)
```

### Components

| Component | Path | Function |
|-----------|------|----------|
| **Session hook** | `hooks/post-tool-use.js` | Captures each agent turn to session buffer |
| **Stop hook** | `hooks/session-stop.js` | Signals session end to trigger extraction |
| **Daemon** | `.wiki-daemon/daemon.js` | Background processor managing extraction |
| **Extractor** | `.wiki-daemon/extract.js` | Heuristic NLP: entities, facts, decisions |
| **Store** | `.wiki-daemon/store.js` | Writes extracted knowledge as OKF concepts |
| **Curator** | `.wiki-daemon/curate-wiki.py` | Enriches stub entities with learned content |
| **Consolidator** | `.wiki-daemon/consolidate.py` | Deduplicates and fuzzy-clusters entities |
| **Classifier** | `.wiki-daemon/curate.py` | Multi-tier hierarchy classification |
| **Viewer** | `.wiki-daemon/viewer.py` | Lightweight HTTP concept browser |
| **Graph server** | `okf server` | Interactive Cytoscape.js knowledge graph |

### Data Flow

1. **Session capture**: Each agent turn is buffered as JSONL with tool name, input, and output
2. **Entity extraction**: Regex patterns identify capitalized phrases, tech keywords, code references
3. **Tag association**: Co-occurrence analysis links entities to sessions
4. **Knowledge writing**: Extracted entities become OKF concept files with YAML frontmatter
5. **Cross-linking**: Tag-based entity↔entity relationships are computed
6. **Hierarchy classification**: Entities are assigned to domains and supercategories
7. **Content enrichment**: Stub entities get synthesized content from session context and known tech definitions

## III. Current State

### Statistics
- **2,204 total concepts** across 10 domains
- **1,722 enriched entities** with definitions, session references, and context snippets
- **281 sessions** capturing 63,000+ agent turns
- **105 knowledge clusters** from fuzzy semantic grouping
- **12 domains** with 7 nested supercategories

### What's Captured
- **Technologies**: Languages, frameworks, tools, platforms (Python, FastAPI, Angular, Docker, etc.)
- **Patterns**: API design, auth flows, deployment strategies, testing approaches
- **Decisions**: Architecture choices, tool selections, workarounds
- **Errors**: Bug patterns, error types, resolution strategies
- **Preferences**: Development style, editor choice, workflow preferences

### User Profile (Inferred from Data)
- **Primary languages**: Python (backend/automation), TypeScript (frontend)
- **Framework stack**: FastAPI + Angular with Vite build tooling
- **Host environment**: Android via Termux — a mobile-centric development setup
- **Development style**: Heavy terminal use (Bash in 76 sessions), CLI-first, Tmux for multitasking
- **AI usage**: Multiple LLM providers (Gemini, Claude, OpenAI) for different tasks
- **DevOps**: Docker for consistency, cloud deployment (AWS/Vercel)
- **Knowledge management**: Auto-extraction with periodic manual curation

## IV. Enrichment Theory: Active Strategies

### Current Passive Pipeline

The existing system is **reactive** — it captures what happens during agent sessions but doesn't actively seek new knowledge. To evolve from a passive log to an active knowledge system, several strategies are available:

### Strategy A: Proactive Questioning

**Concept**: The daemon periodically generates questions based on knowledge gaps and presents them to the user.

**Implementation**:
```
def detect_knowledge_gaps():
    # Find entities with low enrichment confidence
    for entity in entities:
        if entity.session_count > 3 and entity.content_score < 0.5:
            yield f"What is your experience with {entity.title}?"
```

**Questions would target**:
1. **Unenriched stubs** (0 stubs currently, but future entities may be unenriched)
2. **Entities with one session** (1,149 entities with only 1 reference)
3. **Acronym entities** (AAA, ABI, ACE, etc. with no semantic meaning)
4. **Gaps between domains** (areas where no concepts exist)

**Output**: Answers become new concept entries or enrichment for existing entities.

### Strategy B: Cross-Session Synthesis

**Concept**: Many sessions cover related topics. The system should identify connected sessions and synthesize cross-cutting insights.

**Implementation**:
- Cluster sessions by tag overlap (281 sessions, tagged with api(235), ast(222), auth(198), etc.)
- For tag clusters with 5+ sessions, generate a synthesis concept combining insights
- Track how technology stances evolve across sessions (e.g., "migrated from Webpack to Vite")

**Current candidates**:
- **API development patterns**: 235 sessions with api tag
- **Authentication evolution**: 198 sessions with auth — OAuth → JWT patterns
- **Mobile development**: 122 sessions with android — Termux workflow evolution

### Strategy C: External Knowledge Integration

**Concept**: Augment auto-extracted knowledge with structured data from package registries, documentation, and changelogs.

**Implementation**:
```
def enrich_from_registries():
    for entity in entities:
        if entity.is_tech() and not entity.has_external_refs():
            pypi = check_pypi(entity.title)
            npm = check_npm(entity.title)
            github = check_github(entity.title)
            if pypi or npm:
                entity.add_external_refs(pypi_version, docs_url)
```

**Sources**:
- **PyPI API**: Package metadata, versions, dependencies for Python entities
- **npm registry**: Package info for JavaScript/TypeScript entities
- **GitHub API**: Stars, issues, activity for tool entities
- **ReadTheDocs/OpenAPI**: Documentation URLs for framework entities

### Strategy D: Usage Analytics

**Concept**: Track how entities are used together to infer workflows and generate "recipe" concepts.

**Implementation**:
- Co-occurrence matrix: entity A appears in sessions with entity B → potential workflow
- Sequential patterns: entity A always precedes entity B → dependency or pipeline
- Frequency trends: entity usage over time → adoption or deprecation signals

**Example patterns from current data**:
- `FastAPI → Pydantic → SQLAlchemy → PostgreSQL` (API stack)
- `Angular → TypeScript → Vite` (frontend stack)
- `Docker → AWS` (deployment pipeline)
- `Bash → Python → Termux` (local dev workflow)

### Strategy E: Semantic Reclassification

**Concept**: As the knowledge base grows, periodically re-run hierarchy classification with improved algorithms.

**Current limitations**:
- Rule-based keyword matching can over-classify (e.g., entities with "api" tag → Web Platforms even if they're Android API calls)
- Acronym entities (AA, AAA, ABI) pollute domain pages
- Supercategory assignment could use ML-based topic modeling

**Improvements**:
1. Use LLM-based classification on enriched entity bodies for more accurate domain assignment
2. Filter acronym entities (length < 4, all caps) into a separate "acronyms" category
3. Add sub-group level classification beneath supercategories

### Strategy F: Active Learning Loop

**Concept**: The system tracks what the user accesses and prioritizes enrichment of frequently-viewed entities.

**Implementation**:
- Track viewer access patterns (which entities are viewed, searched, or explored)
- Boost enrichment priority for recently/frequently accessed entities
- Generate "Related entities" suggestions based on navigation patterns

## V. Future Vision

### Phase 1 — Foundation (Current)
✅ Passive session capture → entity extraction → OKF storage
✅ Basic enrichment with known tech definitions
✅ Multi-tier hierarchy classification
✅ Searchable web viewer with graph visualization
✅ Domain-based knowledge navigation

### Phase 2 — Active Enrichment (Next)
⬜ Proactive questioning for knowledge gaps
⬜ Cross-session synthesis generation
⬜ External knowledge integration (PyPI, npm, GitHub)
⬜ Usage analytics for workflow detection

### Phase 3 — Intelligent Curation (Future)
⬜ LLM-based classification and clustering
⬜ Automated ontology evolution
⬜ Predictive enrichment (anticipating what the user will need)
⬜ Cross-repository knowledge integration
⬜ Multi-user collaboration

## VI. Design Principles

1. **Passive by default, active on demand**: Knowledge capture should never interrupt workflow
2. **Structure emerges from usage**: Don't force taxonomy — let it emerge from co-occurrence
3. **One concept, one file**: Atomic knowledge units enable precise linking and search
4. **Progressive enrichment**: Start with stubs, improve over time, never block on incomplete data
5. **Raw → curated pipeline**: Original data is preserved (raw/) while knowledge is refined (wiki/)
6. **Graph-native**: Every concept is a node; every relationship is an edge; navigation is traversal
7. **Version-controlled**: The entire wiki is a git repository — every change is tracked
8. **Portable format**: OKF (Open Knowledge Format) with YAML frontmatter — readable by humans and agents

## VII. Conclusion

mykb represents a new paradigm for personal knowledge management: **auto-extracted, continuously curated, graph-native wikis** that grow organically from daily work. The system already captures 2,204 concepts from 281 sessions with zero manual input. The next evolution — active enrichment, external integration, and intelligent curation — will transform it from a passive log into an active knowledge partner.

The key insight is that **most valuable knowledge is already being generated** — it just needs to be captured, structured, and connected. mykb does this automatically, creating a living document of the developer's expertise that grows more valuable with every session.

**Domain:** Concepts

## Related

- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]]
- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/concepts/identity-system|Identity System]]
- [[wiki/concepts/project-lineage|Project Lineage]]
