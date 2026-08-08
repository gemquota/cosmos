
var AD, PD, g, pu, sh, ch = {};

function loadData() {
  var url = (typeof DATA_DIR !== 'undefined' ? DATA_DIR : '') + (typeof DATA_FILE !== 'undefined' ? DATA_FILE : 'dashboard-data.json');
  // Also try without leading ./ if needed
  fetch(url)
    .then(function(r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function(d) {
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
      document.getElementById('load').innerHTML = '<div class="text-red-400 text-center mt-10">Error loading data: ' + e.message + '<br><br><button onclick="location.reload()" style="background:#6366f1;color:white;border:none;padding:8px 20px;border-radius:8px;cursor:pointer;font-size:14px">Retry</button></div>';
    });
}

function esc(s){
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function up(){
  var sm = (AD && AD.summary) || {};
  var set = function(id, v){ var el = document.getElementById(id); if (el) el.textContent = v; };
  set('s-pass', sm.pass || 0);
  set('s-fail', sm.fail || 0);
  set('s-hold', sm.hold || 0);
  set('s-tot', sm.tot || 0);
  set('s-pulses', sm.pulse_count || (pu ? pu.length : 0));
  var tot = sm.tot || 0, pass = sm.pass || 0;
  var rate = tot > 0 ? (pass / tot * 100) : 0;
  set('srate-txt', pass + '/' + tot + ' (' + rate.toFixed(1) + '%)');
  var bar = document.getElementById('srate-bar');
  if (bar) bar.style.width = rate.toFixed(1) + '%';
  set('hdr-stats', (sm.pulse_count || pu.length) + ' pulses · ' + tot + ' goals · ' + (sm.impl_count || 0) + ' improvements');
}

function loadLiveEcosystem(){
  // Client-side live counts from the public GitHub API (public repo). The
  // committed ecosystem.json values stay as the instant fallback; when the
  // tree loads, counts are refreshed and the footer marks the data LIVE.
  // Cached per session (10 min) to respect unauthenticated API limits.
  var KEY = 'cosmos-live-tree';
  var cached = null;
  try { cached = JSON.parse(sessionStorage.getItem(KEY) || 'null'); } catch (e) {}
  var apply = function(tree){
    if (!tree || !tree.tree) return;
    var visible = function(pth){ return !pth.split('/').some(function(s){ return s.indexOf('.') === 0; }); };
    var count = function(prefix, mdOnly){
      return tree.tree.filter(function(n){
        return n.type === 'blob' && n.path.indexOf(prefix) === 0 && visible(n.path) &&
               (!mdOnly || n.path.slice(-3) === '.md');
      }).length;
    };
    var set = function(id, v){ var el = document.getElementById(id); if (el) el.textContent = v; };
    set('ec-mykb', count('components/mykb/', true));
    set('ec-space', count('components/space/', false));
    set('ec-rsis3', count('components/rsis3/', false));
    var f = document.getElementById('dash-footer');
    if (f) f.textContent = '\u25cf LIVE \u2014 counts from GitHub (main); snapshot generated ' +
      ((AD && AD.generated) || 'unknown') + ' \u00b7 run `cosmos` locally for full live data';
  };
  if (cached && Date.now() - cached.at < 10 * 60 * 1000) { apply(cached.tree); return; }
  fetch('https://api.github.com/repos/gemquota/cosmos/git/trees/main?recursive=1')
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(tree){
      if (!tree) return;
      try { sessionStorage.setItem(KEY, JSON.stringify({at: Date.now(), tree: tree})); } catch (e) {}
      apply(tree);
    })
    .catch(function(){});
}

function loadEcosystem(){
  fetch('ecosystem.json')
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(e){
      if (!e) return;
      var set = function(id, v){ var el = document.getElementById(id); if (el) el.textContent = v; };
      var c = e.components || {};
      set('ec-mykb', (c.mykb && c.mykb.md) ? c.mykb.md : '?');
      set('ec-space', c.space ? c.space.files : '?');
      set('ec-rsis3', c.rsis3 ? c.rsis3.files : '?');
      var f = document.getElementById('dash-footer');
      if (f) f.textContent = 'Static snapshot · generated ' + (e.generated || 'unknown') + ' · counts from tracked repo files · run `cosmos` locally for live data';
    })
    .catch(function(){});
}


