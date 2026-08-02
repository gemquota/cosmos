---
type: "concept"
title: "Prompt Debugging"
description: "Systematic techniques for diagnosing why a prompt produces bad outputs"
tags: ["prompt-debugging", "prompts", "debugging", "techniques"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prompt Debugging

## Summary
Systematic techniques for diagnosing why a prompt produces bad outputs

## Details
- Isolate variables: model, temperature, context, and formatting.
- Compare against golden-test-sets for signal.
- Use traces to inspect prompt composition.
- Precedes prompt-testing automation.

## Related
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — automated checks
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — change tracking
- [[wiki/testing/golden-test-sets|Golden Test Sets]] — regression data
- [[wiki/prompt-engineering/prompt-templates|Prompt Templates]] — structure
- [[wiki/agent-systems/agent-run-inspectors|Agent Run Inspectors]] — run inspection
