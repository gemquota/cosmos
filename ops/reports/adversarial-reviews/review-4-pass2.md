# Adversarial Review #4 (Pass 2) — MyKB Stub Promotion Wave, post-cleanup re-review

Reviewer: adversarial reviewer #4. Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice4.txt` (219 paths under `components/mykb/wiki/`; areas: identity, infrastructure, js-ts-ecosystem, llm-agents, memory, meta-learning, ml-frameworks, os-shell).

## Verdict

**Health score: 68 / 100**

The hard invariants hold again in this slice: 217/219 files pass the checker, both flagged items are false positives, no file is missing or below the 320-body-word floor, all frontmatter keys and `status: growing` are present, and there are no self-links, no unclosed links, no dead README links, and no `raw/archive` stragglers. Most of the Pass 1 fixes landed and are verifiable in this slice: all 6 self-links are gone, the "related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" strings are gone (0 hits), the duplicate cross-links in `federated-components.md`/`module-federation.md` are deduped, the Summary-into-Details duplication is gone, and the one in-slice factual fix (`gpu-drivers-and-cuda.md`) is now correct. **But the Pass 1 fixes did not fully hold:** the cleanup item "removed the fixed syntheses trailer" did not land here — 80/219 files still carry the two trailer lines verbatim, exactly the 80 files Pass 1 counted. Worse, the "related coverage" cleanup stripped the boilerplate descriptions but left the topically irrelevant targets in place, so 98/219 files now end in bare, link-padding Related rows (OSPF Protocols, Storage Systems, WireGuard) with no description at all — a cleanup-induced regression in link quality. The defect classes deliberately left unfixed are still at high prevalence and were re-measured: 61/219 files contain unverifiable "the wiki's / the loop's" system-behavior claims (several contradicted by a repo scan), 55/219 files carry keyword-matched irrelevant padding links, and a large cluster of files sits at 320-338 words, consistent with topping-up to threshold. Content accuracy of the actual prose remains genuinely good — I found no fabricated papers, models, APIs, or URLs, and the strongest files (identity cluster, `retry-with-backoff`, `awk-text-processing`, `evpn-bgp-evpn`) are excellent reference notes. The score is down slightly from Pass 1 (71) because a headline cleanup item did not land and the description-stripping produced a net regression in the slice's largest defect area.

## Critical findings

1. **The fixed syntheses trailer was NOT removed — still verbatim in 80/219 files (confirmed).**
   Pass 2's stated cleanup includes "removed the fixed syntheses trailer". It did not land in this slice. The exact two lines Pass 1 quoted are still present in the same 80 files, e.g. `infrastructure/erasure-coding.md` lines 25-26:
   > `- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb`
   > `- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to`
   Identical rows appear in `infrastructure/bandwidth-allocation.md`, `infrastructure/bufferbloat-and-queueing.md`, `infrastructure/precision-time-protocol.md`, `os-shell/btrfs-features-and-limitations.md`, `os-shell/cron-and-scheduled-tasks.md`, `infrastructure/evpn-bgp-evpn.md`, `infrastructure/nvme-multipath.md`, `infrastructure/nvme-over-fabrics-tcp.md`, and 72 more. The trailer claims every one of these topics is "a stub" that belongs to "the curation loop" — false for pages like `precision-time-protocol.md` (a substantive, topically unrelated page). This is word-stuffing-by-template and pollutes the graph with two synthetic edges per file. Fix: delete both rows from all 80 files (the cleanup intended to do exactly this and missed the whole slice).

2. **Cleanup regression: 98/219 files now end in bare, still-irrelevant Related rows (confirmed).**
   The cleanup stripped the "related coverage in the same cluster" descriptions but did not evaluate the link targets, leaving rows with no description and no topical connection. `infrastructure/bufferbloat-and-queueing.md` now ends:
   > `- [[wiki/infrastructure/storage-systems|Storage Systems]]`
   > `- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]`
   A page about bufferbloat and AQM linking to OSPF and Storage Systems with zero annotation is worse than the boilerplate version: the link count is unchanged, the relevance is unchanged, and the reader gets no hint of why the edge exists. The 98-file count matches Pass 1's count of files with the boilerplate almost exactly, so the cleanup replaced one bad form with another. 55/219 files specifically retain OSPF/Storage Systems/WireGuard rows (e.g. `infrastructure/precision-time-protocol.md` links `[[wiki/cloud-infra/wireguard-protocol|WireGuard Protocol]]`; `infrastructure/evpn-bgp-evpn.md` links `[[wiki/infrastructure/storage-systems|Storage Systems]]`). Fix: delete or replace the rows with topically related targets and add one-clause descriptions, matching the identity/memory clusters' Related style.