var LOOPS_META = {
  L0:['L0','Substrate','#64748b'],L1:['L1','Execution','#10b981'],L2:['L2','Improvement','#6366f1'],
  L3:['L3','Evolution','#f59e0b'],L4:['L4','Optimizer','#ec4899'],L5:['L5','Evolution','#8b5cf6'],
  L6:['L6','Identity','#14b8a6'],L7:['L7','Meta-Cog','#f97316'],L8:['L8','Meta-Meta','#06b6d4'],
  L9:['L9','MMM','#84cc16']
};
function loadLoops(){
  fetch('loops.json')
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(d){ if (d) renderLoops(d); })
    .catch(function(){});
}
function renderLoops(d){
  var grid = document.getElementById('loops-grid');
  if (!grid) return;
  var meta = document.getElementById('loops-meta');
  if (meta) meta.textContent = 'static snapshot · ' + (d.generated || 'unknown') + ' · RECENT = ran within 24h';
  var html = '';
  for (var i = 0; i < d.loops.length; i++) {
    var l = d.loops[i], meta = LOOPS_META[l.id] || [l.id, l.name, '#64748b'];
    var color = meta[2];
    // "implemented" means the loop exists in code — it is not proof it is
    // running (the loops run on demand; nothing is continuously active).
    // Liveness comes from the snapshot's runtime field (or, for older
    // snapshots, from runs + last_run recency).
    var runtime = l.runtime || (l.status === 'n/a' ? 'n/a' : (l.runs > 0 ? 'idle' : 'never'));
    var status;
    if (runtime === 'recent') {
      status = '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/15 text-emerald-400 border border-emerald-500/25">RECENT</span>';
    } else if (runtime === 'idle') {
      status = '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/15 text-amber-400 border border-amber-500/25">IDLE</span>';
    } else if (runtime === 'never') {
      status = '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-600/20 text-slate-400 border border-slate-500/30">NOT RUN</span>';
    } else {
      status = '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-600/20 text-slate-400 border border-slate-500/30">' + esc(runtime.toUpperCase()) + '</span>';
    }
    var params = (l.params || []).map(function(p){
      return '<div class="flex justify-between text-[11px]"><span class="font-mono text-slate-400">'+esc(p.key)+'</span><span class="font-mono font-semibold" style="color:'+color+'">'+esc(p.value)+'</span></div>';
    }).join('') || '<div class="text-[11px] text-slate-500">—</div>';
    var signal = l.last_signal ? esc(l.last_signal) : '—';
    var last = l.last_run ? String(l.last_run).substring(0,16).replace('T',' ') : 'never';
    var metaLine = 'runs ' + (l.runs||0) + ' · cycle ' + (l.cycle||0) + ' · signal ' + signal;
    html += '<div class="bg-slate-900/40 rounded-xl p-3 border border-slate-700/30">' +
      '<div class="flex items-center justify-between mb-1.5">' +
        '<div class="flex items-center gap-2"><span class="text-xs sm:text-sm font-bold font-mono" style="color:'+color+'">'+meta[0]+'</span>' +
        '<span class="text-xs font-bold text-slate-200">'+esc(meta[1])+'</span></div>' + status +
      '</div>' +
      '<p class="text-[10px] text-slate-400 mb-2">'+esc(l.target)+'</p>' +
      '<div class="space-y-0.5 mb-2">'+params+'</div>' +
      '<div class="flex justify-between text-[10px] text-slate-500 border-t border-slate-700/30 pt-1.5">' +
        '<span>'+metaLine+'</span><span>last '+last+'</span>' +
      '</div></div>';
  }
  grid.innerHTML = html;
}

function renderAll(){renderDrives();ly();rg();rp();rc();rcb();bk();pf();sw('overview');}

// Active multitiered goal stack (Output > Communicate > Wrap > Bridge)
function renderDrives(){
  var url = (typeof GOALS_FILE !== 'undefined' ? GOALS_FILE : '../rack/goals_stack.json');
  fetch(url).then(function(r){ return r.ok ? r.json() : null; }).then(function(g){
    if (!g || !g.tiers || !g.tiers.length) return;
    var el = document.getElementById('drives');
    if (!el) return;
    el.innerHTML =
      '<div class="bg-slate-800/60 border border-slate-700/50 rounded-xl p-3 sm:p-4 mb-4">' +
      '<div class="flex items-center justify-between gap-2 mb-2">' +
      '<div class="text-xs sm:text-sm font-semibold text-slate-300">🧭 Active Drives</div>' +
      '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-indigo-500/15 text-indigo-400 border border-indigo-500/25 uppercase">' + esc(g.status || 'active') + '</span>' +
      '</div>' +
      '<p class="text-[11px] text-slate-400 mb-2">' + esc(g.title || '') + '</p>' +
      '<div class="flex flex-wrap gap-1.5">' +
      g.tiers.map(function(t){
        return '<span class="text-[10px] sm:text-[11px] px-2 py-1 rounded-lg bg-slate-700/40 text-slate-300 border border-slate-600/40" title="' + esc(t.goal || '') + '">T' + t.tier + ' ' + esc(t.name) + '</span>';
      }).join('') +
      '</div></div>';
  }).catch(function(){});
}

var _chartsInited = false;
function sw(n){
  if(n==='graphs' && !_chartsInited){
    _chartsInited = true;
    requestAnimationFrame(function(){
      requestAnimationFrame(function(){ ic(); });
    });
  }
  document.querySelectorAll('.tb').forEach(function(t){
    t.classList.remove('bg-indigo-500','text-white','shadow');
    t.classList.add('text-slate-400','hover:text-slate-200','hover:bg-slate-700/40');
  });
  document.querySelectorAll('.tb[data-t="'+n+'"]').forEach(function(t){
    t.classList.add('bg-indigo-500','text-white','shadow');
  });
  document.querySelectorAll('.tab-body').forEach(function(b){b.classList.add('hide');});
  var el=document.getElementById('b-'+n);
  if(el)el.classList.remove('hide');
}

function fa(a){
  if(!a&&a!==0)return'';
  if(typeof a==='string')return esc(a);
  if(typeof a==='object'){try{return esc(JSON.stringify(a));}catch(e){return esc(String(a));}}
  return esc(String(a));
}

