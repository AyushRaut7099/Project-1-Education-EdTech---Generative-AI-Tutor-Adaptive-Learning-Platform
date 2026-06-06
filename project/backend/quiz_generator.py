from openai import OpenAI# for using OpenRouterAPI
from dotenv import load_dotenv#loading .env file to get the API key stored in .env file
import os #it is used here for accessing environment variables, in this case, the API key for OpenRouter stored in .env file
import json# for parsing the JSON response from the OpenRouter API

# Load environment variables from .env file
load_dotenv()

# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),# Access the API key from environment variables
    base_url="https://openrouter.ai/api/v1"#base url is for making API requests to OpenRouter
)


def generate_quiz(context): #function to generate quiz from the context retrieved from VectorDB
    """
    Generates 5 MCQs from the provided context.
    Returns quiz data in JSON format.
    """

    prompt = f"""
    You are an expert tutor.
    Use ONLY the context given below.
    Generate exactly 5 multiple-choice questions.

    Each question must contain:
    - question
    - optionA
    - optionB
    - optionC
    - optionD
    - answer
    - explanation

    Return ONLY valid JSON.

    Example format:

    [
        {{
            "question": "What is Machine Learning?",
            "optionA": "Database",
            "optionB": "Subset of AI",
            "optionC": "Programming Language",
            "optionD": "Network Protocol",
            "answer": "B",
            "explanation": "Machine Learning is a subset of AI."
        }}
    ]

    Context:
    {context}
    """

    response = client.chat.completions.create( # Making a request to OpenRouter API to generate quiz based on the provided context and prompt
        model="openai/gpt-3.5-turbo", # Using the GPT-3.5-turbo model for generating quiz
        messages=[ #
            {
                "role": "user",# The role of the message is set to "user" to indicate that this message is coming from the user (our application) to the AI model. It helps the model understand the context of the conversation and generate an appropriate response.
                "content": prompt
            }
        ]
    )

    quiz_text = response.choices[0].message.content # Extracting the generated quiz text from the API response

    # Convert JSON string into Python list
    #what is the meaning of parsing the JSON response? -- it means converting the JSON string received from the API into a Python data structure (like a list of dictionaries) that we can easily work with in our code.
    quiz_data = json.loads(quiz_text) #json loads is used to parse the JSON string (quiz_text) into a Python list of dictionaries (quiz_data) that we can use in our application.
#
    return quiz_data # Return the generated quiz data in JSON format