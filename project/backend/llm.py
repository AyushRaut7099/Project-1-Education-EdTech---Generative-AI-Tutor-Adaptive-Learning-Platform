# Question
# ↓
# Retrieve Relevant Chunks
# ↓
# Create Prompt
# ↓
# Send to Model
# ↓
# Generate Final Answer
from openai import OpenAI # Importing the OpenAI client from the openai library to interact with the model
from dotenv import load_dotenv # Importing the load_dotenv function from the dotenv library to load environment variables from a .env file
import os

load_dotenv()
client = OpenAI( # Initializing the OpenAI client with the API key and base URL for the OpenRouter API
    api_key=os.getenv("OPENROUTER_API_KEY"), # Retrieving the API key from environment variables
    base_url="https://openrouter.ai/api/v1"
)
def generate_response(context, question, chat_history): # Defining a function to generate a response using the model, taking context and question as input
    prompt = f"""
    You are an expert tutor.
    Use ONLY the context below to answer the question.
    Use can use the chat history for reference but do not include it in the answer.
    If answer is not present in context, say:
    "Answer not found in uploaded document."
    
    Previous Conversation:
    {chat_history}

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content