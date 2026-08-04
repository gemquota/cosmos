---
type: "concept"
title: "While"
description: "While loops: repetition control flow in scripting, CLI tools, and agent loops"
tags: ["entity", "ast", "bug", "cli", "edge", "ide", "loops"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# While

## Summary

A while loop repeats a block of code as long as a condition holds true. It is a fundamental control-flow construct in every scripting language and CLI tool. Understanding loop semantics matters because loops are where both powerful automation and subtle bugs, like infinite loops and off-by-one errors, live. Getting loop semantics right is a prerequisite for writing safe automation.

## Details

- **Definition** — A while loop evaluates a condition before each iteration and continues until the condition becomes false.
- **Pre-test semantics** — Because the condition is checked first, a while loop may run zero times, unlike a do-while loop that always runs once.
- **Loop variables** — Loops need progress: the body must eventually change state that affects the condition, or the loop never terminates.
- **Infinite loops** — A condition that never turns false, or state that never changes, hangs the program; timeouts and iteration caps are standard guards.
- **Invariants** — A loop invariant is a property true before and after each iteration; stating it helps prove the loop does what it claims.
- **Worked example** — A CLI retry loop polls an endpoint while attempts remain and the response is not ready, sleeping between checks.
- **Variants** — For loops, for-each loops, and recursion are alternative iteration styles; each fits a different data shape.
- **Failure modes** — Off-by-one boundaries, busy-wait loops that burn CPU, and mutation during iteration are the classic bugs.
- **Practical relevance** — Agentic systems generalize the same idea: a loop with a stop condition is the skeleton of every autonomous run.
- **Early exit** — Break and continue statements reshape loop flow; using them sparingly keeps bodies readable.
- **Iteration limits** — A maximum iteration count converts a potential hang into a handled failure with a clear message.
- **State observation** — Printing loop state at debug time, or capturing it in logs, makes terminating bugs diagnosable.

## Related

- [[wiki/development/categories/cli-tools/dev|Dev]] — scripts where loops live
- [[wiki/development/categories/cli-tools/cognitive|Cognitive]] — loop structure and mental load
- [[wiki/development/categories/cli-tools/reality|Reality]] — verifying loop outcomes
- [[wiki/development/categories/cli-tools/performance|Performance]] — loop efficiency
- [[wiki/development/categories/cli-tools/sovereign-orchestrator|Sovereign Orchestrator]] — orchestration loops
