var AD, PD, g, pu, sh, ch = {};

// Data loading: supports both API mode and direct file mode
function loadData() {
  var url;
  if (typeof USE_API !== 'undefined' && USE_API) {
    var base = typeof API_BASE !== 'undefined' ? API_BASE : '';
    var ep = typeof API_DATA_ENDPOINT !== 'undefined' ? API_DATA_ENDPOINT : '/api/data';
    url = base + ep;
  } else {
    var dir = typeof DATA_DIR !== 'undefined' ? DATA_DIR : '';
    var file = typeof DATA_FILE !== 'undefined' ? DATA_FILE : 'dashboard-data.json';
    url = dir + file;
  }

  fetch(url)
    .then(function(r) {
      if (!r.ok) throw new Error('HTTP ' + r.status + ' ' + r.statusText);
      return r.json();
    })
    .then(function(d) {
      if (d.error) throw new Error(d.error);
      AD = d;
      PD = d.pulse_data || {};
      g = AD.goals || [];
      pu = AD.pulses || [];
      sh = AD.score_history || {};
      document.getElementById('load').style.display = 'none';
      document.getElementById('app').style.display = 'block';
      renderAll();
    })
    .catch(function(e) {
      document.getElementById('load').innerHTML =
        '<div class="text-red-400 text-center mt-10">' +
        'Error loading data: ' + e.message +
        '<br><br>' +
        '<button onclick="location.reload()" ' +
        'style="background:#6366f1;color:white;border:none;padding:8px 20px;border-radius:8px;cursor:pointer;font-size:14px">Retry</button>' +
        '</div>';
    });
}

function renderAll() { ly(); rg(); rp(); rc(); rcb(); bk(); pf(); sw('overview'); }

var _chartsInited = false;

function sw(n) {
  if (n === 'graphs' && !_chartsInited) {
    _chartsInited = true;
    requestAnimationFrame(function() {
      requestAnimationFrame(function() { ic(); });
    });
  }
  document.querySelectorAll('.tb').forEach(function(t) {
    t.classList.remove('bg-indigo-500', 'text-white', 'shadow');
    t.classList.add('text-slate-400', 'hover:text-slate-200', 'hover:bg-slate-700/40');
  });
  document.querySelectorAll('.tb[data-t="' + n + '"]').forEach(function(t) {
    t.classList.add('bg-indigo-500', 'text-white', 'shadow');
  });
  document.querySelectorAll('.tab-body').forEach(function(b) { b.classList.add('hide'); });
  var el = document.getElementById('b-' + n);
  if (el) el.classList.remove('hide');
}

function fa(a) {
  if (!a && a !== 0) return '';
  if (typeof a === 'string') return a;
  if (typeof a === 'object') { try { return JSON.stringify(a); } catch (e) { return String(a); } }
  return String(a);
}

// ── Layer Scores ──────────────────────────────────────────────

function ly() {
  var ks = Object.keys(sh).filter(function(k) { return sh[k] && Object.keys(sh[k]).length > 0; });
  var lk = ks.pop(),
    sc = lk ? sh[lk] : {},
    el = document.getElementById('layers');
  if (!el) return;
  el.innerHTML = '';
  var ls = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'],
    cs = ['#10b981', '#6366f1', '#f59e0b', '#ec4899', '#8b5cf6', '#14b8a6', '#f97316', '#06b6d4', '#84cc16'],
    nm = ['Execution', 'Planning', 'Self-Direction', 'Optimizer', 'Evolution', 'Identity', 'Meta-Cog', 'Meta-Meta', 'MMM'];
  for (var i = 0; i < ls.length; i++) {
    var l = ls[i],
      v = sc[l] || 0;
    el.innerHTML += '<div class="bg-slate-900/40 rounded-lg p-2.5 sm:p-3 border border-slate-700/30" data-tt="layer:' + l + '">' +
      '<div class="flex justify-between mb-1"><span class="text-xs sm:text-sm font-bold text-slate-200">' + l +
      ' <span class="text-[10px] text-slate-400 font-normal">' + nm[i] + '</span></span>' +
      '<span class="text-xs font-mono font-bold" style="color:' + cs[i] + '">' + v.toFixed(1) + '</span></div>' +
      '<div class="h-2 bg-slate-700 rounded-full"><div class="h-full rounded-full" style="width:' + v + '%;background:' + cs[i] + '"></div></div></div>';
  }
}

// ── Goals List ────────────────────────────────────────────────

var _go = {};

function tg(i) { _go[i] = !_go[i]; var e = document.getElementById('gd' + i); if (e) { e.classList.toggle('hide'); } }