function ly(){
  var ks=Object.keys(sh).filter(function(k){return sh[k]&&Object.keys(sh[k]).length>0;});
  var lk=ks.pop(),sc=lk?sh[lk]:{},el=document.getElementById('layers');
  if(!el)return;
  el.innerHTML='';
  var ls=['L1','L2','L3','L4','L5','L6','L7','L8','L9'],cs=['#10b981','#6366f1','#f59e0b','#ec4899','#8b5cf6','#14b8a6','#f97316','#06b6d4','#84cc16'],nm=['Execution','Planning','Self-Direction','Optimizer','Evolution','Identity','Meta-Cog','Meta-Meta','MMM'];
  for(var i=0;i<ls.length;i++){var l=ls[i],v=sc[l]||0;
    el.innerHTML+='<div class="bg-slate-900/40 rounded-lg p-2.5 sm:p-3 border border-slate-700/30">'+
      '<div class="flex justify-between mb-1"><span class="text-xs sm:text-sm font-bold text-slate-200">'+l+' <span class="text-[10px] text-slate-400 font-normal">'+nm[i]+'</span></span>'+
      '<span class="text-xs font-mono font-bold" style="color:'+cs[i]+'">'+v.toFixed(1)+'</span></div>'+
      '<div class="h-2 bg-slate-700 rounded-full"><div class="h-full rounded-full" style="width:'+v+'%;background:'+cs[i]+'"></div></div></div>';
  }
}

function rg(){
  var el=document.getElementById('gl');if(!el)return;el.innerHTML='';
  for(var i=0;i<g.length;i++){var x=g[i];
    var dc=x.dec==='PASS'?'text-emerald-400 bg-emerald-400/10 border-emerald-400/20':x.dec==='FAIL'?'text-rose-400 bg-rose-400/10 border-rose-400/20':'text-amber-400 bg-amber-400/10 border-amber-400/20';
    var cv=x.conversation||[];
    var cd=document.createElement('div');
    cd.className='bg-slate-800/60 border border-slate-700/50 rounded-xl overflow-hidden';
    cd.innerHTML='<div class="p-3 sm:p-4 cursor-pointer flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 hover:bg-slate-700/20" onclick="tg('+i+')">'+
      '<div class="flex-1"><div class="flex gap-2 flex-wrap mb-1"><span class="px-1.5 py-0.5 bg-slate-900 font-mono text-[10px] font-bold rounded text-slate-400">P'+x.p+'</span>'+
      '<span class="'+dc+' px-2 py-0.5 text-[10px] font-semibold rounded-full border">'+x.dec+'</span>'+
      '<span class="text-[10px] text-slate-500 font-mono">'+(x.conf||'')+'</span></div>'+
      '<p class="text-xs sm:text-sm text-slate-100" style="overflow-wrap:break-word">'+esc(x.d)+'</p>'+
      '<div class="flex gap-2 mt-1 text-[10px] font-mono text-slate-500"><span>'+(x.file||'')+'</span>'+(x.func?' &middot; '+x.func:'')+(x.type?' &middot; '+x.type:'')+'</div></div>'+
      '<span class="text-xs text-slate-400 arrow">&#x25BC;</span></div>'+
      '<div class="hide border-t border-slate-700/50 p-3 sm:p-4 bg-slate-900/40 space-y-3" id="gd'+i+'">'+
      '<div class="grid grid-cols-1 md:grid-cols-2 gap-3"><div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Constraints</h4>'+
      (x.constraints?Object.keys(x.constraints).map(function(n){var t=x.constraints[n];var c=t==='REQUIRED'||t==='LOCKED'?'bg-amber-500/10 text-amber-400 border-amber-500/30':t==='RECOMMENDED'?'bg-blue-500/10 text-blue-400 border-blue-500/30':'bg-slate-800 text-slate-400 border-slate-700';return '<span class="px-2 py-0.5 rounded text-[10px] font-mono border '+c+'">'+n+' <span class="text-[8px] opacity-70">'+t+'</span></span>';}).join(''):'<span class="text-[11px] text-slate-500">None</span>')+
      '</div><div><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">Details</h4>'+
      '<div class="text-xs text-slate-400 space-y-1"><div>Decision: <strong class="text-slate-200">'+x.dec+'</strong></div>'+
      '<div>Confidence: <strong class="text-slate-200">'+(x.conf||'')+'</strong></div>'+
      '<div>Pulse: <strong class="text-slate-200">#'+x.p+'</strong></div>'+
      (cv.length?'<div>Exchanges: <strong class="text-slate-200">'+cv.length+'</strong></div>':'')+
      '</div></div></div>'+
      (cv.length?'<div class="border-t border-slate-700/40 pt-3"><h4 class="text-[10px] font-bold text-slate-400 uppercase mb-2">RRP Conversation</h4><div class="space-y-2 max-h-[300px] overflow-y-auto">'+
      cv.map(function(e,ci){return '<div class="bg-slate-800/60 rounded-lg p-2 border border-slate-700/30"><div class="text-[10px] text-slate-500 font-mono mb-1">'+(ci+1)+(e.r?' (R'+e.r+')':'')+'</div>'+
      (e.q?'<div class="text-[11px] text-slate-300 mb-1" style="overflow-wrap:break-word"><span class="text-indigo-400 font-bold">Q:</span> '+fa(e.q)+'</div>':'')+
      (e.a!==undefined&&e.a!==null&&e.a!==''?'<div class="text-[11px] text-slate-400" style="overflow-wrap:break-word"><span class="text-emerald-400 font-bold">A:</span> '+fa(e.a)+'</div>':'')+'</div>';}).join('')+
      '</div></div>':'')+
      '</div>';
    el.appendChild(cd);
  }
  document.getElementById('gc').textContent=g.length+' goals';
}

function tg(i){
  var e=document.getElementById('gd'+i);
  if(e)e.classList.toggle('hide');
}

