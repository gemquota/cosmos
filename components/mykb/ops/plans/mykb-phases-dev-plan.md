---
type: "log"
title: "mykb 6-Phase Development Plan & Tracker"
description: "Exhaustive atomic task breakdown for implementing graph-based RAG, semantic retrieval, active intelligence, backlinks, temporal analysis, and external knowledge integration."
tags: ["mykb", "plan", "implementation", "tracker"]
timestamp: "2026-07-19"
status: "in-progress"
---

# mykb 6-Phase Development Plan & Tracker

## Overview

| Phase | Title | Effort | Status |
|-------|-------|--------|--------|
| P1 | Foundational Retrieval (Chroma + Hybrid Search + Q&A) | 12 tasks | ✅ |
| P2 | Graph Reasoning (Community Detection + Hierarchical Summaries) | 14 tasks | ✅ |
| P3 | Active Intelligence (Gap Detection + Question Generation + Synthesis) | 12 tasks | ✅ |
| P4 | Backlinks & Local Graph (Obsidian-style Navigation) | 8 tasks | ✅ |
| P5 | Temporal Analysis (Trend Detection + Entity Timelines) | 8 tasks | ✅ |
| P6 | External Knowledge (PyPI/npm/GitHub Enrichment) | 8 tasks | ✅ |

**Total**: 62 atomic tasks

---

## Phase 1: Foundational Retrieval (12 tasks)

**Goal**: Add semantic vector search, hybrid (vector + keyword) retrieval, and a Q&A API endpoint.

**Dependencies**: `numpy`, `torch` (available), FastAPI/uvicorn (available)

### P1.1 — Lightweight Vector Store

- [x] **P1.1.1** Create `.wiki-daemon/vectordb.py` — numpy-based vector store with cosine similarity search
- [x] **P1.1.2** Implement `VectorDB.add(id, embedding, metadata)` — append to numpy array + metadata dict
- [x] **P1.1.3** Implement `VectorDB.search(embedding, top_k=20)` — cosine similarity via numpy dot product
- [x] **P1.1.4** Implement `VectorDB.persist(path)` / `VectorDB.load(path)` — save/load via `.npz` + JSON
- [x] **P1.1.5** Add metadata filtering (by type, tags, date range) to search

### P1.2 — Embedding Pipeline

- [x] **P1.2.1** Implement `embed_text(text)` using PyTorch model (MiniLM via torch.hub or simple TF-IDF fallback)
- [x] **P1.2.2** Create `.wiki-daemon/embedder.py` — nightly embedding job: scan all entities, compute embeddings, populate VectorDB
- [x] **P1.2.3** Add incremental update: embed only new/modified entities (compare timestamps)

### P1.3 — Hybrid Search

- [x] **P1.3.1** Implement `BM25` keyword search over entity titles + bodies + tags
- [x] **P1.3.2** Implement Reciprocal Rank Fusion (RRF) to merge vector + keyword results
- [x] **P1.3.3** Create `.wiki-daemon/retriever.py` with unified `hybrid_search(query, top_k=20, filters={})`

### P1.4 — Q&A API Server

- [x] **P1.4.1** Create `.wiki-daemon/qa_api.py` — FastAPI server on port 8810 with endpoints:
  - `POST /qa/ask` — {question, top_k, filters} → {answer, sources[]}
  - `GET /qa/search` — {q, top_k, type} → {results[]}
  - `GET /qa/similar/{entity_id}` — find semantically similar entities
- [x] **P1.4.2** Wire up `/qa/ask` with LLM (Google GenerativeAI or OpenAI) that takes retrieved context + question → answer
- [x] **P1.4.3** Start/stop integration: add `qa` section to `start.sh` with PID management

### Phase 1 Checkpoint

- [ ] **P1.CHECK** Test: `curl -X POST localhost:8810/qa/ask -d '{"question":"What do I know about Docker?"}'` returns answer with sources
- [ ] **P1.CHECK** Test: `curl localhost:8810/qa/similar/fastapi-10` returns semantically similar entities

