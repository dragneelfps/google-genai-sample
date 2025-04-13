import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()

print("Python verson:", sys.version)

client = genai.Client(api_key=os.getenv("API_KEY"))

res = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        {"role": "user", "parts": [{"text": "who are you?"}]}
    ],
    config={
        'candidate_count': 1,
        'temperature': 0.2,
    })

print(res.text)