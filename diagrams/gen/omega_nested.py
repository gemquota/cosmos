"""X++ nested-loop graph — the whole ecosystem, with the 9 loops rendered nested.

Same data as the omega graph (all 52 nodes, all 64 LINKS, 5 colour groups) but
the L1–L9 loop stack is drawn as concentric rings, L1 innermost → L9 outermost,
as the loops were originally conceived: each ring wraps the previous one, outer
loops tune inner targets (L4→L1, L5→L2, L6→L3, L7→L4, L8→L5, L9→L6), and the
runtime core L1→L2→L3 is drawn as a labeled chain through the innermost rings.

Layout: semantic (x,y) anchors preserved; the loop stack sits at the semantic
centroid of the L-nodes; every other node keeps its semantic position unless it
falls inside the outermost ring, in which case it is pushed radially out. A
force pass separates ring labels, loop discs and pushed nodes. λ slider, pan,
zoom (fixed direction) and readouts identical to the omega graph.
"""
import json, math, os
from omega import NODES, LINKS, GROUPS, PALETTE, OUT, AX_PLOT

W = AX_PLOT[1][0] - AX_PLOT[0][0]          # 920
H = AX_PLOT[1][1] - AX_PLOT[0][1]          # 1220
AX0 = AX_PLOT[0]

LOOP_IDS = ["l%d" % i for i in range(1, 10)]
TUNE = {a: b for a, b, c, lab in LINKS if a in LOOP_IDS and b in LOOP_IDS and lab == "tune"}
CHAIN = [("l1", "l2"), ("l2", "l3")]

def to_plot(x, y):
    return ((x + 1) / 2 * W + AX0[0], (1 - y) / 2 * H + AX0[1])

# ── semantic centroid of the loop stack (omega NODES coords are already relaxed) ──
lp = {n[0]: (n[3], n[4]) for n in NODES if n[0] in LOOP_IDS}
C = (sum(p[0] for p in lp.values()) / len(lp), sum(p[1] for p in lp.values()) / len(lp))
CX, CY = to_plot(*C)

RING0, RINGSTEP = 48.0, 36.0                # px: r1=48 … r9=336
def ring_r(i):                              # i is 1-based
    return RING0 + (i - 1) * RINGSTEP

def bearing(x, y):                          # y-up angle from centroid, radians
    return math.atan2(y - C[1], x - C[0])

# ── loop node bearings with a minimum angular separation ──
angs = {nid: bearing(*p) for nid, p in lp.items()}
MINSEP = 0.24                               # ~14°
for _ in range(400):
    moved = False
    items = sorted(angs.items(), key=lambda kv: kv[1])
    for k in range(len(items)):
        a, ang_a = items[k]
        b, ang_b = items[(k + 1) % len(items)]
        gap = ang_b - ang_a if k < len(items) - 1 else ang_b + 2 * math.pi - ang_a
        if gap < MINSEP:
            d = (MINSEP - gap) / 2
            angs[b] += d
            moved = True
    if not moved:
        break

loop_pos = {}
for nid in LOOP_IDS:
    r = ring_r(int(nid[1:]))
    a = angs[nid]
    loop_pos[nid] = (CX + r * math.cos(a), CY - r * math.sin(a))

# ── non-loop nodes: omega's relaxed position, pushed out of the bullseye ──
R9 = ring_r(9)
node_plot = {}
pushed = []                                 # (id, bearing)
for (nid, label, group, x, y, r0, r1, facts, st, src) in NODES:
    if nid in loop_pos:
        node_plot[nid] = loop_pos[nid]
        continue
    px, py = to_plot(x, y)
    dx, dy = px - CX, py - CY
    d = math.hypot(dx, dy)
    keep = R9 + 26 + max(r0, r1) * 1.5 / 2
    if d < keep and d > 1e-6:
        px = CX + dx / d * keep
        py = CY + dy / d * keep
        pushed.append((nid, bearing(x, y)))
    node_plot[nid] = (px, py)

