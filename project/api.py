from fastapi import FastAPI
from pydantic import BaseModel

from backend.retrieval import retrieve_chunks
from backend.llm import generate_response
from backend.quiz_generator import generate_quiz

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Tutor API Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    results = retrieve_chunks(request.question)

    retrieved_docs = results["documents"][0]

    context = "\n".join(retrieved_docs)

    answer = generate_response(
        context,
        request.question,
        []
    )

    return {
        "question": request.question,
        "answer": answer
    }


@app.post("/quiz")
def quiz(request: ChatRequest):

    results = retrieve_chunks(request.question)

    retrieved_docs = results["documents"][0]

    context = "\n".join(retrieved_docs)

    quiz_data = generate_quiz(context)

    return {
        "quiz": quiz_data
    }