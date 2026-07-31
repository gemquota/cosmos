#!/usr/bin/env python3
"""Enrich mykb wiki articles with cross-links and content.

Pass 1: Domain index pages — add related domain links and richer descriptions
Pass 2: Supercategory index pages — add child category links
Pass 3: Category index pages — add child subcategory links and entity counts
Pass 4: Subcategory index pages — add entity listings
Pass 5: Entity stubs — add cross-references to sibling entities
"""
import os, re, json
from collections import defaultdict

WIKI = 'wiki'
BUNDLE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if '__file__' in dir() else '.'
if not os.path.exists('wiki'):
    BUNDLE = os.getcwd()
    WIKI = os.path.join(BUNDLE, 'wiki')

# ── Domain knowledge base ──
DOMAIN_INFO = {
    'ai-ml': {
        'title': 'AI & Machine Learning',
        'desc': 'LLM ecosystems, machine learning frameworks, prompt engineering, neural architectures, and AI agent capabilities.',
        'related': ['agent-systems', 'software-engineering', 'web-platforms'],
        'tags': ['llm', 'neural', 'ml', 'ai', 'prompt', 'embedding', 'transformer', 'training'],
    },
    'agent-systems': {
        'title': 'Agent Systems',
        'desc': 'Autonomous LLM-powered agent architectures, tool-use patterns, multi-agent orchestration, and session capture pipelines.',
        'related': ['ai-ml', 'software-engineering', 'dev-tools'],
        'tags': ['agent', 'tool', 'session', 'orchestration', 'daemon', 'hook', 'codex'],
    },
    'data-storage': {
        'title': 'Data Storage',
        'desc': 'Database technologies, caching systems, ORM patterns, and data persistence strategies.',
        'related': ['web-platforms', 'software-engineering', 'security-auth'],
        'tags': ['database', 'sql', 'cache', 'redis', 'sqlite', 'postgres', 'orm', 'alembic'],
    },
    'dev-tools': {
        'title': 'Development Tools',
        'desc': 'IDEs, CLI tools, debuggers, linters, formatters, and developer productivity utilities.',
        'related': ['software-engineering', 'os-shell', 'devops-infra'],
        'tags': ['ide', 'cli', 'debug', 'lint', 'format', 'git', 'npm', 'pip'],
    },
    'devops-infra': {
        'title': 'DevOps & Infrastructure',
        'desc': 'Deployment pipelines, cloud services, containerization, CI/CD, and infrastructure automation.',
        'related': ['security-auth', 'web-platforms', 'data-storage'],
        'tags': ['deploy', 'docker', 'aws', 'ci', 'pipeline', 'terraform', 'kubernetes'],
    },
    'mobile-platform': {
        'title': 'Mobile Platform',
        'desc': 'Android development, Termux environment, mobile API patterns, and platform-specific tooling.',
        'related': ['os-shell', 'security-auth', 'web-platforms'],
        'tags': ['android', 'termux', 'mobile', 'apk', 'gradle', 'activity', 'intent'],
    },
    'os-shell': {
        'title': 'OS & Shell',
        'desc': 'Operating system internals, shell scripting, terminal workflows, and system-level tooling.',
        'related': ['dev-tools', 'devops-infra', 'mobile-platform'],
        'tags': ['bash', 'shell', 'terminal', 'linux', 'process', 'filesystem', 'grep', 'sed'],
    },
    'security-auth': {
        'title': 'Security & Authentication',
        'desc': 'Authentication protocols, authorization patterns, cryptographic primitives, and security best practices.',
        'related': ['data-storage', 'web-platforms', 'devops-infra'],
        'tags': ['auth', 'oauth', 'jwt', 'crypto', 'tls', 'ssl', 'token', 'session'],
    },
    'software-engineering': {
        'title': 'Software Engineering',
        'desc': 'Programming languages, design patterns, code quality, testing strategies, and engineering practices.',
        'related': ['dev-tools', 'ai-ml', 'data-storage'],
        'tags': ['pattern', 'testing', 'refactor', 'design', 'architecture', 'typescript', 'python'],
    },
    'web-platforms': {
        'title': 'Web Platforms',
        'desc': 'HTTP protocols, API design, frontend frameworks, CSS styling, backend services, and web security.',
        'related': ['data-storage', 'security-auth', 'software-engineering'],
        'tags': ['http', 'rest', 'graphql', 'react', 'angular', 'css', 'html', 'spa', 'ajax'],
    },
}

