from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

API_KEY = os.getenv("API_KEY")

API_URL = "https://api.freemodel.dev/v1/chat/completions"

class ChatRequest(BaseModel):
    messages: list

@app.post("/chat")
def chat(req: ChatRequest):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": req.messages
    }

    r = requests.post(
        API_URL,
        json=payload,
        headers=headers
    )

    data = r.json()

    return {
        "reply":
            data["choices"][0]["message"]["content"]
    }
