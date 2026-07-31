#!/usr/bin/env python3
"""Build hierarchical wiki tree JSON & copy markdown files for the dashboard.

Outputs:
  /dev/codex/dashboards/wiki-tree.json    — tree with previews
  /dev/codex/dashboards/wiki-content/     — mirrored wiki .md files for static serving
"""
import os, re, json, shutil

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wiki')
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codex', 'dashboards')
OUT_JSON = os.path.join(OUT_DIR, 'wiki-tree.json')
OUT_CONTENT = os.path.join(OUT_DIR, 'wiki-content')

def extract_frontmatter(text):
    """Extract title, type, tags from YAML frontmatter."""
    result = {'title': None, 'type': None, 'tags': []}
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', text, re.DOTALL)
    if m:
        fm = m.group(1)
        t = re.search(r'^title:\s*"([^"]+)"', fm, re.MULTILINE)
        if t:
            result['title'] = t.group(1)
        typ = re.search(r'^type:\s*"([^"]+)"', fm, re.MULTILINE)
        if typ:
            result['type'] = typ.group(1)
        tags = re.search(r'^tags:\s*\[(.*?)\]', fm, re.DOTALL)
        if tags:
            parsed = re.findall(r'"([^"]+)"', tags.group(1))
            if parsed:
                result['tags'] = parsed
    return result

def count_files_in_entries(entries):
    """Count total files in a list of entries."""
    count = 0
    for e in entries:
        if e['type'] == 'file':
            count += 1
        elif e['type'] == 'dir':
            count += count_files_in_entries(e.get('children', []))
    return count

def walk_tree(dir_path):
    """Walk directory and build nested dict tree."""
    entries = []
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return entries

    for item in items:
        if item.startswith('.') or item == '__pycache__':
            continue
        full = os.path.join(dir_path, item)
        if os.path.isdir(full):
            children = walk_tree(full)
            fc = count_files_in_entries(children)
            if children:
                entries.append({
                    'type': 'dir',
                    'name': item,
                    'children': children,
                    'count': fc
                })
        elif item.endswith('.md'):
            rel = os.path.relpath(full, WIKI)
            try:
                with open(full, 'r', encoding='utf-8', errors='replace') as f:
                    text = f.read()
            except:
                text = ''
            
            fm = extract_frontmatter(text)
            preview = text.strip() if text else ''
            preview = re.sub(r'^---\n.*?\n(?:---|\.\.\.)', '', preview, flags=re.DOTALL).strip()
            preview = preview[:300]
            
            entries.append({
                'type': 'file',
                'name': item,
                'path': rel,
                'title': fm['title'] or item.replace('.md', '').replace('-', ' ').title(),
                'doc_type': fm['type'] or 'doc',
                'tags': fm['tags'],
                'preview': preview,
                'size': os.path.getsize(full)
            })
    
    return entries

# Build the full tree
tree = walk_tree(WIKI)

# Get all domains at top level
domains = []
for entry in tree:
    if entry['type'] == 'dir':
        domains.append(entry['name'])

# Build stats
total_files = count_files_in_entries(tree)
total_dirs = len(domains)

data = {
    'name': 'wiki',
    'type': 'dir',
    'children': tree,
    'stats': {
        'total_files': total_files,
        'total_domains': total_dirs,
        'domains': sorted(domains)
    }
}

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1, ensure_ascii=False)

json_size = os.path.getsize(OUT_JSON) / 1024

# Copy wiki content files for static serving
content_dir = OUT_CONTENT
if os.path.exists(content_dir):
    shutil.rmtree(content_dir)

copied = 0
for root, dirs, files in os.walk(WIKI):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
    for fn in files:
        if not fn.endswith('.md'):
            continue
        src = os.path.join(root, fn)
        rel = os.path.relpath(src, WIKI)
        dst = os.path.join(content_dir, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1

print(f"Built wiki tree: {total_files} files in {total_dirs} domains")
print(f"  JSON: {OUT_JSON} ({json_size:.1f} KB)")
print(f"  Content: {content_dir} ({copied} files)")
