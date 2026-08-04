---
type: "concept"
title: "mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint"
description: "Comprehensive research report analyzing personal knowledge database systems, LLM-native wikis, graph-based RAG, and related methodologies — with an implementation blueprint for mykb."
tags: ["mykb", "research", "knowledge-graph", "rag", "integration", "architecture", "synthesis"]
timestamp: "2026-07-19"
resource: ""
---

# mykb Research Report: Personal LLM Wiki Systems
## Methodologies, Architectures & Integration Blueprint

> *A systematic survey of personal knowledge management systems, LLM-native wikis, graph-based RAG, and agent memory architectures — with a concrete implementation roadmap for mykb.*

---

## 0. Executive Summary

mykb is a **personalized, auto-extracted knowledge wiki** that captures developer knowledge from Codex agent sessions. It already has passive extraction, entity enrichment, hierarchy classification, and dual viewer servers. However, compared to state-of-the-art systems (GraphRAG, Mem0, Obsidian ecosystem), several capabilities are absent:

| Capability | mykb (current) | Industry Best | Gap |
|---|---|---|---|
| Entity extraction | Regex + heuristics | LLM-based + semantic parsing | Significant |
| Retrieval | Filesystem scan | Vector search + hybrid ranking | Critical |
| Graph reasoning | Static knowledge graph | GraphRAG traversal + LLM inference | Critical |
| Active questioning | None | Proactive gap detection | Significant |
| External knowledge | None | Package registry integration | Moderate |
| Cross-session synthesis | Manual | Automated topic clustering | Significant |
| Temporal tracking | Timestamps only | Trend analysis + drift detection | Absent |
| Collaborative features | None | Multi-user graph merge | Future |

This report surveys 12 reference systems across 5 methodological categories, then proposes a **6-phase integration architecture** to close these gaps.

---

## 1. Reference Systems Survey

### 1.1 GraphRAG (Microsoft Research)

**Concept**: Combines knowledge graphs with retrieval-augmented generation. Instead of flat vector search, GraphRAG builds a hierarchical entity graph from source documents, then uses LLM-guided graph traversal for query answering.

**Key Innovations**:
- **Community detection**: Leiden algorithm clusters related entities into communities at multiple resolution levels
- **Hierarchical summaries**: Each community gets an auto-generated summary, enabling both global and local query understanding
- **Graph traversal**: Answers are synthesized by walking entity relationships rather than flat similarity search
- **Covariate extraction**: Captures claims, relationships between entities with structured output

**Applicability to mykb**:
- mykb already has entity extraction and cross-linking — GraphRAG's community detection would replace the current rule-based hierarchy with emergent, data-driven clustering
- The hierarchical summary approach maps directly to mykb's domain → supercategory → subgroup structure
- GraphRAG could replace the current regex-based extraction with LLM-guided entity and relationship extraction

**Integration effort**: High (requires LLM calls for community summarization + Leiden clustering implementation)

### 1.2 Mem0 / MemGPT (Letta)

**Concept**: LLM-native memory systems that give AI agents persistent, evolving memory. Mem0 provides memory operations (create, update, search) while MemGPT introduces a virtual memory hierarchy (working, archival, recall).

**Key Innovations**:
- **Memory tiers**: Working memory (immediate context), archival memory (long-term), recall (episodic)
- **Memory consolidation**: Periodic summarization and pruning to prevent context overflow
- **Conflict resolution**: When memories conflict, newer or more specific memories take precedence
- **Experience extraction**: Automatically deriving structured memories from conversation turns

**Applicability to mykb**:
- mykb's session extraction is analogous to MemGPT's archival memory — agent sessions become permanent knowledge
- The wiki daemon already captures every session turn — Mem0's extraction patterns could improve entity/decision extraction quality
- **Crucial gap**: mykb has no working memory tier — it cannot recall what was recently relevant
- **Crucial gap**: No memory consolidation — as the wiki grows, retrieval degrades without summarization/pruning

