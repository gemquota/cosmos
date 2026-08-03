---
type: "entity"
title: "Context Efficiency"
description: "Using an LLM context window productively: relevant tokens, minimal waste"
tags: ["entity", "context", "llm", "efficiency", "prompting"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Context Efficiency

## Summary

Context efficiency is the practice of getting the most value from a language model's finite context window — packing in what matters, removing what does not. It matters because context is a hard budget: overflowing it truncates instructions, and wasting it on noise degrades output quality. Efficiency is achieved through curation, compression, and retrieval.

## Details

- **Definition** — Every token in the context competes for attention and window space; efficiency maximizes signal per token.
- **Curating** — Selecting the relevant documents, conversation turns, and tool results beats stuffing everything in and hoping the model copes.
- **Compressing** — Summaries, extracted facts, and structured digests shrink verbose material while preserving the load-bearing content.
- **Retrieval** — Retrieval-augmented pipelines fetch only what the current task needs, trading a search step for a smaller, better context.
- **Worked example** — A long debugging session is reduced to the error trace, the changed files, and a one-paragraph summary before the next model call.
- **Common failure modes** — Context overflow that silently drops system instructions, duplicate information that biases answers, and over-compression that loses critical detail.
- **Practical relevance** — Cost and latency scale with tokens, so efficiency is a budget lever as well as a quality lever.
- **Variants** — Sliding windows, hierarchical summaries, and key-value memories are different architectures for keeping context fresh.
- **Telemetry note** — Recorded in API and cloud sessions, consistent with cost- and latency-sensitive agent deployments.
- **Prioritization** — Instructions and recent, task-relevant facts belong near the end of the prompt where models attend most reliably.
- **Measurement** — Tracking token counts, truncation events, and answer quality per task quantifies whether context changes actually help.
- **Worked example** — A support agent context keeps the policy summary and current ticket, evicting resolved threads; truncation events dropped to zero and first-answer accuracy rose.
- **Trade-offs** — Compression costs fidelity and retrieval costs latency; the right mix depends on the task and budget.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/gce-2|GCE]] — the context engineer role
- [[wiki/concepts/working-memory|Working Memory]] — the cognitive analogue
- [[wiki/concepts/cognitive-load|Cognitive Load]] — limits on held information
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ingestioncontext-2|IngestionContext]] — how context enters
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/promptsession-2|PromptSession]] — the context container
- [[wiki/concepts/selective-attention|Selective Attention]] — choosing what to process
