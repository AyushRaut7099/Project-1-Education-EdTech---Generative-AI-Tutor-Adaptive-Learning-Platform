#Before using ChromaDB we need to install the chromadb using pip install chromadb

import chromadb
from sentence_transformers import SentenceTransformer 

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2') #pretrained AI model for converting text to vector

# This automatically creates "chroma_db" folder using path provided by us
client = chromadb.PersistentClient(path="E:\Embeddings 0th\Embedding without primary key and viewing in ChromaDB./chroma_db")

# Create collection
collection = client.create_collection(name="my_collection")

# texts that will convert from text to vecotr and stored in chromadb
texts = [
    "I love cricket",
    "Artificial Intelligence is amazing",
    "Dogs are loyal animals"
]

# primary key used to identification
ids = ["id1", "id2", "id3"]

# converting texts into vectors(numbers)
embeddings = model.encode(texts).tolist()

# Store data into Chroma DB
collection.add(
    ids=ids,
    documents=texts,
    embeddings=embeddings
)

print("Data stored successfully in Chroma DB!")