**Integration effort**: Moderate (add memory tier system + consolidation pipeline)

### 1.3 Obsidian + Graph View

**Concept**: Local-first markdown knowledge base with an interactive graph visualization showing note connections. The ecosystem includes 1,500+ community plugins for extending functionality.

**Key Innovations**:
- **Backlinks**: Every note automatically tracks which other notes reference it
- **Graph view**: Interactive force-directed graph of note relationships
- **Local graph**: Per-note local connection view
- **Plugins**: Dataview (query engine), Templater (templates), Kanban, Excalidraw
- **Obsidian Publish**: Shared knowledge base hosting

**Applicability to mykb**:
- mykb's okf server (8808) already provides a graph view — but it's Cytoscape.js based, not Obsidian's refined UX
- **Crucial gap**: No backlinks panel — entity pages don't show which sessions/entities reference them
- **Crucial gap**: No local graph view — viewing an entity should show its immediate neighbors
- **Integration**: The Dataview plugin's SQL-like querying of metadata could inspire a query interface for mykb

**Integration effort**: Low (add backlinks + local graph)

### 1.4 Roam Research / Logseq

**Concept**: Block-level outliners with bidirectional linking. Every block in a note has a unique ID and can be referenced from anywhere. This enables unprecedented granularity of knowledge connection.

**Key Innovations**:
- **Block references**: Reference individual paragraphs, not just pages
- **Daily notes as defaults**: Every day gets a note; all thoughts start there
- **Page references**: `[[wiki/memory/backlinks]]` syntax creates automatic bidirectional links
- **Query blocks**: Embedded queries aggregate blocks by metadata
- **Attributes**: `property:: value` syntax for structured data within blocks

**Applicability to mykb**:
- **Crucial gap**: mykb has page-level entities but no block-level granularity — a session turn is the smallest extractable unit
- **Daily notes**: mykb has a `daily/` directory but it's not the default entry point
- **Bidirectional links**: mykb's `Related:` tag lists are unidirectional — no backlinks
- **Integration**: The block-reference model would enable finer-grained knowledge extraction (per-turn concepts rather than per-session entities)

**Integration effort**: High (block ID system + bidirectional index)

### 1.5 Dendron

**Concept**: Hierarchical note-taking built on a filesystem hierarchy. Notes use dot-notation (`topic.subtopic.concept`) inspired by programming package structures.

**Key Innovations**:
- **Hierarchy as first-class**: `topic.subtopic.concept.md` enables navigation by drilling down
- **Schema**: YAML schemas define note types, templates, and required fields
- **Hierarchical refactoring**: Move entire sub-trees of knowledge
- **Lookup**: Fuzzy-find notes by hierarchical path

**Applicability to mykb**:
- mykb's domain/supercategory/entity structure is already hierarchical — but it's enforced by directory structure, not note naming
- **Crucial gap**: No hierarchical lookup — you can't type `web.api.fastapi` to find the FastAPI entity
- **Integration opportunity**: Add aliases or hierarchy tags to entities for dot-notation navigation

**Integration effort**: Low (add hierarchy tags to frontmatter)

### 1.6 Zettelkasten (Luhmann Method)

**Concept**: The original knowledge management system developed by Niklas Luhmann. Tiny atomic notes (Zettels) with unique IDs that link freely. Emergent structure through accumulation.

**Key Principles**:
- **Atomicity**: One concept per note
- **Connection**: Notes link to other notes through connection indices
- **Emergent order**: No top-down categories — structure emerges from link density
- **Communication**: The system "talks back" — browsing links reveals unexpected connections

**Applicability to mykb**:
- mykb already follows atomicity (one entity = one file)
- **Crucial gap**: No connection index — entities have Related: tags but no hub notes showing dense connection clusters
- **Crucial gap**: Zettelkasten thrives on manual linking — mykb's auto-extracted links need manual curation to reach emergent insight quality
- **Integration opportunity**: Hub notes for dense clusters, weekly "Zettelkasten review" workflow

