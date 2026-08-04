---
type: "concept"
title: "Vision-Language Models"
description: "Models that jointly process images and text for captioning, QA, and grounding"
tags: ["vlm", "vision", "multimodal", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Vision-Language Models

## Summary

Vision-language models (VLMs) jointly process images and text for tasks like captioning, visual question answering, and grounding. They align visual and linguistic representations in one network. They matter because they are the foundation for document AI, multimodal agents, and image-based reasoning. VLMs are the perception layer for agents: everything an agent claims to see passes through them.

## Details

- **Definition** — A VLM combines a vision encoder with a language model, letting the model reason about images in natural language.
- **Architecture** — A frozen or trainable vision encoder projects image patches into tokens that the language model attends to.
- **Core tasks** — Captioning, visual QA, referring expressions, and grounding exercise different facets of the same alignment.
- **Instruction following** — Models answer natural-language instructions about images, generalizing beyond fixed benchmark tasks.
- **Multimodal context** — Text, diagrams, screenshots, and video frames can all be mixed into one reasoning context.
- **Failure modes** — Hallucinated objects, brittle OCR on complex layouts, and visual reasoning that is really text priors are key failures.
- **Worked example** — A VLM reads a chart image and answers a question about trends, pointing to the region it based the answer on.
- **Practical relevance** — VLMs are the substrate for OCR, grounding, and any agent that needs to see.
- **Resolution limits** — Downsampled images lose fine detail; high-resolution strategies trade tokens for accuracy.
- **Safety** — Vision inputs can bypass text filters, so VLMs need their own content-safety evaluation.
- **Tool integration** — VLMs paired with tools can inspect regions, zoom, and read documents rather than guessing from one pass.
- **Evaluation** — VLM benchmarks should separate perception from reasoning so failures are attributed to the right stage.

## Related

- [[wiki/llm-agents/grounding-vision-to-text|Grounding Vision to Text]] — verifiable visual claims
- [[wiki/llm-agents/ocr-and-document-ai|OCR and Document AI]] — document applications
- [[wiki/llm-agents/multimodal-evaluation|Multimodal Evaluation]] — evaluating VLMs
- [[wiki/llm-agents/cross-modal-retrieval|Cross-Modal Retrieval]] — searching with VLMs
- [[wiki/llm-agents/interleaved-modalities|Interleaved Modalities]] — mixed-media sequences
