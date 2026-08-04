---
type: "entity"
title: "EAGLE"
description: "EAGLE: a speculative decoding method for faster LLM inference"
tags: ["entity", "acronym", "speculative-decoding", "llm", "inference"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# EAGLE

## Summary

EAGLE is a speculative decoding method that accelerates LLM inference by drafting multiple future tokens with a lightweight model and verifying them in one forward pass. It matters because generation latency is dominated by sequential token steps, and speculative methods cut steps while preserving output quality. EAGLE specifically learns a draft head on top of the target model rather than using a separate small model.

## Details

- **Definition** — Speculative decoding drafts candidate continuations and accepts or rejects them using the target model, reducing the number of sequential decoding steps.
- **Drafting** — A draft mechanism proposes several tokens per step; acceptance requires the target model's distribution to match, and rejected tokens are resampled.
- **EAGLE approach** — EAGLE trains an autoregressive draft head conditioned on hidden states, achieving high acceptance rates with modest extra memory.
- **Why it speeds up** — Draft and verify work in parallel or amortize cost: the target model processes several candidates in one pass instead of one token per pass.
- **Worked example** — A draft head proposes four tokens; the target model verifies them at once, accepts three, and decoding continues from the third — four positions for one step.
- **Common failure modes** — Low acceptance rates on unusual text, draft drift that wastes verification compute, and added memory or engineering complexity.
- **Practical relevance** — Latency-sensitive deployments adopt speculative decoding to serve larger models within interactive budgets.
- **Variants** — Lookahead decoding, draft-model approaches, and EAGLE's learned-head family trade memory, implementation effort, and speedup.
- **Telemetry note** — The stub explicitly identifies EAGLE 3.1 as a speculative decoding method, which this note preserves from session d3507371.
- **Acceptance guarantee** — Speculative decoding preserves the target model's distribution exactly when rejection sampling is implemented correctly, so outputs match the baseline.
- **Memory cost** — Draft heads add parameters and hidden-state storage; the speedup must be weighed against the increased memory footprint per request.
- **Worked example** — A chat service runs EAGLE-style drafting at batch size eight, measurably lowering time-to-first-token while keeping answer quality identical to the baseline.
- **Engineering** — Integration spans sampling kernels, KV-cache management, and serving stacks, which is why adoption is usually a framework feature.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/lm-2|LM]] — the models being accelerated
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]] — transformer internals
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/gce-2|GCE]] — managing model context
- [[wiki/testing/agent-evaluations|Agent Evaluations]] — measuring accelerated inference
- [[wiki/concepts/calibration|Calibration]] — verifying output quality
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/gemmaharness|GemmaHarness]] — running model evaluations