**Integration effort**: Low (add hub notes + linking workflow)

### 1.7 PARA Method (Tiago Forte)

**Concept**: Organize digital life into four top-level categories: Projects, Areas, Resources, Archives. Everything fits into one of these.

**Key Innovations**:
- **Projects**: Short-term outcomes with deadlines
- **Areas**: Long-term responsibilities without deadlines
- **Resources**: Topics of interest
- **Archives**: Inactive items from the above three
- **Progressive summarization**: Five-layer note summarization (original → bold → highlights → executive summary → source)

**Applicability to mykb**:
- **Crucial gap**: No project/area distinction — mykb entities are all "concepts" with no temporal or responsibility scope
- **Crucial gap**: No progressive summarization — entity pages grow but never summarize
- **Integration**: Add `scope: project|area|resource|archive` field to frontmatter; implement summarization pipeline

**Integration effort**: Low (frontmatter field + periodic summarization pass)

### 1.8 Notion Databases

**Concept**: All-in-one workspace with relational databases, kanban boards, calendars, and wikis. Content is stored in database rows with typed properties.

**Key Innovations**:
- **Relational properties**: Link database rows across tables (like foreign keys)
- **Views**: Same data as table, board, calendar, gallery, or list
- **Templates**: Database templates for consistent entry creation
- **Rollups**: Aggregate data from related rows
- **Formulas**: Computed properties (spreadsheet-like)

**Applicability to mykb**:
- **Crucial gap**: No typed properties on entities — frontmatter is unstructured YAML without a schema
- **Crucial gap**: No computed properties — can't auto-derive "total sessions using FastAPI" or "most co-occurring tags"
- **Integration opportunity**: Add OKF schema validation + computed property scripts

**Integration effort**: Moderate (schema enforcement + computed property engine)

### 1.9 OKF (Open Knowledge Format)

**Concept**: Portable project knowledge as a directory of markdown files with YAML frontmatter that humans and agents read from one source. The format mykb already uses.

**Key Specifications**:
- **Concept-per-file**: One OKF concept = one `.md` file with YAML frontmatter and body
- **Required fields**: `type`, `title` (and optionally `description`, `tags`, `timestamp`, `source`)
- **Cross-linking**: `[title](path)` markdown links between concepts
- **Bundle structure**: `okf validate` and `okf lint` commands for conformance and quality

**Applicability to mykb**:
- ✅ Already adopted as the core format
- **Crucial gap**: Only `entity`, `session`, `synthesis`, `domain`, and `topic` types are used — OKF allows `source`, `question`, `project`, `daily` which are underutilized
- **Crucial gap**: No source attribution pipeline — entities lose their session origin after extraction
- **Integration**: Expand type usage, add provenance tracking

**Integration effort**: Low (expand type taxonomy + provenance field)

### 1.10 Vector Databases (Chroma, Pinecone, Weaviate)

**Concept**: Specialized databases for storing and searching embedding vectors. Enable semantic similarity search across knowledge base content.

**Key Innovations**:
- **Semantic search**: Find concepts by meaning, not just keyword match
- **Hybrid search**: Combine vector similarity with keyword/Boolean filters
- **Metadata filtering**: Narrow search by type, tag, date, or any metadata
- **Multi-modal embeddings**: Search across text, code, images in one index

**Applicability to mykb**:
- **Crucial gap**: mykb search is grep-based (the 8809 viewer searches titles and descriptions) — no semantic search
- **Integration**: Add Chroma (local, Termux-compatible) for embedding-based retrieval
- **Low-hanging fruit**: Embed entity bodies + session texts, enable "find similar concepts" on entity pages

**Integration effort**: Low (add Chroma + nightly embedding job)