function fl(){
  var q=document.getElementById('gs').value.toLowerCase();
  var d=document.getElementById('gf').value;
  var cards=document.querySelectorAll('#gl > div');var c=0;
  for(var i=0;i<cards.length;i++){
    var txt=cards[i].querySelector('p')?.textContent||'';
    var bdg=cards[i].querySelector('.font-semibold')?.textContent||'';
    var mq=!q||txt.toLowerCase().indexOf(q)>-1;
    var md=!d||bdg.indexOf(d)>-1;
    cards[i].style.display=(mq&&md)?'':'none';
    if(mq&&md)c++;
  }
  document.getElementById('gc').textContent=c+'/'+g.length+' goals';
}

function rp(){
  var el=document.getElementById('pl');if(!el)return;el.innerHTML='';
  for(var i=0;i<pu.length;i++){var p=pu[i];
    var pid=(''+p.id).padStart(3,'0'),hd=PD[pid],ps=hd&&hd.pre_state;
    var cd=document.createElement('div');
    cd.className='bg-slate-800/60 border border-slate-700/50 rounded-xl overflow-hidden';
    cd.innerHTML='<div class="p-3 sm:p-4 cursor-pointer flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 hover:bg-slate-700/20" onclick="tp('+i+')">'+
      '<div class="flex items-center gap-3"><span class="px-2 py-1 bg-indigo-500/10 text-indigo-400 text-xs font-bold rounded-full border border-indigo-500/20">#'+p.id+'</span>'+
      '<div><div class="text-sm font-semibold text-slate-200">'+esc(p.type||'Pulse')+'</div>'+
      '<div class="text-[10px] text-slate-500 font-mono">'+(p.ts_start?.substring(11,19)||'')+'</div></div></div>'+
      '<div class="flex items-center gap-3"><span class="text-[10px] text-slate-400">'+(p.goals_count||0)+'g</span>'+
      '<span class="text-[10px] text-emerald-400 font-mono">'+(p.duration||'?')+'s</span>'+
      '<span class="text-xs text-slate-400 arrow">&#x25BC;</span></div></div>'+
      '<div class="hide border-t border-slate-700/50 p-3 sm:p-4 bg-slate-900/40" id="pd'+i+'">'+
      '<div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-3">'+
      '<div class="bg-slate-800/60 rounded-lg p-2 text-center"><div class="text-xs font-bold text-emerald-400">'+(p.approved||0)+'</div><div class="text-[9px] text-slate-400">Approved</div></div>'+
      '<div class="bg-slate-800/60 rounded-lg p-2 text-center"><div class="text-xs font-bold text-indigo-400">'+(p.goals_count||0)+'</div><div class="text-[9px] text-slate-400">Goals</div></div>'+
      '<div class="bg-slate-800/60 rounded-lg p-2 text-center"><div class="text-xs font-bold text-amber-400">'+(p.implementation_count||0)+'</div><div class="text-[9px] text-slate-400">Impl</div></div>'+
      '<div class="bg-slate-800/60 rounded-lg p-2 text-center"><div class="text-xs font-bold text-purple-400">'+(p.avg_confidence||'')+'</div><div class="text-[9px] text-slate-400">Conf</div></div></div>'+
      (ps?'<div class="border-t border-slate-700/40 pt-3"><div class="grid grid-cols-5 gap-2">'+
      '<div class="bg-slate-800/60 rounded p-2 text-center"><div class="text-[9px] text-slate-400">Rate</div><div class="text-xs font-bold text-emerald-400">'+(ps.success_rate*100).toFixed(1)+'%</div></div>'+
      '<div class="bg-slate-800/60 rounded p-2 text-center"><div class="text-[9px] text-slate-400">Imps</div><div class="text-xs font-bold">'+(ps.total_improvements||0)+'</div></div>'+
      '<div class="bg-slate-800/60 rounded p-2 text-center"><div class="text-[9px] text-slate-400">OK</div><div class="text-xs font-bold text-emerald-400">'+(ps.successful||0)+'</div></div>'+
      '<div class="bg-slate-800/60 rounded p-2 text-center"><div class="text-[9px] text-slate-400">Cyc</div><div class="text-xs font-bold">'+(ps.cycle_count||0)+'</div></div>'+
      '<div class="bg-slate-800/60 rounded p-2 text-center"><div class="text-[9px] text-slate-400">Layers</div><div class="text-xs font-bold text-indigo-400">'+(ps.scores?Object.keys(ps.scores).length:'0')+'</div></div></div></div>':'')+
      '</div>';
    el.appendChild(cd);
  }
}

function tp(i){
  var e=document.getElementById('pd'+i);
  if(e)e.classList.toggle('hide');
}

function rc(){
  var pf=document.getElementById('cpf').value;
  var el=document.getElementById('cl');if(!el)return;el.innerHTML='';
  var f=[];
  for(var i=0;i<g.length;i++){var c=g[i].conversation||[];if(c.length>0&&(!pf||''+g[i].p===pf))f.push(g[i]);}
  document.getElementById('cc').textContent=f.length+' conversations';
  for(var fi=0;fi<f.length;fi++){var g2=f[fi],c2=g2.conversation||[];
    var d=document.createElement('div');
    d.className='bg-slate-800/60 border border-slate-700/50 rounded-xl p-3 sm:p-4';
    d.innerHTML='<div class="flex items-center gap-2 mb-2"><span class="px-1.5 py-0.5 bg-indigo-500/10 text-indigo-400 text-[10px] font-bold rounded border border-indigo-500/20">P'+g2.p+'</span>'+
      '<span class="text-xs text-slate-200" style="overflow-wrap:break-word">'+esc(g2.d).substring(0,80)+(g2.d.length>80?'...':'')+'</span></div>'+
      '<div class="space-y-2 max-h-[500px] overflow-y-auto">'+
      c2.map(function(e,ci){return '<div class="bg-slate-900/40 rounded-lg p-2.5 border border-slate-700/30"><div class="text-[10px] text-slate-500 font-mono mb-1">#'+(ci+1)+(e.r?' (R'+e.r+')':'')+'</div>'+
      (e.q?'<div class="text-xs text-slate-300 mb-1" style="overflow-wrap:break-word"><span class="text-indigo-400 font-bold">Q:</span> '+fa(e.q)+'</div>':'')+
      (e.a!==undefined&&e.a!==null&&e.a!==''?'<div class="text-xs text-slate-400" style="overflow-wrap:break-word"><span class="text-emerald-400 font-bold">A:</span> '+fa(e.a)+'</div>':'')+'</div>';}).join('')+
      '</div>';
    el.appendChild(d);
  }
}

