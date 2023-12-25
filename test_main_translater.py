from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_1():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'Я люблю машинное обучение!'


def test_predict_2():
    response = client.post("/predict/",
                           json={"text": "We hate testing!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'Мы ненавидим тестирование!'