3. **"The wiki's tool registry is the single source of truth for agent capabilities" — unverifiable system assertion presented as fact (confirmed unverifiable, likely false).**
   `llm-agents/tool-registry.md`: "RSIS3/mykb relevance: the wiki's tool registry is the single source of truth for agent capabilities, and the loop's permission model reads from the same metadata." A repo scan (`rg -i "tool.?registr"` across `components/rsis3` and `components/mykb` excluding markdown) finds no tool registry in code — only JSON indexes that mirror the wiki page itself. There is no evidence the system has a tool registry, so this sentence asserts product behavior that cannot be verified and appears not to exist. This is the fabrication class the review is hunting for, just under a softer verb ("the wiki's X does Y"). Fix: rewrite as design intent ("a registry would be the single source of truth…") or delete the row.

## Major findings

1. **Unverifiable "the wiki's / the loop's / mykb's X does Y" claims — 61/219 files (re-measured, deliberately not fixed).** Beyond the tool-registry case, the same class recurs:
   - `llm-agents/prompt-caching.md`: "the wiki's loop prompts keep static system/tool prefixes stable so long sessions reuse caches, and cost telemetry tracks the savings." No prompt-caching or prefix-stability mechanism was found in `components/rsis3` code.
   - `js-ts-ecosystem/esbuild-practice.md`: "RSIS3 relevance: the dashboard's JS build is a prime esbuild candidate — near-instant rebuilds keep the loop fast." The dashboard (`components/rsis3/dashboard/index.html`) is static HTML with Tailwind and Chart.js; there is no JS build pipeline, so "the dashboard's JS build" describes something that does not exist.
   - `js-ts-ecosystem/import-maps.md`: "RSIS3 relevance: the dashboard could use an import map for its few external dependencies…" — speculative and hedged, but placed in the same slot as factual claims.
   - `ml-frameworks/pytorch.md`: "It is the framework most models in the wiki's stack are trained and fine-tuned with." Unverifiable from the wiki's own content; the wiki also documents JAX, TensorFlow, and local runtimes as first-class.
   - `meta-learning/delay-of-gratification.md`: "mykb's scheduling should budget for long-horizon tasks the same way a saver budgets for retirement." An editorial opinion inside a research summary.
   These are the Pass 1 "provenance" class; the cleanup explicitly left them, but they remain the second-largest source of unverifiable content in the slice.

2. **Keyword-matched irrelevant padding links — 55/219 files.** Re-measured after the description strip: OSPF Protocols appears in pages about erasure coding, bufferbloat, IPFS, and GPU drivers; Storage Systems appears in EVPN, tcpdump, PTP, NVMe, and GPU pages; WireGuard appears in `precision-time-protocol.md`. None of these edges survive a topical-relevance test. They are the residue of the template that wrote "related coverage in the same cluster" — now with the description removed but the padding intact (see Critical 2).

3. **Padding-to-threshold: a large cluster sits at 320-338 body words.** `llm-agents/agent-logs.md` and `ml-frameworks/langchain.md` are at exactly 320; `ml-frameworks/jax.md` at 321; `llm-agents/tool-registry.md` and `js-ts-ecosystem/macrotasks.md` at 324; `js-ts-ecosystem/esbuild-practice.md` and `meta-learning/colbert.md` at 326; 15 of the 18 `js-ts-ecosystem/` files fall between 324 and 337. These files are not empty filler — content quality is decent — but the uniformity and the two exact-320 counts indicate topping-up to pass the floor. The js-ts cluster is the most templated: identical Related shapes (7 bare links), identical trailing "Operational notes/practice" bullets, same two extra bullets before Related. The 320-word bar is being met, but not by margin, and the checker's word count rewards the template.

4. **Near-duplicate page clusters remain.** `infrastructure/tcpdump-and-wireshark.md` and `infrastructure/tcpdump-filters-and-capture.md` are genuinely distinct, but together with `infrastructure/packet-analysis-with-tcpdump`, `os-shell/tcpdump`, and `os-shell/wireshark-and-tshark` (all linked from `tcpdump-and-wireshark.md`) there are five tcpdump/wireshark pages in the wiki; a reader cannot tell which is canonical. `infrastructure/retry-with-backoff.md` links to both `[[wiki/api-protocols/exponential-backoff|Exponential Backoff]]` and `[[wiki/api-protocols/retry-backoff|Retry & Backoff]]` as separate rows — two targets that are almost certainly near-duplicates of each other and of the page itself. The time-sync trio (`network-time-protocol.md`, `precision-time-protocol.md`, `time-synchronization-in-dc.md`) is defensible but overlapping. No merge was attempted in the cleanup.