# Cross-domain relationship descriptions
CROSS_DOMAIN_LINKS = {
    ('ai-ml', 'agent-systems'): 'LLM agents power the agent architecture',
    ('ai-ml', 'software-engineering'): 'ML models require engineering best practices',
    ('agent-systems', 'dev-tools'): 'Agents use development tools for code execution',
    ('agent-systems', 'ai-ml'): 'Agents are built on LLM foundations',
    ('data-storage', 'web-platforms'): 'Web apps need persistent data layers',
    ('data-storage', 'security-auth'): 'Data access requires authentication',
    ('dev-tools', 'os-shell'): 'CLI tools run in shell environments',
    ('dev-tools', 'software-engineering'): 'Tools support engineering workflows',
    ('devops-infra', 'web-platforms'): 'Infrastructure hosts web services',
    ('devops-infra', 'security-auth'): 'Infrastructure requires security controls',
    ('mobile-platform', 'os-shell'): 'Termux provides shell on Android',
    ('mobile-platform', 'security-auth'): 'Mobile apps need auth flows',
    ('security-auth', 'web-platforms'): 'Web platforms need auth layers',
    ('security-auth', 'data-storage'): 'Data access requires authorization',
    ('software-engineering', 'dev-tools'): 'Engineering uses dev tools',
    ('web-platforms', 'data-storage'): 'Web apps store data',
    ('web-platforms', 'security-auth'): 'Web apps need security',
}

def get_domain(filepath):
    parts = filepath.split(os.sep)
    if 'domains' in parts:
        idx = parts.index('domains')
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return None

def is_index(filepath):
    return os.path.basename(filepath) == 'index.md'

def count_entities_in_dir(dirpath):
    count = 0
    if os.path.isdir(dirpath):
        for f in os.listdir(dirpath):
            fp = os.path.join(dirpath, f)
            if f.endswith('.md') and f != 'index.md' and f != 'overview.md':
                count += 1
            elif os.path.isdir(fp):
                count += count_entities_in_dir(fp)
    return count

def get_children_dirs(dirpath):
    """Get immediate subdirectories that contain .md files."""
    children = []
    if os.path.isdir(dirpath):
        for d in sorted(os.listdir(dirpath)):
            dp = os.path.join(dirpath, d)
            if os.path.isdir(dp) and not d.startswith('.'):
                md_count = len([f for f in os.listdir(dp) if f.endswith('.md')])
                if md_count > 0:
                    children.append((d, dp, md_count))
    return children

def list_entities_in_dir(dirpath, limit=10):
    """List entity files in a directory."""
    entities = []
    if os.path.isdir(dirpath):
        for f in sorted(os.listdir(dirpath)):
            if f.endswith('.md') and f != 'index.md' and f != 'overview.md':
                name = f.replace('.md', '').replace('-', ' ').title()
                entities.append((f, name))
    return entities[:limit]

def frontmatter_block(tags=None, extra=None):
    """Generate YAML frontmatter."""
    fm = '---\n'
    fm += 'type: concept\n'
    if tags:
        fm += f'tags: [{", ".join(tags)}]\n'
    fm += '---\n\n'
    return fm

changes = []

# ═══════════════════════════════════════════════
# PASS 1: Domain index pages
# ═══════════════════════════════════════════════
print("=== Pass 1: Domain index pages ===")
domain_dirs = []
for d in sorted(os.listdir(WIKI + '/domains')):
    dp = os.path.join(WIKI, 'domains', d)
    if os.path.isdir(dp) and not d.startswith('.'):
        domain_dirs.append((d, dp))

