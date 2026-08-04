---
type: "entity"
title: "TransformPluginContext"
resource: ""
---
description: "The context object passed to build plugins for transforming modules"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "build-tools", "plugins"]
timestamp: "2026-07-19T22:41:43Z"

# TransformPluginContext

## Summary
A transform plugin context is the object passed to a build-tool plugin when it transforms a module, carrying the source, metadata, and utility methods. It matters because modern bundlers are extended through such plugins, and the context defines what a plugin may do. Understanding the context is how teams write correct, efficient transforms and debug build pipelines.

## Details
- **Definition** — the context bundles the module's source, id, and metadata, plus helpers for emitting warnings, resolving, and sharing state.
- **Source handling** — plugins read and return source text, optionally changing it, so transforms compose into a pipeline.
- **Virtual modules** — plugins can synthesize modules that do not exist on disk, enabling features such as inlining and injection.
- **Warnings and errors** — the context provides structured ways to surface issues that integrate with the build log.
- **Shared state** — contexts let plugins persist data across modules in a build, enabling whole-bundle reasoning.
- **Performance** — transforms run per module, so plugins must avoid unnecessary parsing and heavy per-file work.
- **Common failure modes** — mutating shared state unsafely, producing source that breaks downstream parsers, and transforms that ignore error conditions.
- **Worked example** — a plugin rewrites import paths in each module's source using the context's resolver, then returns the modified code.
- **Practical relevance** — transform contexts are the seams where bundler ecosystems are extended and customized.

- **Errors** — plugins should report errors with module context so users can locate the failing file quickly.
- **Caching** — expensive transforms should be cached keyed by input hash to avoid rework in incremental builds.
- **Composition** — transform order matters; plugins should be designed to compose predictably with others.
## Related
- [[wiki/js-ts-ecosystem/vite-practice|Vite Practice]] — plugin model
- [[wiki/js-ts-ecosystem/webpack-practice|Webpack Practice]] — loader context
- [[wiki/js-ts-ecosystem/rollup-practice|Rollup Practice]] — transform hooks
- [[wiki/js-ts-ecosystem/esbuild-practice|esbuild Practice]] — fast transforms
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]] — ecosystem
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — module formats
