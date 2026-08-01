"""The X++ interactive omega graph — a single self-contained HTML+SVG+JS page.

One graph of the whole ecosystem: 52 real module/artifact nodes mapped on
two semantic spectra (X = theory↔execution, Y = short-term↔long-term),
node size = footprint, node colour = owning component, edge colour =
performing component. The 4th axis is time: a λ slider (λ₁ engine →
λ₄ full ecosystem) assembles the system stage by stage — memory spawns
out of the engine, ideation out of the RRP, the dashboard last — so each
node fades in, flies in from its parent, and grows as you drag. The
canvas is pan/zoomable (drag, wheel, pinch, +/−/reset buttons). Touch-first.
"""
import json, os
from design import *

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AX_PLOT = ((90, 90), (1010, 1310))  # plot area inside the 1100×1400 viewBox

PALETTE = {
    "rsis": RSIS, "mykb": MYKB, "space": SPACE, "dash": DASH, "ext": EXT,
}

# (id, label, group, x -1..1 (theory..execution), y -1..1 (short↑..long↓),
#  r0 (λ1), r1 (λ4), facts, stage (birth λ: 1 engine · 2 memory · 3 ideation · 4 dash),
#  from (the node it assembles out of))
NODES = [
    ("l1", "L1 \u00b7 action", "rsis", 0.908, 0.792, 15, 15, "tool calls \u00b7 observations \u00b7 retries \u00b7 ~1s", 1, "l1"),
    ("l2", "L2 \u00b7 improvement", "rsis", 0.620, 0.220, 16, 16, "candidates \u00b7 25 rounds \u00b7 evaluator-gated", 1, "l1"),
    ("l3", "L3 \u00b7 evolution", "rsis", 0.400, -0.660, 14, 16, "consolidation \u00b7 strategies \u00b7 ~60s cycle", 1, "l2"),
    ("l4", "L4 \u00b7 optimizer", "rsis", 0.544, 0.549, 11, 12, "meta-parameter deltas \u00b7 tunes L1 \u00b7 checkpointed", 1, "l1"),
    ("l5", "L5 \u00b7 strategies", "rsis", 0.330, 0.080, 11, 12, "population evolution \u00b7 tunes L2 \u00b7 evaluator-gated", 1, "l2"),
    ("l6", "L6 \u00b7 identity", "rsis", 0.160, -0.420, 10, 12, "tunes L3 plateau timeout \u00b7 identity band", 1, "l3"),
    ("l7", "L7 \u00b7 meta-cog", "rsis", 0.327, 0.719, 10, 11, "tunes L4 window / thresholds", 1, "l4"),
    ("l8", "L8 \u00b7 meta-meta", "rsis", 0.060, 0.220, 9, 11, "tunes L5 on stagnation / volatility", 1, "l5"),
    ("l9", "L9 \u00b7 MMM", "rsis", -0.100, -0.100, 9, 11, "tunes L6 identity band on oscillation", 1, "l6"),
    ("evalc", "evaluator client", "rsis", 0.720, 0.020, 10, 10, "SHA-256 verify \u00b7 spawns the judge", 1, "l2"),
    ("eval", "evaluator \u00b7 immutable", "ext", 0.880, -0.240, 13, 13, "subprocess \u00b7 60s cap \u00b7 \u22645/session \u00b7 read-only", 1, "evalc"),
    ("memmgr", "memory manager", "rsis", 0.060, -0.600, 11, 12, "KG + vectors \u00b7 .rsis/knowledge_graph.json", 1, "l3"),
    ("tele", "telemetry", "rsis", 0.305, 0.660, 11, 11, "JSONL events \u00b7 extrapolator feeds L3", 1, "l1"),
    ("extrap", "extrapolator", "rsis", 0.240, 0.320, 9, 10, "trend fit on telemetry \u2192 L3 projections", 1, "tele"),
    ("ckpt", "checkpoint \u00b7 recovery", "rsis", 0.500, -0.280, 9, 10, "crash-safe state \u00b7 checkpoint before mutation", 1, "l4"),
    ("capture", "capture hooks", "mykb", -0.063, -0.417, 10, 12, "session \u2192 wiki pages + KG edges + snapshot", 2, "l3"),
    ("wiki", "wiki corpus", "mykb", -0.219, -0.961, 20, 26, "2,360+ pages \u00b7 48 domains \u00b7 source of truth", 2, "capture"),
    ("tfidf", "TF-IDF index", "mykb", -0.100, -0.700, 12, 14, "search_index.json \u00b7 built from corpus", 2, "wiki"),
    ("temporal", "temporal engine", "mykb", 0.000, -0.860, 11, 13, "git snapshots \u00b7 time-travel queries", 2, "capture"),
    ("kg", "knowledge graph", "mykb", -0.341, -0.799, 12, 14, "graph.json \u00b7 edges = consolidated lessons", 2, "wiki"),
    ("kgview", "KG graph viewer", "mykb", -0.440, -0.620, 9, 11, "okf-graph.html \u00b7 embedded in dashboard", 2, "kg"),
    ("daemon", "MyKB daemon :8765", "mykb", 0.120, 0.440, 12, 13, "only always-on server \u00b7 search + retrieval", 2, "l1"),
    ("fusion", "search fusion", "mykb", -0.220, -0.520, 9, 11, "search_fusion.py \u00b7 enhanced TF-IDF \u00b7 hybrid rerank", 2, "tfidf"),
    ("enrich", "link enrichment", "mykb", -0.560, -0.850, 9, 11, "enrich_links.py \u00b7 auto-links + backlinks", 2, "wiki"),
    ("linter", "KB linter", "mykb", -0.700, -0.600, 8, 10, "kb_linter.py \u00b7 link_check.py \u00b7 integrity audits", 2, "wiki"),
    ("wikibrowse", "wiki browser", "mykb", 0.260, -0.100, 9, 11, "mykb/index.html \u00b7 Obsidian-style reader \u00b7 embedded", 2, "daemon"),
    ("rrp", "RRP engine", "space", -0.620, 0.020, 13, 13, "recursive refinement protocol \u00b7 25 rounds/spec", 3, "rrp"),
    ("probe", "probe framework", "space", -0.820, 0.220, 17, 17, "326 probes \u00b7 7 series \u00b7 S1\u2192S7 dependency chain", 3, "rrp"),
    ("provider", "provider factory", "space", -0.420, 0.300, 11, 11, "7 LLM providers \u00b7 failover by construction", 3, "rrp"),
    ("export", "exports \u00b7 6 formats", "space", -0.300, -0.180, 10, 12, "MD / JSON / YAML / HTML / XML / TXT", 3, "probe"),
    ("webui", "SPACE web UI :8888", "space", -0.200, 0.620, 12, 12, "self-contained SPA \u00b7 launched from dashboard", 3, "rrp"),
    ("metaview", "meta viewer :8899", "space", -0.157, -0.323, 10, 10, "spec viewer for exports", 3, "export"),
    ("sstore", "session store \u00b7 SQLite", "space", -0.520, -0.460, 10, 10, "session state + artifact persistence", 3, "rrp"),
    ("intel", "intelligence", "space", -0.660, -0.300, 9, 10, "analytics \u00b7 contradiction detection on sessions", 3, "sstore"),
    ("templ", "template engine", "space", -0.740, 0.400, 9, 10, "renders RRP prompt templates", 3, "rrp"),
    ("promptapp", "prompt-app \u00b7 React", "space", -0.450, 0.520, 10, 11, "React client for RRP sessions", 3, "rrp"),
    ("vitespa", "Vite UI \u00b7 :3000", "space", -0.100, 0.780, 9, 10, "alternative React SPA", 3, "webui"),
    ("spcli", "SPACE CLI", "space", -0.950, 0.550, 10, 11, "src/cli \u00b7 commander \u00b7 init/run/export/serve \u00b7 TUI", 3, "rrp"),
    ("sconfig", "config module", "space", -0.340, 0.460, 8, 9, "src/config \u00b7 defaults + validation", 3, "rrp"),
    ("sint", "git integration", "space", -0.950, -0.200, 8, 9, "src/integration/git.ts \u00b7 external hooks", 3, "spcli"),
    ("rack", "rack \u00b7 pulses", "dash", 0.570, 0.901, 11, 12, "JSONL buffer \u2192 dashboard-data.json \u00b7 ~1s", 4, "tele"),
    ("dash", "unified dashboard :9000", "dash", 0.212, 0.895, 15, 17, "embeds wiki, KG graph, SPACE UI, meta viewer", 4, "config"),
    ("dd", "dashboard-data.json", "dash", 0.450, 0.781, 12, 13, "rack snapshot \u00b7 read via config.js", 4, "rack"),
    ("config", "config.js", "dash", 0.155, 0.780, 8, 9, "dashboard reader \u00b7 Chart.js + Tailwind", 4, "dd"),
    ("teldash", "telemetry dashboard", "dash", 0.686, 0.601, 10, 11, "Flask-style backend + 20-pulse telemetry view", 4, "rack"),
    ("gcosmos", "GH Pages \u00b7 cosmos", "dash", -0.104, 0.982, 9, 11, "root redirect \u2192 unified dashboard", 4, "dash"),
    ("ghub", "GH Pages \u00b7 hub", "dash", 0.264, 1.011, 8, 9, "all non-COSMOS projects", 4, "dash"),
    ("vercel", "vercel-deploy", "dash", 0.420, 0.960, 8, 9, "Vercel deployment config", 4, "gcosmos"),
    ("launcher", "start.sh launcher", "dash", -0.300, 1.050, 9, 10, "boots dashboard + all services \u00b7 one command", 4, "dash"),
    ("orchestrator", "cosmos CLI", "dash", -0.520, 1.000, 9, 10, "cli/cosmos \u00b7 status / start / stop / logs", 4, "launcher"),
    ("heartbeat", "heartbeat \u00b7 sentry", "dash", 0.842, 0.858, 9, 10, "infra/heartbeat \u00b7 watches.json \u00b7 auto-restart", 4, "dash"),
    ("srv", "serve-dashboard.mjs", "dash", 0.620, 1.060, 8, 9, "Node server \u00b7 alternative launcher", 4, "launcher"),
]