# fan out pushed nodes so none share an angular slot (avoids same-radius collisions)
if pushed:
    pushed.sort(key=lambda kv: kv[1])
    MINP = 0.17                              # ~10°
    for _ in range(60):
        ok = True
        n = len(pushed)
        for k in range(n):
            _, ang_a = pushed[k]
            _, ang_b = pushed[(k + 1) % n]
            gap = ang_b - ang_a if k < n - 1 else ang_b + 2 * math.pi - ang_a
            if gap < MINP:
                d = (MINP - gap) / 2
                pushed[(k + 1) % n] = (pushed[(k + 1) % n][0], pushed[(k + 1) % n][1] + d)
                ok = False
        if ok:
            break
    for nid, a in pushed:
        n = next(n for n in NODES if n[0] == nid)
        keep = R9 + 26 + max(n[5], n[6]) * 1.5 / 2
        node_plot[nid] = (CX + keep * math.cos(a), CY - keep * math.sin(a))

# ── relax pushed discs against all fixed discs (loop + non-pushed) ──
fixed_discs = []
for nid, (x, y) in node_plot.items():
    if nid in loop_pos or nid in [k for k, _ in pushed]:
        continue
    n = next(n for n in NODES if n[0] == nid)
    r = max(n[5], n[6]) * 1.5 + 2
    fixed_discs.append((nid, x, y, r))

pushed_ids = [nid for nid, _ in pushed]
push_ents = []
for nid in pushed_ids:
    x, y = node_plot[nid]
    n = next(n for n in NODES if n[0] == nid)
    push_ents.append([nid, x, y, max(n[5], n[6]) * 1.5, x, y])

def pnd(a, b):
    dx = a[1] - b[1]; dy = a[2] - b[2]
    sx = a[3] + b[3]; sy = a[3] + b[3]
    return (dx * dx) / (sx * sx) + (dy * dy) / (sy * sy)

for _ in range(4000):
    for i in range(len(push_ents)):
        a = push_ents[i]
        for j in range(i + 1, len(push_ents)):
            b = push_ents[j]
            nd = pnd(a, b)
            if nd < 1.22:
                dx = a[1] - b[1]; dy = a[2] - b[2]
                dist = math.hypot(dx, dy) or 1e-9
                ux, uy = dx / dist, dy / dist
                f = min((1.22 - nd) * (a[3] + b[3]) * 0.10, 4.0)
                a[1] += ux * f; a[2] += uy * f
                b[1] -= ux * f; b[2] -= uy * f
        for d in fixed_discs:
            nd = pnd(a, d)
            if nd < 1.18:
                dx = a[1] - d[1]; dy = a[2] - d[2]
                dist = math.hypot(dx, dy) or 1e-9
                ux, uy = dx / dist, dy / dist
                f = min((1.18 - nd) * (a[3] + d[3]) * 0.10, 4.0)
                a[1] += ux * f; a[2] += uy * f
    for e in push_ents:
        e[1] += (e[4] - e[1]) * 0.05
        e[2] += (e[5] - e[2]) * 0.05
for e in push_ents:
    node_plot[e[0]] = (e[1], e[2])

# ── ring labels (opposite the loop node, just outside the ring) ──
ring_meta = []
for nid in LOOP_IDS:
    i = int(nid[1:])
    r = ring_r(i)
    a = angs[nid] + math.pi                     # opposite the node
    sub = TUNE.get(nid)
    label = next(n[1] for n in NODES if n[0] == nid)
    txt = label + (" · tunes L%s" % sub[1:] if sub else "")
    ring_meta.append({"id": nid, "r": round(r, 1), "a": a,
                      "lx": CX + (r + 16) * math.cos(a), "ly": CY - (r + 16) * math.sin(a),
                      "label": txt, "sub": "tunes L%s" % sub[1:] if sub else None,
                      "w": 6.2 * len(txt) / 2 + 8})

