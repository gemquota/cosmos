---
type: "concept"
title: "Static Analysis Agents"
description: "Agents that review code without executing it to find bugs and smells"
tags: ["static-analysis-agents", "code", "analysis", "review"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Static Analysis Agents

## Summary
Static analysis agents review code without executing it, combining parsers, linters, and type checkers with language model reasoning to find bugs and smells. They matter because many defects are visible in structure long before runtime, and catching them early is far cheaper. The challenge is separating real issues from false positives. Static analysis is strongest when deterministic tools and model judgment reinforce each other.

## Details
- **Definition** — a static analysis agent inspects source code for defects, style violations, and risky patterns using both deterministic tools and model judgment.
- **Mechanism** — agents run linters, type checkers, and AST-based rules, then apply language-model reasoning to prioritize and explain findings.
- **Complementarity** — static checks catch issues before runtime, complementing dynamic tests that find behavioral failures.
- **Triage** — false positives need triage by models or humans; an agent that cries wolf too often loses trust and gets ignored.
- **Worked example** — a review agent flags an unused variable, a missing null check, and a security-sensitive function call, each with a suggested fix and reasoning.
- **Failure modes** — high false-positive rates, shallow pattern matching, and missed context-dependent issues are the main weaknesses.
- **Evaluation** — static analysis quality is measured by precision and recall against labeled code-review findings.
- **Practical relevance** — static analysis agents slot into code-review pipelines and feed code-repair-agents with structured findings.
- **Rule integration** — deterministic rules anchor the analysis while the model explains and prioritizes findings.
- **Security focus** — static agents are a natural home for vulnerability scanning of dependencies and patterns.
- **Worked example** — a pull-request agent runs lint and type checks, then summarizes the actionable issues with fixes.
- **Failure example** — a static agent that flags every style nit buries the one real bug in noise.

## Related
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — the fixer counterpart
- [[wiki/agent-systems/testing-agents|Testing Agents]] — the dynamic complement
- [[wiki/agent-systems/code-generation-agents-revisited|Code Generation Agents]] — the producer of analyzed code
- [[wiki/ai-ml/code-benchmarks|Code Benchmarks]] — the quality bar for code skills
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]] — where review stages integrate