## Minor & nits

- `memory/org-mode.md` — the Pass 1 broken-link fix landed as recommended (`[[file:notes.org]]` instead of `[[file:...]]`), but the checker still flags it because the link is inside backticks describing org syntax. It is a doc example, not a real wiki link; suggest removing the brackets entirely so the checker stops flagging the slice.
- `infrastructure/tokenization-and-masking.md` — checker placeholder hit is a false positive: `user1@example.com` is a legitimate masked-email example.
- `identity/oauth-flows.md` — near-verbatim intra-file duplication: Summary says "each has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage"; Details bullet 4 repeats "Each flow has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage." One of the two should go.
- Formatting inconsistency: js-ts files (e.g. `esbuild-practice.md`, `import-maps.md`) omit the blank line after the closing frontmatter `---`, unlike every other cluster.
- Related-section style is now inconsistent across the slice: identity/memory/meta-learning/ml-frameworks rows carry "— description"; infrastructure/js-ts/os-shell rows are bare. This looks like a mid-cleanup state, not a deliberate style choice.
- The other five factually-fixed files (`contrast-ratios.md`, `dom-clobbering.md`, `calibration.md`, `dp-vs-px.md`, `anr-diagnostics.md`) are not in this slice, so their corrections could not be re-verified here. The syntheses `type: "concept" → "synthesis"` fix is likewise unverifiable in-slice (no `syntheses/` paths in slice 4).
- `ml-frameworks/google-gemini.md` — "context windows extend to 1M+ tokens on flagship models" is accurate but provider-versioned; worth a "as of" qualifier, as with `openai-api.md`'s "gpt-4o style aliases".

## Sample audit table

| File | Words | Verdict | Notes |
|---|---|---|---|
| identity/totp.md | 457 | PASS | RFC 6238 mechanics, replay/phishing-relay limits accurate; on-topic links; real source in frontmatter |
| identity/oauth-flows.md | 464 | PASS* | Grant types and PKCE accurate; intra-file sentence duplication (Summary to Details bullet 4) |
| identity/session-fixation.md | 450 | PASS | Attack model and rotation defense accurate; example clean |
| infrastructure/bufferbloat-and-queueing.md | 490 | FAIL | Content accurate; Related = bare OSPF/Storage Systems padding + trailer |
| infrastructure/erasure-coding.md | 498 | PASS* | Reed-Solomon k+m and rebuild-window reasoning accurate; OSPF row + trailer in Related |
| infrastructure/precision-time-protocol.md | 492 | PASS* | PTP/BMCA/boundary-clock content accurate; WireGuard/Storage Systems padding + trailer |
| infrastructure/gpu-drivers-and-cuda.md | 509 | PASS* | Pass 1 factual fix verified correct (module set enumerated); Storage Systems/OSPF rows + trailer remain |
| infrastructure/sidecar-pattern.md | 354 | PASS | Ambassador/adapter distinction accurate; all links on-topic with descriptions |
| infrastructure/retry-with-backoff.md | 488 | PASS | Backoff/jitter/breaker composition accurate; double-links to two api-protocols retry pages |
| infrastructure/evpn-bgp-evpn.md | 430 | PASS* | EVPN NLRI/multi-homing/ARP-suppression accurate; Storage Systems row + trailer |
| infrastructure/tcpdump-and-wireshark.md | 415 | PASS* | Workflow content accurate; 5-page tcpdump cluster overlap; Storage Systems row + trailer |
| infrastructure/tcpdump-filters-and-capture.md | 396 | PASS* | BPF syntax accurate; overlaps sibling pages; trailer |
| infrastructure/nvme-multipath.md | 459 | PASS* | Path-policy/failover content accurate; trailer |
| infrastructure/nvme-over-fabrics-tcp.md | 475 | PASS | Queue-pair-to-TCP-connection mapping accurate; links on-topic; trailer |
| js-ts-ecosystem/esbuild-practice.md | 326 | FAIL | Accurate; "dashboard's JS build is a prime esbuild candidate" — no JS build exists in repo; bare 7-link Related; near floor |
| js-ts-ecosystem/import-maps.md | 354 | PASS* | Import-map semantics accurate; speculative dashboard claim; bare Related rows |
| js-ts-ecosystem/microtasks.md | 331 | PASS | Microtask semantics accurate; bare 6-link Related; near floor |
| js-ts-ecosystem/federated-components.md | 333 | PASS* | Self-link and duplicate link removed (verified); bare 5-link Related; near floor |
| llm-agents/reflexion.md | 361 | PASS* | Reflexion described accurately; "wiki's syntheses capture the durable lessons" unverifiable |
| llm-agents/tool-registry.md | 324 | FAIL | Content accurate; "the wiki's tool registry is the single source of truth" — no tool registry in codebase; near floor |
| llm-agents/prompt-caching.md | 345 | PASS* | Caching mechanics accurate; "80-90% at cache prices" and loop-prefix claim unverifiable |
| llm-agents/agent-logs.md | 320 | PASS* | Logging advice sound; exact 320 words; wiki-loop claim unverifiable |
| memory/evergreen-notes.md | 438 | PASS | Atomic/linked/title-as-claim accurate; links on-topic with descriptions |
| memory/progressive-summarization.md | 483 | PASS | Layer model accurate; no padding links |
| memory/logseq.md | 425 | PASS | Block-reference model accurate; cross-links Logseq/Org/Obsidian properly |
| memory/obsidian.md | 429 | PASS | Wikilink/backlink/graph description accurate; on-topic links |
| meta-learning/colbert.md | 326 | PASS* | MaxSim/late-interaction and ColBERTv2 claims accurate; near floor |
| meta-learning/delay-of-gratification.md | 358 | PASS | Self-link removed (verified); marshmallow reanalysis accurate; scheduling opinion in RSIS3 bullet |
| meta-learning/word2vec.md | 371 | PASS | Skip-gram/CBOW and analogy properties accurate |
| ml-frameworks/openai-api.md | 359 | PASS* | API surface accurate; "gpt-4o style aliases" unverifiable as current in 2026; loop-endpoint claim unverifiable |
| ml-frameworks/google-gemini.md | 345 | PASS* | Multimodal/1M+ context accurate; "model registry includes Gemini" unverifiable |
| ml-frameworks/jax.md | 321 | PASS* | grad/jit/vmap/pmap accurate; near floor; "training experiments record framework choice" unverifiable |
| ml-frameworks/pytorch.md | 349 | PASS* | Eager/compile/export accurate; "most models in the wiki's stack" unverifiable |
| ml-frameworks/langchain.md | 320 | PASS* | LangGraph state-machine description accurate; exact 320 words; loop claim unverifiable |
| os-shell/awk-text-processing.md | 492 | PASS | NR/FNR, FS/RS traps, CSV caveat all accurate; links on-topic |
| os-shell/btrfs-features-and-limitations.md | 450 | PASS* | CoW/snapshot/RAID5/6 caveats accurate; Memory Management & Paging row is a stretch; trailer |
| os-shell/cron-and-scheduled-tasks.md | 498 | PASS | cron/anacron/systemd-timer comparison accurate; Kernel Architecture row is thin; trailer |

