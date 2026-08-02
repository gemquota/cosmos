---
type: "concept"
title: "Webpack Concepts"
description: "Loaders, plugins, chunks, and configuration model"
tags: [webpack", "bundlers", "build-tools", "javascript", "configuration"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://webpack.js.org/concepts/", "https://webpack.js.org/loaders/"]
---

# Webpack Concepts

## Summary
webpack is a configuration-driven module bundler built around a few core concepts: entry, output, loaders, plugins, and mode. Loaders transform files before they enter the graph, plugins extend the pipeline with optimizations and custom behavior, and the config file declares everything. It powers most of the legacy React and Vue tooling ecosystem.

## Details
- Entry and output: entry declares the graph root; output controls bundle filenames, paths, and public URLs.
- Loaders: module.rules map file types to transforms — babel-loader, ts-loader, css-loader, and sass-loader.
- Plugins: HtmlWebpackPlugin, MiniCssExtractPlugin, and DefinePlugin hook into compilation lifecycle events.
- Mode: development enables source maps and fast rebuilds; production enables minification and tree shaking.
- Chunks: splitChunks separates vendor and shared code; runtimeChunk isolates the bootstrap; contenthash caches safely.
- Dev server: webpack-dev-server serves with live reload and hot module replacement, proxying APIs in development.
- Modern role: newer tools use webpack's concepts with simpler defaults; webpack remains ubiquitous in existing codebases.

## Related
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the family webpack belongs to
- [[wiki/frontend/code-splitting|Code Splitting]] — splitChunks in practice
- [[wiki/frontend/tree-shaking|Tree Shaking]] — production-mode dead code removal
- [[wiki/frontend/dev-server|Dev Server]] — webpack-dev-server behavior
- [[wiki/frontend/hot-module-replacement|Hot Module Replacement]] — webpack's HMR model
- [[wiki/frontend/bundle-analysis|Bundle Analysis]] — analyzing webpack output
