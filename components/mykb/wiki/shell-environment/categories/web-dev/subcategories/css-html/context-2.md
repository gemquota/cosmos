---
type: "entity"
title: "Context"
description: "Context"
tags: ["ast", "bash", "bug", "ci/cd", "cli", "css", "dom", "edge", "entity", "ide"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
status: "growing"
---

## Context 2

Context — the information provided to an LLM alongside a query. Sessions show context window management, summarization, and pruning strategies.

**Related topics:** bash, bug, ci/cd, cli, css, dom, edge, ide

**Domain:** OS & Shell › [[wiki/web-platforms/index|Shell Environment]] › [[wiki/web-platforms/index|Web Dev]] › Context 2

## Overview

Context, in the LLM sense, is the information supplied to a model alongside the current query: system instructions, conversation history, retrieved documents, and tool results. It determines both the quality of the output and its cost, since everything in the window is processed as tokens. The page was recorded in a session tagged bash, css, dom, ide, and more, where context engineering is a daily concern.

## Context Windows

A context window is the fixed number of tokens the model can attend to at once. Content beyond the limit must be truncated, summarized, or omitted, so window management is a design task, not an afterthought. Applications budget the window among system prompt, history, retrieval results, and the space reserved for the model's reply.

## Management Strategies

Common strategies are summarization (compress old turns into a short digest), pruning (drop turns that no longer matter), and retrieval (pull in only the passages relevant to the current query). Ordering matters: instructions near the ends of the window often influence output more than material in the middle. Utilities that count tokens and enforce budgets make these strategies practical.

## Engineering Trade-offs

More context improves fidelity but raises cost and latency and can dilute attention. Teams measure whether added context changes outcomes before paying for it, using evaluation sets and A/B comparisons. The related entities in this branch — analysis-2, budget, engine-telemetry-core — record the tooling and analysis around these trade-offs.

## Related Entities

- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/analysis-2|Analysis 2]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/budget|Budget]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/canvas|Canvas]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/chemical-playground|Chemical Playground]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/defi|Defi]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/diffusion-simulator|Diffusion Simulator]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/engine-telemetry-core|Engine Telemetry Core]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/fields|Fields]]