# ── force pass: ring labels only; every disc is fixed ──
lab = [[m["id"], m["lx"], m["ly"], m["w"], 17.0, m["lx"], m["ly"]] for m in ring_meta]
discs = [(x, y, r) for _, x, y, r in fixed_discs] +         [(x, y, max(n[5], n[6]) * 1.5 + 2) for nid, (x, y) in loop_pos.items() for n in [next(n for n in NODES if n[0] == nid)]]

def lab_nd(a, b):
    dx = a[1] - b[1]; dy = a[2] - b[2]
    sx = a[3] + b[3]; sy = a[4] + b[4]
    return (dx * dx) / (sx * sx) + (dy * dy) / (sy * sy)

def disc_nd(l, d):
    dx = l[1] - d[0]; dy = l[2] - d[1]
    sx = l[3] + d[2]; sy = l[4] + d[2]
    return (dx * dx) / (sx * sx) + (dy * dy) / (sy * sy)

for it in range(15000):
    for i in range(len(lab)):
        for j in range(i + 1, len(lab)):
            a, b = lab[i], lab[j]
            nd = lab_nd(a, b)
            if nd < 1.35:
                dx = a[1] - b[1]; dy = a[2] - b[2]
                dist = math.hypot(dx, dy) or 1e-9
                ux, uy = dx / dist, dy / dist
                f = min((1.35 - nd) * (a[3] + b[3]) * 0.08, 6.0)
                a[1] += ux * f; a[2] += uy * f
                b[1] -= ux * f; b[2] -= uy * f
        for d in discs:
            nd = disc_nd(lab[i], d)
            if nd < 1.25:
                dx = lab[i][1] - d[0]; dy = lab[i][2] - d[1]
                dist = math.hypot(dx, dy) or 1e-9
                ux, uy = dx / dist, dy / dist
                f = min((1.25 - nd) * (lab[i][3] + d[2]) * 0.10, 5.0)
                lab[i][1] += ux * f; lab[i][2] += uy * f
    for e in lab:
        e[1] += (e[5] - e[1]) * 0.06          # hold ring anchor
        e[2] += (e[6] - e[2]) * 0.06
        d = math.hypot(e[1] - CX, e[2] - CY)
        rr = ring_r(int(e[0][1:]))
        if d < rr + 5:                         # keep outside its own ring
            u = 1 if d < 1e-6 else (rr + 5) / d
            e[1] = CX + (e[1] - CX) * u
            e[2] = CY + (e[2] - CY) * u

for m, e in zip(ring_meta, lab):
    m["bx"] = round(e[1], 1); m["by"] = round(e[2], 1)

# ── write final coords into NODES / RINGS JSON ──
final_nodes = []
for (nid, label, group, x, y, r0, r1, facts, st, src) in NODES:
    px, py = node_plot[nid]
    sx, sy = node_plot.get(src, node_plot[nid])
    final_nodes.append({"id": nid, "label": label, "group": group,
                        "x": round(x, 3), "y": round(y, 3),
                        "px": round(px, 1), "py": round(py, 1),
                        "sx": round(sx, 1), "sy": round(sy, 1),
                        "r0": r0, "r1": r1, "facts": facts, "st": st, "src": src})
