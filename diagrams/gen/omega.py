"""The X++ interactive omega graph — a single self-contained HTML+SVG+JS page.

One graph of the whole ecosystem: ~27 real module/artifact nodes mapped on
two semantic spectra (X = theory↔execution, Y = short-term↔long-term),
node size = footprint, node colour = owning component, edge colour =
performing component. The 4th axis is time: a λ slider (λ₁ engine →
λ₄ full ecosystem) interpolates each node's keyframed position/size, so
memory grows and the dashboard fades in as you drag. Touch-first: tap or
hover a node to highlight its neighbourhood and pin a detail readout.
"""
import json, os
from design import *

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PALETTE = {
    "rsis": RSIS, "mykb": MYKB, "space": SPACE, "dash": DASH, "ext": EXT,
}

# (id, label, group, x -1..1 (theory..execution), y -1..1 (short↑..long↓),
#  r0 (λ1), r1 (λ4), facts)
NODES = [
    ("rrp", "RRP engine", "space", -0.62, 0.02, 13, 13, "recursive refinement protocol · 25 rounds/spec"),
    ("probe", "probe framework", "space", -0.82, 0.22, 17, 17, "326 probes · 7 series · S1→S7 dependency chain"),
    ("provider", "provider factory", "space", -0.42, 0.3, 11, 11, "7 LLM providers · failover by construction"),
    ("export", "exports · 6 formats", "space", -0.3, -0.18, 10, 12, "MD / JSON / YAML / HTML / XML / TXT"),
    ("webui", "SPACE web UI :8888", "space", -0.2, 0.62, 12, 12, "self-contained SPA · launched from dashboard"),
    ("metaview", "meta viewer :8899", "space", -0.157, -0.323, 10, 10, "spec viewer for exports"),
    ("sstore", "session store · SQLite", "space", -0.52, -0.46, 10, 10, "session state + artifact persistence"),
    ("l1", "L1 · action loop", "rsis", 0.9, 0.8, 15, 15, "tool calls · observations · retries · ~1s"),
    ("l2", "L2 · improvement", "rsis", 0.62, 0.22, 16, 16, "candidates · 25 rounds · evaluator-gated"),
    ("l3", "L3 · evolution", "rsis", 0.4, -0.66, 14, 16, "consolidation · strategies · ~60s cycle"),
    ("evalc", "evaluator client", "rsis", 0.72, 0.02, 10, 10, "SHA-256 verify · spawns the judge"),
    ("eval", "evaluator · immutable", "ext", 0.88, -0.24, 13, 13, "subprocess · 60s cap · ≤5/session · read-only"),
    ("memmgr", "memory manager", "rsis", 0.06, -0.6, 11, 12, "KG + vectors · .rsis/knowledge_graph.json"),
    ("tele", "telemetry collector", "rsis", 0.312, 0.679, 11, 11, "JSONL events · extrapolator feeds L3"),
    ("rack", "rack · pulses", "dash", 0.57, 0.901, 11, 12, "JSONL buffer → dashboard-data.json · ~1s"),
    ("daemon", "MyKB daemon :8765", "mykb", 0.12, 0.44, 12, 13, "only always-on server · search + retrieval"),
    ("wiki", "wiki corpus", "mykb", -0.219, -0.961, 20, 26, "2,360+ pages · 48 domains · source of truth"),
    ("tfidf", "TF-IDF index", "mykb", -0.1, -0.7, 12, 14, "search_index.json · built from corpus"),
    ("temporal", "temporal engine", "mykb", 0.0, -0.86, 11, 13, "git snapshots · time-travel queries"),
    ("kg", "knowledge graph", "mykb", -0.341, -0.799, 12, 14, "graph.json · edges = consolidated lessons"),
    ("kgview", "KG graph viewer", "mykb", -0.44, -0.62, 9, 11, "okf-graph.html · embedded in dashboard"),
    ("capture", "capture hooks", "mykb", -0.063, -0.417, 10, 12, "session → wiki pages + KG edges + snapshot"),
    ("dash", "unified dashboard :9000", "dash", 0.212, 0.895, 15, 17, "embeds wiki, KG graph, SPACE UI, meta viewer"),
    ("dd", "dashboard-data.json", "dash", 0.45, 0.781, 12, 13, "rack snapshot · read via config.js"),
    ("config", "config.js", "dash", 0.155, 0.78, 8, 9, "dashboard reader · Chart.js + Tailwind"),
    ("gcosmos", "GitHub Pages · cosmos", "dash", -0.104, 0.982, 9, 11, "root redirect → unified dashboard"),
    ("ghub", "GitHub Pages · hub", "dash", 0.264, 1.011, 8, 9, "all non-COSMOS projects"),
]

