import os
from dotenv import load_dotenv
load_dotenv()

from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
response = client.chat.completions(
    model="groq/qwen2-32b",
    messages=[{"role":"user","content":"explain LLM in 20 words only"}]
)
print(response.choices[0].message.content)
