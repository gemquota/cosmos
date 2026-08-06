---
type: "concept"
title: "RAG Benchmarks"
description: "Evaluations for retrieval-augmented generation pipelines covering retrieval and answer quality"
tags: ["rag", "benchmarks", "evaluation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# RAG Benchmarks

## Summary
RAG benchmarks evaluate retrieval-augmented generation pipelines on both halves of the system: how well retrieval finds the right evidence, and how well generation answers from it. Good RAG evals isolate retrieval failures from generation failures so a pipeline regression can be attributed to the right component.

## Details
- **Retrieval metrics** — recall@k, hit rate, and nDCG measure whether the right documents are found; they are computed against a corpus where ground-truth relevant chunks are known.
- **Generation metrics** — faithfulness checks that the answer stays within the retrieved evidence; correctness compares the answer to a reference; both are needed because a fluent answer can ignore its evidence.
- **Datasets** — classic open-domain QA sets (Natural Questions, MS MARCO) plus RAGAS-style metric suites provide corpora, queries, and reference answers; domain-specific suites add realism where the distribution differs.
- **Isolation** — a good harness measures retrieval quality with a fixed reader and generation quality with perfect (oracle) retrieval, so component regressions are separable.
- **Service context** — for evaluation-rag-as-a-service, benchmarks run continuously against pipeline variants: index changes, chunking changes, and reranker changes each get an A/B read.
- **Limits** — benchmark corpora rarely match a production knowledge base, and citation-grounded answers need human verification for subtle errors; benchmarks are a floor, not a complete guarantee.
- **Relationship to other evals** — retrieval quality overlaps with search ranking evaluation; answer quality overlaps with hallucination benchmarks; RAG benchmarks combine the two axes in one pipeline view.

- **Per-component scores** — report chunk-retrieval recall, reranker lift, and answer faithfulness separately; a single blended score can hide a retrieval regression behind a strong reader, and component scores make the fix location obvious.
## Related
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — system under test
- [[wiki/ai-ml/evaluation-rag-as-a-service|Evaluating RAG as a Service]] — service pattern
- [[wiki/ai-ml/hallucination-benchmarks|Hallucination Benchmarks]] — faithfulness axis
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — pipeline variants
- [[wiki/ai-ml/model-evaluation-metrics|Model Evaluation Metrics]] — scoring methods
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — agent-driven retrieval variant