LINKS = [
    ("rrp", "probe", "space", "dispatch"),
    ("rrp", "provider", "space", "ask"),
    ("rrp", "sstore", "space", "persist"),
    ("probe", "export", "space", "answers → spec"),
    ("export", "metaview", "space", "render"),
    ("rrp", "webui", "space", "host"),
    ("rrp", "l2", "space", "spec drafts"),
    ("l2", "evalc", "rsis", "candidate"),
    ("evalc", "eval", "ext", "spawn · SHA-256"),
    ("eval", "l2", "ext", "verdict"),
    ("l1", "rack", "rsis", "pulse"),
    ("tele", "rack", "rsis", "pulse"),
    ("rack", "dd", "dash", "extract"),
    ("dd", "config", "dash", "read"),
    ("config", "dash", "dash", "render"),
    ("l3", "memmgr", "rsis", "consolidate"),
    ("l3", "capture", "rsis", "session capture"),
    ("capture", "wiki", "mykb", "write page"),
    ("capture", "kg", "mykb", "write edge"),
    ("capture", "temporal", "mykb", "snapshot"),
    ("wiki", "tfidf", "mykb", "build"),
    ("wiki", "kg", "mykb", "derive"),
    ("daemon", "tfidf", "mykb", "query"),
    ("daemon", "l1", "mykb", "retrieval :8765"),
    ("kg", "daemon", "mykb", "serve"),
    ("kg", "kgview", "mykb", "render"),
    ("dash", "webui", "dash", "launch :8888"),
    ("dash", "gcosmos", "dash", "redirect"),
    ("dash", "metaview", "dash", "embed"),
    ("dash", "daemon", "dash", "embed wiki"),
    ("dash", "kgview", "dash", "embed graph"),
]

