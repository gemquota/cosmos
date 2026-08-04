# 13 — Algorithm Analysis

**Doc ID:** COSMOS-AUDIT-13 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [15 Performance](15_PERFORMANCE_AUDIT.md) · [16 Memory](16_MEMORY_ANALYSIS.md)

---

## 1. Algorithm Inventory & Complexity

| Algorithm | Module | Type | Time (avg) | Space | Notes |
|---|---|---|---|---|---|
| TF-IDF search (`search_query`) | mykb/server.py | scoring / top-k | O(Q·D + D·log?) | O(D) | naive; counts word freq per doc per query |
| Hybrid search | mykb/.wiki-daemon/search_fusion.py | fused retrieval | O(D·k) | O(D) | TF-IDF + semantic vectors |
| Semantic cosine | search_fusion.py | vector cosine | O(D) per dim | O(V) | dense npy |
| Priority aging (`PriorityPool`) | rsis/priority_pool.py | priority queue | O(log N) insert/pop | O(N) | + aging boost per wait-second |
| Clamp tuned params | rsis/config.py | bounded apply | O(K) per state | O(1) | per-state file |
| Deadline/Budget | rsis/timeout.py | timer | O(1) | O(1) | monotonic deadline checks |
| Extrapolation | rsis/extrapolation.py | trend-fit | O(N) | O(1) | outcome trends |
| framework validation | space/src/data/framework-loader.ts | schema check | O(F) | O(F) | structure correctness |
| answer validation | space/src/engine/validator.ts | rule check | O(A) | O(A) | per-answer |
| Contradiction detection | space/src/intelligence/contradiction-detector.ts | pairwise compare | O(A²) | O(A) | over answers in session |
| artifact extraction | space/src/data/artifact-extractor.ts | regex/dictionary | O(T) | O(T) | text → artifacts |

## 2. Complexity Correctness Notes

- **TF-IDF `search_query` O(Q·D):** each query scans the full doc set (`for i, doc in
  enumerate(SEARCH_INDEX['docs'])`) and counts words — scales linearly with corpus; fine at current
  ~5.4k docs, will not scale to >100k without an inverted index [I, Med].
- **Contradiction detection O(A²):** pairwise comparison over answers within a session (326 Q max)
  bounded; acceptable. [I, Low]
- **Priority aging:** amortized O(log N); suitable for D2 parallelism. [I, Low]

## 3. Worst/Average/Best Cases

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| TF-IDF query | Ω(1) (cached) | O(Q·D) | O(Q·D) matching all docs |
| Semantic cosine | Ω(D) | O(D) | O(D) |
| Priority pool ops | Ω(1) | O(log N) | O(log N) |
| Contradiction detection | Ω(A) | O(A²) | O(A²) |

## 4. Cache Friendliness

- Vector files are read into NumPy and reused across queries — good spatial locality. [I, Low]
- TF-IDF loop touches every doc array sequentially — cache-friendly but bandwidth-bound. [I, Med]

## 5. Parallelizability & Vectorization

- **Vectorizable:** TF-IDF scoring (SIMD/NumPy over doc-word matrices); semantic cosine (already
  vectorized). [I, Med]
- **Parallelizable:** doc scoring across processes (embarrassingly parallel); L2 candidate DAG already
  parallel. [I, Low]
- **Not vectorized:** priority aging, validation, artifact extraction (string ops). [O]

## 6. Optimization Opportunities

1. Build an inverted index for MyKB search (term→docs) to get O(Q·log D) queries. [Med effort, High gain]
2. Precompute doc-length norms and idf once, cache per server start (currently recomputed per query for
   `tf`). [Low effort, Med gain]
3. Replace the `300-byte title read` inside the scoring loop with a precomputed `titles[]` array (I/O
   reduction). [Low, Low]
4. `contradiction-detector` — hash by normalized answer to prune pairs. [Low, Low]
5. Extrapolation — use a simple linear regression cache keyed by window. [Med, Med]

## 7. Alternative Algorithm Options

| Current | Alternative | When to switch |
|---|---|---|
| Naive TF-IDF | BM25 + FAISS/HNSW | corpus > ~20k docs or sub-50ms SLA |
| Priority aging | Weighted-fair queue / deadline scheduling | many concurrent RSI tasks |
| Extrapolation | ARIMA / quantile regression | needs interval forecasts |
| Regex artifact extraction | LLM-structured output / schema-guided extractor | accuracy demand rises |

---
*End of document 13. Next: [14 Static Code Analysis](14_STATIC_CODE_ANALYSIS.md).*
