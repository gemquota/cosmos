#!/usr/bin/env python3
"""VectorSearch + SemanticMemory — wraps mykb's hybrid retriever and embedder.

Provides RSIS3 with semantic search over its accumulated knowledge
using mykb's TF-IDF vector DB, BM25 keyword search, and RRF fusion.
"""

from pathlib import Path
from typing import Optional
from memory_bridge.config import resolve_wiki_path
from memory_bridge.mykb_loader import load_mykb_module


#  ── SemanticMemory ────────────────────────────────────────────

class SemanticMemory:
    """RSIS3's semantic memory — store, retrieve, and search knowledge.

    Wraps mykb's VectorDB + TF-IDF vectorizer + BM25 retriever so RSIS3
    can treat mykb as its long-term semantic store.

    Usage::

        mem = SemanticMemory()
        mem.store("entity-id", "Some text to embed and index")
        results = mem.search("query about something")
        similar = mem.find_similar("entity-id")
    """

    def __init__(self, mykb_wiki: Optional[str | Path] = None):
        wiki_path = Path(mykb_wiki) if mykb_wiki else self._default_wiki()
        self._wiki_path = wiki_path
        self._vdb_path = wiki_path.parent / '.wiki-daemon' / 'vdb'
        self._retriever = None  # lazy-loaded

    # ── retriever (lazy) ─────────────────────────────────────

    @property
    def retriever(self):
        if self._retriever is None:
            r = load_mykb_module("retriever")
            self._retriever = r.load_retriever()
        return self._retriever

    def ensure_indexed(self) -> bool:
        """Ensure the vector DB is built. Returns True if ready."""
        # Check if vector DB exists; if not, run embedder
        if not (self._vdb_path.with_suffix('.npz').exists()):
            self._rebuild_index()
        return self.retriever is not None

    def _rebuild_index(self):
        """Run mykb's embedding pipeline to index all wiki docs."""
        ed = load_mykb_module("embedder")
        print("[memory] Rebuilding mykb vector index…")
        ed.embed_all()
        self._retriever = None  # force reload

    # ── search ───────────────────────────────────────────────

    def search(self, query: str, top_k: int = 20,
               filters: Optional[dict] = None) -> list[dict]:
        """Hybrid semantic + keyword search across all stored knowledge.

        Returns list of ``{id, score, title, type, snippet}`` dicts.
        """
        r = self.retriever
        if r is None:
            return []
        results = r.hybrid_search(query, top_k=top_k, filters=filters or {})
        return [
            {
                'id': item_id,
                'score': round(score, 4),
                'title': meta.get('title', item_id),
                'type': meta.get('type', 'unknown'),
                'snippet': meta.get('description', ''),
            }
            for item_id, score, meta in results
        ]

    def find_similar(self, entity_id: str, top_k: int = 10) -> list[dict]:
        """Find semantically similar entities to a given one."""
        r = self.retriever
        if r is None:
            return []
        results = r.find_similar(entity_id, top_k=top_k)
        return [
            {
                'id': item_id,
                'score': round(score, 4),
                'title': meta.get('title', item_id),
            }
            for item_id, score, meta in results
        ]

    def store(self, doc_id: str, text: str,
              metadata: Optional[dict] = None) -> bool:
        """Store a document into mykb's vector DB.

        The document is also written as a wiki entity page so it
        appears in future rebuilds.
        """
        from memory_bridge.wiki_writer import WikiWriter
        writer = WikiWriter(self._wiki_path)
        writer.write_entity(
            entity_id=doc_id,
            title=(metadata or {}).get('title', doc_id),
            description=(metadata or {}).get('description', ''),
            tags=(metadata or {}).get('tags', []),
            body=text,
        )
        # Rebuild vector DB incrementally
        vdb = load_mykb_module("vectordb")
        ed = load_mykb_module("embedder")
        vectorizer = ed.TfidfVectorizer(max_features=3000)

        # Load existing, add new doc, re-save
        existing = vdb.VectorDB()
        if self._vdb_path.with_suffix('.npz').exists():
            existing.load(str(self._vdb_path))
            vectorizer.load(str(self._vdb_path) + '_tfidf.json')

        vec = vectorizer.transform(text)
        existing.add(doc_id, vec, metadata or {})
        existing.persist(str(self._vdb_path))
        vectorizer.save(str(self._vdb_path) + '_tfidf.json')
        self._retriever = None  # force reload on next query
        return True

    def store_batch(self, docs: list[tuple[str, str, dict]]) -> int:
        """Store multiple documents at once.

        Each tuple is ``(doc_id, text, metadata_dict)``.
        """
        count = 0
        for doc_id, text, metadata in docs:
            if self.store(doc_id, text, metadata):
                count += 1
        return count

    # ── count ────────────────────────────────────────────────

    def count(self) -> int:
        """Number of vectors currently indexed."""
        vdb = load_mykb_module("vectordb")
        db = vdb.VectorDB()
        if self._vdb_path.with_suffix('.npz').exists():
            db.load(str(self._vdb_path))
        return db.count()

    @staticmethod
    def _default_wiki() -> Path:
        return resolve_wiki_path()