function rg() {
  var el = document.getElementById('gl');
  if (!el) return;
  el.innerHTML = '';
  for (var i = 0; i < g.length; i++) {
    var x = g[i];
    var dc = x.dec === 'PASS' ? 'text-emerald-400 bg-emerald-400/10 border-emerald-400/20' :
      x.dec === 'FAIL' ? 'text-rose-400 bg-rose-400/10 border-rose-400/20' :
      'text-amber-400 bg-amber-400/10 border-amber-400/20';
    var cv = x.conversation || [];
    var cd = document.createElement('div');
    cd.className = 'bg-slate-800/60 border border-slate-700/50 rounded-xl overflow-hidden';
    cd.innerHTML = '<div class="p-3 sm:p-4 cursor-pointer flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 hover:bg-slate-700/20" onclick="tg(' + i + ')">' +
      '<div class="flex-1"><div class="flex gap-2 flex-wrap mb-1"><span class="px-1.5 py-0.5 bg-slate-900 font-mono text-[10px] font-bold rounded text-slate-400">P' + x.p + '</span>' +
      '<span class="' + dc + ' px-2 py-0.5 text-[10px] font-semibold rounded-full border">' + x.dec + '</span>' +
      '<span class="text-[10px] text-slate-500 font-mono">' + (x.conf || '') + '</span></div>' +
      '<p class="text-xs sm:text-sm text-slate-100" style="overflow-wrap:break-word">' + x.d + '</p>' +
      '<div class="flex gap-2 mt-1 text-[10px] font-mono text-slate-500"><span>' + (x.file || '') + '</span>' +
      (x.func ? ' &middot; ' + x.func : '') + (x.type ? ' &middot; ' + x.type : '') + '</div></div>' +
      '<span class="text-xs text-slate-400 arrow">&#x25BC;</span></div>' +
      '<div class="hide border-t border-slate-700/50 p-3 sm:p-4 bg-slate-900/40 space-y-3" id="gd' + i + '">' +
      '<div class="grid grid-cols-1 md:grid-cols-2 gap-3"><div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Constraints</h4>' +
      (x.constraints ? Object.keys(x.constraints).map(function(n) {
        var t = x.constraints[n];
        var c = t === 'REQUIRED' || t === 'LOCKED' ? 'bg-amber-500/10 text-amber-400 border-amber-500/30' :
          t === 'RECOMMENDED' ? 'bg-blue-500/10 text-blue-400 border-blue-500/30' :
          'bg-slate-800 text-slate-400';
        return '<span class="px-2 py-0.5 rounded text-[10px] font-mono inline-block mr-1 mb-1 border ' + c + '">' + n + ' <span class="text-[9px] opacity-70">' + t + '</span></span>';
      }).join('') : '<span class="text-[10px] text-slate-500">None</span>') + '</div>' +
      '<div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Evaluation</h4>' +
      (x.rrp_eval ? '<div class="text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-700/40 font-mono">' + fa(x.rrp_eval) + '</div>' :
        '<span class="text-[10px] text-slate-500">No evaluation data</span>') + '</div></div>' +
      (cv.length > 0 ? '<div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Conversation</h4>' +
        cv.map(function(m) {
          return '<div class="bg-slate-800/40 p-2 rounded border border-slate-700/40 mb-1 text-xs"><span class="font-bold ' +
            (m.role === 'evaluator' ? 'text-indigo-400' : 'text-emerald-400') + '">' + m.role + ':</span> ' + fa(m.content) + '</div>';
        }).join('') + '</div>' : '') +
      '</div>';
    el.appendChild(cd);
  }
}

// ── Pulses ────────────────────────────────────────────────────

var _po = {};

function tp(i) { _po[i] = !_po[i]; var e = document.getElementById('pd' + i); if (e) { e.classList.toggle('hide'); } }

function rp() {
  var el = document.getElementById('pl');
  if (!el) return;
  el.innerHTML = '';
  for (var i = 0; i < pu.length; i++) {
    var p = pu[i];
    var pg = g.filter(function(gl) { return '' + gl.p === '' + p.id; });
    var pass = pg.filter(function(x) { return x.dec === 'PASS'; }).length;
    var fail = pg.filter(function(x) { return x.dec === 'FAIL'; }).length;
    var cd = document.createElement('div');
    cd.className = 'bg-slate-800/60 border border-slate-700/50 rounded-xl overflow-hidden';
    cd.innerHTML = '<div class="p-3 sm:p-4 cursor-pointer flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 hover:bg-slate-700/20" onclick="tp(' + i + ')">' +
      '<div class="flex-1"><div class="flex items-center gap-2 mb-1"><span class="px-2 py-0.5 bg-indigo-500/15 text-indigo-400 text-[10px] font-bold rounded-full border border-indigo-500/25">Pulse #' + p.id + '</span>' +
      '<span class="text-[10px] text-slate-400 font-mono">' + (p.type || 'standard') + '</span>' +
      '</div><div class="flex gap-3 text-xs text-slate-400">' +
      '<span>' + pg.length + ' goals</span>' +
      '<span class="text-emerald-400">' + pass + ' passed</span>' +
      (fail > 0 ? '<span class="text-rose-400">' + fail + ' failed</span>' : '') +
      (p.duration ? '<span>' + p.duration + 's</span>' : '') +
      '</div></div>' +
      '<span class="text-xs text-slate-400 arrow">&#x25BC;</span></div>' +
      '<div class="hide border-t border-slate-700/50 p-3 sm:p-4 bg-slate-900/40 space-y-3" id="pd' + i + '">' +
      '<div class="grid grid-cols-4 gap-2 text-center text-xs">' +
      '<div class="bg-slate-800/60 p-2 rounded-lg"><div class="font-bold text-lg text-indigo-400">' + pg.length + '</div><div class="text-[10px] text-slate-400">Goals</div></div>' +
      '<div class="bg-slate-800/60 p-2 rounded-lg"><div class="font-bold text-lg text-emerald-400">' + pass + '</div><div class="text-[10px] text-slate-400">Passed</div></div>' +
      '<div class="bg-slate-800/60 p-2 rounded-lg"><div class="font-bold text-lg text-rose-400">' + fail + '</div><div class="text-[10px] text-slate-400">Failed</div></div>' +
      '<div class="bg-slate-800/60 p-2 rounded-lg"><div class="font-bold text-lg text-amber-400">' + (p.duration || '?') + '</div><div class="text-[10px] text-slate-400">Duration</div></div>' +
      '</div>' +
      (p.conversation ? '<div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Pulse Conversation</h4>' +
        p.conversation.map(function(m) {
          return '<div class="bg-slate-800/40 p-2 rounded border border-slate-700/40 mb-1 text-xs"><span class="font-bold ' +
            (m.role === 'evaluator' ? 'text-indigo-400' : m.role === 'system' ? 'text-amber-400' : 'text-emerald-400') + '">' +
            (m.role || 'system') + ':</span> ' + fa(m.content || m.text || '') + '</div>';
        }).join('') + '</div>' : '') +
      (pg.length > 0 ? '<div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Goals in this Pulse</h4>' +
        pg.map(function(x) {
          var dc2 = x.dec === 'PASS' ? 'text-emerald-400' : x.dec === 'FAIL' ? 'text-rose-400' : 'text-amber-400';
          return '<div class="bg-slate-800/40 p-2 rounded border border-slate-700/40 mb-1 text-xs flex justify-between items-center">' +
            '<span>' + x.d + '</span><span class="font-bold ' + dc2 + ' ml-2">' + x.dec + '</span></div>';
        }).join('') + '</div>' : '') +
      '</div>';
    el.appendChild(cd);
  }
}

