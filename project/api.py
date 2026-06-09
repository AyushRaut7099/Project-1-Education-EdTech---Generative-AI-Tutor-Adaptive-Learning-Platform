from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI is working"
    }
@app.post("/chat")
def chat(question: str):

    return {
        "question_received": question,
        "status": "success"
    }