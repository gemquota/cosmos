---
type: "concept"
title: "Context Injection"
description: "Inserting retrieved or computed context into prompts at the right position and granularity"
tags: ["context-injection", "context", "rag", "prompting"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Context Injection

## Summary

Context injection is the practice of inserting retrieved or computed information into a prompt at the right position and granularity so the model can ground its response in it. It is the prompting half of retrieval-augmented generation and agent memory. Context injection matters because what is injected, where it sits, and how it is framed determines whether the model uses the information correctly or ignores it. Injection design is about control: deciding what enters the context is a policy decision, not just a mechanical step.

## Details

- **Definition** — context injection places external knowledge — documents, tool results, memory — into the prompt before generation.
- **Position effects** — instructions and injected content have different salience at the start and end of context; placement affects adherence.
- **Granularity** — injecting too much dilutes relevance; too little starves the answer; selection and trimming are part of the craft.
- **Framing** — labeling injected content ("Use the following documents:") and adding usage rules improves grounding.
- **Retrieval link** — injection is the delivery mechanism for retrieval-prompting pipelines and RAG systems.
- **Security** — untrusted injected content can carry prompt injection payloads, so separation and sanitization matter.
- **Worked example** — a Q&A system retrieves three passages, labels them, and tells the model to answer only from them with citations.
- **Failure modes** — context overload, conflicting instructions, injection attacks, and stale content are the main risks.
- **Practical relevance** — context injection is central to agents, RAG, and any grounded generation system.
- **Relation to context engineering** — injection is one lever within the broader design of what context enters the model and why.
- **Source labeling** — telling the model which parts of the prompt are retrieved data and which are instructions reduces confusion and injection risk.


## Related

- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — the retrieval pipeline
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — the design discipline
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — the security layer
- [[wiki/prompt-engineering/agentic-context-crafting|Agentic Context Crafting]] — agent-context design
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — the grounding goal
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — the budget control

