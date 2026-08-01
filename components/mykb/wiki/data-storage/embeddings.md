---
type: "concept"
title: "Embeddings"
description: "Dense vector representations that capture semantic meaning of tokens, texts, or entities"
tags: ["embeddings", "representation", "semantic", "vector", "nlp"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Word_embedding"]
---

# Embeddings

## Summary
Embeddings map words, sentences, or documents to dense vectors such that similar meanings sit close together in vector space. They are the foundation of semantic search, clustering, and RAG because similarity is computed geometrically. mykb's embedding pipeline produces vectors for notes so RSIS3 can recall related memories.

## Details
- **Idea** — instead of sparse one-hot words, each token gets a learned fixed-length vector; 'king' and 'queen' are near neighbours under classic word embeddings.
- **Generations** — static word embeddings (word2vec, GloVe) give one vector per word; contextual models (BERT-family, sentence-transformers) produce vectors that depend on surrounding text.
- **Text vs entity** — sentence embeddings average or transform token representations; graph embeddings (node2vec) vectorize nodes of a knowledge graph.
- **Similarity** — cosine similarity is the default metric because it is scale-invariant and fast at high dimensions.
- **Worked example** — chunk a note, run it through a sentence-transformer, store the vector in FAISS, then query with another note's embedding to surface semantically related memories.
- **Caveats** — embeddings capture statistical co-occurrence, not verified facts; provenance and metadata filters still matter.

## Related
- [[wiki/meta-learning/word2vec|Word2Vec]] — the canonical static word embedding method
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — models that embed whole sentences and documents
- [[wiki/data-storage/vector-databases|Vector Databases]] — where embedding vectors are stored and searched
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the standard distance for comparing embeddings
- [[wiki/data-storage/semantic-search|Semantic Search]] — the application embeddings enable
- [[wiki/meta-learning/embedding-alignment|Embedding Alignment]] — mapping embeddings across spaces or languages
- [[wiki/memory/README|Memory Layer]] — the layer embedding recall serves in mykb
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — evaluates embedding choices for mykb
