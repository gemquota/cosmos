---
type: "concept"
title: "Debugging Methodology"
description: "The systematic process of finding and fixing defects"
tags: ["debugging", "methodology", "root-cause", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Debugging", "https://en.wikipedia.org/wiki/Software_testing"]
---

# Debugging Methodology

## Summary
Debugging methodology is the disciplined process of finding defects: reproduce, form a hypothesis, isolate, verify the fix, and prevent recurrence. It replaces flailing with a repeatable loop that gets faster with practice.

## Details
- Reproduce first: a bug you cannot reproduce you cannot verify fixing; capture inputs and state.
- Form falsifiable hypotheses and test them cheaply — log, instrument, or bisect before guessing.
- Isolate by divide and conquer: binary search the code path, the data, or the history (git bisect).
- Read the error message literally before theorizing; most debugging time goes to unread errors.
- Verify the fix against the original repro, then add a regression test so it stays fixed.
- Postmortem the process: what would have found this bug in minutes?
- For the mykb bundle, debugging includes broken wikilinks, frontmatter validation failures, and sync corruption.

Worked example — a wiki build produces a broken link. Reproduce with the failing article, check the link target exists, bisect which migration broke the path, fix, and add a link-check test to CI.

## Related
- [[wiki/dev-tools/breakpoint-debugging|Breakpoint Debugging]]
- [[wiki/communities/bisect-workflows|Bisect Workflows]]
- [[wiki/software-engineering/static-analysis|Static Analysis]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/dev-tools/core-dumps|Core Dumps]]
- [[wiki/software-engineering/logging-strategies|Logging Strategies]]
- [[wiki/dev-tools/printf-debugging|Printf Debugging]]
- [[wiki/dev-tools/watchpoints|Watchpoints]]
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/dev-tools/git-bisect|Git Bisect]]
