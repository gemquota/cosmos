# Adversarial Review #5 (PASS 2) — MyKB Stub-Promotion Wave (slice 5, 219 files)

Reviewer: adversarial-reviewer-5 (PASS 2, post-cleanup re-review)
Slice: `/data/data/com.termux/files/home/.cache/mykb-review/slice5.txt` (219 files)
Areas: os-shell, prompt-engineering, software-engineering, web-platforms, syntheses, security-auth, pulses, shell-environment, tooling
Checker run: `python3 ops/reports/adversarial-reviews/check_slice.py <slice>` → 210 clean / 9 flagged; all 9 flags opened and verified → **all false positives** (0 confirmed).

## Verdict

**Health score: 71 / 100**

**Pass 1 fixes held in my slice — verified, not assumed.** Every Pass 1 defect class I re-checked is gone: 0 self-links across all 219 files, 0 occurrences of the "related coverage in the same cluster" / "the full treatment of this theme" / "existing graph context" annotation strings, 0 unclosed `[[raw/archive/…]]` links, 0 `sources|syntheses/README` links, all 6 `syntheses/` files now declare `type: "synthesis"`, and the two factually-fixed files in my slice (`contrast-ratios.md`, `dom-clobbering.md`) are now correct — I recomputed the WCAG math (`#777777` = 4.48:1 fails, `#757575` = 4.61:1 passes, `#595959` = 7.0:1) and the file's numbers match exactly; the `dom-clobbering.md` vectors (`<form><input name=attributes>`-style clobbers, `id="defaultView"`) are the known, real attack class. No file dropped below the 320-body-word floor (min = 320), no `## Related` section is empty, and the checker's 9 flags are all legitimate usage: `[[:alpha:]]` locale class in `grep-patterns.md` (checker mis-parses `[[`), "placeholder box/text", "example.com" example domains, "insert nodes / insert via node APIs" DOM phrasing, and a `TODO` inside a quoted `rg -l "TODO" src/` example.

What keeps the score at 71 instead of much higher is that the substantive quality classes Pass 1 identified were **deliberately not fixed**, and they are systemic, not occasional: (a) keyword-matched irrelevant links are still everywhere (confirmed in ≥8 files, with a recurring "kernel-architecture + memory-management-paging" filler pair in os-shell Related lists); (b) unverifiable "the wiki's X does Y" claims are present in ~183/219 files, each fabricating a different specific about the dashboard/daemon/loop that cannot be checked offline; (c) padding-to-threshold is visible in the word distribution — 155/219 files (71%) sit in the 320–360 band, median 340, and every file carries the same short "Header: sentence" bullet appendices that read as floor-aiming top-ups; (d) near-duplicates are worse than Pass 1 reported (I count 8+ clusters, including two triples and a 6-file CSS-unit cluster); and (e) the syntheses files repeat their Summary paragraph verbatim as the first Details bullet. The cleanup also introduced a small regression: 5 `prompt-engineering` files now have orphaned, headerless bullets where annotation-stripping removed a heading.

