from fastapi.testclient import TestClient
from engine_db import check_db
from main import app


client = TestClient(app)
check_db()


def test_not_found_template() -> None:
    "Тест должен проверяет что такой шаблон не найден"

    request_data = {
        "name": "Pasha",
        "address": "Moscow",
        "car": "Audi"
    }
    response_data = {"Error": "The template was not found"}

    response = client.post("/get_form", json=request_data)
    
    assert response.status_code == 200
    assert response.json() == response_data
    print(f"status = {response.status_code}\njson={response.json()}")
    

def test_template_user() -> None:
    "Тест проверяет шаблон User"

    request_data = {
        "name": "Pasha",
        "phone": "+7 918 640 20 20",
        "date": "20.20.2001",
        "email": "pasha_mayskiy@mail.ru",
        "address": "Moscow"
    }
    response_data = {"Template": "User"}
    
    response = client.post("/get_form", json=request_data)

    assert response.status_code == 200
    assert response.json() == response_data
    print(f"status = {response.status_code}\njson={response.json()}")
    
    

def test_template_email() -> None:
    "Тест проверяет шаблон Email"
    
    request_data = {
        "name": "Sasha",
        "email": "sasha_vasyliva@mail.com",
        "address": "Moscow"
    }
    response_data = {"Template": "Email"}
    
    response = client.post("/get_form", json=request_data)
    
    assert response.status_code == 200
    assert response.json() == response_data
    print(f"status = {response.status_code}\njson={response.json()}")
    


def test_template_phone() -> None:
    "Тест проверяет шаблон Phone"
    
    request_data = {
        "name": "Mariy",
        "phone": "+7 940 520 34 21",
        "address": "Moscow"
    }
    response_data = {"Template": "Phone"}
    
    response = client.post("/get_form", json=request_data)
    
    assert response.status_code == 200
    assert response.json() == response_data
    print(f"status = {response.status_code}\njson={response.json()}")
    
    

def test_template_birthday_with_data_1() -> None:
    "Тестро проверяет шаблон Birthday с датой в формате YYYY-MM-DD"

    request_data = {
        "name": "Sergey",
        "date": "1999-10-12",
        "address": "Moscow"
    }
    response_data = {"Template": "Birthday"}
    
    response = client.post("/get_form", json=request_data)
    
    print(f"status = {response.status_code}\njson={response.json()}")
    assert response.status_code == 200
    assert response.json() == response_data


def test_template_birthday_with_data_2() -> None:
    "Тестро проверяет шаблон Birthday с датой в формате DD.MM.YYYY"
    
    request_data = {
        "name": "Sergey",
        "date": "12.10.1999",
        "address": "Moscow"
    }
    response_data = {"Template": "Birthday"}
    
    response = client.post("/get_form", json=request_data)
    
    print(f"status = {response.status_code}\njson={response.json()}")
    assert response.status_code == 200
    assert response.json() == response_data
    