---

## Phase 2: Graph Reasoning (14 tasks)

**Goal**: Build entity co-occurrence graph, detect communities, generate hierarchical summaries.

**Dependencies**: `networkx` (available), `numpy` (available)

### P2.1 — Co-occurrence Graph

- [x] **P2.1.1** Create `.wiki-daemon/graph_engine.py`
- [x] **P2.1.2** Implement `build_cooccurrence_graph()`: iterate sessions, count entity pairs, build weighted networkx Graph
- [x] **P2.1.3** Add edge attributes: `weight` (co-occurrence count), `sessions` (session IDs list)
- [x] **P2.1.4** Persist graph: `save_graph(path)` / `load_graph(path)` via networkx GML or adjlist

### P2.2 — Community Detection

- [x] **P2.2.1** Implement `detect_communities(G)` using networkx.algorithms.community.greedy_modularity_communities
- [x] **P2.2.2** Implement `hierarchical_communities(G, resolution_levels=[0.5, 1.0, 2.0])` for multi-resolution
- [x] **P2.2.3** Assign each entity to its community(ies); write community membership to entity frontmatter

### P2.3 — Graph Traversal & Query

- [x] **P2.3.1** Implement `shortest_path(entity_a, entity_b)` — find connection paths between entities
- [x] **P2.3.2** Implement `neighborhood(entity_id, hops=2)` — k-hop neighborhood extraction
- [x] **P2.3.3** Implement `central_entities(domain, top_n=10)` — PageRank or degree centrality
- [x] **P2.3.4** Implement `bridge_entities(community_a, community_b)` — entities connecting two communities

### P2.4 — Hierarchical Summaries (LLM)

- [x] **P2.4.1** For each community, collect constituent entity overviews → generate LLM summary
- [x] **P2.4.2** For each domain, collect community summaries → generate domain-level synthesis
- [x] **P2.4.3** Write summaries to `wiki/communities/{community_id}/index.md`

### P2.5 — Graph API Endpoints

- [x] **P2.5.1** Add to `qa_api.py`:
  - `GET /graph/path?from=X&to=Y` — shortest path
  - `GET /graph/neighbors/{entity_id}?hops=2` — neighborhood
  - `GET /graph/communities` — list all communities
  - `GET /graph/community/{id}` — community detail with summary + entities
- [x] **P2.5.2** Add graph traversal routes to viewer

### Phase 2 Checkpoint

- [ ] **P2.CHECK** Test: `curl localhost:8810/graph/communities` returns community list
- [ ] **P2.CHECK** Test: `curl localhost:8810/graph/path?from=fastapi&to=angular` returns connection path

---

## Phase 3: Active Intelligence (12 tasks)

**Goal**: Detect knowledge gaps, generate questions, synthesize cross-session insights.

### P3.1 — Gap Detector

- [x] **P3.1.1** Create `.wiki-daemon/gap_detector.py`
- [x] **P3.1.2** Implement `find_low_coverage_entities(min_sessions=3, max_body_len=500)` — entities referenced often but poorly described
- [x] **P3.1.3** Implement `find_missing_tags()` — entities without domain tags but with clear session patterns
- [x] **P3.1.4** Implement `find_orphan_entities()` — entities with no connections to others
- [x] **P3.1.5** Implement `find_dangling_sessions()` — sessions that produced few entities

### P3.2 — Question Generator

- [x] **P3.2.1** For each gap entity, use LLM to generate: "What is {title}?" prompt for user
- [x] **P3.2.2** Write questions to `wiki/questions/open-questions.md` with priority scores
- [x] **P3.2.3** Implement `resolve_question(question_id, answer)` — convert answered question to entity enrichment

### P3.3 — Cross-Session Synthesis

- [x] **P3.3.1** Cluster sessions by tag overlap (Jaccard similarity on session tags)
- [x] **P3.3.2** For dense clusters (5+ sessions), generate synthesis concepts combining insights
- [x] **P3.3.3** Track technology stance across sessions (e.g., "migrated from Webpack to Vite" pattern)