final_links = [{"a": a, "b": b, "c": c, "label": lab} for a, b, c, lab in LINKS]
final_groups = {k: list(v) for k, v in GROUPS.items()}
final_rings = [{"id": m["id"], "r": m["r"], "node": [round(loop_pos[m["id"]][0], 1), round(loop_pos[m["id"]][1], 1)],
                "label": m["label"], "sub": m["sub"],
                "lx": m["bx"], "ly": m["by"]} for m in ring_meta]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>COSMOS — The Nested-Loop Graph (interactive)</title>
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
    <h1>Ω⊃9 — THE NESTED-LOOP GRAPH</h1>
    <p>The whole ecosystem — every node &amp; edge of the Ω graph — with the 9 loops rendered nested, L₁ ⊂ L₂ ⊂ … ⊂ L₉: each ring wraps the previous, outer loops tune inner targets. Pan &amp; zoom, hover/tap a node or ring, drag λ to watch it assemble.</p>
  </div>
  <div class="stage">
    <label>λ &middot; TIME</label>
    <input type="range" id="lambda" min="1" max="4" step="0.01" value="4" aria-label="integration stage λ">
    <span class="lv" id="lambdaLabel">λ₄ · full ecosystem</span>
  </div>
  <div class="frame">
    <svg id="omega" viewBox="0 0 1100 1400" role="img" aria-label="Nested-loop graph of the COSMOS ecosystem"></svg>
    <div class="zoom-ctl">
      <button id="zIn" title="Zoom in" aria-label="Zoom in">+</button>
      <button id="zOut" title="Zoom out" aria-label="Zoom out">−</button>
      <button id="zReset" title="Reset view" aria-label="Reset view">⤾</button>
    </div>
  </div>
  <div class="axis-note">◎ 9 NESTED LOOPS — L₁ ⊂ L₂ ⊂ … ⊂ L₉ (outer tunes inner: L4→L1 · L5→L2 · L6→L3 · L7→L4 · L8→L5 · L9→L6) &nbsp;·&nbsp; X — THEORY ⇄ EXECUTION &nbsp;·&nbsp; Y — SHORT-TERM ↑ ⇄ LONG-TERM ↓ &nbsp;·&nbsp; r ∝ FOOTPRINT</div>
  <div class="readout" id="readout">
    <h2 id="roTitle">Ω⊃9 — COSMOS</h2>
    <div class="facts" id="roFacts">52 nodes · 64 real edges · 9 nested loops · 3-loop runtime chain (L1→L2→L3) · 5 colour groups. Pick a node or ring to inspect it; drag λ to age the system from λ₁ (engine only) to λ₄ (deployed ecosystem).</div>
    <div class="meta" id="roMeta">loops nested by construction · outer loops tune inner targets · drag the canvas or pinch to pan/zoom</div>
  </div>
  <div class="legend">
    <span><i style="background:var(--space)"></i> SPACE · ideation</span>
    <span><i style="background:var(--rsis)"></i> RSIS3 · execution</span>
    <span><i style="background:var(--mykb)"></i> MyKB · memory</span>
    <span><i style="background:var(--dash)"></i> Dashboard · telemetry</span>
    <span><i style="background:var(--ext)"></i> Evaluator · trust boundary</span>
    <span><i style="background:var(--rsis)"></i> ◎ L_i ⊂ L_{i+1}</span>
    <span style="margin-left:auto">edges coloured by performing component · λ assembles: 1 engine → 2 memory → 3 ideation → 4 dash</span>
  </div>