// ── Constraints ───────────────────────────────────────────────

function rc() {
  var el = document.getElementById('cbd');
  if (!el) return;
  if (!AD.summary || !AD.summary.cd) {
    el.innerHTML = '<div class="text-xs text-slate-500">No constraint data available.</div>';
    return;
  }
  var cd = AD.summary.cd;
  var names = Object.keys(cd).sort();
  el.innerHTML = names.map(function(n) {
    var c = cd[n];
    var lr = c.freq > 0 ? (c.locked / c.freq * 100) : 0;
    return '<div class="bg-slate-900/40 rounded-lg p-3 border border-slate-700/30" data-tt="constraint:' + n + '">' +
      '<div class="flex justify-between items-center mb-2">' +
      '<span class="text-xs font-bold text-slate-200">' + n.replace(/_/g, ' ') + '</span>' +
      '<span class="text-[10px] font-mono text-slate-400">' + c.freq + ' used</span></div>' +
      '<div class="flex gap-4 text-xs text-slate-400 mb-2"><span>Locked: <strong class="text-amber-400">' + c.locked + '</strong></span>' +
      '<span>Lock rate: <strong>' + lr.toFixed(0) + '%</strong></span></div>' +
      '<div class="h-1.5 bg-slate-700 rounded-full overflow-hidden">' +
      '<div class="h-full bg-gradient-to-r from-amber-500 to-rose-400 rounded-full" style="width:' + lr + '%"></div></div></div>';
  }).join('');
}

function rcb() {
  // Placeholder for additional constraint rendering
}

// ── Knowledge Graph ───────────────────────────────────────────

var _kgMode = 'force';
var _kgNodes = [];
var _kgEdges = [];

function ak(m) {
  _kgMode = m;
  bk();
}

function bk() {
  var canvas = document.getElementById('kgC');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var W = canvas.parentElement.clientWidth || 700;
  var H = 500;
  canvas.width = W;
  canvas.height = H;
  ctx.clearRect(0, 0, W, H);

  // Build KG data from AD
  _kgNodes = [];
  _kgEdges = [];
  if (AD && AD.goals) {
    AD.goals.forEach(function(g, i) {
      _kgNodes.push({ id: 'g' + i, label: (g.d || '').substring(0, 30), type: 'goal', x: 0, y: 0 });
    });
  }
  if (AD && AD.pulses) {
    AD.pulses.forEach(function(p, i) {
      _kgNodes.push({ id: 'p' + i, label: 'Pulse #' + p.id, type: 'pulse', x: 0, y: 0 });
    });
  }

  if (_kgNodes.length === 0) {
    ctx.fillStyle = '#64748b';
    ctx.font = '14px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('No knowledge graph data available', W / 2, H / 2);
    return;
  }

  if (_kgMode === 'force') drawForceGraph(ctx, W, H);
  else if (_kgMode === 'radial') drawRadialGraph(ctx, W, H);
  else if (_kgMode === 'grid') drawGridGraph(ctx, W, H);
}