LINKS = [
    # SPACE internals + handoff
    ("rrp", "probe", "space", "dispatch"),
    ("rrp", "provider", "space", "ask"),
    ("rrp", "sstore", "space", "persist"),
    ("probe", "export", "space", "answers → spec"),
    ("export", "metaview", "space", "render"),
    ("rrp", "webui", "space", "host"),
    ("templ", "rrp", "space", "render"),
    ("intel", "sstore", "space", "analyze"),
    ("promptapp", "rrp", "space", "session client"),
    ("vitespa", "webui", "space", "alternative UI"),
    ("rrp", "l2", "space", "spec drafts"),
    # improvement cycle + trust boundary
    ("l2", "evalc", "rsis", "candidate"),
    ("evalc", "eval", "ext", "spawn · SHA-256"),
    ("eval", "l2", "ext", "verdict"),
    # tuning diagonals L4–L9
    ("l4", "l1", "rsis", "tune"),
    ("l5", "l2", "rsis", "tune"),
    ("l6", "l3", "rsis", "tune"),
    ("l7", "l4", "rsis", "tune"),
    ("l8", "l5", "rsis", "tune"),
    ("l9", "l6", "rsis", "tune"),
    ("extrap", "l3", "rsis", "projection"),
    ("ckpt", "l4", "rsis", "checkpoint"),
    # telemetry pipeline
    ("l1", "rack", "rsis", "pulse"),
    ("tele", "rack", "rsis", "pulse"),
    ("rack", "dd", "dash", "extract"),
    ("dd", "config", "dash", "read"),
    ("config", "dash", "dash", "render"),
    ("teldash", "rack", "dash", "telemetry views"),
    # memory write path + retrieval
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
    # dashboard embeds + deployment
    ("dash", "webui", "dash", "launch :8888"),
    ("dash", "gcosmos", "dash", "redirect"),
    ("dash", "metaview", "dash", "embed"),
    ("dash", "daemon", "dash", "embed wiki"),
    ("dash", "kgview", "dash", "embed graph"),
    ("vercel", "gcosmos", "dash", "deploy"),
    # MyKB extended modules
    ("daemon", "fusion", "mykb", "query v2"),
    ("tfidf", "fusion", "mykb", "hybrid index"),
    ("wiki", "enrich", "mykb", "auto-link"),
    ("enrich", "kg", "mykb", "backlink edges"),
    ("wiki", "linter", "mykb", "integrity audit"),
    ("daemon", "wikibrowse", "mykb", "serve :8765"),
    ("dash", "wikibrowse", "dash", "embed"),
    # SPACE extended modules
    ("rrp", "spcli", "space", "CLI entry"),
    ("spcli", "export", "space", "export cmd"),
    ("rrp", "sconfig", "space", "config load"),
    ("spcli", "sint", "space", "git hooks"),
    # launcher / orchestrator / heartbeat
    ("launcher", "dash", "dash", "serve :9000"),
    ("launcher", "orchestrator", "dash", "invokes"),
    ("orchestrator", "heartbeat", "dash", "supervise"),
    ("heartbeat", "dash", "dash", "watch"),
    ("heartbeat", "daemon", "dash", "watch"),
    ("heartbeat", "webui", "dash", "watch"),
    ("launcher", "srv", "dash", "alternative"),
    ("srv", "dash", "dash", "serve"),
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
  .stage .lv { font:700 12px ui-monospace,Menlo,monospace; color:#a5b4fc; min-width:120px; text-align:right; }
  .frame { position:relative; background:var(--panel); border:1px solid var(--border); border-radius:14px; padding:6px; }
  svg { display:block; width:100%; height:auto; touch-action:none; cursor:grab; user-select:none; -webkit-user-select:none; }
  svg.panning { cursor:grabbing; }
  .zoom-ctl { position:absolute; top:16px; right:16px; display:flex; gap:6px; z-index:5; }
  .zoom-ctl button { width:34px; height:34px; border-radius:9px; border:1px solid var(--border2); background:rgba(15,23,42,.88); color:var(--text); font:700 16px system-ui; cursor:pointer; user-select:none; -webkit-user-select:none; }
  .zoom-ctl button:active { background:var(--border2); }
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
    <p>The whole ecosystem on two semantic spectra — pan &amp; zoom the canvas, hover/tap a node to pin its readout, drag λ to watch the system assemble: engine → memory → ideation → dashboard.</p>
  </div>
  <div class="stage">
    <label>λ &middot; TIME</label>
    <input type="range" id="lambda" min="1" max="4" step="0.01" value="4" aria-label="integration stage λ">
    <span class="lv" id="lambdaLabel">λ₄ · full ecosystem</span>
  </div>
  <div class="frame">
    <svg id="omega" viewBox="0 0 1100 1400" role="img" aria-label="Omega graph of the COSMOS ecosystem"></svg>
    <div class="zoom-ctl">
      <button id="zIn" title="Zoom in" aria-label="Zoom in">+</button>
      <button id="zOut" title="Zoom out" aria-label="Zoom out">−</button>
      <button id="zReset" title="Reset view" aria-label="Reset view">⤾</button>
    </div>
  </div>
  <div class="axis-note">X — THEORY ⇄ EXECUTION &nbsp;·&nbsp; Y — SHORT-TERM ↑ ⇄ LONG-TERM ↓ &nbsp;·&nbsp; r ∝ FOOTPRINT &nbsp;·&nbsp; λ = 4TH AXIS (drag to assemble)</div>
  <div class="readout" id="readout">
    <h2 id="roTitle">Ω — COSMOS</h2>
    <div class="facts" id="roFacts">52 nodes · 64 real edges · 5 colour groups. Pick a node to inspect it; drag λ to age the system from λ₁ (engine only) to λ₄ (deployed ecosystem).</div>
    <div class="meta" id="roMeta">x: theory⇄execution · y: short-term↑⇄long-term↓ · r: footprint · drag the canvas or pinch to pan/zoom</div>
  </div>
  <div class="legend">
    <span><i style="background:var(--space)"></i> SPACE · ideation</span>
    <span><i style="background:var(--rsis)"></i> RSIS3 · execution</span>
    <span><i style="background:var(--mykb)"></i> MyKB · memory</span>
    <span><i style="background:var(--dash)"></i> Dashboard · telemetry</span>
    <span><i style="background:var(--ext)"></i> Evaluator · trust boundary</span>
    <span style="margin-left:auto">edges coloured by performing component · λ assembles: 1 engine → 2 memory → 3 ideation → 4 dash</span>
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
const AX = [[90, 90], [1010, 1310]];       // plot area inside the 1100×1400 viewBox
const VB0 = {x:0, y:0, w:1100, h:1400};
const STAGE_NAMES = ['λ₁ · engine only', 'λ₂ · + memory', 'λ₃ · + ideation', 'λ₄ · full ecosystem'];
let vb = {x:VB0.x, y:VB0.y, w:VB0.w, h:VB0.h};
let pinned = null;

/* ── λ model: every node is born at n.st and assembles out of n.src ── */
function appear(n, lam) {
  const a = (lam - (n.st - 0.6)) / 0.6;
  return Math.max(0, Math.min(1, a));
}
function pos(n, lam) {
  const a = appear(n, lam);
  const t = (lam - 1) / 3;
  const e = a * a * (3 - 2 * a);            // smoothstep: fly-in + fade-in
  const nx = n.sx + (n.x - n.sx) * e;       // interpolate in -1..1 spectra space
  const ny = n.sy + (n.y - n.sy) * e;
  const x = (nx + 1) / 2 * (AX[1][0] - AX[0][0]) + AX[0][0];
  const y = (1 - ny) / 2 * (AX[1][1] - AX[0][1]) + AX[0][1];
  const r = (n.r0 + (n.r1 - n.r0) * t) * 1.5;
  return {x:x, y:y, r:r, a:a};
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
  const si = Math.min(3, Math.max(0, Math.floor(lam - 1)));
  LABEL.textContent = STAGE_NAMES[si] + ' · λ=' + lam.toFixed(2);
  // axes
  SVG.appendChild(el('line', {x1:AX[0][0], y1:AX[1][1], x2:AX[1][0], y2:AX[1][1], stroke:'#334155', 'stroke-width':2}));
  SVG.appendChild(el('line', {x1:AX[0][0], y1:AX[0][1], x2:AX[0][0], y2:AX[1][1], stroke:'#334155', 'stroke-width':2}));
  // links under nodes
  for (const l of LINKS) {
    const a = NODES.find(n => n.id === l.a), b = NODES.find(n => n.id === l.b);
    const pa = pos(a, lam), pb = pos(b, lam);
    const op = Math.min(pa.a, pb.a) * 0.8;
    if (op <= 0.02) continue;
    const col = PALETTE[l.c];
    const d = 'M '+pa.x+' '+pa.y+' Q '+(pa.x+pb.x)/2+' '+((pa.y+pb.y)/2-36)+' '+pb.x+' '+pb.y;
    const line = el('path', {d:d, fill:'none', stroke:col, 'stroke-width':l.c==='ext'?3:2.2,
      'stroke-dasharray':l.c==='ext'?'6,4':'7,5', opacity:op, 'data-a':l.a, 'data-b':l.b});
    line.classList.add('edge');
    line.dataset.op = op;
    SVG.appendChild(line);
    const tl = el('text', {x:(pa.x+pb.x)/2, y:(pa.y+pb.y)/2-42, 'text-anchor':'middle',
      fill:'#64748b', 'font-size':12, 'font-family':'ui-monospace,Menlo,monospace', opacity:op}, l.label);
    tl.classList.add('elabel');
    SVG.appendChild(tl);
  }
  // nodes
  for (const n of NODES) {
    const p = pos(n, lam);
    if (p.a <= 0.02) continue;
    const col = PALETTE[n.group];
    const g = el('g', {'data-id':n.id, transform:'translate('+p.x+','+p.y+')'});
    g.classList.add('node');
    g.dataset.op = p.a;
    const halo = el('circle', {r:p.r+9, fill:col, opacity:.1});
    const disc = el('circle', {r:p.r, fill:col, opacity:.22, stroke:col, 'stroke-width':2});
    const fs = n.label.length > 10 ? 12 : 14;
    const txt = el('text', {'text-anchor':'middle', dy:3, fill:'#e2e8f0', 'font-size':fs,
      'font-weight':700, 'font-family':'system-ui,sans-serif'}, n.label);
    g.appendChild(halo); g.appendChild(disc); g.appendChild(txt);
    SVG.appendChild(g);
  }
  highlight(pinned);
  applyVB();
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
    'x ' + n.x.toFixed(2) + ' (theory⇄execution) · y ' + n.y.toFixed(2) + ' (short↑⇄long↓) · footprint r0→r1 ' + n.r0 + '→' + n.r1 +
    ' · born at λ' + n.st + ' · assembles from ' + n.src;
}

function highlight(id) {
  const near = id ? neighbors(id) : null;
  SVG.querySelectorAll('.node').forEach(g => {
    const base = parseFloat(g.dataset.op || '1');
    g.style.opacity = !near || near.has(g.dataset.id) ? base : base * 0.14;
  });
  SVG.querySelectorAll('.edge').forEach(e => {
    const base = parseFloat(e.dataset.op || '0.8');
    e.style.opacity = !near || (near.has(e.dataset.a) && near.has(e.dataset.b)) ? base : base * 0.08;
  });
}

/* ── pan & zoom (viewBox transform) ── */
function applyVB() {
  SVG.setAttribute('viewBox', vb.x + ' ' + vb.y + ' ' + vb.w + ' ' + vb.h);
  const hide = vb.w > VB0.w * 1.12;         // zoomed out past the default → drop edge labels
  SVG.querySelectorAll('.elabel').forEach(t => t.style.display = hide ? 'none' : '');
}
function clientToVB(px, py) {
  const r = SVG.getBoundingClientRect();
  return {x: vb.x + (px - r.left) * vb.w / r.width, y: vb.y + (py - r.top) * vb.h / r.height};
}
function zoomAt(f, cx, cy) {
  const nw = Math.max(240, Math.min(3400, vb.w * f));
  const nh = nw * VB0.h / VB0.w;
  const k = nw / vb.w;
  vb.x = cx - (cx - vb.x) * k;
  vb.y = cy - (cy - vb.y) * k;
  vb.w = nw; vb.h = nh;
  applyVB();
}
function resetView() { vb = {x:VB0.x, y:VB0.y, w:VB0.w, h:VB0.h}; applyVB(); }

const pointers = new Map();
let panStart = null, panMoved = false, pinch = null;

SVG.addEventListener('pointerdown', function (ev) {
  const g = ev.target.closest ? ev.target.closest('.node') : null;
  if (g) {
    const n = NODES.find(x => x.id === g.dataset.id);
    pinned = pinned === n.id ? null : n.id;
    if (pinned) showReadout(n);
    highlight(pinned);
    return;
  }
  ev.preventDefault();
  SVG.classList.add('panning');
  SVG.setPointerCapture(ev.pointerId);
  pointers.set(ev.pointerId, {x: ev.clientX, y: ev.clientY});
  panStart = {x: vb.x, y: vb.y, px: ev.clientX, py: ev.clientY};
  panMoved = false;
  if (pointers.size === 2) {
    const p = [...pointers.values()];
    pinch = {d: Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y), c: {x: (p[0].x + p[1].x) / 2, y: (p[0].y + p[1].y) / 2}};
  }
});

SVG.addEventListener('pointermove', function (ev) {
  if (!pointers.has(ev.pointerId)) {
    if (pointers.size === 0 && !pinned && !panMoved) {
      const g = ev.target.closest ? ev.target.closest('.node') : null;
      if (g) { const n = NODES.find(x => x.id === g.dataset.id); showReadout(n); highlight(n.id); }
      else highlight(null);
    }
    return;
  }
  pointers.set(ev.pointerId, {x: ev.clientX, y: ev.clientY});
  if (pointers.size === 2 && pinch) {
    const p = [...pointers.values()];
    const d = Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y);
    const c = {x: (p[0].x + p[1].x) / 2, y: (p[0].y + p[1].y) / 2};
    const v = clientToVB(c.x, c.y);
    zoomAt(d / pinch.d, v.x, v.y);
    const r = SVG.getBoundingClientRect();
    vb.x -= (c.x - pinch.c.x) * vb.w / r.width;
    vb.y -= (c.y - pinch.c.y) * vb.h / r.height;
    applyVB();
    pinch.d = d; pinch.c = c;
    panMoved = true;
    return;
  }
  const r = SVG.getBoundingClientRect();
  const dx = (ev.clientX - panStart.px) * vb.w / r.width;
  const dy = (ev.clientY - panStart.py) * vb.h / r.height;
  if (Math.abs(ev.clientX - panStart.px) + Math.abs(ev.clientY - panStart.py) > 4) panMoved = true;
  vb.x = panStart.x - dx;
  vb.y = panStart.y - dy;
  applyVB();
});

