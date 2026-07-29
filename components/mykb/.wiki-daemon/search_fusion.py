#!/usr/bin/env python3
"""Hybrid Search Engine (Epic 1) + Structure-Aware Chunking (Epic 2)

Provides:
  - Structure-aware markdown chunking at header boundaries
  - Code block extraction with AST metadata
  - BM25 sparse index
  - TF-IDF dense vector index (cosine similarity)
  - Reciprocal Rank Fusion (RRF) of both result sets
  - Batch ingestion and unified search API

Usage:
  python3 .wiki-daemon/search_fusion.py build-index   # Build/rebuild indices from wiki files
  python3 .wiki-daemon/search_fusion.py query <text>   # Search from CLI
  python3 .wiki-daemon/search_fusion.py serve          # Start API server (port 8850)
"""
import os, re, sys, json, math
from collections import defaultdict, Counter
from datetime import datetime

import numpy as np
from rank_bm25 import BM25Okapi

BUNDLE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_DIR = os.path.join(BUNDLE, '.wiki-daemon')

RFF_K = 60  # RRF smoothing constant
MAX_CHUNK_SIZE = 4000  # max chars per chunk (fallback for very long sections)

# ── Epic 2: Structure-Aware Chunking ─────────────────────────────

def chunk_markdown(text, source_path):
    """Split markdown at #, ##, ### headers. Returns list of chunks with metadata."""
    chunks = []
    lines = text.split('\n')
    
    current_header = None
    current_header_level = 0
    current_lines = []
    parent_headers = []  # stack of parent header titles
    
    def flush():
        if not current_lines:
            return
        body = '\n'.join(current_lines).strip()
        if not body:
            return
        
        # Build header chain
        header_chain = ' > '.join(h for h in parent_headers if h)
        
        # Detect code blocks
        code_blocks = []
        in_code = False
        code_lang = ''
        code_lines = []
        for line in current_lines:
            if line.startswith('```'):
                if in_code:
                    code_blocks.append({'language': code_lang, 'code': '\n'.join(code_lines)})
                    code_lines = []
                    in_code = False
                else:
                    code_lang = line[3:].strip()
                    in_code = True
            elif in_code:
                code_lines.append(line)
        
        chunk = {
            'source': source_path,
            'header': current_header or '',
            'header_chain': header_chain,
            'header_level': current_header_level,
            'body': body[:MAX_CHUNK_SIZE],
            'size': len(body),
            'has_code': len(code_blocks) > 0,
            'code_blocks': code_blocks[:3],  # cap at 3 blocks per chunk
            'signatures': extract_signatures(code_blocks),
        }
        chunks.append(chunk)
    
    for line in lines:
        header_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if header_match:
            flush()
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            
            # Update parent header stack
            while parent_headers and len(parent_headers) >= level:
                parent_headers.pop()
            parent_headers.append(title)
            
            current_header = title
            current_header_level = level
            current_lines = [line]
        else:
            current_lines.append(line)
    
    flush()
    return chunks

def extract_signatures(code_blocks):
    """Extract function/class signatures from code blocks."""
    sigs = []
    for block in code_blocks:
        code = block['code']
        # Python functions
        for m in re.finditer(r'^\s*(?:async\s+)?def\s+(\w+)\s*\(', code, re.MULTILINE):
            sigs.append({'type': 'function', 'name': m.group(1), 'language': 'python'})
        # Python classes
        for m in re.finditer(r'^\s*class\s+(\w+)', code, re.MULTILINE):
            sigs.append({'type': 'class', 'name': m.group(1), 'language': 'python'})
        # JS functions
        for m in re.finditer(r'(?:function|const)\s+(\w+)\s*(?:=|\(|\s*:\s*(?:async\s+)?\()', code, re.MULTILINE):
            sigs.append({'type': 'function', 'name': m.group(1), 'language': 'javascript'})
        # JS classes
        for m in re.finditer(r'^\s*class\s+(\w+)', code, re.MULTILINE):
            sigs.append({'type': 'class', 'name': m.group(1), 'language': 'javascript'})
    return sigs

def build_chunks_from_wiki():
    """Walk wiki directory and chunk all markdown files."""
    all_chunks = []
    file_count = 0
    
    for root, dirs, files in os.walk(BUNDLE):
        # Skip non-content dirs
        skip = {'.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian', '.wiki-daemon', 'hooks'}
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith('.')]
        
        for fn in files:
            if not fn.endswith('.md'):
                continue
            # Skip export files
            if fn in ('mykb-code.md', 'mykb-content.md', 'COMPREHENSIVE_AUDIT.md', 'build-export.py'):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, BUNDLE)
            try:
                with open(path, encoding='utf-8', errors='replace') as f:
                    text = f.read()
            except:
                continue
            
            # Strip frontmatter
            text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL)
            
            chunks = chunk_markdown(text, rel)
            all_chunks.extend(chunks)
            file_count += 1
    
    return all_chunks, file_count

# ── Epic 1: BM25 + Vector Index + RRF ────────────────────────────

