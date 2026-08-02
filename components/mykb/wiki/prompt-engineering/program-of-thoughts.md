---
type: "concept"
title: "Program of Thoughts"
description: "Reasoning technique that expresses reasoning steps as executable program code"
tags: ["program-of-thoughts", "prompting", "code", "reasoning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Program of Thoughts

## Summary
Reasoning technique that expresses reasoning steps as executable program code

## Details
- Model writes code that computes the answer, reducing arithmetic errors.
- Execution results ground the final response.
- Requires a safe code-execution-environment.
- Bridges chain-of-thought and tool use.

## Related
- [[wiki/prompt-engineering/code-prompting|Code Prompting]] — code-focused prompting
- [[wiki/agent-systems/code-execution-environments|Code Execution Environments]] — runtime requirement
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — verbal baseline
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — result capture
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — checking outputs
