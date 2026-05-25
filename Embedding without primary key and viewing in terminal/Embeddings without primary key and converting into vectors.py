# Before installing we need to install the SentenceTransformer so that we can use it to convert text to number(vector)
# Here we're veiwing result in terminal only
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')#pretained model

# Some sample texts
texts = [
    "I love playing cricket",
    "Artificial Intelligence is powerful",
    "Dogs are loyal animals"
]

# Convert text into embeddings(vectors)
embeddings = model.encode(texts)#converting texts into numbers(vectors)

# Print vectors
for i, embedding in enumerate(embeddings):
    print(f"\nText: {texts[i]}")
    print(f"Vector Length: {len(embedding)}")
    print("First 10 vector values:")
    print(embedding[:10])