function endPointer(ev) {
  if (!pointers.has(ev.pointerId)) return;
  const wasPan = panMoved;
  pointers.delete(ev.pointerId);
  if (pointers.size < 2) pinch = null;
  if (pointers.size === 1) {
    const p = [...pointers.values()][0];
    panStart = {x: vb.x, y: vb.y, px: p.x, py: p.y};
  }
  if (pointers.size === 0) {
    SVG.classList.remove('panning');
    panMoved = false;
    if (!wasPan && ev.type === 'pointerup') { pinned = null; highlight(null); }
  }
}
SVG.addEventListener('pointerup', endPointer);
SVG.addEventListener('pointercancel', endPointer);

SVG.addEventListener('wheel', function (ev) {
  ev.preventDefault();
  const v = clientToVB(ev.clientX, ev.clientY);
  zoomAt(Math.exp(-ev.deltaY * 0.0014), v.x, v.y);
}, {passive:false});

SVG.addEventListener('dblclick', function (ev) { ev.preventDefault(); resetView(); });
document.getElementById('zIn').addEventListener('click', function () { zoomAt(1.4, vb.x + vb.w / 2, vb.y + vb.h / 2); });
document.getElementById('zOut').addEventListener('click', function () { zoomAt(1 / 1.4, vb.x + vb.w / 2, vb.y + vb.h / 2); });
document.getElementById('zReset').addEventListener('click', resetView);

LAMBDA.addEventListener('input', draw);
draw();
</script>
</body>
</html>
"""


def build_html():
    final = {n[0]: (n[3], n[4]) for n in NODES}
    nodes = []
    for (nid, label, group, x, y, r0, r1, facts, st, src) in NODES:
        src_xy = final.get(src, (x, y))
        nodes.append({"id": nid, "label": label, "group": group,
                      "x": round(x, 3), "y": round(y, 3), "r0": r0, "r1": r1,
                      "facts": facts, "st": st, "src": src,
                      "sx": round(src_xy[0], 3), "sy": round(src_xy[1], 3)})
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