</div>
<script>
const PALETTE = __PALETTE__;
const NODES = __NODES__;
const LINKS = __LINKS__;
const RINGS = __RINGS__;
const CHAIN = [{"a":"l1","b":"l2"},{"a":"l2","b":"l3"}];
const GROUPS = __GROUPS__;
const LAMBDA = document.getElementById('lambda');
const LABEL = document.getElementById('lambdaLabel');
const READOUT = document.getElementById('readout');
const SVG = document.getElementById('omega');
const NS = 'http://www.w3.org/2000/svg';
const AX = [[90, 90], [1010, 1310]];
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
  const x = n.sx + (n.px - n.sx) * e;       // interpolate in plot space
  const y = n.sy + (n.py - n.sy) * e;
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
  SVG.appendChild(el('line', {x1:AX[0][0], y1:AX[1][1], x2:AX[1][0], y2:AX[1][1], stroke:'#1e293b', 'stroke-width':2}));
  SVG.appendChild(el('line', {x1:AX[0][0], y1:AX[0][1], x2:AX[0][0], y2:AX[1][1], stroke:'#1e293b', 'stroke-width':2}));
  // nested loop rings (under edges)
  for (const m of RINGS) {
    const n = NODES.find(x => x.id === m.id);
    const a = appear(n, lam);
    if (a <= 0.02) continue;
    const r = m.r * (0.4 + 0.6 * a);
    const g = el('g', {'data-id':m.id});
    g.classList.add('ring');
    g.dataset.op = a;
    g.appendChild(el('circle', {cx:m.node[0], cy:m.node[1], r:m.r, fill:'none',
      stroke:'#818cf8', 'stroke-width':1.3, opacity:0.10 + 0.16 * a,
      'stroke-dasharray': (parseInt(m.id[1]) % 2) ? '' : '3,4'}));
    const tl = el('text', {x:m.lx, y:m.ly, 'text-anchor':'middle', fill:'#a5b4fc',
      'font-size':11, 'font-weight':700, 'font-family':'ui-monospace,Menlo,monospace', opacity:0.9});
    tl.classList.add('rlabel');
    g.appendChild(tl);
    const tspan = el('tspan', {x:m.lx, dy:13, fill:'#818cf8', 'font-size':9.5, 'font-weight':400}, m.label);
    tl.appendChild(tspan);
    SVG.appendChild(g);
  }
  // runtime core chain L1→L2→L3
  for (const c of CHAIN) {
    const a = NODES.find(x => x.id === c.a), b = NODES.find(x => x.id === c.b);
    const pa = pos(a, lam), pb = pos(b, lam);
    const op = Math.min(pa.a, pb.a) * 0.95;
    if (op <= 0.02) continue;
    const mx = (pa.x + pb.x) / 2, my = (pa.y + pb.y) / 2;
    const d = 'M '+pa.x+' '+pa.y+' Q '+mx+' '+my+' '+pb.x+' '+pb.y;
    const line = el('path', {d:d, fill:'none', stroke:'#a5b4fc', 'stroke-width':3.2, opacity:op, 'data-a':c.a, 'data-b':c.b});
    line.classList.add('edge');
    line.dataset.op = op;
    SVG.appendChild(line);
    const tl = el('text', {x:mx, y:my + 24, 'text-anchor':'middle', fill:'#a5b4fc',
      'font-size':10.5, 'font-family':'ui-monospace,Menlo,monospace', opacity:op}, 'runtime chain');
    tl.classList.add('elabel');
    SVG.appendChild(tl);
  }
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
  SVG.querySelectorAll('.node, .ring').forEach(g => {
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
  const hide = vb.w > VB0.w * 1.12;
  SVG.querySelectorAll('.elabel, .rlabel').forEach(t => t.style.display = hide ? 'none' : '');
}
function clientToVB(px, py) {
  const r = SVG.getBoundingClientRect();
  return {x: vb.x + (px - r.left) * vb.w / r.width, y: vb.y + (py - r.top) * vb.h / r.height};
}
function zoomAt(f, cx, cy) {
  const nw = Math.max(240, Math.min(3400, vb.w / f));
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
  const g = ev.target.closest ? ev.target.closest('.node, .ring') : null;
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
      const g = ev.target.closest ? ev.target.closest('.node, .ring') : null;
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
    return (HTML_TEMPLATE.replace("__PALETTE__", json.dumps(PALETTE))
            .replace("__NODES__", json.dumps(final_nodes))
            .replace("__LINKS__", json.dumps(final_links))
            .replace("__RINGS__", json.dumps(final_rings))
            .replace("__GROUPS__", json.dumps(final_groups)))


def main():
    html = build_html()
    path = os.path.join(OUT, "x-plus-plus-nested.html")
    with open(path, "w") as f:
        f.write(html)
    print("✅  %s  (%dKB)" % (os.path.basename(path), os.path.getsize(path) // 1024))
    return path


if __name__ == "__main__":
    main()
