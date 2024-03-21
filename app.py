from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text: str

app = FastAPI()

instruct_model = pipeline('text2text-generation', model='mistralai/Mistral-7B-Instruct-v0.2')

@app.post("/generate")
def generate(item: Item):
    try:
        result = instruct_model(item.text)
        return {"generated_text": result[0]['generated_text']}
    except Exception as e:
        return {"error": str(e)}