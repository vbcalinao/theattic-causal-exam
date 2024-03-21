from fastapi import FastAPI
from pydantic import BaseModel
import requests

class Item(BaseModel):
    text: str

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.post("/generate")
def generate(item: Item):
    try:
        result = query({"inputs": item.text})
        return {"generated_text": result['generated_text']}
    except Exception as e:
        return {"error": str(e)}