function drawForceGraph(ctx, W, H) {
  // Simple force layout
  var nodes = _kgNodes.map(function(n, i) {
    return { x: W * 0.1 + Math.random() * W * 0.8, y: H * 0.1 + Math.random() * H * 0.8, id: n.id, label: n.label, type: n.type };
  });

  // Run simple force simulation (few iterations for performance)
  for (var iter = 0; iter < 50; iter++) {
    for (var i = 0; i < nodes.length; i++) {
      for (var j = i + 1; j < nodes.length; j++) {
        var dx = nodes[j].x - nodes[i].x;
        var dy = nodes[j].y - nodes[i].y;
        var dist = Math.sqrt(dx * dx + dy * dy) || 1;
        var force = 1000 / (dist * dist);
        var fx = force * (dx / dist);
        var fy = force * (dy / dist);
        nodes[j].x += fx;
        nodes[j].y += fy;
        nodes[i].x -= fx;
        nodes[i].y -= fy;
      }
    }
    // Center gravity
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].x += (W / 2 - nodes[i].x) * 0.01;
      nodes[i].y += (H / 2 - nodes[i].y) * 0.01;
    }
  }

  // Draw edges (dummy edges between goals and pulses)
  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 0.5;
  var gCount = (AD.goals || []).length;
  for (var i = 0; i < nodes.length; i++) {
    for (var j = i + 1; j < nodes.length; j++) {
      if (nodes[i].type !== nodes[j].type) {
        ctx.beginPath();
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(nodes[j].x, nodes[j].y);
        ctx.stroke();
      }
    }
  }

  // Draw nodes
  nodes.forEach(function(n) {
    ctx.beginPath();
    var color = n.type === 'goal' ? '#6366f1' : n.type === 'pulse' ? '#10b981' : '#f59e0b';
    var radius = n.type === 'goal' ? 6 : 8;
    ctx.fillStyle = color + '40';
    ctx.strokeStyle = color;
    ctx.lineWidth = 1.5;
    ctx.arc(n.x, n.y, radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    if (n.label) {
      ctx.fillStyle = '#94a3b8';
      ctx.font = '8px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(n.label, n.x, n.y + radius + 10);
    }
  });
}

