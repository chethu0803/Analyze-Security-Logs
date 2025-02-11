from fastapi import FastAPI
from groq import Groq
import os
from dotenv import load_dotenv

app=FastAPI()

load_dotenv()

client = Groq(
    api_key=os.environ.get("API_KEY"),
)

@app.post("/analyze")
async def analyze(logs:str):
  response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Find the potential issues or suggestions in the following logs:\n{logs}",
        }
    ],
    model="llama-3.3-70b-versatile",
  )

  return {"response":response.choices[0].message.content}