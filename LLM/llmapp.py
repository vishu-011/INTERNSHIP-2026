from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=API_KEY)
result = client.models.generate_content(model="gemini-3.5-flash", contents="explain LLM in 20 words only")
print(result.text)
