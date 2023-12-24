from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item (BaseModel):
    text: str

app = FastAPI() #Создаем объект app
translator = pipeline ('translation',"Helsinki-NLP/opus-mt-en-ru")

@app.get ("/")
def root ():
    return {"Message": "Translator is ready"}

@app.post ("/predict/")
def predict (item, Item):
    return translator (item.text)[0]