function rcb(){
  var cd=(AD.summary&&AD.summary.cd)||{};
  var el=document.getElementById('cbd');if(!el)return;el.innerHTML='';
  for(var n in cd){var d=cd[n],lr=d.freq>0?((d.locked/d.freq)*100).toFixed(1):0;
    el.innerHTML+='<div class="bg-slate-900/40 rounded-lg p-3 border border-slate-700/30">'+
      '<div class="flex justify-between mb-1"><span class="text-xs sm:text-sm font-bold text-slate-200">'+n+'</span><span class="text-xs font-mono">'+d.locked+'/'+d.freq+' ('+lr+'%)</span></div>'+
      '<div class="h-2 bg-slate-700 rounded-full"><div class="h-full bg-gradient-to-r from-amber-500 to-rose-400 rounded-full" style="width:'+lr+'%"></div></div></div>';
  }
}

var kn=[];
function bk(){
  kn=[];for(var i=0;i<g.length;i++){var x=g[i];
    kn.push({id:'g'+i,label:x.d.substring(0,25)+'..',color:x.dec==='PASS'?'#10b981':x.dec==='FAIL'?'#f43f5e':'#f59e0b',x:50+Math.random()*700,y:50+Math.random()*400,r:4+Math.random()*5});}
  rk();
}
function rk(){
  var ca=document.getElementById('kgC');if(!ca)return;
  var ctx=ca.getContext('2d'),rect=ca.parentElement.getBoundingClientRect();
  ca.width=Math.min(rect.width-48,1000);ca.height=500;
  ctx.clearRect(0,0,ca.width,ca.height);
  ctx.strokeStyle='#334155';ctx.lineWidth=0.5;
  for(var i=0;i<kn.length;i++)for(var j=i+1;j<kn.length;j++){if(Math.abs(i-j)<3){ctx.beginPath();ctx.moveTo(kn[i].x,kn[i].y);ctx.lineTo(kn[j].x,kn[j].y);ctx.stroke();}}
  for(var ni=0;ni<kn.length;ni++){var n=kn[ni];
    ctx.beginPath();ctx.arc(n.x,n.y,n.r,0,Math.PI*2);ctx.fillStyle=n.color;ctx.shadowColor=n.color;ctx.shadowBlur=8;ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle='#94a3b8';ctx.font='7px monospace';ctx.fillText(n.label,n.x+n.r+3,n.y+3);}
}
function ak(l){
  var ca=document.getElementById('kgC');var w=ca?ca.width:800;var h=500;
  for(var i=0;i<kn.length;i++){var n=kn[i];
    if(l==='radial'){var a=(2*Math.PI*i)/kn.length;var r=Math.min(w,h)*0.35;n.x=w/2+r*Math.cos(a);n.y=h/2+r*Math.sin(a);}
    else if(l==='grid'){var c=Math.ceil(Math.sqrt(kn.length));n.x=(w/(c+1))*(1+(i%c));n.y=(h/(Math.ceil(kn.length/c)+1))*(1+Math.floor(i/c));}
    else{n.x=50+Math.random()*(w-100);n.y=50+Math.random()*(h-100);}
  }
  rk();
}