### 1.11 LangChain / LlamaIndex RAG

**Concept**: Frameworks for building RAG (Retrieval-Augmented Generation) systems — retrieving relevant context and injecting it into LLM prompts.

**Key Innovations**:
- **Document loaders**: Parsers for every file format (PDF, HTML, code, markdown)
- **Text splitters**: Chunking strategies (recursive, semantic, token-aware)
- **Retrievers**: Vector search, BM25 keyword search, ensemble retrieval
- **Query engines**: Structured Q&A, multi-hop, agent-based
- **Index types**: Summary index, tree index, keyword table index

**Applicability to mykb**:
- **Crucial gap**: No RAG pipeline — the wiki can't answer questions using its knowledge
- **Integration**: Add LlamaIndex query engine over the wiki content
- **Use case**: "What do I know about Docker deployment patterns?" → retrieves relevant entity pages + sessions → synthesizes answer

**Integration effort**: Moderate (add LlamaIndex + API endpoint for Q&A)

### 1.12 Agent Memory & Knowledge Sharing (CrewAI, AutoGen)

**Concept**: Multi-agent systems where agents share knowledge, delegate tasks, and build a shared understanding over time.

**Key Innovations**:
- **Shared memory**: Agents read/write to a shared knowledge store
- **Agent handoff**: Context passing when one agent delegates to another
- **Knowledge distillation**: Long conversations condensed into reusable knowledge
- **Tool documentation**: Agents document their own tools for other agents to use

**Applicability to mykb**:
- **Crucial gap**: No multi-agent memory — each Codex session starts fresh with no knowledge from previous sessions
- **Crucial gap**: No tool documentation — agents use tools (exec_command, apply_patch, etc.) but their usage patterns aren't captured as reusable knowledge
- **Integration**: mykb as shared knowledge base for all Codex agents; tool usage patterns → wiki/tools/ pages

**Integration effort**: High (agent-side integration + tool documentation pipeline)

---

## 2. Gap Analysis: mykb vs. State of the Art

### 2.1 What mykb Does Well ✅

| Strength | Details |
|----------|---------|
| **Passive capture** | Zero-effort session logging — the daemon works automatically |
| **Entity extraction** | 1,722 entities from 281 sessions — good coverage |
| **Content enrichment** | All entities have `## Overview`, `## References`, `## Context` sections |
| **Hierarchy classification** | 10 domains with sub-groups covering 99% of entities |
| **Dual viewer system** | Graph view (okf server) + searchable list view |
| **OKF conformance** | Portable, human-readable, agent-readable format |
| **Scale** | 2,204 concepts, 63K turns processed — real-world validation |

### 2.2 Critical Gaps 🔴

| Gap | Impact | Reference System |
|-----|--------|-----------------|
| **No vector search** | Can't find semantically similar concepts | Chroma, Pinecone, LlamaIndex |
| **No graph reasoning** | Can't answer "what connects these domains?" | GraphRAG, Neo4j |
| **No LLM querying** | Can't ask the wiki questions in natural language | GraphRAG, LlamaIndex |
| **No backlinks** | Entity pages don't show what references them | Obsidian, Roam Research |
| **No temporal analysis** | Can't detect trends or evolution over time | Mem0/GPT |
| **No active gap detection** | System doesn't ask questions | Mem0, knowledge tracing |

### 2.3 Moderate Gaps 🟡

| Gap | Impact | Reference System |
|-----|--------|-----------------|
| **No cross-session synthesis** | Related session insights stay isolated | PARAS, consolidated summarization |
| **No progressive summarization** | Entity pages get longer but never shorter | Tiago Forte, Mem0 |
| **No external knowledge** | Can't enrich from PyPI/npm/GitHub APIs | — |
| **No semantic clustering** | Groups are rule-based, not emergent | GraphRAG community detection |
| **No block-level references** | Can't reference specific session turns | Roam/Logseq |
| **No daily note system** | No daily capture habit | Roam/Logseq daily notes |
| **No project tracking** | Can't distinguish ongoing from one-off work | PARA, Notion |

