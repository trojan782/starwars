from http import client
import requests
from fastapi.testclient import TestClient, Depends
from utils.config import Settings, get_settings
from .main import app

client = TestClient(app)

def test_home():
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {
        "message": "Welcome to our starwars favorite, kindly explore all your starwars related things!",
        "link": "http://127.0.0.1:8000/docs"
    }

def test_ping(settings: Settings = Depends(get_settings)):
    res = client.get('/ping')
    assert res.status_code == 200
    result = res.json()
    ass = {
        "Staus": "Server is live!",
        "environment": settings.environment,
        "testing": settings.testing
    }
    assert result == ass

def people_test():
    url = 'https://swapi.dev/api/people'
    res = client.get('/people')
    url_request = requests.get(url)
    res_json, url_json = res.json(), url_request.json()
    assert res_json == url_json()
    assert res.status_code == 200 and url_request.status_code == 200

def test_person(id):
    res = client.get('/people/{id}')
    url = f'https://sw'