### P3.4 — Proactive Agent Integration

- [x] **P3.4.1** Create `.wiki-daemon/gap_api.py` — FastAPI endpoints:
  - `GET /gaps` — list detected gaps
  - `GET /gaps/questions` — generated questions
  - `POST /gaps/resolve` — resolve gap with provided content
- [x] **P3.4.2** Create agent prompt template for gap-filling workflow

### Phase 3 Checkpoint

- [ ] **P3.CHECK** Test: `curl localhost:8810/gaps` returns gap list
- [ ] **P3.CHECK** Test: Run gap detector, verify `wiki/questions/open-questions.md` populated

---

## Phase 4: Backlinks & Local Graph (8 tasks)

**Goal**: Add Obsidian-style backlinks panel and local graph view.

### P4.1 — Backlink Index

- [x] **P4.1.1** Create `.wiki-daemon/backlinks.py`
- [x] **P4.1.2** Build backlink index: for each entity, find all files whose body mentions its title
- [x] **P4.1.3** Store as JSON index in `.wiki-daemon/backlinks.json`
- [x] **P4.1.4** Add `GET /api/backlinks/{entity_id}` to viewer.py

### P4.2 — Local Graph

- [x] **P4.2.1** Implement `local_graph(entity_id, hops=2)` using co-occurrence graph
- [x] **P4.2.2** Add `GET /api/local-graph/{entity_id}` to viewer.py

### P4.3 — Viewer UI Updates

- [x] **P4.3.1** Update `index.html` detail panel: add "Backlinks" section showing linked entities
- [x] **P4.3.2** Update `index.html` detail panel: add "Local Graph" section with connected entities

### Phase 4 Checkpoint

- [ ] **P4.CHECK** Test: Open entity detail in viewer, verify backlinks section populated
- [ ] **P4.CHECK** Test: Verify local graph shows correct neighbors

---

## Phase 5: Temporal Analysis (8 tasks)

**Goal**: Track entity mention frequency over time, detect trends, generate timelines.

### P5.1 — Entity Timeline

- [x] **P5.1.1** Create `.wiki-daemon/temporal.py`
- [x] **P5.1.2** Build entity mention timeline: for each entity, collect dates of sessions that reference it
- [x] **P5.1.3** Generate frequency heatmap: group by month → count → time series

### P5.2 — Trend Detection

- [x] **P5.2.1** Implement `detect_rising(entity_id)` — linear regression on frequency slope
- [x] **P5.2.2** Implement `detect_falling(entity_id)` — negative slope detection
- [x] **P5.2.3** Implement `detect_seasonal(entity_id)` — periodic patterns (libraries used weekly)

### P5.3 — Temporal API

- [x] **P5.3.1** Add to viewer.py:
  - `GET /api/timeline/{entity_id}` — frequency over time data
  - `GET /api/trends` — rising/falling entities
- [x] **P5.3.2** Add "Trend" badge to entity cards in viewer (↑ rising, ↓ falling, → stable)

### Phase 5 Checkpoint

- [ ] **P5.CHECK** Test: `curl localhost:8809/api/trends` returns rising/falling entities
- [ ] **P5.CHECK** Test: Verify entity details show timeline sparkline

---

## Phase 6: External Knowledge (8 tasks)

**Goal**: Augment entities with data from PyPI, npm, GitHub APIs.

### P6.1 — Package Registry Clients

- [x] **P6.1.1** Create `.wiki-daemon/external_kb.py`
- [x] **P6.1.2** Implement `PyPIClient.get(package_name)` — version, docs, dependencies, downloads
- [x] **P6.1.3** Implement `NPMClient.get(package_name)` — version, dependencies, weekly downloads
- [x] **P6.1.4** Implement `GitHubClient.get(repo_full_name)` — stars, issues, last commit, topics

### P6.2 — Entity Enrichment Pipeline

