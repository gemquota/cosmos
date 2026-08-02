---
type: "concept"
title: "Blame"
description: "Finding which edit introduced a line"
tags: ["blame", "history", "edits", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Blame

## Summary
Blame attributes each line of an article to the edit (and editor) that introduced it, answering 'who wrote this and when'.

## Details
- It is the first stop when a questionable claim appears: blame finds the edit, the summary explains the intent, and the diff shows the context.
- Blame is a lens on history, not a verdict — the blamed editor may have inherited the line from elsewhere.
- For mykb, blame supports accuracy review and is the wiki analog of git-blame workflows.

## Related
- [[wiki/dev-tools/blame-wiki|Blame]]
- [[wiki/dev-tools/page-history|Page History]]
- [[wiki/dev-tools/revision-compare|Revision Compare]]
- [[wiki/concepts/contrib-history|Contribution History]]
- [[wiki/concepts/accuracy-score|Accuracy Score]]
- [[wiki/dev-tools/git-bisect|Git Bisect]]