### 2.4 Future Gaps 🔵

| Gap | Impact | Reference System |
|-----|--------|-----------------|
| **Multi-agent memory** | Agents can't learn from past sessions | CrewAI, Mem0 |
| **Collaborative graph** | No multi-user knowledge merging | Obsidian Sync |
| **Mobile client** | Can't read wiki on the go | — |
| **API for external tools** | No REST API for wiki queries | — |
| **Visual knowledge mapping** | Excalidraw/P4-style concept diagrams | Obsidian Canvas |

---

## 3. Implementation Blueprint

### Phase 1: Foundational Retrieval (2-3 days)

**Goal**: Add semantic search and RAG Q&A to make the wiki queryable.

```
┌─────────────┐    ┌──────────┐    ┌──────────────┐
│ Entity Files │───▶│ Chroma   │───▶│ Hybrid       │
│ Session Files│    │ DB       │    │ Retriever    │
│ .md on disk │    │ (local)  │    │ (vector+kw)  │
└─────────────┘    └──────────┘    └──────┬───────┘
                                          │
                                    ┌─────▼─────┐
                                    │ mykb Q&A  │
                                    │ API        │
                                    │ (port 8810)│
                                    └───────────┘
```

**Implementation**:

```python
# 1. Embed wiki content nightly
def embed_wiki():
    import chromadb
    chroma = chromadb.PersistentClient(path=".wiki-daemon/chroma")
    collection = chroma.get_or_create_collection("mykb")
    for entity in scan_entities():
        embedding = embed_text(entity['title'] + "\n" + entity['body'])
        collection.add(entity['id'], embedding, metadata=entity['fm'])
    return collection

# 2. Query with hybrid search
def query_wiki(question: str, top_k=10):
    # Vector search
    vec_results = collection.query(embed_text(question), n_results=top_k)
    # Keyword search (BM25 fallback)
    kw_results = bm25_search(question, entities)
    # Reciprocal rank fusion
    return fuse_rankings(vec_results, kw_results)
```

**Files to create**: `.wiki-daemon/rag_engine.py`, `.wiki-daemon/qa_api.py`
**Port**: 8810 for Q&A API

### Phase 2: Graph Reasoning (3-4 days)

**Goal**: Add GraphRAG-style community detection and hierarchical summarization.

```
┌──────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Entity Graph  │───▶│ Community        │───▶│ Hierarchical     │
│ (co-occurrence│    │ Detection        │    │ Summarization    │
│  + tag links) │    │ (Leiden algo)     │    │ (LLM per cluster)│
└──────────────┘    └──────────────────┘    └──────────────────┘
                                                        │
                    ┌───────────────────────────────────┘
                    ▼
           ┌────────────────┐
           │ Global Query   │
           │ (cross-community│
           │  synthesis)     │
           └────────────────┘
```

**Key additions**:
- Build entity co-occurrence graph from session data
- Run Leiden clustering for community detection (replacing rule-based hierarchy)
- Generate LLM summaries for each community
- Support global queries (cross-community) and local queries (within-community)

**Implementation**:

```python
# 1. Build co-occurrence graph
def build_graph():
    G = nx.Graph()
    for session in sessions:
        entities = extract_entities_from_session(session)
        for e1, e2 in combinations(entities, 2):
            if G.has_edge(e1, e2):
                G[e1][e2]['weight'] += 1
            else:
                G.add_edge(e1, e2, weight=1)
    return G

# 2. Community detection
def detect_communities(G):
    communities = leidenalg.find_partition(G, leidenalg.ModularityVertexPartition)
    for i, community in enumerate(communities):
        summary = llm_summarize([entities[e] for e in community])
        write_community_index(i, community, summary)
```

