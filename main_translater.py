from fastapi import FastAPI   #Импорт fastapi 
from transformers import pipeline  #импорт пайплайн обращения к Hugg Face
from pydantic import BaseModel    # импорт ограничителя ввода данных

class Item(BaseModel):   # ограничение ввода данных - только строка
    text: str


app = FastAPI()   # присвоение переменной класса FastAPI
translator = pipeline(task = 'translation', #вызов задачи и модели из библ
    model = 'Helsinki-NLP/opus-mt-en-ru')


@app.get("/")  # Что делать при обращении в корень


def root():
    return {"message": "Hello World"}


@app.post("/predict/")  # Что делать при обращении в каталог predict


def predict(item: Item):
    return translator (item.text )[0]
