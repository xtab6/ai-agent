import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.freemodel.dev/v1/chat/completions"

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "free-model",
        "messages": [
            {"role": "system", "content": "Kamu adalah AI assistant."},
            {"role": "user", "content": req.message}
        ]
    }

    r = requests.post(API_URL, json=payload, headers=headers)

    if r.status_code == 200:
        data = r.json()
        return {
            "reply": data["choices"][0]["message"]["content"]
        }

    return {"error": r.text}