function drawRadialGraph(ctx, W, H) {
  var cx = W / 2,
    cy = H / 2;
  var nodes = _kgNodes;
  var radius = Math.min(W, H) * 0.35;

  // Sort: goals inner, pulses outer
  var goals = nodes.filter(function(n) { return n.type === 'goal'; });
  var pulses = nodes.filter(function(n) { return n.type === 'pulse'; });

  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 0.5;

  [goals, pulses].forEach(function(group, gi) {
    var r = radius * (gi === 0 ? 0.5 : 1);
    group.forEach(function(n, i) {
      var angle = (i / group.length) * Math.PI * 2 - Math.PI / 2;
      n.x = cx + r * Math.cos(angle);
      n.y = cy + r * Math.sin(angle);

      // Draw edge to center
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(n.x, n.y);
      ctx.stroke();
    });
  });

  // Draw center
  ctx.beginPath();
  ctx.fillStyle = '#6366f140';
  ctx.strokeStyle = '#6366f1';
  ctx.lineWidth = 2;
  ctx.arc(cx, cy, 10, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();
  ctx.fillStyle = '#6366f1';
  ctx.font = '10px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('RSIS', cx, cy + 3);

  // Draw nodes
  nodes.forEach(function(n) {
    if (!n.x) return;
    ctx.beginPath();
    var color = n.type === 'goal' ? '#6366f1' : '#10b981';
    var rad = n.type === 'goal' ? 5 : 7;
    ctx.fillStyle = color + '40';
    ctx.strokeStyle = color;
    ctx.lineWidth = 1.5;
    ctx.arc(n.x, n.y, rad, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    if (n.label) {
      ctx.fillStyle = '#94a3b8';
      ctx.font = '7px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(n.label, n.x, n.y + rad + 8);
    }
  });
}

function drawGridGraph(ctx, W, H) {
  var nodes = _kgNodes;
  var cols = Math.ceil(Math.sqrt(nodes.length));
  var cellW = W / cols;
  var cellH = H / Math.ceil(nodes.length / cols);

  nodes.forEach(function(n, i) {
    var col = i % cols;
    var row = Math.floor(i / cols);
    n.x = col * cellW + cellW / 2;
    n.y = row * cellH + cellH / 2;
  });

  // Draw grid connections
  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 0.5;
  for (var i = 0; i < nodes.length; i++) {
    if (i + 1 < nodes.length) {
      ctx.beginPath();
      ctx.moveTo(nodes[i].x, nodes[i].y);
      ctx.lineTo(nodes[i + 1].x, nodes[i + 1].y);
      ctx.stroke();
    }
    if (i + cols < nodes.length) {
      ctx.beginPath();
      ctx.moveTo(nodes[i].x, nodes[i].y);
      ctx.lineTo(nodes[i + cols].x, nodes[i + cols].y);
      ctx.stroke();
    }
  }

  nodes.forEach(function(n) {
    ctx.beginPath();
    var color = n.type === 'goal' ? '#6366f1' : '#10b981';
    ctx.fillStyle = color + '40';
    ctx.strokeStyle = color;
    ctx.lineWidth = 1.5;
    ctx.arc(n.x, n.y, 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    if (n.label) {
      ctx.fillStyle = '#94a3b8';
      ctx.font = '7px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(n.label, n.x, n.y + 10);
    }
  });
}
function pf(){
  var el=document.getElementById("cpf");if(!el)return;
  var seen={};for(var i=0;i<g.length;i++){var c=g[i].conversation||[];if(c.length>0)seen[""+g[i].p]=true;}
  Object.keys(seen).sort(function(a,b){return parseInt(a)-parseInt(b);}).forEach(function(p){var o=document.createElement("option");o.value=p;o.textContent="Pulse #"+p;el.appendChild(o);});
}

// ── Pulse Filter ──────────────────────────────────────────────


// ── Charts ────────────────────────────────────────────────────

function ic() {
  if (typeof Chart === 'undefined') {
    document.querySelectorAll('#b-graphs canvas').forEach(function(c) {
      c.parentElement.innerHTML +=
        '<div class="text-xs text-rose-400">Chart.js not loaded. Check CDN.</div>';
    });
    return;
  }

  // Pie: Decision Distribution (c1)
  var decCounts = { PASS: 0, FAIL: 0, HOLD: 0 };
  g.forEach(function(x) { if (decCounts[x.dec] !== undefined) decCounts[x.dec]++; });
  new Chart(document.getElementById('c1'), {
    type: 'pie',
    data: {
      labels: Object.keys(decCounts),
      datasets: [{ data: Object.values(decCounts), backgroundColor: ['#10b981', '#f43f5e', '#f59e0b'] }]
    },
    options: { responsive: true, plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 10 } } } } }
  });

  // Pie: Goal Type Distribution (c11)
  var typeCounts = {};
  g.forEach(function(x) { var t = x.type || 'unknown'; typeCounts[t] = (typeCounts[t] || 0) + 1; });
  var typeColors = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6', '#14b8a6'];
  new Chart(document.getElementById('c11'), {
    type: 'pie',
    data: {
      labels: Object.keys(typeCounts),
      datasets: [{ data: Object.values(typeCounts), backgroundColor: typeColors.slice(0, Object.keys(typeCounts).length) }]
    },
    options: { responsive: true, plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 10 } } } } }
  });

  // Pie: Constraint Lock State (c12)
  var lockState = { locked: 0, optional: 0 };
  g.forEach(function(x) {
    if (x.constraints) {
      Object.keys(x.constraints).forEach(function(k) {
        if (x.constraints[k] === 'REQUIRED' || x.constraints[k] === 'LOCKED') lockState.locked++;
        else lockState.optional++;
      });
    }
  });
  new Chart(document.getElementById('c12'), {
    type: 'pie',
    data: {
      labels: ['Locked', 'Optional'],
      datasets: [{ data: [lockState.locked, lockState.optional], backgroundColor: ['#f59e0b', '#64748b'] }]
    },
    options: { responsive: true, plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 10 } } } } }
  });

  // Pie: Pulse Type Distribution (c13)
  var pulseTypes = {};
  pu.forEach(function(p) { var t = p.type || 'standard'; pulseTypes[t] = (pulseTypes[t] || 0) + 1; });
  var pulseTypeColors = ['#10b981', '#6366f1', '#f59e0b', '#ec4899', '#8b5cf6'];
  new Chart(document.getElementById('c13'), {
    type: 'pie',
    data: {
      labels: Object.keys(pulseTypes),
      datasets: [{ data: Object.values(pulseTypes), backgroundColor: pulseTypeColors.slice(0, Object.keys(pulseTypes).length) }]
    },
    options: { responsive: true, plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 10 } } } } }
  });

  // Bar/Line: Success Rate (c2)
  new Chart(document.getElementById('c2'), {
    type: 'line',
    data: {
      labels: pu.map(function(p) { return '#' + p.id; }),
      datasets: [{
        label: 'Success Rate',
        data: pu.map(function(p) {
          var pg2 = g.filter(function(gl) { return '' + gl.p === '' + p.id; });
          return pg2.length > 0 ? pg2.filter(function(x) { return x.dec === 'PASS'; }).length / pg2.length * 100 : 0;
        }),
        borderColor: '#10b981',
        backgroundColor: '#10b98120',
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 10 } } } },
      scales: { x: { ticks: { color: '#64748b', font: { size: 9 } } }, y: { min: 0, max: 100, ticks: { color: '#64748b', font: { size: 9 } } } }
    }
  });

  // Bar: Duration (c3)
  new Chart(document.getElementById('c3'), {
    type: 'bar',
    data: {
      labels: pu.map(function(p) { return '#' + p.id; }),
      datasets: [{
        label: 'Duration (s)',
        data: pu.map(function(p) { return p.duration || 0; }),
        backgroundColor: '#6366f160',
        borderColor: '#6366f1',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 10 } } } },
      scales: { x: { ticks: { color: '#64748b', font: { size: 9 } } }, y: { ticks: { color: '#64748b', font: { size: 9 } } } }
    }
  });

  // Line: Confidence (c4)
  new Chart(document.getElementById('c4'), {
    type: 'line',
    data: {
      labels: pu.map(function(p) { return '#' + p.id; }),
      datasets: [{
        label: 'Avg Confidence',
        data: pu.map(function(p) { return p.avg_confidence || 0; }),
        borderColor: '#f59e0b',
        backgroundColor: '#f59e0b20',
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 10 } } } },
      scales: { x: { ticks: { color: '#64748b', font: { size: 9 } } }, y: { min: 0, max: 1, ticks: { color: '#64748b', font: { size: 9 } } } }
    }
  });

  // Multi-line: Layer Scores (c5)
  var ls5 = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'];
  var lColors = ['#10b981', '#6366f1', '#f59e0b', '#ec4899', '#8b5cf6', '#14b8a6', '#f97316', '#06b6d4', '#84cc16'];
  var shKeys = Object.keys(sh).sort();
  new Chart(document.getElementById('c5'), {
    type: 'line',
    data: {
      labels: shKeys.map(function(k) { return k.substring(0, 5); }),
      datasets: ls5.map(function(l, i) {
        return {
          label: l,
          data: shKeys.map(function(k) { return (sh[k] && sh[k][l]) || 0; }),
          borderColor: lColors[i],
          backgroundColor: lColors[i] + '20',
          fill: false,
          tension: 0.3,
          pointRadius: 2
        };
      })
    },
    options: {
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 9 } } } },
      scales: {
        x: { ticks: { color: '#64748b', font: { size: 8 } } },
        y: { min: 0, max: 100, ticks: { color: '#64748b', font: { size: 8 } } }
      }
    }
  });

  // Stacked Bar: Goals Per Pulse (c6)
  new Chart(document.getElementById('c6'), {
    type: 'bar',
    data: {
      labels: pu.map(function(p) { return '#' + p.id; }),
      datasets: [{
        label: 'Goals',
        data: pu.map(function(p) { return g.filter(function(gl) { return '' + gl.p === '' + p.id; }).length; }),
        backgroundColor: '#6366f160',
        borderColor: '#6366f1',
        borderWidth: 1
      }, {
        label: 'Approved',
        data: pu.map(function(p) { return p.approved || 0; }),
        backgroundColor: '#10b98160',
        borderColor: '#10b981',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 9 } } } },
      scales: { x: { stacked: true, ticks: { color: '#64748b', font: { size: 9 } } }, y: { stacked: true, ticks: { color: '#64748b', font: { size: 9 } } } }
    }
  });

  // Horizontal Bar: Constraints (c7)
  var cd = (AD.summary && AD.summary.cd) ? AD.summary.cd : {};
  var cNames = Object.keys(cd);
  new Chart(document.getElementById('c7'), {
    type: 'bar',
    data: {
      labels: cNames,
      datasets: [{
        label: 'Frequency',
        data: cNames.map(function(n) { return cd[n].freq; }),
        backgroundColor: '#f59e0b60',
        borderColor: '#f59e0b',
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 9 } } } },
      scales: { x: { ticks: { color: '#64748b', font: { size: 9 } } }, y: { ticks: { color: '#64748b', font: { size: 8 } } } }
    }
  });

  // Radar: Layer Scores (c8)
  var lastSH = shKeys.length > 0 ? sh[shKeys[shKeys.length - 1]] : {};
  new Chart(document.getElementById('c8'), {
    type: 'radar',
    data: {
      labels: ls5,
      datasets: [{
        label: 'Current',
        data: ls5.map(function(l) { return lastSH[l] || 0; }),
        backgroundColor: '#6366f140',
        borderColor: '#6366f1',
        pointBackgroundColor: '#6366f1'
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 9 } } } },
      scales: { r: { min: 0, max: 100, ticks: { color: '#64748b', font: { size: 8 }, backdropColor: 'transparent' }, grid: { color: '#334155' } } }
    }
  });

  // Constraint Distribution (c9)
  new Chart(document.getElementById('c9'), {
    type: 'pie',
    data: {
      labels: cNames,
      datasets: [{ data: cNames.map(function(n) { return cd[n].freq; }), backgroundColor: ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6', '#14b8a6', '#f97316', '#06b6d4', '#84cc16', '#f43f5e'] }]
    },
    options: { responsive: true, plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 8 } } } } }
  });

  // Lock Rate (c10)
  new Chart(document.getElementById('c10'), {
    type: 'bar',
    data: {
      labels: cNames,
      datasets: [{
        label: 'Lock Rate %',
        data: cNames.map(function(n) { return cd[n].freq > 0 ? (cd[n].locked / cd[n].freq * 100) : 0; }),
        backgroundColor: '#f43f5e60',
        borderColor: '#f43f5e',
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: { legend: { labels: { color: '#94a3b8', font: { size: 9 } } } },
      scales: { x: { min: 0, max: 100, ticks: { color: '#64748b', font: { size: 9 } } }, y: { ticks: { color: '#64748b', font: { size: 8 } } } }
    }
  });
}

// ── Tooltips ──────────────────────────────────────────────────

var _tt = document.createElement('div');
_tt.className = 'tooltip';
_tt.style.display = 'none';
document.body.appendChild(_tt);

var _ttTimeout = null;

document.addEventListener('mouseover', function(e) {
  var el = e.target.closest('[data-tt]');
  if (!el) { hideTooltip(); return; }
  var key = el.getAttribute('data-tt');
  showTooltip(e, key);
});

document.addEventListener('mouseout', function(e) {
  var el = e.target.closest('[data-tt]');
  if (!el) return;
  hideTooltip();
});

document.addEventListener('mousemove', function(e) {
  if (_tt.style.display !== 'none') {
    _tt.style.left = Math.min(e.pageX + 15, window.innerWidth - 330) + 'px';
    _tt.style.top = Math.min(e.pageY + 15, window.innerHeight - 200) + 'px';
  }
});

function showTooltip(e, key) {
  if (!key) return;
  var html = getTooltipContent(key);
  if (!html) return;
  _tt.innerHTML = html;
  _tt.style.display = 'block';
  _tt.className = 'tooltip show';
  _tt.style.left = Math.min(e.pageX + 15, window.innerWidth - 330) + 'px';
  _tt.style.top = Math.min(e.pageY + 15, window.innerHeight - 200) + 'px';
  clearTimeout(_ttTimeout);
}

function hideTooltip() {
  _ttTimeout = setTimeout(function() {
    _tt.style.display = 'none';
    _tt.className = 'tooltip';
  }, 100);
}

function getTooltipContent(key) {
  // Tab tooltips
  if (key.indexOf('tab:') === 0) return getTabInfo(key.substring(4));

  // Graph tooltips
  if (key.indexOf('graph:') === 0) return getGraphInfo(key.substring(6));

  // Summary tooltips
  if (key.indexOf('summary:') === 0) return getSummaryInfo(key.substring(8));

  // Layer tooltips
  if (key.indexOf('layer:') === 0) return getLayerInfo(key.substring(6));

  // Pulse stat tooltips
  if (key.indexOf('pulsestat:') === 0) {
    var parts = key.substring(10).split(':');
    return getPulseStatTooltip(parseInt(parts[0]) || 0, parts[1] || '');
  }

  // Constraint tooltips
  if (key.indexOf('constraint:') === 0) return getConstraintInfo(key.substring(11));

  return '<h4>Info</h4><p>RSIS Telemetry Dashboard.</p>';
}

function getSummaryInfo(name) {
  var info = {
    pass: {
      h: 'Passed Goals',
      d: 'Total number of goals that passed RRP evaluation and were approved for implementation.',
      m: { 'Total Goals': AD ? (AD.goals || []).length : 0, 'Pass Rate': '100%' }
    },
    fail: {
      h: 'Failed Goals',
      d: 'Total number of goals that failed RRP evaluation and were rejected.',
      m: { 'Failed Goals': 0 }
    },
    hold: {
      h: 'Held Goals',
      d: 'Total number of goals held for further review or pending additional information.',
      m: { 'Held Goals': 0 }
    },
    tot: {
      h: 'Total Goals',
      d: 'Total number of improvement goals generated across all pulses.',
      m: { 'Total Goals': AD ? (AD.goals || []).length : 0 }
    },
    pulse_count: {
      h: 'Pulse Count',
      d: 'Total number of execution pulses completed. Each pulse represents one improvement cycle.',
      m: { 'Total Pulses': AD ? (AD.pulses || []).length : 0 }
    }
  };
  var i = info[name];
  if (!i) return '<h4>Summary</h4><p>Dashboard summary stat.</p>';
  return '<h4>' + i.h + '</h4><p>' + i.d + '</p>' +
    '<div class="tt-section"><table>' + Object.keys(i.m).map(function(k) {
      return '<tr><td>' + k + '</td><td class="text-right font-bold">' + i.m[k] + '</td></tr>';
    }).join('') + '</table></div>';
}

function getLayerInfo(layer) {
  var info = {
    L1: { n: 'Execution Loop', d: 'Pure execution — runs commands, git apply, test verification.', ts: 'Seconds', m: ['execution_reliability', 'failure_recovery', 'pipeline_activity', 'crisis_immunity'] },
    L2: { n: 'Planning & Improvement', d: 'Goal analysis, step planning, codegen, evaluation, application, verification.', ts: 'Minutes', m: ['goal_analysis', 'step_planning', 'apply_success_rate', 'iteration_efficiency', 'pipeline_throughput'] },
    L3: { n: 'Self-Direction', d: 'Signal detection, goal generation, task assignment.', ts: '5-15 min', m: ['signal_coverage', 'goal_generation', 'goal_execution', 'goal_diversity', 'queue_health'] },
    L4: { n: 'Optimizer', d: 'A/B testing, parameter tuning, experimentation.', ts: '0.5-1 hr', m: ['parameter_tuning', 'experimentation', 'kg_utilization', 'optimization_depth', 'learning_maturity'] },
    L5: { n: 'Evolution', d: 'Cross-session consolidation, pattern detection, strategy evolution.', ts: '2-3 hr', m: ['pattern_detection', 'strategy_evolution', 'insight_utilization', 'redundancy_detection', 'kg_growth'] },
    L6: { n: 'Identity & Values', d: 'Self-model, value reinforcement, capability tracking.', ts: '4-6 hr', m: ['value_definition', 'value_adherence', 'value_reinforcement', 'identity_stability', 'self_knowledge'] },
    L7: { n: 'Meta-Cognition', d: 'Reflects on the improvement process itself, generates super-goals.', ts: 'Daily', m: ['meta_reflection_depth', 'self_critique_quality', 'improvement_meta_awareness'] },
    L8: { n: 'Meta-Meta', d: 'Reflects on meta-cognition quality, second-order awareness.', ts: 'Daily', m: ['reflection_on_reflection', 'recursive_insight_depth', 'meta_meta_awareness'] },
    L9: { n: 'MMM', d: 'Third-order recursive self-awareness, self-transcendence.', ts: 'Daily', m: ['meta_mmm_coherence', 'recursive_synthesis_quality', 'self_transcendence'] }
  };
  var i = info[layer];
  if (!i) return '<h4>' + layer + '</h4><p>Layer score.</p>';
  return '<h4>' + layer + ' - ' + i.n + '</h4><p>' + i.d + '</p>' +
    '<div class="tt-section"><div class="tt-metric"><span class="tt-label">Timescale</span><span class="tt-val">' + i.ts + '</span></div></div>' +
    '<div class="tt-section"><table><tr><th>Metric</th></tr>' + i.m.map(function(mm) {
      return '<tr><td>' + mm.replace(/_/g, ' ') + '</td></tr>';
    }).join('') + '</table></div>';
}

function getPulseStatTooltip(idx, name) {
  if (idx < 0 || idx >= pu.length) return '<h4>Stat</h4><p>Unknown.</p>';
  var p = pu[idx];
  var descs = {
    approved: 'Goals that passed RRP evaluation and were approved for implementation in this pulse.',
    goals: 'Total improvement goals generated and processed in this pulse.',
    impl: 'Improvements successfully implemented (code generated, applied, verified).',
    conf: 'Average RRP evaluator confidence score across all goals in this pulse. Higher = clearer goals.'
  };
  var vals = {
    approved: p.approved || 0,
    goals: (g.filter(function(gl) { return '' + gl.p === '' + p.id; })).length,
    impl: p.implementation_count || 0,
    conf: p.avg_confidence !== undefined ? (p.avg_confidence * 100).toFixed(0) + '%' : 'N/A'
  };
  return '<h4>' + name.charAt(0).toUpperCase() + name.slice(1) + '</h4><p>' + (descs[name] || 'Pulse metric.') + '</p>' +
    '<div class="tt-metric"><span class="tt-label">Value</span><span class="tt-val">' + (vals[name] || '?') + '</span></div>';
}

function getConstraintInfo(name) {
  var info = {
    error_handling: { d: 'Ensures errors are caught with try/except, logged with context, and handled with graceful fallbacks.', i: 'Critical for production reliability.' },
    type_safety: { d: 'Requires type annotations on function signatures and runtime validation.', i: 'Prevents type-related runtime errors.' },
    test_coverage: { d: 'New/modified code must have corresponding tests.', i: 'Essential for regression prevention.' },
    logging: { d: 'Appropriate logging for debugging and monitoring.', i: 'Required for operational visibility.' },
    documentation: { d: 'Docstrings and docs for new/modified APIs.', i: 'Critical for maintainability.' },
    security: { d: 'Security best practices — input validation, auth, safe deserialization.', i: 'Prevents vulnerabilities.' },
    input_validation: { d: 'Validate all external inputs before processing.', i: 'Defense against malformed data and injection.' },
    code_quality: { d: 'DRY, single responsibility, clear naming.', i: 'Reduces technical debt.' },
    maintainability: { d: 'Modular code with clear interfaces.', i: 'Essential for sustainable development.' },
    performance: { d: 'Algorithm choice, caching, async, resource management.', i: 'Prevents performance regressions.' }
  };
  var ci = info[name];
  if (!ci) return '<h4>' + name.replace(/_/g, ' ').replace(/\b\w/g, function(l) { return l.toUpperCase(); }) + '</h4><p>RRP constraint.</p>';
  var cd = (AD.summary && AD.summary.cd) ? AD.summary.cd[name] : null;
  return '<h4>' + name.replace(/_/g, ' ').replace(/\b\w/g, function(l) { return l.toUpperCase(); }) + '</h4>' +
    '<p><strong>Definition:</strong> ' + ci.d + '</p>' +
    '<p><strong>Importance:</strong> ' + ci.i + '</p>' +
    (cd ? '<table><tr><th>Freq</th><th>Locked</th><th>Lock Rate</th></tr><tr><td>' + cd.freq + '</td><td>' + cd.locked + '</td><td>' + (cd.freq > 0 ? (cd.locked / cd.freq * 100).toFixed(0) : '0') + '%</td></tr></table>' : '');
}

function getGraphInfo(name) {
  var d = {
    'c1': 'Pie chart showing the distribution of PASS/FAIL/HOLD decisions across all evaluated goals.',
    'c11': 'Distribution of goal types (implementation, refactor, test, documentation, etc).',
    'c12': 'Shows how many constraints are locked (required) vs optional across all goals.',
    'c13': 'Distribution of pulse types (standard, optimization, evolution, etc).',
    'c2': 'Line chart tracking the success rate trend per pulse. Helps identify performance regressions.',
    'c3': 'Bar chart showing execution duration per pulse. Longer durations may indicate complexity.',
    'c4': 'Line chart showing evaluator confidence trend over pulses. Higher = clearer goals.',
    'c5': 'Multi-line chart showing all 9 layer capability scores over time.',
    'c6': 'Stacked bar chart comparing total goals vs approved goals per pulse.',
    'c7': 'Horizontal bar chart showing constraint frequency by type.',
    'c8': 'Radar chart providing a holistic view of all layer scores at the latest snapshot.',
    'c9': 'Pie chart showing the distribution of constraint types across all goals.',
    'c10': 'Horizontal bar chart showing the lock rate percentage for each constraint type.'
  };
  return '<h4>Chart ' + name.toUpperCase() + '</h4><p>' + (d[name] || 'Telemetry chart.') + '</p>' +
    '<div class="tt-section"><p class="text-[10px] text-slate-500">Hover over data points for detailed values.</p></div>';
}

function getTabInfo(name) {
  var d = {
    overview: 'Summary statistics, overall success rate, and per-layer capability scores.',
    pulses: 'Individual pulse details with expandable cards showing goals, evaluation data, and conversations.',
    kg: 'Interactive knowledge graph visualization with force-directed, radial, and grid layout modes.',
    graphs: 'Full chart suite including decision distributions, trends, durations, confidence scores, and constraint analysis.',
    constraints: 'Constraint frequency and lock rate analysis with detailed per-type breakdowns.'
  };
  return '<h4>' + name.charAt(0).toUpperCase() + name.slice(1) + ' Tab</h4><p>' + (d[name] || 'Dashboard tab.') + '</p>';
}

// ── Initialize ────────────────────────────────────────────────

loadData();