for domain, dp in domain_dirs:
    idx_path = os.path.join(dp, 'index.md')
    info = DOMAIN_INFO.get(domain, {})
    title = info.get('title', domain.replace('-', ' ').title())
    desc = info.get('desc', f'Technologies and patterns in the {domain} domain.')
    
    # Count entities in this domain
    entity_count = count_entities_in_dir(dp)
    
    # Get children (supercategories)
    sc_dir = os.path.join(dp, 'supercategories')
    children = get_children_dirs(sc_dir) if os.path.isdir(sc_dir) else get_children_dirs(dp)
    
    # Build new content
    lines = []
    lines.append(f'# {title}')
    lines.append('')
    lines.append(f'> {desc}')
    lines.append('')
    lines.append(f'**{entity_count} entities** across {len(children)} sub-areas.')
    lines.append('')
    
    # Related domains
    related = info.get('related', [])
    if related:
        lines.append('## Related Domains')
        lines.append('')
        for r in related:
            r_info = DOMAIN_INFO.get(r, {})
            r_title = r_info.get('title', r.replace('-', ' ').title())
            rel_path = f'[[wiki/domains/{r}/index|{r_title}]]'
            relationship = CROSS_DOMAIN_LINKS.get((domain, r), '')
            if relationship:
                lines.append(f'- {rel_path} — {relationship}')
            else:
                lines.append(f'- {rel_path}')
        lines.append('')
    
    # Sub-areas
    if children:
        lines.append('## Sub-Areas')
        lines.append('')
        for child_name, child_path, child_count in children:
            child_title = child_name.replace('-', ' ').title()
            # Find index.md in child
            child_idx = os.path.join(child_path, 'index.md')
            if os.path.exists(child_idx):
                lines.append(f'- [[wiki/domains/{domain}/supercategories/{child_name}/index|{child_title}]] — {child_count} files')
            else:
                lines.append(f'- **{child_title}** — {child_count} files')
        lines.append('')
    
    # Key entities (sample)
    sample_entities = list_entities_in_dir(dp, limit=8)
    if sample_entities:
        lines.append('## Key Entities')
        lines.append('')
        for fname, ename in sample_entities:
            entity_path = f'wiki/domains/{domain}/{fname}'
            lines.append(f'- [[{entity_path.replace(".md", "")}|{ename}]]')
        lines.append('')
    
    new_content = '\n'.join(lines)
    
    # Only write if significantly different (at least 20% change)
    old_content = ''
    if os.path.exists(idx_path):
        with open(idx_path, encoding='utf-8', errors='replace') as f:
            old_content = f.read()
    
    if len(new_content) > len(old_content) * 0.8 or len(old_content) < 100:
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        changes.append(f"domain: {domain} ({len(lines)} lines)")
        print(f"  ✓ {domain}: {entity_count} entities, {len(children)} children, {len(related)} related")

