with open('/data/data/com.termux/files/home/dev/space/meta-viewer.html', 'r') as f:
    html = f.read()

# ============================================================
# 1. Reassign groups in DOCUMENTS
# ============================================================
replacements = [
    ("{ file:'CYCLE-001-AUDIT-REPORT.md', title:'Cycle 001 Audit Report', group:'Reports', icon:'🔍', cat:'audit' },",
     "{ file:'CYCLE-001-AUDIT-REPORT.md', title:'Cycle 001 Audit Report', group:'Cycle 001', icon:'🔍', cat:'audit' },"),
    ("{ file:'CYCLE-002-AUDIT-REPORT.md', title:'Cycle 002 Audit Report', group:'Reports', icon:'🔍', cat:'audit' },",
     "{ file:'CYCLE-002-AUDIT-REPORT.md', title:'Cycle 002 Audit Report', group:'Cycle 002', icon:'🔍', cat:'audit' },"),
    ("{ file:'CYCLE-002-IMPROVEMENT-ROADMAP.md', title:'Cycle 002 Improvement Roadmap', group:'Reports', icon:'🗺️', cat:'roadmap' },",
     "{ file:'CYCLE-002-IMPROVEMENT-ROADMAP.md', title:'Cycle 002 Improvement Roadmap', group:'Cycle 002', icon:'🗺️', cat:'roadmap' },"),
    ("{ file:'CYCLE-002-COMPLETION-REVIEW.md', title:'Cycle 002 Completion Review', group:'Reports', icon:'✅', cat:'review' },",
     "{ file:'CYCLE-002-COMPLETION-REVIEW.md', title:'Cycle 002 Completion Review', group:'Cycle 002', icon:'✅', cat:'review' },"),
    ("{ file:'CYCLE-002-COMPLETION-REPORT.md', title:'Cycle 002 Completion Report', group:'Reports', icon:'✅', cat:'review' },",
     "{ file:'CYCLE-002-COMPLETION-REPORT.md', title:'Cycle 002 Completion Report', group:'Cycle 002', icon:'✅', cat:'review' },"),
    ("{ file:'CYCLE-003-AUDIT-REPORT.md', title:'Cycle 003 Audit Report', group:'Reports', icon:'🔍', cat:'audit' },",
     "{ file:'CYCLE-003-AUDIT-REPORT.md', title:'Cycle 003 Audit Report', group:'Cycle 003', icon:'🔍', cat:'audit' },"),
    ("{ file:'CYCLE-003-IMPROVEMENT-ROADMAP.md', title:'Cycle 003 Roadmap', group:'Reports', icon:'🗺️', cat:'roadmap' },",
     "{ file:'CYCLE-003-IMPROVEMENT-ROADMAP.md', title:'Cycle 003 Roadmap', group:'Cycle 003', icon:'🗺️', cat:'roadmap' },"),
    ("{ file:'CYCLE-003-COMPLETION-REVIEW.md', title:'Cycle 003 Review', group:'Reports', icon:'✅', cat:'review' },",
     "{ file:'CYCLE-003-COMPLETION-REVIEW.md', title:'Cycle 003 Review', group:'Cycle 003', icon:'✅', cat:'review' },"),
    ("{ file:'CYCLE-004-AUDIT-REPORT.md', title:'Cycle 004 Audit Report', group:'Reports', icon:'🔍', cat:'audit' },",
     "{ file:'CYCLE-004-AUDIT-REPORT.md', title:'Cycle 004 Audit Report', group:'Cycle 004', icon:'🔍', cat:'audit' },"),
    ("{ file:'CYCLE-004-COMPLETION-REVIEW.md', title:'Cycle 004 Review', group:'Reports', icon:'✅', cat:'review' },",
     "{ file:'CYCLE-004-COMPLETION-REVIEW.md', title:'Cycle 004 Review', group:'Cycle 004', icon:'✅', cat:'review' },"),
]

for old, new in replacements:
    assert old in html, f"NOT FOUND: {old[:60]}"
    html = html.replace(old, new)

print("Groups reassigned")

# Add project-status.md to Development group
insert_point = "  { file:'dev/README.md', title:'Dev Docs Overview', group:'Development', icon:'📋', cat:'dev' },"
new_entry = "  { file:'project-status.md', title:'Project Status', group:'Development', icon:'📊', cat:'dev' },\n  { file:'dev/README.md', title:'Dev Docs Overview', group:'Development', icon:'📋', cat:'dev' },"
assert insert_point in html
html = html.replace(insert_point, new_entry)
print("Added project-status.md")

# ============================================================
# 2. Add collapsible group CSS
# ============================================================
collapse_css = '''
/* Collapsible groups */
.nav-group-header{display:flex;align-items:center;gap:4px;padding:8px 10px 4px;cursor:pointer;user-select:none;transition:color .15s}
.nav-group-header:hover{color:var(--text)}
.nav-group-header .collapse-icon{font-size:8px;color:var(--text-muted);transition:transform .2s;width:12px;text-align:center;flex-shrink:0}
.nav-group-header .collapse-icon.collapsed{transform:rotate(-90deg)}
.nav-group-title{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--text-muted);margin:0}
.nav-group-header:hover .nav-group-title{color:var(--text-secondary)}
.nav-group-content{overflow:hidden;transition:max-height .25s ease}
.nav-group-content.collapsed{max-height:0 !important}'''

