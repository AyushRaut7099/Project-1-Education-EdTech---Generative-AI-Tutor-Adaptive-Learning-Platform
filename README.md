# Embeddings and Chroma DB

## Embeddings
Embeddings convert text into vector numbers so AI can understand meaning.

Example:
"Dog" → [0.12, -0.45, 0.88]

Similar texts produce similar vectors.

## Libraries Used
### chromadb
Used to store vectors in vector database.

Install:
pip install chromadb

### sentence-transformers
Used to generate embeddings from text.

Install:
pip install sentence-transformers

## Model Used
all-MiniLM-L6-v2

## Workflow

Text → Embedding → Vector → Store in Chroma DB