# ═══════════════════════════════════════════════
# PASS 2: Supercategory index pages
# ═══════════════════════════════════════════════
print("\n=== Pass 2: Supercategory index pages ===")
sc_count = 0
for domain, dp in domain_dirs:
    sc_dir = os.path.join(dp, 'supercategories')
    if not os.path.isdir(sc_dir):
        continue
    for sc_name in sorted(os.listdir(sc_dir)):
        sc_path = os.path.join(sc_dir, sc_name)
        if not os.path.isdir(sc_path):
            continue
        idx_path = os.path.join(sc_path, 'index.md')
        
        entity_count = count_entities_in_dir(sc_path)
        children = get_children_dirs(os.path.join(sc_path, 'categories'))
        
        sc_title = sc_name.replace('-', ' ').title()
        domain_title = DOMAIN_INFO.get(domain, {}).get('title', domain.replace('-', ' ').title())
        
        lines = []
        lines.append(f'# {sc_title}')
        lines.append('')
        lines.append(f'Part of [[wiki/domains/{domain}/index|{domain_title}]]. {entity_count} entities.')
        lines.append('')
        
        if children:
            lines.append('## Categories')
            lines.append('')
            for cat_name, cat_path, cat_count in children:
                cat_title = cat_name.replace('-', ' ').title()
                cat_idx = os.path.join(cat_path, 'index.md')
                if os.path.exists(cat_idx):
                    lines.append(f'- [[wiki/domains/{domain}/supercategories/{sc_name}/categories/{cat_name}/index|{cat_title}]] — {cat_count} files')
                else:
                    lines.append(f'- **{cat_title}** — {cat_count} files')
            lines.append('')
        
        # Sibling supercategories
        siblings = [s for s in os.listdir(sc_dir) if s != sc_name and os.path.isdir(os.path.join(sc_dir, s))]
        if siblings:
            lines.append('## See Also')
            lines.append('')
            for sib in siblings:
                sib_title = sib.replace('-', ' ').title()
                lines.append(f'- [[wiki/domains/{domain}/supercategories/{sib}/index|{sib_title}]]')
            lines.append('')
        
        new_content = '\n'.join(lines)
        old_content = ''
        if os.path.exists(idx_path):
            with open(idx_path, encoding='utf-8', errors='replace') as f:
                old_content = f.read()
        
        if len(new_content) > len(old_content) * 0.8 or len(old_content) < 80:
            with open(idx_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            sc_count += 1
            print(f"  ✓ {domain}/{sc_name}: {entity_count} entities, {len(children)} cats")

print(f"  Updated {sc_count} supercategory indexes")

# ═══════════════════════════════════════════════
# PASS 3: Category index pages
# ═══════════════════════════════════════════════
print("\n=== Pass 3: Category index pages ===")
cat_count = 0
for domain, dp in domain_dirs:
    sc_dir = os.path.join(dp, 'supercategories')
    if not os.path.isdir(sc_dir):
        continue
    for sc_name in sorted(os.listdir(sc_dir)):
        sc_path = os.path.join(sc_dir, sc_name)
        cat_dir = os.path.join(sc_path, 'categories')
        if not os.path.isdir(cat_dir):
            continue
        for cat_name in sorted(os.listdir(cat_dir)):
            cat_path = os.path.join(cat_dir, cat_name)
            if not os.path.isdir(cat_path):
                continue
            idx_path = os.path.join(cat_path, 'index.md')
            
            entity_count = count_entities_in_dir(cat_path)
            children = get_children_dirs(os.path.join(cat_path, 'subcategories'))
            
            cat_title = cat_name.replace('-', ' ').title()
            sc_title = sc_name.replace('-', ' ').title()
            domain_title = DOMAIN_INFO.get(domain, {}).get('title', domain.replace('-', ' ').title())
            
            lines = []
            lines.append(f'# {cat_title}')
            lines.append('')
            lines.append(f'Part of [[wiki/domains/{domain}/supercategories/{sc_name}/index|{sc_title}]] › {cat_title}. {entity_count} entities.')
            lines.append('')
            
            if children:
                lines.append('## Sub-Categories')
                lines.append('')
                for subcat_name, subcat_path, subcat_count in children:
                    subcat_title = subcat_name.replace('-', ' ').title()
                    subcat_idx = os.path.join(subcat_path, 'index.md')
                    if os.path.exists(subcat_idx):
                        lines.append(f'- [[wiki/domains/{domain}/supercategories/{sc_name}/categories/{cat_name}/subcategories/{subcat_name}/index|{subcat_title}]] — {subcat_count} files')
                    else:
                        lines.append(f'- **{subcat_title}** — {subcat_count} files')
                lines.append('')
            
            # Direct entities (not in subcategories)
            direct_entities = list_entities_in_dir(cat_path, limit=15)
            if direct_entities:
                lines.append('## Entities')
                lines.append('')
                for fname, ename in direct_entities:
                    entity_path = f'wiki/domains/{domain}/supercategories/{sc_name}/categories/{cat_name}/{fname}'
                    lines.append(f'- [[{entity_path.replace(".md", "")}|{ename}]]')
                lines.append('')
            
            new_content = '\n'.join(lines)
            old_content = ''
            if os.path.exists(idx_path):
                with open(idx_path, encoding='utf-8', errors='replace') as f:
                    old_content = f.read()
            
            if len(new_content) > len(old_content) * 0.8 or len(old_content) < 80:
                with open(idx_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                cat_count += 1

print(f"  Updated {cat_count} category indexes")

# ═══════════════════════════════════════════════
# PASS 4: Subcategory index pages
# ═══════════════════════════════════════════════
print("\n=== Pass 4: Subcategory index pages ===")
subcat_count = 0
for domain, dp in domain_dirs:
    sc_dir = os.path.join(dp, 'supercategories')
    if not os.path.isdir(sc_dir):
        continue
    for sc_name in sorted(os.listdir(sc_dir)):
        sc_path = os.path.join(sc_dir, sc_name)
        cat_dir = os.path.join(sc_path, 'categories')
        if not os.path.isdir(cat_dir):
            continue
        for cat_name in sorted(os.listdir(cat_dir)):
            cat_path = os.path.join(cat_dir, cat_name)
            subcat_dir = os.path.join(cat_path, 'subcategories')
            if not os.path.isdir(subcat_dir):
                continue
            for subcat_name in sorted(os.listdir(subcat_dir)):
                subcat_path = os.path.join(subcat_dir, subcat_name)
                if not os.path.isdir(subcat_path):
                    continue
                idx_path = os.path.join(subcat_path, 'index.md')
                
                entities = list_entities_in_dir(subcat_path, limit=20)
                entity_count = len(entities) + count_entities_in_dir(subcat_path)
                
                subcat_title = subcat_name.replace('-', ' ').title()
                cat_title = cat_name.replace('-', ' ').title()
                sc_title = sc_name.replace('-', ' ').title()
                domain_title = DOMAIN_INFO.get(domain, {}).get('title', domain.replace('-', ' ').title())
                
                lines = []
                lines.append(f'# {subcat_title}')
                lines.append('')
                lines.append(f'Part of [[wiki/domains/{domain}/supercategories/{sc_name}/categories/{cat_name}/index|{cat_title}]] › {subcat_title}. **{entity_count} entities.**')
                lines.append('')
                
                if entities:
                    lines.append('## Entities')
                    lines.append('')
                    for fname, ename in entities:
                        entity_path = f'wiki/domains/{domain}/supercategories/{sc_name}/categories/{cat_name}/subcategories/{subcat_name}/{fname}'
                        lines.append(f'- [[{entity_path.replace(".md", "")}|{ename}]]')
                    if entity_count > 20:
                        lines.append(f'- *...and {entity_count - 20} more*')
                    lines.append('')
                
                # Sibling subcategories
                siblings = [s for s in os.listdir(subcat_dir) if s != subcat_name and os.path.isdir(os.path.join(subcat_dir, s))]
                if siblings:
                    lines.append('## See Also')
                    lines.append('')
                    for sib in siblings:
                        sib_title = sib.replace('-', ' ').title()
                        lines.append(f'- [[wiki/domains/{domain}/supercategories/{sc_name}/categories/{cat_name}/subcategories/{sib}/index|{sib_title}]]')
                    lines.append('')
                
                new_content = '\n'.join(lines)
                old_content = ''
                if os.path.exists(idx_path):
                    with open(idx_path, encoding='utf-8', errors='replace') as f:
                        old_content = f.read()
                
                if len(new_content) > len(old_content) * 0.8 or len(old_content) < 80:
                    with open(idx_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    subcat_count += 1

print(f"  Updated {subcat_count} subcategory indexes")

# ═══════════════════════════════════════════════
# PASS 5: Enrich entity stubs with cross-links
# ═══════════════════════════════════════════════
print("\n=== Pass 5: Entity stubs ===")
entity_count = 0
for domain, dp in domain_dirs:
    sc_dir = os.path.join(dp, 'supercategories')
    if not os.path.isdir(sc_dir):
        continue
    for sc_name in sorted(os.listdir(sc_dir)):
        sc_path = os.path.join(sc_dir, sc_name)
        cat_dir = os.path.join(sc_path, 'categories')
        if not os.path.isdir(cat_dir):
            continue
        for cat_name in sorted(os.listdir(cat_dir)):
            cat_path = os.path.join(cat_dir, cat_name)
            subcat_dir = os.path.join(cat_path, 'subcategories')
            dirs_to_scan = []
            if os.path.isdir(subcat_dir):
                for subcat_name in sorted(os.listdir(subcat_dir)):
                    subcat_path = os.path.join(subcat_dir, subcat_name)
                    if os.path.isdir(subcat_path):
                        dirs_to_scan.append((subcat_path, domain, sc_name, cat_name, subcat_name))
            # Also scan direct entities in category
            dirs_to_scan.append((cat_path, domain, sc_name, cat_name, None))
            
            for ent_dir, dom, sc, cat, subcat in dirs_to_scan:
                for fname in sorted(os.listdir(ent_dir)):
                    if not fname.endswith('.md') or fname in ('index.md', 'overview.md'):
                        continue
                    fpath = os.path.join(ent_dir, fname)
                    
                    with open(fpath, encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    
                    # Skip if already has meaningful content (>300 chars and has wikilinks)
                    existing_links = len(re.findall(r'\[\[', content))
                    if len(content) > 300 and existing_links > 0:
                        continue
                    
                    # Build enriched content
                    entity_name = fname.replace('.md', '').replace('-', ' ').title()
                    cat_title = cat.replace('-', ' ').title() if cat else ''
                    sc_title = sc.replace('-', ' ').title() if sc else ''
                    domain_title = DOMAIN_INFO.get(dom, {}).get('title', dom.replace('-', ' ').title())
                    
                    # Extract existing frontmatter
                    fm_match = re.match(r'^(---\s*\n.*?\n---\s*\n)', content, re.DOTALL)
                    fm = fm_match.group(1) if fm_match else ''
                    
                    # Extract any existing overview text
                    overview_match = re.search(r'## Overview\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
                    existing_overview = overview_match.group(1).strip() if overview_match else ''
                    
                    # Build breadcrumb
                    if subcat:
                        breadcrumb = f'{domain_title} › [[wiki/domains/{dom}/supercategories/{sc}/index|{sc_title}]] › [[wiki/domains/{dom}/supercategories/{sc}/categories/{cat}/index|{cat_title}]] › {entity_name}'
                    elif cat:
                        breadcrumb = f'{domain_title} › [[wiki/domains/{dom}/supercategories/{sc}/index|{sc_title}]] › [[wiki/domains/{dom}/supercategories/{sc}/categories/{cat}/index|{cat_title}]]'
                    else:
                        breadcrumb = f'{domain_title} › [[wiki/domains/{dom}/supercategories/{sc}/index|{sc_title}]]'
                    
                    lines = []
                    if fm:
                        lines.append(fm)
                    
                    lines.append(f'## {entity_name}')
                    lines.append('')
                    if existing_overview:
                        lines.append(existing_overview)
                        lines.append('')
                    lines.append(f'**Domain:** {breadcrumb}')
                    lines.append('')
                    
                    # Add sibling links (other entities in same directory)
                    siblings = [s for s in os.listdir(ent_dir) 
                               if s.endswith('.md') and s != fname and s not in ('index.md', 'overview.md')]
                    if siblings:
                        lines.append('## Related Entities')
                        lines.append('')
                        for sib in siblings[:8]:
                            sib_name = sib.replace('.md', '').replace('-', ' ').title()
                            sib_path = fpath.replace(ent_dir + '/', '').replace(fname, sib).replace('.md', '')
                            # Build relative path
                            sib_rel = os.path.relpath(os.path.join(ent_dir, sib), BUNDLE).replace('.md', '')
                            lines.append(f'- [[{sib_rel}|{sib_name}]]')
                        lines.append('')
                    
                    new_content = '\n'.join(lines)
                    
                    # Only write if we added meaningful content
                    if len(new_content) > len(content) + 50:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        entity_count += 1

print(f"  Enriched {entity_count} entity stubs")

print(f"\n=== Summary ===")
print(f"Domain indexes updated: {len([c for c in changes if c.startswith('domain')])}")
print(f"Supercategory indexes: {sc_count}")
print(f"Category indexes: {cat_count}")
print(f"Subcategory indexes: {subcat_count}")
print(f"Entity stubs enriched: {entity_count}")