html = html.replace('/* Search */', collapse_css + '\n\n/* Search */')
print("Collapsible CSS added")

# ============================================================
# 3. Replace buildSidebar
# ============================================================
old_build = """// Build sidebar
function buildSidebar(filter='') {
  const q = filter.toLowerCase();
  const groups = {};
  for (const d of DOCUMENTS) {
    if (q && !d.title.toLowerCase().includes(q) && !d.group.toLowerCase().includes(q)) continue;
    // Latest mode: only show CYCLE-004 docs
    if (filterMode === 'latest' && !d.file.includes('CYCLE-004')) continue;
    (groups[d.group] = groups[d.group] || []).push(d);
  }
  const groupOrder = Object.keys(groups).sort((a, b) => {
    // Custom order: Reports, Development, Specifications
    const order = ['Reports', 'Development', 'Specifications'];
    return order.indexOf(a) - order.indexOf(b);
  });
  let html = '';
  let total = 0;
  for (const group of groupOrder) {
    const docs = groups[group];
    html += '<div class="nav-group">';
    html += `<div class="nav-group-title">${group}</div>`;
    for (const d of docs) {
      const active = currentDoc && currentDoc.file === d.file ? ' active' : '';
      const dot = d.cat ? `<span class="status-dot ${d.cat}"></span>` : '';
      html += `<div class="nav-item${active}" onclick="loadDoc('${d.file}','${d.title}','${d.cat}')" title="${d.title}">${dot}<span class="icon">${d.icon}</span>${d.title}</div>`;
      total++;
    }
    html += '</div>';
  }
  docNav.innerHTML = html;
  docCount.textContent = `${total} documents${filterMode === 'latest' ? ' (latest)' : ''}`;
}"""

new_build = """// Group collapse state
const groupCollapse = {};

function loadCollapseState() {
  try {
    const saved = localStorage.getItem('space-group-collapse');
    if (saved) Object.assign(groupCollapse, JSON.parse(saved));
  } catch(e) {}
}

function saveCollapseState() {
  try {
    localStorage.setItem('space-group-collapse', JSON.stringify(groupCollapse));
  } catch(e) {}
}

function toggleGroup(group) {
  groupCollapse[group] = !groupCollapse[group];
  saveCollapseState();
  buildSidebar(document.getElementById('search').value);
  if (currentDoc) {
    const el = document.querySelector(`.nav-item[data-file="${currentDoc.file}"]`);
    if (el) el.classList.add('active');
  }
}

// Build sidebar
function buildSidebar(filter='') {
  loadCollapseState();
  const q = filter.toLowerCase();
  const groups = {};
  for (const d of DOCUMENTS) {
    if (q && !d.title.toLowerCase().includes(q) && !d.group.toLowerCase().includes(q)) continue;
    // Latest mode: only show CYCLE-004 docs
    if (filterMode === 'latest' && !d.file.includes('CYCLE-004')) continue;
    (groups[d.group] = groups[d.group] || []).push(d);
  }
  // Custom group order: cycles 1-4, then dev, then specs
  const groupOrder = ['Cycle 001', 'Cycle 002', 'Cycle 003', 'Cycle 004', 'Development', 'Specifications']
    .filter(g => groups[g]);
  let html = '';
  let total = 0;
  for (const group of groupOrder) {
    const docs = groups[group];
    const isCollapsed = groupCollapse[group] === true;
    html += '<div class="nav-group">';
    html += `<div class="nav-group-header" onclick="toggleGroup('${group}')">`;
    html += `<span class="collapse-icon ${isCollapsed ? 'collapsed' : ''}">\\u25bc</span>`;
    html += `<div class="nav-group-title">${group}</div>`;
    html += '</div>';
    html += `<div class="nav-group-content ${isCollapsed ? 'collapsed' : ''}">`;
    for (const d of docs) {
      const active = currentDoc && currentDoc.file === d.file ? ' active' : '';
      const dot = d.cat ? `<span class="status-dot ${d.cat}"></span>` : '';
      html += `<div class="nav-item${active}" data-file="${d.file}" onclick="loadDoc('${d.file}','${d.title}','${d.cat}')" title="${d.title}">${dot}<span class="icon">${d.icon}</span>${d.title}</div>`;
      total++;
    }
    html += '</div></div>';
  }
  docNav.innerHTML = html;
  docCount.textContent = `${total} documents${filterMode === 'latest' ? ' (latest)' : ''}`;
  saveCollapseState();
}"""

assert old_build in html, "ERROR: old buildSidebar not found!"
html = html.replace(old_build, new_build)
print("buildSidebar replaced")

# ============================================================
# 4. Update loadDoc to auto-expand groups
# ============================================================
old_start = """async function loadDoc(file, title, cat) {
  currentDoc = { file, title, cat };
  buildSidebar();"""

new_start = """async function loadDoc(file, title, cat) {
  currentDoc = { file, title, cat };
  // Auto-expand the group containing this doc
  const doc = DOCUMENTS.find(d => d.file === file);
  if (doc && groupCollapse[doc.group] === true) {
    groupCollapse[doc.group] = false;
    saveCollapseState();
  }
  buildSidebar();"""

assert old_start in html, "ERROR: old loadDoc start not found!"
html = html.replace(old_start, new_start)
print("loadDoc updated")

with open('/data/data/com.termux/files/home/dev/space/meta-viewer.html', 'w') as f:
    f.write(html)

print("\nAll updates complete!")
