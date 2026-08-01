#!/usr/bin/env python3
"""Rebuild index.html from the intact parts of the mangled file.

Extracts the head/header/nav/legend, the original 37 tier cards from the
three existing panels, the originals section, and the footer+script; then
reconstructs the content wrapper with 12+12 / 13+13 / 12+12 tier cards,
the new Expert+ and X++ panels, and the updated tab JS.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _index_update import BASIC_CARDS, ADVANCED_CARDS, EXPERT_CARDS, PLUS_CARDS, OMEGA_CARD, NESTED_CARD, card, section

HTML = os.path.join(os.path.dirname(HERE), "index.html")
src = open(HTML).read()

def between(a, b):
    ia = src.index(a)
    ib = src.index(b, ia)
    return src[ia:ib]

# 1 · static head/header/nav/legend + content open
head = src[:src.index('<div class="content">') + len('<div class="content">')]
assert '37 new diagrams in three tiers' in head and '>Expert <span class="count">12</span>' in head

# 2 · original cards from the three panels
def panel_cards(panel):
    dp = src.index(f'data-panel="{panel}"')
    start = src.rindex('<section', 0, dp)
    start = src.index('<div class="panel-head">', start)
    start = src.index('</div>', start) + len('</div>')  # after panel-head
    end = src.index('</section>', start)
    body = src[start:end]
    return body

basic_old = panel_cards('basic')
advanced_old = panel_cards('advanced')
expert_old = panel_cards('expert')
assert basic_old.count('<article class="diagram-card">') == 12, basic_old.count('<article')
assert advanced_old.count('<article class="diagram-card">') == 13
assert expert_old.count('<article class="diagram-card">') == 12

# 3 · originals section
originals = between('<!-- ═══ ORIGINALS ═══ -->', '</section>')
assert originals.count('<article class="diagram-card">') == 4, originals.count('<article')

# 4 · footer + script tail (after originals' </section>)
tail_start = src.index('</section>', src.index('<!-- ═══ ORIGINALS ═══ -->')) + len('</section>')
tail = src[tail_start:]
assert '<footer' in tail and '</html>' in tail

# 5 · rebuild panels
def panel(open_tag, heading, sub, cards_html):
    return (open_tag + "\n    <div class=\"panel-head\">\n      <h2>" + heading +
            "</h2>\n      <p>" + sub + "</p>\n    </div>\n\n" + cards_html + "\n  </section>")

basic_new = panel('<section class="tab-panel active" data-panel="basic" id="basic" role="tabpanel">',
                  "Basic — the whole ecosystem at a glance",
                  "High-level conceptual views: what the three components are, how they connect, how they improve, and where everything runs.",
                  basic_old + "\n" + "\n".join(card(*c) for c in BASIC_CARDS))
advanced_new = panel('<section class="tab-panel" data-panel="advanced" id="advanced" role="tabpanel" hidden>',
                     "Advanced — how each component works",
                     "Deeper views of the internals: loops, pipelines, matrices, state machines, and the semantic spaces the components live in.",
                     advanced_old + "\n" + "\n".join(card(*c) for c in ADVANCED_CARDS))
expert_new = panel('<section class="tab-panel" data-panel="expert" id="expert" role="tabpanel" hidden>',
                   "Expert — internals, pipelines, meta",
                   "Code-level pipelines and systems-theoretic views: entropy, invariants, fault logic, budgets, coupling, and conservation.",
                   expert_old + "\n" + "\n".join(card(*c) for c in EXPERT_CARDS))

xplus_extra = '''
    <div class="diagram-frame" style="margin:0 0 22px;padding:6px;">
      <iframe src="x-plus-plus-omega.html" title="Interactive omega graph" loading="lazy"
        style="width:100%;height:min(94vh,1250px);border:0;border-radius:6px;background:var(--surface2);display:block"></iframe>
    </div>
    <p style="color:var(--text3);font-size:11px;margin:-8px 4px 18px;line-height:1.7">
      The single interactive &Omega; graph — one self-contained HTML file, no build step. Hover/tap nodes to pin their readout,
      drag the &lambda; slider to travel &lambda;&#8321; &rarr; &lambda;&#8324;. The same picture is also available as a static SVG in
      Expert+ (X+-12) and as the downloadable HTML below.
    </p>'''
plus_section = section("EXPERT-PLUS", "Expert+ — cross-cutting systems views",
                       "Diagrams that read across all four runtimes at once: causality, entropy fields, resilience, time-scale separation, feedback topology, dependency lattices, resource flows, stability, phylogeny, and constraint hypergraphs.",
                       PLUS_CARDS)
xplus_section = section("X++", "X++ — the interactive ecosystem graphs",
                        "Two interactive views of the whole ecosystem: the &Omega; graph (27 nodes on two semantic spectra, &lambda; slider as the 4th axis) and the nested-loop graph (all 52 nodes / 64 links with the L1&ndash;L9 stack as nine concentric rings).",
                        [OMEGA_CARD, NESTED_CARD], extra=xplus_extra)

# fix x++ panel name (section() lowercases "X++" to "x++")
xplus_section = xplus_section.replace('data-panel="x++"', 'data-panel="x-plus-plus"').replace('id="x++"', 'id="x-plus-plus"')

content = ("\n" + basic_new + "\n\n" + advanced_new + "\n\n" + expert_new + "\n" +
           plus_section + "\n" + xplus_section + "\n\n</div>")

# nav with 5 buttons + counts
nav = '''<nav class="tabs" role="tablist" aria-label="Diagram tiers">
  <button class="tab-btn active" data-tab="basic" role="tab" aria-selected="true">Basic <span class="count">24</span></button>
  <button class="tab-btn" data-tab="advanced" role="tab" aria-selected="false">Advanced <span class="count">26</span></button>
  <button class="tab-btn" data-tab="expert" role="tab" aria-selected="false">Expert <span class="count">24</span></button>
  <button class="tab-btn" data-tab="expert-plus" role="tab" aria-selected="false">Expert+ <span class="count">12</span></button>
  <button class="tab-btn" data-tab="x-plus-plus" role="tab" aria-selected="false">X++ <span class="count">2</span></button>
</nav>'''

# header text
head = head.replace("RSIS3 core engine &middot; MyKB memory &middot; SPACE ideation — 37 new diagrams in three tiers",
                    "RSIS3 core engine &middot; MyKB memory &middot; SPACE ideation — 88 diagrams in five tiers + two interactive &Omega; graphs")
head = head.replace('<span class="badge">Basic &middot; Advanced &middot; Expert &middot; Mobile-first SVG</span>',
                    '<span class="badge">Basic &middot; Advanced &middot; Expert &middot; Expert+ &middot; X++ &middot; Mobile-first SVG</span>')
head = re.sub(r'<nav class="tabs".*?</nav>', nav, head, flags=re.S)

# script tail
tail = tail.replace("var NAMES = ['basic', 'advanced', 'expert'];",
                    "var NAMES = ['basic', 'advanced', 'expert', 'expert-plus', 'x-plus-plus'];")
tail = tail.replace("// Deep-link: #basic / #advanced / #expert",
                    "// Deep-link: #basic / #advanced / #expert / #expert-plus / #x-plus-plus")

out = head + content + "\n" + originals + "\n</section>" + tail
open(HTML, "w").write(out)
print("rebuilt index.html")