function ic(){
  var c1=document.getElementById('c1');if(c1){var p=0,f=0,h=0;g.forEach(function(x){if(x.dec==='PASS')p++;else if(x.dec==='FAIL')f++;else h++;});
    ch.c1=new Chart(c1,{type:'doughnut',data:{labels:['Passed','Failed','Held'],datasets:[{data:[p,f,h],backgroundColor:['#10b981','#f43f5e','#f59e0b'],borderWidth:2}]},options:{responsive:true,plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:10}}}}}});}
  var c11=document.getElementById('c11');if(c11){var gt={};g.forEach(function(x){var t=x.type||'unknown';gt[t]=(gt[t]||0)+1;});var gtk=Object.keys(gt);
    ch.c11=new Chart(c11,{type:'doughnut',data:{labels:gtk,datasets:[{data:gtk.map(function(k){return gt[k];}),backgroundColor:['#6366f1','#f59e0b','#ec4899','#8b5cf6','#14b8a6','#f97316'],borderWidth:2}]},options:{responsive:true,plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:10}}}}}});}
  var c12=document.getElementById('c12');if(c12){var totalL=0,totalO=0;g.forEach(function(x){var cn=x.constraints||{};Object.keys(cn).forEach(function(k){if(cn[k]==='LOCKED')totalL++;else totalO++;});});if(totalL+totalO===0){totalL=1;totalO=1;}
    ch.c12=new Chart(c12,{type:'doughnut',data:{labels:['Locked','Optional'],datasets:[{data:[totalL,totalO],backgroundColor:['#f59e0b','#6366f180'],borderWidth:2}]},options:{responsive:true,plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:10}}}}}});}
  var c13=document.getElementById('c13');if(c13){var pt={};pu.forEach(function(x){var t=x.type||'standard';var s=t.split('_')[0]+'_'+t.split('_')[1];if(s==='rrp_')s='rrp_v2';if(s==='full'||t==='standard')s=t.split('_')[0];pt[s]=(pt[s]||0)+1;});var ptk=Object.keys(pt);
    ch.c13=new Chart(c13,{type:'doughnut',data:{labels:ptk,datasets:[{data:ptk.map(function(k){return pt[k];}),backgroundColor:['#10b981','#6366f1','#f59e0b','#ec4899','#8b5cf6','#14b8a6','#f97316','#06b6d4','#84cc16'],borderWidth:2}]},options:{responsive:true,plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:10}}}}}});}
  var c2=document.getElementById('c2');if(c2){ch.c2=new Chart(c2,{type:'line',data:{labels:pu.map(function(p){return '#'+p.id;}),datasets:[{label:'Success %',data:pu.map(function(p){return p.goals_count>0?(p.approved/p.goals_count*100):0;}),borderColor:'#10b981',backgroundColor:'rgba(16,185,129,0.1)',fill:true,tension:0.3}]},options:{responsive:true,plugins:{legend:{labels:{color:'#94a3b8',font:{size:10}}}},scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b'},beginAtZero:true,max:100}}}});}
  var c3=document.getElementById('c3');if(c3){ch.c3=new Chart(c3,{type:'bar',data:{labels:pu.map(function(p){return '#'+p.id;}),datasets:[{label:'Duration(s)',data:pu.map(function(p){return p.duration||0;}),backgroundColor:'#6366f1'}]},options:{responsive:true,plugins:{legend:{labels:{color:'#94a3b8',font:{size:10}}}},scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b'}}}}});}
  var c4=document.getElementById('c4');if(c4){ch.c4=new Chart(c4,{type:'line',data:{labels:pu.map(function(p){return '#'+p.id;}),datasets:[{label:'Confidence %',data:pu.map(function(p){return(p.avg_confidence||0)*100;}),borderColor:'#f59e0b',backgroundColor:'rgba(245,158,11,0.1)',fill:true,tension:0.3}]},options:{responsive:true,plugins:{legend:{labels:{color:'#94a3b8',font:{size:10}}}},scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b'},beginAtZero:true,max:100}}}});}
  var c5=document.getElementById('c5');if(c5){var vk=Object.keys(sh).filter(function(k){return sh[k]&&Object.keys(sh[k]).length>0;});var ly=['L1','L2','L3','L4','L5','L6','L7','L8','L9'];var co=['#10b981','#6366f1','#f59e0b','#ec4899','#8b5cf6','#14b8a6','#f97316','#06b6d4','#84cc16'];
    ch.c5=new Chart(c5,{type:'line',data:{labels:vk.map(function(k){return 'P'+k;}),datasets:ly.map(function(l,i){return{label:l,data:vk.map(function(k){return sh[k][l]||null;}),borderColor:co[i],backgroundColor:co[i]+'20',tension:0.3,pointRadius:2,borderWidth:1.5};})},options:{responsive:true,interaction:{mode:'index',intersect:false},plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:9}}}},scales:{x:{ticks:{color:'#64748b',font:{size:8}}},y:{ticks:{color:'#64748b',font:{size:9}},beginAtZero:true,max:100}}}});}
  var c6=document.getElementById('c6');if(c6){ch.c6=new Chart(c6,{type:'bar',data:{labels:pu.map(function(p){return '#'+p.id;}),datasets:[{label:'Total',data:pu.map(function(p){return p.goals_count||0;}),backgroundColor:'#6366f180'},{label:'Approved',data:pu.map(function(p){return p.approved||0;}),backgroundColor:'#10b98180'}]},options:{responsive:true,plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:10}}}}}});}
  var c7=document.getElementById('c7');if(c7&&AD.summary&&AD.summary.cd){var cd=AD.summary.cd,cn=Object.keys(cd);
    ch.c7=new Chart(c7,{type:'bar',data:{labels:cn,datasets:[{label:'Total',data:cn.map(function(n){return cd[n].freq;}),backgroundColor:'#6366f180'},{label:'Locked',data:cn.map(function(n){return cd[n].locked;}),backgroundColor:'#f59e0b80'}]},options:{responsive:true,indexAxis:'y',plugins:{legend:{labels:{color:'#94a3b8',font:{size:10}}}},scales:{x:{ticks:{color:'#64748b'}},y:{ticks:{color:'#64748b'}}}}});}
  var c8=document.getElementById('c8');if(c8){var vk2=Object.keys(sh).filter(function(k){return sh[k]&&Object.keys(sh[k]).length>0;});var lk=vk2[vk2.length-1]||'1',ls=sh[lk]||{};
    ch.c8=new Chart(c8,{type:'radar',data:{labels:['L1','L2','L3','L4','L5','L6','L7','L8','L9'],datasets:[{label:'Latest',data:['L1','L2','L3','L4','L5','L6','L7','L8','L9'].map(function(l){return ls[l]||0;}),backgroundColor:'rgba(99,102,241,0.2)',borderColor:'#6366f1',pointBackgroundColor:'#6366f1',pointRadius:4}]},options:{responsive:true,plugins:{legend:{labels:{color:'#94a3b8',font:{size:10}}}},scales:{r:{ticks:{color:'#64748b',backdropColor:'transparent'},grid:{color:'#334155'},beginAtZero:true,max:100}}}});}
  var c9=document.getElementById('c9');if(c9&&AD.summary&&AD.summary.cd){var cd2=AD.summary.cd,cn2=Object.keys(cd2);
    ch.c9=new Chart(c9,{type:'pie',data:{labels:cn2,datasets:[{data:cn2.map(function(n){return cd2[n].freq;}),backgroundColor:['#6366f1','#10b981','#f59e0b','#ec4899','#8b5cf6','#14b8a6','#f97316','#06b6d4','#84cc16','#f43f5e']}]},options:{plugins:{legend:{position:'bottom',labels:{color:'#94a3b8',font:{size:9}}}}}});}
  var c10=document.getElementById('c10');if(c10&&AD.summary&&AD.summary.cd){var cd3=AD.summary.cd,cn3=Object.keys(cd3),rt=cn3.map(function(n){return cd3[n].freq>0?(cd3[n].locked/cd3[n].freq*100):0;}),rc=rt.map(function(r){return r>80?'#f43f5e':r>50?'#f59e0b':'#10b981';});
    ch.c10=new Chart(c10,{type:'bar',data:{labels:cn3,datasets:[{label:'Lock %',data:rt,backgroundColor:rc}]},options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{ticks:{color:'#64748b'},beginAtZero:true,max:100},y:{ticks:{color:'#64748b'}}}}});}
}

function pf(){
  var el=document.getElementById('cpf');if(!el)return;
  var seen={};for(var i=0;i<g.length;i++){var c=g[i].conversation||[];if(c.length>0)seen[''+g[i].p]=true;}
  Object.keys(seen).sort(function(a,b){return parseInt(a)-parseInt(b);}).forEach(function(p){var o=document.createElement('option');o.value=p;o.textContent='Pulse #'+p;el.appendChild(o);});
}

// Comprehensive tooltip system
document.addEventListener('mouseover', function(e){
  if(e.target.tagName==='CANVAS') return;
  var t = e.target.closest('[data-tt]');
  if(!t) return;
  if(t.classList.contains('tb') && window.matchMedia && window.matchMedia('(hover: none)').matches) return;
  var key = t.getAttribute('data-tt');
  var existing = t.querySelector('.tooltip');
  if(existing) { existing.classList.add('show'); return; }
  var tip = document.createElement('div');
  tip.className = 'tooltip';
  tip.innerHTML = getTooltipContent(key);
  t.style.position = 'relative';
  t.appendChild(tip);
  setTimeout(function(){tip.classList.add('show');}, 10);
});
document.addEventListener('mouseout', function(e){
  if(e.target.tagName==='CANVAS') return;
  var t = e.target.closest('[data-tt]');
  if(!t) return;
  var tip = t.querySelector('.tooltip');
  if(tip) setTimeout(function(){tip.classList.remove('show');}, 200);
});

function getTooltipContent(key){
  var parts = key.split(':');
  var type = parts[0], name = parts[1]||'', a = parseInt(parts[2]||-1), b = parseInt(parts[3]||-1), c = parseInt(parts[4]||-1);
  if(type==='layer') return '<h4>Layer '+name+'</h4><p>Capability score for this RSIS layer. Higher is better (0-100).</p>';
  if(type==='pulse') return getPulseHeaderTooltip(a);
  if(type==='pstat') return getPulseStatTooltip(a, name);
  if(type==='ppre') return '<h4>Pre-State '+name+'</h4><p>Pre-pulse system metric.</p>';
  if(type==='pgoal') return '<h4>Goal</h4><p>An improvement goal processed in this pulse. Click to expand for RRP conversation details.</p>';
  if(type==='pconv') return '<h4>RRP Exchange</h4><p>A single question-answer exchange from the Recursive Refinement Protocol dialogue.</p>';
  if(type==='pconst') return getConstraintInfo(name);
  if(type==='graph') return getGraphInfo(name);
  if(type==='tab') return getTabInfo(name);
  if(type==='summary') return '<h4>'+name+'</h4><p>Summary metric from the telemetry dashboard.</p>';
  return '<h4>Info</h4><p>'+name+'</p>';
}

function getPulseHeaderTooltip(idx){
  if(idx<0||idx>=pu.length) return '<h4>Pulse</h4><p>Unknown.</p>';
  var p=pu[idx];
  var pg=g.filter(function(gl){return ''+gl.p===''+p.id;});
  var pass=pg.filter(function(gx){return gx.dec==='PASS';}).length;
  var fail=pg.filter(function(gx){return gx.dec==='FAIL';}).length;
  var hold=pg.filter(function(gx){return gx.dec==='HOLD';}).length;
  return '<h4>Pulse #'+p.id+' \u2014 '+(p.type||'Standard')+'</h4>'+
    '<p>An execution pulse processing '+pg.length+' goals through the RSIS pipeline. Click to expand for goal details, RRP conversations, and pre-state metrics.</p>'+
    '<div class="tt-grid">'+
    '<div class="tt-grid-item"><div class="tt-gv">'+pg.length+'</div><div class="tt-gl">Goals</div></div>'+
    '<div class="tt-grid-item"><div class="tt-gv">'+pass+'</div><div class="tt-gl">Passed</div></div>'+
    '<div class="tt-grid-item"><div class="tt-gv">'+fail+'</div><div class="tt-gl">Failed</div></div>'+
    '<div class="tt-grid-item"><div class="tt-gv">'+(p.duration||'?')+'s</div><div class="tt-gl">Duration</div></div>'+
    '</div>'+
    '<div class="tt-section"><table><tr><th>Metric</th><th>Value</th></tr>'+
    '<tr><td>Implementation Count</td><td>'+(p.implementation_count||0)+'</td></tr>'+
    '<tr><td>Avg Confidence</td><td>'+(p.avg_confidence!==undefined?(p.avg_confidence*100).toFixed(0)+'%':'N/A')+'</td></tr>'+
    '<tr><td>Timestamp</td><td>'+(p.ts_start?'<span class="text-[10px]">'+p.ts_start.substring(11,19)+'</span>':'N/A')+'</td></tr>'+
    '</table></div>';
}

function getPulseStatTooltip(idx, name){
  if(idx<0||idx>=pu.length) return '<h4>Stat</h4><p>Unknown.</p>';
  var p=pu[idx];
  var descs={
    approved:'Goals that passed RRP evaluation and were approved for implementation in this pulse.',
    goals:'Total improvement goals generated and processed in this pulse.',
    impl:'Improvements successfully implemented (code generated, applied, verified).',
    conf:'Average RRP evaluator confidence score across all goals in this pulse. Higher = clearer goals.'
  };
  var vals={approved:p.approved||0,goals:(g.filter(function(gl){return ''+gl.p===''+p.id;})).length,impl:p.implementation_count||0,conf:p.avg_confidence!==undefined?(p.avg_confidence*100).toFixed(0)+'%':'N/A'};
  return '<h4>'+name.charAt(0).toUpperCase()+name.slice(1)+'</h4><p>'+(descs[name]||'Pulse metric.')+'</p><div class="tt-metric"><span class="tt-label">Value</span><span class="tt-val">'+(vals[name]||'?')+'</span></div>';
}

function getConstraintInfo(name){
  var info={
    error_handling:{d:'Ensures errors are caught with try/except, logged with context, and handled with graceful fallbacks.',i:'Critical for production reliability.'},
    type_safety:{d:'Requires type annotations on function signatures and runtime validation.',i:'Prevents type-related runtime errors.'},
    test_coverage:{d:'New/modified code must have corresponding tests.',i:'Essential for regression prevention.'},
    logging:{d:'Appropriate logging for debugging and monitoring.',i:'Required for operational visibility.'},
    documentation:{d:'Docstrings and docs for new/modified APIs.',i:'Critical for maintainability.'},
    security:{d:'Security best practices \u2014 input validation, auth, safe deserialization.',i:'Prevents vulnerabilities.'},
    input_validation:{d:'Validate all external inputs before processing.',i:'Defense against malformed data and injection.'},
    code_quality:{d:'DRY, single responsibility, clear naming.',i:'Reduces technical debt.'},
    maintainability:{d:'Modular code with clear interfaces.',i:'Essential for sustainable development.'},
    performance:{d:'Algorithm choice, caching, async, resource management.',i:'Prevents performance regressions.'}
  };
  var ci=info[name];
  if(!ci) return '<h4>'+name.replace(/_/g,' ').replace(/\b\w/g,function(l){return l.toUpperCase();})+'</h4><p>RRP constraint.</p>';
  var cd=(AD.summary&&AD.summary.cd)?AD.summary.cd[name]:null;
  return '<h4>'+name.replace(/_/g,' ').replace(/\b\w/g,function(l){return l.toUpperCase();})+'</h4>'+
    '<p><strong>Definition:</strong> '+ci.d+'</p>'+
    '<p><strong>Importance:</strong> '+ci.i+'</p>'+
    (cd?'<table><tr><th>Freq</th><th>Locked</th><th>Lock Rate</th></tr><tr><td>'+cd.freq+'</td><td>'+cd.locked+'</td><td>'+(cd.freq>0?(cd.locked/cd.freq*100).toFixed(0):'0')+'%</td></tr></table>':'');
}

function getGraphInfo(name){
  var d={'c1':'Pie chart: PASS/FAIL/HOLD decision distribution.','c11':'Goal type distribution.','c12':'Constraint lock vs optional.','c13':'Pulse type distribution.','c2':'Line chart: success rate trend per pulse.','c3':'Bar chart: pulse duration.','c4':'Line chart: evaluator confidence trend.','c5':'Multi-line: all 9 layer scores.','c6':'Stacked bar: goals vs approved per pulse.','c7':'Horizontal bar: constraint frequency by type.','c8':'Radar: latest layer scores.','c9':'Pie: constraint distribution.','c10':'Horizontal bar: constraint lock rate.','c11':'Pie: goal type distribution.','c12':'Pie: constraint lock vs optional.','c13':'Pie: pulse type distribution.'};
  return '<h4>Chart '+name.toUpperCase()+'</h4><p>'+(d[name]||'Telemetry chart.')+'</p>';
}

function getTabInfo(name){
  var d={overview:'Summary stats, success rate, layer scores.',pulses:'20 pulses with embedded goals, conversations, and evaluation results.',kg:'Interactive knowledge graph.',graphs:'Full chart suite: decisions, trends, durations, constraints, radar.',constraints:'Constraint frequency and lock rate analysis.',loops:'Nine-loop stack: targets, tuned params, last signal, run counts, honest runtime state (RECENT/IDLE/NOT RUN from loops.json).',mykb:'Wiki browser, knowledge graph, stats, guidance (stub review, feedback & research direction).',space:'SPACE web UI + spec viewer (lazy-loaded iframes).'};
  return '<h4>'+name.charAt(0).toUpperCase()+name.slice(1)+' Tab</h4><p>'+(d[name]||'Dashboard tab.')+'</p>';
}

// ── Initialize ────────────────────────────────────────────────

loadData();
