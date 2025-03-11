import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ff67c4c377e85e4eec3dcd5e9bc37e66'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

boby_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = boby_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

boby_update = {
    "pokemon_id": pokemon_id,
    "name": "Пикачу",
    "photo_id": 2
}

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = boby_update)
print(response_update.text)

boby_catch = {
    "pokemon_id": pokemon_id,
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = boby_catch)
print(response_catch.text)