Quantified (219 files): status 0 fail (0%), body-words <320: 0 fail (0%), frontmatter keys 0 fail (0%), self-links 0 (0%), broken/truncated links 0 (0%, checker's `:alpha:` flag is a false positive), annotation strings 0 (0%), README/raw links 0 (0%), syntheses `type` wrong 0 (0%), checker placeholders 9 flagged → 0 confirmed, orphaned bullets 5 (2.3%), near-duplicate clusters ≥8 (covering ~40 slice files), "RSIS3/mykb relevance" unverifiable claims ~183 (84%), keyword-matched irrelevant links ≥8 confirmed, template section boilerplate ("Mechanism"/"Concrete example"/"Failure modes"/"Operational tradeoffs") present in ~90%+ of files.

## Critical findings

None confirmed. The invariant and factual-error classes that were critical in Pass 1 (truncated raw links, wrong contrast numbers, leaked generator self-correction in `dom-clobbering.md`) are all fixed in this slice. The nearest thing to critical now is the volume of unverifiable system-specific claims — individually minor, collectively a fabrication risk for a memory store. Listed under Major.

## Major findings

1. **Unverifiable "the wiki's X does Y" claims are pervasive (~183 files, deliberate non-fix).** Nearly every article ends with an `RSIS3/mykb relevance` bullet asserting a specific behavior of the dashboard/daemon/loop that I cannot verify from the repo (rules: "if you cannot verify a claim offline, say cannot verify"). Examples, all quoted exactly:
   - `web-platforms/contrast-ratios.md`: "the rack telemetry includes a periodic contrast audit of key surfaces."
   - `web-platforms/compositing-triggers.md`: "keeping interaction-to-next-paint low on the low-power devices the team tracks in rack telemetry."
   - `web-platforms/speculative-loading.md`: "the wiki adds preconnect for its API and prerenders the most-visited synthesis from Speculation Rules, with data-usage telemetry reviewed by the loop."
   - `web-platforms/cls-avoidance.md` vs `web-platforms/cumulative-layout-shift.md`: two incompatible versions of the same claim — "the dashboard tracks CLS from the Performance API as a rack pulse" vs "the dashboard reports CLS from real sessions into rack telemetry".
   - `os-shell/environment-variables.md`: invents a specific env var, "a daemon reads `MYKB_WIKI_ROOT` to locate its corpus" — I could not find this var referenced anywhere I checked; even if it exists, the article asserts it as fact.
   - `prompt-engineering/adversarial-prompts.md`: "a fuzzer generates 10,000 obfuscated variants nightly" — an invented specific number presented as a concrete example.
   These read as generated filler tuned to the 320-word target, and they are the single largest residual credibility risk in the slice. Suggested fix: either delete the RSIS3/mykb bullet from files where it is not a documented fact, or mark it explicitly as "aspirational pattern" rather than present-tense fact.

2. **Keyword-matched irrelevant links (confirmed ≥8 files, deliberate non-fix).** The cleanup retargeted dead README links but left the keyword-matching behavior intact:
   - `os-shell/users-groups-and-acls.md` → `[[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]` (network security groups; irrelevant to POSIX file ACLs — pure "groups" keyword match), plus `[[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]]` (job control, not identity) and `[[wiki/os-shell/memory-management-paging|Memory Management & Paging]]` (irrelevant).
   - `os-shell/mdadm-and-lvm2.md` → `[[wiki/os-shell/memory-management-paging|Memory Management & Paging]]` and `[[wiki/os-shell/kernel-architecture|Kernel Architecture]]` — no topical link to RAID/LVM.
   - `os-shell/tcp-keepalive.md` → `[[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]` — NVMe-oF/TCP is a storage protocol; the only connection is the string "TCP" in the title. A reading agent following this link wastes a hop.
   - The "kernel-architecture + memory-management-paging" pair recurs as filler in `select-poll-epoll-comparison.md`, `io-uring-and-async-io.md`, `swap-and-zram.md`, `oom-killer-and-memory-pressure.md`, `users-groups-and-acls.md`, `mdadm-and-lvm2.md` — in several of these at least one link is off-topic.
   - `software-engineering/estimation-techniques.md` → `[[wiki/memory/spaced-repetition|Spaced Repetition]]` ("scheduling analog") — stretched.
   Verified: all targets exist (link hygiene for existence is clean); the defect is topical relevance, which the checker cannot see.

3. **Near-duplicates are more extensive than Pass 1 reported (≥8 clusters, ~40 slice files).** All still present:
   - Triple: `os-shell/path-resolution.md` ↔ `os-shell/path-resolution-and-symlinks.md` ↔ `os-shell/symlinks.md` — same namei walk, 40-link ELOOP, openat2 RESOLVE_*, realpath, find -L/-P, backup semantics; the two path articles are near-verbatim in places and link each other instead of being merged.
   - Pair: `web-platforms/cumulative-layout-shift.md` ↔ `web-platforms/cls-avoidance.md` — same definition, mechanism, main-causes list, budget (<0.1), and dashboard-CLS claim.
   - Pair: `web-platforms/color-spaces.md` ↔ `web-platforms/srgb-vs-p3.md` — same sRGB ~35% / P3 ~45% gamut facts, oklch authoring advice, fallback ordering, dashboard-token claims.
   - Six-file cluster: `web-platforms/em-vs-rem.md`, `px-vs-rem.md`, `vw-vh.md`, `dvh-svh.md`, `container-relative-units.md`, `responsive-units.md` — the same "which unit when" theme with a shared 4–7 link Related skeleton and six variants of "dashboard uses <policy>"; `responsive-units.md` is effectively a meta-summary of the other five.
   - Triple: `web-platforms/layout-triggers.md` ↔ `paint-triggers.md` ↔ `compositing-triggers.md` — distinct enough per stage, but with 7 identical Related links and the same dashboard claim template.
   - Five-file cluster: `dns-prefetch.md`, `preconnect-practice.md`, `preload-practice.md`, `prefetch-practice.md`, `speculative-loading.md` — each hint file is defensible, but `speculative-loading.md` re-covers all of them.
   - Cross-namespace pair: `security-auth/bug-bounty.md` (concept) ↔ `syntheses/bug-bounty-ai.md` (synthesis) — the synthesis repeats the concept's scope/rules/triage/tradeoff content plus an AI angle.
   - Pair: `os-shell/users-and-groups.md` ↔ `os-shell/users-groups-and-acls.md` — partial overlap (identity model) but the ACL file earns its slug; lowest-priority of the set.
   For a retrieval-driven memory store, eight overlapping clusters mean an agent pulling "CLS" or "CSS units" gets 2–6 near-identical pages. Fix: canonical slug + merge or redirect note per cluster.

4. **Duplicated passages inside files (dedup pass missed cross-section repeats).**
   - `syntheses/bug-bounty-ai.md`, `syntheses/coordinated-disclosure.md`, `syntheses/safety-case-approach.md`: the Summary paragraph is repeated verbatim as the first Details bullet. E.g. `syntheses/coordinated-disclosure.md` Summary: "Coordinated disclosure is a formal process where researchers, vendors, and platforms agree on the timing and content of vulnerability publication." and Details bullet 1: "Coordinated disclosure is a formal process where researchers, vendors, and platforms agree on timing and content of vulnerability publication." The dedup pass removed duplicate bullets within a section but not Summary↔Details duplication.
   - `software-engineering/actor-model.md`: two consecutive relevance bullets — "RSIS3 relevance: agents modeled as actors get explicit message handoffs…" followed by "- RSIS3/mykb relevance: the wiki records actor-style designs for agent runtimes…" — the same generator pattern Pass 1 flagged; still here.

5. **Padding-to-threshold is measurable and unchanged.** 155/219 files (71%) land in the 320–360 band (median 340; `aspect-ratio-images.md` and `polyglot-xss.md` sit at exactly 320). The top-up mechanism is visible as the same short "Header: 1–2 sentences" bullet appendices appended after the RSIS3 bullet in file after file: "Source switching:", "Parser differentials:", "Test corpus:", "Alternatives first:", "Focus order:", "Animation interplay:", "Overlay roots:", "Interaction windows:", "Swap timing:", "Measurement:", "Layer audit:", "Cost containment:", "Read-after-write rule:", "Will-change scoping:", "Keyboard behavior:", "Fallback order:", "Migration path:", "Budgeting:", "Battery composition:", "Probe lifecycle:", "External anchoring:", "Cost accounting:", "Server side:", "Client side:", "Contract-first:", "Consistency expectations:", "Migration practice:", "Context inventory:", "Policy review:", "Input vs output:", "Gamut mapping:", "Authoring default:", "Display testing:", "Asset pipeline:", "Cache correctness:", "Priority audit:", "Monitoring:", "Same-site constraints:", "Budget control:", "Media query note:", "Accessibility check:", "Landscape and rotation:", "Print and embed:", "Safe-area interplay:", "Component scaling:", "Detection:", "Immutable singletons:", "Thread-safety illusion:", "Audit pattern:", "Filesystem note:", "Testing:", "Security angle:", "Filenames and URLs:". Individually these are accurate sentences; collectively they are floor-aiming appendices. The 320-word bar is being met by construction, not by curation.

6. **Template boilerplate remains (unchanged).** "Failure modes" appears in all 219 files, "Concrete example" in 216, "Mechanism:" in 201, "Operational tradeoffs" in 189, "RSIS3/mykb relevance" in 183. The identical syntheses meta-link pair — `[[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb` and `[[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to` — appears in 27 files; the target `mykb-acquisition-curation-and-practices.md` is real and the description is accurate, but 27 identical boilerplate links add graph noise. This is the deliberate non-fix category: honest but templated.

## Minor & nits

1. **Cleanup regression: 5 prompt-engineering files have orphaned, headerless bullets.** A bullet now dangles between the RSIS3 paragraph and `## Related`, where an annotation-bearing heading was clearly stripped: `prompt-engineering/multi-step-reasoning.md` ("- Separate reasoning output from the final answer in the prompt so steps inform, not pollute, the conclusion."), `red-teaming.md` ("- Keep a scored findings log…"), `refusal-behaviour.md` ("- Measure refusal consistency across phrasings…"), `retrieval-prompting.md` ("- Require the model to cite or quote retrieved evidence…"), `safety-tuning.md` (two bullets: "Treat safety tuning as a continuous loop…", "Document the preference data…"). Fix: restore a heading or fold the bullets into an existing section.
2. **`security-auth/ssrf-prevention.md`** has a double blank line before `## Related` ("…trust boundary like any other.\n\n\n## Related") — formatting remnant.
3. **Frontmatter spacing is inconsistent across the slice**: web-platforms files use `---\n# Title` (no blank line), os-shell and software-engineering files use `---\n\n# Title`. Cosmetic, but it is exactly the kind of drift a formatter pass would fix in one shot.
4. **Two syntheses carry "Open Threads" titles but are promoted to `status: growing` as syntheses**: `syntheses/evidence-and-provenance.md` and `syntheses/knowledge-acquisition-workflow.md` are structured as open questions ("Next step — design the provenance fields…") rather than conclusions. Type/tags now agree with the namespace, but the content is arguably a question-note promoted early.
5. **`security-auth/bug-bounty.md`** includes a `source:` frontmatter key with a Wikipedia URL — fine, but no other concept file in the slice carries sources, so provenance practice is inconsistent wave-wide.
6. **`web-platforms/srgb-vs-p3.md`**: "Wide-gamut support in CSS is broad by 2024+" — a dated claim with no source; likely true, but unverifiable from the file.
7. **`os-shell/oom-killer-and-memory-pressure.md`** Related list is all memory files plus the two syntheses meta-links; it is the only file in the slice whose Related is almost entirely same-cluster — acceptable, but the boilerplate pair makes it look padded.
8. **`prompt-engineering/prompt-compression.md`**: "a 50-turn session is compressed to a 5-turn digest" — invented-but-plausible example number; fine as illustration, note the pattern (see Major 1).

## Sample audit table

| File (relative to `components/mykb/wiki/`) | Words | Verdict | Notes |
|---|---|---|---|
| os-shell/path-resolution.md | 441 | OK content, dup | Part of 3-file near-duplicate cluster; fine standalone |
| os-shell/path-resolution-and-symlinks.md | ~460 | DUP | Near-verbatim twin of path-resolution; ELOOP 40, openat2, realpath repeated |
| os-shell/symlinks.md | ~430 | DUP | Third member of the cluster |
| os-shell/users-and-groups.md | ~450 | OK | Accurate identity model; Related clean |
| os-shell/users-groups-and-acls.md | ~460 | MINOR | Keyword links: cloud-security-groups, process-groups-and-sessions, memory-management-paging |
| os-shell/mdadm-and-lvm2.md | ~470 | MINOR | Accurate; filler Related (kernel-architecture, memory-management-paging) |
| os-shell/tcp-keepalive.md | ~470 | MINOR | Correct defaults (7200s/75s/9); irrelevant nvme-over-fabrics-tcp link |
| os-shell/swap-and-zram.md | ~460 | OK | Accurate; zswap/zram/swapiness correct |
| os-shell/select-poll-epoll-comparison.md | ~430 | OK | Correct FD_SETSIZE/epoll semantics; filler Related pair |
| os-shell/io-uring-and-async-io.md | ~450 | OK | Accurate (pre-5.1, EOPNOTSUPP, registered files); boilerplate meta-links |
| os-shell/oom-killer-and-memory-pressure.md | ~450 | OK | Correct cgroup v2 memory.pressure framing; boilerplate tail |
| os-shell/grep-patterns.md | ~430 | OK | Checker flags (`:alpha:`, TODO) are false positives |
| os-shell/environment-variables.md | ~440 | MINOR | Invents `MYKB_WIKI_ROOT` as fact; otherwise accurate |
| os-shell/tmux-sessions.md | ~430 | OK | Accurate |
| os-shell/zsh-configuration.md | ~440 | OK | Accurate; weak bash-patterns link acceptable |
| prompt-engineering/adversarial-prompts.md | ~370 | MINOR | "10,000 obfuscated variants nightly" invented number |
| prompt-engineering/agentic-rails.md | ~360 | OK | Accurate; rail/log/approve framing sound |
| prompt-engineering/indirect-injection.md | ~360 | OK | Accurate; truncated raw link now fixed (verified) |
| prompt-engineering/multi-step-reasoning.md | ~370 | REGRESSION | Orphaned headerless bullet before Related |
| prompt-engineering/red-teaming.md | ~360 | REGRESSION | Orphaned bullet; otherwise accurate |
| prompt-engineering/refusal-behaviour.md | 322 | REGRESSION | Orphaned bullet; 322 words (near floor) |
| prompt-engineering/retrieval-prompting.md | ~360 | REGRESSION | Orphaned bullet |
| prompt-engineering/safety-tuning.md | ~370 | REGRESSION | Two orphaned bullets; otherwise accurate |
| prompt-engineering/emergent-abilities.md | ~380 | OK | Correctly hedges emergence debate (2022 paper + metric critique) |
| prompt-engineering/in-context-learning.md | ~360 | OK | Accurate |
| software-engineering/actor-model.md | ~430 | MINOR | Duplicate RSIS3 relevance bullets still present |
| software-engineering/transactional-outbox.md | ~400 | OK | Accurate (Debezium, dual-write) |
| software-engineering/retry-after.md | ~380 | OK | Accurate; Related topical |
| software-engineering/singleton-pitfalls.md | ~420 | OK | Accurate |
| software-engineering/estimation-techniques.md | ~410 | MINOR | Stretched spaced-repetition link |
| software-engineering/code-formatters.md | ~400 | OK | Accurate |
| syntheses/bug-bounty-ai.md | ~400 | MINOR | Summary duplicated as first Details bullet; overlaps security-auth/bug-bounty |
| syntheses/coordinated-disclosure.md | ~420 | MINOR | Summary duplicated as first Details bullet |
| syntheses/safety-case-approach.md | ~410 | MINOR | Summary duplicated as first Details bullet |
| syntheses/evidence-and-provenance.md | ~380 | MINOR | "Open threads" content promoted to growing synthesis |
| syntheses/knowledge-acquisition-workflow.md | ~380 | MINOR | Same; the 27-file boilerplate link target |
| syntheses/model-updates-risks.md | ~420 | OK | Accurate; good canary/rollback framing |
| security-auth/bug-bounty.md | ~400 | MINOR | Near-duplicate of syntheses/bug-bounty-ai; has source: key |
| security-auth/ssrf-prevention.md | ~430 | OK | Accurate; double blank line before Related |
| pulses/capability-probes.md | ~430 | OK | Accurate; probe-hygiene advice sound |
| pulses/recursive-improvement-loops.md | ~410 | OK | Accurate; metric-gaming framing good |
| tooling/caching-layers.md | ~420 | OK | Accurate; miss-rate-per-layer point good |
| tooling/flag-cleanup.md | ~400 | OK | Accurate |
| tooling/game-days.md | ~430 | OK | Accurate |
| shell-environment/shell-scripting-robustness.md | 577 | OK | Densest file in slice; solid |
| shell-environment/unix-text-processing-tools.md | ~450 | OK | Accurate (spot-checked) |
| web-platforms/contrast-ratios.md | ~430 | FIXED-OK | Factual fix verified: 4.48/4.61/7.0 all correct |
| web-platforms/dom-clobbering.md | ~440 | FIXED-OK | Corrupted sentence gone; vectors accurate |
| web-platforms/cumulative-layout-shift.md | 321 | DUP | Near-duplicate of cls-avoidance; dashboard claim unverifiable |
| web-platforms/cls-avoidance.md | ~360 | DUP | Same content, same claim, incompatible with sibling's version |
| web-platforms/color-spaces.md | ~370 | DUP | Near-duplicate of srgb-vs-p3 |
| web-platforms/srgb-vs-p3.md | ~370 | DUP | Same gamut facts; "by 2024+" unsourced |
| web-platforms/em-vs-rem.md | 322 | CLUSTER | Member of 6-file unit cluster; top-up bullets visible |
| web-platforms/responsive-units.md | ~380 | CLUSTER | Meta-summary of the other unit files |
| web-platforms/layout-triggers.md | ~370 | CLUSTER | Accurate; identical Related to paint/compositing |
| web-platforms/compositing-triggers.md | ~380 | CLUSTER | Accurate; unverifiable rack-telemetry claim |
| web-platforms/speculative-loading.md | ~400 | CLUSTER | Meta-article over the hint cluster; unverifiable prerender claim |
| web-platforms/dns-prefetch.md | ~380 | OK | Checker "example.com" flag is false positive |
| web-platforms/preconnect-practice.md | ~380 | OK | Same; accurate |
| web-platforms/aspect-ratio-images.md | 320 | OK | Exactly at floor; content still substantive |
| web-platforms/polyglot-xss.md | 320 | OK | Exactly at floor; accurate |
| web-platforms/toctou.md | ~380 | OK | Accurate; open-then-fstat advice correct |
| web-platforms/unicode-normalization.md | ~380 | OK | Accurate; NFC/NFKD distinctions correct |
| web-platforms/mutation-xss.md | ~380 | OK | Checker "insert nodes" flag is false positive |
| web-platforms/safe-html-rendering.md | ~400 | OK | Checker flag false positive; pipeline advice correct |

(24 rows shown at full detail; table covers all 9 areas of the slice.)

## Recommendations (top 5)

1. **Re-curate or delete the "RSIS3/mykb relevance" bullets** (≈183 files). Decide whether these are facts (then verify and source them) or aspirations (then label them as such). As written, they are the slice's largest fabrication surface: a future session citing "the rack telemetry includes a periodic contrast audit" will inherit an unverifiable claim as memory. Highest impact, lowest effort is a wave-wide rewrite to a single honest sentence or removal.
2. **Merge the near-duplicate clusters to one canonical slug each** (path-resolution ×3, CLS ×2–3, color ×2, CSS units ×6, triggers ×3, speculative-loading ×5, bug-bounty ×2). For a retrieval store, eight overlapping clusters directly degrade search precision. Add a near-duplicate check (normalized-body similarity) to the promotion gate.
3. **Re-curate Related links by meaning, not keyword**, and drop the automatic "kernel-architecture + memory-management-paging" filler pair. At minimum remove the confirmed misfires: `nvme-over-fabrics-tcp` from `tcp-keepalive.md`, `cloud-security-groups` and `process-groups-and-sessions` from `users-groups-and-acls.md`, `memory-management-paging` from `mdadm-and-lvm2.md`.
4. **Fix the cleanup regression and the cross-section duplication**: restore a heading (or fold the bullets) in the 5 `prompt-engineering` files with orphaned bullets, and dedupe Summary↔first-Details repeats in the 3 syntheses files plus the twin RSIS3 bullets in `actor-model.md`.
5. **Raise the floor's honesty**: either raise the body-word minimum and re-measure content density, or replace the 320-word gate with a quality gate that counts distinct facts/links. The 71% concentration in the 320–360 band shows the current floor is being padded to, and the short "Header: sentence" appendices are the visible signature; a density check would catch both the padding and the boilerplate in one mechanism.

## Rules compliance

- No wiki file modified; no `git` run; only `ops/reports/adversarial-reviews/review-5-pass2.md` written.
- All flagged items opened and verified; all link targets in this report checked for existence.
- Unverifiable claims are labeled "cannot verify" rather than asserted true or false.
