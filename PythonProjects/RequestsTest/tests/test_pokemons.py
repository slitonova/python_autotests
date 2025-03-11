import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ff67c4c377e85e4eec3dcd5e9bc37e66'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '19604'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Lollipop'

