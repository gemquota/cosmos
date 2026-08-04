---
type: "concept"
title: "Prompt Repositories"
description: "Versioned storage and review workflows for prompts as code"
tags: ["prompt-repos", "prompts", "versioning", "repos"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Prompt Repositories

## Summary

Prompt repositories are versioned storage and review systems that treat prompts as code: stored in files, diffed, reviewed, tested, and deployed through pipelines. They give prompt engineering the same discipline that source control gives software. Repositories matter because prompts are live artifacts whose changes affect production behavior, and untracked prompt changes are untraceable failures waiting to happen. The repository is the single source of truth for what the system says, which makes audits and rollbacks straightforward.

## Details

- **Definition** — a prompt repository stores prompt definitions, templates, metadata, and versions in a reviewable, deployable structure.
- **Prompts as code** — prompts live in version control, inherit change history, and go through code review before release.
- **Metadata** — entries carry purpose, owner, model compatibility, test results, and usage notes for maintainability.
- **Review workflow** — changes are proposed, reviewed, and tested against golden sets before merging.
- **Deployment** — repositories connect to serving pipelines so the tested version is the shipped version.
- **Worked example** — a team keeps prompts in a repository with a CI job that runs prompt tests on every merge, catching a regression before release.
- **Failure modes** — prompts hidden in notebooks, undocumented changes, and repositories without tests recreate the chaos they are meant to prevent.
- **Practical relevance** — repositories are the backbone of LLMOps, enabling rollback, auditing, and collaboration.
- **Relation to libraries** — libraries curate usable prompts; repositories provide the storage and review infrastructure.
- **Measurement** — healthy repositories track version history, test coverage, and rollback frequency.
- **Ownership** — assigning an owner per prompt ensures that drift, breakage, and review requests have a clear responder.


## Related

- [[wiki/prompt-engineering/prompt-libraries|Prompt Libraries]] — the curated collection
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — the version discipline
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — the quality gate
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — the model analog
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — the deployment pipeline
- [[wiki/prompt-engineering/prompt-debugging|Prompt Debugging]] — the change driver

