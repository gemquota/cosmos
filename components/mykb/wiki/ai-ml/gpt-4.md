---
type: "entity"
title: "GPT-4"
description: "OpenAI's flagship multimodal LLM family, the reference point for frontier capabilities and evaluation"
tags: ["gpt-4", "openai", "llm", "models"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# GPT-4

## Summary
GPT-4 is OpenAI's large multimodal model family spanning text and image understanding, with strong reasoning, coding, and instruction-following. It defines the capability baseline most production systems compare against, and the technical report's evaluation methodology set the template for public model documentation.

## Details
The GPT-4 technical report (2023) set a new standard for how frontier models were evaluated and disclosed, publishing results across professional and academic benchmarks while deliberately withholding architecture and training details. The pattern that emerged — broad benchmark reporting, capability-limits discussion, and selective transparency — became the de facto template for later frontier releases, for better and worse.

The variant ecosystem is the practical surface most teams interact with: chat-tuned models for conversational workloads, vision-capable variants that accept images, tool-calling support for agentic flows, and successive generations that improve reasoning and long-context behaviour while keeping the same API shape. Pricing and context options vary by tier, so token-budget planning is essential; an application tuned for one tier can see its cost or latency profile change materially when the tier changes.

Operationally, GPT-4-class models behave differently from smaller open models in ways that matter for production: they follow complex instructions with fewer restarts, handle multi-step tool sequences more reliably, and are substantially better at self-correcting when given error feedback. The failure modes are still real — occasional instruction drift on very long prompts, over-verbosity, and sensitivity to ambiguous tool schemas — but the error rates are lower, which is exactly why they anchor agent baselines.

RSIS3 relevance: RSIS3 dashboards and evals frequently benchmark against GPT-4-class models as the frontier reference, and mykb should record the exact model version, eval set, and date behind any comparison so that scores remain interpretable as the family evolves.

## Related
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The interface to the model family
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — The planning discipline behind it
- [[wiki/testing/eval-sets|Eval Sets]] — The benchmarks it is scored on
- [[wiki/prompt-engineering/function-calling|Function Calling]] — A flagship GPT-4 capability
- [[wiki/ai-ml/benchmark-gaming|Benchmark Gaming]] — Controversies around its benchmark claims
