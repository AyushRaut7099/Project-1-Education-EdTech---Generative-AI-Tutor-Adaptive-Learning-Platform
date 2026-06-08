from fastapi import FastAPI
from backend.retrieval import retrieve_chunks
from backend.llm import generate_response

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI is working"}


@app.post("/chat")
def chat(question: str):

    # Retrieve relevant chunks from ChromaDB
    results = retrieve_chunks(question)

    # Extract retrieved documents
    retrieved_docs = results["documents"][0]

    # Create context
    context = "\n".join(retrieved_docs)

    # Generate answer
    answer = generate_response(
        context,
        question,
        []
    )

    # Return JSON response
    return {
        "answer": answer
    }