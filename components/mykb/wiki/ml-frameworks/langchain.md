---
type: "concept"
title: "LangChain"
description: "A framework for composing LLM applications: chains, agents, retrieval, and integrations"
tags: ["langchain", "llm", "framework", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# LangChain

## Summary
LangChain is a popular application framework that standardizes LLM building blocks — model wrappers, prompts, retrieval, chains, and agent loops — across dozens of providers. It accelerates prototyping and carries a large integration ecosystem.

## Details
- Core abstractions: models, prompts, parsers, retriever, chains, agents, and callbacks.
- LangSmith adds tracing and evaluation for the same workflows.
- Criticisms: abstraction overhead and churn; many teams end up with thin custom layers.
- RSIS3 relevance: RSIS3's own loop is comparable to LangChain agents but purpose-built for RRP; patterns port across.

## Related
- [[wiki/ml-frameworks/llamaindex|LlamaIndex]] — The retrieval-focused sibling framework
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — The pattern chains implement
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern LangChain standardizes
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Agent tool loops in the framework
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — MCP integration in LangChain