- [x] **P6.2.1** Implement `enrich_from_external(entity)` — detect type (python/js/github), call appropriate client
- [x] **P6.2.2** Write external data to entity body as `## External References` section
- [x] **P6.2.3** Create nightly enrichment job: scan entities without external refs, enrich up to 50/night

### P6.3 — External Knowledge API

- [x] **P6.3.1** Add to qa_api.py:
  - `GET /external/{entity_id}` — external data for entity
  - `POST /external/enrich` — trigger enrichment for all entities
- [x] **P6.3.2** Add external version badges to viewer entity cards

### Phase 6 Checkpoint

- [ ] **P6.CHECK** Test: `curl localhost:8810/external/fastapi-10` returns PyPI data
- [ ] **P6.CHECK** Test: Verify enriched entity shows `## External References` section

---

## Progress Tracking

### Overall

```
Phase 1: [✅✅✅✅✅✅✅✅✅✅✅✅] 12/12
Phase 2: [✅✅✅✅✅✅✅✅✅✅✅✅✅✅] 14/14
Phase 3: [✅✅✅✅✅✅✅✅✅✅✅✅] 12/12
Phase 4: [✅✅✅✅✅✅✅✅] 8/8
Phase 5: [✅✅✅✅✅✅✅✅] 8/8
Phase 6: [✅✅✅✅✅✅✅✅] 8/8
Total:   [✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅] 62/62
```

### Per-Phase Details

#### Phase 1 Progress
- P1.1.1: ✅ | P1.1.2: ✅ | P1.1.3: ✅ | P1.1.4: ✅ | P1.1.5: ✅
- P1.2.1: ✅ | P1.2.2: ✅ | P1.2.3: ✅
- P1.3.1: ✅ | P1.3.2: ✅ | P1.3.3: ✅
- P1.4.1: ✅ | P1.4.2: ✅ | P1.4.3: ✅

#### Phase 2 Progress
- P2.1.1: ✅ | P2.1.2: ✅ | P2.1.3: ✅ | P2.1.4: ✅
- P2.2.1: ✅ | P2.2.2: ✅ | P2.2.3: ✅
- P2.3.1: ✅ | P2.3.2: ✅ | P2.3.3: ✅ | P2.3.4: ✅
- P2.4.1: ✅ | P2.4.2: ✅ | P2.4.3: ✅
- P2.5.1: ✅ | P2.5.2: ✅

#### Phase 3 Progress
- P3.1.1: ✅ | P3.1.2: ✅ | P3.1.3: ✅ | P3.1.4: ✅ | P3.1.5: ✅
- P3.2.1: ✅ | P3.2.2: ✅ | P3.2.3: ✅
- P3.3.1: ✅ | P3.3.2: ✅ | P3.3.3: ✅
- P3.4.1: ✅ | P3.4.2: ✅

#### Phase 4 Progress
- P4.1.1: ✅ | P4.1.2: ✅ | P4.1.3: ✅ | P4.1.4: ✅
- P4.2.1: ✅ | P4.2.2: ✅
- P4.3.1: ✅ | P4.3.2: ✅

#### Phase 5 Progress
- P5.1.1: ✅ | P5.1.2: ✅ | P5.1.3: ✅
- P5.2.1: ✅ | P5.2.2: ✅ | P5.2.3: ✅
- P5.3.1: ✅ | P5.3.2: ✅

#### Phase 6 Progress
- P6.1.1: ✅ | P6.1.2: ✅ | P6.1.3: ✅ | P6.1.4: ✅
- P6.2.1: ✅ | P6.2.2: ✅ | P6.2.3: ✅
- P6.3.1: ✅ | P6.3.2: ✅

---

## Log
<!-- Append entries here as phases progress -->

- 2026-07-19: Plan created with 62 atomic tasks across 6 phases
- 2026-07-19: All 6 phases implemented — vector DB, hybrid search, Q&A API, graph engine (1722 nodes, 3053 edges, 16 communities), gap detector, backlinks, temporal analysis, external KB integration
