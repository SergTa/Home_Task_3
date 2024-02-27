from fastapi.testclient import TestClient  # Импорт тест - клиента
from main_translater import app  # Импорт объекта арр из файла main

client = TestClient(app)  # Создание клиента тестирования


def test_read_main():  # Функция проверки ответа на гет - запрос в корне
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_1():  # Функция проверки ответа на пост - запрос варианта
    response = client.post(
        "/predict/",
        json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == 'Я люблю машинное обучение!'


def test_predict_2():  # Функция проверки ответа на пост - запрос друг варианта
    response = client.post("/predict/",
                           json={"text": "We hate testing!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == 'Мы ненавидим тесты!'
