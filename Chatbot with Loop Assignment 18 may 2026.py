from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyBpULzkHKdlQxkaMf3eb-UDNFHQ1-NrfNY")

config = types.GenerateContentConfig(
    temperature=0.7,
    top_p=0.9,
    top_k=40,
)

while True:

    user = input("You: ")
    if user.lower() == "bye":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user,
        config=config
    )

    print("Bot:", response.text)