def tokenize(text):
    """Tokenize text for BM25 and vector index."""
    # Strip markdown syntax
    text = re.sub(r'[#*_`~\[\]()>|]', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = re.findall(r'[a-zA-Z][a-zA-Z0-9_]{1,}', text.lower())
    return tokens

def build_indices(chunks):
    """Build BM25 sparse index and TF-IDF dense vectors."""
    print(f"  Tokenizing {len(chunks)} chunks...")
    
    # Tokenize all chunks
    chunk_texts = []
    for c in chunks:
        # Weighted text: header chain + body
        text = f"{c['header_chain']} {' '.join(s['name'] for s in c['signatures'])} {c['body']}"
        chunk_texts.append(text)
    
    tokens_list = [tokenize(t) for t in chunk_texts]
    
    # ── BM25 Index ──
    print("  Building BM25 index...")
    bm25 = BM25Okapi(tokens_list)
    
    # ── TF-IDF Dense Vectors ──
    print("  Building TF-IDF vector index...")
    # Build vocabulary from all tokens
    vocab = {}
    for tokens in tokens_list:
        for t in tokens:
            if t not in vocab:
                vocab[t] = len(vocab)
    
    vocab_size = len(vocab)
    num_docs = len(chunks)
    
    # Compute IDF
    doc_freq = Counter()
    for tokens in tokens_list:
        for t in set(tokens):
            doc_freq[t] += 1
    
    idf = {t: math.log((num_docs + 1) / (freq + 1)) + 1 for t, freq in doc_freq.items()}
    
    # Build TF-IDF vectors as dense numpy array
    vectors = np.zeros((num_docs, min(vocab_size, 3000)), dtype=np.float32)  # cap vocab at 5000
    
    for i, tokens in enumerate(tokens_list):
        tf = Counter(tokens)
        doc_len = len(tokens)
        for t, count in tf.items():
            if t in vocab and vocab[t] < 3000:
                tf_val = count / max(doc_len, 1)
                vectors[i, vocab[t]] = tf_val * idf.get(t, 1)
    
    # Normalize vectors to unit length
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1
    vectors = vectors / norms
    
    index_data = {
        'chunks': chunks,
        'bm25': bm25,
        'vectors': vectors,
        'vocab': {k: v for k, v in vocab.items() if v < 3000},
        'idf': idf,
        'num_chunks': num_docs,
        'vocab_size': min(vocab_size, 3000),
        'built_at': datetime.now().isoformat(),
    }
    
    return index_data

def save_index(index_data):
    """Serialize index to disk."""
    chunks_path = os.path.join(INDEX_DIR, 'search_chunks.json')
    meta_path = os.path.join(INDEX_DIR, 'search_meta.json')
    vectors_path = os.path.join(INDEX_DIR, 'search_vectors.npy')
    
    # Save chunks as JSON
    with open(chunks_path, 'w') as f:
        json.dump(index_data['chunks'], f)
    
    # Save vectors as numpy array
    np.save(vectors_path, index_data['vectors'])
    
    # Save metadata (BM25 params, vocab)
    meta = {
        'num_chunks': index_data['num_chunks'],
        'vocab_size': index_data['vocab_size'],
        'vocab': index_data['vocab'],
        'idf': index_data['idf'],
        'built_at': index_data['built_at'],
    }
    with open(meta_path, 'w') as f:
        json.dump(meta, f)
    
    print(f"  Saved: {len(index_data['chunks'])} chunks")
    print(f"  Vectors: {index_data['vectors'].shape}")
    print(f"  Size: {vectors_path} ({os.path.getsize(vectors_path)/1024/1024:.1f}MB)")

def load_index():
    """Load index from disk (leaving BM25 to be rebuilt on demand)."""
    chunks_path = os.path.join(INDEX_DIR, 'search_chunks.json')
    meta_path = os.path.join(INDEX_DIR, 'search_meta.json')
    vectors_path = os.path.join(INDEX_DIR, 'search_vectors.npy')
    
    if not all(os.path.exists(p) for p in [chunks_path, meta_path, vectors_path]):
        return None
    
    with open(chunks_path) as f:
        chunks = json.load(f)
    with open(meta_path) as f:
        meta = json.load(f)
    vectors = np.load(vectors_path)
    
    # Rebuild BM25 from saved chunks
    tokens_list = [tokenize(f"{c['header_chain']} {' '.join(s['name'] for s in c['signatures'])} {c['body']}") for c in chunks]
    bm25 = BM25Okapi(tokens_list)
    
    return {
        'chunks': chunks,
        'bm25': bm25,
        'vectors': vectors,
        'vocab': meta['vocab'],
        'idf': meta['idf'],
        'num_chunks': meta['num_chunks'],
        'built_at': meta['built_at'],
    }

# ── RRF Fusion ────────────────────────────────────────────────────

def rrf_fusion(dense_results, sparse_results, k=RFF_K, top_n=30):
    """Fuse two ranked result lists using Reciprocal Rank Fusion."""
    # Build score maps
    scores = defaultdict(float)
    seen = {}
    
    for rank, (idx, score) in enumerate(dense_results):
        scores[idx] += 1.0 / (k + rank + 1)
        seen[idx] = scores[idx]
    
    for rank, (idx, score) in enumerate(sparse_results):
        scores[idx] += 1.0 / (k + rank + 1)
        if idx not in seen:
            pass  # Only appears in sparse results
    
    # Sort by fused score
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    return ranked[:top_n]

# ── Query Orchestrator ────────────────────────────────────────────

def search_query(index_data, query_text, top_n=30):
    """Run hybrid search: dense + sparse → RRF fusion."""
    query_tokens = tokenize(query_text)
    if not query_tokens:
        return []
    
    # ── Sparse: BM25 ──
    bm25_scores = index_data['bm25'].get_scores(query_tokens)
    sparse_results = [(i, bm25_scores[i]) for i in np.argsort(bm25_scores)[-top_n*2:][::-1]]
    
    # ── Dense: TF-IDF cosine similarity ──
    # Build query vector
    query_vec = np.zeros(index_data['vectors'].shape[1], dtype=np.float32)
    vocab = index_data['vocab']
    idf = index_data['idf']
    tf = Counter(query_tokens)
    for t, count in tf.items():
        if t in vocab and vocab[t] < index_data['vectors'].shape[1]:
            query_vec[vocab[t]] = (count / len(query_tokens)) * idf.get(t, 1)
    
    # Normalize query vector
    norm = np.linalg.norm(query_vec)
    if norm > 0:
        query_vec = query_vec / norm
    
    # Cosine similarity with all document vectors
    similarities = index_data['vectors'] @ query_vec
    dense_results = [(i, float(similarities[i])) for i in np.argsort(similarities)[-top_n*2:][::-1]]
    
    # ── RRF Fusion ──
    fused = rrf_fusion(dense_results, sparse_results, top_n=top_n)
    
    # Build response
    results = []
    for idx, rrf_score in fused:
        chunk = index_data['chunks'][idx]
        results.append({
            'rank': len(results) + 1,
            'score': round(rrf_score, 4),
            'source': chunk['source'],
            'header': chunk['header'],
            'header_chain': chunk['header_chain'],
            'snippet': chunk['body'][:300],
            'has_code': chunk['has_code'],
            'signatures': chunk['signatures'],
            'size': chunk['size'],
        })
    
    return results

# ── CLI Commands ──────────────────────────────────────────────────

def cmd_build_index():
    print("Building structure-aware chunks from wiki...")
    chunks, file_count = build_chunks_from_wiki()
    print(f"  {file_count} files → {len(chunks)} chunks")
    
    print("Building hybrid search indices...")
    index_data = build_indices(chunks)
    
    print("Saving to disk...")
    save_index(index_data)
    print("Done!")

def cmd_query(query_text):
    index_data = load_index()
    if not index_data:
        print("No index found. Run 'build-index' first.")
        return
    
    results = search_query(index_data, query_text)
    print(f"\nQuery: '{query_text}'")
    print(f"Results: {len(results)}\n")
    for r in results[:10]:
        sigs = ', '.join(f"{s['name']}" for s in r['signatures'][:2]) if r['signatures'] else ''
        sig_str = f" [{sigs}]" if sigs else ''
        print(f"  #{r['rank']} (score={r['score']}) {r['source']} → {r['header']}{sig_str}")
        print(f"    {r['snippet'][:120]}...")
        print()

def cmd_serve():
    """Start a lightweight API server on port 8850."""
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import urllib.parse
    
    index_data = load_index()
    if not index_data:
        print("No index found. Run 'build-index' first.")
        return
    
    port = int(sys.argv[3]) if len(sys.argv) > 3 else 8850
    
    class SearchHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode() if length > 0 else '{}'
            try:
                params = json.loads(body)
            except:
                params = {}
            
            q = params.get('q', params.get('query', ''))
            top_n = int(params.get('top_n', 30))
            
            results = search_query(index_data, q, top_n=top_n) if q else []
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'query': q, 'results': results, 'total': len(results)}).encode())
        
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            
            if parsed.path == '/api/v2/search/hybrid':
                q = params.get('q', [''])[0]
                top_n = int(params.get('top_n', [30])[0])
                results = search_query(index_data, q, top_n=top_n) if q else []
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'query': q, 'results': results, 'total': len(results)}).encode())
            elif parsed.path == '/api/v2/search/stats':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                stats = {
                    'chunks': index_data['num_chunks'],
                    'vocab_size': index_data['vectors'].shape[1],
                    'index_built': index_data['built_at'],
                }
                self.wfile.write(json.dumps(stats).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'{"error":"not_found"}')
        
        def log_message(self, format, *args):
            pass
    
    print(f"Search API server on http://localhost:{port}")
    server = HTTPServer(('', port), SearchHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == 'build-index':
        cmd_build_index()
    elif cmd == 'query':
        if len(sys.argv) < 3:
            print("Usage: search_fusion.py query <text>")
            sys.exit(1)
        cmd_query(' '.join(sys.argv[2:]))
    elif cmd == 'serve':
        cmd_serve()
    else:
        print(f"Unknown command: {cmd}")