`PASS*` = content accurate with a noted unverifiable/borderline item. Word counts are body words (frontmatter excluded), same method as `check_slice.py`.

## Recommendations

1. **Finish the trailer removal properly (80 files).** The single most important Pass 2 finding is that a claimed cleanup step never happened in this slice. Delete both syntheses rows from all 80 files and add a verification pass (grep for the two phrases; assert zero) so it cannot silently fail again.
2. **Fix the bare-link regression (98 files).** Either restore one-clause descriptions to rows whose targets are genuinely related, or delete the rows. Specifically purge the OSPF/Storage Systems/WireGuard edges from the 55 files where they are topically unrelated; a knowledge graph consumed by an agent should not contain edges that name unrelated topics.
3. **Gate "the wiki's / the loop's" claims on provenance (61 files).** Before publishing, each such sentence should either be verified against the repo (as the tool-registry and esbuild claims fail today) or rewritten as design intent. Batch templates that assert system behavior are how fabricated product facts enter a memory store.
4. **Treat near-floor word counts as a quality signal.** Extend `check_slice.py` to report files in the 320-345 band and require a human pass on them; the js-ts cluster's template uniformity (same Related shapes, same trailing bullets) shows the 320-word floor can be met without adding knowledge. Also deduplicate the five tcpdump/wireshark pages and the retry-backoff/exponential-backoff pair.
5. **Add the cleanup's missing checks to the pipeline**: bare-wikilink-row detection (a Related row with `[[…]]` and no description), the two trailer phrases as a denylist, and an "unverifiable system claim" scan for the strings `the wiki's | the loop's | mykb's | rsis3's`. These three string checks would have caught every critical and major finding in this Pass 2 review.

*Out of scope / not verifiable in this slice: the other five factual fixes, the syntheses `type` correction, and 62-file topping-up totals (only the residue is visible here: 20+ files at 320-338 words).*