### Phase 3: Active Intelligence (2-3 days)

**Goal**: Make the wiki proactive — detecting gaps, asking questions, suggesting connections.

```
┌──────────────┐    ┌────────────────┐    ┌─────────────────┐
│ Gap Detector │───▶│ Question       │───▶│ Answer          │
│ (low-coverage│    │ Generator      │    │ Integration     │
│  entities)   │    │ (LLM prompts)   │    │ (→ entity update)│
└──────────────┘    └────────────────┘    └─────────────────┘

┌──────────────┐    ┌────────────────┐
│ Connection   │───▶│ Cross-Session  │
│ Suggestion   │    │ Synthesis      │
│ Engine       │    │ Generator      │
└──────────────┘    └────────────────┘
```

**Implementation**:

```python
# 1. Detect knowledge gaps
def detect_gaps():
    gaps = []
    for entity in entities:
        # Entity referenced in 5+ sessions but body < 500 chars → gap
        if entity['session_count'] >= 5 and len(entity['body']) < 500:
            gaps.append(entity)
        # Entity has tags but no overview → gap
        if entity['tags'] and '## Overview' not in entity['body']:
            gaps.append(entity)
    return gaps

# 2. Generate questions
def generate_questions(gaps):
    questions = []
    for entity in gaps:
        prompt = f"Entity '{entity['title']}' is referenced in {entity['session_count']} sessions with tags: {entity['tags']}. Generate a question to learn more about it."
        question = llm.generate(prompt)
        questions.append(question)
    return questions

# 3. Cross-session synthesis
def synthesize_cluster(tag_cluster):
    sessions = get_sessions_by_tag(tag_cluster)
    combined = "\n".join(s['turn_log'] for s in sessions)
    synthesis = llm.summarize(combined, focus=f"common patterns in {tag_cluster}")
    return synthesis
```

### Phase 4: Backlinks & Local Graph (1 day)

**Goal**: Add Obsidian-style backlinks panel and local graph view to the viewer.

```python
# Backlink index (computed nightly)
def build_backlink_index():
    backlinks = defaultdict(list)
    for entity in entities:
        # Find all entities that link to this one
        for other in entities:
            if entity['title'].lower() in other['body'].lower():
                backlinks[entity['id']].append(other['id'])
    return backlinks

# Local graph (entities within 2 hops)
def local_graph(entity_id, hops=2):
    visited = {entity_id}
    queue = [(entity_id, 0)]
    while queue:
        current, depth = queue.pop(0)
        if depth >= hops: continue
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    return visited
```

Add to viewer.py:
- `/api/backlinks/{id}` — returns entities referencing this one
- `/api/local-graph/{id}` — returns 2-hop neighborhood
- UI detail panel shows backlinks section

### Phase 5: Temporal Analysis & Trends (2 days)

**Goal**: Track how knowledge evolves over time — rising/falling topics, emerging patterns.

```python
# Entity mention frequency over time
def entity_timeline(entity_id):
    dates = []
    for session in sessions:
        if entity_id in session['entities']:
            dates.append(session['timestamp'])
    # Group by month → frequency heatmap
    return group_by_month(dates)

# Trend detection
def detect_trends():
    trends = {}
    for entity in entities:
        freq = entity_timeline(entity['id'])
        if is_rising(freq): trends['rising'].append(entity)
        if is_falling(freq): trends['falling'].append(entity)
    return trends
```

### Phase 6: External Knowledge Integration (2-3 days)

**Goal**: Augment entities with data from package registries, documentation, changelogs.

```python
def enrich_from_external(entity):
    if is_python_package(entity['title']):
        data = pypi_client.get(entity['title'])
        entity['external'] = {
            'version': data['info']['version'],
            'docs': data['info']['project_urls']['Documentation'],
            'dependencies': data['info']['requires_dist'],
            'github_stars': fetch_github_stars(data['info']['home_page'])
        }
    elif is_npm_package(entity['title']):
        data = npm_client.get(entity['title'])
        entity['external'] = {
            'version': data['version'],
            'dependencies': data['dependencies'],
            'weekly_downloads': data['downloads']
        }
```

