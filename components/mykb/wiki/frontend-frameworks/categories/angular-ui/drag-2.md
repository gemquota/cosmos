---
type: "entity"
title: "DRAG"
description: "RAG (Retrieval-Augmented Generation)"
tags: ["acronym", "android", "angular", "api", "ast", "bash", "cli", "css", "dom", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Drag 2

RAG (Retrieval-Augmented Generation) — a pattern combining information retrieval with LLM generation for knowledge-grounded responses.

RAG addresses the weaknesses of a language model that only knows what it saw during training: stale knowledge, missing private data, and confident fabrication. Instead of relying on memory alone, the system retrieves relevant documents at query time and supplies them to the model as context, so the answer is grounded in the retrieved text.

The pipeline has three main stages. First, the knowledge base is prepared: documents are split into chunks of a size that fits retrieval and generation, and each chunk is embedded into a vector space. Second, at query time the question is embedded and the nearest chunks are found in the vector store, often supplemented by keyword search in a hybrid approach. Third, the model generates an answer conditioned on the question and the retrieved chunks, with citations pointing back to sources.

Design choices shape quality: chunk size and overlap affect whether facts survive intact, embedding models determine what counts as similar, and the number of retrieved chunks trades context budget against coverage. Retrievers are evaluated with hit-rate and ranking metrics, and the whole pipeline with answer-level quality checks and faithfulness judgments.

RAG reduces hallucinations by forcing the model to answer from provided text, and it makes updating knowledge as simple as re-indexing. It is a core building block of agent systems, complementing the [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/autonomous-iterative-mode-2|Autonomous Iterative Mode 2]] and related entries in the [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/index|Angular Ui]] domain.

The entry sits under Angular UI because sessions encountered RAG while building agent-driven interfaces, and the same retrieval pipeline serves chat, search, and reporting features.

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/index|Angular Ui

## Related Entities

- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/aim-2|Aim 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/autonomous-iterative-mode-2|Autonomous Iterative Mode 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/avg-age-2|Avg Age 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/avg-energy-2|Avg Energy 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/batch-2|Batch 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/dna-10|Dna 10
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/harmonica-explorer-2|Harmonica Explorer 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/hidpi-2|Hidpi 2
