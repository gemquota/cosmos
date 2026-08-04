---
type: "concept"
title: "LM"
description: "Language model: a model trained to predict and generate natural language"
tags: ["entity", "acronym", "llm", "language-model", "generation"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# LM

## Summary

LM is an acronym for language model, a statistical model trained to predict plausible continuations of text and, in larger form, to power chat, coding, and reasoning agents. Language models matter because they have become the substrate for assistants, tool use, and recursive self-improvement pipelines. The term spans everything from small n-gram predictors to frontier transformers.

## Details

- **Definition** — A language model assigns probabilities to sequences of tokens; sampling from those probabilities generates new text.
- **Scale spectrum** — Small models run on phones for autocomplete; large models with billions of parameters handle complex instruction following and tool orchestration.
- **Training signal** — Next-token prediction on large corpora is the core objective, refined by instruction tuning and preference optimization for helpfulness.
- **Context handling** — Models consume a limited context window; prompt construction and retrieval determine whether relevant knowledge is available at generation time.
- **Worked example** — A coding assistant receives a failing test, generates a fix, and explains the change — the LM conditions each token on the full conversation history.
- **Common failure modes** — Hallucination of unsupported facts, overconfidence in wrong answers, and sensitivity to prompt phrasing are persistent limitations.
- **Practical relevance** — In agent systems, the LM is the reasoning core, so its reliability, cost, and latency dominate system design.
- **Variants** — Encoder-only models specialize in understanding, decoder-only models in generation; multimodal LMs extend the same machinery to images and audio.
- **Telemetry note** — The stub records LM as an acronym from session d3507371; the language-model reading matches the agent-heavy context where it appeared.
- **Prompting** — Instruction placement, few-shot examples, and output constraints steer generation; small phrasing changes can flip results.
- **Evaluation** — Automated metrics, human review, and reference comparisons each capture different aspects of quality, and none alone is sufficient.
- **Latency and cost** — Token generation cost and latency scale with output length, so engineering uses caching, constrained decoding, and shorter targets.
- **Worked example** — A support bot conditions on the ticket, retrieves policy snippets, and drafts a reply that a human approves before sending.

## Related

- [[wiki/llm-agents/success-criteria|Success Criteria]] — judging model output
- [[wiki/concepts/calibration|Calibration]] — confidence and accuracy
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/gce-2|GCE]] — managing model context
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]] — models inside loops
- [[wiki/concepts/superforecasters|Superforecasters]] — human calibration comparison
- [[wiki/concepts/bayesian-updating-practice|Bayesian Updating Practice]] — probabilistic reasoning with models