GROUPS = {
    "space": ("SPACE · ideation", SPACE),
    "rsis": ("RSIS3 · execution", RSIS),
    "mykb": ("MYKB · memory", MYKB),
    "dash": ("Dashboard · telemetry", DASH),
    "ext": ("Evaluator · trust boundary", EXT),
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>COSMOS — The Ω Graph (interactive)</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  :root {
    --bg:#0b1120; --panel:#0f172a; --border:#1e293b; --border2:#334155;
    --text:#e2e8f0; --text2:#94a3b8; --text3:#64748b; --text4:#475569;
    --rsis:#818cf8; --mykb:#22d3ee; --space:#f59e0b; --dash:#10b981; --ext:#f472b6;
  }
  body { background:var(--bg); color:var(--text); font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; min-height:100vh; display:flex; flex-direction:column; }
  .wrap { max-width:1000px; margin:0 auto; width:100%; padding:14px; flex:1; display:flex; flex-direction:column; gap:12px; }
  .head h1 { font-size:clamp(18px,4.6vw,24px); font-weight:700; letter-spacing:.4px;
    background:linear-gradient(135deg,#a5b4fc,#818cf8,#a5f3fc); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
  .head p { color:var(--text3); font-size:clamp(11px,2.8vw,13px); margin-top:4px; }
  .stage { display:flex; align-items:center; gap:10px; background:var(--panel); border:1px solid var(--border); border-radius:12px; padding:10px 14px; }
  .stage label { font:700 11px ui-monospace,Menlo,monospace; color:var(--text2); white-space:nowrap; }
  input[type=range] { flex:1; accent-color:var(--rsis); min-height:28px; touch-action:pan-x; }
  .stage .lv { font:700 12px ui-monospace,Menlo,monospace; color:#a5b4fc; min-width:96px; text-align:right; }
  .frame { background:var(--panel); border:1px solid var(--border); border-radius:14px; padding:6px; }
  svg { display:block; width:100%; height:auto; touch-action:none; }
  .readout { background:var(--panel); border:1px solid var(--border); border-radius:12px; padding:12px 14px; min-height:86px; }
  .readout h2 { font-size:14px; font-weight:700; color:var(--text); }
  .readout .facts { color:var(--text2); font-size:12px; margin-top:4px; line-height:1.55; }
  .readout .meta { color:var(--text4); font-size:10.5px; margin-top:5px; font-family:ui-monospace,Menlo,monospace; }
  .legend { display:flex; flex-wrap:wrap; gap:8px; color:var(--text3); font-size:10.5px; background:var(--panel); border:1px solid var(--border); border-radius:12px; padding:10px 12px; }
  .legend span { display:inline-flex; align-items:center; gap:6px; }
  .legend i { width:10px; height:10px; border-radius:3px; display:inline-block; }
  .axis-note { color:var(--text4); font-size:10px; text-align:center; }
  @media (min-width:768px) { .wrap { padding:22px; } }
  @media (prefers-reduced-motion: reduce) { * { transition:none !important; animation:none !important; } }
</style>
</head>
<body>
<div class="wrap">
  <div class="head">
    <h1>Ω — THE INTERACTIVE OMEGA GRAPH</h1>
    <p>The whole ecosystem on two semantic spectra — hover/tap a node to pin its readout; drag λ to move through the four integration stages.</p>
  </div>
  <div class="stage">
    <label>λ &middot; TIME</label>
    <input type="range" id="lambda" min="1" max="4" step="0.01" value="4" aria-label="integration stage λ">
    <span class="lv" id="lambdaLabel">λ₄ · full ecosystem</span>
  </div>
  <div class="frame"><svg id="omega" viewBox="0 0 1000 1000" role="img" aria-label="Omega graph of the COSMOS ecosystem"></svg></div>
  <div class="axis-note">X — THEORY ⇄ EXECUTION &nbsp;·&nbsp; Y — SHORT-TERM ↑ ⇄ LONG-TERM ↓ &nbsp;·&nbsp; r ∝ FOOTPRINT &nbsp;·&nbsp; λ = 4TH AXIS</div>
  <div class="readout" id="readout">
    <h2 id="roTitle">Ω — COSMOS</h2>
    <div class="facts" id="roFacts">4 runtimes · 27 nodes · 31 real edges. Pick a node to inspect it; drag λ to age the system from λ₁ (engine only) to λ₄ (deployed ecosystem).</div>
    <div class="meta" id="roMeta">x: theory⇄execution · y: short-term↑⇄long-term↓ · r: footprint (LOC / corpus / probes)</div>
  </div>
  <div class="legend">
    <span><i style="background:var(--space)"></i> SPACE · ideation</span>
    <span><i style="background:var(--rsis)"></i> RSIS3 · execution</span>
    <span><i style="background:var(--mykb)"></i> MyKB · memory</span>
    <span><i style="background:var(--dash)"></i> Dashboard · telemetry</span>
    <span><i style="background:var(--ext)"></i> Evaluator · trust boundary</span>
    <span style="margin-left:auto">edges = six handoffs + internal paths</span>
  </div>
</div>
<script>
const PALETTE = __PALETTE__;
const NODES = __NODES__;
const LINKS = __LINKS__;
const GROUPS = __GROUPS__;
const LAMBDA = document.getElementById('lambda');
const LABEL = document.getElementById('lambdaLabel');
const READOUT = document.getElementById('readout');
const SVG = document.getElementById('omega');
const NS = 'http://www.w3.org/2000/svg';
const AX = [[130, 130], [870, 870]]; // plot area (1000x1000 viewBox)
let pinned = null;

function pos(n, lam) {
  const t = (lam - 1) / 3;
  const x = (n.x + 1) / 2 * (AX[1][0] - AX[0][0]) + AX[0][0];
  const y = (1 - n.y) / 2 * (AX[1][1] - AX[0][1]) + AX[0][1];
  const r = (n.r0 + (n.r1 - n.r0) * t) * 1.5;
  const op = n.group === 'dash' ? Math.min(1, t * 2.6) : 1;
  return { x, y, r, op };
}

function el(tag, attrs, text) {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (text) e.textContent = text;
  return e;
}

function draw() {
  SVG.textContent = '';
  const lam = parseFloat(LAMBDA.value);
  LABEL.textContent = ['λ₁ · engine only','λ₂ · + memory','λ₃ · + ideation','λ₄ · full ecosystem'][Math.min(3, Math.max(0, Math.floor(lam - 1)))] + ' · λ=' + lam.toFixed(2);
  // axes
  const ax = el('line', {x1:AX[0][0], y1:AX[1][1], x2:AX[1][0], y2:AX[1][1], stroke:'#334155', 'stroke-width':2});
  const axy = el('line', {x1:AX[0][0], y1:AX[0][1], x2:AX[0][0], y2:AX[1][1], stroke:'#334155', 'stroke-width':2});
  SVG.appendChild(ax); SVG.appendChild(axy);
  // links under nodes
  for (const l of LINKS) {
    const a = NODES.find(n => n.id === l.a), b = NODES.find(n => n.id === l.b);
    const pa = pos(a, lam), pb = pos(b, lam);
    const col = PALETTE[l.c];
    const line = el('path', {d:'M '+pa.x+' '+pa.y+' Q '+(pa.x+pb.x)/2+' '+((pa.y+pb.y)/2-36)+' '+pb.x+' '+pb.y,
      fill:'none', stroke:col, 'stroke-width':l.c==='ext'?3:2.2, 'stroke-dasharray':l.c==='ext'?'6,4':'7,5', opacity:.75,
      'data-a':l.a, 'data-b':l.b});
    line.classList.add('edge');
    SVG.appendChild(line);
    const tx = el('text', {x:(pa.x+pb.x)/2, y:(pa.y+pb.y)/2-42, 'text-anchor':'middle', fill:'#64748b', 'font-size':11, 'font-family':'ui-monospace,Menlo,monospace'}, l.label);
    SVG.appendChild(tx);
  }
  // nodes
  for (const n of NODES) {
    const p = pos(n, lam);
    const col = PALETTE[n.group];
    const g = el('g', {'data-id':n.id, transform:'translate('+p.x+','+p.y+')', opacity:p.op});
    g.classList.add('node');
    const halo = el('circle', {r:p.r+9, fill:col, opacity:.1});
    const disc = el('circle', {r:p.r, fill:col, opacity:.22, stroke:col, 'stroke-width':2});
    const txt = el('text', {'text-anchor':'middle', dy:3, fill:'#e2e8f0', 'font-size':n.label.length>10?11:13, 'font-weight':700, 'font-family':'system-ui,sans-serif'}, n.label);
    g.appendChild(halo); g.appendChild(disc); g.appendChild(txt);
    SVG.appendChild(g);
  }
  highlight(pinned);
}

function neighbors(id) {
  const set = new Set([id]);
  for (const l of LINKS) {
    if (l.a === id) set.add(l.b);
    if (l.b === id) set.add(l.a);
  }
  return set;
}

function showReadout(n) {
  const g = GROUPS[n.group];
  document.getElementById('roTitle').textContent = n.label + ' — ' + g[0];
  document.getElementById('roTitle').style.color = g[1];
  document.getElementById('roFacts').textContent = n.facts;
  document.getElementById('roMeta').textContent =
    'x ' + n.x.toFixed(2) + ' (theory⇄execution) · y ' + n.y.toFixed(2) + ' (short↑⇄long↓) · footprint r0→r1 ' + n.r0 + '→' + n.r1;
}

function highlight(id) {
  const near = id ? neighbors(id) : null;
  SVG.querySelectorAll('.node').forEach(g => {
    const on = !near || near.has(g.dataset.id);
    g.style.opacity = on ? 1 : .14;
  });
  SVG.querySelectorAll('.edge').forEach(e => {
    const on = !near || (near.has(e.dataset.a) && near.has(e.dataset.b));
    e.style.opacity = on ? .75 : .06;
  });
}

SVG.addEventListener('pointerdown', function (ev) {
  const g = ev.target.closest ? ev.target.closest('.node') : null;
  if (g) {
    const n = NODES.find(x => x.id === g.dataset.id);
    pinned = pinned === n.id ? null : n.id;
    if (pinned) showReadout(n);
    highlight(pinned);
  }
});
SVG.addEventListener('pointermove', function (ev) {
  if (pinned) return;
  const g = ev.target.closest ? ev.target.closest('.node') : null;
  if (g) {
    const n = NODES.find(x => x.id === g.dataset.id);
    showReadout(n); highlight(n.id);
  } else {
    highlight(null);
  }
});
LAMBDA.addEventListener('input', draw);
draw();
</script>
</body>
</html>
"""


def build_html():
    nodes = []
    for (nid, label, group, x, y, r0, r1, facts) in NODES:
        nodes.append({"id": nid, "label": label, "group": group,
                      "x": round(x, 3), "y": round(y, 3), "r0": r0, "r1": r1, "facts": facts})
    links = [{"a": a, "b": b, "c": c, "label": lab} for a, b, c, lab in LINKS]
    groups = {k: list(v) for k, v in GROUPS.items()}
    return HTML_TEMPLATE.replace("__PALETTE__", json.dumps(PALETTE)).replace(
        "__NODES__", json.dumps(nodes)).replace(
        "__LINKS__", json.dumps(links)).replace(
        "__GROUPS__", json.dumps(groups))


def main():
    html = build_html()
    path = os.path.join(OUT, "x-plus-plus-omega.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"✅  {os.path.basename(path)}  ({os.path.getsize(path)//1024}KB)")
    return path


if __name__ == "__main__":
    main()