---

## 4. Architecture Integration Diagram

```
                           ┌─────────────────────────────────────┐
                           │         mykb Knowledge Graph         │
                           │  (2,204 concepts, 10 domains, graph) │
                           └──────────┬──────────────────────────┘
                                      │
            ┌─────────────────────────┼──────────────────────────┐
            │                         │                          │
            ▼                         ▼                          ▼
    ┌───────────────┐       ┌─────────────────┐       ┌────────────────┐
    │  Viewer Layer  │       │  Retrieval Layer │       │  Intelligence  │
    │  (ports 8808,  │       │  (port 8810)     │       │  Layer         │
    │   8809)        │       │                  │       │  (daemon)      │
    ├───────────────┤       ├─────────────────┤       ├────────────────┤
    │ • Graph view  │       │ • Vector search  │       │ • Gap detector  │
    │ • List view   │       │ • Keyword search │       │ • Question gen  │
    │ • Backlinks   │       │ • Hybrid rank    │       │ • Synthesis     │
    │ • Local graph │       │ • Q&A generation │       │ • Trend analysis│
    │ • Domain tree │       │ • Graph traversal│       │ • Consolidation │
    └───────┬───────┘       └────────┬────────┘       └───────┬────────┘
            │                        │                        │
            └────────────────────────┼────────────────────────┘
                                     │
                                     ▼
                    ┌─────────────────────────────┐
                    │     Storage Layer            │
                    │  (wiki/*.md on disk +        │
                    │   Chroma vector DB +         │
                    │   co-occurrence graph)       │
                    └─────────────────────────────┘
```

---

## 5. Resource Estimates

| Phase | Components | Estimated Effort | Dependencies |
|-------|-----------|-----------------|-------------|
| **P1** | Chroma embedding + hybrid retriever + Q&A API | 2-3 days | `chromadb`, `sentence-transformers` |
| **P2** | Co-occurrence graph + Leiden clustering + hierarchical summaries | 3-4 days | `networkx`, `leidenalg`, LLM API |
| **P3** | Gap detector + question generator + cross-session synthesis | 2-3 days | LLM API |
| **P4** | Backlink index + local graph API + UI components | 1 day | None (pure filesystem) |
| **P5** | Temporal frequency analysis + trend detection | 2 days | `pandas`, `scipy` |
| **P6** | PyPI/npm/GitHub API integration | 2-3 days | `requests`, API keys |

**Total**: ~12-18 days for full implementation

---

## 6. Quick Wins (This Week)

These items deliver high value with minimal effort:

| Item | Effort | Impact |
|------|--------|--------|
| 1. **Backlink index** | 2 hours | See what references each entity |
| 2. **Local graph view** | 4 hours | Visualize entity neighborhoods |
| 3. **Daily note prompt** | 1 hour | Start a daily capture habit |
| 4. **Question registry** | 2 hours | Collect open questions from gaps |
| 5. **Trend timeline** | 4 hours | See entity frequency over session history |

---

## 7. References

1. Microsoft GraphRAG: https://microsoft.github.io/graphrag/
2. Mem0: https://mem0.ai/
3. Letta (MemGPT): https://letta.com/
4. Obsidian Graph View: https://obsidian.md/
5. Zettelkasten Method: https://zettelkasten.de/
6. PARA Method (Tiago Forte): https://fortelabs.com/blog/para/
7. OKF Specification: https://okfgem.com/
8. Chroma DB: https://www.trychroma.com/
9. LlamaIndex: https://www.llamaindex.ai/
10. Dendron: https://www.dendron.so/
11. Roam Research: https://roamresearch.com/
12. Logseq: https://logseq.com/
