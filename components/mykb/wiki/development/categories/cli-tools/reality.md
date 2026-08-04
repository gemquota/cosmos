---
type: "entity"
title: "Reality"
description: "Reality: grounding work in actual system state rather than assumptions"
tags: ["entity", "ast", "bug", "cli", "edge", "ide", "ground-truth"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Reality

## Summary

Reality, in this cluster, means the actual state of the system as opposed to assumptions, plans, or documentation about it. Debugging and agentic work both fail when they argue from belief instead of evidence. Checking reality first is the cheapest way to avoid large misdirected efforts. Reality checking is the discipline that keeps both humans and agents honest about system behavior.

## Details

- **Definition** — Reality is ground truth: the files, processes, logs, and outputs that exist right now, independent of what anyone expects.
- **Evidence first** — Reproducing a problem and reading the actual error beats hypothesizing about causes; evidence narrows the search space.
- **State inspection** — CLI tools that print current state, such as process listings and file contents, are the instruments of reality checking.
- **Assumption drift** — Documentation and memory decay, so long-lived projects accumulate claims that no longer match the code.
- **Verification loops** — Each fix should be confirmed against the observed failure, closing the loop between change and evidence.
- **Failure modes** — Debugging from stale logs, trusting memory over current output, and fixing symptoms without reproducing the cause waste hours.
- **Worked example** — A failing build is traced by running it, reading the first real error, and fixing that line; the rebuild then verifies the fix.
- **Practical relevance** — Agents that consult tool output instead of guessing are dramatically more reliable, which is why grounding is a design principle here.
- **Minimal reproduction** — Shrinking a failure to the smallest command that triggers it isolates the responsible component.
- **Bisection** — Halving the change or input range repeatedly finds the introducing commit or condition.
- **Environment parity** — Reproducing on the same environment, or documenting the differences, explains most unreproducible bugs.

## Related

- [[wiki/development/categories/cli-tools/technical-reality|Technical Reality]] — verifying what systems actually do
- [[wiki/development/categories/cli-tools/dev|Dev]] — day-to-day development practice
- [[wiki/development/categories/cli-tools/cognitive|Cognitive]] — mental models versus evidence
- [[wiki/development/categories/cli-tools/state-isolation|State Isolation]] — keeping observed state trustworthy
