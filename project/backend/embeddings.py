from sentence_transformers import SentenceTransformer #for converting tezt into vectors(numbers)
model = SentenceTransformer('all-MiniLM-L6-v2') #pretained model for converting  text into numbers(vectors)
def get_embedding(text): #function to get the embedding vector for a given text chunk
    embedding = model.encode(text) #converting the text chunk into a vector using the model
    return embedding.tolist() 