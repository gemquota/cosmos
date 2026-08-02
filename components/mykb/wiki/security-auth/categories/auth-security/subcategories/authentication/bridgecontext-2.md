---
type: "entity"
title: "BridgeContext"
description: "Context"
tags: ["ajax", "android", "api", "ast", "auth", "authentication", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
status: "growing"
---

## Bridgecontext 2

Context — the information provided to an LLM alongside a query. Sessions show context window management, summarization, and pruning strategies.

For a large language model, context is everything in the prompt beyond the immediate instruction: prior conversation turns, retrieved documents, tool outputs, and system guidance. The model conditions every response on that context, so its quality bounds the quality of the answer. Context windows are measured in tokens, and managing those tokens — deciding what to include, in what order, and for how long — is a core engineering discipline in agent and chat applications.

The strategies named on this page form a practical toolkit. Summarization compresses older turns into a running digest, trading fidelity for space. Pruning drops turns that stop mattering — tool noise, resolved sub-tasks, or duplicate results — while preserving the decisions they led to. Retrieval, as in RAG, pulls the most relevant passages in only when needed, keeping the window lean without losing knowledge. Together they let a session run long without silently truncating the oldest and most important instructions.

Ordering also matters: recent instructions and the current task usually carry the most weight, so systems place critical guidance near the end, and some models degrade when relevant material sits mid-prompt. Instrumentation — tracking token counts, evictions, and summaries — turns context management from guesswork into a measurable policy.

This page records the concept so future sessions can attach the specific budgets, summarization passes, and eviction rules implemented in the agent stack. These policies are most useful when they are versioned with the system they govern.

**Related topics:** ajax, android, api, auth, authentication

**Domain:** Web Platforms › [[wiki/web-platforms/index|Security Auth]] › [[wiki/web-platforms/index|Auth Security]] › Bridgecontext 2

## Related Entities

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/automatic-10|Automatic 10]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]
