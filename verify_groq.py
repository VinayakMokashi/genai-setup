from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # current small/fast model (replaces deprecated llama3-8b-8192)
    messages=[
        {"role": "user", "content": "Say hello world"}
    ]
)

print(response.choices[0].message.content)
